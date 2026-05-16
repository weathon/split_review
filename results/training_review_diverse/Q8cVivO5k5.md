Now I have a thorough understanding of the paper and all the claims. Let me produce the consolidated review.

## Summary

This paper proposes LBN-MOBO, a Bayesian optimization framework for multi-objective engineering design problems where very large batch sizes (thousands of samples) can be evaluated in parallel but iterations are expensive. The key innovation is a 2MD acquisition function that performs non-dominated sorting over both performance objectives and their epistemic uncertainties, enabling exploration of under-represented regions alongside exploitation of high-performance areas. The method is paired with Bayesian neural network surrogates (Deep Ensembles recommended) and evaluated on two real-world problems — airfoil CFD design and 3D printer color gamut optimization — with batch sizes up to 20,000.

## Strengths

1. **Novel 2MD acquisition function treating epistemic uncertainty as an additional objective** (Section 4.2, Eq. 2): Rather than the standard \(M\)-dimensional Pareto front over performance objectives, the acquisition function constructs a \(2M\)-dimensional front that jointly maximizes predicted objectives and their epistemic uncertainties. This is a clean, practical design that enables exploration without a separate exploration-exploitation trade-off parameter. The ablation study (Section 5.4, Figure 5) directly confirms that including uncertainty produces more diverse candidate distributions and broader Pareto fronts.

2. **Demonstrated scalability to extremely large batch sizes (15,000–20,000)**: Section 5.3 shows LBN-MOBO handling batch sizes that are orders of magnitude larger than what existing acquisition functions can manage. Section 3 demonstrates that qEHVI fails at batch size >10, qNEHVI and qParEGO become computationally prohibitive beyond 200–500 (Figure 1), and the 44-hour GPU time budget is exhausted. This contrast substantiates the paper's central motivation that existing methods fundamentally cannot operate in the target regime.

3. **Iteration efficiency on real-world problems**: Both real-world experiments converge to high-quality Pareto fronts within 10 iterations (Figure 4). Given that each iteration in the printer problem corresponds to a lab visit and in the airfoil problem to a batch of CFD simulations, this directly addresses the stated goal of minimizing iterations when NFP evaluations are expensive.

4. **Systematic benchmarking of neural surrogates under large-batch conditions** (Section 5.1, Figure 2): The paper evaluates six surrogate families (Deep Ensembles, MC Dropout, HMC, SGHMC, IBNN, DKL) paired with the proposed acquisition function, identifying Deep Ensembles as the best trade-off between performance and runtime for batch sizes up to 1,000. This provides practical guidance for practitioners and is a useful contribution in its own right.

5. **Ablation study confirming the mechanism** (Section 5.4, Figure 5): The ablation on both real-world problems clearly shows that removing epistemic uncertainty from the acquisition causes candidate clustering and reduced coverage, while including it promotes exploration. This provides direct empirical support for the core design rationale.

6. **Proof-of-concept extension to noisy settings** (Section 5.5): The noise-robust variant demonstrates on a toy and a simplified printer problem that aleatoric uncertainty can be incorporated to avoid noisy regions when the surrogate captures it reliably. This is preliminary but points in a useful direction.

## Weaknesses

### Fatal

None.

### Major

1. **No baseline comparisons on the real-world problems.** Section 5.3 compares only two variants of LBN-MOBO (Deep Ensembles vs. MC Dropout) against each other. No external baseline — not random search, not an evolutionary algorithm (e.g., NSGA-II run directly on the NFP), not a simplified BO variant with a comparable surrogate — is evaluated on the airfoil or printer problems. The paper claims superiority in the abstract ("demonstrate the superiority of our method by comparing it with state-of-the-art multi-objective optimizations") and in Section 5.3 ("There we also establish the superiority of our method over a few other algorithms"), but these claims are not supported by any experiment in that section. Section 3 does show that existing acquisition functions (qEHVI, qNEHVI, qParEGO) cannot scale to the relevant batch sizes on a synthetic problem, which is indirect evidence. But the key question — "given the same total NFP budget, does LBN-MOBO find better Pareto fronts than a reasonable alternative that can also handle large batches?" — is not answered for the real-world problems. This is the most consequential weakness because it underdetermines whether the method's complexity is justified.

2. **Acquisition function scalability not quantitatively analyzed.** Section 4.2 notes that NSGA-II struggles with large populations and proposes running independent NSGA-II seeds with smaller batch sizes and combining results. But the paper provides no details on: the number of seeds used, how results are combined into the requested batch size \(S\), whether this introduces selection bias, or how long the acquisition computation takes relative to surrogate training. Figure 2 reports total optimization time but does not break out acquisition time. The claim that "the sole limiting factor for executing LBN-MOBO is our parallel processing or experimentation capability when querying the NFP" (line 240) is therefore unsubstantiated. This matters because if the acquisition itself becomes a bottleneck at batch sizes of 20,000, the practical advantage over simpler methods diminishes.

