Now let me write the final consolidated review.

## Summary

This paper proposes a novel method for crafting adversarial attacks that operate within a low-dimensional subspace of an image's transformed representation (DCT, DWT, or Glow) while simultaneously obeying the L∞ pixel-level constraint via a barrier method from nonlinear programming — avoiding the need for closed-form projections that are unavailable for nonlinear transforms. The authors demonstrate three instantiations, show that the resulting adversarial examples have lower LPIPS and L² distances than standard full-box attacks at the same L∞ budget, and report that adversarial training with the DWT subspace attack yields ~12% higher accuracy on CIFAR-10-C corruptions than standard L∞-box AT, with only a ~1.5% drop in natural accuracy.

## Strengths

1. **Technically novel attack formulation** — The combination of subspace constraints in a transformed representation with a barrier method to enforce L∞ pixel bounds is a genuine technical advance. Prior subspace attacks either ignored pixel bounds or required linearity for closed-form projection; this paper's approach works for any differentiable, invertible transform (including nonlinear flow-based models), which meaningfully expands the design space (Section 2.3, Eq. 8–9).

2. **Generality across three distinct transforms** — The method is instantiated with DCT, DWT, and Glow, showing it is not tied to a single representation (Section 3). This is non-trivial because the barrier method does not require the transform to be orthogonal or linear.

3. **Practically interesting corruption-robustness result** — Adversarial training under the DWT subspace constraint (S_dwt) yields 12.17% higher average accuracy on CIFAR-10-C than standard L∞-box AT, while natural accuracy drops only ~1.5% (Table 2). This is a substantial improvement that could be practically valuable, and it connects adversarial robustness with corruption robustness in a direction consistent with prior findings (Ford et al. 2019, Hendrycks & Dietterich 2019).

4. **Careful handling of the L∞ gradient discontinuity** — The paper replaces the L∞ norm constraint with 2n linear inequality constraints (Eq. 9) to avoid the spurious gradient of ∥·∥∞, which is a useful engineering detail for stable optimization.

5. **Sanity-check baseline** — Including a barrier method applied to the full L∞ box (no subspace) as a baseline confirms that the improved perceptual similarity arises from the subspace constraint, not from the optimizer change (Table 1, "barrier in pixel" column).

## Weaknesses

### Fatal
None.

### Major

