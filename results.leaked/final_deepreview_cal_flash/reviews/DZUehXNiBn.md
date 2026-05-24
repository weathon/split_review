Now let me write the consolidated review.

## Summary

VISTA proposes a modular framework for causal structure learning that decomposes the global DAG problem into Markov-blanket-centered local subgraphs, runs any off-the-shelf base learner on each subgraph in parallel, aggregates edge votes via a weighted voting scheme with exponential down-weighting of low-support edges, and enforces acyclicity using a Greedy Feedback Arc Set heuristic. The paper provides finite-sample error bounds and asymptotic consistency guarantees for the aggregation, and evaluates the framework across five diverse base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) on synthetic and real data.

## Strengths

- **Model-agnostic improvement across diverse base learners.** Tables 1 and 2 show that VISTA with weighted voting (WV) improves F1 and reduces FDR for five fundamentally different base learners under both linear and nonlinear settings, using a single fixed hyperparameter configuration (λ=0.5, t=0.7). The consistency of improvement across NOTEARS (gradient-based), GOLEM (likelihood-based), DAG-GNN (VAE-based), GraN-DAG (gradient-based), and SCORE (ordering-based) provides direct evidence that the gains stem from the aggregation rule rather than any one base learner's inductive bias.

- **Substantial, well-documented runtime reductions.** Table 3 reports dramatic speedups (e.g., NOTEARS on ER3 n=300 from 12,515s to 2,136s; DAG-GNN from 17,713s to 1,960s; SCORE from >10,000s to 225s). These reductions are a natural consequence of the divide-and-conquer design (parallel subgraph processing), and the measurements across multiple graph sizes make the scalability advantage concrete.

- **Clean, modular design with explicit model-agnostic interface.** The framework separates MB identification, local learning, edge-level aggregation, and acyclicity enforcement into independent stages (pseudocode in Figure 2, pipeline in Figure 3). The aggregation operates purely on edge counts (O(|V|²) one-pass), requiring no solver, no training, and no assumptions about the base learner's internal structure. This modularity is a genuine practical advantage over monolithic or solver-based alternatives like DCILP.

- **Empirical validation of the λ-controlled precision-recall trade-off.** Figure 4 sweeps λ across three diverse settings (GOLEM, SCORE, DAG-GNN) and shows a smooth transition from high precision to high recall, plateauing as predicted by the theoretical analysis. This confirms that the weighting parameter provides controllable behavior rather than requiring per-dataset tuning.

- **Robustness under data standardization.** Table 2 repeats experiments on normalized data where base learners' standalone performance fluctuates significantly (e.g., NOTEARS TPR drops from 0.74 to 0.39). VISTA-WV maintains consistent improvements, supporting the claim that the framework does not rely on specific data properties.

## Weaknesses

### Major

- **Theoretical guarantees rely on assumptions not justified for the target setting.** Two issues undermine the theory as presented:

  (1) **Independence of subgraph votes (Theorem 3.2).** The concentration bounds model votes as Binomial(m,p) with independent subgraph contributions. The paper briefly acknowledges this is idealized (Section 3.2: "the bound should be interpreted as a qualitative guide") but provides no analysis of how dependence affects the bounds. No mixing conditions, covariance bounds, or sensitivity analysis is given. This weakens the theoretical support substantially—the guarantees are stated for a regime the paper itself admits is not realistic.

  (2) **Scaling of m with n (Theorem 3.5).** The asymptotic consistency result requires m = C log n subgraphs per candidate edge. In sparse graphs—the regime where divide-and-conquer is most needed—an edge (X,Y) appears only in the Markov blankets of X and Y and possibly a few spouses. The Markov blanket size in a sparse graph is O(1) relative to n, so m is bounded by a constant and does not grow with n. The paper states that "the required number of independent subgraphs per edge grows only logarithmically with the graph size" (Section 3.2) without noting that this scaling has no basis in the proposed decomposition for sparse graphs. The asymptotic consistency guarantee therefore does not apply to the very graphs where VISTA is designed to be most useful.

  These issues are structural: the theory as presented gives an impression of rigor that the actual analysis cannot support. The paper would need either to redevelop the analysis for the actual dependence structure and bounded-m regime, or to recast the theoretical claims as heuristic motivation.

