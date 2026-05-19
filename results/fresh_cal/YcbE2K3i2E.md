Confirmed: Section 6.2 "RESULTS AND ANALYSIS" is entirely empty — just a heading followed by blank lines and then the conclusion. Zero results, zero tables, zero figures. The Conclusion then makes sweeping quantitative claims without any supporting data.

---

## Summary

This paper proposes SaTran, a transformer for satellite image time series (SITS) that aims to exploit spatiotemporal redundancies via two modules: PatchTubeSelect (attention-based selection of non-redundant patch tubes) and TemporalRedundancyHandler (distributed VideoMAE-style tube masking). The intended contribution is a computationally efficient architecture capable of processing high-resolution Landsat-8 SITS at original resolution where existing video models fail. However, the paper presents **no experimental results whatsoever** — not a single table, figure, or quantitative comparison — rendering it impossible to evaluate its claims.

## Strengths

None. The paper's core claims (state-of-the-art performance, ~2× memory reduction, sublinear scaling, successful processing of full-resolution Landsat-8 SITS) are all asserted without any supporting evidence. The problem motivation (spatiotemporal redundancy in SITS) is clearly articulated, but this is a generic observation about the domain, not a strength of the paper as a submission.

## Weaknesses

### Fatal

- **No experimental results are presented.** Section 6.2 ("RESULTS AND ANALYSIS") is an empty section heading followed by nothing — no tables, figures, numerical results, or analysis of any kind. The Conclusion (Section 7) then makes specific quantitative claims (e.g., "memory requirements by approximately a factor of 2," "increase of 18% in processing time for 900GB of Landsat-8 data," "outperforms all the competitive models for all downstream tasks") without a single supporting data point anywhere in the paper. Six downstream tasks are described, four baselines are listed, evaluation metrics are defined — but no results are reported. A paper that claims empirical contributions but presents no evidence for them cannot be accepted. This is not a missing appendix or supplementary; the main paper's core results section is entirely blank.

### Major

- **Method description is too vague for reproducibility or rigorous assessment.** Several key architectural details are described only at a high level: the attention mechanism used by the Tube Selection Module is not specified; the iterative selection process (how ROI-S determines "unprocessed neighboring tubes" and the stopping criterion for the traversal ratio $1/x$) is described in prose with no algorithm or pseudo-code; the embedding generator is "two linear layers" with no dimensions; the reconstruction decoder is "trans-convolutional layers" with no kernel sizes, number of layers, or upsampling strategy; the choice of 75% masking ratio (versus VideoMAE's 95%) is justified qualitatively but not empirically. Since no results exist to validate the design choices, the reader cannot assess whether the architecture works as claimed.

### Minor

- **No ablation or sensitivity analysis.** The paper introduces several hyperparameters (patch tube size, tiny tubelet size, traversal ratio $1/x$, top-$k$ selection count, masking ratio) that are critical to the method's efficiency/accuracy trade-off, yet none are studied empirically. Multiple references to "the results section" for these studies appear in the text (lines 90, 111), but that section is empty.

- **Downstream task evaluation protocol is underspecified.** The paper lists six downstream tasks but does not explain how SaTran's SITS-level embeddings are adapted for each task (e.g., output head architecture, how county-level ground truth is mapped to predictions). The statement "All predictions are done at timestamp $t+1$" (line 129) is ambiguous with respect to how spatially aggregated predictions are produced.

### Trivial

None.

## Nice-to-Haves

None applicable — the fatal flaw precedes any nice-to-have improvements.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength: "Processing of full-resolution Landsat-8 SITS where all baselines fail"** — The paper states that baselines give OOM errors on Landsat-8, but presents no evidence that SaTran successfully processes this data while achieving acceptable performance. This claim is unsubstantiated and conflicts with the verified fatal weakness (no results).

- **Strength: "Novel dual redundancy-handling architecture that reduces memory by ~2× and scales sublinearly"** — The ~2× reduction and sublinear scaling are asserted in the conclusion but not backed by any experiments in the paper.

- **Strength: "State-of-the-art results across six diverse downstream tasks"** — Asserted in the conclusion but completely unsupported; no results appear anywhere in the paper.

- **Strength: "Pre-training tailored to SITS dynamics"** / **"Adaptability to different satellite systems"** — These describe architectural intentions and parameter values, but without experimental validation they are unsubstantiated claims, not strengths.

- **Weakness (Harsh Critic): "Comparison baselines are adapted in ways that undermine fairness claims"** — The paper explicitly describes how baselines are adapted (resize to 1/4 resolution; segment into 16 parts). The critic's concern about information loss asymmetry is speculative since no results exist to evaluate it. Removed as speculative.

- **Weakness (Harsh Critic): "Missing parts and places to improve" subsections about failure cases, hyperparameter sensitivity, limitations** — These are generic expectations rather than specific identified problems with the paper's content. Removed as aspirational rather than grounded.

- **Weakness (Harsh Critic): "Pre-training data distribution, class balance, sample diversity not provided"** — Removed as a minor detail that would be relevant only if the paper actually presented results validating the pre-training.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight that the paper itself does not already state, because there are no experimental findings to analyze.

## Suggestions

The paper cannot be repaired within a rebuttal. To be resubmitted, the authors must:

1. **Add a complete experimental section** with full quantitative results for all six downstream tasks, comparing SaTran against all baselines (including the two adapted forms for each baseline).
2. **Include ablation studies** isolating PatchTubeSelect and TemporalRedundancyHandler, with analysis of varying $k$, masking ratio, and traversal ratio.
3. **Provide runtime and memory comparisons** against baselines to substantiate the claimed efficiency.
4. **Add a precise algorithmic description** (pseudo-code) of the patch tube selection process.
5. **Specify output head architectures** for each downstream task.

## Score and Decision

This paper cannot be accepted in its current form. Its core claim is an empirically validated architecture for SITS, yet it contains zero experimental evidence. The missing results are verifiable from the paper as written (Section 6.2 is entirely empty), and this fatal flaw overrides any other consideration. The problem motivation and architecture idea are reasonable, but a submission that makes performance claims without presenting data to support them is not publishable.

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>