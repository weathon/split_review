---
job_id: 7ea55192-b067-4baa-8c2c-c0a468b9147c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: WhO6Km5Rku.pdf
paper: QUBITCache: Quantum-Inspired Probabilistic Attention Preservation for KV-Cache Compression
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper squarely targets efficient inference for transformer-based language models through KV-cache compression, which fits ICLR’s scope on large-scale learning systems, representation learning for language, and ML infrastructure.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, including Abstract, Introduction, Related Work, Method, Experiments, Results, and Conclusion. While there are serious issues in technical soundness, novelty positioning, and experimental validation, these are better handled in full review rather than as desk-reject criteria.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the paper text or figures of hidden prompts, reviewer-targeting instructions, or other manipulative content aimed at automated/LLM-based review systems.

# Expected Review Outcome:
## Summary
This paper proposes QubitCache, a hybrid KV-cache compression framework for autoregressive transformers that keeps a small subset of tokens in classical storage and compresses the remaining tokens by encoding aggregated attention scores into quantum-inspired amplitude states. During inference, the method reconstructs probabilistic attention weights from these states and combines them with interpolated value vectors for compressed tokens. The paper reports around $7\times$ memory reduction with relatively small performance loss across several language models and long-context benchmarks, and also presents a theoretical error bound for preserving low-rank attention structure.

## Strengths
The paper targets an important systems-and-modeling problem. KV-cache memory is a real bottleneck for long-context inference, and methods that preserve quality under aggressive compression are of broad interest to the ICLR community.

The central intuition, namely that compression should preserve relational structure and not only individual token identities, is interesting and well motivated at a high level. Even if I am not convinced the current formulation fully delivers on that promise, the framing itself is more thoughtful than yet another pure eviction heuristic.

The hybrid design is also reasonable in spirit. Keeping anchor, recent, and attention-critical tokens in classical memory while softly reconstructing the remainder is a plausible compromise between fully discrete eviction and blunt quantization. In particular, the component ablation in **Table 4** suggests that the choice of which tokens remain explicit matters a great deal. The drop from 0.491 to 0.391 when removing critical tokens is a useful signal that the token partitioning is not arbitrary, and the comparison against “Random + Quantum” supports the claim that attention-guided retention is better than random retention.

The experimental section does include a reasonably broad set of models and tasks. **Table 1** covers five models and multiple task types, and the pattern is fairly consistent: QubitCache usually outperforms the token-eviction baselines under the stated compression regime. On long-range reasoning tasks such as HotpotQA and TriviaQA, the method often narrows much of the gap to Full KV relative to ScissorHand, H2O, and StreamingLLM. That pattern is aligned with the paper’s stated hypothesis that relational information matters more on tasks with delayed dependencies.

Some figures help convey the intended mechanism. **Figure 1** gives a quick overview of the hybrid pipeline, and it is one of the clearer parts of the paper: the distinction between preserved tokens and probabilistically reconstructed non-critical tokens is visually understandable. **Figure 3a** also communicates the intended qubit-count trade-off reasonably well, namely that performance improves with representational capacity but with diminishing returns.

## Weaknesses
I have substantial concerns about the technical formulation, the claimed compression mechanism, and the experimental evidence. In its current form, the paper reads more like a provocative concept paper than a solidly established ICLR contribution.

1. **The core “logarithmic compression” claim is not scientifically supported in the way the paper presents it.**  
   The paper repeatedly argues that amplitude encoding stores $N$ token-related values in only $O(\log N)$ qubits, for example around **Eq. (1)**, **Eq. (5)**, and **Table 3**. But in the actual implementation, the method is a **classical simulation** of quantum states on GPU, explicitly acknowledged in Section 3.2.2 and Appendix A.1.1. In that setting, representing the statevector for a 9-qubit system already requires storing all $2^9 = 512$ amplitudes, so the operational memory is not logarithmic in any practical classical sense. More importantly, even on hypothetical quantum hardware, the paper counts only the qubit register while ignoring the cost of state preparation, measurement, repeated estimation, and storage/access to the amplitude parameters themselves. This matters because the paper’s headline comparison in **Table 3** directly attributes the $7.0\times$ compression to a complexity term $O(L \times H \times 0.15S \times D + \log N)$, which is not a fair end-to-end memory accounting for the actual implementation described.

