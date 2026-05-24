Now I have all the information needed. Let me compose the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces In-Context Watermarking (ICW), a method to watermark LLM-generated text solely through prompt engineering — without any access to model internals, logits, or decoding process. It proposes four strategies (Unicode, Initials, Lexical, Acrostics) at different linguistic granularities, each with a tailored detection algorithm, and evaluates them in both a direct text stamping (DTS) setting and an Indirect Prompt Injection (IPI) scenario motivated by detecting AI-generated peer reviews.

## Strengths

- **Near-perfect detection without model access (Table 2):** With GPT-o3-mini, three of the four ICW strategies achieve ROC-AUC ≥ 0.995 and T@1%F ≥ 0.93 in the DTS setting, with several entries at 1.000. This provides strong evidence that watermarking via prompt engineering alone can match the detection accuracy of methods requiring access to the decoding process, for sufficiently capable models.

- **First formulation and evaluation of watermarking in the IPI setting (Section 3.2, Table 2):** The paper is the first to define the Indirect Prompt Injection watermarking scenario and evaluate it. All four ICW methods achieve AUC ≥ 0.997 with GPT-o3-mini in IPI — a capability that existing in-process watermarking cannot provide because conference organizers have no control over the LLM used by reviewers.

- **Stronger robustness to paraphrasing than post-hoc baselines (Figure 3):** Under a paraphrase attack, Initials, Lexical, and Acrostics ICWs maintain AUC ≥ 0.887, whereas the post-hoc baselines YCZ+23 and PostMark drop to 0.557 and 0.841 respectively. This demonstrates that prompt-based watermarking can survive transformations that cripple existing black-box approaches.

- **Higher text quality than the PostMark baseline (Table 3):** ICW methods achieve overall LLM-as-a-Judge scores ≥ 4.28 (out of 5), while PostMark scores 2.997. The paper thus demonstrates that prompt-based watermarking can embed a detectable signal with much less degradation to fluency and relevance than a popular post-processing alternative.

- **Systematic exploration of strategies across linguistic granularities (Table 1, Section 4):** The paper characterizes four strategies along LLM requirements, detectability, robustness, and text quality, providing practitioners with a principled framework for selecting a scheme based on their constraints.

## Weaknesses

### Major

- **Missing control: detector performance on unwatermarked LLM output vs. human text (Section 5.1, Table 2).** The detection experiments (Table 2) compare watermarked LLM output against human text only. For Initials and Lexical ICWs, the detector's z-statistic assumes the null distribution matches human-written text (e.g., initial-letter distribution from Canterbury Corpus for Initials ICW, uniform word-list proportion for Lexical ICW). If GPT-o3-mini naturally produces text with different initial-letter frequencies or word-choice distributions than humans (which is plausible given LLM output biases), the reported AUCs could partially reflect inherent LLM–human differences rather than the watermark instruction's effect. For example, Initials ICW with GPT-4o-mini gives only AUC 0.572 — barely above chance — suggesting the detector's signal is dominated by instruction-following. But without the unwatermarked LLM control, we cannot quantify how much of GPT-o3-mini's 0.999 AUC comes from the instruction vs. inherent output properties. This specifically threatens the interpretability of Initials and Lexical ICW results; Unicode ICW (detecting specific inserted characters) and Acrostics ICW (using self-resampling of sentence initials) are less affected.

- **Claims of "model-agnostic" generalizability are unsupported by the experimental scope (Abstract, Section 5.1).** The abstract claims ICW is "model-agnostic" and "practical," but experiments are limited to two proprietary OpenAI models (GPT-4o-mini and GPT-o3-mini). The method is not tested on any other model family (e.g., Llama-3, Claude, Gemini), and the paper shows that with a less capable model (GPT-4o-mini), three of the four strategies essentially fail (AUC 0.572–0.910 in DTS). The term "model-agnostic" is misleading; the method is better described as "model-capability-dependent." Testing on at least one open-weight model and one alternative proprietary model would be needed to support the generalizability claim.

- **The IPI setting lacks evaluation of realistic document-handling pipelines (Section 3.2).** The proposed threat model involves embedding hidden instructions via white text or zero-width characters in PDF manuscripts, then relying on reviewers to copy-paste the full PDF into an LLM. Practical challenges are not evaluated: (1) PDF text extraction quality varies across tools (some strip invisible text), (2) copy-paste workflows may not transfer hidden characters, and (3) reviewers might only paste visible excerpts. Without validating the survival rate of the hidden instruction through realistic pipelines, the IPI scenario remains speculative.

### Minor

