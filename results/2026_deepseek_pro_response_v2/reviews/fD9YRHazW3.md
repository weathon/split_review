Now I have a clear picture. Let me compare:

- **r6aX67YhD9** (4.75): RL watermarking requiring model training. Reviewers flagged evaluation gaps (detector needs original prompt), limited practicality. Our paper is clearly stronger — genuinely novel angle (no model access at all), more creative IPI setting, stronger results.

- **DEJIDCmWOz** (6.00): Studies robustness of in-process watermarks. Solid evaluation, well-received (all 6s). Our paper is more novel in approach but has the unwatermarked baseline evaluation gap that this paper doesn't.

- **FDfq0RRkuz** (5.50): WASA — Unicode-based watermarking for source attribution. Similar evaluation balance (good idea, some gaps). Our paper is comparable — broader method exploration and more creative framing, but similar evaluation limitations.

Our paper is stronger than the 4.75 anchor, comparable to the 5.50 anchor, and slightly below the 6.00 anchor due to the unwatermarked baseline evaluation gap being a more significant methodological concern than anything raised against the Reliability paper. **Bracket: 5.0–6.0, landing at 5.5.**

---

## Summary

This paper proposes In-Context Watermarking (ICW): embedding detectable watermarks into LLM outputs through prompt engineering alone, without access to model internals. Four strategies are explored at different linguistic granularities — Unicode (zero-width space insertion), Initials (biasing word-initial letters toward a secret green set), Lexical (biasing toward a secret green word list), and Acrostics (controlling sentence-initial letters to spell a secret sequence). The paper evaluates these in two settings: Direct Text Stamp (DTS) where the watermark instruction is in the system prompt, and Indirect Prompt Injection (IPI) where the instruction is covertly embedded in a document (motivated by detecting AI-generated peer reviews). Experiments use GPT-4o-mini and GPT-o3-mini, reporting detection ROC-AUC, robustness under editing/paraphrasing, and text quality via LLM-as-Judge.

## Strengths

- **Creative and well-motivated problem framing**: The paper identifies a genuine gap — watermarking LLM outputs when the user has no model access — and grounds it in a concrete, vivid use case (detecting AI-generated peer reviews via covertly embedded instructions in manuscripts). The IPI setting reverses the typical prompt-injection threat model in a clever way that is practically motivated.

- **Useful taxonomy of watermarking strategies at different linguistic granularities**: The four ICW methods (Unicode, Initials, Lexical, Acrostics) constitute a sensible design-space exploration spanning character-level, word-initial, lexical, and sentence-level watermarking. Each method comes with a paired detection procedure and the paper discusses trade-offs in LLM requirements, detectability, robustness, and text quality (Table 1).

- **Strong empirical demonstration that ICW works with a capable model**: Table 2 shows that with GPT-o3-mini, Initials ICW reaches ROC-AUC=0.999 (T@1%F=0.990), Lexical ICW reaches 0.995 (T@1%F=0.930), and Acrostics ICW reaches 1.000 (T@1%F=1.000) in the DTS setting, with similarly strong results in the IPI setting. The detection performance with GPT-o3-mini is genuinely strong across the three non-trivial methods.

- **Robustness to paraphrasing substantially exceeds post-hoc baselines**: Under paraphrase attack (Figure 3), Initials ICW (AUC=0.887), Lexical ICW (AUC=0.924), and Acrostics ICW (AUC=0.922) all dramatically outperform YCZ+23 (AUC=0.557) and PostMark (AUC=0.841). This is practically meaningful because paraphrasing is the most realistic attack in many deployment scenarios.

- **Text quality is well-preserved relative to unwatermarked LLM output**: Table 3 shows ICW methods scoring 4.282–4.813 overall (LLM-as-Judge, 1–5 scale), close to unwatermarked text (4.992) and far above PostMark (2.997). While the absolute scores are inflated by the judge's preference for AI-generated text, the relative comparison between ICW and unwatermarked outputs is the relevant one and shows minimal degradation.

