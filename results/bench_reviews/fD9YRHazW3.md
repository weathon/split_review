Now I have sufficient calibration. Let me write the final review.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for LLM watermarking that operates entirely through prompt engineering and in-context learning, requiring no access to the model's decoding process, logits, or weights. The authors propose four strategies at different granularities — Unicode, Initials, Lexical, and Acrostics ICW — each paired with a detection scheme. They evaluate these in the Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study targeting AI misuse detection in peer review. Experiments on GPT-o3-mini show near-perfect detection (ROC-AUC ≥ 0.995) and strong robustness, demonstrating the feasibility of the concept.

## Strengths

- **Genuinely novel paradigm shift for LLM watermarking.** All prior watermarking methods require either model-internal access (logits, decoding) or post-hoc text modification. ICW shows that watermarking can be achieved purely through instruction-following and in-context learning — a conceptual departure that opens a new research direction. The paper provides clear evidence of this with GPT-o3-mini: Initials ICW achieves ROC-AUC 0.999, Lexical 0.995, and Acrostics 1.000 in the DTS setting (Table 2).

- **Systematic exploration of four watermarking strategies across multiple axes.** The paper proposes Unicode, Initials, Lexical, and Acrostics ICWs, evaluates trade-offs among LLM requirements, detectability, robustness, and text quality (Table 1), and confirms these trade-offs experimentally. Strategies span character-level (Unicode), word-initial-letter (Initials), vocabulary (Lexical), and sentence-level (Acrostics) granularities. This structured taxonomy frames the design space well.

- **Comprehensive robustness evaluation.** The methods are tested under random deletion (30%), synonym replacement (30%), and LLM paraphrasing attacks (Tables 5, 6). Under paraphrase on GPT-o3-mini, Initials ICW holds at ROC-AUC 0.887, Lexical at 0.924, and Acrostics at 0.922, often exceeding baselines like PostMark (0.841). Ablation studies on context length (10-turn conversations) and output length (1000 words) confirm detection remains ≥ 0.995 (Tables 7, 8).

- **Honest framing of limitations.** The paper explicitly notes that the green letter set for Initials ICW "can be easily inferred, making the method vulnerable to spoofing attacks" (Sec. 4.2.2), that effectiveness depends on LLM capability, and that current methods are limited by instruction-following reliability (Sec. 6). The "initial exploration" framing is appropriate and well-maintained.

## Weaknesses

### Fatal
None.

### Major

1. **Model dependence sharply limits current applicability.** On GPT-4o-mini (a capable 2024 model), Initials ICW achieves ROC-AUC 0.572 and Acrostics 0.590 in the DTS setting — essentially random. Lexical ICW (0.910) fares better but still well below GPT-o3-mini's 0.995. The paper frames this as "expected to improve as models advance," which is honest but concedes that ICW provides no practical solution for the vast majority of current LLM deployments. Since the IPI motivation (peer review) cannot control which model a reviewer uses, this dependence is a serious practical barrier.

2. **The "watermarking" framing is strained because keys are publicly inferable.** For all four strategies, the "secret key" is observable from a single watermarked text instance — the Unicode character, the green letter set, the green word list, and the acrostic key sequence are all trivially extractable. The detection test cannot distinguish between text genuinely watermarked by the instruction and text intentionally mimicked by an adversary who has seen one watermarked sample. The paper acknowledges this for Initials ICW (vulnerability to spoofing, Sec. 4.2.2) but does not adequately address what it means for the overall claim: the scheme is closer to prompt-engineered style steering with a detectable statistical footprint than to a key-based watermark. This does not invalidate the paper's core feasibility result, but it does weaken the contribution relative to the paper's framing.

3. **No empirical false positive rate calibration on human text.** The paper provides a theoretical false-alarm guarantee for Initials and Lexical ICWs (Appendix B) adapted from Zhao et al. (2023a), assuming i.i.d. letter/word distributions. However, real text distributions vary by topic, author, and genre, breaking this assumption. The paper reports ROC-AUC and TPR@fixed-FPR, which implicitly use the validation data to set thresholds, but does not report the empirical FPR on a held-out corpus of natural human text. Without this, the reported TPR@1%FPR numbers may not reflect actual operating characteristics in deployment.

### Minor

1. **The IPI case study, while motivated well, has unaddressed practical failure modes.** The paper does not evaluate what happens when: (a) reviewers use models that filter invisible characters or strip formatting, (b) the instruction exceeds the model's effective context window (papers can be very long), or (c) the reviewer notices the invisible text (trivial via select-all). The paper tests an "ignore prior prompts" attack (Table 11) where ICW still works, but does not systematically study these other threat vectors. For a claimed "case study," this is a gap.

2. **Baseline comparison lacks context for the key trade-off.** The paper compares ICW against PostMark and YCZ+ (post-hoc methods) and GPTZero, showing comparable or better detection. However, the natural baseline for the DTS setting is in-process watermarking (Kirchenbauer et al., Aaronson, etc.), which achieves similar detection with provable FPR control and strong robustness. The paper avoids this comparison because those methods require model access — which is precisely the point: the reader cannot evaluate the quality/robustness/deployability trade-off of giving up model access. Including such a comparison (even as an upper bound) would contextualize what ICW sacrifices.

3. **Acrostics ICW detection procedure needs better justification.** The detector estimates the null distribution's mean and standard deviation by resampling sentence-initial letters from the *same suspect text* being tested (Sec. 4.2.4). If the text is watermarked, the resampled sequences inherit the watermark's bias toward the key sequence, making the test conservative (less likely to detect). While this does not create false positives, the procedure is not rigorously validated against a proper independent null distribution.

