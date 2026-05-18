Now I have a complete picture of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes E3D, a two-stage strategy for sparsely-supervised 3D object detection that leverages 2D Large Multimodal Models (specifically FastSAM + SemanticSAM) to generate pseudo-labels that warm-start a 3D detector. E3D consists of three modules: (1) Confident Points Semantic Transfer (CPST) for obtaining clean 3D seed points from 2D semantic masks via boundary-constrained mask shrinking, (2) Dynamic Cluster Pseudo-label Generation (DCPG) for fitting bounding boxes from seed points using a dynamically updated clustering radius, and (3) a Distribution Shape (DS) score for unsupervised quality assessment of generated proposals. Experiments on KITTI show improvements over the CoIn baseline at 0.1% and 2% annotation rates.

## Strengths

- **Large improvements at extremely low annotation rates**: E3D improves CoIn's average AP by 36.92% at 0.1% and 14.89% at 2% annotation rates on KITTI (contributions list, Table 2 discussion), demonstrating that LMM-derived pseudo-labels provide useful feature initialization where prior sparsely-supervised methods collapse. The gains are particularly striking for single-stage detectors like CenterPoint, where the gap from CoIn is largest.

- **CPST module addresses a concrete 2D-to-3D transfer problem**: The paper identifies the real issue of noisy edge semantics during projection (Section 3.2, Figure 4) and proposes a principled boundary-constrained mask shrink (Eq. 3) that retains only the central portion of foreground masks before transfer. This design choice is well-motivated by the known depth ambiguity and calibration errors in 2D-3D projection.

- **DCPG's dynamic radius is motivated by a known failure of fixed-radius clustering**: Unlike prior unsupervised approaches (Zhang et al., 2023) that use a fixed constant radius, DCPG updates the clustering radius dynamically (Eq. 4) to adapt to multi-scale geometry. The paper explicitly identifies the failure mode of fixed-radius clustering (incomplete foreground or excess background noise) and designs around it.

- **Evaluation across multiple detector architectures**: E3D is validated with CenterPoint, VoxelRCNN, and CasA (Table 2), showing consistent improvements over CoIn across detector families, which supports the claim of generalizability.

## Weaknesses

### Fatal

None.

### Major

- **Zero-shot results are claimed but not presented**: The abstract states "we have verified our E3D in the zero-shot setting, and the results demonstrate its performance exceeding that of the state-of-the-art methods." The contributions list similarly claims "without fine-tuning on labeled data, our E3D has shown superior performance compared to zero-shot methods." However, **no zero-shot experiments, tables, or figures appear anywhere in the visible paper**. This is not a missing appendix detail — it is a central claim made twice in the paper's headline presentation with zero supporting evidence. For a paper whose core thesis is using LMMs to generate pseudo-labels, the zero-shot setting (where these pseudo-labels are used directly without any fine-tuning on labeled data) is the most direct test of whether the pseudo-labels are actually useful. Its absence is a major omission that makes the claimed advantages unverifiable.

- **No ablation study isolating the three proposed modules**: The paper claims three contributions (CPST, DCPG, DS score) but provides no experiment that removes or replaces any single component to measure its individual contribution. This means the reader cannot tell: (a) whether all three modules are necessary, (b) whether the gains come primarily from the CPST mask shrinking alone (which is the simplest component), or (c) whether a simpler alternative to any module would work equally well. For a method paper, this is a critical gap — the claim that E3D is a "strategy" comprising three specific designs cannot be evaluated without component-level ablation.

- **Missing comparison against MixSup and other image-assisted sparse-label methods**: The related work (Section 2.3) discusses MixSup (Yang et al., 2024), which also transfers 2D image information to 3D point clouds for pseudo-label generation under sparse annotation. MixSup is a direct competitor with a similar motivation, yet it appears nowhere in Tables 1–2. Without this comparison, it is impossible to judge whether E3D's improvements come from the LMM-based pipeline or from other design choices, and the claim of "state-of-the-art" performance is unsubstantiated within the image-assisted sparse-label niche.

### Minor

- **Unclear distinction between CoIn and CoIn++**: The abstract and Section 4.1 refer to "CoIn++" (citing Xia et al., 2023b — the same reference as CoIn), while other parts of the paper refer to "CoIn." The paper never explains whether CoIn++ is an improved variant of CoIn, a different method, or just a naming convention. Table 1 compares against sparsely-supervised methods (using CoIn++), while Table 2 compares against fully-supervised methods trained with sparse labels (using CoIn). These are different comparison regimes, which is valid, but the naming ambiguity makes it difficult for readers to understand the baseline hierarchy. The paper should clearly define CoIn vs. CoIn++ and reconcile which one is used where.

