Now I have all the anchors I need to calibrate. Let me now write the final review.

**Round 1 bracket:** 5.0 – 7.0. The paper is clearly above weak anchors (eKGEsFdpin at 3.67, r6aX67YhD9 at 4.75) and below the strong anchor (E4LAVLXAHW at 7.00).

**Round 2 narrowing:** Compared to DEJIDCmWOz (6.00, Accept), our paper has a more novel contribution (a new watermarking paradigm) but somewhat less rigorous evaluation. Compared to FDfq0RRkuz (5.50, Reject), our paper has a cleaner, more impactful idea. Compared to E4LAVLXAHW (7.00, Accept), our paper's evaluation is less thorough.

The paper lands at approximately **6.0**: a solid contribution that warrants acceptance, with clear evaluation gaps that should be addressed.

---

## Summary

This paper introduces In-Context Watermarking (ICW), a novel approach that embeds watermarks into LLM-generated text purely through prompt engineering, without requiring access to the model's decoding process. The authors propose four ICW strategies at different linguistic granularities (Unicode, Initials, Lexical, and Acrostics), each with a tailored detection method. They evaluate these strategies in two settings: Direct Text Stamp (DTS), where users explicitly include watermarking instructions as system prompts, and Indirect Prompt Injection (IPI), where watermarking instructions are covertly embedded into documents (e.g., academic manuscripts) to detect AI-generated reviews. The results show that ICW is effective with capable LLMs like gpt-o3-mini, achieving strong detection, robustness to paraphrasing, and preserved text quality.

## Strengths

- **Novel and well-motivated problem framing.** The paper identifies a genuine gap: existing watermarking methods require model-provider cooperation (access to decoding), leaving third parties without recourse. ICW addresses this by shifting watermarking entirely to the prompt level, which is a creative and previously unexplored direction. The IPI case study for detecting AI-generated peer reviews makes the motivation concrete and compelling.

- **The effectiveness of ICW demonstrably scales with LLM capability.** Table 2 shows dramatic improvements when moving from gpt-4o-mini to gpt-o3-mini: Initials ICW jumps from ROC-AUC 0.572 to 0.999, and Acrostics ICW from 0.590 to 1.000. This directly supports the paper's central thesis that ICW's feasibility depends on instruction-following ability and will improve as models advance.

- **Strong robustness to paraphrasing attacks.** Figure 3 shows that Acrostics ICW retains an AUC of 0.922 and Initials ICW retains 0.887 under LLM paraphrasing — a transformation that often breaks watermarking methods (e.g., YCZ+23 drops to AUC 0.557). This is a meaningful practical advantage.

- **Text quality is well-preserved.** Table 3 demonstrates that ICW methods (e.g., Acrostics: 4.950 relevance, 4.978 quality, 4.510 clarity) closely match unwatermarked baselines (4.982/5.000/4.994) on LLM-as-a-Judge evaluation, while substantially outperforming the post-hoc baseline PostMark (2.648/3.848/2.494).

- **Well-structured comparative design.** The paper systematically explores four strategies at different granularities (character, word-initial, word-lexical, sentence-acrostic) and explicitly analyzes trade-offs among LLM requirements, detectability, robustness, and text quality (Table 1), giving practitioners a clear menu of options.

## Weaknesses

### Fatal

None.

### Major

- **The detection evaluation uses human-written text as the negative class, without testing against unwatermarked LLM outputs.** Throughout the experiments, negatives are human-written text (ELI5 answers for DTS, and the paper does not explicitly state the negative source for IPI). While distinguishing AI text from human text is a stated goal of the paper, in the IPI scenario a realistic concern is that a reviewer might use an LLM *without* triggering the watermark instruction — producing unwatermarked LLM text. If unwatermarked LLM outputs have different statistical properties (e.g., word-initial letter distributions) than human text, the reported T@1%F and T@10%F numbers may not reflect the actual false positive rate against unwatermarked LLM text. The paper would be strengthened by including unwatermarked LLM outputs (same model, same prompt, no watermark instruction) as an additional negative class, or at minimum discussing why human-text calibration is sufficient for the claimed use cases.

