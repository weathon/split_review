## Summary

This paper addresses the scarcity of high-quality training data for LLM-based CUDA kernel generation by proposing a data synthesis and curation pipeline. The pipeline generates kernels and reasoning traces using Kevin-32B, then curates them based on the observation that shorter, concise reasoning traces are associated with correct and performant kernels. This produces **ConCuR**, a dataset of 4,892 curated CUDA kernel + CoT pairs, and **KernelCoder**, a LoRA fine-tune of QwQ-32B that achieves state-of-the-art results on KernelBench Levels 1 and 2 (58% Exec pass@1 on Level 1, 59% on Level 2) while requiring only 64 A100 GPU hours of training — an order-of-magnitude reduction in compute over competitors.

---

## Strengths

- **State-of-the-art results on KernelBench.** KernelCoder achieves 58% Exec pass@1 on Level 1 and 59% on Level 2, outperforming DeepSeek-R1-0528 (52%/55%), Kevin* (50%/46%), and all other baselines (Table 1). At pass@10 it reaches 91% (Level 1) and 95% (Level 2) Exec, matching or exceeding every competitor including frontier models (Table 2). These results are the paper's strongest evidence that the curated dataset enables effective SFT.

- **Exceptional training efficiency.** KernelCoder uses only 4,892 samples and 64 A100 GPU hours, compared to >600 H200 GPU hours for Kevin (GRPO) and 640 GPU hours for AutoTriton (SFT+GRPO) (Table 3). This is a genuine practical advantage — the pipeline produces a small, high-quality dataset that dramatically reduces the compute barrier for kernel-generation SFT.

- **Empirical grounding of the curation strategy.** Figure 3 shows that correct kernels have shorter reasoning traces (median ~6K tokens vs ~8K for incorrect), and accuracy decreases monotonically from ~0.65 (shortest bins) to ~0.04 (longest bins). The paper also documents that speedup is essentially independent of reasoning length (r = −0.047, Figure 2). These observations jointly motivate the curation criteria and are a novel finding specific to kernel generation.

- **Ablation studies validate joint curation.** KernelCoder substantially outperforms alternatives using a single criterion: pass@1 Exec on Level 1 is 58% vs. 5K-random (39%), 5K-max (34%), 5K-min (35%), and 5K-speedup (42%) (Table 4). This demonstrates that jointly selecting for conciseness, speedup, and task-type balance is necessary — the gains are not simply from selecting easy tasks.

- **Dataset generalizes across base models.** Fine-tuning Qwen3-8B, Qwen3-32B, and QwQ-32B on ConCuR improves all three (Table 5), e.g., Qwen3-8B Level 2 Exec jumps from 53% to 89%. This shows ConCuR captures transferable knowledge not tied to a single architecture.

---

## Weaknesses

### Fatal

None.

### Major

None that are verifiable from the paper as written.

### Minor

1. **The within-task evidence for the conciseness-correctness relationship is deferred to the appendix.** The paper claims that "for the same task, CUDA kernels generated after shorter reasoning traces tend to be correct more frequently" (Section 3.4) and references Appendix B for the detailed within-task analysis. However, the main-text evidence (Figure 3) pools all generations across tasks, which is compatible with an alternative explanation — that the aggregate trend is driven by easy tasks having both shorter reasoning and higher accuracy. A reader of the main text alone cannot independently verify the per-task claim. The appendix likely addresses this (it exists in the original submission, stripped by the PDF parser), but the main text would benefit from at least one within-task visualization or a concise per-task summary statistic.

2. **No confidence intervals or significance tests on the main results.** Tables 1 and 2 report point estimates without uncertainty. Given that pass@10 is computed over 100 tasks per level, the standard errors are non-negligible (e.g., for pass@1 Exec of 58% on 100 tasks, the 95% CI spans roughly ±10%). Reporting binomial confidence intervals or bootstrap estimates would clarify whether the observed improvements are reliable.

3. **The ARL-based difficulty division thresholds are ad hoc.** Section 6.1 divides tasks into easy/medium/hard using ARL thresholds of 4000 and 8500 tokens, derived from the quantiles of Kevin-32B's generation statistics. While the resulting trend in Table 7 is supportive, the thresholds are not justified beyond observing that they produce monotonic degradation. A continuous analysis (e.g., correlation between task ARL and model performance) or a principled method for choosing thresholds would strengthen this contribution.

4. **Scope is limited to KernelBench Levels 1 and 2.** The paper explicitly acknowledges that Levels 3 and 4 exceed current model capabilities, which is a reasonable justification for exclusion. However, the title claims "State-of-the-Art Kernel Generation" without qualifying this scope. A minor qualification would improve precision.

### Trivial

None.

---

## Nice-to-Haves

- **Full-data baseline:** Training on all 24,136 correct kernels (without curation) and comparing against KernelCoder would provide a direct ablation of the curation benefit. The current ablation compares against random/min/max/speedup selections all at the same size (4,892), which already shows that curation matters. A full-data baseline would further strengthen the claim, but its absence is not a flaw — the paper's claim is that curation is beneficial, not that a smaller dataset is the goal.

