Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

## Summary

This paper introduces VISTA, a model-agnostic modular framework for causal structure learning that decomposes the global DAG into node-centered Markov Blanket subgraphs, learns local structures in parallel, and aggregates them via a weighted voting scheme with acyclicity enforcement through a Feedback Arc Set heuristic. The paper provides finite-sample error bounds, an asymptotic consistency theorem, and extensive experiments across synthetic and real data.

## Strengths

1. **Model-agnostic framework validated across diverse base learners and data regimes.** VISTA is applied to five distinct causal discovery algorithms (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) under linear/nonlinear synthetic settings (Tables 1–2) and real-world Sachs data (Table 4). In nearly every case, weighted voting improves F1 and reduces SHD relative to the standalone baseline. This universality is a genuine advance over prior modular approaches such as SADA (limited to LiNGAM) or DCILP (NP-hard ILP formulation).

2. **Substantial empirical speedups from parallelization.** Table 3 shows VISTA reduces total runtime for NOTEARS by ~6× (from ~12,515s to ~2,137s for n=300), and similar improvements hold across all tested base learners. These gains derive directly from the divide-and-conquer design, not algorithm-specific acceleration.

3. **Clean coverage guarantee for the divide step.** Proposition 3.1 formally proves that the union of Markov-Blanket-induced subgraphs contains every true edge under correct MBs. This provides a sound foundation for the decomposition and is explicitly leveraged in the theoretical analysis.

## Weaknesses

### Major

1. **Asymptotic consistency theorem requires a condition inconsistent with the MB decomposition.** Theorem 3.5 states that consistency holds if *"the number of local subgraphs per candidate edge is m = C log n"*. However, under the Markov Blanket decomposition, m — the number of subgraphs containing both endpoints of a given edge — is bounded by a small constant (typically O(deg), i.e., the node degree plus spouse connections). For a true edge (X,Y), the only subgraphs that contain both X and Y are those centered at X, at Y, and at any node whose MB includes both; in a sparse DAG this number does not grow with n. The paper provides no argument establishing that m scales with n under the proposed decomposition, and in the presented framework it manifestly does not. This is not a minor technical gap — the asymptotic consistency claim is highlighted in the abstract, introduction, and conclusion as a key theoretical contribution, yet its central sufficient condition cannot be realized by the method as described. The finite-sample bounds (Theorems 3.2, 3.4) remain valid but the asymptotic claim is an overstatement.

2. **MB identification algorithm used in all experiments is not specified in the main text.** The paper states *"we also implemented the MB solver used in that work"* (referring to DCILP) but never names the algorithm. The identity of the MB solver is critical for reproducibility and for assessing the practical impact of MB estimation errors, which the theory does not account for. Figure 1, which motivates the framework by showing MB identification accuracy remains high, also omits which MB algorithm produced those results.

### Minor

1. **The claim "typically increasing precision without sacrificing recall" is overstated.** In Table 1, NOTEARS on ER5 shows VISTA-WV yielding TPR 0.68 versus the baseline 0.74 — a reduction in recall. While the vast majority of settings show improved or maintained recall, the blanket phrase "without sacrificing recall" is inaccurate for this prominent case. The paper would be more credible by acknowledging the precision-recall trade-off explicitly.

2. **The theoretical analysis does not incorporate MB estimation errors.** Proposition 3.1 guarantees coverage only under *true* Markov Blankets. In practice, estimated MBs may miss some true edges, which cannot then be recovered by any voting scheme. The finite-sample bounds (Theorems 3.2, 3.4) and consistency proof all condition on subgraph-level outputs without accounting for MB identification errors. This makes the theoretical contribution an analysis of the aggregation sub-problem under idealized inputs rather than the end-to-end procedure.

3. **Theorem 3.2's independence assumption on subgraph votes is acknowledged but its practical implications unexplored.** The paper correctly notes this is an idealization, but does not discuss how correlation among votes (which is inevitable given the subgraphs share data) would affect the bound in practice. The sufficient condition derived under independence may not carry over.

### Trivial

None.

## Nice-to-Haves

- A decomposition of runtime into MB identification, local learning, and aggregation stages would clarify where the speedups come from.
- An ablation separating the effect of MB decomposition from the effect of weighted voting (e.g., baseline vs. baseline + MB decomposition + naive voting vs. full VISTA) would isolate which component drives improvements.
- Reporting the actual m values (number of subgraphs per edge) observed in experiments would contextualize the theoretical requirements.

