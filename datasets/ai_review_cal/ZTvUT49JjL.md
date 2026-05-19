- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 3, 5, 3
Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper proposes a matrix factorization model $X = U D U^\top$ where $U$ is constrained to a Frobenius norm ball and $D$ is a non-negative diagonal matrix, and extends this to a neural network architecture (UDV) with constrained outer layers and a diagonal middle layer. The central idea is that explicit norm constraints on the outer factors, together with the diagonal factor, produce truly low-rank solutions regardless of initialization and step size — overcoming limitations of standard Burer-Monteiro factorization. Experiments on one synthetic matrix completion problem (Figure 1) show that UDU yields singular values decaying to numerical zero across a range of step sizes and initializations, while BM produces only approximately low-rank spectra. On neural network tasks including regression (HPART, NYCTTD) and transfer-learned classification (MNIST), the UDV architecture achieves competitive accuracy while inducing faster singular-value decay that can be exploited for SVD-based pruning.

## Strengths

1. **Truly low-rank solutions from the UDU factorization regardless of initial distance to origin and step size.** Figure 1 provides clear empirical evidence that the proposed UDU model drives singular values to numerical zero across a wide sweep of both $\eta$ (step size) and $\xi$ (initial Frobenius norm), while standard BM factorization yields only approximately low-rank spectra that depend sensitively on these hyperparameters. This directly addresses and improves upon the conditions required in the Gunasekar et al. (2017) conjecture (Remark 2, line 87). The contrast between BM's sensitivity and UDU's robustness in this setting is visually striking and well-supported.

2. **Novel neural architecture (UDV) that achieves competitive accuracy while producing low-rank weight matrices, enabling SVD-based pruning.** Table 2 shows UDV matching or exceeding the validation accuracy/loss of two-layer UV networks with linear or ReLU activations across regression and classification tasks. Figure 3 confirms consistently faster singular-value decay in UDV solutions compared to baselines. The SVD-based pruning demonstration (Figure 4, HPART dataset) shows that compact models derived from the UDV solution can maintain or improve generalization, a practically interesting finding.

3. **Conceptual framing linking implicit bias to divergent (rather than convergent) dynamics.** The paper draws an analogy between the power method's normalization-after-multiplication and the projection step in UDU/UDV (line 25, line 134). While this framing is more narrative than mechanistically established, it provides a fresh conceptual perspective that contrasts with the predominant convergent-dynamics analysis in the implicit bias literature. This perspective motivates the architecture design in a way that is distinct from prior work.

## Weaknesses

### Fatal

None.

### Major

1. **The matrix factorization experiments that form the core evidence for UDU's low-rank bias are conducted on a single problem instance.** The synthetic matrix completion experiment (line 115) uses one matrix size ($100\times 100$), one rank (3), one sampling density (900 out of 10,000 entries), and one distribution (Gaussian factors). While $\eta$ and $\xi$ are varied within this instance, there is no evidence that UDU's "truly low-rank" property holds across different matrix dimensions, ranks, or sampling densities. The paper claims UDU "consistently finds truly low-rank solutions" (line 27) and "obviates the need to rely on these conditions" (line 27), but the scope of the evidence does not match the generality of the claim. This is the paper's central empirical finding, and it needs to be demonstrated across more diverse problem configurations to be convincing.

2. **Critical ablations that isolate the effect of constraints are relegated to supplementary material, not shown in the main paper.** The UDV architecture (3 layers + constraints) is compared against two-layer UV baselines (linear or ReLU). This confounds two factors: extra depth and explicit constraints. Prior work (Arora et al., 2019; Feng et al., 2022) shows that increasing depth strengthens implicit low-rank bias even without constraints. The paper acknowledges this in Section 4.1.3 (point 5, lines 220–222) and claims that the comparison against a three-layer unconstrained network "indicates that the pronounced bias in the UDV framework cannot be attributed solely to depth" — but the actual results are only described in text and deferred to supplementary material. Similarly, the comparison against weight-decay regularization (point 6) and UDV without constraints are only text mentions. Since the paper's core claim about UDV is that its low-rank bias comes from the explicit constraints and diagonal factor (not merely from added depth), this evidence must be presented in the main paper, not just referenced.

### Minor

1. **The divergent-dynamics / power-method motivation is narratively asserted but not mechanistically established.** The paper states that projection onto the norm ball "results in a scaling step similar to the Power Method" (line 25) and that the model "unravels these competing forces" (line 18), but provides no analysis — theoretical or dynamical — that rigorously connects the projection operation to power-method-like amplification of dominant singular components. The qualitative observation that columns of $U$ grow in some directions and shrink in others (line 134) is suggestive but does not constitute a mechanistic explanation. The core technical contribution (constrained factorization + diagonal factor) stands independently of this framing, but the paper over-promises a mechanistic understanding it does not deliver.

