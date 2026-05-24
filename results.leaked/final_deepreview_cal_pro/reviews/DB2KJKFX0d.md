## Summary

This paper presents BDSB, a framework that enhances 3T BOLD fMRI toward 7T quality by mapping cortical surface fMRI onto a shared 2D parametric disk via conformal mapping, then applying an unpaired Schrödinger Bridge diffusion model with structural regularization. The method is evaluated across three experimental settings (synthetic, cross-dataset real, and paired TDM) using both image-similarity metrics and downstream pRF retinotopic decoding. Results show consistent improvements over baselines and the ablation study validates the contributions of conformal mapping and the BD-SSIM regularizer.

## Strengths
- **Novel and well-motivated methodological combination.** The conformal brain disk parameterization (Section 2.2) elegantly solves the cross-subject, cross-dataset alignment problem, enabling unpaired 3T→7T translation on a shared 2D domain. The ablation (Table 3) directly validates this: conformal mapping achieves SSIM=0.849 vs. 0.237 for naive slicing, confirming geometric fidelity is critical.
- **Comprehensive multi-faceted evaluation compensates for the scarcity of paired 3T/7T data.** The paper constructs synthetic, cross-dataset, and limited paired TDM experiments (Section 2.1, Table 1), providing both controlled ground-truth comparisons and realistic cross-scanner assessments. This is a pragmatic and principled response to a genuine data scarcity problem.
- **Strong quantitative results across all experimental settings.** On synthetic data, the proposed method reduces FID from 152.3 (raw LQ) to 42.88 and raises pRF \( \bar{R}^2 \) from 18.30 to 24.00—both substantially better than all baselines (Cycle-GAN, OTT-GAN, OTE-GAN, SCR-Net, fast-DDPM). Cross-dataset results show similar gains (FID 183.83→70.65, \( \bar{R}^2 \) 20.26→25.91) despite having no paired ground truth.
- **Ablation study cleanly isolates each component's contribution.** Table 3 demonstrates that conformal mapping, PatchNCE, and BD-SSIM each provide measurable, complementary gains in both image quality (PSNR, FID) and downstream decoding (\( \bar{R}^2 \)), with BD-SSIM contributing +2.1 \( \bar{R}^2 \) points over the unregularized model.
- **Downstream pRF validation demonstrates practical utility beyond image metrics.** The enhanced fMRI yields visibly sharper, more coherent retinotopic maps (Fig. 6) and more stable receptive center estimates under randomized stimulus intervals (Fig. 7b), confirming that the signal enhancement translates to better functional interpretability.

## Weaknesses

### Fatal
None.

### Major
- **The 7T ground-truth \( \bar{R}^2 \) is never reported quantitatively, weakening the central claim.** In the synthetic experiment, the paper reports that raw LQ achieves \( \bar{R}^2 = 18.30 \) and the enhanced output reaches 24.00, but never states what \( \bar{R}^2 \) the native 7T data achieves. Without this ceiling, the reader cannot assess how much of the 3T–7T gap was actually closed. Figure 7(a) shows the scatter qualitatively and the text says the enhanced results maintain "a comparable confidence threshold to the ground truth," but a single aggregate number for the 7T baseline is essential to justify the repeated claim that enhanced data is "comparable to 7T quality" (abstract, conclusion). This is the most significant evidential gap in the paper.
- **The claim of "comparable to native 7T scans" (Conclusion) is overstated given the current evidence.** The synthetic experiment shows clear improvement but the gap to 7T is unquantified; the cross-dataset experiment has no ground truth at all; TDM is acknowledged as too small (2 subjects, 1 session each) to carry independent weight. The paper would be on firmer ground claiming "substantial improvement toward 7T quality" rather than equivalence.

