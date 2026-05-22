Now I have a thorough understanding of the paper, the reviews, and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper investigates whether translating benchmark data into Arabic can "mask" data contamination — i.e., whether models fine-tuned on Arabic-translated versions of English benchmarks still benefit from that exposure while standard English-only contamination checks fail to detect it. The authors fine-tune four open-weight LLMs (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) on mixtures of English data and varying proportions (0%, 10%, 50%, 100%) of Arabic-translated benchmark data, then evaluate on the original English MMLU, XQuAD, and MLQA benchmarks. They also extend the TS-Guessing memorization probe with a choice-reordering strategy for multiple-choice questions.

## Strengths

1. **Clear and consistent MMLU findings across diverse models.** All four models show monotonically increasing English MMLU accuracy as the proportion of Arabic-translated contamination rises (e.g., Mistral-7B: 0.577 → 0.690; LLaMA-3.2-1B: 0.332 → 0.431; Gemma-3-1B: 0.220 → 0.284). The consistency of this trend across models of different sizes, architectures, and Arabic capabilities is the paper's most compelling piece of evidence.

2. **Timely and practically important research question.** The possibility that translation could mask contamination while preserving performance benefits is a genuine blind spot in current English-centric contamination detection. This is a legitimate concern for multilingual evaluation pipelines.

3. **Choice-reordering extension to TS-Guessing for MCQs.** The methodological innovation — shuffling answer choices then masking an incorrect option and checking whether the model recalls the pre-shuffle index (IDR) — is a creative adaptation of an existing probe. It tests a form of surface-level memorization that standard accuracy metrics do not capture.

4. **Multi-model, multi-dataset, multi-level experimental design.** Evaluating 4 models × 3 datasets × 4 contamination levels provides useful dimensionality for analyzing how model characteristics interact with contamination dynamics.

## Weaknesses

### Major

1. **No English-to-English contamination baseline, so the "masking" claim is unsubstantiated.** The paper's central claim is that translation *masks* or *conceals* contamination signals. To support this, one must compare an English-to-English condition (adding English benchmark data to training) against the Arabic-to-English condition, showing that the former produces detectable behavioral shifts while the latter does not. Without this control, the observed "flatness" in TS-Guessing scores (Table 3a) cannot be attributed to translation — it may simply reflect that the probe is insensitive, or that the models do not memorize translated content the same way. The paper assumes what it needs to prove.

2. **Training set size confound invalidates clean interpretation.** The training condition is D_train = D_EN ∪ D_AR(p). The English data is always included in full, while varying amounts of Arabic data are added. The p=0 condition has strictly less total training data than p=100. Any performance increase could be partially or entirely due to having more training data, not specifically to contamination from benchmark-relevant content. This is a basic experimental design issue the paper does not address.

3. **Contradictory claims about "flatness" vs. actual data.** Section 4.2 states that "the models exhibit approximately equal performance on all evaluated benchmarks" across contamination levels and that "scores remain broadly stable as p increases." But Table 2 shows Mistral MMLU moving from 0.577 to 0.690 — a 20% relative increase, not "approximately equal." The paper cannot simultaneously claim that (a) contamination drives performance gains (to motivate the work) and (b) scores are flat across p (to claim masking). This inconsistency undermines the paper's interpretative framework.

4. **No statistical significance or variance reported.** All results are from single runs with no confidence intervals, standard deviations, or significance tests. Given the small effect sizes (e.g., Qwen MMLU: +0.028) and highly non-monotonic XQuAD/MLQA trends (e.g., Mistral XQuAD: 0.455 → 0.272 → 0.114; Qwen MLQA: 0.162 → 0.409 → 0.157), the reader cannot distinguish signal from noise.

5. **TS-Guessing probe results missing for p=0 baseline condition.** Table 3 reports TS-Guessing (IDR, EM, ROUGE-L) only for p ∈ {10%, 50%, 100%}. Without p=0 results, we cannot determine whether observed probe scores reflect contamination-driven memorization or baseline probe difficulty / model tendencies. This is a straightforward missing control.

### Minor

6. **The fine-tuning setup does not match the pre-training contamination framing.** The paper's literature review (Section 2), abstract, and introduction are framed around pre-training contamination, but the experiments study fine-tuning on a known, controlled set of downstream examples. These are different regimes (number of epochs, loss weighting, memorization capacity). The paper is transparent about using fine-tuning, but the framing mismatch weakens the connection to the contamination detection literature it engages with.

7. **TACD framework is a non-contribution as presented.** Section 5 describes a "Translation-Aware Contamination Detection framework" that is entirely conceptual — no implementation, no experiments, no empirical validation. The paper admits this. A high-level suggestion about multi-language contamination checks does not constitute a research contribution and should not be counted among the paper's findings.

8. **The literature review is disproportionately long.** Section 2 occupies roughly 40% of the paper's content and reads as a textbook summary rather than a targeted motivation. Key material (subsections 2.1.1–2.1.3, 2.2–2.4) could be condensed to a few paragraphs, freeing space for experimental justification, ablations, or analysis.

### Trivial

9. **The "embedding figure" is referenced but not shown** (likely stripped by the parser, but the paper should describe it more fully in text). The cosine similarity claim about Arabic→English translations is stated without quantitative evidence in the main body.

