Now I have all the information I need. Let me compose the final consolidated review.

## Summary

VISTA is a modular, model-agnostic framework that decomposes global causal structure learning into node-centered Markov Blanket subgraphs, aggregates them via a weighted voting mechanism (with exponential decay that penalizes low-support edges), and enforces acyclicity through a Feedback Arc Set heuristic. The framework wraps any base learner (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) and any MB estimator, operating purely on edge-level outputs. The paper claims finite-sample error bounds and asymptotic consistency for the weighted voting aggregation, and supports these with extensive synthetic and real-data experiments.

## Strengths

- **Model-agnostic, plug-and-play design.** VISTA imposes no restrictions on the base learner's internal structure or the MB identification method. The experiments demonstrate consistent improvements across 5 diverse base learners (differentiable and combinatorial) on both linear and nonlinear synthetic data (Tables 1, 2), as well as on the Sachs real dataset. This generality is a genuine advance over prior modular frameworks like DCILP (which is tied to a specific ILP formulation) or SADA (limited to LiNGAM).

- **Substantial computational efficiency.** The divide-and-conquer decomposition reduces the per-subgraph problem size dramatically, and the aggregation is a one-pass O(|V|²) edge-level operation requiring no solver. Table 3 shows 5–7× runtime reductions (e.g., NOTEARS on n=300: 12,515s → 2,136s; DAG-GNN: 17,713s → 1,960s), and the design fully supports parallel independent subgraph learning.

- **Consistent empirical accuracy gains.** Across nearly all base learners and graph settings, VISTA with Weighted Voting (WV) reduces FDR by 50–80% relative to the standalone baseline while keeping TPR at or above 0.68 in the main synthetic setting (Table 1, n=100). The improvements hold under data standardization (Table 2) and on real data (Table 4). The use of fixed hyperparameters (λ=0.5, t=0.7) without per-dataset tuning adds credibility.

- **Practical sensitivity analysis.** Figure 4 systematically maps the precision–recall trade-off induced by λ, confirming the theoretical prediction that larger λ increases recall at the cost of precision and that the curves plateau as (1−e^{−λm})→1. This provides actionable guidance for hyperparameter selection.

## Weaknesses

### Major

1. **Asymptotic consistency (Theorem 3.5) relies on a scaling condition that does not hold in the intended setting.** The theorem requires that the number of local subgraphs containing a candidate edge scales as m = C log n. In a sparse DAG with bounded degree — precisely the setting VISTA targets — each edge appears in the MB subgraphs of its two endpoints and possibly a constant number of spouses. Thus m is bounded by a function of the maximum degree, not of n. The condition m → ∞ as n → ∞ cannot be met, making the asymptotic consistency claim vacuous for the actual problem domain. The paper does not discuss this gap. This does not invalidate the finite-sample bounds (Theorems 3.2–3.4), which are stated for a given m, but it severly overstates the asymptotic guarantees.

2. **The core theoretical results (Theorems 3.2, 3.5) assume independent Binomial votes across subgraphs, but the votes are strongly correlated.** As the paper acknowledges (line 142), subgraphs learned from the same dataset share overlapping data (Markov Blankets overlap heavily), so votes for a given edge are dependent. The paper correctly frames the independence assumption as an idealization and calls the bounds a "qualitative guide," but it provides no analysis — not even a simple bound under low-correlation or exchangeability assumptions — of how dependence affects the guarantees. This leaves a significant gap between the theoretical claims (finite-sample error bounds, consistency) and the actual method. While this weakness alone may not be fatal (similar independence assumptions appear in accepted ensemble causal discovery work — e.g., "Causal Discovery in the Wild" at ICLR 2026), it is more consequential here because the subgraphs share data deterministically, unlike bootstrapped ensemble members.

3. **The MB solver used in experiments is never specified.** The paper states VISTA is "agnostic to the specific MB estimator" but does not reveal which MB identification algorithm was actually run in any experiment (e.g., IAMB, MMPC, PC). Since the entire divide stage depends on MB quality, and Figure 1 explicitly reports MB identification F1 scores, the omission harms reproducibility. The code is provided, which mitigates this, but the paper should state the solver directly.

### Minor

4. **The theoretical guarantees cover only the weighted voting stage, not the final acyclic graph.** Theorems 3.2–3.5 analyze the weighted voting rule in isolation, but the pipeline includes a GreedyFAS post-processing step that can add or remove edges regardless of their vote scores. The paper does not extend the error bounds to the final output. The conclusion acknowledges that FAS may prune correct edges, but the scope of the theory should be stated more precisely up front.

5. **The feasible λ interval in Theorem 3.4 depends on m, which varies per edge, but a single λ is used globally.** The bound in (5) fixes a specific m, yet in practice different edges appear in different numbers of subgraphs. The paper does not discuss how to choose λ when m varies across edges, or whether the error control guarantee degrades for edges with m far from the nominal value.

6. **The choice of the exponential weighting function (1−e^{−λm}) is presented without justification over alternatives.** Any monotone function converging to 1 as m→∞ would produce qualitatively similar behavior. The paper would benefit from a brief rationale (e.g., connection to exponential concentration bounds) or an ablation comparing alternatives.

### Trivial