2. **The method does not actually preserve attention relations in the strong sense claimed; it mostly preserves a 1D importance distribution.**  
   The introduction and abstract make very strong claims about preserving “attention patterns between tokens” and “relational structure.” However, the encoding in **Eq. (3)-(5)** collapses the attention matrix into scalar aggregated scores $a_i^{(l,h)} = \sum_j A_{j,i}^{(l,h)}$, then averages them over layers and heads. This discards almost all pairwise structure. Two very different attention graphs can induce the same column-sum statistics. So the object encoded in the quantum state is not an attention topology or relational graph, but a normalized per-token importance profile. That is a much weaker object. This is not a semantic quibble, because the paper’s novelty claim hinges on preserving relations rather than tokens. As written, the formulation does not match the rhetoric.

3. **Several mathematical definitions are underspecified or inconsistent, especially in the actual inference rule.**  
   The most serious issues are in **Eq. (2)**, **Eq. (6)**, and **Eq. (7)**:
   - In **Eq. (2)** and **Eq. (7)**, the attention output is written as a convex combination of preserved-token values and reconstructed-token values, but the coefficients $\alpha_i$ for preserved tokens are never clearly defined in the same way as the compressed-token probabilities $p_j(\psi)$. Are these the original query-dependent attention weights for the current generation step, historical aggregate scores, or something else?
   - The attention formula no longer appears query-dependent in the usual transformer sense. Standard attention depends on the current query $Q_t$ through $\mathrm{softmax}(Q_tK^\top/\sqrt{d})V$. Here, beyond carrying the symbol $Q_t$ in the left-hand side, the right-hand side in **Eq. (7)** depends only on precomputed $\alpha_i$, segment states, and interpolated values. If that is intentional, then the method is replacing query-conditioned attention with a static mixture, which is a much stronger approximation than the paper acknowledges.
   - The expression for $p_j(|\psi\rangle)$ in **Eq. (7)**, written as $|(j\mod n_s|\psi_{S_{j/n_s}}})|^2$, is malformed and difficult to parse. I assume the intended expression is something like $|\langle j \bmod n_s \mid \psi_{S_{\lfloor j/n_s\rfloor}}\rangle|^2$, but the paper should state it correctly.
   - The notation also alternates between $\hat V_j$ and $\tilde V_j$ across **Eq. (2)** and **Eq. (7)** without explanation.

   These are not cosmetic issues. They make it hard to determine what is actually computed at inference time.

4. **The interpolation rule in Eq. (6) is questionable and internally inconsistent with the stated weighting.**  
   The paper defines $d_{j,k} = |j-k|^{-1}$ and then uses
   $$
   \hat V_j = \frac{d_{j,\text{left}}}{d_{j,\text{left}} + d_{j,\text{right}}}V_{\text{left}(j)} + \frac{d_{j,\text{right}}}{d_{j,\text{left}} + d_{j,\text{right}}}V_{\text{right}(j)}.
   $$
   If $d_{j,k}$ is inverse distance, then this formula does give larger weight to nearer tokens, which is fine mathematically, but the exposition is sloppy because the text around **Page 5-6** discusses left/right “distance weighting” without clarifying boundary cases. What happens if $\text{left}(j)$ or $\text{right}(j)$ does not exist, for example near segment boundaries or at the extreme ends of the compressed region? This is especially relevant because preserved tokens include a small set of anchors and recents, not a dense lattice. The paper also never justifies why linear interpolation between the two nearest preserved values should approximate a token’s value vector well across diverse tasks or layers. This is a strong modeling assumption hidden inside a simple formula.

