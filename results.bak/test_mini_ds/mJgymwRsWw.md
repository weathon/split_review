Now I have sufficient calibration. Let me synthesize the final review.

**Round-1 bracket (from 4 queries):** 4.0–6.5. The paper is well above the weak-anchor band (papers at 2-3.5) but clearly below the high-anchor band (7.5+). The most plausible range is between 4.5 and 6.0.

**Round-2 narrowing:** Compared to DockedAC (5.75, reject) and MF-LAL (5.20, reject), this paper has a stronger method contribution and more extensive evaluation scope (90 targets), but the single-baseline issue is a notable weakness that the better anchors (Efficient Biological Data Acquisition at 6.25, accept) do not share. The paper is solidly above the 3-4 band but meaningfully weaker than the accepted papers.

Let me write the final review.

Here is my consolidated review:

## Summary
This paper proposes Active Probabilistic Drug Discovery (APDD), a method that iteratively cycles through probabilistic molecule clustering (MPC), selective docking of cluster representatives via Vina-GPU+, and active learning-based wet experiment selection to reduce costs in early drug discovery. The method is evaluated on 90 targets from DUD-E and LIT-PCBA and on a simulated 1.4-million-molecule library, reporting average reductions of 80–85% in computational docking and 40–75% in wet experiments compared to full enumeration (VE).

## Strengths
- **Large-scale evaluation across diverse benchmarks.** Experiments cover 79 DUD-E targets and 11 LIT-PCBA targets with varied protein families and library sizes (from <4k to >300k molecules), providing evidence for robustness across settings (Section 5.2, Tables 1–2).
- **Validation on a simulated large library.** Section 5.4 demonstrates that APDD still recovers active molecules with ~20% of the docking and wet experiments compared to VE when the decoy set is expanded to 1.4 million molecules, suggesting scalability.
- **Well-motivated problem formulation.** The paper frames integrated intelligent computing and automated experiments as an active probabilistic learning problem (Section 3), providing a principled foundation that goes beyond simple docking-score ranking.
- **Novel query strategy tailored to drug discovery's recall-focused goal.** The expected recall improvement criterion (Section 4.3, Equations 3–5) is a non-trivial, domain-specific acquisition function that differs from generic uncertainty sampling, with separate cluster-based and molecule-based variants.
- **Probability calibration via isotonic regression.** Section 4.2 describes a sensible pipeline for mapping docking scores to binding probabilities using open labeled data, with a literature-motivated cap at 0.3 based on reported experimental hit rates.

## Weaknesses

### Fatal
None.

### Major
- **Insufficient baselines and no ablation of the method's components.** The paper compares APDD only against full Vina enumeration (VE). There is no ablation to isolate which component drives the cost savings. Specifically: (i) a clustering-only baseline (dock two representatives per cluster, pick top clusters for wet experiments, no active refinement) would determine whether the savings come from clustering alone; (ii) a random-selection-from-top-clusters baseline would test whether the active learning query strategy adds value beyond naive selection. The paper's justification for excluding ML methods ("cannot retrain or fine-tune due to limited wet experiments," Section 5.1) is reasonable for retraining-intensive approaches, but the absence of non-ML ablation baselines means the reader cannot attribute the claimed savings to the active probabilistic refinement loop versus the clustering step alone. This is the most significant gap in the evaluation.
- **No standard virtual screening metrics reported.** The paper reports only docking/wet experiment reductions, omitting standard metrics such as enrichment factor, AUC-ROC, or hit rate at 1%. This prevents direct comparison to the extensive VS literature and makes it difficult to assess whether the cost reductions come at the expense of screening quality beyond "same recall rate" (which itself is defined by an underspecified target recall threshold, Section 5.2).
- **The target recall rate is not concretely defined.** The stopping criterion is described as "when the recall rate of the top 100 molecules reaches the target recall rate" (Section 5.1), but the target recall rate itself is never specified (e.g., 30%, 50%, 80%). This directly affects the reported cost numbers and makes the results difficult to reproduce or compare.

### Minor
- **Probability model assumptions are stated but not validated.** The key assumption — that Tanimoto similarity of Morgan fingerprints equals the probability that two molecules bind the same target (Equation 1) — is asserted without empirical verification. The paper mentions validation "using statistics from Lit-PCBA/DUD-E/PubChem datasets" (Section 4.1) but never presents this validation. Similarly, the conditional independence assumptions in the multi-modal fusion formula (Equation 2) and the active learning update (Equations 4–5) are noted but not checked against data.
- **Per-target variation is acknowledged but not systematically analyzed.** The paper reports that APDD requires the same or more wet experiments than VE on three targets (MAPK1, KAT2A, PKM2) where docking scores are uniformly distributed (Section 5.2). However, there is no per-target breakdown or systematic analysis of when the method succeeds versus fails, leaving the aggregate averages (82%/75%) somewhat unreliable.
- **Wet experiment simulation is idealized.** Wet experiments are simulated by looking up ground-truth labels, assuming perfect, noise-free, cost-uniform experiments. This is standard computational practice, but the claimed "70% reduction in wet experimental costs" is a projection onto an idealized setting; the paper does not discuss how measurement noise or variable per-molecule costs would affect the results.
- **Large-dataset experiment uses a pooled-decoy setup that may overestimate difficulty separation.** Section 5.4 pools all decoys from all 79 targets as inactives for each target, making the inactive set artificially diverse and likely more separable from any given target's actives than a realistic large library would be.
- **The conclusion overstates the contribution.** The claim that APDD "eliminates the need for lead optimization" (Section 6) is not supported by the paper's results, which concern hit discovery only, not the multi-parameter optimization process required for lead development.

