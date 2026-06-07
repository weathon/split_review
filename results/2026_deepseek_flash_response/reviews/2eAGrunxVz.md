## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that embeds binary watermarks into the Gaussian noise input without per-image key storage. The method decomposes into three modules: (1) binary embedding via a sparse mixing matrix T that produces 3-wise independent Bernoulli(1/2) bits, (2) spherical mapping that maps these bits onto the unit sphere, applies a fixed orthogonal rotation, and scales by a chi-square-distributed radius, and (3) diffusion integration that feeds the watermarked noise into a pretrained Stable Diffusion pipeline. The authors prove that the output matches standard Gaussian noise up to third-order moments (spherical 3-design) and evaluate on SD v1.5/v2.1 against traditional and latent-based watermarking methods.

## Strengths

1. **Rigorous theoretical foundation for undetectability.** The chain of guarantees — Theorem 3.1 (3-wise independence of z^(1)), Theorem 3.2 (spherical 3-design of z^(2) on the unit sphere), Lemma 3.3 (rotation invariance of the 3-design), and Lemma 3.4 (chi-square scaling → Gaussian) — constitutes a more formal treatment of losslessness than prior work. The hypercube vertices with 3-wise independence genuinely form a spherical 3-design, and the theoretical pipeline is mathematically sound.

2. **Elimination of per-image key storage with practical efficiency gains.** Unlike Gaussian Shading (which requires a unique key+nonce per image) and PRC (which uses heavyweight cryptographic error-correcting codes), the method uses a single fixed secret signature (T, C). Figure 4 shows extraction is ~4 orders of magnitude faster than PRC (~10⁻³⁵ s vs ~10¹ s), a practically meaningful advantage.

3. **Superior robustness at high watermark capacity.** Figure 6(a) shows that under JPEG-70 compression, PRC Watermark's accuracy deteriorates rapidly beyond l_m = 2000 and fails entirely, while Spherical Watermark sustains high detection across the full capacity range. This is a clear improvement over the primary lossless competitor.

4. **FID matching the unwatermarked baseline in Table 1.** The method's FID (48.1224 on COCO SD v1.5) is essentially identical to the original unwatermarked baseline (48.1256) within error bars. Only PRC and the proposed method achieve this; all other baselines (DwtDct, DwtDctSvd, RivaGAN, Tree-Ring, Gaussian Shading) introduce measurable shifts.

5. **Clean ablations isolating each module's contribution.** Figure 6(b) shows omitting binary embedding makes the latent "trivially distinguishable"; Figure 6(c) shows omitting spherical mapping causes robustness under brightness to "drop dramatically." Tables 4–5 demonstrate robustness across ODE solvers (DDIM, PNDM, DPM-Solver++) and timestep configurations (10–50 steps).

## Weaknesses

### Major

1. **Figure 2 does not display the undetectability results the text attributes to it.** The text states (Section 4.2): "According to Figure 2, both Tree-Ring and Gaussian Shading (with fixed keys) are easily detected with accuracies of 100% and 97%, while PRC Watermark and our method remain indistinguishable." It also claims "In Figure 2, we also train a ResNet-18 classifier for image-level classification. Tree-Ring and Gaussian Shading are detectable, while PRC Watermark and ours show near-chance detection (50%)." However, the figure caption (lines 217–221) explicitly states: *"Each plot compares 'True Ring' (blue line) and 'PRC watermark' (orange line)."* Neither Gaussian Shading nor the proposed method appear in the figure as described. Since undetectability is the paper's core claim, the central empirical evidence for it is not verifiable from what is presented. This is a concrete evidential gap — the reviewer cannot tell whether the claimed near-chance accuracy for the proposed method reflects genuine indistinguishability or a selection of favorable results. **This is fixable (replot with all four methods), but in the current submission it undermines the paper's main empirical claim.**

### Minor

2. **FID computation methodology is non-standard and unclearly explained.** The paper states FID is "measured against the unwatermarked output distribution" (line 229), which means it compares two sets of generated images (not generated vs. real), explaining the atypically high baseline values (~48). The table header "Lower FID indicates higher image quality" is misleading in this context — the metric reflects distributional *shift from the unwatermarked baseline*, not absolute image quality. The authors should explicitly state: "We compute FID between watermarked generated images and unwatermarked generated images from different prompts."

3. **The "encryption-free" framing overstates the advantage and omits a security trade-off.** The method relies on a fixed secret Signature K = {T, C} kept secret during runtime (line 82: "K is kept fixed and secret during runtime to prevent unauthorized removal"). This is a single-point-of-compromise: if the signature is leaked, *all* watermarks become forgeable or removable. Per-image key schemes (Gaussian Shading) offer per-image security despite storage overhead. The paper accurately touts "no per-image key storage" as an advantage, but calling it "encryption-free" without discussing the fixed-key security model is incomplete. This trade-off should be acknowledged.

4. **The theoretical guarantee is up to third-order moments, but the abstract and introduction claim "statistically indistinguishable from standard Gaussian noise" without always carrying this qualifier.** The Limitations section (Section 5) honestly states "higher-order moments may deviate from the true prior," but the main narrative uses stronger language. A spherical 3-design matches moments up to degree 3 but may deviate at degree 4 and higher; the paper would benefit from consistently framing this as "indistinguishable up to third-order statistics" in the contributions.

5. **Uneven payload sizes across baseline groups.** Traditional methods (DwtDct, DwtDctSvd, RivaGAN) embed 32-bit watermarks while latent methods embed 512-bit, making direct ACC/TPR comparison across these groups less informative (32-bit is inherently easier to recover). The paper does acknowledge this at line 193, so the comparison among latent methods (where payloads are consistent) is what matters. This is a minor cross-group comparison concern.

