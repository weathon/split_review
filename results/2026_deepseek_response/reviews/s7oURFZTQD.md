Now let me finalize my analysis. I've gathered strong calibration data. Let me write the final review.

**Round 1 Bracket:** Based on the wide bracketing, the paper clearly falls between the low band (~3.0 for papers with fundamental flaws) and the high band (~8.0 for polished papers). The plausible range is between 4.0 and 6.0.

**Round 2 Narrowing:** Comparing against anchors in this range — the 5.75 (Reject) multiscale CNN paper has a similar theory-practice profile, the 5.50 (Reject) non-linear feature learning paper has cleaner theory but limited scope, and the 6.00 (Accept) regression paper is clearly tighter methodologically. The paper under review is weaker than the 6.0 accept anchor but stronger than the 4.0-4.5 anchors with serious proof errors or trivial contributions.

**Final Score Assessment:** The paper is in the 4.5–5.5 range. I'll place it at **5.0** with a **Reject** decision — it has interesting ideas and broad experiments, but the structural gaps (theory-practice mismatch in smoothness/optimizer, lack of capacity controls, no error bars, restrictive convexity result) are too significant to accept.

---

## Summary

This paper proposes Multi-Grade Deep Learning (MGDL), which decomposes end-to-end neural network training into a sequence of shallow networks trained on residuals. The paper provides convergence theorems for gradient descent on MGDL (Theorems 1–2), a convexity result for single-layer ReLU grades (Theorem 3), an eigenvalue analysis showing MGDL's iteration matrix stays within \((-1,1)\) (Section 7), and experiments on image regression, denoising, deblurring, CIFAR-100, and time-series transformers showing MGDL outperforms standard end-to-end (SGDL) training.

## Strengths

1. **Convex subproblem decomposition for single-layer ReLU grades (Theorem 3, Section 4).** The paper proves that when each MGDL grade is a single hidden-layer ReLU network, the overall nonconvex optimization reduces to a sequence of convex programs, explicitly extending Pilanci & Ergen (2020)'s shallow convexification to deep architectures via the MGDL decomposition. This gives a formal theoretical connection not present in prior MGDL work.

2. **Eigenvalue analysis provides a mechanistic explanation for MGDL's stability (Section 7, Theorem 4, Figures 4–6).** By tracking eigenvalues of \(I - \eta H\) during training, the paper shows empirically that MGDL's eigenvalues remain within \((-1,1)\) while SGDL's frequently drop below \(-1\), correlating with loss oscillations. This offers a concrete, testable explanation for the observed convergence differences that goes beyond post-hoc reasoning.

3. **Consistent empirical gains across diverse tasks and architectures (Tables 1–5).** MGDL outperforms SGDL on image regression/denoising/deblurring (PSNR gains of 0.42–3.94 dB), achieves ~100× lower training loss on CIFAR-100 (Figure 3), and on time-series transformers reduces test MSE by an order of magnitude while using 28–33% of the training time (Tables 4–5). The breadth across FC, CNN, and Transformer architectures demonstrates scalability beyond prior MGDL studies.

4. **Robustness to learning rate over a wider interval (Section 6, Figure 2).** On synthetic regression, MGDL maintains stable training for a learning-rate range roughly 3–6× larger than SGDL (e.g., \([0.01, 0.3]\) vs. \([0.03, 0.08]\) in Setting 1), directly supporting the claim that MGDL is more forgiving to hyperparameter choices, and this experiment uses GD (consistent with the theory).

5. **Convergence theorems formalize the intuition that shallow subproblems are easier to optimize (Theorems 1–2).** The analysis bounds the per-grade Hessian spectral norm \(\alpha_l\) and argues \(\alpha_l \ll \alpha\), implying a larger admissible learning-rate interval \((0, 2/\alpha_l)\) for MGDL. This formalizes a natural intuition into a concrete mathematical statement.

## Weaknesses

### Fatal
None.

### Major

1. **Smoothness assumptions of convergence theorems are violated by the experimental setup.** Theorems 1 and 2 explicitly require the activation function \(\sigma\) to be *twice continuously differentiable*. ReLU is not differentiable at zero. Every experiment in the paper uses ReLU. The paper offers no justification (e.g., smooth approximation, subgradient extension, or a remark that the analysis should be interpreted heuristically). While it is common in ML theory to prove results under smoothness and apply to ReLU as a heuristic, the paper does not acknowledge this gap, and the abstract's promise of "rigorous theoretical guarantees" is overstated. The paper could address this by testing with smooth activations (tanh, SiLU) or explicitly scoping the theoretical claims.

2. **Optimizer inconsistency between theory and main experiments.** The convergence theorems (Theorems 1–2) and eigenvalue analysis (Section 7) are derived for plain gradient descent. The main benchmarks on image regression, denoising, deblurring, and CIFAR-100 (Section 5) use the Adam optimizer. Adam modifies gradient magnitudes and directions per-parameter, so the Hessian-based eigenvalue analysis does not directly transfer to Adam dynamics. The paper never reconciles this discrepancy, making it unclear whether the theoretical explanations (based on GD) actually explain the experimental results (obtained with Adam). The learning-rate robustness experiments (Section 6) do use GD, but these are on synthetic data and one small image task—not the main benchmarks.

