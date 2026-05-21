---
job_id: c198d383-61b1-4aad-9e11-f8c323fba7b0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: rajioNWfRs.pdf
paper: TNT: Improving Chunkwise Training for Test-Time Memorization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on large-scale sequence modeling, efficient training of recurrent/deep memory architectures, and representation learning for language.

## Minimum Quality
Pass ✅. The submission contains the essential components of a research paper, including abstract, introduction, related-work discussion, methodology, experiments, quantitative results, and conclusion; while there are important weaknesses in novelty positioning and methodological clarity, the work is complete enough for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious formatting, or text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes TNT, a two-stage training framework for deep memory modules such as Titans and TTT. The main idea is to use an efficiency-oriented pretraining stage with a hierarchical memory design, consisting of one global memory operating on large chunks and several local memories that are periodically reset to enable context parallelism, followed by a short fine-tuning stage that adapts the local memories to smaller chunk sizes for higher-quality inference. Empirically, the paper reports substantial reductions in training time-to-target-loss and improvements in perplexity and downstream reasoning accuracy over Titans baselines.

## Strengths
The paper addresses a real bottleneck in deep test-time memorization models, namely the very poor hardware utilization induced by small chunk sizes. This is a practical and relevant problem, and the paper stays focused on it throughout.

The proposed two-stage framing is intuitive and easy to follow. Separating an efficiency-focused stage from a performance-focused stage is a sensible way to tackle the speed versus chunk-resolution tension that is nicely illustrated in **Figure 2**. That figure is one of the clearest parts of the paper: it directly shows that inference performance is not monotonically improved by using smaller chunks at test time, and instead peaks near the training chunk size, which motivates the need for the adaptation stage in Section 4.2.

The hierarchical design itself is reasonably compelling. **Figure 1** gives a useful conceptual picture of how global and local memories run at different resolutions, and **Figure 3** helps explain how the architecture combines the global memory path with multiple local memories. Even though the architectural drawing in Figure 3 is somewhat high level, it does communicate the central intuition that TNT mixes coarse global context with fine local memories rather than simply enlarging chunk size everywhere.

The empirical efficiency gains are meaningful. In **Table 1**, the time-to-target-loss comparison is strong and practically relevant: TNT with local chunks \(\{64\}\) reaches the target loss in 1.12 hours versus 19.48 hours for Titans with chunk size 8, which is indeed a large reduction in wall-clock training cost. Importantly, the table is not just reporting faster per-step runtime, but time to a matched loss target, which is the right direction for a practical systems-oriented claim.

The performance results in **Table 2** are also better than I expected given the speed focus. TNT Stage 1 with \(C_L=[4,8,16,32]\) improves average perplexity from 25.07 for the best small-chunk Titans baseline to 23.13, and Stage 2 further improves to 23.09. This means the method is not merely a throughput trick that sacrifices quality.

The ablations in **Table 3** are directionally useful. In particular, the degradation from removing the global memory and from removing Q-K projection supports the claim that the gains are not solely from adding more parameters or doing a different chunk schedule. The paper also does a good job linking those ablations back to the three challenges presented in Section 3.

Overall, I found the paper strongest as a practically useful training recipe for deep memory models. It does not close the gap to highly optimized attention models, but it clearly improves the feasibility of training this class of models.

## Weaknesses
1. **The mathematical formulation of the local update is underspecified and partly inconsistent, which matters because the claimed training parallelism hinges on these details.**  
   The core training rule in **Equation (6)** is difficult to interpret precisely. The “otherwise” branch is written as
   \[
   W_t \leftarrow W_{t-1} - \sum_{\tau=\xi(t,C_L)}^{t}\eta_\tau \nabla_W \mathcal{L}\big(f(W_{\xi(t,C_L)},k_\tau),v_\tau\big),
   \]
   which mixes a recurrence from \(W_{t-1}\) with a chunkwise gradient sum evaluated at \(W_{\xi(t,C_L)}\). This is not the same pattern as **Equation (3)**, where \(W_t\) is directly defined from the chunk-start state. If the intended update is a chunkwise approximation, then using \(W_{t-1}\) in Eq. (6) is odd, because \(W_{t-1}\) already contains prior chunkwise accumulated terms; if the intended update is a recursive within-shard rule, then the formula is not an actual parallel chunkwise expression. This is not a cosmetic issue. The claimed ability to “break sequential dependencies” and obtain “true context parallelism” depends on the exact state evolution. The paper should cleanly define whether the local state within a shard is
   \[
   W_t = W_{\xi(t,C_L)} - \sum_{\tau=\xi(t,C_L)}^{t}\cdots
   \]
   or whether it is recursively updated from \(W_{t-1}\), because those are materially different algorithms.

