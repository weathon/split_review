Now I have all the information needed. Here is my consolidated final review:

## Summary
The paper introduces Scalable Ensemble Diversification (SED), which enables disagreement-based ensemble training at ImageNet scale by dynamically selecting hard training samples as disagreement targets (replacing the separate OOD data required by prior methods) and using stochastic pair selection to reduce computational cost from O(M²) to O(1). The paper also proposes a Predictive Diversity Score (PDS) for OOD detection. Experiments show OOD generalization gains (e.g., +5.3% on ImageNet-R with M=50 prediction ensembles) and strong OOD detection AUROC on semantic shifts.

## Strengths

- **Problem framing and technical contribution.** The paper correctly identifies a real barrier — prior disagreement-based diversification (A2D, DivDis) required separate OOD data and O(M²) pairwise computation, limiting it to small-scale settings. The dynamic hard-sample weighting (Eq. 4–5) and stochastic pair selection (§3.2) are principled workarounds that enable ImageNet-scale experiments. SED-A2D outperforms A2D while being computationally cheaper.

- **Substantial OOD generalization improvements.** For M=5 (Table 2, prediction ensemble), SED-A2D achieves 85.3% ID accuracy (essentially matching the 85.4% of deep ensemble) while substantially outperforming all baselines on OOD: 43.0% vs 39.9% on IN-A, 48.7% vs 46.3% on IN-R. For M=50, the OOD gains increase further (53.8% on IN-R vs 48.5% for +Diverse HPs, +5.3%) although at some ID accuracy cost (83.6% vs 85.5%). These gains hold across prediction ensembles and uniform soups.

- **Strong OOD detection for semantic shifts.** The semantic shift detector (Table 3, SED-A2D+PDS) achieves best AUROC on iNaturalist (0.977) and OpenImages (0.941) with a moderate ID accuracy drop (82.9% vs 85.5%). PDS is a conceptually clean relaxation of the number of unique argmax predictions, and the qualitative examples (Figure 1) confirm it captures meaningful diversity.

- **Thorough evaluation.** Experiments span IN-A, IN-R, IN-C (1,5), iNaturalist, and OpenImages across both semantic and covariate shifts, with three aggregation strategies.

## Weaknesses

### Fatal
None.

### Major

1. **Covariate-shift OOD detector evaluated against structurally unfair baselines.** The SED-A2D covariate shift detector (Table 3) achieves only **1.0% accuracy on IN-Val** — essentially random for 1000-class ImageNet. The paper acknowledges this in one sentence (line 374), but then compares this detector's AUROC (0.681, 0.894) against baselines that maintain **85.5% ID accuracy**. Any detector that cannot classify ID data is not practically usable as a combined classifier+detector. The AUROC numbers may still be discriminative, but framing these as "superior OOD detection" without prominently emphasizing that the best results come from a detector useless for classification is misleading. The semantic shift detector (82.9%) is far less affected.

2. **Diversity metrics (Table 1) and generalization results (Table 2) come from different model configurations, weakening the causal claim.** Table 1 reports diversity for ensembles explicitly tuned for OOD detection (different λ values, as stated in the caption), while Table 2 reports generalization for ensembles trained separately. The paper claims "increased ensemble diversity contributes to the improvements in OOD generalization" (line 307) and "superior diversification ability verified in §4.1 leads to greater OOD generalization" (line 299), but never verifies that the specific ensembles in Table 2 have the diversity levels claimed in Table 1. The causal link is asserted without direct evidence from a consistent configuration.

### Minor

1. **PDS definition has a formula-to-table normalization inconsistency.** Equation (7) defines η_PDS = (1/C) Σ_c max_m p_c^m, which for C=1000 would yield values ≤0.005 — but Table 1 reports PDS values of 3.98–4.46 (consistent with the unnormalized sum), and Figure 1 reports values of 0.216–0.300 (consistent with a different normalization). This is a presentation error, not a substantive one — the values are internally interpretable — but it should be corrected.

