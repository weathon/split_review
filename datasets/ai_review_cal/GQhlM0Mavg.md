- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper formalizes the connection between Out-of-Distribution (OOD) detection and Conformal Prediction (CP) and illustrates two benefits of using them jointly: (1) applying CP corrections to standard OOD evaluation metrics (AUROC, FPR@TPR95) to obtain "conformal" versions with probabilistic conservativeness guarantees, and (2) exploring the use of OOD scores as nonconformity scores in CP to improve prediction-set efficiency. The first contribution is sound, clearly derived, and validated on OpenOOD and ADBench benchmarks. The second contribution is preliminary and underdeveloped relative to the claims made in the paper.

## Strengths
- **Formal derivation of the OOD–CP link via p-values and CP corrections (Sections 4.1–4.4):** The paper provides a rigorous translation of the OOD false positive rate into a p-value, then applies corrections from Bates et al. (2022) (marginal and calibration-conditional) to define *conformal AUROC* and *conformal FPR@TPRβ*. This is the paper's primary technical contribution, cleanly adapting established CP theory to OOD evaluation with clear probabilistic guarantees.

- **Empirical validation on two major benchmarks showing the correction's impact and practicality (Table 1, Figure 3):** On OpenOOD (δ=0.01) and ADBench (δ=0.05), the conformal correction lowers AUROC by roughly 1–2%, which is significant for leaderboard comparisons but not so severe as to render the metric unusable. The ADBench results further show the correction affects all baselines similarly. These experiments demonstrate that the correction provides meaningful conservativeness without destroying practical utility.

- **Concrete illustration of FPR fluctuation using SVHN extra data (Figure 1):** Using 53 disjoint calibration sets of 10k points from SVHN, the paper empirically shows that the estimated FPR follows a Beta distribution matching the theoretical prediction of Bates et al. (2022). This grounds the abstract statistical concern in observable data and convincingly motivates the need for the conformal correction.

## Weaknesses

### Fatal
None.

### Major
- **The second contribution (OOD scores as nonconformity scores) is underdeveloped and insufficiently supported (Section 5).** The experiments use only one backbone (ResNet18), two datasets (CIFAR-10, CIFAR-100), and no error bars are reported for the OOD-based methods (std. dev. is reported only for the APS/RAPS baselines that involve random sampling). The transformation of OOD scores to class-conditional nonconformity scores via exponentiation + softmax (line 205) is introduced as a heuristic without any justification, ablation, or comparison to alternative adaptations (e.g., using the raw OOD score directly for the predicted class). The paper's own text says "all OOD scores are inefficient for CP" (line 209) but then claims they "can improve efficiency" (abstract) — this tension is never resolved. As a result, the second contribution reads more like a preliminary exploration than a validated finding, but it is presented as a co-equal contribution alongside the first.

- **The Limitations section omits the most important limitation.** Section 6 discusses data availability and compute resources but does not acknowledge that the OOD-scores-as-CP-scores experiments are exploratory, based on limited backbones and datasets, and may not generalize. Acknowledging this would make the paper more honest and help readers calibrate their trust in the second contribution.

### Minor
- **The paper does not analyze whether conformal metrics actually change method rankings.** It shows that conformal AUROC is 1–2% lower than classical AUROC, but does not examine whether the relative ordering of OOD methods changes. If rankings are preserved, the practical benefit is weaker; if they change, it would be a strong argument for adopting the correction. This is a missed opportunity to strengthen the first contribution's impact.

- **The choice of δ is not discussed or justified.** The paper uses δ=0.01 for OpenOOD and δ=0.05 for ADBench without explaining the rationale. Since δ controls the stringency of the conservativeness guarantee, some guidance (e.g., based on calibration set size or downstream risk tolerance) would improve usability.

- **Internal inconsistency in how the second contribution is framed.** Line 209 states "Table 5 shows that all OOD scores are inefficient for CP," but the abstract and conclusion claim OOD scores "can improve the efficiency" of CP. The body's "however" clause partially resolves this, but the blanket statement that OOD scores are "inefficient" is too strong and contradicts the more nuanced (and supported) finding that some OOD scores (KNN, Mahalanobis) sometimes outperform classical CP scores.

### Trivial
None.

