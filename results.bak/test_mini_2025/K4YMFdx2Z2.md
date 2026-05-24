Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper formalizes Unsolvable Problem Detection (UPD) for Large Multimodal Models (LMMs), defining three distinct problem types: Absent Answer Detection (AAD), Incompatible Answer Set Detection (IASD), and Incompatible Visual Question Detection (IVQD). The authors introduce MM-UPD Bench, a 2,095-question benchmark constructed from MMBench across 18 ability dimensions, and propose Dual accuracy as a unified metric that captures the trade-off between answering correctly when possible and withholding when not. Experiments on 20 LMMs (15 open-source, 5 closed-source) show that performance on standard benchmarks is largely uncorrelated with UPD performance, demonstrating that the benchmark captures a previously unmeasured dimension of LMM trustworthiness. The paper also explores prompting strategies (CoT, self-reflection) and instruction tuning as baselines.

## Strengths

- **Novel problem definition with three well-motivated unsolvable scenarios.** The paper formalizes UPD with three settings (AAD, IASD, IVQD) that go well beyond prior work, which focused almost exclusively on image-question mismatches (Section 3, Figure 1). This provides a more comprehensive evaluation of LMM refusal capabilities and trustworthiness.

- **Dual accuracy metric for unified evaluation.** Dual accuracy (Section 4.2) requires a model to answer correctly on both a standard question and its unsolvable variant, providing a single score that captures the ideal behavior trade-off. This addresses a genuine gap in prior work that lacked such a unified measure.

- **Rigorous benchmark construction with fine-grained ability coverage.** MM-UPD Bench contains 2,095 questions across 18 abilities, built from MMBench through filtering image-agnostic questions, mechanical UPD-variant generation, and manual verification. The use of CircularEval (Section 4.4) and GPT-involved choice extraction ensures robust evaluation. The benchmark enables ability-wise diagnostic analysis (Figure 4) that prior unsolvable-problem benchmarks lack.

- **Comprehensive empirical evaluation demonstrating a new capability dimension.** Table 1 shows dramatic drops for models that perform well on standard benchmarks (e.g., LLaVA-OV-7B drops from 86.0% Orig to 4.5% Base AAD), and the paper reports correlation coefficients as low as −0.35 between MMBench and UPD accuracy (Section 5.2, F1). This provides clear evidence that UPD measures a distinct aspect of model behavior not captured by existing benchmarks.

- **Exploration of solution approaches with honest assessment of limitations.** The paper evaluates CoT prompting, self-reflection, and instruction tuning (Section 6.1, Tables 3-4), documenting both where each approach helps and where it fails (e.g., CoT hurts InternVL2-8B on IVQD). The instruction tuning experiments show improvement but also a cost to standard accuracy, providing realistic baselines for future work.

- **Insightful error analysis distinguishing vision vs. language bottlenecks.** Section 6.2 analyzes GPT-4o's failures by testing whether the model can correctly identify "None of the above" when given the correct answer directly, finding that most errors stem from unstable vision understanding rather than language-side limitations, with one exception (Physical Property Reasoning).

## Weaknesses

### Major

- **Insufficient documentation of manual quality assurance for the benchmark.** The construction relies on manual removal of ambiguous samples (Section 4.1), but the paper reports no inter-annotator agreement, no specific criteria for removal, and no counts of how many samples were removed at each stage. The descriptions are vague: "manually remove some questions with ambiguity" (AAD), "manually removed questions where the shuffled answer set was somehow compatible" (IASD), "manual check to guarantee the incompatibility" (IVQD). For a dataset paper where the central claim is that unsolvable questions are *genuinely* unsolvable (not merely difficult or ambiguous), this opacity is a significant gap. The number of questions per ability is also not reported, making it hard to assess whether fine-grained scores are statistically reliable (especially IVQD with 356 questions over 12 abilities ≈ 30 per ability on average).

- **The correlation claim is overstated relative to the evidence presented.** The paper asserts that performance trends of MMBench and MM-UPD are "completely different" and reports a max correlation of 38.7 (Section 5.2, F1). A correlation of ~0.39 is low but not *trivially* low—it indicates ~15% shared variance. The paper would benefit from presenting the correlation data more transparently (with per-model scatterplots and confidence intervals) and characterizing the relationship more precisely. The core claim that UPD captures a distinct dimension is supported by the dramatic drops in Table 1; the correlation analysis just needs better presentation and more measured language.

### Minor

- **The base-setting results are over-interpreted as a model capability finding rather than a training distribution artifact.** In the Base setting, models receive the standard answer-choosing prompt with no refusal instruction. Finding that open-source models score near 0 (Section 5.2, F2) primarily reflects that they lack refusal training, not a direct measure of UPD capability. The paper partially acknowledges this ("closed-source models... are trained for refusal"), but the presentation of F1 and F2 does not sufficiently emphasize this distinction. The Option and Instruction settings are more informative for assessing actual UPD ability. This concern does not invalidate the benchmark—the three settings together are a strength—but the Base results should be framed with clearer caveats.

- **No human performance baseline.** For a new benchmark claiming to measure a meaningful capability, a human evaluation (even on a 100-sample subset) would calibrate difficulty and confirm that the task is indeed trivial for humans. This is standard practice for dataset papers. Many models scoring near 0 on Base and struggling on Option/Instruction would be more informative with a human anchor showing, e.g., "humans achieve 98% on this benchmark."

- **No discussion of potential contamination.** Since questions are derived from MMBench (a public benchmark), some models may have been trained on these images or similar question formats. The paper should acknowledge this limitation.

