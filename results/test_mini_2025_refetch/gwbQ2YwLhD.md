## Summary

This paper investigates how variable scaling can cause structure learning algorithms that optimize square-based or log-likelihood-based losses to prefer incorrect DAGs. It extends prior results (Loh & Bühlmann, 2014; Reisach et al., 2021) by providing exact theoretical conditions under which MMSE is minimized by wrong DAGs for *d*-dimensional chains, forks, and colliders (Propositions 2–6). It then shows that log-likelihood based losses (BIC, ELBO) reduce to MMSE under Gaussian noise assumptions (Propositions 7–10), thus inheriting the same scaling sensitivity. Experiments on synthetic data and the Sachs et al. (2005) dataset confirm the theoretical predictions across multiple structure learning algorithms (NOTEARS, DAG-GNN, Gran-DAG, GES).

## Strengths

1. **Generalization of variance-sensitivity results to *d*-dimensional chains, forks, and colliders.** Propositions 2–6 provide exact inequalities (involving variances and covariances) under which the MMSE-minimizing DAG differs from the ground truth for chains (Prop. 2–3), forks (Prop. 4), Markov equivalence classes (Prop. 5), and colliders (Prop. 6). These go substantially beyond the 2-node setting of prior work.

2. **Demonstration that log-likelihood–based losses (BIC, ELBO) are also scale-sensitive.** Propositions 7–10 show that under the Gaussian noise assumption common in the literature, optimizing log-likelihood, BIC, or ELBO reduces to optimizing MMSE, and therefore inherits the same variance-driven failures. This extends the vulnerability from square losses to the loss families most widely used in score-based structure learning.

3. **Empirical confirmation across multiple state-of-the-art algorithms.** Table 1 reports that under artificially imposed scaling, NOTEARS, DAG-GNN, Gran-DAG, and GES predict the wrong DAG in the large majority of tested cases (100% for NT/DG/GND across both linear and non-linear configurations). This directly supports the theoretical analysis and shows the effect is not algorithm-specific.

4. **Honest acknowledgment of scope.** The paper explicitly states in Section 3.2.2 (line 156–157) that deriving non-linear conditions analogous to Props. 2–6 is left for future work, and in the conclusion (lines 239–240) acknowledges the limitation of the (A1) assumption. This candor allows readers to correctly calibrate the contributions.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical generalization beyond chains/forks/colliders is not formally justified.** Remark 1 (lines 66–67) states that "each DAG can be decomposed into subgraphs fulfilling (A1) Immiscible Structures" but only if "we do not allow for such structures" where nodes are simultaneously a fork and a collider. This is effectively a restriction to a subclass of DAGs, not a rigorous decomposition argument. The claim that this "allows us to reason about far more complex graphs" is therefore overstated. The experiments with random DAGs (Q3) partially address this gap empirically, but the theory itself only covers the three basic structures. The paper's honest limitation statement in the conclusion (lines 239–240) mitigates this somewhat, but the main text still asserts more generality than the proofs deliver.

2. **The non-linear theoretical contribution is narrower than the paper's framing suggests.** Propositions 7–10 show that log-likelihood losses reduce to MMSE under Gaussian noise, but they do **not** derive conditions (analogous to Props. 2–6) under which the wrong DAG is *guaranteed* to be preferred in the non-linear case. The paper acknowledges this (line 156–157), yet the abstract claims "we provide conditions under which square-based losses are minimal for wrong DAGs in *d*-dimensional cases" and "also show that scale can impair performance...for non-linear...log-likelihood based losses." The latter is a weaker claim (showing *can* happen, not *when* it will), which is supported by experiments but not by the same kind of exact theoretical characterization. This asymmetry between the abstract's phrasing and the delivered content could mislead readers about the depth of the non-linear results.

### Minor

