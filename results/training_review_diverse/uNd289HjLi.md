Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces Corruption2Self (C2S), a score-based self-supervised MRI denoising framework. The core contribution is a Generalized Ambient Denoising Score Matching (GADSM) loss that extends denoising score matching to settings where only noisy observations are available, unifying DSM, ADSM, and Noisier2Noise as special cases. C2S achieves state-of-the-art self-supervised results on M4Raw (32.77/0.919 PSNR/SSIM on T1) and competitive performance on fastMRI, with a multi-contrast extension that surpasses supervised baselines.

## Strengths

- **GADSM provides a principled theoretical unification.** Theorem 1 shows that GADSM reduces to DSM, ADSM, and Noisier2Noise as special cases, establishing a rigorous connection between score matching and self-supervised denoising. This is a genuine theoretical contribution.

- **State-of-the-art self-supervised results on M4Raw across all contrasts (Table 2).** C2S with detail refinement achieves 32.77/0.919 (T1), 32.33/0.890 (T2), and 32.92/0.876 (FLAIR), consistently outperforming all compared self-supervised methods (Noise2Void, Noise2Self, PUCA, LG-BPN, Noisier2Noise, Recorrupted2Recorrupted) and matching or exceeding supervised methods on higher-SNR test data.

- **Multi-contrast C2S exceeds supervised baselines (Table 6).** Using T1 & T2 as inputs, C2S achieves 33.19/0.923 on T1, outperforming single-contrast C2S (32.77/0.919) and supervised Noise2Noise (31.08/0.895) and BM3D (30.04/0.888). This demonstrates practical value beyond what theoretical justification alone would suggest.

- **Reparameterization improves training stability (Figure 2, Table 4a).** The reparameterization from \(t\) to \(\tau\) combined with EMA yields smoother and faster convergence, with PSNR gains of ~0.4 dB across contrasts on M4Raw.

- **Consistent performance on fastMRI across contrasts and noise levels (Table 3).** C2S achieves best or comparable self-supervised results on PD, PDFS, and T1 at both \(\sigma=13/255\) and \(25/255\), demonstrating generalizability beyond the primary dataset.

- **Ablation studies validate key architectural choices (Table 4b).** Time conditioning and NVC-MSA provide substantial improvements (T1 PSNR from 30.46 to 32.59), confirming that the architectural design choices are well-motivated.

## Weaknesses

### Major

- **Noise-level estimation robustness is asserted without supporting evidence.** The paper claims (line 153) that C2S "demonstrates strong robustness to noise level estimation errors" and can function as a blind denoising model using standard noise estimation tools. However, no experiment varies the estimated noise level or compares performance when \(\sigma_{t_{\mathrm{data}}}\) is intentionally mis-specified. Since the method requires knowledge of the input noise level, this claim directly affects the practical applicability claim but is entirely unsupported. The paper should either provide such an experiment or temper the claim.

- **Multi-contrast extension is presented without theoretical or methodological justification.** The paper adds other contrasts as inputs (line 155) but does not discuss how this affects the GADSM loss derivation, the conditional expectation being learned, or whether the ambient-score-matching theory remains valid when additional contrasts are not simply noisier versions of the same underlying image. The empirical results in Table 6 show it works, but there is no reasoning about input formation (concatenation? separate processing?), loss adjustments, or architectural changes. This makes a claimed contribution feel incomplete.

### Minor

- **No statistical significance or confidence intervals for main quantitative results (Tables 2, 3, 5, 6).** Only the detail refinement comparison (Table 1) includes a paired t-test. Given the limited number of test subjects in M4Raw, variance across samples could be non-negligible. Reporting standard deviations or confidence intervals would strengthen the reliability of the claimed improvements.

