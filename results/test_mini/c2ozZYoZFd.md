Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper systematically re-examines all four lines of evidence from "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), an ICLR 2025 Oral. Through extensive re-analysis including newly conducted experiments (~6000 A100-hours of compute across 9 models × 2 stages × 31 temperatures), discovery of omitted data, application of proper statistical testing, and verification of community claims, the paper demonstrates that the original work's data do not support its claims of min-p's superiority. From this case study, the paper distills six actionable lessons for improving rigor in empirical ML research and contributes a novel Best-of-N methodology for controlling hyperparameter volume in method comparisons.

## Strengths

- **Exposure of omitted data and flawed statistical analysis in human evaluations**: The paper demonstrates that the original study excluded one-third of its human evaluation data (basic sampling scores) without justification, and that when correct statistical tests are applied (Bonferroni correction, IUT), the data provide no evidence that min-p "consistently" outperforms baselines (Table 1, Figure 1, Sections 2.1–2.2). This is a concrete, verifiable finding that directly undercuts the original paper's central quality/diversity claim.

- **Novel Best-of-N methodology for fair hyperparameter comparison**: The paper develops a principled approach to equalize hyperparameter tuning volume across methods, conducting an extensive sweep on GSM8K across 9 models, 31 temperatures, and 6 hyperparameters per sampler. The results consistently show that min-p is indistinguishable from or worse than other samplers when hyperparameter volume is controlled (Figures 4, 5, Section 3). This methodology itself is a transferable contribution to fair method comparison.

- **Identification of selective reporting in LLM-as-a-Judge results**: The paper documents a specific instance where the higher of two scores was reported for min-p while the lower was reported for top-p in the original Table 3(b), with supporting evidence from a public Telegram link (Section 4.3). This is a precise, verifiable finding.

- **Verification of retracted community adoption claims**: The paper shows that the claimed 54,000 repositories and 1.1 million stars could not be substantiated (453k stars across leading LM repositories is less than half the claimed figure) and were subsequently retracted from the camera-ready manuscript. Three of four original reviewers cited these unsubstantiated numbers as key justification for acceptance (Section 5).

- **Actionable blueprint for rigorous methodology**: The paper distills six concrete, well-supported lessons from the case study — fair hyperparameter control, correct statistical testing, data transparency, scrutiny of qualitative summaries, methodological clarity, and detection of selective reporting (Section 6).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **NLP sweep limited to a single benchmark (GSM8K)**: The hyperparameter sweep covers 9 models with impressive breadth but only evaluates on GSM8K CoT. The original paper also presented results on GPQA (5-shot). The authors acknowledge the compute budget (~6000 A100-hours) as the constraint, but this means the claim that "min-p does not outperform baselines on NLP benchmarks" rests on evidence from a single task type (math reasoning). Including even one additional benchmark would strengthen generalizability. The transparency about the limitation is commendable, but the limitation itself remains.

- **No formal statistical tests reported for the second human evaluation study (Section 2.4)**: The paper presents the second human study's results via visualization (Figure 3) and a noted data-entry discrepancy (7.80 vs. 5.80), concluding that min-p does not outperform baselines. However, the rigorous hypothesis testing framework applied to the first study (paired t-tests with corrections) is not extended to this second dataset. While the visual pattern in Figure 3 is clear and the paper's main conclusions do not depend on this study alone, formal tests would make the argument stronger and more consistent with the paper's own advocacy for statistical rigor.

- **Sensitivity of hyperparameter range choices in the Best-of-N analysis**: The sweep uses values "taken from the original paper" (top-p: {0.7, 0.8, 0.9, 0.95, 0.98, 0.99}; min-p: {0.01, 0.02, 0.05, 0.1, 0.2, 0.3}). While these cover the meaningful operating region for each method and the Best-of-N subsampling mitigates individual value dependence, a sensitivity analysis testing whether conclusions hold under alternative range choices (e.g., extending either range) would further strengthen the claim. The paper uses ranges from the original work, which is reasonable, but the question of how results vary with range boundaries is not addressed.