- **Markov Blanket identification method is not specified in the paper.** The experiments do not state which MB estimator is used. Figure 1 reports MB identification F1 around 0.9 (suggesting the MB is estimated, not oracle—oracle MB would yield F1=1.0), but the algorithm is never named. The pseudocode (Figure 2) takes an `MB_solver` argument, and the paper notes the framework is "agnostic to the choice of MB identification methods" (Section 3), but for reproducibility and fair assessment, readers need to know what specific method was used. This is especially critical because VISTA's performance depends at least as much on MB quality as on the base learner. The code is provided in supplementary material, which mitigates the reproducibility concern, but the paper itself should disclose this detail.

### Minor

- **DCILP comparison is relegated to the appendix.** The paper positions VISTA as a lightweight alternative to solver-based merging (DCILP is cited as "solver-heavy" and "NP-hard") but the direct comparison appears only in Appendix F.2. While the main evaluation against five standalone base learners is sufficient to demonstrate improvement over individual methods, a direct comparison against another modular pipeline in the main text would better contextualize the contribution.

- **No ablation on the FAS ordering claim.** The paper states that applying GreedyFAS before threshold filtering (rather than after) is an "important implementation detail" that avoids precision loss (Section 3.1). This claim is plausible but no experiment validates it. An ablation study would strengthen the paper.

- **FAS post-processing and Markov equivalence.** The GreedyFAS heuristic may orient edges in directions not supported by the data, potentially violating Markov equivalence constraints. The paper does not discuss this caveat, which is relevant for practitioners using VISTA with constraint-based or score-based learners that return equivalence classes.

- **Sachs real-data results show mixed trade-offs.** Table 4 shows that for some base learners (e.g., GraN-DAG), TPR drops substantially when VISTA is applied (from 0.53 to 0.29), even though FDR improves and SHD/SID decrease. The paper highlights the FDR reduction but could more explicitly discuss whether this precision-recall trade-off is acceptable for the intended applications.

- **Unsubstantiated claim about overall error rate bound.** The introduction states "We also establish a theoretical result showing that the overall error rate of the procedure is bounded above by that of the subgraph-level aggregation" (Section 1), but this result is not stated or proven in the main text (it may appear in the stripped appendix). The main text's theorems concern edge-level errors, not a global error rate bound.

### Trivial

- The paper would benefit from a formal derivation or Bayesian motivation for the exponential weighting function in Equation (2). Currently it is introduced as a heuristic with no clear connection to the theoretical analysis that follows.

## Nice-to-Haves

- An experiment that systematically varies MB estimation quality (e.g., by injecting errors or using weaker MB learners) to demonstrate that VISTA degrades gracefully rather than catastrophically.
- A comparison with a simple alternative modular baseline in the main text (e.g., random partitioning of nodes followed by majority voting) to isolate the benefit of the MB-based decomposition from the voting scheme itself.
- Reporting results across a grid of t (threshold) values in addition to the λ sweep in Figure 4, to provide a fuller picture of hyperparameter sensitivity.

## Removed Points

These points were raised in the inputs but are removed as per the filtering rules:

- **"Paper does not cite ensemble-based causal discovery"** — Removed per rules: cannot flag missing related works.
- **"λ=0.5 and t=0.7 may be cherry-picked"** — Removed: the paper explicitly states these are fixed to avoid per-dataset tuning, and Figure 4 provides a sensitivity analysis for λ.
- **"Proposition 3.1 is trivial"** — Not a weakness; it is a needed foundational statement.
- **"Weighted voting formula lacks derivation"** — The paper provides intuitive motivation and references Appendix D.1; this is a design choice, not a flaw.
- **"No error bars for Sachs data"** — Sachs is a single standard benchmark with well-known ground truth; per-method results are reported directly.

## Novel Insights

None beyond the paper's own contributions. The review process surfaced a genuine tension between the paper's theoretical framing (which suggests stronger guarantees than the assumptions support) and its empirical contributions (which are genuinely positive and well-executed). This tension is worth the authors' attention but is not a novel insight per se.

## Suggestions

