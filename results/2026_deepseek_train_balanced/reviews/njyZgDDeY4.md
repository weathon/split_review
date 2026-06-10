Now let me produce the final consolidated review.

## Summary

The paper introduces Pessimistic PCFR⁺ (P2PCFR⁺), a variant of PCFR⁺ that scales the prediction term by \(1/(1+\alpha)\) to reduce strategy discrepancy between consecutive iterations. The modification is motivated by a Cauchy-Schwarz bound (Eq. 5) decomposing the cross-iteration strategy discrepancy into within-iteration discrepancies. The paper provides regret bounds showing constant-factor improvements and demonstrates empirically that P2PCFR⁺ converges faster than PCFR⁺, CFR⁺, DCFR, and other variants across 9 instances of 4 benchmarks.

## Strengths

1. **Simple, principled modification**: Replacing \(r^{t-1}\) with \(\frac{1}{1+\alpha}r^{t-1}\) in PCFR⁺'s explicit regret update is a single-line change grounded in a Cauchy-Schwarz decomposition (Eq. 5) that cleanly motivates why shrinking the prediction step should reduce strategy oscillations.

2. **Theoretical bounds with genuine constant improvement**: Theorems 4.3–4.4 give regret/exploitability bounds with a factor \(\sqrt{1+1/(1+\alpha)^2}\) that decreases as \(\alpha\) increases. When \(\alpha\to0\) (PCFR⁺), the factor is \(\sqrt{2}\); for \(\alpha=5\) it is \(\approx 1.014\) — a concrete constant-factor improvement within the \(O(1/\sqrt{T})\) worst-case class.

3. **Empirical outperformance with mechanism evidence**: Figure 1 shows P2PCFR⁺ converging faster than all six baselines (PCFR⁺, Stable PCFR⁺, Smooth PCFR⁺, CFR⁺, DCFR, vanilla CFR) across 9/9 game instances. Figure 2 directly measures the within-iteration discrepancy (\(\ell_1\)-norm) that the method targets, confirming the mechanism and showing correlation between discrepancy reduction and convergence speedup.

4. **Parameter sensitivity analysis**: Figure 3 systematically varies \(\alpha\) across \(\{0, 0.5, 1, 5, 10, 50, 100\}\), showing robustness for \(\alpha \le 10\) and degradation only at extreme values — with an honest explanation of why large \(\alpha\) diminishes the look-ahead effect.

5. **Concrete diagnosis of a real PCFR⁺ limitation**: Section 4.1 provides a clear numerical example (implicit regret \([2;0]\), instantaneous regret \([1;-1]\), leading to strategy reversal \([1;0]\to[0;1]\)) that illustrates how PCFR⁺ can suffer from strategy flips across iterations.

## Weaknesses

### Fatal

None.

### Major

1. **Theory–experiment gap on the \(\alpha\) constraint**: Theorem 4.2 explicitly requires \(\alpha \le 1\) ("Assume that \(T\) iterations of P2PCFR⁺ with any \(1 \ge \alpha \ge 0\) are conducted"), yet the main experiments use \(\alpha = 5\). The paper acknowledges this ("Although Theorem 4.2 requires \(\alpha \le 1\), we set \(\alpha = 5\)") but does not reconcile it. While Theorem 4.4 (the worst-case bound) has no \(\alpha\) constraint and still applies, the paper invokes Theorem 4.2 when interpreting results (Section 5: "Since large discrepancies have significant effect on empirical convergence rates as shown in Theorem 4.2"). This means the central theoretical guarantee that directly involves the \(\alpha\)-dependent factor does not cover the regime in which the method is evaluated, creating a structural disconnect between the theory and experiments.

2. **"Parameter-free" claim is factually incorrect**: The paper states that Stable PCFR⁺ and Smooth PCFR⁺ "forfeit a crucial property of PCFR⁺ —parameter-free—meaning no parameters need to be tuned," and explicitly claims P2PCFR⁺ "still obtaining the parameter-free property" (Section 2). However, P2PCFR⁺ introduces \(\alpha\), a scalar hyperparameter that the paper systematically tunes: it tests \(\alpha \in \{0, 0.5, 1, 5, 10, 50, 100\}\) and selects \(\alpha = 5\) based on empirical performance. This directly contradicts the paper's own definition of "parameter-free."