### Minor
- **No variance estimates (standard deviations, confidence intervals, or per-subject breakdowns) are reported for any metric in Tables 2–3.** With test cohorts of only 2 subjects per experiment, the reader cannot assess whether observed differences are robust or driven by individual subjects. The large-magnitude improvements (e.g., FID dropping by ~110 points) make it unlikely that the gains are spurious, but including variance would significantly strengthen confidence.
- **The BD-SSIM loss and the reference structure \( x' \) are not fully specified in the main text.** Section 2.3 introduces BD-SSIM as a structural regularizer between generated brain disks and "the original fsaverage BD structure \( x' \)," but how \( x' \) is constructed (fixed geometric template? subject-specific?) and the exact formulation of BD-SSIM are deferred to the appendix. The ablation (Table 3) shows this term is important, so the mechanism deserves more than a one-sentence description in the main paper.
- **The synthetic degradation model (downsampling + Gaussian noise) is a simplified proxy for real 3T–7T differences.** The paper acknowledges this in the Discussion, and the cross-dataset real experiment partially mitigates the concern, but the simplicity of the degradation should be noted earlier rather than only in Section 4.

### Trivial
- **Table 2 bolding inconsistency on TDM SSIM.** OTT-GAN's SSIM (0.727) is bolded as best, but Proposed achieves 0.718. The method is still best on PSNR and FID for TDM, so the narrative is not undermined, but the bolding should be corrected.
- **Table 3 uses opaque abbreviations "Reg_face" and "Reg_hslsim"** rather than the clearer "PatchNCE" and "BD-SSIM" used in the text. This makes the ablation table harder to parse without cross-referencing.
- **"Spatiotemporal resolution" in the abstract/introduction** is slightly imprecise—the method enhances spatial resolution (via surface upsampling) and SNR, but does not alter the temporal sampling rate. "Spatial resolution and SNR" would be more accurate.

## Nice-to-Haves
- Reporting the 7T ground-truth \( \bar{R}^2 \) for the synthetic experiment as a single number would immediately contextualize the gap closure and is the highest-impact addition the authors could make.
- A supervised paired upper bound (e.g., training a simple U-Net on paired synthetic LQ/HQ brain disks) would provide a ceiling for how well any method could perform in the synthetic setting and contextualize the unpaired BDSB results.
- Temporal-coherence evaluation (e.g., autocorrelation or spectral properties of enhanced time series) would help rule out frame-to-frame artifacts introduced by the generative model, which processes each time slice independently.
- Per-subject or per-run breakdowns of all primary metrics would increase confidence given the small test cohorts.
- pRF retinotopic map visualizations for at least the strongest baseline (OTT-GAN) alongside the proposed method would strengthen the claim that baselines produce "spurious BDs" that distort brain structure.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Incomplete baseline comparison for downstream decoding — no pRF outcomes reported for any baseline."** (Harsh Critic) — **REMOVED as factually incorrect.** Table 2 reports \( \bar{R}^2 \) for every baseline in both the synthetic and cross-dataset experiments (e.g., Cycle-GAN: 17.22, OTT-GAN: 18.01, Proposed: 24.00). The pRF metrics are clearly present. The Harsh Critic appears to have missed the \( \bar{R}^2 \) column in Table 2.

2. **"The introduction of BD-SSIM is opaque / the exact formulation of \( \mathbb{L}_{\text{Reg}_{\text{bdl}}} \) must be given."** (Harsh Critic) — **DEMOTED to Minor, not removed entirely.** The formulation is deferred to Appendix B.1 (referenced in the text), which is standard practice. The concern about insufficient description in the main text is retained as Minor, but the assertion that the method is incomplete is speculative without seeing the appendix.

3. **"No paired supervised upper bound"** and **"No temporal-coherence evaluation"** and **"No discussion of potential hallucination"** (Harsh Critic) — **MOVED to Nice-to-Haves.** These are suggestions for additional experiments, not flaws in the existing work. The paper's evaluation is already more comprehensive than typical for its domain.

4. **"TDM is acknowledged as small; the decision to still treat it as a third experimental pillar is questionable."** (Harsh Critic) — **REMOVED.** The paper is explicitly transparent about TDM's limitations (Section 2.1: "making the dataset too small to support large-scale training") and treats it as supplementary, not a pillar.

