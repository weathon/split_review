Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the source. Let me produce the final consolidated review.

## Summary

This paper proposes Time-LLM, a framework that repurposes frozen large language models (LLMs) for time series forecasting. The core idea has two components: (1) *patch reprogramming* — transforming time series patch embeddings into the LLM's embedding space via multi-head cross-attention with a learned set of text prototypes (condensed from the LLM's own word embeddings), and (2) *Prompt-as-Prefix (PaP)* — prepending a natural language prompt containing dataset context, task instruction, and input statistics to activate the LLM's reasoning. The LLM backbone remains completely frozen (only 6.6M trainable parameters in the reprogramming and projection layers). Experiments span long-term, short-term, few-shot, and zero-shot forecasting on standard benchmarks (ETT, Weather, Electricity, Traffic, ILI, M4).

## Strengths

- **Novel frozen-LLM adaptation framework with clear conceptual contribution.** Unlike prior work such as GPT4TS (which fine-tunes the LLM), Time-LLM keeps the backbone fully frozen and instead reprograms the input via cross-attention between patch embeddings and text prototypes sampled from the LLM's own embedding space. This is a principled way to align modalities without altering pre-trained weights. The architecture is cleanly described with three well-separated components (input embedding + reprogramming, frozen LLM, output projection).

- **Extreme parameter efficiency.** The trainable components (patch embedder, reprogramming cross-attention, output projection) total fewer than 6.6M parameters — approximately 0.2% of the Llama-7B backbone's parameters (Section 4.5, efficiency table). This makes the approach practical for resource-constrained settings and favorably compares even against parameter-efficient fine-tuning methods like QLoRA.

- **Consistent gains across diverse forecasting settings.** The method shows improvements in long-term forecasting (e.g., 12% over GPT4TS, 20% over TimesNet), short-term M4 forecasting (8.7% over GPT4TS), few-shot (5–8.4% over GPT4TS), and zero-shot (22% over GPT4TS). The trend of increasing advantage as data becomes scarcer (7.7% → 8.4% → 22% across 10% few-shot → 5% few-shot → zero-shot) is coherent and supports the thesis that the LLM's pre-training is activated effectively.

- **Ablation studies isolate component contributions.** The paper systematically ablates patch reprogramming (9.2% degradation, 17% in few-shot), Prompt-as-Prefix (8% degradation, 19% in few-shot), and individual prompt components (input statistics hurt most at 10.2%). This gives reasonable evidence that both major design choices matter.

## Weaknesses

### Fatal
None.

### Major

- **Baseline performance numbers are borrowed from another paper without independent verification.** The paper states (Section 4): "We compare with the SOTA time series models, and we cite their performance from [zhou2023one] if applicable." For a paper that claims state-of-the-art performance, this is a significant methodological limitation. The GPT4TS paper (Zhou et al., 2023) may have used different data splits, normalization procedures, training configurations, or evaluation protocols. Even when settings appear identical (e.g., input length 512), subtle differences in preprocessing, random seeds, or hardware can shift MSE by nontrivial amounts. This weakens the quantitative claim that *Time-LLM* outperforms specialized models — the central promise of the paper rests on comparisons that may not be apples-to-apples. The few-shot and zero-shot evaluations (Section 4.3–4.4) state they "adhere to the setups in [zhou2023one]" but this does not eliminate the concern that reproducing those baselines in-house could yield different numbers. *Note: the short-term M4 forecasting results are partially exempt from this concern, as the paper reports "unified seeds across all methods" (line 131), suggesting those baselines were re-run.*

### Minor

- **Prompt-as-Prefix sensitivity and generalizability are not analyzed.** The paper does not study how sensitive performance is to the exact wording of prompts, whether prompts were optimized per dataset, or how much effort is required to craft them for new domains. The ablation shows that removing input statistics hurts most (10.2% MSE increase), which is useful, but this essentially provides the LLM with numeric summary features (trend, lag). It remains unclear whether the prompt activates "reasoning" versus simply providing informative side information that a different architectural component could exploit. The claim that PaP "directs the transformation of reprogrammed input patches" (line 96) is not backed by any analysis of how the prompt influences the LLM's internal processing (e.g., attention patterns).

- **The 75% improvement over LLMTime is not properly contextualized.** In zero-shot results (Section 4.4), the paper reports a >75% improvement over LLMTime (Gruver et al., 2023) with comparable-size backbones. However, LLMTime uses a fundamentally different paradigm — tokenizing time series values as text and generating forecasts via direct text generation. The paper itself criticizes this approach (Section 3.2) for numeral tokenization issues. The 75% figure is then at least partly a consequence of this architectural mismatch rather than a clean head-to-head comparison. The paper should clarify the evaluation protocol used for LLMTime or contextualize the comparison as demonstrating that patching + reprogramming is more suitable for standard forecasting metrics than direct text generation.

- **No variance or confidence intervals reported.** None of the reported results include error bars, standard deviations, or statistical significance tests. While single-seed evaluation is common in forecasting benchmarks, reporting variance over 3–5 seeds would strengthen reliability claims. This is especially relevant given that the main comparison is against borrowed numbers, where the margin of error is unknown.

