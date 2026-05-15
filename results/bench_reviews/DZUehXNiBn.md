Now I have all the information needed. Let me synthesize the final review.

---

## Summary

VISTA is a modular framework for causal structure learning that decomposes the global DAG learning problem into local Markov Blanket subgraphs, applies arbitrary base learners to each subgraph, and aggregates the results via a weighted voting scheme with exponential confidence decay, followed by acyclicity enforcement via GreedyFAS. The framework is model-agnostic, supports parallelization, and empirically improves accuracy (F1, SHD, FDR) and runtime across five diverse base learners on synthetic ER and scale-free graphs.

## Strengths

- **Modular, model-agnostic design with sound coverage guarantee:** Proposition 3.1 proves that the union of MB-induced subgraphs covers every true edge, providing a principled foundation for the divide-and-conquer decomposition. The framework is validated across five structurally different base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) spanning linear, nonlinear, differentiable, and combinatorial methods, demonstrating genuine plug-and-play compatibility (Tables 1–2).

- **Effective weighted voting that provides tunable precision–recall control:** The exponential decay term (1 − e^(−λm)) in Equation 2 adaptively down-weights low-support edges, enabling calibrated filtering without solver-based optimization. The λ sweep in Figure 4 confirms smooth, retraining-free precision–recall trade-off, and the fixed operating point (λ = 0.5, t = 0.7) yields consistent FDR reductions of 50–80% over standalone baselines while maintaining reasonable TPR (Table 1).

- **Substantial runtime gains from parallel decomposition:** Table 3 shows order-of-magnitude wall-clock reductions (e.g., NOTEARS on n=300 from ~12,500s to ~2,100s; SCORE under 230s at n=300 vs. unable to complete standalone). The gains arise from the divide-and-conquer architecture rather than algorithm-specific tuning.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 3.5 (Asymptotic Consistency) is stated as a property of VISTA but the required condition is not established for the method's actual operation.** The theorem requires the number of local subgraphs per candidate edge to satisfy m = C log n with constant C > 2/min{δ_p², δ_q²}. In VISTA, m is determined by how many Markov Blankets contain a given edge — which, under the sparse graphs studied (constant average out-degree h ∈ {3, 5}), is roughly O(h²) = O(1), not Ω(log n). The paper provides no analysis showing that VISTA's MB decomposition meets this growth condition under any standard graph model, nor does it discuss the discrepancy. As a result, the claimed asymptotic consistency is a conditional statement about a hypothetical voting rule, not a proven property of VISTA. This significantly weakens the theoretical contribution.

- **Lack of head-to-head comparisons with other modular/merging methods in the main evaluation.** The introduction positions VISTA as superior to existing divide-and-conquer and fusion-based approaches (DCILP, rule-based voting, separation–reunion), yet the main experimental tables (Tables 1–4) compare only against standalone base learners. The DCILP comparison is relegated to Appendix F.2 (not present in the main paper). Without main-paper comparisons against the very merging schemes VISTA aims to replace, the claim that weighted voting provides better-calibrated and more efficient aggregation than existing alternatives remains unsubstantiated in the paper's primary evidence.

### Minor

- **MB identification method is unspecified.** The paper correctly asserts that VISTA is agnostic to the MB solver, but it never reports which specific MB discovery method was used in experiments, its hyperparameters, or how sensitive final DAG quality is to MB estimation errors. Since Proposition 3.1's coverage guarantee assumes correct MBs, and all downstream aggregation depends on this, the omission affects reproducibility and makes it hard to assess whether observed gains depend on a particularly strong MB estimator. The high MB accuracy in Figure 1 suggests the chosen solver is effective, but its identity remains invisible.

- **The theoretical analysis operates under idealized independence assumptions that do not hold in practice.** Theorem 3.2 assumes independent votes across subgraphs, yet subgraphs learned from the same dataset induce correlations. The paper acknowledges this limitation (Section 3.1), but Theorem 3.4 and the bounds derived from it inherit the same issue. A clearer discussion of how dependence among votes affects the error guarantees — or a weakening of the theoretical claims accordingly — would strengthen the paper.

### Trivial

- The real-data experiment (Sachs network, 11 nodes, 17 edges) is a standard benchmark but too small to validate the scalability claims that motivate the framework. The improvements there (Table 4) are modest, and the claim that VISTA "reliably enhance[s] the performance of arbitrary causal discovery algorithms" is stated too broadly given a single small real-world dataset.

- Figure 1 does not specify which MB identification method or metric was used for the "Markov Blanket" curve, making the comparison to base learner degradation harder to interpret precisely.

## Nice-to-Haves

