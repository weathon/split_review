Now I have a good understanding of the paper and the calibration landscape. Let me write the consolidated review.

**Round 1 bracket:** Based on the calibration anchors, the plausible range for this paper is roughly 4.0–6.0. Papers in the 3.0–4.0 range have more fundamental correctness or clarity problems. The paper under review is clearly better than those — it has a genuinely novel idea and a clean application on real large-scale data. However, it falls short of the 6.5 anchor (PU learning benchmark accepted as poster), which had more thorough empirical validation across multiple methods. The paper under review has a theoretical concern that prevents it from reaching that tier.

**Round 2 narrowing:** Within the 4.0–6.0 bracket, the conformal prediction bounds paper (5.0, rejected) serves as a useful comparator. That paper had clean theory but limited experiments and practical actionability concerns. The current paper has a more creative theoretical contribution and stronger empirical demonstration, but also has an unresolved theoretical gap. Comparing against the 4.67 anchor (accepted poster, subspace clustering) which had correctness concerns in its proofs but was accepted — the current paper is better presented and more practically relevant, but its theoretical gap is more central to the contribution. I place it at 5.0.

---

## Summary

This paper proposes a method for evaluating unsupervised record linkage without labeled data by exploiting a structural constraint: an individual can originate at most one first-lien mortgage. The authors derive observable lower bounds on precision and relative recall using only the unconditional origination probability and the fraction of clusters with multiple originations. They demonstrate the approach on 65.5M HMDA mortgage applications, reporting 92.3% estimated precision using a hierarchical agglomerative clustering algorithm.

## Strengths

- **Derives observable lower bounds on precision and relative recall without labels** (Theorem 1, Corollary 1, Section 2.2). The bounds depend only on the empirically estimable rate of multiple originations Pr[Mult] and the unconditional origination probability p, enabling principled model evaluation and tuning when no ground-truth labels exist. This is a genuinely novel methodological contribution.

- **Validates the bounds via simulation** (Section 3, Figures 3a vs. 4a). The true precision and the lower-bound estimate show close agreement — e.g., at ε=0.06 with the date variable, the bound is 93.7% vs. true precision ~95%. This provides concrete evidence that the bounds are informative in a controlled setting.

- **Demonstrates practical utility on a large-scale real dataset** (Section 4, Figure 5). On 65.5M HMDA applications, the preferred specification identifies 314,344 cross-applicant clusters with an implied precision of 92.3%. The scale of the application and the use of confidential HMDA data are strengths.

- **Domain-agnostic framework with clear analogies** (Section 1). The paper identifies other settings where the same structural constraint applies (insurance, college admissions, job offers), showing generality beyond mortgage data.

- **Clean presentation of the precision-sample-size frontier** (Figure 5). The trade-off between precision and recall is visualized clearly, and the preferred specification is motivated by the knee of the frontier.

## Weaknesses

### Major

1. **The core theoretical bound lacks a fully transparent justification for realistic heterogeneity in the main text.** The bound relies on the inequality Pr[Mult|False] ≥ p². The main text's intuition (paragraph after Theorem 1) treats false positives as random pairs, which is the best-case scenario, not the worst-case. The critic's concern is that if the clustering algorithm systematically pairs low-origination-probability applicants in false-positive clusters (e.g., low-FICO applicants who look similar), then Pr[Mult|False] could be substantially less than p². The paper states that Lemma 1 in the Appendix proves the inequality under Assumptions 1 and 2, but the main text does not explain *how* these assumptions address the selection-into-false-positives problem. Assumption 1 (independence across borrowers) and Assumption 2 (monotonicity in own application count) do not on their face constrain how the clustering algorithm's false-positive rate correlates with origination probability. Since the Appendix is not visible, the reader cannot verify whether the bound is proven under conditions that cover realistic scenarios. *Why this matters:* If the bound is not generally valid, the claimed 92.3% precision may be a substantial overestimate, and the entire evaluation framework loses its foundation. The simulation (Section 3) validates the bound in one favorable setting but does not stress-test it under adverse selection where false positives concentrate among low-probability applicants.

