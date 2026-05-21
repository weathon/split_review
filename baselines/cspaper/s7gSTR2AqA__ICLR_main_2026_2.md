---
job_id: 48a4667d-96a0-44ec-bb62-acfeda6c6b45
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: s7gSTR2AqA.pdf
paper: Evolution and Compression in LLMs: On the Emergence of Human-Aligned Categorization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, at the intersection of representation learning for language/multimodal models, cognitive-science-inspired evaluation of learned semantic representations, and analysis of emergent structure in LLMs.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including abstract, introduction, background/related work, experimental setup, results, and discussion, and it presents a nontrivial empirical study rather than a trivial repackaging. While I have substantive concerns about methodology and claim strength, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the provided paper content of hidden prompts, concealed reviewer-targeting instructions, or other manipulative content aimed at automated review systems.

# Expected Review Outcome:
## Summary
This paper studies whether LLMs develop human-aligned semantic category systems through the same Information Bottleneck (IB) efficiency principle that has been used to explain human categorization, focusing primarily on color naming. The authors run two main experiments: an English color-naming benchmark across 39 LLMs, and an iterated in-context language learning (IICLL) setup intended to emulate cultural transmission of category systems and reveal inductive biases beyond direct imitation of training data. They report that larger instruction-tuned models are more aligned with English and more IB-efficient, and that in IICLL several LLMs move toward more efficient systems, with Gemini 2.0 covering a broader range of near-optimal tradeoffs similar to human data.

## Strengths
1. The paper asks an interesting and well-motivated question: not just whether LLMs can match human labels on a benchmark, but whether they exhibit a pressure toward efficient semantic compression analogous to humans. That is a stronger and more scientifically meaningful framing than simple accuracy evaluation.

2. The connection between cognitive science and LLM analysis is thoughtful. The paper leverages established human datasets and theories rather than inventing an ad hoc benchmark, which gives the empirical study more interpretability than many “LLMs do X” papers.

3. The empirical scope of the English color naming experiment is substantial. Testing 39 models across multiple families, model sizes, and training stages is useful, and the broad coverage shown in **Figure 2(c)** supports one of the clearest findings in the paper, namely that scale and instruction tuning are associated with increased complexity and better English alignment, but with substantial heterogeneity across families. This figure is especially helpful because it disentangles family-level trends better than the information-plane plot alone.

4. **Figure 2(a)** is an effective summary visualization. Plotting models directly on the IB complexity-accuracy plane against the human English point and the theoretical IB bound gives a compact and interpretable view of the main claim. The visual message is clear: some models are close to the English point, many are not, and proximity to the bound varies significantly. This is one of the stronger parts of the presentation.

5. The qualitative mode maps in **Figure 2(b)** are genuinely informative, not decorative. They help verify that the high-level information-theoretic metrics correspond to meaningful category structure on the WCS grid. In particular, the contrast between English and the better-performing LLMs gives a concrete sense of which boundaries are captured and which are blurred.

6. The IICLL setup is creative. Extending iterated in-context learning into a language-learning setting that mirrors human iterated learning experiments is a clever way to probe inductive biases in a behavioral style that is different from standard prompting evaluations.

7. **Figure 3** is a strong figure. The chain trajectories from random initializations toward regions near the IB curve are central to the paper’s argument, and the side-by-side comparison across Gemini, Gemma, Llama, and Qwen usefully shows that “movement toward efficiency” and “covering the human complexity range” are distinct phenomena. The figure supports a nuanced claim better than a single aggregate score would.

8. The paper does a good job of separating two claims that are often conflated: matching English categories versus exhibiting a broader tendency toward human-like efficient categorization. That conceptual distinction improves the framing of the contribution.

9. The appendix appears fairly comprehensive. Although my evaluation is based on the main paper, it is helpful that procedural details, prompts, and model lists are provided. In particular, **Table 1** in Appendix D is useful for understanding the breadth of the model sweep and the tuning/multimodality axes being compared.

## Weaknesses
1. The central causal claim, that IICLL reveals an intrinsic LLM inductive bias rather than reuse of training-set regularities, is overstated relative to the evidence presented. The paper argues in **Section 4.2** and the **Discussion** that LLMs are “not merely mimicking patterns in their training data,” but the experiments do not really isolate that conclusion. The IICLL prompts still use color features drawn from a highly familiar domain, and for the main color experiments the textual inputs are sRGB triples, which themselves may be highly represented online. Even the authors note on **Page 9** that numeric representations matter a lot, since Gemini struggled on Shepard circles presented as numbers but improved with images. That is a sign that the observed behavior may depend heavily on prior exposure to input formats and domain-specific regularities, not just a domain-general categorization bias. This matters because the paper’s strongest claims go beyond “the models can produce efficient color systems” to “they exhibit the same fundamental principle that underlies human semantic efficiency,” which is a much stronger statement.