- **Inference computational cost is not discussed.** The efficiency analysis (Section 4.5) covers only trainable parameters (6.6M). But inference with a frozen 7B LLM is slow and memory-intensive. For a method presented as practical and efficient, the omission of inference latency, FLOPs, or memory usage is notable.

- **The prompt includes numeric statistics but the paper criticizes LLMTime for numeral tokenization issues.** The paper's own PaP includes numeric input statistics (e.g., "increase 0.2, trend 0.01") that are tokenized by the LLM. The paper should discuss whether the same numeral insensitivity concern applies here, or why it does not affect PaP's effectiveness.

### Trivial

- The cross-attention reprogramming introduces trainable parameters beyond the embedder and projector (W^Q, W^K, W^V matrices). A breakdown of the 6.6M trainable parameters across components would improve transparency.

- The description of text prototype initialization ("linearly probing E", line 73) is somewhat vague — whether these are actual vocabulary entries or learned vectors initialized from a subset of embeddings could be clarified.

## Nice-to-Haves

- A control experiment replacing the frozen LLM with a randomly initialized transformer of the same architecture would help determine whether the pre-training is essential or the framework works as a generic transformer architecture.
- Testing zero-shot transfer across more diverse domains (e.g., training on Weather, testing on Traffic) beyond the ETT family would strengthen generalization claims.
- A systematic analysis of learned prototype nearest neighbors in the embedding space would strengthen the claim that prototypes learn "language cues" describing time series properties.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not evaluate whether Time-LLM outperforms N-HiTS on SMAPE"** — Removed as factually inaccurate. The paper states (line 131) that *Time-LLM* "remains competitive...w.r.t. MASE and OWA," not that it outperforms N-HiTS on SMAPE. The critic misread the claim.
- **"The paper omits discussion of alternative approaches using frozen LLMs as feature extractors"** — Removed per instructions: missing related works should not be mentioned without external verification.
- **"Prompt templates are not provided in the main text"** — Removed as factually wrong. The paper explicitly references a prompt example figure (Fig. 6, line 90–92) that is in the main text.
- **"LLMs possessing robust pattern recognition is a strong assumption never tested directly"** — Removed as a strawman. The paper's experiments test end-task performance, which is the standard evaluation paradigm. The internal mechanism of "reasoning" is not claimed to be directly verified and doing so is outside the paper's scope.
- **"The paper should edit the input time series directly"-type suggestions** — Removed where they conflict with the paper's stated design philosophy.
- **Criticisms of missing appendix content** — Removed per instructions that the parser strips appendix sections.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the **tension between the paper's critique of LLMTime's numeral tokenization issues and the paper's own use of numeric statistics in PaP prompts** is a real inconsistency that the paper does not address. If LLMs are insensitive to high-precision numerals (as the paper argues to motivate PaP over Patch-as-Prefix), then including numeric values in the prompt should suffer from the same issue, yet performance improves. This suggests either (a) that the insensitivity claim is overstated for summary statistics embedded in natural language context, or (b) that the benefit of PaP comes from the language context around the numbers rather than the numbers themselves. Either direction would make for an interesting follow-up study. The reviews also collectively highlight that the paper's evaluation strategy (borrowing baselines) is a recurring concern in this rapidly growing subfield — an observation worth the community's attention.

## Suggestions

1. **Rerun at least the most critical baselines** (PatchTST, GPT4TS, DLinear, TimesNet) in-house on 3–5 representative datasets (e.g., ETTh1, Weather, ECL) to verify that the claimed margins hold under identical conditions. This is the single highest-impact improvement.
2. **Add a prompt-sensitivity analysis**: vary wording, remove individual components systematically beyond the current ablation, and compare against providing the same numeric statistics via a non-prompt channel (e.g., concatenated to patch embeddings).
3. **Report error bars** over at least 3 random seeds for a representative subset of results.
4. **Add inference cost metrics** (wall-clock time, peak memory, FLOPs) to contextualize the efficiency claims.
5. **Clarify the LLMTime comparison protocol** in the main text: were both methods evaluated on exactly the same cross-domain splits and with the same metric computation?

## Score and Decision

This paper presents a genuinely novel and well-motivated approach to adapting frozen LLMs for time series forecasting. The architecture is clean, the parameter efficiency is impressive, and the empirical pattern — larger gains in data-scarce settings — is coherent and supports the core thesis. However, the evaluation has a significant limitation: the primary quantitative evidence for state-of-the-art performance relies on baseline numbers borrowed from another paper without independent verification. While borrowing numbers is a common practice in standardized benchmarks, the paper's central claim of "outperforming state-of-the-art specialized forecasting models" demands stronger empirical support. Combined with the lack of variance reporting, the uncontextualized LLMTime comparison, and the shallow analysis of PaP, the paper is strong methodologically but falls short of the rigorous evaluation standard expected for its core claim.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>