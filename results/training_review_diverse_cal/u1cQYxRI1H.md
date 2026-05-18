Here is my synthesized final review.

---

## Summary

This paper proposes IC-Light, a method for scaling up training of diffusion-based illumination editing models by imposing a "light transport consistency" loss. The loss regularizes the diffusion model so that its predictions under composited illumination are consistent with predictions under separate illuminations, rooted in the physical principle that light transport is linear. The paper demonstrates training on >10M samples from multiple data sources (3D renderings, light stage captures, and in-the-wild augmented images) using strong backbones (SD 1.5, SDXL, Flux). The main contribution is enabling stable large-scale training that preserves intrinsic image properties (albedo, details) while modifying illumination. Ablations show performance drops when either the consistency loss or the augmented data is removed, and quantitative results on a held-out 3D rendering test set show competitive LPIPS scores.

## Strengths

1. **Empirically effective consistency regularization.** The ablation study (Section 4.2, Fig. 4) shows that removing the consistency loss causes visible degradation: color saturation shifts, loss of albedo details, and "red and blue differences vanished." This provides compelling evidence that the loss preserves intrinsic properties during illumination editing, serving its practical purpose even if the theoretical framing via the MLP φ is approximate rather than exact.

2. **Large-scale data engineering with diverse sources.** The paper details a substantial data pipeline spanning 6M in-the-wild augmented images, 4M Objaverse renderings, and light stage captures. The scheduled probability balancing across data sources (Section 4.1) and the use of multiple albedo/normal/shadow synthesis methods represent a non-trivial engineering effort that directly enables the claimed scalability.

3. **Demonstrated versatility across backbones and downstream tasks.** The method is shown to work with SD 1.5, SDXL, and Flux backbones, and the paper demonstrates additional applications including background-conditioned harmonization and normal map inference from multiple consistent relightings. The normal map extraction (Section 4.3, Eqs. 7–9) is a clever side benefit that leverages the model's cross-illumination consistency.

## Weaknesses

### Fatal

None.

### Major

1. **Quantitative evaluation is limited to synthetic 3D renderings from the same distribution as training.** Table 1 evaluates on 50k unseen Objaverse renderings sharing the same rendering pipeline and object categories. Despite the paper's framing around "in-the-wild" generalization and practical deployment, no quantitative evaluation is provided on real photographs (e.g., Multi-Illumination dataset, light-stage captures of real objects with ground-truth relighting). The qualitative comparisons in Fig. 6 are helpful but cherry-picked examples do not substitute for a controlled real-world benchmark. This gap substantially weakens the claim that the method generalizes to genuine in-the-wild scenarios.

2. **The consistency loss uses a learned MLP φ as an adapter, which weakens the physical grounding claimed for the method.** The paper derives linearity in raw HDR space (Eqs. 2–3) but then acknowledges that "most diffusion models are not pixel diffusion models trained on HDR images" and introduces a 5-layer MLP φ to "learn an implicit adaptation" between latent-domain predictions. The actual loss is ∥ε_{L₁+L₂} − φ(ε_{L₁}, ε_{L₂})∥² rather than the direct sum. While the paper is transparent about this, it never verifies that decoded outputs satisfy I_{L₁+L₂} ≈ I_{L₁} + I_{L₂} in image space — the central physical claim. Without this verification, the loss is better described as a learned compositional regularizer than an imposition of physical light transport. The ablation shows the loss helps empirically, but its mechanism is unclear.

3. **No quantitative comparison for the normal map application.** The paper claims normal maps are "higher quality for human than alternatives GeoWizard and DSINE" (Section 4.5) but provides no quantitative angular error metrics. This is a significant omission for a claimed additional application, especially since GeoWizard and DSINE are dedicated normal estimators with established benchmarks.

### Minor

1. **The paper mentions "reducing uncertainties" (abstract, conclusion) but never defines or measures uncertainty.** This is a recurring rhetorical claim without any operationalization.

