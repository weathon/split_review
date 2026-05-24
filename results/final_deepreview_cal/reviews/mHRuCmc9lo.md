Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

This paper introduces a robust decision-making framework for acting on forecasts that satisfy partial (\(\mathcal{H}\)-)calibration constraints — a relaxation of full calibration that is more tractable in high dimensions. The central contributions are: (1) a duality-based characterization of the minimax-optimal decision policy for any finite \(\mathcal{H}\) (Theorem 3.1), and (2) the discovery of a sharp transition: once \(\mathcal{H}\) contains the decision-calibration indicators (only \(|\mathcal{A}|\) test functions), the optimal robust rule collapses to the plug-in best response (Theorems 4.1–4.2). This means a decision-maker who can request decision-calibrated forecasts can simply best-respond to predictions and achieve minimax optimality without full calibration. The paper also derives practical robust policies from structural properties of standard training pipelines (self-orthogonality under squared loss, bin-wise calibration) and provides proof-of-concept experiments on two regression datasets.

## Strengths

- **Sharp theoretical insight on decision calibration.** Theorems 4.1–4.2 establish that when the test class \(\mathcal{H}\) contains the decision-calibration indicators \(\{\mathbf{1}_{R_a}\}_{a \in \mathcal{A}}\), the adversarial tilt disappears (\(q^*(v) = v\) a.e.) and the robust rule collapses to the plug-in best response. This upgrades decision calibration from a swap-regret guarantee (prior work) to full minimax optimality — a crisp, clean result that substantially refines our understanding of what calibration guarantees are sufficient for trustworthy decision-making.

- **Duality characterization yields computable policies.** Theorem 3.1 provides a finite-dimensional dual formulation reducing the minimax problem to concave maximization over multipliers and pointwise convex minimization. The resulting two-step procedure (compute adversarial belief, then best-respond) is practical and can be solved with standard convex optimization methods.

- **Practical "free" calibration structure from standard training.** Proposition 4.4 proves that any model with a linear last layer trained to a first-order stationary point of squared loss automatically satisfies self-orthogonality (\(\mathbb{E}[f(X)(Y-f(X))] = 0\)), giving practitioners an \(\mathcal{H}\)-calibration guarantee without algorithmic intervention. Proposition 4.5 derives an elegant closed-form robust policy under bin-wise calibration.

- **Experiments validate theoretical predictions.** Table 1 confirms that the robust policy outperforms the plug-in best response under adversarial distribution shifts that respect the calibration constraints, while incurring only mild cost under i.i.d. evaluation — consistent with the saddle-point property predicted by theory.

- **Well-scoped and honest about limitations.** The paper clearly acknowledges the linearity assumption on utility, the focus on exact calibration (with approximate calibration deferred to the appendix), and the finite action set. These are stated upfront and do not overclaim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No empirical measurement of calibration error.** The experiments rely on the self-orthogonality property holding approximately for the trained MLP, but the paper never quantifies how closely \(\mathbb{E}[f(X)(Y - f(X))] \approx 0\) holds in practice. This matters for interpreting whether observed robust gains stem from genuine calibration gaps or from sampling noise alone. A brief quantification would strengthen confidence in the experimental results.

- **Limited experimental scope.** The evaluation uses two datasets and a single utility parameterization. While this is acceptable for a theory paper and the results align with theoretical predictions, broader validation — even a brief discussion of robustness to alternative utility specifications — would increase confidence in the generality of the practical benefit. The paper is appropriately honest about its scope.

### Trivial

- Table 1 reports mean utilities without standard errors or confidence intervals, making it difficult to assess the statistical significance of the reported differences. The qualitative trends are consistent with theory, but including variability estimates would complete the picture.

## Nice-to-Haves

- A sketch in the main body of how *approximate* decision calibration yields near-optimality of the plug-in rule, with explicit bounds on the increase in worst-case regret when \(\mathcal{H}\) is only approximately satisfied (e.g., \(|\mathbb{E}[h(f(X))(Y - f(X))]| \leq \epsilon\)). This would connect the sharp transition more directly to realizable guarantees from known post-processing algorithms.

- A brief concrete example contrasting what minimax optimality buys over swap-regret guarantees (Zhao et al., 2021; Noarov et al., 2023) could sharpen the exposition for readers less familiar with the distinction.

## Removed Points

These points were flagged for removal; treat them with caution.

