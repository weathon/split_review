Now I have a thorough understanding of both the paper and the reviews. Let me synthesize the final review.

## Summary

The paper introduces DeepSPF, a learnable patch-wise SO(3)-equivariant representation for point clouds. It proposes Spherical Patch Fields (SPF) to encode point clouds into multiple spherical Gaussian patches, and a Patch Gaussian Layer (PG-Layer) that preserves the SG form for deeper networks with adaptive receptive fields. The method is evaluated on three Scan-to-CAD tasks—registration, retrieval, and completion—showing consistent improvements when replacing standard encoders.

## Strengths

1. **Novel patch-wise extension of spherical Gaussian representations**: Unlike prior global spherical representations (Salihu & Steinbach 2023), SPF splits a point cloud into multiple learnable spherical patches and models inter-/intra-patch relationships via a graph (Eq. 3–6). This is a fundamentally new direction for combining local and global information while maintaining an equivariant property, grounded in Spherical Gaussians (Section 3.1).

2. **PG-Layer reformulates SG convolution to preserve the SG form for deeper networks**: The paper correctly identifies that prior SG convolutions (Salihu & Steinbach 2023) deform the SG representation, limiting them to a single layer. PG-Layer (Eq. 12–14) reformulates the convolution so the output remains a valid SG, enabling multiple successive layers. This is supported by experiments where DeepSPF outperforms methods using a single SG layer (Tables 1, 4).

3. **Adaptive patch radii for switching between local and global information**: The differentiable volume term V(r) (Eq. 7) lets PG-Layer shrink or expand each spherical patch based on local point density, a novel capability absent in fixed-size patch methods (Rao et al., 2022). Table 1 (conditions E, U, V) attributes improvements to this component.

4. **Consistent experimental gains across three S2C tasks**: The paper reports a reduction in rotation error for registration (Table 1: RRMSE from 4.54 to 3.78), a 17% improvement in Top-1 retrieval error (Table 4: from 0.714 to 0.591), and up to 33% reduction in Chamfer Distance for completion (Table 5: from 1.38 to 0.92). Results on real-world Scan2CAD (Table 3) confirm generalization beyond synthetic data.

5. **Plug-and-play compatibility**: DeepSPF replaces the PointNet encoder in DeepGMR (Tables 1–2) and PCN (Table 5), improving results without modifying the decoder or loss. This demonstrates versatility as a backbone.

## Weaknesses

### Fatal
None.

### Major

1. **The rotation-equivariance proof relies on an unsubstantiated approximation**. The core assumption $R_\nu \approx R_p$ (Eq. 9 and 11) is stated but never justified. The paper does not specify how the spherical sampling grid $\nu$ (generated via Vogel 1979) transforms when the input point cloud rotates. If $\nu$ is a fixed pre-computed grid (as the description suggests), the assumption $R_\nu \approx R_p$ has no mechanism to hold. The proof therefore does not establish exact SO(3)-equivariance, and the degree of approximation is not characterized. For a paper with "SO(3)-Equivariant" in its title, this is a significant theoretical gap. The method may still work empirically (and the experiments suggest it does), but the claimed property is not properly supported.

2. **No error bars, confidence intervals, or multi-seed statistics across all experiments**. Many reported values are very small (Chamfer distances on the order of $10^{-3}$), and differences of a few percent could arise from random variation. Without variance estimates over multiple runs (standard in the field for such metrics), the statistical significance of the claimed improvements cannot be assessed. This is especially important for Table 1 (ablation) and Table 4 (Top-1 error differences).

3. **The mathematical formulation has unresolved dimensional and notational ambiguities** that impede reproducibility:
   - Eq. (2) states $z \in \mathbb{R}^{|\nu| \times 3}$, but how the product $\mathrm{E}(\nu,p)\mathrm{V}(r)\mathrm{U}(P(\nu,p))e^{\lambda(\nu^T p-1)}$ closes dimensionally is never specified. The "$\cdot$" operation is not defined as element-wise, matrix-matrix, or some other operation.
   - In Eq. (3), $\phi$ and $\theta$ are described as "learnable parameters" in the text but used as functions in the equation; their exact form (MLPs? linear layers?) is not specified.
   - The Legendre polynomial derivation $P(\nu,p) = Y(\nu)\bar{Y}(p)$ evaluates spherical harmonics at 3D points $p$, but spherical harmonics are defined on $S^2$, not $\mathbb{R}^3$, and this conversion is unstated.
   
   These issues do not invalidate the core idea but make faithful re-implementation unnecessarily difficult.

