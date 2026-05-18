Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper first identifies labeling error rates of 14%, 24%, and 5% in the RefCOCO, RefCOCO+, and RefCOCOg benchmarks respectively, and releases cleaned versions. It then introduces Ref-L4, a new REC benchmark with 45,341 annotations across 365 categories, featuring long referring expressions (avg. 24.2 words) and a large vocabulary (22,813 words). The paper evaluates 24 LMMs using multiple metrics (Acc₀.₅, Acc₀.₇₅, Acc₀.₉, mAcc) and provides scale-aware and category-wise analysis.

## Strengths

- **Quantification of labeling errors in existing benchmarks (Table 1):** The manual examination revealing 14% (RefCOCO), 24% (RefCOCO+), and 5% (RefCOCOg) error rates directly supports the claim that benchmark noise undermines evaluation authenticity. This is a concrete, useful finding.
- **Demonstration that cleaning reveals hidden model capability (Table 2):** Accuracy improvements of 1.57–3.08 points across four LMMs on cleaned versions provide causal evidence that noise was suppressing measured performance.
- **Introduction of a substantially more comprehensive benchmark:** Ref-L4 (45,341 annotations, 365 categories, avg. 24.2 words, 22,813 vocabulary) meaningfully advances beyond RefCOCO/+/g in scale, diversity, and linguistic complexity (Table 3).
- **Large-scale evaluation with fine-grained analysis:** 24 LMMs evaluated at multiple IoU thresholds, across instance sizes (small/medium/large), per-category, and across data sources (COCO vs. O365-P1 vs. O365-P2). This provides insights not possible with older benchmarks — e.g., CogVLM-Grounding excelling on small instances while SPHINX-v2-1k leads on large instances (Table 5).
- **Rigorous annotation pipeline with human verification:** GPT-4V generation followed by manual review to correct hallucinations and ensure uniqueness (Section 3.1, Step-3) and a two-stage rephrasing process with manual review (Annotation Expansion).
- **Release of cleaned benchmark versions:** Corrected versions of RefCOCO, RefCOCO+, and RefCOCOg are released, enabling future work to build on cleaner data.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained GPT-4V near-floor performance (9.91% Acc₀.₅).** GPT-4V's result is catastrophically low compared to every other model (e.g., OFA-Tiny 55%, CogVLM-Grounding 82%) yet the main text contains zero discussion or analysis of this anomaly. The paper merely notes the evaluation prompt is in the appendix and moves on. While this does not invalidate the benchmark or the other 23 model evaluations, the omission is conspicuous. Readers are left wondering whether the evaluation protocol for GPT-4V is broken (prompt parsing issue, inability to follow coordinate-output instructions) or whether the gap is genuinely informative. A brief discussion — even showing a few qualitative examples of GPT-4V outputs — would resolve this and strengthen confidence in the overall evaluation pipeline.

### Minor

2. **The per-category "training bias" claim lacks quantitative support.** The paper states (Section 4) that Figure 5 shows "a training bias issue, as all four models exhibit poor performance on some common categories" but provides no correlation analysis between model performance and category frequency in training data. This observation is presented as a finding but remains superficial; a simple rank-correlation test would substantiate or qualify the claim.

3. **The error-detection methodology, while referenced to the appendix, is opaque in the main text.** The paper says errors include "typos, misalignment between referring expressions and target instances, as well as inaccurate bounding box annotations" and cites Section sec:label_error (appendix). However, the main text does not clarify who performed the manual examination, how many annotators were involved, what specific criteria defined each error type, or whether inter-annotator agreement was measured. Since these error rates (14–24%) are a key motivation for the cleaned datasets and the new benchmark, this opacity is a limitation. The appendix likely contains some of this detail (which the parser strips), but the authors should integrate a summary in the main text.

### Trivial

None.

## Nice-to-Haves

- **Human performance baseline on a random subset of Ref‑L4** would calibrate how far current models (CogVLM at 81.70%) are from ceiling, and help contextualize the GPT-4V result.
- **Statistical significance tests (e.g., bootstrap)** for the accuracy improvements in Table 2 would strengthen the claim that cleaning effects are beyond sampling noise.
- **Data contamination disclosure:** Several evaluated models may have been trained on Objects365. Discussing which models have seen these images would help interpret the COCO vs. O365 performance gaps.
- **Expression quality analysis** for the GPT-4V-generated portion (how often human reviewers corrected hallucinations, common error types) would further validate benchmark quality.

## Removed Points

- **"The error rates are unverifiable and could reflect subjective judgment"** — The paper explicitly references Section sec:label_error for the error detection methodology, which is in the appendix (stripped by the parser). Per hard rules, we assume this content exists in the original submission.
- **"GPT-4V's result casts doubt on the entire experimental setup"** — Overstatement. The other 23 models produce consistent, reasonable results. An issue with one model's evaluation does not invalidate the benchmark or the rest of the evaluation.
- **"The composition of Ref‑L4 creates a potential circularity"** — The "cleaned" portion and the Objects365 portion involve separate validation steps (human review of GPT-4V outputs is independent of the RefCOCO error detection). The concern about GPT-4V language bias is valid as a suggestion but does not constitute a structural flaw, as Step-3 human review explicitly corrects hallucinations.
- **"The benchmark division makes the validation set redundant"** — Many benchmarks provide this structure. The paper explicitly recommends using the combined set, which is a clear and reasonable design choice.
- **"Very brief referring expressions... is well known"** — The paper's contribution is quantifying this (not discovering it), and the error rates are the novel part.
- **"The paper does not discuss whether very small instances (√area=30) are resolvable by typical input resolutions"** — CogVLM achieves 75% Acc₀.₅ on small instances, empirically demonstrating resolvability.
- Several generic or unfounded criticisms from the strength finder were filtered out as they did not apply.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a brief paragraph analyzing GPT-4V's 9.91% result — show a few qualitative examples and clarify whether the evaluation protocol is sound or if a parsing issue exists.
2. Add a short quantitative analysis (e.g., Spearman correlation) linking per-category performance to category frequency in training data to substantiate the "training bias" claim.
3. Include a brief summary of the error-detection methodology (who, criteria, agreement) in the main text rather than deferring entirely to the appendix.
4. Consider adding a human performance estimate on a small random subset (100–200 examples) as a sanity check on benchmark difficulty.

## Score and Decision

I assign a score of **7.0 / 10**. The paper makes real contributions — a useful new benchmark, cleaned versions of existing datasets, and a broad model evaluation. The weaknesses (undiscussed GPT-4V anomaly, superficial per-category analysis, opaque error-detection methodology in the main text) are addressable and do not invalidate the core contributions. The paper is a solid contribution to the REC / LMM evaluation community and should be accepted after addressing these issues.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>