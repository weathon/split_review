Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper studies how variable scale (measurement units) affects score-based DAG structure learning. It extends prior results (limited to 2-node linear settings) by deriving explicit variance-ordering conditions (Propositions 2–6) under which mean squared error (MMSE) is minimized by a wrong DAG for d-dimensional chains, forks, and colliders. It further shows that log-likelihood, BIC, and ELBO losses reduce to MSE under Gaussian noise, inheriting the same vulnerability, and proposes a Scale Robust Loss (SRL) for discrete learners. Experiments on synthetic and real-world data confirm that NT, DAG-GNN, and GraN-DAG predict wrong structures in 100% of tested scaling scenarios.

## Strengths

1. **Precise theoretical conditions for d-dimensional chains, forks, and colliders (Propositions 2–6)**. Propositions 2–5 derive exact variance-ordering inequalities (e.g., Var(X₁ᵀ) > … > Var(X_dᵀ) for the reversed chain) under which MMSE favors a wrong DAG. Proposition 6 shows scale can even change d-separation statements by inducing an extra edge and a collider. These are clean theoretical advances over prior work limited to 2-node systems.

2. **Unifies multiple loss families under the same vulnerability.** Propositions 7–10 show that under Gaussian additive noise, log-likelihood, BIC, and ELBO all reduce to the same squared-loss form, making them equally susceptible to scaling. This connects a broad class of popular structure learners (NT, DG, GND, GES) to the same underlying issue.

3. **Extensive empirical validation across learners, settings, and real data.** Table 1 and Figure 2 report that NT, DG, and GND predict the expected wrong structure in 100% of trials for chains/forks/colliders under both linear and non-linear dependencies. The ablation study (Q3) confirms the effect persists in random 10-node DAGs violating assumption (A1). The Sachs et al. (2005) experiment (Q4) grounds the findings in a practical application.

4. **Proposes a concrete mitigation (SRL) for discrete learners.** Section 3.3 defines SRL (ℒₛ = ℒ − Σ Var(source nodes)) and Table 1 shows GES+SRL predicts the correct graph in all tested scenarios, demonstrating feasibility for the discrete search setting.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical results are restricted to three elementary structures (chains, forks, colliders), yet the title and framing imply broader generality.** Propositions 2–6 are proved under Assumption (A1), which explicitly limits the ground-truth DAG to these three structures. Remark 1 sketches a decomposition argument ("each DAG can be decomposed into subgraphs fulfilling (A1)") but this is *not* formalized into a theorem — the paper offers no proof that scale sensitivity in a subgraph reliably induces scale sensitivity in the full DAG, or that the decomposition preserves optimality. The title "Learning Large DAGs is Harder than you Think" and the Introduction's claim to "generalize the above mentioned results to d-dimensional and non-linear cases" overstate the theoretical breadth. The experiments on complex DAGs (Q3) are empirical only and lack a supporting theory. This gap between the framing and the actual proofs weakens the paper's claimed generality.

### Minor

1. **Propositions 7–10 (log-likelihood equivalence) are standard consequences dressed as novel results.** The equivalence of negative log-likelihood to MSE under homoscedastic Gaussian noise is textbook material. Propositions 8–10 are immediate corollaries given Definition 2 (which defines "log-likelihood loss family" so broadly that any loss with a log-likelihood term qualifies). The real contribution is *connecting* this equivalence to scale sensitivity, which could be stated in one paragraph rather than four propositions. This inflates the apparent theoretical contribution.

2. **The theoretical generalization to non-linear dependencies is incomplete.** The paper acknowledges this directly: "it is not trivial to derive conditions under which the optimum of the log-likelihood render a wrong DAG without additional assumptions about functions f_{j,θ}." The experiments on non-linear data confirm that scaling causes wrong predictions, but the theory provides no explanation of *why* or *when* beyond the linear intuition. The abstract and introduction should more clearly separate the linear (proved) and non-linear (empirically observed) cases.

3. **SRL does not apply to the continuous learners (NT, DG, GND) that are the paper's primary experimental focus.** The paper acknowledges this limitation honestly but does not resolve it. For the algorithms most affected by scale, the paper's only actionable recommendation is data standardization — yet prior work (Reisach et al., 2021, cited in the paper) found that standardization *degrades* performance of the same algorithms. This tension is not discussed or reconciled.

4. **Experimental results lack measures of variability.** Findings are reported as percentages (100%, 40%, 20%) without error bars, confidence intervals, or standard deviations. While the 100% results are striking, some statistical grounding (e.g., exact counts over 30 trials) would strengthen the empirical claims.

5. **No systematic investigation of scaling thresholds.** The theory gives inequality conditions, but the paper does not study *how much* scaling is required to cause flips in practice. In Q2, a single variable is scaled "by a factor of 12" — would factors of 2 or 3 suffice? Understanding the regimes where scale sensitivity is practically concerning versus requiring extreme scaling would strengthen the practical implications.

### Trivial

1. **Notation could be clarified.** The use of superscript T in X_i^T (denoting a column vector from the data matrix) is confusing, especially when combined with matrix transpose notation.

## Nice-to-Haves

- A systematic comparison of data standardization vs. non-standardization for continuous learners, resolving the tension with prior work showing standardization harms performance.
- Derivation of unified theoretical conditions for arbitrary DAG structures (beyond chains, forks, colliders) under linear models, or a rigorous decomposition theorem formalizing Remark 1.
- Investigation of realistic scaling thresholds: what factor of scaling is needed to flip predictions in representative settings?

## Removed Points

These points were considered but removed with justification:
- **"Medical example adds little" (Harsh Critic)**: This is a subjective presentation judgment about a motivating example, not a technical weakness; removed as a stylistic nitpick.
- **"Missing related works" (Harsh Critic)**: Removed per instructions — I cannot confirm what works exist beyond those cited.
- **"Missing appendix content" (Harsh Critic)**: Removed per instructions — the appendix was stripped by the PDF parser.
- **"Proposition 7 is 'true by definition'" exaggeration**: The propositions are standard but not vacuous; the critic's phrasing overstates. The point is retained in Minor #1 with corrected framing.
- **Strengths that conflict with verified weaknesses**: Generic praise about "important problem" removed. The concrete strengths listed above are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the title and abstract** to accurately reflect the scope: the theory covers chains, forks, and colliders, with empirical evidence for more complex DAGs. A title like "Scale Sensitivity in Score-Based DAG Learners: Theoretical Conditions for Simple Structures and Empirical Evidence for Larger Graphs" would be more precise.
2. **Consolidate Propositions 7–10** into a single paragraph or lemma, making clear the standard equivalence and focusing on its consequence for scale sensitivity.
3. **Address the Reisach et al. tension** explicitly: discuss whether standardization might help in some settings and harm in others, and under what conditions.
4. **Add error bars or confidence intervals** to experimental results.
5. **Investigate scaling thresholds** to show what factors of scaling cause flips for representative configurations.

## Score and Decision

This paper makes a valid, bounded contribution: it extends known scale-sensitivity results from 2-node to d-dimensional settings for three elementary structures, unifies multiple loss families under the same vulnerability, and provides extensive experimental confirmation. The core theoretical results (Propositions 2–6) are clean and new. However, the paper's framing overstates the theoretical generality — the title implies a general theory for "large DAGs" that the proofs do not deliver. The log-likelihood analysis is presented with more formal weight than its novelty warrants. These issues are addressable through reframing and consolidation rather than requiring new results. The paper is at the boundary between a strong workshop submission and a conference paper; with corrected framing it would be a solid contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>