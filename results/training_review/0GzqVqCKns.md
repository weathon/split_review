Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

This paper proposes using dynamical susceptibility (a measure of correlated token changes) in forward-backward diffusion experiments as a probe of latent hierarchical structure in data. The authors derive a mean-field theory showing that in a synthetic hierarchical model (RHM), the correlation length of token changes diverges at the class-reconstruction phase transition, and validate this with belief propagation simulations. They then apply the same measurement to real text (MDLM on WikiText) and images (DDPM on ImageNet with CLIP patch embeddings), reporting qualitatively similar susceptibility peaks.

---

## Strengths

- **Clean theoretical prediction in a controlled setting.** The mean-field derivation of the diverging correlation length $\xi \sim |\epsilon-\epsilon^*|^{-\nu}$ (Eq.~5) and the validation via belief propagation (Fig.~2a-I, a-II) establish a clear, quantitative signature of what one should expect from hierarchical latent structure. The agreement between theory (dashed) and simulation (solid) is genuinely excellent.

- **Cross-modal experimental scope.** Testing both text and images with different types of diffusion models (masked discrete for text, Gaussian DDPM for images) and observing qualitatively similar behavior is ambitious and hints at a universal phenomenon, even if the evidence is not yet definitive.

- **The basic idea — using dynamical susceptibility as an experimental observable in forward-backward diffusion — is novel and potentially generative.** It provides a concrete, physically motivated tool for studying latent structure that goes beyond standard reconstruction probability or visual inspection.

- **Appropriate synthetic grounding.** Using an exactly solvable generative model (RHM) with known latent tree structure as a testbed is methodologically sound; it allows the paper to establish what the signature of hierarchy *should* look like under ideal conditions.

---

## Weaknesses

### Fatal
None.

### Major

1. **The causal attribution of the real-data susceptibility peaks to hierarchical latent structure is not convincingly established.** The argument rests on qualitative analogy: the peak in real data looks similar to the peak in the RHM (which has known hierarchy). However, the paper tests only one non-hierarchical alternative (a Gaussian random field), which (a) uses a different, non-neural diffusion process, (b) is continuous rather than discrete, and (c) lacks the complex architecture and tokenization of real-world diffusion models. This leaves open the possibility that the peak arises from other sources — the transformer architecture, the masking schedule, the CLIP representation, or some non-hierarchical but structured property of real data (e.g., low-dimensional manifold structure). The claim in the conclusion (line 420) that the results "support the hypothesis that hierarchical and compositional structures are fundamental, universal properties" is disproportionate to the evidence provided. **This is the paper's most significant weakness and directly limits the strength of its central contribution.**

2. **No error bars or statistical significance assessment for real-data experiments.** The correlation functions and susceptibility curves for both language (Fig.~3b–c) and images (Fig.~5a–b) are reported without confidence intervals, standard deviations, or any measure of variance. For images, with only 49 patches and ~340 starting samples, the correlation estimates at larger distances involve very few pairs and are necessarily noisy. The susceptibility peak in Fig.~5b appears modest relative to the expected noise level; without error bars the reader cannot assess its significance.

### Minor

3. **The image representation involves significant conceptual shifts from the theory.** The paper replaces binary spin variables (token changed/did not change) with continuous norms of CLIP embedding differences, and the 7×7=49 patches provide only ~6 distinct Euclidean distances. While this adaptation is reasonable for continuous data, it is a substantial departure from the theoretical setup. The choice of CLIP embeddings also introduces a pretrained representation whose own hierarchical properties are unknown and could confound the measurement.

4. **The text experimental protocol needs clarification.** The caption of Fig.~3a states: "The words in blue (green) are those that were masked and changed (did not change), while the words in red changed following the backward process." It is unclear whether "red" tokens are a subset of masked-and-changed tokens (overlapping with "blue") or whether they correspond to a different mechanism (e.g., unmasked tokens that changed). In standard masked diffusion (MDLM), only masked tokens are modified during the backward pass. The paper should clarify the color scheme and confirm that the backward process follows standard MDLM conventions.

