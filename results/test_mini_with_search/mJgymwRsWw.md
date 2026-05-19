Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

The paper proposes APDD, a pipeline that combines probabilistic molecule clustering (MPC with Tanimoto similarity on Morgan fingerprints), initial docking on cluster representatives, and active learning with iterative wet-lab feedback to reduce computational and experimental costs in early drug discovery. The method is evaluated on 90 targets from DUD-E and LIT-PCBA, reporting average reductions of 82%/75% (docking/wet experiments) on DUD-E and 85%/40% on LIT-PCBA while maintaining comparable recall to a full-docking baseline.

## Strengths

1. **Formulation of drug discovery as an active probabilistic learning problem (Section 3)** — The paper explicitly frames the end-to-end process as iteratively updating binding probabilities under the assumption that actives are few and cluster-distributed. This conceptual framing is a genuine departure from deterministic affinity-score ranking.

2. **Probabilistic clustering pipeline using substructure similarity (Section 4.1)** — The use of the MPC algorithm with Tanimoto similarity on Morgan fingerprints, combined with Faiss-based k-NN, provides a principled way to cluster molecules without requiring known active molecules, addressing a practical limitation of prior clustering approaches.

3. **Active probabilistic refinement with an expected-recall query strategy (Section 4.3)** — Two query variants (cluster-based and molecule-based) that quantify expected recall improvement, plus a context probability refinement step that updates cluster posteriors after wet-lab results, are well-motivated components.

4. **Evaluation across 90 targets on two established benchmarks** — The scale of evaluation (79 DUD-E + 11 LIT-PCBA targets) is substantial. The reported cost savings (82%/75% for DUD-E, 85%/40% for LIT-PCBA) are practically interesting if supported.

5. **Performance on large virtual libraries (Section 5.4)** — The demonstration that APDD recovers target actives with ~20% of docking and wet experiments on 1.4M-molecule augmented datasets provides preliminary evidence of scalability.

## Weaknesses

### Major

1. **The active learning component's contribution is not isolated from the clustering+docking stage.** The paper compares APDD only against VE (full docking → wet test top-scorers). This design cannot separate savings from (a) clustering + representative docking from (b) the active learning refinement loop. A natural ablation would compare APDD against a baseline that docks cluster representatives and then wet-tests top-ranked clusters without iterative active refinement. Without this, the paper's central novelty claim — the active probabilistic refinement — is unsubstantiated. The paper also dismisses ML-based active screening methods with the statement that "machine learning models cannot be retrained or fine-tuned due to the limited number of wet experiments," which overlooks uncertainty-based acquisition strategies that require no retraining.

2. **The core assumption that Tanimoto similarity of Morgan fingerprints approximates co-binding probability is stated but never validated.** Section 4.1 claims this is "further validated using statistics from Lit-PCBA/DUD-E/PubChem datasets," but no validation results appear anywhere in the paper. This is a foundational step in the pipeline — the probabilistic clustering, the representative selection criterion, and the active learning acquisition function all depend on it. Without empirical evidence that this similarity measure correlates with shared target binding, the method's theoretical grounding is incomplete.

3. **The target recall rate used as the termination condition is not specified.** Both APDD and VE are run "until a predetermined recall number is achieved" / "when the recall rate of the top 100 molecules reaches the target recall rate." Without knowing what recall target is used (50%? 80%? 100%?), the reader cannot evaluate whether the cost comparison is fair — a lower target trivially favors the method, while a higher target may favor the baseline differently across targets.

### Minor

4. **Results are reported as point estimates without any measure of variance.** Even if the pipeline is entirely deterministic per protein, multiple choices (e.g., k in k-NN, number of representatives per cluster) introduce degrees of freedom. Per-target results (rather than only averages), or at minimum bootstrapped confidence intervals, would help assess the reliability of the claimed savings.

5. **The assumption that actives are tightly clustered is violated for LIT-PCBA, but this is not systematically analyzed.** Table 3 shows that active cluster purity for LIT-PCBA targets is very low (e.g., 0.092 for ADRB2, 0.011 for ALDH1), and the reported savings are indeed lower on LIT-PCBA (40% wet experiment reduction vs. 75% on DUD-E). The paper notes this correlation in passing but does not analyze it: does APDD's performance degrade proportionally when clustering assumptions fail? Which targets are most affected?

6. **The conclusion claims the paradigm "aims to eliminate the need for lead optimization," which is unsupported.** The proposed method performs hit identification only; lead optimization is a distinct downstream process not addressed by any experiment in the paper.

7. **The paper dismisses ML-based screening baselines with an incomplete justification.** "Machine learning models cannot be retrained or fine-tuned due to the limited number of wet experiments" overlooks pool-based active learning strategies (uncertainty sampling, query-by-committee, Bayesian optimization of docking scores) that operate without retraining by acquiring labels for the most informative unlabeled points.

### Trivial

