- Decision: Accept
- Avg Score: 7.00
- Scores: 10, 5, 6, 8, 6
I have now verified the paper content against both reviews. Let me produce the final synthesized review.

---

## Summary

This paper presents the results of the inaugural AlgoPerf: Training Algorithms competition, a large-scale empirical study (~4,000 training runs across 8 base workloads and held-out variants) that benchmarks training algorithms under a realistic, time-to-result protocol with fixed hardware and controlled hyperparameter tuning. The key findings are: (1) Distributed Shampoo (non-diagonal preconditioning) achieves ~28% faster training than the NADAMW baseline on wall-clock time, (2) Schedule Free AdamW sets a new bar for hyperparameter-free training with ~8–10% speedups over baselines, and (3) top-scoring submissions are characterized by robustness across workload variations. The paper also documents substantial engineering efforts to ensure fair cross-framework (JAX vs. PyTorch) comparisons.

## Strengths

- **Rigorous wall-clock comparison of Distributed Shampoo vs. Adam across diverse workloads.** The paper shows that Distributed Shampoo achieves ~28% faster average training than the NADAMW baseline across eight base workloads (Section 3.1, Table 7). This is a concrete, multi-workload speedup measured on wall-clock time under a controlled competition protocol, providing stronger evidence than typical per-epoch or single-workload comparisons.

- **First multi-workload demonstration of an effective hyperparameter-free training algorithm.** Schedule Free AdamW is the only self-tuning submission that surpasses the baseline, yielding ~8% faster training than the self-tuning baseline and ~10% faster than the external tuning baseline on seven common workloads (Section 1, Table 1b). This establishes a new benchmark for hyperparameter-free training, as prior work rarely evaluates such algorithms across diverse tasks with full tuning costs accounted for in runtime.

- **Evidence that robustness to workload changes is a key differentiator.** The paper shows that top submissions maintain consistent performance across base and held-out workloads, and that removing held-out workloads does not change the leaderboard order (Section 3.3, Figure 4, Table 4). This supports the claim that consistent multi-workload performance is a major challenge, which is not typically quantified in training algorithm comparisons focused on a single task.

- **Systematic counterfactual analysis of scoring rules.** Section 3.3 examines how rankings would change under alternative rules (removing held-out workloads, using only a qualification set, varying τ_max, removing individual workloads). This level of analysis is rare in competition reports and provides a nuanced understanding of how design choices affect conclusions.

- **Detailed engineering methodology for cross-framework fairness.** Section 4 documents specific measures to ensure functional equivalence between JAX and PyTorch workloads, including handling of framework-specific defaults (GeLU approximation, layer norm epsilon, weight initialization), data pipeline synchronization, LSTM CUDA kernel improvements, and PyTorch 2.0 compilation techniques. This level of detail is critical for reproducing fair comparisons and is rarely provided in benchmarking papers.

- **Use of performance profiles (Dolan–Moré) as the aggregate metric.** Rather than relying solely on average speedup (which the paper correctly notes can be misleading, e.g., the Caspr Adaptive example in Section 3.1), the paper uses performance profiles that capture the fraction of workloads a submission trains within a factor τ of the fastest. This is appropriate for the multi-workload setting.

## Weaknesses

### Fatal
None.

### Major

- **Speed-up estimates lack uncertainty quantification.** The headline claims — Distributed Shampoo achieving ~28% faster training than NADAMW and Schedule Free AdamW achieving ~8% faster than its baseline — are reported as point estimates without confidence intervals, standard errors, or measures of variance across the five studies per workload. The paper itself notes substantial runtime variation (e.g., RESNET, where several submissions reached the target in some studies but not others), so the reader cannot assess whether the reported speed-ups are statistically robust. Given that these are the paper's central quantitative claims, adding bootstrapped confidence intervals or reporting per-workload speed-up spreads (interquartile range or similar) would substantially strengthen the evidence. The paper's own honest discussion of imputation assumptions and the Caspr Adaptive counterexample (Section 3.1) only underscores the need for variance reporting.

### Minor

- **"Hyperparameter-free" framing is imprecise.** The paper describes the self-tuning winner as "completely hyperparameter-free" (abstract) and operating "without any hyperparameters" (Section 1). Schedule Free AdamW, like all optimizers, has fixed default hyperparameters (learning rate, betas, weight decay, etc.) — it requires no *per-workload* tuning, but it is not parameterless. This phrasing invites misinterpretation, especially since the self-tuning ruleset description in Section 2 already makes the correct distinction (submissions "use the same hyperparameters across all workloads"). Replacing "completely hyperparameter-free" with "requiring no per-workload hyperparameter tuning" would be more precise without diminishing the significance of the result.

- **Hyperparameter search spaces for external-tuning submissions are not reported.** The paper discusses that submissions provide "workload-agnostic hyperparameter search spaces" (Section 2) but does not detail the specific ranges or search space designs used by each submission. Reporting these would help readers understand why certain submissions succeeded or failed on particular workloads and would improve reproducibility.

- **RESNET workload analysis could go deeper.** The paper notes that the target-setting hyperparameter search space "may have been more suitable for this workload given its well-studied nature" (Section 3.1) but does not provide a concrete explanation of why the competition search spaces fell short where the target-setting procedure succeeded. A brief qualitative comparison would strengthen the diagnosis.

### Trivial
None.

## Nice-to-Haves

- Report total GPU-hours in addition to the number of runs (~3,850 external tuning + 420 self-tuning) to help other researchers plan similar benchmarking efforts.
- Condense some of the engineering detail in Section 4 (e.g., the four bullet points on PyTorch 2.0 compilation) into a summary table, moving compiler-flag-level specifics to supplementary material. The main lessons are important; the granular detail is more appropriate for an engineering blog post.
- Include a brief table showing the specific search space ranges used for target-setting vs. the competition's submissions for the RESNET workload, to make the analysis more concrete.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Table 2 and Figure 1 are referenced but not visible in the parsed text"* — These are images in the original PDF; the parsed-text extraction is incomplete. This is a parser artifact, not a paper flaw.
- *"The paper could condense the engineering section"* — Moved to Nice-to-Haves; the level of detail is a stylistic choice, not a weakness, and the reviewer acknowledges the content is informative.
- *"Missing discussion of compute costs (GPU-hours)"* — Moved to Nice-to-Haves; reporting total GPU-hours is a reasonable suggestion but not a weakness of the current paper.
- Any formatting, grammar, or typographic nitpicks — These are parser-induced artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard evaluation concerns (uncertainty quantification, framing precision) but do not identify novel angles the paper itself missed.

## Suggestions

1. **Add uncertainty quantification to the central speed-up numbers.** At minimum, report the interquartile range of per-workload speed-ups for the headline ~28% and ~8% claims. Bootstrapped 95% confidence intervals around the median would be stronger still. This single change would address the most substantive weakness.
2. **Tighten "hyperparameter-free" phrasing throughout.** Replace "completely hyperparameter-free" and "without any hyperparameters" with "requiring no per-workload hyperparameter tuning" or "using fixed default hyperparameters across all workloads." This eliminates a source of potential misinterpretation with no cost to the paper's message.
3. **Include a brief table of the search space designs for the top external-tuning submissions.** Even a qualitative summary would help readers interpret the per-workload results.