5. **The Gaussian random field control does not control for the neural network architecture itself.** Since the GRF experiment uses an analytical (non-learned) diffusion process, it cannot rule out the possibility that the peak is an artifact of the learned neural network's approximation errors or architectural biases. A more appropriate control would apply the *same* MDLM/DDPM to non-hierarchical data (e.g., shuffled tokens or scrambled image patches).

6. **The susceptibility for text integrates correlations only up to r=10** (footnote, line 322), while tokens span 128 positions. The paper justifies this as avoiding finite-size effects, but does not show robustness to the choice of cutoff. This matters because long-range correlations (if present) could affect the location or prominence of the peak.

### Trivial
None.

---

## Nice-to-Haves

- **Bootstrapped confidence intervals** for the correlation functions and susceptibility in both language and image experiments.
- **Control experiments** applying the same MDLM/DDPM to non-hierarchical data (shuffled text, scrambled image patches, synthetic random sequences) and showing that the susceptibility peak disappears or shifts.
- **Quantitative comparison to RHM predictions** — e.g., fitting the measured correlation functions to the predicted scaling form or estimating the critical exponent $\nu$ from real data.
- **Sensitivity analysis** of the peak location to textual inversion time to tokenizer choice, sequence length, or model checkpoint; for images, to CLIP backbone variant or patch size.

---

## Removed Points

These points were flagged by reviewers but are removed or relocated as per guidelines:

- **"The peak at ~0.6 T could arise from the model's own properties"** — This is a speculative concern without supporting evidence. The peak location aligns with independently established class-transition times from prior work (Sclocchi et al. 2024). The concern about confounds is valid but cannot be asserted as a specific alternative mechanism without evidence; folded into Major point 1 as a general confound concern.
- **Specific claim that "red tokens [are] genuinely unmasked but changed"** — This is an interpretation of an ambiguous caption, not a verified fact about the experiment. The ambiguity is kept as Minor point 4, but the specific conclusion is removed.
- **"The mean-field derivation assumes the joint distribution factorizes"** — The paper acknowledges this is a mean-field approximation, and the excellent agreement with BP simulations validates its use for the parameters studied. Not a weakness.
- **Missing appendix content / missing proofs** — The appendices exist in the original submission but were stripped by the PDF parser. Not a flaw in the paper.
- **"Text in figures is difficult to read"** — A PDF extraction artifact, not an author error.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension between an elegant theoretical framework applied to a synthetic model and a promising but under-evidenced extension to real data, but do not themselves generate new observations about the science.

---

## Suggestions

1. **Temper the central claims** about real data. The paper can claim that the real-data experiments are *consistent with* the hierarchical hypothesis and constitute a suggestive demonstration, but the current framing (especially the conclusion) overstates the evidence.

2. **Add at least one strong negative control** using the same neural network architecture on non-hierarchical data. For language, apply the MDLM to randomly shuffled WikiText sequences; for images, apply the DDPM to randomly permuted patches or Gaussian noise. If the susceptibility peak disappears, this would substantially strengthen the hierarchy interpretation.

3. **Report error bars.** Bootstrap confidence intervals over the $N_S$ starting samples for all real-data correlation functions and susceptibility curves.

4. **Clarify the text experiment protocol.** Explain the color coding (blue/green/red), confirm that only [MASK] tokens are reconstructed in the backward pass, and describe how the spin variable $\sigma_i(t)$ is computed for language tokens.

5. **Validate the CLIP-based image measure** by showing (even qualitatively) that the norms of variation vectors correlate with perceptually meaningful changes (e.g., patch-level semantic segmentation or class activation maps).

---

## Score and Decision

The paper's theoretical contribution — the mean-field prediction and RHM validation of diverging correlation length at the class transition — is solid and well-supported. The central idea of using dynamical susceptibility to probe latent structure is novel and interesting. However, the real-data experiments are presented as the headline contribution ("confirmed in both text and image datasets," "universal properties" of natural data) but lack the statistical rigor and causal controls needed to support this claim. The evidence for hierarchy in real data is suggestive but not conclusive. This gap between the strength of the claims and the strength of the evidence is the paper's core problem. The paper would be significantly improved by tempering its claims and adding controls.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>