## Summary

This paper presents a pilot study on applying active learning (AL) to conditional flow matching generative models in engineering shape design settings where labels require costly numerical simulation. The core contribution is a theoretical framework based on piecewise-linear neural networks and closed-form flow matching, which characterizes how individual data points influence model diversity and accuracy. From this framework, the authors derive two query strategies—one maximizing diversity (Q_D) and one maximizing accuracy (Q_A)—and demonstrate these objectives are inherently conflicting, offering a dataset-level explanation for the diversity–accuracy trade-off. Experiments on four datasets (a synthetic task and three aerodynamic shape datasets) show Q_D and Q_A outperform classical AL strategies adapted from discriminative settings.

---

## Strengths

- **Novel problem formulation.** Active learning tailored specifically for generative models (rather than generative models used to assist AL for classifiers) is genuinely underexplored. Framing the task around continuous condition datasets in engineering simulation is well-motivated—numerical solvers do make labeling expensive, and the continuous label space makes direct application of standard AL strategies nontrivial.

- **Clean theoretical insight from the piecewise-linear framework.** Under the assumed CPWL interpolation behavior (Eq. 1–3), the derivation that interpolation in label space induces interpolation in data space is elegant. The conclusion that label-consistent samples drive diversity while label-diverse samples drive accuracy is a crisp, falsifiable claim, and Figure 1 makes it visually intuitive.

- **Dataset-level decoupling improves efficiency.** A practical strength is that both Q_D and Q_A operate on dataset statistics (using lightweight RBF networks for label prediction) rather than requiring expensive re-training of the flow matching model at every AL iteration. This is a meaningful advantage in the target application domain.

- **Diverse experimental settings.** Applying the method to three physically grounded datasets (airfoil, flying wing, starship) with labels from CFD solvers, and showing qualitative differences in generated shapes (Figures 5–8), validates the practical relevance beyond the synthetic toy example.

---

## Weaknesses

### Fatal
None that fully invalidate every result.

### Major

1. **Unverified core assumption—piecewise-linear condensation in practice.** The entire theoretical framework rests on the hypothesis that flow matching networks undergo condensation and behave as piecewise-linear interpolators. The referenced condensation literature (Luo et al., 2021; Xu et al., 2025) addresses specific regimes (small initialization, dropout, infinite-width). No evidence is provided that the 8-layer, 512-unit LeakyReLU networks actually trained in the experiments exhibit this behavior. Without empirical or theoretical justification that the assumption holds in the experimental setup, the theoretical analysis is decoupled from the practical algorithms.

2. **Loose connection between theory and Q_D.** The theoretical analysis prescribes that diversity is maximized by adding points whose labels exactly match existing labels. Since exact matches are infeasible, the paper relaxes this to three heuristic terms (Eq. 4): a label-proximity penalty, a cluster-entropy bonus, and a coresets-style data-space distance. This relaxation is plausible but not derived from the framework—it is engineered. The resulting Q_D could have been motivated without the piecewise-linear analysis. The paper does not prove or empirically verify that Eq. 4 actually maximizes Eq. 3's upper bound on generation diversity.

3. **Q_A reduces to label-space coresets without independent justification.** The paper explicitly states "Q_A performs the coresets algorithm in the label space." Lemma 2 (Eq. 5) bounds the error within a subregion by the maximum pairwise label distance, making Q_A a principled consequence of the framework—but only if the piecewise-linear assumption holds (see weakness 1). If that assumption is questioned, both the accuracy bound and Q_A lose their theoretical grounding.

4. **Hybrid strategy Q_hybrid lacks comparative baseline experiments.** Figure 7 shows the diversity–accuracy trade-off for varying ω, which qualitatively demonstrates controllability. However, no competing method is shown on the same Pareto curve. It is unclear whether Q_hybrid's trade-off frontier dominates (or is dominated by) baselines such as random querying or coreset+committee combinations.

### Minor

5. **Limited active learning iterations.** Only 5 rounds of 6%-budget selection are reported. With such a small number of iterations, it is difficult to assess whether trends are stable and whether differences are meaningful as the dataset grows. More iterations would strengthen confidence in the long-term behavior of each strategy.

6. **Accuracy-metric direction is inverted in text.** The paper describes "Q_D achieves the lowest accuracy" (Fig. 4 caption and text), but lower MSE means *higher* accuracy—the wording conflates the metric with its value direction in several places, creating confusion about which strategies perform better.

7. **Sensitivity of strategies to RBF label prediction quality.** Both Q_D and Q_A rely on RBF-predicted labels for the unlabeled pool. No analysis is provided of how prediction error in these labels affects strategy quality, particularly in high-label-dimensional settings (e.g., y ∈ ℝ⁴ for starship).

### Trivial
None worth listing beyond OCR/parser artifacts already present.

---

## Nice-to-Haves

- An empirical check (e.g., comparing network activation patterns before and after training) that the trained networks exhibit piecewise-linear behavior would substantially strengthen the theoretical claims.
- Including a Pareto-frontier comparison of Q_hybrid vs. baselines in the same diversity–accuracy space (as a single figure per dataset) would make the hybrid's value clearer.
- The diversity score is described as "a custom variant of the Vendi score" but is defined as average pairwise distance (Eq. 8)—clarifying the relationship to the actual Vendi score would avoid confusion.

---

## Novel Insights

The paper's most genuinely novel observation is the dataset-level decomposition of the diversity–accuracy trade-off in conditional generative models: the combinatorial product structure of same-label data (driving diversity) versus cross-label interpolation (driving accuracy) offers a concrete, data-centric explanation for a phenomenon usually attributed to model design. This perspective—that the trade-off can be steered purely through dataset curation without changing the model—is a meaningful conceptual contribution to the generative modeling literature, even if the formalization rests on an unverified interpolation hypothesis.

---

## Suggestions

- **Validate the piecewise-linear assumption empirically:** Plot the activation patterns or linear region count of trained flow matching networks before and after condensation, comparing networks trained on small vs. large datasets. Even one such diagnostic on the synthetic dataset would substantiate the core hypothesis.
- **Decouple Q_D's empirical performance from its theoretical motivation:** Run an ablation where Q_D is applied to a standard diffusion model (not a closed-form flow matching model) to test whether the framework generalizes or is specific to the closed-form setting.
- **Add a Pareto curve comparison:** For the hybrid strategy, overlay random, coreset, and committee baselines on the diversity–accuracy scatter plot to show whether Q_hybrid achieves a frontier that is not reachable by competitors.
- **Report variance across seeds:** All result plots show single-run curves; adding confidence intervals across multiple random initializations would clarify whether differences are statistically meaningful.

---

## Score and Decision

The paper addresses a genuine gap (active learning for flow matching generative models), produces tractable theoretical analysis, and validates the approach on practically relevant engineering tasks. However, the central theoretical assumption (piecewise-linear condensation in practical flow matching networks) is stated as a hypothesis and never verified, Q_D's formulation is loosely derived from theory, and the hybrid strategy's advantage is not demonstrated against baselines on a common Pareto frontier. These are substantive issues for a theory-grounded method paper, reducing confidence that the theoretical framework truly explains the empirical results rather than simply accompanying them.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>