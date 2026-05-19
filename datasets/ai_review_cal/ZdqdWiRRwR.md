- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper introduces Recursive Metadata Normalization (R-MDN), a learnable layer that removes the influence of confounding variables from intermediate DNN feature representations. R-MDN adapts recursive least squares (RLS) to update an internal regression model online, operating at the individual-example level rather than requiring batch statistics. This design enables compatibility with vision transformers and continual learning settings where data distributions shift over time. Experiments on synthetic data, neuroimaging (ABCD), and dermatoscopic images (HAM10000 with ViT) show that R-MDN reduces confounder correlation, promotes fairer predictions, and mitigates forgetting of confounder effects better than prior methods (MDN, P-MDN, BR-Net) and standard continual-learning baselines (EWC, LwF, PackNet).

## Strengths

- **Individual-example-level operation enables ViT compatibility.** Section 3.2 explains that because R-MDN processes examples independently rather than requiring batch-level statistics (as MDN does), it can be inserted into vision transformers without architectural awkwardness. This is demonstrated in the HAM10000 experiment (Table 4), where R-MDN is successfully integrated into a ViT.

- **RLS formulation enables continual learning without pre-computation.** Section 3 derives an online update via the Sherman-Morrison formula, eliminating the need to pre-compute covariance matrices over the full dataset (required by MDN). Table 3 shows R-MDN achieves superior forward transfer (FWTd) across three synthetic continual-learning datasets.

- **Substantially reduces confounder correlation and improves fairness on ABCD neuroimaging data.** Table 2 shows R-MDN achieves the lowest squared distance correlation with the PDS confounder (0.07 for boys, 0.05 for girls) and the smallest TPR–TNR gap (0.01), while Figure 4 confirms R-MDN does not rely on the cerebellum (the region most confounded by PDS).

- **Robust generalization to absent confounders.** Figure 5 shows R-MDN maintains near-constant accuracy (~0.83) as confounder intensity decreases from 1 to 0, whereas base model, BR-Net, and P-MDN all drop sharply. This directly supports the claim that R-MDN learns task-relevant features rather than spurious confounder correlations.

- **Evaluated across multiple architectures (CNN, ViT) and data modalities (synthetic, 3D MRI, 2D dermatoscopic).** The paper demonstrates R-MDN's flexibility as a general-purpose layer, not a bespoke solution for one setting.

## Weaknesses

### Fatal
None.

### Major

- **HAM10000 results lack multiple initializations.** Table 4 reports means and standard deviations computed across the five test stages *within a single training run* — not across model initializations or data splits. The caption reads "mean and standard deviation over test sets of different stages of training." The paper carefully reports multiple seeds/runs for other experiments (100 runs for Table 1, 5-run cross-validation for Table 2, 5 seeds for Table 3), so the omission for the HAM10000 ViT experiment is conspicuous. Some accuracy differences are modest (e.g., Stage 3: R-MDN(C) 63.9 vs. LwF 63.5), and without run-level variance the reader cannot assess whether the reported advantage of R-MDN over LwF/EWC at certain stages is robust or driven by sampling noise. This weakens the strongest practical demonstration of R-MDN in a ViT setting.

### Minor

- **BWTd metric can understate forgetting when baseline accuracy is poor.** BWTd = (1/(S−1)) Σ (|R_{S,i}−A_i| − |R_{i,i}−A_i|). If a method already performs far from the theoretical maximum A_i on stage i after training (large |R_{i,i}−A_i|), then even substantial further forgetting can yield a small BWTd because the initial deviation is already large. The paper reports BWTd consistently across methods so relative comparisons are still meaningful, but an explicit check (e.g., reporting raw |R_{S,i}−A_i| alongside BWTd) would strengthen the analysis.

- **R-MDN requires the confounder value at inference time, which is not discussed as a limitation.** The method residualizes features using the confounder matrix X, so at test time the confounder must be available to compute the residual. In deployment scenarios where confounder information is unknown (e.g., a model deployed on an unseen population), R-MDN cannot be directly applied. This should be acknowledged.

- **Scalability to high-dimensional confounders is not addressed.** The RLS update maintains a covariance matrix whose dimension equals the number of confounder features plus labels. For high-dimensional confounders (e.g., 50+ demographic/acquisition variables), per-layer cost grows quadratically. A brief discussion of this limitation would help practitioners assess suitability.

- **Overstatement about MDN and vision transformers.** The introduction says MDN "cannot be applied…in association with vision transformers." Section 3.2 more accurately says MDN is "unsuitable." MDN *can* be applied (at a computational cost), and the over-strong phrasing in the introduction is unnecessary given the paper's real architectural advantage.

- **Accuracy decrease on ABCD not fully discussed.** R-MDN achieves the lowest dcor² and TPR–TNR gap but also the lowest accuracy (Table 2). The paper calls this "a modest decrease in performance," but does not explicitly discuss whether the higher accuracy of other methods partially stems from their use of confounder information, which would make the trade-off more favorable for R-MDN.

### Trivial
None.

## Nice-to-Haves
- Report HAM10000 results over multiple random seeds (or provide bootstrap confidence intervals from resampling the test set) to establish statistical reliability.
- Extend the "absent confounder" experiment (Figure 5) to the HAM10000 dataset to demonstrate practical value for cross-hospital generalization.
- Test P-MDN inserted after each transformer block (not just pre-logits) on HAM10000 to definitively rule out placement as a confound.
- Include a brief computational complexity analysis in the main text (currently deferred to Appendix B).

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Reproducibility of synthetic continual learning setup (missing appendix details).** The critic noted the description of the three synthetic CL datasets is too vague. However, the paper explicitly states "A complete description of the 3 datasets is presented in suppl. C." Since the parser strips appendix content, this criticism cannot be verified from the available text. **Removed per rule: missing appendix details stripped by parser.**

2. **Missing limitations section.** The critic noted the absence of a limitations section. This is a presentation choice, not a verifiable error. The specific missing limitation (confounder at test time) is already retained as a Minor weakness above. The generic complaint about missing sections is removed.

3. **The harsh critic's various area-of-concern speculations** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?") that lack concrete anchor in the paper text have been removed or subsumed into specific verifiable points above.

## Novel Insights

None beyond the paper's own contributions. The two reviews identify the same core strengths and weaknesses: the RLS-based per-example design is the key innovation, and the main evidential gap is the lack of multiple-seed results for the HAM10000 ViT experiment.

## Suggestions
- **For the rebuttal:** Provide HAM10000 results with at least 5 random seeds (or justify why a single run is sufficient with bootstrap confidence intervals). Even a small number of seeds would substantially strengthen the paper's strongest practical claim.
- **For the camera-ready:** Add a brief limitations paragraph acknowledging (1) the need for confounder availability at inference time, (2) the linearity assumption between confounders and features, and (3) scalability considerations for high-dimensional confounders. Add the BWTd interpretation caveat (raw |R_{S,i}−A_i| alongside BWTd).
