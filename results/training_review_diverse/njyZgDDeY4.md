I now have all the verification needed. Let me produce the final consolidated review.

---

## Summary

The paper introduces Pessimistic PCFR$^+$ (P2PCFR$^+$), a variant of Predictive CFR$^+$ that scales the prediction term (the instantaneous regret from the previous iteration) by $1/(1+\alpha)$ before adding it to the implicit accumulated regret. The goal is to reduce the discrepancy between strategies represented by implicit and explicit accumulated regrets within the same iteration, which in turn reduces strategy swings across iterations that slow down PCFR$^+$. The paper provides regret bounds showing improved constants, and experiments on nine instances of four games show that P2PCFR$^+$ with $\alpha=5$ converges faster than several CFR baselines.

## Strengths

1. **Clear motivational grounding with a concrete example**: The paper identifies a precise failure mode of PCFR$^+$ — the flip-flopping of strategies between iterations (Section 4.1, the $[1;0] \to [0;1]$ example) — and directly motivates the proposed solution from this diagnosis. The example makes the problem intuitive and the method's rationale transparent.

2. **Simple, easily implementable modification**: P2PCFR$^+$ changes only a single line of the existing PCFR$^+$ update — scaling the prediction term by $1/(1+\alpha)$. This makes the method immediately practical and accessible, as the paper notes.

3. **Rigorous theoretical regret bounds with clear improvement**: The paper provides four theorems (4.1–4.4) establishing regret bounds for P2PCFR$^+$ under both the favorable-alignment case (Theorems 4.1–4.2) and the worst-case scenario (Theorems 4.3–4.4). In both settings, the constant in the bound improves over PCFR$^+$ for $\alpha > 0$ (smaller factor $\sqrt{(2+\alpha)/(1+\alpha)}$ in Theorem 4.2 when $\alpha \leq 1$, and smaller $\sqrt{1+1/(1+\alpha)^2}$ in Theorem 4.4 for any $\alpha \geq 0$).