2. **The Q-K projection formulation is not mathematically well justified as stated, and the paper overstates what it achieves.**  
   In **Equation (7)**, the local retrieval uses
   \[
   \sum_{\tau=\xi(t,C_L)}^{t}\frac{k_\tau k_\tau^\top}{\|k_\tau\|^2}q_t.
   \]
   The text says this projects \(q_t\) onto “the subspace spanned by previously observed keys.” But the operator
   \[
   \sum_{\tau} \frac{k_\tau k_\tau^\top}{\|k_\tau\|^2}
   \]
   is generally **not** the orthogonal projector onto \(\mathrm{span}\{k_\tau\}\) unless the normalized keys are orthonormal. In the general case, the orthogonal projector would involve the Gram matrix inverse, e.g.
   \[
   P = K(K^\top K)^{-1}K^\top
   \]
   when \(K\) stacks the keys. So the current mechanism is better described as an unnormalized accumulation of rank-1 directional filters, not a true projection. That matters because the central motivation in Section 4.1.2 is to resolve a domain mismatch by “projecting onto the key subspace.” As written, the method may help empirically, but the mathematical story is looser than the paper suggests.

3. **The paper does not sufficiently disentangle whether gains come from the hierarchical/reset design, from increased effective model capacity, or from multi-resolution ensembling of local memories.**  
   This is especially important for the strongest quality numbers in **Table 2**. TNT with \(C_L=[4,8,16,32]\) uses four local memories plus one global memory, whereas the Titans baseline uses a single memory pathway. So there are at least three changes at once: hierarchy, reset-induced parallelism, and more memory modules operating at multiple resolutions. **Table 3** partially probes this, but the ablation is still too coarse. For example, there is no parameter-matched baseline that adds comparable extra memory capacity without periodic resets, and no ablation isolating “multiple local modules at heterogeneous chunk sizes” versus “one stronger local module with similar parameter budget.” Without this, the claim that the main gain comes from decoupling training efficiency from inference resolution is weaker than it could be.

4. **The efficiency evaluation is favorable to TNT, but it is not yet broad enough to support some of the stronger comparative language in the paper.**  
   **Figure 4** shows the expected scaling advantage, and the crossover behavior at long sequences is interesting. However, the experiments are run in one hardware/software setup, and the paper itself admits that TNT does not beat the most optimized gated Transformer with FlashAttention in time-to-quality. In **Table 1**, the best TNT configuration is still slower than both FlashAttention Transformer rows for reaching the same target loss. So statements in the abstract and conclusion can read slightly stronger than the evidence really supports. The paper convincingly shows TNT is much faster than baseline Titans implementations; it is less convincing if interpreted as establishing a broadly competitive alternative to modern optimized attention stacks.

5. **The empirical scope is narrow for a paper claiming a general training paradigm.**  
   The introduction and conclusion repeatedly describe TNT as general for “deep memory modules,” yet the substantive evaluation is centered on a 150M Titans-style setup, with TTT mentioned as a baseline but not actually developed in depth in the main results tables. A general training recipe should ideally show either: (i) at least two materially different deep-memory instantiations in the main paper, or (ii) stronger evidence that the mechanism is architecture-agnostic rather than tailored to the particular Titans design choices. As it stands, the work reads more like “TNT for Titans-style models” than “TNT for deep memory modules” broadly.

6. **The novelty is somewhat incremental at the level of ideas, even if the package is useful.**  
   The building blocks are not individually surprising: hierarchical memory, chunkwise training, query/key alignment heuristics, and short adaptation stages are all fairly natural moves in this area. What the paper contributes is a coherent and effective combination of these ingredients for a difficult training regime. That is still valuable, but the presentation sometimes leans toward framing this as a more fundamental architectural advance than the evidence supports. I think the contribution is better described as a strong training recipe and systems-aware redesign for Titans-like deep memory models.

