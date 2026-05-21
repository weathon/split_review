Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

This paper presents a pilot study on active learning for flow matching generative models in shape design. The authors develop a theoretical framework based on piecewise-linear neural network analysis, deriving generation rules that reveal how same-label data drives diversity while different-label data drives accuracy. From this analysis, they propose two query strategies—\(Q_D\) for diversity and \(Q_A\) for accuracy—along with a weighted hybrid. Experiments across synthetic, airfoil, flying wing, and starship-like datasets show that \(Q_D\) and \(Q_A\) respectively outperform discriminative-model active learning baselines on diversity and accuracy metrics.

## Strengths

- **Novel problem framing**: The paper addresses active learning *for* generative models (flow matching), a direction distinct from the more common "generative models for active learning." This is a genuinely underexplored area, and the application to shape design with numerical simulation labels is well-motivated.

- **Productive theoretical framework**: The piecewise-linear analysis of closed-form flow matching provides a coherent, if idealized, account of how dataset composition affects generation diversity and accuracy. The derivation that adding same-label points increases combinatorial sample types (diversity) while adding distinct-label points reduces interpolation error (accuracy) is intuitively compelling and directly motivates the two query strategies. The framework frames the diversity–accuracy trade-off as inherent to dataset structure, which is a useful perspective.

- **Consistent empirical results across multiple datasets**: Figure 4 demonstrates that \(Q_D\) yields the highest diversity and \(Q_A\) yields the highest accuracy on all four datasets, outperforming coreset, committee, and anchor baselines. The hybrid strategy (Figure 7) shows a controllable trade-off. These results are reproducible across domains (synthetic, airfoil, flying wing, starship-like), lending credibility to the approach.

- **Model-free query selection is a practical advantage**: As the paper notes, \(Q_D\) and \(Q_A\) operate solely on dataset distances and RBF-predicted labels without requiring the flow matching model's internal state. This avoids costly iterative retraining of the generative model during active learning rounds, which is a genuine practical benefit.

- **Ablation validates multi-term design**: Figure 9 confirms that all three terms of \(Q_D\) (label-distance minimization, entropy increase, data-distance maximization) positively contribute to diversity, with the data-distance term being most influential. This provides empirical grounding for the combined objective beyond mere assertion.

## Weaknesses

### Fatal

None. The paper's core claims are supported by the experiments; no single flaw invalidates the entire contribution.

### Major

- **Theory built on an unvalidated hypothesis**: The entire analytical framework rests on the assumption that flow matching networks exhibit piecewise-linear interpolation under condensation (lines 25–26, 49–50). The paper cites prior work on condensation (Luo et al. 2021; Xu et al. 2025) to motivate this, but provides no empirical test of whether the trained models actually satisfy Equations (1)–(3). Without such verification—e.g., checking whether generated samples lie in the convex hull of training data, or whether adding same-label points increases combinatorial sample types as predicted—the paper cannot claim that the theory *explains* why the strategies work, only that it motivated their design. This weakens the paper's central intellectual contribution.

- **Gap between theoretical prescription and practical implementation**: The theory requires new data points to have labels *exactly identical* to existing ones for diversity gains (Section 2.3). The paper acknowledges this is infeasible in practice and falls back to "sufficient similarity" via an RBF label predictor and entropy-based clustering (line 93). This is not a trivial relaxation—it severs the direct link between the combinatorial argument (going from \(mn\) to \((m+1)n\) sample types) and the actual query strategy. The RBF predictor introduces its own errors, and "sufficient similarity" is operationalized through distance thresholds and clustering that are not derived from the theory. The paper would benefit from analyzing under what conditions this approximation preserves the theoretical guarantees.

### Minor

- **Diversity metric is limited**: Diversity is measured as average pairwise Euclidean distance (Eq 8), which can be inflated by outlier or unrealistic samples. For shape design, this matters: a physically invalid airfoil could increase the diversity score while being useless. The visual examples (Figures 5, 6, 8) partially mitigate this concern, but a quality-filtered diversity metric or a feasibility check would strengthen trust in the reported numbers.

- **Limited exploration of the hybrid strategy**: Equation (7) combines scores in different units with a single weight \(\omega\), and only \(\omega = 0.1\text{–}0.4\) is explored. The paper does not discuss normalization, calibration, or whether the resulting points actually lie on a meaningful Pareto frontier. The demonstration of a trade-off is sufficient for the paper's scope, but the analysis is shallow.

- **No analysis of RBF predictor accuracy**: The query strategies depend on RBF-predicted labels for unlabeled data (line 93, 107), yet the paper provides no evaluation of prediction accuracy or how errors propagate into query selection. If the RBF predictor is poor, \(Q_D\) could select points with labels that are actually far from existing ones, undermining the strategy.

- **Missing naive heuristic baselines**: While coreset and committee are reasonable baselines, the paper does not compare against the simplest instantiations of its own principles—e.g., farthest-point sampling in data space (pure diversity without label considerations) or uniform sampling in predicted label space (pure accuracy without data-space considerations). Such comparisons would isolate the unique value of the combined terms in \(Q_D\) and better validate the theoretical motivation.

### Trivial

- The notation for Eq (1) is somewhat underspecified: the term \(\mathbf{e}_{t,i}\) is described as "the noise that make \(\mathbf{x}_i\) to \(\mathbf{x}'\)" without formal definition of the noise schedule or its relationship to the flow matching objective.
- The paper states that closed-form flow matching uses optimal transport noise schedules (line 49–50) but does not detail how this connects to the piecewise-linear assumption.

## Nice-to-Haves

