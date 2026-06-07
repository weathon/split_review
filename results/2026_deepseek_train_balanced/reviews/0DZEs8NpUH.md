## Summary

This paper introduces "Personality Alignment" — tailoring LLM behavior to individual users' Big Five personality profiles — along with two contributions: (i) the PAPI dataset (307k subjects with IPIP-NEO-120/300 responses) and (ii) the Personality Activation Search (PAS) method, an inference-time activation steering approach with a searched intervention magnitude α. The core idea is well-motivated and the dataset is a genuine resource.

## Strengths

- **Large-scale psychometrically-grounded dataset**: PAPI covers 307,313 real subjects across ages 10–99 with responses to the well-validated IPIP-NEO-120 and IPIP-NEO-300 inventories (lines 64–65). This is orders of magnitude larger than prior personalization datasets and grounded in established personality theory, providing a useful resource for future work.

- **PAS outperforms same-model baselines in Table 1**: On Llama-3-8B-Instruct, PAS achieves a Composite Score of 4.41 vs. 5.96 (Few-Shot), 7.45 (DPO), and 7.62 (PPO) — all on the same base model (Table 1). On Llama-3-70B-Instruct, PAS scores 4.74 vs. 5.21 (Few-Shot). Lower scores are better on this metric.

- **Dynamic α search is a principled improvement over fixed-distance intervention**: The paper identifies a specific limitation of prior activation-intervention work (ITI — Li et al., 2024) — that a fixed intervention distance is poorly suited for alignment (line 109) — and replaces it with a searched α ∈ [0,10] (Equations 5–6). This is a concrete methodological refinement.

- **Efficiency advantage is demonstrated**: PAS requires no backpropagation, stores ~1,000 parameters per user, and the paper reports~1/6 the time of PPO (line 194). For per-user personalization, this is a meaningful cost reduction.

- **Generalization from multiple-choice to open-ended generation**: Figure 5 shows PAS transfers from the multiple-choice training format to open-ended responses, with GPT-4o evaluation favoring PAS over baselines. The human evaluation (Section 5.4) finds a Value-Aligned Assistant preferred 38% vs. 15% for a misaligned one (31% ties), providing direct evidence that personality alignment improves user satisfaction.

## Weaknesses

### Major

- **DPO and PPO baselines are completely underspecified, rendering the central comparison uninterpretable**: The paper's headline empirical claim is that PAS outperforms DPO and PPO while requiring 1/5–1/6 the time. However, the paper never describes how DPO or PPO were adapted to this task. DPO requires preference pairs (chosen/rejected completions for the same prompt); PPO requires a reward model. The PAPI training data consists of Likert-scale (1–5) responses to personality questionnaire items — how were pairwise preferences constructed? What was the reward model trained on? The experimental setup section (lines 173–180) lists PPO and DPO as baselines but provides zero details on their implementation. Without this, the reader cannot assess whether the baselines were reasonably configured, whether they had sufficient data, or whether the comparison is valid. This undermines the paper's strongest claimed advantage. *(Verified: lines 155–156 show scores; line 175 lists baselines; no DPO/PPO implementation details exist anywhere in the paper.)*

- **The most directly relevant baseline — ITI — is completely absent from the experiments**: The paper explicitly positions PAS as a modification of Inference-Time Intervention (ITI, Li et al., 2024), stating ITI "shift[s] a large and fixed distance" and that PAS improves this by searching over α (lines 29, 109). Yet ITI does not appear in Table 1 or anywhere in the experimental section. This is a striking omission. Without comparing against the method PAS is *designed to improve upon*, there is no evidence that the α-search contribution actually helps. Other activation-steering methods (representation engineering, activation addition) are also absent. *(Verified: ITI cited in Related Work and line 109; no ITI results in Table 1 or experiments.)*

### Minor

