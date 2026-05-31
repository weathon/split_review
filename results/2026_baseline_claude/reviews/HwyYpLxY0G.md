## Summary
The paper proposes the **Aligned Scoring Rule (ASR)** for textual information elicitation, building on the reduction framework of Wu & Hartline (2024) which maps textual peer reviews to numerical scoring via LLM-based summarization and question-answering oracles. The core contribution is formulating a convex optimization program over the space of *separate* proper scoring rules to minimize MSE against a reference score (instructor score or LLM-judge score), thereby yielding a scoring rule that is both provably proper and aligned with human preferences. Experiments on peer grading data from two undergraduate algorithm classes show lower MSE and higher Pearson/Spearman correlations compared to baselines.

---

## Strengths

- **Clean problem formulation.** The paper identifies a genuine and underexplored tension: the Wu & Hartline (2024) framework guarantees properness but says nothing about human preference alignment. Framing this as a constrained MSE minimization over a restricted function class is natural and principled.
- **Convexity result (Corollary 3.4).** The observation that optimizing over *separate* (weighted-sum) scoring rules yields a convex program—while max-over-separate does not—is a useful structural insight that enables efficient, scalable optimization with guarantees on convergence.
- **Interpretability angle.** Assigning per-dimension weights allows identifying which summary rubric points matter most for a given assignment, which has real educational utility beyond scoring.
- **Practical motivation.** The peer grading setting is well-motivated, and the end-to-end LLM pipeline (Summarization + QA oracle + optimization) is clearly described.

---

## Weaknesses

### Fatal
*None.*

### Major

1. **No train/test split described.** The paper does not clearly separate the data used to fit ASR from the data used to evaluate it. The optimization (Program 2) explicitly minimizes MSE on a dataset D, and then Table 1 reports MSE on what appears to be the same data. The "nearly-identity linear regression" in Figure 4 is also almost certainly in-sample, which is trivially expected by construction. Without a proper held-out evaluation, the reported metrics are not informative about generalization.

2. **Unfair baseline comparison.** The EGPT(AV) and EGPT(MV) scoring rules from Wu & Hartline (2024) output scores in [0, 1], while the instructor reference score is in [0, 10]. The table shows EGPT(AV) MSE = 9.541, far worse even than the best constant at 3.741. A simple affine rescaling of EGPT outputs would substantially reduce its MSE. Without normalizing baselines to the same scale as the reference, or reporting only scale-invariant metrics like Pearson/Spearman, the MSE comparison is misleading. The Pearson/Spearman results are more credible (EGPT AV: 0.294/0.301 vs. ASR: 0.717/0.622), but even these benefit from the in-sample evaluation issue.

3. **Incremental technical contribution.** The properness guarantees (Theorems 3.2 and 3.3) are directly imported from Wu & Hartline (2024) and explicitly attributed there. The new contribution is replacing a fixed scoring rule (V-shaped) with one optimized by a standard convex QP over 6m variables. While useful, this is a modest engineering extension. There is no new theoretical result about the tradeoff between properness and alignment, sample complexity of the optimization, or generalization across assignments.

4. **No ablation isolating the properness constraint.** The paper's central claim is that ASR aligns well *while maintaining properness*. But the benefit of the properness constraint is never isolated—there is no comparison to unconstrained MSE regression on the same features. Without knowing whether the properness constraint costs alignment quality, it is impossible to judge whether a simpler non-proper predictor would dominate.

### Minor

1. **Dataset is small and narrow.** 516 total peer reviews across 22 assignments in two undergraduate algorithm courses is a limited empirical base. The assignments are all from the same pedagogical context and may share strong distributional similarities, making results hard to generalize to other domains or question types.

2. **The non-inverting oracle assumption is not empirically verified.** Theorem 3.2 conditions on the QA oracle being non-inverting (error rate < 50%). The paper does not report empirical error rates of the QA oracle, so the properness guarantee's practical relevance is unclear.

3. **Pearson r = 0.554 between instructor and LLM-judge is modest.** The paper describes this as "high correlation," but r ≈ 0.55 implies only ≈ 30% shared variance. This tempers conclusions about LLM-Judge serving as a scalable substitute.

### Trivial
*None worth noting.*

---

## Nice-to-Haves
- A cross-assignment leave-one-assignment-out evaluation would make the generalization claims credible.
- An ablation comparing ASR to unconstrained regression (same features, no properness constraint) would clarify the cost of properness.
- Reporting oracle QA error rates to empirically validate the non-inverting assumption would strengthen the paper's theoretical claims.

---

## Novel Insights
The main genuinely novel insight is that restricting to *separate* proper scoring rules (weighted sum of single-dimensional rules) is both sufficient for practical properness and necessary for convexity of the alignment optimization, while the alternative max-over-separate structure breaks convexity. This structural observation—that the aggregation choice simultaneously determines computational tractability and expressiveness—is an underappreciated design principle in the scoring rule literature that deserves wider attention.

---

## Suggestions

1. **Rerun all evaluations with a held-out test split** (e.g., leave-one-assignment-out cross-validation), reporting both in-sample and out-of-sample metrics. This is the most important revision.
2. **Normalize EGPT outputs to the reference scale** before computing MSE, or drop MSE from the baseline comparison and rely solely on Pearson/Spearman.
3. **Add an unconstrained regression baseline** (predict instructor scores directly from QA outputs without the properness constraint) to quantify the alignment cost of enforcing properness.
4. **Report QA oracle accuracy** on a subset of manually labeled examples to empirically bound the properness error under the non-inverting assumption.

---

## Score and Decision

The paper tackles an interesting and practical problem, and the convexity observation is clean. However, the core empirical claims appear to rest on in-sample evaluation, the baseline comparison is confounded by scale mismatch, the technical contribution over Wu & Hartline (2024) is incremental, and the dataset is small and domain-restricted. These are not trivial issues: the experimental section is the main original contribution of the paper, and its methodology is insufficiently rigorous for confident conclusions.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>