Now I have all the information to produce the final consolidated review. Let me write it.

## Summary

This paper proposes Recursive Metadata Normalization (R-MDN), a normalization layer that removes the effects of known confounding variables from intermediate DNN feature representations by leveraging the recursive least squares (RLS) algorithm. Unlike prior methods such as MDN (which requires batch-level statistics precomputation), R-MDN operates at the individual example level, enabling compatibility with vision transformers and natural integration into continual learning settings where data and confounder distributions shift across training stages. The method is evaluated on synthetic data, structural MRI sex classification (ABCD study), and dermatoscopic lesion classification (HAM10000), demonstrating reduced feature–confounder correlation and more equitable predictions across population groups.

## Strengths

- **Individual-example operation enables ViT compatibility and online learning.** Unlike MDN, which requires batch-level covariance precomputation and batch statistics during training (Section 2), R-MDN processes each example independently via the RLS update. This is a concrete architectural advantage that is empirically validated in the HAM10000 experiment (Section 4.2.2), where R-MDN is integrated into a vision transformer — something MDN cannot do.

- **Recursive state update naturally prevents catastrophic forgetting of confounder effects.** R-MDN maintains and continuously updates an internal model state (regression coefficients and inverse covariance matrix) using the Sherman–Morrison update. This allows a single network to generalize across training stages without stage-specific components. The continual learning experiments (Tables 3, 4) show that R-MDN achieves better backward and forward transfer than MDN, P-MDN, BR-Net, and standard continual learning methods (EWC, LwF, PackNet).

- **Strong empirical evidence of confounder invariance and equitable predictions.** In the ABCD sex classification (Table 2), R-MDN yields the lowest mean difference between true positive and true negative rates (1.1 ± 1.0) and the lowest squared distance correlation (dcor²) for both boys and girls, indicating unbiased predictions. The synthetic static learning experiment (Table 1) shows R-MDN achieving dcor² near zero at batch size 2048 (0.01 ± 0.00) across 100 random seeds.

- **Principled theoretical derivation with mini-batch extension.** Section 3 provides a clean mathematical derivation of the per-sample RLS update, extends it to mini-batches via the Sherman–Morrison–Woodbury formula (Section 3.1), and introduces a regularization term (λI) for numerical stability (Section 3.3). This distinguishes R-MDN from both the batch-level closed-form approach of MDN and the penalty-based heuristic of P-MDN.

- **Robust generalization to absent confounders.** Figure 5 shows that when the confounder intensity is reduced to zero, R-MDN maintains near-constant accuracy close to the theoretical maximum, whereas the base model, BR-Net, and P-MDN exhibit sharp drops. This is relevant to deployment scenarios like cross-hospital generalization where a confounder (e.g., machine type) may be absent.

- **Introduction of tailored continual learning metrics (BWTd, FWTd).** The paper adapts metrics from Lopez-Paz & Ranzato (2017) to account for theoretical maximum accuracy, providing a more precise evaluation of confounder-related forgetting than standard accuracy alone (Section 4.2.1, Equations 1–2).

## Weaknesses

### Fatal

None.

### Major

