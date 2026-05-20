Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for embedding watermarks into LLM-generated text purely through prompt engineering, without any access to model internals (weights, logits, or sampling). Four strategies (Unicode, Initials, Lexical, Acrostics) are proposed with tailored detection methods. The paper evaluates these in a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting motivated by detecting AI-generated peer reviews. Experiments on GPT-4o-mini and GPT-o3-mini show that with sufficiently capable models, ICW achieves strong detection accuracy, robustness, and text quality.

## Strengths

1. **Prompt-only watermarking is a genuinely novel paradigm.** Existing watermarking methods require either in-process access (logits/sampling) or post-hoc text modification. ICW demonstrates that watermarks can be embedded solely through instruction following, which opens a new research direction. This is a clean conceptual contribution with clear practical motivation.

2. **Strong empirical results on capable LLMs.** Table 2 shows that with GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in both DTS and IPI settings, with near-perfect detection rates (e.g., Acrostics ICW ROC-AUC 1.000, T@1%F 1.000). These results convincingly demonstrate feasibility.

3. **First work to enable watermarking in the Indirect Prompt Injection scenario.** The IPI setting (Section 3.2) is a genuinely novel application where neither in-process (no model access) nor post-hoc (no reviewer incentive) methods can operate. The paper demonstrates detection performance in this setting (e.g., Acrostics ICW ROC-AUC 0.997, T@1%F 0.982), showing the practical relevance of the paradigm.

4. **Superior robustness to paraphrasing vs. post-hoc baselines.** Under paraphrase attack (Figure 3), Initials ICW (AUC 0.887), Lexical ICW (AUC 0.924), and Acrostics ICW (AUC 0.922) all outperform YCZ+23 (0.557) and PostMark (0.841), a practically important result since paraphrasing is a common evasion strategy.

5. **Minimal impact on text quality.** LLM-as-a-Judge evaluation (Table 3) shows ICW responses scoring 4.28–4.81 (out of 5) overall, comparable to unwatermarked text (4.99) and substantially better than PostMark (3.00), demonstrating that the watermarking does not degrade response quality.

## Weaknesses

### Fatal
None.

### Major

1. **Only two models from a single provider are tested.** The paper evaluates on GPT-4o-mini and GPT-o3-mini — both OpenAI models with similar architectural lineage. The central claim that "as LLMs become more capable, ICWs will become correspondingly more powerful" (Section 1, line 45) rests on this single comparison (2 data points, same lineage). Without testing on non-OpenAI models with strong instruction-following (e.g., Claude 3.5 Sonnet, Gemini 2.0, Llama-3), the evidence is only suggestive. The paper would benefit from tempering this generalizability claim or adding at least one additional model from a different provider.

### Minor

2. **Acrostics ICW detection method is underspecified.** The detection procedure (Section 4.2.4, line 182) states: "we randomly resample N sequences of sentence initial letters (ℓ̃₁, ..., ℓ̃_N) from the suspect text" to estimate the null distribution parameters. The paper does not specify *how* resampling is performed (e.g., random permutation vs. bootstrap with replacement), which matters for the statistical validity of the z-test. While the watermark signal is so strong (AUC=1.000) that the core empirical finding is robust, the detection procedure as described is not reproducible. The specification should be clarified or corrected.

3. **The IPI setting lacks a practical feasibility demonstration for covert embedding.** The paper proposes hiding watermarking instructions as invisible text (e.g., white text, zero-font-size) in PDF manuscripts, but provides no experiment showing that such instructions survive realistic document processing (PDF-to-text extraction, copy-paste, LLM document parsers). This is acknowledged as future work (Section 3.2, line 106), but the gap between the motivating use case and the experimental validation limits the practical claim.

4. **No confidence intervals or error bars.** All reported detection metrics (AUC, T@1%F, T@10%F) and text quality scores are point estimates without uncertainty quantification (standard errors or confidence intervals). Given the 500-sample evaluation, bootstrapped confidence intervals would be straightforward and informative.

### Trivial
- The paper does not report false positive rate calibration for Acrostics ICW on unwatermarked text. Theoretical guarantees are provided for Initials and Lexical ICWs (Appendix B) but not for Acrostics, leaving an empirical gap.