1. **Experiments test only deliberately engineered worst-case scaling, not practical frequency.** The synthetic experiments (Q1, Q2) choose scaling factors that match the variance ordering the theory predicts will cause a flip. This correctly validates the theory, but it does not address the practically relevant question: over the space of *natural* scalings (e.g., those corresponding to real measurement units), how often would this effect actually mislead practitioners? The paper would be strengthened by varying scaling factors continuously and reporting the proportion of flips, or by testing on real datasets with known ground truth (e.g., from DREAM challenges).

2. **The real-world experiment (Q4) on Sachs data measures change in algorithm output, not correctness.** The paper acknowledges that the ground truth DAG is unknown (line 233). The protocol shows that scaling *changes* the predicted graph, but cannot establish that the scaled prediction is *wrong* (relative to the true causal structure). This limits the strength of the real-world evidence. A dataset with a known causal DAG would have been a more powerful demonstration.

3. **SRL only applies to discrete structure learners.** The Scale-Robust Loss (Section 3.3) subtracts variances of root nodes, which requires knowing which nodes have no parents. The paper correctly notes (line 178) that this does not work for continuous learners (NT, DAG-GNN, Gran-DAG) where all nodes initially have parents in the optimization. Since the paper's main experiments focus on continuous learners, SRL's utility is limited. This is acknowledged but leaves the paper's proposed mitigation applicable only to one of the four tested algorithms.

### Trivial
None beyond parser artifacts that are not author errors.

## Nice-to-Haves

- A continuous sweep of scaling factors (e.g., from 1× to 100×) with the proportion of wrong predictions plotted against the scale ratio would give practitioners practical guidance on the "danger zone" where flips occur.
- Reporting standard deviations or confidence intervals for the experimental percentages (especially the non-100% GES/GESR results) would improve the experimental presentation.
- A real-data experiment with a known ground-truth DAG (e.g., from a simulated biological pathway or the bnlearn repository) would strengthen the practical evidence.

## Removed Points

- *Criticism about the medical example (Figure 1) not involving scaling* — the medical example is purely motivational; it illustrates why getting the DAG right matters, not that scaling is involved. The reviewer misread its purpose.
- *Complaints about missing error bars for 100% results* — 30 replications yielding 100% means zero observed variance; this is a valid result, not a flaw.
- *Allegations of table formatting errors (multiple percentages per cell)* — the table columns (ch, fo, co) label what graph type was predicted; the three numbers in GESR rows correspond to prediction rates for each target graph type. Parser artifacts from PDF extraction, not author errors.
- *Criticism about missing related work* — I cannot verify what related work exists or does not exist.
- *Complaint about reproducibility / unverifiable GitHub code* — Hard Rule: cited entity is assumed to exist.
- *Demand for discussion of other scaling types (standardization, normalization, log transforms)* — scope creep; the paper's analysis is about multiplicative scaling as a model of measurement unit changes.
- *Criticism that Proposition 3's condition is "not very interpretable"* — a mathematical condition does not need heuristic interpretation; it is stated precisely and correctly.
- *Complaint that the non-linear theory "does not derive conditions for when a wrong DAG will be preferred"* — the paper explicitly acknowledges this as a limitation (line 156–157). The strength finder and the paper's abstract accurately distinguish what is and isn't proven for the non-linear case.
- *Criticism about SRL being incomplete* — the paper clearly states SRL is limited to discrete learners and that extending it is future work. This is appropriate scope-delineation, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely confirm the paper's stated results and limitations without offering observations that the paper itself does not contain.

## Suggestions

1. **Explicitly bound the theoretical scope.** In Section 2.1 and again in the abstract, state clearly: "The theoretical conditions (Props. 2–6) apply to DAGs composed of a single chain, fork, or collider. Generalization to arbitrary DAGs is supported empirically but not theoretically proven." This would prevent any misreading of the contribution's generality.

2. **Add a continuous scaling experiment.** Vary the scaling factor for a single variable over a range (e.g., 1×, 2×, 5×, 10×, 20×, 50×) and plot the proportion of incorrect predictions. This would give practitioners a concrete sense of the scale discrepancy needed to cause failures.