- **Lexical ICW's detection statistic relies on an unjustified uniform-probability assumption.** The null parameter γ is set to |green list| / |vocabulary|, which assumes every word in the restricted vocabulary (adjectives, adverbs, verbs) is equally likely in unwatermarked text. This assumption does not hold — word frequencies follow highly non-uniform distributions. Consequently, the z-statistic for Lexical ICW is likely miscalibrated even against human text, and the claimed false-positive control (Appendix B) does not apply under realistic word-frequency distributions. This directly affects the Lexical ICW detection numbers in Table 2 and the Lexical robustness numbers in Figure 3.

### Minor

- **The IPI white-text injection mechanism is not empirically validated.** The paper proposes embedding watermark instructions as "white text" or zero-font-size text in PDFs (Section 3.2) but does not test whether these instructions survive standard PDF-to-text extraction pipelines or whether LLMs actually process them when a paper is copied in. The paper acknowledges this as future work, but a pilot experiment would strengthen the practical credibility of the IPI case study.

- **Only two models from a single provider are tested.** The claim that "ICW effectiveness will improve as LLMs advance" is supported only by gpt-4o-mini and gpt-o3-mini (both OpenAI). Testing on a more diverse set of models — including open-source models with varying instruction-following capability — would make this claim more robust.

- **The paraphrasing attack implementation is underspecified.** Section 5.1 states paraphrasing is done "using an LLM" without naming the model or providing the prompt. This matters because using the same model that generated the watermarked text could inflate robustness estimates.

- **Content quality of watermarked reviews is not assessed.** The text quality evaluation (LLM-as-a-Judge, perplexity) measures linguistic quality but does not assess whether ICW instructions degrade the factual accuracy or substantive quality of generated reviews — a critical concern for the IPI scenario where review integrity is paramount.

### Trivial

- The paper does not explicitly state the negative examples used for the IPI detection experiments in the main text.

## Nice-to-Haves

- Including unwatermarked LLM outputs as an additional negative class and recalibrating detection thresholds accordingly would address the most significant evaluation gap.
- For Lexical ICW, replacing the uniform γ assumption with an empirically estimated green-word probability (from a corpus of unwatermarked LLM text) or adopting the Acrostics-style within-text resampling approach would fix the calibration issue.
- A small pilot study testing whether hidden instructions in PDFs survive common extraction tools (e.g., pdftotext, PyPDF2) would validate the IPI premise.
- Testing on open-source models (e.g., Llama, Mistral) to confirm the capability-scaling claim across model families.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh critic claim that negative class issue is "structural" and "fatal":** DEMOTED to Major. The paper's stated goal includes distinguishing AI from human text (abstract), making human text a legitimate negative class for that goal. The concern about unwatermarked LLM text as negatives is valid but is an evaluation completeness issue rather than a fatal flaw — the detectors may still perform well against unwatermarked LLM text (e.g., for Initials ICW, LLM initial-letter distributions likely closely match human text). Without evidence that the gap is large, calling this "fatal" overstates.

- **Harsh critic claim that Lexical ICW's uniform assumption is fatal:** KEPT as Major but demoted from fatal. This is a real methodological issue, but Lexical ICW is only one of four proposed strategies, and the paper's core contribution (ICW as a concept) does not hinge on this one detector being perfectly calibrated. The other three methods have different detection mechanisms not affected by this assumption.

- **Harsh critic concern about initial letter distribution differences between LLM and human text:** WEAKENED. This is speculative — LLMs are trained to match human text distributions, and the critic provides no evidence that initial-letter frequencies differ substantially. Incorporated into the Major weakness at a reduced severity level.

- **Harsh critic claim about overselling IPI practicality:** Kept in spirit but reframed as Minor (lack of empirical validation) rather than as a fatal flaw, since the paper explicitly acknowledges this as future work (Section 3.2: "a detailed investigation of attack and defense methods is left for future work").