2. **The recall claim for the real application is unsubstantiated.** Corollary 1 gives a lower bound on recall proportional to α̂(θ)N⁺(θ)/P_tot, but P_tot (the true number of cross-applicants) is unknown in the real data. Therefore, no numeric recall — not even a lower bound — can be reported for the HMDA application. The abstract and conclusion claim "only minimal loss in relative recall" without any quantification on real data. The 92% recall figure from the simulation (Section 3) does not transfer to the real application because P_tot is unknown and the data distribution differs. *Why this matters:* A central claim of the paper is unsupported for its main empirical demonstration.

3. **The model-comparison claim is not demonstrated.** The paper advertises that the bounds enable "both hyper-parameter tuning and cross-model comparisons" (Abstract, Introduction). However, the application uses only a single clustering algorithm (hierarchical agglomerative with complete linkage), varying only the distance function and threshold ε. This demonstrates tuning, not cross-model comparison. To substantiate the claim of model-agnostic comparability, the paper would need to apply the bound to at least one fundamentally different algorithm (e.g., DBSCAN, k-means) and show the ranking is sensible. *Why this matters:* A stated contribution of the paper remains speculative.

4. **The restriction to size-2 clusters is a significant limitation that is under-discussed.** Footnote 4 states that all clusters with more than two applications are dropped, meaning the method only captures cross-applicants who submit exactly two near-identical applications. Cross-applicants who submit three or more applications are systematically excluded, which likely lowers the true recall relative to what the bound suggests. The paper does not quantify how many cross-applicants this excludes or discuss how this limitation affects the conclusions. *Why this matters:* The method's coverage of the target phenomenon is substantially weaker than implied.

### Minor

1. **The adjusted bound (Equation 2)** drops clusters with multiple originations and re-estimates precision. The derivation assumes the remaining false positives have the same Pr[Mult|False] as before. If dropping multi-origination clusters changes the composition of false positives (e.g., leaving only those with very low origination probabilities), the adjusted bound could become unreliable. This should be acknowledged.

2. **The distance function uses equal weighting** of date (in days), income (in $1000s), FICO (in points), and LTV across five variables in a weighted ℓ₂ norm. Equal weighting of such different scales and units may not be appropriate. The paper explores 96 combinations of distance functions and thresholds but does not discuss sensitivity to the choice of variable weights within the distance function itself.

3. **The independence assumption (Assumption 1)** is strong for mortgage markets, where origination probabilities are correlated through common economic conditions, lender policies, and regional shocks. The paper does not discuss robustness to violations of this assumption (e.g., positive correlation would strengthen the bound, but negative correlation could weaken it).

### Trivial

- None that survive filtering — the presentation is clean.

## Nice-to-Haves

- A stress-test simulation where false-positive clusters are designed to pair low-origination-probability applicants would strengthen confidence in the bound's robustness.
- Reporting actual runtime of the clustering algorithm on 65.5M applications would help practitioners assess feasibility.
- A comparison to a simpler baseline (e.g., exact matching on a subset of variables) would contextualize the complexity of the clustering approach.
- Bootstrap confidence intervals for the precision bound would quantify estimation uncertainty.

## Removed Points

- **Criticism about the bound being "not generally valid" and "the core theoretical result is not justified" — kept as Major #1.** These are serious concerns, but I downgraded them from "fatal" to "major" because (a) the paper claims Lemma 1 in the Appendix addresses this (inaccessible), and (b) the simulation provides some empirical support. I have framed the weakness as a *lack of transparent justification in the main text* rather than a definitive proof that the bound is wrong.

- **"The bound fails if the clustering algorithm creates false positives with low-probability applicants" (concrete example)** — Merged into Major #1.

- **"No numeric recall for real data"** — Kept as Major #2.

- **"Model comparison not demonstrated"** — Kept as Major #3.

- **"Size-2 cluster limitation"** — Kept as Major #4.

- **"The adjusted bound's assumption about remaining false positives"** — Kept as Minor #1.

- **"Distance function weighting"** — Kept as Minor #2.

- **"Independence assumption discussion"** — Kept as Minor #3.

- **"Statistical significance / confidence intervals"** — Moved to Nice-to-Haves. This is not standard practice for clustering applications at this scale.