4. **Missing comparison against VN-based methods for registration**. The paper cites VN (Deng et al., 2021) in the related work, claims "improvements over VN," and compares against VN-PointNet for completion (Table 5). However, the registration experiments (Tables 1 and 2) do not include VN-based baselines. Since VN is a well-known rotation-equivariant backbone with public implementations, its absence from the main registration comparisons weakens the claim that DeepSPF advances the state of the art for rotation-equivariant registration.

### Minor

1. **The parameter count claim is unsubstantiated**. The conclusion states that DeepSPF works "without increasing the number of parameters compared to similar state-of-the-art methods," but no parameter counts are provided anywhere in the paper. This claim is unverifiable.

2. **The PG-Layer $\lambda$ approximation is not justified**. The derivation (Eq. 14) assumes $\lambda_G \approx \lambda_H \approx 2\lambda_R$ without any justification or empirical validation. Additionally, the number of PG-Layers $m$ per SA layer (mentioned in Section 3.4) is never varied or ablated, so the claim that stacking PG-Layers yields improvements over a single layer is indirectly supported at best.

3. **The ablation is limited**. Table 1 tests conditions E, U, V on only one dataset (ModelNet40) and one metric set. Moreover, condition "U" bundles the Legendre polynomial term with edge function changes, so the contribution of low-frequency information alone is not isolated. Architectural choices (number of PG-Layers $m$, initial radius values, patch count $f_{no}$) are not ablated.

4. **Inference time R is listed as a metric (Section 4.3) but never reported** in any table. Compute time comparisons would be valuable for a method that adds patch-wise processing.

### Trivial
None.

## Nice-to-Haves

- Provide pseudo-code or a detailed algorithm box for generating SPF features from a point cloud to improve reproducibility.
- Add an ablation removing the Legendre term while keeping the edge function and volume adjustment, to isolate the effect of low-frequency information.
- Add a small-scale study varying the number of PG-Layers to validate the claim that deeper SG networks improve results.

## Removed Points

- **"The paper does not specify which results are from original papers and which are re-trained"**: The paper states this clearly in Section 4.2 ("All results are either taken directly from the respective work or re-trained with the preferred configurations"). This is a standard disclosure; the reviewer's concern is addressed.

- **"The retrieval evaluation describes SVD without discussing validity"**: The retrieval procedure (cross-covariance → SVD → transformation → Chamfer distance) follows the established protocol of Zhao et al. (2021) and Salihu & Steinbach (2023). It is a reasonable approach for this task, and the reviewer's concern about validity is not substantiated by a concrete flaw.

- **"The paper does not compare against VN for retrieval"**: The reviewer's criticism was specifically about registration (Tables 1, 2). For retrieval, the paper follows the protocol of Zhao et al. (2021)/Salihu & Steinbach (2023), which does not include VN. Scope-creeping to add VN for retrieval is not a fair demand.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the equivariance proof**: Either provide a clean argument for exact equivariance (specifying how $\nu$ transforms when the input rotates) or explicitly characterize the method as approximately equivariant with error bounds. This is the single most important revision.

2. **Add statistical rigor**: Report means and standard deviations over at least 3 random seeds for all quantitative results, especially for the small-magnitude differences in Tables 1 and 4.

3. **Clarify dimensional arithmetic**: Rewrite Eq. (2) with explicit tensor shapes for each term and specify the operation types (element-wise, matrix multiplication, etc.).

4. **Provide parameter counts** for DeepSPF and all compared baselines to substantiate the claim about parameter efficiency.

5. **Include VN-based comparisons for registration** or explicitly acknowledge the missing comparison and justify why it was not performed.

6. **Report inference time R** as promised in the metrics section.

