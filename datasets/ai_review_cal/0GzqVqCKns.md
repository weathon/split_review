- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the consolidated review.

---

## Summary

This paper proposes using forward-backward experiments in diffusion models as a probe for hierarchical latent structure in data. The authors derive a theoretical prediction — a diverging correlation length at the class phase transition — in a synthetic hierarchical model (the Random Hierarchy Model, RHM) using mean-field theory, and validate it numerically with Belief Propagation. They then apply the same measurement protocol to natural language (MDLM on WikiText-2) and images (DDPM on ImageNet with CLIP patch embeddings), reporting a peak in dynamical susceptibility at a finite inversion time in both modalities. The theoretical derivation is clean and the core idea is novel, but the evidence that the observed phenomena specifically indicate *hierarchical* (rather than merely clustered) structure in real data is incomplete.

## Strengths

1. **Clean theoretical derivation of a diverging correlation length in a hierarchical model.** Section 3.1 derives ξ ∼ |ε − ε\*|^{−ν} from a mean-field linearization of the iterative map F(p) (Eq. 8). This goes beyond prior work (e.g., Sclocchi et al. 2024) that identified the class phase transition but did not characterize the spatial structure of token changes. The prediction — that changes are correlated over a length scale diverging at the critical noise level — is explicit and testable.

2. **Quantitative numerical validation with Belief Propagation on the RHM.** Figure 2(a-I) shows system-spanning power-law correlation functions at the critical point with mean-field theory (dashed lines) falling on top of BP simulations (solid lines). The susceptibility peak in Figure 2(a-II) and the critical exponent test in Appendix (referenced) confirm quantitative agreement between theory and exact inference on the synthetic model. The same phenomenology is also validated under masking diffusion (Figure 2b), linking the theoretical ϵ-process to the practically used discrete diffusion.

3. **Novel experimental observations on natural language and images.** The paper is the first to apply this forward-backward correlation analysis to language data. Section 4 reports a clear susceptibility peak on WikiText-2 at t\* ≈ 0.6 T (Figure 3c), with maximal correlation extending 7–8 tokens. For images, the experiments on DDPM/ImageNet with CLIP patch embeddings (Figure 5ab) show a susceptibility peak at t\* ≈ 0.6–0.7 T and a system-spanning correlation function. These observations demonstrate that the predicted phenomenology generalizes beyond the synthetic RHM.

4. **Ruling out a trivial alternative explanation.** Section 3.3 compares the RHM to a Gaussian random field with power-law covariance and shows that, in that model, the correlation length grows monotonically with noise and is maximal at t = T — not at a finite critical point. This control establishes that the peaking behavior is not a trivial consequence of spatial correlations.

## Weaknesses

### Fatal

None.

### Major

1. **The susceptibility peak may not be uniquely diagnostic of hierarchy (missing baseline).** The paper argues that a peaking correlation length/susceptibility is a signature of hierarchical structure, and Section 3.3 rules out a Gaussian random field (no latent variables). However, the natural alternative baseline is a **simple mixture model with a single latent class variable** (e.g., a mixture of Gaussians). Prior work [Ambrogioni 2023, Biroli 2024] has shown that diffusion on such data exhibits a speciation/class transition. Since the susceptibility peak in the RHM coincides with the class transition, it is plausible that a single-level clustering model would also produce a peak — just at the level of the single latent class, without any multi-level hierarchy. The Gaussian random field comparison rules out unstructured spatial correlations, but not this more relevant alternative. The paper's related work claims these speciation works "do not present growing dynamical susceptibility or length scale at the transition" (line 399), but it does not experimentally verify this claim. Without the mixture baseline, the paper's central inference — that the observed peaks in text and images reflect *hierarchical* structure — is not uniquely supported. This is the most significant evidential gap.

2. **For text, the link between the susceptibility peak and a semantic/class transition is unverified.** In the RHM, the susceptibility peak coincides with a measurable phase transition in class reconstruction probability (p(x^{(L)}\_1 | x_t)). For images, Sclocchi et al. (2024) previously established a class transition at a similar inversion time, so the connection is plausible. For text, however, the paper provides no independent measure that the peak at t/T ≈ 0.6 corresponds to a change in interpretable high-level linguistic variables (e.g., topic, sentiment, or grammatical structure). The qualitative examples in Figure 3(a) are suggestive but not quantitative. Without a ground-truth latent variable or an independent semantic measure, the paper cannot confirm that the peak reflects hierarchical latent structure rather than some other property of the diffusion model or tokenizer. This weakens the claim that the susceptibility peak "establishes the existence of a phase transition for the language modality" (line 322).

### Minor