5. **The theoretical claim is overstated relative to what is actually shown in the main paper.**  
   The abstract and introduction claim a proof that QubitCache preserves rank-$r$ attention structure with bounded reconstruction error. But in the main paper, I do not see a theorem statement, assumptions, proof sketch, or even a precise error bound. The paper invokes this guarantee repeatedly as a selling point, yet the mathematical support is absent from the core submission. Given how central this claim is, it should not be asserted at this level of confidence without a self-contained statement in the main paper. Right now the reader is asked to trust a theorem that is effectively invisible.

6. **The experimental comparison is not sufficiently fair because baselines are not matched by compression budget.**  
   The paper repeatedly emphasizes that QubitCache retains only 15% of tokens while some baselines retain around 50%, and then frames this as evidence of stronger compression quality. But the baselines in **Table 1** and the configurations in Appendix A.1.9 are not normalized to equal memory or equal latency budgets. This is a problem because some methods, especially quantization-based ones such as GEAR, compress in a different space than eviction methods. If you want to claim superiority under aggressive compression, the key comparison should be iso-memory or iso-latency curves, not one operating point per method with different design assumptions. As a concrete example, **Table 3** reports GEAR at 6.7$\times$ and QubitCache at 7.0$\times$, which is much closer than the narrative suggests, yet **Table 1** does not clearly establish whether those results are at truly comparable budgets across all models/tasks.

7. **The results tables are weaker than the narrative claims, and some textual interpretations are overstated.**  
   **Table 1** does show QubitCache usually beating ScissorHand, H2O, and StreamingLLM, but the gains over GEAR are often modest, and on some tasks the method remains noticeably below Full KV. For example, on Mistral-7B HotpotQA, QubitCache is 0.459 versus 0.566 for Full KV, which is not “near-lossless.” On Phi-4-mini PIQA, QubitCache is 0.781 versus 0.859, a meaningful drop. The paper’s blanket statement of retaining “92-97% of baseline performance across all tasks” smooths over task-specific degradations that are not small. Also, **Table 2** on larger models only includes NarrativeQA and does not demonstrate broad scalability in the way the section title “Scaling to Larger Models” implies.

8. **The ablation evidence for the quantum part is not convincing enough.**  
   In **Table 4**, the “No Quantum” variant drops from 0.491 to 0.472, which is a small absolute gain relative to the grand claims about quantum-inspired relational preservation. In Appendix **Table 5**, removing entanglement or noise dropout produces essentially no difference, which undercuts the emphasis placed on the circuit design and NISQ feasibility in **Figure 2** and **Figure 3b**. If the quantum-specific components barely matter, then the paper needs to explain much more carefully what exactly the “quantum-inspired” machinery contributes beyond a classical probabilistic encoding of normalized importance scores.

9. **The hardware and practicality claims are not well aligned with the presented implementation.**  
   Section 3.2.2 and **Figure 2** devote significant space to quantum circuits, controlled rotations, entanglement, and measurement, while the actual implementation uses Qiskit simulation on GPUs. The discussion around coherence times and gate durations in **Figure 3b** feels speculative because the paper does not present experiments on real quantum hardware, nor does it quantify the wall-clock cost of simulation versus straightforward classical alternatives. The phrase “practically implementable solution” is too strong given the evidence provided.

10. **Presentation quality is below what is needed for a method paper making aggressive claims.**  
   There are many signs of hurried writing: duplicated text in Section 4.3 on **Pages 7-8**, typos such as “binary dcisions” in the abstract, malformed math in **Eq. (7)**, inconsistent notation, and some claims that are more rhetorical than measured. The figures also do not rescue the lack of precision. **Figure 2** looks sophisticated, but because the corresponding equations never precisely define how the measured probabilities are integrated into query-conditioned attention, the diagram risks conveying more completeness than the method section actually provides.

11. **Related-work positioning is incomplete for a fast-moving area.**  
   The paper compares against several established methods, but the positioning remains too narrow for strong claims about opening a “new frontier.” Recent dynamic eviction and high-compression KV methods are not discussed in a way that convinces me the paper has been benchmarked against the best contemporary alternatives. This matters because the contribution is not just a neat idea, it is an empirical systems claim competing in a crowded design space.

