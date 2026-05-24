## Summary

This paper provides theoretical and empirical analysis of Multi-Grade Deep Learning (MGDL), which trains shallow networks sequentially on residuals of previous grades, compared to standard end-to-end training (SGDL). It presents convergence theorems for GD (assuming smooth activations), a convexity result for single-layer ReLU grades, an eigenvalue analysis of the iteration matrix, and experiments across image regression, denoising/deblurring, CIFAR-10/100 classification, and transformer-based time series.

## Strengths

- **Extensive empirical validation across diverse tasks**: The paper benchmarks MGDL against SGDL on six image regression tasks (Table 1), three images × six noise levels for denoising (Table 2), three blur levels for deblurring (Table 3), CIFAR-100 classification (Figure 3), CIFAR-10 classification (Figure 6), and synthetic/financial time series with transformers (Tables 4–5). MGDL consistently achieves lower loss and higher PSNR across all tasks, with PSNR gains of 0.16–4.23 dB for denoising and MSE reductions by orders of magnitude for time series.

- **Quantified learning-rate robustness**: Section 6 systematically tests learning rates from 0.001 to 0.5 (synthetic) and up to 1.0 (image regression), showing MGDL maintains low loss over a wider range than SGDL. Synthetic results concretely show SGDL converges only for η ∈ [0.03, 0.08] while MGDL works for η ∈ [0.01, 0.3] (Setting 1).

- **Eigenvalue-based stability analysis**: Section 7 monitors eigenvalues of I−ηH during training across synthetic regression, image regression/denoising, and CIFAR-10 (Figures 4–6, 21–29). The paper demonstrates that SGDL's eigenvalues frequently fall below −1 causing oscillatory loss, while MGDL's eigenvalues remain within (−1,1) across grades. This provides a mechanistic explanation grounded in GD dynamics, even if the theoretical framing assumes differentiability.

- **Convex decomposition of single-layer ReLU grades** (Theorem 3): The paper proves that when each MGDL grade is a single-hidden-layer ReLU network, the problem decomposes into a sequence of convex subproblems. While the condition m_l ≥ P_l is impractical for large datasets, the theoretical equivalence is correctly established.

## Weaknesses

### Fatal
None.

### Major

- **Theory–practice gap in convergence analysis**: Theorems 1, 2, and 4 assume the activation function σ is twice continuously differentiable (explicitly stated at lines 128, 162, and 313), but every experiment in the paper uses ReLU (σ(x) = max{0,x}, stated at line 94: "ReLU activation σ(x) = max{0,x} applied componentwise"). ReLU is not even once differentiable at zero, so the convergence guarantees proven in Theorems 1, 2, and 4 do not apply to any of the experimental settings. The paper makes no attempt to extend the theory to non-smooth activations, argue that results hold in a limiting sense, or even acknowledge this gap. This substantially weakens the claim that the paper provides a "rigorous theoretical explanation" for MGDL's advantages. (Note: Theorem 3 explicitly handles ReLU, which partially mitigates but does not resolve the gap for the convergence theorems.)

- **Missing test accuracy for classification tasks**: The CIFAR-100 section (lines 281–283) and CIFAR-10 section (line 347) report only training/validation loss, never test accuracy. The abstract and conclusion repeatedly claim "superior accuracy," but for the two classification benchmarks no accuracy numbers are provided. Loss is not a substitute for accuracy in classification, and this omission undercuts the central empirical claim for these tasks.

### Minor

- **Convexity result has impractical scope and overstated novelty**: Theorem 3 requires m_l ≥ P_l, where P_l is the number of possible activation patterns — exponential in the input dimension and dataset size. For any realistic problem, P_l is astronomically larger than the hundreds of neurons used in experiments, making the convex program intractable. The claim that this "extending[s] convexification from shallow to deep architectures" (line 206) is overstated: the paper applies the Pilanci & Ergen (2020) technique independently to each shallow grade rather than convexifying the deep network as a whole.

- **Model capacity not fully controlled between SGDL and MGDL**: The paper uses different architectures (e.g., SGDL depth 8, width 128 vs. MGDL 4 grades of depth 2) but does not report total parameter counts or explicitly verify that the comparison is capacity-controlled. Without this information, the observed PSNR gains might partly reflect different model sizes rather than the multi-grade training paradigm itself. The consistent improvements across many tasks alleviate this concern but do not eliminate it.

- **No statistical significance reporting**: No multiple seeds, standard deviations, or confidence intervals are reported for any experimental result (Tables 1–5), making it impossible to gauge result variability.

- **The claim α_l ≪ α is asserted without evidence**: Theorem 2's key advantage — that MGDL allows a broader learning-rate range because α_l ≪ α — is simply stated (line 170) with no proof, measurement, or quantitative comparison of Hessian spectral norms between SGDL and MGDL architectures.

### Trivial

