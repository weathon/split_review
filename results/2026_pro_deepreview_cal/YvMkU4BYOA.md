Now I have a thorough calibration picture. Let me compile my final review.

---

## Summary

XBIC proposes augmenting the BIC score for discrete causal discovery with edge-specific directional evidence derived from Shapley values. For each variable, an XGBoost classifier predicts it from all others; TreeExplainer SHAP values are aggregated across confident predictions to produce directional weights. These weights modulate BIC's complexity penalty — edges with strong directional support are penalized less — helping resolve Markov equivalence class ambiguities. The method is evaluated across 10 benchmark discrete Bayesian networks, 7 sample-size regimes, and 700 total runs, showing modest but consistent improvements in oriented-edge F₁ over BIC hill-climbing (+5.6% relative, ~0.04 absolute), PC (+20.9%), and GES (+9.6%).

## Strengths

- **Genuinely novel integration of Shapley evidence into score-based causal discovery.** Rather than using causal knowledge to constrain explanations (the standard direction), XBIC uses feature attributions to inform structure learning. The idea of soft-weighting BIC's penalty term with edge-specific directional signal is creative and, to the authors' knowledge, the first such approach for discrete data (Section 2.3, Equation 2).

- **Extensive and well-structured empirical evaluation.** Ten benchmark networks (6–76 nodes) × 7 sample-size regimes × 10 repetitions = 700 runs, compared against three baselines (BIC-HC, PC, GES). The per-network deltas in Table 2 and aggregate summary in Table 4 provide a transparent view of where the method helps and where it doesn't.

- **Graceful fallback to standard BIC.** When the Shapley signal is weak (w = 0 or SHAP(G) = 0), XBIC reduces exactly to BIC. This is confirmed empirically: on small samples, XBIC often delivers zero delta (Table 2, 0.125 M² column), indicating it does not degrade results when the attribution pipeline lacks confident predictions.

- **Robustness to the confidence threshold τ.** Varying τ from 0.7 to 0.95 changes downstream F₁ by <1% (Section 4.1), suggesting the method is not brittle to this hyperparameter.

- **Reproducibility commitment.** Code, data splits, and scripts are released at an anonymized repository.

## Weaknesses

### Fatal

None.

### Major

- **In-sample Shapley computation without discussion of implications.** Algorithm 1 (Section 3.2) trains XGBoost classifiers on the full dataset and then computes TreeExplainer SHAP values on those same training instances (filtered by the confidence threshold τ). Because the model has already seen these instances, the attributions may reflect overfit patterns rather than genuine conditional dependencies. The paper has mitigating factors — the confidence filter discards low-certainty predictions, SHAP values from regularized tree ensembles are not maximally overfit, and the method gracefully falls back to BIC when signal is weak — but the absence of any discussion of this issue is a significant gap. An out-of-sample or cross-validated SHAP scheme (e.g., computing attributions only from fold-held-out models) would substantially strengthen the validity of the central empirical claim. In its current form, the reader cannot assess how much of the observed gain is attributable to in-sample signal inflation versus genuine directional evidence.

### Minor

- **Limited statistical reporting.** Table 4 gives absolute F₁ deltas (e.g., +0.04 over BIC) but the absolute baseline F₁ scores are never reported, making it difficult to contextualize the gains (is BIC-HC achieving 0.30 F₁ or 0.70 F₁?). The paper mentions a Friedman test with p < 0.05 followed by Wilcoxon signed-rank tests (Section 4.3) but provides no specific p-values, test statistics, or multiple-comparison correction details. Error bars in Figure 2 cover only 3 of the 10 networks. This makes it harder to assess whether the observed improvements are statistically stable.

- **Heuristic theoretical basis.** The exponential form of the penalty modifier, exp(w · SHAP(G)), is not derived from any principle — it is an ad-hoc re-weighting. The "consistency remark" (Section 3.3) only shows the penalty remains O(log N), which is a minimal property that many alternative functional forms would also satisfy. The paper acknowledges this gap in the limitations section ("formal analysis of the weighting mechanism... is an important direction"), but the abstract's description of a "principled enhancement" overstates the current theoretical support.

- **Underspecified BIC hill-climbing baseline.** The starting graph (empty DAG or other), tie-breaking rule, and whether random restarts are used are not described (Section 4.1). These choices influence which DAG within an equivalence class is returned and therefore affect the baseline's oriented-edge performance that XBIC is compared against.

- **Hyperparameter w selected on test data.** The paper sweeps w ∈ {1, 2, 3} and reports w = 2 as best (Table 4), but no validation procedure (e.g., held-out networks or cross-validation) is described. This raises the possibility that the reported gains are optimistically tuned to the test set.

- **GES comparison on a filtered subset.** GES failed to complete within 7 days on many settings (Table 2, "-" entries). The paper acknowledges this and compares XBIC against GES only on the subset where both completed (Section 4.5), but then draws aggregate conclusions (e.g., +9.6% over GES in Table 4) that may be optimistic since they exclude the hardest instances where GES timed out.