## Weaknesses

### Fatal

None.

### Major

- **Missing unwatermarked LLM baseline for detection experiments**: For Initials, Lexical, and Acrostics ICWs, the detection ROC-AUC compares watermarked LLM text against human-written text (ELI5 answers). The practical question the detector must answer is whether the text carries the watermark, not whether it is LLM-generated vs. human-written. If GPT-o3-mini naturally produces text whose word-initial-letter distribution, vocabulary choices, or sentence-initial-letter patterns differ from human text, the detector could flag unwatermarked LLM outputs as watermarked. The paper does not report detection scores for unwatermarked LLM outputs, so we cannot determine how much of the detected signal comes from the watermark instruction vs. the model's baseline generation tendencies. For Initials ICW specifically, the detection z-statistic uses γ estimated from the Canterbury Corpus; if GPT-o3-mini's natural word-initial-letter distribution deviates from this baseline, unwatermarked outputs could produce inflated z-scores. This gap affects the interpretability of the central detection claims for three of four methods. (Unicode ICW is immune since it detects a physically inserted character.)

- **The "scales with capability" claim is supported by only two models from one provider**: The paper's motivating thesis is that ICW effectiveness depends on LLM capability and will improve as models advance. The evidence is a single comparison between GPT-4o-mini and GPT-o3-mini — two models from the same provider and family. This does not distinguish between "ICW works because o3-mini is more capable" and "ICW works because of OpenAI-specific instruction-tuning choices." Testing across at least one model from a different provider would be needed to support the general capability-scaling claim.

### Minor

- **Text quality evaluation is partially circular**: The LLM-as-Judge uses gemini-2.0-flash to rate GPT-o3-mini outputs. Table 3 shows unwatermarked GPT-o3-mini substantially outscoring human text (4.992 vs. 4.235), indicating systematic judge preference for AI-generated text. While the relative comparison between ICW methods and unwatermarked outputs is still informative (the key comparison), this circularity should be acknowledged and ideally supplemented with a reference-based metric.

- **IPI setting evaluated only under best-case conditions**: The IPI experiments feed the entire paper to the LLM. In practice, a reviewer might copy only an abstract or specific sections, use an interface that strips formatting, or extract plain text — any of which could cause the watermark instruction to be lost. The paper does not test these realistic failure modes. Additionally, the Unicode ICW performance drop from DTS (1.000 ROC-AUC) to IPI (0.857) with GPT-4o-mini in Table 2 is a substantial degradation that receives no discussion, and may hint at context-length or instruction-burial effects relevant to other methods.

### Trivial

- The paper would benefit from reporting descriptive statistics on how often the LLM actually conforms to each watermarking instruction (e.g., proportion of green-initial words for Initials ICW, exact match rate for Acrostics ICW). This would make the detection mechanism more transparent.

## Nice-to-Haves

- Testing on at least one non-OpenAI model (Claude, Gemini, or an open-weight model) to strengthen the capability-scaling claim.
- For the IPI setting, reporting results under partial-document scenarios (abstract only, random 50% of the paper).
- Supplementing text quality evaluation with a reference-based metric (e.g., BERTScore against ELI5 reference answers).
- Discussing and explaining the Unicode ICW performance drop from DTS to IPI with GPT-4o-mini.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **[Removed] Harsh Critic claimed the detection evaluation lacks negative control for Unicode ICW.** REMOVED: Unicode ICW detects a physically inserted character (zero-width space), so the distinction from unwatermarked text is trivial — if the character is present, it was watermarked. The critic themselves acknowledged this exemption.

2. **[Removed] Harsh Critic suggested the Lexical ICW vocabulary restriction (excluding nouns) is a fundamental limitation.** REMOVED: The paper explicitly discusses this design choice in Section 4.2.3, citing prior work (Liang et al., 2024a; Lin et al., 2023) as justification. This is a deliberate design choice with acknowledged rationale.

