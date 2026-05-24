## Summary

This paper presents a detailed case-study re-analysis of a high-profile ICLR 2025 Oral paper on min-p sampling. Through four independent lines of investigation (human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community-adoption claims), the authors demonstrate that the original paper's evidence does not support its central claims. The paper introduces a novel "Best-of-N" methodology for controlling hyperparameter tuning volume in comparative evaluations, applies correct statistical testing with multiple-comparison corrections, and derives six generalizable lessons for rigorous empirical ML research. The work is a well-executed methodological critique that doubles as a practical blueprint.

## Strengths

1. **Discovery of omitted human evaluation data (Section 2.1).** The authors found that the original paper excluded 1/3 of collected scores (the basic-sampler condition) without justification, confirmed the omission with the original authors, and showed that including the data changes the paper's conclusions. This is clean, verifiable investigative work.

2. **Novel "Best-of-N" analysis for controlling hyperparameter volume (Section 3.1, Figures 4–5).** The paper introduces a principled subsampling method that equalizes the number of hyperparameters searched across samplers before measuring maximum performance. Applied across 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters (~6000 A100-hours), this analysis shows that min-p's claimed advantage disappears when tuning effort is controlled. This is the paper's strongest and most generalizable contribution.

3. **Rigorous statistical re-analysis with proper corrections (Table 1).** The paper applies one-sided paired t-tests with Bonferroni correction (and an Intersection-Union Test as an even stronger standard), correctly demonstrating that the original claim of "consistent" outperformance is unsupported by its own data. This directly illustrates the blueprint's lesson about transparent statistical practice.

4. **Verification of retracted community-adoption claims (Section 5).** The authors independently compute that the claimed 54,000 GitHub repositories and 1.1M stars are impossible given that leading LM repositories sum to 453k stars. The original authors retracted both claims. The observation that 3 of 4 reviewers cited these numbers as justification for acceptance is a powerful illustration of why the blueprint's lessons matter.

5. **Transparency and self-awareness about limitations.** The paper acknowledges its own limitations (only GSM8K evaluated, reliance on informal evidence for one finding) rather than over-claiming. This intellectual honesty strengthens the credibility of the overall critique.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core contribution.

### Minor

1. **NLP benchmark evidence is limited to GSM8K.** The paper's central empirical claim—that samplers perform approximately equally when given equal hyperparameter tuning—is demonstrated on only one math reasoning task. The original paper also reported GPQA results, and generalizing from GSM8K alone is a narrower evidence base than the headline claim suggests. The authors acknowledge this as a compute-budget limitation (line 208), but the scope constrains the generality of Lesson 1.

2. **The selective-reporting claim in Section 4.3 relies on a Telegram link.** The allegation that the original paper reported the higher of two scores for min-p but the lower for top-p is supported by a Telegram post from the first author. While the claim may be factually correct, this evidence is less independently verifiable than the rest of the paper's analyses. The methodological concerns in Sections 4.1 and 4.2 (under-specification, unequal tuning, indirect comparisons) stand on their own and are more robust. The Telegram-dependent claim should be either backed by a reproducible source or framed more cautiously.

3. **The "Best-of-N" analysis controls hyperparameter *count* but not *coverage* or *quality* of the hyperparameter space.** Equalizing the *number* of hyperparameter values searched does not guarantee that the values themselves are comparably informative or span equivalent regions of the space. This is a nuance worth noting, though it does not undermine the analysis's intended purpose (detecting cherry-picking).

4. **The paper does not present its own analysis of the GPQA benchmark**, even though the original paper used it. While the authors cite compute budget, readers evaluating the claim "min-p does not outperform" must rely on GSM8K extrapolation for the NLP dimension.

### Trivial
None. The paper is well-written and cleanly presented.

## Nice-to-Haves

- Extending the NLP sweep to GPQA (even with fewer models) would broaden the empirical base for the claim about equal performance under controlled hyperparameter volume.
- A reproducible alternative to the Telegram evidence for Section 4.3 would strengthen that claim, or alternatively framing it as a plausible interpretation rather than a definitive finding.

## Novel Insights

The most insightful aspect of the reviews is the observation that the paper's main contribution is not any single individual lesson (most are individually familiar) but rather the *integrative demonstration* of how multiple flawed methodological practices can compound within a single high-profile publication, and how each can be systematically detected and corrected. The Best-of-N methodology is genuinely novel as a *detection* tool for cherry-picking, not just a fairness mechanism. The review process also surfaces a meta-lesson: the fact that this paper will likely need to exist to correct for the original paper's success—and that 3 of 4 original reviewers cited the now-retracted community-adoption numbers as justification—raises uncomfortable questions about whether current review processes are structurally vulnerable to the kinds of errors this blueprint diagnoses.

