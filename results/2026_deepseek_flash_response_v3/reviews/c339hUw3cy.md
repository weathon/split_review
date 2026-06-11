## Summary

This paper introduces ConCuR, a curated dataset of 4,892 CUDA kernels with chain-of-thought reasoning traces, and KernelCoder, a LoRA fine-tuned QwQ-32B model trained on it. The curation pipeline selects kernels based on conciseness of reasoning traces, execution speedup, and task-type balance. KernelCoder achieves 58%/59% Pass@1 Exec on KernelBench Levels 1 and 2, surpassing prior models including Kevin (50%/46%) and DeepSeek-R1-0528 (52%/55%), while using only 64 A100 GPU hours for training — over an order of magnitude less compute than existing approaches.

## Strengths

- **State-of-the-art Pass@1 Exec results with dramatic compute savings.** KernelCoder achieves best Exec on both Level 1 (58%) and Level 2 (59%) of KernelBench, outperforming all baselines including Kevin (50%/46%) and DeepSeek-R1-0528 (52%/55%). Training requires only 4,892 samples and 64 A100 GPU hours — Kevin alone consumes >600 H200 GPU hours. This is a concrete, measurable advantage (Table 1, Table 3).

- **Controlled ablation isolating the effect of each curation criterion.** Table 4 compares four counterfactual datasets (random, max-length, min-length, max-speedup) against KernelCoder's combined method. Every single-criterion variant scores worse on Level 1 Exec (34–42%) vs. KernelCoder (58%). This clean comparison demonstrates that the specific combination of conciseness, speedup, and task-type balance drives improvement, not just having more data.

- **Dataset utility generalizes across multiple base models.** Fine-tuning Qwen3-8B, Qwen3-32B, and QwQ-32B on ConCuR improves all three (Table 5), showing the dataset's value is not architecture-specific. E.g., Qwen3-8B rises from 31→47 (L1 Exec) and 53→89 (L2 Exec).

- **ARL-based task difficulty division shows cross-model validity.** Table 7 shows consistent monotonic performance degradation across Easy→Medium→Hard for all five tested models, giving convergent evidence that average reasoning length correlates with task difficulty.

## Weaknesses

### Fatal

None.

### Major

1. **The central within-task claim is not supported by the evidence in the main text.** Section 3.4 states that "for the same task, CUDA kernels generated after shorter reasoning traces tend to be correct more frequently than those produced through longer reasoning traces." However, the evidence presented (Figure 3) is entirely aggregated across tasks — a boxplot of reasoning lengths pooled across all generation pairs, and accuracy binned by reasoning length without controlling for task identity. The observed negative correlation could be driven entirely by a between-task confound: easy tasks are solved quickly *and* accurately, while hard tasks require long reasoning *and* are error-prone. The paper acknowledges this possibility in passing ("although more challenging tasks typically require a greater number of reasoning tokens") but does not provide within-task stratified analysis in the main text. This matters because the entire narrative framing ("conciseness → high quality") rests on this within-task claim. The curation pipeline's empirical results may hold independently, but the paper overinterprets the aggregate correlation.

2. **The relationship between KernelBook (training data source) and KernelBench (evaluation benchmark) is never stated.** The paper trains on tasks from KernelBook (line 71) and evaluates on KernelBench (line 146). These are cited as different references, but the overlap (if any) between them is not clarified. If KernelBench tasks or near variants appear in the training data, the evaluation is contaminated. This is a basic methodological requirement for any paper that constructs a training dataset and evaluates on a benchmark.

### Minor

3. **Figure 2 uses a truncated x-axis that is visually misleading.** The scatter plot of speedup vs. reasoning length shows an x-axis of 0–1600 tokens, while Figure 3(a) shows the median reasoning length for correct kernels is ~6000 tokens (IQR ~4000–8000). The plot thus displays only the left tail of the distribution without acknowledging this truncation. The reported correlation (r = -0.047) may be computed on the full data, but the visualization creates a misleading impression that all data points have short reasoning.

4. **No variance or confidence intervals reported.** Point estimates are given for all metrics without standard errors, confidence intervals, or significance tests. While single-run evaluation is standard practice in this benchmark setting, some margins are thin (e.g., Level 2 fast₁ Pass@1: KernelCoder 39% vs. DeepSeek-R1-0528 38%), making it unclear whether differences are statistically reliable.

5. **The part (c) curation (544 single-operator samples) is not justified.** The paper states that single-operator and multi-operator tasks "represent two distinct design paradigms" and that "we need to balance the ratio," but provides no rationale for the specific choice of 544 samples and no ablation exploring sensitivity to this ratio.

6. **The efficiency comparison in Table 3 conflates multiple dimensions.** The comparison contrasts SFT on curated data (KernelCoder, 64 A100 hours) with GRPO on KernelBench problems (Kevin, >600 H200 hours). These differ in training paradigm, number of problems, number of generations per problem, and hardware. The comparison is suggestive but not directly apples-to-apples.

7. **The ARL-based difficulty division is somewhat circular.** Tasks are divided by the average reasoning length of Kevin-32B, and then models (including Kevin-32B) are evaluated on those same divisions. Validation against an independent measure of difficulty would strengthen this contribution.

### Trivial

None.

## Nice-to-Haves

