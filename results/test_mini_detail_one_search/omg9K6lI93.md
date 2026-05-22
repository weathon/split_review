Now I have all the information I need. Let me construct my final consolidated review.

---

## Summary

The paper investigates whether translating evaluation benchmarks into Arabic masks traditional contamination signals while still allowing models to benefit from exposure to contaminated data. The authors fine-tune four open-weight models on Arabic-translated benchmark data at varying contamination proportions (0%, 10%, 50%, 100%), evaluate on English benchmarks, and apply TS-Guessing with a choice-reordering trick to probe memorization. They propose a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint for addressing multilingual contamination.

## Strengths

1. **Novel and timely research question.** The problem of how translation interacts with contamination is genuinely underexplored. Prior contamination work has focused almost exclusively on English. Asking whether multilingual evaluation introduces a blind spot is a well-motivated, important question.

2. **Multi-model, multi-dataset experimental design.** The paper fine-tunes four different models (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) across three benchmarks (MMLU, XQuAD, MLQA) at four contamination levels. This breadth provides reasonable evidence that the observed effects are not idiosyncratic to a single model or task.

3. **TS-Guessing with choice reordering is a creative methodological adaptation.** Figure 1 and Section 3.3 describe a procedure where multiple-choice options are shuffled and one incorrect answer is masked, then the model's ability to reproduce the pre-shuffle index letter is measured. This probes index-pattern memorization rather than surface-form overlap, which is a principled extension of the TS-Guessing framework to the multiple-choice setting.

4. **Empirical contrast between accuracy gains and detection blindness is informative.** The juxtaposition of monotonic MMLU accuracy gains (Table 2) with low TS-Guessing scores for several models (Table 3) provides evidence that Arabic contamination helps model performance while partly evading a probe-based detection method. This contrast is the paper's most compelling single observation.

## Weaknesses

### Fatal
None.

### Major

1. **Internal contradiction between Sections 4.1 and 4.2.** Section 4.2 states: "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks. This near-flat trend indicates that Arabic → English translation is effectively masking contamination effects… The consolidated results in Tables 2 and 3a show that scores remain broadly stable as p increases." This directly contradicts Table 2, where MMLU accuracy shows clear monotonic increases (e.g., Mistral: 0.577→0.690; LLaMA: 0.332→0.431; Gemma: 0.220→0.284). Section 4.1 itself acknowledges these are "monotonic increase[s]." Claiming "broadly stable" or "approximately equal" performance for the very data that shows consistent upward trends is a significant internal inconsistency. **Why it matters:** This overclaim weakens the paper's central narrative. If the claim is about TS-Guessing being flat, the text should say that clearly and not claim that Table 2 accuracy is flat. A reader cannot trust the paper's interpretation of its own results when the text contradicts the tables.

2. **TS-Guessing results for LLaMA undermine the "flat and low" narrative.** Table 3a shows LLaMA-3.2-1B has IDR of 0.287, 0.643, and 0.410 at 10%, 50%, and 100% contamination respectively. An IDR of 0.643 means the model reproduces the pre-shuffle answer index 64.3% of the time after shuffling — this is a *strong and variable* contamination signal, not a "flat" or "low" one. The paper's claims about TS-Guessing being uniformly insensitive are only partially true (holding for Mistral, partially for Gemma and Qwen) and do not apply to LLaMA. **Why it matters:** The paper presents a universal claim ("translation conceals contamination from TS-Guessing") that its own data contradicts for one of four models. This suggests the effect is model-dependent, not a general property of translation.

3. **No positive control for the TS-Guessing adaptation.** The paper applies TS-Guessing to detect contamination but never validates that the method works in a standard setting (e.g., fine-tuning on English test data and showing TS-Guessing detects the memorization). Without a positive control, the low TS-Guessing scores could equally mean (a) translation masks contamination, (b) the method is insensitive, or (c) these models simply do not memorize the Arabic data in a way detectable via this probe. **Why it matters:** The central claim depends on interpreting null or low TS-Guessing results as evidence of masked contamination. Without a validation experiment showing the probe can detect contamination when it is known to exist, the interpretation is ambiguous.

### Minor

4. **Data volume confound.** The experimental design adds Arabic data on top of a fixed English dataset, so the total training set grows with contamination proportion (the 100% condition has roughly twice the examples of 0%). Some accuracy gains could be attributed to simply having more training data rather than contamination per se. Adding a control condition with an equal volume of non-contaminated Arabic data from a different domain would strengthen the causal interpretation.

5. **No statistical significance reporting.** The paper reports only point estimates without confidence intervals or significance tests. Given that some accuracy differences across contamination levels are modest (e.g., Qwen MMLU: 0.553→0.581 from 0% to 100%), it is unclear whether these reflect genuine contamination effects or are within noise.

6. **Section 4.2's framing conflates different constructs.** The paragraph in Section 4.2 moves between claims about accuracy being flat (contradicted by data), TS-Guessing being flat (partially contradicted by LLaMA), and translation "compressing observable differences" without clearly distinguishing these. The "near-flat" language would be more accurate if restricted specifically to the TS-Guessing probe results (and even then, qualified for LLaMA).

### Trivial
None.

## Nice-to-Haves

