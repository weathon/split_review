Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces a sampling-based method to enforce topological constraints (contact ratios and minimum distances) between components of composite 3D objects represented as deep implicit signed distance functions. The approach samples random points in the volume, identifies topologically meaningful subsets (contact, intersection, violation points) via signed distance checks, and jointly refines the latent vectors of the SDFs using custom loss functions. It is demonstrated on two medical tasks: whole-heart reconstruction (enforcing contact ratios between chambers) and lumbar spine reconstruction (enforcing a minimum gap between vertebrae).

---

## Strengths

1. **Novel Monte Carlo formulation for enforcing non-local topological constraints via implicit functions.** The paper introduces a method to compute and enforce contact ratios between implicit surfaces by counting uniformly sampled points near each surface (Eq. 2, Section 3.2.1). This enables constraints that are inherently non-local (contact ratio, gap) to be checked and optimized, which existing local-patch or intersection-penalty approaches cannot handle (Section 1, related work). The idea of reading and adjusting implicit surface relationships through random sampling is creative and practically useful.

2. **Unified framework handles two fundamentally different constraints with the same machinery.** The same sampling-based pipeline enforces both contact ratios (heart chambers, Section 3.2) and minimum distances (spine vertebrae, Section 3.3). The only difference is the selection of topologically meaningful points and the loss function (Eq. 1 vs. Eq. 4). This generality is demonstrated on two distinct medical reconstruction tasks with different geometric requirements.

3. **Demonstrated quantitative improvement over independent SDF fitting.** The method substantially reduces topological errors compared to fitting SDFs independently. The ablation study (Tab. 5) confirms that each loss component (intersection, contact, non-contact, data) contributes to the overall performance, and omitting any term degrades results. A mesh-based alternative is discussed and shown qualitatively to produce rougher surfaces, further motivating the implicit approach.

4. **The method is shown to extend beyond the two main constraints.** The parallel-surface experiment (Section 4.3) demonstrates that the framework can handle interval constraints (both a minimum and maximum distance), suggesting broader applicability.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline — joint SDF fitting without constraint losses.** The paper compares against "independent SDF fitting" (fitting each part separately), but not against *joint* SDF fitting with data loss only and no constraint losses. The SDF auto-decoder is trained on ~100 heart volumes, while nn-UNet is trained on only 15 images. The paper acknowledges this disparity ("Fitting an SDF to the individual parts greatly reduces the Chamfer distance error by a factor of more than 10 because the latent vector model imposes priors on the noisy data"), but this means the strong SDF prior is a confound that could explain some of the improvement. The marginal gain from constraints on Chamfer distance is small (e.g., 1.1→0.8 in the OOD heart case). The main evidence for the constraints' value therefore rests on topological metrics (contact ratio error, penetration), but without a "joint SDF + data loss only" baseline, it is unclear how much of the topological improvement comes from joint refinement (which could naturally reduce penetration by coordinating shapes) versus the constraint-specific losses. The ablation study partially addresses this (Tab. 5 shows each loss component matters), but it is limited to one pair (LV–M-LV) on 10 OOD images, and the "no contact loss" / "no non-contact loss" variants are not the same as a clean "joint fitting, no constraints" baseline.

2. **OOD evaluation conflates constraint enforcement with prior correctness.** The contact ratio prior is computed from the (in-distribution) training data. For the OOD heart dataset, the ground-truth contact ratio is computed from manual segmentations of those same OOD subjects. If the OOD subjects have systematically different anatomy (e.g., due to pathology), forcing the training prior could produce anatomically incorrect results. The reported contact ratio error (e.g., 4.1%) conflates two things: (a) how well the method enforces the prior, and (b) how appropriate the prior is for that subject. The paper should report the variance of contact ratios within the training set to justify applying a single prior to all cases, and discuss the limitation that the method may enforce a wrong prior on pathological cases.

