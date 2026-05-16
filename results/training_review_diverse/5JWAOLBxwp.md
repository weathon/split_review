I now have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes FER (Frequency-based Equivariant Representation), a method to construct high-dimensional SO(3)-equivariant features by defining a mapping $D: SO(3) \to SO(n)$ and using it to transform 3D point coordinates into an $n$-dimensional feature space whose frequency content grows with $n$. The representation plugs directly into Vector Neuron (VN) architectures, addressing VN's core limitation of being confined to 3-dimensional features. Experiments across six tasks (completion, compression, normal estimation, registration, classification, segmentation) show consistent improvements over VN baselines and achieve state-of-the-art results among equivariant methods on several benchmarks.

## Strengths

- **Novel and intuitive high-dimensional equivariant representation for Vector Neurons**: The paper derives $D: SO(3) \to SO(n)$ from geometric principles (preserving rotation angles/axes) rather than relying on Wigner-D matrices or spherical harmonics, making the connection between feature dimensionality and frequency content explicit. The construction is motivated clearly in Section 1 and Figure 2, and the paper proves the representation reduces to sinusoids whose frequency is bounded by $\lfloor (n-1)/2 \rfloor$, directly connecting to the NeRF/Fourier-feature literature.

- **State-of-the-art results among equivariant networks across multiple benchmarks**: FER-VN-DGCNN achieves the highest accuracy among rotation-equivariant methods on ModelNet40 classification (90.5% in both z/SO(3) and SO(3)/SO(3) settings, surpassing TFN's 85.3–88.5% and VN-DGCNN's 89.5–90.2%) and on ShapeNet part segmentation (83.5% mean IoU in SO(3)/SO(3), versus TFN's 76.2% and VN-DGCNN's 81.4%). In normal estimation, FER-VN-DGCNN achieves the lowest angular error (0.143 on ShapeNet, 0.078 on ModelNet40). In registration, FER-VN-EquivReg reduces Chamfer Distance from 0.00560 to 0.00347 (distinct sample setting). These results are verified in Tables 1–3.

- **Consistent empirical evidence that FER captures fine details**: The shape compression experiment on EGAD (Figure 3) shows FER-VN-OccNet's IoU advantage over VN-OccNet grows from <1% to >5% as shape complexity increases, directly supporting the claim that multi-frequency features are needed for high-detail 3D data. Qualitative reconstructions (Figures 1 and 4) visually confirm that FER-VN recovers wheels, side mirrors, and chair legs that VN-OccNet smooths away.

## Weaknesses

### Fatal

None.

### Major

- **No uncertainty quantification across any experiment**: No standard deviations, confidence intervals, or error bars are reported in any table or figure. Many results are numerically close (e.g., OccNet 71.4% vs. FER-VN-OccNet 71.9% in completion I/I; VN-DGCNN 0.152 vs. FER-VN-DGCNN 0.143 in normal estimation on ShapeNet) and could fall within run-to-run variance. Without this information, the reader cannot assess whether the improvements are statistically significant. This is the single most important missing piece.

- **Limited comparison to high-dimensional equivariant methods on non-standard tasks**: While the paper does compare against TFN on classification and segmentation (Tables 2 and 3), the normal estimation, shape compression, and registration experiments compare only against VN and Frame Averaging baselines, omitting high-dimensional equivariant methods (TFN, SE(3)-transformers, etc.). Since the paper's central claim is offering a superior/competitive *high-dimensional* equivariant representation, the absence of such comparisons on these tasks weakens the evidence. The improvements over VN are substantial but could partly reflect higher feature capacity rather than properties specific to the FER construction.

### Minor

- **Incomplete presentation of the method construction in the extracted text**: The core mathematical construction of $D$ and the proof of equivariance reside in an `\input{method_bk}` file that the parser could not resolve. While the original submission's compiled PDF would contain this content, the extracted text alone does not permit independent verification of the construction's correctness. The high-level intuition is well described in the introduction (lines 25–36) and the commented-out block (lines 44–48), but formal details are absent from this extraction.

- **Normal estimation table lacks metric definition**: Table 4 (table:normal) reports numerical values without stating what the metric is (presumably angular error in radians or Chamfer distance, but the caption does not specify, nor does the accompanying text clarify).