7. **Some claims around “massive context parallelization” and resolving a “long-standing challenge” are too strong relative to the level of evidence and analysis provided.**  
   The periodic reset definitely reduces long-range dependence for local memories, but it does so by truncating state propagation and then compensating using a separate global memory. That is a reasonable engineering tradeoff, not a clean resolution of nonlinear recurrence parallelization in the broader sense. The paper would be stronger if it stated this more carefully, namely that TNT achieves practical parallelization by restructuring the model and accepting a hierarchical approximation, rather than by directly parallelizing the original nonlinear recurrent computation.

8. **Presentation clarity is decent overall, but several technical choices that affect reproducibility are missing or buried.**  
   Examples include the exact initialization and parameterization of \(W_{\text{init}}\), whether local memories share parameters or are independent across resolutions, whether adding multiple local memories changes total parameter count relative to baselines, and how the fine-tuning budget in Stage 2 is chosen. These omissions are important because the gains in **Table 2** and **Table 3** could depend materially on these implementation choices.

9. **The paper would benefit from more careful interpretation of the ablations.**  
   For instance, in **Table 3**, “w Stage 2” is shown only for the 1-local-memory setup, while the best main result in **Table 2** uses four local memories in Stage 2. That makes it harder to understand whether Stage 2 consistently helps across all hierarchy depths, or whether the effect depends on the particular Stage 1 configuration. Similarly, the common-sense reasoning accuracy numbers fluctuate enough that stronger conclusions about downstream gains should be made cautiously.

## Questions
1. **Please clarify the exact intended state update in Equation (6).**  
   Is the local-memory rule supposed to be a recursive update from \(W_{t-1}\), or a direct chunkwise construction from \(W_{\xi(t,C_L)}\) analogous to Eq. (3)? A precise corrected equation would significantly increase my confidence in the method description.

2. **How does the parameter count compare between Titans and the multi-local TNT variants in Table 2?**  
   If the best TNT model has materially more fast-weight parameters or more retrieval pathways than the Titans baseline, please quantify that clearly. A parameter-matched comparison would help isolate whether the gains are architectural/training gains or simply capacity gains.

3. **Can the authors provide a stronger justification for the Q-K “projection” language?**  
   As written, Eq. (7) is not the orthogonal projector onto the span of keys in the general case. If the method is instead a heuristic approximation, please say so explicitly and discuss why this particular form is preferable to alternatives such as learned query-to-key alignment or a proper low-rank projector approximation.

4. **How robust are the speedups across hardware/software stacks?**  
   The current results are on TPUv4 with JAX. Since the work is motivated as a practical training framework, it would be helpful to know whether the qualitative ranking in Figure 4 and Table 1 remains similar on other accelerators or under stronger kernel engineering.

5. **How general is TNT beyond Titans-style models in practice?**  
   Since the paper claims applicability to any deep memory module, I would like either a concrete additional experiment or a more carefully bounded claim. Even a small-scale validation on a second architecture in the main paper would help.

6. **What exactly is updated in Stage 2, and what is frozen?**  
   Section 4.2 says “only the local memory modules are adjusted,” but it would help to know whether this means only local fast-weight module parameters, only local slow weights, or both local memory pathways while freezing the global path and surrounding backbone.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns requiring escalation are apparent from the paper. The work is a methodological study on sequence-model training efficiency and does not present a new dataset, human-subject experiment, or directly harmful deployment setting.

## Soundness Rating
3: good. The core empirical claims, especially the speedup over baseline Titans configurations and the quality improvements in Tables 1 to 3, are reasonably supported, but there are notable issues in the mathematical precision of the update rules and in the causal attribution of why the method works.

## Presentation Rating
2: fair. The paper is readable and the high-level motivation is clear, with helpful figures such as Figures 1 to 4, but several key equations and implementation details are underspecified or imprecisely described, which weakens clarity for a technical ICLR audience.

## Contribution Rating
3: good. I see this as a useful and relevant contribution for training deep memory models, especially as a practical recipe that improves both throughput and quality, although the conceptual novelty is moderate and the generality claims are somewhat broader than what is empirically demonstrated.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important practical bottleneck, shows convincing gains over Titans baselines, and presents a training recipe that the community working on deep memory models may find useful. My hesitation comes from the imprecise mathematical exposition, incomplete disentangling of capacity versus architecture effects, and somewhat overstated generality/positioning. So I end up slightly positive, but not enthusiastically so.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the sequence-modeling setting, though some implementation-level details are not fully recoverable from the main paper due to underspecification in the equations and setup.