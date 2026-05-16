Now I have a thorough understanding of the paper and can cross-check the reviewer claims. Let me compose the consolidated review.

## Summary

The paper presents TapMo, a text-driven animation pipeline for skeleton-free 3D characters. It combines a Mesh Handle Predictor (which adaptively assigns control handles via a GCN) with a Shape-aware Motion Diffusion module that generates both handle motion and mesh-specific adaptations conditioned on mesh deformation features. The method is trained with a weakly-supervised strategy to handle the scarcity of ground-truth motion data for non-rigged characters. The core technical contributions are the handle-based universal motion representation, the mesh-conditioned diffusion that produces per-character adaptations, and the combination of spring loss and adversarial loss for mesh-specific motion learning.

## Strengths

- **First end-to-end pipeline for text-driven animation of skeleton-free characters.** The paper identifies and addresses a genuine gap: prior motion-generation methods assume pre-rigged SMPL humans, limiting applicability to diverse non-rigged 3D models. TapMo handles heterogeneous meshes (humanoid and non-humanoid) directly from text descriptions (Section 1, contribution bullet 1).

- **Mesh-specific adaptation drastically improves geometric integrity.** The key quantitative result is in Table 2: TapMo achieves ARAP-Loss of 0.271 on seen characters versus 0.897 (MDM-SR) and 1.006 (MDM-SFR)—reductions of ~70–73%. On unseen characters, the advantage is similar (0.329 vs. 0.787/0.910). The user study confirms this: over 84% of 1,335 pairwise rankings prefer TapMo's animations (Figure 6).

- **Weakly-supervised training enables generalization beyond available data.** The use of Spring Loss (Eq. 10, penalizing bone-length changes) and Adversarial Loss (Eq. 11, aligning generated motions with skeleton-driven priors) allows the model to learn shape-aware behavior without ground-truth motion data for non-human characters. Ablations in Table 2 show each loss component contributes positively.

- **The internal comparison of diffusion architectures is clean and informative.** TapMo (MDM) vs. TapMo (Ours) in Table 1 is a valid within-space comparison showing the multi-token CLIP + Transformer Decoder yield real improvements (FID 1.058 → 0.515, R-Precision Top-1 0.498 → 0.542).

- **Root handle prediction is a practical improvement over SfPT.** Fixing the first handle as the character's root (Eq. 6) enables global motion control, which SfPT lacks and which causes mesh distortion in prior skeleton-free approaches (Section 3.1).

## Weaknesses

### Fatal
None.

### Major

- **Table 1's cross-space comparison of motion quality metrics is invalid and undermines a stated claim.** The paper compares TapMo (measured in a retrained feature space, "Real†") against baselines T2G, Hier, TEMOS, T2M, MDM (measured in the original HumanML3D feature space, "Real"). Because the metrics (R-Precision, FID, Diversity, Multimodal Dist) all depend on the embedding space, and the two spaces produce different baseline distributions (e.g., R-Precision Real: 0.511 vs. Real†: 0.559; Diversity Real: 9.503 vs. Real†: 17.176), comparing TapMo's metrics to baselines' metrics is apples-to-oranges. The paper's claim that "TapMo outperforms previous models significantly in terms of both R-Precision and FID metrics" (line 215) rests on this comparison and is not supported. This does not invalidate the paper's core contribution (shape-aware animation of skeleton-free characters), but the paper should either (a) convert all methods to a common evaluation space, (b) restrict the HumanML3D comparison to the valid within-space rows (TapMo-MDM vs. TapMo-Ours), or (c) reframe the claim to reflect that the primary motion-quality evidence comes from geometry metrics and the user study rather than this table.

### Minor

- **Skinning Loss (L_s) and Pose Loss (L_p) are introduced but never defined.** The paper states (line 92) that three losses are used for adaptive handle learning—Skinning Loss L_s, Pose Loss L_p, and Root Loss L_r—but only Root Loss is specified (Eq. 6). Eq. 8 includes L_s and L_p in the training objective, so their absence prevents reproducibility of the handle predictor. (These may be inherited from SfPT [Liao et al., 2022], but the paper should state this explicitly.)

- **No direct evidence that the mesh deformation feature f_φ actually drives shape-aware behavior, as opposed to the adaptation δ doing all the work.** The paper shows that the adaptation δ improves geometry (Table 2: w/o δ vs. full model), but the mesh deformation feature f_φ conditions both the base motion x̂₀ and the adaptation δ̂. A straightforward ablation—swapping the mesh feature between different characters (e.g., cat mesh feature with a human motion description) or removing f_φ entirely—would demonstrate that the model genuinely uses shape information. Without this, it is unclear whether f_φ is meaningfully influencing generation or whether the weak losses are merely regularizing the output space.

- **Handle-FID metric uses only two SMPL models to estimate a distribution.** The paper states (line 189) that "two SMPL human models that vary significantly in body size" are used. FID is a distributional metric that typically requires a much larger sample for reliable estimation; two data points are insufficient to characterize a distribution. The Handle-FID values should be interpreted with caution.

