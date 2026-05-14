Now I have all the information I need to produce the consolidated review.

---

## Summary

This paper identifies a genuine and practically important gap in interventional causal discovery: post-treatment selection bias, where samples are retained only after interventions (e.g., QC filtering in single-cell genomics). The authors model this via an augmented DAG with explicit selection nodes, define a finer-grained equivalence class (FI-Markov equivalence) and a new graphical representation (F-PAG) that extends PAGs with square marks and new edge types, and propose a sound and complete constraint-based algorithm (F-FCI). The theoretical development is rigorous, and experiments on synthetic and real-world data show improvements over six baselines.

## Strengths

- **Novel problem formulation with real practical relevance.** The paper identifies a previously overlooked source of bias in interventional causal discovery — post-treatment selection. The case is compellingly illustrated (Figure 1: existing methods cannot distinguish causal relations from selection-induced dependencies) and grounded in concrete applications (single-cell QC filtering, per-protocol clinical trial analysis). This is a genuine extension of the problem scope beyond what existing frameworks (FCI, GIES, CDIS) handle.

- **Rigorous theoretical characterization of FI-Markov equivalence and F-PAG.** The paper formalizes the augmented DAG with intervention indicators and selection (Definition 1), characterizes CI patterns that distinguish causal relations from selection (Lemmas 2–4, Theorem 1), defines FI-Markov equivalence (Definition 2), and provides graphical criteria (Theorem 2). The F-PAG representation (Definition 5) extends PAGs with new edge types (→-, -, □-□, etc.) that capture strictly more information than standard PAGs. The soundness (Theorem 3) and completeness (Theorem 4) proofs are provided.

- **Provably sound and complete algorithm.** F-FCI (Algorithm 1) integrates observational and interventional CI patterns with tailored orientation rules. The proof structure builds appropriately on prior work (Kocaoglu et al. 2019, Zhang 2008b) and extends it to handle post-treatment selection. The algorithm is implemented and the code is released.

- **Comprehensive empirical evaluation.** Experiments span synthetic graphs with 10–25 variables (Figure 6, Figure 10), scalability to 50 variables (Figure 11), robustness under varying noise levels (Figure 12), and a large-scale real-world application to the Norman single-cell perturbation dataset (5,045 genes, 105 perturbations). F-FCI consistently improves DAG Precision (≈5%+) and reduces SHD over six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-INTERVEN, CDIS). Table 1 directly reports accuracy of identifying post-treatment selection.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation does not disaggregate the core claim by edge type.** The paper's central contribution is distinguishing causal relations from selection-induced dependencies (Figure 1). Yet the main metrics (DAG Precision, DAG SHD, F1) are aggregated over all edges, conflating the novel contribution with standard parts of the graph. Table 1 reports accuracy for identifying post-treatment selection, which partially addresses this, but there is no breakdown by specific edge type (→-, -, □-□) or per-intervened-pair performance. Without knowing whether F-FCI correctly classifies Figure 1(a) vs (b) where baselines fail, the reader cannot verify whether the claimed distinguishing power is real or driven by improvements elsewhere in the graph. This is the paper's most significant empirical gap.