- **DS score priors are adopted from prior work without validation in the target domain**: The Gaussian prior (μ=0.8, σ=0.2) is cited from Luo et al. (2024), and the meta-shape templates are cited from Wu et al. (2024). While citing established priors is standard practice, the paper does not verify that these priors transfer well to KITTI point cloud data. A simple histogram of interior-point-to-boundary distances on ground-truth boxes from KITTI would have sufficed to validate the Gaussian parameters. Without this, the DS score's reliability in the target domain remains unconfirmed.

- **No hyperparameter sensitivity analysis**: Several key parameters (shrink factor γ=0.3, initial radius r_initial=1, adjustment δ=0.1, DS weights λ1=λ2=0.5) are set without any sensitivity study. While these values are reported in the implementation details, the reader has no sense of how performance varies with these choices or whether the method is brittle. Given that these parameters directly control pseudo-label quality (and thus downstream detection performance), their robustness matters.

- **Experiments are limited to KITTI**: The method is evaluated only on KITTI. While KITTI is a standard benchmark, modern 3D detection evaluation commonly includes Waymo or nuScenes to demonstrate generalizability. The paper should at minimum discuss this limitation and what would be needed to extend to other datasets.

### Trivial

None of note.

## Nice-to-Haves

- A sensitivity study over the shrink factor γ would strengthen confidence in the CPST module.
- A comparison against MixSup, even if limited to the same VoxelRCNN backbone and 2% annotation setting, would significantly strengthen the positioning.
- Visualizing failure cases (e.g., the slight drop in Easy Car AP noted in Table 1) would give insight into the method's boundaries.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **"Inconsistent baseline reporting / factor-of-5 difference between Table 1 and Table 2"** — Removed because the two tables compare fundamentally different settings: Table 1 compares **sparsely-supervised methods** (CoIn++), while Table 2 compares **fully-supervised detectors trained with only 2% labels** (where "Sparse Label" is the baseline of training a standard detector with sparse data). The paper's text makes this distinction clear ("Comparison with SoTA sparsely-supervised methods" vs. "Comparison with fully-supervised methods"). The critic's "factor-of-5" complaint compares apples to oranges. The naming confusion between CoIn and CoIn++ is retained in Minor above, but the inconsistency claim is not valid.

2. **"Algorithm 1 is referenced but missing"** — Removed per instructions: the parser strips algorithmic blocks from many papers; this reflects a parsing artifact, not an author omission. The DCPG procedure is described in prose and Eq. 4.

3. **"LMM framing overstates multimodality (FastSAM + SemanticSAM)"** — Removed. FastSAM performs class-agnostic segmentation, and SemanticSAM uses CLIP-based semantic labeling. This is a legitimate use of vision-language models to extract semantic masks, which constitutes multimodal processing. The critic's objection is a taste disagreement, not a substantive weakness.

4. **"The paper should be evaluated on multiple datasets"** — Downgraded from the critic's framing. KITTI-only evaluation is standard for method papers in this sub-area, and the paper discusses its split protocol. Kept as a minor limitation rather than a major weakness.

5. **Strength Finder's generic strengths** — Some strengths from the Strength Finder (e.g., "comprehensive evaluation across multiple detector architectures") are retained as valid; generic phrasing has been condensed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tensions (method is promising but experimentally incomplete) without offering a new lens on the work.

## Suggestions

1. **Add the missing zero-shot results.** This is the single most important fix — the paper makes this claim prominently and must back it up with a table showing performance of E3D-generated pseudo-labels used directly (no fine-tuning) vs. existing zero-shot methods on KITTI.

2. **Add a component ablation study.** At minimum: (a) full E3D, (b) w/o CPST (no mask shrinking), (c) w/o DCPG (fixed-radius clustering instead of dynamic), (d) w/o DS score (no quality-based NMS). This would validate that each module contributes.

3. **Reconcile the CoIn vs. CoIn++ naming.** Clearly state whether CoIn++ is a variant of CoIn, and if so, how it differs. Ensure tables and text use consistent names.

4. **Add MixSup as a baseline.** Even if exact reproduction is difficult, include the best available numbers from their paper under comparable settings (VoxelRCNN, 2% annotations) to contextualize E3D's gains.

5. **Provide a brief validation of the DS score priors on KITTI.** A small figure showing the empirical distribution of interior-point-to-boundary distances on ground-truth boxes would suffice to show the Gaussian prior is reasonable.

## Score and Decision

The paper proposes a sensible idea (use 2D LMMs to generate pseudo-labels for sparsely-supervised 3D detection) and the reported improvements over CoIn are noteworthy. However, the paper is experimentally incomplete in ways that directly affect the believability of its claims: zero-shot results are promised but entirely absent, there is no ablation isolating the three claimed components, and a directly related competitor (MixSup) is discussed but never compared against. These gaps prevent acceptance in the current form. The core direction is reasonable and could become a strong paper with the missing experiments, but as submitted the empirical support is insufficient.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>