Now I have all the information needed to write a thorough, verified review. Let me synthesize everything.

## Summary
This paper introduces TapMo, a text-driven animation pipeline for generating motion on skeleton-free 3D characters (i.e., meshes without pre-rigged skeletons). The method has two components: (1) a Mesh Handle Predictor that learns adaptive control handles and skinning weights across heterogeneous meshes, and (2) a Shape-aware Motion Diffusion model that generates text-guided motion together with mesh-specific geometric adaptations in a weakly-supervised manner, preserving the character's shape during animation.

## Strengths
- **First text-driven pipeline explicitly targeting skeleton-free characters.** Prior motion generation (MDM, T2M, TEMOS) requires pre-rigged SMPL models; auto-rigging methods produce inconsistent skeletons. TapMo's unified handle-based representation applies to diverse, non-rigged meshes. (Abstract, Section 1)
- **Strong and consistent geometry preservation on both seen and unseen characters.** TapMo reduces ARAP-Loss by 69.8% (0.271 vs. 0.897) on seen characters and 58.2% (0.329 vs. 0.787) on unseen characters compared to the best baseline (MDM-SR), with ablations confirming each component contributes (Table 2). This metric is representation-agnostic and directly measures the paper's core claim of geometric integrity.
- **Weakly-supervised design that trains without ground-truth handles/motions for diverse characters.** The spring loss (bone-length consistency) and adversarial loss (skeleton-driven motion prior) provide supervision signals without requiring per-character ground-truth motion data. (Section 3.2, Equations 10–12)
- **Generalization to unseen characters with heterogeneous topologies.** The method is evaluated on both seen and unseen meshes (Table 2), and qualitative results show reasonable animation of non-humanoid shapes (Figures 2, 4).
- **User study confirms perceptual preference.** 1,335 rankings from 100 volunteers show TapMo ranked first across all three quality axes (overall, text-motion matching, geometry); 84%+ prefer TapMo over baselines (Section 4.4, Figure 5).

## Weaknesses

### Fatal
None.

### Major
- **Incomparable motion quality metrics in Table 1 undermine strong performance claims.** The paper compares TapMo (handle-based motion representation) against prior methods (T2G, Hier, TEMOS, T2M, MDM) that use skeleton-based representations. Because the feature extractor must be retrained for the different motion representation, the FID and R-Precision values live in different metric spaces — as evidenced by the "Real" vs. "Real†" rows having substantially different numbers (e.g., Diversity 9.503 vs. 17.176; R-Precision Top-1 0.511 vs. 0.559). Directly comparing FID=0.515 (TapMo in handle-space) to FID=1.067 (T2M in skeleton-space) is not meaningful. The paper states "TapMo outperforms previous models significantly" based on this comparison, which overstates the evidence. The within-representation comparison (TapMo vs. TapMo(MDM), improving FID from 1.058 to 0.515) is valid and shows architectural improvement, but the cross-representation comparisons should be removed or presented with explicit caveats that they are not on the same scale.

### Minor
- **Skinning Loss ℒ_s and Pose Loss ℒ_p are mentioned but never defined.** Section 3.1 introduces three losses (ℒ_s, ℒ_p, ℒ_r) for adaptive handle learning, and Equation 8 trains the Handle Predictor with ℒ_s + ν_p ℒ_p + ν_r ℒ_r. However, only ℒ_r (Root Loss) is defined (Eq. 6). ℒ_s and ℒ_p are critical for understanding how semantic parts and skinning weights are learned, yet their formulations are absent from the paper. While they may follow from SfPT (Liao et al., 2022), the paper should at minimum describe what each loss penalizes.
- **Conversion from SMPL motions to handle-based representation is not validated.** The diffusion model is trained on existing motion-language data by "converting SMPL motions to our handle-based motion representation using the analytical method introduced in [Besl & McKay, 1992]." This conversion defines the ground-truth motion distribution (Real†), but the paper provides no analysis of its accuracy, reconstruction error, or potential artifacts. A vertex-position reconstruction error after linear blend skinning with the converted handles would help establish data quality.
- **Seen/unseen character split is not described.** Table 2 and the text report ARAP-Loss separately for seen and unseen characters, but the paper never specifies which characters belong to each set, how many characters are in each split, or what "unseen" means (topologically novel? different mesh family?). This makes the generalization claim difficult to interpret.
- **Multimodality scores are reported but not discussed.** Table 1 reports Multimodality for TapMo (2.559) and TapMo(MDM) (2.744), alongside prior methods like T2M (2.090) and MDM (2.799). The text does not compare or interpret these values, making the column uninformative.
- **Adversarial loss samples only 100 arm vertices.** The paper justifies this by observing "motion distortion mainly occurs in the arm parts." This is a reasonable heuristic but could miss distortion elsewhere (e.g., legs during walking, stretching motions). A broader sampling strategy or an ablation showing that arm-only sampling suffices would strengthen the case.