4. **Comprehensive empirical validation**: Experiments across nine instances from four standard benchmarks (Kuhn Poker, Leduc Poker, Goofspiel, Liar's Dice) show that P2PCFR$^+$ converges faster than PCFR$^+$, Stable PCFR$^+$, Smooth PCFR$^+$, CFR$^+$, DCFR, and vanilla CFR in nearly all cases. The paper reports that PCFR$^+$ never outperforms P2PCFR$^+$ on these benchmarks.

5. **Empirical verification of the core mechanism**: Figure 2 directly measures the discrepancy between strategies represented by implicit and explicit accumulated regrets. The results confirm that P2PCFR$^+$ reduces this discrepancy relative to PCFR$^+$, supporting the paper's central motivational claim.

6. **Hyperparameter sensitivity analysis**: Figure 3 systematically shows the effect of $\alpha$ on performance across four games, demonstrating that P2PCFR$^+$ consistently beats PCFR$^+$ for $\alpha \leq 10$, while performance degrades at very large $\alpha$ (e.g., 50, 100). The paper provides a plausible explanation (diminishing "looking one step ahead" insight).

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between theory range and experimental configuration**: Theorem 4.2 is stated with the restriction $1 \geq \alpha \geq 0$ (line 160), yet the main experimental results (Figure 1) use $\alpha=5$. The paper acknowledges this (line 256: "Although Theorem 4.2 requires $\alpha \leq 1$, we set $\alpha=5$ because it empirically achieves a faster convergence rate than $\alpha=1$") but does not resolve the inconsistency. The paper's central narrative — that reducing discrepancy via scaling the prediction term (tied to Theorems 4.1–4.2) yields faster convergence — is experimentally evaluated with a parameter outside the proven range for precisely that narrative.  

   *Mitigating factor*: Theorem 4.4 (the worst-case bound) has no $\alpha$ restriction and shows a strictly improving constant $\sqrt{1+1/(1+\alpha)^2}$ for all $\alpha \geq 0$, so the theory does not completely break down at $\alpha=5$. However, the paper does not cleanly separate which theorem covers which experimental configuration, leaving the reader uncertain whether the theory actually explains the observed speedups. The authors should either extend Theorem 4.2 to $\alpha > 1$, explicitly note that Theorem 4.4 covers the experimental range, or run the main experiments with $\alpha \leq 1$ and demonstrate that the gains still hold.

### Minor

2. **"Faster theoretical convergence rate" phrasing is ambiguous**: The paper repeatedly states that P2PCFR$^+$ enjoys a "faster theoretical convergence rate" than PCFR$^+$ (lines 4, 20, 27, 249), but the improvement is in the *constant factor* of the bound, not the asymptotic order — both are $O(1/\sqrt{T})$ in the worst case (Theorem 4.4) and depend on a sum-of-differences term in the favorable case (Theorem 4.2). While technically correct, this phrasing could mislead readers into expecting an improved exponent. The paper would benefit from stating "a smaller constant in the regret bound" or "improved multiplicative factor" when describing the theory, reserving "faster convergence" for the empirical results.

3. **Figure 2 discrepancy metric is underspecified**: The paper reports the "discrepancy between strategies represented by the implicit and explicit accumulated counterfactual regrets" using the $\ell_1$-norm (line 263), but the reported y-axis values exceed 2 (and in some games exceed 10), confirming the metric is aggregated over infosets. The paper does not specify the aggregation method (sum? average? max?). Without this definition, readers cannot interpret the magnitude or compare across games, which undermines Figure 2, a plot central to the paper's motivational narrative.

4. **Overclaim on "parameter-free" property**: The paper claims P2PCFR$^+$ "obtain[s] the parameter-free property" (line 38), contrasting with Stable/Smooth PCFR$^+$ which forfeit it. While P2PCFR$^+$ does not require tuning $\alpha$ for *convergence guarantees* (any $\alpha \geq 0$ works), the paper itself explicitly tunes $\alpha$ for performance ("we set $\alpha=5$ because it empirically achieves a faster convergence rate than $\alpha=1$"). This makes the "parameter-free" claim misleading in a practical sense. The paper should clarify that the algorithm is parameter-free in the narrow theoretical sense (no learning-rate tuning needed for convergence) but acknowledges $\alpha$ as a performance parameter.

5. **No results for $\alpha \leq 1$ in the main convergence plots (Figure 1)**: Although Figure 3 shows that $\alpha \leq 10$ works well, and the text mentions $\alpha=1$ was tested, the reader cannot see where $\alpha=1$ sits relative to $\alpha=5$ and PCFR$^+$ in the primary results figure. Given that Theorem 4.2 only covers $\alpha \leq 1$, explicitly showing $\alpha=1$ in Figure 1 (or a companion plot) would strengthen the connection between theory and experiment.

### Trivial

None.

## Nice-to-Haves

- An ablation that artificially increases the discrepancy (e.g., $\alpha < 0$, or scaling the prediction term up instead of down) would strengthen the causal argument that *reducing* discrepancy *causes* faster convergence.
- A full table of exploitability after a fixed number of iterations for multiple $\alpha$ values across all nine games (not just the four in Figure 3) would give a more complete picture of $\alpha$ sensitivity.

## Removed Points

- *"Cauchy-Schwarz bound claim about $\|\tilde{\sigma}_i^{t+1}(I) - \tilde{\sigma}_i^t(I)\|_2^2$ remaining the same is questionable because implicit regrets differ"* — The reviewer's point is technically correct (the implicit regrets evolve differently under P2PCFR$^+$ vs. PCFR$^+$), but the paper's argument is about the *functional form* being identical, not about the numerical values being identical. This is an extremely subtle point that does not affect the paper's core argument.
- *"Undefined $\eta$ in Theorem 4.1"* — Parser artifact (bracketed notation in the equation).
- *"Missing statistical significance / variance"* — CFR full-tree traversals are deterministic; this is not standard practice for this class of paper.
- *"Missing related works"* — Per instructions, not verifiable.
- *"PCFR$^+$ converges more slowly than classical CFR algorithms — not cited"* — The paper says "as evidenced by our experiments using the open-source implementation," so the claim is self-referentially supported. The reviewer's suggestion to position this differently is a taste preference.

## Novel Insights

The most interesting observation to emerge from the reviews is a limitation that the paper itself does not fully explore: the optimal $\alpha$ represents a tradeoff that the theory only partially captures. Theorem 4.2 (favorable-alignment case) suggests $\alpha \leq 1$, Theorem 4.4 (worst-case) gets better with arbitrarily large $\alpha$, and empirically $\alpha \approx 5$ is best. The fact that very large $\alpha$ (50, 100) degrades performance — because the "looking one step ahead" insight of PCFR$^+$ is lost — reveals that P2PCFR$^+$ operates in a Goldilocks zone: enough pessimism to stabilize strategies, but not so much that the predictive mechanism is nullified. This three-way tension (theory vs. theory, theory vs. practice, mechanism vs. stability) is not currently articulated in the paper and would make a deeper contribution if analyzed.

## Suggestions

1. **Reconcile the theory-experiment range.** Either (a) explicitly note that Theorem 4.4 covers $\alpha=5$ and that the experimental results are consistent with both theorems, or (b) add a sub-figure to Figure 1 showing $\alpha=1$ alongside $\alpha=5$ so readers can see the progression. If possible, extend Theorem 4.2 to $\alpha>1$ or clarify whether the $\alpha \leq 1$ restriction is a proof artifact.

2. **Define the discrepancy metric in Figure 2 precisely.** Specify whether the $\ell_1$-norm discrepancy is summed over all infosets, averaged, or another aggregation. State the formula.

3. **Replace "faster theoretical convergence rate" with more precise language** (e.g., "improved constant in the regret bound") when describing the theoretical results. Reserve "faster convergence" for empirical claims.

4. **Clarify the "parameter-free" claim.** Either drop it or clearly separate the theoretical sense (no tuning needed for convergence) from the practical sense ($\alpha$ affects performance).

5. **Provide a sensitivity table/heatmap** of $\alpha$ across all nine games, not just the four in Figure 3, to give complete guidance for practitioners.

## Score and Decision

The paper presents a simple, well-motivated modification to PCFR$^+$ with strong empirical support across diverse benchmarks. The idea is novel, the implementation is trivial, and the gains are consistent. However, the structural inconsistency between the theory range ($\alpha \leq 1$ for the main proof) and the experimental configuration ($\alpha=5$) weakens the coherence of the contribution. While Theorem 4.4 partially mitigates this concern, the paper would be significantly stronger if this gap were addressed. The contribution is real and the paper is above the rejection threshold with revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>