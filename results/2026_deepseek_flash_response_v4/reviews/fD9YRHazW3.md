Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for embedding detectable signals into LLM outputs purely through prompt engineering, without any access to the model's decoding process, logits, or sampling mechanism. Four ICW strategies (Unicode, Initials, Lexical, Acrostics) are proposed across different linguistic granularities, each with tailored detection methods. Experiments in both Direct Text Stamp (DTS) and Indirect Prompt Injection (IPI) settings show that with sufficiently capable LLMs (GPT-o3-mini), ICW achieves high detection accuracy (ROC-AUC ≥ 0.995) and strong robustness to paraphrasing, while maintaining text quality superior to post-hoc black-box baselines.

## Strengths

- **Novel paradigm requiring no decoding access**: Unlike all existing in-process watermarking methods (Kirchenbauer et al., 2023; Aaronson, 2023) that require logits or sampling-process access, ICW operates purely through prompt engineering. This is validated across both DTS and IPI settings in Table 2 — a capability no prior watermarking method provides, since existing methods require model access that conference organizers or third parties lack.

- **Concrete and timely application in IPI setting**: The IPI scenario (Section 3.2) addresses the specific problem of detecting LLM-generated peer reviews, where conference organizers cannot access the reviewer's model. Table 2 shows GPT-o3-mini achieves ROC-AUC ≥ 0.997 for all ICW methods under IPI, with T@1%F ranging from 0.910 to 1.000 — providing direct evidence that the approach works when the instruction is present in the input the LLM processes.

- **Text quality substantially better than black-box-compatible baselines**: Table 3 shows ICW methods achieve LLM-as-a-Judge overall scores of 4.282–4.813, far exceeding PostMark (2.997) and YCZ+23 (3.865), and approaching unwatermarked text (4.992) and human text (4.235).

- **Robustness to paraphrasing that matches or exceeds post-hoc baselines**: Under LLM-based paraphrasing attacks (Figure 3), Initials (AUC=0.887), Lexical (AUC=0.924), and Acrostics (AUC=0.922) ICW all outperform YCZ+23 (0.557) and PostMark (0.841), showing that semantic-level ICW strategies survive text regeneration that would remove character-level signals.

- **Systematic design space across four levels of granularity**: The four strategies (Unicode char-level, word-initial-letter, full-word lexical, sentence-level acrostics) in Section 4, summarized in Table 1, systematically cover different trade-offs among LLM requirements, detectability, robustness, and text quality — offering a structured taxonomy for future work.

## Weaknesses

### Major

- **IPI pipeline not tested end-to-end**: The paper's flagship application — embedding watermark instructions via white/transparent text in PDFs (Section 3.2, line 89) — is not tested through the actual deployment pipeline. The IPI experiments supply the watermarking instruction directly in the LLM input text, not through PDF embedding and extraction. While the paper notes these obfuscation methods "have been extensively explored in many prompt injection attacks" (line 95), no experimental validation that the instruction survives PDF-to-text extraction is provided. This gap between the motivating scenario and the tested setup undercuts the central application.

- **ICW fails entirely on 3/4 strategies with a capable-but-not-frontier model**: Table 2 shows that Initials ICW (AUC=0.572, T@1%F=0.006) and Acrostics ICW (AUC=0.590, T@1%F=0.036) are essentially random detectors with GPT-4o-mini, and Lexical ICW (AUC=0.910, T@1%F=0.320) is substantially degraded. Only Unicode ICW works well across both models. This means ICW's viability is currently limited to the most capable (and expensive) proprietary models. The paper is transparent about this dependency, but the abstract's claim of "a model-agnostic, practical watermarking approach" (line 9) is at odds with results showing heavy model-specificity.

- **No statistical uncertainty reported**: All detection metrics (Table 2, Figure 3) are reported as point estimates without confidence intervals, standard errors, or significance tests. Given that T@1%F is defined by only ~5 false positives out of 500, these estimates are noisier than they appear, making it impossible to assess whether fine-grained differences between methods are meaningful.