2. **The individual components of the complex augmentation pipeline (6 albedo methods, 3 normal methods, shadow materials, specular synthesis, CLIP filtering) are not ablated.** The ablation removes the entire "w/o aug data" block, but this confounds dataset size with the specific physical-plausibility design choices. Simpler augmentations (random color jitter, brightness) are not compared, leaving open whether the massive pipeline engineering is necessary.

3. **Training cost implications are not discussed.** The consistency loss requires three forward passes per sample (L₁, L₂, L₁+L₂), tripling the per-iteration compute relative to the vanilla objective without this being reported or acknowledged.

### Trivial

- The comparison of normal maps to GeoWizard/DSINE is on uneven footing (ad-hoc method vs. dedicated estimators). The paper acknowledges this in Section 4.3 ("this normal extraction is an empirical method since the neural models are not optimized to approximate light stage ground truths or 3D normal maps"), but the claim of "higher quality" in Section 4.5 still overstates without quantitative backing.

## Nice-to-Haves

- Verify the consistency property in decoded image space: decode predictions for L₁, L₂, L₁+L₂ and compute ∥I_{L₁+L₂} − (I_{L₁} + I_{L₂})∥, comparing with/without the consistency loss. This would directly substantiate the physical claim.
- Evaluate on a real-image relighting benchmark (e.g., Multi-Illumination dataset) with quantitative metrics.
- Replace the MLP φ with a fixed sum (φ(x,y)=x+y) to test whether the linearity holds approximately in latent space already, or whether the adapter is essential.
- A limitation paragraph discussing failure cases (inter-reflections, caustics, subsurface scattering where light transport is more complex).

## Removed Points

- *"The paper does not analyze the contribution of each component... the drop could be due to dataset size reduction rather than the specific physical plausibility."* — Kept in weakened form under Minor 2. The paper does ablate the full pipeline vs. no pipeline, which is a valid comparison; the "dataset size reduction" framing ignores that the w/o-consistency ablation keeps the same data and shows degradation. The remaining concern about sub-component ablation is fair.
- *"The training cost of the consistency loss is not discussed... triples the inference cost."* — The critic incorrectly says "inference cost" is tripled; it is training cost that is tripled. Inference is unchanged since the consistency loss is only applied during training. Kept in corrected form under Minor 3.
- Strength Finder strength about "physically grounded light-transport consistency loss" — Partially conflicts with Major Weakness 2 (the φ adapter weakens the physical grounding). Kept with the caveat that the physical grounding is approximate, since the empirical ablation independently supports the loss's usefulness.

## Novel Insights

The harsh critic's observation that the MLP φ can absorb arbitrary non-linearities, combined with the missing verification in image space, points to a broader pattern in generative model research: physically-motivated losses are increasingly applied in learned latent spaces where the original physical invariants do not directly hold, and learned adapters (like φ) bridge the gap. This paper is a clear case study — the adapters make training tractable but also make it difficult to know whether the physical principle is being enforced or merely approximated. The community would benefit from a convention of verifying physical losses in the original physical domain (e.g., decoded pixel space) even when training occurs in a latent space. None beyond this observation emerges from the reviews.

## Suggestions

1. Add quantitative evaluation on at least one real-image relighting benchmark before claiming "in-the-wild" generalization.
2. Decode the consistency-loss predictions for L₁, L₂, L₁+L₂ and report image-space linearity error (e.g., PSNR between decoded I_{L₁+L₂} and decoded I_{L₁} + I_{L₂}) to substantiate the physical claim.
3. Report the angular error for normal maps against ground-truth normals (e.g., from 3D renderings in the test set) to quantitatively support the qualitative normal map claims.
4. Include a brief limitations paragraph addressing cases where the linear light transport assumption may break down (e.g., inter-reflections, translucent materials).
5. Report training GPU-hours and training wall time for the vanilla vs. full method to help readers assess the practical cost of the consistency loss.

## Score and Decision

This paper presents an interesting and practically-motivated approach with a substantial engineering effort, and the ablation convincingly shows that the consistency loss helps empirically. However, the two major weaknesses — (1) no real-image quantitative evaluation despite "in-the-wild" framing, and (2) unverified physical grounding due to the learned MLP adapter — prevent the paper from meeting its own claims in the current form. The core contribution is promising but insufficiently validated.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>