- **The MDN baseline implementation in continual learning is underspecified.** The paper argues in Section 2 that MDN cannot be straightforwardly applied in continual learning — it would require either repeated recomputation of Σ⁻¹ at each stage or a "look-ahead" precomputation on all stages' data. Yet MDN appears as a baseline in Tables 3 and 4 (continual learning experiments) without any explanation of which protocol was used. If MDN was given full-data look-ahead (pre-computing Σ⁻¹ on all stages), the comparison is informative but should be stated explicitly so readers can judge the fairness. If MDN was recomputed per stage, that needs to be stated as well. This matters because the paper's central novelty claim about continual learning rests partly on comparisons against MDN; the reader cannot evaluate those comparisons without knowing the setup. *(Note: this is a clarification issue, not necessarily an error — the paper's own analysis in Section 2 acknowledges both possibilities, suggesting the authors are aware of the issue. The core R-MDN contribution — example-level operation, ViT compatibility, online updates — is not undermined by this, but the experimental comparison is incomplete without specification.)*

### Minor

- **Hyperparameters ε and λ are not reported in the main text.** The paper mentions ε (initialization for R(0)⁻¹ = εI) in Section 3 and λ (regularization) in Section 3.3, noting that λ is tuned (ablation in suppl. F). However, the chosen values are not reported in the main text for any experiment. Since the paper criticizes P-MDN for having a "difficult-to-tune" penalty parameter γ, the reader needs to see that R-MDN's own parameters (ε, λ) are not themselves sensitive or difficult to tune. The appendix ablation partly addresses this, but reporting values and a brief sensitivity summary in the main text would strengthen the practical usability claim.

- **No pairwise statistical significance tests for the ABCD and continual learning experiments.** Table 1 reports a one-way ANOVA (p < 10⁻⁵⁸) across methods for the synthetic static experiment, but Tables 2, 3, and 4 lack pairwise significance testing. Some differences (e.g., R-MDN vs. MDN on ABCD TNR) are modest, and the reader cannot assess whether the improvements are robust across runs. Adding pairwise tests or confidence intervals would strengthen claims.

- **The feedback loop between residualized features and the classifier during training is not theoretically analyzed.** The paper uses the standard residualization formulation z = x̃β̃_x + yβ̃_y + r and removes only the confounder component (x̃β̃_x). This is correct in a static regression sense. However, during end-to-end training, the features z are not fixed — they co-adapt with the classifier and the regression coefficients, creating a feedback loop. The paper does not analyze whether this loop is stable or whether the linear residualization assumption remains valid under this dynamics. This limitation is shared with MDN (prior work) and does not invalidate the empirical results, but it is a gap in the theoretical justification presented in Section 3.

- **Linear residualization assumption is discussed but not diagnostically validated.** The paper motivates the linearity assumption in Section 1 (interpretability, avoidance of arbitrary nonlinear extraction) but does not include a diagnostic (e.g., comparing dcor² before vs. after residualization across multiple feature layers) to verify that linear regression is sufficient for the learned features in practice. Given that the method's effectiveness depends on this assumption holding, such a diagnostic would strengthen confidence in the results.

### Trivial

- None.

## Nice-to-Haves

- A stage-wise breakdown of dcor² for the HAM10000 experiment would be more informative than reporting a single test-set aggregate, especially since the confounder (age) distribution varies across stages.
- A brief wall-clock time or parameter count comparison with MDN and P-MDN in the main text (beyond the complexity analysis in suppl. B) would support the efficiency claim.
- A null distribution or baseline for interpreting the extremely low dcor² values (e.g., 0.002 for R-MDN) could help readers gauge practical significance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about MDN "look-ahead" being inherently unfair.** *(Reason: The paper's Section 2 explicitly discusses that in a cross-sectional study, MDN can compute Σ⁻¹ on all data. This is not "unfair" — it is MDN's standard operation mode, which the paper acknowledges. The actual concern is lack of specification, which is retained in Major Weaknesses above.)*

- **Criticism that "disagreement on taste" would lead the paper to not use certain methods.** *(Reason: Not present in the harsh critic's review. This rule is about potential issues, not actual criticisms made.)*

- **Strength Finder's generic summary paragraph.** *(Reason: The Strength Finder's closing paragraph is a summary of the paper's contributions, not a specific strength; it is redundant with the paper's own abstract and introduction.)*

## Novel Insights

The harsh critic identifies a genuinely important tension in the paper: R-MDN criticizes P-MDN for having a difficult-to-tune hyperparameter (γ), yet introduces its own hyperparameters (ε and λ). The paper partially addresses this via ablation (suppl. F), but the juxtaposition reveals a broader pattern in the confounder-removal literature — every method in this family trades batch-level statistical efficiency (MDN) for hyperparameter sensitivity (P-MDN) or initialization/regularization dependence (R-MDN). The paper's empirical advantage comes less from eliminating hyperparameter tuning and more from enabling a fundamentally different operational regime (online, example-level, ViT-compatible) that prior methods cannot enter at all. This is a more nuanced and defensible framing than "our method has no tuning problems."

## Suggestions

1. **Clarify MDN implementation in continually learning experiments.** State explicitly whether MDN's Σ⁻¹ was pre-computed on all stages' data (cross-sectional) or recomputed per stage (online). If the former, note that this is MDN's standard operation and does not violate the experimental setup for the cross-sectional HAM10000 study; if the latter, describe the recomputation protocol.

2. **Report ε and λ values used for each experiment in the main text** (a single sentence or brief table), and add a short paragraph summarizing the sensitivity analysis from suppl. F, demonstrating that performance is stable over a reasonable range.

3. **Add pairwise confidence intervals or statistical significance tests** (e.g., paired t-tests or bootstrap intervals) for the ABCD and continual learning experiments to help readers assess the robustness of observed differences.

4. **Include a brief diagnostic** showing dcor² before vs. after R-MDN residualization at multiple feature layers to empirically verify the linearity assumption in practice.

## Score and Decision

The paper proposes a clean, well-motivated extension of confounder-removal normalization to online and continual learning settings, with a clear practical advantage (example-level operation, ViT compatibility) and strong empirical support across multiple datasets, architectures, and evaluation metrics. The main weakness is an underspecified MDN baseline in the continual learning experiments, which needs clarification but does not fundamentally undermine the core contribution — R-MDN's unique capabilities (online updates, ViT compatibility, stage-generalization) are architectural properties independent of the MDN comparison. The remaining issues (hyperparameter reporting, statistical testing, theoretical analysis of the feedback loop) are addressable. The paper is a solid contribution that would benefit from clarification but does not require re-execution of experiments.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>