### Minor

3. **Noise-robust variant validated only on simplified problems.** The noise experiments (Section 5.5) use a 1D toy problem and a printer problem where 6 of 8 design variables are fixed. The paper acknowledges this limitation (lines 386–387: "Reliable computing... of aleatoric and epistemic uncertainties for complex problems... lies outside the scope of this work"), but this means the noise-robust contribution is not tested in a realistic high-dimensional setting, which limits its practical value.

4. **Missing reproducibility details for Deep Ensembles.** The paper does not specify the ensemble size \(K\), the number of layers and width of each network, training hyperparameters (learning rate, epochs, optimizer), or how the initial random samples are drawn. These details are needed for reproducibility. (If these are in the appendix, that addresses the concern, but the main text should at least reference them.)

5. **Single-run results without variance reporting.** No experiment reports variance across multiple runs. Given stochasticity in DE training, NSGA-II, and random initialization, single-run results make it difficult to assess the significance of observed differences. This is somewhat mitigated by the fact that the real-world experiments are expensive, but the ZDT3 benchmarks (Section 3 and 5.1) could feasibly be repeated.

### Trivial

6. The schematic inset figure (20mm width) is too small to be interpretable (line 243). The text description is sufficient, so this does not affect evaluation.

## Nice-to-Haves

- A comparison on the real-world problems against a simple baseline such as random search or NSGA-II applied directly to the NFP for the same total budget would substantially strengthen the paper's claims.
- A wall-clock time breakdown of acquisition vs. surrogate training vs. NFP evaluation for a representative large-batch iteration would substantiate the scalability argument.
- Hypervolume improvement over random initialization (percentage gain) would make the real-world results more interpretable to readers unfamiliar with the specific domains.
- Guidance for setting \(\alpha\) and \(\beta\) in the noise-robust variant (or a default tuning-free scheme) would increase practical utility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The 44-hour GPU time cap is arbitrary"* — This is a standard experimental design choice for bounded-comparison studies; not a valid weakness.
- *"Section 3 does not show whether these methods would converge given more compute"* — Speculative; the paper shows they fail within reasonable resource bounds, which is a meaningful result.
- *"The regret analysis contribution is never referenced in the evaluation"* — Section \ref{sec:regret} is almost certainly in the appendix (stripped by parser); per hard rules, missing appendix content is not a valid criticism.
- *"The paper does not report variance or multiple runs"* — Kept as Minor 5, but the harsh critic's framing as a structural flaw is excessive; single-run experiments are common for expensive real-world evaluations.
- *"The inset figure is too small to read"* — Kept as Trivial 6; the substantive content is already conveyed by text.
- *Formatting/style nitpicks* — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not provide.

## Suggestions

1. Add at least one external baseline on the real-world problems — e.g., random search with the same batch size, or a simple acquisition function (expected improvement per objective with random scalarization) paired with the same Deep Ensemble surrogate and applied for the same number of iterations. This would directly support the claim of superiority.
2. Provide a compute-time breakdown for one iteration at batch sizes 1,000, 5,000, and 20,000, separating acquisition time, surrogate training time, and NFP evaluation time.
3. Specify the architecture, ensemble size \(K\), and training hyperparameters for Deep Ensembles in the main paper (or ensure the appendix is clearly referenced).
4. Report results over at least 3 random seeds for the synthetic ZDT3 benchmarks to give a sense of variability.

## Score and Decision

This paper addresses an understudied and practically important problem — large-batch, iteration-expensive multi-objective optimization — and proposes a genuinely novel acquisition function that is well-motivated and supported by ablation analysis. The method demonstrably operates at batch sizes that break existing approaches, and the real-world validation on two distinct domains (CFD simulation and physical 3D printing) is commendable.

However, the paper's strongest claims of superiority are made without direct baseline comparison on the real-world problems. The evidence for superiority rests on the synthetic Section 3 experiments showing that existing methods cannot scale, which is necessary but not sufficient to show LBN-MOBO is the best approach. A reasonable reader would want to know how the method compares to even simple alternatives (random search, NSGA-II directly on the NFP) on the same real-world problems. The acquisition function scalability also lacks quantitative support. These are consequential gaps but not fatal — the core algorithm is novel and the iteration-efficiency results are convincing even without baselines.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>