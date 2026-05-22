Now I have a thorough understanding of the paper and have verified the reviewer claims against the actual content. Let me write the consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for embedding detectable watermarks into LLM-generated text **solely through prompt engineering**, without any access to model internals, logits, or decoding processes. The authors propose four strategies (Unicode, Initials, Lexical, and Acrostics ICWs), design tailored detection methods for each, and evaluate them in both a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) setting motivated by detecting AI-written peer reviews. With sufficiently capable models (GPT-o3-mini), three of four methods achieve near-perfect detection (ROC-AUC ≥ 0.995) while maintaining strong text quality and competitive robustness against paraphrasing.

## Strengths

- **Genuinely novel watermarking paradigm.** ICW is the first systematic exploration of embedding watermarks through prompt engineering alone, without modifying the decoding process. This addresses a real gap: third parties who interact with LLMs only through APIs currently have no means to watermark outputs. Table 2's results — near-perfect AUC with GPT-o3-mini across multiple strategies — provide direct evidence that the approach is feasible.

- **Systematic exploration of four strategies with explicit trade-offs.** Section 4 and Table 1 characterize Unicode, Initials, Lexical, and Acrostics ICWs across LLM requirements, detectability, robustness, and text quality. This structured comparison goes beyond demonstrating a single technique and lets practitioners choose a method suited to their deployment constraints.

- **Introduces the IPI setting as a concrete use case.** The paper formalizes a scenario (Section 3.2, Figure 2) where watermarking instructions are covertly embedded into documents to detect misuse of LLMs, e.g., dishonest reviewers. Experimental results (Table 2, IPI columns) show high detection performance (e.g., Acrostics ICW: 0.997 AUC), demonstrating a concrete application that prior watermarking work does not address.

- **Competitive robustness against paraphrasing.** Figure 3 shows that under paraphrasing attacks, Initials (AUC=0.887), Lexical (AUC=0.924), and Acrostics (AUC=0.922) ICWs outperform the YCZ+23 (AUC=0.557) and PostMark (AUC=0.841) baselines in the DTS setting, indicating that prompt-based watermarks survive regeneration better than lexical-substitution methods.

- **Better text quality than the PostMark baseline.** Table 3 reports that ICW methods achieve substantially higher LLM-as-a-Judge overall scores (e.g., Acrostics: 4.813, Lexical: 4.808) than PostMark (2.997), showing that ICW does not sacrifice readability for detectability.

- **Honest discussion of limitations.** Section 6 openly discusses model-dependence, the difficulty of Lexical ICW with large vocabularies, and the treatment of ICW as an alignment task. The paper does not overclaim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theoretical null distribution for Lexical ICW is not validated against human text.** For Lexical ICW, the detection z-statistic uses γ = |V_G|/|V|, which assumes each word in the vocabulary is equally likely in human text. This is not true — word frequencies in natural language are heavily skewed. If the randomly sampled green set contains a disproportionate share of common (or rare) words, the expected green proportion under the null will deviate from the uniform baseline. Unlike Initials ICW, which correctly estimates γ from the Canterbury Corpus (line 151), Lexical ICW provides no such empirical calibration. The paper claims a "theoretical guarantee on controlling the false alarm rate" (line 168, Appendix B) for both methods, but for Lexical ICW this guarantee may be misspecified. That said, the paper's **empirical** results (ROC-AUC, T@1%F, T@10%F) are computed from data and remain valid — the concern is about the theoretical framing. The authors should either validate empirically that the null distribution holds, or adopt a corpus-estimated γ for Lexical ICW as well.

- **No confidence intervals or variance estimates for detection metrics.** Table 2 reports AUC, T@1%F, and T@10%F without error bars or variance measures. With 500 watermarked and 500 human texts per condition, bootstrap confidence intervals would help assess the stability of the reported numbers, especially at the stringent low-FPR operating points where variance is nontrivial.

- **IPI case study does not test realistic covert embedding.** The paper tests the IPI setting by concatenating the watermarking instruction with the paper text (Section 3.2), but in practice the instruction would need to be covertly embedded (e.g., white text, zero-font-size characters). The paper acknowledges this gap (line 106: "a detailed investigation of attack and defense methods is left for future work"), which is appropriate for a first exploration. However, since the IPI motivation (detecting dishonest reviewers) is a centerpiece of the paper's narrative and the abstract, testing at least one realistic embedding pipeline — e.g., white text in a PDF followed by text extraction — would substantially strengthen the claims about practical deployability.

### Trivial

