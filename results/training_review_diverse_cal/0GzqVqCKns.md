Now I have a thorough understanding of the paper and the reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes using forward-backward experiments in diffusion models to probe the hierarchical latent structure of data. The authors derive a mean-field theory in a toy hierarchical model (RHM) predicting that the dynamical correlation length of token changes diverges at a class-reconstruction phase transition. They confirm this prediction quantitatively on the RHM, and then show qualitatively similar phenomenology — a peak in dynamical susceptibility at a finite inversion time — in masked diffusion on WikiText text data and DDPMs on ImageNet images. The core contribution is the theoretical framework linking hierarchical structure to measurable quantities in diffusion processes, supported by clean synthetic experiments and suggestive real-data evidence.

## Strengths

- **Theoretical derivation of diverging correlation length in a hierarchical generative model (Section 3.1).** The mean-field analysis yields a scaling relation ξ ∼ |ε − ε*|^{-ν} with ν = log s / log F'_* (Eq. 6), linking the size of correlated token-change blocks to the class-reconstruction phase transition. This directly supports the claim that hierarchical structure produces a growing correlation length.

- **Quantitative validation on the Random Hierarchy Model (RHM) with two diffusion processes (Figure 2).** Both the ε-process and masking diffusion produce a clear peak in dynamical susceptibility at the critical noise/inversion time, with system-spanning power-law correlation functions. The theoretical mean-field curves (dashed lines) agree excellently with numerical experiments, and the critical exponent prediction is verified (Appendix RHM).

- **Gaussian random field counterexample (Section 3.3).** The paper explicitly contrasts the RHM results with a Gaussian random field model, showing that spatial correlations alone produce a monotonic increase of correlation length with noise rather than a peak. This strengthens the claim that the susceptibility peak is a signature of latent hierarchical structure rather than a generic artifact.

- **Clear and reproducible methodology.** The paper reports experimental parameters (starting samples N_S, trajectories per sample N_R, diffusion models, tokenization schemes) in detail, facilitating reproduction.

- **Demonstration across two real data modalities.** Showing the same qualitative pattern — a peak in susceptibility at a finite inversion time — in both text (MDLM on WikiText) and images (DDPM on ImageNet with CLIP tokenization) suggests the framework generalizes beyond synthetic data.

## Weaknesses

### Fatal
None.

### Major

- **The real-data evidence is qualitative/suggestive, and the paper's language overstates the strength of confirmation.** The paper claims in the abstract to "confirm this prediction in both text and image datasets" and states that a susceptibility peak "establish[es] the existence of a phase transition for the language modality." However, for real data the evidence is limited to a peak in a summary statistic (susceptibility) and a visually growing correlation length. No correlation length ξ(t) is explicitly extracted from real-data correlation functions; no exponents are fit; no scaling collapse or finite-size scaling analysis is performed. The Gaussian random field counterexample rules out spatially-correlated but non-hierarchical models, but other structured non-hierarchical latent-variable models (e.g., mixture models with a single latent class, factorial hidden Markov models) are not tested or discussed as potential alternative explanations for a susceptibility peak. The real-data results are consistent with the hierarchical hypothesis but do not constitute a quantitative confirmation, and the paper would benefit from a more measured framing.

- **No error bars or statistical significance estimates on real-data measurements.** The real-data correlation functions and susceptibility curves are presented without error bars. With 300 text samples × 50 trajectories and 344 images × 128 trajectories, these averages likely have meaningful variance, and the reader cannot assess whether adjacent t-values are statistically distinguishable. This is standard practice for this type of analysis and should be included.

### Minor

- **Image observables are a proxy for the theoretical binary change indicator.** For text, the binary spin variable σ_i ∈ {−1, +1} is directly available because tokens are discrete. For images, the paper uses correlations of CLIP embedding norm variations (‖Δx_i‖). This is a reasonable approach for continuous data, but it is several steps removed from the binary "changed/didn't change" used in the theory — different semantic changes produce different-magnitude norm variations, and correlated norms do not straightforwardly correspond to "blocks of tokens that change in concert." The paper should acknowledge this limitation more explicitly.

