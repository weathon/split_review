Now I have sufficient calibration data. Let me formulate my final review.

## Summary of Calibration

**Round 1 bracket**: Between ~3.5 and ~6.5 (the paper is clearly stronger than the 3.0 rejects but not at the level of 7.0+ papers).

**Round 2 narrowing**: The paper compares to PoseCheck (4.75) and MF-LAL (5.2) — both have method contributions with evaluation gaps — but is weaker than DynamicFlow (6.2, accepted). I place it at **5.0**.

Now I'll write the final consolidated review.

## Summary

The paper proposes Active Probabilistic Drug Discovery (APDD), a method that combines probabilistic clustering (MPC), selective molecular docking via Vina-GPU+, and active wet-experiment feedback to reduce computational and experimental costs in early drug discovery. The core formulation — treating drug discovery as an active probabilistic learning problem where active molecules cluster in chemical space, using clustering to guide selective docking and active refinement — is novel and well-motivated. Experiments on 79 DUD-E and 11 LIT-PCBA targets show average reductions of 80%+ in docking runs and 40-75% in wet-lab experiments compared to full enumeration docking. However, the evaluation has several significant gaps that prevent the paper's central claims from being fully supported: the target recall rate used as the stopping criterion is never stated, so the "high accuracy" claim is unverifiable; the active learning component is not ablated; and simpler baselines are missing. The method is promising and the results are suggestive, but the evidence as presented is insufficient to validate the claimed contributions.

## Strengths

1. **Novel formulation and method design**: The paper casts early drug discovery as an active probabilistic learning problem, proposing the APDD pipeline that integrates probabilistic clustering (MPC), selective docking, and principled active refinement. The query strategy (Eq. 3, 5) uses expected recall improvement, which is a well-motivated departure from simple score-ranking approaches. (Sections 3–4)

2. **Substantial and well-documented cost savings across 90 targets**: On 79 DUD-E targets, APDD achieves an average 82% reduction in docking runs and 75% reduction in wet-lab experiments; on 11 LIT-PCBA targets, 85% and 40% reductions respectively. Results are reported per-target in Tables 1–2, providing multi-protein evidence of efficiency. The savings are substantial and presented transparently.

3. **Validation of the clustering assumption**: Table 3 demonstrates that active molecules in DUD-E are completely separated from decoys in small clusters (P_k=1.0 for k=2,4,6), with 52% of actives in clusters of size ≤6 for aa2ar. This directly supports the paper's core premise that active molecules cluster in chemical space.

4. **Scalability demonstration on 1.4M molecules**: On augmented datasets (Table 4), APDD recovers active molecules using ~20% of the docking and wet-lab costs of enumeration, showing practical applicability to large virtual libraries.

5. **Principled handling of unreliable docking scores**: The isotonic regression mapping from Vina scores to binding probabilities (capped at 0.3 per literature) and the multi-modality fusion framework (Eq. 4.2) address known limitations of docking-based screening.

## Weaknesses

### Fatal
None. The core method is sound, the experiments are extensive, and the cost-savings comparison between APDD and VE at the same recall level is meaningful. However, significant evaluation gaps exist (see below).

### Major

1. **Target recall rate is not stated, making the "high accuracy" claim unverifiable**. The paper states it terminates "when the recall rate of the top 100 molecules reaches the target recall rate" (Section 5.1) and that APDD achieves "the same recall rate" as VE — but the target recall value is never specified per target or globally. Without knowing whether APDD is recovering 90% of actives or 20%, the claim of "maintaining high accuracy" (abstract) is unsubstantiated. The relative cost savings between APDD and VE are valid at the same recall level, but their practical significance depends on the absolute recall achieved. This is the single most important missing piece in the evaluation.

2. **Missing ablation of the active learning component**. The paper does not compare APDD against a simpler variant that uses only clustering + representative docking without the active refinement loop. Such an ablation is essential to measure the contribution of the wet-experiment feedback and the query strategy described in Section 4.3. Without it, it is unclear whether the cost savings are driven by the clustering (which aggregates similar molecules) or the active learning refinement.