- A positive control experiment validating the TS-Guessing adaptation (fine-tune on English test data and show the probe detects it).
- A data-volume control condition using non-contaminated Arabic text.
- Reporting exact match and F1 for XQuAD/MLQA alongside ROUGE-L in Table 2 (the paper already reports EM + ROUGE-L in Table 3b for the TS-Guessing variant; extending to Table 2 would improve comparability with prior work).
- Confidence intervals or bootstrap estimates for key accuracy figures.
- Qualitative examples of model predictions from the TS-Guessing probe (showing what models actually output when asked to fill the mask).

## Removed Points

*These points were raised by a reviewer but do not survive cross-checking against the paper and are removed for the reasons listed.*

1. **"Central claim is contradicted by paper's own data (Fatal)."** The harsh critic claimed that the paper's thesis that translation "conceals traditional contamination signals" is contradicted by MMLU monotonic increases. This misreads the paper's claim. The thesis is that *surface-form detection methods* (n-gram overlap, TS-Guessing) are blinded by translation, not that accuracy is flat. The monotonic MMLU gains support the "models still benefit" part of the argument. The real problem is the *internal inconsistency* in Section 4.2's language (retained as Major Weakness #1), not a fatal contradiction of the core claim.

2. **"TS-Guessing masks an incorrect answer, not the correct one — design not explained."** The harsh critic questioned masking an incorrect answer choice. The paper's design is intentional and well-motivated: after shuffling, if the model outputs the pre-shuffle index letter of a now-relocated correct answer, this signals index-pattern memorization — a stronger contamination signal than text overlap. This is a reasonable methodological choice.

3. **"ROUGE-L is not standard for QA; paper should report EM/F1."** Factually incorrect. Section 3.4 specifies that the paper computes both EM and ROUGE-L F1 for XQuAD/MLQA, and Table 3b reports both. The main accuracy table (Table 2) uses ROUGE-L, but EM is reported in the probe results.

4. **"Literature review occupies too much space (~40%)."** This is a formatting/presentation concern, not a scientific weakness. It does not affect the evaluation of the paper's contributions.

5. **"TACD framework is speculative and not a contribution."** The paper transparently presents TACD as "a forward-looking blueprint rather than a complete implementation" (Section 5.3). Criticizing a paper for not implementing something it explicitly scopes out as future work is not fair.

6. **"Missing appendix proofs/implementation."** The parser strips appendix content. These exist in the original submission.

## Novel Insights

The most interesting observation is the *divergence* between closed-book MMLU (monotonically increasing with Arabic contamination) and extractive QA performance (non-monotonic, often peaking at 10% then declining). This suggests that contamination-driven memorization benefits multiple-choice option selection (surface-level pattern matching) more than it benefits span extraction (which requires fine-grained semantic alignment). The "peak at 10% then collapse" pattern for MLQA across multiple models hints at a sweet-spot phenomenon: small amounts of cross-lingual overlap provide useful anchor points, but larger contamination overfits to distributional quirks of the Arabic training data that do not transfer back to English evaluation. No reviewer raised this specific interpretation, but it is a genuinely subtle finding embedded in the paper's results that warrants further investigation.

## Suggestions

1. **Fix the internal contradiction in Section 4.2.** Clearly separate the narrative: (a) MMLU accuracy shows monotonic gains (contamination helps performance), (b) TS-Guessing scores are low for most models (detection methods are partially blinded), and (c) LLaMA's high IDR values complicate the story and should be discussed honestly rather than glossed over.

2. **Add a positive control experiment.** Fine-tune a model on the English MMLU test set and run TS-Guessing with choice reordering to demonstrate that the probe can detect known contamination. This would make the negative results for the Arabic setting interpretable.

3. **Discuss model-dependence explicitly.** LLaMA shows strong TS-Guessing signals while Mistral shows none. This is interesting — is it due to different Arabic proficiency levels, model size, or tokenizer overlap? The paper should explore this rather than making universal claims.

4. **Add a data-volume control experiment** (or at minimum discuss the confound transparently as a limitation).

5. **Restructure or shorten Section 2.** The literature review is comprehensive but overly long relative to the contribution. Moving some content to an appendix would allow more room for analysis and discussion.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` | 6.75 | Stronger methodology, cleaner claims, open-source release — this paper is less thorough |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` | 4.25 | Similar "detection evasion" theme; this paper has better experiments but similar issues with overclaiming |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` | 6.75 | Stronger theoretically with scaling law analysis — this paper is less rigorous |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` | 8.00 | Much stronger execution and clarity throughout — this paper is substantially weaker |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MyotJECv0D.md` | 2.50 | Much weaker paper with minimal contribution — this paper is substantially stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` | 5.67 | Cross-lingual LLM evaluation paper with similar methodological rigor — this paper is slightly weaker |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/syThiTmWWm.md` | 7.75 | Much stronger experimental design and more surprising findings |

The paper tackles a genuinely novel and important question (how translation interacts with contamination detection), and its multi-model multi-dataset design provides broad coverage. However, it has significant issues: an internal contradiction in Section 4.2 where the text claims "near-flat" performance while Table 2 shows clear monotonic MMLU gains, LLaMA's TS-Guessing IDR scores that contradict the "detection is blinded" narrative, and no positive control validating the TS-Guessing adaptation. These weaknesses prevent the paper from being accepted in its current form but do not invalidate the core research direction. Positioned against the calibration anchors, the paper is clearly above the ~2.5 level of weak submissions but well below the ~6.75+ level of strong contamination papers, clustering around the 4.0–4.5 band of "reasonable idea but execution/claims need major revision."

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>