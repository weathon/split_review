Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a watermarking paradigm that embeds detectable signals into LLM-generated text *solely through prompt engineering*, without any access to model weights, logits, or decoding process. The paper proposes and systematically evaluates four ICW strategies at different linguistic granularities (Unicode, word-initial letters, whole-word lexical, and sentence-initial acrostics) in two settings: Direct Text Stamp (DTS) where the watermark is in the system prompt, and Indirect Prompt Injection (IPI) where it is covertly embedded in input documents to detect AI-generated peer reviews. The key result is that with a sufficiently capable LLM (GPT-o3-mini), all four strategies achieve near-perfect detection (AUC ≥ 0.995 in DTS), demonstrating that prompt-only watermarking is feasible.

## Strengths

- **First systematic demonstration of purely prompt-based watermarking.** Unlike all prior LLM watermarking (Kirchenbauer et al., Aaronson, Christ et al.) that requires modifying logits or sampling, ICW operates entirely through instruction-following. Table 2 provides the primary evidence: with GPT-o3-mini, Acrostics ICW achieves AUC 1.000 in DTS and 0.997 in IPI. This opens a new axis in the watermarking design space that is accessible to third parties without model provider cooperation.

- **Novel application (IPI) that existing methods cannot address.** The Indirect Prompt Injection setting targets the concrete problem of detecting AI-generated peer reviews, where post-hoc methods (PostMark, YCZ+23) and in-process methods are inapplicable because the dishonest reviewer has no incentive to watermark their own output. The paper correctly identifies this gap and demonstrates that the IPI setting achieves AUC ≥ 0.997 with GPT-o3-mini for multiple ICW strategies.

- **Principled exploration of four strategies with explicit trade-off characterization.** The paper designs ICW methods at Unicode, word-initial, word-level, and sentence-level granularities, and summarizes their trade-offs across LLM requirements, detectability, robustness, and text quality in a single table (Table 1). This provides practitioners with a framework for selecting a strategy based on model capability and application constraints — no prior work has done this for prompt-based watermarking.

- **Scaling behavior empirically validated.** The contrast between GPT-4o-mini and GPT-o3-mini (Table 2) provides direct evidence that ICW effectiveness grows with model capability (e.g., Initials ICW: AUC 0.572 → 0.999). This supports the paper's central claim that ICW becomes more viable as LLMs advance, grounding what would otherwise be speculation in data.

- **Text quality preservation demonstrated.** LLM-as-a-Judge evaluation (Table 3) shows ICW overall scores (4.808–4.813 for Lexical and Acrostics) close to unwatermarked text (4.992), markedly better than PostMark (2.997) and YCZ+23 (3.865).

## Weaknesses

### Fatal
None.

### Major

