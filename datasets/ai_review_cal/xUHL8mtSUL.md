- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 5, 3, 5
Now I have sufficient information. Let me compose the final consolidated review.

---

## Summary

This paper proposes a scalable Gaussian process regression method based on the Hilbert-Schmidt Singular Value Decomposition (HS-SVD). The key idea is to leverage the known Mercer decomposition of a kernel — specifically a compact Matérn kernel on a bounded domain — to obtain a low-rank basis that is computed once and reused during MLE optimization, because the eigenfunctions are independent of the kernel parameters. This yields O(nm²) time and O(nm) space complexity, with no per-iteration decomposition cost. The method is evaluated on simulated data against nine state-of-the-art GP approximations and shown to be competitive or superior in MSE, runtime, and memory.

## Strengths

- **Parameter-independent eigenfunctions eliminate per-iteration decomposition cost.** Section 3.3 explicitly states that for the compact Matérn kernel, only the eigenvalues λⱼ(θ) depend on parameters θ, while the eigenfunctions φⱼ(x) do not. This means the n×m matrix Φₘ is computed once and reused during MLE optimization (line 189). This is the core algorithmic novelty — prior low-rank methods typically require recomputing or updating the decomposition at each optimization step, whereas HS-SVD sidesteps this entirely.

- **Principled theoretical connection between the compact Matérn and standard Matérn kernels.** Proposition 3.5 proves that both kernels are Green's functions of the same modified Helmholtz operator (−Δ + α²I)ᵝ, differing only in domain boundary conditions (ℝʳ vs. [0,1]ʳ with zero boundary). This grounds the method in well-understood GP theory and justifies comparisons against standard Matérn-based methods with matched smoothness.

- **Provable smoothness of the compact Matérn kernel.** Theorem 3.3 states the kernel is β−r−1 times differentiable, giving practitioners principled control over the regularity of the GP. This matches the smoothness control of the standard Matérn family.

- **O(nm) memory footprint without GPU dependence.** The algorithm in Section 3.4 stores only the n×m matrix Φ and a few m×m matrices, avoiding O(n²) storage of the full kernel matrix. The method is designed to run on a single CPU, making it accessible to users without GPU hardware — a concrete practical advantage over DKL, SVGP variants, and others listed in Section 1.

- **Comprehensive benchmarking against nine methods with matched smoothness.** Section 4 compares HS-SVD against NNGP, SVGP, SVGP-CIQ, VNN, NGD, DKL, SGPR, SKI, and LOVE, with explicit smoothness matching (β=3 in 1-D, ν=3/2 for Matérn-based competitors). The scope of this comparison is a genuine strength.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Overstated simplicity claims.** The abstract and introduction state "only one easy-to-tune parameter, m, an integer" and "requires no preprocessing." In practice, the kernel has parameters (ρ, α, β) plus a nugget σ² that must be estimated by MLE (lines 118, 167). While m is the main tuning parameter for the low-rank approximation and the kernel parameters are estimated rather than tuned by hand, the phrasing "only one easy-to-tune parameter" is misleading. Additionally, data must be scaled to the [0,1]ʳ domain (or any bounded region), which is a form of preprocessing, albeit trivial. These overstatements do not undermine the core contribution but should be corrected.

- **Missing experimental details that hinder reproducibility.** The experimental section (Section 4) does not report: (a) the GPU model(s) used, (b) the optimizer or convergence criteria for MLE, (c) the number of inducing points for SVGP, (d) the SKI grid size, (e) the number of Lanczos iterations for LOVE, or (f) batch sizes for GPU methods. These are standard details needed to interpret runtime and memory comparisons. The paper also makes a vague statement that "RAM usages should be judged in a relative manner" (line 236), which weakens the rigor of the memory analysis.

- **Evaluation limited to simulated data.** All experiments use simulated data (Section 4). The paper motivates GPR for domains like forestry, geospatial applications, climate science, and single-cell RNA sequencing (line 12), but provides no real-data demonstration. While simulated data are standard for controlled benchmarking, the absence of at least one realistic dataset limits the strength of the claimed practical utility. This is a gap, not a fatal flaw.

- **Boundary effects of the sine-basis compact Matérn not discussed.** The compact Matérn kernel uses sine eigenfunctions √2 sin(lπx) on [0,1] with zero boundary conditions (Definition 3.1, line 116; line 158). This means the kernel enforces zero at the domain boundaries, which could bias predictions near edges. The paper does not discuss this effect or suggest mitigations (e.g., extending the domain). While likely minor in practice for large n, the omission should be addressed.

