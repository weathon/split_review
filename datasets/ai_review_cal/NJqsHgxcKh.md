- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

MetaTST proposes to incorporate multi-level metadata (dataset, task, sample) into time series forecasting by converting unstructured metadata into natural language via pre-designed templates, encoding these texts with a frozen LLM, and injecting the resulting metadata tokens alongside endogenous and exogenous series tokens into a Transformer encoder. The paper evaluates on short-term and long-term forecasting benchmarks under both single-dataset individual training and multi-dataset joint training, reporting state-of-the-art average performance.

## Strengths

1. **Novel and well-motivated integration of multi-level metadata via a frozen LLM encoder.** MetaTST is the first to formalize dataset-, task-, and sample-level metadata through language templates and encode them with a *frozen* LLM (Section 3.2), contrasting with prior LLM4TS works that fine-tune the LLM as the prediction backbone. The efficiency analysis (Figure 6b in the paper) shows that this design achieves better performance with lower computational cost than fine-tuning-based LLM baselines. The three-level decomposition of metadata (dataset properties, task specifications, sample statistics) is a useful conceptual contribution.

2. **Consistent state-of-the-art across individual and joint training settings with strong joint training results.** MetaTST achieves the best average MSE/MAE on short-term (Table 1: 0.300/0.264) and long-term forecasting (Table 2: 0.125/0.231) under individual training. More notably, in multi-dataset joint training, MetaTST is the *only* method with positive promotion (green arrows) on *all* sub-datasets in both short-term (Table 3, Promotion: 10.8% MSE reduction) and long-term (Table 4, Promotion: 3.54% MSE) settings, whereas PatchTST, iTransformer, and TimeXer all show degradations on some datasets. This consistent positive transfer in diverse-scenario training is the paper's strongest empirical evidence.

3. **Ablation studies validate the contribution of each input modality.** Figure 4 systematically removes endogenous, exogenous, and metadata components, showing performance drops when metadata is removed, particularly on datasets with few exogenous series (ETTm1, EPF). The finding that metadata matters more when exogenous information is limited provides practical insight into when the approach is most beneficial.

4. **t-SNE visualization confirms metadata representations are context-discriminative.** Figure 5b shows metadata tokens from different datasets form distinct clusters, with similar datasets (ETTh1 vs. ETTh2) clustering more closely than dissimilar ones (Weather vs. Traffic), providing direct evidence that the frozen LLM encoder extracts domain-relevant semantic features.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline that feeds the same metadata as simple numeric features.** The paper's central claim is that *LLM-encoded textual metadata* provides valuable context that improves forecasting. Yet every baseline receives only the raw numerical series — no comparison method incorporates metadata in any simpler featurized form (e.g., appending sample-level mean and std as additional channels, adding a dataset-ID one-hot, or encoding task context as numeric inputs). Without this comparison, the reader cannot determine whether the improvement comes from *having additional information at all* (which would be a trivial finding) or from the *specific LLM-based textual encoding* (which is the claimed contribution). The paper needs a control where the same metadata fields are provided as numeric embeddings to isolate whether the LLM encoding is the source of the gains.

### Minor

1. **No uncertainty quantification or statistical significance for small-margin improvements.** Many of the reported improvements are very small — e.g., average MSE on long-term individual training: MetaTST 0.125 vs. TimeXer 0.132 (Table 2); on ETTh1: 0.069 vs. 0.073. On NP in short-term individual training, TimeXer actually achieves lower MSE (0.238 vs. 0.239). With no error bars, repeated-seed statistics, or significance tests, it is unclear whether these margins are reliable or within the noise of hyperparameter search or random initialization. This is especially important for the individual training setting where margins are tight. (The joint training results are stronger and less affected by this concern given the consistent pattern.)

2. **The contribution of the LLM encoder is not fully isolated from the effect of adding extra tokens.** MetaTST adds three metadata tokens. The ablation (Figure 4) removes metadata entirely but does not test replacing metadata tokens with three learnable, randomly initialized tokens carrying no textual information. Without this control, some of the observed gain could be attributed to increased model capacity from extra tokens rather than the semantic content of the LLM-encoded metadata. A control replacing metadata with (a) three learnable no-information tokens or (b) tokens from random/nonsense text would strengthen the attribution.

