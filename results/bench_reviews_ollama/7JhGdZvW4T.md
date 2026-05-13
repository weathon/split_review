Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes **StopNow**, an LLM serving system with two main contributions: (1) recycling internal LLM layer embeddings as input to a lightweight MLP classifier for iterative output length prediction, combined with Bayesian smoothing to refine predictions token-by-token; and (2) a variant of Shortest Predicted Remaining Processing Time (SPRPT) with limited preemption, which allows preemption early (when KV cache memory is small) but disables it late (when memory overhead is costly). The authors derive a closed-form formula for the mean response time of limited-preemption SPRPT in an M/G/1 model, and integrate their approach into vLLM, demonstrating latency and TTFT improvements over FCFS scheduling.

## Strengths

- **Novel prediction approach using recycled LLM embeddings**: Extracting embeddings from an intermediate LLM layer and feeding them to a lightweight MLP for per-token remaining-length prediction is an elegant, well-motivated idea that avoids the overhead of a separate prediction model. Figure 4 shows that iterative embedding-based refinement achieves substantially lower MAE than BERT prompt-based prediction (2.66× improvement claimed).

- **Principled Bayesian smoothing for iterative refinement**: The transition-matrix-based Bayesian update (Section 4.2) is a thoughtful mechanism for aggregating noisy per-token predictions. The Markov transition matrix encodes the natural prior that remaining length decreases by 1 per step, providing a principled way to reduce variance across iterations.

- **Limited preemption concept directly addresses a real LLM system constraint**: The idea of allowing preemption early (small KV cache) but prohibiting it later (large KV cache) maps directly to the memory-constrained reality of GPU-based LLM serving, and is a practical improvement over standard SRPT. Figure 5 shows that C=0.8 outperforms both C=1 (unlimited preemption) and lower C values.

- **Low prediction overhead**: Table 1 shows MLP inference times under 1μs per sample on CUDA for batch sizes up to 2048, and Section 4.3 notes the MLP contributes only ~0.03% of the LLM's FLOPs, making the approach practical.

## Weaknesses

### Fatal
None.

### Major

- **Mathematical error in the worst future rank formula (Section 3.1)**: Lines 148–156 state that `rank_worst(a) = r - a₀` for `a < a₀`, claiming the rank function is "monotonic." However, the rank function `rank(a) = r - a` is monotonically *decreasing*, so the worst future rank at age `a` should be `sup_{b ≥ a} rank(b) = r - a`, not `r - a₀`. Line 158 further states `r_worst(0) = r`, which contradicts the stated formula (which would give `r - a₀` at `a = 0`). The proof computations (e.g., lines 175–178) correctly use `r - a` and `r`, suggesting the Lemma result may be derived correctly but the stated intermediate formula is wrong. This inconsistency undermines confidence in the theoretical derivation and should be corrected.

- **Limited experimental scope undermines generalization claims**: All experiments use a single dataset (Alpaca), a single small model (LLaMA-3 8B on one A100), and a single workload pattern. The paper claims "1.66× to 2.01× lower mean latency" and "24.07× lower TTFT" broadly, but provides no evidence that these gains generalize to larger models (70B+ where memory pressure is far more severe), different workload distributions, or multi-GPU serving. The paper's own limitations section acknowledges this constraint.

- **No comparison with FastServe**: FastServe (cited in Related Work) directly addresses iteration-level scheduling with preemption for LLMs using MLFQ, and is the most directly competing preemptive scheduling approach. Its absence from the experimental evaluation leaves a significant gap in establishing improvement over the state of the art.

- **Section 3.3 (SPRPT with refined predictions) is incomplete**: The section contains a `\todo` comment ("prove with one refined prediction and then we can make it more general with any number of refined predictions"), complex interval-based notation for `X^old` that lacks a closed-form result, and no Lemma or Theorem analogous to Lemma 1 for the limited-preemption case. Since refined predictions are one of the paper's two main contributions, the absence of a complete theoretical treatment for how refined predictions interact with the scheduling policy is a gap.

- **No ablation isolating prediction accuracy from scheduling policy**: The evaluation combines embedding-based predictions with limited-preemption scheduling, making it impossible to determine how much of the latency improvement comes from better predictions versus the scheduling policy itself. Running the same scheduler with (a) oracle predictions, (b) BERT-only predictions, (c) embedding predictions, and (d) random/uniform predictions would clarify the relative contributions.

### Minor

- **The "24.07× lower TTFT" claim is misleading**: This extreme ratio occurs at low request rates where absolute TTFT values are in single-digit milliseconds, making the difference operationally insignificant. At higher loads where latency truly matters, the improvement is 1.76×..Reporting multiplicative ratios without absolute values inflates the headline result.

- **No memory usage measurements despite memory being the core motivation**: The paper's central argument is that preemption is costly because of KV cache memory overhead, yet no GPU memory consumption metrics, OOM event counts, or KV cache occupancy measurements are reported under varying `C` values or load levels.