- **Spoofing vulnerability for Initials ICW acknowledged but unpursued**: The paper states that "the green letter set A_G can be easily inferred, making the method vulnerable to spoofing attacks" (line 148) and that defensive strategies are left for future work (line 101). For a method whose value proposition is attribution and accountability, this is a first-order security concern. The "ignore prior prompts" attack results are tested but deferred entirely to the Appendix.

### Minor

- **Only OpenAI models tested**: ICW is evaluated on only two models (GPT-4o-mini, GPT-o3-mini), both from the same provider and API family. Without testing on at least one non-OpenAI model (e.g., Claude, Gemini, or an open-weight model), it is unclear whether the results reflect general instruction-following capability or idiosyncrasies of OpenAI's instruction-tuning. The paper's central finding — that ICW works on sufficiently capable models — would be significantly strengthened by cross-model validation.

- **LLM-as-a-Judge evaluation may suffer from ceiling effects**: The Unwatermarked GPT-o3-mini condition achieves near-perfect scores (4.982–5.000/5.0) across all dimensions (Table 3), suggesting the evaluator (gemini-2.0-flash) is not discriminating well at the high end. This could mask subtle quality degradation from watermarking.

- **Statistical null for Initials ICW estimated from general-domain corpus**: The distribution of initial letters is estimated from the Canterbury Corpus (Section 4.2.2, line 146), which may differ from domain-specific text like academic reviews. This could affect false positive rate calibration in the IPI setting, though the practical impact is likely small.

### Trivial

None.

## Nice-to-Haves

- Testing ICW on at least one non-OpenAI model family to establish generality.
- End-to-end IPI evaluation simulating the full PDF embedding → extraction pipeline.
- Bootstrap confidence intervals or standard errors for detection metrics, especially T@1%F.
- A table showing where Unicode ICW breaks under specific transformations, analogous to how Figure 3 handles the other three methods.
- A discussion of whether the detector would need to know which ICW scheme was used when the scheme is unknown, or whether a combined detection strategy could be designed.

## Removed Points

These points are flagged to be removed, treat them with caution:

**From Harsh Critic:**
- The claim that "major LLM providers do not publicly use watermarks" was presented "as fact without citation" — the paper actually includes the qualifier "to our knowledge" (line 17), so this is a misreading. **Removed.**
- The assertion that ICW's capability-dependence claim is "not a demonstrated property" but "an appeal to future progress" — Table 2 directly demonstrates the capability dependency with two models, so the dependency claim is empirically supported. The paper's speculation about future improvement is clearly separated from the demonstrated result. **Removed.**
- The criticism that "detection is not attribution" broadly applied to all ICW methods — this conflates Initials ICW (where the concern is partially valid) with Lexical and Acrostics ICWs (where the secret key/word list is not easily inferable from output alone). **Removed as overgeneralization; the specific spoofing concern for Initials ICW is kept in Weaknesses.**
- The criticism about the detector needing to know the scheme type — this is by design in the problem formulation (Section 3.1), where both k and τ are shared with the detector, which is standard for symmetric watermarking. **Removed.**

**From Strength Finder:**
- None removed. All listed strengths are concrete, specific to the paper, and supported by evidence.

## Novel Insights

The reviews collectively surface one observation that goes beyond the paper's own framing: the paper's most valuable contribution may not be a production-ready watermarking system, but rather the empirical mapping of the boundary where in-context watermarking transitions from non-functional to highly effective as LLM capability increases (the GPT-4o-mini vs. GPT-o3-mini gap in Table 2). This suggests ICW could serve double duty as both a watermarking method and a behavioral probe for instruction-following capability — a model that can reliably execute Complex Lexical ICW across many generations demonstrates a degree of in-context learning that may correlate with other advanced capabilities. This framing reframes the paper's central limitation (model-specificity) as a feature that future work could exploit.

