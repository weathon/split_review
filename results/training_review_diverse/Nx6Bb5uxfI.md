Now I have a thorough understanding of the paper and all reviewer claims. Here is my consolidated review:

---

## Summary

This paper proposes E3D, a two-stage training strategy for sparsely-supervised 3D object detection. In the first stage, Large Multimodal Models (FastSAM + SemanticSAM) generate semantic masks on 2D images, which are transferred to 3D point clouds via a Confident Points Semantic Transfer (CPST) module with boundary-constrained mask shrink. A Dynamic Cluster Pseudo-label Generation (DCPG) module produces pseudo-label proposals using adaptive-radius clustering, and a Distribution Shape (DS) score (combining a Gaussian interior-point-to-boundary prior with category-level meta-shape templates) filters proposals via NMS without ground truth. The detector is first trained on these pseudo-labels, then fine-tuned on sparse ground-truth annotations. Experiments on KITTI show non-trivial improvements over CoIn and CoIn++ at 0.1%–2% annotation rates.

## Strengths

1. **Novel pipeline integrating LMMs into sparsely-supervised 3D detection.** The idea of using off-the-shelf LMMs (FastSAM + SemanticSAM, no fine-tuning needed) to bootstrap pseudo-labels for a 3D detector under extreme annotation sparsity is well-motivated and practically appealing. The paper explicitly identifies and addresses the 2D–3D semantic projection noise problem (Figure 4) with a principled mask shrink operation (Section 3.2, Eq. 3).

2. **Dynamic clustering radius in DCPG is a clear improvement over fixed-radius baselines.** Section 3.3 (Eq. 4) introduces a linear update rule that varies the DBSCAN radius per seed point based on its position within the instance's seed set. This is a sensible solution to the foreground incompleteness / background noise trade-off that plagues fixed-radius approaches (Zhang et al., 2023), and the downstream detection gains support its effectiveness.

3. **DS score provides a practical unsupervised NMS surrogate.** The combined distribution constraint (modeling point-to-boundary distances as Gaussian) and meta-shape constraint (category-specific normalized dimensions) gives a quality metric for pseudo-labels when no ground-truth IoU is available (Section 3.4, Eq. 5–7). This is a non-trivial engineering contribution that makes the two-stage pipeline feasible.

4. **Large and consistent empirical gains.** Table 1 shows E3D improves CoIn++ average car AP by 14.31% at 2% annotation rate and CoIn by 36.92% at 0.1% annotation rate. These gains are substantial and validate the core thesis that LMM-derived pseudo-labels can boost feature discrimination under extreme sparsity.

5. **Practicality and reproducibility.** The method uses off-the-shelf LMMs without any additional fine-tuning and adopts standard detector backbones (VoxelRCNN, CenterPoint, CasA) within OpenPCDet, lowering the barrier for adoption.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies or component analysis anywhere in the main paper (or in the visible content).** The pipeline has three distinct modules (CPST, DCPG, DS score), multiple hyperparameters (γ, r_initial, δ, λ1, λ2), and design choices (mask shrink vs. no shrink, dynamic vs. fixed radius, DS score components). Without isolating the contribution of each component — e.g., removing CPST, using a fixed clustering radius, ablating one of the two DS score terms — the paper cannot demonstrate that each module justifies its complexity. The reported gains could plausibly come largely from the DS score or the mask shrink alone. This is the most significant weakness because it undermines attribution of the reported improvements.

2. **The distribution prior in the DS score (N(μ=0.8, σ=0.2)) and the meta-shape priors are cited from prior work but never validated on KITTI.** Section 3.4 states these are "inspired by (Luo et al., 2024)" and "followed this shape prior (Wu et al., 2024)," but the paper provides no evidence — not even a simple histogram or a table — that the actual point-to-boundary distance distribution in KITTI ground-truth boxes resembles N(0.8, 0.2), or that the adopted meta-shape templates match the KITTI statistics for cars, pedestrians, and cyclists. Since the DS score directly determines which pseudo-labels survive NMS and thus controls first-stage supervision quality, an inaccurate prior could systematically bias the training. A sensitivity analysis varying μ, σ, and the meta-shape dimensions would substantially strengthen the claims.

3. **No hyperparameter sensitivity analysis.** The paper sets γ=0.3, r_initial=1, δ=0.1, λ1=λ2=0.5 (Section 4, Implementation Details) without any analysis of how performance varies with these choices. While some hyperparameters are standard empirical choices, the DS score weights (λ1, λ2) and the shrink factor γ directly affect the quality and quantity of pseudo-labels and should be ablated.

### Minor

4. **The "zero-shot" framing is overstated.** The abstract claims the method is "verified ... in the zero-shot setting" where "without fine-tuning on labeled data, our E3D has shown superior performance compared to zero-shot methods." However, in this setting the detector is still trained on the target dataset (KITTI) using pseudo-labels generated from the same scenes — this is unsupervised/self-training adaptation, not zero-shot in the conventional sense (which implies no training on the target domain). The comparison is against methods that are truly zero-shot, making the framing asymmetrical and potentially misleading. The paper should either drop "zero-shot" or clearly define the setting as "pseudo-label pre-training without ground-truth labels."

5. **The relationship between CoIn and CoIn++ is never defined.** The abstract reports an 11.63% improvement over CoIn++, while the contributions section reports 14.89% improvement over CoIn at the same 2% rate. The paper never explains what CoIn++ adds over the original CoIn or why these baselines yield different improvement numbers. This creates unnecessary confusion even if the numbers are technically consistent (different baselines = different gains).

