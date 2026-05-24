Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper presents a novel method for unsupervised evaluation of anonymous record linkage by deriving observable lower bounds on precision and relative recall, exploiting a structural constraint that individuals can have at most one positive outcome (e.g., originate only one first-lien mortgage). The approach is method-agnostic and enables hyperparameter tuning without labeled data. The authors instantiate it with hierarchical clustering on 65.5M confidential HMDA mortgage applications, reporting an estimated 92.3% precision at their preferred specification, with simulation evidence showing the bound closely tracks true precision.

## Strengths

1. **Clever theoretical contribution — observable precision bound from a structural constraint.** Theorem 1 derives $\Pr[\text{False}] \leq \Pr[\text{Mult}]/p^2$ using only the observed fraction of clusters with multiple originations and the unconditional origination probability. This is a genuinely novel idea: using the at-most-one-origination constraint to turn a data artifact (multiple-origination clusters) into a diagnostic signal. (§2.2, Theorem 1)

2. **Simulation convincingly validates the bound under the assumed DGP.** Figure 4a shows the implied precision (from the bound) closely tracks the true precision (Figure 3a) across tuning parameters $\varepsilon$, with the "with date" specification achieving ~93.7% implied precision at $\varepsilon=0.06$ versus ~95% true precision. This confirms the bound is not just theoretically sound but practically tight in an idealized setting. (§3.1, Figures 3a, 4a)

3. **Method-agnostic framework enabling tuning and model comparison without labels.** Corollaries 1 and 2 show that ranking specifications by $\hat{\alpha}(\theta)N^+(\theta)$ is equivalent to ranking by recall (up to an unknown constant $P_{\text{tot}}$), and similar bounds exist for $F_\beta$ and weighted precision-recall scores. This means the framework applies to *any* label-generating algorithm. (§2.2, Corollaries 1, 2)

4. **Practical large-scale application.** The method is implemented on 65.5 million applications using efficient $\mathcal{O}(\ell^2)$ agglomerative clustering (fastcluster). The application to HMDA data is societally relevant, and the paper identifies three concrete downstream uses (fairness measurement, monitoring lending standards, studying shopping behavior). (§4, §5)

## Weaknesses

### Major

1. **Assumptions behind the precision bound are neither validated nor tested for robustness.** Theorem 1 requires Assumption 1 (independence of origination decisions across borrowers) and Assumption 2 (weakly increasing origination probability). The paper states these "do not appear very strong to us" (Section 2.2) but provides no empirical check, sensitivity analysis, or even a qualitative discussion of when they might fail. The simulation operates under the same assumptions, so it does not test robustness. In practice, if origination decisions are positively correlated (e.g., due to common rate movements or local economic shocks), the bound is conservative — but this is not discussed. If negative correlation exists (e.g., lender capacity constraints), the bound could fail. Without any robustness analysis, the 92.3% headline figure from the HMDA application remains a mathematical deduction under unverified assumptions, not an empirically grounded estimate.

2. **No external or ground-truth validation of clusters in the real data application.** The main text states "We perform additional diagnostics...in the Appendix" but provides no summary of what those diagnostics show. Beyond the bound itself, there is no evidence in the visible portion of the paper that the clusters actually correspond to same-person pairs — no small labeled audit, no manual inspection, no comparison with an external name-address source. While the bound is a statistical guarantee under the assumptions, its interpretation as "92.3% of clusters are true cross-applicants" would be substantially strengthened by even a small-scale validation.

### Minor

1. **The "observable" recall bound claim is slightly over-stated.** Corollary 1 gives $\text{Recall}(\theta) \geq \hat{\alpha}(\theta) N^+(\theta)/P_{\text{tot}}$ where $P_{\text{tot}}$ is unknown, so the absolute recall value is not observable. The paper correctly notes the bound is proportional to the observable $\hat{\alpha}(\theta)N^+(\theta)$ and can be used for ranking. However, the abstract's phrasing — "observable lower bounds on both precision and relative recall" — could mislead readers into thinking absolute recall is bounded. The technical content is sound; the framing in the abstract and introduction could be more precise.

