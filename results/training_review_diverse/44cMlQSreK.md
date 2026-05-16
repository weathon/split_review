Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces NeuroQuant, a post-training quantization (PTQ) method for implicit neural representation–based video coding (INR-VC). NeuroQuant achieves variable-rate coding by adjusting quantization parameters (QPs) of a single pre-trained model rather than retraining for each target bitrate. The method combines: (1) a mixed-precision bit allocation strategy guided by a Hessian-vector sensitivity criterion Ω = Δwᵀ H Δw that accounts for inter-layer dependencies and perturbation directionality; (2) network-wise calibration and channel-wise quantization to minimize reconstruction distortion. Experiments on UVG show NeuroQuant outperforms existing PTQ methods (AdaRound, BRECQ, QDrop, RDO-PTQ) and QAT-based INR-VC methods (FFNeRV, HiNeRV) across bitwidths, with up to 7.9× encoding speedup for achieving a new bitrate.

## Strengths

- **First PTQ framework for variable-rate INR-VC.** The paper is the first to demonstrate that variable-rate INR-VC can be achieved by adjusting quantization parameters of pre-trained weights rather than retraining for each bitrate (Sec. 1, Fig. 1). Table 2 provides concrete evidence: NeuroQuant supports a new bitrate in 1.8–2.8 hours compared to 10–22 hours for retraining, a speedup of up to 7.9×. This fills a practical gap in the INR-VC literature.

- **Theoretically motivated sensitivity criterion that addresses inter-layer dependencies.** Theorem 1 and the derivation in Sec. 3.1 define Ω = Δwᵀ H^(w) Δw, which captures off-diagonal Hessian terms and perturbation direction. The paper provides concrete counterexamples (Eq. 7–8) showing why prior Hessian-based criteria (HAWQ, HAWQ‑V2) that assume layer independence and isotropy are insufficient for non-generalized INR-VC. The Hessian-vector product approximation (Eq. 10) makes the criterion tractable.

- **State-of-the-art quantization results across architectures and bitwidths.** Table 1 shows NeuroQuant consistently outperforms AdaRound, BRECQ, QDrop, and RDO-PTQ at all bitwidths on UVG, with the advantage growing at lower bitwidths. At INT2, NeuroQuant surpasses QAT-based HiNeRV by >3 dB PSNR across all model sizes. The method works across three different INR-VC architectures (NeRV, HNeRV, HiNeRV).

- **Empirical validation of variable-rate capability.** Fig. 4 presents R-D curves where NeuroQuant achieves 25.5–27.8% bitrate savings over direct 8-bit quantization baselines, and 4.8% over HiNeRV's built-in QAT. The analysis of mixed-precision vs. unified precision (Fig. 5) demonstrates that mixed precision enables finer-grained rate control.

- **Theoretical grounding connecting representation and compression.** Sec. 3.3 reframes NeuroQuant through variational inference, explaining that prior INR-VC methods optimize p(x|w) (representation only), while NeuroQuant directly optimizes p(x|w̃) (representation after quantization), resolving a mismatch that degrades performance after compression (Remark 2).

## Weaknesses

### Fatal
None.

### Major
None that threaten the core contribution. The paper's claims (first PTQ for INR-VC, principled sensitivity criterion, SOTA results) are all reasonably supported.

### Minor

- **Mixed-precision allocation algorithm is underspecified.** The paper mentions that the sensitivity criterion Ω "enabl[es] efficient mixed-precision search using techniques like integer programming, genetic algorithms, or iterative approaches" (line 127), but does not specify which method was actually used, nor its hyperparameters. This is a reproducibility gap. Additionally, the paper does not clarify how the circular dependency is resolved: Ω = Δwᵀ H Δw depends on Δw, which itself depends on the chosen bitwidths. While iterative/greedy schemes are standard in practice, the paper should specify the actual procedure.

- **The claim that network-wise calibration is necessary is not isolated by ablation.** The paper argues that layer/block-wise calibration fails for INR-VC due to inter-layer dependencies, and adopts network-wise calibration. However, NeuroQuant differs from the compared baselines (AdaRound, BRECQ, QDrop, RDO-PTQ) along multiple dimensions simultaneously: mixed-precision allocation, the Ω sensitivity criterion, channel-wise granularity, *and* network-wise calibration. No ablation is presented where only calibration granularity is varied (e.g., NeuroQuant with layer-wise vs. block-wise vs. network-wise calibration while keeping all other components fixed). The qualitative evidence in Fig. 3(c) ("statistic of the weight distribution") is not accompanied by a quantitative metric (e.g., block-wise Hessian off-diagonal magnitude). This weakens the attributability of the gains to the proposed calibration granularity specifically.

- **Figure 5 (left) shows available rate points but not a direct R-D comparison.** The left subplot of Fig. 5 shows the number of available rate points for mixed vs. unified precision, but does not compare actual R-D performance at the same total bitrate. A direct R-D curve comparing mixed-precision NeuroQuant against the best unified-precision model (at matched bitrates) would more cleanly demonstrate the benefit of mixed-precision rate control.

