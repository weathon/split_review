Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces VISTA, a modular framework for causal structure learning that decomposes the global DAG learning problem into Markov Blanket subgraphs, aggregates local predictions via a weighted voting mechanism, and enforces acyclicity through a Feedback Arc Set heuristic. The framework is model-agnostic, parallelizable, and operates purely at the edge level. The paper provides theoretical finite-sample error bounds (under an independence assumption) and asymptotic consistency, along with experiments on synthetic and real (Sachs) data across six base learners.

## Strengths

- **Model-agnostic modularity validated across diverse base learners**: VISTA is tested with six different base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM) under both linear and nonlinear settings across ER and SF graph topologies. Tables 1–2 show consistent F1 improvements over standalone baselines across virtually all configurations, demonstrating that the framework does not depend on the inductive bias of any particular learner.

- **Substantial and consistent runtime reductions**: Table 3 shows large factors of speedup (e.g., NOTEARS from 12,515s to 2,136s at n=300; GraN-DAG from 25,205s to 2,336s). These gains come from the divide-and-conquer design's natural parallelism and are not claimed as an algorithmic innovation, but they are real and practically meaningful.

- **Coverage guarantee provides a clean theoretical foundation**: Proposition 3.1 proves that every true edge appears in the union of MB-induced subgraphs. This is a simple but important guarantee that the decomposition does not lose true edges, providing soundness for the divide stage.

- **Tunable precision–recall trade-off with no retraining cost**: Figure 4 shows smooth precision/recall curves as λ is swept, and cached votes enable full curves without re-running base learners. The use of a fixed operating point (λ=0.5, t=0.7) across all main tables to avoid cherry-picking is good practice.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical analysis rests on an independence assumption that is known to be violated, and the resulting conditions are not practically actionable.** Theorem 3.2 and Corollary 3.3 assume votes from different subgraphs are independent Binomial draws. The paper candidly acknowledges (Section 3.1) that "subgraphs learned from the same dataset can induce correlations among votes, so the bound should be interpreted as a qualitative guide." While transparency is commendable, this admission fundamentally undermines the claim of providing "finite-sample error guarantees." Furthermore, Theorem 3.5 requires the number of subgraphs per edge to grow as m = C log n, but m is determined by the graph's MB structure and the MB solver — it is not a free parameter the algorithm controls, so the condition is not actionable. The theory thus functions more as intuition than as a verifiable guarantee.

2. **Critical sensitivity to Markov Blanket quality is unexamined.** The accuracy of MB identification is the linchpin of the entire pipeline: if MBs miss true neighbors or include spurious ones, the downstream voting operates on incomplete or contaminated input. Yet the paper provides almost no analysis of this dependency. The MB solver used in experiments is never named, and there is no ablation study varying MB quality or comparing different MB estimators. Figure 1 asserts MB accuracy is "relatively stable" but this is a single synthetic experiment with an unidentified solver. For a framework that claims to be "plug-and-play" with respect to MB solvers, the complete absence of sensitivity analysis on this dimension is a significant gap.

3. **The Naive Voting baseline is a weak strawman that inflates the apparent value of Weighted Voting.** VISTA-NV produces FDRs of 0.84–0.95 across nearly all methods in Table 1, meaning the vast majority of its predicted edges are false. Presenting this as a baseline within the main results table (without a strong, upfront caveat that it is catastrophically poor) gives the misleading impression that the step from NV to WV is a principled improvement, when in reality NV is essentially unusable. The paper would be stronger if it compared WV against a more reasonable baseline — e.g., a frequency-threshold rule with majority-vote orientation — to isolate whether the exponential weighting in Eq. (2) adds value beyond simple frequency-based filtering.

### Minor

1. **Improvements for the strongest baseline (NOTEARS) are modest.** For NOTEARS at n=100 (Table 1), VISTA+WV improves F1 from 0.76 to 0.79, while TPR drops from 0.74 to 0.68. The net gain is positive but small. The claimed "notable improvements in both accuracy and efficiency" are better supported for weaker base learners (GOLEM, DAG-GNN, GraN-DAG, SCORE) than for NOTEARS.

2. **The weighted voting formula is presented without formal justification.** Equation (2) uses an exponential decay factor (1 − e^{−λm}) as a "soft confidence modulator." While the intuition is clear, no derivation or principled argument connects this specific functional form to any optimality criterion. The paper correctly notes it is "analogous to smoothing priors in Bayesian estimation," but this is an analogy, not a derivation. The theoretical results (Theorems 3.2–3.5) do not depend on the exponential form specifically, but the paper does not discuss whether other weighting schemes would perform similarly.

