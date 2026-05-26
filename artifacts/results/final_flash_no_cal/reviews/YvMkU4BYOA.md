Now I have a comprehensive understanding of the paper. Let me write the consolidated review.

## Summary

XBIC augments the BIC score for discrete Bayesian network discovery by soft-weighting its complexity penalty with edge-specific Shapley values from per-node XGBoost classifiers. The idea is that when a candidate parent contributes strongly to predicting its child, the penalty on that edge is reduced, helping hill-climbing prefer orientations within Markov-equivalence classes. Evaluated on 10 benchmark networks (6–76 nodes) across 7 sample-size regimes (700 runs), XBIC achieves a +5.6% relative F₁ improvement over hill-climbing BIC and larger gains over PC and GES, at a substantial computational cost.

## Strengths

1. **Novel integration of Shapley values into score-based discrete causal discovery.** To the best of the authors' knowledge (and plausibly), this is the first method that directly incorporates *local* feature attributions as an edge-specific, directional modulation of a score-based objective (BIC) for purely discrete data. This cross-pollination of explainability and causal discovery is creative and underexplored.

2. **Thorough and systematic empirical evaluation.** The evaluation spans 10 networks (6–76 nodes), 7 sample-size regimes (0.125M² to 8M²), and 10 repetitions each — 700 runs in total. Table 1 provides detailed network metadata. Results are reported per (network, sample-size) combination in Table 2, and all three hyperparameter settings (w=1,2,3) are shown. This level of breadth and documentation exceeds the typical scope in the discrete causal discovery literature.

3. **Clean, interpretable improvement over BIC-HC.** The comparison to hill-climbing BIC is apples-to-apples (same search procedure, same scoring framework, only the penalty is modified). The +5.6% relative F₁ gain (+0.04 absolute, Table 4) is a measurable improvement on a well-established baseline without changing the search algorithm. This part of the evaluation is not affected by the protocol issues that complicate the PC/GES comparisons.

4. **Preserves BIC's large-sample consistency and degrades gracefully.** The penalty still scales as O(log N), and when the Shapley signal is absent (confidence filter yields few instances), SHAP(G) → 0 and XBIC approaches BIC. This theoretical safeguard means the method cannot catastrophically fail compared to BIC in low-data regimes.

## Weaknesses

### Fatal

None. The paper's core claim is not theoretically impossible — the method compares Shapley values derived from *different* conditional distributions (P(X_i|X_{\i}) vs. P(X_j|X_{\j})), so asymmetry is possible even asymptotically. The fundamental weakness is insufficient justification, not impossibility.

### Major

1. **No theoretical rationale for why Shapley asymmetry encodes causal direction.** This is the paper's most significant gap. The method asserts that |φ̄_{j→i}| > |φ̄_{i→j}| should favor the orientation j→i, but offers no explanation for why this holds, nor any connection to known asymmetry principles (e.g., independence of cause and mechanism, or the complexity asymmetry exploited by additive-noise-based methods). The consistency remark only addresses the penalty order, not whether the Shapley-weighted score is consistent for the *true* DAG within an equivalence class. The paper candidly lists "formal analysis" as future work, but this means the central mechanism is presented as a heuristic — which conflicts with the "principled" framing in the abstract and introduction. Without some justification, the reader cannot distinguish a genuine signal from an artifact of XGBoost's inductive bias or the specific regularization choices.

2. **Biased comparison with PC and GES.** The evaluation protocol completes PDAGs/CPDAGs (from PC and GES) to DAGs by *randomly orienting undirected edges* before computing directed-edge metrics (Section 4.1). This systematically penalizes these baselines for edges they correctly leave undirected — exactly the edges whose direction is not identifiable from observational data. The reported 20.9% improvement over PC and 9.6% over GES are therefore unreliable and likely inflated. The comparison against BIC-HC (5.6%) is not affected by this issue and should be treated as the primary result.

3. **Unfavorable cost-benefit ratio for practitioners.** The absolute F₁ improvement over BIC is +0.04 on a [0,1] scale (Table 4), while runtime increases by factors of 28–192× (Table 5: e.g., Asia: 0.4s→75s, 192×; Alarm: 9.3s→524s, 56×; Win95pts: 75s→2139s, 28×). Many Table 2 entries show zero or negative F₁ deltas, especially for smaller networks and sample sizes. The practical appeal — paying a 1–2 order-of-magnitude runtime premium for a small F₁ bump that is not guaranteed in all settings — is limited. The paper acknowledges the cost but the central claim of practical value remains weakened by this trade-off.

### Minor

4. **The confidence threshold τ is not reported explicitly.** The paper states it is "fixed" and that varying it between 0.7–0.95 changed F₁ by <1% (Section 4.1), but the actual value used in the main experiments is not given. This is a mild reproducibility gap.

5. **Hyperparameter w is evaluated without validation-set separation.** The weight w is swept over {1, 2, 3} and w=2 is presented as the best (Table 4). While all three values are reported transparently, emphasizing w=2 as "strongest overall" without a cross-validation or holdout selection procedure constitutes mild indirect test-set tuning.

6. **Exponential weighting form is not justified.** Equation (2) uses exp(w·SHAP(G)) in the denominator, which can cause the penalty to nearly vanish for moderate w·SHAP(G). No rationale is given for why exponential weighting is preferable to linear, sigmoid, or thresholded alternatives, nor are the implications for overfitting discussed (e.g., a near-zero penalty could admit spurious edges with moderate Shapley support).

