## Summary

This paper introduces In-Context Watermarking (ICW), a model-agnostic approach that embeds detectable watermarks into LLM-generated text using only prompt engineering — without requiring access to model weights, logits, or the decoding process. Four watermarking strategies are proposed at different linguistic granularities (Unicode insertion, word-initial letter bias, lexical green-listing, and sentence-level acrostics), each paired with a tailored statistical detection scheme. The paper evaluates these methods in both a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting, the latter motivated by detecting AI-generated peer reviews. The central empirical finding is that ICW effectiveness is highly dependent on model capability: weaker models (GPT-4o-mini) largely fail to execute the watermarking instructions, while a capable model (GPT-o3-mini) achieves ROC-AUC ≥ 0.995 across all four methods in both settings.

## Strengths

- **Well-motivated problem with a concrete, under-addressed threat model**: The IPI setting — where conference organizers embed watermarking instructions into manuscripts to detect AI-generated reviews — inverts the typical prompt injection threat model and addresses a genuine gap in the watermarking literature (Section 3.2, Figure 2). The paper clearly articulates why existing watermarking methods (requiring model access) and post-hoc detectors (low accuracy) are insufficient for this use case.

- **Systematic taxonomy of ICW strategies across linguistic granularities**: The four methods span character-level (Unicode), word-initial, lexical, and sentence-level (Acrostics), with each method accompanied by a tailored detection scheme (z-statistic for Initials/Lexical, Levenshtein distance for Acrostics, ratio-based for Unicode). Table 1 provides an intuitive trade-off comparison across LLM requirements, detectability, robustness, and text quality.

- **Strong empirical evidence that ICW effectiveness scales with model capability**: Table 2 provides a crisp, well-controlled demonstration. Initials ICW jumps from ROC-AUC 0.572 (GPT-4o-mini) to 0.999 (GPT-o3-mini); Acrostics ICW from 0.590 to 1.000; Lexical ICW from 0.910 to 0.995. This capability-dependence is the paper's most important empirical finding and directly supports the thesis that ICW feasibility is gated by — and will improve with — underlying LLM capability.

- **Competitive robustness under paraphrasing, outperforming post-hoc baselines**: Figure 3 shows that with GPT-o3-mini under paraphrasing attack, Initials ICW (AUC=0.887), Lexical ICW (AUC=0.924), and Acrostics ICW (AUC=0.922) all substantially outperform YCZ+23 (AUC=0.557) and PostMark (AUC=0.841). This is notable given that the ICW methods are prompt-only while the baselines directly modify text.

- **Minimal degradation of text quality**: Table 3 shows that Lexical ICW scores 4.918/5.000 relevance and 4.990/5.000 quality, nearly indistinguishable from unwatermarked GPT-o3-mini output (4.982, 5.000), and far above PostMark (2.648, 3.848). Acrostics ICW similarly preserves quality (4.950, 4.978), confirming that sentence-initial constraints leave the bulk of generation unconstrained.

- **IPI results validate instruction-following over long contexts**: Table 2 (IPI columns) shows GPT-o3-mini achieves ROC-AUC ≥ 0.997 for all four ICW methods when the watermarking instruction is embedded within full academic papers, demonstrating that LLMs can reliably follow covert watermarking instructions even in long-context scenarios.

## Weaknesses

### Fatal

None.

### Major

- **Missing unwatermarked LLM baseline for detection**: The detection evaluation compares watermarked LLM output against *human-written* text (ELI5 answers for DTS, human reviews for IPI). While the theoretical framework (random green-list selection) implies that unwatermarked LLM text should produce the same null distribution as human text, the paper never empirically verifies this. The operational detection question in practice is whether the detector can distinguish watermarked LLM output from *unwatermarked* LLM output — and without this empirical check, the reported FPR and ROC-AUC values are not fully validated for the most relevant comparison. This is the highest-priority gap to address.

- **Only two models from a single provider**: The central thesis — that ICW effectiveness scales with model capability — is supported by only two models (GPT-4o-mini and GPT-o3-mini), both from OpenAI. Two data points from the same model family do not establish a robust trend, and it is unclear whether the capability-dependence generalizes to models from other providers (e.g., Claude, Gemini, Llama) with different architectures and training pipelines.

### Minor

- **IPI experimental protocol underspecified in the main text**: The exact query Q used to elicit reviews from the LLM in the IPI setting is not stated (Section 5.1 defers to Appendix C, which is stripped). Similarly, the source and nature of human-generated negatives for IPI detection are not described. Given that the IPI case study is the paper's most distinctive contribution, these details should be summarized in the main text.

- **LLM-as-Judge evaluation bias not discussed**: Table 3 reveals a strong evaluator bias — Gemini-2.0-flash rates GPT-o3-mini unwatermarked text at 4.982–5.000 while human text scores 3.946–4.440. The paper notes that ICW methods score close to unwatermarked text (reassuring), but the interpretation of absolute quality scores is complicated by this bias, and the paper does not address it.

- **Acrostics detection resampling bias**: The Acrostics ICW detection (Section 4.2.4) estimates the null distribution of Levenshtein distances by resampling sentence-initial letter sequences from the suspect text itself. If the suspect text is watermarked (H₁), the resampled sequences are drawn from a watermarked distribution, potentially biasing estimates of μ and σ. The paper does not discuss whether this creates a conservative or anti-conservative bias.

- **Vocabulary and green-list sizes not reported**: For Lexical ICW, the actual vocabulary size |𝒱| and green-list size |𝒱_G| used in experiments are not reported in the main text. These numbers are important for understanding the feasibility of the approach given LLMs' known limitations in retrieving specific information from long contexts.

