Now I have all the information needed. Let me construct the final consolidated review.

**Calibration Round 1 (Bracketing):**
- Low band (score < 3.5): Too weak — irrelevant papers about contracts, crowds.
- Middle band (3.5–7.5): Data Valuation (6.0), Vendiscope (5.0), SMI Critique (6.5), IEM (7.0), AbC (6.5), Conformal w/ Corrupted Labels (6.0).
- High band (> 7.5): Papers on angle testing, LLMs, transducing — not topically similar; no good anchors.

**Initial bracket:** 5.0–7.0

**Calibration Round 2 (Narrowing):**
- Data Valuation (6.0): Theory + experiments, some experimental gaps, accepted poster. Our paper has stronger theory (axiomatic + impossibility + uniqueness) but weaker experiments (no baselines).
- Conformal w/ Corrupted Labels (6.0): Strong theory on corrupted labels, accepted poster. Similar quality — theory stronger than experiments.
- SMI Critique (6.5): Strong theoretical critique with clean experiments, accepted poster. Our theory is comparable in depth but experiments are weaker.
- AbC (6.5): Axiomatic approach + experiments, accepted poster. Similar structure but more comprehensive experiments.

**Final calibrated score: 6.0** — Comparable to the Data Valuation and Conformal Prediction papers (both 6.0, accepted posters). The theory is genuinely novel and stronger than what a typical 6.0 paper offers, but the experimental evaluation is noticeably weaker (no baselines, small-scale real-data experiment). These balance to a solid 6.0.

---

## Summary

This paper introduces a novel problem — reliability scoring for datasets when ground truth is inaccessible but auxiliary observations from an unknown experiment are available — and proposes the Gram determinant score as a solution. The score measures the volume spanned by vectors describing the joint distribution of reported data and experiment outcomes. The paper proves that the score preserves three ground-truth-based reliability orderings (exact match, Blackwell, approximate Hamming), provides a uniqueness characterization (experiment-agnosticism up to scaling), and gives matching impossibility results showing the conditions are nearly tight. A plug-in estimator with asymptotic guarantees and a kernel extension are provided, with experiments on synthetic data, CIFAR-10 embeddings, and real employment data.

## Strengths

- **Strong axiomatic characterization with matching impossibility results.** The paper proves that the Gram determinant preserves exact-match, Blackwell, and approximate-Hamming orderings under linearly independent experiments (Theorem 4.2), while Proposition 3.1 shows that these conditions are nearly necessary — no score can preserve Hamming ordering under diagonally dominant misreport matrices, and no score can preserve exact-match ordering beyond non-permutation misreports. This tightness gives the theoretical analysis unusual depth.

- **Experiment-agnostic uniqueness result.** Proposition 4.3 proves that the Gram determinant score is, up to scaling, the unique continuous score that yields the same dataset ranking regardless of which linearly independent experiment is used. This is a genuinely distinctive property derived from the determinant's multiplicative structure (Eq. 4: $\Gamma(PQ) = \det(P^\top P)\det(Q)^2$) and is not shared by obvious alternatives.

- **Clean geometric interpretation.** The Gram determinant naturally measures the squared volume of the parallelepiped spanned by column vectors of $PQ$, with a clear geometric intuition: as reported data deviate further from the truth, the convex combinations of columns shrink the volume, decreasing the score.

- **Practical estimator with clean theory.** The plug-in estimator (Definition 4.4) is simple to compute from observed co-occurrence data and asymptotically preserves all orderings from Theorem 4.2 (Proposition 4.5). The kernel extension (Definition 4.6) handles continuous observation spaces, demonstrated on CIFAR-10 embeddings.

## Weaknesses

### Major

- **No baseline comparisons in the main empirical evaluation.** Since the paper introduces a new problem, there are no direct competitors, but the experiments only show that the Gram score is monotonic with respect to corruption level. Simple baselines — e.g., average inner product of embeddings conditioned on reported labels, total correlation, or the determinant of the empirical covariance of $y$ given $\hat{x}$ — would help establish that the Gram score captures non-trivial structure. The paper mentions (in the conclusion) that Appendix G discusses additional candidates, but this comparison is not in the main text, and the reader cannot judge whether the Gram score behaves differently from naive alternatives. Without baselines, the experiments demonstrate consistency but not superiority or unique utility.

- **Finite-sample behavior is uncharacterized.** The conclusion states "finite-sample guarantees" but Proposition 4.5 only provides asymptotic guarantees. No finite-sample bounds, convergence rates, or confidence intervals are given for the plug-in estimator. The synthetic experiment (Fig. 2d) shows that ranking accuracy is around 0.6–0.7 for $N=250$, which may not suffice for many applications, but the paper offers no guidance on sample size selection or uncertainty quantification. The stratified matching estimator mentioned in Section 4.2 is deferred entirely to the appendix.

