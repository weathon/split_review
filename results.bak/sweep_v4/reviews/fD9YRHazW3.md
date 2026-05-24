Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

## Summary

The paper introduces In-Context Watermarking (ICW), a method to embed detectable watermarks into LLM-generated text entirely through prompt engineering—requiring no access to model weights, logits, or the sampling process. The authors propose four strategies at different granularities (Unicode, Initials, Lexical, Acrostics) each with tailored detection methods, and evaluate them in both a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study motivated by detecting AI-generated peer reviews. With sufficiently capable models (GPT-o3-mini), ICW achieves near-perfect detection (ROC-AUC ≥ 0.995 in DTS, ≥ 0.997 in IPI) while preserving text quality close to unwatermarked outputs.

## Strengths

- **Novel and well-motivated approach**: ICW opens a new direction for LLM watermarking—embedding watermarks solely through prompt engineering, without any privileged access to model internals. This addresses a genuine gap: existing in-process methods require decoding access, while post-hoc methods cannot be used in the IPI setting where the user (reviewer) controls the generation.

- **Demonstrated effectiveness with capable LLMs**: Table 2 shows that with GPT-o3-mini, all four ICW strategies achieve ROC-AUC ≥ 0.995 in DTS and ≥ 0.997 in IPI. Unicode ICW attains T@1%F = 1.000 in both settings, and Acrostics ICW reaches T@1%F = 0.982 in IPI. These results concretely validate that prompt-based watermarking can work in principle with state-of-the-art models.

- **Robustness advantage over post-hoc baselines under paraphrasing**: Figure 3 shows that under LLM paraphrasing attacks, Initials ICW (AUC=0.887), Lexical ICW (AUC=0.924), and Acrostics ICW (AUC=0.922) all outperform YCZ+23 (AUC=0.557) and PostMark (AUC=0.841). This is a meaningful finding since paraphrasing is a common real-world editing pattern.

- **Text quality preserved compared to post-hoc methods**: Table 3 shows ICW methods (Overall scores 4.282–4.813) substantially outperform PostMark (2.997) and YCZ+23 (3.865) on LLM-as-a-Judge evaluation, while remaining close to unwatermarked text (4.992). The methods embed watermarks without the quality degradation typical of post-processing approaches.

- **Clear comparative framework**: Table 1 provides a concise, intuitive comparison of the four ICW strategies across LLM requirements, detectability, robustness, and text quality, enabling practitioners to select methods based on their constraints.

## Weaknesses

### Fatal
None.

### Major

1. **The "model-agnostic" claim in the Abstract contradicts the paper's own findings.** The Abstract states ICW is a "model-agnostic, practical watermarking approach," but the paper's contributions explicitly note "the effectiveness of ICW is highly dependent on the capability of the underlying LLMs." Table 2 bears this out: on GPT-4o-mini, Initials ICW achieves ROC-AUC 0.572 (near random), Acrostics ICW achieves 0.590, and even Lexical ICW drops to 0.910 in DTS and 0.889 in IPI—far below the near-perfect results on GPT-o3-mini. Only Unicode ICW works across models. The method is *model-dependent*, not model-agnostic. The framing should be corrected to reflect this.

