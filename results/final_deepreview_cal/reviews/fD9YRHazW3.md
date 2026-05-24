Now I have a comprehensive picture. Let me write the final review.

---

## Summary

This paper introduces In-Context Watermarking (ICW), a novel paradigm for embedding detectable signals into LLM-generated text using only prompt engineering — without requiring access to the model's decoding process. Four watermarking strategies are proposed at different linguistic granularities: Unicode (zero-width space insertion), Initials (biasing word-initial letters), Lexical (green-listing adjectives/adverbs/verbs), and Acrostics (controlling sentence-initial letters). The methods are evaluated in two settings: Direct Text Stamp (DTS), where the watermark instruction is a system prompt, and Indirect Prompt Injection (IPI), where watermarking instructions are covertly embedded into academic manuscripts to detect LLM-generated peer reviews. On GPT-o3-mini, all four methods achieve ROC-AUC ≥ 0.995 in DTS and strong detection in IPI, with good robustness to editing and paraphrasing.

## Strengths

- **Genuinely novel paradigm.** ICW is, to my knowledge, the first framework for watermarking LLM outputs purely through prompt engineering, without logit access, weight access, or post-hoc text editing. This opens watermarking to third parties (e.g., conference organizers, content platforms) who have no relationship with the model provider. The distinction between DTS and IPI settings (Section 3) is clean and well-motivated.

- **Strong detection performance with capable models.** On GPT-o3-mini, all four ICW strategies achieve near-perfect detection in the DTS setting (ROC-AUC ≥ 0.995, T@1%F ≥ 0.930; Table 2). Robustness experiments (Figure 3) show that Initials, Lexical, and Acrostics ICW retain high detectability under word deletion, synonym replacement, and LLM paraphrasing — including AUC > 0.88 under paraphrasing for Initials and Acrostics ICW, which is a stringent test.

- **Well-preserved text quality.** The LLM-as-a-Judge evaluation (Table 3) shows that watermarked text from all four ICW methods scores comparably to unwatermarked LLM text and above human-written text on relevance and quality, while outperforming the PostMark baseline substantially. This indicates that the watermarking instructions do not severely degrade output quality.

- **Meaningful baseline comparisons.** In the DTS setting, ICW is benchmarked against two post-hoc black-box baselines (PostMark and YCZ+23) and matches or exceeds their detection and robustness when paired with a capable model — despite ICW operating under a strictly harder constraint (no access to generated text for post-processing).

- **Clear ablation of model capability.** The dramatic performance gap between GPT-4o-mini and GPT-o3-mini (e.g., Initials ICW: ROC-AUC 0.572 → 0.999; Table 2) convincingly demonstrates that ICW effectiveness depends on the underlying LLM's instruction-following ability. This is a practically important insight for deployment.

## Weaknesses

### Major

- **IPI evaluation is incomplete for the paper's primary motivating scenario.** The IPI setting — embedding watermark instructions into manuscripts to catch dishonest reviewers — is the paper's most distinctive and compelling use case. Yet the evaluation reports only detection signal (ROC-AUC, T@1%F in Table 2) without examining: (a) whether the hidden watermarking instruction ever leaks into the LLM's review output (which would break stealth), or (b) whether the presence of a watermarking instruction degrades review quality when the model must follow a hidden directive buried in a long document. The paper acknowledges that "a detailed investigation of attack and defense methods is left for future work" (line 106), which is fair, but the current IPI results — as the paper's flagship application — feel like a detection-only proof-of-concept rather than a validated case study. This does not invalidate the core idea but does mean the paper's strongest narrative hook is not fully substantiated.

### Minor

- **Lexical ICW under-specified.** The method partitions a vocabulary of adjectives, adverbs, and verbs into green and red lists, but the paper does not specify the vocabulary size or list sizes (these are deferred to Appendix C, which is not available for review). The detection statistic uses γ = |V_G|/|V|, assuming uniform word usage under the null, but actual human and unwatermarked LLM text does not use these word classes uniformly. The ROC evaluation partially masks this calibration concern, but the method's statistical foundations would benefit from validation on held-out human text.

