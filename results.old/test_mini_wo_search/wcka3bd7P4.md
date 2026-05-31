Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper introduces FROND, a framework that generalizes continuous GNNs by replacing integer-order derivatives with Caputo fractional derivatives of order β ∈ (0,1]. The core theoretical contributions are: (1) a non-Markovian random walk interpretation connecting the fractional diffusion equation to a path-history-dependent walk on the graph, and (2) a proof that the linear fractional diffusion model (F-GRAND-l) converges to its stationary distribution at a slow algebraic rate Θ(t^{−β}) rather than the exponential rate of integer-order models, thereby mitigating oversmoothing. Empirically, FROND variants built on five backbone architectures (GRAND, GRAND++, CDE, GREAD, GraphCON) show improved accuracy across many datasets.

## Strengths

- **Algebraic convergence proof (Theorem 3/Theorem thm.rate)**. The paper proves that the linear fractional diffusion model converges to stationarity at rate Θ(t^{−β}) — strictly slower than the exponential rate O(e^{−rt}) of the integer-order counterpart. This is a clean, non-trivial theoretical result that provides a principled explanation for oversmoothing mitigation in deep GNNs. The oversmoothing experiment (Figure 2) corroborates this: F‑GRAND‑l maintains accuracy up to 128 layers while GRAND‑l degrades.

- **Non-Markovian random walk interpretation (Theorem 2/Theorem thm.rand_walk_int, Corollary 1)**. The paper constructs a random walk whose transition probabilities depend on the full path history (Eq. 31) and proves its continuous limit satisfies the fractional diffusion equation (Eq. 8). This explicitly connects the fractional derivative to a memory-bearing stochastic process that reverts to Markovian (memoryless) walk only at β=1. The construction goes beyond the Markovian interpretation available for GRAND‑l.

- **Consistent empirical improvement across multiple backbone architectures (Tables 1–3, Table 4)**. FROND variants (F‑GRAND‑l, F‑GRAND‑nl, F‑CDE) outperform their integer-order counterparts on nearly all 10 node-classification datasets (up to ∼7–18% on tree-structured graphs) and on all 6 graph-classification settings. Improvements are demonstrated across 5 different backbone architectures (GRAND, GRAND++, CDE, GREAD, GraphCON), showing generality beyond a single model.

- **Ablation study on β (Table 4)**. The ablation shows optimal β is dataset-dependent and non-integer for many cases — smaller β (more memory) is beneficial for tree-structured data, larger β for citation networks. This provides concrete evidence that the fractional order introduces a meaningful degree of freedom and that the default β=1 is not optimal for all graph topologies.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison fairness weakens empirical claims.** The paper states (line 309) *"Where available, results from the paper [Chamberlain2021] are used"* for GRAND baselines, and (line 396) *"the results from the original paper are reported"* for CDE baselines. This means the integer-order baselines were not re-run under identical conditions (same data splits, same hyperparameter tuning budget) as the FROND variants. Since β is a tunable hyperparameter for FROND but fixed at 1 for the baseline, FROND benefits from an additional degree of freedom that is searched over during tuning. While FROND strictly generalizes the baseline (β=1 recovers it), the comparison against literature-reported numbers rather than re-tuned baselines means the paper does not cleanly isolate whether the gain comes from the fractional-order dynamics or simply from having an extra tunable parameter. This undermines the central empirical claim of "consistently improved performance" — the improvements could be real, but they are not demonstrated in a controlled apples-to-apples setup. The paper would be strengthened by re-running all baselines under the same tuning budget (same random splits, same hyperparameter search space minus β).

### Minor

- **Theoretical oversmoothing guarantee is proven only for the linear diffusion model (F‑GRAND‑l), but the paper also evaluates nonlinear variants without corresponding theory.** Theorem thm.rate is explicitly derived for the linear case F‑GRAND‑l (Eq. 13) and the random walk interpretation (Section 3.2) is also for the linear diffusion. The paper then reports results for F‑GRAND‑nl (nonlinear attention-based dynamics), F‑CDE, F‑GREAD, and F‑GraphCON — all nonlinear. While the oversmoothing experiment (Figure 2) does compare GRAND‑l vs F‑GRAND‑l (consistent with the theory), there is no theoretical guarantee that the nonlinear variants also benefit from algebraic convergence to stationarity. The paper would benefit from either extending the analysis (e.g., via approximation) or explicitly acknowledging this gap and providing separate empirical evidence.