- **Algorithm Step 2.3 is underspecified.** The description of detecting Type I inducing nodes in Step 2.3 lacks sufficient operational detail. The paper says "Detect if the path has non-endpoints vertex and Type I inducing nodes" without specifying the detection procedure. The notation "XI(i) → Xn □- Xj" mixes marks that come from different sources (some from Step 2.2, some from the path structure), and it is not fully clear how the required edge marks are obtained for non-intervened nodes along the path. While this is not a fundamental circularity (the critic's claim is overstated — Step 2.2 does produce square marks before Step 2.3 runs), the description is not precise enough to implement from the text alone. The requirement that Type I inducing nodes must have available interventional data is also a significant practical limitation that should be discussed explicitly.

### Minor
- **Precision-recall tradeoff with FCI-INTERVEN is not discussed.** Table 2 shows that F-FCI has substantially higher precision (e.g., 60.1 vs 46.7 for n=500 hard) but lower recall (55.7 vs 69.0) compared to FCI-INTERVEN. The paper frames this as an advantage, but the recall drop means F-FCI misses more true edges. Reporting F1 (which is comparable: 56.7 vs 54.8) partially mitigates this, but a frank discussion of the precision-recall tradeoff is warranted.

- **Real-world validation is a coverage check, not a discrimination test.** The biological experiment (Section 5.2) reports which edges F-FCI finds and checks against databases (Enrichr, ARCHS4). This verifies that some outputs are consistent with prior knowledge, but does not evaluate (a) how many edges are not supported, (b) whether baselines find the same supported edges more efficiently, or (c) whether the flagged selection genes are genuinely due to QC filtering rather than other biological functions. The connections drawn (CDKN1A → cell-cycle arrest → QC filtering) are plausible but speculative.

- **The "at least two observed parents" assumption for selection is stated but not motivated.** Line 156 assumes selection works on at least two observed variables, which excludes the common case of selection on a single variable (e.g., thresholding on one QC metric). The paper does not discuss how restrictive this is or whether it can be relaxed.

- **No complexity analysis.** The algorithm inherits FCI's exponential search over conditioning sets, and the F-PAG orientation rules additionally check paths between every pair of intervened nodes. The paper acknowledges parallelization via Fast FCI but provides no runtime analysis or scaling discussion beyond a figure showing a 50-variable output.

### Trivial
- The new edge marks (→-, -, □-□, □-, □) in Figure 5 are visually dense and hard to distinguish. A larger, clearer figure would help.
- The claim "go beyond traditional equivalence classes toward the underlying true causal structure" (line 22) is slightly over-enthusiastic given that F-FCI still identifies up to FI-Markov equivalence, not the exact DAG. The paper correctly qualifies this elsewhere.

## Nice-to-Haves
- Reporting precision/recall/F1 specifically on edges between intervened nodes, broken down by edge type.
- A "controlled experiment without selection" to verify that F-FCI degrades gracefully to matching baselines when there is no post-treatment selection.
- A discussion of how many intervened variables are needed in practice and what happens when only a subset of potential Type I nodes have interventions.

## Removed Points

**Removed: "Algorithm circularity in Step 2.3" as fatal flaw.** The claim that detecting Type I inducing nodes is circular because they are defined in terms of →□ edges in the F-PAG under construction is incorrect. Step 2.2 already assigns edge marks (including square marks) to edges between intervened node pairs before Step 2.3 runs. Step 2.3 then detects Type I nodes along paths using those pre-existing marks. The description is underspecified (see Major weaknesses), but not circular. The circularity criticism is moved here.

**Removed: "Simulation selection mechanism may not reflect real selection."** The paper uses a sum of nonlinear functions with thresholding. This is a reasonable synthetic mechanism for a first evaluation. Whether it perfectly matches real selection is a secondary concern that does not threaten the paper's contribution.

**Removed: "Harsh critic's claim that Theorem 1's statement about conditional invariance under post-treatment selection is stated without proof."** The paper states this as a known property from the augmented DAG framework (citing Tian & Pearl 2001, Kocaoglu et al. 2019). Theorem 1 provides the formal CI/invariance mapping for the general setting.

**Removed: "Missing related works" style criticisms.** These cannot be verified without external sources.

**Removed: Various formatting/style nitpicks.** These are parser artifacts, not author errors.

## Novel Insights

The harsh critic's most valuable observation is the evaluation gap: the paper's central distinguishing power is not directly measured at the edge-type granularity that would most convincingly demonstrate the contribution. However, this is an empirical gap, not a theoretical flaw. The critic's circularity claim is incorrect upon verification — Step 2.2 produces square marks before Step 2.3 uses them — though the underspecification complaint has merit. A genuinely novel insight is the precision-recall asymmetry in Table 2: F-FCI trades recall for precision relative to FCI-INTERVEN, which may or may not be desirable depending on the application. The paper would benefit from acknowledging and contextualizing this tradeoff.

## Suggestions

1. **Add targeted evaluation for the core claim.** Report precision, recall, and accuracy specifically on edges between intervened nodes, broken down by edge type (→, →-, -, →, □-□, etc.). Show a confusion matrix comparing predicted vs. true edge types. This would directly validate the Figure 1 claims.

2. **Clarify Step 2.3 implementation.** Provide pseudocode or a more detailed description of how Type I inducing nodes are detected along inducing paths, including how the required edge marks for non-intervened nodes are obtained.

3. **Discuss the precision-recall tradeoff openly.** Address why F-FCI has lower recall than FCI-INTERVEN and in what scenarios users should prefer one over the other.

4. **Add a "no selection" control experiment.** Show that F-FCI matches baseline performance when there is no post-treatment selection (only latent confounders). If performance degrades, explain why.

5. **Provide a runtime/scaling analysis.** Even a brief discussion of how the number of CI tests scales with graph size and number of interventions would be useful for practitioners.

## Score and Decision

I evaluated this paper against the following calibration anchors:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `ta8BKRa1bl.md` | 6.00 (Accept Poster) | Strong identifiability theory, very narrow experiments (bivariate only). Our paper has broader experiments but less striking theoretical novelty. Comparable overall quality. |
| `WtbPaWO8lH.md` | 6.00 (Accept Poster) | Solid contribution with theory and experiments. Our paper has stronger theoretical depth. |
| `expkpx9TWg.md` | 4.00 (Reject) | Decent theory but significant concerns about evaluation and scope. Our paper has stronger empirical support and clearer contribution. |
| `V7pT2ZRoTB.md` | 4.50 (Accept Poster) | Theory-focused, questions about practical relevance. Our paper has better practical grounding. |
| `aS7EVadvZD.md` | 3.00 (Reject) | Fundamentally flawed theory and poor writing. Our paper is in a different tier. |

This paper makes a clear and well-motivated contribution to a genuine problem. The theory is rigorous, the algorithm is principled, and the experiments show meaningful improvements. The most significant weaknesses are the evaluation gap (not disaggregating by edge type) and the underspecified algorithm step — both addressable. No fatal flaws exist. 

Relative to the anchors, the paper sits comfortably in the 6.0 range: stronger than papers scoring 4.0–5.0 (which typically have significant empirical or theoretical gaps), comparable to well-regarded papers at 6.0 (which have genuine strengths and tolerable weaknesses), but below the exceptional papers at 7.0+ (which would have more polished evaluation or more striking results).

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>