2. **No baseline comparison in the HMDA application.** Figure 5 shows the precision-sample-size frontier for the proposed method's 96 tuning combinations, but there is no reference curve (e.g., exact matching on a subset of categorical variables, or random clustering) to contextualize the reported numbers. A simple deterministic baseline would help the reader assess whether the method adds value over trivial alternatives.

3. **Selection of the 96 distance/ε combinations is not justified.** The paper mentions 96 combinations of distance functions and tolerance parameters but provides no rationale for how these were generated, whether they are exhaustive, or whether any systematic search was performed. This makes the tuning process difficult to reproduce or assess for completeness.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis that varies the baseline origination probability $p$ or introduces correlation across origination decisions (even a simple simulation with positively/negatively correlated $O_{im}$) would substantially strengthen confidence in the bound's practical applicability.
- Including a brief summary of the appendix diagnostics in the main text (e.g., "In a manual review of 200 clusters, X% showed consistent name/address patterns") would make the real-data results more compelling.

## Removed Points

- **"Clusters could contain different individuals who by chance avoid multiple originations, so the bound cannot rule out systematic misclassification."** REMOVED — This misunderstands what a lower bound guarantees. The bound $\Pr[\text{False}] \leq \Pr[\text{Mult}]/p^2$ provides a mathematical guarantee on the *overall* false positive rate; it does not claim to certify individual clusters. The bound's validity does not require per-cluster certainty. This is how all statistical bounds operate.

- **"The paper never demonstrates applicability beyond the mortgage case."** REMOVED — Scope creep. The paper uses mortgage as one concrete application, states the framework is domain-agnostic, and lists other domains (insurance, college admissions, job offers). Criticizing the absence of empirical demonstrations in unrelated domains asks the paper to do more than it set out to do.

- **"Additional diagnostics referred to in the appendix are not visible."** REMOVED — Per instructions: the appendix was stripped by the parser. The paper references it; the content exists in the original submission.

- **"The notation in Equation (1) is confusing."** REMOVED — Minor presentation issue. The formula is substantively correct; the notation is consistent with standard probabilistic notation in the paper.

- **"The simulation does not test robustness"** (as a standalone weakness) — MERGED into Major Weakness #1 (assumption validation), not treated as a separate point.

## Novel Insights

The paper's core insight — that a structural at-most-one constraint can transform a nuisance (multiple-origination clusters) into a diagnostic signal for unsupervised evaluation — is genuinely clever and transportable to many domains. The key tension this review surfaces is between the mathematical cleverness of the bound and the empirical credibility of its real-world application. The bound is provably correct under its assumptions, and the simulation shows it works in a controlled setting. But the leap to "92.3% precision in HMDA data" skips over the crucial step of verifying those assumptions or providing convergent evidence. The paper would be substantially stronger not by doing more math, but by doing more empirical due diligence on a single, well-chosen application.

## Suggestions

- **Add a robustness analysis for Assumptions 1 and 2.** For example: (a) artificially introduce positive/negative correlation in origination decisions in the simulation and track whether the bound degrades gracefully; (b) provide a qualitative discussion of the direction and likely magnitude of assumption violations in the HMDA context, including the empirical origination autocorrelation within census tracts.
- **Include a small-scale ground-truth validation.** Even auditing 100-200 clusters manually (using name/address data available to the data provider but not in the public file) and reporting the precision would transform the paper's empirical section.
- **Add a deterministic baseline** (e.g., exact match on a subset of categorical variables like census tract × property type × loan purpose) to contextualize the frontier in Figure 5.
- **Clarify the abstract** to say "observable precision bound and a ranking-based recall criterion" rather than "observable lower bounds on both precision and relative recall."

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>