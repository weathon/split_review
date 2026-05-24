Now I have enough information. Let me compile the final review.

---

## Summary

This paper proposes BDSB, a framework that maps 3D cortical fMRI surfaces to 2D parametric "brain disks" via conformal mapping, then applies an unpaired Schrödinger Bridge diffusion model to enhance 3T BOLD fMRI signals toward 7T quality. The pipeline is evaluated across three experimental settings (synthetic, cross-dataset real, and TDM paired real) and shows consistent quantitative improvements over baselines (Cycle-GAN, OTT-GAN, OTE-GAN, SCR-Net, fast-DDPM) in SSIM, PSNR, FID, and downstream pRF decoding R².

## Strengths

- **Novel technical combination.** The pairing of conformal cortical surface parameterization with Schrödinger Bridge diffusion for fMRI enhancement is well-motivated and, to my knowledge, original. The conformal mapping ensures the 2D representation preserves local geometry, and the SB formulation naturally handles the unpaired setting that the data scarcity demands (Section 2.2–2.3).

- **Consistent quantitative improvements across all settings.** Table 2 shows BDSB outperforming five baselines on every metric in every experiment. In the synthetic setting, SSIM rises from 0.475 (raw LQ) to 0.855 (vs. 0.803 for the best baseline), and mean pRF R² rises from 18.30% to 24.00%. The pattern holds in the cross-dataset real experiment (R²: 20.26% → 25.91%) and the TDM real experiment (PSNR: 13.00 → 19.24). These are substantial, non-trivial gains.

- **Well-designed ablation study.** Table 3 cleanly isolates the contributions of conformal mapping (vs. harmonic mapping and direct slicing) and the two regularization terms (PatchNCE, BD-SSIM). The ablation confirms that both the surface parameterization choice and the structure-preserving losses are essential — direct slicing collapses SSIM to 0.237, while adding BD-SSIM raises R² from 22.02% to 24.00%.

- **Practical experimental design given data constraints.** The authors are honest about the near-total absence of large-scale paired 3T/7T visual fMRI data and design three complementary experiments (synthetic, cross-dataset, TDM) that together stress-test the method under different levels of data availability. The dual strategy of using controlled synthetic data for ground-truth evaluation and real cross-dataset data for practical demonstration is sensible.

- **Convincing qualitative evidence.** Figure 4 shows enhanced brain disks that visually match ground-truth 7T disks across subjects, runs, and time points. Figure 5 demonstrates that enhanced time series track ground truth well for strongly responsive vertices. Figure 7(b) shows that enhanced fMRI yields more stable receptive center estimates across randomized stimulus intervals, confirming improved temporal interpretability.

## Weaknesses

### Fatal

None.

### Major

- **The "comparable to 7T quality" claim is unsubstantiated.** The abstract states the method makes enhanced 3T data "comparable to 7T quality," and the conclusion repeats that it "achieves signal quality and downstream performance comparable to native 7T scans." Yet the one experiment where this could be directly tested — the synthetic setting, where 7T ground-truth fMRI is available — never reports the native 7T pRF R². Table 2 shows raw LQ R² = 18.30% and enhanced R² = 24.00%, but the mean R² of the 7T data itself is absent. Figure 7(a) shows the full scatter distribution, so the data clearly exist, but without the summary statistic the reader cannot judge whether the gap was closed from (say) 30%→18% to 30%→24% (a large remaining gap) or from 26%→18% to 26%→24% (genuinely close). This is not a data-collection problem — the number already exists and must be reported for the central claim to be evaluable. The claim should either be supported with the missing number or recalibrated to what the evidence actually shows: a significant *improvement toward* 7T quality.

- **No individual-level fidelity analysis in the cross-dataset real experiment.** In this setting, 3T NOD data are mapped to the 7T NSD distribution across different subjects with no paired ground truth. The evaluation relies on FID (a distribution-level metric) and downstream pRF R². Because the model is trained unpaired and cross-subject, the improvements could arise from the model learning to replace subject-specific BOLD patterns with generic "7T-typical" patterns rather than faithfully enhancing individual signals. This matters because the stated use case is subject-level retinotopic mapping. The paper does not provide any analysis that would distinguish faithful enhancement from distribution matching — for instance, split-half reliability of enhanced retinotopic maps within subjects, or demonstration that known idiosyncratic topographic features are preserved rather than averaged away. The limitation is acknowledged in Section 4 ("Lack of Paired Data") but is not accompanied by any mitigatory analysis.

### Minor

- **FID computation on brain disks is unexplained and its validity is unclear.** FID is reported as a primary metric (Table 2), but the paper never describes how it was computed on parametric disk representations of cortical fMRI — what feature network was used, whether it was the standard InceptionV3 pretrained on ImageNet, or how the disk images were preprocessed. Applying an ImageNet-pretrained feature extractor to brain disk images is non-standard and the paper owes the reader a justification or, at minimum, a description. This weakness is mitigated by the fact that FID trends align with SSIM, PSNR, and R², so the paper's conclusions do not depend solely on FID.

- **TDM experiment is too small for strong conclusions.** The TDM real experiment uses only 2 subjects with 3 training runs and 3 test runs each. The paper correctly notes this limitation (Section 2.1), but the conclusions drawn from TDM results (lines 137–138, Table 2) should be explicitly hedged given the sample size.

