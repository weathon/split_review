Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

---

## Summary

This paper proposes Autoformalizer with Tool Feedback (ATF), a training framework that equips an LLM with two verification tools — a Lean 4 syntax compiler and a multi-LLM ensemble consistency judge — and trains it to iteratively refine formal statements based on tool feedback. The training proceeds through cold-start synthetic trajectory generation, expert iteration, and DPO for efficient revision. ATF achieves substantial improvements over existing autoformalizers across three benchmarks, with particularly striking gains (29 percentage points) on out-of-distribution combinatorial problems, validated by human evaluation.

## Strengths

- **Substantial, consistent outperformance of baselines across all benchmarks.** ATF-32B achieves Pass@1 semantic consistency of 94.51%, 89.78%, and 65.38% on FormalMath-Lite, ProverBench, and CombiBench respectively, surpassing the strongest baseline Goedel-V2-Formalizer-32B by margins of 9.1, 10.1, and 29.1 percentage points (Table 3). The 29pp improvement on out-of-distribution CombiBench is particularly compelling evidence for the method's generalizability.

- **Human evaluation corroborates the automatic metrics.** In a study of 100 instances per benchmark evaluated by 3 experts each, ATF-32B improves CombiBench consistency from 22% (best baseline) to 49% (Table 3). The Pearson correlation of 0.746 between the automatic consistency tool and human judgments provides reasonable validation that the automatic metric tracks human-perceived quality.

- **Rigorous ablation study isolates the contribution of each tool and training phase.** Table 4 demonstrates that removing the consistency tool drops CombiBench from 65.38% to 41.68%, and removing all tools collapses performance to 23.69%. Each training phase (cold start → expert iteration → DPO) yields cumulative improvements, directly validating the staged training design.

- **The multi-LLM ensemble consistency check design is well-motivated.** On a purpose-built benchmark of 800 queries with character-level similarity >0.95 between positive and negative statements, the ensemble vote (QWQ-32B + Qwen3-32B) achieves a low false positive rate of 5.79% while maintaining high true negative rate of 94.21% (Table 1). Prioritizing low FPR over FNR is a defensible design choice for a training signal.

- **Inference-time scaling demonstrates learned revision strategies generalize beyond training constraints.** Although trained with revision attempts <8, ATF's consistency success continues to rise with more attempts (Figure 4a), and parallel sampling achieves 100% consistency on CombiBench at Pass@32 (Figure 4b). This is strong evidence that the model has genuinely learned to revise rather than memorized a fixed budget.

- **Open-sourced dataset of 750K formal statements (Numina-ATF)** provides a substantial resource for the community, synthesized from competition-level NuminaMath-1.5 queries (Section 6).

- **Practical engineering contributions.** The grouped batching for Lean 4 execution (Section 3.1.1, Figure 3) and the pre-check filtering stage address real efficiency bottlenecks in using Lean compilers at scale.

## Weaknesses

### Fatal
None.

### Major

- **High false negative rate of the consistency tool (40.33%) is acknowledged but its impact on training data quality is not analyzed.** The expert iteration phase accepts only trajectories that pass the consistency check. With an FNR of 40.33%, a substantial fraction of genuinely correct formalizations are filtered out during training. The paper acknowledges this in passing ("the strictness of the multi-LLMs-as-judge method results in some sacrifices in recall") but provides no analysis of how this filtering shapes the training distribution — whether it biases the model toward formalization styles easier for the specific LLM judges, or how much truly correct data is lost. The human evaluation partially mitigates this concern by showing ATF still outperforms baselines, but the 16pp drop from tool pass rate (65.38%) to human pass rate (49%) on CombiBench — somewhat larger than the baseline drops — suggests the gap merits investigation. A targeted analysis of what the consistency tool is rejecting would substantially strengthen the paper.

### Minor

- **Expert iteration details are underspecified.** The paper does not report the number of expert iterations, the amount of data collected per round, or the precise filtering criteria applied. The description (Section 3.2) says "in each iteration, we use the current model to generate formalization attempts... and filter out those that violate the tool invocation rules." Without iteration counts and data volumes, the training procedure is not fully reproducible. This does not undermine the core claims — the ablation (Table 4) already demonstrates expert iteration's value — but it limits reproducibility.

- **The "No tools" ablation lacks a description of its training setup.** Table 4 reports results for a "NO TOOLS" configuration, but the paper does not explain how this model was trained (e.g., were the same informal-formal pairs used without tool interactions? Were the trajectories single-pass generations?). Clarifying this would make the ablation more informative for isolating the effect of tool feedback.

