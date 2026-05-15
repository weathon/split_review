Here is my consolidated review, with all claims verified against the paper text.

---

## Summary

This paper identifies labeling errors in existing REC benchmarks (14% in RefCOCO, 24% in RefCOCO+, 5% in RefCOCOg), shows that removing noisy instances raises model accuracy by 1.57–3.08 points, and introduces Ref-L4 — a new, substantially larger and more diverse REC benchmark with 45,341 annotations, 365 categories, expressions averaging 24.2 words, and a vocabulary of 22,813 words. The authors evaluate 24 LMMs under multiple protocols (standard accuracy, scale-aware, per-category, cross-source), providing a comprehensive snapshot of current REC capabilities.

## Strengths

- **Identifies and quantifies high labeling error rates in widely-used benchmarks.** Through manual examination (Table 1), the paper reports error rates of 14% in RefCOCO, 24% in RefCOCO+, and 5% in RefCOCOg. Reevaluating four models on cleaned versions shows consistent accuracy improvements of 1.57–3.08 points (Table 2), providing concrete evidence that benchmark noise inflates reported performance.

- **Introduces Ref-L4, a substantially larger and more diverse REC benchmark.** Compared to RefCOCO/+/g, Ref-L4 includes 45,341 annotations (2–3× more), 365 categories (4.6–5.1× more), average expression length 24.2 words (2.9–6.7× longer), and vocabulary 22,813 words (4.5–6.5× larger) (Table 3). The data sources span both COCO and Objects365, providing broader coverage.

- **Provides a rigorous, multi-faceted evaluation of 24 LMMs.** The evaluation includes accuracy at multiple IoU thresholds (Acc₀.₅, Acc₀.₇₅, Acc₀.₉, mAcc), scale-aware performance (small/medium/large in Table 5), per-category analysis (Figure 2), and cross-source evaluation (Figure 6) revealing training biases and domain gaps. This establishes a useful baseline for the community.

- **Cross-source evaluation reveals training bias in an interpretable way.** By partitioning Ref-L4 into COCO-derived, Objects365-overlapping, and Objects365-novel subsets, the paper demonstrates that models perform worst on categories unseen in COCO, providing actionable insight into generalization weaknesses of current LMMs (Figure 6).

- **Releases cleaned versions of RefCOCO, RefCOCO+, and RefCOCOg, plus the Ref-L4 benchmark.** These resources enable the community to build on the findings and use the new benchmark for future evaluation.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Error rate assessment lacks documentation of annotation protocol.** The paper claims 14%, 24%, and 5% error rates but reports no details on the manual assessment: number of annotators, inter-annotator agreement, annotation guidelines, or how borderline cases (e.g., multiple valid bounding boxes) were handled. While an appendix section (referenced as §sec:label_error) likely contained additional detail stripped by the PDF parser, the main paper's description remains too brief for the error rates to be considered rigorously established. This weakens a finding used to motivate the paper's central argument, though it does not undermine the primary contribution (Ref-L4) since the cleaned datasets are released and independently verifiable.

- **Human review process for Ref-L4 is described qualitatively but not quantified.** The paper states that manual review corrected hallucinations and ensured factual accuracy, but reports no statistics: number of reviewers, percentage of expressions that required correction, inter-reviewer agreement, or how disagreements were resolved. Since the value of the benchmark depends on annotation quality, this transparency gap limits the reader's ability to assess reliability. The prominence of this concern is mitigated by the fact that the full dataset is released for community scrutiny.

