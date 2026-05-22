Here is the consolidated final review.

---

## Summary

This paper proposes ATF (Autoformalizer with Tool Feedback), a framework that integrates Lean 4 compiler feedback (syntax check) and a multi-LLM ensemble judge (consistency check) into the autoformalization process. The model iteratively refines generated formal statements based on tool feedback through a three-stage training pipeline (cold-start → expert iteration → DPO). ATF-32B substantially outperforms existing formalizers across three benchmarks (e.g., +29.13% consistency on CombiBench), with results validated by human evaluation and a released dataset of 750K formal statements.

## Strengths

1. **Novel and well-designed tool-integrated formalization pipeline.** The paper introduces a concrete instantiation of tool feedback for autoformalization: a grouped Lean 4 execution method (Section 3.1.1, Figure 3) that makes compiler feedback practical at scale, paired with a multi-LLM ensemble consistency judge (Table 1) that demonstrably reduces false positive rate (FPR from ~9% to 5.79%) compared to single-model judges used in prior work.

2. **Consistent and large-margin improvements over all baselines.** ATF-32B achieves 94.51% vs. 85.41% (FormalMath-Lite), 89.78% vs. 79.70% (ProverBench), and 65.38% vs. 36.25% (CombiBench) on Pass@1 consistency compared to Goedel-V2-Formalizer-32B (Table 3). The 29.13-point gain on the out-of-distribution CombiBench is compelling evidence that tool feedback confers genuine generalization benefit.

3. **Human evaluation validating both the metric and the method.** The paper evaluates 100 instances per benchmark with 3 independent experts, computing a Pearson correlation of 0.746 between tool-based consistency and human judgments (Section 4.2). The human evaluation rows in Table 3 confirm that ATF's advantage is not an artifact of training on the same judge — e.g., ATF-32B scores 49% human-judged consistency on CombiBench vs. 22% for the best baseline, a 27-point gap that mirrors the automated gap.

4. **Rigorous ablation study isolating each component's contribution.** Table 4 decomposes every design choice: removing both tools drops CombiBench consistency from 65.38% to 23.69%, removing only the consistency check drops it to 41.68%, and each training stage (cold-start → expert iteration → DPO) provides cumulative gains. This directly attributes the improvement to the tool-feedback mechanism rather than to training data scale or model capacity.

5. **Analysis of inference-time scaling behavior.** Section 5.1 (Figure 4) shows that ATF's consistency pass rate continues to improve beyond its training limit of 8 revisions, approaching 100% on CombiBench at Pass@32. This demonstrates that the model learns generalizable revision strategies, not just brittle memorization of training trajectories.

6. **Open-source dataset contribution.** The release of Numina-ATF (750K formal statements) addresses a concrete data scarcity bottleneck in ATP research and provides a resource for future work.

## Weaknesses

### Major

1. **The consistency check tool serves as both training signal/labeler and primary evaluation metric, and the calibration of the automated metric against human judgment leaves residual uncertainty.** The ensemble judge that filters training data and provides inference-time feedback is also the CC metric in Table 3. While human evaluation partially addresses this (Pearson r = 0.746), 0.746 is a moderate-to-strong correlation, meaning ~44% of the variance in tool scores is unexplained by human judgment. The paper reports this correlation but does not discuss what kinds of disagreements drive the divergence — e.g., whether ATF's advantage systematically shrinks when measured only on cases where tool and human disagree. The human evaluation subset (100 per benchmark) provides point estimates with wide confidence intervals; extending this to more samples or analyzing disagreement patterns would substantiate the metric more convincingly.

2. **Compute unfairness in the baseline comparison.** ATF's "Pass@1" includes up to 4 rounds of iterative refinement with tool invocations (Lean compiler + two LLM judges per round), while baselines generate a single statement with no tool access. The paper states that "output lengths [are] roughly equivalent" (Section 4.1), but this only addresses decoder output tokens — it does not account for the substantial cost of invoking the Lean compiler and two large LLM judges per revision attempt. The Pass@1 comparison thus conflates the method's architectural advantage with additional inference compute. An experiment controlling for total inference cost (e.g., giving baselines equivalent wall-clock time or token budget) would clarify how much of the gain comes from the tool-feedback design versus simply running more computation per query.

### Minor

