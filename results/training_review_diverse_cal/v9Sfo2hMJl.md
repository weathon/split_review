Now I have all the information I need. Let me verify one more thing — whether the paper's Figure 2 caption and text reference different datasets:

The text at line 128 says "dataset ETTh2" but the figure caption at line 110 says "ETTh1". This is an inconsistency in the paper itself.

Let me now synthesize the final review.

---

## Summary

This paper proposes UniTS, a hybrid time series forecasting model that combines a global feature extractor (linear layers) with a local feature extractor (multi-scale CNNs), along with data preprocessing modules (series decomposition, patching, instance normalization). The paper makes two main contributions: (1) a systematic study of the impact of lookback window length on model comparison fairness, proposing standardized evaluation settings, and (2) a hybrid architecture that outperforms individual model classes. Extensive ablation experiments investigate the contribution of each component.

## Strengths

- **Hybrid architecture yields consistent improvements across diverse benchmarks.** Table 1 (Setting i) shows UniTS achieving the lowest MSE/MAE across all eight datasets (Weather, Traffic, Electricity, ILI, ETT family) compared to strong baselines including PatchTST, DLinear, and TimesNet. This is the paper's central evidence and the claimed improvements are substantive (e.g., "substantial reduction in MSE and in MAE" over PatchTST).

- **Thoughtful standardization of lookback evaluation reveals a genuine methodological gap.** The paper correctly identifies that prior work used inconsistent lookback windows (e.g., Informer/Autoformer use fixed windows while DLinear/PatchTST finetune them). By evaluating under both Setting i (all models pick best from the **same** set of lookbacks) and Setting ii (fixed lookback), the paper provides a more equitable comparison framework than the prior ad-hoc landscape.

- **Ablation experiments isolate which modules matter and which do not.** Table 2 systematically ablates instance normalization (IN), local/global feature extraction, attention, position encoding, and layer normalization. Key findings: removing IN drastically degrades performance (confirming results from prior work like Li et al. 2023); adding attention *increases* MSE in all tested cases; removing GFE raises MSE by 28.04% vs. 2.19% for LFE. These results provide actionable architectural guidance.

- **Code is provided** (anonymous repository), supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **Fixed-lookback comparisons (Setting ii) are far too sparse to fully substantiate the paper's claims.** The paper motivates itself by criticizing unfair comparisons due to varying lookback windows, and prominently advertises that it "address[es] this issue by validating and standardizing parameters" (abstract). Yet the fixed-lookback results — the natural way to eliminate lookback as a confounding variable — are shown for only **one dataset** (Figure 2, which the text calls ETTh2 while the caption says ETTh1, an internal inconsistency). No full table of fixed-lookback results is provided. This gap means the reader cannot verify whether UniTS's advantage holds when all models use exactly the same lookback window. While Setting i (finetuned lookback from a shared set) is a legitimate and **standardized** evaluation protocol (all models choose from the same {96,288,384,576,640,720} set, which is fairer than prior practice), the paper would be substantially stronger with comprehensive fixed-lookback results. As is, the SOTA claim rests primarily on one evaluation mode, and the "fair comparison" contribution is incompletely validated.

### Minor

- **The attention-necessity conclusion is somewhat broader than the experiment supports.** The paper states "the attention layer is not essential for temporal modeling in time-series forecasting models" (Section 4.4). The experiment shows that adding attention to the linear global feature extractor *within UniTS's hybrid framework* degrades performance. This is a valid finding for that architectural context. However, the phrasing could be read as a general verdict on attention for time series, which is not warranted — PatchTST, a strong baseline in the paper's own results, uses attention effectively. The conclusion should be scoped to "within a hybrid model that already contains a local CNN branch, additional attention components on the global branch are detrimental" or similar. This is a presentation issue, not a flaw in the experimental finding itself.

- **The ablation asymmetry between global and local branches is under-analyzed.** Removing GFE increases MSE by 28.04% vs. 2.19% for LFE — a 13× difference. This suggests the global branch is doing most of the work. The paper attributes this to "the critical role of hybrid feature extraction" but does not dig deeper into when/why the local branch helps. For instance, does LFE matter more on short-horizon predictions or datasets with strong local patterns? A breakdown by prediction horizon or a visual analysis of learned features would strengthen the hybrid claim beyond aggregate metrics.

