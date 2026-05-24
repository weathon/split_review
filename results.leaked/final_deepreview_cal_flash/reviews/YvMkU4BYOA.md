Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

The paper proposes XBIC, a method that enhances BIC-based score causal discovery for discrete data by soft-weighting the complexity penalty with Shapley values from per-node classifiers. Edges with strong directional support from feature attributions incur a reduced penalty, while weak support preserves the standard BIC. The method is evaluated on ten benchmark Bayesian networks across seven sample sizes (700 runs), reporting relative F₁ improvements of 5.6% over BIC-HC, 20.9% over PC, and 9.6% over GES.

## Strengths

- **Novel integration of Shapley-based directional evidence into score-based discrete causal discovery.** The idea of using local feature attributions to modulate BIC's penalty term is original and well-conceived. Equation (2) and the three-stage pipeline (Figure 1, Algorithms 1–2) are clearly presented. The paper correctly distinguishes the proposed approach from prior work that assumes known causal structure (Frye et al., Heskes et al.) or uses attributions for post-hoc explanation rather than structure learning itself (Section 2.3).

- **Large-scale and well-structured empirical evaluation.** Experiments span 10 networks (6–76 nodes, 6–123 edges) and 7 sample-size regimes (0.125M²–8M²), with 10 repetitions each — 700 runs in total. Results are disaggregated by network and sample size (Table 2), and precision/recall are reported separately (Figure 2), enabling diagnosis of where gains come from. Statistical significance is assessed with adjusted Friedman and Wilcoxon tests.

- **Drop-in compatibility with the BIC framework.** When the Shapley signal is near zero (e.g., few confident predictions at small sample sizes), XBIC defaults to standard BIC. This graceful degradation means the method does not harm performance in regimes where directional evidence is unavailable, making it a safe replacement in existing pipelines (Section 3, properties (i)–(ii)).

- **Code and data released.** The anonymous repository with code, data splits, and evaluation scripts facilitates reproduction and extension.

## Weaknesses

### Major

- **Flawed baseline comparison for PC and GES via random orientation of undirected edges.** The paper states (Section 4.1): "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." Random orientation of undirected edges injects substantial noise into the baseline precision and F₁. On a PDAG with many reversible edges — standard output for PC — this procedure yields ~50% expected directional correctness on those edges, systematically depressing the baseline. Consequently, the headline "20.9% improvement over PC" and "9.6% improvement over GES" (Table 4, abstract) are uninterpretable as clean measures of method quality; they conflate XBIC's actual performance with an artificial penalty on the baselines. A fairer approach would evaluate at the CPDAG level using appropriate metrics (e.g., CPDAG SHD) or complete the PDAG via a deterministic search (e.g., BIC-guided orientation within the equivalence class). This issue **does not affect** the primary XBIC vs. BIC-HC comparison (both produce DAGs directly), which is clean, but it undermines two of the three claimed improvement figures prominently cited in the abstract and conclusion.

- **No direct evidence that Shapley values specifically help orient edges within Markov-equivalence classes.** The paper's central motivation is that XBIC "provides directional preference within Markov equivalence classes" (Section 1, Section 3), yet the experiments never isolate this effect. The reported F₁ improvement over BIC-HC could plausibly be driven by a general penalty reduction that encourages adding more edges (recall increases, as shown in Figure 2), rather than specifically improving orientation accuracy on edges whose direction is not identifiable from conditional independencies. The evaluation does not include (a) an ablation replacing Shapley values with random or constant weights to verify that the directional signal, rather than mere penalty softening, drives the gain; (b) a metric isolating performance on edges that are reversible in the true CPDAG (the setting where BIC is claimed to struggle); or (c) a comparison to BIC with a uniformly reduced penalty (e.g., λ·logN/2 with λ<1) to show that edge-specific weighting adds value beyond a general parsimony reduction. Without such analyses, the core claim remains supported only by indirect evidence.

### Minor

- **Modest absolute improvement at high computational cost.** The average absolute F₁ gain over BIC-HC is 0.04 (Table 4), while runtime increases by 100–1000× (Table 5). Several settings in Table 2 show flat or negative deltas (e.g., Water at 0.125M², Win95pts at 8M²). The paper honestly acknowledges these limitations, but the practical significance of a method that requires training M classifiers and computing TreeSHAP for every confident instance yet delivers a 0.04 F₁ gain on average — with regression on some networks — should be more directly discussed rather than left implicit.

- **The specific confidence threshold τ used in main experiments is not reported.** The paper states that "Varying this threshold between 0.7 and 0.95 changed downstream F₁ by < 1%" (Section 4.1), which describes sensitivity, but never states the actual default value used in the 700-run evaluation. Similarly, the fraction of instances that pass the threshold (|S_i|/N) across networks and sample sizes is not reported, making it difficult to assess when XBIC is effectively reverting to BIC versus actively leveraging Shapley signal. Both are needed for reproducibility and for understanding failure modes.

- **Use of absolute Shapley values in SHAP(G) (Eq. 3) is not justified.** The paper sums absolute mean attributions across edges. Averaging absolute values discards the sign information that distinguishes "Xⱼ positively predicts Xᵢ" from "Xⱼ negatively predicts Xᵢ," both of which are aggregated into the same positive contribution. The authors should explain why absolute values are appropriate for this scoring function, or compare with a signed alternative.