3. **Experimental comparisons lack controls for model capacity.** The paper compares MGDL against SGDL without reporting parameter counts or FLOPs. For image regression, SGDL uses an 8-hidden-layer network while MGDL uses 4 grades with 2 hidden layers each. Total depth (8 hidden layers) is matched, but the parameter sharing and connectivity differ fundamentally. Without parameter counts or FLOPs, it is unclear whether MGDL's gains come from its training scheme or simply from having more capacity (since grades are trained independently). Additionally, there are no comparisons to other multi-stage methods (e.g., ResNet trained end-to-end, progressive networks, boosting on neural features), making it hard to attribute the advantage specifically to MGDL.

4. **No error bars or repeated runs.** All numerical results (Tables 1–5) are single numbers without standard deviations or confidence intervals. Given training stochasticity, small claimed improvements — such as the 0.16 dB PSNR gain on Chest denoising at noise level 60 (Table 2) — could be within run-to-run noise. Without error bars, the reliability of the results cannot be assessed.

### Minor

1. **Convexity result is severely restricted and the limitations are not acknowledged.** Theorem 3 requires \(m_l \geq P_l\), where \(P_l\) is the number of possible activation patterns — typically exponential in the input dimension (Cover, 2006). This makes the condition essentially impossible to satisfy in practice. Moreover, the theorem only applies when every grade is a *single hidden-layer* ReLU network, but all experiments use deeper grades. The abstract's claim that MGDL "reduces a highly nonconvex problem to a sequence of convex subproblems" omits these qualifications, making it misleading as stated.

2. **Eigenvalue analysis is validated only on small networks.** The eigenvalue plots (Figures 4–6, etc.) use networks much smaller than the main experiments (e.g., width 48 or 128 fully-connected nets, not CNNs). The paper notes that "shallow networks are used to enable Hessian computation" but does not attempt approximations (e.g., Lanczos, NTK) to bridge the scale gap. It is unclear whether the eigenvalue behavior generalizes to the practical-scale models where performance claims are made.

3. **CIFAR-100 learning-rate discrepancy.** Section 5 states that two learning rates of \(5 \times 10^{-4}\) and \(1 \times 10^{-4}\) are tested. However, the Figure 3 caption says "MGDL(1-2: \(\eta = 5 \times 10^{-5}\), 3-4: \(\eta = 1 \times 10^{-4}\))" — the values \(5 \times 10^{-4}\) and \(5 \times 10^{-5}\) differ by an order of magnitude, and the figure caption describes a two-learning-rate scheduling scheme per grade, which is not mentioned in the main text.

4. **The eigenvalue linearization heuristic lacks rigorous justification.** Section 7 linearizes the GD update by dropping the Taylor remainder (order \(\|W^k - W^{k-1}\|^2\)). Theorem 4 only proves convergence of the linearized iterates, and connecting it to the true iterates requires third differentiability (also violated by ReLU). The analysis is instructive but the paper presents it as "analysis" rather than "heuristic explanation."

### Trivial

1. The financial data source is cited imprecisely as "Yahoo Finance or Bloomberg" without specifying which was actually used or providing ticker/date-range identifiers beyond the stated range.

## Nice-to-Haves

- Include parameter counts and FLOPs for all experiments to enable capacity-controlled comparisons.
- Add results with SGD (consistent with theory) as a complement to Adam experiments.
- Use Lanczos or other approximations to validate eigenvalue analysis on at least one realistic-scale model.
- Compare against standard baselines (e.g., ResNet for CIFAR-100, BM3D for denoising) to contextualize absolute performance.
- Report results over multiple random seeds with error bars.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing architectures 26–29 and appendix content.** Removed per hard rules — the parser strips appendix sections; these equations exist in the original submission.
- **Missing comparison to BM3D/non-local means for denoising.** Removed — the paper's scope is MGDL vs. SGDL, not achieving SOTA. A baseline for context would be nice but is not required.
- **Missing related work comparisons.** Removed per hard rules — cannot verify missing related works.
- **"Not yet released" or reproducibility concerns about code.** Removed per hard rules — the paper cites anonymous code; questioning its existence is not permitted.
- **Criticism that the eigenvalue analysis is "purely heuristic" with "no quantitative measure."** Weakened and demoted — the paper does show eigenvalue plots alongside loss curves, providing qualitative correlation. The real concern is about scale, which is already captured as a Minor weakness.
- **Criticism that the CIFAR-100 MSE loss is non-standard for classification.** Removed — MSE is a valid loss for classification and the comparison is between SGDL and MGDL using the same loss; this is a design choice, not a flaw.
- **Criticism that Section 8 transformer architecture doesn't specify block counts.** Removed — the paper states each grade uses a single-block transformer and references Appendix C; the appendix content was stripped by the parser.
- **Criticism from the Strength Finder claiming the paper "compares only to SGDL without other baselines."** This is already captured in Major weakness #3; duplicative.
- **Generic strengths about "addressing an important problem" from Strength Finder.** Removed — these are superficial and not specific to this paper.
- **Strength about "rigorous theoretical guarantees."** Removed — conflicts with verified weaknesses about the smoothness assumption mismatch.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Explicitly acknowledge the smoothness gap in Theorems 1–2 and either (a) add experiments with smooth activations (tanh, SiLU) that satisfy the assumptions, or (b) clearly state that the theorems require smooth activations and the ReLU experiments are heuristic extensions.
2. Report parameter counts for every experiment and ensure MGDL/SGDL comparisons are capacity-matched, or explain any unavoidable discrepancies transparently.
3. Add results from multiple random seeds with standard deviations.
4. Resolve the CIFAR-100 learning-rate discrepancy between text and figure caption.
5. Either use GD for the main experiments (to align with theory) or explain why the eigenvalue analysis still applies under Adam dynamics.
6. Qualify the convexity claim in the abstract to reflect the single-layer, exponential-neuron restriction.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**