- **BD-SSIM vs. FID trade-off is not discussed.** Table 3 shows that adding BD-SSIM improves PSNR (24.26 → 25.05) and R² (22.02 → 24.00) but worsens FID (34.23 → 42.88). This trade-off between distribution-matching and structural fidelity is interesting and merits brief discussion — it may indicate that BD-SSIM prioritizes functionally meaningful structure at some cost to distributional alignment.

### Trivial

- Table 3 column labels "Reg face" and "Reg hslsim" are cryptic; they should directly name the losses (PatchNCE and BD-SSIM).

## Nice-to-Haves

- Statistical testing or confidence intervals for the comparisons in Table 2 would strengthen conclusions, particularly given small test sets (2 subjects per experiment).
- The potential interpolation effects from upsampling NOD data from 32k fsLR to 164k fsaverage (Section 2.2) could be briefly discussed.
- A concise pseudocode for the inference procedure would aid reproducibility, though the appendix (stripped here) may already contain this.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Removed:** "The inference procedure is not explained with sufficient clarity" — the paper defers inference details to Appendix B.1, which was stripped by the parser. This is not a valid criticism of the submitted paper.
- **Removed:** "The synthetic LQ generation does not model other 3T-vs-7T differences (susceptibility artifacts, etc.)" — the paper already acknowledges this limitation in Section 4 ("Synthetic Data" paragraph) and explicitly states that down-sampling and noise injection "cannot fully capture scanner hardware, pulse sequence, or subject-level variability." The criticism is redundant with the paper's own discussion.
- **Removed:** "Figure 5(b) shows poor alignment for inactive vertices" — the paper already discusses this explicitly (lines 182–198): "for inert vertices, where the signal remains relatively constant, the alignment is weaker. This discrepancy likely arises from the difficulty in learning unchanging values."
- **Removed:** "No statistical testing or confidence intervals are reported" — this is moved to Nice-to-Haves; it is a standard practice (not a gap) for this type of benchmark evaluation, and Figure 7(b) already provides a form of variability analysis via 50 independent pRF analyses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Report the native 7T pRF mean R² for the synthetic experiment and use it to calibrate the abstract/conclusion claims. If the gap between enhanced (24.00%) and 7T ground truth is small, make that explicit; if it is large, reframe the contribution honestly as "a measurable step toward 7T quality" rather than "comparable to 7T quality."
- For the cross-dataset experiment, add at minimum a within-subject consistency analysis (e.g., split-half reliability of eccentricity/angle estimates across runs) to demonstrate that the enhancement preserves individual-level retinotopic organization rather than just matching the 7T distribution.
- Describe the FID computation (feature network, preprocessing) or replace it with a metric more appropriate for cortical surface data.
- Add a sentence discussing the BD-SSIM/FID trade-off observed in Table 3.

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| MRI Super-Resolution — Cerebellum | exei8zvY13 | 2.00 | R1 (low) | Much weaker; narrow technical contribution |
| Efficient Multi-Subject Visual Recon. | z2QdVmhtAP | 3.00 | R1 (low) | Weaker; limited novelty and evaluation |
| LEA: Latent Embedding Alignment | QdHg1SdDY2 | 3.00 | R1 (low) | Weaker; narrower scope |
| MindLoc | A5utJ4xf27 | 2.33 | R1 (low) | Much weaker; different problem |
| Rethinking Brain-to-Image Recon. | UUNTAwJIIn | 4.00 | R1 (mid) | Weaker; less technical novelty |
| fMRI-PTE | BZkKMQ25Z7 | 4.00 | R1 (mid) | Weaker; less complete evaluation |
| Universal Brain Encoder | xHGL9XqR8Y | 6.25 | R1 (mid) | Stronger; more validated contribution |
| Toward Generalizing Visual Decoding | At9JmGF3xy | 5.75 | R1/R2 (mid) | Comparable quality; BDSB has more technical novelty but similar overclaim issues |
| MindSimulator | vgt2rSf6al | 5.75 | R2 | BDSB has stronger technical contribution and better-controlled experiments |
| Mirror Schrödinger Bridges | 0F1rIKppTf | 5.75 | R2 | Related method but different application |
| Self-Supervised dMRI Denoising | wxPnuFp8fZ | 6.80 | R2 | Stronger; more thorough validation |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowing:** The paper sits above the 5.75 cluster (MindSimulator, Toward Generalizing) in technical novelty and experimental quality, but below the 6.80 dMRI Denoising paper due to the overclaim and missing individual-level validation. Final placement: **5.5**.

The paper addresses a genuine and important problem — enhancing 3T fMRI using unpaired 7T data for retinotopic mapping — with a clever technical approach that combines conformal surface parameterization and Schrödinger Bridge diffusion. The experimental results show consistent and substantial improvements over baselines. However, the central claim of "comparable to 7T quality" is unsubstantiated because the one number that could verify it (native 7T pRF R²) is missing, and the cross-dataset real experiment lacks any analysis that would confirm individual-level fidelity rather than mere distribution matching. These are addressable issues — the 7T R² data already exist, and within-subject consistency analyses are feasible — but as they stand they undermine the paper's headline claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>