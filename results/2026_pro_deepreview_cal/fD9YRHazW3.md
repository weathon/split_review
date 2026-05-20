I've now read the paper thoroughly and all relevant calibration anchors. Let me write the consolidated review.

---

## Summary
This paper proposes In-Context Watermarking (ICW), a method for embedding watermarks into LLM-generated text purely through prompt engineering — without requiring access to the model's decoding process. Four strategies are explored (Unicode, Initials, Lexical, Acrostics) across two settings: Direct Text Stamp (DTS, where the user provides the watermark instruction directly) and Indirect Prompt Injection (IPI, where a third party embeds a watermark instruction into documents to detect AI-generated reviews). Experiments on GPT-4o-mini and GPT-o3-mini demonstrate that capable LLMs can follow watermarking instructions, achieving strong detection performance and robustness under paraphrasing.

## Strengths
- **Genuinely novel problem formulation**: ICW shifts watermarking from a model-access paradigm to a prompt-engineering paradigm, which is a fresh and timely angle. The IPI setting — where conference organizers embed watermark instructions into manuscripts to detect AI-generated reviews — provides a concrete, compelling use case that existing watermarking methods cannot address (lines 21-22, 94-96).

- **Systematic exploration across linguistic granularities**: The four strategies (Unicode, Initials, Lexical, Acrostics) span character-level, word-initial, lexical, and sentence-level watermarking, with clear trade-offs characterized in Table 1 across LLM requirements, detectability, robustness, and text quality.

- **Strong empirical results with capable models**: On GPT-o3-mini, Initials, Lexical, and Acrostics ICWs achieve ROC-AUC ≥ 0.995 and T@1%F ≥ 0.910 in the DTS setting (Table 2), and retain high detectability under paraphrasing (AUC 0.887–0.924, Figure 3), outperforming black-box baselines. Watermarked text quality remains within 3–4% of unwatermarked baselines on LLM-as-Judge evaluations (Table 3).

## Weaknesses

### Fatal
None.

### Major
- **IPI claims overreach the executed experiments.** The abstract and introduction (lines 13, 41) frame ICW as "covertly triggered" via hidden instructions (e.g., white text, zero-font-size), and the paper's headline application — detecting AI-generated peer reviews — depends on instructions being invisible to the reviewer yet actionable by the LLM. However, all IPI experiments (Table 2) are conducted by concatenating the watermark instruction as plain, visible text within the paper (`t ⊕ Instruction(k, τ)`). The paper does not test whether detection works after realistic covert embedding (e.g., white text in a PDF followed by text extraction). The paper acknowledges (line 106) that "a detailed investigation of attack and defense methods is left for future work," which is a reasonable scope limitation. But the abstract's unqualified claim of "covertly triggered" and the framing of the IPI experiments as validating covert watermarking overstate what was actually tested. The experiments demonstrate that an LLM follows watermarking instructions in long-context settings — a necessary but insufficient condition for covert applicability.

- **Lexical ICW detection formula is imprecisely specified, with ambiguous FPR control.** Section 4.2.3 (line 164) states the detection statistic uses `γ = |V_G|/|V|` where V is restricted to adjectives, adverbs, and verbs, and applies this to `|y|` (total words in the text). Under the null hypothesis, the expected green word count is `γ × (#words in V)`, not `γ|y|`, since words outside V can never match V_G. The z-statistic as written would be biased unless |y| is redefined as the count of words belonging to V — but the paper does not specify this. The paper states (line 168) that theoretical FPR guarantees are provided in Appendix B (stripped by the parser), so the issue may be addressed there. However, the main-text description as written is mathematically imprecise and would mislead a reader attempting to reproduce the detection.

### Minor
- **Acrostics detection lacks empirical FPR validation.** The Acrostics detector (Section 4.2.4) estimates its null distribution by resampling sentence-initial letter sequences from the suspect text itself — essentially a permutation test. While this is a defensible statistical approach for testing whether the observed ordering matches the secret key, the paper does not report empirical false-positive rates on known unwatermarked text. The ROC-AUC alone does not guarantee that the FPR is well-calibrated at the low thresholds (1%F) that are practically relevant. This is addressable with a supplementary experiment.

- **LLM-as-Judge scores are near-ceiling for unwatermarked text.** In Table 3, the unwatermarked GPT-o3-mini baseline receives scores of 4.982–5.000 on a 5-point scale, leaving very little dynamic range to distinguish watermarked from unwatermarked text. The relative ordering is informative, but the absolute calibration of the judge (gemini-2.0-flash) may be inflated, and a sanity check (e.g., comparing against human-written text, which scores meaningfully lower at 4.235 overall) would strengthen confidence in the metric.

### Trivial
- The paper does not specify how the green word list for Lexical ICW is constructed (vocabulary source, size of V_G, how the secret key determines the partition), which affects reproducibility. This information is likely in Appendix C (stripped), but should at minimum be summarized in the main text.

