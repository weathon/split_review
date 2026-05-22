Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper introduces In-Context Watermarking (ICW), a novel paradigm that embeds watermarks into LLM-generated text solely through prompt engineering, without requiring access to model internals or post-hoc editing. Four strategies at different granularities (Unicode, Initials, Lexical, Acrostics) are proposed, each with a tailored detection method. The paper also introduces the Indirect Prompt Injection (IPI) setting as a case study for detecting AI-generated peer reviews. Experiments with GPT-o3-mini show near-perfect detection (AUC ≥ 0.995 for all four methods), with competitive text quality and robustness compared to post-hoc baselines.

## Strengths

1. **Genuinely novel paradigm for LLM watermarking** — The paper is the first to systematically study watermarking through prompt engineering alone, without modifying the decoding process or requiring model access. This opens a new axis of watermarking research that is distinctly different from both in-process (logit-modifying) and post-hoc (text-modifying) approaches.

2. **Impressive detection results with capable models** — Table 2 shows that with GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in both the DTS and IPI settings (e.g., Acrostics ICW AUC = 1.000 in DTS, Unicode ICW AUC = 1.000 in IPI). These results substantiate the central claim that ICW is feasible with sufficiently capable instruction-following models.

3. **IPI setting is genuinely novel and well-motivated** — Section 3.2 and Figure 2 describe a covert watermarking scenario (e.g., white text in PDFs) where reviewers unknowingly produce watermarked reviews. As the paper notes, this is a scenario where all existing baselines (YCZ+23, PostMark, GPTZero) are explicitly inapplicable (Section 5.1), making this a meaningful extension of the watermarking application space.

4. **Strong robustness to paraphrasing** — Figure 3 shows Initials (AUC 0.887), Lexical (AUC 0.924), and Acrostics (AUC 0.922) ICWs significantly outperform YCZ+23 (AUC 0.557) and PostMark (AUC 0.841) under paraphrasing attacks with GPT-o3-mini, demonstrating that the in-context signal survives rewriting better than post-hoc embeddings.

5. **Favorable text quality compared to baselines** — Table 3 shows ICW methods (e.g., Acrostics ICW Overall = 4.813) score much closer to unwatermarked text (4.992) than PostMark (2.997) and YCZ+23 (3.865) in LLM-as-a-Judge evaluation, with all ICW methods outperforming PostMark in every dimension.

6. **Systematic trade-off analysis across four strategies** — Table 1 and the performance gap between GPT-4o-mini and GPT-o3-mini (Table 2) provide concrete evidence that ICW effectiveness scales with LLM instruction-following capability, supporting the forward-looking claim that ICW will improve as models advance.

## Weaknesses

### Fatal
None.

### Major

1. **Detection evaluation uses human text as the negative class instead of unwatermarked LLM output** — The paper's detection evaluation (Section 5.1, line 200) uses 500 human-generated texts (from ELI5) as the negative class. However, the hypothesis test in Section 3.1 (line 84) defines H0 as "the text is generated without the knowledge of k and τ," which should encompass *LLM-generated text without the watermark instruction*. This conflation means the reported ROC-AUC values may reflect general AI-text detection rather than watermark-specific signal. For the z-statistic methods (Initials and Lexical ICW), the null distribution is estimated from the Canterbury Corpus (human text, line 151), making the theoretical false alarm rate guarantee contingent on the unvalidated assumption that unwatermarked LLM output follows the same letter/word distribution as human-written text. A proper evaluation should include unwatermarked LLM responses (same models, same queries) as the negative class. This is the single most important gap in the paper's evidence.