2. **The SVD-based pruning demonstration is too preliminary to support strong claims about utility.** It is conducted on one dataset (HPART) only (Figure 4 caption, line 203), with no comparison to standard pruning baselines (e.g., magnitude pruning at comparable sparsity levels), and no error bars or statistical testing. The paper appropriately calls it "an example" (line 200), but the claims in the conclusion about "efficient and lightweight networks" (line 235) outpace the evidence.

3. **The matrix factorization experiments lack statistical reporting.** There are no error bars or confidence intervals across random trials (the paper does not mention multiple trials for the matrix experiments). The singular value spectra are shown without quantifying what "truly low-rank" means (e.g., number of singular values above a threshold). Adding these would strengthen the claims.

4. **The paper mentions four constraint variants of UDV** (Section 4.1.3, point 1, line 212) but does not compare them in the main paper. The selection criterion ("generally produces the most pronounced decay") is stated without supporting evidence in the main text.

### Trivial

None.

## Nice-to-Haves

- Include the critical ablations (3-layer unconstrained, UDV without constraints, weight-decay comparison) as figures in the main paper. This would directly address the most significant weakness.
- Expand the matrix factorization experiments to include varying matrix dimensions (e.g., 50×50, 200×200), ranks, and sampling densities to demonstrate generality.
- Add error bars / confidence intervals for the matrix factorization spectral decay results across random trials.
- Include a standard pruning baseline (e.g., magnitude pruning) and report on additional datasets to strengthen the pruning demonstration.
- Add a quantitative measure of "truly low-rank" (e.g., effective rank, number of singular values above a threshold) alongside the spectral decay plots.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No comparison to explicit nuclear-norm regularization or rank-constrained optimization"** — Removed as scope creep. The paper's contribution is about implicit bias in a specific factorization approach compared to BM factorization, not about surpassing all possible matrix completion methods.
- **"The impact of step-size is examined only with fixed initialization and vice versa (not a full factorial)"** — Removed as overly strict. One-at-a-time parameter sweeps are standard in the literature and the sweeps cover a reasonable range of values.
- **"It is not shown whether BM would ever converge to low rank if allowed more iterations"** — Removed as speculative. Both methods were run for 10^6 iterations; speculating about what would happen with more iterations is not a concrete weakness.
- **Strength: "Ablation studies rule out alternative explanations"** — Weakened (moved from being listed as a strong strength) to reflect that these ablations are in supplementary material, not the main paper. The claim is plausible but cannot be verified from the main text alone.
- **Strength: "Explicitly obviates the three conditions required by prior implicit-bias theory"** — Kept but qualified: this is demonstrated on a single problem configuration; generality remains to be shown.

## Novel Insights

The most interesting observation emerging from the review process is the structural tension in the paper: the UDU matrix factorization results (Figure 1) are genuinely striking and suggest that explicit norm constraints plus a diagonal factor produce a qualitatively different implicit bias than standard BM factorization. However, the neural network extension (UDV) inherits the narrative connection to this finding without providing the same tight control — the confound of depth vs. constraints is not fully resolved in the main paper. This creates an unusual situation where the matrix factorization half of the paper may be the stronger scientific contribution (even though it is described as the "warm-up"), while the neural network half — which the paper emphasizes as the main deliverable — has weaker causal evidence. Future work could benefit from directly testing whether the UDU mechanism (projected gradient on bounded U + diagonal D) provably leads to rank-revealing dynamics, perhaps through a dynamical systems analysis of the projection step's effect on the singular value evolution.

## Suggestions

1. **Move the critical ablations from supplementary into the main paper.** Specifically, show a figure comparing spectral decay for: (a) two-layer unconstrained, (b) three-layer unconstrained, (c) three-layer constrained without diagonal (U only), and (d) full UDV. Without this, the main paper cannot support the claim that constraints (not depth) drive the effect.

2. **Add at least 2–3 additional matrix problem configurations** (different sizes, ranks, sampling rates) to Figure 1 to support the generality claim. Report the effective rank or the number of singular values above a threshold quantitatively.

3. **Add error bars to Figure 1 and Figure 3** from multiple random trials (at least 5 seeds) to demonstrate statistical robustness.

4. **Either strengthen the pruning evaluation** with baselines and multiple datasets, or explicitly position it as an illustrative example rather than a validation of the architecture's utility.
