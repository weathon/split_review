## Summary

VISTA is a modular framework for causal structure learning that decomposes the global DAG learning problem into node-centered Markov Blanket subgraphs, aggregates local predictions via a weighted voting mechanism with exponential down-weighting of low-support edges, and enforces acyclicity through a greedy Feedback Arc Set heuristic. The framework is model-agnostic, operates purely on edge-level outputs, and requires only a one-time O(|V|²) aggregation pass. The paper provides theoretical error bounds (under an idealized independence assumption) and extensive synthetic experiments across six base learners.

## Strengths

1. **Clean coverage guarantee (Proposition 3.1):** The paper formally proves that the union of node-centered Markov Blanket subgraphs contains every true edge. This is a simple but important formal justification that most existing modular frameworks lack, and it correctly grounds the divide-and-conquer strategy.

2. **Consistent empirical improvement across diverse base learners and graph families:** Using a single fixed hyperparameter setting (λ=0.5, t=0.7), VISTA-WV improves F1 and reduces FDR relative to every standalone base learner on both ER and SF graphs. For example, NOTEARS F1 improves from 0.76→0.79 (ER5), GOLEM from 0.35→0.60 (ER5), GraN-DAG FDR drops from 0.92→0.43 (ER5). The improvements hold across six very different base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM), supporting the model-agnosticism claim.

3. **Substantial and well-documented runtime reductions:** Table 3 shows 2–10× speedups across all tested base learners (NOTEARS from 12,515s to 2,136s at n=300, SCORE from 10,040s to 198s at n=100). The speedups come from decomposing the graph into smaller subproblems, and the framework supports parallel execution in the divide phase. This is a practical and significant contribution.

4. **Theoretical analysis provides useful qualitative guidance despite acknowledged limitations:** Theorems 3.2, 3.4, and 3.5 formalize how the required number of subgraph votes depends on the gap between the true orientation probability p and the effective threshold. The λ sensitivity analysis (Figure 4) empirically validates the predicted precision–recall trade-off, showing that the theory provides useful practical guidance even if the strict independence assumption is violated.

## Weaknesses

### Major

1. **The Markov Blanket solver used in experiments is not specified in the main paper.** The pseudocode (Figure 2) treats `MB_solver` as a parameter, but the main text never states which MB identification algorithm was used in the experiments, what hyperparameters were chosen, or how it was validated. The paper states "we also provide a flexible interface in our implementation" and mentions the DCILP MB solver in passing (for the appendix comparison), but the reader cannot determine what MB solver produced the main results (Tables 1–4). This is a fundamental reproducibility gap — the MB stage is the very first step of the pipeline, and without knowing what algorithm was used, the entire experimental evaluation is difficult to assess or reproduce. The supplementary code is mentioned in the reproducibility statement, but the paper itself should state this information.

2. **Real-data evaluation is limited to a single small graph (Sachs, 11 nodes).** The Sachs network is a standard benchmark, but at 11 nodes it does not demonstrate the claimed scalability or the benefits of the divide-and-conquer strategy. The paper's central selling point is handling large-scale graphs, yet the only real-data experiment is on a graph that can be learned directly by any baseline without decomposition. At minimum, one larger real benchmark (e.g., from the bnlearn repository with 20+ nodes, or a gene regulatory network) is needed to establish that the approach works outside synthetic settings.

### Minor

3. **The theoretical guarantees are derived under an independence assumption that is acknowledged to be violated, creating a gap between claimed and delivered guarantees.** Theorem 3.2 models votes as independent Binomial trials, but the paper admits (end of §3.1) that "subgraphs learned from the same dataset can induce correlations among votes, so the bound should be interpreted as a qualitative guide." The abstract and introduction claim "finite-sample error bounds" and "asymptotic consistency guarantees" without immediately caveating the independence assumption. While the paper is transparent about the limitation, the presentation overstates what is actually proved. This is not a fatal flaw (many causal discovery papers have similar theory-practice gaps), but the framing should be adjusted to avoid misleading readers.

4. **No ablation study isolating the contribution of individual components.** The experiments compare "baseline vs. VISTA-NV vs. VISTA-WV," but this conflates the MB decomposition effect with the aggregation scheme. Specific questions left unaddressed:
   - How much of the improvement comes from the MB decomposition itself versus the weighted voting?
   - What happens if naive voting is used *without* FAS? What about weighted voting *without* FAS?
   - The ordering of FAS before threshold filtering is claimed to be important (Section 3.1), but this is not experimentally validated.
   - No sensitivity analysis is shown for the threshold parameter t (fixed at 0.7 throughout).

5. **The DAG-GNN VISTA-NV result on normalized data (Table 2) shows aggregation harming performance without discussion.** On normalized data (n=50, ER5), DAG-GNN baseline achieves F1=0.55, but VISTA-NV drops to F1=0.25. The weighted voting recovers to 0.63, which is better than baseline. However, the paper does not discuss why naive voting hurts DAG-GNN specifically under normalization, which would be informative about the method's sensitivity properties.

6. **The FAS post-processing is not covered by the theoretical analysis.** The consistency theorem (Theorem 3.5) and error bounds (Theorems 3.2, 3.4) apply only to the weighted voting output, not to the final DAG after FAS and threshold filtering. The paper notes in the conclusion that FAS "may also prune edges that are weakly supported yet correct," but this limitation is not addressed in the experiments or analysis. Since FAS can remove correct edges that were correctly identified by the voting stage, the theoretical guarantees do not extend to the actual output of the system.

