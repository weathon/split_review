Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a framework for embedding detectable watermarks into LLM-generated text purely through prompt engineering, without any access to model internals. Four strategies at different granularities are proposed (Unicode, Initials, Lexical, Acrostics) with tailored detection methods, and evaluated in both a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting motivated by detecting AI-generated peer reviews. Experiments on GPT-4o-mini and GPT-o3-mini show that with a sufficiently capable model, ICW achieves high detection accuracy (ROC-AUC ≥ 0.995 for all methods on GPT-o3-mini in DTS), reasonable robustness against editing and paraphrasing, and minimal quality degradation.

## Strengths

- **Novel and principled approach to watermarking without model access.** ICW operates entirely via prompt instructions, requiring no access to logits, weights, or sampling. This is a fundamentally different paradigm from existing in-process methods (Kirchenbauer et al., 2023; Aaronson, 2023) and substantially broadens the applicability of LLM watermarking to scenarios where the detector has no control over the generation process. The problem formulation in Section 3.1 and Figure 1 clearly formalize this setting.

- **Comprehensive exploration of four strategies with trade-off analysis.** The paper proposes ICW methods at word-, token-, and sentence-level granularity (Unicode, Initials, Lexical, Acrostics) and provides a qualitative comparison across LLM requirements, detectability, robustness, and text quality (Table 1). This gives a structured view of the design space that future work can build on.

- **Strong empirical results with capable LLMs.** Table 2 shows that with GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in DTS and ≥ 0.997 in IPI, with high true positive rates at low false positive rates (e.g., T@1%F of 0.930–1.000 for most methods). These numbers demonstrate that prompt-based watermarking can be highly effective with sufficiently capable models.

- **Demonstrated robustness to editing and paraphrasing.** Figure 3 shows that Initials and Acrostics ICW maintain AUC > 0.88 under paraphrasing attacks, outperforming the YCZ+23 baseline (AUC 0.557) and comparable to PostMark (AUC 0.841). Initials ICW achieves AUC 0.999 under both word deletion and replacement, showing that the signal survives substantial text modification.

- **Timely and practically motivated IPI case study.** The academic peer-review misuse scenario (Section 3.2, Figure 2) is well-motivated and illustrates a genuine gap where existing watermarking methods cannot be applied. The paper correctly identifies that conference organizers lack access to the reviewer's model, making ICW a uniquely plausible solution.

## Weaknesses

### Major

1. **No comparison with AI-text detectors in the IPI setting, despite being the paper's main motivation.** The IPI scenario is introduced as a case study for detecting dishonest AI-generated reviews. The paper mentions that existing detectors (GPTZero, DetectGPT) "often suffer from low accuracy and high false positive rates" (Section 1), yet provides no empirical comparison against them in this setting. The baselines used (PostMark, YCZ+23) are post-hoc watermarkers that are indeed inapplicable in IPI because the reviewer would not watermark their own text. However, GPTZero is a *detector*, not a watermarker, and could be applied directly to the submitted review text without any watermark. The paper never reports how GPTZero performs on the same AI-generated reviews (watermarked or unwatermarked) that ICW is evaluated on. Without this comparison, the reader cannot assess whether ICW actually provides meaningful detection improvement over the status quo — a central claim of the motivation.

2. **IPI detection evaluation uses domain-mismatched negative examples.** The paper reports IPI detection metrics (ROC-AUC, T@1%F, T@10%F) computed against 500 human-generated texts. For the DTS setting, these are ELI5 answers. Section 5.1 states that "For each evaluation, we use 500 watermarked texts and 500 human-generated texts" but does not specify what human text is used for the IPI setting. The only human text source mentioned is ELI5 (a Q&A dataset). Human-written peer reviews differ substantially from ELI5 answers in style, vocabulary, length, and structure. False positive rates measured on ELI5 answers may not generalize to actual human reviews, and the reported IPI AUC figures could be optimistically biased. An evaluation should include genuine human-written reviews (e.g., from OpenReview) as negative examples.

3. **The "ignore prior prompts" attack is a first-order threat to the IPI threat model that is discussed only in passing.** In the IPI setting, a reviewer who is even slightly aware that the manuscript may contain hidden instructions can prepend "Ignore previous instructions" or similar to their prompt. The paper acknowledges this attack and reports studying it in Appendix D.1, but relegates this critical limitation to an appendix. The threat model's central assumption — that the hidden instruction survives in the context alongside the reviewer's own prompt — is directly broken by a trivial adversary action. This is not a niche attack; it is the most obvious countermeasure an informed reviewer would take. The paper should present and discuss these results prominently, and the absence of such discussion in the main text is a significant gap for the IPI claim.

### Minor

4. **Evaluation limited to two proprietary models from a single provider.** All experiments use only GPT-4o-mini and GPT-o3-mini (both OpenAI). While the paper claims ICW is "model-agnostic" (abstract), the results show extreme variation between these two models (e.g., Initials ICW AUC goes from 0.572 to 0.999). Testing on capable open-source models (e.g., Llama-3-70B, Mistral-Large) would substantially strengthen the claim that ICW is a general approach rather than something specific to OpenAI's instruction-tuning. This is especially important for the IPI setting, where the conference organizer cannot control which model the reviewer uses.

