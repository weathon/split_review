## Summary

This paper identifies a concrete problem in neural PDE surrogates — pointwise nonlinearities inject spurious high-frequency noise ("spectral junk") into learned solutions — and proposes a simple remedy: insert a discrete Gaussian low-pass filter after every nonlinearity. The diagnostic analysis (Figures 1–3) is strong and novel, and the method delivers consistent improvements in spectral fidelity and rollout accuracy across three challenging fluid dynamics problems (Kuramoto-Sivashinsky, Kolmogorov flow, Rayleigh-Bénard convection).

## Strengths

1. **Quantitative demonstration that pointwise nonlinearities inject high-frequency noise and spectral shaping removes it**: Figure 3b graphs the Fourier spectrum after a dozen activation functions; all raise amplitudes in the high-wavenumber band by 7–12 orders of magnitude relative to the clean signal. The curve for `G_σ * softplus` is the only one overlapping the original spectrum.

2. **Spectral shaping stabilizes the learned flow map**: Figure 1a shows eigenvalues of the linearized flow map. The vanilla UNet produces eigenvalues with magnitude >1 (up to 100× larger than unity), while the spectrally shaped model yields eigenvalues inside the unit circle, closely matching ground-truth and ETDRK4.

3. **Machine-precision one-step spectral match on KS**: Figure 3a shows the power spectral density of the spectrally shaped model overlapping the true spectrum down to the float64 round-off floor (~10⁻¹⁴) for one-step predictions.

4. **Consistent improvements in long-term rollout accuracy across three diverse PDEs**: Figure 6 reports MELR and decorrelation times. On Kolmogorov flow spectral shaping outperforms all competing stabilization methods (denoising, pushforward, autoregressive) by a wide margin; on RBC it is the only technique achieving decorrelation time above zero for τ₀.₈.

5. **Ablation shows filtering after every nonlinearity is critical, not just at the output**: Figure 8 compares spectral shaping (filter after every activation) with post-filtering (filter only the model output). While both reach similar minimum spectral gaps, spectral shaping consistently yields higher decorrelation times, especially on RBC.

6. **Phase-space diagrams confirm capture of the correct solution manifold**: Figure 5 shows 2D histograms of uₓ vs. uₓₓₓ with two-sample KS distances to ground truth. Spectral shaping achieves Dₙ = 0.0011, beating denoising (0.0013), pushforward (0.0102), and baseline (0.0344).

7. **Spectral shaping is compatible with spectral-loss regularizers**: Figure 9 combines spectral shaping with MELR and DySLIM losses. In every combination, adding shaping further reduces MELR and increases decorrelation time, showing the architectural fix provides benefits unavailable from loss functions alone.

## Weaknesses

### Fatal
None.

### Major

1. **Only one architecture tested — the generality claim is unvalidated.** The paper tests spectral shaping exclusively on UNet (line 145: "We focus on the UNet"), yet the title, abstract, and framing promise a broadly applicable principle for "Neural PDE Surrogates." Many neural PDE surrogates use other architectures (FNO, DeepONet, graph networks, transformers) that also contain pointwise nonlinearities and would in principle exhibit the same spectral junk. Without validation on at least one additional architecture, the contribution is demonstrated only for UNet-based surrogates. A practitioner working with FNO or a transformer-based surrogate has no experimental basis to trust that the method transfers. This is the most impactful gap — the experiments and code are already in place, and adding one more architecture would directly justify the claimed generality.

2. **No statistical significance or variance reporting in main results.** Figures 6, 8, and 9 present bar charts and box plots without any indication of multiple random seeds. The paper states each bar represents the model that maximized decorrelation time from a hyperparameter sweep (line 177), but does not clarify whether the sweep included re-running the same configuration with different weight initializations. Without variance estimates, the reader cannot assess whether reported improvements are robust or reflect lucky hyperparameter selection. The box plots in Figure 8 show range across Gaussian width sweeps but not seed variation. At minimum, three seeds per configuration with error bars would be needed for confidence in reproducibility.

3. **Missing direct comparison to PDE-Refiner.** The paper mentions PDE-Refiner (Lippe et al., 2023) as a related projection-based technique that also addresses spectral issues via iterative denoising (line 113), but never includes it in experimental comparison. Since PDE-Refiner explicitly tackles the same problem (poor spectral modeling at high frequencies) and is a well-cited baseline, its omission is significant. The paper's own results are mixed against existing simple tricks (on KS all methods perform similarly), so a comparison to PDE-Refiner would clarify whether spectral shaping fills an actual gap or covers already-served ground.

### Minor

4. **The source of spectral junk is attributed to pointwise nonlinearities alone, but the role of aliasing from convolutions before nonlinearities is not disentangled.** The paper shows all activation functions introduce high-frequency noise (Figure 3b) and that filtering after each nonlinearity helps. However, it does not isolate whether the noise originates from the nonlinearity alone or from the combination of convolution + nonlinearity (convolution can also introduce aliasing). A cleaner ablation — checking whether the same filter placed *before* the nonlinearity (smoothing pre-activations) also works — would strengthen the causal story. This is a gap in the diagnostic analysis, not the method itself.

