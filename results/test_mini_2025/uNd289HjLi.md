Now I have strong calibration. Let me synthesize the final review.

**Round 1 Bracket:** Based on the initial calibration, the paper sits between the low-score MRI papers (avg ~2-3, clearly flawed) and the high-score papers (avg ~8+, oral/spotlight). The relevant band is the middle range (3.5-7.5), where anchors scored 5.0-5.67 and were mostly rejected.

**Round 2 Narrowing:** Comparing against specific anchors:
- DIP-MRI (avg 5.0, Reject): C2S is *stronger* — better theory, more thorough experiments
- Meta-Guided Diffusion (avg 5.0, Reject): C2S is *stronger* — cleaner contribution, better presentation
- X-Diffusion (avg 5.5, Reject): C2S is *comparable* — similar quality but different weakness profiles
- sRGB Noise Modeling (avg 6.5, Accept): C2S is *weaker* — less crisp experimental validation, more overclaiming

The paper sits around 5.5 — borderline, with real methodological concerns but a solid theoretical core.

---

## Summary

**Score: 5.5, Decision: Reject**

Now let me write the full review.

Key decisions on which criticisms to keep:

**KEEP (Major):**
1. Supervised comparison framing is structurally asymmetric and the abstract overstates
2. Multi-contrast SOTA over claim (no multi-contrast supervised baseline)
3. Reparameterization ablation gain suspiciously large without explanation

**KEEP (Minor):**
4. Baseline adaptation for self-supervised methods not discussed
5. Error bars missing from main results

