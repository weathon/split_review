Now I have a thorough understanding of the paper and can write the final consolidated review.

## Summary

This paper introduces XBIC, a score-based causal discovery method for discrete Bayesian networks that augments the BIC score with edge-specific Shapley evidence. For each ordered pair (j,i), XBIC computes the mean absolute Shapley value of variable X_j when predicting X_i, then uses the sum of these values over a candidate DAG's edges to softly reduce the complexity penalty — edges with strong asymmetric predictive support get less penalized. The method defaults to standard BIC when directional signal is weak. Extensive experiments on 10 benchmark discrete networks (6–76 nodes) across 7 sample-size regimes (700 runs) show consistent improvements in oriented-edge F₁: +5.6% over BIC-HC, +9.6% over GES, and +20.9% over PC, with statistical significance testing.

## Strengths

1. **Clean, principled integration of Shapley evidence into BIC.** Equation (2) defines XBIC as a simple drop-in modification that reduces the complexity penalty by exp(w·SHAP(G)). When SHAP(G)=0 or w=0, XBIC reduces exactly to standard BIC. This is a theoretically clean design that preserves BIC's familiar framework and asymptotic properties.

2. **Consistent empirical gains across diverse discrete networks.** Table 4 aggregates results from 700 runs showing that XBIC (w=2) improves oriented-edge F₁ by 5.6% relative to BIC-HC, with similarly consistent gains over PC and GES. These gains are supported by adjusted Friedman tests (p<0.05) and Wilcoxon signed-rank tests, providing evidence that the improvements are not due to chance.

3. **Meaningfully addresses a challenging domain.** Discrete Bayesian network structure learning has received less attention than continuous settings, yet is critical for domains like healthcare and survey analysis. The paper tackles the real problem of orienting edges within Markov equivalence classes using a novel source of signal (predictive Shapley attributions) rather than relying on stronger parametric assumptions.

4. **Robustness analysis for design choices.** The paper reports that varying the confidence threshold τ between 0.7 and 0.95 changes downstream F₁ by <1% on average, demonstrating that the filtering mechanism is robust. The explicit algorithm description (Algorithm 1) and hyperparameter search space (Table 3) aid reproducibility.

## Weaknesses

### Major

1. **Baseline evaluation for PC and GES uses random orientation of undirected edges, likely inflating headline improvements.** Section 4.1 states: "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." When PC or GES correctly leaves an edge undirected (because its direction cannot be determined from observational data alone), random orientation will produce the wrong direction ~50% of the time, systematically lowering the baseline's directed-edge F₁. The reported 20.9% improvement over PC is therefore partially an artifact. The paper neither discusses this issue nor provides bounds or sensitivity analysis. **Why it matters:** The headline improvement over PC is the largest claimed gain; if substantially inflated, the paper's strongest numerical result is undermined. The BIC-HC comparison (5.6% relative / 0.04 absolute) is unaffected and provides a cleaner evaluation.

2. **No CPDAG-level metrics reported for PC or GES.** The standard evaluation for methods that return PDAGs/CPDAGs uses metrics like SHD to the true CPDAG, which do not penalize legitimately undirected edges. The paper defines SHD as a metric but only reports it for the GES comparison (Section 4.5). Reporting SHD to the CPDAG for PC and GES would provide a fair comparison that does not conflate genuine orientation ability with random orientation noise. **Why it matters:** Without this, the reader cannot assess whether XBIC truly improves orientation within Markov equivalence classes or simply benefits from including more edges through penalty reduction.

### Minor

3. **The evaluation does not isolate orientation from edge discovery.** The paper's central motivation is resolving Markov-equivalence ambiguities (mediator vs. confounder). However, the reported metrics conflate edge discovery with orientation. Since XBIC reduces the complexity penalty, it tends to include more edges (higher recall, as shown in Figure 2). It is plausible that some of the F₁ gains come from discovering true edges that BIC's harsher penalty missed, rather than from correctly orienting edges that both methods include in the skeleton. A targeted evaluation — e.g., measuring orientation accuracy conditional on the correct skeleton, or testing on synthetic mediator/confounder motifs — would strengthen the central claim.

4. **Computational cost is 10–100× higher than BIC for modest gains.** Table 5 shows XBIC (w=2) takes 2139s on Win95pts vs. 75s for BIC (28× slower). The absolute F₁ improvement over BIC is 0.04. While the paper acknowledges this cost and discusses parallelization, the practical significance of such expensive computation for a 4-point absolute F₁ gain is unclear, especially since the method provides little benefit in small-sample regimes where structure learning is hardest.

5. **No analysis of whether signed Shapley values carry useful directional information.** The paper uses absolute Shapley values in Equation (3) without discussing whether the sign carries directional signal. While the asymmetry in magnitudes across opposite directions (|Φ̄_{j→i}| vs. |Φ̄_{i→j}|) provides the directional signal, the paper never examines whether incorporating sign information or using signed Shapley values would improve performance. This omission leaves an unresolved design question.

