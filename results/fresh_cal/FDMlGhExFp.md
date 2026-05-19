Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces TabDPT, a tabular foundation model that combines a transformer encoder (row-as-token architecture), self-supervised learning via random column prediction, and end-to-end retrieval-based training to perform in-context learning on real-world tabular data without any per-dataset fine-tuning or hyperparameter optimization. The paper presents three main contributions: (1) competitive performance on CC18 and CTR23 benchmarks without task-specific tuning, (2) the first scaling-law analysis for tabular foundation models showing power-law improvements with model size and data volume (α=0.42, β=0.39), and (3) a practical inference-time speed advantage of 1–4 orders of magnitude over tuned tree-based and neural baselines.

## Strengths

- **Competitive performance without per-dataset tuning is convincingly demonstrated.** Table 1 shows TabDPT achieves the highest or tied-highest score on three of four metrics (AUC 0.929, Correlation 0.833, R² 0.729) across CC18 and CTR23 benchmarks, *without any task-specific fine-tuning or HPO*, while tuned baselines (XGBoost, CatBoost, TabR) undergo extensive per-dataset hyperparameter optimization. Even accounting for overlapping CIs on regression metrics, the fact that a single fixed model matches or exceeds tuned methods on 72+35 datasets is a genuine achievement.

- **First scaling-law analysis for tabular foundation models.** Section 5.2 fits a joint power-law model ℓ̂(P,D) = A/P^α + B/D^β + E to TabDPT trained across model sizes from 33K to 78M parameters and data from 52M to 2B cells. The exponents α=0.42 and β=0.39 are close to each other and within the expected range, mirroring findings from language modeling. Figure 1 empirically shows that real data consistently outperforms synthetic data (PFN++) at larger model sizes — a direct, quantitative demonstration that tabular ICL benefits from scaling.

- **Training-time retrieval is shown to improve performance over inference-only retrieval.** The ablation study (Figure 3b) demonstrates that replacing end-to-end retrieval with subsampling *during training* (while keeping retrieval at inference) causes a clear drop in both AUC and R². This is a differentiator from prior work (e.g., TabPFN + kNN retrieval only at test time) and supports the claim that aligning training and inference distributions matters.

- **Inference speed advantage is large and well-characterized.** Figure 3a shows TabDPT is 1–4 orders of magnitude faster than tuned baselines at test time, with consistent per-row costs. This is a practical advantage that does not depend on being marginally ahead on accuracy.

- **Base-C_max encoding for many-class classification** (Section 3.4) is a practical innovation that allows handling hundreds of classes with ⌈log_{C_max}(C)⌉ forward passes instead of C passes for one-vs-all.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation protocol asymmetry weakens the headline SOTA claim.** TabDPT is evaluated on "at least two different splits" (line 313) with bootstrapped CIs, while key baselines on CC18 (XGBoost, CatBoost, LightGBM, MLP) use numbers from the TabZilla repository, which follows a stronger 5-fold cross-validation protocol with per-fold HPO. The paper does not specify whether TabDPT was evaluated on the same splits that generated the TabZilla numbers, or whether the "at least two splits" refers to two folds, two random splits, or two repeated CV runs. Combined with the fact that TabDPT's margins are small — AUC 0.929 vs. TabR 0.925 (CIs barely touch), Accuracy trails TabR by 0.001, and all regression CIs overlap with TabR and MLP-PLR — the "state-of-the-art" claim is not as robust as it could be. A proper 5-fold evaluation on the same folds as baselines would either confirm or refute the SOTA claim with greater confidence.

- **Contamination check is described procedurally but lacks empirical evidence.** Section 4.3 describes a reasonable pipeline using metadata, hashes, feature statistics, and k-d trees to detect training/evaluation overlap. However, no results are reported: no counts of how many training–evaluation dataset pairs were flagged, no list of removed datasets, no examples of detected overlaps. Since the training data is drawn from the same OpenML ecosystem as CC18 and CTR23 — including datasets from the grinsztajn2022why, TabZilla, and AMLB benchmarks that CC18/CTR23 were built from — the possibility of contamination is non-trivial. Without any empirical validation (e.g., flagged pairs, dataset IDs), a reader cannot assess whether the reported results reflect genuine generalization or partial memorization.

### Minor

- **Scaling law uses a combined metric (average of cross-entropy and 1-ρ) that mixes losses with different units and scales.** The paper acknowledges that "neither classification nor regression alone is explained quite as well" (line 362), which suggests the combined metric may be masking mis-specification in the individual scaling laws. Reporting scaling laws separately for classification and regression would strengthen the analysis.