- **Within-task analysis in the main text.** A per-task paired comparison (e.g., for each task, is the shortest-reasoning generation more likely to be correct than the longest?) would directly support the central claim. If the within-task relationship is weaker than the aggregate trend, the narrative should be recalibrated.
- **Explicit statement of the KernelBook/KernelBench relationship.** A simple sentence or table clarifying overlap (or confirming disjointness) would resolve the contamination concern.
- **Extended x-axis or inset in Figure 2** showing the full distribution of reasoning lengths alongside the current zoomed view.
- **Small ablation on the single-operator sample ratio** (part (c) curation) to justify the specific number.

## Removed Points

- **Criticism about the GPU-hours comparison being "not directly informative" as an overall weakness** — retained as Minor (#6 above) since the asymmetry favors the author's method, making it a valid concern to note.
- **The harsh critic's point about Appendix B being stripped** — the weakness about insufficient evidence in the main text is kept (Major #1); the appendix reference is noted but not penalized since it was stripped by the parser.
- **Strength Finder's "evidence-based contradiction of conventional wisdom"** — kept as a strength but with the caveat that the within-task nuance is unresolved.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add within-task analysis (per-task paired comparison of reasoning length vs. correctness) to the main text or explicitly recalibrate the claim to match the aggregate evidence.
2. Add a sentence or table clarifying whether KernelBook and KernelBench overlap, and if so, quantify the overlap and show results on the non-overlapping subset.
3. Fix Figure 2 to show the full range of reasoning lengths, or add an inset with the full distribution.

## Score and Decision

**Round 1 bracket (wide search):** Papers scoring <2.5 are fundamentally flawed or trivial. Papers scoring 2.5–4.5 have limited contributions or significant flaws. Papers scoring 4.5–6.1 have meaningful contributions with some issues. Papers scoring 6.0–7.5 have solid contributions with manageable weaknesses. Papers scoring >7.5 are exceptionally strong. The current paper clearly falls in the 4.5–7.5 range — it has a strong empirical contribution and a clean ablation but contains verifiable narrative and methodological gaps.

**Round 2 narrowing (within 4.5–7.5):** Compared to accepted anchors:
- *CraftRTL* (7.00, accepted): Similar domain (HDL code generation via data curation). CraftRTL had comparable issues (hand-crafted data generation) but no data contamination concern. Our paper has stronger empirical improvements (8–13% absolute Exec vs. 3.8–10.9% pass@1) and a cleaner ablation. **Current paper is slightly weaker** due to the unaddressed data contamination concern and the unsupported within-task claim.
- *LLM-Assisted Code Cleaning* (7.00, accepted): Modest improvements (1.2x–1.3x) on standard code benchmarks with a cleaner narrative. **Current paper is slightly weaker** due to the narrative-evidence gap.
- *Improving Data Efficiency via Curating LLM-Driven Rating Systems* (5.75, accepted): Cleaner theoretical framing but smaller empirical improvements. **Current paper is stronger** due to the magnitude and clarity of the empirical results.

The paper sits between these anchors. The two major issues are verifiable and non-speculative, and would need to be addressed for the paper to reach the 7.0 level. But the core empirical contribution (SoTA results with an order-of-magnitude compute reduction, validated by systematic ablations) is genuine and practically significant.

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| NlY3XppPt3.md | 2.00 | 1 | Much weaker — vague contribution, no concrete results |
| OdoS6cH8MP.md | 2.00 | 1 | Much weaker — limited empirical validation |
| dsALpkd1OU.md | 1.67 | 1 | Much weaker — unclear methodology |
| cLTM1gc6Qm.md | 2.25 | 1 | Much weaker — early-stage platform paper |
| TkXisc47la.md | 3.50 | 1 | Weaker — dataset without strong model results |
| QBlegfNZNE.md | 3.50 | 1 | Weaker — theoretical claim without empirical validation |
| RrWAtQNGAg.md | 4.00 | 1 | Weaker — repository-level dataset without downstream performance |
| SXB9LnJ0SK.md | 3.50 | 1 | Weaker — limited evaluation scope |
| rZmQ2z7MPA.md | 5.33 | 1 | Weaker — dataset with smaller absolute improvements |
| GcJE0HPy4X.md | 6.00 | 1 | Similar — dataset curation pipeline, but less focused evaluation |
| m2kJuN1bKt.md | 4.60 | 1 | Weaker — method for kernel selection without LLM generation |
| QxbJYBZVbE.md | 6.00 | 1 | Similar — programming assistant with data pipeline |
| ynguffsGfa.md | 6.33 | 1 | Similar — LLM + data curation, different domain (tabular) |
| maRYffiUpI.md | 7.00 | 1 | Stronger — cleaner narrative, well-motivated pipeline |
| 8KQzoD5XAr.md | 7.00 | 1 | Stronger — HDL + synthetic data, cleaner narrative |
| ix7rLVHXyY.md | 7.25 | 1 | Stronger — comprehensive evaluation, cleaner claims |
| m2nmp8P5in.md | 8.00 | 1 | Much stronger — novel paradigm, thorough evaluation |
| OI3RoHoWAN.md | 8.00 | 1 | Much stronger — broader impact, cleaner execution |
| XmProj9cPs.md | 8.00 | 1 | Much stronger — large-scale benchmark, thorough |
| GGlpykXDCa.md | 8.00 | 1 | Much stronger — comprehensive evaluation |
| DKkQtRMowq.md | 5.75 | 2 | Weaker — smaller empirical improvements, cleaner theory |
| Fq8tKtjACC.md | 6.00 | 2 | Similar — strong results, narrative concerns |
| UNxCphTxWp.md | 6.00 | 2 | Similar — data quality via programs |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>