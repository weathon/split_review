Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

The paper proposes MMD-MP, a multi-population aware optimization for kernel-based Maximum Mean Discrepancy that removes the intra-class MGT distance term $k_\omega(y,y')$ from the training objective to reduce variance when dealing with MGTs from diverse LLMs. The method is applied to paragraph-based (two-sample test) and sentence-based (single-instance detection) MGT detection tasks. Extensive experiments across ChatGPT, GPT2, GPT3, and GPT-Neo series show consistent improvements over baselines, with particularly large gains in transfer to unseen LLMs.

## Strengths

1. **Novel and well-motivated variance-reduction approach**: The paper identifies a genuine problem — training deep kernel MMD on multi-population MGT data inflates variance (Fig. 1) — and proposes a clean solution: remove the $k_\omega(y,y')$ intra-class term during optimization. The motivation is supported by empirical variance decomposition (Fig. 2c–d) showing MMD-MP achieves substantially lower variance than MMD-D.

2. **Large and convincing gains on transfer to unknown LLMs**: When trained on ChatGPT/GPT2-series MGTs and tested on unseen LLMs (GPT-Neo-L, GPT-j-6b, GPT4all-j), MMD-MP achieves absolute test-power gains of **23.61%–27.65%** over MMD-D (Table 5) and ~3–4% AUROC gains (Table 6). These are large, unambiguous improvements that directly support the paper's claim of enhanced transferability.

3. **Consistent superiority across diverse settings**: Across single/multi-population, full/limited/unbalanced training data, paragraph-based and sentence-based detection, MMD-MP outperforms all baselines (MMD-D, C2ST, metric-based, model-based) in every table. The advantage is particularly pronounced when multiple MGT populations are present — e.g., 79.92 vs 62.34 on three-population limited data (Table 2) — which is exactly the scenario the method is designed for.

4. **Theoretical backing for the proposed objective**: Proposition 1 (asymptotic normality of MPP), Corollary 1 (test power expression), and Theorem 1 (uniform convergence bound) provide statistical grounding for the proxy objective, going beyond purely heuristic modification.

## Weaknesses

### Fatal
None.

### Major
None. The issues raised do not threaten the core claims of the paper.

### Minor

1. **Training MGTs for non-ChatGPT LLMs generated from only 20 prompts (line 382).** The paper uses the first 20 prompts of HWT in HC3 to generate training MGTs for all non-ChatGPT LLMs. This is a narrow prompt distribution, and the paper does not discuss whether test prompts are disjoint or how representative these 20 prompts are. While this does not invalidate the method — the core contribution is about optimization, not data scaling, and the synthetic experiments (Section 4.1) and ChatGPT results (which use the full HC3) provide complementary evidence — it does limit confidence that the results would fully generalize to broader prompt distributions. The paper should acknowledge this as a limitation.

2. **Significance level for test power not specified.** Test power is defined as the probability of rejecting the null when $P \neq Q$, but the rejection threshold $\alpha$ (e.g., 0.05) is never stated. Algorithm 2 outputs a p-value, but the paper does not say what threshold is used to compute the reported test powers. This makes the raw numbers not fully interpretable, though relative method comparisons remain valid.

3. **Some single-population improvements are modest relative to reported variance.** On a few cells (e.g., ChatGPT column in Table 1: 93.21$\pm$1.35 vs 91.76$\pm$1.58; ChatGPT column in Table 2: 92.31$\pm$2.30 vs 91.38$\pm$2.09), the improvement is less than the sum of standard deviations. This tempers the claim of "superiority" on those specific settings, though the method never loses to baselines and the multi-population/transfer results are decisive.

### Trivial

1. **Data generation details for non-ChatGPT LLMs are underspecified.** The paper states "first 20 prompts of HWT in HC3" but does not specify which prompts, how many MGTs were generated per prompt, or any filtering criteria applied. These details would improve reproducibility.

2. **The variance decomposition analysis (Section 2.3) is shown for a single run.** While the paper uses this as motivation (not proof) and validates the method extensively downstream, noting that the observations come from a single un-ablated trajectory would improve rigor.

## Nice-to-Haves

- A controlled ablation training with the full MMD objective plus an explicit variance regularizer would further strengthen the causal claim that variance reduction is the mechanism.
- Quantitative metrics of feature separation (e.g., silhouette score, centroid distance) to complement the t-SNE visualization in Figure 4.
- A brief discussion of how the 20-prompt limitation might affect generalization and why the method's core contribution does not depend on prompt diversity.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Disconnect between training objective and test-time statistic"** — The paper explicitly addresses this at line 288 ("Empirically, the performance of these two strategies is almost identical") and at line 316 with a clear rationale (MMD equals zero when $P=Q$, MPP would be negative). The theoretical analysis of the MPP objective is for training; the empirical validation shows the trained kernel works with the full MMD at test time. The critic's concern is addressed by the paper.

2. **"Variance decomposition analysis is empirical and not controlled"** — The paper presents the variance decomposition as observational motivation (Section 2.3: "conduct empirical studies to demonstrate the trends"), not as a rigorous proof. The method is then rigorously evaluated in experiments. This is standard hypothesis-generation followed by validation.

3. **"Figure 1 axis labels not described"** — Figure axis labels are embedded in the figure images, which are not accessible in plain text extraction. The subfigure captions clearly indicate what each plot shows (MMD values, MMD variance, test power).

4. **"unbanlance hc3" typo in Figure 3** — Per instructions, formatting/typo nitpicks are removed as parser artifacts.

5. **"Missing baselines (DNA-GPT, Fast-DetectGPT)"** — The existing baseline set (Log-Likelihood, DetectGPT, OpenAI-D, ChatGPT-D, C2ST, MMD-D, CE-Classifier) is adequate for demonstrating the method's effectiveness. Adding more baselines would not change the core claims.

6. **"Request for t-SNE quantitative metrics"** — This is a nice-to-have; the t-SNE visualization is qualitative and appropriate as a supplement.

7. **"Notation Var(E[H*]) is ambiguous"** — The paper explicitly defines this at line 137: "$\mmE$ denotes taking expectations across two populations sampled from MGTs and HWTs and $\mathrm{Var}$ denotes taking variances within these sampled populations." The notation is explained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- State the significance level $\alpha$ used in permutation tests for test power computation explicitly.
- Add a brief limitations paragraph discussing the reliance on 20 prompts for non-ChatGPT MGT generation and whether test prompts are disjoint.
- For single-population results where gains are modest, consider adding bootstrap confidence intervals or paired significance tests to clarify which differences are reliable.
- Specify the number of MGTs generated per prompt and any filtering steps used in data preparation.

## Score and Decision

This paper makes a genuine contribution: it identifies a real problem (variance inflation in MMD under multi-population training), provides a clean solution (removing $k_\omega(y,y')$), and validates it extensively with particularly strong results on the practically important transfer-to-unknown-LLM scenario. The weaknesses — limited prompt diversity for non-ChatGPT models, unspecified test-power significance level, and modest gains on a few single-population settings — are real but addressable and do not undermine the core claims. The paper is acceptable with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>