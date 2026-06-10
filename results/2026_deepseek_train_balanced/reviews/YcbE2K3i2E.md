## Summary

SaTran proposes a transformer architecture for large-scale Satellite Image Time Series (SITS) that attempts to improve efficiency by distinguishing between two types of redundancy — spatiotemporal redundancy (patches unchanged throughout the time series) and temporal redundancy (shorter-duration redundancy). Two modules are introduced: PatchTubeSelect (attention-based selection of non-redundant patch tubes) and TemporalRedundancyHandler (distributed VideoMAE with a reduced 75% masking ratio). The motivation — that existing video models fail on full-resolution SITS due to memory constraints — is well-articulated, and the conceptual decomposition of SITS redundancy is a reasonable starting point.

---

## Strengths

1. **Domain-specific two-tier redundancy characterization.** SaTran is the first SITS model to explicitly separate spatiotemporal redundancy (patches unchanged for the entire time series, e.g., water bodies) from temporal redundancy (shorter-duration redundancy). This decomposition is concretely described in Section 3.1 (lines 72–76) and Figures 1–2, and it contrasts with prior models (TSViT, SITSFormer) that do not identify redundancy types. The two-module design (PatchTubeSelect + TemporalRedundancyHandler) follows from this characterization.

2. **Principled adaptation of VideoMAE masking for SITS.** The paper identifies that VideoMAE's 95% masking ratio (designed for RGB video) is inappropriate for SITS due to shorter temporal redundancy spans, and proposes a reduced 75% ratio based on the physical characteristics of SITS data (Section 3.2, line 90). This is a reasoned, task-specific adaptation rather than a blind transfer.

3. **Identifies a genuine memory bottleneck.** The paper documents that all four competing models (VideoMAE, ViViT, SITSFormer, TSViT) produce OOM errors on an A100 80GB GPU when processing Landsat-8 at native resolution (lines 15, 138). This establishes a clear practical gap that motivates the SaTran design.

---

## Weaknesses

### Fatal

**The results section (Section 6.2) is completely empty.** Lines 146–150 contain only a section header and blank space before Section 7 (CONCLUSION). No tables, figures, RMSE/MAE values, accuracy/F1 scores, ablation studies, runtime benchmarks, or memory measurements are reported for any of the six downstream tasks or any baseline comparison. This is verifiable from the paper as written:

- The paper states "The comparative study for different masking ratios is given in the results section" (line 90) — it is not.
- The paper states "The impact of different masking ratios by VideoMAE is given in the results section" (line 111) — it is not.
- The abstract claims "SaTran outperforms competing models and exhibit state-of-the-art performance" — zero supporting numbers.
- The conclusion claims "SaTran reduces the memory requirements by approximately a factor of 2" and "an increase of 18% in processing time for 900GB... in comparison to 100GB" (lines 154–155) — no data supports either claim.

An empirical paper whose only evidence section is empty has not completed its core task. Every performance-related claim in the abstract and conclusion is unsubstantiated. This is not a gap that revision can patch; the experiments need to be conducted and reported. **This single issue invalidates the paper.**

### Major

1. **Unfair comparison by design on Landsat-8.** Baselines (VideoMAE, ViViT, SITSFormer, TSViT) are forced to process heavily degraded input — either resized to 1/4 resolution ("-R" variants) or segmented into 16 tiles ("-S" variants) — while SaTran processes full-resolution data (Section 6.1, lines 140–142). Any performance difference conflates architectural merit with information loss from downsampling or segmentation. A fair comparison would require a controlled experiment where SaTran is also evaluated on downsampled input to isolate the contribution of resolution from the contribution of architecture.

2. **Pre-training disparity.** ViViT is explicitly described as "not pretrained" while SaTran and VideoMAE are pretrained (line 138). This systematically disadvantages ViViT and makes the comparison uninformative about architectural quality.

### Minor