5. **Aliasing from downsampling in the UNet is not discussed.** The paper does not consider whether strided convolutions or pooling in the UNet encoder compound the spectral junk. If the method is applied only after nonlinearities but not after downsampling operations, it may miss another source of spectral error. A brief acknowledgment or ruling-out would improve completeness.

### Trivial
None.

## Nice-to-Haves

- **Sensitivity analysis for σ**: The paper sweeps Gaussian width σ ∈ [1,10] and shows box plots (Figure 8), but a dedicated plot of performance (MELR or decorrelation time) vs. σ for at least one PDE would help practitioners choose σ and demonstrate robustness.
- **Wall-time comparison**: The paper states "we do not notice any slow down" (line 135) but provides no timing measurements. A table comparing training/inference time per step with and without shaping would be helpful.
- **Explicit limitations statement**: The paper should note that experiments were conducted only on UNet and that transfer to other architectures is not yet verified.
- **Clarify whether filtering before activation would also work**: As noted in Minor weakness 4 above.

## Removed Points

- *Overstatement of "machine precision" claim*: The paper clearly distinguishes one-step (machine precision, Figure 3a) from rollout (diverges, line 201). The claim is accurate in context — removed.
- *Lax-Richtmeyer theorem tangential*: The section motivates why stability and accuracy matter; this is a pedagogical choice, not a weakness.
- *Autoregressive training confusion*: The paper clearly separates the baseline from combinations with other methods (lines 149, 179). No confusion upon reading.
- *MELR invariance concern*: The paper acknowledges this (line 155) and it is a known property of the metric, not a hidden problem.
- *"Cannot be easily learned" wording issue*: Minor phrasing preference; the paper's meaning is clear.
- *Missing related works*: Per instructions, I cannot verify absence of references.

## Novel Insights

The harsh critic noted that the identification of pointwise nonlinearities as the source of spectral junk (Figure 3b) is the paper's strongest diagnostic contribution, and this stands even without the method itself. Separately, the critic correctly observed that the paper's core finding — that filtering after *every* nonlinearity (deep filtering) is necessary, not just at the output — is a non-obvious architectural insight. The ablation in Figure 8 convincingly demonstrates this: post-filtering can achieve low spectral gap but poor decorrelation time, showing the placement of filters inside the network matters for hidden representations. This is a genuinely useful finding that future architecture design should account for.

## Suggestions

1. **Add one more architecture** (FNO is the natural choice — same codebase, different operator layer) to validate generality. This single addition would resolve the most impactful weakness.
2. **Report results with 3 random seeds and error bars** on all main figures (Figures 6, 9 at minimum).
3. **Include PDE-Refiner as a baseline** on at least one PDE (e.g., KS, where PDE-Refiner was originally tested).
4. **Add a sensitivity plot** for σ vs. performance to help practitioners set the hyperparameter.
5. **Disentangle aliasing source** with a pre-activation vs. post-activation filter placement ablation.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Neural Spectral Methods (2DbVeuoa6a) | 6.75 | R1 | Stronger — broader validation, spectral loss theory |
| PDE-constrained Learning (stcN89QGfL) | 5.67 | R1 | Comparable — both have clean contributions but incomplete validation |
| Geometric/Physical Constraints (gz8Rr1iuDK) | 4.00 | R1 | Weaker — only 2 PDEs, single architecture, less clear presentation |
| On expressiveness/spectral bias of KANs (ydlDRUuGm9) | 6.25 | R1 | Stronger — theoretical results with broader impact |
| Physics-enhanced Neural Operator (5LvTfc4fBz) | 5.00 | R1 | Weaker — unclear presentation, short rollouts, missing comparisons |

**Round 1 Bracket:** [5.0, 6.5]

**Round 2 — Narrowing:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Unisolver (f3xXPDCh8Q) | 5.50 | R2 | Comparable — both have strong motivation but incomplete validation |
| TE-FNO (ZtTgoomrT1) | 5.00 | R2 | Weaker — incremental novelty, marginal improvements |
| Active Learning for PDE Solvers (x4ZmQaumRg) | 7.00 | R2 | Stronger — comprehensive benchmark with broad scope |
| MgNO (8OxL034uEr) | 6.50 | R2 | Stronger — solid theory, diverse experiments, clean presentation |

**Final calibration:** The paper is clearly stronger than reject-level papers at 5.0 (PENO, TE-FNO) and comparable to papers at 5.5 (Unisolver). It is weaker than accepted posters at 6.0+ (MgNO 6.5, Neural Spectral Methods 6.75) which have broader validation and stronger completeness. The paper's core diagnostic insight and simple method are genuine contributions, but the incomplete validation (single architecture, no error bars, missing PDE-Refiner) pulls it below the acceptance threshold.

**Final Score:** 5.5 — Marginally below the acceptance threshold. This reflects a solid paper with a clear, well-motivated contribution that needs additional experimental validation (another architecture, statistical rigor) to meet the bar for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>