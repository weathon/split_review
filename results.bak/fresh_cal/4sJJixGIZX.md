Now I have a thorough understanding of both the paper and the reviews. Let me compose the final consolidated review.

## Summary

The paper formalizes Online Continual Graph Learning (OCGL), a node-level streaming setting with bounded per-batch computation, bridging a gap between the online CL and continual graph learning literatures. It provides the first systematic benchmark on four datasets (CoraFull, Arxiv, Reddit, Amazon Computer), adapting six CL methods to the online graph setting. A key additional contribution is identifying "neighborhood expansion"—the problem that multi-hop GNN aggregation can grow to encompass the entire evolving graph—and demonstrating fixed-size neighborhood sampling as a pragmatic first solution.

## Strengths

- **First formal definition of OCGL (Section 3):** The paper provides a precise problem statement with a growing graph, mini-batching, bounded compute per batch, and a task-agnostic algorithm. This bridges a genuine gap identified in Section 2 ("to the best of our knowledge it has not yet been applied to graphs"). The framework is clearly scoped and will serve as a useful reference for future work.

- **Systematic benchmark with four datasets and six adapted methods (Sections 4–6, Tables 1–4):** Four standard node classification graphs are adapted into class-incremental node streams. CL methods (ER, EWC, A-GEM, LwF, MAS, TWP) are each carefully modified for the online setting. Full-neighborhood results establish a set of initial baselines. Replay methods (especially A-GEM) consistently outperform regularization methods, consistent with findings in other domains.

- **Identification of neighborhood expansion as a distinct, graph-specific challenge (Section 3.2, Figure 2):** The paper formally shows that multi-hop neighborhoods can grow to encompass the entire graph as the graph evolves (scaling as O(d^L) where d is average degree). Figure 2 quantifies this on all four datasets, most dramatically on Reddit where 3 hops cover nearly all nodes. This is a unique problem in graph CL not present in standard OCL, and the paper deserves credit for surfacing it clearly.

- **Online-tailored hyperparameter selection protocol (Section 5):** The paper follows Chaudhry et al. (2018b) by using only the first 20% of tasks for validation, avoiding the unrealistic multiple-pass grid search common in prior CGL work. This aligns with the "one pass over the stream" principle of online learning.

- **Anytime evaluation beyond final metrics (Section 6, Figure 1):** The paper reports Average Anytime Accuracy (AAA) and per-task accuracy breakdowns, revealing that regularization methods offer greater stability while replay methods show higher variance and backward transfer. This provides nuance unavailable from final accuracy alone.

## Weaknesses

### Fatal
None. The core contributions (OCGL formalization, benchmarks, identification of neighborhood expansion) are sound and do not rely on any single piece of evidence that would invalidate them.

### Major

- **Missing memory buffer size for ER and A-GEM (Section 4, line 56, 59):** The paper states that ER and A-GEM use a memory buffer with reservoir sampling but never specifies the buffer capacity. For a benchmark paper that aims to establish reproducible baselines, this is a critical omission. The buffer size directly controls the strength of replay and is a standard parameter to report. Without it, researchers cannot replicate or meaningfully compare against these results.

- **Architecture confound between full-neighborhood and sampling experiments (Sections 6 vs. 7, line 75 vs. line 122):** Reddit uses a 1-layer GCN in the full-neighborhood experiments (Section 6) because 2 layers would require almost the full graph, but switches to a 2-layer GCN in the sampling experiments (Section 7: "we use 2 GCN layers on all datasets"). This means the comparison between Tables 3 and 7 does not isolate the effect of sampling—it simultaneously increases model depth. Any difference in performance could be due to the additional layer rather than sampling itself. The paper justifiably makes this change for computational reasons, but it prevents clean conclusions about the cost/benefit of sampling. The paper should either use 1-layer GCN in both settings or add a controlled comparison on a subset of batches where 2-layer full-neighborhood is feasible.

### Minor

- **AAA breakdown only shown for CoraFull (Section 6, Figure 1 vs. claims about other datasets):** The per-task anytime accuracy analysis (Figure 1) is only provided for CoraFull. The paper makes claims about "the other three datasets" (line 107: "On the other three datasets though the higher stability does not offset their poorer performance") without showing the corresponding curves. Since AAA is the most informative metric for online performance, showing this analysis for all datasets would strengthen the claims.

- **Task-free framing vs. class-incremental evaluation (Sections 3–5):** The paper describes OCGL as a "general, task free setting" (line 38) and states the learning algorithm is "task agnostic" (line 71). However, the evaluation stream is built on class-paired task boundaries with task-specific metrics (AA, AF) and a validation protocol that uses task boundaries for hyperparameter selection. The paper explicitly acknowledges this tension (line 71: "This allows us to consider metrics from the CL literature which require task boundaries, even though in our experiments the learning algorithm itself is task agnostic"), which mitigates the issue, but the framing overclaims generality. A clearer separation—positioning the experiments explicitly as class-incremental OCGL evaluation while reserving "task-free" for the abstract setting definition—would resolve the inconsistency.