### Trivial
- The paper's table images are missing from the extracted text (parser issue), but the relevant results are discussed in the body text.

## Nice-to-Haves
- Adding a cluster-only baseline (dock representatives, no active refinement) would substantially strengthen the paper by isolating the contribution of the active learning loop.
- Reporting standard VS metrics (enrichment factor, AUC-ROC) alongside cost savings would improve comparability with the broader virtual screening literature.
- Providing a fixed-budget comparison (number of actives found for K=1,5,10,... wet experiments) rather than an underspecified "target recall rate" would make results more informative and reproducible.
- A systematic analysis of failure cases (targets where docking scores are flat) would give users practical guidance about when the method can be expected to work.

## Removed Points
These points were flagged by the reviewers but are removed or demoted for the following reasons:
- **Missing related works in the active learning literature:** Removed per protocol — I cannot verify literature omissions from external knowledge. The paper does cite relevant clustering and docking-related prior work.
- **Code release / reproducibility details:** Removed per protocol — hyperparameter details are provided (k=50 for FPC, 2 representatives per cluster); demanding a complete code release is outside the submission norms for this venue.
- **"Strawman" baseline characterization:** The harsh critic called VE a "strawman." While the baseline set is incomplete, VE (dock everything, pick top-scoring molecules) is the standard practice in many drug discovery pipelines and is a legitimate if not exhaustive comparison point. The criticism about insufficient baselines is retained under Major; calling it a strawman overstates the case.
- **Selection bias from dataset exclusion (79/102, 11/15 targets):** This is a speculative concern — the paper mentions exclusion due to preprocessing issues and docking errors, which is standard practice. No evidence suggests the excluded targets differ systematically.
- **The "noise ignored" criticism in the wet-experiment simulation:** Retained as Minor rather than Major because simulated wet-lab experiments are the universal standard in computational drug discovery papers; the paper does not misrepresent this as real experimentation.
- **Various formatting/style nitpicks and missing appendix content:** Removed per protocol — these reflect PDF parsing artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add ablation baselines.** At minimum: (A) cluster-only: dock two representatives per cluster, select molecules from top clusters by docking score for wet experiments, no active refinement; (B) APDD without probability updating (fixed probabilities throughout); (C) APDD as proposed. This is the single most impactful improvement.
2. **Specify the target recall rate** and ideally report results as a function of the number of wet experiments performed (e.g., actives found after 1, 5, 10, 20 experiments), replacing the ambiguous termination criterion.
3. **Validate the Tanimoto-as-probability assumption** by showing, even on a subset of the benchmark data, that molecules with high Tanimoto similarity to known actives are indeed more likely to be active than those with low similarity.
4. **Add standard VS evaluation metrics** (enrichment factor or AUC-ROC of the top-ranked molecules) to enable comparison with other screening methods.
5. **Provide per-target box plots of savings** and a brief discussion of when the method fails, rather than only aggregate averages.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| An87ZnPbkT (GNNAS-Dock) | 3.00 | R1 | Weaker — limited evaluation, lower contribution |
| CaNp8ALCRT (Bayesian MDP) | 3.00 | R1 | Weaker — different framing, less empirical depth |
| y2ch7iQSJu (Budget-constrained AL) | 2.00 | R1 | Weaker — smaller scope, less direct relevance |
| Ocg3XIymmp (Pharmacophore design) | 3.50 | R1 | Weaker — narrower contribution |
| gVkX9QMBO3 (Efficient Bio Data Acquisition) | 6.25 | R1/R2 | Stronger — more thorough evaluation, accepted |
| UfBIxpTK10 (Deep Confident Steps) | 6.00 | R1/R2 | Stronger — new benchmark + method, accepted |
| RyWypcIMiE (Reframing SBDD) | 6.50 | R1/R2 | Stronger — focused evaluation contribution, accepted |
| HBbbhAZuia (DockedAC) | 5.75 | R1/R2 | Comparable/slightly stronger — more baselines but only a dataset |
| bKAqK7Bh7n (MF-LAL) | 5.20 | R2 | Comparable — similar methods contribution with evaluation gaps |
| ZuU4mZILBB (Deep Learning Docking Survey) | 4.38 | R1 | Weaker — survey, no method contribution |
| kYg04pmX7i (Molecular AL with LLMs) | 4.40 | R2 | Weaker — less extensive evaluation |
| PHkUNcno9n (BALSA) | 4.67 | R2 | Weaker — benchmarking framework, not a method |

**Round-1 bracket:** 4.0–6.5

**Round-2 narrowing:** The paper sits between DockedAC (5.75, reject) and MF-LAL (5.20, reject). It has a stronger contribution than DockedAC (a full method, not just a dataset) and more extensive evaluation than MF-LAL (90 targets vs. 2 proteins). However, the single-baseline issue is more acute than what the accepted anchors (6.0–6.5) exhibit. The paper is meaningfully better than the 3–4 band papers.

**Final score:** 5.0 — The work has a well-motivated method and broad empirical scope, but the evaluation is incomplete in ways that prevent full support of the core claims (no ablation, single baseline, underspecified stopping criterion, no standard VS metrics). The contribution is real but the evidence is partial.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>