### Minor

1. **"Faster theoretical convergence rate" phrasing overstates the improvement**: The improvement established in Theorems 4.3–4.4 is in the constant factor within the \(O(1/\sqrt{T})\) rate class, not a change in asymptotic rate. PCFR⁺ can achieve \(O(1/T)\) in the best case (when predictions align); P2PCFR⁺ inherits this property, but the paper's theoretical comparison focuses on the worst-case bounds. The repeated phrasing "faster theoretical convergence rate" suggests a rate-class improvement rather than a constant-factor one, which could mislead readers about the nature of the advance.

2. **Motivating claim about PCFR⁺ vs CFR⁺ is too strong**: The paper asserts that PCFR⁺ "converges more slowly than other classical CFR algorithms, such as CFR⁺, even in standard IIG benchmarks like Leduc Poker, Goofspiel, and Liar's Dice" (Section 1). This is stated as an established fact but is the paper's own observation from one implementation (Liu et al., 2024). The original PCFR⁺ paper (Farina et al., 2021) reports the opposite. The paper should present this as an empirical finding conditional on the specific implementation, not as a settled fact about the algorithm.

3. **Core mechanism asserted rather than formally proven**: The paper states that scaling the prediction "intuitively reduces the gap between implicit and explicit accumulated counterfactual regrets" (Section 4.2) but does not provide a formal argument — only intuition. Figure 2 provides empirical support, which partially mitigates this, but the theoretical narrative relies on an unproven assertion.

### Trivial

None.

## Nice-to-Haves

- A discussion of whether the \(\alpha \le 1\) constraint in Theorem 4.2 is an artifact of the proof technique or a fundamental limitation, and whether it could be relaxed.
- Clarification of how alternating updates and linear averaging (applied uniformly to all algorithms) interact with the \(\alpha\) parameter, since these techniques can affect different CFR variants differently.

## Removed Points

The following points from the reviewer inputs were verified against the paper and removed with justification:

- **"Ceteris paribus assumption is contradictory"** (Harsh Critic #3): Comparing regret bounds under the condition that \(\|r^t_I - r^{t-1}_I\|_2^2\) remains the same is standard practice in the regret analysis literature (cf. any paper comparing bounds with data-dependent terms). It does not claim the quantities *are* the same across algorithms; it isolates the effect of the leading constant. If the method additionally shrinks this term (as argued), the improvement is even larger. This is not a logical contradiction.
- **No error bars / lack of statistical significance**: Single-run evaluation is standard in deterministic CFR algorithms for two-player zero-sum games. The method is deterministic, so the absence of confidence intervals is not a weakness by the field's norms.
- **Theorem bounds are "garbled" / difficult to parse**: These are PDF-parser artifacts. The submitted paper contains properly formatted equations.
- **Missing appendices, proofs, references**: Parser strips these from all papers; they exist in the original submission.
- **Formatting / style nitpicks**: Parser artifacts, not author errors.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question"): These are superficial and lack specific evidence; dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reconcile the theory–experiment \(\alpha\) gap**: Either (a) relax the \(\alpha \le 1\) constraint in Theorem 4.2 (or provide a modified proof), or (b) run the primary experiments with \(\alpha = 1\) (Figure 3 suggests \(\alpha=1\) still meaningfully outperforms PCFR⁺) and present \(\alpha=5\) results as a supplementary exploration.
2. **Remove or redefine the "parameter-free" claim**: Acknowledge \(\alpha\) as a tunable parameter and provide practical guidance for setting it (the paper already has most of the data for this in Figure 3).
3. **Reframe "faster convergence rate"**: Clarify that the theoretical improvement is in the leading constant within the \(O(1/\sqrt{T})\) worst-case class, not a change in asymptotic rate.
4. **Add a formal argument** (even a brief sketch) for why scaling by \(1/(1+\alpha)\) reduces the implicit–explicit strategy gap, rather than relying entirely on intuition.
5. **Soft the motivating claim about PCFR⁺**: Present the observation that PCFR⁺ sometimes underperforms CFR⁺ as an empirical finding from the specific implementation, not as a general established fact.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>