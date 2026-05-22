Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper investigates whether translating evaluation benchmarks into Arabic masks data contamination in LLM evaluation. The authors fine-tune four open-weight models on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated test data alongside the English test data, evaluate on the original English benchmarks, and use a choice-reordering extension of TS-Guessing (the IDR metric) to probe memorization. The core empirical finding — that MMLU accuracy rises monotonically with added Arabic-translated contamination (e.g., Mistral: 0.577→0.690) — is genuinely interesting and shows that translation does not eliminate contamination benefit. However, the paper's stronger claims about "masking contamination signals" and creating a "dangerous blind spot" are not adequately supported by the experimental design.

## Strengths

- **Novel research question on multilingual contamination dynamics.** The paper identifies an underexplored angle — whether translation into a low-resource language obscures contamination — and backs it with a controlled fine-tuning experiment that systematically varies contamination proportion. This is a timely and relevant problem given the increasing multilingual deployment of LLMs.

- **Clear empirical result on performance inflation via Arabic contamination.** Table 2 documents a consistent pattern: across all four models, MMLU accuracy increases monotonically as the proportion of Arabic-translated test data grows (e.g., LLaMA: 0.332→0.431; Gemma: 0.220→0.284). This demonstrates that models benefit from translated benchmark data even when the evaluation is in English — a finding that directly supports the claim that translation ≠ decontamination.