## Removed Points

**1. Insufficient comparison to DCILP in main paper** — The paper explicitly states DCILP comparison is in Appendix F.2. Since the appendix exists in the actual submission (only the parser stripped it), this criticism is about placement rather than absence. Relegating one comparison to the appendix is a reasonable space trade-off given the paper's extensive experiments already occupying Tables 1–4.

**2. Theorem 3.4 λ validation** — The critic argues the paper doesn't specify ε or verify inequality (5) for actual m values. The paper provides Figure 4 (precision-recall curves) and states the chosen λ=0.5 "lies within (5)." An empirical sensitivity analysis is a reasonable practical validation; full verification of every theoretical inequality is not expected.

**3. "Modest improvements on Sachs"** — Real-data results are inherently modest; the paper does not overclaim on this. This is an observation about the difficulty of the task, not a paper weakness.

**4. Theorem 3.2 independence assumption** — Already acknowledged in the paper as an idealization. Included above as a Minor weakness since the paper could do more to discuss practical implications, but the critic's framing as a major oversight is inappropriate.

**5. Time efficiency composition (Table 3)** — Requesting a decomposition is a nice-to-have, not a weakness. The total time gains are sufficient to demonstrate the method's value.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel observations about the method or problem that the paper itself failed to articulate.

## Suggestions

1. **Reframe or remove the asymptotic consistency claim.** Either replace Theorem 3.5 with a finite-sample analysis that does not require m to grow with n (e.g., a bound in terms of maximum MB size or maximum node degree), or explicitly acknowledge that the asymptotic result applies only in settings where m can be made to grow (e.g., through resampling or ensemble strategies) and is not guaranteed under the basic MB decomposition.

2. **Specify the MB identification algorithm** used in all experiments in the main text. Name the algorithm (e.g., IAMB, PCMB, etc.) and ideally cite the original work.

3. **Correct the overstatement in the conclusion.** Replace "typically increasing precision without sacrificing recall" with a more accurate characterization, e.g., "typically improving the precision-recall trade-off, with recall gains in most settings."

4. **Include the DCILP comparison summary in the main paper** (even as a single-row table) if space permits, since the paper's contribution is a modular framework and DCILP is the most directly comparable prior approach.

## Score and Decision

**Round-1 bracketing:** The paper sits clearly above the weak-anchor band (avg 2.5–3.4, rejected papers with major execution flaws) and well below the strong-anchor band (avg 8.0, oral/poster papers with clean theoretical and empirical contributions). The plausible range is (4.0, 7.0).

**Round-2 narrowing anchors:**

- **Auto-Ensemble BN (avg 4.75, withdrawn/rejected)** — Similar D&D approach for BN learning with ensemble methods. VISTA is stronger in breadth of experiments and cleaner framework design, but the Auto-Ensemble paper's theoretical guarantees are internally consistent whereas VISTA's asymptotic claim has a structural issue. VISTA is slightly stronger overall.

- **Modular Deep Causal Generative Models (avg 4.75, rejected)** — Theoretical analysis with limited experiments. VISTA has substantially more extensive empirical validation and a cleaner practical contribution. Comparable theory quality (both have gaps), but VISTA's experiments are far more comprehensive.

- **Meta-Learning Bayesian CD (avg 6.0, accepted poster)** — Well-written, well-executed but seen as incremental. VISTA has more novel methodology but a more significant theoretical flaw. The meta-learning paper's theoretical claims are sound; VISTA's asymptotic claim is not.

- **Beyond DAGs (avg 5.75, rejected)** — Confusing presentation, limited experiments. VISTA is clearly stronger in presentation and empirical scope.

- **Doubly Robust Structure ID (avg 4.8, rejected)** — Novel approach but unclear evaluation and minimal experiments. VISTA is substantially better.

**Final score:** 5.0. The paper has genuine contributions — a clean, modular framework, strong empirical results across diverse settings, and real speedups — but the asymptotic consistency claim, presented as a key theoretical contribution, relies on a condition that cannot be met by the method's own decomposition. This gap prevents the paper from reaching the acceptance threshold while the empirical contributions keep it above a clear reject.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>