3. **Missing simpler baselines**. The only baseline is Vina Enumeration (VE), which docks all molecules. There is no comparison with (a) random selection of molecules for docking, (b) clustering + random selection of representatives, or (c) a clustering-only approach without active refinement. These simple baselines would contextualize the gains from the active learning component. The paper's justification that "machine learning models cannot be retrained or fine-tuned due to the limited number of wet experiments" explains the absence of ML-based active screening baselines, but does not justify the absence of simple non-ML baselines.

### Minor

1. **Probability calibration not empirically validated**. The paper states that the Tanimoto-based pairwise probability (Eq. 1) is "further validated using statistics from Lit-PCBA/DUD-E/PubChem datasets" (Section 4.1), but no such validation is shown. The isotonic regression mapping from Vina scores to probabilities (Section 4.2) is also not evaluated with calibration curves or hold-out validation. While Table 3 validates clustering structure, it does not validate that the probability estimates are well-calibrated.

2. **APDD underperforms on several LIT-PCBA targets but this is not systematically characterized**. APDD requires 290% (MAPK1), 121% (KAT2A), and 131% (PKM2) of the wet experiments compared to VE (Table 2). The paper attributes this to "low-quality" or "uniform" Vina scores, but does not report the Vina AUC per target or systematically analyze the relationship between Vina score quality and APDD's relative performance. This would give practitioners clearer guidance on when to apply the method.

3. **Large-scale test uses random inactive molecules**. The 1.4M molecule experiment (Section 5.4) augments DUD-E targets with random inactive molecules from other proteins, rather than using properly constructed decoy sets. Random inactives are likely easier to separate from actives than carefully matched decoys, which may inflate APDD's measured advantage.

4. **No sensitivity analysis of key parameters**. The number of nearest neighbors (k=50), number of representatives per cluster, number of active learning iterations, and the maximum probability cap (0.3) are set without ablation or sensitivity analysis on representative targets.

5. **Computational overhead of clustering is not discussed**. APDD requires k-NN search on the full library for MPC initialization. For million-molecule libraries, this overhead is relevant to the claimed cost savings but is not reported.

### Trivial
None that warrant mention given the parser artifacts.

## Nice-to-Haves

- A systematic characterization of when APDD underperforms (e.g., a scatter plot of Vina AUC vs. APDD/VE cost ratio for each target) would be practically valuable.
- Reporting standard screening metrics (enrichment factor, ROC AUC of the probability ranking) alongside the cost savings would strengthen the paper.
- A figure showing the convergence behavior of APDD over active learning iterations for a representative target would help the reader understand the method's dynamics.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justifications:

- **"Cost numbers are meaningless without accuracy numbers"** — Overstated. The cost comparison between APDD and VE is at the *same* recall level; it is meaningful in relative terms. The specific issue is that the absolute recall level is unknown, which is addressed in Major weakness #1.
- **"The paper does not report any screening metrics"** — The paper does report cost savings at the same recall level as the baseline, which is a valid comparison format. The missing information is the absolute recall value, not the comparison itself.
- **"Prior clustering methods 'cannot effectively separate active molecules' is asserted without evidence"** — Table 3 provides direct evidence that MPC separates actives from decoys on DUD-E.
- **"Missing code and data release"** — The paper states these will be available upon acceptance. Per hard rules, such points are removed.
- **"Selection of k=50 not justified"** — This is a generic hyperparameter sensitivity concern; folded into Minor weakness #4.
- **"The baseline does not represent SOTA active screening"** — The paper provides a reasonable scope justification (no model retraining). However, simpler non-ML baselines are missing (kept as Major #3).
- **"The formulation conflates affinity with binding probability"** — This is the paper's key insight (treating docking scores as probabilistic), not a confusion.

## Novel Insights

The reviews reveal a tension that the paper itself does not fully resolve: the probabilistic formulation is elegant and the clustering validation (Table 3) is genuinely strong for DUD-E, but the evaluation framework — cost savings at an unspecified recall level — creates a disconnect between the method's theoretical grounding and its empirical support. The paper would be significantly strengthened by closing this gap with a single table showing the actual recall values achieved on each target, which would simultaneously validate the "high accuracy" claim and make the cost savings fully interpretable.

## Suggestions

1. **State the target recall rate** explicitly for each target (or globally) and report the actual recall achieved by both APDD and VE. This is the single most important fix.
2. **Add an ablation study** comparing APDD against a clustering-only variant (without active refinement).
3. **Add simple baselines**: random selection, clustering + random representative selection.
4. **Validate probability calibration** with reliability diagrams or AUC of predicted binding probabilities against known labels.
5. **Report Vina AUC per target** and show the relationship with APDD's relative cost savings.
6. **Perform sensitivity analysis** on k (nearest neighbors), number of representatives, and number of active learning iterations.

## Score and Decision

**Final Score: 5.0**

**Decision: Reject**

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/An87ZnPbkT.md | 3.00 | R1 | Weaker — method is about algorithm selection, not a full pipeline; less extensive experiments |
| /home/wg25r/review_agent/human_reviews/nWO75tVjfp.md | 3.00 | R1 | Weaker — focuses on dataset noise analysis without a novel pipeline method |
| /home/wg25r/review_agent/human_reviews/uUEvmY8Gfz.md | 3.00 | R1 | Weaker — RL for de novo design with different scope; less experiment coverage |
| /home/wg25r/review_agent/human_reviews/IZiKBis0AA.md | 3.00 | R1 | Weaker — fragment-based antibiotic design; different problem scope |
| /home/wg25r/review_agent/human_reviews/rjLgCkJH79.md | 3.67 | R2 | Weaker — lead optimization RL method with preliminary experiments; current paper has more extensive evaluation despite gaps |
| /home/wg25r/review_agent/human_reviews/eIYDKNqXuV.md | 3.80 | R2 | Weaker — pure clustering method; no drug discovery pipeline |
| /home/wg25r/review_agent/human_reviews/q20kiEt1oW.md | 3.75 | R2 | Not comparable — learning curve estimation |
| /home/wg25r/review_agent/human_reviews/bKAqK7Bh7n.md | 5.20 | R1/R2 | Comparable — MF-LAL has active learning for drug discovery with evaluation gaps; current paper has more extensive multi-target experiments |
| /home/wg25r/review_agent/human_reviews/S8gbnkCgxZ.md | 7.00 | R1 | Stronger — careful dataset curation with thorough evaluation; accepted poster |
| /home/wg25r/review_agent/human_reviews/QfyZ28FpVY.md | 4.00 | R1 | Comparable but different domain — DEL ranking with clear method but presentation issues |
| /home/wg25r/review_agent/human_reviews/xoUUCS9IGl.md | 4.75 | R1/R2 | Comparable — PoseCheck has evaluation gaps (missing baselines) similar to current paper |
| /home/wg25r/review_agent/human_reviews/KSLkFYHlYg.md | 8.00 | R1 | Stronger — generative model with thorough evaluation; accepted oral |
| /home/wg25r/review_agent/human_reviews/HhfcNgQn6p.md | 7.75 | R1 | Stronger — theory paper; not directly comparable |
| /home/wg25r/review_agent/human_reviews/0VBsoluxR2.md | 8.00 | R1 | Stronger — MOF generation with thorough evaluation |
| /home/wg25r/review_agent/human_reviews/5t57omGVMw.md | 8.00 | R1 | Stronger — theory paper; not comparable |
| /home/wg25r/review_agent/human_reviews/9qS3HzSDNv.md | 6.20 | R2 | Stronger — DynamicFlow has more polished evaluation despite concerns; accepted poster |

**Reasoning**: The paper presents a genuinely novel formulation and extensive experiments across 90 targets with substantial cost savings. However, the evaluation has three significant gaps: (1) the target recall rate is not stated, making the "high accuracy" claim unverifiable; (2) the active learning component is not ablated; (3) simpler baselines are absent. These gaps are addressable but collectively prevent the paper from being accepted in its current form. The method is promising and could become a strong contribution with revisions, particularly by reporting the actual recall achieved and adding ablations. Score 5.0 reflects a paper that is above the rejection baseline (it has a valid method and substantial data) but falls short of the acceptance threshold due to incomplete evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>