Now I have a good set of anchors. Let me synthesize my final review.

**Calibration summary across anchors:**

- **BQIzu1T6F0** (6.00, Accept): Solid theory with clear practical implications, well-executed. Our paper has more ambitious claims but weaker support.
- **jITPFROpWN** (5.00, Accept): Genuine contribution with novel controllability guarantees, though incremental. Our paper's theoretical contribution is less cleanly tied to its headline claim.
- **Debxx12J0U** (4.50, Reject): Strong theory but limited/oversold experiments. Similar pattern to our paper but the theory there was more substantive.
- **7UPZMoLRTI** (4.00, Reject): Purely theoretical, limited novelty. Our paper has experiments but the theory-scope issue is parallel.
- **iElE0OESEf** (3.33, Withdrawn): Theory + experiments, but weak novelty and limited benchmarks. Our paper has more experiments but a more fundamental theory-scope mismatch.
- **hSjjVXWPS5** (3.00, Withdrawn): Disconnect between claims and evidence. Our paper is better organized but shares some of this pattern.

Our paper is closest to the 4.0-4.5 range. The theoretical framing is significantly oversold relative to what's actually proved, and the experiments don't isolate the claimed phenomenon from optimization artifacts. I'll assign **4.0**.

---

## Summary

This paper argues that ensembles of nonlinear (neural) policies are inherently sub-optimal compared to ensembles of linear policies in control settings. It provides three theorems: (1) neural ensembles have strictly larger cost than linear ensembles on linear systems under diversity/nonlinearity conditions, (2) time-varying ensemble weights can destabilize neural ensembles even when individual policies are stable, and (3) non-convex (neural) mixing of optimal linear policies is sub-optimal relative to convex mixing. Experiments on linear multi-regime systems and nonlinear benchmarks (Pendulum, CartPole) are presented to support the claims.

## Strengths

- **Interesting motivating question.** The paper correctly identifies a genuinely underexplored question: whether the statistical averaging benefits that ensembles enjoy in i.i.d. classification settings transfer to temporally-coupled sequential decision-making. (Section 1)

- **Theorem 2 isolates a real mechanism.** The stability result—showing that time-varying ensemble weights can cause instability even when every component policy is individually stable—captures a failure mode specific to *ensembles* (not just nonlinearity) and provides a concrete condition on the weight-change rate β. (Section 3.2)

- **Systematic diversity experiments.** The experiments vary ensemble diversity δ across a range (Figure 3) and test multiple switching patterns (Figure 2), which is more thorough than a single-condition comparison. The diversity experiments show the neural ensemble gap persists across all δ values, which is consistent with the paper's thesis.

- **Clear formal framework.** The mathematical setup (Definitions 1–13) is self-contained and makes the theorems' assumptions transparent, allowing verification of the proofs in the supplementary material.

## Weaknesses

### Fatal

None that individually invalidate all contributions, though the cumulative effect of the major weaknesses below undermines the paper's central headline claim.

### Major

- **Theorem 1 does not support the paper's central claim about ensembles.** The theorem is set on a stabilizable *linear* system with quadratic costs, where the optimal controller is known to be linear. The linear ensemble in the comparison is constructed from optimal LQR controllers (line 105: "corresponding optimal linear policies... solving individual LQR problems"), making it a weighted combination of optimal linear gains—itself an optimal or near-optimal linear controller. The neural ensemble is compared against this de facto optimal linear controller. The resulting cost gap follows from the well-known fact that a nonlinear controller cannot outperform the optimal linear controller on a linear system with quadratic cost; the *ensemble* structure contributes nothing beyond what a single-neural-policy vs. single-optimal-linear-policy comparison would yield. The theorem's conditions (diversity δ, nonlinearity κ₀, complexity L_f) are set-dressing that obscure this. This is a structural mismatch between what the theorem actually proves and what the paper claims it proves about ensembles.

- **Experiments do not rule out optimization failure.** The paper compares analytically-computed LQR controllers against neural networks trained via gradient descent, but provides no evidence that the individual neural policies can approach optimal performance even on a single regime. The observed 2× cost gap (432 vs. 234 in Figure 1) could arise from insufficient training, poor architectures, or inadequate hyperparameter tuning—not from any inherent property of ensembles. The paper notes that the neural ensemble adapts weights more slowly than the linear ensemble (Figure 2, middle row), which is itself a plausible optimization-based explanation for the gap. Without single-regime convergence evidence, the empirical results cannot be attributed to the claimed ensemble sub-optimality.

### Minor

- **Theorem 3 does not engage with standard softmax-based neural mixing.** The theorem shows non-convex mixing (weights outside the simplex) is suboptimal for LQ costs. However, many practical neural mixing approaches (e.g., MoE gating with softmax) produce simplex-constrained weights by construction and would thus fall under the paper's own definition of "convex mixing." The paper does not discuss this case, making the claim that "neural mixing is sub-optimal" (line 32) overstated without qualification. The experiments (Figure 5) test an unconstrained neural mixer; whether a softmax-constrained neural mixer would also underperform is not investigated.

- **Stability experiments do not verify Theorem 2's conditions.** The stability experiments (Section 5, Figure 4) use nonlinear systems (Pendulum, CartPole) against a linearized LQR baseline. Theorem 2 requires each neural policy to have a verified CLF satisfying ∇V_i(x)^T f(x, π^{iθ}(x)) ≤ −α_i‖x‖²—a condition that is neither verified nor discussed in the experiments. The comparison is effectively between a model-based linearized controller and a model-free neural ensemble on nonlinear systems, which does not isolate the ensemble-weight-variation mechanism identified in Theorem 2.

