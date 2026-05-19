- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 8, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper extends the Benefit of Personalization (BoP) framework — originally limited to classification and prediction accuracy — in two key directions: (1) to regression tasks, by defining BoP for squared-error loss and deriving the first information-theoretic lower bound for real-valued cost functions (Theorem 2), and (2) to explainability (BoP-X), by defining BoP in terms of sufficiency and incomprehensiveness of model explanations. The paper also proves an incompatibility result (Theorem 3: BoP-P = 0 does not imply BoP-X = 0) and provides a hypothesis testing framework with reliability guarantees. Empirical results on the HSLS dataset illustrate the framework.

---

## Strengths

- **Extension of BoP to regression tasks (Section 4.1).** The paper formally defines Minimal Group BoP for regression using squared-error loss, which is a genuine extension beyond the classification-only setting of Monteiro Paes et al. (2022). Theorem 2 provides the first BoP lower bound for real-valued cost functions, enabling a much broader set of applications (e.g., continuous clinical predictions).

- **Introduction of BoP for explainability (BoP-X, Section 4.2).** By defining BoP through sufficiency and incomprehensiveness cost functions (Definitions 3–4), the paper opens a new dimension for auditing personalization models. This directly addresses a gap in the prior literature, which focused solely on prediction accuracy.

- **Theorem 3 (incompatibility between BoP-P and BoP-X).** The paper proves constructively that a personalized model can yield zero accuracy gain while still improving explainability. This is a concrete, non-obvious theoretical result with practical implications for safety-critical applications where both accuracy and interpretability matter.

- **Lemma 2 (partial converse under additive models).** Showing that for Bayes-optimal classifiers under an additive independent-features model, BoP-X=0 implies BoP-P=0 provides a helpful boundary condition on the relationship between the two metrics, even if the conditions are restrictive.

- **Practical hypothesis testing framework (Section 5).** The formalized threshold test with explicit probability-of-error lower bounds gives practitioners a principled way to decide whether empirical BoP estimates are trustworthy given sample size and number of groups.

---

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous/contradictory experimental reporting for classification BoP-P.** The paper states (line 306): "the minimal BoP-P in classification exceeds 0.035, so we can conclude that in this case the use of sensitive attributes worsens accuracy." Under the paper's own definition (BoP = C(h₀) − C(hₚ), with positive BoP meaning improvement), a value exceeding +0.035 would mean personalization *improves* accuracy for all groups — directly contradicting the conclusion that it "worsens" accuracy. The table caption further notes that worsened values are colored red, implying the actual BoP-P is negative. This makes it impossible for a reader to determine the actual empirical result. The most charitable reading is that the authors meant "|BoP| exceeds the detection threshold of 0.035" while the signed value is negative — but this is not what the text says. Because the experimental section is the paper's main empirical demonstration, this ambiguity seriously undermines the reported results as currently written.

### Minor

- **Normality assumption in Theorem 2 is stated but not justified.** The regression bound in Theorem 2 is derived under the assumption that individual BoP follows a normal distribution with the same σ across all groups. While the assumption is clearly flagged (line 222: "any scenario where the individual BoP can be described by a Normal random variable"), no justification, plausibility argument, or sensitivity analysis is provided. The bound's practical value depends on whether this assumption is reasonable for real regression settings. A brief justification (e.g., CLT on loss differences, or a robustness discussion) would significantly strengthen the regression component.

- **Claimed tightening of classification bound is unsubstantiated.** Theorem 1 states it "refines Theorem 1 of (Monteiro Paes et al., 2022) to provide a tighter lower bound," but no comparison, numerical example, or explanation of where the slack was removed is given. The reader cannot evaluate this claim. Either the original bound should be shown alongside the new one with a concrete comparison, or the claim should be softened.

- **Incomprehensiveness-based BoP-X formulas are omitted from Section 4.2.** Section 4.2 explicitly introduces BoP-X and gives formulas for sufficiency (classification and regression), but the incomprehensiveness versions — which are defined in Section 3 (Definition 3) and used in experiments (Section 6) — are not shown. While a reader can infer them by analogy, the omission makes the presentation incomplete.

- **Limited empirical breadth.** Only one dataset (HSLS), one explanation method (Integrated Gradients), and one value of r (50% of features) are used. The paper frames the experiments as an illustration ("exemplify the analysis possibilities"), which is reasonable for a primarily theoretical contribution, but the thinness limits the empirical support for general claims, especially the comparative insight that regression tolerates more attributes than classification.

### Trivial

- **Corollary 3 (line 260) is an empty stub** — the heading appears with no content. This should be filled in or removed.

---

## Nice-to-Haves

- A brief discussion of how the choice of explanation method might affect BoP-X results (the paper uses only Integrated Gradients).
- A sensitivity analysis or justification for the fixed choice of r = 50% of top features used in the explanation evaluation.
- A discussion of possible strategies to relax the Gaussian assumption in Theorem 2, e.g., non-parametric resampling or sub-Gaussian bounds.

---

## Removed Points

The following points from the reviews were removed with justification:

- **"Theorem 3 is trivial" (Harsh Critic).** Removed. Theorem 3 is a constructive existence proof showing an important non-obvious relationship. It is not deep but it is not trivial — it settles a meaningful question.
- **"Bound expression presented without derivation" (Harsh Critic, regarding Theorem 1).** The derivation is in the appendix (stripped by parser). The weakness about lack of *comparison evidence* is retained; the accusation of missing derivation is removed per parser-strip guidelines.
- **"No discussion of whether including group attributes changes 'important features'" (Harsh Critic).** Removed. The paper's BoP-X framework by design compares explanations from models with different input spaces; this is a feature of the analysis, not a bug. The paper clearly defines the notation for both cases.
- **"The paper could use a second dataset or synthetic experiment" + "No ablation on r" + "Additive model in Lemma 2 is restrictive."** These are reasonable suggestions but were moved from weaknesses to Nice-to-Haves since they either lie outside the paper's stated scope (illustrative experiments for a theory paper) or are acknowledged limitations.
- **Strength Finder's claim that Theorem 1 is a "tighter bound."** This was removed from strengths because the tightening is unsubstantiated (no comparison shown). The existence of the bound itself is a genuine contribution; the tightening claim is unverified.
- **Generic strengths from Strength Finder (e.g., "this paper addressed an important problem," "experimental validation shows the framework is practically actionable").** Removed as generic or superficially stated.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make.

---

## Suggestions

1. **Fix the experimental reporting.** Clarify the sign of the classification BoP-P result. If the minimal BoP-P is negative (worsening), state it clearly: e.g., "the minimal BoP-P is −0.04, whose magnitude exceeds the detection threshold of 0.035, allowing us to conclude that personalization significantly worsens accuracy for at least one group." Separate the detection-threshold discussion from the signed result reporting. Show the actual BoP-P values for each group with confidence intervals.

2. **Add a brief justification or discussion of the normality assumption** for Theorem 2. Even a one-paragraph argument (e.g., by a central-limit-theorem heuristic on the difference of squared errors) and an acknowledgment of the assumption's limitations would improve the paper.

3. **Either demonstrate the tightening of Theorem 1** (e.g., a small table comparing the two bounds for representative N, k, ε) or remove the claim and state the bound is derived independently.

4. **Add the incomprehensiveness-based BoP-X formulas** to Section 4.2, or at minimum add a sentence noting they follow analogously from the sufficiency formulas.

5. **Remove or fill Corollary 3.**

6. **Add a limitations paragraph** to the conclusion, flagging the single-dataset illustration, the normality assumption, and the need for further validation across diverse settings.

---