### Trivial

7. Table formatting renders inconsistently in places (e.g., line 204 shows "123.3" with a decimal point but other entries use two decimals; the GraN-DAG method name is inconsistently capitalized as "Gran-DAG" in Table 1 but correctly as "GraN-DAG" elsewhere).

## Nice-to-Haves

- A comparison to at least one other modular framework (DCILP, SADA) in the *main* paper, not only the appendix — the paper acknowledges this comparison exists in Appendix F.2, but the main results would be strengthened by including it.
- A larger real-world dataset (e.g., from bnlearn or gene expression) to demonstrate scalability claims on real data.
- Significance testing (e.g., paired bootstrap) to quantify whether VISTA-WV improvements over baselines are statistically significant, given that some improvements are modest.

## Removed Points

*"Theoretical guarantees are not applicable to the actual method"* (harsh critic's claim of a fatal flaw) — Demoted to **Minor** weakness #3. The paper openly acknowledges the independence assumption is violated and frames the bounds as a "qualitative guide." This is a real limitation, but the paper is transparent about it, and the λ sensitivity experiments (Figure 4) empirically validate the predicted monotonic trends. Many published causal discovery papers have similar theory-practice gaps (e.g., the 6.0-scored "Causal Discovery in the Wild" ensemble paper has the same issue and was accepted). Calling it "fatal" overstates the severity given current community standards.

*"No comparison to other modular approaches at all"* — Partially removed. The paper states (line 178) that a comparison to DCILP is provided in Appendix F.2 (stripped by the parser). So a comparison does exist in the submission; it is fair to note its absence from the main paper but incorrect to claim it's entirely missing.

*"The extremely high FDR of VISTA-NV (0.87) is a red flag"* — Removed. The paper explicitly frames NV as a demonstration that all true edges are captured in the candidate pool, with WV acting as a principled filter to prune FPs. The high FDR of NV is expected and the paper is transparent about it.

*"Missing ablation for naive voting without FAS"* — Merged into Minor #4 rather than listed separately.

*"GraN-DAG TPR drops on Sachs"* — Removed as a standalone criticism. The paper presents the full set of metrics including SHD (16→12), FDR (0.82→0.00), and SID (48→45), all of which improve. The TPR drop is a trade-off, not a hidden flaw.

Several generic criticisms from the harsh critic about "missing larger dataset," "sensitivity to threshold parameter t," and "edge-case analysis" have been moved to Nice-to-Haves where appropriate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the MB solver explicitly in the main paper.** State which algorithm was used (e.g., IAMB, PCMB, or a heuristic threshold on pairwise associations), its hyperparameters, and how its quality was validated. This is necessary for reproducibility.

2. **Add at least one moderate-sized real benchmark** (e.g., from the bnlearn repository with 20–100 nodes) to demonstrate scalability on real data.

3. **Include a simple ablation:** compare VISTA without FAS, VISTA with FAS before vs. after thresholding, and VISTA with uniform (unweighted) voting plus FAS. This would isolate the contribution of each design choice.

4. **Reframe the theoretical section** to avoid claiming "finite-sample error guarantees" for the deployed method. Either derive bounds that hold under dependence, or explicitly state upfront (abstract, introduction) that the theory provides qualitative guidance under an idealized model.

5. **Discuss the DAG-GNN normalized-data anomaly** (Table 2) and any other cases where NV harms performance, to provide insight into when the method may fail.

**Score and Decision**

I calibrate against the following anchor papers retrieved across two rounds of calibration search:

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Causal Discovery in the Wild (voting ensemble) | WtbPaWO8lH.md | 6.00 | R2 | Most similar: voting-based aggregation for CD, same independence assumption issue. Has stronger real-data evaluation (multiple bnlearn benchmarks) and clearer theory framing. VISTA has better runtime results and broader synthetic eval, but weaker on reproducibility. |
| Multi-View Causal Discovery | wnFbqvUJ6D.md | 5.00 | R1,R2 | Mixed reviews (8,4,6,2). Strong theory but practical assumption concerns. Comparable to VISTA in overall quality. |
| Query-Specific Causal Graph Pruning | bOfiLeoUJf.md | 4.67 | R1,R2 | Accepted as Poster despite a low 2 from one reviewer. Narrower scope but clean evaluation. VISTA is slightly stronger. |
| CausalSteward (D&C framework) | 3lFAyPa9Fe.md | 4.00 | R1 | D&C framework but with LLM-agent overhead. VISTA is clearly stronger methodologically and in evaluation rigor. |
| Improving constraint-based discovery (MosaCD) | 7K8mS5QNkf.md | 4.50 | R1 | LLM+constraint-based hybrid. Data leakage concerns. VISTA is comparable or slightly stronger. |

**Round-1 bracket:** 3.5–7.5. **Round-2 narrowing:** Inspecting anchors around 4.5–6.0 places VISTA between CausalSteward (4.0) and the "Wild" ensemble paper (6.0). VISTA's core idea is well-motivated and the synthetic experiments are extensive, but the unspecified MB solver, single real dataset, and lack of ablations make it weaker than the accepted ensemble paper. I rate it slightly below the Multi-View CD paper (5.0) due to reproducibility concerns, settling at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>