- **Human evaluation, while well-executed, would benefit from inter-rater agreement reporting.** The human evaluation uses 3 experts per instance with majority voting on 100 instances per benchmark. This is a reasonable scale, but reporting inter-rater agreement (e.g., Fleiss' kappa) would strengthen the claim of reliability.

### Trivial

- **"ATF-8B-Distilled" is a misleading name.** The model is trained from scratch on the same data as ATF-32B, not produced via knowledge distillation. The name should be corrected (e.g., "ATF-8B") to avoid confusion.

- **The text slightly overstates the trend in Figure 4a.** The paper states that "performance continues to improve gradually as the number of revision attempts increases," but the figure shows a clear plateau after approximately 6 revisions for all benchmarks. The claim should be tempered to match the visual evidence.

- **The declining consistency check success rate by attempt number (Figure 5c) is noted but its implications for training signal quality are not discussed.** The observation that success drops from 69.5% (attempt 1) to 8.8% (attempt 8) is interesting — especially given that the expert iteration phase accepts trajectories with up to 8 attempts — and a brief discussion of how this pattern interacts with training data collection would add insight.

## Nice-to-Haves

- A dedicated analysis of how the consistency tool's false negative rate affects the expert-iteration data distribution, e.g., measuring the true (human-verified) pass rate of trajectories filtered out by the tool. This would clarify the precision-recall trade-off in the training signal.
- A direct ablation holding the base model and training data constant: train Qwen3-32B without tools on exactly the same informal-formal pairs to fully isolate the tool-feedback effect. The current "No tools" ablation approaches this but its setup is unclear.
- Reporting confidence intervals or variance estimates for Pass@k metrics would help assess the statistical significance of the reported improvements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Dependency on proprietary models for data generation (Harsh Critic #3).** The cold-start trajectories use Claude-4-Sonnet and the consistency benchmark uses Gemini-2.5-Pro. Per the hard rules, criticism questioning the availability of cited models is removed. Both models exist and are available. The authors also release the resulting dataset (Numina-ATF, 750K statements), which mitigates any practical reproducibility concern.

- **"The claim that previous formalizers 'lack formal knowledge' could be sharpened" (Harsh Critic Section-by-Section).** This is a phrasing nitpick, not a substantive weakness. The paper's meaning is clear from context.

## Novel Insights

None beyond the paper's own contributions. The review process confirmed that the core idea — integrating both syntactic and semantic verification tools as explicit feedback signals into the autoformalization training loop — is genuinely novel in the way it is executed, combining cold-start tool-use training, expert iteration with tool-filtered data, and DPO for revision efficiency. The paper's finding that revision strategies learned under a fixed budget generalize to longer revision sequences at inference time is a noteworthy empirical observation that the paper already highlights.

## Suggestions

- Report the number of expert iterations and data volumes collected per round. Even if approximate, this significantly aids reproducibility.
- Describe how the "No tools" ablation model was trained — what data format was used, whether the same base queries were used, and how many training examples were included.
- Add a brief analysis of what kinds of formalizations the consistency tool rejects during expert iteration (e.g., a qualitative sample of rejected-but-actually-correct cases), to characterize the bias introduced by the high FNR.
- Rename "ATF-8B-Distilled" to avoid the false implication of knowledge distillation.
- Tone down the claim about Figure 4a: acknowledge the plateau rather than describing it as "continues to improve gradually."

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| Process-Driven Autoformalization in Lean 4 (k8KsI84Ds7) | 4.75 | R1 | ATF is clearly stronger — better benchmarks, human eval, comprehensive ablations |
| FormalAlign (B5RrIFMqbe) | 6.50 | R2 | ATF is broader in scope and has stronger empirical validation |
| Rethinking autoformalization (hUb2At2DsQ) | 7.20 | R1/R2 | Comparable contribution level; ATF has larger scale and more comprehensive evaluation |
| Lean-STaR (SOWZ59UyNc) | 7.50 | R2 | Different task (proving vs. formalizing) but comparable novelty and empirical quality |
| MUSTARD (8xliOUg9EW) | 7.33 | R2 | Different task; ATF is comparable in contribution quality |
| LEGO-Prover (3f5PALef5B) | 7.50 | R2 | Different task; ATF is comparable |

Round 1 bracket: 5.5–8.0. Round 2 narrowed this to the 7.0–7.5 range. ATF is stronger than FormalAlign (6.50), comparable to or slightly above Rethinking autoformalization (7.20), and comparable to Lean-STaR (7.50) when accounting for task differences. The paper has a clean core idea, strong empirical results across three benchmarks with human validation, comprehensive ablations, and a useful open-sourced dataset. The major weakness (high FNR of the consistency tool without analysis of its impact on training data) is real but does not undermine the central contribution, as human evaluation confirms ATF's superiority. The minor weaknesses (underspecified expert iteration, unclear no-tools ablation setup) are addressable.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>