Now I have a solid calibration. Let me construct the final review.

**Score calibration reasoning:**

- **Round 1 (bracketing):** Weak anchors (scores 2–3) are papers with fundamental methodological flaws or severe confounds — clearly worse than the current paper. Middle anchors (scores 4–7) include the fMRI synthesis paper at 6.75 (accepted) and the dMRI denoising paper at 6.80 (accepted). Strong anchors (scores 8) are clearly stronger papers with more thorough validation. So initial bracket: 5–7.

- **Round 2 (narrowing):** MindSimulator (5.75, accepted) has substantial confounds and weaker experimental validation — the current paper is stronger. Universal Brain Encoder (6.25, rejected due to novelty concerns) — the current paper has clearer novelty. The fMRI synthesis at 6.75 has more thorough validation. Comparing within bracket, this paper is stronger than 5.75 anchors and slightly below 6.75 anchors due to evaluation gaps (missing 7T baselines, no error bars, no pRF parameter comparison). **Final score: 6.0.**

---

## Summary

The paper proposes a pipeline for enhancing 3T BOLD fMRI toward 7T quality for retinotopic decoding. The approach maps 3D cortical surfaces onto a shared 2D parametric domain (Brain Disks) via conformal mapping, then applies an unpaired Schrödinger Bridge diffusion model (BDSB) to translate 3T-like fMRI distributions toward 7T distributions. The framework is evaluated on synthetic data (down-sampled 7T → reconstruct to original 7T), a cross-dataset real experiment (3T NOD → 7T NSD distribution), and a paired 3T/7T TDM dataset. Results show consistent improvements across SSIM, PSNR, FID, and downstream pRF R², outperforming several image-translation baselines.

## Strengths

- **Novel and well-motivated pipeline for a real problem.** The combination of conformal surface parameterization with an unpaired Schrödinger Bridge diffusion model is a technically coherent approach to the genuine challenge of limited paired 3T/7T fMRI data. Mapping 3D cortical surfaces onto 2D Brain Disks (Sec 2.2) provides a principled shared domain for cross-subject, cross-dataset alignment, and the unpaired design directly addresses the stated scarcity of paired data.

- **Consistent quantitative improvement across multiple settings.** Table 2 shows the proposed method outperforms all baselines on synthetic data (SSIM 0.855 vs. next-best 0.803, PSNR 25.05 vs. 23.39, FID 42.88 vs. 71.40, and — most importantly — downstream pRF R² 24.00 vs. 18.01 for raw LQ). In the cross-dataset real experiment, R² rises from 20.26 (raw 3T) to 25.91, while all baselines either plateau or degrade. The consistency across three distinct datasets (NSD, NOD, TDM) strengthens the generalizability claim.

- **Systematic ablation validating design choices.** Table 3 isolates the contribution of each component: conformal mapping over harmonic mapping (R² 22.02 vs. 16.97), and the additive gains from PatchNCE and BD-SSIM regularizations. This provides clear empirical support for the specific pipeline elements.

## Weaknesses

### Major

- **Missing ground-truth 7T metrics as an upper bound.** The paper's central claim is that enhanced 3T fMRI becomes "comparable to 7T quality" (Abstract), yet Table 2 does not report the corresponding native 7T metrics — most importantly the mean pRF R² of the original 7T test subjects in the synthetic experiment. Without this anchor, the reader cannot assess how close the enhanced R² of 24.00 actually is to genuine 7T quality (e.g., if native 7T R² is 24.5, the gap is tiny; if it is 35, the gap is large). The scatter plots in Fig 7(a) are helpful but do not substitute for a summary statistic. This is the single largest evaluation gap.

- **No error bars or variability measures.** All results in Tables 2 and 3 are reported as single values. The synthetic experiment uses only 2 test subjects, and the cross-dataset experiment uses 2 test subjects. Without standard deviations, per-subject breakdowns, or at least a range, the reader cannot judge the reliability or variability of the reported improvements. This is a basic requirement for empirical reproducibility.

- **No direct comparison of pRF parameters (center, size) in the synthetic experiment.** The primary downstream metric is R², but an increase in R² could partially reflect systematic amplitude scaling or structured noise rather than genuinely better decoding. While the stability analysis in Fig 7(b) helps, a direct comparison of estimated pRF centers and sizes (from enhanced vs. ground-truth fMRI) would provide much stronger evidence that the enhancement improves *decoding* rather than just *fitting*. This analysis is straightforward for the synthetic setting where ground-truth parameters are known.

### Minor

- **Cross-dataset confounds not disentangled.** In the cross-dataset experiment, source (NOD 3T) and target (NSD 7T) differ in visual stimuli, subjects, preprocessing pipelines, and potentially hemodynamic response functions. The paper acknowledges this limitation (Sec 4) but does not attempt to separate field-strength effects from dataset-specific shifts (e.g., mean activation levels). An experiment training on NSD synthetic data and testing on held-out NSD subjects (same stimuli, same pipeline, only field-strength simulated) would help isolate the source of the gains.

