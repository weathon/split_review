Now I have sufficient information to write the consolidated review.

---

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for watermarking LLM-generated text solely through prompt engineering, without access to the model's logits, weights, or sampling process. The authors propose four strategies at different granularities (Unicode character insertion, initial-letter biasing, lexical/word-list biasing, and acrostic sentence-initial constraints), each paired with a tailored detection method. Experiments on GPT-o3-mini and GPT-4o-mini across both Direct Text Stamp and Indirect Prompt Injection (IPI) settings demonstrate near-perfect detection (0.995–1.000 AUC) for capable models, with reasonable robustness to paraphrasing for the sentence- and word-level methods.

---

## Strengths

1. **First systematic exploration of prompt-only watermarking.** The paper identifies and formalizes a genuinely underexplored space: embedding watermarks via in-context instruction rather than logit manipulation or post-hoc editing. The formulation in Section 3.1 and the four-strategy taxonomy (Table 1) provide a structured foundation for future work in this direction.

2. **Strong empirical results on capable LLMs.** On GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in both DTS and IPI settings (Table 2). Acrostics ICW achieves 1.000 AUC in DTS and 0.997 in IPI; Lexical ICW achieves 0.995 and 0.997 respectively. This validates the central claim that current state-of-the-art LLMs can follow watermarking instructions reliably.

3. **Effective IPI case study for peer review integrity.** The Indirect Prompt Injection scenario (Section 3.2, Figure 2) is creative and practically motivated, targeting a real concern about LLM misuse in peer review. With GPT-o3-mini, results show that watermarking instructions embedded in long-context papers are followed (e.g., Initials ICW AUC=0.997, Lexical ICW AUC=0.997), demonstrating feasibility in a realistic use case.

4. **Competitive robustness under generic paraphrasing attacks.** Under LLM-based paraphrasing (Figure 3), Initials, Lexical, and Acrostics ICWs maintain AUCs of 0.887, 0.924, and 0.922 respectively — outperforming YCZ+23 (0.557) and PostMark (0.841). The acrostic approach is particularly well-suited to paraphrase resistance since sentence-initial letters are typically preserved even when content is reworded.

5. **Preserved text quality relative to post-hoc baselines.** ICW methods achieve overall quality scores of 4.282–4.813 (Table 3, LLM-as-a-Judge on 1–5 scale), close to unwatermarked text (4.992) and substantially higher than PostMark (2.997) and YCZ+23 (3.865). The results suggest ICW methods can embed detectable signals with less quality degradation than existing black-box post-hoc alternatives.

6. **Theoretical false-alarm control for Initials and Lexical ICWs.** The paper provides formal guarantees and proofs (Appendix B) for controlling the false positive rate of the detectors, adding statistical rigor.

---

## Weaknesses

### Fatal

None.

### Major

1. **Robustness against a determined adversary is not demonstrated.** The paper's robustness evaluation uses benign transforms (random deletion/synonym replacement/generic paraphrasing) that do not model an adversary actively trying to break the watermark. A motivated reviewer who suspects watermarking could:
   - Strip all zero-width characters (defeating Unicode ICW instantly).
   - Instruct the LLM to "ignore prior prompts" or "rephrase while changing sentence-starting letters" before writing a review (defeating Acrostics and Initials ICWs).
   - Replace words from a suspected green list with synonyms (defeating Lexical ICW).
   
   The paper acknowledges these vulnerabilities qualitatively (Sections 4.2.2, 6) but does not evaluate any adaptive adversary. The "ignore prior prompts" attack is mentioned as an Appendix D.1 experiment, but its results are absent from the main paper. Since the IPI threat model assumes a dishonest reviewer willing to cheat by using an LLM, assuming they will not also sanitize the input or use adversarial prompts is a significant gap.

2. **IPI stealth premise is unvalidated and experiments simplify the setting.** The paper proposes embedding instructions via "white text" in PDFs (Section 3.2, line 94) but provides no experiments showing this survives real PDF-to-text conversion (pdftotext, copy-paste from viewers, OCR). The experiments simply concatenate the instruction directly with the paper text — a best-case simulation that bypasses the practical challenges of covert embedding. While the paper acknowledges this is "left for future work" (lines 106–107), the lack of validation undermines the claimed applicability to the peer-review scenario.