6. **GES comparison may favor XBIC due to selective retention.** Section 4.5 retains only (network, sample-size) pairs where GES completed within 7 days. This subset is not random — GES systematically failed on larger/denser networks. While XBIC is compared head-to-head on the same retained runs, the reported SHD reductions of 6–32% may not generalize to settings where GES is computationally feasible.

### Trivial

None.

## Nice-to-Haves

- A synthetic experiment on simple causal motifs (mediator X→Y→Z vs. confounder X←Y→Z) that directly tests whether XBIC prefers the correct DAG over the alternative within the equivalence class.
- A sensitivity analysis for the random baseline orientation: report variance over multiple random completions, or compare using CPDAG-level metrics as the primary evaluation.
- A broader sweep of w (including fractional values <1) to characterize the behavior near w=0 more precisely.

## Removed Points

The following points from the inputs were removed with justification:

- **Harsh Critic Issue 1 (absolute Shapley values prevent directional signal):** This criticism misunderstands the paper. The directional signal comes from asymmetry in the *magnitudes* across opposite ordered pairs: |Φ̄_{j→i}| vs. |Φ̄_{i→j}|. When the true direction is X→Y, X is typically a stronger predictor of Y than vice versa, yielding |Φ̄_{X→Y}| ≫ |Φ̄_{Y→X}| and thus a larger penalty reduction for the correct orientation. The absolute value does not discard this directional information because Φ̄_{j→i} and Φ̄_{i→j} are independently computed quantities. The paper's statement in Section 3.2 — "if |Φ̄_{1→2}| ≫ |Φ̄_{2→1}|, the edge X₁→X₂ has stronger directional support" — is correct.

- **Harsh Critic Issue 4 (theoretical gap about why predictive Shapley carries direction):** A fair question, but the paper provides extensive empirical evidence (700 runs across 10 networks) that the approach works. The absence of a formal theoretical justification is not a flaw — many empirical contributions in causal discovery operate without full theory. The paper acknowledges this as future work.

- **Strength Finder's "principled integration" overstated:** While the clean reduction to BIC is a nice property, the integration is straightforward algebraically. This is kept but downgraded from "core strength" framing.

- **Strength Finder's "honest runtime reporting":** This is standard practice, not a distinctive strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the PC/GES baseline evaluation.** Replace the random orientation of undirected edges with CPDAG-level metrics (SHD to the true CPDAG) or, at minimum, report F₁ with error bars over multiple random completions and include a discussion of how this affects comparisons. This is the single most impactful fix.

2. **Add an ablation that isolates orientation effects.** Generate synthetic data from simple 3-node motifs (mediator vs. confounder, and a fork vs. chain structure) and measure how often XBIC selects the correct DAG over the Markov-equivalent alternative. This would directly validate the paper's central claim of resolving equivalence-class ambiguities.

3. **Report signed-Shapley versions as a secondary analysis.** Add a comparison variant that uses Σ sign(Φ̄_{j→i})·|Φ̄_{j→i}| or a softmax over both directions, and show whether it improves or degrades performance relative to the absolute-value baseline.

## Calibration Report

**Round 1 (Bracketing):** Queried for score-based BN structure learning papers (score < 3.5), causal discovery with Shapley/XAI (3.5–7.5), and BIC score augmentation ( > 7.5). Topical similarity was moderate; initial bracket estimated at 4.0–5.5.

**Round 2 (Narrowing):** Queried for discrete BN causal discovery benchmarks (3.5–5.5) and BIC-based structure learning evaluation (4.0–6.0). Examined anchors:
- *FLOP (Embracing Discrete Search)* [id: lejOV6j3cj, 5.00, Accept]: Stronger algorithmic innovation (orders-of-magnitude speedup), cleaner evaluation, but limited to linear Gaussian models. XBIC is slightly weaker due to modest improvements and evaluation issues, but tackles the harder discrete setting.
- *Top-K Structure Search* [id: FNA0AlYBMS, 4.50, Reject]: Similar BIC-based approach with synthetic + Sachs evaluation, but limited to linear models and modest novelty. XBIC has a more original contribution and broader evaluation.
- *Score-based Greedy Search for Partially Observed Models* [id: BNHplerBYE, 5.33, Accept]: Stronger theoretical contributions (identifiability guarantees) but narrower empirical scope. XBIC has more extensive experiments.

**Final Position:** XBIC is stronger than Top-K (4.50) due to originality and experimental scope, but weaker than FLOP (5.00) due to evaluation issues and more modest results. Score of **4.5** reflects a borderline paper with a genuinely novel idea and extensive experiments, but with evaluation issues (PC baseline) that need resolution before it can be considered a clear accept.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>