- **The temporal-coupling intuition from the introduction is not captured by the theory.** The introduction motivates the paper by contrasting classifier ensembles (where errors cancel under i.i.d. sampling) with policy ensembles (where temporal feedback loops amplify errors). This is a compelling intuition, but none of the three theorems model or leverage this temporal error-propagation mechanism. Theorem 1 reduces to a linear-vs-nonlinear gap on a static optimality comparison; Theorem 2 is about weight variation speed, not error amplification through dynamics; Theorem 3 is about convexity of mixing weights, not temporal coupling. The gap between motivating intuition and formal results weakens the paper's coherence.

### Trivial

- The abstract claims "2 orders of magnitude" performance gaps, but the actual gaps in Figure 1 are roughly a factor of 2, not 100. The phrasing is misleading.

## Nice-to-Haves

- It would strengthen the paper to show a training-curve for a single neural policy on a single regime, demonstrating convergence to near-LQR performance. This would help rule out optimization failure as the explanation for the ensemble gap.
- A softmax-constrained neural mixer baseline in the policy-mixing experiments would directly test whether neural mixing per se is suboptimal or only *unconstrained* neural mixing.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Theorem 1 is fundamentally vacuous"** (Harsh Critic, Point 1) — Removed in its strongest form. The theorem is mathematically valid; its weakness is scope and interpretation, not vacuity. The gap it identifies is real but does not isolate an ensemble-specific phenomenon. Weakened and reframed above as a major weakness about scope mismatch.

2. **"Theorem 3 and policy-mixing experiments attack a strawman"** (Harsh Critic, Point 3) — Partially removed. The strong "strawman" characterization is excessive; the paper does cite works that may use unconstrained mixing. However, the failure to address softmax-based mixing is retained as a minor weakness.

3. **"Modern neural mixing methods (e.g., MoE gating with softmax) produce weights that lie in the simplex by construction, making the result irrelevant"** — Removed as an absolute claim. The relevance depends on whether the cited prior work uses softmax; the paper should discuss this but the theorem is not "irrelevant."

4. **"The paper does not engage with the extensive literature on stable neural network control, Lyapunov-based neural controllers, or safe RL"** (Harsh Critic, Section-by-Section) — Removed per instructions (missing related works).

5. **Various formatting/style nitpicks** — Removed per instructions (parser artifacts, not author errors).

6. **Strength Finder: "Large, statistically significant empirical gap..."** — Retained in modified form but the evidential value is weakened by the optimization-failure concern.

7. **Strength Finder: "Stability experiments demonstrate severe performance losses..."** — Retained but qualified by the mismatch between experimental setup and theoretical conditions.

## Novel Insights

The most genuinely novel observation from the reviews is the structural mismatch between Theorem 1's actual content and the paper's ensemble-focused narrative. The theorem's setup—comparing nonlinear controllers to optimal linear ones on a linear system—is a canonical result in control theory; the ensemble framing is orthogonal to why the gap exists. This pattern recurs across the paper: the temporal-coupling motivation is not formalized, the stability result is about weight-variation speed rather than nonlinearity per se, and the mixing result is about simplex constraints rather than neural architectures. The paper would be stronger if it narrowed its claims to what it actually proves: that common practices in neural policy ensembles (unconstrained mixing, time-varying weights without stability analysis, reliance on nonlinear function approximation where linear controllers are optimal) can lead to suboptimality, rather than claiming a universal "inherent sub-optimality" of neural ensembles.

## Suggestions

- **Reframe Theorem 1 honestly:** Acknowledge that it shows a nonlinear-vs-optimal-linear gap on linear systems, not an ensemble-specific phenomenon. The ensemble aspect of the theorem is the *construction* (weighted combination of per-regime policies), but the gap driver is nonlinearity vs. linear optimality.
- **Add a single-regime training baseline:** Train one neural policy on one regime and compare its cost to the LQR cost for that regime. If the gap is small, the ensemble gap is more plausibly an ensemble phenomenon. If large, the ensemble gap is confounded by optimization.
- **Test softmax-constrained neural mixing** to determine whether the suboptimality in Section 6 is due to non-convex weights or to neural mixing per se.
- **Tone down the abstract:** Replace "2 orders of magnitude" with the actual factor (~2×) and soften "formally prove... sub-optimal" to reflect the linear-system scope of the theoretical result.

## Score and Decision

**Anchor comparison:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| BQIzu1T6F0 | Spectral control of LDS | 6.00 (Accept) | Much stronger: theory directly supports claims, clear practical advance |
| jITPFROpWN | Koopman + controllability | 5.00 (Accept) | Stronger: contribution is narrower but well-supported; our paper oversells |
| Debxx12J0U | Optimal control + multiplicative noise | 4.50 (Reject) | Similar pattern (theory oversold relative to experiments) but cleaner theoretical contribution |
| 7UPZMoLRTI | Policy transfer for LQR | 4.00 (Reject) | Our paper has experiments but similar theory-scope mismatch |
| iElE0OESEf | Neural policy iteration | 3.33 (Withdrawn) | Our paper has more empirical breadth but similar disconnect between claims and support |
| hSjjVXWPS5 | Sliding window Q-ensemble | 3.00 (Withdrawn) | Our paper is better organized with genuine theorems, less disconnect |

The paper under review has genuine theoretical contributions (Theorems 2 and 3 in particular) and systematic experiments, but the headline claim about neural ensemble sub-optimality is not supported by Theorem 1 (which does not isolate an ensemble effect) and the experiments do not rule out optimization failure. This places it below Debxx12J0U (cleaner theory) and above iElE0OESEf (less empirical validation). **Score: 4.0, Reject.**

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>