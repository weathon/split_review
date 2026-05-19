Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final consolidated review.

## Summary

The paper proposes a scheduling framework for LLM inference that (1) recycles the LLM's own internal embeddings at each token generation step to make lightweight, iteratively-refined predictions of remaining output length (via a 2.1M-parameter MLP probe), and (2) uses these predictions in a limited-preemption variant of SRPT that disables preemption after a fraction C of a request's predicted length, to avoid excessive KV-cache memory consumption from preempted-but-unfinished requests. The paper also derives a closed-form expression for mean response time under this limited-preemption policy in an M/G/1 queue.

## Strengths

1. **Novel embedding-recycling prediction with 2.66× lower MAE than BERT baselines.** The probing approach that extracts hidden states from intermediate LLM layers (layer 11 for Llama3-8B) and trains a lightweight MLP classifier is well-motivated and clearly described. The Bayesian smoothing over iterations is a sensible refinement. The 2.66× reduction in mean absolute error over BERT-only prompt-based prediction (Figure 3) is substantiated by both layer-wise profiling (Figure 2) and heatmap comparisons (Figure 5).

2. **Consistent latency and TTFT improvements across request rates.** The end-to-end comparison of four system configurations (vLLM-FCFS, vLLM-SJF_BERT, \alg{}-BERT, \alg{}) on the Alpaca dataset shows that \alg{} achieves 1.66×–2.01× lower mean latency and 1.76×–24.07× lower mean TTFT versus vLLM-FCFS (Figure 7). The latency gains persist across a range of request rates and hold for both mean and median metrics, and the burst experiment (Figure 8) shows that gains also arise from better (SJF-style) ordering, not just preemption.

3. **Theoretical closed-form for limited-preemption SPRPT.** Lemma 1 provides a nontrivial extension of the SOAP framework to a limited-preemption variant, yielding a closed-form expression for mean response time in an M/G/1 queue with predicted job sizes. While the paper is transparent that this model does not capture LLM-specific memory dynamics, it is a valid formal contribution in its own right.

4. **Measured prediction overhead is low.** Table 1 reports that the MLP forward pass takes ~0.5 μs per sample on GPU, and the paper correctly notes that the 2.1M-parameter predictor is 0.03% of Llama3-8B's parameter count. Two design options (compute on GPU inline vs. async CPU) are discussed.

5. **Ablation design exists and is informative.** The four-way comparison (vLLM-FCFS → vLLM-SJF_BERT → \alg{}-BERT → \alg{}) allows readers to separately observe: (i) the limited benefit of SJF ordering alone without preemption, (ii) the large benefit of adding limited preemption (vLLM-SJF_BERT vs. \alg{}-BERT), and (iii) the additional benefit of better predictions (\alg{}-BERT vs. \alg{}).

## Weaknesses

### Fatal
None.

### Major

1. **Missing direct memory measurements that would validate the core motivation.** The paper's entire motivation for limited preemption is to manage KV-cache memory pressure from preempted requests. Yet the evaluation never measures memory consumption, preemption frequency, swap/recomputation events, or OOM occurrences. The claim that C=0.8 beats C=1 because of "memory overhead" (line 680) is asserted based on latency differences alone — a reasonable inference but not directly shown. Given that the burst experiment (Figure 8) shows \alg{} with C=0.8 and C=1 perform nearly identically (since no new arrivals trigger preemption), it is possible that the latency gap between C=0.8 and C=1 in the steady-state experiment is driven by other factors (e.g., overhead of managing preempted requests rather than memory pressure specifically). Measuring memory utilization, recomputation counts, or swap events would directly substantiate the paper's central design claim.

2. **Evaluation limited to one model and one workload.** All experiments use Llama3-8B and the Alpaca dataset only. The limitations section (line 866) acknowledges this but does not discuss how the optimal choice of C or the prediction accuracy might vary with model size, architecture, or workload characteristics (e.g., ShareGPT with heavier tail latencies). Single-model, single-dataset evaluation weakens the generality of the claimed improvements.

### Minor

1. **No statistical reporting for serving experiments.** Mean and median latency/TTFT are reported as single points per request rate without error bars, confidence intervals, or multiple trials (Figure 7). Given the well-known variability in LLM serving (due to batching dynamics, kernel timing, and memory state), single-run results leave it unclear whether observed differences between configurations are stable or noise-dominated.