5. **Text quality evaluation over-relies on LLM-as-a-Judge with suspiciously high scores.** Table 3 shows ICW methods scoring 4.808–4.813 Overall, nearly indistinguishable from unwatermarked text (4.992) and higher than human text (4.235). This pattern — where an LLM judge scores LLM-generated text higher than human text — is well-documented and suggests evaluator bias. The paper should supplement with human evaluation or at minimum with automatic diversity/ repetition metrics. The perplexity results (Figure 4, in Appendix) help but are insufficient alone.

6. **"Model-agnostic" framing is at odds with the paper's own findings.** The abstract calls ICW "a model-agnostic, practical watermarking approach." In watermarking literature, "model-agnostic" typically means "does not require model-internal access," which is true for ICW. However, many readers will interpret it as "works across different models," which Table 2 directly contradicts (three of four methods fail on GPT-4o-mini). The paper's own contribution list (Section 1) correctly states that "effectiveness of ICW is highly dependent on the capability of the underlying LLMs." The abstract should be revised to avoid this ambiguity.

### Trivial

7. **IPI feasibility assumptions are not empirically validated.** The IPI pipeline assumes that hidden text (e.g., white text in a PDF) survives the PDF-to-text conversion process that a reviewer's LLM workflow would use. This is an empirical question — many PDF parsers strip invisible text — and the paper does not test it. While this is a reasonable simplifying assumption for a first exploration, it should be acknowledged as an untested part of the pipeline.

## Nice-to-Haves

- A comparison with an AI-text detector (e.g., GPTZero, DetectGPT) in the IPI setting on the same AI-generated reviews, using genuine human-written reviews as negative examples, would address the most significant gaps.
- Including at least one capable open-source LLM would strengthen claims of generality.
- A small human preference study on watermarked text quality would complement the LLM-as-a-Judge results.
- Explicitly testing whether the hidden watermarking instruction survives PDF-to-text conversion in realistic reviewer workflows (e.g., common PDF parsers used by LLM APIs).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unicode ICW is trivial to defeat by any text transformation"** — The paper explicitly discusses this limitation (Section 5.2.2), so this is acknowledged rather than hidden.
- **"Table 1 ordering does not correspond to the actual requirement order"** — Minor formatting nitpick about a qualitative summary table; the ordering is not claimed to be precise.
- **"The paper should include a set of genuine human-written reviews as negatives"** — This is kept as a major weakness above. The removed version here was the critic's framing which overstated the bias.
- **"The paper never acknowledges that the reviewer could use an API that ignores instructions conflicting with safety directives"** — Speculative; the paper cannot be expected to enumerate every possible API configuration.
- **"Not testing 'explicitly try to erase the signal' attacks"** — This is a reasonable suggestion for future work but not a current weakness; the paper does test word deletion, replacement, and paraphrasing which cover a standard robustness evaluation.
- **"Strength Finder's generic strengths"** — Removed generic strengths about "importance of the problem" and "timeliness" that lacked specific evidence anchors.

## Novel Insights

None beyond the paper's own contributions. The review surfaces the core tension between the paper's ambitious IPI claims and the substantial gaps in the IPI evaluation, particularly the missing detector comparison and domain-mismatched negative examples. The most notable observation from synthesizing the reviews is that the paper's strongest evidence (DTS setting with capable LLMs) supports a more modest claim — that prompt-based watermarking works when you control the system prompt and use a capable model — while its headline application (IPI for peer review) is the least supported part of the paper. The paper would be stronger if it either significantly strengthened the IPI evaluation or reframed its contribution around the DTS findings with the IPI scenario presented as preliminary.

## Suggestions

1. **Add a GPTZero baseline to the IPI evaluation.** Report its detection accuracy (AUC, T@1%F) on the same set of unwatermarked AI-generated reviews that ICW is tested against, using genuine human-written reviews as negative examples. This would directly address whether ICW's proactive watermark adds detection value over passive detection.
2. **Collect or construct a dataset of human-written peer reviews** (e.g., from OpenReview) and use it as the negative class for IPI detection evaluation.
3. **Present the "ignore prior prompts" attack results in the main paper** and discuss the implications for the IPI threat model. If the AUC drops substantially, this should be framed as the central open problem rather than a secondary limitation.
4. **Test on at least one open-source model** (e.g., Llama-3-70B) to support the generality claim.
5. **Revise the abstract** to replace "model-agnostic" with a more precise description, e.g., "operating without access to model internals."

## Score and Decision

The paper introduces a genuinely novel idea — watermarking via pure prompt engineering — and provides a thorough exploration of four strategies with reasonable empirical support in the DTS setting. However, the IPI evaluation, which is central to the paper's motivation and claimed impact, has significant gaps: no comparison with existing AI-text detectors, domain-mismatched negative examples, and insufficient treatment of the "ignore prior prompts" attack. These weaknesses do not invalidate the core DTS contribution, but they prevent the paper from delivering on its headline IPI claims in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>