3. **The consistency judge's low recall (59.67%) potentially biases training data.** The ensemble-vote method achieves high precision (83.74%) at the cost of rejecting ~40% of truly consistent statements (FNR = 0.4033, Table 1). During training, this means a substantial fraction of valid formalizations are discarded, which could bias the model toward a narrow distribution of patterns that satisfy this particular judge. The paper acknowledges the recall sacrifice (Section 3.1.2, Section 4.2) but does not analyze its effect on training: e.g., how many queries had no surviving trajectory, or whether the model's performance varies by the strictness of the consistency filter.

4. **Cold-start data generation relies entirely on a closed proprietary model (Claude-4-Sonnet).** The method is not fully reproducible from the paper alone, as the initial tool-calling trajectories that bootstrap the pipeline come from a model whose behavior cannot be independently replicated. While the paper releases a downstream dataset and mentions possible substitution with open models, the cold-start phase is a critical dependency that is not itself reproducible.

5. **Human evaluation is limited to 32B-scale models (100 instances per benchmark).** The human evaluation in Table 3 covers only the 32B models (including baselines), not the 8B-distilled variant or lower-scale models. Extending human judgments to additional model sizes would strengthen the claim that the automated metric is reliable across scales, not just at the largest model size where the gap is widest.

### Trivial

None.

## Nice-to-Haves

- A controlled comparison where a baseline (e.g., Goedel-V2-Formalizer) is given access to the same tools at inference time (without retraining) would isolate what the training pipeline contributes beyond the tool access itself.
- A cost-benefit analysis reporting average tool calls per query and estimated token/compute cost relative to baselines would help practitioners evaluate the trade-off.
- An analysis of the consistency judge's false negatives on the evaluation set — e.g., what fraction of statements that humans deem consistent are flagged as inconsistent by the ensemble, and does ATF suffer from this more or less than baselines?

## Removed Points

These points were identified in the inputs but are filtered or demoted based on verification against the paper:

1. *"63% remaining vs ~40% fail is ambiguous/incoherent"* — The figure caption says 37% fail, the text says "~40% fail syntax." These are approximately the same figure; the minor discrepancy (~37% vs ~40%) is within rounding and not a substantive issue. **Removed.**

2. *"Human Evaluation SC/CC columns are confusing — which represent human judgments?"* — The paper states that human evaluators assessed both syntax and consistency (3 experts per instance). Both SC and CC columns in the Human Evaluation rows represent human judgments. The text further clarifies that the Pearson correlation was computed for the consistency check specifically. **Removed** (based on a misreading).

3. *"DPO assumes fewer revisions = better quality but this is unvalidated"* — This is a standard and well-motivated assumption (shorter successful trajectories are more efficient and less likely to contain spurious corrections). The paper also masks tool-invocation tokens to avoid instability. This is a reasonable design choice, not a weakness. **Removed.**

4. *"Missing related works"* — The reviewer cannot know what works exist beyond the paper's cited references. **Removed per hard rule.**

5. *"No appendix/proofs"* — Parser artifact; appendix exists in the original submission. **Removed per hard rule.**

6. Several strengths from the Strength Finder are generic ("addressed an important problem," "well-motivated") and lack specific evidence from the paper. These are removed and the concrete, verifiable strengths are retained above.

## Novel Insights

Beyond the paper's own contributions, the most interesting finding that emerges from combining the harsh critic's analysis with the paper's data is the **tension between using an automated judge for training vs. for evaluation**. The paper's ensemble judge prioritizes precision (83.74%) at the cost of recall (59.67%), which is the correct choice if the judge is used *evaluatively* — you want high confidence when declaring a statement consistent. But when the same judge is used to *filter training data*, low recall means the model is trained on a narrow, high-precision subset that may not reflect the full distribution of valid formalizations. The paper does not disentangle these two roles, and doing so could reveal whether even better performance is achievable with a recall-recovered judge (e.g., single-model consistency check) and a post-hoc precision filter. The inference-time scaling results (Figure 4a) partially mitigate this concern by showing the model can improve beyond its training distribution, but a direct analysis of training data loss from false negatives would be informative.

## Suggestions

1. **Disentangle the judge's dual role.** Report how many training trajectories were discarded due to consistency-check false negatives, and whether the model's performance correlates with the strictness of the filter. A sensitivity analysis varying the ensemble threshold would directly address the recall concern.