- **The reparameterization approximation \(T' \approx T\) and uniform sampling over \(\tau\) are justified only empirically.** The mapping changes the sampling distribution over noise levels, and the approximation cuts off the upper tail, but there is no connection to importance-weighting or variance-reduction techniques from the score-matching literature. The empirical evidence (Figure 2, Table 4a) is convincing, but the theoretical grounding is thin.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Justify the exclusion of DDM2, Coil2Coil, and Patch2Self from quantitative comparisons. These are cited in the background but target different MRI settings (4D diffusion MRI, multi-coil data, diffusion MRI respectively); a brief explanation would preempt reader confusion.
- Add a short intuitive paragraph before Theorem 1 explaining why the linear combination \(\gamma h_\theta + \delta X_t\) yields a prediction of \(X_{t_{\mathrm{target}}}\) and how Tweedie's formula connects — this would improve accessibility for readers unfamiliar with ambient score matching.
- Provide a sensitivity analysis of the weighting function hyperparameter \(\alpha\) and the choice of \(\sigma_{t_{\mathrm{data}}}\), as these are the knobs practitioners would need to tune.

## Removed Points

- **Detail refinement extension not described (Critical Issue 1 from the harsh reviewer).** This criticism concerns content that may reside in the appendix, which is stripped by the parser. Per policy, weaknesses about missing appendix content are removed. If the detail refinement is not described in the appendix either, this would be a major issue — the authors should verify it is fully specified in the full submission.
- **Missing baselines (DDM2, Coil2Coil, Patch2Self).** These methods target different MRI subdomains (4D diffusion MRI, multi-coil, diffusion MRI) with different data requirements, and the paper's experiments use low-field brain MRI and knee MRI where these methods may not be directly applicable. The criticism is weakened by the domain mismatch.
- **Strength Finder claim about robustness to noise estimation errors being "supported by experimental validation."** This claim from the strength finder is factually incorrect — no such experiment exists in the paper. This strength conflicts with a verified weakness and is dropped.
- **Generic/superficial strengths from Strength Finder** (e.g., "this paper addressed an important problem") — dropped per filtering rules.
- **Various formatting/style nitpicks and reproducibility nitpicks** — removed per hard rules.

## Novel Insights

The most interesting observation across the reviews is the tension in the multi-contrast results: the empirical performance is strong enough to surpass supervised methods, yet the theoretical grounding for why the GADSM loss remains valid across different contrasts is absent. This suggests either (a) the method is more general than the authors theoretically justify, or (b) the empirical success is driven by the network's capacity to exploit correlated features rather than by the score-matching theory. Either case would be valuable to disambiguate. Additionally, the fact that C2S matches supervised methods trained on 3-repetition-averaged labels when tested on 6-repetition-averaged data (Table 2) reveals a subtle but important point about supervised MRI denoising: the "clean" labels used to train supervised methods are themselves noisy, which limits their ceiling. This insight is worth emphasizing beyond the paper's current framing.

## Suggestions

1. **Add a noise-level sensitivity experiment.** Vary \(\sigma_{t_{\mathrm{data}}}\) by \(\pm 10\%, \pm 20\%, \pm 50\%\) from the estimated value and report PSNR/SSIM. This directly addresses the practical blind-denoising claim.
2. **Clarify the multi-contrast input mechanism.** State explicitly how multiple contrasts are combined (channel concatenation? separate encoders?); discuss whether the GADSM loss derivation extends or requires modification when conditioning on a different contrast's image.
3. **Add confidence intervals or standard deviations to the main tables** (Tables 2, 3, 5, 6) using bootstrap or multiple test-sample splits.
4. **Provide a brief sketch of the detail refinement mechanism in the main text** (even 2–3 sentences) so the reader understands whether it is a loss term, a second network, a post-processing step, or a feature-matching objective — even if the full details are in the appendix.

## Score and Decision

The paper makes a genuine theoretical contribution (GADSM unification), is well-motivated, and presents strong empirical results that are useful to the MRI community. The two major weaknesses — an unsupported robustness claim and a gap in multi-contrast justification — are real but addressable and do not invalidate the core contribution. The noise robustness claim needs either experimental backing or tempering, and the multi-contrast extension needs methodological clarification. Neither issue is fatal.

**Originality:** Good — GADSM is a novel framework.  
**Importance of question:** High — self-supervised MRI denoising is practically significant.  
**Claims well supported:** Mixed — main results are solid, but the robustness claim is unsupported.  
**Soundness of experiments:** Good for core claim; missing sensitivity analyses.  
**Clarity:** The GADSM derivation is rigorous but could be more accessible; the detail refinement not being in main text is a concern (though likely in appendix).  
**Value to community:** High — practical method with strong results and clear theoretical grounding.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>