**REMOVE:**
- Inference procedure distribution shift concern (misreading of the paper; τ=0 is in training distribution)
- Loss weighting w(τ) not specified (it IS specified in Eq 10 description)
- Missing appendix/proofs (parser issue)
- Missing comparisons with DDM2/Di-Fusion (diffusion MRI, different task)
- Detail refinement practical benefit marginal (this is factual but doesn't threaten the contribution; C2S without refinement still beats baselines)
- Architecture improvement small (this is fine — the contribution is the loss, not the arch)
- Multi-contrast architecture details missing (appendix issue)

Let me also filter the Strength Finder's output.

**KEEP strengths:**
1. GDSM unifies/extends prior work (Theorem 1, Remark 1) — clear and verified
2. SOTA among self-supervised methods on M4Raw (Table 2) — verified
3. Multi-contrast extension improves over single-contrast (Table 5) — verified (though the SOTA over supervised claim is overblown)
4. Noise-level reparameterization improves performance (Table 4a) — verified
5. Detail refinement shows statistically significant improvements (Table 1) — verified
6. Robustness to noise estimation errors — verified (text mentions ±50% robustness)

**WEAKEN/RENAM:**
- The Strength Finder says "outperforms supervised SwinIR on T1 and T2" — this is within the asymmetric setup. Should be caveated. I'll keep it as "competitive with supervised methods" with the caveat noted in weaknesses.

**REMOVE from Strengths:**
- Generic/overblown claims that conflict with weaknesses.

Let me write the review now.Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper introduces Corruption2Self (C2S), a score-based self-supervised framework for MRI denoising. The core theoretical contribution is the Generalized Denoising Score Matching (GDSM) loss, which extends denoising score matching to work with noisy observations by modeling conditional expectations of higher-SNR images given further corrupted ones — unifying DSM, ADSM, and Noiser2Noise under a single framework. The method incorporates noise-level reparameterization for stable training, a detail-refinement extension to preserve fine textures, and can leverage multi-contrast inputs. Experiments on M4Raw (low-field real noise) and fastMRI (simulated noise) show that C2S achieves the best results among self-supervised methods and is competitive with supervised approaches.

## Strengths

- **Principled theoretical unification of existing methods**: Theorem 1 and Remark 1 (Section 3.1) show that GDSM generalizes denoising score matching (DSM), ambient denoising score matching (ADSM), and Noiser2Noise under a single loss with different choices of target noise level. This provides a clean theoretical lens for self-supervised denoising and is the paper's most solid contribution.

- **State-of-the-art among self-supervised methods on real MRI data**: Table 2 shows C2S with detail refinement achieves the highest PSNR/SSIM among all self-supervised methods across three contrasts on M4Raw (e.g., T1: 32.77 dB / 0.919, T2: 32.33 dB / 0.890, FLAIR: 32.51 dB / 0.876). The improvements over second-best methods are often modest (~0.4–0.9 dB) but consistent.

- **Multi-contrast extension produces clear improvements**: Table 5 shows that using complementary contrasts (e.g., FLAIR & T1 to denoise T1) yields 33.89 dB PSNR, a gain of over 1 dB over single-contrast C2S (32.77 dB) and outperforming single-contrast Noise2Noise (32.59 dB). This demonstrates the framework's ability to leverage multi-modal information.

- **Noise-level reparameterization stabilizes training**: Table 4a reports substantial gains from reparameterization (e.g., T1: 31.14 → 34.43 PSNR), and the paper shows convergence dynamics in Appendix I.

- **Detail refinement module shows statistically significant gains**: Table 1 reports paired t-test p-values < 0.05 across all contrasts on the validation set, providing rigorous evidence that the refinement module improves beyond the base C2S.

## Weaknesses

### Fatal
None.

### Major

1. **Supervised comparison is structurally asymmetric, but the abstract frames it as a head-to-head strength.**  
   The paper states (lines 149–151) that supervised baselines (SwinIR, Restormer) are trained on 3-repetition-averaged labels and evaluated on 6/4-repetition-averaged labels — a harder problem for supervised methods. The paper acknowledges this asymmetry (lines 187–188, and Appendix F with matched-noise experiments), but the abstract and introduction present "competitive with supervised" as a headline claim without prominently flagging the asymmetric setup. On matched-noise evaluation (Appendix F), supervised methods perform better. This framing is misleading: C2S is genuinely a strong *self-supervised* method, but the paper's claim about matching supervised methods is qualified by a training-label asymmetry that is buried.

2. **Multi-contrast SOTA claim over supervised methods is unsubstantiated.**  
   The abstract states that "after extending to multi-contrast on the M4Raw dataset, [C2S] shows state-of-the-art performance among both self-supervised and supervised methods." However, Table 5 compares multi-contrast C2S only against *single-contrast* BM3D, Noise2Noise, and C2S. No multi-contrast supervised baseline (e.g., SwinIR or Restormer with multi-channel input) is included. The claim of SOTA over supervised methods in the multi-contrast setting is therefore not supported by the evidence presented.

3. **Reparameterization ablation shows an implausibly large gain that is not adequately explained.**  
   Table 4a reports that reparameterization improves PSNR from 31.14 to 34.43 on T1 — a 3.3 dB jump. On T2 the gain is similar (30.53 → 33.82). This is an order of magnitude larger than any other component ablation. The paper states "without reparameterization" but does not define the implementation: does this mean uniform sampling over the original noise level `t`? Fixed noise level? The gap is so large that it raises concern that the "without" baseline may be operating suboptimally (e.g., poor coverage of the noise-level range). The paper should clarify the exact implementation of the "without" condition and demonstrate that the gain stems from the reparameterization mechanism itself rather than from an unfairly weak baseline.

### Minor

4. **Baseline adaptation for self-supervised methods is not discussed.**  
   Several self-supervised baselines (PUCA, LG-BPN) were originally designed for natural images. The paper provides no evidence that these methods were tuned for MRI data — architectures, hyperparameters, or noise estimation. Their lower performance (e.g., PUCA at 30.52 dB vs. C2S at 32.59 dB on T1) could partially reflect domain mismatch rather than inherent algorithmic inferiority. Since the gap to the strongest self-supervised baselines (Noisier2Noise, Recorrupted2Recorrupted) is modest (≤1 dB on M4Raw, and C2S is sometimes second-best on fastMRI), the SOTA claim among self-supervised methods would be stronger with evidence that baselines were appropriately adapted.

5. **Error bars and significance tests are absent from the main results tables.**  
   Statistical significance is reported only for the detail refinement ablation (Table 1, validation). The main comparisons on test sets (Tables 2, 3, 4, 5) report point estimates without standard deviations or significance tests. Many differences are within fractions of a dB (e.g., C2S 32.59 vs. Noise2Noise 32.59 on T1 — identical PSNR; on fastMRI PDFS σ=13/255, Recorrupted2Recorrupted edges C2S 30.95 vs. 30.91). Without error bars, the reader cannot assess whether claimed improvements are meaningful or reflect noise. Given that validation p-values were computed, the same rigor should extend to test-set results.

### Trivial
None.

## Nice-to-Haves

- The paper mentions robustness to ±50% noise estimation error (Appendix H) — this is a practically important finding that should be elevated to the main paper with quantitative results.
- The loss weighting function `w(τ)` is described as `(σ_τ² + σ_{t_data}²)^α` but the value of α is not stated. Reporting it would improve reproducibility.
- The abstract's "competitive with supervised" claim would be more effective if reframed explicitly for the label-scarce regime, and the matched-noise results from Appendix F were brought into the main paper.

## Removed Points

These points are flagged to be removed; treat them with caution if referenced:

- **Inference distribution shift concern** (harsh critic): The claim that the model never sees τ=0 during training is incorrect — τ ∼ U(0, T) is used in Eq. 10 and Algorithm 1, so τ=0 is in the training distribution. At τ=0, σ_τ=0 and X_τ = X_{t_data}, matching inference. Removed: misreading of the paper.
- **Loss weighting w(τ) not specified** (harsh critic): The paper explicitly states that w(τ) can be set to (σ_τ² + σ_{t_data}²)^α (Section 3.2). The exact α is a tunable hyperparameter; its absence is a minor reproducibility detail, not a missing design decision. Removed: claim is factually incorrect.
- **Missing appendix/proofs** (harsh critic): The GDSM proof and other details are deferred to appendices that were stripped by the PDF parser. Criticizing their absence is not a valid weakness of the submission. Removed: parser artifact.
- **Missing comparisons with DDM2 / Di-Fusion** (harsh critic): These are diffusion MRI (dMRI) methods designed for 4D data, not standard structural MRI denoising. The paper mentions them in related work. Criticizing their absence as baselines is scope creep. Removed: scope creep.
- **Multi-contrast architecture details missing** (harsh critic): The paper states multi-contrast inputs are "incorporated as additional inputs" and refers to Appendix D for architecture details. The appendix was stripped. Removed: parser artifact.
- **GDSM coefficients stated without derivation** (harsh critic): The coefficients are stated in Equations 3 and 7, and the proof is in the appendix. The main text is appropriately concise for a readable methodology section. Removed: presentation preference, not a weakness.
- **Architecture improvement is small** (harsh critic): Table 4b shows U-Net → DDPM → Ours improves from 33.11 → 34.82 → 34.91 (M4Raw). This is correct but the paper does not oversell the architecture — the contribution is the GDSM loss, not architectural novelty. Removed: not a genuine weakness.
- **Detail refinement yields marginal test-set gains** (harsh critic): The gains are ~0.1–0.2 dB on test sets. This is factual but does not weaken the paper — the refinement is presented as a balanced option, and the base C2S already outperforms baselines. Removed: over-interpretation of a secondary result.
- **Rician noise limitation mentioned but not tested** (harsh critic): The paper acknowledges the Gaussian assumption and mentions VST as a workaround; testing non-Gaussian noise is a reasonable extension, not a missing experiment. Removed: scope creep.
- **"Reparameterization is standard practice"** (harsh critic claim that it's just the variance schedule from Karras et al.). The paper contextualizes this correctly as a training stabilization technique; it does not claim reparameterization as a novel invention separately from the GDSM framework. Removed: the critic overstates the novelty claim.
- **Strength Finder's generic/delusional strengths removed**: Claims like "addressed an important problem" and "comprehensive analysis" without specific anchor points. These are generic and conflict with identified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that changes how its contribution should be understood — the GDSM theoretical framing is the paper's own insight, and the reviewers' observations about framing issues and ablation concerns are critical feedback rather than novel re-interpretations.

## Suggestions

1. **Reframe the comparison with supervised methods**: Restructure the abstract and introduction to clearly state the asymmetric training setup upfront ("supervised methods trained on 3-rep averages"), and bring the matched-noise experiments (Appendix F) into the main paper as the primary comparison. This turns a weakness into a strength: C2S outperforms supervised methods when both are trained on the same noisy labels.

2. **Add a multi-contrast supervised baseline to Table 5**: Include a supervised method (e.g., SwinIR or a U-Net) with multi-channel input to substantiate the SOTA claim over supervised methods in the multi-contrast setting.

3. **Clarify the "without reparameterization" condition in Table 4a**: State explicitly what the baseline is (uniform over `t`? fixed noise level? a single noise level?), and explain the mechanism that produces the 3.3 dB gap.

4. **Add error bars or significance tests** to all main result tables (Tables 2, 3, 4, 5), at minimum across test-set samples or via paired bootstrapping.

5. **Discuss baseline tuning**: Add a sentence or short paragraph describing whether self-supervised baselines (PUCA, LG-BPN) used their default hyperparameters from natural images or were tuned for the MRI domain.

## Score and Decision

**Round 1 (Bracketing)**: The paper was compared against three score bands:

| Band | Example Anchor | Avg Score | How It Compares |
|------|---------------|-----------|-----------------|
| Weak (< 3.5) | CRL-NET (1.67), Brain MRI SR (2.0) | 1.7–3.0 | C2S is clearly stronger |
| Middle (3.5–7.5) | DIP-MRI (5.0), X-Diffusion (5.5), Screener (5.33) | 5.0–5.67 | C2S is comparable or slightly stronger |
| Strong (> 7.5) | Never Train from Scratch (8.0), CrIBo (8.0) | 8.0+ | C2S is substantially weaker |

Initial bracket: between 4.5 and 6.5.

**Round 2 (Narrowing)**:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DIP-MRI | cFT9jWI7vT.md | 5.0 | 2 | C2S is stronger: cleaner theory, more thorough experiments, better presentation |
| Meta-Guided Diffusion | mbPvdO2dxb.md | 5.0 | 2 | C2S is stronger: clearer contribution, less speculative |
| X-Diffusion | urf8a5G59f.md | 5.5 | 2 | C2S is comparable: both have solid cores but overclaim; C2S has stronger theory |
| Screener | K4JHTZ13G3.md | 5.33 | 2 | C2S is slightly stronger: clearer methodology, better contextualized |
| sRGB Noise Modeling | 2XBBumBGeP.md | 6.5 | 2 | C2S is weaker: more overclaiming, less rigorous experimental framing |

After round 2, C2S sits between the 5.0 anchors (stronger) and the 6.5 anchor (weaker), close to X-Diffusion at 5.5. The paper has a solid theoretical contribution and comprehensive experiments, but the overclaiming in the abstract (unsupported multi-contrast SOTA, asymmetric supervised comparison) and the unexplained 3.3 dB reparameterization gap are significant issues that prevent a higher score.

**Final Score**: 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>