2. **Comparison with FastServe-style scheduling is absent.** FastServe (cited in related work) is a preemption-based scheduler (MLFQ) that does not require length prediction. A head-to-head comparison — or at minimum a description of why it is not directly comparable — would help readers evaluate the claim that \alg{} improves over state-of-the-art systems. The current evaluation compares only vLLM variants.

3. **Prediction overhead measured only for the MLP forward pass, not the full pipeline.** Table 1 reports MLP inference time (0.5 μs on GPU), but does not account for the cost of extracting the embedding from layer 11 during the forward pass, transferring it (if computed on CPU), or the scheduling decision itself. While these are likely small, the paper claims "negligible overhead" (line 584) based on parameter-count arithmetic and MLP-only timing, not end-to-end profiling of the serving loop.

4. **The theoretical M/G/1 analysis remains disconnected from the system evaluation.** The paper acknowledges this limitation ("While this model does not capture the complexity of LLM systems," line 612), but the simulation figures (1–6) lack descriptions of their parameters, and no attempt is made to validate whether the theory qualitatively or quantitatively predicts the observed system behavior. The theory does not guide the choice of C or explain the magnitude of improvements seen in the real system.

5. **The 24.07× TTFT figure in the abstract is uncontextualized.** The paper reports a range ("1.76× to 24.07×") without stating which request rate produces the extreme value. At very low load, absolute TTFT is small, making the ratio large and potentially misleading as a headline number. The main evaluation figures (Figure 7) should clarify this.

### Trivial
None.

## Nice-to-Haves

- A version of \alg{} with embedding predictions but preemption disabled (C=0 or equivalently no preemption) would complete the 2×2 ablation design and cleanly separate the benefit of prediction refinement from the benefit of the scheduling policy change.
- Investigating prediction sensitivity (e.g., by degrading prediction quality with noise) would strengthen the claim that refined predictions drive the \alg{}-BERT to \alg{} improvement.
- The transition matrix used in Bayesian smoothing assumes uniform bin sizes and neighboring-bin transitions only — this choice seems ad-hoc and could be better justified or compared with alternatives.

## Removed Points

- **"Burst experiment is misleadingly framed as supporting preemption"** — REMOVED. The paper explicitly states (line 740): "since no new requests arrive during processing, preemption has no advantage, leading to similar performance between \alg{} with c = 0.8 and c = 1." The paper correctly treats the burst experiment as demonstrating the ordering benefit, not the preemption benefit. The critic misread this section.

- **"No ablation exists"** — REMOVED in its strong form. The paper does have an ablation design across its four baselines that isolates the effect of preemption (vLLM-SJF_BERT vs. \alg{}-BERT) and the effect of prediction refinement (\alg{}-BERT vs. \alg{}). A cell with embedding predictions + no preemption is missing (moved to Nice-to-Haves), but the claim of "no ablation" is factually incorrect.

- **"Theory uses r (initial prediction), not refined prediction"** — REMOVED. The definition at line 610 says "given the initial prediction r for a job (which we treat as a number corresponding to the middle of its predicted bin)" — this is consistent with the limited-preemption theory which uses the initial prediction to set a_0 = C·r. The theory in Section 3.1 is clearly scoped to a single initial prediction + refinement via the g(x,y) density, and the limited-preemption Lemma uses this framework consistently.

## Novel Insights

None beyond the paper's own contributions. The two reviewers broadly agree on the paper's strengths (embedding-recycling prediction, latency improvements, low overhead) and on its main gap (lack of direct memory measurements). No novel synthesis emerges from the interplay of the reviews beyond what the paper itself states.

## Suggestions

1. Add direct measurements of memory usage, preemption frequency, and recomputation/swap counts across different C values to validate the causal chain: limited preemption → lower memory pressure → lower latency.
2. Evaluate on at least one additional model (e.g., a 7B or 13B model from a different family) and one additional workload (ShareGPT or LMSys-Chat) to support generality claims.
3. Report serving results with error bars (multiple independent runs) to establish statistical significance.
4. Consider adding a FastServe-style MLFQ baseline or explain why it is not directly comparable under the same infrastructure.
5. Profile the end-to-end overhead of embedding extraction + prediction + scheduling decision in the serving loop, not just the MLP forward pass.
6. Clarify which request rate(s) produce the extreme values of the 1.76×–24.07× TTFT range.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>