- **Narrow model coverage limits the capability-scaling claim.** The claim that ICW "becomes stronger as LLMs improve" is supported by a single pair of proprietary models (GPT-4o-mini → GPT-o3-mini). While the performance gap is dramatic and suggestive, two data points from the same model family cannot distinguish a genuine capability trend from differences in fine-tuning recipes, prompt sensitivity, or architecture. At least one open-weight model at multiple scales would substantially strengthen the argument. The paper's language is appropriately hedged ("our findings suggest"), but the evidence remains thin.

- **Unicode ICW is trivial in both concept and robustness.** Inserting zero-width spaces after each word achieves perfect detection but is trivially removed by any text normalization pipeline, and the paper correctly notes it does not survive paraphrasing or cross-platform transmission. It serves mainly as a lower bound on LLM requirements rather than a practical method. This is not a flaw per se, but it inflates the method count without adding substantive novelty.

### Trivial

- The paper could clarify the number of resamples N used in the Acrostics ICW detection z-statistic (Section 4.2.4) and report typical sentence counts, as these affect the reliability of the resampled mean and standard deviation estimates.
- For the IPI setting, robustness results are mentioned to be in the appendix (Table 6) but are absent from the main text; given the scenario's importance, a summary in Section 5.2.2 would improve readability.

## Nice-to-Haves

- A simple IPI sanity check: feed the watermarked manuscript + review prompt to the LLM and automatically scan the output for the watermarking instruction itself, to verify that the hidden prompt is not echoed verbatim.
- A sensitivity analysis for Lexical ICW showing how detection degrades as the green-list proportion γ or absolute vocabulary size varies.
- Incorporating at least one open-weight model at multiple scales (e.g., Llama-3 8B → 70B) to strengthen the capability-scaling narrative.
- A preliminary test of the "ignore prior prompts" adversarial instruction in the IPI setting, which the paper mentions as future work but would add immediate practical impact.

## Removed Points

These points were raised in the input reviews but removed from the final review for the stated reasons:

- **"GPT-o3-mini's provenance and actual capability relative to GPT-4o-mini are unclear"** — REMOVED. The paper cites GPT-o3-mini as a released OpenAI model (OpenAI, 2025). Its existence and relative capability ordering are assumed. This reflects a reviewer knowledge gap, not an author error.

- **"The obfuscation technique (white text) is not tested experimentally"** — DEMOTED to contextual note. The paper explicitly states IPI is exploratory and that detailed attack/defense investigation is future work. The concatenation case is the natural first step.

- **"The Lexical ICW vocabulary size is not provided"** — RETAINED as Minor, but the implied claim that this makes the method "reduce to a trivial keyword-insertion trick" is REMOVED as speculative. The paper clearly grounds the approach in part-of-speech filtering and the green/red list paradigm; the missing size is a specification gap, not a fatal design flaw.

- **"The z-test for Lexical ICW is mis-calibrated in principle"** — PARTIALLY RETAINED. The calibration concern is valid and appears in the Minor weakness. However, the claim that this is a fatal methodological error is REMOVED — the ROC-AUC evaluation is threshold-free and does not depend on calibration, so the method's discriminative power is independently validated.

- **"No comparison against a baseline that detects the watermarking instruction itself in the output"** — DEMOTED to Nice-to-Have. This is a useful diagnostic but not a standard baseline for watermarking evaluation.

- **"The paper would need to specify list sizes and validate the null distribution"** — RETAINED in Minor. The specification gap is real.

## Novel Insights

A genuinely novel insight from this work is the empirical demonstration that *instruction-following capability is the bottleneck for prompt-based watermarking*. The performance cliff between GPT-4o-mini and GPT-o3-mini on Initials and Acrostics ICW (Table 2) — where the weaker model essentially fails to follow the instruction at all — suggests that ICW is not just an engineering trick but a capability test: as models get better at following complex natural-language constraints, prompt-based watermarking becomes not merely feasible but competitive with logit-level methods. This inverts the usual watermarking narrative (where better models are harder to watermark because their outputs are more human-like) and suggests a future where watermarking is a byproduct of alignment quality.

## Suggestions