2. **Limited and non-adaptive adversarial evaluation.** The robustness evaluation tests only three attacks: 30% random word deletion, synonym replacement, and LLM paraphrasing. None of these are *adaptive*—they do not target the specific watermarking mechanism (e.g., instructing the LLM to avoid green letters, ignore the watermarking instruction, or use a counter-prompt). The paper acknowledges this vulnerability in Section 6 but does not evaluate it. Since the watermarking instruction is public knowledge (the detector's key and scheme design are assumed known to the adversary, per the problem formulation), a realistic adversary would deploy countermeasures. The paper tests the "ignore prior prompts" attack in the appendix (referenced but not in main text), but this is insufficient to support robustness claims against an informed adversary. This gap weakens both the IPI threat model and the general robustness claims.

3. **Missing relevant black-box baseline.** The paper cites Bahri et al. (2024), a black-box in-process watermarking method that also requires only API access, but does not compare against it. The baselines used (PostMark, YCZ+23) are post-processing approaches that operate on already-generated text under different constraints. Without a comparison to black-box in-process methods that work in the same "no model access" setting, it is difficult for the reader to assess whether ICW offers meaningful advantages over the closest alternative for the stated use case. The comparison to PostMark and YCZ+23 is useful but incomplete.

### Minor

1. **The IPI adversarial model assumes a non-adversarial or naive reviewer.** The IPI case study envisions a reviewer who inputs the entire PDF (including invisible "white text" watermarking instructions) into an LLM without any preprocessing. A dishonest reviewer could: copy only the visible text, use OCR that strips formatting, ask the LLM to ignore prior instructions, or use a model that does not follow the injected instruction. The paper frames this as "an initial exploration" and states that "detailed investigation of attack and defense methods is left for future work," so this is not a fatal flaw. However, the IPI scenario is presented as a primary motivation, so the gap between the motivating application and the evaluated threat model should be clearly scoped.

2. **The z-statistic detection for Initials ICW assumes i.i.d. letter distributions.** The detection statistic uses a z-test that treats word-initial letters as independent draws from a fixed distribution estimated from the Canterbury Corpus. In natural language, the letter distribution is context-dependent (e.g., a paragraph about "quantum" will have many 'q'-words), so false positive rates under this approximation could deviate substantially from nominal levels. The paper references theoretical guarantees in Appendix B (not available in main text), but the main text would benefit from empirical false positive rate calibration against diverse human text corpora.

3. **Text quality evaluation uses LLM-as-a-Judge with potential self-bias.** Table 3 shows "Unwatermarked" text (generated by GPT-o3-mini) receiving near-perfect scores (Relevance 4.982, Quality 5.000, Clarity 4.994, Overall 4.992) from Gemini-2.0-flash. These ceiling effects suggest the evaluator may be positively biased toward LLM outputs. While ICW methods still score well (4.28–4.81), the absolute scores should be interpreted cautiously. No inter-annotator agreement or variance is reported.

4. **Unicode ICW robustness is excluded from quantitative evaluation.** The paper states that Unicode ICW "robustness result is omitted from the figure due to its strong dependence on the specific operations applied to the watermarked text" but does not provide quantitative robustness numbers. Since Unicode ICW is the only method that works reliably across both GPT-4o-mini and GPT-o3-mini, understanding its robustness profile quantitatively would be valuable, even if the results show fragility under certain transformations.

### Trivial
- The claim "major LLM providers do not publicly use watermarks" (Introduction) is stated without citation. As of 2026, several providers have publicly discussed or deployed watermarking, though the paper hedges with "to our knowledge."

## Nice-to-Haves
- Evaluate adaptive adversarial countermeasures (e.g., asking the LLM to "ignore previous formatting instructions" or providing counter-prompts to avoid green-list words/letters).
- Include a black-box in-process baseline (Bahri et al., 2024) for the DTS setting to complete the comparison picture.
- Report empirical false positive rates on diverse human text corpora for each ICW method at theoretically motivated thresholds.
- Systematically vary context length in the IPI setting (e.g., 512, 1024, 2048, 4096 tokens) to measure how detection degrades.
- Provide example watermarked and unwatermarked text side-by-side to illustrate the perceptual impact of each ICW strategy.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Implementation details not provided in main text (Appendix C would be critical)"** — Removed per hard rule: criticisms about missing appendix content (parser-stripped) must be removed. The paper's main text should ideally stand alone, but the authors reference Appendix C for implementation details, which is standard practice.
- **"The paper does not include comparison to YCZ+23 in IPI setting"** — Removed: the paper explicitly states the baselines are not applicable in IPI because "the dishonest reviewer has no incentive to add a watermark by themselves" (Section 5.1). This is a reasoned exclusion, not an oversight.
- **"The paper claims ICW is model-agnostic but results show failure on GPT-4o-mini"** — Already retained above as a Major weakness, not removed.
- **"The detection performance for Unicode ICW in DTS (ROC-AUC 1.000) is suspicious because human text may contain zero-width spaces"** — Removed: this is a speculative concern not supported by evidence in the paper. The detector counts zero-width spaces inserted via the watermarking instruction; if the evaluation corpus does not contain such characters (a standard preprocessing assumption), the perfect separation is expected. The critic provides no evidence that the ELI5 or ICLR paper corpora contain zero-width spaces.
- **"Unwatermarked text quality scores are nearly perfect, suggesting LLM-as-a-Judge bias"** — Retained above as a Minor weakness, noting the ceiling effect. However, the specific claim that scores are "unrealistic" is weakened because the comparison between ICW and baselines is still valid (all methods are evaluated by the same judge).
- **"Missing related work"** — Removed per instruction: cannot confirm existence of missing citations without external knowledge.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Revise the "model-agnostic" claim** to accurately reflect the findings: ICW's performance is highly model-dependent, scaling with the LLM's instruction-following capability. This honest framing is already present in the contributions but contradicted by the Abstract.

2. **Add adaptive adversarial evaluations.** At minimum, test: (a) "ignore prior instructions" as a prepended prompt, (b) instructing the LLM to avoid words beginning with green letters or using green-list words, (c) paraphrasing through a different LLM. This would substantially strengthen the robustness claims.

3. **Include the black-box in-process baseline** (Bahri et al., 2024) or clearly explain why a comparison is infeasible. This would help the reader understand where ICW fits in the landscape of black-box methods.

4. **Calibrate false positive rates empirically** for the Initials and Lexical ICW z-statistic detectors on human-written text from diverse domains, and report actual TPR at low FPR thresholds (e.g., 0.1%, 1%) rather than relying solely on asymptotic approximations.

5. **Provide quantitative robustness results for Unicode ICW** even if they are expected to be poor under certain transformations—acknowledging fragility is better than omission.

## Score and Decision

**Calibration anchors (from batch retrieval):**

| Path | Avg Score | Comparison to this paper |
|---|---|---|
| `ujpAYpFDEA` — *Can Watermarked LLMs be Identified by Users via Crafted Prompts?* | 7.50 | More thorough evaluation and clearer contribution; this paper is weaker in experimental rigor |
| `E4LAVLXAHW` — *Black-Box Detection of Language Model Watermarks* | 7.00 | Well-executed with clear findings; this paper is less rigorous on adversarial analysis |
| `FDfq0RRkuz` — *WASA: Watermark-based Source Attribution* | 5.50 | Similar score band; this paper has higher novelty but comparable evaluation gaps |
| `RKQcJ1lXNT` — *Optimizing Adaptive Attacks against Content Watermarks* | 5.50 | Similar quality; this paper's contribution direction is complementary |
| `6p8lpe4MNf` — *A Semantic Invariant Robust Watermark* | 5.50 | Comparable novelty; this paper's evaluation is less comprehensive |
| `0koPj0cJV6` — *A Watermark for Black-Box Language Models* | 4.60 | This paper is stronger in novelty and clearer in contribution |
| `r6aX67YhD9` — *Learning to Watermark LLM-generated Text via RL* | 4.75 | This paper explores a more novel direction |
| `eKGEsFdpin` — *I Know You Did Not Write That!* | 3.67 | This paper is clearly stronger in contribution and insight |
| `1AYrzmDK4V` — *Watermark Smoothing Attacks* | 4.25 | This paper's contribution direction is more constructive |
| `8o6LdeVi1K` — *WAPITI: Watermark for Finetuned Open-Source LLMs* | 3.75 | This paper is stronger in novelty and results |

The paper introduces a genuinely novel watermarking paradigm (prompt-based, no model access) and provides promising initial results. However, the evaluation has notable gaps in adversarial robustness testing, the "model-agnostic" framing is contradicted by the data, and the IPI threat model is insufficiently stress-tested. Relative to the 5.5–7.0 band of watermarking papers, this work is on the lower end of that range: its novelty and idea quality are strong, but its evidential support is less comprehensive than the higher-scoring anchors. The paper is a solid initial exploration that would benefit from additional evaluation before it meets the bar for a top conference.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>