- **Memory cost of the basic predictor is underdiscussed in the main paper.** The basic predictor solver (used in all main experiments) requires storing all past function evaluations {ℱ(W, X^{(j)})} for each layer k (line 289). This yields O(T²) memory cost in the number of time steps T, compared to O(T) for the integer-order Euler solver. The paper mentions the "short memory principle" and computational complexity analysis in the appendix, but the main paper does not quantify the memory/time overhead or provide a Pareto analysis comparing cost vs. accuracy. For practitioners deciding whether FROND is worth the computational premium, this is relevant information that is deferred rather than presented.

### Trivial
None.

## Nice-to-Haves

- For the graph classification experiments (Table 2/Table graphclas), including GRAND‑nl results alongside GRAND‑l and F‑GRAND‑l would make the comparison more comprehensive.
- The connection between β and fractality of graph datasets is motivating but speculative — measuring fractal dimension of the datasets and correlating with optimal β (as mentioned in the appendix) would strengthen this narrative.
- Directly measuring the convergence rate (‖P(t) − π‖₂ vs. t) on real data and fitting the decay exponent to confirm Θ(t^{−β}) would provide direct empirical validation of Theorem thm.rate beyond the accuracy-vs-depth curves.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Improvements on Cora, Citeseer, Pubmed are small (1–2%)"* — This is an observation, not a weakness. Small improvements on saturated benchmarks are still improvements, and the paper explicitly highlights the larger gains on tree-structured data.
- *"Figure 2 doesn't specify the model variant"* — The main text (lines 390–392) explicitly states the comparison is between GRAND‑l and F‑GRAND‑l, consistent with the theory section.
- *"Proof deferred to appendix"* — Standard practice. The main text states the theorem and provides key equations.
- *"Missing GRAND-nl in graph classification table"* — The table focuses on the controlled comparison (GRAND‑l vs F‑GRAND‑l). The absence of GRAND‑nl is a scope choice, not an error.
- *"Experiments on F-GRAND++, F-GREAD, F-GraphCON relegated to the appendix"* — Standard space-constrained paper organization; the main paper shows representative results (F-GRAND, F-CDE) and references the appendix for completeness.
- *Fractality motivation is speculative* — The paper provides references to the established connection between fractal media and fractional differential equations; this is a motivation, not an empirical claim. The correlation with optimal β is explored in the appendix.
- *"Does not discuss failure cases"* — The F-CDE table shows a tie on Questions (both 75.17, β=1), which is implicitly a failure case where FROND offers no gain. This is present in the data.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface the same central concern (baseline comparison fairness) and recognize the same strengths (algebraic convergence proof, random walk interpretation, extensive experiments). The harsh critic's framing of the baseline issue as potentially "the paper does not demonstrate that FROND's memory mechanism provides a meaningful advantage" is overstated — the ablation on β (Table 4) clearly shows non-integer β ≠ 1 gives better performance than β=1 under the same model (F-GRAND‑l with varying β), which does isolate the benefit of the fractional order. The concern is about comparing F-GRAND against literature-reported GRAND values, not about whether β≠1 helps. The reviews agree that the theoretical contribution is solid and the experimental scope is broad.

## Suggestions

1. **Re-run all integer-order baselines under the same tuning conditions.** Use identical random splits, the same hyperparameter search budget (learning rate, weight decay, hidden dimension, integration time T, etc.), and the same solver for both the baseline and FROND. This is the single most impactful step to strengthen the empirical claims.
2. **Report memory/time cost alongside accuracy for the basic predictor, short-memory variant, and implicit L1 solver.** This would give practitioners a clear accuracy–cost tradeoff.
3. **Acknowledge the theory–experiment gap explicitly.** Add a sentence noting that the algebraic convergence proof applies to the linear case, and that the strong depth-performance of nonlinear variants is empirical.
4. **Consider a small-scale direct verification of the convergence rate.** On a small graph (e.g., Airport), compute the distance from the stationary distribution at each layer and fit the decay exponent to see if it matches Θ(t^{−β}).

## Score and Decision

Originality: High. The use of Caputo fractional derivatives in continuous GNNs and the non-Markovian random walk interpretation are novel. Importance: Good. Oversmoothing is a well-recognized challenge, and the formal algebraic convergence proof is a genuine theoretical advance. Claims: The theoretical claims are well-supported; the empirical claims are partially supported but weakened by the baseline comparison methodology. Soundness: The core theory is sound; experiments are extensive but comparison fairness needs attention. Clarity: Well-written and clearly structured. Value: The framework provides a principled new direction for continuous GNNs and the theoretical analysis is a meaningful contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>