- **No direct evidence that Ref-L4 captures *different* model capabilities than existing benchmarks.** The paper shows that Ref-L4 is larger, longer, and more diverse, but does not demonstrate that model *rankings* diverge from those on RefCOCO or that Ref-L4 reveals gaps invisible on existing benchmarks. The cross-source and scale-aware analyses are useful but do not directly address whether the benchmark provides complementary information to existing ones. A rank-correlation analysis (e.g., Spearman's ρ between model rankings on Ref-L4 vs. RefCOCO) would strengthen this claim.

- **No evaluation of semantic equivalence for rephrased expressions.** The annotation expansion step uses GPT-4 to rephrase expressions, followed by human review, but the paper does not verify whether rephrased variants are semantically equivalent or whether they differ in ways that affect model behavior (e.g., introducing subtle ambiguities or changing the referent). This is a standard concern for any generated dataset.

- **No discussion of whether multiple valid annotations exist.** The paper treats all errors as definitive mistakes but does not acknowledge that some "errors" could reflect genuine alternative annotations (e.g., multiple valid bounding boxes for the same instance). A more nuanced error taxonomy would improve credibility.

### Trivial

- **Inconsistency in instance size definition across sections.** The analysis (§3.2, Figure 3.2) defines instance size as the square root of *normalized* size sqrt(hw/HW), while the scale-aware evaluation (§3.3, Table 5) and dataset comparison (Table 3) use absolute sqrt(hw). This inconsistency is confusing and should be harmonized.

- **The vocabulary analysis (Figure 4) lists part-of-speech distributions without connecting them to evaluation difficulty.** It is descriptive but not actionable for understanding model behavior.

## Nice-to-Haves

- A human baseline on Ref-L4 (accuracy of human annotators given the same referring expressions) would establish an upper-bound and verify that expressions are unambiguous.
- Reporting model performance on individual expression-length bins (e.g., short vs. long) could provide more insight into where models struggle.
- Confidence intervals or error bars on the main results (Table 4) would strengthen comparative claims, though their absence is standard practice for large-scale benchmark evaluations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that error identification methodology lacks prompt details (appendix).** The paper explicitly references appendix sections (§sec:prompt_instance-level, §sec:prompt_contextual, §sec:prompt_rephrase, §sec:label_error) for these details. The PDF parser stripped the appendix; the original submission contained them. Removed per rule about missing appendix content.

- **"No figure showing examples of errors."** Such figures would have been in the stripped §sec:label_error appendix section. Same rationale as above.

- **"CogVLM-Grounding and SPHINX variants may have seen Objects365 during training."** The paper already acknowledges this limitation in the cross-source analysis (line 336: "partially because most models are trained on the RefCOCO series and have limited exposure to Objects365 images"). This is a known property of the evaluation setting, not an oversight.

- **"No confidence intervals or statistical tests."** Single-run evaluation on large benchmarks is the standard practice in this field. Requesting confidence intervals is a methodological preference, not a shortcoming.

- **"The paper does not release cleaning criteria."** The paper states it releases the cleaned datasets. The exact criteria for removal are implicit in what was filtered, and the cleaned versions are independently inspectable. The reviewer's phrasing ("cannot be independently verified") overstates the issue.

- **Strength Finder claim that is too generic:** None of the strength finder's strengths were generic or conflicting with verified weaknesses, so no strength was removed.

- **"Analysis is descriptive but not actionable"** — the analysis is intended to characterize the dataset, not to be directly actionable. This is a scope expectation mismatch.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Quantify the annotation pipeline.** Report the number of human reviewers, the percentage of GPT-4V-generated expressions that required correction, and inter-reviewer agreement statistics (even if informally). This is the single most impactful improvement for the camera-ready version.

2. **Add a ranking correlation analysis.** Show whether model rankings on Ref-L4 (e.g., by mAcc) correlate with rankings on RefCOCO or its cleaned version. If rankings diverge, this concretely demonstrates that Ref-L4 captures different capabilities.

3. **Harmonize the instance size definition** across the analysis and evaluation sections, or clearly explain why two different definitions are used.

4. **Add a brief discussion of the ambiguity of bounding box annotations** — noting that some "errors" might be legitimate alternative annotations — to preempt concerns about the error rate methodology.

## Score and Decision

The paper tackles a well-motivated problem, makes a concrete contribution with Ref-L4, and provides a thorough evaluation of 24 models. The weaknesses are about methodological transparency and missing validation analyses, not about fundamental flaws in the contribution. The benchmark itself, released cleaned datasets, and extensive evaluation are valuable resources for the community. The paper would be strengthened by quantifying the human review process and adding a ranking-correlation analysis, but these are addressable improvements rather than fatal omissions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>