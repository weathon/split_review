## Summary

This paper introduces **In-Context Watermarking (ICW)**, a family of prompt-engineering-based watermarking techniques that embed detectable signals into LLM-generated text without requiring any access to the model's decoding process. The authors propose four strategies at different granularity levels (Unicode insertion, Initials bias, Lexical word-list bias, and Acrostics/sentence-initial-letter encoding) and evaluate them in two settings: a Direct Text Stamp (DTS) system-prompt scenario and an Indirect Prompt Injection (IPI) scenario targeting AI-generated academic peer reviews. The key thesis is that as LLMs grow more capable at following instructions, ICW becomes proportionally more effective.

---

## Strengths

- **Novel, practically motivated problem formulation.** The gap between "watermarking that needs decoding access" and "watermarking that can be applied by a third party who only has API access" is real and underexplored. The IPI peer-review scenario is a compelling, timely concrete instantiation of a broader challenge.
- **Well-designed spectrum of strategies.** The four ICW methods cover a principled design space (character → word-initial → word → sentence level), each paired with a tailored detection statistic (ratio test, z-score from Canterbury Corpus baseline, Levenshtein z-score). The theoretical false-alarm guarantees for Initials and Lexical ICW add rigor.
- **Strong empirical results with GPT-o3-mini.** On the more capable model, all four ICW methods reach ROC-AUC ≥ 0.995 in both DTS and IPI settings (Table 2), and maintain high AUC under 30% word deletion, synonym replacement, and LLM paraphrasing (Figure 3). Text quality (Table 3) is largely preserved—ICW methods score substantially higher than PostMark on LLM-as-a-Judge and preserve perplexity.
- **IPI results transfer well from DTS.** Table 2 shows only marginal degradation when going from the system-prompt setting to the long-context IPI paper-review setting, validating that LLMs can act on injected instructions even buried in full research manuscripts.
- **Honest capability dependency analysis.** The paper clearly documents that GPT-4o-mini largely ignores the more demanding instructions (Initials/Acrostics AUC ≈ 0.57–0.59, near-random), and frames this as a feature—effectiveness scales with model capability—rather than concealing it.

---

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation limited to two same-family proprietary models.** The entire experimental section uses GPT-4o-mini and GPT-o3-mini exclusively. The paper's central claim of being "model-agnostic" is not empirically validated on any non-OpenAI model (e.g., Claude, Gemini, Llama, Mistral). The capability-scaling argument rests on a single vendor's product line, making it unclear whether the findings transfer to instruction-tuned open-source models or competing proprietary APIs.

2. **Table 1's qualitative summary contradicts the quantitative results.** Table 1 assigns equal "filled circle" ratings for Detectability, Robustness, and Text Quality to Initials, Lexical, and Acrostics ICW—yet Table 2 shows Initials and Acrostics achieving AUC ≈ 0.57–0.59 on GPT-4o-mini, effectively indistinguishable from random. The summary table is misleading and could cause readers to overestimate the reliability of these methods on typical production-grade models.

3. **IPI injection mechanism is described but not fully validated.** The paper states that "white text" or zero-font-size embedding can hide the watermarking instruction in a PDF, but the experiments use full text as input rather than testing the actual PDF-level steganography pathway. It is unclear whether the injected instruction would survive realistic PDF-to-text extraction pipelines (e.g., those used by commercial LLM file-upload interfaces), which often strip invisible or zero-font text during OCR or PDF parsing. This gap matters critically for the IPI setting's practical claims.

### Minor

1. **Spoofing vulnerability of Initials ICW acknowledged but not analyzed.** The paper notes that the green-letter set can be inferred from the output distribution. A quantitative analysis of how many observed tokens are needed to recover the key—and how this affects practical security—would strengthen the discussion.

2. **IPI robustness results deferred entirely to the appendix.** Since the IPI setting is the paper's most novel application, the robustness evaluation for that setting (Table 6) should appear in the main text alongside Figure 3.

3. **No minimum-capability threshold identified.** The dramatic flip between GPT-4o-mini (near-random for Initials/Acrostics) and GPT-o3-mini (near-perfect) is interesting, but the paper provides no analysis or characterization of what capability threshold is required—making it hard to know which currently available models would support ICW deployment.

### Trivial

- The watermarking instruction examples truncated to "abbreviated" forms are fine for exposition, but readers cannot verify prompt sensitivity without the full prompts (referenced to the appendix, which is unavailable due to parser stripping).

---

## Nice-to-Haves

- An experiment with at least one open-source model (e.g., Llama-3.1-70B, Mistral-Large) to demonstrate cross-vendor generality.
- A concrete PDF-injection experiment confirming that the instruction survives a typical PDF upload pipeline.
- An analysis of the minimum output length needed to achieve a given TPR at 1% FPR, which would guide practitioners.
- Quantification of false positive risk in the IPI/peer review scenario at scale (if conference X receives 10,000 reviews, how many innocent reviewers are falsely flagged at T@1%F?).

---

## Novel Insights

The most genuinely novel observation is the adversarial repurposing of indirect prompt injection as a *pro-social* tool: the same mechanism typically used by malicious actors to hijack LLM behavior is turned into a provenance-tracking channel by a trusted authority (the conference organizer). This reversal of the IPI threat model—from attacker-plants-instruction to defender-plants-instruction—opens an underexplored design space. Additionally, the empirical finding that sentence-level acrostics are more robust to paraphrasing than word-level lexical watermarks (because paraphrasing preserves paragraph structure while changing word choice) is a practically useful insight about the robustness-granularity trade-off in linguistic steganography.

---

## Suggestions

- **Broaden model evaluation**: Test at minimum one open-source instruction-tuned model and one non-OpenAI proprietary API (e.g., Claude Sonnet, Gemini Pro) to support the model-agnosticism claim.
- **Validate the PDF injection pipeline end-to-end**: Use actual white-text PDFs, upload them through a commercial API's file-upload interface, and report whether the watermarking instruction is actually followed in the output.
- **Fix Table 1**: Use a finer scale or add a footnote clarifying that ratings are conditional on using a sufficiently capable LLM; otherwise the table is actively misleading.
- **Include a brief security analysis of key recovery**: Estimate the number of watermarked tokens needed to reliably recover the Initials or Lexical key, to characterize the spoofing attack surface quantitatively.

---

## Score and Decision

The paper introduces a clearly motivated, novel problem formulation and provides a well-organized initial exploration with principled detection methods and solid results on GPT-o3-mini. The limiting factor is the narrow two-model, one-vendor evaluation for a paper that claims model-agnosticism as a central selling point, and the gap between the described IPI deployment mechanism and what is actually tested. These are significant but not fatal for an exploratory contribution at this stage.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>