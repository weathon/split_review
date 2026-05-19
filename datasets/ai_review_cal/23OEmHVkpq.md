- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
I have thoroughly read the paper and verified all reviewer claims against the actual paper content. Here is my consolidated review.

---

## Summary

The paper proposes TopDis (Topological Disentanglement), a method that adds a topological loss term (based on Representation Topology Divergence / RTD) to VAE-based models to encourage disentangled representations. The key idea is to penalize topological dissimilarity between reconstructions of original and group(oid)-shifted latent codes, with gradient orthogonalization to preserve reconstruction quality. Experiments span 5 VAE variants × 4 benchmark datasets × 4 metrics, plus a correlated-factors experiment and a StyleGAN direction-discovery extension.

## Strengths

- **First differentiable topological loss for disentanglement.** The paper introduces a genuinely novel approach — using persistent-homology-based topological dissimilarity (RTD) as a differentiable regularizer for disentanglement. This is a creative departure from the dominant statistical-independence paradigm and is explicitly distinguished from prior topological work (Moor et al., 2020, which applied topological loss to autoencoders for a different purpose). (Supporting: abstract, Section 4.3, Algorithm 2)

- **Broad empirical coverage across model families.** The evaluation combines 5 base VAE variants (β-VAE, FactorVAE, β-TCVAE, ControlVAE, DAVA) × 4 standard disentanglement datasets (dSprites, 3D Shapes, 3D Faces, MPI 3D) × 4 metrics (FactorVAE score, MIG, SAP, DCI), totaling 80 comparison pairs. The TopDis variant improves over its base counterpart in the large majority of these cases. (Supporting: Table 1, lines 254–334)

- **Mathematically principled shift operation.** Propositions 1 and 2 (Section 4.2) formally show that the proposed inverse-CDF shift (Equation 1) preserves the Gaussian prior and that such shifts preserving the aggregate posterior imply a factorized posterior — connecting the topological loss to the standard disentanglement definition. (Supporting: lines 171–188)

- **Extension beyond VAEs.** The StyleGAN experiment (Section 5.4) demonstrates that the topological loss can discover disentangled directions in a pretrained GAN, showing the idea's versatility beyond the VAE framework the paper focuses on. (Supporting: lines 404–416, Figure 5)

## Weaknesses

### Fatal
None. The paper's core idea is valid and the experiments are executed; the issues below are major but addressable.

### Major

- **No explanation of how RTD is made differentiable.** The paper centrally claims a "differentiable topological loss" (abstract, line 5) and backpropagates through it (Section 4.3, gradient orthogonalization on lines 248–252), but never explains how RTD — which involves computing persistent homology / R-Cross-Barcodes — is differentiated. Persistent homology barcodes are piecewise-constant; backpropagation through them requires specialized approximations (e.g., Carrière et al., 2017, or recent differentiable topology frameworks). The paper cites no such technique and provides no derivation. This is a critical gap: without this explanation, the central technical claim of the paper ("first differentiable topological loss for disentanglement") is unsubstantiated and the method cannot be understood or reproduced.

- **No ablation or sensitivity analysis.** The method has multiple free components: the shift scale `C`, the exponent `p` in RTD (1 vs. 2), the gradient orthogonalization, the weight `γ` on the topological loss, and the option to compute RTD in pixel space vs. a representation space. None of these are ablated, making it impossible to attribute the observed improvements to the topological reasoning versus side effects of generic regularization. A non-topological baseline (e.g., replacing RTD with L2 distance between original and shifted reconstructions) is also absent. (No ablation section exists in the paper.)

- **No reconstruction quality metrics reported, despite claiming preservation.** The abstract and Section 4.4 claim that the method "preserves the reconstruction quality" and that gradient orthogonalization improves it. However, no reconstruction quality metrics (MSE, FID, LPIPS, PSNR) are reported anywhere in the paper for any model. Without this evidence, the claim is unverifiable, and it is possible that the disentanglement improvements come at the cost of reconstruction quality — a known trade-off the paper itself acknowledges (line 56, line 248).

- **Missing hyperparameter details needed for reproducibility.** The paper does not report learning rate, optimizer, batch size, number of epochs, encoder/decoder architecture details, the shift scale `C`, or the weight `γ` for each base model. Only the latent dimensionality (10) is stated (line 353). These omissions make it very difficult to reproduce the results or build on the method.

- **"State-of-the-art" claim is not fully supported by the comparison structure.** The primary comparison in Table 1 is within-family (base vs. base+TopDis). While blue entries mark the overall best method per (dataset, metric), many non-TopDis baselines achieve comparable scores within one standard deviation (e.g., β-TCVAE on dSprites MIG: 0.332 vs. β-VAE+TopDis: 0.348; β-VAE on 3D Faces DCI: 0.873 vs. β-VAE+TopDis: 0.854). The 94% figure mixes cases where improvement is genuine with cases where the base model already achieves ceiling (e.g., all models score 1.0 on 3D Faces FactorVAE score) and cases where TopDis slightly decreases performance. The aggregate claim overstates the consistency of benefit.

