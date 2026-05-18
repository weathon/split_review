Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes a novel EM-style clustering algorithm that jointly optimizes Most Discriminative Stimuli (MDS) for functional cell types and reassigns neurons to clusters, using deep predictive "digital twin" models. The key innovation is coupling stimulus optimization with clustering in an alternating procedure, producing interpretable stimuli that can be used for rapid online cell-type identification without requiring the digital twin at test time. The algorithm is validated across mouse retina (against established Baden et al. 2016 types), marmoset retina, and macaque V4.

## Strengths

1. **Novel EM-style clustering that jointly optimizes discriminative stimuli and reassigns neurons.** The alternating M-step (optimizing softmax-based MDS) and E-step (reassigning neurons) in Algorithm 1 is a principled, domain-knowledge-free approach to functional clustering. This is a genuine methodological contribution.

2. **Broad empirical validation across species, brain areas, and recording techniques.** The method recovers the known functional hierarchy in mouse retina (OFF, ON-OFF, fast ON, slow ON, and color-opponent types), finds plausible ON/OFF splits in marmoset retina, and yields well-separated clusters in macaque V4 — demonstrating generalizability from retina to cortex and across calcium imaging and multi-electrode array recordings.

3. **Interpretable stimuli that reveal distinctive functional properties.** The MDS are directly visualizable. The paper provides a concrete example: the MDS for the "ON contrast suppressed" RGC type reveals center color opponency that was not exposed by prior fingerprinting stimuli but is known to characterize this type (Discussion). This provides data-driven understanding of what distinguishes each cluster.

4. **Demonstrated utility for rapid cell-type identification.** The simulated experiment shows that 9 MDS repetitions (1min45s) outperform a chirp-based classifier (73.5% accuracy) while saving 20% experimental time. Once MDS are established, no digital twin is needed for new recordings, enabling fast online typing.

5. **Robustness across initializations.** Across 11 comparison runs with varying initial cluster counts (5 vs. 30) and random seeds, cluster assignments show high similarity (median ARI: 0.67 for mouse retina, 0.96 for marmoset retina), indicating the algorithm converges to consistent solutions.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The cluster-splitting criterion is underspecified.** Algorithm 1 states that candidate sub-clusters are kept if "they improve mean objective ⟨J_c⟩_c," but "improve" is not defined: is it any positive change? A relative improvement threshold? A statistically meaningful change? Since the objective depends on the softmax temperature and other clusters' MDS, different interpretations could lead to different numbers of clusters. The authors should precisely define the criterion and quantify sensitivity (e.g., by varying the threshold and measuring ARI against reference types). The existing robustness analysis partially addresses this concern (the algorithm produces stable results across runs), but the specification gap remains.

2. **No single-number summary of the MDS clusters' discriminative power.** The paper shows confusion matrices (Fig. 2D,E) but does not report overall accuracy, per-cluster precision/recall, or a summary metric for how well the MDS separate clusters on held-out test neurons. This makes it harder to compare against potential future approaches and to assess how much of the separation is driven by a few strong clusters vs. all clusters.

3. **Computational cost is not reported.** The paper never states the GPU-hours required for the full MDS clustering, the number of EM iterations until convergence, or the average number of stimulus optimization steps per M-step. This information is essential for potential users to judge feasibility for their own datasets.

4. **Number of discarded small clusters not reported.** The paper discards clusters with fewer than 10 cells (mouse retina) or 6 cells (V4) but does not state how many clusters were discarded at each step or whether these might correspond to rare but genuine cell types. The robustness analysis should also report the variability in the number of clusters found across runs, not just ARI.

5. **Missing systematic comparison to readout-weight-based clustering.** The paper discusses Ustyuzhaninov et al. (2022) — who clustered digital twin readout weights in mouse V1 — in Related Work, but does not quantitatively compare MDS clustering against this or other representation-based clustering approaches on the same data. Such a comparison (e.g., running k-means on readout weights and comparing ARI against Baden types) would directly test whether the joint MDS-cluster optimization adds value over simply clustering the model's internal representations.

### Trivial
- The paper describes V4 MDS interpretability as limited ("difficult to describe in words"), which is an honest acknowledgment rather than a flaw.

## Nice-to-Haves

- **Synthetic control experiment.** A valuable extension would be to construct a semi-synthetic dataset where the true functional types are known (e.g., by defining types based on known tuning properties) and the digital twin is sufficiently expressive. This would directly test the algorithm's ability to recover finer structure when the model is not a limiting factor, separating the question "does the algorithm work given a good model?" from "is the model good enough for this dataset?" The reduced classifier analysis (Fig. 2E) partially addresses this by showing that even a supervised classifier without direction selectivity confuses the same types, but a synthetic experiment would be a cleaner control.

- **Ablation of the cluster-splitting procedure.** Showing how the mean objective changes as clusters are split, and how often the same final number of clusters emerges across initialization runs, would strengthen confidence in this part of the algorithm.

## Removed Points

These points from the reviewers are flagged for removal — treat with caution:

- **"The 20% time-savings claim is oversold" / "oddly constructed comparison."** The critic claims the chirp classifier is "first forced to predict 17 types, then its predictions are merged into 7 superclusters" as a post-hoc step, but the paper clearly states (lines 180–181) that the baseline classifier was *retrained* on the merged 7-class task. The critic also acknowledges that the baseline (chirp only) is narrower than the full Baden protocol, which would make the actual time savings *larger* — this works in the paper's favor, not against it. The comparison is appropriate for what it claims.

- **"The validation claim is weaker than advertised" (under-clustering as a core weakness).** The paper is transparent about the 7 vs. 17 cluster discrepancy (lines 143–144) and provides the reduced classifier analysis (Fig. 2E) as direct empirical evidence that the under-clustering is due to missing direction selectivity — not a limitation of the algorithm. The critic's concern is addressed by the paper's own analysis.

- **"Strawman about ARI 0.67 being 'only moderate'."** The paper describes ARI 0.67 as "high" (line 167), which is reasonable for clustering with random initializations on a 2,448-neuron, 17-type dataset. The marmoset ARI of 0.96 further demonstrates strong stability.

- **Criticism that the paper should have tested direction selectivity as a "synthetic experiment."** The paper already conducts the reduced classifier comparison which serves this purpose empirically. The synthetic experiment is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the method or results that the authors themselves have not already identified.

## Suggestions

1. **Define the cluster-splitting criterion precisely.** Specify what constitutes an "improvement" in mean objective (e.g., any positive change, a relative improvement > ε, or a threshold on the change in ⟨J_c⟩_c). Report sensitivity of the final cluster count to this choice.
2. **Add per-cluster discriminative power metrics** (accuracy, precision, recall) for held-out test neurons.
3. **Report computational cost** (GPU-hours, EM iterations, M-step optimization steps).
4. **Report how many clusters were discarded** at each stage and evaluate whether they correspond to rare genuine types.
5. **Add a quantitative comparison to readout-weight-based clustering** (e.g., k-means on digital twin readout weights) on the same datasets, comparing ARI against the Baden reference types.

## Score and Decision

The paper presents a genuinely novel algorithm that demonstrably works across multiple species and brain areas. The core contribution is sound and the empirical validation is substantial. The weaknesses are real but addressable in revision and do not threaten the paper's main claims. The paper merits acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>