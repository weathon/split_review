## Summary

This paper proposes GELS (Generic Estimator based on Least Squares) and GELS-R for efficiently approximating probabilistic values by exploiting a connection between probabilistic values and least-squares regression. The key insight is that the ranking induced by any probabilistic value differs from the value vector only by an additive constant, enabling one utility evaluation to simultaneously update estimates for all contained data points. The paper also introduces TrELS, which casts distributional values as least-squares problems, enabling unsupervised training of neural-network estimators. Experiments at n=24 verify convergence, and TrELS experiments on MNIST/FMNIST with n=10,000 show that trained estimators can outperform Monte Carlo with 20× fewer utility evaluations per point.

## Strengths

- **Novel least-squares connection for generic probabilistic values (Proposition 2)**: The paper identifies that the ranking from any probabilistic value can be obtained as the solution to a weighted least-squares problem with weights m_s^n = p_s^n + p_{s+1}^n (lines 108–113). This unified formulation covers the entire spectrum of probabilistic values, extending beyond the subfamily handled by prior AME (Lin et al., 2022).

- **GELS-R achieves a clear per-evaluation advantage over prior generic estimators**: Each utility evaluation U^n(S) updates s estimates simultaneously (Algorithm 1, line 138), whereas the sampling lift requires two utility evaluations per data point (line 115). This structural advantage is concretely demonstrated and is the mechanism behind the claimed speedup.

- **TrELS provides a principled, unsupervised approach to learning distributional values**: The paper shows that distributional values can be cast as optimizing a least-squares regression (Section 3, line 88), enabling neural-network training without supervised signals. The experiment (Section 4.2) demonstrates that a LeNet trained with 1,000 utility evaluations per point outperforms Monte Carlo at 20,000 evaluations per point (line 177), which is a practically meaningful reduction.

- **Honest discussion of trade-offs**: The paper acknowledges that GELS-Shapley converges slower than specialized Shapley estimators (complement, kernelSHAP) while using only Θ(n) memory versus their Θ(n²) (line 163), and notes that MSR outperforms GELS in relative error for the Banzhaf value (line 163). This transparency strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **The central O(n log n) complexity bound cannot be evaluated from the main text.** The bound is stated as O((n̄/ε²) log(n/δ)) (line 32), but n̄ is never defined anywhere in the main text. The reader cannot tell whether n̄ = n, whether it absorbs a problem-dependent constant, or whether it corresponds to an effective dimension. Additionally, the bound is claimed for "many probabilistic values" (abstract, line 32, line 88) without any characterization of which values satisfy whatever regularity condition is needed. The main text provides no theorem statement or proof sketch that would clarify either issue. This makes the headline theoretical contribution impossible to verify from the paper as presented.

- **No scaling experiments to support the central complexity claim.** The GELS convergence experiments (Section 4.1) use n = 24 data points. At n = 24, the difference between O(n log n) ≈ 76 and O(n² log n) ≈ 1830 is a small constant factor. The paper's headline improvement is an asymptotic scaling advantage, yet no experiment tests n > 24. Without evidence at n = 100, 500, or 1000, the empirical support for the scaling claim is absent.

- **TrELS evaluation lacks essential baselines and does not account for total computation.** TrELS is compared only against a Monte Carlo baseline (lines 173–177). No comparison is made against simpler estimators such as a linear model trained on the same least-squares objective, or a weighted average of Monte Carlo estimates from nearby training points. Furthermore, the comparison reports only utility evaluations (1,000 vs. 20,000 per point) but ignores the cost of training a LeNet (1,000 batches, Adam optimization). A practitioner's relevant metric is total time-to-solution, which is not reported.

### Minor

- **The "ground truth" for TrELS is itself a Monte Carlo estimate.** The paper uses 600,000 utility evaluations per data point to generate "ground-truth" distributional values (line 170). This is still a stochastic estimate, and the paper does not quantify its accuracy or provide confidence intervals. Error in the ground truth systematically compresses apparent prediction error.