## Suggestions

1. **Add an end-to-end IPI experiment** that simulates the full pipeline: embed a watermarking instruction in a PDF via white/transparent text, extract text via standard PDF-to-text tools, feed to an LLM for review generation, and measure watermark detectability. This is the single highest-leverage experiment to support the paper's motivating scenario.
2. **Test on at least two non-OpenAI models** (e.g., Claude 3.5 Sonnet, Gemini 2.0 Flash, or Llama 3 70B) to establish whether ICW's effectiveness generalizes across model families or is specific to OpenAI's instruction-tuning.
3. **Add bootstrap confidence intervals** for all detection metrics, especially T@1%F where the small number of false positives makes point estimates noisy.
4. **Move the "ignore prior prompts" attack results** from the Appendix into the main body, as they are directly relevant to the IPI threat model.
5. **Validate the null distribution for Initials ICW** on review-domain text rather than relying solely on the general-domain Canterbury Corpus, to tighten the connection between the statistical test and the IPI application.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jbfDg4DgAk.md (Sparse Watermarking) | 3.00 | R1 | Much weaker — less novel, less thorough evaluation |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/xRi8sKo4XI.md (Unsupervised Prompt Learning) | 3.00 | R1 | Different topic, not directly comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/eKGEsFdpin.md (Sampling Watermarking) | 3.67 | R1 | Weaker — less novel, less rigorous evaluation |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/0koPj0cJV6.md (Black-Box Watermark) | 4.60 | R2 | Most comparable anchor — both propose black-box watermarking. ICW has greater paradigm novelty but less theoretical analysis and narrower evaluation. ICW is slightly better. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/r6aX67YhD9.md (Learning to Watermark via RL) | 4.75 | R1 | Comparable — both have notable limitations but ICW's paradigm is more novel. Slightly better. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/0KHW6yXdiZ.md (End-to-End Logits Watermarking) | 5.25 | R2 | Comparable — more thorough evaluation across 3 LLMs, but uses a less novel logits-based approach |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/6p8lpe4MNf.md (Semantic Invariant Watermark) | 5.50 | R1 | Stronger — accepted paper with theoretical analysis and more thorough evaluation |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FDfq0RRkuz.md (WASA) | 5.50 | R1 | Stronger — more comprehensive evaluation and well-scoped setup |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DEJIDCmWOz.md (On Reliability of Watermarks) | 6.00 | R2 | Different type of contribution (empirical study, not new method), higher quality |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/j7b4mm7Ec9.md (Lightweight Deep Watermarking) | 7.60 | R1 | Different domain (image watermarking), much higher quality |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jOmk0uS1hl.md (Training on Test Task) | 8.00 | R1 | Different topic, much higher quality |

**Round 1 bracket:** The paper sits between the weak anchors (3.0–3.67) and strong anchors (7.6–8.0). Narrowest plausible range: 4.0–6.0.

**Round 2 narrowing:** Compared against directly comparable anchors (Black-Box Watermark at 4.60, Learning to Watermark at 4.75, End-to-End Logits at 5.25, Semantic Invariant at 5.50, WASA at 5.50), the ICW paper is slightly better than the 4.6–4.75 papers (due to greater paradigm novelty) and weaker than the 5.5 papers (due to narrower evaluation and no theoretical analysis). This places it at approximately **5.0**.

**Final Score:** 5.0

**Decision:** Reject. The paper introduces a genuinely novel and interesting paradigm for LLM watermarking. However, the current evaluation has three verifiable gaps that prevent acceptance: (1) the flagship IPI application is not tested end-to-end through the actual PDF embedding/extraction pipeline, (2) ICW is only validated on two models from one provider, with 3/4 methods failing on the less capable model, and (3) no uncertainty quantification is provided for any detection metric. These are fixable with additional experiments, and the core idea is promising enough to warrant further development. With cross-model validation, end-to-end IPI evaluation, and confidence intervals, a revised version could be a strong paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>