- **`C` parameter tuning is narrow**: The choice of `C = 0.8` is justified by a single experiment at request rate 14 on one workload. `C = 0.2` results are mentioned but not shown. The paper acknowledges `C` may be workload- and system-dependent, but provides no guidance for tuning it.

- **Predictor layer selection not validated for generalization**: Layer 11 was selected based on profiling 1,000 prompts on LLaMA-3 8B. No analysis is provided on whether this transfers across datasets, model sizes, or fine-tuning variants.

- **Markovian assumption for refined predictions is stated without validation**: The Bayesian update (Section 4.2) assumes the remaining-length prediction evolves as a Markov chain (the next prediction depends only on the current one). Real prediction refinements may have longer-range dependencies that violate this assumption, and no empirical validation is offered.

### Trivial
None beyond those already removed.

## Nice-to-Haves

- Evaluate on larger models (70B+) and different workload distributions (e.g., ShareGPT) to strengthen generalization claims.
- Add a request scheduling timeline visualization showing individual requests being admitted, preempted, and completed under different policies.
- Report absolute TTFT/latency values alongside ratios to provide more honest context for improvement claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"M/G/1 model does not support system design"**: The paper explicitly acknowledges this disconnect on line 612: "While this model does not capture the complexity of LLM systems (as it has no notion of memory, and is single-server), we think it also provides insight into the potential of limited preemption." The theory serves as motivation and qualitative insight, not direct validation. The paper is transparent about this. Downgraded from major to a point partially addressed by the authors.

- **"Predictor trained on same distribution as evaluation, raising overfitting concerns"**: The paper states (line 638) that evaluation uses "10k unique prompts from the dataset for model serving, distinct from those used to train the length predictor." This is standard train/test separation.

- **"Burst evaluation shows preemption provides no advantage"**: This is not a weakness—it actually demonstrates that the system works correctly. When all requests arrive at once (no future arrivals), SRPT degenerates to SJF with no preemption, which is the expected behavior. The paper honestly reports this.

- **"The '2.66× lower MAE' comparison is against a known-weak baseline (BERT)"**: While BERT is a simpler method, it is the established baseline from prior work (S³). The paper also shows the iterative improvement of its own method from raw embedding predictions to Bayesian-refined predictions (Figure 4).

- **"End-to-end overhead including CPU↔GPU data transfer not measured"**: The paper discusses both GPU-based and CPU-based prediction paths (Section 4.3) and notes the MLP contributes only ~0.03% of FLOPs. While a detailed end-to-end latency breakdown would be nice, the overhead argument is strongly supported.

- **"a₀ = C·x (true size) vs. a₀ = C·r (predicted size) definition inconsistency"**: Section 3.1 uses a₀=C·x (theoretical model with known sizes), while Section 4 uses a₀=C·r (practical system with predicted sizes). These are used in different contexts (theory vs. system) and the distinction is reasonable—though the transition between them could be clearer.

## Novel Insights

The embedding-recycling approach for length prediction is the paper's most compelling contribution—rather than running a separate model, it repurposes computations already happening in the forward pass. The Bayesian smoothing mechanism is a principled way to aggregate noisy per-token predictions, though the Markovian assumption should be validated. The observation that preemption should be limited (not eliminated) in memory-constrained LLM serving is intuitive and well-motivated but the theoretical analysis contains an incorrect intermediate formula. The gap between the M/G/1 theory and the actual batch-parallel LLM system means the theory serves mainly qualitative insight rather than quantitative prediction, which the authors acknowledge.

## Suggestions

- Correct the worst future rank formula in Section 3.1. The correct expression should be `rank_worst(a) = r - a` for `a < a₀` (and the tag at age 0 should be `r`, consistent with `r_worst(0) = r`). Verify that Lemma 1's final expression remains valid under this correction.
- Provide ablation results separating prediction accuracy from scheduling policy effects.
- Add absolute metric values (milliseconds for latency/TTFT) alongside multiplicative ratios in the abstract and results section.
- Add FastServe as a baseline in experiments.
- Report actual KV cache memory usage and OOM event rates to validate the memory-motivated limited preemption design.

## Score and Decision

The paper's core idea—recycling LLM embeddings for prediction—is genuinely novel and practical, and shows clear empirical improvements. However, the theoretical contribution has a demonstrable mathematical error (incorrect worst future rank formula) and the experimental evaluation is too narrow (single dataset, single small model, no key baseline) to support the broad claims made. The incomplete theoretical treatment of SPRPT with refined predictions (Section 3.3, with TODO comments) further weakens the contribution. The "24.07×" headline claim is misleading. These issues collectively make the paper not ready for acceptance in its current form, but the core idea is promising and could be strong with revisions.

Originality: Moderate. Embedding recycling is novel; limited preemption SRPT is incremental.

Importance of research question: High. LLM serving efficiency is an important and timely problem.

Claims well supported: Partially. Empirical gains are demonstrated but on a narrow setup; theory has errors.

Soundness of experiments: Limited scope, missing baselines, no memory measurements.

Clarity: Moderate. Some mathematical presentation is incorrect; TODO comments remain in the paper.

Value to community: Moderate to High. The prediction approach is useful; scheduling contributions are weaker.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>