## Nice-to-Haves
- Testing on at least one non-OpenAI model (e.g., Claude 3.5 Sonnet or Gemini 2.0) would substantially strengthen the generalizability claim.
- A simple sanity-check experiment for IPI: embed an instruction as invisible text in a PDF, extract via common PDF readers/pipelines, and verify the instruction is preserved.
- Discussion of computational/context overhead (Lexical ICW's large green word list consumes prompt capacity).
- The "ignore prior prompts" attack analysis is deferred to Appendix D.1; including the key finding in the main text would help the reader assess the IPI threat model.

## Removed Points
These points were flagged by reviewers but are removed with justification:

- **Harsh Critic's claim that Acrostics detection is "structurally flawed" and the null distribution is "contaminated"**: This claim assumes resampling preserves watermark structure rather than breaking it. The paper does not specify the resampling method, making the criticism speculative rather than verifiable. The near-perfect detection results (AUC=1.000) demonstrate the watermark is trivially detectable regardless of the exact test calibration. Downgraded to Minor (underspecification).

- **Harsh Critic's point about IPI robustness not shown in main text (relegated to Appendix)**: The paper shows DTS robustness in the main text (Figure 3) and IPI robustness in the appendix (Table 6). This is a presentation choice, not a weakness.

- **Strength Finder's claim about "Clear scaling with model capability"**: While the data shows improvement from GPT-4o-mini to GPT-o3-mini, this is only two models from one provider. The strength is real but tempered by the limited data; the Major weakness above captures the limitation.

- **Strength Finder's generic strengths about "important problem" and "timely topic"**: Removed as superficial/generic per filtering rules.

## Novel Insights

The most interesting insight from these reviews (beyond the paper's own contributions) is the tension between the paper's novelty and its thin empirical base. The ICW paradigm is genuinely new — it shifts watermarking from a model-access problem to an instruction-following problem — yet the central claim about scaling with model capability is supported by only two data points from one model family. This points to a broader question for the field: how should reviewers weigh high conceptual novelty against limited empirical scope in a paper that explicitly frames itself as an "initial exploration"?

## Suggestions
1. Clarify the Acrostics resampling procedure — specify whether it is a permutation test or another method, and provide empirical FPR calibration on unwatermarked text.
2. Add at least one non-OpenAI model (e.g., Claude 3.5 Sonnet or Gemini 2.0) to demonstrate that the findings are not vendor-specific.
3. Run a simple end-to-end IPI sanity check: embed an invisible instruction in a PDF, extract via common pipelines, and verify the instruction survives.
4. Add bootstrapped confidence intervals to the main detection results (Table 2).
5. Soften the generalization claim about "as LLMs become more capable" to acknowledge the limited evidence base.

## Score and Decision

**Round 1 bracket:** After reading the paper and comparing to calibration anchors, I estimate the paper sits between 4.5 and 6.5. It is clearly stronger than PromptHash (3.00, Reject) and dMARK (3.33, Reject) due to higher novelty and clearer presentation. It is comparable to PRO (5.00, Reject), OpenStamp (5.00, Reject), and CATMark (5.33, Reject) — these papers have similar methodological quality but less novelty. It is weaker than PMark (7.00, Accept Poster) and LLM Fingerprinting via Semantically Conditioned Watermarks (6.50, Accept Oral), which have more thorough evaluations and stronger theoretical foundations.

**Round 2 narrowing:** Focusing on the 4.5–6.5 bracket, I compared the paper against:
- **PRO (5.00, Reject)**: ICW has higher novelty (new paradigm vs. incremental improvement on existing paradigm) but PRO has more thorough robustness evaluation across multiple models. ICW is slightly stronger overall.
- **CATMark (5.33, Reject)**: CATMark has strong cross-task experiments but incremental novelty. ICW has higher novelty but thinner evaluation. Comparable quality.
- **LLM Fingerprinting (6.50, Accept Oral)**: This paper evaluates across multiple models, multiple attack settings, and has a more thorough empirical foundation. ICW is clearly weaker than this anchor.
- **PMark (7.00, Accept Poster)**: Strong theoretical framework (proxy functions, distortion-free guarantees) and thorough experiments. ICW has higher conceptual novelty but weaker theory and evaluation. ICW is clearly weaker.

The paper's high novelty is its strongest asset, but the limited model coverage (2 models, 1 provider) and the underspecified Acrostics detection method prevent it from reaching the 6.5+ range of accepted watermarking papers. It sits above the 5.0–5.33 rejected papers due to its genuinely new paradigm.

**Final calibration against anchors:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| PromptHash | 3.00 | 1 | ICW is stronger — better presentation, more convincing experiments |
| dMARK | 3.33 | 1 | ICW is stronger — clearer contribution, better evaluation |
| PRO | 5.00 | 1, 2 | ICW is slightly stronger — higher novelty but thinner evaluation |
| OpenStamp | 5.00 | 1 | ICW is slightly stronger — higher novelty |
| Detecting Benchmark Contamination | 5.00 | 2 | ICW is similar — both have clear novelty and reasonable but limited evaluation |
| CATMark | 5.33 | 2 | ICW is comparable — different tradeoffs in novelty vs. evaluation breadth |
| LLM Fingerprinting | 6.50 | 1, 2 | ICW is weaker — less thorough evaluation, more limited model coverage |
| PMark | 7.00 | 2 | ICW is weaker — PMark has stronger theory and more thorough evaluation |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>