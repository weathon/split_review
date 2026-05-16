Now I have all the information I need. Let me construct the final review.

## Summary

The paper proposes TopDis, a differentiable topological loss term for disentangled representation learning in VAEs. The key idea is to encourage the learned representation such that shifting along a latent dimension produces a reconstruction whose multi-scale topological structure (measured by RTD) is similar to the original reconstruction. The loss is added to standard VAE-based objectives, and gradient orthogonalization is used to prevent degradation of reconstruction quality. Experiments across 6 VAE variants, 4 benchmark datasets, and 4 metrics show consistent improvements, and the method also extends to discovering directions in pretrained GANs.

## Strengths

- **Novel and principled approach**: TopDis is the first differentiable topological loss designed specifically for disentanglement learning. The connection between topological preservation under latent traversal and the continuity/invertibility of symmetry transformations (Section 4.1) provides a non-statistical theoretical motivation that is distinct from the existing independence-based approaches.

- **Consistent empirical improvements across broad baselines**: Table 1 shows that adding TopDis improves FactorVAE score, MIG, SAP, and DCI in the vast majority (94%) of 120+ configurations spanning 6 base methods (β-VAE, FactorVAE, β-TCVAE, ControlVAE, DAVA) and 4 datasets (dSprites, 3D Shapes, 3D Faces, MPI 3D). Many improvements are substantial (e.g., +70% MIG, +110% SAP on MPI 3D). No other regularizer has been shown to generalize this broadly across models and datasets.

- **Effectiveness when factors are correlated**: The paper explicitly tests the correlated-factors setting (Table in supplement), where statistical-independence-based methods are known to struggle. TopDis improves all metrics here, demonstrating robustness beyond what factorized-prior methods can offer.

- **Gradient orthogonalization is a practical contribution**: The orthogonal projection of the TopDis gradient onto the reconstruction loss gradient (Section 4.4) is a principled way to mitigate the known reconstruction-disentanglement trade-off, and is computationally lightweight.

- **Extends beyond VAEs**: The StyleGAN experiment (Section 5.3) shows that the topological dissimilarity objective can discover meaningful disentangled directions even in unconditional GANs, suggesting broader applicability.

## Weaknesses

### Fatal
None.

### Major
- **The "state-of-the-art" claim is over-extrapolated from the presented evidence.** The abstract and contribution list state that TopDis "improves disentanglement scores ... with respect to state-of-the-art results," and Section 5 states "We compare the results obtained by our method with the state-of-the-art models." However, Table 1 only compares each base method *with* versus *without* TopDis — it does not include a column of published best-known SOTA numbers for these benchmarks. The base methods (FactorVAE, β-TCVAE, etc.) are indeed SOTA models, so the relative improvement claim is partially supported. But without external reference numbers, the reader cannot assess whether, e.g., β-VAE+TopDis (DCI 0.506 on dSprites) is competitive with the best published results on that dataset. The paper would significantly strengthen its claim by either adding a SOTA baseline column or qualifying the language to "improves over strong baselines."

- **Critical hyperparameter details are absent from the main text, impairing reproducibility.** The objective is ℒ = ℒ_VAE-based + γ ℒ_TD (Eq. 4), and Algorithm 1 includes the shift magnitude C. The paper does not state what values of γ or C were used, whether they were tuned per method/dataset or held constant, or whether the base methods' own hyperparameters (β for β-VAE, discriminator settings for FactorVAE) were re-tuned after adding TopDis. The sentence "Since the quality of disentanglement has high variance w.r.t." (line 353) is truncated by a parser artifact, but even accounting for this, no explicit values or ranges are given. Without this information, the results cannot be reproduced and the possibility of implicit tuning advantage cannot be ruled out.

- **Gap between the formal definition and the actual algorithm creates a misleading theoretical narrative.** Section 4.1 presents a definition of VAE-based disentangled representations in terms of Lie group(oid) actions, equivariance of encoder/decoder, and a decomposition G = G₁×…×Gₙ. However, the TopDis loss does not enforce any of these properties directly — it only measures RTD between original and shifted reconstructions. The loss encourages the decoder's output to be topologically consistent under traversal, which is a *consequence* of the formal definition (continuity + invertibility → topological preservation) but is neither necessary nor sufficient for it. The paper would be more coherent if it explicitly framed TopDis as encouraging a smoothness/topological-consistency property that is *desirable* for disentanglement, rather than presenting the group-action apparatus as if the loss enforces it. Propositions 1-2 are correct and useful, but they address the shift mechanism, not the connection between RTD and the formal definition.

### Minor
- **Percentage improvements on near-zero baselines are misleading.** e.g., "+100% SAP on dSprites" sounds dramatic but reflects an improvement from 0.045 (β-TCVAE) to 0.090 (β-TCVAE+TopDis) — still a very small absolute value. Reporting absolute deltas alongside (or instead of) percentages would be more informative.

