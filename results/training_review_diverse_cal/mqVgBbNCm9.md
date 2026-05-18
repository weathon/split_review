Now I have a thorough understanding of the paper and all reviewer inputs. Let me compose the consolidated review.

## Summary

This paper introduces Skeleton-of-Thought (SoT), a prompting strategy that reduces end-to-end LLM generation latency by first eliciting a concise answer skeleton from the model, then expanding each skeleton point in parallel (via batched decoding for local models or parallel API calls for API-based models). The method achieves over 2× speed-up on 8 out of 12 tested models (up to 2.39×) while maintaining or modestly improving answer quality on several question categories. A router extension (SoTR) adaptively triggers SoT only for suitable questions, improving quality on previously unsuitable categories like math and coding.

## Strengths

1. **Novel approach achieving latency reduction without model or system modification.** The paper demonstrates that off-the-shelf LLMs can be accelerated purely through prompting strategy, explicitly stating "parallel decoding of off-the-shelf LLMs *without* any changes to their model, system, or hardware" (Section 1). This is a distinct departure from prior efficient inference methods requiring quantization, pruning, or architectural changes.

2. **Substantial and consistent speed-ups across diverse models.** Empirical results show >2× speed-up on 8 out of 12 models (Figure 2, Section 3.1.1), including both open-source models (Vicuna-33B: 2.69× on an example) and API-based models (Claude: from 22s to 12s). The paper tests on 12 models spanning 9 open-source and 3 API-based LLMs, and validates on two datasets (Vicuna-80 and WizardLM-218).

3. **Maintained answer quality with systematic evaluation.** Using two LLM-based evaluation frameworks (FastChat and LLMZoo) with GPT-4 as judge, the paper shows SoT achieves win/tie rates around 60% overall (Figure 5). The evaluation mitigates ordering bias by running pairwise comparisons in both orders. Net win rates are positive on five question categories (generic, common-sense, knowledge, roleplay, counterfactual) across both evaluation frameworks.

4. **Adaptive router addressing the key limitation.** The paper proposes and evaluates two router variants (prompting-based and a trained RoBERTa model) that selectively apply SoT only when beneficial. This addresses SoT's main weakness (unsuitability for step-by-step reasoning), and the trained router achieves speed-ups on 7 out of 12 models while improving quality on previously challenging categories (Figure 8, 9).

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the evidence presented and the paper is transparent about its limitations.

### Minor

1. **Speed-up validation for open-source models is deferred to the appendix.** The main paper's primary speed-up results for open-source models (Figures 2, 3) are derived from pre-computed profiling tables rather than actual end-to-end measurements. The paper states that actual latency comparisons exist in the appendix (Section 3.1), but the main quantitative results a reader sees first are estimates. While estimation via validated profiling tables is a legitimate methodology (and the paper does report actual API measurements for API-based models in the main text, as well as a concrete Vicuna-33B example in the introduction), the headline speed-up figures would carry more weight if at least a subset of actual measurements were shown in the main paper alongside the estimates. This is a presentation issue, not a fundamental flaw — the appendix (which exists in the original submission) addresses it.

2. **LLM-as-judge structural bias is not addressed.** The paper acknowledges that human evaluation would be biased because humans can detect the SoT pattern (Section 6), but the same concern applies to GPT-4 as evaluator: the structured, numbered-point format of SoT answers could systematically bias the LLM judge regardless of content quality. The paper mitigates ordering bias but not structural bias. The fact that the two evaluation frameworks (FastChat and LLMZoo) give different absolute net win rates (45.8% vs 29.5%) suggests sensitivity. This does not undermine the "maintains quality" conclusion (both frameworks agree SoT is not worse ~60% of the time), but it weakens the "improves quality on several categories" claim, which would benefit from stronger support.

3. **No quantification of API cost overhead.** The paper notes that SoT increases token counts by 1–2× and can raise API costs (Section 3.1.1, Section 6), but does not report actual dollar-cost increases for the API models tested (ChatGPT, Claude, GPT-4). For practitioners evaluating the speed-cost-quality trade-off, this is actionable information that is missing.

### Trivial

1. The "data-centric optimization" framing (Section 1, Section 6) is a stretch — SoT manipulates output format via prompts rather than data curation or augmentation. The paper explains its reasoning, but the terminology may confuse readers expecting data-level methods in the conventional sense.

2. The router evaluation is conducted on relatively small datasets (Vicuna-80, WizardLM-218). The paper acknowledges this is a proof-of-concept, and the results are consistent, but the scale limits confidence in generalization.

3. The paper does not discuss the GPU memory overhead of batched decoding (storing B× KV-cache simultaneously) when expanding points in parallel for open-source models. This is a practical detail relevant to practitioners.

## Nice-to-Haves

- An ablation study showing how different skeleton prompt templates (e.g., requiring more/fewer points, different levels of detail) affect both speed-up and quality.
- A human evaluation study where SoT and baseline answers are reformatted into a common prose format to eliminate structural bias, even at small scale (50 questions, 2–3 annotators).
- Reporting estimated dollar-cost increases per answer for API-based models to make the speed-cost-quality trade-off actionable.

## Removed Points

- **"Speed-up results rest entirely on estimated latencies"** — This is not entirely accurate. The paper reports actual latency measurements for API-based models (Section 3.1) and provides concrete actual examples (Vicuna-33B going from 43s to 16s in Section 1). Only the open-source model bulk results use estimation, and the paper explicitly references actual measurements in the appendix (which exists in the original submission). The criticism is downgraded to Minor issue #1 above reflecting the real residual concern about main-paper presentation.

- **"Data-centric framing is somewhat forced" (critic's words)** — This is a stylistic/subjective opinion about framing, not a substantive weakness. Kept in Trivial with softened language.

- **"Router evaluation small datasets"** — Retained in Trivial since the limitation is stated but the scale is indeed modest.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the method's cleverness and the difficulty of fairly evaluating it: SoT's distinctive output structure (numbered points) makes it immediately identifiable to both humans and LLM judges, creating a circular evaluation challenge where the very feature that enables the speed-up (structured, independently expandable points) also makes it hard to assess whether the quality difference is real or an artifact of the evaluator's sensitivity to format. This is a deeper methodological issue that extends beyond this paper to any method that changes output surface form.

## Suggestions

- Include actual end-to-end latency measurements for at least 2–3 open-source models in the main paper, side-by-side with the estimated numbers, to validate the profiling-table approach.
- Report the dollar-cost increase per answer for API-based models to make the trade-off actionable for practitioners.
- Add a discussion of the structural bias issue in the LLM judge evaluation, and ideally conduct a small-scale de-biased evaluation (e.g., reformatting both SoT and baseline answers into plain prose before presenting to the judge).

## Score and Decision

The paper presents a creative, well-motivated, and practically useful method for reducing LLM latency. The core claims are supported by evidence across 12 models and two evaluation frameworks. The weaknesses identified are presentation-level (deferred validation), secondary (structural bias in the quality evaluator), or incremental (missing cost quantification) — none invalidate the central contribution. The paper is clearly written, properly scopes its limitations, and makes a genuine contribution to efficient LLM inference.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>