Now I have complete verification of all claims. Here is the final consolidated review.

---

## Summary

This paper introduces a method to enforce topological constraints (target contact ratios between touching objects, and minimum-distance constraints between gapped objects) in multi-part 3D reconstructions by refining latent-vector implicit SDF representations. The core idea is to sample random points, detect constraint violations via signed distances, and define loss functions that push/pull the implicit surfaces toward constraint compliance. Experiments on heart (5-chamber) and spine (L1–L5 vertebrae) reconstruction show substantial reductions in interpenetration and contact-ratio error compared to independent SDF fitting, especially on out-of-distribution data.

## Strengths

- **Unified handling of two fundamentally different topological constraints.** The same sampling-based framework enforces contact-ratio constraints (touching objects, heart chambers) and minimum-distance constraints (gapped objects, spine vertebrae) with near-identical loss formulations (Sec. 3.2 vs. 3.3). Prior work separately handles only intersection or containment, making this a genuine technical advance.

- **Monte Carlo estimation of contact ratio from implicit surfaces avoids costly mesh computations.** The stochastic approximation (Eq. 4) directly couples the constraint to the SDF parameterization, enabling gradient-based refinement without explicit surface extraction. The ablation (Tab. 3) confirms that both the contact and non-contact losses derived from this approximation are individually necessary.

- **Large quantitative gains on out-of-distribution test data.** On the private hospital (OOD) heart dataset, the method reduces average surface penetration from 88.21% (independent SDF fitting) to 5.46%, and contact-ratio error from 48.49% to 3.22%, while also improving Chamfer distance (stated in text, Sec. 4). These dramatic reductions on realistic, noisy medical images demonstrate the method's practical value.

- **Ablation study isolating each loss term.** Tab. 3 systematically drops each constraint loss individually; removing any single term causes a sharp increase in contact-ratio error (e.g., 48.10% without the contact loss, 29.36% without the non-contact loss), demonstrating each component's necessity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing "joint fitting without constraints" condition in ablation.** The ablation (Sec. 4) drops one loss term at a time but does not test the condition where *all* constraint losses (L_intersecting, L_contact, L_non-contact, L_min-distance) are removed simultaneously, leaving only the per-object data loss. While the data loss (Eq. 13) has no cross-object coupling term — so joint fitting without constraints is largely equivalent to independent fitting — a complete ablation would include this condition for rigorous attribution. (Note: the critic's claim that "joint optimization already encourages consistency across parts by tethering surfaces to shared SDF samples" is not supported by Eq. 13, where each object has its own independent sample set X_A and X_B.)

- **No statistical characterization of results.** Test sets are small (5 ID heart, 10 OOD heart, ~46 spine). No error bars, confidence intervals, or significance tests are reported for any metric. Given the method's dependence on randomized sampling and thresholding (ε, point count), variance could be non-trivial, and the reported numerical differences lack uncertainty quantification.

- **No sensitivity analysis of the Monte Carlo contact-ratio estimator.** Eq. (4) estimates contact ratio via indicator counts within an ε-band. The paper does not analyze bias or variance of this estimator as a function of ε or point count. While the empirical results implicitly validate the approximation, a direct comparison against ground-truth mesh-based computation (especially for thin or curved interfaces) would strengthen the methodology.

- **Mesh-based refinement baseline shown only qualitatively.** The explicit-mesh vertex-pushing alternative (Sec. 4, Fig. 8) is described and shown qualitatively but is not included in any quantitative table (Tabs. 1–3). Including it would strengthen the comparison and better demonstrate the advantage of the implicit approach.

- **Incomplete reporting of parallel-surface experiment.** The sentence introducing parallel-surface results cuts off at "The results are given in Tab." with no table reference or numbers provided. This experiment, while a useful demonstration of generality, cannot be evaluated in its current form.

### Trivial

- **Several hyperparameters (ε, λ weights, point count, resampling frequency) are listed but no guidance or sensitivity analysis is provided.** A brief discussion of how these were chosen would improve reproducibility.

## Nice-to-Haves

- A sensitivity analysis of the contact-ratio estimator (Eq. 4) over a range of ε values (e.g., 0.1–1.0 mm) and point counts (50K–500K) against mesh-computed ground truth.
- Error bars (±std or bootstrap confidence intervals) on all quantitative results, especially for the smaller test sets.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Joint optimization already encourages consistency across parts (e.g., by tethering surfaces to shared SDF samples)"** — Factually wrong. The data loss (Eq. 13) is per-object with independent sample sets X_A and X_B; there is no cross-object coupling. The mechanism the critic invokes does not exist in the paper.

2. **"Independent SDF row missing for heart OOD in Tab. 1"** — The text (line 200) explicitly states "Fitting an SDF to the individual parts greatly reduces the Chamfer distance error by a factor of more than 10," confirming that independent SDF numbers are reported (whether in the table or text). The critic's claim of omission is unsupported.

3. **"Ground-truth contact ratio for OOD dataset — how was it obtained?"** — This is a standard experimental question answered by the paper: contact ratios are pre-computed from training data (line 193). Questioning this without evidence is a reviewer knowledge gap.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a "joint without constraints" row to the ablation table** (all constraint losses removed, only L_data remains). Even if the result is similar to independent SDF fitting, it closes the experimental loop and preempts this criticism.

2. **Report means and standard deviations** for all metrics, or at minimum bootstrap-based confidence intervals.

3. **Add a brief sensitivity paragraph** for the MC estimator: show contact-ratio estimate as a function of ε for one representative case, compared to the mesh-computed ground truth.

4. **Complete the parallel-surface results** with a proper table or at minimum a sentence stating the quantitative outcome.

5. **Include the mesh baseline in Tab. 1 or Tab. 3** quantitatively (even if it performs worse), rather than only qualitatively in a figure.

## Score and Decision

The paper addresses a genuinely under-explored problem (enforcing contact-ratio and minimum-distance constraints in multi-part implicit reconstructions), proposes a clean and technically sound solution, and provides strong empirical evidence of large improvements on realistic medical data. The weaknesses are real but not fatal — they concern experimental completeness and reporting rigor rather than flaws in the core method. With reasonable revisions (completing the ablation, adding error bars, sensitivity analysis), the paper would be solid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>