3. **Which LLM was used for the main results is not specified.** The method section mentions Llama-3-8B as an example (line 105), and Section 4.4 tests BERT, T5, Llama, and others (Figure 4a). But the main experimental tables (Tables 1–4) do not state which LLM was used as the metadata encoder for those reported results. This is a reproducibility gap that should be explicitly clarified.

4. **The actual language templates are not provided.** The paper describes the three levels of metadata (dataset, task, sample) at a conceptual level (Section 3.2) but does not show example template texts. While the high-level description is sufficient for understanding the idea, verbatim templates are needed for exact reproducibility and to assess sensitivity to template phrasing.

5. **The Weather dataset reports saturated metrics (all methods at MSE 0.002), inflating the impression of uniform improvement.** In Table 2, every method achieves essentially the same near-zero MSE on Weather. Including this dataset in the average gives the appearance of narrower gaps than actually exist on the harder datasets. Reporting averages both with and without Weather, or noting this saturation explicitly, would be more informative.

### Trivial
None.

## Nice-to-Haves

- **Ablation of individual metadata levels.** The paper ablates all metadata jointly but does not test which of the three levels (dataset, task, sample) contributes most. This would help understand whether all three are needed or one level dominates.
- **Discussion of robustness to noisy or missing metadata.** In real-world deployment, metadata may be missing, incorrect, or inconsistently formatted. A discussion of robustness would strengthen practical relevance.
- **Reporting inference cost per sample** in addition to training time (Figure 4b) would be helpful for deployment considerations.
- **Testing on other time series tasks** (classification, anomaly detection) would demonstrate generality, though the paper scopes itself to forecasting, so this is strictly optional.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Related work does not discuss prior work feeding dataset-level or sample-level statistics into forecasting models."** — Removed per guidelines: the reviewer cannot confirm whether such prior work exists or not. The paper's related work already covers relevant native TS models and LLM4TS works.
- **"The introduction does not discuss providing metadata as structured numeric features, biasing the reader."** — Removed as this is a framing preference, not a factual error. The paper is entitled to frame the problem in terms of LLM encoding; the missing numeric baseline is already captured as a Major weakness above.
- **"The figure is hard to read due to scaling and lack of numeric labels"** and **"the text claims removing metadata hurts performance but magnitude is unclear"** — These may be parser artifacts from PDF extraction. The ablation conclusions are stated qualitatively and are consistent with the aggregated experimental picture.
- **"Pure formatting/style nitpicks"** (the harsh critic's comment about figure readability) — Removed.
- **The harsh critic's "Strengthening the Paper on Its Own Terms" points** that duplicate weaknesses already included above are not re-listed here. Non-duplicative ones (template sensitivity, per-level ablation, learnable token control) are moved to Nice-to-Haves or Minor weaknesses as appropriate.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — Removed. Only concrete, specific strengths are retained.

## Novel Insights

The reviews surface an important but subtle point that the paper itself does not fully address: the multi-dataset joint training results (Tables 3–4) are likely the *real* contribution here, not the individual training results. The individual training improvements are small and comparable to what one might get from better hyperparameter tuning or a slightly different architecture. But the joint training setting — where MetaTST is the *only* method showing uniform positive transfer across all sub-datasets — reveals a qualitatively different benefit: metadata helps the model disambiguate which forecasting scenario it is in, which is critical when training across heterogeneous datasets. This suggests the core value of the approach may not be "metadata provides useful numeric information" but rather "metadata provides a context signal that prevents catastrophic forgetting or domain confusion in multi-task learning." The reviews do not fully articulate this distinction, but it emerges from juxtaposing the tight margins in individual training with the clean, all-positive transfer in joint training.

## Suggestions

1. **Add a numeric metadata baseline.** For the main experiments, include a baseline where the same three metadata levels are provided as numeric features (e.g., dataset one-hot, input/output length as scalars, sample mean/std as additional channels concatenated to the series). If MetaTST still outperforms this, the case for LLM encoding is substantially strengthened.
2. **Specify the LLM used for main results** and include a statement about whether its choice affects comparisons across tables.
3. **Report results over multiple seeds** (at least 3) with mean and std for the key comparisons, especially on datasets where margins are tight.
4. **Include a control experiment** replacing metadata tokens with randomly initialized learnable tokens (no textual input) to verify gains come from content, not extra capacity.
5. **Provide at least one example of each metadata template** in an appendix or supplement.