3. **The image analysis relies on CLIP embeddings without discussing potential confounds.** The paper uses CLIP ViT-B32 patch embeddings to define "tokens" for images, measuring correlations between the norms of embedding variations. Since CLIP's representation space already encodes high-level semantic information, the measured correlations could partially reflect the structure of the CLIP embedding space rather than the raw pixel distribution. The forward-backward diffusion happens in pixel space, and the CLIP embeddings are used only as a measurement tool, so this concern is not fatal — but the paper should discuss it. A brief acknowledgment or a pixel-level control (e.g., raw patches or wavelet coefficients) would strengthen the claim that the phenomenology is not an artifact of the chosen representation.

4. **No explicit correlation length extraction for image data.** For text, the paper reports a maximum correlation length of 7–8 tokens (line 322). For images, only the susceptibility and correlation functions are shown (Figure 5), but no effective correlation length is extracted (e.g., from an exponential fit or the integral of the correlation function). The theory predicts a diverging length ξ; showing that the extracted length peaks at t\* for real data would strengthen the match to the RHM prediction.

5. **The paper overstates the confirmation of theoretical predictions on real data.** The introduction and conclusion claim that the predictions are "confirmed" on text and images. However, the theory makes quantitative predictions about the critical exponent ν and the functional form of the correlation function — none of these are tested on real data. The real-data experiments only check for a qualitative peak in susceptibility, which is a weaker signature. This should be scoped more carefully.

### Trivial

6. **Correlation functions for text (Figure 3b) appear to show a secondary structure at high masking fractions.** The reviewer notes a possible secondary peak at r=1 for high t/T. The paper does not comment on this. This may be a finite-size or tokenization artifact, but it deserves a brief remark.

7. **Some experimental details (e.g., number of diffusion steps T, noise schedule, exact reverse sampling procedure) are deferred to the appendix.** A brief mention in the main text would improve readability.

## Nice-to-Haves

- Test a simple mixture model (e.g., mixture of Gaussians with well-separated components) to directly demonstrate that the susceptibility peak either does not arise or has a qualitatively different shape than in the hierarchical case. This is the most direct way to strengthen the claim that the method specifically probes hierarchy.
- For text, provide an independent measure that the peak corresponds to a semantic transition — e.g., use a text classifier to measure topic/semantic similarity between original and reconstructed text as a function of t, analogous to the class-reconstruction probability in the RHM.
- For images, consider a pixel-level analysis (e.g., patches of 8×8 pixels) as a control to verify the peak is not an artifact of the CLIP representation.
- Frame the contribution more precisely: the method may primarily probe the *top-level* class transition (rather than full multi-level hierarchy), which is still interesting and connects to prior theoretical work. The claim about probing "hierarchical" structure should acknowledge that the signature is consistent with hierarchy but not uniquely diagnostic without additional controls.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The paper would benefit from directly contrasting its method with the speciation crossover: how does a simple mixture produce a different correlation function shape than a deep hierarchy?"* — This is a suggestion for improvement, not a weakness. Moved to Nice-to-Haves.
- *"Details of the forward-backward sampling are missing from the main text."* — This is a presentation nitpick. The appendix exists in the original submission.
- *"The paper's later claim that 'our theoretical predictions' are confirmed on real data overstates the case"* — This is already covered in Weakness 5 (minor).
- Several formatting/style complaints and speculation about missing appendix content — removed per guidelines.
- Generic strength praise from the Strength Finder about "addressing an important problem" without specific evidence — removed as generic/superficial.

## Novel Insights

The most insightful observation from the review process is that the paper's central contribution may be best understood as a **method to detect and localize the class phase transition in diffusion models** — i.e., to determine at what noise level the top-level latent variable becomes unrecoverable — rather than as a method to specifically diagnose multi-level hierarchy. The theoretical machinery (mean-field analysis of the RHM, diverging correlation length) is valuable regardless of whether the real-data peaks turn out to uniquely indicate hierarchy. The paper could be reframed around this more modest but still significant claim without losing its impact.

## Suggestions

1. Add a mixture-of-Gaussians (or mixture-of-discrete-distributions) experiment to demonstrate that the susceptibility peak is not universal to any data with a clustering structure. Ideally, compare the shape of χ(t) and the correlation function C(r) between the mixture and the RHM.
2. For text, add an independent semantic similarity measure (e.g., cosine similarity of sentence embeddings between x₀ and x̂₀(t), or classifier-based topic probability) plotted against t to verify that the susceptibility peak coincides with a semantic transition.
3. For images, either add a pixel-level control experiment or explicitly discuss why the CLIP embedding confound does not undermine the conclusions.
4. Soften the central claim: state that the results are "consistent with" hierarchical structure rather than claiming the method "probes hierarchical latent structure" as a unique diagnostic.