- Empirically testing the core hypothesis by measuring whether generated samples conform to Equation (3) under the trained models would substantially strengthen the paper.
- Replacing the weighted-sum hybrid with a principled multi-objective formulation (e.g., Pareto-front selection) would deepen the analysis.
- Adding a shape-validity check (e.g., closed airfoil profiles, physically plausible lift curves) would address concerns about the diversity metric.

## Removed Points

These points are flagged to be removed. Treat them with caution.

- **Harsh critic claim: "The theory contradicts how deep generative models actually work—real flow matching models are not constrained to the convex hull of training data."** — REMOVED. The paper specifically uses *closed-form* flow matching (Scarvelis et al. 2023; Chen 2025) under the condensation hypothesis, which is a specific regime. The critic's general claim about "real flow matching models" does not engage with the paper's specific setting and stated assumptions.

- **Harsh critic claim: "The paper does not compare against obvious heuristic baselines like 'select points far from existing data points' (for diversity)."** — REMOVED as a standalone fatal criticism. The coreset baseline (Sener & Savarese 2017) is essentially a data-space coverage strategy and serves as a reasonable heuristic baseline. However, the *absence of even simpler instantiations* is retained as a Minor weakness above.

- **Harsh critic claim: "The derivations in Section 2.2 mix the closed-form flow matching model with piecewise-linear network properties, but the two do not obviously combine."** — REMOVED. This is a claim about what "obviously" combines, not a specific identified error. The paper presents Lemma 1 (deferred to the appendix) to bridge these two components. Without access to the appendix, this criticism is speculative rather than verifiable.

- **Harsh critic claim: "The strategies never interrogate the flow matching model's internal regions, activation patterns, or generation behavior."** — REMOVED as a weakness. The paper explicitly presents model-free query selection as a *feature*, not a bug (lines 107–108: "Eq4 and Eq6 do not incorporate the trained flow matching model, but instead operate directly on the dataset for data selection. This implies that the available annotation budget can be utilized efficiently... thereby avoiding the need for repeated training of the flow matching model."). Criticizing the paper for not doing something it deliberately chose not to do is scope creep.

- **Strength Finder: "Model-free query selection reduces computational cost."** — RETAINED but merged into Strengths as a practical advantage.

- **Strength Finder: "Consistent experimental superiority."** — RETAINED but qualified: the paper outperforms the chosen baselines, but the baselines are discriminative-model methods, not generative-model-specific ones.

## Novel Insights

The paper's most interesting insight—beyond its own contributions—is the observation that diversity and accuracy in conditional generative models can be understood as competing claims on the *same* dataset resource: same-label points feed diversity through combinatorial generation, while distinct-label points feed accuracy through interpolation-error reduction. This framing, even if the precise theoretical model is idealized, offers a useful lens for thinking about dataset design for conditional generation more broadly, and could inform future work on data valuation or dataset pruning for generative models.

## Suggestions

- Add a diagnostic experiment: for a trained flow matching model, measure the extent to which generated samples under interpolated conditions actually lie near affine combinations of training samples (testing Equation 3 empirically). This would directly validate or falsify the theoretical framework.
- Compare \(Q_D\) against a pure farthest-point-sampling baseline in data space (no label considerations) and \(Q_A\) against pure farthest-point sampling in label space (no data-space considerations) to isolate the value of the multi-term design.
- Report and analyze the RBF predictor's accuracy on each dataset, and discuss how prediction errors could affect query selection quality.
- Discuss normalization of the \(Q_D\) and \(Q_A\) scores before combining in Equation (7), or explore a Pareto-based combination.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| FALCUN (yZBpnKpBCw) — active learning for discriminative models | 4.50 | R1 (mid) | Current paper is stronger: novel generative-model framing, broader evaluation, theoretical motivation |
| Statistical theory of data selection (HhfcNgQn6p) | 5.50 | R2 | Comparable: both have theoretical frameworks with some gaps, interesting empirical phenomena |
| Be More Diverse (2Chkk5Ye2s) — mixture selection for generative diversity | 5.80 | R1 (mid) | Comparable: different problem but similar level of novelty and validation |
| Conformal Gen (1i6lkavJ94) — conformal prediction for generative models | 6.25 | R2 | Slightly stronger: more rigorous theoretical guarantees, clearer theory-to-practice link |
| GMValuator (WncnpvJk83) — data valuation for generative models | 6.50 | R2 | Stronger: more polished theoretical foundation, better theory-practice integration |
| SE(3) Flow Matching (kJFIH23hXb) — protein backbone generation | 8.00 | R1 (high) | Much stronger: rigorous theory, clear validation, impactful application |

### Round 1 Bracket
Based on round-1 anchors, the paper falls between 4.5 and 8.0, with the middle band (4.5–5.8) being most relevant.

### Round 2 Narrowing
Round-2 anchors in the 4.5–7.5 range, particularly the statistical data selection paper (5.50) and GMValuator (6.50), bracket the paper. The current paper is comparable to the 5.50 anchor (novel theory with gaps, interesting empirical results) but falls short of the 6.25–6.50 anchors that have tighter theory-practice integration.

### Final Score: 5.5

The paper makes a genuine contribution by bringing active learning to flow matching models, supported by a novel (if idealized) theoretical framework and consistent empirical results across multiple shape-design datasets. However, the theory is built on an unvalidated hypothesis, and the gap between the theoretical prescription and the practical implementation is significant. These are addressable concerns but currently weaken the paper's central intellectual claim. The empirical results and practical value of the model-free query strategies warrant acceptance, though the theoretical contribution requires substantial strengthening.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>