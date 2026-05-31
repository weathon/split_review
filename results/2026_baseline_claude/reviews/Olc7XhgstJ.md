## Summary

This paper proposes **Steady Thought (ST)**, a three-stage framework to mitigate the *under-thinking* problem in Large Reasoning Models (LRMs), where models frequently abandon promising intermediate reasoning thoughts to switch to new ones. ST operates via: (1) entropy-based thought segmentation that partitions model responses into coherent thought units; (2) logit-suppressed thought completion that forces the model to complete individual thoughts without switching; and (3) Steady Thought Preference Optimization (STPO), a SimPO-variant that operates at the thought level, treating completed correct thoughts as "chosen" and subsequent wasteful continuations as "rejected." Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks show simultaneous accuracy gains (+1.9–5.3%) and token reductions (17.3–39.3%).

---

## Strengths

- **Well-motivated empirical premise.** Figures 1a and 1b directly demonstrate that correct thoughts emerge early in the reasoning chain yet are frequently abandoned, providing concrete evidence for the under-thinking problem rather than relying on anecdote. The scatter plots across two models and two datasets make the claim hard to dismiss.

- **Principled preference optimization formulation.** Conditioning the STPO loss on the thought prefix (Q, T_i) rather than just the question Q is a clean and principled design: the model is taught to recognize and commit to a promising intermediate state, not merely to prefer globally correct outputs. The length-normalized objective inherited from SimPO addresses the natural imbalance in length between chosen (completed thought) and rejected (subsequent wasteful thoughts).

- **Strong and consistent empirical results.** Table 1 shows that ST is the only method that consistently improves *both* accuracy and token efficiency across all three base models. The failure modes of competitors are striking: NOWAIT inflates Qwen3-8B token count by 84.6% while dropping accuracy 21 points; NoThink collapses accuracy by up to 29 points. ST avoids these failure modes entirely.

- **OOD generalization to code.** Trained exclusively on mathematical data (Omni-Math), ST improves LiveCode accuracy by +5.3% (Qwen3-8B) and +4.2% (14B), suggesting the learned behavior—committing to promising thoughts—transfers across domains. This supports the authors' claim that the model learns a reasoning pattern rather than memorizing problem-specific solutions.

- **Meaningful ablations on training algorithm.** Table 4 isolates the contribution of STPO versus SFT and DPO on the same data, showing DPO fails to reduce token length and SFT degrades accuracy. This directly supports the design choice of SimPO-style length normalization.

---

## Weaknesses

### Fatal
None.

### Major

- **Data-collection suppression is the same mechanism criticized in baselines.** The Thought Completion stage suppresses "wait"/"alternatively" tokens via logit manipulation—identical in principle to NOWAIT. The paper criticizes NOWAIT for globally suppressing switching, yet uses the same suppression mechanism to build training data. The key difference (inference-time versus data-collection) is implied but never explicitly addressed, which weakens the paper's framing that ST is fundamentally different from token-level suppression methods. This conflation is conceptually important and should be resolved.

- **Trigger-word list is brittle and underspecified.** The thought segmentation and completion both rely on a predefined list of switch trigger words (e.g., "wait", "alternatively"). The paper does not report the full list, does not discuss coverage, and does not analyze what happens when the model uses unlisted switching phrases. Different LRM families use different vernacular for thought transitions, and an incomplete list will produce silent failures—thoughts that switch without suppression, and segments that are incorrectly merged.

- **Entropy threshold requires per-model manual tuning.** Table 3 shows threshold sensitivity (2.8 vs. 3.0 vs. 3.2 yield noticeably different outcomes for 1.5B). Appendix D reportedly extends this to more models, but the requirement for model-specific threshold tuning is a practical limitation on reproducibility and scalability. The entropy threshold is also computed over the full vocabulary during decoding, but the paper does not state whether top-k/p filtering is applied, which can substantially alter entropy values.

### Minor

- **AIME 2024 evaluation reliability.** AIME 2024 has only 30 problems. Even with 8-run averaging, the reported accuracy values (e.g., 31.2%, 65.8%) have substantial variance. Confidence intervals are not reported anywhere in the paper, making it difficult to assess significance of the gains on this benchmark.

- **The "Percentage of Correct Thoughts" (PCT) metric is self-referential.** PCT is measured using the same segmentation and completion pipeline used to build training data. Any systematic errors in the pipeline (e.g., mis-segmented thoughts, trigger-word misses) would contaminate both the training signal and the metric, potentially inflating the apparent improvement in Table 2.

- **No comparison with training-based under-thinking baselines.** The baselines (NoThink, NOWAIT, SEAL) are all inference-time methods. Wang et al. (2025c), cited as the original under-thinking paper, presumably includes training-based variants; comparing ST against those would strengthen the case.

### Trivial

- Table 1 column header "Acc[%]↓" should be "↑" for accuracy; the direction arrows appear inverted throughout the table.

---

## Nice-to-Haves

- Reporting confidence intervals or standard deviations on AIME results would strengthen statistical claims.
- An explicit list and discussion of trigger words, along with an analysis of their coverage across different model families, would improve transparency.
- Comparing the inference-time cost of ST (which requires no additional computation after training) versus SEAL (which modifies hidden states at every step) would be informative.

---

## Novel Insights

The core insight of STPO—conditioning the preference signal on an intermediate thought prefix (Q, T_i) rather than the full question—is genuinely novel. It converts the global preference between complete responses into a local preference over continuations from a specific reasoning checkpoint, providing more surgical training signal. This thought-level conditioning could generalize beyond under-thinking: it is an instance of *prefix-conditioned* preference optimization applicable wherever one can identify critical intermediate states in a multi-step generation process. The observation (Figures 1a/1b) that earlier thoughts in a chain are disproportionately likely to be correct—meaning the first correct thought appears at a low rank—also offers a useful diagnostic about under-thinking severity that could guide future data curation or model evaluation.

---

## Suggestions

- Explicitly discuss why logit suppression during data collection does not suffer the same failure modes as NOWAIT at inference time; perhaps include a controlled experiment where NOWAIT-collected data is used to train a model, compared against ST-collected data.
- Provide the complete trigger-word list and an out-of-vocabulary analysis showing what fraction of actual thought switches are captured by it.
- Report error bars on AIME 2024 results, and consider including AIME 2025 or additional contest problems to increase statistical power.
- Clarify the entropy computation details (vocabulary size, temperature, whether filtering is applied) to ensure reproducibility.

---

## Score and Decision

The paper addresses a real and practically significant problem, offers a principled formulation, and delivers compelling empirical results across model scales and domains. The main conceptual tension—using suppression to build data while criticizing suppression in baselines—is resolvable but currently underaddressed. The algorithmic novelty (adapting SimPO to thought-level prefixes) is moderate but purposeful, and the complete experimental story justifies acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>