- **Multi-model, multi-dataset scope.** Experiments span four model families (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three datasets (MMLU, XQuAD, MLQA), reducing the chance that findings are an artifact of a single architecture or task format.

- **Choice-reordering IDR metric.** The extension of TS-Guessing with answer-letter reordering (Section 3.3) is a concrete methodological contribution — it probes whether a model relies on memorized index patterns rather than semantic reasoning, and is well-motivated for the MCQ setting.

## Weaknesses

### Major

1. **The p=0 baseline is already trained on the English test set, preventing a clean comparison.** The training data is defined as D_EN^d ∪ D_AR^d(p), where D_EN^d is explicitly "English test items formatted as MCQ" for MMLU. This means even the p=0 condition has been fine-tuned on the exact English test set. Consequently: (a) the paper cannot compare against a genuinely clean model to measure contamination effects; (b) the "masking" claim requires showing that Arabic contamination is harder to detect than English contamination, but the baseline is already the most contaminated condition (English test set memorized). The experimental design studies how *additional* Arabic-translated data affects a model already exposed to the English answers, which is a substantially different question from whether translation obscures realistic contamination. This is the most serious weakness.

2. **No TS-Guessing results for the p=0 condition (Table 3).** Table 3 reports IDR and ROUGE-L F1 for p=10, 50, 100 only. Without TS-Guessing at p=0 — where the model has been fine-tuned on the English test set — the reader cannot assess whether Arabic translation *reduces* detectability relative to English-only contamination. The paper's central claim that translation "conceals traditional contamination signals" hinges on this comparison, yet it is absent. The non-monotonic IDR patterns (e.g., LLaMA: 0.287→0.643→0.410) are also left unexplained and could be noise from single-run measurements.

3. **Internal inconsistency in results interpretation.** Section 4.2 states that "the models exhibit approximately equal performance on all evaluated benchmarks" across contamination levels and that this "near-flat trend indicates that Arabic→English translation is effectively masking contamination effects." But Table 2 shows MMLU rising monotonically for all models (e.g., Mistral: 0.580→0.690→0.690; relative increase of ~19%). Section 4.3 then correctly observes that "MMLU increases monotonically with contamination," directly contradicting the earlier claim of near-flatness. This coherence failure undermines trust in the analysis.

4. **The "dangerous blind spot" claim is unsupported.** The paper argues that translation creates a blind spot in current evaluation practices, but it never tests any existing detection method (Min-K% Prob, guided prompting, corpus-level search) on the translated data to demonstrate that they fail. Only the authors' own TS-Guessing variant is used. Without showing that established methods indeed miss translated contamination, the claim is an overreach. Related work in the literature review thoroughly discusses these methods, so the gap is conspicuous.

5. **TACD is presented as a contribution but is not implemented.** The Translation-Aware Contamination Detection framework receives a full section (Section 5) and is mentioned in the title, abstract, and conclusion, but the paper acknowledges it as "a forward-looking blueprint rather than a complete implementation." No experiments, baselines, or empirical evaluation are provided. A detection framework proposed without any demonstration does not constitute a scientific contribution in the current paper.

### Minor

- **No statistical significance or variance estimates.** Results are reported from single runs per condition with no error bars, confidence intervals, or standard deviations. Given the small scale of the experiments and non-monotonic patterns in XQuAD/MLQA, reported differences could be noise.

- **Ambiguity in the "embedding figure" reference.** Section 4.3 references "The embedding figure shows that Arabic→English translations remain close to their English originals in representation space" without providing the actual figure or quantitative similarity values. This claim is stated qualitatively without supporting evidence.

### Trivial

- The literature review (Section 2) is disproportionately long (~2/3 of the pre-experiment body) relative to the experimental contribution, but the survey is competent and well-structured.
- Minor: the paper refers to "Appendix B" for dataset statistics and "Appendix A" for hyperparameters, which were stripped by the PDF parser; these are not evaluable from the current submission.

## Nice-to-Haves

- Testing existing detection methods (Min-K% Prob, guided prompting) on the translated training data to empirically support the "blind spot" claim
- Adding a truly clean baseline (no English test set in training) to measure the full contamination effect
- Including TS-Guessing at p=0 for comparison
- Reporting embedding similarity values quantitatively instead of referencing a missing figure

## Removed Points

- **"Experimental design invalidates the paper's core claims" as fatal:** While the p=0 issue is a major weakness, the paper's core finding (Arabic-translated contamination boosts MMLU performance) is still supported by the data. The design does not invalidate this result — it limits the scope of what can be concluded about "masking." Demoted from Fatal to Major.
- **Criticism about not testing standard detection methods being absent:** Kept as Major weakness 4 — it is a real gap, but the paper's claim about "dangerous blind spot" goes beyond what the evidence supports.
- **Strength Finder's claim about "TS-Guessing with choice reordering being a concrete methodological improvement":** Kept as a strength — the IDR extension is methodologically sound.
- **Strength Finder's "multi-model, multi-dataset ablation":** Kept — this is a genuine strength.
- **Strength Finder's "non-monotonic analysis of extractive QA":** WEAKENED — it is a descriptive observation, not a strength per se. It remains because the observation is empirically grounded.
- **Harsh critic's claim that "the entire experiment studies overfitting to the test set, twice":** This overstates the case. The paper's finding that adding Arabic-translated data on top of English test set data further increases MMLU accuracy is informative about translation-mediated contamination, even if the baseline is imperfect. Removed the framing but kept the underlying concern.
- **Harsh critic's point about the "embedding figure" not being shown:** The figure may have been stripped by the PDF parser. Removed as a parser artifact concern.
- **"Missing related works":** Removed per hard rule — I cannot verify what related works exist beyond those in the paper.

## Novel Insights

The reviews surface an interesting tension: the paper's *stated* contribution (translation masks contamination) is undercut by its own design choices (p=0 already contaminated), but the *actual* finding is arguably more provocative — even when a model has already memorized the English test answers, Arabic translations of the same content still provide additional performance lift. This suggests that translation introduces some representation-level complementarity rather than simple duplication, which is a direction the paper does not fully explore. The non-monotonic XQuAD/MLQA results (peaking at 10% then declining) also hint at task-specific dynamics worth investigating further, though the single-run setup makes interpretation tentative.

## Suggestions

1. **Add a truly clean baseline.** Either evaluate the off-the-shelf base model without any fine-tuning, or fine-tune on an unrelated Arabic dataset (not the test set). This would establish the uncontaminated reference point needed to measure contamination effects.
2. **Include TS-Guessing at p=0.** Without this, the paper cannot support claims about translation reducing detectability relative to English-only contamination.
3. **Test at least one existing detection method (e.g., Min-K% Prob).** If the paper claims a "dangerous blind spot," it must show that current methods fail on translated data.
4. **Reconcile Section 4.2 and 4.3.** The text should acknowledge the MMLU increases directly rather than claiming flatness, and reframe the "masking" discussion around the XQuAD/MLQA results where trends are less clear.
5. **Either implement TACD with experiments or remove it as a claimed contribution.** A blueprint for future work belongs in a "Future Directions" paragraph, not in the title/abstract as a key contribution.

## Score and Decision

**Round 1 bracketing:** I compared the paper against anchors at three score bands. The weak band (avg 2.0–3.25) contained clearly weaker papers (unrelated topics, poor methodology). The middle band (4.25–6.75) contained the most relevant comparison — *Evading Data Contamination Detection for Language Models is (too) Easy* (4.25, Reject) — which studies a similar evasion-of-detection question. The strong band (7.5+) contained top-tier papers far beyond this paper's quality. Initial bracket: **3.5–6.0.**

**Round 2 narrowing:** I retrieved additional anchors in the (3.5, 5.5) and (5.5, 7.0) ranges. Comparing against:
- *Evading Data Contamination Detection* (4.25, Reject): This paper similarly studies evading detection but tests against actual detection methods. Our paper has a more controlled contamination experiment but lacks testing of existing detectors. Roughly comparable quality.
- *Benchmark Inflation: Revealing LLM Performance Gaps* (4.25, Reject): Methodologically stronger than our paper but narrower scope. Our paper addresses a more novel angle.
- *How much can we Forget about Data Contamination?* (6.75, Reject): Significantly more rigorous, with extensive scaling experiments and theoretical analysis. Our paper is substantially weaker.
- *Fine-tuning can Help Detect Pretraining Data* (6.25, Accept): Clean methodology and strong empirical results. Our paper is weaker.

Our paper's core experimental finding is genuine, but the design issues (p=0 baseline contaminated, missing p=0 TS-Guessing, internal inconsistency) and overclaiming prevent acceptance. It is somewhat stronger than the 4.25 papers due to a more novel research question and controlled experiment, but significantly weaker than the 6.25+ papers. This places it at the borderline.

**Final score: 4.5** — a borderline reject. The paper identifies an important underexplored problem and presents one genuinely interesting result (MMLU inflation persists through translation), but the experimental design prevents it from supporting its central claims about detection masking, key baselines are missing, and the framing overreaches relative to the evidence.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>