## Nice-to-Haves

- Adding an English-to-English contamination condition would directly test whether translation actually masks contamination or merely changes its magnitude.
- Reporting TS-Guessing results at p=0 to establish baseline probe behavior.
- Adding confidence intervals or multiple seeds to distinguish signal from noise in the non-monotonic XQuAD/MLQA results.
- Implementing even a limited version of TACD on one dataset would turn a conceptual suggestion into a real contribution.

## Removed Points

- **Criticism about "the experimental setup does not model the phenomenon it claims to study (Structural)"**: The paper is transparent about using fine-tuning. While the framing tilts toward pre-training contamination, the paper's actual claim about contamination through translation is legitimate in any training regime. The reviewer overstates this as a fatal flaw; it is a minor framing mismatch. → Demoted to Minor weakness #6 above.

- **Criticism about TS-Guessing being "misapplied" — that it probes index recall of incorrect answers rather than correct-answer memorization**: The paper explicitly states the method tests "reliance on memorized index patterns rather than reasoning about content." The probe does what it claims to do (index recall). The reviewer's objection that it doesn't test correct-answer memorization is correct but orthogonal — the paper never claims it does. However, the missing p=0 baseline is a real issue, retained in Major weakness #5.

- **Criticism that "Results are weak, non-monotonic, and overclaimed" — specifically that MMLU increases are "small"**: The Mistral-7B gain of +0.113 (57.7%→69.0%) and LLaMA-3.2-1B gain of +0.099 (33.2%→43.1%) are meaningful improvements, not "small." The monotonic pattern across all 4 models is strong evidence. → The statistical rigor criticism (no confidence intervals) is retained; the dismissal of effect sizes as "small" is removed.

- **Criticism from Strength Finder about "Thorough contextualization of prior contamination work"**: Dropped because the literature review, while thorough, is overly long relative to the paper's contribution. A strength about length is not appropriate when the length is a weakness.

- **Criticism about "Systematic multi-model, multi-dataset experimental design" as a strength**: Partially retained — it is a genuine strength, but the design has a fundamental confound (training set size) that weakens the systematicity claim. Kept as Strength #4 with caveat implicit in weaknesses.

## Novel Insights

The reviews do not surface any genuinely novel observation beyond the paper's own contributions. The one notable meta-point is that the paper's most robust result (monotonic MMLU improvement across 4 models) is at odds with its own interpretive framework (claiming "flatness" to argue for masking). This tension — between strong-enough results to claim contamination benefit and weak-enough results to claim undetectability — is the paper's central unresolved contradiction.

## Suggestions

1. Add an English-to-English contamination condition. This is the single most important experiment needed to support the masking claim.
2. Control for training set size (e.g., by keeping total data fixed and varying only the proportion of Arabic data).
3. Report TS-Guessing results at p=0 to establish baseline probe sensitivity.
4. Add multiple runs and report variance/confidence intervals.
5. Remove or significantly revise Section 4.2's "flatness" claim, which contradicts Table 2.
6. Either implement TACD or acknowledge it as a limitation/future work rather than a contribution.
7. Condense the literature review (Section 2) to make room for the above improvements.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to Paper Under Review |
|------|-----------|----------------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` (Evading Data Contamination Detection) | 4.25 (Reject) | Similar topic (evading detection), but that paper had serious presentation issues and unclear methodology. Current paper is better structured and has clearer contributions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rAylWUIKtu.md` (Benchmark Inflation) | 4.25 (Reject) | Comparable quality. Both papers have a genuine research question and methodology but significant experimental limitations. Current paper's multi-model design is broader but has a more critical confound. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` (How much can we Forget) | 6.75 (Reject) | Much stronger experimental rigor (controlled pre-training, theoretical framework, scaling analysis) and statistical depth. Current paper is notably weaker on all these dimensions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zWqr3MQuNs.md` (Detecting Pretraining Data) | 6.25 (Accept) | Cleaner methodology, clearer experiments, accepted. Current paper has a more interesting question but messier execution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` (To the Cutoff... and Beyond) | 6.75 (Accept) | Rigorous longitudinal analysis with statistical significance. Current paper lacks comparable rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` (Crosslingual Capabilities) | 5.67 (Reject) | Also studies multilingual LLM evaluation. Current paper has a more focused claim but less thorough analysis. |

The paper under review sits between the ~4.25 papers (which have serious methodological issues) and the ~6.25+ papers (which demonstrate stronger experimental rigor). The core MMLU finding is genuinely interesting and the research question is important, but the experimental design has a fundamental confound (training set size), a missing critical baseline (English-to-English), and an internal contradiction (claiming flatness while showing non-flat results). These issues are real but not fatal — the MMLU trend is real and replicable across 4 models. However, the paper's strongest claims about "masking" are not supported by the current experimental design.

**Score: 5.0**

**Decision: Reject**

The paper should be encouraged to resubmit after adding the English-to-English baseline, controlling for training set size, reporting p=0 probe results, and adding statistical rigor. The core research question has merit and the MMLU finding is worth pursuing, but the current experimental design cannot support the paper's central claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>