6. **Evaluation on only KITTI.** The method depends on 2D image availability and LMM quality. Testing on nuScenes or Waymo (which also provide images and have established sparsely-supervised baselines) would substantially strengthen generalization claims. As is, the method's broader applicability is unconfirmed.

7. **Quality analysis of seed points is missing.** The paper should report precision/recall of the LMM-generated seed points (after CPST mask shrink) against ground-truth object centers to show the CPST module actually provides accurate semantic transfer. Showing qualitative examples of successful and failed pseudo-labels would also be informative.

### Trivial

8. The paper mentions "CoIn++" in Section 4.1 without a formal definition or citation distinguishing it from CoIn — a single sentence of clarification would resolve this.

## Nice-to-Haves

- A component-level ablation study (remove CPST individually vs. DCPG vs. DS score) is needed for the paper to convincingly claim that all three modules contribute positively.
- A sensitivity analysis varying γ, λ1/λ2, and the DS score distribution parameters (μ, σ) would show the method is robust rather than brittle.
- Reporting variance across multiple random scene-selection seeds would address potential concerns about the limited split being unrepresentative.
- An analysis of the actual distribution of point-to-boundary distances on KITTI ground-truth boxes (even a small held-out set) to validate the N(0.8, 0.2) prior.

## Removed Points

These points are flagged as removed from the main review; treat them with caution.

- **"The DS score relies on arbitrary, unvalidated priors" (partially removed):** The priors are cited from published work (Luo et al., 2024; Wu et al., 2024), not "arbitrary." The criticism that they are unvalidated on KITTI is kept in Major Weakness #2, but the framing of "arbitrary" is removed as too strong given the citations.

- **"Inconsistency in baseline naming" (removed):** The numbers for CoIn (14.89% at 2%) and CoIn++ (11.63% at 2%) are for different baselines, which is expected. The paper should clarify the relationship, but there is no factual inconsistency. Moved to Minor Weakness #5 with corrected framing.

- **"Disconnect between motivation and mechanism" (Section 1 critique, removed):** The reviewer claims the LMMs only provide seed points while the real work is done by geometric clustering, but the paper's stated contribution is precisely that LMMs provide semantic prior knowledge for bootstrapping — not that LMMs perform clustering. The paper's motivation and mechanism are consistent.

- **"Comparison tables not visible" (removed):** This is a parser artifact (images not extracted from PDF), not an author error. The paper likely includes the tables in the original submission.

- **"Missing appendix" (removed per hard rules):** The parser strips these sections; they exist in the original submission.

- **Strength Finder strengths about "explicit semantic mask transfer avoids cross-modal feature confusion" and "uses off-the-shelf LMMs without fine-tuning":** Retained as Supporting Strengths #4 and #5. These are valid supporting points, not strong enough to be primary strengths but worth mentioning.

- **Strength Finder's "novel contribution to sparsely-supervised 3D detection" (about DS score replacing IoU for NMS):** This is kept as Strength #3.

## Novel Insights

The reviewers collectively surface an important tension: the paper's core innovation is using LMMs to provide semantic priors, yet the pseudo-label quality depends critically on geometric priors (Gaussian distribution of point-to-boundary distances, meta-shape templates) that are adopted from prior clustering/unsupervised detection work rather than from the LMMs themselves. This creates two distinct types of prior knowledge in the pipeline — semantic (from LMMs) and geometric (from hand-chosen distributions and template shapes) — and the paper never disentangles which contributes what. A deeper insight is that the method's success may depend more on the geometric priors (which have known applicability to KITTI's LiDAR point distribution) than on the LMMs, which primarily serve as a convenient source of 2D foreground segmentation. The paper would be stronger if it acknowledged and tested this separation explicitly.

## Suggestions

1. **Add component ablation.** This is the single most impactful improvement. Show E3D with: full pipeline, w/o CPST (use raw LMM masks), w/o DCPG (fixed-radius clustering), w/o DS score (no NMS filtering), and with each DS score term individually. This would transform the paper from "interesting but unvalidated pipeline" to "demonstrably well-designed framework."

2. **Validate or learn the DS score priors.** Either (a) compute the actual point-to-boundary distance distribution on a set of KITTI ground-truth boxes and show it approximates N(0.8, 0.2), or (b) treat μ, σ as learnable parameters or estimate them per-frame from the data, and show this improves or maintains performance.

3. **Clarify the "zero-shot" framing.** Replace "zero-shot setting" with "pseudo-label pre-training without ground-truth labels" or "unsupervised first-stage training." This is a simple fix that avoids potential criticism from the broader community.

4. **Clarify what CoIn++ is relative to CoIn** in one sentence, and use consistent notation throughout.

## Score and Decision

**Originality:** 6/10 — The idea of using LMMs to bootstrap pseudo-labels for sparsely-supervised 3D detection is novel, though each individual component (mask shrink, DBSCAN clustering, distribution-based filtering) draws from prior work.  
**Importance of question:** 7/10 — Reducing annotation cost for 3D detection is practically important and actively researched.  
**Claims well-supported:** 4/10 — The core claim that E3D improves sparsely-supervised detectors is supported by the KITTI results, but the lack of ablation and hyperparameter analysis means the attribution of these gains to specific proposed modules is unsubstantiated. The zero-shot framing is somewhat overstated.  
**Soundness of experiments:** 5/10 — Results are positive but incomplete: single dataset, no ablation, no sensitivity analysis, no variance reporting.  
**Clarity of writing:** 6/10 — The method descriptions are generally clear (modules are well-separated, equations are specified), but the CoIn/CoIn++ ambiguity and zero-shot framing create unnecessary confusion.  
**Value to community:** 6/10 — If validated with proper ablation, the pipeline could be practically useful; in its current form, the lack of validation limits confidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>