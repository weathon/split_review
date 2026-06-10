## Summary

This paper presents an analysis of hard pixels in semantic segmentation by categorizing boundary errors into three types (false responses, merging mistakes, displacements) and linking them to frequency aliasing during downsampling. It introduces an Equivalent Sampling Rate (ESR) formula to compute the Nyquist frequency considering kernel size and channel expansion (not just stride), and an aliasing score to quantify aliasing. Two lightweight modules are proposed: a De-Aliasing Filter (DAF) that zeros out aliasing-causing frequencies before downsampling, and a Frequency Mixing module (FreqMix) that learns to weight low/high frequencies within encoder blocks. Experiments on Cityscapes (+1.6 mIoU), PASCAL VOC (+1.8), ADE20K (+1.5), and low-light instance segmentation (+1.1–1.2 AP) show consistent improvements with minimal computational overhead.

## Strengths

- **Empirical validation of the ESR-derived cutoff through systematic ablation (Table "lowcut").** The paper sweeps cutoff frequencies from 1/4×1.0 (stride-only) to 1/4×1.6. The ESR-based cutoff of 1/4×√2 achieves the best mIoU (79.3), outperforming the stride-only cutoff (78.6) while lower/higher cutoffs degrade performance. This direct ablation provides concrete evidence that the proposed formula identifies a useful threshold, irrespective of how one labels the theoretical justification.

- **DAF is parameter-free and adds negligible FLOPs while outperforming prior anti-aliasing methods.** In Table "compwithblur", DAF alone achieves 79.3 mIoU at 297.96G FLOPs (same as baseline), beating Blur (78.8, +0.5G), AdaBlur (78.9, +38.6G), and FLC (78.6). DAF+FreqMix reaches 79.7 at +0.71G FLOPs — substantially more efficient than AdaBlur's +38.6G overhead for lower performance.

- **The aliasing score provides a quantitative link between frequency-domain degradation and segmentation errors.** Table "blur" shows that inserting a 3×3 Gaussian blur drops the aliasing score from 9.4% to 0.27% with corresponding improvements in all three error types. Table "noise" shows Gaussian noise (σ=20) raises Stage-1 aliasing from 5.4% to 9.6% while mIoU collapses from 78.1 to 20.6. These controlled experiments establish a causal pathway that prior work on aliasing in neural networks only asserted qualitatively.

- **Consistent improvement across multiple datasets and generalization to low-light instance segmentation.** The method improves mIoU on Cityscapes (79.7 vs 78.1 baseline, +1.6), PASCAL VOC (76.1 vs 74.3, +1.8), and ADE20K (40.4 vs 38.9, +1.5). The low-light results (+1.1–1.2 AP on LIS) demonstrate transfer to a domain where noise-induced aliasing is a concrete and known problem, going beyond standard semantic segmentation benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The Equivalent Sampling Rate is framed as a strict signal-processing derivation, but this framing is imprecise.** The paper claims (line 162, Figure 2) that a stride-2, 2×2 kernel with 4× channel expansion achieves a spatial sampling rate of 1, not 1/2, because "all pixels are actually sampled." In standard signal processing, the spatial sampling rate after stride-2 is determined by the output grid density — it is 1/2. What changes with larger kernels and channel expansion is the *information capacity* of the output (different input positions can be routed to different channels), not the *spatial sampling density*. The Nyquist-Shannon theorem concerns the latter. The ESR formula may produce a useful heuristic cutoff (and the ablation in Table "lowcut" empirically supports that it does), but the paper's framing as a precise Nyquist-theoretic derivation is overstated. This does not invalidate the empirical results, but the paper should honestly reframe the ESR as an empirically motivated heuristic that captures the effective information-preservation capacity of the downsampling operation, rather than a correction to the spatial sampling rate. The current theoretical claim is not standard and invites reasonable skepticism.

### Minor

- **No variance or statistical significance is reported for any experimental result.** All tables report single numbers. The key comparisons involve differences of 0.4–0.8 mIoU (e.g., DAF at 79.3 vs AdaBlur at 78.9). Without run-to-run variance (3 seeds with mean±std), it is impossible to assess whether these differences are meaningful or within random seed variation. While single-run reporting is common in large-scale segmentation benchmarks, the margins here are small enough that variance information would substantially strengthen the evidence. The paper would be materially stronger with this addition.

