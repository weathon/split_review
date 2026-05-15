Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes a keypoint detection and description framework that fuses rotation-equivariant features (from G-CNNs) with global positional information (via a Transformer encoder). It introduces a directional uncertainty weighted descriptor (DUWD) loss to handle discrete group sampling errors. The method is evaluated on rotated variants of HPatches, MegaDepth, and YFCC100M, reporting state-of-the-art pose estimation accuracy under large rotations.

## Strengths

- **Novel architecture combining rotation-equivariant features with positional encoding**: The paper proposes a specific design (Section 3.1.2, Fig. 2) that fuses a G-CNN-based rotation-equivariant feature pyramid with a Transformer encoder applied to the deepest feature maps. The design is validated by ablations (Table 4) showing that the proposed fusion strategy outperforms two alternative fusion patterns on both rotated and non-rotated MegaDepth.

- **State-of-the-art results on large-rotation datasets**: On MegaDepth-Rot-Rand, the method achieves the best pose error AUC among compared methods (ReF, RELF, AWDesc, and handcrafted detectors). On YFCC100M-Rot-Rand it similarly leads. These results directly demonstrate the claimed rotation robustness improvement.

- **Directional uncertainty weighted descriptor loss**: The DUWD loss (Section 3.3, Eq. 5) incorporates principal-direction confidence weighting and a cross-entropy term for discrete-group orientation alignment. This is a principled attempt to address the bias introduced by discrete group sampling, and it is tied to the method's performance gains on rotated benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **Missing detail on how ground-truth rotation O_gt is obtained from MegaDepth training data**: The DUWD loss (Eq. 5) includes a cross-entropy term `CE(Shift(D_A, O_gt, D_B))` that requires the ground-truth relative 2D rotation between image pairs. The training uses MegaDepth (Section 4.1), which provides 3D camera poses, not 2D in-plane rotations. The paper states "even when the ground truth rotations can be obtained during training" (line 120) but never explains how the 2D rotation `O_gt` — needed to index into a discrete group of size K=8 — is derived from the 3D camera poses, or what approximation is used. This is not a fatal flaw (the relative camera rotation can be projected to obtain an approximate 2D rotation, and this is standard practice), but the omission is a significant reproducibility gap that prevents readers from understanding or re-implementing the training pipeline. Without this detail, the reader cannot assess whether the loss computation is sound for non-planar, depth-rich scenes where the effective 2D rotation varies across the image.

2. **Ablation study does not isolate individual contributions**: The ablation (Table 4, Section 4.4) compares only three variants of the fusion module (where the Transformer output is added relative to the dilated module). It does NOT ablate: (a) the rotation-equivariant backbone vs. a standard CNN backbone, (b) the DUWD loss vs. a standard triplet loss, or (c) the multi-scale rotation-equivariant fusion vs. single-scale. Without these ablations, the reader cannot attribute the performance gains to any specific claimed contribution. The ablation results are also described only qualitatively ("ablation1 performs weaker") without reporting numerical values in the text, making the analysis thin.

3. **Missing standard baselines on non-rotated data**: On the MegaDepth and YFCC100M non-rotated benchmarks (Tables 2–3), the paper compares only to ORB, BRISK, AKAZE, KAZE, ReF, RELF, and AWDesc. Standard learned local feature methods such as SuperPoint, D2-Net, and R2D2 are absent from the comparison. While the paper's focus is rotation robustness and the most relevant rotation-equivariant baselines (ReF, RELF) are included, the absence of these widely-used methods makes the claim of "best performance" on *non-rotated* data less well-supported and leaves unclear how much non-rotation performance is traded for rotation gains.

### Minor

1. **Missing specification of PCA-to-group-index mapping for inference**: The paper states (Section 3.3, line 106) that PCA estimates the principal direction, and Figure 2 shows descriptors undergoing circular shifts after PCA. However, the paper never specifies how the continuous PCA output is mapped to a discrete group index (K=8) for circular shifting during inference — a critical step that prior works like ReF and RELF explicitly handle via group pooling or group aligning.

2. **Incompatibility between motivation and method is acknowledged but not resolved**: The paper (Section 3, line 60) states that "local rotation-equivariance and global position information are often incompatible" and then combines them without a mechanism to decouple global vs. local rotations. This is a valid concern about the framing: the paper identifies a tension as motivation but does not theoretically analyze how the combined architecture resolves it. The empirical results help justify the design, but the framing over-promises. This is a presentation issue, not a fatal flaw.

3. **Notation issues in Eqs. (3)–(4)**: In Eq. (3), the arguments to D in `D(c, argmax_k Σ_c D(k,c))` appear swapped relative to the declared index ordering D(k,c). In Eq. (4), the denominator `Σ_{k=0}^{k}` has a typo in the upper bound. These do not prevent understanding but indicate sloppy presentation.

4. **Handcrafted methods outperform the proposed method on rotated-HPatches**: The paper honestly reports (Section 4.2, line 151) that traditional handcrafted keypoints "perform slightly better" on the rotated-HPatches dataset. While the paper provides a reasonable explanation (planar scenes limit learning-based advantage), this admission limits the scope of the claimed improvement and warrants more discussion than the single sentence given.