- **Revise the theoretical section** to either (a) analyze the effect of vote dependence explicitly (e.g., via a variance bound under a mild correlation model), or (b) reframe the current theory as heuristic motivation with explicit caveats about the independence and m-scaling assumptions, and strengthen the experimental validation accordingly.
- **Disclose the MB estimator** used in experiments in the main paper (even a one-sentence description). This is essential for reproducibility.
- **Add an ablation study** comparing FAS-before-filtering vs. filtering-before-FAS to validate the claimed ordering advantage.
- **Move the DCILP comparison** from the appendix to the main text, or at minimum summarize the key result in a sentence.
- **Discuss the FAS-related identifiability caveat** explicitly, noting that cycle breaking may orient edges in ways not supported by the data.

## Score and Decision

### Round 1 — Bracketing

Three calibration queries on causal structure learning / modular frameworks produced anchors:
- **Weak band (<3.5):** avg 3.0–3.4 — papers with fundamental flaws, weak or no experiments.
- **Middle band (3.5–7.5):** avg 4.75–7.33 — mixed quality. The most relevant anchors are "Exact Distributed Structure-Learning" (5.25, similar domain, weaker experiments), "Extendable and Iterative Structure Learning" (5.60, strong speedup results but no theory), "Analytic DAG Constraints" (7.00, strong theory + experiments), and "Causal Modelling Agents" (6.25, modular framework).
- **Strong band (>7.5):** avg 8.0 — strong papers with clean contributions and minimal weaknesses.

**Initial bracket:** VISTA is clearly stronger than the 3–3.4 papers. It is stronger than the 5.25 distributed learning paper (which had limited baselines and unclear methodology) and comparable to the 5.60–6.33 range. It is weaker than the 8.0 anchors due to the theory gaps. **Plausible range: 5.0–7.0.**

### Round 2 — Narrowing

Four additional queries inside (5.5, 7.5) returned anchors including "Extendable and Iterative Structure Learning" (5.60, accepted), "Efficient and Trustworthy Causal Discovery" (6.00, accepted — solid theory, limited experiments), and "CausalRivers" (7.33, accepted — strong benchmarking contribution).

Comparing VISTA against these:
- VISTA has stronger and more diverse experiments than the 5.60 anchor (which had limited baselines).
- VISTA has weaker theory than the 6.00 anchor (which had clean identifiability guarantees) but stronger experiments.
- VISTA's experiments are more thorough than the 6.00 anchor's "small and limited to very simple settings."

**Final score: 6.0.** VISTA makes a genuine contribution with a clean modular design and strong empirical evidence across diverse settings. However, the theoretical analysis contains gaps (independence assumption, m-scaling issue in Theorem 3.5) that prevent it from reaching the 7+ tier, and the undisclosed MB estimator is a transparency concern. A score of 6.0 reflects a solid paper with real contributions that would benefit from addressing these issues in revision.

### Anchor Summary

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| JzFLBOFMZ2 (LLM supervised CSL) | 3.20 | R1 | Much weaker; no comparable experiments |
| fSxiromxAq (Sparse Causal Model) | 3.00 | R1 | Much weaker; unclear methodology |
| DUfwD5yiN4 (Exact Distributed Structure-Learning) | 5.25 | R1,R2 | Weaker experiments; only PC baseline |
| Lxst78Rrwj (Causal Graph Learning via Invariance) | 5.00 | R1 | Different approach; limited baselines |
| mGmx41FTTy (Two Time-Slices Topological Ordering) | 6.33 | R1,R2 | Comparable quality but different contribution |
| ZXs3pkmrRG (Test-Time Learning of Causal Structure) | 5.50 | R1 | Different (interventional) setting |
| oCdIo9757e (Analytic DAG Constraints) | 7.00 | R2 | Stronger theory; accepted. VISTA weaker on theory but competitive on experiments |
| pAoqRlTBtY (Causal Modelling Agents) | 6.25 | R2 | Comparable modular framework; accepted |
| 3n6DYH3cIP (Extendable Iterative Structure Learning) | 5.60 | R2 | Accepted but weaker experiments and no theory |
| BZYIEw4mcY (Efficient Trustworthy Causal Discovery) | 6.00 | R2 | Accepted; stronger theory but limited experiments |
| wmV4cIbgl6 (CausalRivers) | 7.33 | R2 | Strong benchmarking contribution; different focus |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>