### Minor

- **Experimental description inconsistency: row-stochastic vs. column-stochastic.** The theory (Section 2.1) defines the experiment $P$ as column-stochastic (columns sum to 1). The synthetic experiment (Section 5) states: "the experiment distribution matrix $P \in [0,1]^{d\times d}$ is constructed by sampling $P(i,j) \sim \text{Uniform}(0,1)$ independently and normalizing **rows** to be stochastic." The Figure 1 example uses a column-stochastic matrix. This discrepancy is almost certainly a description error (the example and the sensible results suggest columns were correctly normalized in the implementation), but the confusion should be resolved. The authors should clarify the exact construction to ensure the theory-experiment link is unambiguous.

- **Score is limited to discrete label spaces $\mathcal{X}$ with no clear path to continuous domains.** The Gram determinant score is defined over a finite set $\mathcal{X} = [d]$. While the kernel extension handles continuous $\mathcal{Y}$, the label space $\mathcal{X}$ remains discrete. The paper acknowledges this in the conclusion but does not discuss whether discretization strategies preserve the ordering properties, making the contribution narrower than the title "Data Reliability Scoring" suggests.

- **Employment experiment has limited scope.** With only $N=209$ months and four quantile buckets, and no error bars or significance tests reported for the differences between vintages, this experiment demonstrates feasibility but not statistical reliability.

### Trivial

- Figure 2d reports fraction correctly ranked averaged over 1000 datasets but does not show variance or confidence intervals.

## Nice-to-Haves

- Testing a non-linear kernel (e.g., RBF) on the CIFAR-10 embeddings would strengthen claim that the kernel extension is general.
- A brief discussion of computational cost for large-scale settings ($N=10^5, d=1000$) and potential approximations (random features, Nyström) would improve practical utility.

## Removed Points

- **"Score is limited to discrete label spaces" (weakened from Major to Minor).** The paper's title and framing are appropriately scoped: the method targets categorical data ($\mathcal{X}=[d]$), which covers many real-world settings (labels, ratings, categories). The discrete-$\mathcal{X}$ limitation is acknowledged in the conclusion, and the problem of continuous-label reliability scoring is explicitly left as future work. Many impactful methods (e.g., mutual information estimators, proper scoring rules) also make domain assumptions; the paper is not misleading about its scope.

- **"Row-stochastic issue is structural/fatal" (removed).** The example in Figure 1 (footnote 5) shows a column-stochastic $P$, and the experimental results are clean and monotonic. The description likely uses a different indexing convention ($P(i,j) = P(y=j|x=i)$ with rows normalized) that is equivalent to the theory's column-stochastic convention for square matrices. This is a presentation imprecision, not a methodological error that invalidates results.

- **"Blackwell ordering restricted to $\mathcal{Q}_{\text{reg}}$ is a strong assumption" (removed).** The paper explicitly justifies this restriction: Section 2.3 notes that diagonal maximality and invertibility are necessary for Blackwell ordering to be a strict partial order. This is a design choice, not a flaw — the paper is transparent about the restriction and explains its necessity.

- **Various generic formatting/reproducibility nitpicks (removed per instructions).**

## Novel Insights

The key structural insight that emerges from the reviews — and that goes beyond what the paper explicitly highlights — is that the Gram determinant score's strength is also its limitation: the determinant's multiplicative decomposition $\Gamma(PQ) = \det(P^\top P)\det(Q)^2$ is what enables experiment agnosticism, but it also means the score can only capture volume-like (determinant-based) aspects of the joint distribution. The impossibility results (Proposition 3.1) establish that no score can preserve Hamming ordering under $\mathcal{Q}_{\text{dom}}$, while the Gram score gets within a factor of $1/(4L\Delta)$ on $\mathcal{Q}_{L, 1/64L^2 d^2}$. This near-tight characterization suggests that "volume" is close to the only game in town for experiment-agnostic reliability scoring — a finding that future work on continuous-label or non-volume-based scores will need to contend with.

## Suggestions

1. **Add baseline comparisons.** Even simple alternatives (average inner product of $y$ given $\hat{x}$, total correlation, or a naive covariance-determinant score) on the synthetic data would substantially strengthen the empirical claims. The reader needs to see that the Gram score captures structure that simpler scores miss.

2. **Resolve the row-stochastic vs. column-stochastic description in Section 5.** Clarify the exact indexing convention used in the synthetic experiment and confirm it matches the theory's column-stochastic definition.

3. **Provide at least a sketch of finite-sample behavior.** Even a short heuristic discussion (e.g., a matrix Bernstein bound sketch or simulation-based guidance on sample size) would significantly improve the paper's practical value.

## Score and Decision

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**