3. **The contact ratio enforcement formulation lacks convergence analysis and synthetic validation.** The method decouples the contact ratio into a fixed target count \(N_{\text{contact}}\) based on the current denominator, then classifies points into \(\mathcal{A}_{\text{contact}}\) and \(\mathcal{A}_{\text{non-contact}}\), and applies opposing losses. The iterative resampling (every 10 iterations) is heuristic, with no theoretical bound on how closely the final contact ratio matches the target. The paper would be substantially strengthened by a synthetic experiment with simple primitives (e.g., a sphere and a plane) where the ground-truth contact ratio is known, to verify that the optimization reliably achieves the intended ratio within a known tolerance. Without this, the reader cannot assess whether the method reliably enforces the constraint or merely nudges shapes in a plausible direction.

### Minor

1. **Reproducibility gaps.** Several hyperparameters are missing: the threshold \(\epsilon\) (contact distance) is defined but never given a numerical value; the loss weights \((\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) are stated to exist but not reported; the learning rate, number of optimization iterations, and optimizer choice are not specified. These details are essential for reproducing the results.

2. **Spine constraint inconsistency and missing pixel spacing.** The method section states the minimum gap as "1 mm" (citing Little 2005), while the experiment section says "1 pixel." The pixel spacing (which determines the physical meaning of "1 pixel") is not reported, nor is it explained how "1 pixel" relates to the cited 1 mm clinical standard. Without this, the constraint's clinical relevance and the interpretability of the reported contact areas (px²) are unclear.

3. **Ablation study is limited in scope.** The ablation (Tab. 5) is conducted on only one pair (LV–M-LV) on the OOD set (10 images) with no statistical significance reported. While the results are suggestive, a more thorough ablation across multiple pairs and datasets would strengthen confidence in the necessity of each loss term. Additionally, while the paper says it measures "both topological error and reconstruction errors" in the ablation, explicitly reporting contact ratio error and penetration percentage (not just Chamfer distance) for each ablated variant would more directly support the main claim about constraint enforcement.

4. **Parallel surface experiment is sparsely described.** The experiment is presented in three sentences that describe the setup, but the quantitative results are deferred to a table (likely in the appendix, which is stripped from this version). The qualitative description is insufficient to assess the method's effectiveness on this third scenario. If the table exists in the full submission, this is less of an issue, but the main text explanation should still be expanded for readability.

5. **The contact ratio loss landscape is not empirically examined.** The paper notes that minimizing \(|f_A + f_B|\) over \(\mathcal{A}_{\text{contact}}\) encourages \(f_A \approx -f_B\), and that "this case, objects A and B are equidistant to the anchor point x, which must reside within at most one of them, or precisely on the surface of both." This analysis is correct but leaves open the question of what happens when the optimization converges to configurations where the point is between the surfaces (e.g., 1 mm outside A, 1 mm inside B) rather than at the intersection of both surfaces. While the data loss constrains this, a brief empirical analysis or discussion would clarify the behavior.

### Trivial
None.

---

## Nice-to-Haves

- A synthetic validation experiment with simple primitives (e.g., sphere-plane with known contact ratio) to verify the optimization's convergence properties.
- Reporting the variance of contact ratios across the training set to justify the single-prior assumption.
- If the pixel spacing for the spine dataset is known, converting the "1 pixel" constraint to physical units to match the clinical reference.
- A brief analysis or visualization showing how the contact ratio evolves during optimization.

---

## Removed Points

These points from the reviews were removed with brief justifications:

- *"The large reduction in Chamfer distance (by a factor of 10+) relative to raw nn-UNet output is expected and has nothing to do with constraint enforcement."* — The paper explicitly acknowledges this: "Fitting an SDF to the individual parts greatly reduces the Chamfer distance error by a factor of more than 10 because the latent vector model imposes priors on the noisy data." The criticism restates what the paper already says.

- *"The marginal gain from constraints on Chamfer is small (0.3), so the improvement on Chamfer is not strong evidence for the constraints' value."* — The constraints are evaluated on topological metrics (contact ratio error, penetration), not Chamfer distance. Chamfer is a reconstruction quality metric, not the primary evidence for constraint enforcement.

- *"The phrase 'refining 3D segmentations obtained from the nn-UNet architecture' is accurate, but the abstract does not mention that the SDF models are trained on a much larger set."* — The abstract is inherently brief; the training details are in the experiment section where they belong.

- *"The ablation table reports Chamfer distance, but the main claim is about constraints, so the ablation should also report contact ratio error and penetration."* — The paper states the ablation measures "both topological error and reconstruction errors." The table content is not fully visible in the extracted text, but the text indicates topological metrics are included.

- *"Minimizing |f_A + f_B| over A_contact... could be achieved when the point is on the surface of one object and inside the other—this may not correspond to both surfaces being at the same point."* — The paper's analysis (Section 3.2.2) explains that when \(f_A = -f_B\), the point is equidistant to both surfaces and "must reside within at most one of them, or precisely on the surface of both." This is a correct description of what the loss achieves, and the data loss provides additional constraints.

- *"The parallel surface experiment defers quantitative results to Tab. 5 (which is stripped—likely in appendix)."* — The parser strips appendix content; the table exists in the original submission. Kept a weakened version as Minor #4 about the main text being sparse.

- *"nn-Unet struggles to generalize to out-of-training-distribution heart images is effectively a restatement of the experiment design; the reason (only 15 training images for nn-UNet) should be stated explicitly."* — The paper states both facts (nn-UNet trained on 15 images, SDF on ~100) in Section 4. The reader can connect them.

---

## Novel Insights

The reviews surface a key tension that the paper does not fully resolve: the method's effectiveness depends on both the SDF shape prior (which provides smooth, regularized surfaces) and the constraint losses (which enforce the specific topological relationship). Separating these two effects is inherently difficult when the SDF model requires more training data than the segmentation model. The most interesting open question is whether the contact ratio loss actually *converges* to the specified ratio, or whether it simply biases the shape in a plausible direction — and this cannot be answered without a controlled synthetic experiment. The reviews collectively suggest that the paper's core technical contribution (sampling-based constraint enforcement via implicit functions) is sound and promising, but the experimental evidence is weaker than the claims warrant due to the confounded setup and missing baseline.

---

## Suggestions

1. **Add the missing baseline:** Joint SDF fitting with data loss only, no constraint losses, across all test cases. If the constraint losses still improve topological metrics relative to this baseline, the contribution is cleanly demonstrated.
2. **Run a synthetic validation experiment** with two simple geometric primitives (e.g., sphere and plane, or two cubes) where the ground-truth contact ratio is analytically known. Initialize the SDF with wrong shapes and measure how closely the optimization recovers the target ratio.
3. **Report all missing hyperparameters:** \(\epsilon\), \(\lambda_1\)–\(\lambda_4\), learning rate, optimizer, number of iterations.
4. **For the spine experiment,** reconcile the "1 mm" vs "1 pixel" inconsistency and report the voxel spacing.
5. **Report the variance of contact ratios** across the training set to support the use of a single prior, and discuss the limitation regarding pathological OOD cases.

---

## Score and Decision

This paper tackles an important and understudied problem with a creative and technically sound approach. The core idea — using Monte Carlo sampling over implicit functions to read and enforce non-local topological constraints — is novel and potentially impactful. However, the experimental evaluation has a significant gap: the absence of a "joint SDF fitting without constraints" baseline makes it hard to attribute the observed improvements to the constraint losses versus the joint refinement and strong SDF prior. The contact ratio loss also lacks convergence analysis or synthetic validation. These weaknesses are substantial but addressable; they do not invalidate the contribution but weaken the evidence for it.

**Score: 5.5 / 10**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>