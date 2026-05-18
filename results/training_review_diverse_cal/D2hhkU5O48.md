Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me produce the final review.

---

## Summary

This paper introduces β-calibration, a group-conditional notion of calibration for generative QA that conditions on a user-specified partition of the QA space (Definition 3). The authors propose two post-hoc calibration algorithms — β-binning and hierarchical scaling-β-binning (HS-BB) — with a distribution-free finite-sample guarantee (Theorem 1). Experiments on 5 QA datasets with Mistral and Gemma models show that both methods substantially reduce β-calibration error compared to standard post-hoc calibrators, while maintaining or improving selective QA performance.

## Strengths

1. **Principled generalization of calibration for generative QA.** The paper correctly identifies a concrete limitation of average-case calibration (Example 1, Table 1) and formalizes β-calibration to address it. This is a well-motivated conceptual contribution that adapts group-conditional calibration ideas to the generative QA setting, where standard calibration aggregates over heterogeneous QA pairs and can misrepresent any specific user's experience.

2. **Novel combination of hierarchical scaling with binning.** Scaling-β-binning (Section 3.2) uses a hierarchical logistic regression model with random intercepts and random slopes per partition (Equation 3), enabling information sharing across partitions. This is a sensible solution to the data-sparsity problem in fine-grained partitions, and the empirical comparison of HS-BB vs. BB (e.g., 0.16 vs. 0.171 on MMLU/Mistral/Ling1S-Top1, Table 2) demonstrates that the hierarchical pooling provides real benefit over independent per-group binning.

3. **Strong empirical results on the β-calibration error metric.** Across 5 datasets, 2 LLMs, and 2 elicitation prompts, the proposed methods (BB, S-BB, HS-BB) consistently achieve substantially lower CE(·;β) than all baselines, often by a factor of 2–4× (e.g., HS-BB CE=0.16 vs. next-best S CE=0.249 on MMLU/Mistral/Ling1S-Top1; Table 2). The results are reported with standard deviations and the paper acknowledges that some improvement is expected since the baselines are not designed for β-calibration.

4. **Downstream selective QA validation.** The paper evaluates on AUAC (area under accuracy-confidence curve) and shows that the improved β-calibration translates to competitive or better selective QA performance compared to raw elicited confidence and other baselines. This goes beyond simply reporting calibration error.

## Weaknesses

### Major

1. **Gap between motivational framing and experimental validation of interpretability.** The paper motivates β-calibration with a compelling user-group example (User 1 vs. User 2, Figure 1), but the experiments use a kd-tree built on DistilBERT embeddings as the only β instantiation. The paper never validates that these embedding-based groups correspond to groups an actual user would find meaningful (e.g., by topic, difficulty, or domain). The paper states that "β is chosen such that the pre-image of a specific value of β represents a grouping that an end-user might be interested in" (line 143) and acknowledges in Limitations that "interpretability ... largely depends on the choice of β" (line 384), but the experimental evaluation cannot substantiate the claimed practical interpretability because the chosen β is never validated against any user-relevant grouping. This leaves a gap between the paper's central motivation and what the experiments actually demonstrate.

2. **Theoretical guarantee plays a limited role in the experimental setup.** Theorem 1 provides a distribution-free bound on conditional β-calibration error, but several practical issues limit its impact: (a) The condition that every partition must contain ≥ b points is violated for fine-grained partitions, with the paper relying on an uncovered fallback (global UMD); (b) The misspecification parameter ν is mentioned as estimable but is never estimated or validated empirically; (c) The hyperparameter selection procedure uses the bound only as a loose starting point, ultimately tuning on AUAC (line 368). The bound's main content (calibration error decreases with bin size) is standard from Gupta et al. (2021) and is not meaningfully employed to ensure calibration in the experiments.

### Minor

1. **Baselines do not use group information, making the CE(·;β) improvement partly tautological.** The paper acknowledges this ("may not be surprising," line 371), but the baseline set notably excludes a natural ablation: per-group Platt scaling (independent logistic regression within each partition). BB already serves as a per-group binning baseline, and HS-BB outperforms BB, showing the value of the hierarchical approach. However, per-group Platt scaling would further isolate whether the benefit comes from simply conditioning on groups vs. the specific algorithmic choices. Including this would strengthen the evaluation.