- **"Ignore prior prompts" attack results are not summarized in the main text.** The paper mentions in passing (line 291) that this attack is investigated in Appendix D.1, but gives no indication of the outcome. A one-sentence summary (e.g., "detection remains effective / degrades under this attack" with a key number) would let readers assess IPI robustness without consulting the appendix.

## Nice-to-Haves

- Extending the evaluation to include open-source models (e.g., LLaMA, Qwen) would test whether ICW generalizes beyond proprietary API models.
- A small human evaluation of text quality (e.g., 50 samples rated for fluency/naturalness) would complement the LLM-as-a-Judge scores and address potential evaluator bias.
- Comparing against a simpler IPI-relevant baseline (e.g., perplexity-based detection or GPTZero) would contextualize how much value the watermark adds over passive detection in the IPI scenario.

## Removed Points

*These points were raised in the reviews but are not included as weaknesses above, with justification:*

- **"Null distribution concern makes reported low-FPR performance unreliable"** — Removed as overblown. The empirical T@1%F and T@10%F values are computed directly from held-out human text (thresholds are set empirically from the data), not derived from the theoretical null. The reported numbers are robust regardless of the theoretical γ parameter. The concern only affects the *theoretical guarantee* framing, not the actual measurements.
- **"IPI realism is a structural gap that undermines the core claim"** — Removed. The paper explicitly frames this as a case study and states that detailed attack/defense investigation is future work (Section 3.2). The core contribution is ICW feasibility, not solving the full deployment pipeline.
- **"PostMark text quality scores are suspiciously low"** — Removed. This is an observation about PostMark's performance in this setting, not a weakness of the ICW paper. The paper honestly reports what it found.
- **"Missing confidence intervals is a major evaluation gap"** — Downgraded to Minor. While CIs would strengthen the paper, 500+500 samples produce stable ROC-AUC estimates, and this level of reporting is within the norm for the field.
- **Strength: "Theoretical FPR control for Initials and Lexical ICWs"** — Moved here. This strength is qualified by the unvalidated null distribution for Lexical ICW (see Minor weakness above). For Initials ICW the corpus-based estimation is sound; for Lexical ICW the theoretical guarantee is on less solid footing without empirical validation.

## Novel Insights

None beyond the paper's own contributions. The key insight — that instruction-following capabilities of modern LLMs are strong enough to embed detectable statistical signals purely through prompting — is well-articulated by the authors themselves.

## Suggestions

1. **Empirically validate the Lexical ICW null.** Compute γ on a held-out human corpus (e.g., a portion of ELI5) by measuring the empirical fraction of green-list words in human text and comparing it to the assumed |V_G|/|V|. If there is a systematic bias, either calibrate γ or switch to a corpus-estimated baseline.
2. **Add bootstrap confidence intervals** to the detection metrics in Table 2, at least for the T@1%F and T@10%F columns where variance matters most.
3. **Run a small-scale realistic IPI test** with white-text-in-PDF embedding, followed by text extraction (copy-paste, pdftotext), to verify that the watermarking instruction survives to the LLM.
4. **Surface the "ignore prior prompts" result** in the main text with a single sentence and a key number.

## Score and Decision

**Round 1 — Bracketing:** Initial search placed the paper in the middle-to-upper band. Weak-band anchors (~3.0) are generic ICL papers far below this paper's quality. Middle-band anchors (4.67–6.00) are watermarking robustness/detection studies — the ICW paper is more novel than these. Strong-band anchors (7.5+) are on different topics (benchmark gaming, model IP protection). Bracket: **[5.5, 7.0]** .

**Round 2 — Narrowing:** Read four anchors: DEJIDCmWOz (6.00, watermark reliability study, accepted), NvSwR4IvLO (4.67, AI text detection, rejected), 0koPj0cJV6 (4.60, black-box watermark, rejected), E4LAVLXAHW (7.00, black-box watermark detection, accepted). Compared to the 6.00 anchor (a thorough robustness study of an existing watermark), this paper is more novel but has less experimental polish in some areas (no CIs, unvalidated Lexical null). Compared to the 7.00 anchor (a well-executed detection method with rigorous experiments), this paper is less experimentally thorough. The paper sits between these two: its contribution is genuinely novel and the core results are convincing, but the experimental validation has gaps that prevent it from reaching the top band.

**Final score: 6.5** — Strong accept. The paper introduces a genuinely new paradigm for LLM watermarking, with systematic exploration of multiple strategies, a novel application scenario (IPI), and convincing empirical results. The identified weaknesses are addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>