12. **Some dataset/task choices are not fully coherent with the stated long-context focus.**  
   The paper says it evaluates on “five benchmark datasets” in Section 4.1.2 but **Table 1** includes seven metrics/tasks, and PIQA in particular is an odd fit for a paper whose core motivation is long-context KV-cache compression. This does not invalidate the results, but it contributes to the impression that the benchmark suite is assembled more for breadth than for stress-testing the claimed mechanism.

To be clear, there is an interesting seed here. But the paper currently over-claims what the encoding preserves, overstates the theoretical support, and does not yet provide the kind of rigorous, apples-to-apples evidence needed for ICLR acceptance.

## Questions
1. Please give a precise, query-dependent derivation of the inference rule in **Eq. (2)** and **Eq. (7)**. In particular, what exactly are the $\alpha_i$ for preserved tokens at generation step $t$? Are they recomputed from $Q_t$, or are they static historical statistics? A clear formula here would substantially increase my confidence.

2. Can the authors state the theoretical guarantee explicitly in the main paper, including assumptions, theorem statement, and the exact reconstruction error bound? Right now the paper repeatedly advertises a bounded-error theorem without presenting it in the core text.

3. What is the true end-to-end memory and latency cost of the actual implementation, including state preparation / simulation overhead? I would like to see an apples-to-apples comparison against a classical baseline that stores the same per-segment importance distribution directly, without quantum notation.

4. Please add matched-budget evaluations. For example, compare QubitCache, GEAR, H2O, and other baselines at the same memory footprint and, separately, at the same latency budget. This is important because the current comparisons mix token retention, quantization, and simulation overhead in a way that is difficult to interpret.

5. Can the authors clarify what relational information is preserved beyond aggregated token importance? Since **Eq. (3)-(5)** compress attention to per-token aggregated scores, I do not see how pairwise token-token relations survive except in a highly reduced sense.

6. What happens in **Eq. (6)** when one of the neighboring preserved tokens does not exist, and how sensitive are results to the interpolation scheme? A stronger ablation would compare IDW interpolation to alternatives such as nearest-neighbor, learned interpolation, local low-rank reconstruction, or direct value quantization.

7. The quantum ablations suggest limited effect from entanglement and some other quantum-specific ingredients. Can the authors isolate the minimal classical analogue of QubitCache and show whether the same gains persist? This would help determine whether the contribution is genuinely tied to the quantum-inspired formulation or mostly to the hybrid token selection plus soft reconstruction design.

8. Please clarify the benchmark accounting. The text mentions five datasets, six benchmarks, and **Table 1** reports seven task metrics. A more systematic benchmark description would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission. The paper studies inference-time compression for language models and does not introduce a new dataset involving human subjects or clearly identifiable privacy-sensitive data in the main paper.

## Soundness Rating
2: fair. The paper has a plausible high-level idea and some empirical support, but the core mathematical formulation is underspecified, the theoretical guarantee is not properly presented in the main paper, and several central claims exceed what the experiments and equations clearly justify.

## Presentation Rating
2: fair. The overall story is understandable, and some figures/tables are helpful, but the writing contains inconsistencies, duplicated text, malformed notation, and several places where rhetoric outruns precision.

## Contribution Rating
2: fair. The problem is important and the hybrid “preserve some tokens, softly reconstruct the rest” idea has some interest, but the current paper does not convincingly establish that the quantum-inspired component yields a sufficiently clear, rigorous, or practically necessary advance over stronger classical formulations.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting intuition and some promising empirical signals, especially on reasoning-heavy tasks, but there are too many unresolved issues in the formulation, theoretical support, fairness of comparisons, and practical interpretation of the claimed compression mechanism for me to recommend acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. The main concerns are based on the paper’s own equations, claims, and tables rather than on obscure implementation details.