## Summary

VISTA proposes a model-agnostic modular framework for causal structure learning that (1) decomposes the global DAG into Markov Blanket subgraphs, (2) applies any off-the-shelf base learner to each subgraph independently, (3) aggregates local predictions via a weighted voting mechanism with exponential decay weighting, and (4) enforces acyclicity with a GreedyFAS heuristic. The paper provides theoretical analysis including finite-sample error bounds and an asymptotic consistency result, alongside experiments on synthetic and real data across five base learners.

## Strengths

1. **Lightweight O(|V|²) aggregation replaces NP-hard ILP-based reconciliation.** Unlike DCILP which formulates subgraph merging as an Integer Linear Program, VISTA's weighted voting is a closed-form, one-pass scoring function (Equation 2, Section 3.1) requiring only matrix-level operations with no solver calls. This is a genuine practical advantage for scalability.

2. **Consistent accuracy improvements across five diverse base learners.** Tables 1 and 2 show VISTA-WV improving F1 scores across NOTEARS, GOLEM, DAG-GNN, GraN-DAG, and SCORE on both ER and SF synthetic graphs. For weaker baselines the gains are substantial (GOLEM 0.35→0.60, DAG-GNN 0.33→0.59 on ER5 at n=100). The trend holds for both differentiable and combinatorial learners, suggesting the gains stem from the aggregation rule rather than any particular estimator.

3. **Substantial runtime reductions via parallel divide-and-conquer.** Table 3 shows VISTA reduces total computation time across all base learners at all tested graph sizes (n=50, 100, 300). For n=300, NOTEARS drops from 12515s→2136s; DAG-GNN from 17713s→1960s. These gains are a direct consequence of the divide-and-conquer design, which is the intended mechanism of the framework.

4. **Single fixed hyperparameter setting (λ=0.5, t=0.7) used across all tabulated results.** The paper avoids per-dataset tuning and post-hoc selection, with the theoretical range from Theorem 3.4 guiding the choice. The sensitivity study in Figure 4 validates the precision-recall trade-off without cherry-picking.

## Weaknesses

### Major

1. **The theoretical guarantees are presented more strongly than the algorithm can deliver.** Theorem 3.5 (Asymptotic Consistency) assumes *m = C log n* subgraphs per edge for its guarantee, but in the actual algorithm *m* is a structural property determined by graph degree — a small constant in sparse graphs that cannot grow with *n*. Theorem 3.2 assumes votes from different subgraphs are independent, which the paper acknowledges (line 138) is violated because subgraphs share data. While the paper calls these "qualitative guides," the abstract and introduction frame the theory as a core contribution ("prove its asymptotic consistency under mild conditions," "finite-sample error bounds"), overstating what is actually guaranteed for the real algorithm. The theory proves properties of an idealized setting that does not correspond to the actual procedure, and this disconnect is not adequately signaled in the paper's front matter.

2. **The Markov Blanket identification method used in experiments is never specified.** The paper states the framework is "agnostic" to the MB estimator (line 59), which is fine for the framework design, but experiments require some concrete method. Line 174 mentions "the MB solver used in that work" (referring to DCILP), but the specific algorithm is not named. Without this detail, the experimental results are not reproducible — a reviewer cannot know whether the MB identification was done with a simple correlation-based method, a sophisticated CI-test-based method, or something else. This also makes it impossible to assess how much of the reported runtime is spent on MB identification versus subgraph learning versus aggregation.

### Minor

3. **The Naive Voting (NV) baseline results are catastrophically poor, and the paper's positive framing of NV is misleading.** In Table 1, NV produces FDR of 0.84–0.95 across all methods and SHD numbers an order of magnitude worse than standalone baselines (e.g., NOTEARS SHD from 208.80 to 3171.80 on ER5). The paper says NV "already lifts recall by pooling evidence from overlapping neighborhoods" (line 178), which is technically true (TPR reaches 0.97), but the framing omits the fact that this comes at the cost of an almost completely dense graph. Presenting NV as a positive signal rather than a diagnostic for what happens *without* the weighted voting crutch is misleading.

4. **Improvements over the strongest baseline (NOTEARS) are modest, and the "precision without sacrificing recall" claim is not consistently supported.** On ER5 at n=100, NOTEARS standalone F1=0.76 → VISTA-WV F1=0.79 (+3 points), with TPR actually dropping from 0.74 to 0.68. The larger relative gains come from weaker baselines (GOLEM: 0.35→0.60, DAG-GNN: 0.33→0.59) whose standalone performance is poor. The headline claim that VISTA "typically increases precision without sacrificing recall" is contradicted by the NOTEARS case where recall drops.

5. **No ablation study isolating components.** The paper compares VISTA (all components) against standalone baselines but does not separate the contribution of (a) simply operating on smaller subgraphs, (b) the weighted voting mechanism itself, and (c) the GreedyFAS post-processing. A natural control would be to run each baseline on the same subgraphs VISTA uses and compare the subgraph-level results against VISTA's aggregation of those subgraphs — this would isolate the benefit of the voting scheme from the benefit of problem-size reduction.

6. **The runtime comparison lacks a cost breakdown.** Table 3 reports total time but does not separate MB identification time, the *n* subgraph learning runs, and aggregation. Without this breakdown, it is difficult to understand where VISTA's efficiency gains come from and whether MB identification is a bottleneck.