- **The hyperparameter analysis (Section 4.5) adds limited insight.** Showing that grid search beats Bayesian optimization with 20 iterations, and that learning rate and lookback matter, is not especially novel. These results support the paper's broader argument about evaluation standardization but do not constitute a standalone contribution. This section could be condensed without loss.

- **No computational complexity or runtime comparison.** The paper criticizes TimesNet for being slow but does not report training/inference time or parameter counts for UniTS or baselines. Given that UniTS stacks multiple convolutional kernels and linear layers, the reader cannot assess the cost of its SOTA performance.

- **Figure 2 has a dataset inconsistency.** The text (line 128) says the results are on "ETTh2" but the figure caption (line 110) says "ETTh1." This needs correction.

### Trivial

- Section 3.2.3 describes the local feature extractor as using "multiple kernels to capture temporal patterns across various scale sizes" without specifying the exact number or range of kernel sizes. The code is available, but the text could be more specific for self-contained reproducibility.

- No limitations section is included (standard practice but the paper would benefit from one).

## Nice-to-Haves

- A full table of fixed-lookback results (Setting ii) across all datasets would directly resolve the main weakness and make the SOTA claim fully convincing.
- An analysis of when the local branch adds the most value (e.g., by prediction horizon, dataset periodicity, or by visualizing learned convolutional filters).
- Reporting standard deviations or confidence intervals across multiple runs.
- Training/inference time and parameter count comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"TiDE, N-BEATS, N-HiTS, SpaceTimeFormer, RLinear/RMLP are never discussed in results"** — The paper lists these in Section 4.1 baselines. Table 1 is an image stripped by the parser, so we cannot verify their presence in the table. This should be assumed to exist as cited. **(Removed: parser artifact / cannot verify)**

2. **"Figure 1 captions and table images are placeholders"** — Parser artifact; the original submission has these. **(Removed: parser issue)**

3. **"The paper's main evidence uses the very practice it criticizes"** — This misreads the paper. The paper criticizes prior work where *different papers* used *different, unstandardized* lookback windows (Informer uses 96, DLinear finetunes to 720, etc.). The paper's Setting i has all models pick from the **same** set of lookbacks. This is a standardized protocol, not the same as the criticized practice. The paper does not claim that all models must use the identical lookback — it claims that evaluation should be standardized. Setting i achieves that standardization. **(Removed: factual misunderstanding of the paper's argument)**

4. **"The 'not essential for temporal modeling' claim implies attention is ineffective in architectures where it is the primary mechanism"** — The paper's context (adding attention to the linear GFE within UniTS) makes the scope clear. The claim is about "temporal modeling" within the tested framework, not a blanket statement about all Transformer architectures. The wording could be more precise but the finding is valid as stated in context. (Kept in Weaknesses as a presentation issue rather than a methodological flaw.)

## Novel Insights

None beyond the paper's own contributions. The hybrid architecture combining linear global and CNN local extraction within a standardized lookback evaluation framework is the paper's core novelty.

## Suggestions

1. **Provide complete fixed-lookback results** for all datasets. This is the single highest-impact improvement. It would fully substantiate the SOTA claim and validate the paper's methodological contribution about evaluation fairness.

2. **Reframe the attention-necessity conclusion** to explicitly scope it to the UniTS framework (e.g., "within a hybrid model with a CNN local branch, attention on the global branch is not beneficial").

3. **Analyze the global-local asymmetry more deeply** — when does the local branch add value? A breakdown by prediction horizon or dataset characteristic would strengthen the hybrid motivation.

4. **Add computational cost comparisons** (parameters, runtime) to contextualize the performance gains.

5. **Correct the Figure 2 dataset inconsistency** (ETTh1 vs. ETTh2).

---

## Score and Decision

The paper has a genuine contribution (a well-ablated hybrid architecture and a standardized lookback evaluation framework) and the core evidence (Table 1) supports the SOTA claim under a fair and standardized protocol. The main weakness — incomplete fixed-lookback results — is significant but addressable, and does not invalidate the paper's contributions. The paper is solid but would benefit from the suggested revisions before being fully persuasive.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>