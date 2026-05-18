Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper proposes an end-to-end framework for robust keypoint description under large rotations. It fuses rotation-equivariant features (via G-CNNs) with global positional information (via a Transformer encoder) and introduces a Directional Uncertainty Weighted Descriptor (DUWD) loss that accounts for discrete rotation-group sampling ambiguity. The method is evaluated on rotated-HPatches, rotated-MegaDepth, and rotated-YFCC100M, consistently outperforming learning-based baselines (ReF, RELF, AWDesc).

## Strengths

- **Novel architectural fusion of rotation-equivariance and global positional encoding.** The paper designs a pipeline that combines G-CNN-based rotation-equivariant multi-scale features with a Transformer encoder for positional context, a direction the authors correctly note is under-explored because local rotation-equivariance and global position are partly incompatible. Evidence: Section 3.1.2 and Figure 2 describe this integration explicitly.

- **Directional Uncertainty Weighted Descriptor Loss (DUWD).** The loss function incorporates a direction-confidence term (β), a direction-clarity loss (L_DC), and a weighted triplet loss, designed to handle the inherent ambiguity from discrete rotation-group sampling. This is a principled adaptation of descriptor learning to the rotation-equivariant setting. Evidence: Section 3.3 defines all components.

- **Consistently strong empirical results on rotated benchmarks.** The method achieves the best or tied-best AUC on MegaDepth-Rot90, MegaDepth-Rot-Rand, and YFCC100M-Rot-Rand against both learning-based and handcrafted baselines, demonstrating that the proposed combination is practically effective. Evidence: Tables 2 and 3 show clear margins on the most challenging rotation-augmented settings.

- **Ablation study testing fusion architecture variants.** The three-way comparison of fusion strategies (proposed, ablation1, ablation2) in Table 4 provides evidence that the specific fusion ordering and skip-connection design matters for performance across rotation conditions. Evidence: Section 4.4, Table 4.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient architectural specification undermines reproducibility.** The paper describes several key components at a high level but omits details needed to reproduce the method:
   - The Transformer encoder is invoked (Section 3.1.2, line 96) without specifying number of layers, heads, hidden dimension, or whether positional encodings are learned or fixed.
   - The "Dilated Feature extraction module" is named and used (lines 96, 198) but its architecture — dilation rates, kernel sizes, number of layers — is never defined.
   - The multi-scale rotation-equivariant fusion (Section 3.1.2, line 94) says "we isolate the rotational group dimensions of the feature maps … concatenate the feature maps together" without explaining the mechanism (e.g., indexing along the group channel, reshaping, separate branches).
   
   For a paper whose main contribution is a new method architecture, these omissions are significant. While the high-level design is clear, a reader cannot reproduce the system from the description alone. This is addressable in a camera-ready version (e.g., a supplementary table) but is a real gap in the current form.

2. **The ablation study does not isolate the contributions of the paper's key novel components.** The ablation (Section 4.4, Table 4) compares three variants of the fusion architecture, but:
   - It never removes the Transformer/positional encoding branch entirely, so the reader cannot determine how much the global positional information contributes relative to a purely rotation-equivariant baseline.
   - The DUWD loss (Section 3.3) — presented as a central innovation — is never ablated against a standard triplet loss (e.g., from AWDesc without the β weighting or L_DC terms). The paper claims this loss "enhances the model's robustness" (Section 5) but provides no experiment isolating this effect.
   - The PCA-based principal direction estimation is not ablated either.
   
   Without these controls, the empirical case for the specific design choices is incomplete.

### Minor

3. **Notation issues in the loss equations.** Several equations contain indexing that is confusing or appears erroneous:
   - Eq. (1): D(k,c) is defined with k (group index) first and c (non-group channel) second, but the numerator D(c, argmax_k Σ_c D(k,c)) uses c as the first index — dimensionally inconsistent with the stated convention.
   - Eq. (2): The denominator Σ_{k=0}^{k} D(k,c) has a nonsensical upper bound "k" (likely K-1 or K).
   - Eq. (3): CE(Shift(D_A, O_gt, D_B)) does not specify what the target for the cross-entropy loss is, or how Shift's output (a circularly shifted descriptor) is turned into a probability distribution.
   
   These issues do not invalidate the method's conceptual contribution (the intent is still understandable from context) but they erode confidence in the rigor of the loss formulation and should be corrected.