### Trivial

7. The Sachs dataset has only 11 nodes and 17 edges, where the full graph is already tractable by most baselines. The modest results here are not informative about scalability.

## Removed Points

- **"Runtime comparison is fundamentally unfair"** (Harsh Critic Issue 2, part): The critic argues that running base learners on smaller subgraphs is trivially faster and the comparison is "unfair." This is incorrect — the divide-and-conquer design *is* the method being proposed. Comparing the full VISTA pipeline (including all overhead) against standalone baselines doing a global search is exactly the right comparison. The speedup from smaller problem instances is the intended mechanism.
- **"Parallelization makes comparison unfair"**: The paper is transparent about parallelization as a design feature. Whether parallelism was used in the reported experiments is a minor detail but does not make the comparison unfair.
- **"Weighted voting formula conflates m and directional consistency"**: The design choice (using (1-e^{-λm}) as a confidence modulator) is clearly motivated in Section 3.1. Different design choices are possible but this one is not incorrect.
- **"Proposition 3.1 is trivial"**: Foundational lemmas in papers are often simple. This is a standard coverage guarantee and is appropriately presented.
- **"No comparison with DCILP in main paper"**: The comparison is in Appendix F.2, which was stripped by the parser. The paper references it at line 174.
- **"Sensitivity study uses t=0.5 not t=0.7"**: The PR curves use t=0.5 to show the full trade-off range; the main tables use t=0.7. This is a standard practice and the paper explains it.
- **"Improvement on Sachs is marginal"**: The paper reports the results as they are. On Sachs, some methods show clear FDR reductions (GraN-DAG: 0.82→0.00).

## Novel Insights

The reviews surface an interesting pattern: the paper has a clean, practical engineering contribution (a model-agnostic voting framework with consistent empirical gains) that is largely independent of its theoretical analysis. The theoretical section attempts to provide formal guarantees but operates under idealized assumptions (independent subgraph votes, *m* growing with *n*) that do not match the actual algorithm's setting. This disconnect between the theory's framing (presented as a core contribution in the abstract and introduction) and its actual applicability (acknowledged as "qualitative guides" in Section 3.2) is the paper's most significant weakness. The practical contribution would be stronger if the paper honestly decoupled these narratives and presented the theory as intuition rather than guarantees.

## Suggestions

1. **Specify the MB identification algorithm** used in experiments — this is essential for reproducibility. If the MB solver from DCILP was used, name it explicitly and cite the relevant paper.

2. **Reframe the theoretical contribution** to honestly state that the guarantees hold under idealized independence assumptions and that *m* is not a controllable parameter in the single-dataset setting. The theory can remain as a qualitative guide or intuition, but the abstract and introduction should not present it as a core guarantee.

3. **Add an ablation study** that runs each baseline on the same subgraphs VISTA uses, then compares the subgraph-level results against VISTA's aggregated output. This would isolate the benefit of the weighted voting mechanism from the benefit of smaller problem sizes.

4. **Report a cost breakdown** of VISTA's pipeline: time for MB identification, time for *n* subgraph runs, and time for aggregation. Also clarify whether parallel execution was used and with how many threads.

5. **Adjust the framing of NV results:** Present NV primarily as a diagnostic demonstrating that the MB decomposition preserves all true edges, and explicitly discuss the catastrophic FDR inflation before introducing WV as the solution.

## Score and Decision

**Score anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| LLM Supervised CSL (JzFLBOFMZ2) | 3.20 | 1 | Much weaker — lacks clear contribution, poor framing |
| Sparse Causal Model (fSxiromxAq) | 3.00 | 1 | Much weaker — limited experiments, unclear methodology |
| IRIS (zgM66fu0wv) | 2.50 | 1 | Much weaker — vague contribution |
| ψDAG (iTVKOOZeYW) | 4.75 | 1 | Weaker — poor presentation, missing proofs, limited scope |
| Temporal Aggregation (WqovbCMrOp) | 5.80 | 1 | Comparable — stronger theory but very weak experiments |
| DAG-TFRC (6O8lh1jIwI) | 5.00 | 1 | Comparable — similar quality but different domain |
| DAG-SHAP (ljZFM2mhbR) | 5.00 | 1 | Comparable |
| Causal Graph via Invariance (Lxst78Rrwj) | 5.00 | 2 | Comparable |
| CoLiDE (fGAIgO75dG) | 5.67 | 2 | Slightly stronger — cleaner theory for its setting, better presentation |
| COSMO (KWO8LSUC5W) | 5.60 | 2 | Comparable — similar level of contribution and issues |
| CMA (pAoqRlTBtY) | 6.25 | 2 | Stronger — more novel integration of LLMs + causal models |

**Round 1 bracket:** 4.5 – 6.5 (determined by comparing against weak anchors at 2.50–3.20 and strong anchors at 8.00).

**Round 2 narrowing:** The paper is clearly better than ψDAG (4.75) which had serious presentation and proof gaps, but somewhat weaker than CoLiDE (5.67) which provides cleaner theoretical guarantees that actually apply to its setting. It is comparable to COSMO (5.60) — both have practical contributions tempered by theoretical overclaim or limited novelty. The two major issues (theory-algorithm mismatch and missing MB method specification) are significant enough to place VISTA below the CoLiDE/COSMO level but above the weaker ψDAG level.

**Final score:** 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>