- **Calibration time per bitrate point is not reported.** Table 2 usefully reports encoding time to support a new bitrate, but the per-bitrate calibration time (which is the true "cost" of adding a bitrate point with PTQ) is not broken out. This would help users understand the practical overhead.

- **Only the UVG dataset is evaluated.** While UVG is the standard benchmark in INR-VC literature, adding a second dataset (e.g., a subset of JVET sequences) would strengthen claims of generalizability. This is a minor scope limitation.

- **Statistical variance is not reported for PSNR results.** Table 1 reports PSNR without variance across sequences. Given the small number of sequences, reporting mean ± std would provide a more complete picture.

### Trivial

- Theorem 1 calls Ω the "optimal sensitivity criteria." Under the stated assumptions (converged weights, zero gradient), Ω is the second-order Taylor term. Calling it "optimal" is a slight overstatement—it is the best *quadratic* approximation, but optimality under a well-defined objective (e.g., minimizing task loss increase) is not formally proven. The practical value of the criterion is clear; the wording could be softened.

## Nice-to-Haves

- **Validate that Ω correlates with actual task loss increase.** The paper uses Ω for bit allocation but does not empirically verify that Ω values correlate well with the measured loss increase under different bitwidth assignments. A correlation plot (predicted Ω vs. measured Δℒ for random bitwidth assignments) would strengthen the motivation for the sensitivity criterion.

- **Direct comparison of R-D curves with mixed-precision baselines.** If the compared PTQ baselines use unified precision, the comparison in Fig. 4 conflates the benefit of mixed-precision allocation with that of network-wise calibration. Running the best baseline (e.g., BRECQ or RDO-PTQ) with the same mixed-precision allocation would provide a fairer comparison.

- **Computational cost of the sensitivity search.** The paper mentions efficiency but does not report the wall-clock time or number of candidate evaluations needed for the mixed-precision search itself.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *No comparison to standard video codecs (H.265/H.266).* This is scope creep — the paper is about quantization methods for neural video representations, not about competing with traditional codecs as a video coding standard. The paper's contribution (PTQ for INR-VC) does not require this comparison.

- *"First time" claim is too strong given prior QAT methods.* The paper explicitly acknowledges QAT methods and compares against them. The claim is specifically about achieving variable-rate INR-VC through (post-training) weight quantization, which QAT methods do not do — they optimize weights during training with quantization awareness. The claim is defensible.

- *Criticism of the "optimal" label in Theorem 1 as overstated.* Under the stated assumptions (zero gradient, PSD Hessian), the second-order term is the dominant approximation. This usage is standard in optimization and not misleading in context.

- *Only one dataset / missing additional datasets.* This is a minor limitation acknowledged in the review; the paper follows the convention of the INR-VC literature (UVG is the standard benchmark). Demanding a second dataset is a nice-to-have, not a structural weakness.

- *Missing formatting details / parser artifacts.* These are not author errors.

## Novel Insights

The key insight that emerges from this review is that NeuroQuant's contribution lies not in any single novel component (the sensitivity criterion is a standard second-order approximation; the calibration objective follows AdaRound's framework; the variational inference perspective is not new to compression) but rather in the *composition* of these components adapted to the specific properties of non-generalized INR-VC models. The paper correctly identifies that INR-VC models violate two assumptions underlying existing PTQ methods — inter-layer independence and loss isotropy — and shows that addressing both simultaneously is necessary for good performance. This is a principled adaptation rather than a paradigm shift. The most practically significant claim is the dramatic encoding time reduction (up to 7.9×) while maintaining or improving compression quality, which directly addresses a real bottleneck in deploying INR-VC systems.

## Suggestions

1. **Specify the mixed-precision search algorithm.** State whether you used greedy iterative rounding, integer programming, or another method, and report its wall-clock time and the number of candidate evaluations. Clarify how the circular dependency (Ω depends on Δw, Δw depends on bitwidth) is broken.

2. **Add a calibration-granularity ablation.** Run NeuroQuant with layer-wise, block-wise, and network-wise calibration keeping all other components (Ω criterion, channel-wise QPs, mixed-precision allocation) fixed. Report the PSNR difference. This directly tests whether network-wise calibration provides the claimed benefit.

3. **Add a direct R-D comparison of mixed vs. unified precision at matched bitrates.** Replace or augment Fig. 5(left) with a plot showing R-D curves for NeuroQuant with mixed precision vs. the best unified-precision model at the same total bitrate.

4. **Report per-bitrate calibration time separately from total encoding time in Table 2**, so readers can see the cost of adding each additional rate point.

## Score and Decision

This is a solid technical paper that makes a practical contribution (first PTQ tailored to INR-VC with demonstrated speedup and quality improvements) with sound theoretical motivation. The identified weaknesses — underspecified allocation algorithm, missing ablation for calibration granularity, and minor presentation gaps — are all addressable and do not invalidate the core claims. The paper would benefit from a revision addressing reproducibility (especially the allocation algorithm) and strengthening the ablation evidence. On balance, the contribution is real and the paper is above the acceptance threshold.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>