## Nice-to-Haves
- A concrete safety-related example showing where the classical (uncorrected) metric leads to an overly optimistic threshold that violates the desired FPR in deployment, while the conformal correction avoids this.
- A comparison with bootstrap-based confidence intervals for AUROC to clarify why the CP-based correction is preferable to simpler statistical corrections.
- Testing the second contribution on more backbones (e.g., ResNet50, ViT) and larger datasets (e.g., ImageNet-200) to assess generalizability.
- Numerical tables for the ADBench results (Figure 3) to complement the scatter plots.

## Removed Points
These points are flagged to be removed — treat them with caution if reading the original reviews:

- **"Internal contradiction" between abstract and body (Harsh Critic).** The critic claimed the abstract says OOD scores "can improve efficiency" while the body says they are "inefficient," constituting a contradiction. The paper's body (line 209) says OOD scores are inefficient *as a general class* but then immediately notes that "some scores, like KNN or Mahalanobis, perform better than classical CP scores." This is a nuanced finding, not a contradiction. The abstract's "explore" and "can improve" are appropriately tentative. *Reason for removal: Criticism misunderstands the paper's nuanced framing.*

- **Claim that the abstract "overclaims" beyond evidence (Harsh Critic).** The abstract says "we explore using OOD scores... and show that they can improve efficiency." "Explore" and "can" are appropriately cautious. The conclusion says some OOD scores "are good candidates" — which is supported by Table 2 (KNN, Mahalanobis sometimes outperform). *Reason for removal: The paper's language is more measured than the critic asserts; the promotional tone is confined to the phrase "unlocking a whole avenue" which is mild hyperbole common in conclusions.*

- **Claim that the paper does not discuss i.i.d./exchangeability assumptions (Harsh Critic).** The paper explicitly states at line 76: "if the x_i are i.i.d and the distribution of s(x) under the ID law is continuous, we obtain marginally valid p-values." *Reason for removal: Factually incorrect — the assumption is stated.*

- **Table numbering inconsistency (Table 2 vs. Table 5).** The image caption says "Table 2" (line 203) but the body text references "Table 5" (line 209). This is a likely parser artifact from the PDF extraction. *Reason for removal: Formatting artifact, not a paper error.*

- **Strength Finder's claim of "statistical significance (mean ± std over 10 runs)" for OOD methods.** The paper explicitly states (line 207) that std. dev. is reported only for APS and RAPS. The OOD methods do not have reported error bars, so this claimed strength about statistical significance is factually inaccurate. *Reason for removal: Factually inaccurate about the paper's content.*

- **Harsh Critic's point about "no comparison with other finite-sample corrections for AUROC."** The paper's contribution is specifically adapting the CP-based correction to OOD metrics, not comparing all possible finite-sample corrections. This is scope creep. *Reason for removal: Demands the paper address a problem outside its stated scope.*

- **Harsh Critic's point about needing a user study or downstream task demonstration for the first contribution.** The paper's claim is about providing safer benchmarks with probabilistic guarantees — this is a methodological contribution validated on standard benchmarks. Demonstrating downstream impact is a nice-to-have, not a required weakness. *Reason for removal: Scope creep / nice-to-have elevated to a weakness.*

## Novel Insights
The Harsh Critic's most insightful observation is that the paper's two contributions are of very different strength, and this asymmetry creates a credibility problem when they are presented as co-equal. The paper would be stronger if it either removed or drastically downscaled the second contribution. This diagnosis is correct: the first contribution is a clean, well-executed methodological adaptation that stands on its own, while the second is a preliminary experiment that needs substantially more evidence. The most actionable synthesis is that the paper's core value is in the conformal metrics contribution, and the review should encourage the authors to either focus there or substantially expand the second part.

## Suggestions
1. **Resolve the asymmetry between the two contributions.** Either (a) remove the second contribution (or demote it to a brief "preliminary exploration" appendix), refocus the paper on conformal metrics for OOD, and soften any overreaching claims; or (b) substantially expand the second contribution with more backbones, datasets, error bars, alternative score transformations, and statistical significance tests — and adjust the claims to match the evidence.
2. **Add an analysis of whether conformal metrics change method rankings** on OpenOOD. This would directly demonstrate the practical value of the correction.
3. **Provide guidance on choosing δ** (the miscalibration tolerance) in practice, perhaps based on calibration set size or desired confidence level.
4. **Resolve the inconsistent framing** of the second contribution (line 209 vs. abstract/conclusion) — the blanket "all OOD scores are inefficient" statement should be replaced with a more precise characterization of the results.
5. **Add error bars** for the OOD-based methods in Table 2 and report results broken down by coverage level α.