- **Gradient orthogonalization is listed as a contribution but not ablated.** The paper presents the orthogonalization trick (Section 4.4) as a key enabler but does not compare results with vs. without it. Without this ablation, the reader cannot determine how much of the improvement comes from TopDis itself versus the orthogonalization mechanism.

- **Lack of statistical significance testing.** Several comparisons in Table 1 have overlapping confidence intervals (e.g., FactorVAE vs. FactorVAE+TopDis on dSprites for FactorVAE score: 0.819±0.028 vs. 0.824±0.038). A paired test or bootstrap would help establish whether the observed improvements are reliable beyond seed variation.

- **The distinction from Moor et al. (2020) is insufficient.** The Related Work mentions Moor et al.'s topological loss for autoencoders but does not explain how TopDis differs (TopDis compares original vs. shifted *reconstructions* to encourage disentanglement; Moor et al. compare data vs. latent topology for representation quality). A brief comparison would help readers understand the novelty.

- **The StyleGAN experiment's search procedure is underspecified.** Section 5.3 states that principal components were optimized but does not describe the optimization objective, search strategy, or hyperparameters used. While the paper appropriately caveats this as a qualitative demonstration, the lack of detail limits its usefulness for practitioners.

- **For CelebA, it is unclear whether RTD was computed in pixel space or a representation space.** The footnote in Section 4.3 mentions that "for complex images, RTD can be calculated in a representation space," but the paper does not specify what was done for CelebA. If pixel space was used, the topological signal may be dominated by low-level statistics rather than semantic factors.

### Trivial
- "TopDiss" typo on line 386 (should be "TopDis").

## Nice-to-Haves
- An ablation comparing RTD against simpler distance measures (Chamfer, MMD, Euclidean) would isolate whether multi-scale topological information is specifically valuable or whether any proximity-preserving loss works.
- Reconstruction quality metrics (MSE, SSIM, ELBO) for a representative subset of experiments would substantiate the claim that TopDis preserves reconstruction quality.
- Runtime comparison against base VAE training would help practitioners assess computational cost.
- A brief hyperparameter sensitivity analysis (γ, C) would increase confidence in the robustness of the results.

## Removed Points
- **"Circular argument" criticism (Point 3 from harsh critic):** The reviewer claimed the theoretical motivation is circular (the method assumes symmetries exist to learn symmetries). This is a misunderstanding. The paper motivates TopDis by noting that *if* a representation is disentangled, topological preservation follows from continuity/invertibility of the traversal transformation — it does not assume the symmetries exist. The loss then *encourages* this property during training, which is standard regularization logic. The real issue (which is kept above) is the gap between the full formal definition and what the loss actually enforces.
- **Criticism about missing appendix content (correlated-factors table, VAE results table):** These are parser artifacts — the appendix and supplementary material were stripped during extraction but exist in the original submission.
- **Criticism about latent dimensionality choice (10) being non-standard:** A 10-dimensional latent is the standard in the disentanglement literature for these benchmarks. This is a nitpick.
- **Criticism about not comparing to published SOTA numbers as a "fatal flaw":** The base methods are themselves SOTA models, so the within-pair comparisons are meaningful. The issue is one of overclaiming and missing context, not invalidity of results. Moved to Major with softened language.

## Novel Insights

The reviewers surface an interesting tension: the paper's theoretical apparatus (group actions, equivariance, decomposition) suggests a stronger mathematical framework than the actual TopDis loss delivers. This points to an opportunity — could the TopDis loss be augmented to more directly enforce aspects of the formal definition (e.g., by checking that traversals along different latent dimensions commute, or by measuring equivariance violation)? The current work would be stronger if it acknowledged this gap explicitly and positioned TopDis as a practical proxy that captures *one* necessary condition (topological consistency under traversal) rather than as an instantiation of the full definition.

## Suggestions

1. **Qualify the SOTA claim.** Replace "improves ... with respect to state-of-the-art results" with "consistently improves strong baseline methods including FactorVAE, β-TCVAE, ControlVAE, and DAVA." If feasible, add a column with published SOTA numbers for context.
2. **Report hyperparameter values.** State the specific γ and C values used, whether they were tuned per method/dataset, and whether base-method hyperparameters were re-optimized after adding TopDis.
3. **Ablate gradient orthogonalization.** Add a small table showing TopDis ± orthogonalization for at least one dataset to establish its necessity.
4. **Reframe the theoretical motivation.** Either remove the full formal definition (items 2-4 in Section 4.1) and simply state the topological-preservation intuition, or explicitly explain that TopDis encourages one necessary condition of the definition without enforcing the full equivariance structure.
5. **Report absolute deltas alongside percentages** for near-zero baseline improvements, and add statistical significance tests for key comparisons where confidence intervals overlap.

## Score and Decision

The paper presents a genuinely novel idea (topological regularizer for disentanglement) with broad and consistent empirical support across multiple frameworks. The core contribution is solid. However, the overclaimed SOTA language, missing hyperparameter details, and gap between the theoretical framing and the algorithm are real concerns that prevent the paper from being accepted as-is. None of these issues are fatal — they are addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>