- **No explicit correlation length ξ(t) is extracted from real data.** The text results report a "growing correlation length" reaching "7–8 tokens" at t*, but this appears to be a visual estimate from the C(r) plots rather than a quantity obtained by fitting (e.g., an exponential exp(−r/ξ) to the correlation functions). Extracting and plotting ξ(t) explicitly would allow direct comparison with the RHM.

- **The choice of integration range r ∈ [0, 10] for text susceptibility is justified only in a brief footnote.** The paper states this avoids finite-size effects, but providing a sensitivity analysis or showing the full-range result alongside the truncated one would strengthen the analysis.

### Trivial

- The abstract states that "changes in data occur by correlated chunks, with a length scale that diverges at a noise level where a phase transition is known to take place." The divergence statement applies strictly to the RHM in the infinite-size limit; for real data the observed behavior is a peak, not a divergence. The paper mostly uses "peaks" for real data, but the abstract's phrasing could cause confusion.

## Nice-to-Haves

- **Parse-based validation for language data.** Annotating WikiText samples with constituency parses and checking whether blocks of co-changing tokens correspond to syntactic constituents would ground the measurements in known structure and significantly strengthen the claim that the method probes hierarchy.
- **Testing against non-hierarchical but structured baselines** beyond Gaussian random fields (e.g., a factorial hidden Markov model or a mixture of components with a single latent class) would directly address whether a susceptibility peak uniquely signals hierarchy.
- **Explicit correlation length extraction** from real data (fitting ξ(t) from C(r) curves) and comparison of its shape with RHM predictions would add quantitative depth.
- **Sensitivity analysis** for image tokenization (patch size, alternative encoders like DINO) would assess robustness.

## Removed Points

- **"Missing related works" per instructions.**
- **"The theory does not apply to the masking process"** — The paper never claims a theory for masking; it explicitly says there is no simple mapping between masking probability and ε, and only claims qualitative agreement (lines 256–257).
- **"The paper should also cover grammatical structure analysis"** — The paper explicitly scopes this to future work (line 422–423). This is scope creep.
- **"The paper should include complete training logs / hyperparameters"** — Trivial implementation detail; removed per instructions.
- **"Gaussian random field is linear"** — The paper explicitly acknowledges the Gaussian RF is a spatial-correlation-only model and contrasts it with the hierarchical mechanism. The suggestion to test additional models is valid and moved to Nice-to-Haves.

## Novel Insights

The reviews collectively surface the central tension of the paper: the theoretical apparatus on the RHM is rigorous and compelling, but the leap to real data is bridged by qualitative similarity rather than quantitative validation. The most interesting unresolved question is whether the observed susceptibility peak is a unique signature of hierarchy or could arise from other forms of structured latent organization. Neither the paper nor the reviews resolve this — it remains a promising but open direction. Additionally, the observation that the Gaussian RF fails to produce a peak (Section 3.3) is an important control that the reviews rightly emphasize as a strength, but its limited scope (only one type of non-hierarchical model) is correctly identified as a gap.

## Suggestions

1. **Reframe the real-data claims** from "confirming" to "consistent with" the hierarchical prediction. The paper's value does not depend on real-data confirmation being definitive; the framework and RHM validation are contributions on their own.
2. **Add error bars / confidence intervals** to all real-data correlation functions and susceptibility plots.
3. **Extract and plot ξ(t) explicitly** from real-data correlation functions (e.g., via exponential fits) and compare the shape to RHM results.
4. **Discuss alternative non-hierarchical models** that could produce a susceptibility peak. Even a brief discussion would strengthen the paper by showing the authors are aware of this limitation.
5. **Include a limitations paragraph** in the conclusion that clearly states what the real-data experiments can and cannot establish.

## Score and Decision

**Originality:** 8/10 — The idea of using dynamical susceptibility in diffusion models as a probe of hierarchical structure is novel and well-motivated.

**Importance of research question:** 8/10 — Characterizing data structure is a fundamental problem in learning theory.

**Claims supported:** 6/10 — The RHM claims are well-supported; the real-data claims are overclaimed relative to the evidence.

**Soundness:** 7/10 — The theory and RHM experiments are sound. The real-data analysis is reasonable but lacks rigor.

**Clarity:** 7/10 — Well-written overall, though some claims could be more carefully qualified.

**Value to community:** 8/10 — The framework is likely to inspire follow-up work.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>