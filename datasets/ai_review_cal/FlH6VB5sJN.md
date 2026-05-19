- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 5, 6, 3, 6
Now I've carefully verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes a Parallel Multi-compartment Spiking Neuron (PMSN) model that extends biological multi-compartment neuron dynamics to an arbitrary number of compartments for deep SNNs. The key contributions are: (1) a generalized multi-compartment formulation derived from cable models, (2) a parallel implementation that decouples temporal dependencies—enabling GPU-parallelized training while preserving a reset mechanism ignored by prior parallel SNN work, and (3) strong empirical results on long-term sequential benchmarks (S-MNIST, PS-MNIST, SHD, Sequential CIFAR-10/100), showing consistent accuracy improvements over single-compartment and two-compartment baselines.

---

## Strengths

1. **First scalable parallel multi-compartment spiking neuron with reset.** The paper develops a clean mathematical derivation (Section 4.1–4.2) that generalizes two-compartment models to *n* compartments using a tridiagonal coupling matrix, then achieves parallel training via eigenvalue decomposition for the hidden compartments (Eqs. 7–12) and a cumulative floor-division reset for the output compartment (Eqs. 13–15). Unlike prior parallel spiking neuron models (Fang et al., 2023) that bypass reset entirely, PMSN retains a reset mechanism shown to improve accuracy (Table 2 ablation: e.g., ~0.7% gain on S-CIFAR10 column).

2. **Substantial measured speed-ups via parallelization.** Section 5.3 reports 5.4–217× (forward) and 6.2–302× (backward) speed-ups over a serial implementation with identical dynamics, with larger gains on longer sequences. This directly validates the parallelization claim.

3. **Consistent accuracy improvements across multiple benchmarks.** PMSN achieves the highest reported accuracy on S-MNIST (99.6%), PS-MNIST (97.8%), and SHD (96.1%) with fewer or comparable parameters relative to multi-compartment baselines, and at least 2% improvement over all baselines on Sequential CIFAR-10 and CIFAR-100 (Table 2). The model consistently outperforms both single-compartment parallel models (PSN, SPSN) and prior multi-compartment models (DEXAT, TC-LIF).

4. **Qualitative evidence of multi-scale dynamics is compelling.** Figure 3 visualizes damped oscillations with distinct frequencies and decay rates across compartments, providing a clear mechanistic explanation for multi-scale temporal modeling. The distribution of oscillation frequencies and damping coefficients across the neuron population further supports this claim.

5. **Gradient analysis provides theoretical grounding.** Section 4.3 derives the gradient flow (Eq. 16) showing that temporal gradients propagate through multiple decay rates (λ_i = diag(λ₁,…,λ_{n-1})) from the hidden compartments, avoiding the vanishing gradient problem of single-compartment LIF with its single decay rate and recurrent reset.

---

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablation of the parallel simplifications for the output compartment.** The parallel implementation requires setting α=1 (no leak) and clamping I_h to non-negative values before aggregation (Eqs. 13–15, line 141). These alter the output compartment's dynamics relative to the general multi-compartment formulation in Section 4.1. The paper compares the parallel version against a serial version with *identical* (i.e., same simplified) dynamics (line 207), so it never isolates the accuracy cost of these simplifications. Without an ablation study comparing the parallel version to a version using full output-compartment dynamics (with leak and no input clamping) trained with standard BPTT on at least a small-scale task, readers cannot determine how much of the reported performance reflects the multi-compartment structure itself versus the parallelization-specific constraints. This is the most significant gap in the evaluation.

### Minor

1. **No statistical characterization of main accuracy results.** The paper reports point accuracies in Tables 1 and 2 without confidence intervals, standard deviations across multiple runs, or significance tests. Given that SNN training is noisy and margins on some tasks are modest (e.g., PMSN 96.1% vs. TC-LIF 95.5% on SHD), readers cannot assess whether the improvements are reliable. While Figure 2 shows learning curves from three runs, these only visualize convergence speed, not final accuracy variance.

2. **Acceleration comparison is internally valid but lacks practical context.** The speed-up ratios against the serial version of the same model (Section 5.3) correctly demonstrate that the parallelization technique works. However, the paper does not report wall-clock training times against competing parallel-capable models (e.g., PSN, SPSN, standard LIF with BPTT) on the same hardware. The energy-accuracy analysis in Section 5.4 compares against these models but omits runtime, making it impossible to assess whether PMSN is *practically faster* than existing parallel SNN models in addition to being more accurate.