5. **Runtime compared only to AWDesc**: The runtime analysis (Section 4.5) compares only against AWDesc (0.4785s vs. 0.3106s, a 54% increase). Comparisons to ORB, BRISK, AKAZE, and KAZE — which are typically much faster — are missing, making it difficult to assess the practical speed trade-off.

### Trivial
- The upper bound typo in Eq. (4) denominator (`Σ_{k=0}^{k}` should be `Σ_{k=0}^{K-1}`).
- No confidence intervals or variance reported for any result (standard practice in this benchmark setting, but reporting would strengthen the paper).

## Nice-to-Haves
- **Confidence intervals**: Reporting variance across runs or bootstrap confidence intervals for the AUC metrics would strengthen the reliability of the reported gains.
- **Synthetic rotation benchmark**: Training on synthetic rotations with known ground-truth O_gt (e.g., rotated MegaDepth images) would cleanly verify that the DUWD loss's cross-entropy term works as intended, and would complement the current real-data training setup where O_gt must be approximated.
- **Equivariance error measurement**: Quantitative measurement of equivariance error (descriptor shift deviation under known rotations) with and without the Transformer branch would provide direct evidence about whether positional information disrupts local equivariance.

## Removed Points
- **Criticism that "the entire method collapses" due to O_gt unavailability** (Critical Issue 1, harsh critic): This is an overstatement. MegaDepth provides camera poses from which relative rotations can be extracted. The issue is a missing implementation detail, not a logical impossibility. The critic's wording ("cannot be executed as described," "collapses") is not supported by the paper — the paper states "even when the ground truth rotations can be obtained during training," implying the authors have a procedure (they simply do not describe it). The criticism is retained as a Major weakness above but stripped of its fatal framing.
- **Criticism that the evaluation "is unsupported" without SuperPoint, D2-Net, R2D2, ASLFeat, SOSNet** (Critical Issue 3): The paper's primary claim is rotation robustness, and the most relevant rotation-robust learned baselines (ReF, RELF) and the SOTA descriptor (AWDesc) are all included. The missing methods are not specifically rotation-robust. Retained as a Minor weakness above but not as a fatal omission.
- **Request for confidence intervals**: Standard practice in this benchmark setting is single-run evaluation. Moved to Nice-to-Haves.
- **Complaint about "generic textbook material" in Section 2.2**: Standard for a related-work section describing background. Not a weakness.
- **Critique about gradient vanishing when β→1** (Section 3.3): This is by design — when the principal direction is clear (β→1), the directional clarity loss contribution is intentionally small. This is a feature, not a bug.
- **"The paper should not be accepted in its current form" / "would need to fundamentally rework the loss formulation"** (Overall Assessment, harsh critic): This conclusion is not supported by the verified weaknesses. The missing implementation details are addressable in revision; the core methodology is sound.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not provide.

## Suggestions

1. **Clarify O_gt derivation**: Explicitly describe how the ground-truth relative 2D rotation `O_gt` is obtained from MegaDepth camera poses for training. If an approximation is used (e.g., extracting the in-plane rotation component from the relative camera rotation), state it clearly and discuss its limitations, especially for non-planar scenes where the effective 2D rotation varies across the image.

2. **Expand the ablation study**: At minimum, add ablations replacing the G-CNN backbone with a standard CNN (to isolate the benefit of rotation-equivariant features) and replacing the DUWD loss with a standard triplet loss (to isolate the benefit of the proposed loss).

3. **Specify the inference pipeline**: Clearly describe how PCA output is mapped to a discrete group index for circular shifting during inference, and how aligned descriptors are matched.

4. **Add standard learned baselines on non-rotated data**: Include SuperPoint, D2-Net, or R2D2 in the non-rotated MegaDepth/YFCC100M comparison to show that the method does not degrade on standard benchmarks.

5. **Fix notation**: Correct the argument ordering in Eq. (3) and the upper bound typo in Eq. (4) for clarity.

## Score and Decision

**Originality**: Good — the fusion of rotation-equivariant features with Transformer-based positional encoding is a novel design. The DUWD loss is also a novel contribution.

**Importance of research question**: High — rotation-robust feature extraction is practically important for robotics, UAVs, and extreme-motion scenarios.

**Claims support**: Moderate — the headline claims of state-of-the-art rotation robustness are supported by comparisons to relevant baselines, but missing implementation details and a thin ablation weaken the evidence.

**Soundness of experiments**: Moderate — the evaluation covers three datasets with rotated variants and uses standard metrics, but the O_gt derivation ambiguity and limited baseline set reduce confidence.

**Clarity of writing**: Below average — the method description is vague in several critical places (O_gt derivation, PCA-to-group-index mapping, exact fusion operation). Notation issues exist. The paper would benefit from tighter editing.

**Value to the research community**: Moderate — the architecture and loss design are of interest to the local feature learning community, and the strong rotated-benchmark results provide a useful reference point. The paper would be more valuable with clarified implementation details.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>