3. **The real-data (Sachs) results are mixed.** For some methods, TPR drops substantially (e.g., GraN-DAG from 0.53 to 0.29; SCORE from 0.18 to 0.12). While the paper interprets this as a reduction in false discoveries, the trade-off is less clearly positive than in the synthetic experiments. This is addressed as a limitation in the conclusion, but the main text emphasizes the positive interpretation.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing VISTA-WV against a simpler frequency-threshold aggregation (e.g., keep edges appearing in ≥ k subgraphs, resolve orientation by majority) would help isolate the specific contribution of the exponential weighting term.
- A study of MB solver quality vs. final DAG accuracy (e.g., varying MB precision/recall systematically) would strengthen the plug-and-play claim.
- A comparison against alternative parallelization baselines (e.g., random variable partitioning) would clarify that the MB-based decomposition specifically, not just any divide-and-conquer scheme, is responsible for the accuracy gains.
- Empirical verification that the correlation among subgraph votes does not catastrophically inflate error relative to the independent-Binomial bound would significantly bolster the theory.

## Removed Points

These points were flagged by reviewers but are removed or downgraded with justification:

- **"Empirical results do not consistently demonstrate that VISTA improves accuracy"** — Removed. The data in Tables 1–2 show F1 improves across all base learners in nearly all configurations. For NOTEARS (0.76→0.79), GraN-DAG (0.06→0.17), and SCORE (0.14→0.31), the improvements are real, even if some involve precision-recall trade-offs. The critic's framing is not supported by the evidence.
- **"Results may be cherry-picked due to fixed λ, t"** — Removed. The paper explicitly uses fixed hyperparameters to avoid cherry-picking and provides full sensitivity curves in Figure 4. This is methodologically sound.
- **"Proposition 3.1 is trivial"** — Removed. A proposition can be straightforward yet important; coverage guarantees are a necessary foundation for the framework. This is not a weakness.
- **"Weighted voting is an ad-hoc heuristic"** — Weakened to minor. Many empirically successful methods use heuristics; the paper provides clear intuition and the form is reasonable. The lack of formal derivation is noted but this is not a fatal issue.
- **"Missing comparison to DCILP"** — Removed. The appendix containing this comparison was stripped by the parser; the original submission includes it.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a systematic assessment of the theory–practice gap but do not uncover any insight not already present in the paper or the reviewer comments.

## Suggestions

1. **Strengthen the theoretical claims or reframe them.** Either (a) provide empirical evidence (e.g., via bootstrap or simulation) that the independent-Binomial bounds are approximately valid despite vote correlation, or (b) reframe the theory as a qualitative/intuitive analysis and remove statements about "finite-sample guarantees" and "asymptotic consistency" that overclaim relative to what is established. The current framing over-promises.
2. **Name the MB solver and conduct a sensitivity analysis.** Report which MB estimator was used, and vary its parameters or substitute alternative MB estimators to show that final DAG accuracy is robust to MB quality.
3. **Replace or supplement the NV baseline.** Either add a more reasonable baseline (e.g., keep edges with frequency ≥ k, resolve by majority vote) to show that the exponential weighting adds value over simple frequency thresholds, or move NV to the appendix with a clear disclaimer about its expected failure mode.
4. **Disaggregate error sources.** Conduct an experiment comparing edges lost due to MB errors vs. edges lost/gained due to voting errors vs. edges removed by FAS, to clarify where the framework's bottlenecks lie.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xByvdb3DCm.md` | 8.00 (Accept) | Much stronger theoretical foundation, rigorous proofs, clear problem identification. VISTA is substantially below this. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mGmx41FTTy.md` | 6.33 (Reject) | Decent method with clear novelty in using two time-slices. VISTA has more extensive experiments but weaker core contribution. Comparable overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ToveGL9vRN.md` | 5.50 (Reject) | Well-motivated critique of faithfulness with unified evaluation framework. VISTA's empirical scope is broader but its theory is weaker. Roughly comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DUfwD5yiN4.md` | 5.25 (Reject) | Distributed structure learning with theoretical guarantees but limited empirical validation. VISTA has substantially stronger experiments. Slightly above this anchor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Lxst78Rrwj.md` | 5.00 (Reject) | Invariance-based causal discovery with unclear core mechanism. VISTA is more clearly presented and better empirically validated. Comparable or slightly above. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JzFLBOFMZ2.md` | 3.20 (Reject) | LLM-supervised CSL with weak baselines and limited contribution. VISTA is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fSxiromxAq.md` | 3.00 (Reject) | Poor clarity, weak contributions, vague problem definition. VISTA is substantially stronger. |

Positioned relative to these anchors: VISTA is clearly above papers scoring 3–4 and comparable to or slightly above papers scoring 5.0–5.5. Its main advantage over those is the breadth and consistency of empirical validation; its main weakness is theoretical over-claiming relative to what is actually proved. The gap between its advertised "finite-sample guarantees" and the acknowledged independence violation is a real liability that a rigorous rebuttal would need to address. In its current form, the paper is a borderline reject.

**Score**: 5.0  
**Decision**: Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>