- **Generation diversity analysis:** Reporting per-task pairwise reasoning-length differences or kernel edit distances across the five generations would illuminate how much diversity the selection heuristic has to work with, but this is not a required experiment.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Data contamination concern (Harsh Critic's Weakness #1):** The critic claims KernelBench tasks may overlap with KernelBook (the training task source), asserting they are "from the same research group" and that "overlap is plausible." The paper cites these as separate works from different groups (Paliskara & Saroufim, 2025 vs. Ouyang et al., 2025) and provides no evidence of overlap. This is pure speculation unsupported by the paper's content. *Removed per rule: criticisms depending on information not present in the paper.*

- **Missing appendix evidence (Harsh Critic's Weakness #2, partial):** The claim that within-task evidence is "relegated to Appendix B" and "not available in the main text" is a complaint about appendix placement, but the appendix exists in the original submission and was stripped by the PDF parser. *Removed per rule: parser-stripped appendix content.*

- **Comparison is not definitive criticism (Harsh Critic, Section-by-Section):** The critic describes the gap between KernelCoder and Kevin* at pass@10 Exec as "modest" and notes "no confidence intervals or significance tests." The concern about confidence intervals is retained in Minor Weaknesses above; the characterization of the gap as "modest" is retained as context but is not a separate weakness.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Add a within-task visualization (e.g., per-task paired scatter plot or within-task accuracy vs. length trend) to the main text to directly support the "same task" claim that is now deferred to the appendix.
2. Report bootstrap confidence intervals or binomial CIs for the pass@k results in Tables 1 and 2.
3. Provide a continuous analysis (e.g., Spearman correlation between task ARL and model Exec) as an alternative to the binned difficulty division, or justify the threshold choices more rigorously.
4. Qualify the title's scope (e.g., "State-of-the-Art Kernel Generation on KernelBench Levels 1 and 2").

---

## Score and Decision

**Calibration Report:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| rsMajBqYrB | 3.00 | R1-bracket | Much weaker — unrelated topic, poor evaluation |
| 2HN97iDvHz | 3.00 | R1-bracket | Much weaker — weaker contribution and evaluation |
| BltaWJZMeR | 3.20 | R1-bracket | Much weaker — benchmark paper with flaws |
| m2kJuN1bKt | 4.60 | R1-bracket / R2-narrow | Weaker — limited evaluation, narrower contribution |
| iM7MfzbF1B | 5.00 | R1-bracket | Weaker — limited benchmarks, insufficient analysis |
| xzSUdw6s76 | 5.80 | R1-bracket | Comparable or slightly weaker — benchmark paper with solid evaluation |
| NmILZXKcOi | 3.75 | R1-bracket | Weaker — text-to-SQL with limited novelty |
| gjfOL9z5Xr | 6.50 | R1-bracket | Slightly stronger — very clean evaluation framework |
| E4Fk3YuG56 | 8.50 | R1-bracket | Much stronger — top-tier, polished contribution |
| ynguffsGfa | 6.33 | R2-narrow | Comparable — similar structure (dataset curation + SFT) |
| QxbJYBZVbE | 6.00 | R2-narrow | Comparable — dataset+model paper with similar strengths/limitations |
| a4sknPttwV | 5.50 | R2-narrow | Slightly weaker — benchmark only, no trained model |
| w0es2hinsd | 5.25 | R2-narrow | Weaker — less focused contribution |
| suz4utPr9Y | 5.75 | R2-narrow | Slightly weaker — mainly a benchmark contribution |
| 8m7p4k6Zeb | 6.00 | R3-final | Comparable — synthetic data + finetuning with clear results |
| C25SgeXWjE | 6.25 | R3-final | Comparable — dataset generation + evaluation, similar profile |
| M4qNIzQYpd | 6.75 | R3-final | Slightly stronger — more polished evaluation framework |
| 1hQKHHUsMx | 6.75 | R3-final | Slightly stronger — more rigorous analysis |

**Round 1 bracket:** 4.5 – 6.5 (clearly above weak ~3.0 band, clearly below strong ~7.5+ band).

**Round 2 narrowing:** The paper's closest peers are CursorCore (6.00) and ENAMEL (5.75) — both are dataset+model or benchmark papers with clear evaluation and some minor presentation concerns. The paper under review is slightly stronger than these due to its SOTA results and the interesting conciseness observation.

**Round 3:** Anchors at 6.25 (ProverGen), 6.75 (OpenRCA), and 6.75 (pretraining data paper) are somewhat more polished. The paper under review sits just below them, at 6.0.

**Final score: 6.0**. The paper makes a solid, well-supported contribution with clear SOTA results, high efficiency, and an interesting empirical finding. The weaknesses are minor and addressable. The calibration anchors that best match the paper's profile — a solid dataset + model contribution with clear evaluation and some presentation rough edges — are CursorCore (6.00) and the synthetic data needles paper (6.00).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>