7. **Contradiction between text and Figure 3 on the order of FAS vs. threshold filtering.** The text at line 118 states "cycles are first removed using GreedyFAS, after which edges with weights below a global threshold t are filtered out" (FAS → threshold), while the Figure 3 caption describes the pipeline as "filtered ... and then GreedyFAS is applied" (threshold → FAS). The pseudocode in Figure 2 (WV returns thresholded graph, then post_prune) aligns with the latter. The authors should resolve this inconsistency.

## Nice-to-Haves

- Empirically estimate the correlation between subgraph votes for a given edge to assess how far the independence-based bounds are from reality.
- Ablate the sensitivity to MB quality by comparing VISTA with true MBs vs. estimated MBs with controlled error rates.
- Ablate the FAS step by comparing VISTA with and without GreedyFAS (or with alternative cycle-breaking heuristics).
- Include a small worked example showing the ground-truth DAG, the base learner's output, and VISTA's output to build intuition.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing comparison with DCILP/SADA in the main text.** The paper states (line 178) that a comparison with DCILP is provided in Appendix F.2. The appendix was stripped by the parser but exists in the original submission. The criticism that the comparison is absent is therefore factually incorrect. (Whether it should appear in the main text rather than the appendix is a presentation judgment, not a factual flaw.)

- **Criticism that NV's high FDR (0.87) "suggests the raw aggregation is broken" and the claim about recall is "misleading."** The paper explicitly positions NV as an ablation that validates coverage (Proposition 3.1) and demonstrates that WV is needed to control precision. NV's poor FDR is not a claim of success but a baseline from which WV improves. The paper's wording ("NV already lifts recall") is accurate — TPR does increase — and is accompanied by the full FDR/SHD numbers. No deception is present.

- **Criticism about Theorem 3.2 depending on unknown p.** The paper openly states that "the true value of p is unknown" and says "we can empirically validate the trend." This is standard for concentration bounds that depend on unknown parameters (e.g., Hoeffding bounds depending on the range). Not a weakness.

- **Criticism that the exponential weighting form has no justification.** This is a presentation preference. The paper provides an intuitive explanation (confidence modulator, analogous to Bayesian smoothing priors). While alternative functions could be compared, the choice is reasonable and the behavior is empirically characterized.

## Novel Insights

None beyond the paper's own contributions. The reviews and my own reading surface a recurring pattern in the causal discovery aggregation literature: papers propose clean, empirically effective voting frameworks but rely on independence assumptions that are technically violated in practice. This paper is transparent about the issue (unlike some related work), but the gap between theory and practice remains unresolved. The more novel observation — which the paper does not fully explore — is that the m-scaling problem (each edge appears in only O(1) subgraphs in sparse graphs) is a fundamental limitation for any MB-based decomposition approach seeking asymptotic guarantees, not just for VISTA's specific voting scheme.

## Suggestions

1. **Either withdraw the asymptotic consistency claim (Theorem 3.5) or rework it** to reflect that m is bounded in sparse graphs; a more honest claim would be that the voting procedure's error probability decays as m grows (for a given graph), without claiming m ~ log n as n→∞.
2. **Specify the MB solver used in all experiments** in the main text or a clear table.
3. **Resolve the FAS/threshold ordering contradiction** between line 118 and Figure 3.
4. **Empirically quantify vote correlations** on synthetic data to demonstrate that the independence-based bound is not wildly optimistic.
5. **Add an ablation that replaces the exponential weight with a simpler baseline** (e.g., linear weight w(m)=min(1, m/M)) to show that the specific functional form matters.

## Score and Decision

**Calibration anchors** (from batch search):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/WtbPaWO8lH.md` ("Causal Discovery in the Wild") | 6.00 | Very similar paper (voting-theoretic ensemble for causal discovery with independence assumptions); accepted as Poster. VISTA has broader experiments but weaker asymptotic theory. |
| `/home/wg25r/review_agent/human_reviews_2026/V7pT2ZRoTB.md` ("Theoretical Guarantees for Causal Discovery on Large Random Graphs") | 4.50 | Accepted Poster with stronger theory but much weaker experiments. Comparable overall quality. |
| `/home/wg25r/review_agent/human_reviews_2026/7K8mS5QNkf.md` ("Improving constraint-based discovery...") | 4.50 | Rejected despite addressing a relevant problem. VISTA has cleaner methodology and stronger experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/3lFAyPa9Fe.md` ("CausalSteward") | 4.00 | Rejected divide-conquer-combine framework. VISTA is more principled and better evaluated. |
| `/home/wg25r/review_agent/human_reviews_2026/aS7EVadvZD.md` (SLCD) | 3.00 | Rejected due to fundamentally flawed theory and weak experiments. VISTA is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/Ml8t8kQMUP.md` ("Exploratory Causal Inference in SAEnce") | 7.00 | Accepted Oral. Significantly more polished, with clearer theoretical connection to practice. VISTA is below this bar. |
| `/home/wg25r/review_agent/human_reviews_2026/mA78uXqcnl.md` ("Causal Structure Learning in Hawkes Processes") | 7.00 | Accepted Oral with stronger theoretical grounding. VISTA does not reach this tier. |

Relative to these anchors, VISTA presents a clean framework with strong and broad experiments, but its theoretical contribution is weakened by the m-scaling gap in the asymptotic consistency claim and the acknowledged-but-unaddressed independence assumption. It sits between the 4–5 range where papers have solid ideas with gaps, and the 6 range where theory and experiments are both well-executed. I place it at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>