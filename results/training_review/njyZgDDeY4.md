Now I have thoroughly verified all claims in the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes P2PCFR+, a variant of Predictive CFR+ that scales the prediction term by a factor of 1/(1+α) to reduce the discrepancy between implicit and explicit accumulated counterfactual regrets. The authors provide theoretical regret bounds (Theorems 4.1–4.4) and evaluate the algorithm across 9 game instances from 4 standard benchmarks (Kuhn Poker, Leduc Poker, Goofspiel, Liar's Dice). The core idea is simple—a single-line modification to existing PCFR+ code—and the empirical results show consistent improvement over PCFR+, Stable PCFR+, Smooth PCFR+, and classical CFR algorithms.

## Strengths

- **Simple and principled algorithmic idea.** The paper identifies a genuine weakness in PCFR+ (large cross-iteration strategy discrepancy) and proposes a clean fix: scaling the prediction by 1/(1+α) to make it more conservative. Unlike Stable/Smooth PCFR+, which sacrifice the parameter-free property by requiring a tuned learning rate, P2PCFR+ retains the hyperparameter-light nature of PCFR+ (α ≤ 10 works well across all tested games without per-game tuning).

- **Consistent and substantial empirical gains.** Across 9 game instances (Figure 1), P2PCFR+ achieves the fastest convergence among all tested algorithms (PCFR+, CFR+, DCFR, vanilla CFR, Stable PCFR+, Smooth PCFR+). In 7 of 9 games, P2PCFR+ substantially outperforms PCFR+, and it strictly outperforms Stable and Smooth PCFR+ in every instance. The improvement is not marginal—in several games (e.g., Leduc Poker, Goofspiel(6)), the gap is several orders of magnitude in exploitability.

- **Direct validation of the proposed mechanism.** Figure 2 plots the within-iteration strategy discrepancy (implicit vs. explicit) for both PCFR+ and P2PCFR+. In games where P2PCFR+ converges faster, the discrepancy is consistently lower, providing evidence that the mechanism works as intended. This strengthens the causal link between the design choice and the observed behavior.

- **Parameter robustness.** Figure 3 shows that α ≤ 10 consistently outperforms PCFR+ (α=0), while performance degrades only at extreme values (α=50, 100). This gives practitioners a wide safe operating range without per-game tuning.

## Weaknesses

### Fatal
None.

### Major

1. **Unjustified claim about implicit strategy discrepancy.** The paper states (line 144): "Obviously, the value of ∥σ̃_i^{t+1}(I)−σ̃_i^t(I)∥₂² remains the same as in PCFR⁺." This claim is NOT obvious and is almost certainly false. The implicit accumulated regrets evolve as R_I^{t+1}=[R_I^t+r_I^t]⁺, where the instantaneous regret r_I^t depends on the explicit strategy σ_i^t. Since P2PCFR+ changes the explicit strategy (by scaling the prediction), the sequence of r_I^t differs from PCFR+, and consequently the implicit regrets R_I^t differ, and hence the implicit strategies σ̃ differ. The argument that reducing within-iteration discrepancy reduces cross-iteration discrepancy while keeping the implicit discrepancy "the same" is therefore unsupported. **This undermines the central theoretical narrative.** The theorems themselves may still be valid mathematical statements about P2PCFR+, but the explanatory chain connecting the algorithm design to tighter bounds is broken.

2. **Theory-practice mismatch in α.** Theorem 4.2 explicitly requires α ≤ 1 ("Assume that T iterations of P2PCFR+ with any 1 ≥ α ≥ 0"). Yet all main experiments (Figure 1, Figure 2) use α = 5, and Figure 3 shows α up to 10 works well. The paper acknowledges this ("although Theorem 4.2 requires α≤1, we set α=5 because it empirically achieves a faster convergence rate than α=1") but does not resolve it. The best-performing configuration is not covered by the theory, severing the connection between the theoretical guarantees and the empirical results. Readers are left wondering whether the theoretical improvement for α≤1 is practically meaningful, and whether the empirical success of α=5 has any theoretical backing.

### Minor

3. **Incomplete experimental reporting.** No multiple seeds, variance, or confidence intervals are reported. While CFR algorithms are deterministic given the seed for chance events, single-run results with no seed documentation provide limited evidence about the reliability and generality of the findings. This is particularly relevant for games like Kuhn Poker where the improvement over PCFR+ is small—without variance estimates, it is unclear whether the difference is meaningful.

4. **The improvement is a constant factor, not an asymptotic rate change.** Theorems 4.2 and 4.4 show bounds with improved constants (e.g., √(1+1/(1+α)²) vs. √2 for PCFR+), but both algorithms have O(1/√T) worst-case rates. The paper repeatedly claims "faster theoretical convergence rate," which oversells a constant-factor improvement. This would be acceptable if appropriately qualified, but the current framing is misleading.

5. **ℓ₁/ℓ₂ norm inconsistency between theory and experiments.** The theoretical analysis (Eq. 5, Eq. 6, Theorems) uses ℓ₂-norm, but Figure 2 quantifies discrepancy using ℓ₁-norm (line 263: "The ℓ₁-norm quantifies this discrepancy"). The paper does not discuss whether these norms behave similarly in this setting or whether the ℓ₁ results support the ℓ₂-based theoretical claims.

6. **The key mechanism is only partially validated.** Figure 2 shows the within-iteration discrepancy (implicit vs. explicit), but the claimed downstream effect—reduced cross-iteration strategy discrepancy ∥σ^{t+1}−σ^t∥ and reduced prediction error ∥r^t−r^{t-1}∥—is not directly measured. The paper asserts the causal chain but provides no direct evidence for the intermediate steps.

### Trivial

7. Theorems 4.1–4.4 are stated without derivation or proof sketch; E and F are defined somewhat sloppily (the "⋮=max" is a parser artifact but the definitions are still compressed).

8. The description of Figure 2 relies on subjective language ("negligible," "large discrepancies have significant effect") without quantitative thresholds.

## Nice-to-Haves

- **Direct measurement of cross-iteration discrepancy and prediction error** for both PCFR+ and P2PCFR+, to complete the validation of the claimed causal mechanism.
- **Ablation study for α=1** (covered by theory) alongside α=5, to bridge the theory-practice gap.
- **Guidance for setting α** beyond trial-and-error (e.g., connection to game size, branching factor, or regret scale).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"PCFR+ slower than CFR+ contradicts the original paper"** — Removed. This is an empirical observation from the authors' experiments using an open-source implementation (Liu et al., 2024). If the results are reproducible, this is a valid finding, not a contradiction.
- **"Example in Section 4.1 is cherry-picked"** — Removed. All illustrative examples are by construction selected to illustrate a point; this is not a meaningful criticism.
- **"Theorems stated without derivation"** — Removed. Proofs are standardly deferred to an appendix (stripped by the parser). The more serious issue is the unjustified σ̃ claim, which is kept above.
- **"Missing appendix / missing proofs"** — Removed. These sections exist in the original submission and were stripped by the parser.
- **Various formatting complaints (⋮=max, sloppy notation)** — Removed. Parser artifacts do not reflect author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the theoretical justification.** The claim that ∥σ̃^{t+1}−σ̃^t∥ "remains the same" needs either a rigorous proof (unlikely to be possible) or a completely different argument for why the within-iteration discrepancy reduction translates to faster convergence. One option: directly bound the regret of P2PCFR+ without relying on the implicit-discrepancy argument, and compare the resulting bounds to PCFR+ honestly (acknowledging that the r^t sequences differ).

2. **Bridge the α gap.** Show that the empirical benefits hold for α ≤ 1 (the theoretically covered regime). If α=1 performs worse than α=5, then the theory and experiments are fundamentally at odds, and this needs to be discussed transparently. Alternatively, extend the theory to cover α > 1.

3. **Add multiple seeds and statistics.** Run each algorithm with at least 5 different random seeds and report mean exploitability with error bars (or shaded bands). This is now standard practice and would significantly strengthen the empirical claims.

4. **Harmonize the norm used in theory and experiments**, or justify why ℓ₁ is appropriate for Figure 2 despite ℓ₂ being used in the analysis.

## Score and Decision

The paper proposes a simple, effective modification to PCFR+ with strong and consistent empirical results across multiple benchmark games. The core algorithmic idea is novel and practically useful. However, the theoretical justification contains a significant gap (the unjustified claim about σ̃ dynamics), and there is a troubling disconnect between the theoretically analyzed regime (α ≤ 1) and the empirically best-performing configuration (α = 5). The paper also lacks statistical rigor in its experimental reporting (no multiple seeds, no variance). Despite these issues, the empirical contribution is valuable enough to warrant acceptance with major revisions—the method clearly works, and the issues are addressable. The paper would be substantially stronger with a repaired theoretical framework and more rigorous experimental methodology.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>