4. **Unclear whether learning-based baselines were trained comparably.** The paper states training uses 118 MegaDepth scenes with SuperPoint-derived ground truth (Section 4.1) but does not state whether ReF, RELF, and AWDesc were retrained on the same data or if their reported numbers come from different training setups. For a head-to-head comparison, this matters — especially since the method uses the same detection supervision as AWDesc (SuperPoint ground-truth) but may differ from ReF/RELF. A brief statement would clarify this.

5. **Rotated-HPatches results need a more nuanced discussion.** Handcrafted methods (KAZE, AKAZE) outperform all learning-based methods on this benchmark (Table 1). The paper attributes this to the dataset being "limited to planar scenes" — a plausible but unverified explanation. Because the paper's core thesis involves rotation robustness, the fact that handcrafted methods with simple rotation-invariant designs still lead on planar rotation is worth deeper analysis. A controlled experiment disentangling planar rotation from depth-infused rotation would strengthen the paper's story.

### Trivial

6. **Section numbering is disordered.** The paper jumps from §3.1.2 directly to §3.3 — there is no §3.2. This appears to be a numbering error (the loss section at §3.3 should likely be §3.2) and slightly disrupts readability.

## Nice-to-Haves

- A table of complete architectural specifications (Transformer layers/heads/hidden dims, dilation rates, kernel sizes, number of layers per module) in a supplement would resolve the reproducibility concern.
- An ablation comparing DUWD loss against a standard triplet loss (without β-weighting and L_DC) would directly validate the loss contribution.
- A controlled experiment on HPatches with and without depth information (or synthetic rotations on non-planar data) to disentangle rotation robustness from depth cue utilization.
- Clarification of whether PCA principal direction estimation is computed per-keypoint, per-patch, or per-image at test time, and how the circular shift is applied during inference.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that L_{CVtri} and Shift are "opaque primitives":** The paper explicitly states L_{CVtri} is from AWDesc (proper citation) and explains Shift as a circular shift of descriptors along the rotation-equivariant group dimension based on ground-truth rotation O_gt (lines 126–127). These are not opaque.
- **"The paper's main claim fails on rotated-HPatches":** The paper's stated result on HPatches is outperforming *learning-based* methods (which it does) — it does not claim to beat all handcrafted methods on this benchmark, and the paper openly acknowledges the handcrafted advantage. This is a strawman.
- **Abstract phrasing clarity complaint:** The critic admits the abstract is accurate. This is a pure wording nitpick.
- **Missing related works complaint:** The hard rules prohibit mentioning missing related works as an external reviewer cannot verify their existence.
- **"Contribution insufficiently supported" / "not reproducible" as fatal framing:** The core contributions (architecture, loss, results) are clearly presented. The missing details are a significant but addressable weakness, not a fatal invalidation of the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a supplementary table with full architectural specifications for all modules (Transformer, Dilated Feature Extraction, backbone channels/layers). This is essential for a methods paper.
2. Run two additional ablations: (a) remove the Transformer/positional encoding branch entirely; (b) replace DUWD loss with a standard triplet loss (e.g., from AWDesc). This would directly validate the claimed contributions.
3. Clarify the notation in Eqs. (1)–(3): ensure dimensional consistency in indexing, fix the upper bound in Eq. (2), and specify the target for the cross-entropy term in Eq. (3).
4. Add a sentence specifying whether baselines use comparable training data/detection supervision.
5. Conduct or at minimum discuss a controlled experiment on HPatches (e.g., using synthetic depth or non-planar scenes) to clarify why the method trails handcrafted methods on planar rotations but leads on depth-infused rotations.

## Score and Decision

The paper addresses a real problem (keypoint description under large rotations) with a sensible and novel approach, and the empirical results on the most challenging rotated benchmarks are convincing. The architectural fusion idea and the DUWD loss are genuine contributions. However, the missing architectural details and incomplete ablation meaningfully weaken the paper in its current form — the reader cannot fully assess what drives the reported gains. These issues are fixable (addressing both requires only a supplementary table and a few additional experiments), and the core contributions are solid enough to warrant acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>