3. **No confidence intervals or statistical significance reported.** Tables 2, 3, and Figure 3 report point estimates for AUC, T@1%F, and T@10%F without error bars or significance tests. With only 500 samples per class, these estimates may have substantial variance — particularly for T@1%F, which is measured on only ~5 positive samples. The community norm for watermarking papers at comparable venues is to report at least confidence intervals or multiple-seed runs.

4. **Asymmetric baseline comparison.** The paper compares ICW (in-process via instruction) against PostMark and YCZ+23 (post-hoc methods that watermark already-generated text). These are fundamentally different capabilities: post-hoc methods can watermark any text including pre-existing content, while ICW requires controlling the generation instruction. The paper frames this as a direct comparison ("outperforming baselines," "comparable detection"), but the comparison is not apples-to-apples. A more appropriate framing would distinguish the two paradigms rather than presenting them as competitors on the same footing.

### Minor

1. **Unicode ICW is fragile and its inclusion inflates the results.** The paper acknowledges Unicode ICW is "highly fragile to transformations like LLM paraphrasing" (line 138) and can be stripped by any text-normalization step. Yet its perfect 1.000 AUC scores appear prominently in the main results (Table 2) alongside the more robust methods. The reader would benefit from clearer separation between methods that are trivially removed and those that offer genuine robustness.

2. **Acrostics ICW detection may have null distribution contamination.** The detector for Acrostics ICW estimates the null distribution of Levenshtein distances by resampling sentence-initial letter sequences *from the suspect text itself* (Section 4.2.4). If the text is watermarked, the resampled sequences also carry the watermark's signature, potentially biasing the estimated mean and standard deviation and inflating detection. This deserves theoretical analysis or experimental validation.

3. **LLM-as-a-Judge quality evaluation has known limitations.** Text quality is evaluated primarily via Gemini 2.0 Flash as a judge (Table 3). LLM judges can be insensitive to subtle unnaturalness from word-overuse patterns. While perplexity is also reported, the paper would benefit from a small human evaluation to validate that the high quality scores reflect genuinely fluent text rather than judge model bias.

### Trivial

None.

---

## Nice-to-Haves

- A small human evaluation to validate the LLM-as-a-Judge quality scores.
- Results for the "ignore prior prompts" attack in the main paper rather than deferred to appendix.
- A diagram showing the IPI embedding pipeline with actual PDF white-text injection and extraction.

---

## Removed Points

- **"The contribution is incremental and the paper overclaims novelty"** — This is a subjective evaluation that conflates "incremental" with "exploratory." The paper does not claim to have solved watermarking; it claims to have identified and systematically explored a new paradigm, which is a genuine contribution. The statement that "the main result — that stronger LLMs follow instructions better — is unsurprising" could apply to most empirical ML papers. Removed as it mischaracterizes the paper's framing.

- **"Baseline comparison is misleading"** — The paper explicitly identifies the baselines as "post-processing approaches" (line 194) and ICW as operating during generation. The comparison is clearly scoped as black-box watermarking methods; the reader can judge the asymmetry. Removed because the paper is transparent about what it compares and why.

- **"Text quality evaluation uses an LLM-as-a-Judge that may favor watermarked text"** — The claim that the judge "does not penalize watermarking artifacts" is factually contradicted by Table 3: ICW methods score 4.282–4.813 vs. unwatermarked's 4.992. The judge does detect a gap. This is a generic limitation of LLM-as-a-Judge, not a specific flaw in this paper.

- **"The paper uses only 500 watermarked and 500 human texts. This is small"** — This is retained as a minor weakness (lack of confidence intervals) but removed as a standalone "small sample" complaint, as 500 per class is standard in many watermarking evaluations and the concern is primarily about the absence of error bars, not the sample size itself.