1. **Detection evaluation uses human text as the negative class, not unwatermarked LLM text.** The hypothesis test (Section 3.1) defines the null as "text generated without knowledge of k and τ." The experiments (Section 5.1) use ELI5 human answers as the negative class. For Initials and Lexical ICWs, the detector is a z-statistic comparing observed letter/word frequencies against a human-written baseline (Canterbury Corpus). If LLMs naturally produce text with different letter/word distributions than humans, the detector could partially pick up "LLM-ness" rather than the watermark signal itself. This concern applies unevenly across methods: Unicode ICW (zero-width spaces) and Acrostics ICW (which resamples the suspect text's own sentence initials as null) are less affected, but Initials and Lexical ICWs have a genuine confound. The paper should evaluate detection against unwatermarked LLM text (same model, same queries, no watermark instruction) to isolate the watermark signal. Without this, the reported AUCs — especially the near-perfect values — cannot be cleanly attributed to the watermark.

2. **IPI setting adversary model is not experimentally validated under realistic countermeasures.** The paper's primary application scenario is detecting AI-generated peer reviews by embedding hidden instructions in manuscripts. However, the experiments test robustness only against random deletion, synonym replacement, and paraphrasing (Section 5.2.2). The obvious adversarial countermeasure — a reviewer who copy-pastes only visible text, uses a PDF-to-text converter that strips hidden annotations, or prepends "ignore previous instructions" — is mentioned as "left for future work" (Section 3.2). The paper notes in Section 5.2.3 that Appendix D.1 investigates "ignore prior prompts" attacks, but this is not visible in the main paper and crucially does not appear in any main-table or figure. For a paper that frames IPI as a central contribution (Abstract, Section 3.2), the lack of main-paper experiments with an adversary who actively tries to strip the instruction weakens the practical claims.

### Minor

1. **No confidence intervals or error bars for detection results.** Table 2 reports ROC-AUC, T@1%F, and T@10%F as point estimates without bootstrap intervals or standard errors. With 500 positive and 500 negative samples per condition, many values are reported as 1.000. The paper does not discuss whether the differences between methods (e.g., AUC 0.995 vs. 1.000) are meaningful, and for methods with variable performance (Lexical ICW on GPT-4o-mini: T@1%F = 0.320, T@10%F = 0.692), the stability is unclear.

2. **No evaluation on open-source LLMs.** All experiments use two proprietary models (GPT-4o-mini, GPT-o3-mini). Results on Llama-3 or similar open-weight models would substantially strengthen the claim of generality and allow independent reproduction.

3. **Initials ICW claimed as "invisible to humans" but uses only 6/26 letters.** The paper states Initials ICW is "invisible to humans" (Section 4.2.2). With a green-letter set of size ~6 (typical — 6/26 ≈ 23%), and the instruction asking the LLM to "maximize" use of such words, the resulting text would likely have a noticeably elevated frequency of words beginning with those specific letters. A brief human judgment experiment or quantitative measure (e.g., how much the letter distribution deviates from natural text) would substantiate this claim.

### Trivial
- None beyond standard formatting artifacts introduced by PDF parsing.

## Nice-to-Haves
- Reporting bootstrap confidence intervals for detection AUCs (Table 2).
- A brief human evaluation of watermark imperceptibility for Initials and Lexical ICW (do human raters notice anything unusual?).
- Testing on at least one open-weight LLM (e.g., Llama-3-70B) to demonstrate generality beyond proprietary APIs.

## Removed Points

These points from the input reviews were removed with brief justification:

- **"No comparison to trivial baseline (e.g., 'include the word plugh')"** — Removed. ICW provides statistical detection guarantees (z-statistics, false alarm control), imperceptibility, and robustness that a fixed-token prompt cannot. The paper's claim is not "LLMs follow instructions" but that prompt-based watermarking with statistical detection is feasible — a trivial token does not demonstrate this.

- **"ICW is not model-agnostic because it only works on capable models"** — Removed. The paper uses "model-agnostic" to mean "does not require model-internal access," not "works equally well on all models." The dependency on model capability is explicitly discussed throughout.

- **"The paper does not clearly position ICW relative to stealing/encoding a secret via prompt"** — Removed. The paper discusses the difference: existing work uses fixed tokens or simple instructions; ICW provides systematic strategies with statistical detection. This criticism reflects insufficiently careful reading.

- **"The definition of Instruction(k, τ) is too abstract"** — Removed. The paper provides concrete abbreviated instructions for each method (Section 4), full instructions in Appendix A, and all four methods are clearly described with algorithms and detection procedures.

- **"The paper does not mention how hidden instructions survive PDF processing"** — Removed. The paper discusses that the instruction can use "white text" within PDFs and notes that obfuscation methods have been "extensively explored in many prompt injection attacks" (Section 3.2). A detailed study of obfuscation robustness is explicitly scoped as future work.

- **"Missing inter-rater reliability for LLM-as-a-Judge"** — Removed. LLM-as-a-Judge is a single model, so inter-rater reliability does not apply. The concern about prompt bias is noted but speculative.

- Strengths from the Strength Finder that were generic or lacked specific evidence were removed (e.g., "the paper identifies a real and important problem" — generic framing).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add detection against unwatermarked LLM text.** This is the single most important addition. Generate responses from the same model and queries without the watermarking instruction, and show that the detector does *not* flag them. This would cleanly separate the watermark signal from the LLM-vs-human difference and make the headline results unassailable.

2. **Put the "ignore prior prompts" experiment in the main paper.** Since the paper mentions this is in Appendix D.1, moving at least one representative result (e.g., a bar chart showing AUCs with/without prepended "ignore prior instructions") into Section 5.2 would directly address the biggest practical concern about the IPI setting.

3. **Add bootstrap confidence intervals to Table 2.** This is standard practice and would address the concern about measurement stability, especially for the 1.000 values.

4. **Soften the "invisible to humans" claim for Initials ICW** by replacing it with "statistically unobtrusive" or adding a brief quantification of how much the letter distribution shifts.

## Score and Decision

**Calibration anchors** (all from the human-review corpus):

- **WASA** (avg 5.50, Reject) — Watermarking for source attribution using Unicode chars. ICW is stronger: explores 4 strategies, has a genuinely novel IPI application, better evaluation depth. ICW > WASA.
- **Semantic Invariant Robust Watermark** (avg 5.50, Accept, scores 8/5/6/3) — Semantic-level watermark requiring logit access. Similar overall quality; ICW has more novelty (prompt-only paradigm) but less rigorous treatment of one setting. ICW ≈ this paper.
- **Black-Box Detection of Watermarks** (avg 7.00, Accept) — Rigorous statistical tests for detecting existing watermarks. More polished and thorough than ICW within its scope, but addresses a narrower, different problem. ICW < this paper on execution quality but > on breadth of contribution.
- **I Know You Did Not Write That** (avg 3.67, Reject) — Sampling-based watermarking with limited novelty over Kirchenbauer. ICW is substantially more novel and better executed. ICW >> this paper.
- **Water-Probe** (avg 7.50, Accept) — Detecting watermarked LLMs via crafted prompts. Very well executed with clean contribution. ICW is less polished but comparably novel. ICW < this paper on execution.

The paper introduces a genuinely novel watermarking paradigm (prompt-only) and evaluates it systematically across four strategies. The main weaknesses — detection against human text only rather than unwatermarked LLM text, and limited adversary validation for the IPI setting — are real but addressable and do not invalidate the core contribution. The paper is well-structured, the methods are clearly described, and the trade-offs are transparently presented. I calibrate this as slightly above the Semantic Invariant watermark (5.50) and below the Black-Box Detection paper (7.00).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>