- **No analysis of truncation error vs. m.** The method relies on truncating the Mercer series at m terms, but the paper provides neither theoretical bounds nor an empirical study of how MSE varies with m for different data sizes. Such an analysis would give practitioners actionable guidance on choosing m. Section 4 applies a fixed β and the paper does not ablate m.

### Trivial

- The algorithm pseudocode in Section 3.4 is partially garbled (likely a formatting artifact from the parser), but the surrounding prose description is clear enough to follow.

- The RAM usage discussion (line 236) is accompanied by a hedging caveat ("RAM usages should be judged in a relative manner") that, while honest about the difficulty of measuring memory, undersells the paper's genuine O(nm) memory advantage. A more confident statement would be appropriate.

## Nice-to-Haves

- **Provide a controlled efficiency comparison on identical hardware** (e.g., both HS-SVD and a representative competitor on the same CPU, or both on the same GPU) to isolate algorithmic speed from hardware differences. This would strengthen the claim of efficiency without introducing confounds.

- **Include a real-data application** from one of the motivating domains (e.g., a spatial temperature dataset or a forestry biomass dataset) to demonstrate practical utility.

- **Add an ablation study on m** showing the trade-off between MSE, runtime, and memory across several values of m and data sizes. This is the paper's key tuning parameter and practitioners need this guidance.

- **Provide an empirical or theoretical bound on the truncation error** of the Mercer series approximation.

## Removed Points

*These points were flagged by reviewers but are removed with justification:*

1. **"Unfair CPU vs. GPU comparison invalidates the efficiency claim."** — REMOVED per hard rules. The rule states to remove "weaknesses about unfair comparison with other methods if the asymmetry favors the baseline and not the author's method." Here, the baselines (SKI, LOVE) use GPU (advantage), while HS-SVD uses a single CPU core. The paper's claim is about practical efficiency without requiring GPU hardware. Showing that a CPU method outperforms GPU methods on the dimension being tested *strengthens* the practical claim; this is not a flaw. The valid sub-points about missing experimental details (GPU model, hyperparameters) are retained in Minor weaknesses above.

2. **"The paper does not clearly position itself relative to structured kernel interpolation or Nyström methods."** — REMOVED per the rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."

3. **"If the domain is any other bounded region, the eigenfunctions are not simple sinusoids."** — This misunderstands the paper. The paper explicitly states (line 160) that "[0,1] is used for simplicity of presentation, and the domain can be replaced with any closed interval or bounded region without loss of generality" — this is achieved by scaling the data to the unit hypercube, preserving the sine basis. The criticism is factually incorrect about the method's scope.

4. **"The implementation language difference (R vs Python) introduces confounding."** — The asymmetry favors the baselines (Python/GPyTorch is generally faster than R for numerical computing). Per the same hard rule as point 1, this is removed. If anything, this makes the CPU-vs-GPU result more conservative.

5. **Various formatting/style nitpicks and speculation about missing appendix content** — Removed per rules.

## Novel Insights

The synthesis of the two reviews reveals an interesting tension: the paper's core algorithmic contribution (parameter-independent eigenfunctions eliminating per-iteration decomposition cost) is genuinely novel and well-supported, yet the paper packages it with slightly inflated claims about simplicity and zero preprocessing. The experimental comparison is simultaneously the paper's strongest asset (9 methods, matched smoothness, orders-of-magnitude speedup) and its weakest link (hardware confounds acknowledged but not addressed via same-hardware control). The most actionable path forward would be to: (i) add one same-hardware experiment (HS-SVD vs. one competitor on CPU) to satisfy the pure-algorithmic-efficiency question, while keeping the CPU-vs-GPU comparison as a valid practical demonstration; (ii) tighten the language about tuning/preprocessing; and (iii) include one real-data benchmark. Doing so would make a strong paper stronger without changing the method itself.

## Suggestions

1. Correct the overstated simplicity claims in the abstract and introduction. Replace "only one easy-to-tune parameter" with something like "only one tuning parameter m for the low-rank approximation (alongside kernel hyperparameters estimated by MLE)" and "requires no preprocessing" with "requires only trivial rescaling to a bounded domain."
2. Report the missing experimental details (GPU model, optimizer, convergence criteria, hyperparameters of competitor methods) in a table or appendix.
3. Add a supplementary experiment on a real spatial dataset (e.g., from climate or forestry) to demonstrate practical applicability.
4. Add an ablation plot showing MSE and runtime as a function of m for a few n values.
5. Briefly discuss boundary effects of the sine basis and either argue they are negligible for large n in interior regions or propose a simple fix (e.g., domain padding).