5. **"The synthetic degradation is simplistic"** — **DEMOTED to Minor.** The paper acknowledges this in the Discussion. Retained as a minor point for transparency to readers.

6. **Strength Finder: "Enhanced BOLD time series exhibit better alignment with ground truth and increased temporal stability."** — **RETAINED but qualified.** Fig. 5 shows alignment for one active and one inert vertex; Fig. 7b shows improved stability for top-40 vertices. The evidence is real but limited to selected examples.

## Novel Insights
None beyond the paper's own contributions. The core insight—that conformally mapping cortical surfaces to a shared 2D disk enables unpaired Schrödinger Bridge translation across scanners and subjects—is genuinely novel and well-motivated by the paper's own arguments.

## Suggestions
- **Highest priority:** Add the 7T ground-truth \( \bar{R}^2 \) for the synthetic experiment and soften the "comparable to 7T" language to "substantially bridges the gap toward 7T quality" or similar.
- Add variance estimates (standard deviations across subjects/runs) for all metrics in Tables 2–3, even if only as supplementary material.
- Move a concise definition of BD-SSIM and the construction of \( x' \) into the main text (one paragraph in Section 2.3), rather than relying entirely on the appendix.
- Fix the Table 2 bolding for TDM SSIM and rename ablation headers to "PatchNCE" and "BD-SSIM" for clarity.
- Replace "spatiotemporal resolution" with "spatial resolution and SNR" throughout the abstract and introduction.

## Score and Decision

### Calibration Anchors Retrieved

**Round 1 (Bracketing):**
| Anchor ID | Paper | Avg Score | Band | Comparison |
|-----------|-------|-----------|------|------------|
| exei8zvY13 | Cerebellum MRI Super-Resolution | 2.00 | <3.5 | Significantly weaker — limited scope, poor results |
| z2QdVmhtAP | fMRI Visual Reconstruction | 3.00 | <3.5 | Weaker — incremental, limited validation |
| vgt2rSf6al | MindSimulator | 5.75 | 3.5–7.5 | BDSB has more comprehensive evaluation and clearer contribution |
| ujX2l7mNX6 | MindGPT | 5.75 | 3.5–7.5 | BDSB has stronger quantitative results and ablation |
| MEbNz44926 | Flexible Residual Binarization (image SR) | 8.00 | >7.5 | Different domain, not directly comparable |

**Round 2 (Narrowing within 4.5–7.5):**
| Anchor ID | Paper | Avg Score | Comparison |
|-----------|-------|-----------|------------|
| zZ6TT254Np | PDH-Diffusion (fMRI synthesis) | 6.75 | BDSB has broader evaluation (3 experiments vs. 1) and stronger downstream validation but less theoretical depth. Similar overall quality. |
| OJsMGsO6yn | SIM (surface fMRI decoding) | 6.50 | BDSB has clearer ablation and presentation, comparable novelty. Slightly stronger contribution. |
| xHGL9XqR8Y | Universal Brain Encoder | 6.25 | BDSB has more complete evaluation and clearer methodology. |
| 3JoLo0mmHH | Coarse-to-fine Audio from fMRI | 5.25 | BDSB is clearly stronger in both method and evaluation. |

**Round 1 Bracket:** BDSB sits clearly above 5.25 (MindSimulator/MindGPT tier) and below the 8.0 range. Initial bracket: approximately 5.5–7.5.

**Round 2 Narrowing:** BDSB is comparable to or slightly stronger than SIM (6.50) and roughly on par with PDH-Diffusion (6.75). It has more comprehensive experimental validation than PDH-Diffusion but shares similar minor weaknesses around incomplete metric reporting and overclaim. It is clearly stronger than the 5.25–5.75 anchors.

**Final Score:** 6.5. The paper makes a genuine methodological contribution with solid experimental support. The main issues (missing 7T baseline \( \bar{R}^2 \), overclaimed conclusions, no variance reporting) are addressable without new experiments and do not invalidate the core contribution. The paper is comparable in quality to SIM (avg 6.50, accepted) and slightly below PDH-Diffusion (avg 6.75) primarily due to the unquantified 7T baseline.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>