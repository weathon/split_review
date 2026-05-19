## Summary
This paper proposes Active Probabilistic Drug Discovery (APDD), a framework combining probabilistic molecule clustering (via Fast Probabilistic Clustering on Morgan fingerprints), selective docking of cluster representatives with VinaGPU+, and active-learning-driven wet-lab experiment selection. The core idea is to treat early drug discovery as an active probabilistic learning problem where active molecules are assumed to be cluster-distributed. Experiments on 79 DUD-E and 11 LIT-PCBA targets report 80%+ reduction in docking runs and 70%+ reduction in wet-lab experiments compared to exhaustive docking with top-score selection (Vina Enumeration).

## Strengths
- **Large-scale empirical validation of cost savings on standard benchmarks.** The paper reports an average 82% reduction in VinaGPU+ docking runs and 75% reduction in wet-lab experiments across 79 DUD-E targets (Section 5.2, line 188). These numbers are documented target-by-target (Table 2), allowing readers to see per-target behavior including cases where the method struggles.

- **Scalability demonstrated on >1 million molecules.** On five DUD-E proteins augmented with 1.4M inactive molecules from other targets, APDD recovers the same number of active ligands using ~20% of the docking and wet experiments required by VE (Section 5.4, Table 4). This speaks to the method's relevance for real-world library sizes.

- **Empirical verification of the cluster assumption.** Table 3 (Section 5.3) shows that active molecules concentrate in a small number of tight clusters (size ≤8) and are well-separated from inactive molecules on both DUD-E and LIT-PCBA targets. This directly supports the paper's key assumption that active ligands are cluster-distributed, explaining why clustering-based active learning can reduce unnecessary experiments.

- **Well-articulated formalization of the query strategy.** Section 4.3 defines expected recall improvement (Equation 3) with cluster-based and molecule-based variants (Equations 4–5), providing a principled mechanism for selecting wet-lab experiments and propagating binding probability updates to neighboring molecules via conditional probability.

## Weaknesses
### Major

- **Insufficient baselines to isolate the contribution of the probabilistic machinery.** The only comparison is Vina Enumeration (VE): dock every molecule, pick top-scoring ones for wet lab. The paper does not compare against simpler clustering-based alternatives such as (a) k-means/UMAP + centroid docking + top-score selection, (b) random sampling of cluster representatives, or (c) diversity-based active learning (e.g., farthest-point sampling). The paper states that ML methods are excluded because they "cannot be retrained or fine-tuned due to the limited number of wet experiments" (line 177), but this justification does not cover non-ML clustering or heuristic selection strategies that require no retraining. Because APDD docks only cluster representatives (which any clustering method would achieve), the meaningful question is whether the *probabilistic clustering and active refinement* add value over simpler cluster-then-dock pipelines. Without these ablations, the reported savings cannot be cleanly attributed to the proposed method's novel components.

- **Underspecified probability calibration training data.** Section 4.2 states that isotonic regression learns the docking-score-to-binding-probability mapping from "open labeled data, which includes proteins and molecules with active or inactive label information" (line 100). The paper does not specify whether these data are disjoint from the 90 test targets (DUD-E and LIT-PCBA). DUD-E and LIT-PCBA are the standard sources of open labeled data in this domain; if they were used for calibration, the probability estimates on test targets would be contaminated. The paper reports a cap at 0.3 based on published literature, but the shape of the calibration curve (not just the cap) influences active-learning decisions. This ambiguity undermines reproducibility and the validity of the probability-driven selection. The paper should either (i) specify that the isotonic regression was trained on a held-out set of proteins (e.g., from PDBbind or a disjoint subset of DUD-E), or (ii) demonstrate that results are insensitive to the calibration source.

### Minor

- **Ambiguity in the recall target stopping criterion.** Section 5.1 states the APDD cycle terminates "when the recall rate of the top 100 molecules reaches the target recall rate" (line 177), but the numerical value of this target is never defined. The reported cost reductions (Tables 2–4) are relative to reaching this unspecified target. This makes the quantitative claims difficult to reproduce or compare, as the relative savings could be sensitive to where the target is set. The paper should either report the target per target or provide cost-vs.-recall curves over a range of recall levels.

- **Multi-modal score fusion is described but not used.** Section 4.2 presents a multi-modal score fusion procedure (lines 102–106) allowing integration of docking scores from multiple tools. However, all experiments use only VinaGPU+. This aspirational content adds confusion about what was actually implemented and evaluated.

- **No reporting of variance or run-to-run stability.** Results appear to be from single runs. MPC is deterministic with fixed k, but the KNN retrieval and active-learning selection procedure could have stochastic elements. At minimum, the paper should state whether the full pipeline is deterministic or provide variance estimates.

- **Conclusion overreaches the evidence.** The conclusion claims APDD "aims to eliminate the need for lead optimization" (line 230). The experiments only evaluate early-stage screening (hit identification), not lead optimization. This claim is unsupported.

### Trivial

- **"Open labeled data"** (line 100) is a vague term that should be replaced with specific dataset names.
- **Tables referenced as images** are not readable in the extracted text, though this is a parsing artifact.

## Suggestions
1. **Specify the exact training data for the isotonic regression calibration** and show that the mapping generalizes to held-out targets. If the calibration uses the same targets as evaluation, retrain and re-report results.
2. **Add at least one non-ML clustering baseline** (e.g., k-means on Morgan fingerprints + centroid docking + same active-learning query strategy) to isolate the benefit of the probabilistic clustering and probability framework over simple grouping.
3. **Define the target recall rate explicitly** for each target or replace single-point cost comparisons with cost-vs.-recall curves across a range of thresholds (e.g., 20%–90%).
4. **Report per-target variance** or confirm determinism of the full pipeline.
5. **Remove aspirational claims about lead optimization** from the conclusion, as they are not supported by the experiments.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