### Trivial
- The number of handles K is never specified. An ablation showing sensitivity to K would improve reproducibility.
- The paper states "state-of-the-art performance" in the conclusion without caveating the evaluation limitations discussed above.

## Nice-to-Haves
- Reporting vertex-position reconstruction error for the SMPL-to-handle conversion step, to validate the training data quality.
- An ablation of the mesh deformation feature f_φ (shape-aware conditioning vs. shape-unaware baseline) to quantify its contribution independently.
- Evaluation on more topologically diverse unseen characters (e.g., animals, fantasy creatures) with per-type ARAP-Loss breakdown.
- A failure case analysis showing where TapMo breaks (e.g., extreme proportions, thin structures).
- Specification of the seen/unseen character split, the handle count K, and the number of ARAP optimization steps for pseudo-label generation.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Handle-FID evaluation is unfair and contradicts the paper's goal"** (Harsh Critic Point 2): The paper already acknowledges that MDM-SR achieves the best Handle-FID (0.012) "due to its utilization of a standard SMPL skeleton structure." Handle-FID is one metric assessed on SMPL models for controlled comparison; the primary geometry metric (ARAP-Loss) is evaluated across all characters and shows clear improvement. The paper is transparent about this limitation. **Removed because the paper already addresses this.**
- **"Spring loss asymmetry causes unconstrained far-apart handles"** (Harsh Critic Section 3.2 note): The exponential adaptive coefficient on the first term (bone-length preservation) is a reasonable design — nearby handles (within a limb) are constrained more tightly than far-apart handles. The second term (temporal smoothing) applies uniformly to prevent jitter. This is not an "asymmetric" flaw; it's a purposeful design. **Removed: mischaracterizes the formulation.**
- **"MDM-SR is a weak baseline"** (Section 4 note): The paper is the first in this space; there are no established baselines for text-driven skeleton-free animation. MDM-SR and MDM-SFR are reasonable adaptations of the closest prior work. The paper acknowledges their limitations qualitatively. **Removed: not a paper flaw that stronger baselines do not exist.**
- **"User study not convincing because baselines are flawed"** (Critical Issue 5): User studies compare against the best available alternatives. Showing 84% preference provides meaningful evidence even if the baselines have known weaknesses. **Removed: the criticism demands an impossible ideal baseline.**
- **"Evaluation on only two SMPL models for Handle-FID is narrow"**: Handle-FID is a secondary metric; the primary geometry metric (ARAP-Loss) is not limited to SMPL models. The paper's main claims about geometry preservation rest on ARAP-Loss across seen/unseen characters.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that its own framing does not already capture.

## Suggestions
1. **Restructure Table 1 to separate the two metric spaces.** Place prior skeleton-based methods and the original "Real" row in one block, and handle-based methods (Real†, TapMo variants) in another. Explicitly state that metrics across blocks are not comparable and remove strong claims of superiority over prior skeleton-based methods based on these numbers. Keep the valid within-representation comparison (TapMo vs. TapMo(MDM)).
2. **Define ℒ_s and ℒ_p**, even briefly. This is essential for understanding the Handle Predictor training. A single sentence per loss describing what it penalizes would address the issue.
3. **Provide a validation of the SMPL-to-handle conversion** — report vertex reconstruction error (e.g., mean per-vertex position error after LBS with predicted handles vs. ground-truth SMPL vertex positions).
4. **Describe the seen/unseen character split** explicitly — list character names, number per split, and topological variety.

## Score and Decision
This paper targets an important and underexplored problem, proposes a well-motivated architecture, and delivers strong results on geometry preservation (ARAP-Loss, user study). The main weakness is an overclaimed motion quality comparison across incomparable metric spaces, which is fixable by restructuring Table 1 and softening the claims. The missing loss definitions and conversion validation are addressable in revision. The core contributions — skeleton-free animation via handle prediction and shape-aware diffusion — remain solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>