Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes Time-LLM, a framework that repurposes frozen large language models (LLMs) for time series forecasting via two key ideas: (1) **patch reprogramming** with learned text prototypes, where time series patches are aligned to the LLM's embedding space through cross-attention over a small set of prototype vectors drawn from the LLM's vocabulary, and (2) **Prompt-as-Prefix (PaP)**, where natural language prompts (dataset context, task instructions, input statistics) are prepended to the reprogrammed patches to guide the LLM's reasoning. The backbone LLM remains completely frozen; only lightweight input/output layers (~0.2% of Llama-7B parameters) are trained. Experiments across long-term, short-term, few-shot, and zero-shot settings show consistent improvements over specialized forecasting models.

## Strengths

1. **Novel and practical framework for leveraging frozen LLMs in time series.** Keeping the backbone LLM entirely frozen while training only 6.6M parameters (~0.2% of Llama-7B) is a clear practical advantage. The paper demonstrates that strong forecasting performance can be achieved without the expense of fine-tuning a 7B model. This is well-supported by the efficiency analysis (Table 5 in the paper) and the ablation study.

2. **Consistent outperformance across diverse settings.** Time-LLM achieves SOTA or near-SOTA results across long-term forecasting (8 datasets, 4 horizons), short-term forecasting (M4 benchmark), few-shot (5% and 10% training data), and zero-shot settings. The improvements over strong non-LLM baselines like PatchTST, TimesNet, and DLinear are substantive and cannot be attributed to backbone size.

3. **Prompt-as-Prefix is validated as critical via ablation.** Ablation studies show that removing PaP causes over 8% degradation in standard forecasting and over 19% in few-shot tasks. The component-level analysis (removing input statistics, task instructions, dataset context separately) provides clear evidence that each contributes meaningfully.

4. **Scaling law holds after reprogramming.** The analysis of model variants (Llama-7B vs. 1/4-capacity Llama vs. GPT-2) shows that larger backbones yield proportionally better results (14.5–14.7% improvement), which is non-trivial — it confirms the reprogramming framework effectively utilizes additional LLM capacity rather than saturating.

5. **Comprehensive evaluation across multiple benchmarks and data-scarce regimes.** The paper covers 8 long-term datasets, the M4 benchmark for short-term, controlled few-shot (5%, 10%), and zero-shot transfer, with comparisons against a broad set of up-to-date baselines. This breadth supports claims of general applicability.

## Weaknesses

### Fatal

None.

### Major

1. **Headline comparison against GPT4TS (fine-tuning approach) is confounded by backbone model size.** TIME-LLM's default backbone is Llama-7B, while GPT4TS (Zhou et al., 2023) uses GPT-2 — a model roughly an order of magnitude smaller. The paper's own model analysis (Section 4) shows that swapping from Llama-7B to GPT-2 within TIME-LLM causes a 14.7% MSE increase, demonstrating that backbone size substantially affects results. The claimed 12% average improvement over GPT4TS (long-term) and 5% (few-shot) therefore conflates the benefit of the reprogramming method with the benefit of using a larger backbone. The paper does not report GPT4TS with a comparable backbone (e.g., Llama-7B with LoRA) nor TIME-LLM with GPT-2 compared against GPT4TS. This gap directly affects the paper's central comparative claim that reprogramming (freezing) outperforms fine-tuning. Without this control, the paper cannot cleanly attribute the gains to the proposed method rather than to backbone scale.

2. **Zero-shot evaluation is too limited to support claims of cross-domain generalizability.** All zero-shot experiments are conducted within the ETT family (ETTh1, ETTh2, ETTm1, ETTm2). These datasets share the same measurement system (electricity transformer temperature) and differ primarily in sampling frequency and resolution. This is not cross-domain generalization — it is cross-resolution generalization within a single domain. The paper's introduction motivates the approach in terms of generalizing across diverse applications (demand planning, energy, climate), but no experiment tests training on one genuinely different domain (e.g., electricity) and testing on another (e.g., traffic or weather). The claim that "LLMs possess remarkable few-shot and zero-shot transfer learning" enabling "generalizable forecasting across domains" is not supported by the evidence presented.

### Minor

1. **Integration of Prompt-as-Prefix with patch embeddings is underspecified.** The paper states that prompt tokens and patch embeddings $\mathbf{O}^{(i)}$ are "packed and feedforwarded" through the frozen LLM, and that "additional prompt prefixes are added to the input." However, it does not specify how the natural language prompt is tokenized and embedded, nor how the resulting token embeddings are concatenated with the continuous patch embeddings. If the patches are inserted as continuous vectors alongside token embeddings (similar to soft prompts), the paper should state this explicitly and note that the LLM's first layer (a linear transformation + nonlinearity) can process continuous inputs — which is standard practice in prefix-tuning but worth clarifying for reproducibility.

2. **Interpretation of text prototypes as learning "language cues" is not quantitatively validated.** The paper claims prototypes correspond to phrases like "short up" and "steady down" based on visual inspection, but provides no quantitative mapping — no nearest-neighbor projection to actual vocabulary tokens, no analysis of whether different prototypes correspond to distinct semantic concepts, and no ablation on the number of prototypes. The claim that prototypes "learn to summarize language cues" remains a post-hoc interpretation rather than an empirically supported finding.

