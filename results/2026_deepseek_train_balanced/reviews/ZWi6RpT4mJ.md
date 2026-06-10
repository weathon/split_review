## Summary

CoINR proposes compressing Implicit Neural Representations (INRs) by representing each weight vector as a sparse code over a random Gaussian dictionary, then storing only the non-zero coefficients and their indices. The central claim is that because INR weights are Gaussian-distributed, a random matrix (generated from a seed) serves as a valid dictionary without needing to be learned or transmitted. The method is applied before quantization/entropy coding and claimed to be compatible with existing INR compressors. Experiments cover images, occupancy fields, and NeRFs, with the strongest evidence coming from the KODAK image benchmark.

## Strengths

- **Measurable compression gains on images under controlled conditions**: Experiment C₁ (Section 4.3, line 120) reports that CoINR achieves ~1.7 bpp at 30 dB PSNR on KODAK, versus 3.7 bpp for COIN and 2.0 bpp for INRIC under the *same* 16-bit uniform quantizer and Brotli entropy coder. These numbers directly isolate the effect of the sparse-coding preprocessing step from the post-processing pipeline.

- **Modular placement in the compression pipeline**: CoINR operates on INR weight spaces prior to quantization and entropy coding (Section 3.2, line 64; Figure 2 caption). Experiments C₃–C₅ (lines 125–132) validate that it can be stacked on top of INRIC and COIN++ to reduce their bpp at matching PSNR, supporting the claim of architectural agnosticism.

- **Sparsity level s depends on neuron count, not signal content**: Section 4.2 (line 113) reports that the optimal sparsity level s for OMP is a function of the number of hidden neurons alone, not the specific image or data modality — a practically useful property for deployment.

## Weaknesses

### Fatal
None. The paper has significant deficiencies, but no single error invalidates the core empirical observations.

### Major

1. **The CLT-based justification for a random dictionary is conceptually unsound**. The paper argues (Section 3.2, lines 62–63): INR weights are Gaussian → "According to the Central Limit Theorem (CLT), a normally distributed random variable can be produced through a finite linear combination of independent random variables" → therefore w = Ax with random A and sparse x. This reasoning is flawed on two levels. First, the CLT is a limit theorem about the *distribution* of a sum approaching normality; it does not assert that *any given* Gaussian vector can be expressed as a sparse combination of a *fixed* random matrix's columns. Second, the paper needs the reverse direction: "w is Gaussian ⇒ w has a sparse decomposition over A." No standard theorem in probability or compressed sensing provides this guarantee. Standard compressed sensing theory (RIP, incoherence) ensures recovery of sparse x from y = Ax, but it does *not* guarantee that an arbitrary dense vector w has a sparse representation over a random A. The paper's central design choice — that the dictionary can be random and seed-controlled — rests on this unsupported logical leap. Replacing this with a direct empirical argument (random A works well enough, as verified by a learned-dictionary ablation) would salvage the contribution, but that ablation is absent.

2. **Audio claimed as a tested modality but no results are presented**. Section 4.1 (line 106) states: "Our experiments... spanned various data types including images, occupancy fields, **audio**, and neural radiance fields." No audio results — no figure, table, or numerical report — appear anywhere in the paper. This is a material omission. If audio was not tested, it should not be claimed; if it was tested, the results are absent.

3. **No comparison against a learned dictionary (e.g., K-SVD or a learned transform)**. The paper's key novelty claim is that the dictionary "does not need to be learned or transmitted" (line 62). The paper dismisses learned dictionaries as "time-consuming" but provides no empirical evidence that a random dictionary performs comparably. Without this ablation, it is impossible to assess whether the random dictionary is an adequate substitute or merely a lossy shortcut that happens to produce passable results on images. Given that the CLT-based theoretical justification is unsound, this empirical comparison is essential to support the central claim.

### Minor

4. **Quantitative occupancy-field and NeRF results are reported only in figure annotations, not in the text**. For occupancy fields (lines 141–142), the text describes Figure 6 qualitatively but provides no numerical IoU or file-size values. For NeRFs (line 145), the text states "more than 50% compression while maintaining the same PSNR" without reporting the actual PSNR or file-size numbers. While the numbers likely appear in the figures, the text should state them explicitly, especially for two of the three non-image modalities claimed.

5. **The COIN++ baseline is altered without justification**. The paper (lines 106–107, 125) modifies COIN++'s hidden neuron size to 300. The original COIN++ paper specifies particular architectures; changing the hidden dimension can significantly affect both compression performance and the behavior of latent modulations. No justification is given for the choice of 300, and no results with the original configuration are reported. This undermines a fair comparison in experiment C₅.

6. **No comparison against direct weight quantization at lower bitwidths**. A natural strawman is to simply quantize the original INR weights at, e.g., 8 bits instead of 32 bits, without any sparse-coding step. This would isolate whether the sparse-coding preprocessing adds value beyond simply reducing precision. The paper compares against COIN and INRIC (which themselves use quantization), but not against this direct baseline.

### Trivial
- The OMP encoding cost (learning sparse codes for millions of NeRF parameters) is not discussed. Given that OMP scales as O(k₁ · k₂ · s) per weight vector, this could be significant for large INRs.

## Nice-to-Haves
- Comparison of random A vs. a learned dictionary (as noted in Major weakness 3).
- Reporting s/k₁ ratios and weight-space reconstruction error (‖w − ŵ‖) across experiments, to clarify the actual compression-distortion trade-off at the weight level.
- Reporting variance or confidence intervals for the image compression results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Garbled text implying garbled reasoning (Harsh Critic)**: The critic cited garbled text at line 63 as evidence that "the underlying reasoning may also be garbled in the original." The garbled characters are a PDF-extraction artifact, not an author error. Per hard rules, formatting artifacts must be removed. The logical flaw in the CLT argument stands on its own independent of the garbled text.

- **"432 433 434..." number run as evidence of sloppiness**: The critic flagged line 134's run of numbers as something "that should have been caught." This is a parser artifact (page numbers or table rendering), not an author error. Removed per the formatting-artifact rule.

- **Theoretical justification could be rescued**: The critic's suggestion that the paper should "replace the CLT argument with a proper justification" is valid in spirit but already subsumed by Major weakness 1 (the CLT argument is unsound). The review already covers this.

- **Strength Finder's first claimed strength ("Seed-based random sensing matrix eliminates dictionary transmission")**: While the property exists, the CLT-based justification is demonstrably flawed (Major weakness 1). The weakness does not *conflict* with the property (the method could still work), but the strength is retained with appropriate caveat.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine theoretical error (CLT misapplication) and several evidential gaps, but raise no novel synthesis that the authors had not already attempted to address (however imperfectly).

## Suggestions

1. **Drop the CLT argument entirely** and instead frame the use of a random dictionary as an empirical design choice. Support this with an ablation comparing random A vs. a learned dictionary (e.g., K-SVD). If random A performs comparably or nearly so, that is an interesting empirical finding in its own right.

2. **Either report audio results or remove audio from the list of tested modalities**. The claim of multi-modality evaluation is hollow without evidence.

3. **State occupancy-field and NeRF quantitative results explicitly in the text** (IoU, PSNR, file sizes) rather than relying solely on figure annotations.

4. **Justify or revert the COIN++ architecture modification**, and report results using the original COIN++ configuration to establish a fair baseline.

5. **Add a baseline of direct weight quantization at lower bitwidths** (e.g., 8-bit uniform quantization of the original weights) to isolate the contribution of the sparse-coding step.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>