- **The improvement from adaptation fine-tuning (w/o δ ft → Ours) is marginal on unseen characters.** ARAP-Loss on unseen characters goes from 0.335 to 0.329 (Table 2), a relative improvement of ~1.8%. On seen characters the improvement is more meaningful (0.301 → 0.271, ~10%), but the unseen gap is small enough that significance is unclear. No confidence intervals or statistical tests are reported for Table 2.

- **Several implementation details are underspecified.** (a) The number of handles K is introduced (line 82) but never discussed—how K is chosen, whether it varies per mesh, and its impact on expressiveness vs. cost are not addressed. (b) The adversarial loss (Eq. 11) requires "skeleton-driven mesh motions" p(V̄ˢᵏ) as real samples; how these are obtained for non-SMPL characters is not explained—does this require rigging each mesh with a skeleton? (c) Dataset splits for Mixamo and ModelsResource-RigNet (how many characters, seen vs. unseen partition) are not specified.

- **Spring Loss exponential weight (Eq. 10) is presented without motivation.** The term e^{-(E(hᵢ⁰, hⱼ⁰) + σ)} assigns smaller weights to larger rest-pose distances, meaning shorter edges are penalized more for length changes. The paper calls this an "adaptive spring coefficient" (line 137) but does not justify why shorter edges should be more heavily regularized—a plausible alternative is that longer limbs could tolerate larger absolute errors. The design choice should be explained or empirically motivated.

### Trivial
None worth enumerating beyond the missing loss definitions already listed under Minor.

## Nice-to-Haves
- A failure-case / limitations section discussing physical violations (foot sliding, self-penetration, inter-penetration) would strengthen the paper.
- Statistical significance tests or confidence intervals for Table 2 would clarify whether the fine-tuning improvements are reliable.
- An analysis of handle consistency across meshes (e.g., does handle index 3 always correspond to the left arm?) would strengthen the claim of "universal motion representation."

## Removed Points

These points are flagged for removal; treat them with caution:

- **Criticism that the weakly-supervised training "may not achieve its stated goal" because there's "no analysis of how the model's behavior changes when the mesh feature is ablated or swapped."** This was downgraded from the critic's framing as a "structural flaw" to a Minor weakness. The paper does provide evidence that the mesh-specific adaptation δ (which is conditioned on f_φ) improves geometry quantitatively (Table 2: w/o δ 0.310 → Ours 0.271) and qualitatively (Figure 4). The criticism that the paper lacks a direct feature-swap or feature-ablation test is valid but partial—the existing ablation shows the adaptation pipeline works, just not the specific isolation test the critic demands. Kept as Minor, not Fatal.

- **Criticism about the Spring Loss (Eq. 10) being "unclear" and suggesting the opposite weighting might be desirable.** This is a design choice, not a flaw. The paper provides the motivation ("adaptive spring coefficient," line 137). The critic's alternative preference does not make the paper wrong. Moved to Minor with weakened framing.

- **"No failure cases or limitations"** — downgraded to Nice-to-Have, as this is a standard paper-length constraint, not a flaw.

- **Strength Finder's claim that "TapMo achieves superior performance on both motion quality (Table 1: FID 0.515 vs. 0.544 for MDM)"** — this conflicts with the verified weakness that the comparison across feature spaces is invalid. The in-space comparison (TapMo-MDM vs. TapMo-Ours, FID 1.058 vs. 0.515) is valid and is preserved as a distinct strength.

- **Strength Finder's "Strong empirical validation across multiple metrics"** — generic framing. The specific geometry and user study results are preserved as individual strengths above.

- **"Quantitative generalization to unseen characters"** from Strength Finder overlaps substantially with existing strengths; merged.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the paper attempts to serve two masters simultaneously—demonstrating competitive motion quality on standard benchmarks (HumanML3D) and demonstrating shape-aware adaptation on novel characters—and the evaluation for the first goal is methodologically compromised. This tension between benchmarking against skeleton-based methods (where the comparison is apples-to-oranges) and demonstrating the core skeleton-free contribution (where the baselines are appropriate but limited) is a recurring pattern in papers that open a new problem setting. The lesson is that when a paper introduces a fundamentally different representation (handles vs. skeletons), the default evaluation framework of the old representation cannot be straightforwardly reused, and the paper would benefit from acknowledging this asymmetry and leaning harder on task-specific evaluation (geometry metrics, user studies) rather than attempting direct numerical comparisons on legacy benchmarks.

## Suggestions

1. **Fix the evaluation framing for Table 1.** Either (a) convert all baselines' outputs into the handle representation and evaluate everything in the retrained feature space (making for a fair comparison), or (b) explicitly relegate the Table 1 comparison to an internal architecture ablation (TapMo-MDM vs. TapMo-Ours) and remove cross-space claims, while defending motion quality primarily with geometry metrics (Table 2) and the user study.

2. **Define L_s and L_p.** Even a one-sentence reference to SfPT's loss formulation would resolve the reproducibility gap.

3. **Add a mesh-feature ablation experiment.** Show generations where the mesh feature is removed or swapped across characters to directly demonstrate that f_φ influences output. This would significantly strengthen the core claim of shape-awareness.

4. **Clarify how skeleton-driven mesh motions are obtained for the adversarial discriminator** and how K (number of handles) is chosen.

5. **Report error bars or significance tests for Table 2** to assess the reliability of the fine-tuning improvements.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>