- **Acrostics ICW detection lacks a formal false-positive guarantee (Section 4.2.4).** Unlike Initials and Lexical ICWs (which provide theoretical false-alarm control via z-statistics, Section 4.2.2–4.2.3, Appendix B), Acrostics ICW uses a resampling-based z-score with estimated mean and variance. No calibration analysis or theoretical false-positive bound is provided. Given that Acrostics achieves perfect detection (AUC 1.000, T@1%F 1.000), this is not an empirical concern for the current results, but the lack of formal analysis weakens the method's statistical grounding.

- **LLM-as-a-Judge evaluation uses Gemini 2.0 to judge OpenAI model outputs (Table 3).** The "Unwatermarked" row shows near-perfect scores (Relevance 4.982, Quality 5.000, Clarity 4.994). These ceiling effects raise the possibility that the judge (Gemini 2.0) is biased toward outputs from its own or similar model families, or that the evaluation prompt is not sufficiently discriminative. While the relative ranking across methods may still be informative, the absolute quality scores should be interpreted cautiously.

- **Lexical ICW's robustness under word replacement drops substantially (Figure 3, AUC 0.758).** The paper correctly attributes this to the fact that the replacement procedure targets adjectives/verbs/adverbs — the same word classes the detector relies on. This is transparently reported, but it reveals a fundamental design tension worth noting: by restricting the green list to content words that are likely targets of editing/paraphrasing, the method creates a built-in vulnerability that the attacker can exploit without knowing the specific green words.

### Trivial

- None that warrant listing.

## Nice-to-Haves

- Evaluate at least one open-weight model (e.g., Llama-3-70B) to test whether ICW generalizes beyond OpenAI's API, supporting the claimed model-agnosticism.
- Add a direct comparison of detector behavior on unwatermarked LLM output vs. human text — this would cleanly separate the watermark contribution from inherent LLM biases.
- Test the IPI setting with realistic PDF extraction and copy-paste pipelines to validate the threat model's practical viability.
- Provide a formal false-positive analysis for the Acrostics detection statistic.

## Removed Points

These points from the reviews were excluded after verification:

- *Criticism about missing "ignore prior prompts" results in the appendix (Table 7):* The parser strips appendix content from all papers; these results exist in the original submission. Removed per hard rule about missing appendix content.
- *Claim that Section 6's fine-tuning suggestion contradicts the "no model access" claim:* The paper presents this as a future direction for LLM providers to improve ICW support — not as a requirement of the current method. This is not a contradiction; it is an orthogonal improvement path. Removed.
- *Criticism about comparison to PostMark/YCZ+23 being "misleading":* The paper explicitly states these are "post-processing approaches that embed watermarks into already generated text" (Section 5.1). The comparison is transparent and useful as a detection-performance benchmark. Removed.
- *"Major LLM providers do not publicly use watermarks" is not referenced:* This is a statement of common knowledge, not a factual claim requiring citation. Removed.
- *Table 1 filled/unfilled circles are "vague":* The paper explicitly states "Darker circles indicate higher values, offering an intuitive illustration of the trade-offs." This is a visual summary, not a precision instrument. Removed as a formatting nitpick.
- *Acrostics vulnerability to spoofing if key is known:* The paper already acknowledges this vulnerability for Initials ICW explicitly (Section 4.2.2 Discussion). The criticism does not add new information. Removed.
- *Strength Finder's generic/superficial strengths:* The strength "this paper addressed an important problem" and similar generic statements were removed as they lack specific evidence anchored to the paper's content. Only concrete, verifiable strengths were retained.

## Novel Insights

The most interesting observation across the reviews is that the paper establishes an approximate "capability threshold" for watermarking via prompt engineering: with GPT-4o-mini, Initials and Acrostics ICWs barely work (AUC ~0.57–0.59), while on GPT-o3-mini they jump to near-perfect (0.995–1.000). This suggests a step-function relationship between instruction-following ability and ICW effectiveness, rather than a smooth improvement curve. If this threshold can be characterized across more models and instruction complexities, it would provide a practical guide for when ICW becomes viable. The other notable observation is that Acrostics ICW's self-resampling detection makes it uniquely robust to the "missing control" problem — because the null distribution is estimated from the suspect text's own sentence-initial statistics, the detection is inherently calibrated to the text's own properties rather than to an external human-text distribution.

## Suggestions

1. Add a dedicated experiment comparing watermarked LLM output vs. unwatermarked LLM output (both from the same model, same domain) against human text. This is the single most impactful addition: it separates the watermark signal from any inherent LLM–human distributional differences.
2. Replace the term "model-agnostic" with more precise language (e.g., "model-access-free" or "prompt-based") and qualify generalizability claims to acknowledge the experimental scope.
3. For the IPI setting, include a small but concrete test of whether the hidden instruction survives realistic PDF → text → LLM pipelines (e.g., pdftotext extraction, copy-paste from a PDF viewer).
4. Provide a theoretical false-positive bound for the Acrostics detection statistic, or at minimum a calibration plot showing empirical vs. nominal FPR.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>