- **GPT-4o serves as both a baseline method in Table 1 AND the evaluator for open-ended generation** (lines 152, 178). If GPT-4o-as-judge prefers outputs stylistically similar to its own, this introduces systematic measurement bias favoring the confounded evaluation. The paper mentions a "manual evaluation" (line 209) but provides no results, methodology, or inter-rater statistics, so this does not mitigate the concern. The human evaluation (Section 5.4) partially addresses this for the broader value-alignment claim but not for the specific open-ended generation results in Figure 5.

- **No variance estimates or statistical significance reported anywhere**: Table 1, Figure 5, Figure 6, and the human evaluation all report point estimates with no standard deviations, confidence intervals, or significance tests. For the headline comparison (PAS 8B: 4.41 vs. GPT-4o: 4.42), the difference is 0.01 on a [0,25] scale — effectively a tie, and without variance we cannot assess whether any of the reported differences are meaningful. Similarly, the reasoning improvements in Figure 6 are sub-1% (e.g., GSM8K: 73.47 → 74.15, +0.68%) with no error bars. *(Verified: grep confirmed no instances of "standard deviation," "confidence interval," "p-value," or similar.)*

- **K-Means test-set selection is unorthodox and not validated**: The paper clusters all 307,313 subjects into 300 clusters using K-Means (on what feature space is not explicitly stated — presumably the 120-dimensional IPIP-NEO-120 Likert responses) and selects the sample nearest each centroid as the test set (lines 67–73). This produces a test set of 300 "archetypal" individuals rather than a representative random sample. The features (Likert 1–5 ordinal data) are treated with Euclidean distance without justification. No robustness check (e.g., random stratified split) is provided to show results are consistent under different test-set constructions.

- **No ablation studies**: The paper does not ablate K (number of selected heads), the effect of dispersed vs. concentrated intervention, or the α search vs. fixed α (ITI-style). This makes it difficult to attribute results to specific design choices.

- **"Significantly enhances reasoning capabilities" is overclaimed**: Figure 6 shows sub-1% improvements without statistical tests (e.g., GSM8K: +0.68%). These are not compelling evidence of "significantly enhanced" reasoning. Moreover, the experiment only adjusts conscientiousness in isolation, not all five dimensions simultaneously.

### Trivial

- The manual evaluation (line 209) is mentioned but never presented — no methodology, results, or statistics. Either report it or remove the sentence.

## Nice-to-Haves

- Include ITI and/or other activation-steering methods as baselines.
- Provide a description of DPO/PPO implementation specifics (preference pair construction, reward model training).
- Add error bars / confidence intervals to all quantitative results.
- Validate test-set construction with a random stratified split to show robustness.
- Run standard general-purpose benchmarks (MT-Bench, AlpacaEval) to verify that PAS preserves general capabilities when all five dimensions are adjusted simultaneously.
- Report total computational cost across all test subjects (not just per-subject).

## Removed Points

- **"Inconsistent efficiency claims (1/5 vs. 1/6)":** Removed because the abstract says "1/5 of the optimization time compared to DPO" while line 194 says "1/6 of the time needed for PPO." These are comparisons to *different* baseline methods, not an inconsistency. The paper consistently reports 1/6 relative to PPO and 1/5 relative to DPO.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced standard evaluation concerns (baseline underspecification, missing relevant comparisons, lack of statistical rigor) but did not yield a novel synthesized observation about the problem domain or method.

## Suggestions

1. Document the DPO/PPO baseline setup in full — how Likert-scale data was converted to preference pairs, the reward model architecture and training for PPO, and hyperparameter selections.
2. Add ITI as a baseline in Table 1. Since PAS is explicitly presented as an improvement over ITI, this comparison is necessary to validate the core methodological contribution.
3. Report standard deviations or confidence intervals for all reported scores in Table 1 and figures.
4. Replace or supplement the K-Means test-set selection with a random stratified split and show that results are consistent.
5. Replace GPT-4o as the judge for open-ended generation with a different evaluator (e.g., GPT-4 or human annotators), or provide the full manual evaluation that is currently only mentioned.
6. Run standard general-purpose capability benchmarks (e.g., MT-Bench) to validate that PAS preserves conversational quality when all five personality dimensions are adjusted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>