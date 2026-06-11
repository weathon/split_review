Now let me write the final review with score and decision.

---

## Summary
This paper introduces In-Context Watermarking (ICW), a model-agnostic approach that embeds detectable watermarks into LLM-generated text using only prompt engineering — no access to model weights, logits, or decoding required. Four ICW strategies at different linguistic granularities (Unicode, Initials, Lexical, Acrostics) are proposed with tailored statistical detectors. A key contribution is the Indirect Prompt Injection (IPI) setting, where watermark instructions are covertly embedded into academic manuscripts to detect AI-generated peer reviews. Results with GPT-o3-mini show strong detection performance (ROC-AUC ≥ 0.995) and good robustness to paraphrasing, while GPT-4o-mini largely fails on harder strategies, supporting the thesis that ICW effectiveness scales with model capability.

## Strengths
- **Creative and genuinely novel approach to LLM watermarking.** The paper proposes using prompt engineering alone for watermarking, bypassing the need for model access that constrains prior work (Kirchenbauer et al., Aaronson). The four ICW strategies (Unicode, Initials, Lexical, Acrostics) span character, word-initial, lexical, and sentence-level granularity, each with a tailored detection method — a systematic exploration of the design space (Section 4.2). This is a genuinely new paradigm in the watermarking literature.

- **Well-motivated real-world scenario with practical novelty.** The IPI setting (Section 3.2), where conference organizers embed invisible watermark instructions into manuscripts to detect dishonest reviewers using LLMs, crystallizes a practical gap that existing watermarking methods cannot address. The threat model is clearly reasoned, including the nuanced footnote about author conflicts of interest.

- **Honest and thorough discussion of limitations.** The paper does not oversell: it acknowledges vulnerability to spoofing attacks (Section 4.2.2), fragility of Unicode ICW to paraphrasing (Section 4.2.1), and the possibility of adversarial instruction removal (Section 3.2, Section 6). The "ignore prior prompts" attack evaluation is mentioned in the main text. Few empirical papers are this candid about their methods' weaknesses.

- **Strong robustness to paraphrasing attacks.** Under the paraphrase attack (Figure 3), Initials ICW achieves AUC 0.887, Lexical ICW 0.924, and Acrostics ICW 0.922, substantially outperforming PostMark (0.841) and YCZ+23 (0.557). LLM paraphrasing is a realistic attack, making this a meaningful practical result.

## Weaknesses

### Fatal
None.

### Major
- **Detection calibration not validated on unwatermarked LLM outputs.** The Initials ICW detector uses γ estimated from the Canterbury Corpus to represent expected green-initial-letter frequency under H₀ (Section 4.2.2). The Lexical ICW detector sets γ = |V_G|/|V|, implicitly assuming uniform word usage across the green/red vocabulary (Section 4.2.3). Neither assumption is validated against unwatermarked LLM-generated text from the same models. While the paper uses human-generated text (ELI5 answers) as the negative class and the Canterbury Corpus is a reasonable proxy for human text, the practical detection scenario involves distinguishing watermarked from unwatermarked LLM outputs, not from human text. The near-perfect scores (e.g., ROC-AUC 0.999, T@1%F 0.990 for Initials ICW with GPT-o3-mini) could partially reflect miscalibration if the LLM's natural word-initial or lexical distributions deviate from the assumed null. This is addressable with additional calibration experiments.

- **Negative class is ambiguous in the IPI setting.** Section 5.1 states that evaluation uses "500 watermarked texts and 500 human-generated texts." For the DTS setting the human texts are ELI5 answers (clearly stated). For the IPI setting, the paper never specifies what constitutes "human-generated texts" — are these genuine human-written peer reviews? If so, the detection task confounds "does this text contain a watermark" with "is this text LLM-generated or human-written," since LLM-generated reviews may exhibit detectable stylistic properties independent of any watermark signal. This ambiguity weakens the interpretability of the IPI detection results.

- **Adversarial subversion acknowledged but relegated from main evaluation.** The paper's practical value in the IPI setting hinges on the adversary not inspecting their input for hidden prompts. Simple countermeasures (stripping invisible text, prepending "ignore prior prompts") could defeat the scheme. While the paper is admirably honest about this limitation (Section 3.2, Section 6), the empirical case for practical viability remains incomplete without adversarial evaluation in the main results — the "ignore prior prompts" results are only mentioned as existing in Appendix D.1.

### Minor
- **Capability-dependence claim overreaches the evidence.** The paper claims "as LLMs continue to advance, ICWs will become correspondingly more powerful," supported by comparing GPT-4o-mini to GPT-o3-mini (Table 2). Two data points from a single vendor do not establish a general trend across model families. The claim should be narrowed to what the evidence supports.

- **LLM-as-Judge evaluation exhibits known self-preference bias.** Table 3 shows unwatermarked GPT-o3-mini text scoring higher than human text on all dimensions (overall 4.992 vs. 4.235), a documented artifact where LLM judges favor LLM-written text. The paper does not discuss this calibration issue.