- **The recovery of actual values via the null-data-point trick (GELS, Algorithm 2) is not compared against the ranking-only version (GELS-R).** Remark 1 (line 122) acknowledges that p^{n+1} may contain negative entries in the construction, but the paper does not empirically or theoretically investigate whether GELS (actual values) retains the same convergence properties as GELS-R (ranking only). If ranking suffices for most practical use cases (data screening, outlier removal), the paper should lean into this and clarify the relative guarantees.

- **Overclaiming in the conclusion.** The paper concludes that it "significantly broadens the practicality of deploying value-based data valuation methods on rather large datasets" (line 184). The GELS experiments use n = 24 — this does not demonstrate practicality at large scale. The TrELS experiment uses n = 10,000 but trains a separate LeNet estimator, which is a different setting.

- **Undefined notation in the TrELS discussion.** The transform $C\cdot(\phi_{\theta}(\dot{\mathbf{x}},y)-\phi_{o})$ is stated to be "essential for training!" (line 175) but $C$, $\phi_{o}$, and the exact transform are not defined in the main text. Eq. (7), used to compute ground-truth distributional values, is referenced twice (lines 170, 177) but also never appears in the main text. These depend on appendix content that is not visible.

### Trivial

- The sentence at line 20 ("Wang and Jia (2023, Theorem 4.2 therein that the MSR estimator does not extend...") is grammatically broken — appears to be a citation splice that obscures meaning.

## Nice-to-Haves

- Testing GELS and GELS-R at n = 100, 500, 1000 (e.g., with synthetic utility functions) to directly demonstrate the O(n log n) scaling.
- Comparing TrELS against simpler learned baselines (linear model, nearest-neighbor average) to isolate the source of improvement.
- Reporting wall-clock time for TrELS rather than only utility evaluation counts.

## Removed Points

*These points were flagged by the reviewers but removed after verification against the paper.*

- **"The least-squares formulation in Proposition 3 uses negative weights, breaking convexity and convergence guarantees."** Removed as factually incorrect. Proposition 3 uses p_s^n (non-negative by definition, line 12) as weights, not the constructed p^{n+1} which may have negative entries (Remark 1, line 122). The paper's weights are non-negative and the quadratic problem remains convex.
- **"The paper cites missing appendix content (Algorithms 3, 4, Theorem 1)"** — removed per instructions: the parser strips these sections from all papers; they exist in the original submission.
- **"TrELS-SC cherry-picking"** — the paper acknowledges that relative-difference-based selection performs poorly due to training instability (line 177). This is transparent reporting, not cherry-picking.
- **"Broken/parser-garbled sentences are author errors"** — removed per instructions (formatting artifacts are parser issues, not author errors).
- **"Criticism about missing proofs in appendix"** — removed per instructions: proof sections stripped by parser exist in the original submission.
- **"Missing related works"** — removed per instructions (cannot be verified without external sources).
- **The critic claims about "may not be (ε,δ)-approximation for all probabilistic values" being a fatal flaw** — demoted to Major because the bound uses undefined $\bar{n}$ and unspecified "many," but this is an incompleteness in the main text, not a verifiable fatal error given the appendix is stripped.

## Novel Insights

None beyond the paper's own contributions. The reviewer criticisms largely identify gaps in evidence and presentation rather than revealing unexpected insights about the approach itself.

## Suggestions

1. **Define $\bar{n}$ in the main text** and precisely state which probabilistic values the O(n log n) bound covers. If the bound requires a condition on p^n (e.g., bounded variance ratio), state it explicitly.
2. **Run scaling experiments** for GELS/GELS-R at n ≥ 100 on synthetic utility functions to demonstrate the claimed asymptotic advantage.
3. **Add baselines to the TrELS experiment**: a linear regression on the same least-squares objective and a direct Monte Carlo estimator matched on total compute budget (including training time).
4. **Ablate GELS vs. GELS-R** to clarify whether the ranking-only version maintains the same convergence rate as the value-recovery version, and to help practitioners decide which to use.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>