- **The qualitative output difference analysis (Section 6.2) is interesting but not quantified.** The observation that closed-source models tend to explain their refusal while open-source models do not could be measured systematically.

### Trivial

- The paper references Table 2 for correlation coefficients but the actual table is only in the appendix (which was removed by the parser). A brief summary of its contents in the main text would be helpful for readers who cannot access the full submission.

## Nice-to-Haves

- A scatterplot of Original Standard vs. Dual accuracy for each setting would make the correlation analysis more interpretable than a single coefficient range.
- Split-half reliability or per-ability confidence intervals would strengthen the benchmark's validity.
- A brief note on instruction tuning dataset size and computational cost in the main text (currently only in appendix).

## Removed Points

- **"Table 2 is not present in the main text"**: The table is in the appendix. The parser strips appendix content from all papers; this is not an author error.
- **Typos/formatting/grammar nitpicks**: These are parser artifacts, not author errors.
- **Missing related works**: Cannot be verified without external sources.
- **Instruction tuning details relegated to appendix**: Standard practice for main papers; the critical information is summarized in Section 6.1.
- **Criticisms that the paper should address problems outside its stated scope** (e.g., extending to open-ended questions): The paper explicitly identifies this as future work.
- **Generic "could be..." speculation without specific evidence**: Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths (novel problem formulation, careful construction, broad evaluation) and identify the same areas for improvement (manual QA documentation, correlation analysis presentation). A potential insight from the critique pattern is that reviewer 3's meta-commentary—that the harsh critic primarily identified documentation gaps rather than fundamental flaws—reinforces the paper's core validity. The most actionable observation from the review process is that the benchmark's value proposition rests on the quality of its manual verification, and the paper would benefit from treating this verification as a first-class methodological contribution rather than a cleanup step.

## Suggestions

1. **Document the manual verification process thoroughly.** Report the number of questions removed at each manual-check step (AAD, IASD, IVQD), the criteria used, and inter-annotator agreement if multiple people were involved. Provide examples of ambiguous questions that were excluded and explain why they were ambiguous. This is the single most impactful change for a dataset paper.

2. **Re-frame the correlation analysis.** Replace "completely different" with more measured language (e.g., "low to modest correlation"), and either include scatterplots or a table of per-model comparisons. Even a brief qualitative discussion (e.g., "models A and B both score >80% on MMBench but differ by 30 points on UPD") would be more informative than just correlation coefficients.

3. **Add a small human baseline evaluation.** Even 100 randomly sampled questions would significantly strengthen the claim that UPD questions are genuinely unsolvable for humans.

4. **Distinguish more clearly between Base and Option/Instruction findings.** The Base results reflect training distribution; the more interesting capability signals come from Option and Instruction settings. A sentence clarifying this at the start of Section 5.2 would improve interpretability.

## Score and Decision

**Round 1 bracket (initial calibration):** After reading anchor papers in three bands, the most relevant anchor was TUBench (avg 5.25, Reject), a benchmark for unanswerable questions in LVLMs. The paper under review is clearly stronger than TUBench: it covers three unsolvable types rather than one, includes multiple evaluation settings (Base/Option/Instruction) with a unified Dual accuracy metric, provides ability-wise fine-grained analysis, and explores solution approaches. The weak-band anchors (scores 2–3) were dissimilar papers on unrelated topics and are not informative for calibration.

**Round 2 narrowing (within bracket):** I read full reviews for MediConfusion (6.25, Accept), MMDT (7.0, Accept), and The Labyrinth of Links (6.75, Accept) as intermediate anchors. The current paper is comparable to or slightly better than MediConfusion (medical VQA benchmark with 352 questions, accepted as poster) and The Labyrinth of Links (MLLM association benchmark, accepted as poster). It is slightly less comprehensive than MMDT (multi-perspective trustworthiness evaluation, accepted as poster) but has a more focused and novel problem formulation. Considering the fixable-but-real documentation gaps, the paper sits at the lower end of this cluster.

**Anchors retrieved (all rounds):**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| gNoqEdT2wO.md | 2.33 | R1 | Unrelated (continual learning benchmark) |
| BVACdtrPsh.md | 3.00 | R1 | Unrelated (text-rich visual scenes benchmark) |
| S9YfP4rsfX.md | 2.50 | R1 | Unrelated (graph reasoning) |
| NlY3XppPt3.md | 2.00 | R1 | Unrelated (programming challenges) |
| UHHOAe1uIS.md (TUBench) | 5.25 | R1, R2 | Directly related — narrower scope, weaker evaluation, rejected |
| qIbbBSzH6n.md (MMDT) | 7.00 | R1, R2 | Related — broader scope, accepted as poster |
| vJ0axKTh7t.md (Labyrinth of Links) | 6.75 | R2 | Related — MLLM benchmark, accepted as poster |
| Rc8z5wLzBF.md (OmniBench) | 5.75 | R1, R2 | Related but different task (tri-modal), rejected |
| H9UnNgdq0g.md (MediConfusion) | 6.25 | R2 | Related — medical benchmark with similar rigor, accepted as poster |
| q6pm9CObJn.md (MTVQA) | 5.00 | R2 | Related but different task (multilingual text VQA) |
| ZuYvrjh2od.md (ReForm-Eval) | 5.00 | R2 | Related but different (re-formulation of benchmarks) |
| RIbH5ekQpr.md (IMP) | 5.20 | R2 | Related but different (image polysemy) |

**Final determination:** Score 6.5, Decision Accept. The paper makes a solid contribution with a well-motivated problem formulation, a carefully constructed benchmark, comprehensive evaluation, and useful analysis. The weaknesses are real but addressable in revision and do not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>