### Trivial

- The fixed confidence threshold τ used in the main experiments is not explicitly stated in the main text; only the sensitivity range (0.7–0.95) is given (Section 4.1).

## Nice-to-Haves

- An ablation replacing the Shapley-derived weights with random noise (preserving the same penalty-scaling mechanism) would help rule out the possibility that any flexible penalty modulation — not specifically the Shapley signal — drives the improvements.
- A per-edge diagnostic showing the correlation between Shapley asymmetry |φ̄_{j→i}| − |φ̄_{i→j}| and ground-truth direction would make the method's mechanism more transparent.
- Cross-validated SHAP computation would address the most significant methodological concern.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"The in-sample issue invalidates the current experimental results" (Harsh Critic → demoted from Fatal to Major).** The claim of invalidation is too strong. The SHAP values serve as a soft directional signal rather than for formal statistical inference; the method has mitigating factors (confidence filter, CV regularization, graceful fallback); and the small-sample results showing zero delta are inconsistent with severe overfitting-driven inflation. The concern is real and important but not fatal.

- **"The design is essentially a heuristic; the absence of analysis leaves unclear when the approach will help and when it might backfire (e.g., driving the search toward over-dense graphs)."** The claim about over-dense graphs is speculative and not supported by the paper's results — Figure 2 shows that even at w = 3, precision does not collapse, and the paper explicitly reports the precision-recall trade-off.

- **"No p-values, effect sizes, or details of the multiple-comparison correction are provided."** The paper does mention p < 0.05 and Wilcoxon tests; specific p-values and effect sizes would strengthen the reporting but their absence does not constitute a complete evidential gap. Demoted from major to minor.

- **Missing appendix, missing proofs, missing references concerns.** These are parser artifacts; the original submission includes these sections.

## Novel Insights

The paper identifies a reversal of the standard causality–XAI relationship: rather than using known causal structure to produce better explanations, it uses model explanations (Shapley values from per-node classifiers) to recover causal structure. This framing — that predictive importance asymmetries can serve as directional evidence within equivalence classes — is a genuinely fresh perspective. The empirical finding that this signal is robust enough to improve oriented-edge recovery across diverse discrete networks, despite the method's simplicity and heuristic form, suggests that local feature attributions carry more causal information than is commonly assumed.

## Suggestions

- **Highest priority:** Implement a cross-validated SHAP scheme (train on folds, compute attributions only on held-out instances) and report whether the gains persist. This would directly address the most significant validity concern.
- Report absolute baseline F₁ scores alongside the deltas in Tables 2 and 4, and include per-network standard deviations or distributions to allow readers to assess stability.
- Report exact p-values and effect sizes for the statistical tests, and specify the multiple-comparison correction method.
- Describe BIC-HC initialization, tie-breaking, and restart policy explicitly.
- Either use a held-out validation procedure for selecting w or report results for all w values without selecting a "best."

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| JzFLBOFMZ2 (LLM-supervised CSL) | 3.20 | R1 | XBIC is clearly stronger: more rigorous evaluation, cleaner methodology |
| eqQFBnjjPP (ExDBN) | 4.00 | R1 | XBIC has better novelty, broader evaluation, clearer presentation |
| DUfwD5yiN4 (Distributed BN) | 5.25 | R1 | XBIC has weaker theory but stronger empirical evaluation; comparable overall |
| lnMQGBHYRt (do-SHAP) | 5.33 | R2 | Both at causality-XAI intersection; XBIC has much broader experiments |
| HBf6HFnpmH (Manufacturing benchmark) | 5.50 | R2 | XBIC has clearer scientific contribution and better execution |
| ZXs3pkmrRG (TICL) | 5.50 | R2 | Comparable bnlearn-based evaluation; XBIC has more novel core idea but weaker theory |
| 3n6DYH3cIP (Extendable BN) | 5.60 | R1 | Both have novel ideas; Extendable BN has stronger theoretical guarantees; XBIC weaker on theory but comparable on empirics |
| xByvdb3DCm (Selection+Intervention) | 8.00 | R1 | Clearly stronger than XBIC in theoretical depth and significance |

**Round-1 bracket:** 4.0–6.0 (between ExDBN at 4.0 and the extendable BN / TICL cluster at ~5.5–5.6).

**Round-2 narrowing:** The paper is clearly stronger than do-SHAP (5.33) in empirical breadth and presentation, comparable to the manufacturing benchmark (5.50) and TICL (5.50) in overall contribution quality, but weaker than the extendable BN paper (5.60, accepted) in theoretical grounding. The in-sample SHAP issue and modest absolute gains pull the score below the 5.50 cluster.

**Final score: 5.0.** This reflects a paper with a genuinely novel idea and solid empirical execution, held back by a significant methodological concern (in-sample SHAP computation without discussion), limited theoretical grounding, and modest absolute performance gains. It is a borderline submission that could be strengthened to clear acceptance with a revised evaluation pipeline and more complete reporting.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>