2. There is a selection effect in the IICLL experiments that weakens the generality of the conclusions. In **Section 4.2**, the authors restrict the main IICLL analysis to four large instruction-tuned models that already did well on English naming. That is understandable pragmatically, but it also means the paper’s headline message about cultural evolution in LLMs is based on a filtered subset chosen after observing performance on a related task. Appendix L shows that smaller models mostly collapse to degenerate systems. The resulting picture is less “LLMs have this bias” and more “some frontier instruction-tuned LLMs under favorable conditions can sustain this behavior.” That distinction should be stated more carefully, especially in the abstract and conclusion.

3. The experimental protocol introduces confounds that make the comparison to human iterated learning less clean than the paper suggests. In **Appendix G** and **Appendix K**, the authors include a sliding window of the previous 10 interactions during the production phase to “promote coherence” and mimic short-term memory. But this changes the effective learning dynamics in a major way. The label assigned to an item can now depend not only on the training set \(d_{t-1}\), but also on the order of previously queried test items and the model’s own recent outputs. This turns each generation into a path-dependent sequential process rather than a pure generalization from a fixed training sample. Since the human comparison is used to support claims about inductive bias, this matters a lot. A process with autoregressive self-conditioning is not obviously comparable to the classical iterated learning setup described in **Section 2.3**.

4. The mathematical definitions are not fully aligned with the actual LLM evaluation protocol. In **Section 2.2**, the semantic system is modeled as a stochastic encoder \(q(w \mid m)\), and the IB objective in **Equation (1)** depends on mutual-information quantities \(I_q(M;W)\) and \(I_q(W;U)\). But the LLM experiments appear to produce a single label per stimulus via constrained generation or log-probability scoring, effectively yielding deterministic mappings on the 330 WCS chips. The paper does not clearly explain how \(q(w \mid m)\) is estimated from those outputs. Is it a delta distribution on each chip, a model probability over labels extracted from continuation scores, or something else? This is not a cosmetic detail. The values of complexity, accuracy, and \(\varepsilon = \min_\beta \frac{1}{\beta}(\mathcal F_\beta[q]-\mathcal F_\beta^\*)\) on **Page 5** depend directly on that choice. Without a precise mapping from prompted LLM outputs to the encoder \(q\), it is difficult to fully assess the soundness of the information-theoretic evaluation.

5. There is a small but important mathematical inconsistency around the tradeoff parameter \(\beta\). In the main text, **Equation (1)** states \(\beta \ge 0\), whereas in Appendix A, **Equation (4)** writes the same objective with the constraint \(\beta \ge 1\). If this is merely conventional reparameterization, it should be explained; if not, the optimization domain for the IB curve and for \(\varepsilon\)-fitting is inconsistent across sections. Because the paper’s core evidence relies on distance to the IB bound, this should be made precise rather than left ambiguous.

6. The paper does not give enough detail about statistical reliability in the main text. **Figure 4** shows means with 95% confidence intervals, but the number of chains per condition, how the intervals were computed, and whether the variation is across random seeds, across vocabulary-size conditions, or both, are not clearly summarized in the main paper. The same issue affects **Figure 3**, where the density of trajectories suggests many runs, but the exact counts and aggregation are hard to reconstruct from the main text alone. For a paper making comparative claims between models and humans, the reader should not need to infer experimental sample sizes from scattered details.

7. The use of different decoding mechanisms across models is a nontrivial comparability issue that is under-discussed. On **Page 5** and in **Appendix J**, Gemini uses API-level controlled generation while open-weight models are evaluated via log-probability scoring over allowed continuations, with default generation parameters including temperature and top-\(p\). These are not equivalent interfaces to the model. They can induce different effective decision rules and calibration behaviors, especially in a constrained classification setting. Since Gemini is also the model with the strongest IICLL results, the paper should do more to rule out interface effects as a partial explanation, or at least discuss this limitation more explicitly.

8. The evidence for “wide range of near-optimal IB-tradeoffs observed in humans” being recapitulated by Gemini is visually suggestive, but the paper lacks a stronger quantitative test of distributional similarity. **Figure 3** makes the case qualitatively, but a central conclusion hinges on Gemini covering the human complexity range while others collapse to low-complexity solutions. Some explicit measure comparing the distribution of final chain tradeoffs between human IL and each model would have made this much more convincing than visual inspection.