2. **The λ-ablation (Figure 4) shows only PDS and AUROC but not the corresponding accuracy.** Given the known trade-off between diversification strength and ID accuracy (catastrophic drop to 1.0% at high λ for covariate shift), the figure is uninformative without accuracy shown alongside. The operating point where AUROC jumps could correspond to a non-viable accuracy regime.

3. **No direct evidence that "hard training samples" are OOD-like.** The method's core motivation is that disagreement on hard ID samples substitutes for disagreement on OOD data. The paper provides no analysis (visualizations of high-α_n samples, case studies) to validate whether these hard examples are genuinely distributionally different or OOD-like.

4. **The "scalable" claim is demonstrated only in a shallow fine-tuning setting.** All experiments freeze a DeiT3b backbone and train only the last 2 layers. While the comparison to baselines under identical constraints is fair, full end-to-end training — where computational cost is most prohibitive — is not tested.

### Trivial
None beyond the PDS normalization issue noted above.

## Nice-to-Haves
- Add a diversity table (like Table 1) for the OOD generalization ensembles to directly support the causal diversity→generalization claim.
- Include accuracy curves alongside the λ-ablation (Figure 4) so the detection vs. classification trade-off is transparent.
- Show qualitative examples of high-α_n training samples to validate the hard-sample-selection motivation.
- Report the trade-off between PDS-based detection and ID accuracy more systematically (e.g., a pareto curve).

## Removed Points
The following points raised in the reviews are removed per the review guidelines. They are listed here for completeness but should not be treated as valid weaknesses.

- **"#unique=5.00 contradicts 85.3% accuracy"** — The critic confused two different experimental configurations. The #unique=5.00 (Table 1, Covariate detector) corresponds to the ensemble with 1.0% accuracy (Table 3), not the 85.3% generalization ensemble (Table 2). No contradiction exists.
- **"PDS values impossible under the definition"** — The formula has a normalization inconsistency, but the reported values (3.98–4.46) are perfectly interpretable as the unnormalized sum Σ_c max_m p_c^m (range [1, M]). This is a formula typo, not a data fabrication.
- **"Missing OOD detection baselines"** — The paper explicitly references Table \ref{tab:ood_scores} (line 374) in the appendix for MSP/ODIN/Mahalanobis comparisons. Missing appendix content is a parser artifact.
- **"Missing ablation of stochastic pair selection"** — The paper references Table \ref{tab:stoch_sum_abl} (line 218) in the appendix for this ablation. Parser artifact.
- **"Ad-hoc weighting with no justification"** — The paper provides justification (lines 150–154): the squared denominator ensures α_B = 1/mean(CE), controlling for early-training trustworthiness.
- **"Missing theoretical justification"** — The paper explicitly acknowledge this gap in the Limitations section (line 451).

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective the paper does not already articulate.

## Suggestions
1. **Correct the PDS formula normalization** to match the reported values and unify across all tables/figures.
2. **Add diversity numbers for the OOD generalization ensembles** (a row in Table 1 or a companion table) so the diversity→generalization claim is backed by consistent data.
3. **Separate the OOD detection narrative** for the covariate shift detector (1.0% ID accuracy — useful as a pure detector only) from the semantic shift detector (82.9% — practically viable). Prominently caveat that the best AUROC numbers come from a configuration with broken ID classification.
4. **Include accuracy alongside AUROC in the λ-ablation** so readers can see where the trade-off becomes unacceptable.
5. **Add qualitative analysis of samples with high α_n** to validate that they are genuinely OOD-like.

The paper addresses an important problem and the core method shows real empirical gains, particularly at M=5 where there is no ID accuracy loss and clear OOD improvements. The main flaws are in presentation and framing rather than the methodology itself, and are addressable in revision.

## Score and Decision

**Assessment dimensions (language only):** The paper's originality is moderate (incremental but meaningful engineering over A2D). The research question is important — scaling ensemble diversification to realistic settings is a genuine need. The claims are partially supported: the empirical gains are real but the diversity→generalization causal link is not directly evidenced, and the OOD detection comparisons are structurally unfair for the covariate detector. The experiments are broad and otherwise sound. The presentation has several fixable inconsistencies. The value to the community is positive if the presentation issues are corrected.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>