Now I have all the information I need. Let me finalize the review.

**Round 1 bracket**: Based on the calibration search, the weak anchor band (<3.5) contains papers scoring ~3.0 (basic watermarking/LLM papers with major flaws), the middle band (3.5-7.5) contains papers like EditMark (4.25, reject), WAPITI (3.75, reject), A Watermark for Black-Box LMs (4.60, reject), On the Reliability of Watermarks (6.00, accept), Ward (6.50, accept), and Black-Box Detection (7.00, accept). The strong band (>7.5) contains papers at 8.0. The ICW paper clearly sits in the middle band — above the rejected papers in the 3-4.6 range, but below the strongest accepted papers at 7+.

**Round 2 narrowing**: Within the bracket, I compared against EditMark (4.25, rejected — ICW is clearly stronger, more novel problem framing, better evaluation), A Watermark for Black-Box LMs (4.60, rejected — ICW has clearer motivation and the prompt-engineering approach is more practical), On the Reliability of Watermarks (6.00, accepted — comparable in evaluation quality, similar scope of contribution), and Ward (6.50, accepted — ICW's contribution is somewhat narrower but similarly novel). This suggests ICW sits around 5.5-6.0.

**Final calibration**: The paper is stronger than the 4-5 range rejected watermarking papers due to its genuinely novel approach and solid DTS experimental validation. It's weaker than the 6.5+ accepted papers because of the IPI evaluation gap (not testing realistic hidden-instruction embedding) and the narrow model evaluation (only two GPT models). I place it at **6.0**.

## Summary

This paper introduces In-Context Watermarking (ICW), a method for watermarking LLM-generated text solely through prompt engineering, without requiring access to model internals (logits, decoding, or sampling). The authors propose four ICW strategies (Unicode, Initials, Lexical, Acrostics) at different granularities, each with a tailored detection method. They evaluate these in a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study targeting AI-generated peer review detection. With a sufficiently capable model (GPT-o3-mini), all four methods achieve near-perfect detection (AUC ≥ 0.995) in both settings, matching or exceeding post-hoc baselines while operating in a fundamentally more practical black-box regime.

## Strengths

1. **Novel problem framing with clear feasibility evidence.** The paper identifies a genuine gap—watermarking LLM outputs without model access—and demonstrates feasibility through four distinct strategies. Table 2 shows that with GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in the DTS setting and ≥ 0.997 in the IPI setting, directly supporting the claim that ICW works without decoding access.

2. **Principled detection with false alarm guarantees.** For Initials and Lexical ICWs, the paper provides a statistical hypothesis testing framework (Section 4.2.2–4.2.3) with explicit z-statistic formulas and a theoretical guarantee on false alarm rate control (Appendix B). This is a nontrivial contribution over a simple heuristic, enabling quantitative calibration of detection thresholds.

3. **Systematic trade-off analysis across four methods.** Table 1 presents a clear qualitative summary comparing the four ICW strategies across LLM requirements, detectability, robustness, and text quality. Tables 2–3 and Figure 3 empirically validate these trade-offs—e.g., Unicode ICW achieves perfect detection with minimal LLM requirements but zero robustness to paraphrasing, while Initials ICW maintains AUC=0.887 under paraphrase attack.

4. **Empirical validation of the scaling hypothesis.** The contrast between GPT-4o-mini and GPT-o3-mini (Table 2) is striking: Initials ICW jumps from 0.572 to 0.999 AUC in DTS, and Acrostics from 0.590 to 1.000. This controlled comparison provides concrete evidence for the paper's central thesis that ICW effectiveness grows with model capability.

5. **Robustness evaluation under realistic attacks.** Figure 3 evaluates three distinct attack types (word deletion, replacement, paraphrasing). Initials ICW achieves AUC=0.999 under both deletion and replacement attacks, and 0.887 under paraphrasing—competitive with or exceeding YCZ+23 (AUC=0.557 under paraphrase) and PostMark (AUC=0.841 under paraphrase).

## Weaknesses

### Fatal

None.

### Major

1. **IPI experiments do not test the realistic covert-embedding scenario.** The paper motivates ICW with a peer-review scenario where conference organizers embed invisible watermarking instructions into PDF manuscripts (e.g., white text, zero-opacity characters, as described in Section 3.2). However, the IPI experiments simply concatenate the watermarking instruction as *visible* text with the paper document. This tests whether the LLM follows an instruction embedded within a long document, but it does *not* test whether the instruction survives PDF parsing or whether the LLM processes obfuscated/hidden text at all. In a realistic deployment, the LLM may not receive the instruction if the parsing tool discards zero-opacity content or the reviewer copies visible text only. The paper acknowledges this gap ("detailed investigation of attack and defense methods is left for future work," line 101), but this is a significant gap between the claimed application and the experimental evaluation. The IPI results demonstrate potential, but not the claimed covert-embedding practicality.

### Minor

2. **Narrow model evaluation limits generality.** The paper's central thesis that ICW effectiveness scales with LLM capability is supported by only two models (GPT-4o-mini and GPT-o3-mini), both from the same provider and family. The trajectory from failure to success is consistent with the thesis but constitutes a single data point. Without testing on additional capable models (e.g., Claude, Gemini, or a capable open-weight model), the claim that ICW will *continue* to improve as LLMs advance remains speculative.

3. **No IPI comparison against post-hoc AI detectors.** The paper frames ICW as enabling detection when model access is unavailable. The IPI experiments evaluate only ICW methods, while the post-hoc baseline (GPTZero) is only tested in DTS. Since the IPI scenario is the flagship application, a comparison against watermark-free detection (e.g., GPTZero or a perplexity-based detector on the IPI reviews) would clarify ICW's added value. The paper notes these methods "often suffer from low accuracy" (introduction) but provides no IPI-specific data to substantiate this claim.

4. **LLM-as-a-Judge evaluation shows signs of systematic bias.** The judge (gemini-2.0-flash) scores unwatermarked GPT-o3-mini text at near-perfect 4.992 overall, while human text scores 4.235 (Table 3). This approximately 0.76-point gap suggests the judge may have a systematic preference for LLM output. While comparisons between watermarked and unwatermarked LLM text remain valid (both are equally affected by the bias), absolute quality comparisons against human text should be interpreted with caution.

5. **Statistical significance not reported.** ROC-AUC values in Tables 2 and Figure 3 are reported without confidence intervals or bootstrapped standard errors. With 500 watermarked and 500 human texts per condition, variance could be non-negligible, particularly for high AUC values near 1.0.

### Trivial

6. The paper reports T@1%F and T@10%F but could also report TPR at lower FPRs (e.g., 0.1%), which would be more informative for high-stakes settings like peer review where false accusations carry serious consequences.

## Nice-to-Haves
- Testing the IPI setting with actual PDF-embedded hidden instructions (white text, zero-width Unicode characters that survive PDF parsing) to validate the full threat model.
- An ablation study varying output length or instruction complexity to pinpoint *why* GPT-4o-mini fails on Initials/Lexical/Acrostics (insufficient instruction following vs. inability to maintain constraints over long outputs).
- A more detailed discussion of defenses against simple attacks like "ignore prior instructions" (currently in Appendix D but absent from the main text).

## Removed Points

- **Harsh critic #1's framing as "structural issue" / "fatal"**: The IPI evaluation gap is real but not fatal. The paper's core contribution is the ICW concept itself (watermarking through prompt engineering), which is validated by the DTS experiments. The IPI setting is a case study exploring an application. The experiments *do* test the central question of whether an instruction embedded in a long document is followed — they just don't test the additional step of covert PDF embedding. This is a significant gap for the *specific application* but does not invalidate the paper's core claims. Demoted from fatal to major.

- **Criticism about "model-agnostic" framing**: The paper uses "model-agnostic" in the standard sense of "does not require model-specific access" (common usage in the watermarking literature), not "works equally well on all models." Removed as a misreading.

- **Criticism about Lexical ICW vocabulary restriction**: The paper already explicitly discusses this trade-off in Section 5.2.2 ("Lexical ICW shows lower robustness under the replacement attack... because it relies on green words, mainly nouns, verbs, adjectives, and adverbs, which are targeted by the replacement procedure"). Removed as already addressed.

- **Criticism about missing "ignore prior prompts" results in main text**: The paper states in Section 5.2.3 (line 286) that these results are in Appendix D. This is standard practice for supplementary analyses. Removed as a presentation nitpick.

- **Strength Finder items about "importance of the problem"** : Removed as generic/superficial praise lacking concrete evidence specific to this paper.

- **Request for false positive rate at 0.1%**: This is a reasonable request but belongs in nice-to-have, not as a weakness. The paper already provides T@1%F and T@10%F, which is standard.

## Novel Insights

None beyond the paper's own contributions. The reviewers' critiques largely surface acknowledged limitations rather than uncovering fundamentally new observations about the approach.

## Suggestions

1. **Address the IPI evaluation gap**: Test the covert PDF embedding scenario directly (e.g., embed instructions as white text, zero-width Unicode, or other obfuscation methods that survive PDF-to-text extraction) and verify that LLMs process the hidden instruction. Even a small-scale validation would significantly strengthen the IPI claims.

2. **Include an IPI comparison against post-hoc AI detectors**: Add GPTZero (or a simple perplexity-based detector) to the IPI evaluation to demonstrate ICW's added value over watermark-free detection in the peer-review application.

3. **Expand model evaluation**: Add at least one capable model from a different family (e.g., Claude 3.5 Sonnet, Gemini 1.5 Pro) to support the generality of the scaling claim.

4. **Report confidence intervals**: Add bootstrapped confidence intervals for key detection metrics to assess the reliability of the reported results.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| jbfDg4DgAk.md (Sparse Watermarking) | 3.00 | R1 (low) | Weaker — less novel methodology, limited evaluation |
| 3MDmM0rMPQ.md (Inverse Prompt Engineering) | 3.00 | R1 (low) | Less directly related, weaker empirical evaluation |
| xRi8sKo4XI.md (Unsupervised Prompt Learning) | 3.00 | R1 (low) | Different domain, less comprehensive |
| eKGEsFdpin.md (Sampling Based Watermark) | 3.67 | R1 (mid) | Weaker — incremental over Kirchenbauer, limited evaluation |
| 8o6LdeVi1K.md (WAPITI) | 3.75 | R1 (mid) | Weaker — heuristic approximations, limited baselines, less clear contribution |
| qGLzeD9GCX.md (EditMark) | 4.25 | R1 (mid) | Weaker — limited experiments, incremental contribution, drafty presentation |
| 0koPj0cJV6.md (Watermark for Black-Box LMs) | 4.60 | R2 | Weaker — practicality concerns, unclear motivation, less novel framing |
| r6aX67YhD9.md (Learning to Watermark via RL) | 4.75 | R2 | Weaker — requires model tuning, less practical framing |
| DEJIDCmWOz.md (On the Reliability of Watermarks) | 6.00 | R2 | Comparable — thorough evaluation on robustness, similar contribution scope |
| KRMSH1GxUK.md (Can Watermarks Detect IP Infringement) | 5.80 | R2 | Slightly weaker — narrower contribution |
| kVrwHLAb20.md (Ward) | 6.50 | R2 | Slightly stronger — more thorough evaluation, rigorous statistical guarantees |
| E4LAVLXAHW.md (Black-Box Detection of Watermarks) | 7.00 | R2 | Stronger — rigorous statistical tests, broader scope |
| oZtt0pRnOl.md (Privacy-Preserving ICL) | 8.00 | R1 (high) | Stronger — polished, rigorous, different subfield |
| Bo62NeU6VF.md (Backtracking Safety) | 8.00 | R1 (high) | Stronger — different topic |

**Round 1 bracket**: Between ~4 and ~7.5 (clearly above the rejected 3-range papers, below 8.0 top-tier papers).

**Round 2 narrowing**: The paper is comparable to or slightly stronger than On the Reliability of Watermarks (6.00) and Can Watermarks Detect IP Infringement (5.80), but weaker than Ward (6.50) and Black-Box Detection (7.00) due to the IPI evaluation gap and narrower model evaluation.

**Final score**: 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>