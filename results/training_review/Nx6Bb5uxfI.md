Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the consolidated review.

---

## Summary

This paper proposes E3D, a two-stage training strategy that leverages Large Multimodal Models (LMMs) to generate pseudo-labels for sparsely-supervised 3D object detection. E3D consists of three components: (1) CPST, which projects LMM-derived foreground masks onto point clouds using boundary-constrained mask shrinking; (2) DCPG, which dynamically clusters seed points to fit bounding-box proposals; and (3) the DS Score, an unsupervised quality metric for filtering pseudo-labels. The method is applied as a pre-training step before fine-tuning on sparsely annotated data, and is evaluated on KITTI.

---

## Strengths

- **Large and consistent performance gains under extremely sparse supervision.** E3D improves the sparsely-supervised detector CoIn++ by 36.92% at a 0.1% annotation rate and 14.89% at a 2% annotation rate on KITTI (Table 1). These are substantial absolute improvements that directly support the paper's core claim that LMM priors help under extreme label scarcity.

- **Detector-agnostic integration.** Table 2 shows E3D improves three distinct detector architectures (VoxelRCNN, CenterPoint, CasA) under the 2% annotation setting, demonstrating that the benefit is not tied to a single backbone and that the pseudo-label initialization generalizes across detectors.

- **Well-motivated technical components.** The CPST mask shrink operation (Eq. 3) directly addresses the known problem of calibration-error-induced semantic noise at object boundaries — a simple but sensible heuristic. The DS Score combines a distributional prior on point-to-boundary distances with a category-level shape prior, providing an unsupervised quality signal for pseudo-label filtering.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against the most directly relevant baselines (MixSup, SAL).** The paper cites MixSup and SAL (Yang et al., 2024) in §2.3 as methods that also transfer 2D image semantics to 3D point clouds to generate pseudo-labels for label-efficient detection. Since these are the closest competitors with the same motivation (using image information to bootstrap 3D detection under limited labels), their omission from Tables 1 and 2 is a significant evidential gap. Without this comparison, the reader cannot determine whether E3D's improvements over CoIn++ come from the specific design of CPST/DCPG/DS Score or simply from adding image-based pseudo-labels (which MixSup and SAL also provide). The paper claims "Compared with these methods, our E3D provides a simple but efficient way to reduce semantic noise" (§2.3) without any experimental evidence to support this comparative claim.

- **Zero-shot claim is asserted but not supported with experiments in the main text.** The abstract states "we have verified our E3D in the zero-shot setting, and the results demonstrate its performance exceeding that of the state-of-the-art methods," and the contribution list in §1 says "without fine-tuning on labeled data, our E3D has shown superior performance compared to zero-shot methods." However, the main text (§4) contains no zero-shot experiment, no zero-shot table, and no cross-reference to any section where such results appear. The experiments presented use fine-tuning with 2% annotation cost. For a contribution highlighted as a bullet point, this claim is unverifiable from the submission content and undermines the stated achievements.

### Minor

- **DS Score parameters lack ablation or sensitivity analysis.** The distribution constraint score (Eq. 5) fixes the Gaussian prior at μ=0.8, σ=0.2 (cited to Luo et al., 2024, but not justified for this new setting). The meta-shape constraint score (§3.4) uses a per-category "meta instance" shape B_c = {l_c, w_c, h_c} whose derivation is never specified (is this the mean shape from training set statistics? A fixed template?). The two weighting factors λ₁ and λ₂ are both set to 0.5 without any sensitivity study. Because the DS Score directly controls which pseudo-labels survive to the first training stage, these unexamined choices weaken confidence that the reported gains stem from the design rather than fortuitous hyperparameter settings.

- **DCPG clustering procedure description is ambiguous.** The dynamic radius update (Eq. 4) produces a per-seed-point radius that increases with the seed point index t. The paper states this radius is used "as the clustering radius for DBSCAN" (line 119), but standard DBSCAN uses a single ε for all points. It is unclear how per-point radii integrate with DBSCAN, whether multiple seed points of the same instance produce overlapping clusters, or whether Algorithm 1 (referenced but text not visible) clarifies this. This ambiguity makes the core pseudo-label generation step non-reproducible from the description alone.

- **Only KITTI dataset is evaluated.** While KITTI is a standard benchmark, reliance on a single dataset with specific camera-LiDAR calibration quality and driving environment limits generalizability. The paper does not acknowledge this as a limitation.

- **No run-to-run variance or confidence intervals reported.** The reported results in Tables 1 and 2 are single numbers without any indication of variance. Given the inherent randomness in cluster-based pseudo-label generation and sparse label selection, reporting variance would strengthen confidence in the results.

- **Mask shrink factor γ = 0.3 and other hyperparameters (r_initial = 1, δ = 0.1) are unablated.** While small variations in these are unlikely to change the paper's main conclusions, the absence of any ablation study for parameters that directly affect seed-point quality and cluster radii is a gap in empirical rigor.

### Trivial

- The paper does not report pseudo-label statistics (total generated per scene, kept after DS Score filtering) or training/pseudo-label generation time, which would be useful for reproducibility assessment.