### Trivial
None.

## Nice-to-Haves

- A comparative table overlaying the selectively reported LLM-as-a-Judge scores (both p values for min-p and top-p) would make the selective reporting accusation more immediately graspable to readers skimming Section 4.3.
- A short concrete checklist for evaluating sampling method comparisons (beyond the six lessons) would increase practical impact for reviewers and practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's concern that top-p's hyperparameter range is "more tightly concentrated near 1.0" while min-p's "includes values that may be suboptimal." Both ranges span a comparable width of 0.29, both cover the meaningful operating region for each method, and both were taken directly from the original paper. The Best-of-N analysis further sub-samples from these sets, reducing sensitivity to any individual value. This criticism does not identify a genuine flaw.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface insights the paper itself does not already articulate. However, one observation worth noting is the methodological parallel between this paper and the broader trend of "meta-scientific critique" papers in ML: this paper demonstrates that such work can be more than a destructive exercise — by combining re-analysis with new experiments, novel methodology, and constructive lessons, it provides a template for turning critique into positive methodological contributions. The Best-of-N hyperparameter control technique, in particular, could find broad adoption beyond this specific case study.

## Suggestions

1. **Extend the NLP sweep to at least one additional benchmark** (e.g., GPQA as in the original paper, or a creative writing / closed-book QA task) to demonstrate that the results generalize beyond math reasoning. Even a smaller-scale sweep on one additional dataset would substantially strengthen the claim.

2. **Add formal statistical tests (e.g., paired t-tests with correction) for the second human evaluation study** in Section 2.4, consistent with the rigor applied to the first study. Presenting p-values alongside Figure 3 would make the conclusion more definitive.

3. **Include a brief sensitivity analysis** in Section 3 or the appendix showing that the Best-of-N results are robust to moderate shifts in hyperparameter range boundaries (e.g., testing min-p at p=0.4 or top-p at p=0.5). This would address the reasonable question of whether conclusions depend on the specific ranges chosen.

## Score and Decision

Calibration anchors (all from ICLR 2026 human reviews corpus):

| Path | Avg Score | Comparison to This Paper |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/ZHKVPkJMSI.md` | 6.00 | Methodology critique of SITE benchmarks. Our paper has broader scope (4 lines of evidence vs. 1), more extensive experiments, and an additional novel methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/5R11h5o44C.md` | 6.50 | PU learning benchmark with thorough experimentation. Similar in empirical rigor; our paper additionally contributes a novel analysis methodology and has higher potential for cross-field impact. |
| `/home/wg25r/review_agent/human_reviews_2026/19LHXi9uLw.md` | 5.60 | CIL evaluation critique with theory + experiments. Our paper has a larger experimental scope and a more actionable set of lessons. |
| `/home/wg25r/review_agent/human_reviews_2026/vPN4ay2wyu.md` | 4.00 | Reproducibility cost study. Our paper is significantly stronger in methodology and has fewer substantive weaknesses. |
| `/home/wg25r/review_agent/human_reviews_2026/1CR1MTIgmq.md` | 0.00 | Attack paper with no scientific contribution. Not comparable — our paper provides new experiments, novel methodology, and constructive lessons. |
| `/home/wg25r/review_agent/human_reviews_2026/1a9daUteZn.md` | 4.00 | Statistical framework for influential sets. Limited scope (1D OLS only); our paper has broader applicability and stronger empirical contributions. |

This paper is a thorough, transparent, and methodologically rigorous re-analysis of a high-visibility prior work. It goes beyond critique by contributing a novel technique (Best-of-N hyperparameter control) and distilling actionable lessons for the community. The weaknesses are minor — they do not threaten the core claims, which are well-supported across multiple independent lines of evidence. The paper's impact on research norms and practices in empirical ML could be substantial.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>