## Suggestions

- Add a small-scale GPQA analysis (even 4–5 models, 3 seeds) to extend the claim beyond GSM8K. Alternatively, reframe the NLP section's headline to explicitly scope the conclusion to GSM8K.
- Either provide the Telegram link or supplementary data that independently verifies the selective-reporting claim in Section 4.3, or downgrade the certainty of that claim from a finding to a flagged concern.
- Add a brief discussion of the limitation that "Best-of-N" controls hyperparameter *count* but not hyperparameter *quality* or *coverage*.

## Removed Points

Points flagged for removal (treat with caution):

- *"Weaknesses about missing appendix/missing proofs"* — The appendix exists in the original submission; the parser stripped it. Removed per hard rules.
- *"The paper sometimes uses slightly strong language"* — Pure presentation nitpick with no substance. Removed.
- *"Telegram evidence is hearsay" framed as a fatal weakness* — The harsh critic raised this as a critical issue, but it does not invalidate the paper's core claims. The other points in Section 4 (under-specification, unequal tuning) stand independently. Demoted to minor weakness above.
- *"The lessons are not novel in isolation"* — While true, this is not a weakness for a blueprint paper that derives its value from integrative demonstration. Removed.
- *Generic strengths from the Strength Finder about "important problem"* — These are superficial/generic. Removed per filtering rules.

## Score and Decision

**Calibration Summary**

All anchors retrieved across rounds 1 and 2:

**Round 1 (Bracketing, 5.5–7.5 bracket):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CpiOUOaqh3.md` — avg 2.00 (epidemiological modeling, irrelevant topic, far weaker)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/V83xzYnZ5q.md` — avg 3.00 (tuberculosis forecasting, irrelevant topic)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FYvZCwdb6F.md` — avg 3.00 (viral tweet prediction, irrelevant topic)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ReccFdn4zE.md` — avg 2.00 (ionospheric modeling)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GbEmJmnQCz.md` — avg 4.40 (memorization critique paper, **most similar genre**; our paper is clearly stronger — more thorough, more evidence types, novel methodology)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lf8QQ2KMgv.md` — avg 3.75 (memorization critique paper, similar genre; our paper is stronger)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rSAPrQzoQa.md` — avg 5.00 (subject clustering, irrelevant topic)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/X8aFMdXk3N.md` — avg 4.25 (TSF benchmark critique; our paper is stronger — more thorough, more novel methodology)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EUSkm2sVJ6.md` — avg 7.60 (data usage inference; different genre, stronger technical contribution)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` — avg 8.00 ("Training on the Test Task," critique paper; our paper is not at this level — that paper identifies a more fundamental, field-wide problem)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cNmu0hZ4CL.md` — avg 8.00 (neural dynamics, unrelated)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/A3YUPeJTNR.md` — avg 8.00 (prediction-driven allocations, unrelated)

**Round 2 (Narrowing, 6.0–7.0 bracket):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E8gYIrbP00.md` — avg 6.75, Accept ("Beyond correlation" — critique of evaluation metrics; comparable quality, accepted. Our paper is slightly more thorough in its case study but less novel in its proposed method)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hYU0P4Wlj9.md` — avg 6.25, Reject (LIME-Eval; different subfield, less relevant)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m8yby1JfbU.md` — avg 6.50, Accept (video LM judge reliability; comparable quality, accepted)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/icTZCUbtD6.md` — avg 6.20, Accept (hardness characterization; different genre)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fXJCqdUSVG.md` — avg 6.50, Accept ("Durability of Safeguards" — **closest genre match**; case-study critique of evaluation pitfalls, accepted. Our paper is similarly thorough across more evidence types)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Q2bJ2qgcP1.md` — avg 6.00, Accept (CATE benchmark; different topic, accepted)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yuy6cGt3KL.md` — avg 7.25, Accept (CATE model selection; different topic)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GqI4fTVUXC.md` — avg 6.00, Reject (theory-practice disconnect; different genre)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/g16vmAtJ8x.md` — avg 6.00, Reject (privacy metrics critique; our paper is comparably thorough but addresses a more timely case study)

**Final position:** The paper sits above the memorization critique papers (3.75–4.40) and the TSF benchmark paper (4.25), and is comparable to the "Beyond correlation" (6.75, Accept) and "Durability of Safeguards" (6.50, Accept) papers. It is not at the 8.0 level of "Training on the Test Task," which diagnoses a more fundamental field-wide problem. The Best-of-N methodology is a genuine novel contribution, the case study is impactful, and the blueprint lessons are well-anchored in the evidence.

**Score: 6.5 — Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>