## Score and Decision

Assigning score: The paper proposes a genuine architectural innovation (patch-wise SG representation with adaptive radii and graph-based inter-patch communication) and demonstrates consistent empirical improvements across three tasks. However, the equivariance claim is not properly justified (a central advertised property), the mathematical presentation has significant gaps, and the experiments lack statistical rigor. These are not fatal issues — the core method and empirical results hold value — but they are substantive enough to require major revision before the paper meets the bar for acceptance at a top venue.

Score: 5.5 (borderline weak accept — the contribution is real but the theoretical and presentational problems are significant)

Actually, let me reconsider. The FUNDAMENTAL ISSUES rule says: "If any weakness is severe enough to undermine the paper's core claims or it is simply 'not even a paper', it overrides all strengths." The equivariance issue is significant but doesn't invalidate the core contribution (the method works empirically). The paper is a real paper with real experiments. I'll assign a score that reflects the gap between the advertised property (exact equivariance) and what is actually established (approximate equivariance at best).

Score: 5.0 — The paper has a genuine contribution (the patch-wise approach and PG-Layer), but the equivariance claim is overstated without proper justification, and the experimental methodology lacks statistical rigor. These are correctable issues that should be addressed before acceptance.

Hmm, but the paper DID show improvements. Let me think about this more carefully.

The equivariance issue: The paper's title says "SO(3)-Equivariant." The proof is incomplete. This is a significant weakness. But the method still works. And the reviewer also noted the paper could be about approximate equivariance.

I think a score of 5.0 is appropriate. The paper has real contributions but has significant issues that need major revision.

Actually, let me reconsider once more. Looking at the typical review scale:
- 1-3: Strong reject
- 4-5: Weak reject / borderline
- 6-7: Accept
- 8-10: Strong accept

With equivariance being incomplete and math being ambiguous, I'd say:
- The paper has a real contribution (the method works empirically, as demonstrated across 3 tasks)
- But the theoretical foundation is shaky and presentation is unclear
- The missing baselines and error bars weaken but don't invalidate the results

I'll give 5.5, borderline accept with major revisions needed.

Actually, you know what, let me be more decisive. The experimental results across 3 tasks with consistent improvements are compelling. The main issue is the equivariance claim being stronger than what's proven. The paper needs to revise the equivariance section, clarify the math, and add error bars. These are fixable in revision.

Score: 5.0 (weak reject / borderline). The contribution is genuine but the presentation gaps and unsubstantiated equivariance claim are significant enough that I lean towards requiring major revision before acceptance.

Let me go with 5.5 — borderline. The contributions outweigh the weaknesses but the weaknesses are real.

Final decision: Accept, with major revisions required.

Wait, the rules say to be honest about the assessment. Let me re-assess:

The paper claims "SO(3)-Equivariant" in the title. The equivariance proof has a gaping hole. If the method is not exactly equivariant (only approximately), the title is misleading. This IS a significant issue. But does it invalidate the contribution? The method still shows empirical improvements. The contribution is the patch-wise approach and PG-Layer, not just the equivariance.

I'll go with score 5.0 and decision borderline/reject-with-revision-needed.

Actually I need to round to .5 or .0. Let me go with 5.0.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>

Hmm, actually the rules say "Score round to .5 or .0." and I need to assign Accept or Reject. Let me think about this again.

The paper has genuine contributions (patch-wise SG representations, PG-Layer for deeper networks, adaptive radii). The experiments show improvements across 3 tasks. But the equivariance claim is not properly supported, the math is ambiguous, and the experiments lack error bars.

I think this is a borderline paper. It has real contributions that could be accepted after significant revision. But in its current form, there are too many unaddressed issues. I'll lean reject but acknowledge the contributions.

Score: 5.0, Decision: Reject (with encouragement to revise and resubmit)

Actually, re-reading the rules: "Similarly, if the paper made real contributions do not reject just because it has some weaknesses - every paper has some."

But the equivariance issue is not "some weakness" - it's a central advertised property that isn't properly justified. Combined with unclear math and missing error bars, I think reject is appropriate for the current version.