- **The BD-SSIM regularization term is underspecified.** Equation (5) includes "BD-SSIM between the generated BDs and the original fsaverage BD structure \(x'\)." The quantity \(x'\) is never explicitly defined — it appears to be a fixed template disk, but the text is ambiguous. The reader cannot tell whether this term penalizes deviation from an empty canonical disk, a mean fMRI template, or a structural mask. This should be clarified.

- **The resolution of the Brain Disks (pixel grid) is not reported.** The paper states that BDs are "generated by mapping BOLD fMRI time-series ... to their corresponding locations on the refined planar disk" (Sec 2.2), but never specifies the 2D grid dimensions. This matters for reproducibility and for assessing possible interpolation artifacts.

- **Baseline tuning is not documented.** The paper reports that baselines are adopted "to our pipeline" but does not state whether they were hyperparameter-tuned (e.g., via a validation set) for this specific task. If baselines were used with default parameters, the comparison may be unfair.

### Trivial

- Each time slice is processed independently by BDSB; temporal consistency across slices is not modeled. A brief analysis of temporal autocorrelation in the enhanced signals would strengthen the paper.
- The ablation table (Table 3) would benefit from including a "no BDSB" condition (e.g., simple mean/variance matching of distributions) to isolate the generative model's added value.

## Nice-to-Haves

- Report native 7T R² as an explicit row/column in Table 2 for the synthetic experiment.
- Add direct pRF parameter comparisons (center error, size error) for the synthetic setting.
- Add error bars (per-subject or bootstrapped) to Tables 2 and 3.
- Include a simple baseline such as histogram matching or voxel-wise variance scaling.
- Analyze temporal autocorrelation of enhanced vs. ground-truth time series.
- Clarify the definition of \(x'\) in the BD-SSIM term.

## Removed Points

- *"Reproducibility details missing (architecture, training regime, computing time)"* — The paper states these are in the appendix (Sec 3, "further training details listed in B.1"). The appendix is stripped from this extracted PDF; these details exist in the original submission.
- *"Missing ethical considerations"* — Not a standard requirement for this type of methods paper and not relevant to the evaluation.
- *"The claim cannot be independently verified because models/tools may not be released"* — The paper states code will be released; per protocol, cited resources are assumed to exist.
- *"The synthetic 3T data cannot capture scanner hardware variability"* — The paper already acknowledges this limitation (Sec 4, "Synthetic Data") and explicitly complements with real-data experiments.
- *"Baseline comparison is unfair because baselines are not designed for this task"* — The paper uses standard 2D translation models that are widely applied in medical imaging; the comparison is appropriate for assessing relative performance.
- *"Confounds in cross-dataset experiment are fatal"* — The paper acknowledges these limitations and includes the TDM experiment (paired subjects) and the synthetic experiment (controlled setting) as complementary evidence. The weakness is valid but not fatal.

## Novel Insights

None beyond the paper's own contributions. The main insight — that conformal mapping to a shared 2D domain enables unpaired Schrödinger Bridge translation of fMRI across field strengths — is well articulated by the paper itself. The reviewers did not surface a fundamentally new framing or unexpected connection.

## Suggestions

1. **Add native 7T metrics to Table 2.** For the synthetic experiment, append a column showing the SSIM/PSNR/FID of the original 7T data (trivial: 1.0/∞/0 for self-similarity, but the mean R² is non-trivial and critical). For the cross-dataset experiment, report the mean R² of the NSD subjects as a target ceiling.
2. **Add per-subject breakdowns or bootstrapped error bars** to all tables.
3. **In the synthetic experiment, directly compare estimated pRF centers and sizes** from enhanced vs. ground-truth fMRI (e.g., histograms of errors, scatter plots). This directly validates that the improvement reflects better decoding, not just better fitting.
4. **Clarify the definition of \(x'\)** in Eq. (5) and state the pixel resolution of the Brain Disks.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| Efficient Multi Subject Visual Reconstruction (z2QdVmhtAP) | 3.00 | 1 | Weaker: limited contribution, rejected |
| MindLoc Brain-Based Object Localization (A5utJ4xf27) | 2.33 | 1 | Weaker: serious methodological issues |
| fMRI-PTE Pretrained Transformer (BZkKMQ25Z7) | 4.00 | 1 | Weaker: limited novelty, rejected |
| X-Diffusion (urf8a5G59f) | 5.50 | 1 | Comparable: similar evaluation gaps, rejected |
| Synthesizing Realistic fMRI (zZ6TT254Np) | 6.75 | 1 | Stronger: more thorough validation, accepted |
| Self-Supervised dMRI Denoising (wxPnuFp8fZ) | 6.80 | 1 | Stronger: more comprehensive experiments, accepted |
| MindSimulator (vgt2rSf6al) | 5.75 | 2 | Weaker: less clean experiments, accepted |
| Universal Brain Encoder (xHGL9XqR8Y) | 6.25 | 2 | Slightly stronger: more thorough but novelty concerns, rejected |
| Generalizing Brain Decoding (At9JmGF3xy) | 5.75 | 2 | Comparable: similar level of validation, accepted |
| Solving Diffusion ODEs SR (BtT6o5tfHu) | 6.67 | 2 | Stronger: more rigorous evaluation, accepted |
| Decomposed Diffusion Sampler (DsEhqQtfAG) | 6.50 | 2 | Stronger: more thorough methodology, accepted |

**Round 1 bracket:** 5–7. After Round 2 narrowing, the paper sits above MindSimulator (5.75) but below the fMRI synthesis paper (6.75). The paper's contribution is real and the multi-dataset evidence is solid, but the evaluation gaps (missing 7T baseline, no error bars, no pRF parameter comparison) prevent it from reaching the 6.5+ tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>