2. **IPI setting evaluated only under idealized simulation, not realistic document injection** — The IPI evaluation (Section 3.2, line 96) uses direct concatenation of the watermarking instruction to the paper text: `t̃ = t ⊕ Instruction(k, τ)`. The paper mentions obfuscation methods like white text and zero-font-size text (line 100) but never implements or tests any of them. No experiment demonstrates that the instruction survives PDF-to-text extraction (e.g., via `pdftotext` or PyMuPDF) and is still executed by the LLM. Since the IPI setting is the paper's most distinctive contribution and a key claimed advantage over baselines, this gap is significant. The contribution should be positioned as a simulation-based feasibility study rather than a validated practical method.

### Minor

3. **Experiments limited to two proprietary OpenAI models** — Only GPT-4o-mini and GPT-o3-mini are tested (Section 5.1, line 190). Both share architecture and training methodology from a single provider. The claim that ICW is "model-agnostic" (abstract) is a design property, not an empirical finding. Without testing on at least one open-weight model (e.g., LLaMA-3, Mistral) to confirm that the effect generalizes beyond the OpenAI ecosystem, the generality of ICW remains an open question. This is particularly consequential because GPT-4o-mini fails on the more linguistically demanding methods (Initials and Acrostics AUC ~0.57-0.59), suggesting strong sensitivity to model-specific instruction-following traits.

4. **Acrostics ICW is not "invisible" to a careful reader** — The paper describes ICW as generating "invisible watermark[s]" (line 35, 41, 80) and states "Initials ICW is invisible to humans" (line 153). While Unicode and Initials ICW are genuinely imperceptible, Acrostics ICW — where successive sentences begin with letters that spell out a secret string — is readily visible to any attentive reader. This does not invalidate the method (it could still be useful for automated detection) but the categorical "invisible" claim is misleading for this strategy.

5. **Theoretical false alarm rate guarantee is untested against unwatermarked LLM output** — The paper claims "theoretical guarantee on controlling the false alarm rate" (line 168) for Initials and Lexical ICW. The guarantee is derived from a normal approximation based on human-text statistics. Whether the empirical false positive rate on actual unwatermarked LLM output matches the theoretical rate is never examined. If the distributions diverge (likely due to correlated word choices in LLM output), the detection thresholds are not reliable for real use.

### Trivial
None.

## Nice-to-Haves

- Include an evaluation of unwatermarked LLM output (same query distribution) as the negative class for detection, which would directly support the watermark claim.
- Test the IPI setting end-to-end with at least one realistic obfuscation method (e.g., white text embedded in a LaTeX PDF, extracted via `pdftotext`).
- Evaluate on at least one open-weight model family (e.g., LLaMA-3-70B, Mistral-Large) in the DTS setting.
- Ablate the vocabulary set choice for Lexical ICW (adjectives/adverbs/verbs vs. other word classes) to understand its effect on detection and quality.
- Show example watermarked vs. unwatermarked responses side-by-side to help readers assess semantic impact.
- Add a calibration plot showing empirical FPR vs. threshold for the z-statistic methods on unwatermarked LLM output.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Acrostics ICW detection uses circular null distribution (Harsh Critic point 3)**: The critic claims resampling sentence-initial letters from the suspect text itself is "circular." This is incorrect — the method is a permutation test that destroys the sequential structure that the detection relies on, which is a standard statistical approach. The permutation test conditions on the observed letters but randomizes their order, so the null mean reflects the expected Levenshtein distance under random ordering, which is appropriate. **REMOVED (factually incorrect).**