Let me finalize.Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper introduces DeepSPF, a learnable patch-wise SO(3)-equivariant representation for point clouds based on Spherical Patch Fields (SPF) and a Patch Gaussian Layer (PG-Layer) that preserves the Spherical Gaussian form for deeper networks with adaptive receptive fields. The method is evaluated on three Scan-to-CAD tasks—registration, retrieval, and completion—showing consistent improvements when replacing standard encoders (e.g., PointNet) in existing pipelines.

## Strengths

1. **Novel patch-wise extension of spherical Gaussian representations**: Unlike prior global spherical representations (Salihu & Steinbach 2023), SPF splits a point cloud into multiple learnable spherical patches and models inter-/intra-patch relationships via a graph (Eq. 3–6). This enables combining local and global information while maintaining an equivariant property, grounded in Spherical Gaussians (Section 3.1).

2. **PG-Layer enables deeper SG-based networks**: The paper correctly identifies that prior SG convolutions (Salihu & Steinbach 2023) deform the SG representation, limiting them to a single layer. PG-Layer (Eq. 12–14) reformulates the convolution so the output remains a valid SG, enabling multiple successive layers. This architectural contribution is supported by experiments where DeepSPF outperforms methods using a single SG layer (Tables 1, 4).

3. **Adaptive patch radii for local-to-global information**: The differentiable volume term V(r) (Eq. 7) allows each spherical patch to expand or shrink based on local point density, going beyond fixed-size patches (Rao et al., 2022). Table 1 (conditions E, U, V) attributes improvements to this component.

4. **Consistent empirical gains across three S2C tasks**: The paper reports a reduction in rotation error for registration (Table 1: RRMSE from 4.54 to 3.78), a 17% improvement in Top-1 retrieval error (Table 4), and up to 33% reduction in Chamfer Distance for completion (Table 5). Results on real-world Scan2CAD (Table 3) confirm generalization beyond synthetic data.

5. **Plug-and-play compatibility**: DeepSPF replaces the PointNet encoder in DeepGMR (Tables 1–2) and PCN (Table 5), improving results without modifying the decoder or loss functions.

## Weaknesses

### Fatal
None.

### Major

1. **The rotation-equivariance proof relies on an unjustified approximation.** The core assumption $R_\nu \approx R_p$ (Eq. 9 and 11) is stated but never justified. The paper does not specify how the spherical sampling grid $\nu$ (generated via Vogel 1979) transforms when the input rotates. If $\nu$ is a fixed pre-computed grid—as the description of it being generated by Vogel's method for sampling $S^2$ suggests—there is no mechanism for $R_\nu \approx R_p$ to hold. The proof therefore does not establish exact SO(3)-equivariance, and the degree of approximation is not characterized or bounded. For a paper with "SO(3)-Equivariant" in the title and a method that uses FPS (which is itself not rotation-equivariant) for center selection, this is a significant gap between advertised and established properties. The empirical results suggest the method works well, but the theoretical claim is not properly supported.

2. **No error bars or multi-run statistics across any experiment.** Many reported values are small (Chamfer distances on the order of $10^{-3}$), where differences of a few percent could arise from random variation. Without variance estimates—which are standard for such metrics in the field—the statistical significance of the claimed improvements cannot be assessed. This is particularly important for the ablation results (Table 1) and the Top-1 retrieval differences (Table 4).

3. **Mathematical formulation has unresolved dimensional and notational ambiguities** that impede reproducibility:
   - Eq. (2) states $z \in \mathbb{R}^{|\nu| \times 3}$, but the "$\cdot$" product among $\mathrm{E}(\nu,p)$, $\mathrm{V}(r)$, $\mathrm{U}(P(\nu,p))$, and $e^{\lambda(\nu^T p-1)}$ is never specified as element-wise, matrix-matrix, or otherwise. The dimensional arithmetic required to produce $\mathbb{R}^{|\nu| \times 3}$ is not shown.
   - In Eq. (3), $\phi$ and $\theta$ are described as "learnable parameters" in the text but used as functions; their exact form (MLPs? linear projections?) is unspecified.
   - The Legendre polynomial term $P(\nu,p) = Y(\nu)\bar{Y}(p)$ (Eq. 8) evaluates spherical harmonics at 3D points $p$, but spherical harmonics are defined on $S^2$, not $\mathbb{R}^3$, and this conversion is unstated.

   These issues do not invalidate the core idea but make faithful re-implementation unnecessarily difficult for a paper aiming to introduce a new representation.