3. **The 75% improvement over LLMTime is presented with insufficient context in the main text.** While the paper does note that the backbone is of comparable size (7B), the 75% figure is stated without breaking down which specific metrics, horizons, and datasets produce it. This figure is an order of magnitude larger than other reported improvements (1.4% over PatchTST, 5–12% over GPT4TS), which makes it appear anomalous. The referenced table likely contains the details, but the main text should at minimum give the average MSE values for context.

4. **No error bars or confidence intervals reported.** Given the number of datasets, horizons, and comparisons, single-run results without variance estimates make it difficult to assess whether the reported improvements are statistically significant, especially for the smaller margins (e.g., 1.4% over PatchTST).

5. **Training resource costs (GPU hours, convergence time) not reported.** The paper claims the method is efficient and requires "only a small set of time series and a few training epochs," but provides no actual training time or GPU-hour numbers. Given that the forward pass through a 7B-parameter model is expensive even if the backbone is frozen, the practical resource cost is relevant information.

6. **No sensitivity analysis for key hyperparameters.** The number of text prototypes $V'$, number of attention heads $K$, patch length $L_p$, and stride $S$ are not systematically ablated. While the paper provides ablations on the main components, the sensitivity of results to these hyperparameters is unclear.

7. **No discussion of failure cases or settings where Time-LLM underperforms.** The narrative is uniformly positive; acknowledging specific horizons, datasets, or conditions where the method struggles would increase credibility.

### Trivial

1. **Occasional overclaiming in framing.** The statement "our work points the way toward multimodal foundation models that can excel on both language and sequential data tasks" is aspirational but goes beyond the paper's actual demonstration (univariate time series forecasting only). Similar forward-looking language in the intro could be scaled back to match the evidence.

## Nice-to-Haves

- **Backbone-controlled experiment:** Run TIME-LLM with GPT-2 backbone against GPT4TS (GPT-2) to isolate the effect of reprogramming vs. fine-tuning at the same model scale. Conversely, apply GPT4TS-style fine-tuning to Llama-7B (e.g., via LoRA) for comparison.
- **Cross-domain zero-shot evaluation:** Train on one genuinely different domain (e.g., Electricity or Weather) and test on another (e.g., Traffic or ETT), to directly test the claimed domain-generalization capability.
- **Quantitative validation of prototype interpretability:** Map each learned prototype to its nearest token(s) in the LLM's vocabulary and report top-k nearest words. Show whether these words relate to time series properties.
- **Exact prompt template disclosure:** Provide the verbatim prompt template used for at least one dataset in the main text or an appendix.
- **Error bars** over at least 3 random seeds for the main results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's Point 4 (backbone size not controlled for LLMTime comparison):** The paper explicitly states the LLMTime comparison uses "the backbone LLM of comparable size (7B)," so this specific comparison IS controlled for model capacity. The remaining concern is about presentation/context (moved to Minor weakness 3 above), not about an uncontrolled comparison.
- **Critic's claim that the 75% figure is "misleading" due to different evaluation protocols:** The paper references a table (`\input{tables/zero-shot-forecasting-brief}`) with the underlying metrics. The critic provides no evidence that the evaluation protocols differ. The substantive concern (lack of context in main text) is retained as a Minor weakness.
- **Critic's claim that ablation numbers reported "only as percentages" is a weakness:** Reporting relative degradation percentages is standard practice for ablation studies and provides the information a reader needs (relative importance of each component). The absolute MSE values are presumably in the referenced table.
- **Strength Finder's claim of "interpretable" cross-modal alignment:** Conflicts with the verified weakness that the prototype interpretation is not quantitatively validated. The efficiency part of the strength is retained in Strengths (item 1).

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an important meta-point: the field of "LLMs for time series" currently lacks standardized protocols for fair comparison. Different works use different backbones (GPT-2 vs. Llama-7B), different fine-tuning strategies (full fine-tuning, LoRA, freezing), and different evaluation splits. The backbone size confound identified here is a systematic issue that affects not just this paper but the broader literature. A community standard — perhaps reporting results both with a small backbone (GPT-2) and a large backbone (Llama-7B) for all methods — would substantially strengthen future work in this area.

## Suggestions

1. **Run the backbone-controlled experiment as the highest-priority addition.** Comparing TIME-LLM (GPT-2) against GPT4TS (GPT-2) would directly isolate the effect of reprogramming from backbone size and cleanly support or qualify the paper's central claim.
2. **Expand zero-shot evaluation to at least one genuinely cross-domain pair** (e.g., train on Weather → test on ETT, or train on Electricity → test on Traffic). This directly tests the generalizability claim made in the introduction.
3. **Clarify the PaP integration** by specifying (a) how the prompt text is tokenized using the LLM's tokenizer, (b) how the resulting token embeddings and continuous patch embeddings are concatenated along the sequence dimension, and (c) whether this is done at the embedding layer or as prepended tokens.
4. **Provide nearest-vocabulary-token mappings** for a sample of text prototypes to substantiate the interpretability claim.
5. **Add error bars** (standard deviation over 3 runs) for at least the main long-term and zero-shot results.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>