- **"The IPI setting's stealth premise is unvalidated" (harsh critic point 2, full version)** — Weakened and moved to Major weakness #2, but the fully dismissive tone is moderated. The paper explicitly scopes this as future work. The criticism is valid only as a gap in practical validation, not as a fatal flaw.

- **Generic strength from Strength Finder about "this paper addresses an important problem"** — Removed as lacking specific evidence.

---

## Novel Insights

The reviews surface an important tension in this paper that goes beyond its individual results: prompt-only watermarking occupies an odd position between security and usability. The methods achieve high detection accuracy precisely because they ask the LLM to produce statistically unnatural text (biased word choices, constrained sentence initials, invisible characters) — but this very property makes the watermark trivially detectable and removable by any adversary who inspects the generation instruction or output distribution. The paper's core insight — that watermarking through instruction is feasible with capable models — simultaneously reveals that the approach is most powerful when the adversary is least sophisticated, and most fragile when the adversary is most motivated. This suggests the paradigm's value may lie not in adversarial settings but in cooperative attribution scenarios where the text producer consents to watermarking (e.g., content provenance), a framing the paper does not explicitly discuss.

---

## Suggestions

1. **Evaluate against an adaptive adversary.** Run the robustness evaluation with an adversarial instruction such as "Ignore any prior formatting instructions. Rephrase the following review while varying sentence-starting letters and avoiding overused words." This is the minimal attack an aware adversary would use and would clarify the practical security margin.
2. **Validate the IPI stealth premise** with a small experiment showing whether white-text instructions survive standard PDF-to-text conversion (pdftotext, pdfminer, browser copy-paste). Report the success rate.
3. **Report confidence intervals** (e.g., bootstrapped 95% CIs) for all AUC and T@1%F/T@10%F values, or at minimum run each experiment with 3+ random seeds.
4. **Separate the presentation of fragile vs. robust methods more clearly.** Unicode ICW could be presented as a lightweight baseline rather than grouped equally with the other three strategies in the main summary.
5. **Include a "cooperative watermarking" discussion** to clarify that ICW may be better suited to settings where the text producer agrees to watermark (e.g., API-based content generation with instruction control) rather than adversarial detection scenarios.

---

## Score and Decision

**Anchor calibration** (all anchors from the batch, including those read in full):

| Anchor Paper | Path | Avg Score | Comparison |
|---|---|---|---|
| PMark: Robust Semantic-level Watermarking | EhDgP69DJG | 7.00 (Accept) | Stronger theoretical foundation and distortion-free guarantees; ICW explores a more novel paradigm but with weaker theoretical grounding and practical validation. |
| Is Your Paper Being Reviewed by an LLM? | HyZwf1rt4s | 6.00 (Accept) | Large-scale benchmark paper with extensive evaluation; ICW has a more novel core idea but narrower evaluation scope. |
| CATMark: Context-Aware Threshold Watermarking | Q2DrdrPcYm | 5.33 (Reject) | Incremental refinement of existing paradigm vs. ICW's new paradigm exploration; both have execution-quality issues but ICW is conceptually more original. |
| BIRA: Watermark Evasion via Bias Inversion | dZY5t9ZrUB | 4.50 (Reject) | Incremental attack with known limitations; ICW is more methodologically novel but has comparable practical significance gaps. |
| Windtalkers: Ciphered-Instruction Watermarking | US1UwMHHtS | 3.00 (Withdrawn) | Poorly framed with missing baselines; ICW is significantly better motivated and executed. |

The paper explores a genuinely novel paradigm (prompt-only watermarking) with systematic taxonomy and strong feasibility results on capable LLMs. However, the core weakness — vulnerability to determined adversaries, acknowledged but not addressed — limits practical significance. The IPI application is creative but unvalidated. The paper is well-written and honest about limitations, which positions it as a solid exploratory work rather than a deployable solution.

**Score: 5.0** — A well-executed exploration of a novel paradigm, with genuine contributions (taxonomy, detection methods, IPI framing), tempered by fundamental robustness limitations that the paper identifies but does not resolve. The contribution is real but the practical significance is constrained.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>