- *"The appendix is stated to contain a discussion of approximate calibration, though I cannot inspect it here"* — The appendix was stripped by the parser; the paper explicitly references Appendix B for approximate calibration. This is not a weakness of the paper.
- *"The paper does not detail the conditions under which a saddle point is guaranteed (e.g., compactness, convexity, minimax theorem)"* — The problem is cast in terms of finite-dimensional dual variables and a convex inner minimization, making existence credible. The harsh critic themselves note this. Demoted from a concern to a removed point.
- *Generic suggestions about "more datasets" and "alternative utility functions"* — These are scope-creep for a theory paper and were demoted. The paper is honest about its scope.
- *"The regret-based guarantees in prior work are mentioned, but a brief example... could sharpen the exposition"* — This is a presentation preference, not a weakness. Moved to Nice-to-Haves.

## Novel Insights

The paper's most distinctive contribution is the identification of a *sharp threshold* rather than a gradual transition: decision calibration (only \(|\mathcal{A}|\) test functions) suffices to collapse the entire hierarchy of minimax-optimal policies to the plug-in best response. This is surprising because prior work only established swap-regret guarantees for decision calibration — a qualitatively weaker property. The paper's minimax lens reveals that decision calibration is, in a precise sense, *complete*: once you have it, adding more calibration constraints buys you nothing further for downstream decision-making. This reframes decision calibration as a natural and sufficient target for forecaster design and post-processing, with practical consequences (Corollary 4.3 on simultaneous optimality across multiple decision problems).

## Suggestions

- Report the empirical self-orthogonality residual \(\mathbb{E}[f(X)(Y - f(X))]\) on the test/calibration split to give the reader a concrete sense of how closely the theoretical condition is met.
- Add standard errors to Table 1.
- Consider including a sentence or short paragraph in Section 4 sketching the extension to approximate decision calibration, even if the full treatment remains in the appendix, to make the practical relevance of the sharp transition more immediately apparent.

---

**Originality:** High. The minimax robust-decision lens on \(\mathcal{H}\)-calibration is novel, and the sharp transition at decision calibration is a genuinely new insight.

**Importance of research question:** High. Making high-dimensional predictions trustworthy for downstream decisions is a central challenge in ML deployment. The paper provides clear, actionable guidance.

**Claims well supported:** Yes. Theorems are stated clearly with proof sketches; experiments are consistent with theoretical predictions; limitations are acknowledged.

**Soundness of experiments:** Adequate for a theory paper — the experiments faithfully test the theoretical predictions, though they could be broader.

**Clarity of writing:** High. The exposition is well-structured, notation is clear, and the core ideas are communicated effectively.

**Value to the research community:** Significant. The paper bridges calibration theory and robust decision-making, and the decision-calibration threshold result will influence how practitioners and researchers think about calibration requirements.

## Score and Decision

**Round-1 bracket:** Based on the initial calibration search, the paper plausibly sits between 5.5 and 7.5. The weak-band anchors (avg 1.50–3.40) are clearly below this paper; the strong-band anchors (avg 8.00) are clearly above it.

**Round-2 narrowing:** Compared to the round-2 anchors:

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| dNunnVB4W6 (Calibrating Expressions of Certainty) | 6.25 | R2 | Our paper has deeper theory and a cleaner, more general contribution |
| iOMnn1hSBO (Decision-Focused UQ) | 6.80 | R2 | Comparable — both integrate decision-making with uncertainty; our paper's theoretical insight is more elegant |
| TId1SHe8JG (Higher-Order Calibration) | 7.50 | R2 | Slightly above us — has more comprehensive theoretical results (necessary and sufficient conditions) and broader experiments |
| g6fYDGKeyB (SBI Misspecification) | 6.00 | R1 | Our paper is clearly stronger theoretically |
| M1y9JAL7CP (Policy Gradient for MDPs) | 6.50 | R1 | Our paper has a cleaner, more impactful theoretical contribution |
| TTrzgEZt9s (DRO with Bias/Variance Reduction) | 8.00 | R1 | Above us — stronger empirical results and algorithmic contribution |
| A3YUPeJTNR (Hidden Cost of Waiting) | 8.00 | R1 | Above us — broader scope and richer modeling |

The paper sits between iOMnn1hSBO (6.80) and TId1SHe8JG (7.50), closer to the latter in theoretical elegance but with lighter empirical validation. A score of **7.0** reflects its strong theoretical contribution with modest but adequate experiments.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>