- **Many improvements are modest and within noise.** Several reported gains are within one standard deviation (e.g., FactorVAE dSprites FactorVAE score: 0.819±0.028 → 0.824±0.038; β-TCVAE dSprites MIG: 0.332±0.029 → 0.341±0.021). The large relative gains (e.g., +100% SAP) come from very low absolute baselines (DAVA SAP: 0.024→0.048). No statistical significance testing or confidence intervals for the differences are provided.

### Minor

- **Disconnect between the Lie group(oid) formalism and the implemented algorithm.** Section 4.1 introduces a definition of disentangled representation via Lie group(oid) actions, equivariance, and decomposition into 1-parameter subgroups. These conditions are stated but never verified or enforced in practice — the algorithm simply penalizes topological divergence after one random shift. The formalism feels like a post-hoc justification rather than a design principle, and the paper would be clearer if it led with the simple geometric intuition (lines 37–38) rather than the heavy theoretical machinery.

- **Qualitative traversals are anecdotal and not quantitatively compared.** The qualitative evaluation (Section 5.1.2, Figure 4) shows a few example traversals for FactorVAE vs. FactorVAE+TopDis but does not include traversals from other methods under the same conditions, nor any quantitative measure of traversal quality.

- **No explicit limitations section.** The paper concludes by mentioning limitation to the image domain but does not discuss limitations such as sensitivity to hyperparameters, computational cost of RTD, dependence on reconstruction quality, or the fact that only a single random shift per batch is used. A brief limitations section would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- Reporting training time / runtime analysis for the RTD computation, which involves neighborhood graph construction and persistent homology.
- Exploring sensitivity to latent dimensionality (the paper uses 10, standard in the field, but does not justify this choice or test alternatives).
- Reporting confidence intervals or p-values for the differences between TopDis and baseline models.
- Computing RTD in a feature space (e.g., DINO features) for complex images, as the paper notes is possible (footnote, line 225) but does not test.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Related work discussion of Locatello et al. is too brief."** — The paper explicitly addresses this point in lines 35–36, stating that statistical impossibility results do not apply because the method uses active intervention. Whether this argument is fully convincing is a matter of judgment, not a factual weakness.
- **"The paper does not state whether published hyperparameters were used or if the authors performed separate tuning."** — While hyperparameters are indeed missing, the specific concern about discrepancy between 0.819 and ~0.83 for FactorVAE on dSprites is speculative without access to the original publication's numbers.
- **"No justification of latent dimensionality choice."** — Latent dim=10 is standard practice in the disentanglement literature (Locatello et al., 2019; Kim & Mnih, 2018). Demanding a fresh justification for a standard choice is scope creep.
- **"The 94% figure mixes apples and oranges."** — The 94% figure (15/16) is mathematically correct given the paper's stated comparison basis (best variant per dataset/metric pair). The critic's deeper point about ceiling cases is valid and is retained in the Major weaknesses; the "apples and oranges" framing exaggerates the issue.
- **"The StyleGAN experiment adds nothing" / "purely qualitative."** — The paper explicitly states it does not claim superiority over GANSpace/SeFa (line 416) and frames it as a demonstration of applicability. Criticizing it for not being a full comparison is scope creep.
- **Generic criticisms about "evaluation lacking rigor," "baselines may not be fair," "confounders not controlled."** — These are area-of-concern sweeps without specific anchors in the paper and are removed per the filtering rules.
- **"No limitations section."** — Moved to Minor (genuinely worth noting, but a presentational issue).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the method or its implications that the paper itself does not already convey. The key criticism — that the differentiability claim is unsubstantiated — is a gap in the paper's exposition, not a novel insight about disentanglement or topology.

## Suggestions

1. **Explain RTD differentiability explicitly.** Dedicate a paragraph (or a supplementary section) to how gradients flow through the R-Cross-Barcode computation. Cite the relevant differentiable-topology literature (e.g., Carrière et al., 2017; the dglloss framework; or any smooth approximation used). Without this, the central technical claim is unverifiable.

2. **Add a comprehensive ablation study.** At minimum, ablate: (a) TopDis without gradient orthogonalization, (b) gradient orthogonalization with a non-topological regularizer in place of TopDis, (c) different values of `C` and `γ`, (d) `p=1` vs. `p=2`, and (e) a simple non-topological baseline (e.g., L2 or perceptual distance between original and shifted reconstructions).

3. **Report reconstruction quality metrics.** Include FID, LPIPS, or at minimum MSE/PSNR for all models in Table 1. The abstract and Section 4.4 make explicit claims about reconstruction quality that are currently unsupported.

4. **Document all hyperparameters.** Provide a table with learning rate, optimizer, batch size, epochs, architecture details, shift scale `C`, and weight `γ` for each base model.

5. **Tone down the "state-of-the-art" language.** Reframe the claim as: "TopDis consistently improves disentanglement metrics when added to existing VAE-based methods, and often achieves the best results among compared variants." This is accurate and avoids overclaiming.
