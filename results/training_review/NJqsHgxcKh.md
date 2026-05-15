I have thoroughly read the paper and verified each reviewer claim against the actual content. Let me now produce the consolidated review.

## Summary

This paper proposes MetaTST, a Transformer-based time series forecasting method that incorporates multi-level textual metadata (dataset descriptions, task specifications, and sample-level statistics) via a frozen LLM encoder. The metadata tokens are concatenated with endogenous patch tokens and exogenous series tokens, and a Transformer encoder fuses them to produce informed representations. Experiments on 12 benchmarks under both individual and multi-dataset joint training settings show consistent improvements over strong baselines including TimeXer, iTransformer, PatchTST, and LLM4TS methods.

## Strengths

- **Novel and well-motivated metadata paradigm**: The paper identifies a genuine gap — side information beyond the time series itself is underexplored in forecasting — and proposes a clean, three-level taxonomy (dataset, task, sample) for metadata. Using a frozen LLM as a plug-in encoder (rather than a fine-tuned backbone) is a practical and efficient design choice that differs from prior LLM4TS work (GPT4TS, TimeLLM). This is supported by the method description (Section 3.2) and Table 1.

- **Consistent SOTA performance across diverse benchmarks**: Under individual training, MetaTST achieves the best average MSE on short-term (Table 2: 0.300 vs. next-best TimeXer 0.307) and long-term forecasting (Table 3: 0.125 vs. TimeXer 0.132). The improvements are consistent across most of the 12 sub-datasets, ruling out cherry-picking.

- **Multi-dataset joint training results are the most convincing evidence**: In the joint training setting (Tables 4, 5), MetaTST is the only model that shows uniformly positive promotion (all green arrows) across every sub-dataset, while all baselines (PatchTST, iTransformer, TimeXer) degrade on some datasets (red arrows). For short-term, MetaTST achieves 10.8% average MSE promotion; for long-term, 3.54%. This directly validates that metadata helps the model distinguish diverse forecasting scenarios — a qualitatively different result from the small absolute gains in individual training.

- **Ablation studies verify each input component's contribution**: Figure 4 systematically ablates endogenous, exogenous, and metadata components. The metadata consistently improves over the "without metadata" baseline across four settings, and the contribution is especially pronounced when exogenous series are scarce (ETTm1, EPF), which aligns with the paper's hypothesis.

- **Efficiency advantage over LLM4TS alternatives**: Figure 5b shows MetaTST has lower training/inference cost than GPT4TS and TimeLLM while achieving better forecasting accuracy, supporting the practical benefit of using a frozen LLM as a small encoder rather than a full backbone.

## Weaknesses

### Fatal
None.

### Major

- **Missing non-LLM baseline for metadata encoding**: The paper never compares its LLM-based metadata encoder to a simple alternative — e.g., embedding a dataset ID, task ID, and numerical sample statistics (mean, std) via learnable linear projections. Without this control, there is no evidence that the LLM's *semantic understanding* is what drives the improvement; the gains could come from any form of dataset-specific or sample-specific conditioning. This is a critical methodological gap that weakens the central claim about LLMs being necessary or beneficial for metadata encoding.

- **Sample-level metadata (mean, std) confounds the contribution**: The sample-level metadata includes the mean and standard deviation of the time series sample (Section 3.2). This is a simple statistical summary computable from the input, yet it provides an explicit scale signal that baselines must learn implicitly. The paper does not ablate sample-level metadata separately from dataset- and task-level metadata, so it is impossible to determine whether the improvements come from "semantic understanding" of text or from the model trivially receiving pre-computed normalization statistics. This confounds the claimed contribution.

### Minor

- **Lack of statistical significance reporting**: The reported improvements are often small in absolute terms (e.g., long-term avg. MSE 0.125 vs. 0.132, short-term 0.300 vs. 0.307). No confidence intervals, standard deviations, or statistical tests are reported for any main result. While single-run evaluation is common in TS forecasting, the magnitude of gains here (especially on individual datasets like Weather where all models achieve 0.002 MSE) makes statistical significance a genuine concern. This is amplified in the joint training results where the claim of "uniformly positive promotion" would be stronger with error bars.

- **Unclear how baselines handle exogenous series**: The paper defines the task as "forecasting with exogenous series" (line 153) but does not describe how baselines like PatchTST (channel-independent) and iTransformer were adapted to treat some variates as exogenous inputs for a single target rather than as symmetric multivariate targets. Models with strict channel independence would not propagate exogenous information to the target prediction. The paper should clarify whether all baselines received the same exogenous series as input features in a comparable manner.