- **No discussion of potential overfitting in the Shapley computation.** The same data are used to (1) train the XGBoost classifiers via cross-validation, (2) compute Shapley attributions on the training data, and (3) run the structure search. The confidence filter reduces but does not eliminate the risk that attributions reflect spurious patterns that then drive the search. A discussion of this, or a small experiment using held-out attributions, would strengthen confidence in the method.

- **The paper does not acknowledge that BIC has some orientation power for discrete data.** In discrete Bayesian networks, the parameter count varies across DAGs within the same Markov-equivalence class, giving BIC some ability to distinguish orientations. The introduction states that "BIC often struggles to orient edges within Markov-equivalence classes" without noting this nuance for the discrete setting, which would provide useful context for when the Shapley signal is most needed.

### Trivial

- The hyperparameter w is swept post-hoc over {1,2,3} with the best selected by average F₁. No guidance is given for how to set w in practice (e.g., via validation on a held-out set or using the average confidence across nodes).

## Nice-to-Haves

- An ablation replacing the computed Shapley values with random numbers (or a constant) to verify the directional signal is responsible for the gain, rather than just penalty softening.
- A controlled comparison to BIC-HC with a uniformly reduced penalty (λ < 1) to distinguish edge-specific weighting from general parsimony reduction.
- Targeted metrics on edges that are reversible in the true CPDAG, directly testing whether XBIC resolves orientation ambiguities within equivalence classes.
- For PC and GES: orient undirected edges by running a quick BIC-based hill climb restricted to the DAGs consistent with the PDAG, providing a natural baseline completion.

## Removed Points

- **"Excessive computational cost for modest improvement" (from Harsh Critic as a top-level weakness):** Demoted to Minor. The paper openly acknowledges this trade-off and discusses parallelization. The cost-benefit judgment is a matter of application domain, not a flaw in the paper's reasoning.
- **"Convergence of SHAP(G) as N grows" (from Harsh Critic):** Removed. The paper does not claim a formal convergence result for SHAP(G); the consistency remark only notes that the penalty preserves O(log N) growth. Asking for a population-level convergence analysis of a classifier-dependent quantity goes beyond what the paper sets out to do.
- **"Insufficient detail on PDAG completion" (from Harsh Critic):** Merged into the Major weakness on random orientation. The core issue is the methodological choice, not reporting detail.
- **Strength Finder's claim of "consistent gains":** Toned down in the strengths section. Table 2 shows several zero and negative entries, so "consistent" overstates the evidence. The gains are aggregate and statistically significant but not uniform.
- **Strength Finder's "drop-in compatibility" framing:** Kept but framed as "graceful degradation" rather than "drop-in," since the computational overhead is substantial.

## Novel Insights

None beyond the paper's own contributions. The reviewers raise standard concerns (baseline fairness, ablation depth, cost-benefit analysis) that do not reveal novel methodological observations beyond what the paper already describes.

## Suggestions

1. **Fix the PC/GES baseline evaluation.** Either evaluate at the CPDAG level using metrics appropriate for partially directed graphs, or complete undirected edges with a BIC-constrained search rather than random orientation. Re-report the PC and GES improvement figures accordingly.
2. **Add at least one ablation that isolates the role of the Shapley directional signal** (e.g., random Shapley values, or a λ-scaling experiment). This directly addresses the paper's core claim and would significantly strengthen it.
3. **Report the default τ value and the fraction of instances passing the threshold** for each (network, sample size) combination. This lets readers assess when the method is actively using Shapley signal versus defaulting to BIC.
4. **Justify or remove the absolute value in Eq. (3),** or run a comparison with signed Shapley aggregation.
5. **Acknowledge the discrete-data nuance** that BIC's parameter count varies within equivalence classes, clarifying the residual orientation challenge that XBIC targets.

## Calibration

**Round 1 (bracketing):** Weak anchors (avg 3.0–3.25, e.g., "Sparse Causal Model") are clearly below this paper. Strong anchors (avg 8.0) are above it. Middle anchors (avg 4.0–5.33) form the relevant band.

**Round 2 (narrowing):** 
- "Optimal Kernel Choice for Score Function-based Causal Discovery" (avg 4.40, Reject) — weaker experimental scope and contribution than XBIC.
- "Root Cause Analysis of Failure" (avg 4.50, Reject) — less comprehensive evaluation.
- "On Causal Discovery in the Presence of Deterministic Relations" (avg 6.25, Reject) — stronger theoretical contribution but comparable experimental rigor; XBIC is slightly below this anchor due to the baseline comparison issue and lack of targeted evidence for its core claim.
- "DAG-SHAP" (avg 5.00, Reject) — similar novelty level (Shapley + causality) but assumes known causal graph; XBIC has a harder problem setting but less theoretical analysis. Comparable quality.

The paper sits between the 4.4–5.0 anchors and the 6.25 anchor. Its primary comparison (XBIC vs BIC-HC) is sound and shows a modest but significant improvement, but the PC/GES comparison is compromised, and the central claim about orientation within equivalence classes is not directly tested. These issues prevent it from reaching the 6+ level.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>