## Nice-to-Haves
- Testing IPI detection under at least one realistic covert embedding method (e.g., zero-font-size text in a PDF, extracted via a standard PDF parser) would substantially strengthen the paper's central motivating scenario. Even a small pilot experiment would bridge the gap between the current long-context demonstration and the claimed covert applicability.
- Reporting empirical false-positive rates on human-written text for all ICW methods (not just ROC-AUC) would provide stronger evidence for practical deployability, particularly at the low-FPR thresholds the paper emphasizes.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim: "The IPI setting is not evaluated under the conditions that give it meaning" — specifically that the covert injection aspect is entirely absent and this is a structural/fatal gap.** *Removal justification:* The paper does demonstrate the key capability (LLM follows watermarking instructions within long documents) and explicitly scopes the detailed investigation of covert embedding and defenses to future work. The gap is real but has been downgraded to Major (overclaim in framing vs. what was tested) rather than Fatal. The core capability is demonstrated; what's missing is the bridge from "instruction in context" to "instruction hidden in PDF."

- **Harsh Critic claim: "The detection method for Lexical ICW is ill-defined and likely incorrect as written" — labeled as an evidential flaw that casts doubt on all reported AUCs.** *Removal/demotion justification:* The detection formula does have a mathematical imprecision in how γ interacts with |y|, but (a) the paper claims Appendix B provides theoretical FPR guarantees which may resolve this, and (b) even with a biased null expectation, the detector could still separate watermarked from unwatermarked distributions (the ROC-AUC measures ranking, not calibration). The issue is real but has been downgraded to Major (reproducibility concern) rather than treated as evidential grounds to dismiss all Lexical ICW results.

- **Harsh Critic claim: "The Acrostics detection lacks a proper null distribution and FPR control" — labeled as statistically unsound.** *Demotion justification:* The resampling procedure is a permutation test, which is a standard statistical method for testing whether an observed arrangement is significantly more ordered (with respect to a key) than random permutations would produce. This is statistically defensible. The legitimate concern — lack of empirical FPR validation on unwatermarked text — has been retained as Minor.

- **Strength Finder: "Theoretical false-alarm control is provided for Initials and Lexical ICWs."** *Retained but noted as unverifiable:* The paper claims these guarantees are in Appendix B, which is stripped. I note this in the review but cannot weigh it as confirmed evidence.

- **Strength Finder: "Watermarked text quality closely matches unwatermarked generation" with Table 3 evidence.** *Retained as a valid strength, with the caveat about near-ceiling judge scores noted as a Minor weakness.* The relative ordering and proximity to unwatermarked scores still provide meaningful evidence.

- **Harsh Critic: Section 5.2.3 text quality evaluation concern about near-perfect judge scores.** *Retained as Minor weakness — the concern is valid but does not invalidate the text quality comparison.*

## Novel Insights
The review process reveals an interesting tension in the ICW paradigm: the paper demonstrates that as LLM capabilities improve (GPT-4o-mini → GPT-o3-mini), ICW performance improves dramatically (Initials ICW goes from AUC 0.572 to 0.999 in DTS). This suggests ICW's viability is gated by instruction-following ability rather than by any fundamental limitation of prompt-based watermarking — meaning ICW may become increasingly practical as models advance, without requiring any change to the watermarking methodology itself. This "rising tide lifts all boats" property is unusual in watermarking research and worth highlighting.

## Suggestions
- Either rescope the abstract and introduction to accurately reflect what was tested (long-context instruction following rather than covert injection), or add a pilot experiment with one realistic covert embedding method. The current mismatch between framing and evidence is the paper's most significant weakness.
- Clarify the Lexical ICW detection: specify whether |y| in the denominator refers to total words or only to words belonging to V (adjectives/adverbs/verbs). If the latter, state this explicitly; if the former, explain how FPR control is maintained despite the mismatch, or reference the Appendix B derivation.
- Report empirical false-positive rates for Acrostics detection on a corpus of known unwatermarked text to complement the ROC-AUC.

## Score and Decision

**Calibration anchors used across both rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1 | Clearly weaker: narrower contribution, less comprehensive evaluation |
| 0koPj0cJV6 (Black-Box Watermark) | 4.60 | R2 | Weaker: similar black-box framing but less practical, presentation issues |
| FDfq0RRkuz (WASA) | 5.50 | R2 | Similar level: novel problem but evaluation limitations; comparable contribution |
| 9k0krNzvlV (Learnability of Watermarks) | 5.75 | R2 | Slightly stronger than our paper: more rigorous experiments but narrower novelty |
| KRMSH1GxUK (Watermarks for IP Infringement) | 5.80 | R1/R2 | Comparable: clear contribution with evaluation gaps |
| DEJIDCmWOz (Reliability of Watermarks) | 6.00 | R2 | Slightly stronger: more thorough evaluation with human studies |
| E4LAVLXAHW (Black-Box Detection of Watermarks) | 7.00 | R1 | Clearly stronger: more rigorous statistical framework, first-of-its-kind study |

**Round 1 bracket:** 5.0–6.5 (based on comparison with weak anchors at ~3.0, middle at 3.67–7.00, and strong at 7.75–8.00).

**Round 2 narrowing:** 5.5–5.75. Our paper is comparable to or slightly weaker than the 5.75–6.00 anchors due to the IPI overclaim and Lexical detection formula imprecision, but stronger than the 4.60 anchor.

**Final assessment:** The paper proposes a genuinely novel and timely approach to LLM watermarking without model access, with systematic exploration and strong empirical results. However, the abstract's unqualified "covertly triggered" claim overreaches relative to the experiments, and the Lexical ICW detection formula needs clarification for reproducibility. These issues are addressable but weight the paper toward the lower end of the borderline-accept range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>