3. **Gradient analysis does not explicitly address the parallel-specific simplifications.** Section 4.3 derives gradient flow through the hidden compartments (Eq. 16), correctly showing multi-scale temporal credit assignment via T̄ = diag(λ₁,…,λ_{n-1}). However, for the output compartment in the parallel version, gradients also flow through the floor operation (⌊·⌋_θ) and non-negative clamping, which are not analyzed in the derivation. The analysis is valid for the hidden compartments (where the main temporal gradient path lies), but the output compartment's gradient landscape may introduce new pathologies not discussed.

4. **SHD dataset handling unspecified.** The paper states SHD has "250 time steps" but the original dataset has variable-length sequences (max 250). The paper does not specify how padding or truncation was handled, which could affect the comparison.

5. **The PSN model is omitted from the accuracy-energy trade-off figure.** Section 5.4 notes PSN has a "considerably high cost of 5541 nJ" and is omitted from Figure 5(b). Including it as a data point (even as an outlier) would give readers a complete picture of the trade-off landscape.

### Trivial

1. No discussion of numerical stability of the Fourier-transform-based convolution (Eq. 12) for very long sequences or small floating-point values.
2. The discrete-time parameters (Λ, Φ_c, Φ_s) derived from compartment-level parameters (τ_i, β_{i,j}, γ_i) are learnable, but the paper does not specify how the underlying biophysical parameters are initialized or whether they are regularized.

---

## Nice-to-Haves

- Report wall-clock runtime against standard LIF with BPTT and against PSN/SPSN on common hardware to substantiate practical speed claims.
- Include the marginal accuracy gains on SHD with confidence intervals to clarify whether the improvement over TC-LIF is statistically robust.
- Compare the parallel PMSN against a version trained with the full output-compartment dynamics (no α=1 restriction, no I_h clamping) on a small-scale task to ablate the cost of the parallel simplifications.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Acceleration comparison is against a strawman serial baseline" (as originally framed).** The harsh critic characterized the comparison as a strawman. However, comparing against a serial version with identical dynamics is a *valid* way to demonstrate the parallelization works. The paper's core claim about acceleration is that the *parallel implementation* speeds up the multi-compartment model, which this comparison directly validates. The demand for wall-clock comparisons against other parallel models is scope-creeping and has been moved to Minor weakness #2 and Nice-to-Haves.
- **"The paper claims 'the first' parallel multi-compartment spiking neuron... this is a minor contribution."** This is not a substantive weakness; whether a claim about "first" is minor or important is a judgment, not a flaw in the paper.
- **"The reset mechanism bears closer resemblance with biological neurons... no citation or justification."** The paper provides this as an *interpretation*, not a core claim. The relevant empirical claim (that reset improves accuracy) is supported by the ablation in Table 2.
- **Strength Finder's generic framing of "important problem" etc.** The strengths section only retains concrete, evidence-backed claims, not generic praise.

---

## Novel Insights

The most interesting cross-cutting observation from these reviews is that the gradient analysis (Section 4.3) and the parallel implementation (Section 4.2) operate on different versions of the output compartment dynamics. The gradient analysis in Eq. 16 effectively treats v_s[t] as having the standard reset-by-subtraction dynamics (α v_s[t-1] + I_h[t] - θ S[t-1]), which is the *serial* formulation, while the parallel implementation replaces this with a cumulative sum + floor-division operation under α=1 and non-negative clamping. The paper does not reconcile these two views: the formal gradient derivation does not verify whether gradient flow through the parallel floor-operation formulation behaves equivalently. This gap is not fatal—the temporal credit assignment primarily flows through the hidden compartments (the "Temporal" term in Eq. 16, which is unaffected by the output compartment simplifications)—but it means the claimed "analysis on the gradient flow" (Section 4.3 title) is a partial analysis that leaves the parallel-specific operations unexamined.

---

## Suggestions

1. **Add an ablation study** comparing the parallel PMSN (with α=1, non-negative clamping) to the serial version with full output-compartment dynamics on a small task like S-MNIST or SHD. If the accuracy is identical, the concern is resolved. If there is a gap, quantify and discuss it.

2. **Report means and standard deviations** over at least 5 runs for the main accuracy results, particularly for tasks with smaller margins (SHD, S-MNIST).

3. **Include wall-clock runtime comparisons** against LIF-BPTT and PSN/SPSN on the same GPU to contextualize the speed-up ratios.

4. **Clarify the gradient flow through the floor operation** in Section 4.3, even briefly, to connect the theoretical analysis to the actual parallel implementation.

5. **Specify SHD preprocessing** (padding, truncation, or variable-length handling) for reproducibility.

6. **Add PSN to Figure 5(b)** even as a point far off the curve for completeness.

---