- **The three-error-type taxonomy is descriptive but not well integrated into the method design.** The paper categorizes boundary errors into false responses, merging mistakes, and displacements, and shows they correlate differently with the aliasing score (Figure "boundary_error_type"). However, the proposed modules (DAF and FreqMix) reduce all three error types roughly equally (Table "compwithblur": FErr -2.0, MErr -1.8, DErr -2.1). If the taxonomy were informing specific design choices, one would expect different modules to target different error types. As presented, the taxonomy is an interesting observation about the problem space but does not drive architectural decisions in a way that distinguishes it from a general "reduce all boundary errors" approach. This weakens the claimed contribution of the taxonomy beyond what prior binary (easy/hard) distinctions already offer.

- **The FreqMix ablation (spatial vs. channel-wise weighting) is described in prose but the corresponding table is commented out with \iffalse (lines 377–397).** The text states the channel-wise component adds +0.4 mIoU but the actual tabular data with all metrics (BIoU, error types) is not visible in the compiled paper. This should be included as a proper table rather than deferred to prose. (Note: this appears to be a formatting artifact rather than intentional omission, but it should be fixed.)

### Trivial

- No limitations or failure cases are discussed. While not required, this is standard practice in top-venue papers and would strengthen the presentation.

## Nice-to-Haves

- **Ablate the FreqMix threshold.** Since FreqMix separates $f^{\downarrow}$ and $f^{\uparrow}$ using the ESR-based Nyquist frequency, an ablation comparing ESR-based vs. stride-based vs. learned threshold would directly test whether the ESR calculation contributes to FreqMix performance or whether any reasonable split works equally well.
- **Compare against DepthAdaBlur (2023)**, which is cited in related work but not included in experimental comparisons.
- **Report variance (3-run mean±std)** for the main Cityscapes comparison to confirm the 0.4–0.8 mIoU margins are significant.
- **Soften the DAF hard threshold** or discuss potential ringing artifacts from zeroing frequency bins in the Fourier domain. A soft or learnable mask could be considered.
- **Motivate the sigmoid constraint in FreqMix** that limits weights to [0,1] (down-weighting only). It is conceivable that amplifying some frequencies (weight > 1) could be beneficial.

## Removed Points

*These points were flagged by reviewers but are removed from the main assessment for the following reasons:*

- **"Missing related works on frequency-domain analysis for segmentation"** — Rule: Do not mention missing related works when you cannot verify their existence. This also misses that the paper discusses frequency learning in Section 2 (lines 106–112).
- **"No comparison against OHEM/focal loss/hard-region mining"** — These are training-time loss reweighting methods addressing a different problem (sample difficulty during optimization) than aliasing-induced degradation at boundaries. Scope creep.
- **"The correlation evidence in the introduction is not quantitative"** — The evidence is presented in Figure "boundary_error_type" (correlation curves), which is standard practice. The introduction summarizes it with a figure reference.
- **"DAF hard thresholding causes ringing artifacts"** — Speculative. The paper does not evaluate this, and the critic provides no evidence that ringing actually occurs at the reported thresholds.
- **"FreqMix sigmoid limits weights to [0,1]"** — This is a legitimate design choice; the critic speculates that >1 weights might be better without justification.
- **"Figure 2 is misleading"** and **"ESR is not how sampling works"** (framed as fatal) — The core point (theoretical imprecision) is retained as Major. The "fatal" framing is removed because the empirical evidence in Table "lowcut" independently validates the cutoff choice, and the issue is one of conceptual framing rather than the method being wrong or the results being invalid.
- **"The commented-out table is a drafting leftover" and "No Limitations section"** — Speculative or non-standard expectations.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the ESR contribution honestly.** Explicitly state that the formula is an empirically motivated heuristic that accounts for the information-preservation capacity (kernel × channel expansion) of a downsampling operation, rather than a strict spatial sampling rate derived from Nyquist-Shannon theory. The empirical validation in Table "lowcut" is the real evidence for the cutoff choice — lean on it.
2. **Report 3-run mean±std** for at least the main Cityscapes comparison table to demonstrate that the 0.4–0.8 mIoU differences are stable across seeds.
3. **Include the FreqMix ablation table** (currently \iffalse'd) directly in the paper with all reported metrics.
4. **Either (a) show that the three-error taxonomy leads to targeted design decisions** (e.g., a module that specifically reduces displacement errors more than other types), **or (b) tone down the claimed importance of the taxonomy** and present it as a descriptive analysis rather than a driving contribution of the method.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>