2. **AUAC and calibration are partially decoupled.** The paper correctly notes that raw elicited confidence (None) often achieves competitive AUAC despite having poor β-calibration error (e.g., None AUAC=0.269 vs. HS-BB AUAC=0.269 on MMLU/Mistral/Ling1S-Top1). This raises the question of what additional practical benefit β-calibration provides beyond ranking quality. The paper discusses this briefly (line 373) but does not fully reconcile why a user should prefer a β-calibrated score over a well-ranked but miscalibrated one (beyond the conceptual argument that thresholds are interpretable).

3. **kd-tree construction details are underspecified.** The paper specifies using the DistilBERT [CLS] token embedding (768 dimensions) and maximum depth d, but does not describe the splitting criterion for the kd-tree (e.g., median split along the dimension with largest variance, which is standard but should be confirmed). While the general approach is clear, this omission makes exact reproduction more difficult.

4. **Limited analysis of computational cost.** The hierarchical logistic regression with random effects requires fitting a multilevel model per calibration set. The paper mentions it is "more expensive" than β-binning (line 277) but provides no training time comparisons or scaling analysis. This matters for practitioners considering deployment on large datasets.

### Trivial

- Sections referencing appendix tables (Tables S1, S2) are absent from the main text — the appendix was presumably stripped, but this makes the claim of "5 datasets" unverifiable from the main paper alone.
- The term "β-calibration" is orthogonal to standard "beta calibration" (a parametric family), which may momentarily confuse readers familiar with the latter.

## Nice-to-Haves

- **Validate on user-relevant group definitions.** A natural follow-up would evaluate β-calibration with groups defined by topic (e.g., via existing dataset metadata), question difficulty, or domain. This would directly connect the motivational example to the experimental evidence.
- **Empirical validation of the theoretical bound.** Plotting empirical CE(·;β) against the bound from Theorem 1 for various b and N on real data would show whether the bound is non-vacuous and practically useful.

## Removed Points

- **"The experimental comparison is not a fair test" (per-group binning baseline missing):** BB is per-group UMD binning, and HS-BB vs. BB isolates the benefit of hierarchical pooling. The criticism that no per-group binning baseline exists is factually incorrect. A weakened version (per-group Platt scaling missing) is kept in Minor.
- **"Why not evaluate on GPT-4 or larger models":** Asking for GPT-4 (API-only, weight-inaccessible) in a post-hoc calibration paper requiring weight access or extensive API calls is practically infeasible for an academic submission. The paper already uses two capable open-weight models.
- **"Missing related works" (Błasiok et al., Si et al.):** Per instructions, missing related works cannot be confirmed or raised by this review.
- **"Notation confusion about β":** Style/presentation nitpick.
- **"The 'generalize' claim is misleading":** The paper clearly states β-calibration reduces to standard calibration when β is constant (line 143), making the generalization claim technically correct and appropriately caveated. Removed as strawman.
- **"Hierarchical model is standard, not novel":** The paper claims novelty in applying multilevel modeling to calibration, which is a reasonable claim. The observation about the model being standard does not invalidate the contribution.
- **"UMD description is vague":** The paper appropriately cites Gupta et al. (2021) as the source and provides an informal description. This is standard practice.
- **"Error bars — need pairwise significance tests":** The paper already reports ±1 standard deviation. Asking for pairwise significance tests is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a baseline of per-group Platt scaling (independent logistic regression within each β-partition) to isolate whether the improvement over standard calibrators comes from using group information vs. the specific hierarchical-binning design.
2. Include an experiment using a semantically meaningful β (e.g., groups by topic from dataset metadata, or groups by question type) and report per-group calibration error alongside aggregate CE(·;β). This would directly connect the motivational example to the empirical evaluation.
3. Provide empirical estimates of ν on a hold-out set for the scaling-β-binning setup, and show whether Theorem 1's bound is non-vacuous for the b values used in practice.
4. Specify the kd-tree splitting criterion in the main text or appendix, and report approximate training times for a representative dataset.

## Score and Decision

The paper makes a genuinely useful conceptual contribution and the proposed algorithms are technically sound. However, the evaluation has a significant gap: the motivational example is about user-relevant groups, while the experiments only validate on a generic embedding-based kd-tree grouping whose practical interpretability is unexamined. Combined with the limited practical role of the theoretical bound and the absence of per-group baselines that would strengthen the evaluation, the paper does not currently meet the threshold for acceptance. The core ideas have merit and the gap is addressable with additional experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>