3. **Tone down the non-linear claim in the abstract.** Replace "we also show that scale can impair performance of structure learners if relations among variables are non-linear for both square based and log-likelihood based losses" with "we show empirically that scale impairs performance under non-linear relations, and prove theoretically that log-likelihood losses inherit MMSE's scale sensitivity via Gaussian equivalence." The current phrasing could be read as promising conditions analogous to the linear case, which are not delivered.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/4P76wCt9N5.md` | 3.00 | R1 weak | Much weaker; algorithmic proposal without sound theory |
| `/home/wg25r/review_agent/human_reviews/V42LZPlorE.md` | 3.40 | R1 weak | Weaker; narrower scope, less rigorous theory |
| `/home/wg25r/review_agent/human_reviews/JzFLBOFMZ2.md` | 3.20 | R1 weak | Weaker; less rigorous empirical methodology |
| `/home/wg25r/review_agent/human_reviews/oDGkq0AleM.md` | 3.00 | R1 weak | Unrelated topic (anomaly detection) |
| `/home/wg25r/review_agent/human_reviews/ZDoaLbOFaP.md` | 3.00 | R1 weak | Unrelated topic |
| `/home/wg25r/review_agent/human_reviews/aXuWowhIYt.md` | 7.00 | R2 high | Stronger; cleaner contribution with practical solution, better experiments |
| `/home/wg25r/review_agent/human_reviews/KWO8LSUC5W.md` | 5.60 | R1 mid | Comparable; both have genuine contributions but notable limitations |
| `/home/wg25r/review_agent/human_reviews/iaP7yHRq1l.md` | 5.50 | R1 mid | Comparable; similar experimental rigor concerns, less theoretical depth |
| `/home/wg25r/review_agent/human_reviews/UAkVjK00Wv.md` | 4.75 | R1 mid | Weaker; withdrawn paper with less rigorous evaluation |
| `/home/wg25r/review_agent/human_reviews/or8wkKoBP4.md` | 4.00 | R1 mid | Weaker; less clean theoretical contribution |
| `/home/wg25r/review_agent/human_reviews/xByvdb3DCm.md` | 8.00 | R1 strong | Much stronger; oral-level paper on causal discovery |
| `/home/wg25r/review_agent/human_reviews/pOoKI3ouv1.md` | 8.00 | R1 strong | Much stronger; oral-level paper |
| `/home/wg25r/review_agent/human_reviews/xbUlKe1iE8.md` | 4.80 | R2 low | Weaker; less direct relevance |
| `/home/wg25r/review_agent/human_reviews/V1GM9xDvIY.md` | 7.00 | R2 high | Stronger; cleaner methodological contribution |
| `/home/wg25r/review_agent/human_reviews/8muemqlnG3.md` | 6.50 | R2 high | Stronger; cleaner empirical results for a new method |
| `/home/wg25r/review_agent/human_reviews/lk2Qk5xjeu.md` | 7.00 | R2 high | Stronger; more impactful theoretical framing |

**Round 1 bracket:** 4.5 – 6.5  
**Round 2 narrowing:** The paper is weaker than the iSCM paper (7.0) due to the hand-wavy (A1) generalization, incomplete non-linear theory, and limited practical solution (SRL). It is comparable to COSMO (5.6) and the Robustness paper (5.5) — all three have solid contributions with real but non-fatal limitations. It is stronger than the withdrawn Auto-Ensemble paper (4.75) and Doubly Robust (4.8).

The paper's genuine theoretical contribution (extending variance-sensitivity to *d*-dimensional chains/forks/colliders and to log-likelihood losses) is valuable, but the limitations in theoretical generality, non-linear conditions, and experimental scope keep it from being a stronger paper. The final score is positioned just below the mid-point of the bracket to reflect that the paper's core theoretical claims are narrower than its framing suggests.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>