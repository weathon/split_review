Now I have all the information I need. Let me construct the authoritative review.

## Summary

The paper introduces FER (Frequency-based Equivariant feature Representation), a method for mapping 3D points to a high-dimensional SO(n) feature space in a rotation-equivariant way. It constructs a mapping D: SO(3) → SO(n) and uses it to build features that can be plugged into Vector Neuron (VN) networks, overcoming VN's limitation to 3D features. The method is evaluated across six diverse 3D vision tasks (completion, compression, registration, normal estimation, classification, segmentation) and shows consistent improvements over standard VN baselines, particularly in tasks requiring fine detail capture.

## Strengths

- **Addresses a genuine limitation of Vector Neurons with an intuitive approach:** The paper clearly identifies VN's core weakness — confinement to 3D features limits expressivity — and proposes a principled, frequency-aware solution. The construction via D: SO(3) → SO(n) is motivated as a more accessible alternative to Wigner-D matrices from quantum mechanics (Section 2.1), which is a genuine pedagogical contribution.

- **Broad and consistent experimental validation across six tasks:** The method is tested on point cloud completion (Table 1: 71.9 mean IoU vs. VN-OccNet's 69.3), shape compression (Figure 3), normal estimation (Table normal), point cloud registration (Table 3), classification (Table classification: best among equivariant methods at 90.5%), and part segmentation (Table segmentation: best among equivariant methods at 83.5%). This breadth demonstrates that the feature representation benefits multiple downstream applications.

- **Strong registration results with robustness to sampling differences:** In point cloud registration, FER-VN-EquivReg achieves substantially lower Chamfer Distance than VN-EquivReg in both the "Distinct sample" setting (0.00347 vs. 0.00560) and "Varying density" setting (0.00714 vs. 0.01077), demonstrating that the high-dimensional features yield more discriminative point encodings.

- **Effective qualitative improvements shown:** The reconstruction figures (Figure 1, Figure 3) visually demonstrate that FER-VN recovers fine details (car wheels, chair legs, lamp shades) that VN-OccNet smooths out, directly supporting the paper's central claim about capturing high-frequency content.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Missing metric definition in the normal estimation table (Table normal).** The table reports values such as 0.143, 0.214, 0.078, but the paper never states what metric these numbers correspond to (mean angular error? Chamfer distance? chord distance?). Without specifying whether lower is better or what the units are, the table is not self-contained. This is easily fixable but currently makes the results ambiguous.

- **The claim "state-of-the-art performance among equivariant networks" (Introduction, line 36) should be more carefully scoped.** While the claim is technically correct within the "Rotation-equivariant" category in both tables, the rotation-invariant PaRINet outperforms FER-VN on both classification (91.4% vs. 90.5%) and segmentation (83.8% vs. 83.5%). The paper does acknowledge this in the text (Section 5, line 206), but the introduction's phrasing could mislead a casual reader into thinking the method is SOTA across all categories. A more careful qualitative would strengthen the paper.

### Trivial

- The table formatting in the registration section (Table 3) pairs a tabular environment with `\captionof{table}` inside a minipage, which is unconventional and may cause formatting issues in some templates.

- The conclusion is quite brief (Section 6, single paragraph) and largely repeats the introduction. It could better summarize what the experiments revealed about when the method helps and when it does not.

## Nice-to-Haves

- An explicit discussion of when FER-VN does NOT help would strengthen the paper. The classification and segmentation results show diminishing returns over VN-DGCNN (90.5 vs. 90.2, 83.5 vs. 81.4), and PaRINet outperforms on both tasks. A brief analysis of the task characteristics that favor or disfavor the approach would be valuable future guidance.

- The paper references appendices for dimensional analysis (Appendix A, B, C). If those contain ablation on the dimensionality parameter n, including the key finding in the main text would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The core method is not presented in the paper"** — REMOVED. This is a parser artifact. The paper contains `\input{method_bk}` (line 87), a standard LaTeX include command. The method section exists in the actual compiled PDF; the text extraction tool simply did not resolve the included file. The `\iffalse...\fi` block (lines 88–95) is commented-out draft content, not the method section.

- **"Claimed SOTA is contradicted by PaRINet outperforming"** — REMOVED. The paper qualifies its claim as "among equivariant networks" (line 36), and in both the classification and segmentation tables, FER-VN-DGCNN achieves the best results in the rotation-equivariant category (90.5% vs. VN-DGCNN's 90.2% in classification; 83.5% vs. VN-DGCNN's 81.4% in segmentation). PaRINet is in the separate "Rotation-invariant" category, and the paper explicitly acknowledges it (line 206: "ours is only after the PaRINet..."). The criticism misreads the claim.

- **Formatting/style nitpicks** (wrapfigure not captioned, figure reference ordering) — REMOVED as pure formatting issues.

- **"No analysis of dimensionality effect"** — REMOVED. The paper states this analysis is in Appendices A, B, and C (line 139). The parser strips appendices; they exist in the original submission.

- **"No formal demonstration that features capture multiple frequencies"** — REMOVED. Likely contained in the method section and appendices that were not captured by the parser.

- **"Missing parts and places to improve"** about deeper analysis — REMOVED as these are either addressed in appendices or reflect the reviewer's expectations beyond the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new observation about the work that the paper itself does not already state.

## Suggestions

1. **Add the metric definition to the normal estimation table** (Table normal). State clearly what the numbers represent (e.g., mean angular error in radians, or Chamfer distance × 10³) and which direction is better.

2. **Tighten the SOTA claim in the introduction** to explicitly note that the comparison is within the equivariant family, and that rotation-invariant methods like PaRINet achieve higher raw accuracy on classification/segmentation. This would preempt confusion.

3. **Consider moving a key finding from the dimension ablation** (currently deferred to appendices) into the main text — specifically, how performance varies with n and what the relationship is between n and the maximum captured frequency. This directly supports the paper's core technical claim.

4. **Expand the conclusion** with a brief discussion of limitations or failure modes, which would strengthen the paper's scholarly value.

## Score and Decision

The paper presents a well-motivated contribution that addresses a real limitation of Vector Neurons. The core idea — constructing D: SO(3) → SO(n) to build frequency-aware equivariant features — is technically sound and supported by broad experimentation across six diverse tasks. The weaknesses are minor (missing metric definition, slightly loose SOTA phrasing) and easily addressable. The method demonstrably improves detail capture in completion, compression, and registration tasks.

**Originality:** Good — the D: SO(3) → SO(n) construction for VN feature augmentation is novel to this context.  
**Importance of question:** High — improving VN expressivity while maintaining equivariance is a well-recognized need.  
**Claims supported:** Mostly yes, with minor overclaiming in the introduction.  
**Soundness of experiments:** Solid — reasonable baselines, multiple tasks, consistent trend.  
**Clarity:** Good motivation and intuition, though the method section was not available in the extracted text to evaluate.  
**Value to community:** High — provides an accessible, architecture-agnostic equivariant feature for VN-based methods.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>