1. **Attack similarity comparison conflates success rate and distortion** — Table 1 compares LPIPS and L² distances of subspace attacks against full-box attacks (PGD, APGD, Square) at the same ε. The subspace attacks inherently cannot reach the full L∞ boundary, so they naturally produce lower L²/LPIPS. Whether this is a free lunch or a valid comparison depends on the claim: within the same L∞ budget, subspace attacks indeed yield more similar examples. However, the caption does not clarify whether distances are averaged over all images or only successful attacks, and the paper does not report whether success rates are comparable across methods at each ε. If subspace attacks achieve lower success rates, the LPIPS comparison becomes confounded. A matched-distortion comparison (e.g., scaling ε for PGD to match the subspace attack's achieved L² or LPIPS) or a success-rate-vs-distortion trade-off curve would better support the central similarity claim. *This does not invalidate the paper's contribution but weakens the headline claim as currently presented.*

2. **Adversarial-training experiment lacks controls to isolate the subspace effect** — The AT comparison in Table 2 compares TRADES under a subspace attack vs. under standard PGD at T=10 for both. Several uncontrolled confounds make it difficult to attribute the corruption-robustness improvement to the subspace constraint:
   * The barrier method may not converge within 10 iterations, potentially producing weaker adversarial examples during AT independently of the subspace.
   * No baseline is included with a weaker full-box attack (e.g., PGD with fewer steps or smaller ε) to separate attack strength from the subspace constraint.
   * TRADES hyperparameters (β, step size) are not reported for either setting, so it is unclear whether the box AT baseline was reasonably tuned.
   * While the DWT-subspace model shows large gains, the Glow-subspace model performs nearly as poorly as the box model — this asymmetry is noted but not explained beyond speculation about "higher-level features." *The core result is promising but not yet convincingly isolated from confounds; additional controlled baselines are needed.*

### Minor

3. **Barrier method hyperparameters unreported** — The two critical hyperparameters μ (barrier parameter) and η (step size) are neither reported nor ablated. The paper says η should be "small enough" but gives no actual values or schedules. While code release is promised, the absence of these details undermines reproducibility and prevents readers from assessing the method's sensitivity to these choices.

4. **Split operator choices lack rationale and ablation** — For DCT, the split keeps "12 out of 64 luminance frequencies and 51 out of 64 chrominance frequencies," and for DWT, the downscaled image is treated as essential (p = n/4). No rationale or sensitivity analysis is provided for these choices. An ablation varying the retained coefficients would strengthen the empirical grounding.

5. **Missing details on attack evaluation** — Table 1 does not specify whether reported distances (L∞, L², LPIPS) are averaged over all attempted images or only successful attacks. This ambiguity matters because including failed attacks (where the distance is trivially zero or low) would artificially lower the reported distances for methods with lower success rates.

### Trivial

- Table 1 caption says "LIPS distance" instead of "LPIPS."
- The "barrier in pixel" baseline is noted in the text but not clearly marked in the table.
- The claim about projection being "practically unfeasible" for q≥2 could acknowledge that for linear transforms (DCT, DWT) a quadratic program is feasible, albeit expensive.

## Nice-to-Haves

- Include a matched-distortion comparison where PGD's ε is scaled to match the subspace attack's achieved L² or LPIPS, and report success rates at matched distortion.
- Add an AT baseline using a weaker full-box PGD (e.g., fewer steps, or PGD with a smaller ε that achieves similar L² to the subspace attack) to decouple subspace constraint from attack strength.
- Report μ, η values and an ablation over μ showing constraint satisfaction vs. attack success.
- For DCT and DWT, vary the number of retained coefficients and report the effect on attack success, LPIPS, and AT corruption robustness.

## Removed Points

- **"Projection overstatement" (Section 2.2):** The harsh critic claimed the paper overstates the feasibility of projection for linear transforms. The paper says "practically unfeasible" which is accurate given the expensive nature of QP for high-dimensional polytopes. Removed as an overly pedantic point.
- **"Newton vs. first-order justification" (Section 2.3):** The paper explicitly states they "opt for a fast first-order update rule, which we found more practical in our setting." A design choice adequately justified. Removed.
- **"Missing comparison with Luo et al./Wang et al." (Related work):** Those works use similarity distances in the optimization objective, which is a different approach from enforcing subspace + L∞ constraints. Not a required comparison. Removed.
- **Generic strengths** from the Strength Finder that lack specific evidence were dropped.
- Various formatting/style nitpicks, missing related work suggestions, and reproducibility nitpicks about large artifacts were removed per policy.
- The strength about "barrier method in pixel domain sanity check" and "handling of L∞ gradient discontinuity" are retained but classified as minor supporting strengths rather than core strengths.

## Novel Insights

The most novel observation from the reviews is the tension between the paper's two central claims (greater similarity and improved corruption robustness). The similarity claim relies on the fact that subspace attacks cannot fully exploit the L∞ budget, but if the subspace constraint also makes the attacks weaker (lower success rate, harder to converge), then the corruption-robustness improvement could be partially explained by weaker adversaries during training rather than the meaningfulness of the subspace. The paper does not disentangle these explanations, and resolving this would strengthen both claims substantially — but doing so requires controlled experiments (matched-distortion comparison, weaker-box AT baseline) that the paper currently lacks.

## Suggestions

1. Add a matched-distortion experiment: scale ε for PGD so that its achieved average L² matches the subspace attack, then compare LPIPS and success rates. This directly addresses the main concern about the similarity claim.
2. Include a weaker PGD AT baseline (e.g., PGD with fewer steps or a smaller ε that replicates the subspace attack's average L²) and show that its corruption robustness is worse than the subspace AT, thereby isolating the subspace effect.
3. Report μ and η values, and add a brief ablation showing how varying μ affects constraint satisfaction, attack success rate, and LPIPS at a fixed iteration budget.
4. Clarify in Table 1 whether distances are computed over all inputs or only successful attacks. If the latter, also report the success rate per method.
5. Add a brief ablation for the DCT split (e.g., varying the number of retained frequencies) to show how the choice affects attack quality and AT outcome.

## Score and Decision

I performed calibration_search with queries covering topics related to this paper (subspace adversarial attacks, corruption robustness, perceptual similarity) and score bands. Below are the retrieved anchors with their paths, avg human scores, and a one-sentence comparison to the paper under review.

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WVzYMa68Of.md` | 3.50 | Low-scoring; narrow-scope black-box attack paper with unclear motivation — our paper has stronger novelty and broader scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fiTpna7fO5.md` | 3.25 | Low-scoring; weak claims about multi-attacks with limited practical significance — our paper has a more focused contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7GCRhebJEr.md` | 5.00 | Medium-scoring; Bregman-divergence robustness paper with split reviewer opinions (8,6,3,3) — similar to our paper in having a novel core idea but receiving mixed assessments about experimental rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fjwZHuQ3cm.md` | 5.50 | Medium-scoring; LIMANS paper on adversarial noise space modeling, rejected due to conflicting results and methodological concerns — our paper has a similar level of novelty but fewer conflicting results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pE6gWrASQm.md` | 6.50 | Medium-high; clean empirical study on subset AT, accepted — our paper has comparable novelty but less rigorous experimental controls. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IGzaH538fz.md` | 8.00 | High-scoring; deterministic certification for GNNs with clean proofs and strong claims — far more rigorous than our paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I5lcjmFmlc.md` | 8.00 | High-scoring; diffusion-based robust classifier with thorough evaluation — rejected despite high scores, reflecting extremely high bar. |

The paper under review sits between the medium-scoring anchors (5.00–5.50) and the stronger empirical study (6.50). Its core technical idea is genuinely novel and the corruption-robustness result is practically interesting. However, the experimental validation has gaps: the main similarity claim needs a controlled comparison (matched distortion), the AT experiment needs to isolate the subspace effect from attack weakness, and key hyperparameters are unreported. These are not fatal — they are addressable with additional experiments — but they weaken the current form. Relative to the anchors, the paper is stronger than the 3–4 range papers (which have fundamental issues) and comparable to or slightly stronger than the 5.00–5.50 papers, but not yet at the 6.50 level of the accepted AT subset paper.

**Score: 5.5**

**Decision: Reject** — The paper has a novel and promising core idea with an interesting corruption-robustness result, but the experimental validation in its current form does not convincingly support the headline claims. The flaws are addressable with additional controlled experiments, and a revised version could be a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>