- An ablation study using a deliberately weak MB estimator (e.g., correlation-based) to quantify how MB errors propagate to final DAG quality, which would clarify the framework's practical robustness.
- Analysis of the regime where true edges appear in very few subgraphs (m small), to illuminate when the (1 − e^(−λm)) down-weighting might suppress genuine edges.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **"NV variant is a strawman" (from Harsh Critic):** NV is explicitly introduced as an ablation to demonstrate why weighting is necessary. It is a valid experimental design choice, not a strawman. The paper clearly states that NV's poor FDR motivates the WV scheme. Removed.

- **"Modest gains in some cases" (from Harsh Critic):** The gains are substantial where they matter most: GOLEM F1 improves from 0.35→0.60 on ER, DAG-GNN from 0.33→0.59, GraN-DAG from 0.06→0.17. These are large relative improvements, and even the smaller gains (NOTEARS 0.76→0.79) represent improved FDR/SHD. The criticism misreads the effect sizes. Removed.

- **Criticism about λ=0.5, t=0.7 not satisfying (5) universally:** The paper acknowledges this is a fixed compromise point and provides full sensitivity analysis in Figure 4. No per-dataset tuning is performed. This is a reasonable practical choice. Removed from weaknesses; addressed in the paper.

- **"Theorem 3.4 is stated opaquely" and "Corollary 3.3 derivation not provided":** The derivations are in Appendix E (removed during parsing). The theorem statement itself is interpretable: it gives a feasible λ range for error control. This is a presentation nitpick, not a substantive error. Removed from weaknesses.

- **"Introduction misrepresents identifiability guarantees":** The paper explicitly acknowledges this limitation in the conclusion ("latent confounding introduced by restricting the learner to subsets may produce high-confidence redundant edges"). This is addressed. Removed.

- **Strength Finder generic/nonspecific strengths:** Dropped generic claims not backed by specific evidence (none applied — the Strength Finder's points were specific and verified).

## Novel Insights

The paper's most novel observation, supported by both theory (Proposition 3.1) and Figure 1, is that MB identification accuracy degrades far more slowly with graph size than base learner performance, making MB-based decomposition a robust foundation for divide-and-conquer causal discovery even as base learners deteriorate. The empirical demonstration that this decomposition enables a simple, retraining-free weighted voting rule (tunable via λ alone) to substantially outperform standalone baselines — without any solver, iterative optimization, or base-learner-specific calibration — is a genuinely useful insight for practitioners.

## Suggestions

- Either replace Theorem 3.5 with a properly grounded analysis that connects the m = C log n condition to VISTA's MB decomposition (e.g., under appropriate graph density assumptions), or clearly restate it as a property of the voting rule under an external condition not guaranteed by VISTA, and discuss what graph regimes would satisfy it.
- Move the DCILP comparison from the appendix into the main experimental section, or at minimum summarize those results in the main text with a clear pointer.
- Specify the MB identification method and its hyperparameters used in all experiments; report a sensitivity analysis (even a brief one) varying the MB solver quality.

---

## Anchor Comparison

- **WtbPaWO8lH** (avg 6.0, Accept Poster): Voting-theoretic ensemble for causal discovery. Similar in spirit (voting-based aggregation) but uses ensembles of full-graph experts rather than MB subgraphs. Had stronger theoretical formalism but also suffered from gap between theory assumptions and practice. VISTA has more comprehensive experiments (5 base learners × multiple graph families) but weaker theoretical grounding. Slightly below this anchor.

- **V7pT2ZRoTB** (avg 4.5, Accept Poster): Pure theory paper on FNR concentration in random causal graphs. Strong theory but narrow practical scope. VISTA is more practically valuable but its theoretical claims are less solidly established. Comparable overall quality, different strengths.

- **N9RyL52z7y** (avg 4.5, Accept Poster): Divide-and-aggregate framework for conditional independence testing. Similar modular/plug-and-play philosophy with theoretical consistency claims. VISTA has broader experimental validation and a more substantial empirical contribution. VISTA is slightly stronger.

- **3lFAyPa9Fe** (avg 4.0, Reject): Divide-and-conquer causal discovery with LLM agents. VISTA is more principled, more extensively evaluated, and makes a clearer technical contribution. VISTA is clearly stronger.

- **AvkLmnUqtZ** (avg 4.67, Reject): DAG learning algorithm with stochastic approximation. Narrower scope; VISTA's framework-level contribution and cross-learner validation are more significant.

- **vSAWV43kvs** (avg 3.0, Reject): Foundation model approach for DAG learning. Overclaimed and narrowly validated. VISTA is substantially stronger.

- **zGznH3w5tT** (avg 2.67, Withdrawn/Reject): LLM + evolutionary algorithm for causal discovery. VISTA is far stronger in methodology, evaluation, and contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>