8. **Hyperparameters (k=50 nearest neighbors, 2 representatives per cluster) are fixed without any sensitivity analysis.** These choices likely affect both cost savings and recall.

## Nice-to-Haves

- A per-target scatter plot of (docking cost reduction, wet experiment reduction) for all 90 targets would let readers assess the spread and understand when the method helps vs. hurts.
- A brief study on how the number of representatives per cluster and k in k-NN affect performance would strengthen the empirical characterization.

## Removed Points

The following points from the inputs were removed with justification:

- **"Only one baseline (VE) is compared" framed as a fatal omission** → Kept but merged into Major weakness #1 (the real problem is the missing ablation of the active learning loop, not the number of baselines per se).
- **"Tables are unverifiable due to garbled OCR"** → Removed as a parser issue; the original submission has proper tables.
- **"The fusion of multiple docking methods is described but never used"** → Removed; the paper presents this as an extensibility option, not a claimed result.
- **"Method is not tested on unseen proteins"** → Removed; evaluating across 90 different targets on DUD-E/LIT-PCBA constitutes cross-target evaluation.
- **"The derivation of query strategies is heuristic"** → Removed; the paper explicitly acknowledges approximations and provides a reasonable derivation.
- **"Augmentation in Section 5.4 may artificially inflate separability"** → Removed; this is speculative and the experiment is explicitly positioned as a scalability test.
- **"Repeated citations of Wei et al. padding the introduction"** → Removed; standard practice for describing an industrial platform.
- **Strength about isotonic regression mapping** → Removed; this is a standard calibration technique and does not rise to the level of a notable strength.
- **"Multiple equations referenced but not numbered"** → Removed; this is likely a parser artifact from equation numbering in the original PDF.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's strengths (practical framing, scale of evaluation) and surface the key gaps (unvalidated core assumption, missing active learning ablation, unspecified termination criteria) that a reader would independently identify.

## Suggestions

1. **Ablate the active learning loop.** Add a baseline that docks cluster representatives and then wet-tests top clusters by descending dock score (no iterative refinement). Compare this to full APDD to isolate the active learning contribution.
2. **Validate the Tanimoto-similarity assumption.** Show, for a sample of targets, that the distribution of Tanimoto similarities between active-active pairs is significantly higher than between active-decoy pairs. If this does not hold, provide justification for why MPC clustering is still effective.
3. **Specify the target recall rate** used for termination. Report per-target recall achieved by both APDD and VE, so readers can assess the fairness of the comparison.
4. **Report per-target results.** Supplement the averages with a scatter plot or boxplot of docking/wet-lab reductions across all 90 targets, annotated with cases where APDD underperforms VE.
5. **Include uncertainty estimates.** Report confidence intervals or per-target variance for the key metrics.

## Score and Decision

**Round 1 bracket:** 3.5–5.0 (based on initial calibration against DockedAC (3.00), APEX (3.50), CLUSMOL (3.33), ALPS (4.00), FragBench (3.33), Drug-few (3.00), Bento (5.00), and SubDyve (5.50)).

**Narrowing anchors (Round 2):**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SubDyve | 9vo3J4LwoT | 5.50 | 1 | Stronger evaluation with multiple baselines, ablations, per-target analysis. APDD is clearly weaker. |
| Bento | kIxAQxUZHq | 5.00 | 2 | Comprehensive benchmark with different contribution type. Not directly comparable. |
| RL4SBDD | dWEQpTkr1v | 4.50 | 2 | Slightly stronger evaluation, rejected due to other concerns. APDD comparable. |
| ALPS | 87KfYrIPff | 4.00 | 2 | Active learning benchmark paper. Similar quality level, different domain. |
| From Regression to Dose-Response | bKTAIXjiEf | 4.00 | 1 | Mixed reviews (4,6,2,4). Similar quality concerns. |
| FragBench | MMLAvR1juf | 3.33 | 2 | Similar validation issues, Accept Poster at lower venue tier. |
| CLUSMOL | v49kXDCf0n | 3.33 | 2 | Similar assumption-validation issues. APDD slightly stronger in practical relevance. |
| APEX | X5p6k5GSbI | 3.50 | 1 | Similar single-baseline limitation. APDD evaluates on more targets. |
| DockedAC | fgooGoezZJ | 3.00 | 1 | Dataset paper, different contribution type. APDD has stronger method contribution. |
| Drug-few | tBEz4EsVms | 3.00 | 1 | Few-shot screening, similar missing-baseline issue. APDD comparable or slightly stronger. |

**Final position:** APDD is clearly weaker than SubDyve (5.50) but comparable to or slightly stronger than papers in the 3.0–4.0 range (APEX, CLUSMOL, Drug-few). It sits below well-executed benchmark or method papers (Bento 5.00) but above papers with fundamental validation gaps (Drug-few 3.00, DockedAC 3.00). The paper has a genuine method contribution and evaluates on many targets, but the evaluation gaps are significant enough to leave the core claim of active-learning-driven savings unsubstantiated. Final score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>