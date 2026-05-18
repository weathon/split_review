Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

The paper identifies labeling errors in the RefCOCO/RefCOCO+/RefCOCOg benchmarks (reporting 14%, 24%, and 5% error rates respectively), releases cleaned versions of these datasets, and introduces **Ref-L4** — a new REC benchmark characterized by large scale (45,341 annotations, 365 categories, average 24.2 words per expression, 22,813 vocabulary). The paper evaluates 24 modern LMMs on Ref-L4 with multi-threshold accuracy, scale-aware, and per-category analyses, showing that existing benchmarks are saturating while Ref-L4 exposes meaningful performance differentiation among models.

## Strengths

- **Quantification and correction of labeling errors in legacy benchmarks.** The paper manually examines RefCOCO/RefCOCO+/RefCOCOg and reports concrete error rates (Table 1). By releasing cleaned versions and demonstrating that removing erroneous instances yields consistent accuracy gains of 1.6–3.1 points across five models (Table 2), the paper provides causal evidence that benchmark noise inflates reported performance — a concrete, actionable finding.

- **Construction of a genuinely more challenging benchmark (Ref-L4).** Ref-L4 surpasses prior benchmarks across all four claimed dimensions: 45,341 annotations vs. ≤21,586, 365 categories vs. ≤78, average expression length 24.2 words vs. ≤8.4, and vocabulary of 22,813 words vs. ≤5,050 (Table 3). This creates a harder test bed for modern LMMs where even the best model (CogVLM-Grounding) achieves only 81.7% Acc₀.₅ — far from saturation.

- **Comprehensive evaluation with fine-grained analysis.** The paper evaluates 24 LMMs using Acc₀.₅, Acc₀.₇₅, Acc₀.₉, mAcc, scale-aware breakdowns (Table 5), and per-category performance (Figure 4). The O365-P1 vs. O365-P2 comparison (Figure 5) shows that models struggle more on categories not present in COCO, providing a useful signal about generalization to novel categories.

- **Release of cleaned RefCOCO series and the Ref-L4 benchmark.** These are practical community resources that directly enable more trustworthy evaluation on legacy benchmarks and more challenging evaluation on the new one.

## Weaknesses

### Major
None.

### Minor

- **GPT-4V's near-random performance (9.91% Acc₀.₅) is not discussed or explained.** This result is extraordinary — a state-of-the-art multimodal model performing barely above chance on a benchmark that claims to evaluate LMMs. The main text simply reports the number without analysis. While the evaluation prompt is in the appendix, the paper should at minimum discuss whether this reflects a genuine limitation of GPT-4V's spatial reasoning, an evaluation artifact (e.g., coordinate formatting mismatch), or a prompt design issue. The absence of any commentary on this outlier undermines confidence in the evaluation protocol and is a missed opportunity for an interesting finding.

- **Tension between claimed error rates (14–24%) and observed accuracy improvements (2–3%) is not addressed.** If 14–24% of annotations in RefCOCO/RefCOCO+ are errors, removing them might be expected to produce larger accuracy shifts than the observed 1.6–3.1 points. The paper does not discuss whether most errors are "harmless" (e.g., boxes slightly off but still within IoU 0.5), whether the error definition is overly broad, or whether models are simply robust to certain error types. While the error analysis is presented as motivation rather than the core contribution, this discrepancy should be acknowledged and explained.

- **The "encourage combined use" recommendation undermines the benchmark's structure.** The paper explicitly encourages combining val and test sets for evaluation (Section 3.3). While the reasoning (models train on unrestricted data) is acknowledged, providing a strict held-out test split would make the benchmark more useful as a community leaderboard and give users the option of a cleaner evaluation. The current recommendation blurs the distinction between validation and testing, which is unusual for a benchmarking paper.

- **The "training bias" attribution for per-category performance is asserted without evidence.** The paper states that poor performance on common categories (e.g., "Cabinet/shelf," "Flag") reflects "training bias" (Section 4), but provides no analysis — e.g., checking whether these categories are rare in training data, or whether the expressions for these categories are inherently more ambiguous. Alternative explanations (e.g., category ambiguity, expression quality) are equally plausible.

- **No per-instance analysis accounting for paraphrases as repeated measures.** Since 45,341 annotations are rephrasings of 18,653 unique instances (~2.43 variants each), results could be biased toward instances with more paraphrases. The paper should report at least one analysis that averages performance across paraphrases per instance to ensure results are not driven by annotation multiplicity.

### Trivial

- **Scale-aware performance differences (Table 5) are reported but not analyzed.** The pattern is interesting — CogVLM-Grounding dominates on small/medium instances while SPHINX-v2-1k dominates on large instances — but the paper does not attempt to connect these to architectural choices (e.g., input resolution, multi-scale processing, feature pyramid design). Brief speculation would enrich the analysis.

## Nice-to-Haves

- A side-by-side comparison showing that two models with similar accuracy on legacy benchmarks (e.g., both ~92% on RefCOCO) show a larger gap on Ref-L4 would directly validate the claim that the new benchmark is needed to differentiate modern models. The current data supports this implicitly, but an explicit juxtaposition would strengthen the argument.
- A quantified quality check on the generated expressions (e.g., what fraction of GPT-4V hallucinations were caught by human reviewers; inter-reviewer agreement on correctness) would strengthen confidence in the benchmark's annotation quality.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Rephrased annotations inflate the claimed scale"** — Removed because the paper transparently reports both "Instances" (18,653) and "Annotations" (45,341) as separate columns in Table 3. The existing benchmarks (RefCOCO: 7,596 instances → 21,586 annotations) have a similar or higher rephrasing ratio. There is no deception.

2. **"Term 'annotation' used inconsistently"** — Removed as factually incorrect. The paper uses "Annotations" consistently throughout to mean total referring-expression–image pairs.

3. **"GPT-4V prompt relegated to the appendix"** — Removed per the rule that appendix sections are stripped by the parser and exist in the original submission.

4. **"No check for image-level overlap with pretraining datasets"** — Removed because the paper explicitly states it does not control for training data (Section 3.3: "without imposing any limitations on the training data sources"). The O365-P2 subset provides a partial novelty signal. Demanding contamination control evaluates the paper against a different class of expectations than what it claims to deliver.

5. **"Benchmark validity threatened by data contamination"** — Removed for the same reason as #4. The paper is not trying to be a contamination-controlled benchmark; it aims to be a *harder and more diverse* benchmark. The O365-P2 analysis (Figure 5) is precisely the kind of novelty-aware analysis t