- **Base-C_max encoding for many classes is not ablated.** The paper introduces this technique (Section 3.4) but does not compare it to one-vs-all in terms of accuracy trade-off. If base-C_max encoding degrades accuracy compared to one-vs-all, that is important to quantify. If it does not, that would be a useful positive finding to report.

- **The abstract and introduction claim "state-of-the-art performance" without caveating the small margins and overlapping CIs.** Table 1 shows TabDPT is tied or best on 3/4 metrics, but the margins are small (0.001–0.004 on metrics where baselines' CIs overlap or nearly overlap with TabDPT's). Qualifying the SOTA claim with the uncertainty would improve accuracy.

### Trivial
None.

## Nice-to-Haves

- Report scaling laws separately for classification and regression alongside the combined metric.
- Ablate the base-C_max encoding vs. one-vs-all to quantify any accuracy degradation.
- Validate the contamination check by reporting counts of flagged/removed training–evaluation pairs.
- Adding a comparison to PFN++ without retrieval in the main table (currently only shown in scaling plots) would help isolate the effect of real data from the effect of retrieval.

## Removed Points

These points were identified by reviewers but removed or demoted from the final weakness list for the following reasons:

1. **Hyperparameters not stated / reproducibility concern** — The critic noted hyperparameters (learning rate, batch size, etc.) should be in main text or appendix, but acknowledged the appendix was stripped by the parser. The original submission contains these details. *Removed per rule: "remove weaknesses about missing appendix content."*

2. **Concern about library release status** — The critic noted "libraries will be released at a later date" as a reproducibility problem. *Removed per rule: "remove any criticism that questions the existence, release status, or availability of any model, tool, benchmark, dataset, or reference cited in the paper."*

3. **Wrapfigure formatting issues** — The critic mentioned "wrapfigures push text around." *Removed per rule: "remove pure formatting/style nitpicks" and "remove typos/formatting criticisms" (parser artifacts).*

4. **Elo sensitivity to match-order permutation** — The critic claimed this was not addressed. The paper explicitly states it "estimate[s] uncertainty by bootstrapping over match order permutations" (line 343) and describes how missing comparisons are handled via omission (lines 345–349). *Removed because the paper already addresses this concern.*

5. **"Section-by-section notes" that are purely observational without actionable criticism** — Several one-sentence observations (e.g., "the discussion of SSL is adequate," "architecture description is clear") do not constitute weaknesses. These are noted but do not affect the assessment.

6. **Generic "missing baseline" point about PFN++ without retrieval in main table** — The scaling plot (Figure 1) already shows PFN++ without retrieval; the critic's concern is about its absence from Table 1. This is a minor suggestion, moved to Nice-to-Haves.

7. **"CTR23 baselines described vaguely"** — The paper states HPO uses "search space similar to the TabZilla protocol" and the code from Gorishniy et al. This is standard practice for referencing established protocols. *Demoted from weakness to minor and then removed as it is adequately addressed for a conference publication.*

## Novel Insights

The two reviewer perspectives pull in opposite directions: the Harsh Critic focuses on evaluation rigor (split protocol, contamination evidence, overlapping CIs), while the Strength Finder highlights the genuinely novel contributions (scaling laws, training-time retrieval, fast inference). The most interesting synthesis is that the scaling-law analysis (Section 5.2) is both the paper's strongest contribution and its most self-contained one — it does not depend on the SOTA claim at all. Even if TabDPT were merely competitive rather than strictly state-of-the-art, the finding that tabular ICL models exhibit predictable power-law scaling with model size and real-data volume (and that real data consistently beats synthetic data at larger scales) is a valuable empirical result for the field. Conversely, the evaluation weaknesses primarily affect the headline SOTA claim, not the core methodological contributions. This suggests the paper would be strengthened by decoupling these two narratives more clearly: acknowledging that the competitive results are promising but preliminary (given protocol limitations), while the scaling analysis and training-time retrieval findings are on firmer ground.

## Suggestions

1. **Run TabDPT on the standard 5-fold splits** used by TabZilla for CC18, or at minimum report results on the same number of folds/seeds as the baselines. This single change would resolve the evaluation asymmetry and substantially increase confidence in the comparative results.

2. **Provide contamination check results** — at minimum, report how many training–evaluation dataset pairs were flagged and removed, or provide a table of retained training dataset IDs so readers can independently verify.

3. **Report individual scaling laws** for classification and regression separately alongside the combined metric. This would strengthen the scaling analysis and make it more interpretable.

4. **Caveat the SOTA claim** in the abstract and introduction to reflect that margins are small and CIs overlap on some metrics — e.g., "competitive with or exceeding tuned baselines" rather than "state-of-the-art."

5. **Ablate the base-C_max encoding** vs. one-vs-all for multi-class datasets. This is a quick experiment that would either validate the practical utility of the method or identify a performance trade-off.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>