1. **PatchTubeSelect is underspecified.** The mechanism is described only in vague prose (line 88): "attention scores" are used to identify top-k tubes, but which attention mechanism is unclear; how k is determined is unspecified; what "traversal ratio" means is undefined; what fraction (1/x) of the SITS is processed and how x is chosen is not stated. No formal algorithm is provided. This makes the architecture irreproducible as described.

2. **TemporalRedundancyHandler adaptation is vague.** The paper states it "adapts VideoMAE" (line 90) but does not specify what is adapted beyond the masking ratio. The "distributed" processing of patch tubes is mentioned several times but never formally described or analyzed for correctness or communication overhead.

3. **Naming inconsistency.** The model is called "SaTran" throughout the paper but is referred to as "SatTran" in Section 4 (lines 109–113), suggesting inconsistent editing.

4. **No simple baselines.** No comparison with 3D CNNs, LSTM-based models, or a basic ViT with the same patch configuration. The only comparators are two video transformers and two SITS models. Including simple baselines would help isolate the contribution of the proposed modules from the benefit of using a transformer backbone.

### Trivial

- **Broken reference.** Line 130 references "B.4" at the end of a sentence, but no appendix content is present in the submission. (Likely a parser-stripping artifact, but worth noting.)

---

## Nice-to-Haves

- Running SaTran on the same downsampled inputs that baselines receive, to isolate the contribution of resolution from architecture.
- Ablation study comparing: (a) full SaTran, (b) without PatchTubeSelect, (c) without TemporalRedundancyHandler, (d) both removed — to validate the dual redundancy-handling claim.
- Analysis of which patches are selected by PatchTubeSelect (e.g., do they correspond to known land-cover classes).
- Statistical significance or variance reporting across counties/years.

---

## Removed Points

These points were flagged by reviewers but removed for the reasons stated:

- **"Code availability after acceptance makes reproducibility unverifiable"** — The paper states code will be given after acceptance, which is standard practice; removed per rule against reproducibility nitpicks about impractical artifacts.
- **"The paper never explains how SaTran bridges patch-level processing to county-level predictions"** — The Embedding Generator (line 92–93) and fine-tuning section (Section 5) partially address this; the remaining gap is a minor issue already covered above.
- **"Comparison with non-transformer spatiotemporal models"** — Already covered under "No simple baselines" in Minor weaknesses; redundant.
- **"No analysis of which patches are selected by PatchTubeSelect"** — Already covered in Nice-to-Haves; not a weakness but a missing analysis that would strengthen the paper.
- **"The paper oversimplifies pixel-level BERT models being infeasible for prediction tasks"** — The paper's claim is about pixel-level models requiring pixel-level ground truth, which is a reasonable distinction for prediction tasks where ground truth is at county level; the criticism is a misunderstanding.
- **Strength: "Empirical demonstration that existing models fail on large SITS"** — The OOM claim is stated but not empirically demonstrated with memory benchmarks or error logs in the empty results section. It is a stated observation, not a demonstrated result.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers identified the fatal missing results and several design-level concerns (comparison fairness, underspecification), but the harsh critic's detailed analysis of the architecture's vagueness and the comparison design issues is the most substantive secondary insight.

---

## Suggestions

- **Report the actual experimental results.** This is non-negotiable: populate Section 6.2 with all planned comparisons (RMSE/MAE for prediction tasks, accuracy/F1 for classification, for all six downstream tasks across both MODIS and Landsat-8, with all baselines).
- **Add a controlled-resolution experiment.** Run SaTran on the same downsampled/segmented inputs that baselines receive, to separate the benefit of architecture from the benefit of higher-resolution input.
- **Add simple baselines.** Include a basic ViT with identical patch configuration and a 3D CNN to establish a lower bound.
- **Formalize PatchTubeSelect.** Provide a pseudocode algorithm specifying how attention scores are computed, how k and x are determined, and the exact iteration logic.
- **Specify the "distributed" processing.** Clarify whether patch tubes are processed truly in parallel (multi-GPU), batched sequentially, or something else.

---

## Score and Decision

MY FINAL SCORE: <score>1.0</score>
MY FINAL DECISION: <decision>Reject</decision>