7. **Sign of Shapley values is discarded without justification.** Equation (3) sums absolute values |φ̄_{j→i}|. Negative Shapley values indicate the feature pushes the prediction *away* from the observed class, which could encode a different type of directional signal. The paper does not discuss whether preserving sign information would help or hurt.

8. **"Consistent gains" framing overstates the results.** Table 2 shows many zero or negative entries: 13 out of 70 BIC-HC deltas are ≤0; the Water network shows near-zero deltas across all sample sizes; Win95pts and Hepar2 show negative deltas at larger samples. The improvement is not universal and is concentrated in medium-to-large networks with sufficient data.

### Trivial

9. **"Reverts to standard BIC" is slightly imprecise.** XBIC only equals BIC exactly when SHAP(G)=0. When Shapley values are small but non-zero, the penalty is slightly reduced; the method does not truly "revert" but merely approaches BIC. This is a small semantic gap between the framing and the math.

## Nice-to-Haves

- **Ablation with a symmetric association baseline.** Replace |φ̄_{j→i}| with a symmetric measure (e.g., mutual information) in the same weighting scheme to isolate whether the *directional* information in Shapley values adds value over a generic penalty reduction on strongly associated edges.
- **CPDAG-level metrics for PC/GES.** Evaluate at the level of the completed PDAG (e.g., structural Hamming distance on the CPDAG) to separate skeleton recovery from orientation accuracy, removing the random-orientation artifact.
- **Orientation accuracy conditioned on the true skeleton.** Report precision/recall for direction assignment *among edges present in the ground-truth skeleton* to isolate orientation gains from changes in recall.
- **Explicit statement of the τ value used** and a sensitivity analysis over a wider range.

## Removed Points

These points from the inputs were evaluated and removed under the filtering rules, with justification:

- **Critic's claim that the method "cannot, in principle, produce a consistent directional preference" (Critical Issue 1, central argument).** This is not factually supportable. The Shapley values for j→i and i→j are derived from *different* conditional distributions (P(X_i|X_{\i}) vs. P(X_j|X_{\j})), so asymmetry is possible even in the infinite-sample limit. The critic's argument conflates "conditional distributions are invariant within an equivalence class" (true) with "the two Shapley values are functions of the same conditional" (false). The valid gap is lack of *theoretical justification* for why the asymmetry aligns with causality — which is a Major weakness, not a fatal impossibility.
- **Claims that the "drop-in upgrade" framing is inaccurate.** The preprocessing is front-loaded and substantial, but the scoring function *is* a drop-in replacement within the search loop. Reasonable people can disagree on this wording; it is not a substantive flaw.
- **Formatting/style nitpicks and speculation about missing appendix content.** These reflect the PDF extraction process, not the paper.
- **Critic's claim that the SHD comparison with GES suffers from selection bias (Section 4.5).** The paper transparently acknowledges this filtering and explicitly states it is favorable to GES, so the criticism is already addressed.
- **Strength finder's claim that improvements are "consistent."** Overridden by verified evidence (Table 2 shows many zero/negative deltas).
- **Strength finder's "principled" characterization.** Overridden by the verified weakness that the method lacks theoretical justification.

## Novel Insights

The most interesting question surfaced by the review process is whether the observed Shapley-based orientation signal is genuinely causal or an artifact of the XGBoost inductive bias on discrete data. The fact that the method shows *any* improvement over BIC — however modest — on an apples-to-apples comparison within the same search framework suggests there is a real signal worth understanding. If the effect can be traced to a specific property of the data (e.g., that the correct causal direction yields a simpler functional mapping that tree models exploit), this would be a genuinely novel connection between model interpretability and causal structure learning. The paper would be substantially strengthened by providing a synthetic experiment that isolates and demonstrates this mechanism.

## Suggestions

1. **Provide a testable rationale for the Shapley–causality link.** Even without a full proof, a controlled simulation or a connection to the known complexity-asymmetry phenomenon in regression-based causal discovery would greatly strengthen the paper. Show, for example, that in a ground-truth discrete additive noise model, the parent's Shapley value systematically exceeds the child's.
2. **Fix the PC/GES evaluation protocol.** Use CPDAG-level metrics (e.g., SHD on the completed PDAG), or alternatively orient undirected edges via the same BIC score that XBIC uses, rather than randomly.
3. **State the exact τ value used** and consider reporting results averaged over a range of τ values.
4. **Add the symmetric-baseline ablation** (mutual information or correlation) to show that the directional information in Shapley values, not just the penalty reduction on strong associations, drives the improvement.
5. **Include validation-set-based selection of w** or report sensitivity across w without claiming a single best value.
6. **Tone down the "principled" and "consistent" language** to more accurately reflect the heuristic nature of the contribution and the variability in results.

## Score and Decision

The paper presents a novel and potentially fruitful idea — using Shapley values to inform score-based causal discovery on discrete data — supported by a thorough evaluation on the BIC baseline. However, the lack of theoretical justification for the core mechanism, the biased PC/GES evaluation protocol, and the modest absolute gains at extreme computational cost significantly limit the paper's impact in its current form. The BIC-HC result (the cleanest comparison) shows a real but small improvement. With major revisions addressing the theoretical gap and the evaluation issues, the paper could make a meaningful contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>