3. **[Removed] Harsh Critic noted that the Appendix provides theoretical guarantees not verifiable from main text.** REMOVED per hard rule: missing appendix is a parser artifact; the original submission includes Appendix B. Do not penalize for stripped appendices.

4. **[Removed] Harsh Critic claimed the introduction states that major LLM providers do not publicly use watermarks "without citation."** REMOVED: The critic themselves says "this is not central enough to warrant a major objection." This is a minor factual claim in the introduction, not core to the paper's contribution.

5. **[Removed] Strength Finder claimed "Compelling capability-scaling evidence" as an unqualified strength.** DOWNSHIFTED: This is partially valid (the stark gap between GPT-4o-mini and GPT-o3-mini is indeed interesting) but the claim overreaches given only two models from one provider. Retained as a qualified observation in the strengths section rather than as standalone evidence of a general trend.

6. **[Removed] Strength Finder claimed "Principled detection with statistical guarantees" as a standalone strength.** PARTIALLY RETAINED: The detection methodology is sound in principle, but the missing unwatermarked baseline weakens the practical interpretation. Merged into the broader detection discussion.

## Novel Insights

None beyond the paper's own contributions. The core insight — that modern LLMs' instruction-following capabilities can be repurposed for watermarking without model access, including through covertly embedded instructions in documents — is the paper's contribution, and the reviews confirm its novelty in the watermarking landscape.

## Suggestions

- **Add unwatermarked LLM outputs as a negative class in all detection experiments.** This is the single most important addition: for each ICW method and model, report detection ROC-AUC when the negative class is unwatermarked LLM text (same prompts, no watermark instruction). This directly tests whether the watermark signal comes from the instruction or from the model's natural generation tendencies. This can be addressed in rebuttal with a straightforward additional experiment.
- **Qualify the capability-scaling claim** or broaden model coverage. The current claim should be softened to reflect the limited model set, or supplemented with at least one non-OpenAI model.
- **Acknowledge the text quality evaluation circularity** explicitly and note that the relevant comparison is relative (ICW vs. unwatermarked) rather than absolute.
- **Discuss the Unicode ICW performance drop** from DTS to IPI with GPT-4o-mini — this anomaly in Table 2 deserves attention.

## Anchor Comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | 1 | Our paper is much stronger — more novel problem, creative IPI setting, broader method exploration, stronger results |
| eKGEsFdpin (Sampling Watermarking) | 3.67 | 1 | Our paper is clearly stronger — tackles a fundamentally different, more novel problem (no model access) |
| r6aX67YhD9 (RL Watermarking) | 4.75 | 2 | Our paper is stronger — more practical (no training needed), more creative motivation, stronger results with gpt-o3-mini |
| 0KHW6yXdiZ (End-to-End Logits WM) | 5.25 | 2 | Our paper is comparable but more novel in approach; both have evaluation limitations |
| FDfq0RRkuz (WASA) | 5.50 | 1 | Most similar in contribution profile — both have a good idea with some evaluation gaps. Our paper has broader method exploration and more creative framing (IPI) |
| KRMSH1GxUK (WM IP Infringement) | 5.80 | 2 | Our paper is comparable — slightly weaker evaluation rigor but more creative problem framing |
| DEJIDCmWOz (Reliability of WMs) | 6.00 | 2 | Our paper is more novel but evaluation is less rigorous (unwatermarked baseline gap). Slightly below |
| LdIlnsePNt (Semantic-aware WM) | 6.00 | 2 | This paper combines theory + practice; our paper doesn't have theoretical depth but has more practical creativity. Slightly below |

**Round-1 bracket: 3.5–7.5 → narrowed to 5.0–6.0 after round 2.** The paper is most comparable to WASA (5.50) — both introduce a genuinely novel watermarking angle with some evaluation limitations. Our paper edges slightly above WASA in creativity and breadth of methods, but shares the evaluation gap concern. The paper is below the 6.00 anchors which have more rigorous evaluation. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>