4. **Limited model diversity.** Only two models (both from OpenAI) are tested. An evaluation on at least one open-weight model (e.g., Llama-3-70B or Qwen2.5) would strengthen the paper's claims about model-dependence, especially since GPT-o3-mini is a reasoning model that may behave differently from standard chat models.

### Trivial
None that survive the removal rules.

## Nice-to-Haves

- A comparison with in-process watermarking methods (as an oracle upper bound) to quantify what is sacrificed by giving up model access.
- Empirical FPR validation on a large corpus of natural human text (e.g., Wikipedia, news).
- A discussion of how the IPI instruction could survive cross-platform text processing (copy-paste, PDF extraction, formatting stripping).
- Testing on an open-weight model (e.g., Llama-3-70B) to verify the model-dependence claim outside the OpenAI ecosystem.

## Removed Points

These points were identified as invalid, strawman, or parser artifacts by the verification process. They are retained here for traceability but should be treated with caution:

- **Criticism that IPI setting requires "the reviewer to use the specific LLM the organizer expects"** — the paper's IPI experiments test two models and show performance varies by model capability, which the paper explicitly acknowledges. The criticism that this invalidates the case study is overstated; the paper frames it as an exploration, not a production-ready solution.
- **Criticism that the Acrostics detection procedure is "circular"** — The resampling approach is actually conservative (less likely to detect watermarks), not invalid. The procedure creates permutations of the observed sentence-initial letters, which breaks alignment with the key sequence even in watermarked text. This is a reasonable heuristic, not a methodological flaw.
- **Claims that comparison to PostMark/YCZ+ is "inappropriate"** — PostMark and YCZ+ are black-box post-hoc methods, the only class of methods applicable in settings where the detector has no model access. The comparison is appropriate given the setting; the paper could additionally include in-process methods as an oracle, but the current comparison is not misleading.
- **Claims about missing confidence intervals and trials** — The paper states 500 watermarked and 500 human texts each of 300 words, and the use of ROC-AUC as an aggregate metric across these samples is standard for this literature.
- **Claims about GPTZero comparison lacking detail** — The paper provides TPR@4%FPR comparison in Table 9 (Appendix D.1).
- **Formatting/style nitpicks and missing appendix content** — These are parser artifacts from PDF extraction and do not reflect the original submission.

## Novel Insights

The most interesting observation to emerge across the reviews is a question the paper raises but does not fully answer: what is the *fundamental* relationship between instruction-following capability and watermark detectability? The paper's model-dependence results suggest that watermarking through prompts is not simply about designing better instructions — it requires a threshold of in-context learning ability that current models are only beginning to cross. This points to a deeper question: as LLMs become better at following complex instructions, does the space of prompt-based statistical watermarking expand naturally with model capability (as the paper suggests), or does it asymptotically hit a ceiling because instruction-following and statistical bias are fundamentally at odds? The paper's "treating ICW as a new alignment task" suggestion (Sec. 6) is one way to address this, but it also undermines the model-agnostic claim. This tension — between the model-agnostic promise of ICW and its demonstrated model-dependence — is the paper's most provocative finding and deserves deeper investigation.

## Suggestions

- Devote a section or table to the question: what properties does a "watermark" need (key secrecy, spoofing resistance, robustness, FPR control), and which does ICW satisfy vs. fail? The paper currently acknowledges shortcomings piecemeal but would benefit from a systematic accounting.
- Add an empirical FPR calibration experiment on a large corpus of human-written text (e.g., 10K Wikipedia articles) with the proposed detection thresholds. This is critical for any deployment claim.
- To strengthen the IPI case study, test a realistic pipeline: embed the instruction as white/invisible text in a PDF, have the LLM process the PDF (not just stripped text), and measure watermark survivability.
- Clarify the Acrostics detection procedure's null distribution: either switch to an independent reference corpus for mean/standard deviation estimation, or provide a theoretical argument that the resampling-from-suspect-text approach is valid.
- Add at least one open-weight model (e.g., Llama-3-70B) to demonstrate whether the model-dependence claim generalizes beyond GPT models.

## Score and Decision

**Calibration Anchors** (from human reviews corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| Windtalkers (US1UwMHHtS.md) | 3.00 | Weaker — confused framing, missing baselines. ICW is more novel and better executed. |
| p-Mark (0hnnPy6vt2.md) | 2.00 | Much weaker — misleading title, poor theory. ICW is substantially stronger. |
| Benchmark Contamination (WFGxFzFDmQ.md) | 5.00 | Similar tier — both explore novel applications of watermarking with decent experiments but have limitations that warrant rejection. ICW is more conceptually novel. |
| OpenStamp (DU5eTaQSHT.md) | 5.00 | Similar tier — both address gaps in watermarking scenarios with reasonable experiments. ICW has more novel methodology but less statistical rigor. |
| Watermarking Diffusion LMs (3aBWTYGcaT.md) | 5.00 | Similar tier — both extend watermarking to new settings with moderate empirical validation. The DLM paper was accepted (poster), but has a split review (one 8, three 4s). |
| LLM Fingerprinting (t38nZqqi3Z.md) | 6.50 | Stronger — more thorough evaluation, broader attack coverage, clearer practical path. ICW is less mature. |

The paper introduces a genuinely novel concept — watermarking through prompt engineering — that existing work has not explored. The experiments are reasonably extensive for an initial exploration and demonstrate feasibility with strong models. However, the contribution is tempered by: (1) severe model-dependence that limits current applicability, (2) the lack of key secrecy (the "watermark" pattern is publicly inferable), which strains the watermarking framing, and (3) absent empirical FPR calibration. These limitations are acknowledged by the paper but remain significant enough that the work — in its current form — falls short of acceptance at a top venue. The paper is a solid exploratory contribution that would be well-suited for a workshop or as a starting point for a more rigorous full-length treatment.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>