2. **Add a compute-controlled comparison.** Give a baseline (e.g., Goedel-V2-Formalizer) access to the Lean syntax checker and the consistency judge at inference time, without retraining, and report its Pass@1 when allowed the same number of revision attempts. This would clarify how much ATF's advantage comes from the training pipeline vs. from tool access alone.

3. **Expand the human evaluation.** Even adding 100-200 more human-evaluated samples across model scales would narrow confidence intervals and strengthen the claim that the automated metric is trustworthy. Reporting per-category disagreement (e.g., what kinds of inconsistencies humans catch that the tool misses, and vice versa) would be valuable for the community.

4. **Report cost statistics.** Include average tool calls per query, total inference tokens consumed (including tool output tokens), and estimated wall-clock time per query for ATF vs. baselines. This would allow readers to assess the practical trade-off.

## Calibration Report

**Round 1 (bracketing):** Three queries on "autoformalization LLM tool feedback theorem proving" with score filters (-1.0, 3.5), (3.5, 7.5), and (7.5, 11.0). Weak anchor examples scored 2.0–3.25 (rejected papers with methodological flaws). Middle-band anchors included Process-Driven Autoformalization (4.75, Reject), Don't Trust: Verify (6.25, Accept), FormalAlign (6.50, Accept), and Rethinking Autoformalization (7.20, Accept). Strong-band anchors (8.00) were more distant topics (premise selection, WizardMath, LEGO-Prover). **Initial bracket: 6.5 – 8.0.**

**Round 2 (narrowing):** Two queries targeting (6.0, 8.0) — autoformalization refinement and LLM tool feedback for code generation. Retrieved anchors included Rethinking Autoformalization (7.20, Accept), FormalAlign (6.50, Accept), Herald (7.00, Accept), LEGO-Prover (7.50, Accept), and Don't Trust: Verify (6.25, Accept). 

**Comparative judgment:** The ATF paper is clearly stronger than Don't Trust: Verify (6.25) — which uses prompting, not training — and FormalAlign (6.50) — which focuses only on evaluation, not generation. It is comparable to Rethinking Autoformalization (7.20) in experimental rigor, but ATF has actual training methodology and a complete system rather than just an evaluation metric. It is slightly below LEGO-Prover (7.50) in terms of novelty of the core idea (growing library) but has cleaner experiments and more thorough validation. The weaknesses above (metric circularity, compute unfairness) are real but do not threaten the core claims, as the human evaluation confirms ATF's advantage on a held-out subset.

**Final score: 7.0** — a solid paper with a clear contribution, well-supported experiments, and addressable weaknesses.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EXaKfdsw04 (StepProof) | 3.25 | R1 | Weaker — rejected, methodological issues |
| JNZ3Om6NPS (LLM limitations) | 2.00 | R1 | Weaker — not comparable topic |
| CscKx97jBi (Code Generation Feedback) | 3.00 | R1 | Weaker — rejected |
| Pjkes5MdKI (COOL) | 2.50 | R1 | Weaker |
| k8KsI84Ds7 (Process-Driven Autoformalization) | 4.75 | R1 | Weaker — rejected, dataset quality concerns |
| hUb2At2DsQ (Rethinking Autoformalization) | 7.20 | R1/R2 | Comparable — accepted; ATF has stronger training pipeline |
| V5tdi14ple (Don't Trust: Verify) | 6.25 | R1/R2 | Weaker — prompting-only, less comprehensive |
| QqdloE1QH2 (Multilingual Autoformalization) | 5.50 | R1 | Weaker |
| B5RrIFMqbe (FormalAlign) | 6.50 | R2 | Weaker — evaluation-only, no generation method |
| Se6MgCtRhz (Herald) | 7.00 | R2 | Comparable — dataset paper |
| 3f5PALef5B (LEGO-Prover) | 7.50 | R2 | Stronger — more novel concept, but more complex |
| xLoxMvO695 (Subgoal-based Demo Learning) | 6.33 | R2 | Comparable — rejected |
| Zk9guOl9NS (Multi-Turn Code Generation) | 7.00 | R2 | Comparable — less directly related |
| KIgaAqEFHW (miniCTX) | 8.00 | R1 | Stronger — but different topic (theorem proving with context) |
| oYjPk8mqAV (Magnushammer) | 8.00 | R1 | Stronger — but different topic (premise selection) |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>