- **No reported variance across green-list draws.** For Initials and Lexical ICWs, the detection signature depends on which specific green letters/words are randomly selected. The paper reports single-run results without characterizing variance across multiple random draws, leaving it unclear how stable the reported detection scores are.

### Trivial
- Table 1 uses filled circles to summarize trade-offs with only "Darker circles indicate higher values" as explanation — purely illustrative with no quantification.

## Nice-to-Haves
- Testing on models from other providers (Claude, Gemini, Llama) would strengthen the capability-dependence narrative.
- Human evaluation of text quality would complement the LLM-as-Judge results, especially for Initials ICW where clarity drops notably (3.706 vs. 4.994 unwatermarked).
- Analysis of minimum text length needed for reliable detection, as this directly determines applicability to short reviews.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Acrostics AUC=1.000 under word replacement is implausibly perfect"** — REMOVED. The Acrostics ICW constrains only sentence-initial letters (Section 4.2.4). A word-replacement attack targeting nouns, verbs, adjectives, and adverbs within sentences would not affect sentence-initial letters, making AUC=1.000 entirely plausible given the attack design.

- **"GPTZero results omitted from Table 2 — should be shown"** — REMOVED. The paper states these results are in Appendix D.1 (line 218). The parser strips appendices; this is not an author error.

- **"No analysis of detection power vs. text length — should be in main results"** — REMOVED. The paper states this ablation is in Appendix D.1 (line 286). The parser strips appendices.

- **"Missing discussion of linguistic steganography in related work"** — REMOVED per instructions: do not mention missing related works.

- **"Table 1 has no legend or quantification — completely vacuous"** — Demoted to Trivial only. The caption states "Darker circles indicate higher values"; it is underspecified but the paper explicitly calls it "an intuitive illustration" (Section 4.1).

- **"Unicode ICW is fragile to cross-platform transmission"** — REMOVED as a weakness since the paper explicitly acknowledges this in Section 4.2.1: "it is highly fragile to transformations like LLM paraphrasing, which may limit its application in broader scenarios."

## Novel Insights
The most interesting insight is the capability-dependence phenomenon: ICW methods that completely fail on GPT-4o-mini become near-perfect on GPT-o3-mini. This suggests that as LLM instruction-following improves, prompt-engineering-based approaches may become competitive with — and in some ways more practical than — traditional decoding-time watermarking. This inverts the usual framing where watermarking is something model providers must implement; instead, third parties can watermark through prompt engineering alone, with effectiveness improving automatically as models advance. The IPI setting, despite its limitations, opens a genuinely new angle for AI-content provenance that does not depend on model-provider cooperation.

## Suggestions
- Add a calibration experiment: run the Initials and Lexical detectors on unwatermarked LLM-generated text (same model, same prompt domain) and verify that empirical FPR matches nominal thresholds. This is the single highest-impact improvement.
- Clarify the negative class for IPI evaluation and ideally include unwatermarked LLM-generated reviews as an additional control condition to disentangle watermark detection from LLM-text detection.
- Move the "ignore prior prompts" adversarial evaluation from the appendix to the main results, as it directly determines the viability of the IPI scenario.
- Narrow the capability-dependence claim to what the data support: "ICW performance improved from GPT-4o-mini to GPT-o3-mini" rather than the broader forward-looking claim.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Decision | Comparison |
|--------|-----------|-------|----------|------------|
| eKGEsFdpin | 3.67 | R1 | Reject | Our paper clearly stronger: more novel paradigm |
| r6aX67YhD9 | 4.75 | R1 | Reject | Our paper moderately stronger: no fatal flaw like requiring original prompts |
| 0koPj0cJV6 | 4.60 | R2 | Reject | Most comparable black-box watermarking anchor; our paper more novel |
| 0KHW6yXdiZ | 5.25 | R1 | Reject | Comparable quality; our paper slightly more novel, similar evaluation depth |
| FDfq0RRkuz | 5.50 | R1 | Reject | Comparable; our paper has a more creative framing |
| KRMSH1GxUK | 5.80 | R1 | Accept | Our paper slightly weaker: less rigorous validation |
| DEJIDCmWOz | 6.00 | R2 | Accept | Our paper moderately weaker: more evaluation gaps |
| E4LAVLXAHW | 7.00 | R1/R2 | Accept | Our paper clearly weaker: less rigorous, more exploratory |

**Bracket:** 5.0 – 6.0, narrowed to **5.5** based on comparison with the 4.60–5.50 rejected anchors and the 5.80–6.00 accepted anchors. The paper introduces a genuinely novel paradigm with a compelling application scenario and strong robustness results, but the evaluation has genuine methodological gaps (detection calibration, IPI negative class ambiguity, adversarial results relegated to appendix) that prevent it from reaching the rigor of accepted anchors in the 6.0+ range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>