- The normalization method for the two DS Score components before combining (s̅_dc and s̅_msc) is mentioned (line 145) but not specified (min-max? z-score?).

---

## Nice-to-Haves

- An ablation of the DS Score components (removing distribution constraint, removing meta-shape constraint, removing both) would strengthen the paper by isolating which prior contributes most.
- Pseudo-label quality analysis (precision/recall against ground truth at IoU ≥ 0.5 on the KITTI val set) would illuminate whether the DS Score primarily improves precision or recall.
- A comparison of DCPG's dynamic radius against a fixed-radius baseline would clarify the benefit of the dynamic update.
- Evaluation on nuScenes or Waymo would test generalizability to different sensor setups.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Strength from Strength Finder: "Effectiveness in the zero-shot setting"** — Removed because it conflicts with the verified weakness that zero-shot results are neither presented in the main text nor cross-referenced. The strength claimed the paper "reports" zero-shot results in Section 4.1, but Section 4.1 contains no zero-shot experiments. Since strength and weakness conflict, weakness prevails.

- **Strength from Strength Finder: "Novel modules that address specific technical challenges"** — This is generic phrasing. The modules are real contributions, but the strength as formulated is superficial. Kept implicitly via the third bullet in Strengths.

- **Harsh critic's criticism about Figure 1 not labeling 36.92% as relative vs. absolute** — This is a formatting/presentation nitpick about a figure whose numbers cannot be fully verified from text. Minor at best; removed per formatting rule.

- **Harsh critic's criticism about Table 1 header formatting (CoIn++ 100% row confusion)** — Formatting/style nitpick about table layout. Removed per hard rules on formatting.

- **Harsh critic's "Table 2 caption dense"** — Subjective formatting opinion. Removed.

- **Speculative criticism about whether the Gaussian in Eq. 5 is isotropic or anisotropic** — The paper defines D as a set of scalar distances {d₁,...,dₙ} from interior points to the box boundary, so the Gaussian is univariate. This is clear from the formulation. The concern reflects a misreading.

---

## Novel Insights

The most interesting observation that emerges across the reviews is that E3D's design is structured around two well-motivated geometric priors (boundary-constrained mask shrinking and the distribution-shape score) that could, in principle, be applied to any cross-modal pseudo-label pipeline — not just LMM-based ones. However, the paper's evaluation does not isolate whether these geometric priors provide additional value beyond the naive projection of image masks onto point clouds, because the method is never compared against simpler projection baselines (like MixSup's connected-components approach). This leaves the reader uncertain whether the 36.92% gain is attributable to the specific design of E3D or to the general strategy of using image semantics (which prior methods also do). A clean ablation comparing E3D against a "naive mask projection + NMS" baseline would resolve this.

---

## Suggestions

1. **Add the missing baselines.** Implement MixSup's connected-components strategy and SAL's density clustering under the same training protocol and report results alongside E3D in Table 1. This is the single most important experiment needed to substantiate the paper's claims.

2. **Either provide zero-shot results or remove the claim.** If zero-shot experiments exist in an appendix, add an explicit cross-reference in the main text (e.g., "see Appendix A, Table X") and summarize the key numbers. If they do not exist, remove the zero-shot claim from the abstract and contributions.

3. **Ablate the DS Score components and key parameters.** Report AP when: (a) removing the distribution constraint, (b) removing the meta-shape constraint, (c) removing both (falling back to confidence = seed-point count + NMS). Also vary λ₁, λ₂ (e.g., (1,0), (0,1), (0.7,0.3)) and γ (0.1, 0.3, 0.5).

4. **Clarify the DCPG clustering procedure.** Explain how per-seed-point radii interface with DBSCAN (or specify if a modified version of DBSCAN is used). Provide a concrete example for a typical KITTI scene.

5. **Add a pseudo-label quality table** reporting precision and recall against ground truth at IoU≥0.5, to show that the DS Score actually filters low-quality proposals.

---

## Score and Decision

**Originality:** Moderate. The idea of using LMMs to bootstrap sparsely-supervised 3D detection is timely, and the components (CPST, DCPG, DS Score) represent a novel system design. However, the overall strategy of projecting image semantics to generate 3D pseudo-labels is not new (MixSup, SAL).

**Importance of research question:** High. Reducing annotation cost for 3D detection is a practically important problem.

**Claims supported:** Partially. The main claim (improving CoIn++ under sparse supervision) is supported by Tables 1-2. However, the zero-shot claim is unsupported, and the comparative claim against MixSup/SAL is untested.

**Soundness of experiments:** Moderate. Improvements over CoIn++ are clear, but the missing baselines and unablated parameters weaken the overall experimental validation. Single-dataset evaluation limits generality.

**Clarity of writing:** Fair. The method description is generally clear, but key details (DCPG clustering, meta-shape derivation, normalization method) are underspecified.

**Value to community:** Moderate. If validated against proper baselines and with zero-shot evidence, the pipeline would be practically useful. In its current form, the missing evidence makes it hard to assess the actual contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>