### Trivial

- Table captions throughout are duplicated multiple times due to PDF extraction artifacts. While this is a parser issue, authors should ensure clean rendering in the final submission.

## Nice-to-Haves

- **Higher-order statistical test.** Since the method guarantees only up to third-order moments, testing whether fourth-order statistics (e.g., squared-norm distribution, kurtosis) match those of a true Gaussian would strengthen the losslessness claim.
- **PRC implementation details.** The ~10⁴× extraction speedup (Figure 4) warrants a brief note on the PRC configuration used (code rate, BP iterations) to ensure the comparison is not unfairly advantaged.
- **Undetectability classifier power analysis.** Showing that the ResNet-18 successfully detects Tree-Ring and Gaussian Shading demonstrates the test is not insensitive, but does not guarantee it would detect 4th-order deviations. A brief discussion of statistical power would be helpful.

## Removed Points

These points were raised in the inputs but removed after verification against the paper:

- *"The paper's claim that PRC 'can hit an irreducible error floor' is true of any error-correcting code"* — The paper's statement is accurate and not misleading; every method has a failure regime.
- *"Figure 2 caption contains 'True Ring' as a typo for 'Tree-Ring'"* — Minor and not substantive.
- *"The FID values are too high by standard conventions"* — This is addressed by the paper stating FID is "measured against the unwatermarked output distribution," which explains the high baseline. The issue is clarity of presentation, not correctness.
- *Strength Finder's claim that "Figure 2 confirms near-50% accuracy for the proposed method"* — The figure does not show this based on the caption. Removed as factually incorrect about what Figure 2 displays.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension between *theoretical* and *empirical* claims of undetectability. The paper provides a clean theoretical guarantee (spherical 3-design matching moments up to degree 3) that is mathematically rigorous for what it claims, but the empirical verification of that guarantee via classifier-based tests (Figure 2) is where the paper stumbles — the very figure meant to support the theory is incomplete. This suggests that even rigorous theoretical papers in this space need to be especially careful about empirical presentation, because the claim of "undetectability" is ultimately a claim about what an adversary cannot distinguish, which must be verified transparently.

## Suggestions

1. **Fix Figure 2 immediately.** Replot to show all four methods (Tree-Ring, Gaussian Shading, PRC, Ours) in both latent-level and image-level panels, or explicitly correct the text to reference the correct figure/table for the missing methods. This is the single most impactful fix.
2. **Clarify the FID methodology** in the table caption and body text. State explicitly what distributions are being compared and note that the "Original" row establishes the baseline sampling variance.
3. **Add a brief security-model discussion** acknowledging the single-point-of-compromise with the fixed signature K, and how this compares with per-image key schemes.
4. **Rephrase "statistically indistinguishable" to "statistically indistinguishable up to third-order moments"** in the abstract and introduction, to match the precision of the theoretical analysis.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| fkNsgI1nye (Secure Diffusion Model Unlocked) | 3.00 | R1 | Lower-quality paper with encryption focus; current paper is clearly stronger |
| hYEV8QmaOt (From Forgery to Authenticity) | 3.40 | R1 | Anti-forensics paper; less relevant, weaker than current paper |
| 1IwoEFyErz (Shallow Diffuse) | 6.00 | R1 | Similar watermark domain; rejected despite 6.0 due to presentation issues. Current paper has worse presentation issue (Figure 2) but stronger theory |
| ll2nz6qwRG (Hidden in the Noise / WIND) | 5.83 | R1 | Accepted watermark paper. Current paper has more novel technique but a more concrete evidential gap |
| j7b4mm7Ec9 (Towards Lightweight Deep Watermarking) | 7.60 | R1 | Strong paper with different focus (lightweight models); not directly comparable |

**Round 2 (Narrowing):**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| HexshmBu0P (A Recipe for Watermarking DMs) | 5.33 | R2 | Recipe paper; much less novel than current paper, weaker on theory |
| ETFfXGM3e4 (SAT-LDM) | 5.50 | R2 | Training-based watermark; methodological concerns. Current paper is stronger on theory but has the Figure 2 gap |
| jlhBFm7T2J (Undetectable watermark / PRC paper) | 6.50 | R2 | The direct baseline PRC paper, accepted. Current paper compares against this; PRC paper has robustness concerns but no Figure 2-like evidential gap |
| ll2nz6qwRG (WIND) | 5.83 | R2 | Repeated from R1 |

**Bracket:** The paper clearly sits above the 3.0–3.4 range (it has substantive theory and experiments) and below the 7.6–8.0 range (it has a concrete evidential gap). The PRC paper (6.50) provides the most direct comparison: the current paper offers a more novel method and better robustness results, but the PRC paper does not have a central-evidence verification problem. Round 2 narrowed the bracket to 4.5–5.5, with the Figure 2 issue being the primary factor differentiating from accepted papers at 5.83–6.50.

**Final Score:** 5.0

**Reasoning for 5.0:** The paper has a genuinely novel method, solid theory, and thorough experiments across multiple dimensions. However, the Figure 2 issue is a concrete evidential gap in the paper's central claim *as submitted*. The reviewer cannot verify whether the claimed undetectability results (near-chance accuracy for Ours versus 100%/97% for Tree-Ring/Gaussian Shading) are actually shown in the one figure that is supposed to demonstrate them. This is a fixable presentation error, but in the current form it means the paper's most important empirical claim is not properly evidenced. A paper at 5.0 has a solid foundation with a fixable flaw — the authors should be asked to correct Figure 2 and resubmit.

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>