- **"No evaluation on models beyond two OpenAI API endpoints" framed as structural/fatal**: The critic frames this as a fatal weakness. While limited model diversity is a genuine limitation (retained as Minor weakness #3 above), critic overstates it as threatening the core claim. The paper transparently positions ICW as dependent on LLM capability and uses two models specifically to demonstrate this dependency. **Demoted from Harsh Critic's framing to Minor weakness.**

- **Weakness about adaptive adversaries not being tested**: The critic criticizes the robustness evaluation for not including "informed" adversaries who know the scheme. The paper acknowledges this limitation in Section 6 ("we discuss the limitations of current ICW methods under a potential attack"). This is a nice-to-have improvement, not a core weakness. **Demoted to Nice-to-Have territory.**

- **Critic's claim that Section 5.2.1 "downplays" GPT-4o-mini failures**: The paper explicitly states "effectiveness depends on the capabilities of the underlying LLMs" and shows the results in Table 2. The critic claims this "downplays" the failure, but the paper is transparent about it and uses the contrast to demonstrate the capability-dependent nature of ICW. **REMOVED (paper already addresses).**

- **Strength Finder claim about "theoretical false-alarm rate guarantees"**: Retained in Strengths but should be noted as contingent on an unvalidated null assumption. The paper claims this but the details are in the (unavailable) appendix, and the guarantee is against human-text statistics rather than LLM output statistics. **Retained in Strengths with caveat in Weaknesses.**

- **Generic strengths from Strength Finder**: "Comprehensive exploration of strategies" and "Code release" are generic, superficial strengths, or redundant with the stronger strengths listed above. **REMOVED.**

## Novel Insights

None beyond the paper's own contributions. The key insight — that watermarking can be achieved purely through prompt engineering by exploiting instruction-following capabilities — is the paper's own. The reviewer inputs did not surface a genuine novel observation that the paper itself missed.

## Suggestions

1. **Add an experiment with unwatermarked LLM output as the negative class.** Run the same models (GPT-o3-mini, GPT-4o-mini) on the same ELI5 queries *without* the watermarking instruction, and report ROC-AUC, T@1%F, T@10%F for discrimination between watermarked and unwatermarked LLM output. This is the most important experiment to add.

2. **Validate the IPI setting end-to-end.** Pick one realistic obfuscation method (e.g., white text in a LaTeX PDF), embed the watermarking instruction, extract the text with common tools, and verify that the instruction survives and is executed by the LLM.

3. **Test one open-weight model** (e.g., LLaMA-3-70B or Mistral Large) in the DTS setting to demonstrate generalizability beyond the OpenAI ecosystem.

4. **Calibrate the z-statistic thresholds.** For Initials and Lexical ICW, compare empirical false positive rates on unwatermarked LLM output against the theoretical normal approximation, and report the discrepancy if any.

5. **Rephrase the "invisible" claim** for Acrostics ICW to acknowledge that it is visible to a careful reader, and distinguish it from the genuinely imperceptible Unicode and Initials methods.

## Score and Decision

**Calibration anchors:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| High | ujpAYpFDEA.md (Can Watermarked LLMs be Identified...) | 7.50 | Accepted. Well-organized, comprehensive evaluation across watermarking methods and LLMs. The ICW paper has a more novel core idea but weaker evaluation breadth. |
| Medium | FDfq0RRkuz.md (WASA) | 5.50 | Rejected. Watermark-based source attribution. ICW has stronger novelty but similar evaluation gaps (human text vs. unwatermarked LLM null). |
| Medium | r6aX67YhD9.md (RL Watermarking) | 4.75 | Rejected. Training-based approach with limited novelty. ICW is more novel and has stronger results. |
| Low | eKGEsFdpin.md (Sampling Watermark) | 3.67 | Rejected. Too similar to Kirchenbauer et al. ICW is clearly more novel. |
| Low | jbfDg4DgAk.md (Sparse Watermarking) | 3.00 | Rejected. Limited novelty, missing baselines. ICW is much stronger. |
| Low | 8o6LdeVi1K.md (WAPITI) | 3.75 | Rejected. Limited novelty, evaluation gaps. ICW has stronger novelty. |

The paper introduces a genuinely novel idea with impressive preliminary results on a capable model. However, the evaluation has a significant gap: using human text rather than unwatermarked LLM output as the detection negative class, which conflates watermark detection with AI-text detection. The IPI setting is not validated with realistic obfuscation, and only two proprietary models are tested. These gaps prevent the paper from fully establishing its claims at the level of the 7.50 anchor, though the contribution is substantially more novel than the 3.67–5.50 anchors.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>