- **Strength Finder claim about "theoretical false-alarm control (Appendix B)":** REMOVED as a standalone strength. The theoretical guarantee for Initials ICW depends on the human-corpus γ estimate, and for Lexical ICW on the uniform assumption. The guarantee is only as good as the null model, which is part of what the Major weakness targets. The theoretical framing is still a positive aspect, but it doesn't stand as an independent strength given the calibration concerns.

- **Strength Finder claim about "multi-faceted evaluation protocol":** KEPT implicitly (it's a supporting aspect of the evaluation), but the claim that it gives "a holistic picture" is overstated given the negative-class limitation.

## Novel Insights

The paper's key insight — that watermarking can be achieved purely through prompt engineering by exploiting LLMs' instruction-following and in-context learning capabilities — is genuinely novel and opens up a new axis in the watermarking design space. Prior work focused on either decoding-time intervention (in-process) or text transformation (post-hoc); ICW demonstrates a third path that requires neither model access nor post-generation modification. The finding that this approach works surprisingly well with capable models (gpt-o3-mini), despite requiring the LLM to internalize and execute complex multi-sentence watermarking constraints, suggests that prompt-level control is a viable — and perhaps underappreciated — mechanism for content attribution. The scaling trend from gpt-4o-mini to gpt-o3-mini also provides an empirical signal that this approach will become increasingly practical as models improve.

## Suggestions

- The most impactful improvement would be to add unwatermarked LLM outputs as a negative class for all detection experiments, and report detection metrics (ROC-AUC, T@%F) against this class. This would address the central evaluation concern without requiring methodological changes.
- For Lexical ICW, estimate γ empirically from a corpus rather than assuming uniform word probabilities. Alternatively, adopt a non-parametric detection approach (like the Acrostics resampling method) that does not rely on a pre-specified null proportion.
- Add a brief discussion (or a small experiment) on whether common PDF extraction tools preserve hidden text, to ground the IPI case study in practical reality.

## Score and Decision

**Originality:** High. ICW is a genuinely new approach to LLM watermarking that fills a clear gap.

**Importance:** High. Enabling watermarking without model-provider cooperation has significant practical implications for content provenance, academic integrity, and AI misuse detection.

**Claim support:** Moderate-to-Strong. The core claim (ICW works with capable models) is well-supported by Table 2. The evaluation has gaps (negative class, Lexical ICW calibration) that weaken but do not invalidate the contribution.

**Soundness:** Moderate. The methods are sound in principle, but the evaluation choices (human-only negatives, Lexical ICW's uniform γ) reduce confidence in the reported numbers.

**Clarity:** Good. The paper is well-structured and the four strategies are clearly motivated and described.

**Value to community:** High. ICW opens a new research direction and the IPI case study provides a concrete, compelling application scenario.

**Anchor comparison:**
- eKGEsFdpin (3.67, Reject, Round 1): Incremental watermarking method with narrow evaluation. Our paper is substantially more novel and comprehensive.
- r6aX67YhD9 (4.75, Reject, Rounds 1&2): RL-based watermarking requiring model training. Our paper is more practical (no training needed) and has broader applicability.
- 0KHW6yXdiZ (5.25, Reject, Round 2): End-to-end watermarking with limited novelty. Our paper is more creative and better motivated.
- FDfq0RRkuz (5.50, Reject, Round 2): WASA source attribution. Similar quality level but our paper's contribution is more novel. Our paper is slightly stronger.
- DEJIDCmWOz (6.00, Accept, Round 2): Watermark reliability study. Solid but incremental. Our paper has a more novel contribution with comparable evaluation rigor. Slightly stronger overall.
- E4LAVLXAHW (7.00, Accept, Rounds 1&2): Black-box watermark detection with rigorous methodology. Our paper is less rigorous but comparably novel. One notch below.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>