- **Implementation details for regularization methods not fully specified (Section 4):** The modifications of EWC, LwF, MAS, and TWP to the online setting are described conceptually, but key numerical details are omitted. For EWC (line 58): the running average decay for the Fisher information matrix is not given. For LwF (line 60): the teacher update interval is described as "an additional hyperparameter" but the range of values considered or the selected value is not reported. These are tunable hyperparameters and not reporting them (even as "tuned via validation protocol") reduces reproducibility.

- **High variance in some results not discussed (Tables 1–4):** Several entries show large standard deviations (e.g., ER on CoraFull: 24.2±9.2). The paper reports these honestly but does not discuss their implications for the reliability of conclusions. Although 5 seeds is standard, the high variance on certain methods/datasets warrants commentary, especially for a benchmark intended as a reference.

### Trivial

- **Figure references inconsistent:** The paper references "Figures 3a and 3b" (line 107) but the only anytime evaluation figure available is Figure 1. This appears to be a labeling issue in the manuscript.

## Nice-to-Haves

- A sensitivity analysis for the 20% validation-split threshold: how stable are the method rankings if a different percentage of tasks is used for hyperparameter selection?
- Measuring actual training time and memory per batch in the sampling experiments to ground the practical efficiency claims.
- Reporting the sampling coverage ratio (sampled neighbors / average degree) for each dataset to contextualize the aggressiveness of sampling.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No comparison with GraphSAINT/ClusterGCN"** — The paper explicitly presents random sampling as "a first, simple solution" and "leaves room for further research" (line 148). Criticizing the absence of advanced sampling methods is scope creep for a paper that is primarily a framework+benchmark contribution.

- **"Missing DER/Clipper baselines"** — These are image-domain online CL methods. The paper covers the standard CL categories (regularization, replay) with methods adapted to graphs. Demanding domain-specific additional baselines from a different modality is not reasonable for this scope.

- **"Transductive setting is unusual for online CL"** — Transductive evaluation (using test nodes for message passing but not loss) is standard in graph benchmarks and the paper clearly states this choice (line 71). This is not a flaw, it is a standard design decision in the graph literature.

- **"Section 3.2 ignores clustering/local structure"** — The paper explicitly acknowledges (line 47) that in citation networks "the number of references for an article [is] not [expected] to explode" and that "fixing a low number of layers can be a good solution." The analysis is framed as a general worst-case problem, which is appropriate.

- **"Multiple passes (5) not explained"** — The paper clearly states "multiple passes (5) on each batch" (line 75). This is a standard description.

- **"Sampling sizes chosen without reference to actual degrees"** — The paper states the rationale: "we want to sample significantly less nodes than the average degree for our analysis of the sampling strategy to be meaningful" (line 122). The sizes (5 for CoraFull, 10 for Arxiv, 15 for Reddit) are chosen relative to the datasets' degrees.

- **"Batch size rationale is only computational convenience"** — The paper gives a practical rationale (computational feasibility for larger datasets), which is legitimate. The paper also treats batch size as a variable to analyze its impact, not as a controlled experimental parameter.

## Novel Insights

None beyond the paper's own contributions. The reviews corroborate the paper's framing (OCGL formalization and benchmark) and surface methodological concerns (architecture confound, missing buffer size) but do not generate genuinely novel observations about the problem or results beyond what the authors themselves provide.

## Suggestions

1. **Report the memory buffer size** for ER and A-GEM, and ideally show sensitivity to this parameter. This is essential for a benchmark paper.
2. **Fix the architecture confound** by either (a) using 1-layer GCN for Reddit in both Section 6 and Section 7, or (b) adding a controlled comparison on a subset where 2-layer full-neighborhood is computationally feasible.
3. **Add AAA plots for all four datasets** to support the claims about stability differences across datasets.
4. **Clarify the task-free vs. class-incremental framing** by explicitly stating that the *setting* is general/task-free but the *evaluation* in this paper instantiates the class-incremental scenario.
5. **Specify the hyperparameter search ranges** for the running average decay (EWC), teacher update interval (LwF), and learning rate values considered.
6. **Add a brief discussion of the high variance** observed in some entries, noting whether it affects the qualitative conclusions.

## Score and Decision

The paper makes a solid contribution by formalizing OCGL, constructing the first systematic benchmark, and identifying neighborhood expansion as a distinct challenge. The weaknesses are real but fixable: the missing buffer size is the most serious gap for a benchmark paper, and the architecture confound limits clean interpretation of the sampling analysis. Neither undermines the core contribution of the OCGL framework itself. With the suggested revisions, this would be a strong reference for the field.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>