- **Ablation shows metadata benefit is dataset-dependent**: Figure 4 shows that in some datasets (Traffic, ECL, long-term), the gap between "En+Ex" and "En+Ex+Meta" is visually small. The paper acknowledges this but frames it as metadata being more important when exogenous series are limited (ETTm1, EPF). This is honest but limits the generality of the claim that metadata is universally beneficial — it seems most valuable when exogenous information is already scarce.

- **t-SNE visualization is unsurprising**: Figure 5b shows metadata representations clustering by dataset. Since the templates contain dataset names (e.g., "ETTh1 is an electricity transformer temperature dataset"), the encoder trivially distinguishes datasets. This confirms the encoder works but does not prove that this distinction helps forecasting. The attention map visualization (Figure 6) is qualitative and not systematically analyzed.

### Trivial
None.

## Nice-to-Haves
- A controlled ablation that removes sample-level metadata (mean, std) while keeping dataset- and task-level metadata, to isolate the source of improvement.
- Reporting results with standard deviations over 3+ random seeds for the main tables.
- Providing the actual metadata templates used for each dataset (e.g., in an appendix) to improve reproducibility.

## Removed Points
- **"Unfair baseline comparison because baselines may not receive exogenous series"**: This criticism is largely a misunderstanding. In the multivariate forecasting setting used for long-term benchmarks, models like iTransformer, PatchTST (with multi-channel input), and TimeXer naturally receive all variates as inputs. The EPF short-term benchmark has a standard exogenous-series setup. The paper follows established experimental protocols (citing PatchTST and TimeMixer). The critic's claim that "the SOTA claim is invalid" and the issue is "not fixable by ablations" is excessive and not supported by the paper. The critic does not provide evidence that baselines were deprived of information. (The remaining kernel of truth — lack of explicit description — is preserved as a minor weakness above.)
- **"Introduction overstates practical applicability because templates are manually constructed"**: The paper states metadata is "readily available" and uses pre-designed templates. This is standard for work introducing a new paradigm; the first instantiation often uses manual templates. This is a scope-of-contribution issue, not a weakness of the presented method.
- **"Table 1 is misleading"**: Table 1 compares input modalities. "TS" for native models correctly reflects they process only numerical series; "TS+Language" for MetaTST correctly reflects it additionally processes text. This is not misleading — it accurately represents what the methods use.
- **"Average pooling ablation justified only on one task"**: The paper shows the ablation in Figure 5a and states average pooling achieves the best performance in most cases. This is standard practice for such design choices.
- **"Efficiency analysis lacks detail about model configuration"**: The paper states "unified model hyperparameters" and specifies using a 6-layer GPT-2 for LLM baselines. This is sufficient for the main claim (MetaTST is cheaper than backbone-based LLM4TS).

## Novel Insights
The most interesting finding is not visible from the individual training results (where gains are small) but from the joint training setting (Tables 4, 5): MetaTST is the *only* model that benefits uniformly from multi-dataset training (all sub-datasets show positive promotion), while every baseline degrades on at least some datasets. This suggests that metadata acts as a **disambiguation signal** that prevents the model from being confused by conflicting temporal patterns across different domains. This is a qualitatively different benefit from simply improving in-distribution accuracy and points to a genuine advantage of the metadata approach for building multi-domain foundation models — an insight that is more significant than the absolute MSE numbers might suggest.

## Suggestions
1. **Add a non-LLM metadata baseline**: Replace the LLM encoder with a learnable embedding lookup for dataset/task IDs plus a linear projection of sample statistics. If this matches MetaTST, the LLM is unnecessary; if it falls short, the LLM's semantic understanding is validated.
2. **Ablate sample-level metadata separately**: Remove the mean/std from the sample-level template and measure the drop. This would disentangle the contribution of normalization-like information from semantic context.
3. **Report standard deviations**: Even 3 runs would significantly strengthen the empirical claims, especially for the joint training promotion numbers where the qualitative pattern ("all green arrows") is the strongest selling point.
4. **Clarify baseline adaptation**: Explicitly state how each baseline model was adapted to the single-target-with-exogenous setting (e.g., "for PatchTST, all variates were concatenated as input features" or "for iTransformer, the output head was modified to predict only the target variate").

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>