- **Improvements are consistent but modest on several tasks**: In classification, FER-VN-DGCNN (90.5%) improves over VN-DGCNN (89.5–90.2%) by 0.3–1.0 percentage points. In completion, the I/I improvement over OccNet is 0.5 points (71.4→71.9). These are positive but not dramatic. The paper's claim of "state-of-the-art among equivariant networks" is correct but narrows when PaRINet (rotation-invariant) achieves 91.4% on the same classification benchmark.

- **No discussion of limitations or future work**: The conclusion ends abruptly without acknowledging potential limitations (e.g., sensitivity to the chosen basis axis $\hat{z}$, computational cost of large $n$, assumptions about the rotation axis mapping). Including such discussion is standard practice and would strengthen the paper.

### Trivial

- Minor typo: "sinusods" on line 279 should be "sinusoids."

## Nice-to-Haves

- A frequency-domain analysis of the learned features (e.g., Fourier spectrum of reconstructed surfaces in the shape compression task) would directly validate the claim that FER captures multi-frequency content, rather than relying on geometric IoU as a proxy.
- An ablation study varying $n$ (the output dimension) on a main-task experiment (e.g., classification or shape compression) would help practitioners choose $n$ and would further support the claim that higher $n$ systematically captures finer detail. The paper mentions such analysis exists in appendices, but a main-text summary would be valuable.
- A comparison to SE(3)-transformers in addition to TFN, at least on classification/segmentation where published results exist, would broaden the empirical scope.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"The only equivariant baselines are VN and Frame Averaging"** (Harsh Critic): Factually incorrect — TFN is compared in both classification (Table 2) and segmentation (Table 3) experiments. The paper includes multiple equivariant baselines (TFN, Spherical-CNN, $a^3$S-CNN, SVNet-DGCNN). Retained only the valid kernel: high-dimensional equivariant methods are absent from the other four tasks.

- **"The method section is critically incomplete / impossible to assess"**: The `\input{method_bk}` on line 87 resolves to an included file that exists in the original submission. The parser issue does not reflect author error; the compiled paper contains the full method description. This criticism should not count against the paper.

- **"The conclusion does not mention limitations"** kept in Minor — this is valid.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem" — not present in Strength Finder output; the strengths listed are concrete and cited). No removal needed here.

- **"Missing appendix, missing proofs in appendix"**: The parser strips appendices from all papers; these exist in the original submission. Removed per hard rules.

- **"Unfair comparison"** complaints: The paper's experimental setup fairly compares against published methods under standard settings. No asymmetries favoring the proposed method were found.

## Novel Insights

The reviewers largely converge on the paper's core strengths (a novel, intuitive high-dimensional equivariant representation that demonstrably improves detail capture) and its primary weakness (lack of uncertainty quantification). The most interesting insight from combining the reviews is a calibration point: the "missing method" criticism reflects a parser artifact that should not be held against the paper, and the "missing TFN comparison" criticism is overbroad since TFN *is* compared on two of six tasks. The genuine gap is that the paper's improvements, while consistent, are not accompanied by variance estimates — this single fix would substantively address the reviewer's central concerns. Additionally, the paper would benefit from making explicit what the appended dimensional analysis shows (frequency-domain evidence, $n$ ablations) rather than deferring it entirely.

## Suggestions

1. **Add standard deviations or confidence intervals** to all experimental tables and figures. This is the highest-impact fix and would immediately address the most serious weakness.
2. **Clarify the normal estimation metric** (angular error in degrees/radians? Chamfer distance?) in both the table caption and the main text.
3. **Add a limitations paragraph** to the conclusion, discussing the basis-axis choice, computational scaling of $n$, and any assumptions of the $D$ construction.
4. **Include a main-text summary** of the dimensional analysis (currently relegated to appendices) — even one sentence showing how IoU or accuracy changes with $n$ on a representative task would strengthen the core claim about frequency control.
5. **Add a frequency-analysis figure** (e.g., Fourier spectrum of reconstructed shapes) to directly validate the multi-frequency claim rather than inferring it only from geometric quality.

## Score and Decision

The paper proposes a novel, intuitive solution to a well-motivated problem (the dimensionality limitation of Vector Neurons) with consistent empirical support across six diverse tasks. The core contribution is clearly articulated and the experimental results, while modest in magnitude on some tasks, are uniformly in the right direction and achieve SOTA among equivariant methods on classification and segmentation. The most significant weakness — absence of variance reporting — is fixable and does not invalidate the contribution. The missing method content is a parser artifact.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>