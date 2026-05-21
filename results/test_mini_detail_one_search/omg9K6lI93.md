Now I have sufficient calibration material. Let me write the final review.

## Summary

This paper investigates whether translating benchmarks into Arabic can mask data contamination signals in LLM evaluation. The authors fine-tune four open-weight models on varying proportions of Arabic-translated test data from MMLU, XQuAD, and MLQA, then evaluate on the original English benchmarks. They extend the TS-Guessing memorization probe with a choice-reordering strategy and find that while models exhibit measurable performance gains from exposure to translated data, standard contamination probes (TS-Guessing) show limited signal — suggesting translation creates a blind spot. The paper also outlines a Translation-Aware Contamination Detection (TACD) framework as a future direction.

## Strengths

- **Novel problem framing with practical importance.** The question of whether multilingual translation masks contamination is underexplored in the contamination literature, which remains heavily English-centric. Identifying this blind spot is a genuine contribution regardless of the current experimental limitations.

- **Choice-reordering extension to TS-Guessing for MCQ contamination probing.** The paper introduces a concrete methodological improvement over prior TS-Guessing (Deng et al., 2024): shuffling answer labels before masking to isolate index-memorization as a contamination signal. This is clearly described in Section 3.3 and Figure 1, and the IDR metric in Table 3a provides some empirical signal.

- **Multi-model, multi-dataset systematic design.** The paper tests four models (0.5B–7B) across three datasets under four contamination proportions (0%, 10%, 50%, 100%), enabling comparative analysis. This is more thorough than many single-dataset contamination studies.

- **Nuanced finding about closed-book vs. extractive QA.** The observation that MMLU (closed-book MCQ) shows monotonic gains while XQuAD/MLQA (extractive QA) shows model-specific, non-monotonic trends (Section 4.1) reveals that contamination helps surface-form memorization while not improving — and sometimes harming — span localization. This goes beyond simply reporting accuracy increases.

## Weaknesses

### Major

- **Missing control condition: no English-contamination comparison.** The paper's central claim is that translation *specifically* masks contamination signals. However, there is no experimental condition where the same models are fine-tuned on directly contaminated English data (same proportions of English test items) to compare the resulting performance trends and TS-Guessing signals. Without this control, the observed "flatness" of TS-Guessing across Arabic contamination proportions could reflect: (a) translation masking contamination (the paper's claim), (b) TS-Guessing being generally insensitive in this fine-tuning regime regardless of language, or (c) the contamination effects being small and noisy overall. The paper explicitly claims "In typical same-language settings, increasing *p* would be expected to induce noticeable shifts" (Section 4.2), but provides no evidence for this assertion. This is the core evidential gap: the question posed by the title remains unanswered.

- **TS-Guessing probe is unvalidated on positive controls.** The choice-reordering extension is a reasonable methodological idea, but the paper never demonstrates it works as intended on a known-positive case (e.g., a model known to be contaminated on exact English test items). The IDR values are often very low and sometimes non-monotonic (e.g., Gemma-3-1B-it drops from 0.350 at 10% to 0.005 at 100%, Table 3a). The XQuAD/MLQA TS-Guessing results are near floor (EM ≤ 0.017 for most models, Table 3b). Without validation against a positive control, the low TS-Guessing signals cannot be interpreted as evidence that translation masks contamination — they may simply reflect that the probe is insensitive. This is an evidential issue: an uncalibrated instrument cannot support the paper's main interpretive claim.

- **Framing-contribution mismatch: pretraining vs. fine-tuning.** The literature review and discussion (Sections 2 and 6) frame the problem in terms of *pretraining* contamination, where models memorize benchmarks from web-scale training data. However, the experiments only study contamination introduced during *instruction fine-tuning* on small subsets of translated test data. These are fundamentally different regimes (data scale, learning dynamics, memorization behavior). The paper does not acknowledge this gap or argue why findings from fine-tuning should generalize to the pretraining setting. This overstates the paper's relevance to the community's core concern.

- **Narrative inconsistency between text and Table 2.** Section 4.2 states that "Across contamination levels *p* ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." However, Table 2 shows clear, non-flat differences: e.g., Mistral-7B MMLU goes from 0.580 (10%) to 0.690 (100%), a ~19% relative increase. LLaMA-3.2-1B MMLU goes from 0.381 to 0.431 (~13% relative). These are not "approximately equal" and the claim of flatness is misleading. The paper's central interpretive claim is contradicted by its own data.

### Minor

- **No statistical reliability.** No confidence intervals, standard deviations, or multiple random seed runs are reported. Given the modest model sizes (0.5B–7B), the small performance changes in some conditions, and the non-monotonic patterns (e.g., MLQA peaking at 10% then declining at 50%), the results could be dominated by random variation. This is standard practice for empirical studies.

- **The XQuAD/MLQA TS-Guessing probe conflates comprehension with memorization.** For extractive QA, the probe masks a critical token in the question while keeping the context (the passage) unchanged. A model that genuinely understands the passage can also fill in the mask through reasoning, so exact recovery does not specifically signal memorization (Section 3.3). This reduces the probe's specificity as a contamination detector.