- The IPI section would benefit from even a small-scale qualitative analysis: feed 10–20 watermarked papers to GPT-o3-mini with a standard review prompt, manually inspect the outputs for instruction leakage, and judge review quality. This would transform the IPI from a detection-only proof-of-concept into a more convincing case study.
- For the Lexical ICW, specify the actual vocabulary size and green-list size used in experiments. If Appendix C already contains this, note it prominently in Section 4.2.3.
- Add a sentence in Section 5.2.1 clarifying that the IPI evaluation is a feasibility demonstration and that a full adversarial evaluation (including instruction leakage, removal attacks, and review quality measurement) is deferred to future work. The paper already says this in Section 3.2, but restating it near the IPI results would prevent readers from over-interpreting the detection numbers.

## Score and Decision

I evaluated this paper across originality (high — prompt-based watermarking is a genuinely new direction), importance (moderate-to-high — third-party watermarking addresses a real gap), claim support (moderate — DTS claims are well-supported, IPI claims are only partially validated), experimental soundness (moderate — DTS experiments are solid, IPI experiments are detection-only, model coverage is narrow), clarity (high — the paper is well-organized and clearly motivated), and community value (moderate-to-high — the paradigm opens a new research direction).

**Round-1 bracket:** Based on comparison with topically similar anchors, the paper falls between ~5.5 (WASA, FDfq0RRkuz, 5.50 — similar novelty level, comparable evaluation scope) and ~7.5 (Water-Probe, ujpAYpFDEA, 7.50 — more thorough evaluation, more rigorous). Initial bracket: 5.5–7.0.

**Round-2 narrowing:** The paper is stronger than SEAL (LdIlnsePNt, 6.00 — strong theory but weak theory-practice connection, unfair baselines) and the IP infringement watermark paper (KRMSH1GxUK, 5.80 — more limited evaluation scope). It is clearly weaker than Water-Probe (7.50) and Black-Box Detection (E4LAVLXAHW, 7.00), both of which have more comprehensive evaluations and stronger theoretical grounding. The paper sits closest to SEAL (6.00) in terms of contribution quality but with better practical coherence.

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| jbfDg4DgAk (Sparse Watermark) | 3.00 | 1 | Paper is substantially stronger |
| xRi8sKo4XI (Unsupervised Prompt Learning) | 3.00 | 1 | Different topic, not directly comparable |
| eKGEsFdpin (Sampling-Based Watermark) | 3.67 | 2 | Paper is stronger |
| r6aX67YhD9 (RL Watermark) | 4.75 | 1 | Paper is stronger — better coherence, no requirement for original prompt |
| 0KHW6yXdiZ (End-to-End Logits Watermark) | 5.25 | 2 | Paper is somewhat stronger — more novel paradigm |
| 1ou5noWgHM (Source Attribution) | 5.40 | 2 | Paper is comparable — different problem, similar evaluation depth |
| FDfq0RRkuz (WASA) | 5.50 | 2 | Paper is slightly stronger — more novel, better motivated |
| KRMSH1GxUK (IP Infringement Watermark) | 5.80 | 1 | Paper is comparable — both have evaluation limitations, ICW more novel |
| LdIlnsePNt (SEAL) | 6.00 | 2 | Paper is comparable — ICW has better practical coherence, SEAL has stronger theory |
| K7xpl3LZQp (PLA Copyright Tracking) | 6.25 | 2 | Paper is slightly weaker — PLA has more thorough evaluation |
| jlhBFm7T2J (Undetectable Image Watermark) | 6.50 | 2 | Different modality, not directly comparable |
| E4LAVLXAHW (Black-Box Watermark Detection) | 7.00 | 1,2 | Paper is weaker — BB Detection has more rigorous evaluation and theory |
| ujpAYpFDEA (Water-Probe) | 7.50 | 2 | Paper is weaker — Water-Probe has more thorough evaluation |
| oZtt0pRnOl (Privacy-Preserving ICL) | 8.00 | 1 | Different topic |
| SnDmPkOJ0T (REEF) | 8.00 | 1 | Different topic |

**Final score:** 6.0 — The paper introduces a genuinely novel and well-motivated paradigm with solid DTS results, but the IPI evaluation (the paper's flagship application) is detection-only and the model coverage is too narrow to fully warrant the capability-scaling claim. The contribution merits acceptance, with the expectation that the authors will address the IPI evaluation gaps in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>