- **"Comparison to simpler baseline"** — Moved to Nice-to-Haves. Not a core flaw.

- **"Computational scalability / runtime"** — Moved to Nice-to-Haves. The O(ℓ²) complexity is stated; actual runtime is helpful but not essential.

- **"Overselling in abstract"** — Removed. The abstract's claim about recall is slightly imprecise but not deceptive — the recall claim is explicitly stated to be from the simulation where it can be computed.

- **"Missing related works"** — Removed per instructions.

- **"Typos / formatting"** — Removed per instructions (parser artifacts).

- **"Monotonicity assumption discussion"** — Merged into Minor #3 (Assumption 1 discussion). The monotonicity assumption (Assumption 2) is actually less concerning than the independence assumption.

- **Strength: "This paper addressed an important problem"** — Removed as too generic.

- **Strength: "Enables hyperparameter tuning without labels"** — Kept as Strength #1 (merged into the main contribution). Already covered by the first strength.

- **Strength: "Uses a scalable agglomerative clustering implementation"** — Removed as too generic and not central to the contribution.

- **Strength: "Identifies a domain-agnostic structural constraint"** — Kept as Strength #4.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's elegant theoretical framing and the practical difficulty of ensuring the bound holds under realistic data heterogeneity, but this tension is already implicit in the paper's reliance on Lemma 1 (deferred to the appendix).

## Suggestions

1. In the main text, provide a clear intuitive argument for why Pr[Mult|False] ≥ p² holds even when the clustering algorithm selects non-random pairs into false positives. If Lemma 1 uses a convexity or Jensen-type argument (e.g., that the clustering of similar applicants induces positive covariance in origination probabilities within false-positive clusters), state this explicitly in the main text.

2. Add a stress-test simulation where the clustering algorithm is forced to create false positives predominantly among low-origination-probability applicants, and show that the bound remains conservative.

3. Acknowledge the size-2 cluster limitation more prominently, and discuss the fraction of cross-applicants likely excluded by this restriction (e.g., from the empirical distribution of application counts in the data).

4. Report at least a range or upper bound for recall on the real data. Even if P_tot cannot be pinned down, a sensitivity analysis over plausible values of P_tot would give the reader a sense of the recall lower bound's magnitude.

5. Apply the bound to one additional clustering algorithm (e.g., DBSCAN with different parameters) to demonstrate cross-model comparability, even if only on a subset of the data.

---

Calibration anchors consulted:

| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| h4hIuid0HY | 3.00 | R1 | Weaker — SRP-LSH performance modeling paper, rejected; less novel contribution |
| FmLGEJEvJ9 | 3.00 | R1 | Weaker — DP string distances, rejected; different problem |
| hi6opqxk5X | 2.80 | R1 | Weaker — density-based clustering, rejected; limited novelty |
| fQIE4NJOVm | 5.20 | R1 | Comparable — embedding dimension bounds, rejected; theoretical but less applied |
| XvWe1P7P8A | 5.50 | R1 | Comparable — similarity-based weakly supervised learning, rejected; nice theory but limited |
| 5R11h5o44C | 6.50 | R1 | Stronger — PU learning benchmark, accepted poster; more thorough empirical validation |
| uQ45zJJDiH | 4.00 | R1 | Weaker — unsupervised LLM evaluation, rejected; misleading claims |
| I3spHvRHqo | 4.00 | R2 | Weaker — test error bounds for DNNs, rejected; presentation issues |
| Pjcz6ik78E | 4.67 | R2 | Comparable — subspace clustering preservation, accepted poster; had proof correctness concerns but was accepted |
| YM6KIpl6aR | 5.00 | R2 | Comparable — conformal prediction bounds, rejected; clean theory but limited practice |

Round 1 bracket: 4.0 – 6.0
Round 2 narrowing: Compared to the 4.67 anchor (accepted poster with proof concerns) and the 5.0 anchor (rejected conformal prediction bounds paper), the paper under review has a more creative core idea and stronger empirical demonstration than the latter, and is more practically relevant than the former. However, its main theoretical gap (bound validity under heterogeneity) is closer to the surface than in those papers. Final score: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>