- **TACD framework is a sketch, not a contribution.** Section 5 presents TACD as a "forward-looking blueprint" with three high-level components (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency). There is no implementation, validation, or concrete evaluation plan. While outlining future directions is acceptable, the paper presents this as a contribution when it is a vision statement.

- **Claim about "models with stronger Arabic capabilities benefiting more" is untested.** The paper asserts this (Abstract, Section 1) but provides no Arabic-language metric or model ranking to substantiate it. This claim is unsupported speculation.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Adding an English-paraphrased contamination condition (paraphrasing English test items without translation) would help disentangle whether the masking effect is specific to cross-language translation or generalizes to any surface-form perturbation.
- Reporting representation similarity (e.g., cosine similarity between English and translated item embeddings) would make the semantic-preservation argument concrete, as hinted in Section 4.3.
- Running each condition with multiple random seeds and reporting standard deviations would substantially strengthen reliability.

## Removed Points

- **"Missing appendix content, hyperparameters, dataset statistics"** — The paper states these are in Appendices A/B, which are stripped by the PDF parser. An invalid criticism aimed at a parser artifact.
- **"Embedding figure referenced but not present"** — This is a parser issue (the figure is an image file). The text references it; it exists in the submission.
- **"Literature review is overly long"** — A subjective style preference with no bearing on scientific validity.
- **"The claim about translation concealing contamination is presented before being demonstrated"** — This is a standard narrative structure (abstract/introduction stating findings upfront), not a substantive flaw.
- **Strength about TACD as a contribution** — TACD is a blueprint, not an implemented contribution. The paper itself describes it as a "forward-looking blueprint." This overstates what's been delivered.

## Novel Insights

The reviews surface one genuinely novel observation that goes beyond the paper's own contributions: the non-monotonic behavior of extractive QA under contamination (MLQA peaking at low contamination and declining at higher levels) suggests a more complex relationship between contamination and task performance than simply "more contamination = better scores." If contamination helps surface-form familiarity but hurts cross-lingual grounding in extractive tasks, this has implications for how we think about contamination in multilingual evaluation beyond what the paper develops. None of the other insights from the reviews go substantially beyond what the paper already argues.

## Suggestions

1. **Add the English-contamination control condition.** This is the single most important addition. Fine-tune the same models on English-only contaminated data at the same proportions (10%, 50%, 100% of English test items added to a baseline) and compare the resulting TS-Guessing signals to the Arabic-translated condition. If TS-Guessing detects English contamination but not Arabic, the central claim is supported.

2. **Validate TS-Guessing on a positive control.** Show that the probe produces high IDR values when applied to intentionally English-contaminated models, establishing that it can detect contamination when present.

3. **Acknowledge the fine-tuning vs. pretraining gap explicitly** and either (a) argue why fine-tuning findings should generalize, or (b) limit the paper's claims to the fine-tuning regime.

4. **Reconcile the narrative with Table 2.** Either revise the "approximately equal performance" claim to reflect the actual trends, or provide an analysis that justifies why the observed differences are considered small.

5. **Add error bars or multiple runs** to distinguish signal from noise, particularly for the non-monotonic MLQA results.

## Score and Decision

**Calibration anchors:**

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` (avg: 4.25, topic: evading contamination detection) — Similar topic and similar overall quality. The 4.25 paper had a clearer attack method but also lacked validation of defenses; the current paper has a more interesting question but weaker experimental support. Comparable.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` (avg: 6.75, topic: longitudinal contamination analysis) — Cleaner experimental design with a natural experiment (training cutoffs) and stronger evidence for its claims. The current paper does not meet this bar.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` (avg: 6.75, topic: forgetting contamination) — Combines controlled experiments with theoretical bounds. More rigorous execution. The current paper is substantially weaker empirically.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KS8mIvetg2.md` (avg: 7.50, topic: proving test set contamination) — Rigorous statistical framework with provable guarantees. Far stronger methodology. The current paper does not approach this level.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` (avg: 4.75, topic: memorization testing) — Similar scope. The 4.75 paper also had a probing-based approach with some unvalidated assumptions. Roughly comparable.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/syThiTmWWm.md` (avg: 7.75, topic: cheating LLM benchmarks) — Clean, surprising results with rigorous controls. The current paper is not in the same league.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ICwdNpmu2d.md` (avg: 1.50, topic: stock prediction) — Far weaker; no proper experimental validation. The current paper is substantially better.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OdoS6cH8MP.md` (avg: 2.00, topic: data valuation) — Poorly motivated with weak methodology. The current paper is stronger.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rAylWUIKtu.md` (avg: 4.25, topic: benchmark inflation / retro-holdouts) — Similar weakness: interesting idea but limited experimental support. Comparable quality.

The paper identifies a genuinely important and underexplored problem. However, the experimental design has a structural gap (no English-contamination control), the central detection probe is unvalidated, the narrative contradicts the data in places, and the framing oversells the scope. These issues are fundamental enough that they undermine the paper's core claims as currently presented. The paper would benefit substantially from adding the missing control condition before being ready for a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>