9. The Shepard circles section is too preliminary to support the broader generalization claim made around it. In **Section 4.3**, the authors explicitly limit to a single model, one vocabulary size \(k=4\), and present only qualitative chains in **Figure 5(b)**. They also state that they did not test IB-efficiency there. As written, this section is better read as an anecdotal extension than as evidence for domain generality. The paper is a bit too eager in using it to suggest that the results may apply “also in other domains.”

10. The paper’s strongest claims sometimes exceed what the evidence in the figures supports. For example, the concluding sentence on **Page 10** says that LLMs are capable of evolving perceptually grounded, human-like semantic systems guided by the same IB-efficiency principle that underlies human languages. That is too sweeping given the actual empirical pattern in **Figure 3** and **Figure 4**. A more accurate summary would be that some frontier models, under a particular prompting and evaluation protocol in color naming, exhibit trajectories consistent with increased IB-efficiency and partial human alignment. The current wording overreaches.

11. The absence of a main-paper quantitative table is a presentation weakness. The core results are mostly visualized in figures, which is fine, but there is no concise table in the main paper summarizing model-level English alignment, complexity, efficiency loss, and perhaps IICLL outcomes. **Table 1** in Appendix D is only a model inventory, not a results table. This matters because some claims, especially cross-model comparisons in **Section 4.1**, would be easier to verify and less dependent on reading off plots if a compact numerical table were included.

12. The paper does not sufficiently discuss whether the nearest-neighbor baseline in Appendix M is an adequate comparator for the central “not trivial clustering” claim. A stronger baseline family would include simple partitioning or prototype-based learners that have access to the same in-context examples and sequential constraints. Since the paper leans on “Gemini beats NN” to argue that the bias is nontrivial, the strength of that argument depends heavily on the baseline choice.

## Questions
1. Please clarify exactly how the encoder \(q(w \mid m)\) is derived from the prompted LLM outputs. Is each color chip assigned a deterministic label and then treated as a point-mass encoder, or are model probabilities over allowed labels used directly? This is central to interpreting **Equation (1)** and the reported complexity/accuracy values.

2. Relatedly, can the authors explain the discrepancy between \(\beta \ge 0\) in **Equation (1)** and \(\beta \ge 1\) in Appendix A, **Equation (4)**? If this is just a convention inherited from prior IB work, please state it explicitly and clarify which domain was used when computing \(\varepsilon\).

3. How much of the IICLL behavior survives if the sliding-window history is removed or replaced by a fixed ordering-independent mechanism? The current protocol seems to mix inductive generalization with sequential self-conditioning. A more explicit ablation in the main paper would increase my confidence that the reported trajectories are not an artifact of conversation-history dynamics.

4. Can the authors provide a more direct quantitative comparison between final human IL distributions and final model distributions on the information plane, beyond the visual comparison in **Figure 3**? Even a simple summary statistic over chain endpoints would help substantiate the claim that Gemini recapitulates the human range.

5. Since Gemini uses controlled generation while the open models use log-probability scoring, did the authors test whether interface differences materially affect results on models where both styles are possible? This is especially relevant because Gemini is also the strongest model in IICLL.

6. The paper argues that the observed effect is not just training-data imitation. What additional evidence can the authors provide to separate “inductive bias” from “learned familiarity with color-encoding conventions and human color naming regularities”? For example, do the authors have results for held-out synthetic feature spaces where human-like structure is available but internet exposure is unlikely?

7. For **Figure 4**, please state clearly in the main paper how many chains are included per model, what sources of variation the confidence intervals reflect, and whether the averaging mixes conditions with different \(k\). This is important for interpreting the apparent convergence speed and inter-model differences.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work studies model behavior on color categorization using existing datasets and prompting protocols, and I did not identify privacy, safety, or human-subject concerns requiring specialized ethics review from the information provided.

## Soundness Rating
2: fair. The paper is empirically substantial and the main trends are plausible, but several central claims are stronger than the evidence, and key methodological details around the mapping to the IB formalism and the IICLL protocol need sharper justification.

## Presentation Rating
3: good. The paper is generally well written, the figures are informative, and the overall narrative is easy to follow, but some important definitions and experimental details are missing from the main text, and a compact quantitative results table would help considerably.

## Contribution Rating
3: good. The paper tackles an interesting question with a creative experimental design and provides useful evidence about human-aligned categorization in LLMs, but the contribution is somewhat limited by overclaiming and by methodological choices that blur the interpretation of “inductive bias.”

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real contribution, especially in framing and experimental design, and the figures are compelling enough that I think the work is worth discussion by the community. That said, I remain unconvinced by the strongest causal and theoretical claims, and I would like to see a tighter treatment of the IB formalization and the IICLL confounds.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant information-theoretic and representation-learning framing, though some conclusions depend on implementation details that are not fully specified in the main paper.