4. **Missing comparison against VN-based methods for registration.** The paper cites VN (Deng et al., 2021) in the related work, claims "improvements over VN," and compares against VN-PointNet for completion (Table 5). However, the registration experiments (Tables 1 and 2) do not include VN-based baselines. Since VN is a well-known rotation-equivariant backbone with public implementations, its absence from the main registration tables weakens the claim that DeepSPF advances the state of the art in equivariant point cloud processing.

### Minor

1. **The parameter count claim is unsubstantiated.** The conclusion states DeepSPF works "without increasing the number of parameters compared to similar state-of-the-art methods," but no parameter counts are provided anywhere in the paper for DeepSPF or any baseline.

2. **The PG-Layer $\lambda$ approximation is not justified**, and the number of PG-Layers $m$ is not ablated. The derivation (Eq. 14) assumes $\lambda_G \approx \lambda_H \approx 2\lambda_R$ without justification or empirical validation. The architecture mentions $m$ PG-Layer modules per SA layer, but $m$ is never varied or reported.

3. **The ablation is limited.** Table 1 tests conditions E, U, V on only one dataset (ModelNet40). Condition "U" bundles the Legendre polynomial term with the edge function, so the contribution of low-frequency information alone is not isolated. Architectural choices (number of PG-Layers, initial radii, patch count $f_{no}$) are not ablated.

4. **Inference time R is listed as a metric (Section 4.3) but never reported** in any table. This is a useful comparison for a method adding patch-wise computation.

### Trivial
None.

## Nice-to-Haves

- Provide pseudo-code or an algorithm box for generating SPF features to improve reproducibility.
- Add an ablation removing the Legendre term while keeping the edge function and volume adjustment, to isolate the effect of low-frequency information.
- Vary the number of PG-Layers in a small-scale study to validate the claim that deeper SG networks improve results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Does not specify which results are from original papers vs re-trained"**: The paper states this clearly in Section 4.2 ("All results are either taken directly from the respective work or re-trained with the preferred configurations"). This concern is already addressed by the paper.
- **"Retrieval evaluation validity not discussed"**: The retrieval procedure (cross-covariance → SVD → transformation → Chamfer distance) follows the established protocol of Zhao et al. (2021) and Salihu & Steinbach (2023). The reviewer's concern is not substantiated by a concrete flaw.
- **"Missing VN comparison for retrieval"**: The reviewer's original criticism targeted registration (Tables 1, 2); the retrieval evaluation follows a different protocol where VN is not a standard baseline. Expanding to retrieval is scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the equivariance proof**: Either provide a clean argument for exact equivariance (specifying how $\nu$ transforms with the input) or explicitly characterize the method as approximately equivariant with error bounds. This is the single most critical revision.

2. **Add statistical rigor**: Report means and standard deviations over at least 3 random seeds for all quantitative results, especially for small-magnitude differences (Tables 1 and 4).

3. **Clarify dimensional arithmetic**: Rewrite Eq. (2) with explicit tensor shapes for each term and specify operation types (element-wise, matrix multiplication, etc.).

4. **Provide parameter counts** for DeepSPF and all compared baselines.

5. **Include VN-based comparisons for registration** or explicitly acknowledge the limitation and justify why the comparison was not performed.

6. **Report inference time R** as promised in the metrics section.

## Score and Decision

This paper proposes a genuinely novel architectural direction (patch-wise SG representation with adaptive radii and graph-based inter-patch communication) and backs it with consistent empirical improvements across three tasks. However, the central advertised property of SO(3)-equivariance is not properly established—the proof relies on an unjustified approximation—and the mathematical presentation has significant gaps that hinder reproducibility. The absence of error bars further limits confidence in the quantitative claims. These issues are correctable with major revision, but the current version does not fully support its advertised claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>