### Trivial

- **Equation (3) contains a notation error**: Line 93 defines y ← M(t̃ ⊕ Instruction(k, τ) ⊕ Q), but t̃ was already defined as t ⊕ Instruction(k, τ) on line 91. This concatenates the watermarking instruction twice; the intended expression is y ← M(t̃ ⊕ Q).

## Nice-to-Haves

- Include detector calibration at specific operational FPR thresholds (e.g., what TPR does the method achieve at FPR = 0.1% or 0.01% in a realistic deployment?), complementing the ROC-AUC and T@1%F metrics.
- Discuss the practical feasibility of embedding invisible instructions in PDF manuscripts — can current LLM APIs (e.g., OpenAI's file upload) preserve and process zero-font-size or white-text formatting?
- Summarize the key findings from the "ignore prior prompts" attack (currently in Appendix D.1) in the main text, as this is the most obvious countermeasure to the IPI approach.

## Removed Points

These points were flagged by reviewers but are removed from the final review with justification:

- **"Unicode ICW inflates results and is not genuine watermarking"**: REMOVED. The paper explicitly acknowledges Unicode ICW's limitations in Section 4.2.1 ("applies only to digital text... highly fragile to transformations like LLM paraphrasing"). It is presented as one point in a taxonomy with transparent trade-off discussion; calling it "not genuine watermarking" is a semantic argument, not a methodological flaw.

- **"Ignore prior prompts attack not evaluated in main text"**: REMOVED. The paper explicitly states in Section 5.2.2 that these results are in Appendix D.1. The paper also scopes out detailed attack analysis in Section 3.2 ("a detailed investigation of attack and defense methods is left for future work"). Deferring attack results to an appendix is standard practice.

- **"GPTZero baseline results absent from main results"**: REMOVED. GPTZero is listed as a baseline (Section 5.1) and the paper states results are in Appendix D.1. Not every baseline must appear in every table.

- **"LLM APIs may not preserve zero-font-size formatting"**: REMOVED as speculative — the paper does not need to verify API-level formatting support for a proof-of-concept exploration. Moved to Nice-to-Haves as a practical consideration.

- **"Missing related work on instruction-based steganography"**: REMOVED per guidelines (cannot verify existence of specific missing references without external knowledge).

- **Strength Finder: "ICW offers a promising direction for scalable content attribution"**: REMOVED. This is too generic and forward-looking; it describes future potential rather than an achieved contribution verified by the paper's experiments.

## Novel Insights

The paper's most genuinely novel observation is the empirical demonstration that watermarking through prompt engineering alone is not just theoretically possible but practically effective — provided the underlying LLM is sufficiently capable. The sharp capability threshold between GPT-4o-mini (ROC-AUC ≈ 0.57–0.91 for the linguistic methods) and GPT-o3-mini (ROC-AUC ≥ 0.995) suggests that instruction-following for watermarking is an emergent capability that appears only above some model scale. This has implications beyond watermarking: it indicates that as LLMs improve, a range of currently infeasible "prompt-only" interventions may become viable, potentially reshaping the relationship between model providers and third-party oversight mechanisms.

## Suggestions

- Add an experiment comparing watermarked LLM output against unwatermarked LLM output from the same model as the negative class. This is the highest-priority addition and would directly address the major weakness identified above.
- Specify the exact review-generation prompt Q and the source of human review negatives for the IPI setting in the main text.
- Discuss whether the Acrostics resampling procedure is conservative or anti-conservative under H₁, and consider alternative null estimation (e.g., resampling from a corpus of natural sentence-initial letters).
- Test ICW on at least one model from a different provider (Claude, Gemini, or Llama) to strengthen the "scales with capability" claim.
- Acknowledge the LLM-as-Judge evaluator bias in the interpretation of Table 3.

## Calibration

**Round 1 bracketing**: Placed ICW between 5.0 and 6.5 based on first-pass comparison with anchors.

**Anchors examined across both rounds**:

| Path | Avg Score | Round | Comparison to ICW |
|------|-----------|-------|-------------------|
| eKGEsFdpin ("I Know You Did Not Write That!") | 3.67 | R1 | ICW is clearly stronger — more novel idea, better evaluation |
| r6aX67YhD9 ("Learning to Watermark via RL") | 4.75 | R1 | ICW is stronger — cleaner methodology, more practical approach |
| 0koPj0cJV6 ("A Watermark for Black-Box Language Models") | 4.60 | R2 | ICW is stronger — truly prompt-only (no sampling intervention needed), better motivation |
| FDfq0RRkuz ("WASA") | 5.50 | R1 | ICW is comparable — both use Unicode approaches but ICW's non-Unicode methods are more practically useful |
| 1ou5noWgHM ("Source Attribution for LLM-Generated Data") | 5.40 | R2 | ICW is slightly stronger — more novel paradigm, better empirical demonstration |
| 9k0krNzvlV ("On the Learnability of Watermarks") | 5.75 | R2 | ICW is comparable — similar novelty level, both have some evaluation gaps; ICW's core idea is more creative but its evaluation is narrower |
| DEJIDCmWOz ("On the Reliability of Watermarks") | 6.00 | R1/R2 | ICW has a more novel core idea but narrower evaluation and more significant gaps; the Reliability paper's thorough evaluation places it slightly above ICW |

**Final score**: 5.5. The paper introduces a genuinely novel paradigm (prompt-only watermarking) with a well-structured taxonomy and compelling capability-dependence results, but two evaluation gaps — missing unwatermarked LLM baseline and model diversity — prevent it from reaching the 6.0 range. The paper is borderline; a strong rebuttal addressing these evaluation gaps could move it into accept territory.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>