- Figure 4 caption labels use mixed terminology (epochs vs. iterations across subfigures).
- The CIFAR-10 section (line 347) contains a doubled number: "learning rate 0.004 0.004."

## Nice-to-Haves

- A comparison to other multi-stage training methods (greedy layer-wise training, boosting) would strengthen the positioning of MGDL; currently the paper only compares to standard end-to-end training.
- Reporting training computation cost (total gradient steps, wall-clock time) for the image experiments (already done for transformers) would help attribute efficiency gains.
- A brief discussion of why the eigenvalue analysis (which numerically computes Hessians for ReLU networks) is empirically meaningful despite the smoothness requirement in the convergence theorems would help bridge the theory-practice gap.

## Removed Points

The following points from the input reviews were removed as invalid:

- **"Eigenvalue analysis uses different learning rates making comparison invalid"**: The paper selects learning rates by lowest validation loss per method (line 319), which is standard practice. The analysis shows that even at each method's own optimal LR, SGDL eigenvalues exit (−1,1) while MGDL's do not — this is a meaningful comparison about each method's operating point.
- **"No comparison to BM3D or classical denoising methods"**: The paper's scope is MGDL vs. SGDL comparison, not benchmarking against all existing denoising methods. This is scope creep.
- **"Missing related works / Edge of Stability discussion"**: Cannot verify missing references, and the paper's scope does not require engaging with every adjacent literature strand.
- **"No analysis of error propagation across grades in eigenvalue analysis"**: The paper analyzes each grade's eigenvalues independently, which is appropriate since each grade is trained on residuals with fixed previous grades.
- **"Transformer training time comparison not properly attributed"**: The paper does report training time (Tables 4–5: MGT 741s vs SGT 2693s for synthetic; 972s vs 1712s for SPX).
- **"Standard deviations not reported"**: While noted as a weakness above, demoting this to Minor rather than Major since single-run evaluation is common in benchmark comparisons for this type of empirical study.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Bridge the theory-practice gap explicitly**: Either restrict the convergence theorems to smooth activations and run at least one experiment with smooth activations (e.g., GELU, SiLU, tanh) to validate the theoretical predictions, or provide a smoothing argument showing the results extend to ReLU in a limiting sense. At minimum, acknowledge the gap and discuss why the empirical eigenvalue analysis (which numerically computes Hessians under ReLU) remains informative despite the smoothness assumptions in the theorems.

2. **Report test accuracy for CIFAR-10 and CIFAR-100**: This is the most easily fixable omission and is essential to substantiate the "superior accuracy" claims for classification.

3. **Report parameter counts and control for capacity**: Provide a table comparing total parameters, MACs, and training steps for SGDL vs. MGDL across all experiment settings to make capacity comparisons transparent.

4. **Provide evidence for α_l ≪ α**: Include a measurement of spectral norms of Hessians for SGDL and MGDL architectures to substantiate the central claim in Theorem 2.

5. **Temper the convexity claim**: Clearly state that Theorem 3 requires m_l ≥ P_l (exponential), note that it follows Pilanci & Ergen (2020), and avoid the misleading phrasing about "extending convexification to deep architectures" since each grade is independently convexified rather than the deep network as a whole.

## Score and Decision

**Calibration anchors** (all retrieved papers considered):

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|------------------------|
| `h7GAgbLSmC.md` | 7.00 | Sharper convergence guarantees with matched smoothness assumptions; much stronger theory-practice alignment than current paper |
| `UvpuGrd6ey.md` | 6.25 | Strong theoretical generalization bounds with empirical support; better integrated theory-experiment flow |
| `GqI4fTVUXC.md` | 6.00 | Well-executed empirical study of theory-practice disconnect; more focused and rigorous methodology |
| `JslyktsKMY.md` | 5.75 | Clear empirical evaluation of optimization theory with careful methodology; less experiment breadth but higher rigor |
| `n2RIkaf1S4.md` | 4.00 | BCD convergence analysis with practical limitations and circular arguments; comparable quality — both have notable flaws alongside contributions |
| `Zap3nZhRIQ.md` | 3.00 | Disconnected superficial analysis of non-differentiability issues; current paper has more coherence and substance |
| `NbbsRnPBoS.md` | 2.33 | Very narrow problem (deep linear networks); current paper has broader scope and more extensive experiments |

The paper sits between the 4.00 and 5.75 anchors. It has broader empirical coverage than `n2RIkaf1S4.md` (4.00) but falls short of `JslyktsKMY.md` (5.75) in methodological rigor due to the theory-practice gap (smoothness assumption mismatch with ReLU experiments) and missing test accuracy for classification tasks. Overclaimed novelty in the convexity result and lack of statistical significance reporting further weaken the contribution relative to the 5.75 anchor. A score of 4.5 reflects a paper with genuine empirical breadth and a plausible mechanistic analysis, but whose theoretical claims are incompletely supported by the evidence presented.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>