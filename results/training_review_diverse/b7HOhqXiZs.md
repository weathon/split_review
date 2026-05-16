Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes DeMo (Decoupled Momentum Optimization), a distributed optimizer that reduces inter-accelerator communication by decoupling momentum states across nodes and synchronizing only "fast-moving" components extracted via a Discrete Cosine Transform (DCT). The core idea is that momentum can be decomposed into fast and slow components via DCT-based energy compaction; the fast components are synchronized across accelerators while the slow components are left local. The paper evaluates a signum variant of DeMo on OLMo (300M and 1B parameters) trained on 100B tokens of Dolma v1.5, reporting per-GPU communication reductions of several orders of magnitude while matching or exceeding AdamW's downstream performance.

## Strengths

1. **Massive communication reduction demonstrated in principle.** Table 1 reports per-GPU communication requirements reduced from ~8.8 GB per step (full AdamW sync) to as low as 0.0006 GB (k=16) for a 1B model — a reduction of over four orders of magnitude. This directly supports the paper's central claim that full gradient/momentum synchronization is unnecessary.

2. **Performance parity with AdamW on standard benchmarks.** Across Hellaswag, ARC-Easy, and PiQA, DeMo (signum variant) achieves scores comparable to or better than the AdamW baseline for both the 300M and 1B models after 100B tokens of pretraining, as shown in Figure 1/2 and Table 1. This suggests that the massive communication reduction does not catastrophically degrade model quality.

3. **Novel and well-motivated technical approach.** The use of DCT as an approximation to the KLT for decorrelating and extracting dominant momentum components is a genuinely novel application of signal-processing ideas to distributed optimization. The method is architecture-agnostic (applies to arbitrary tensor shapes via separable DCT) and topology-agnostic, which are practical advantages over methods that require specific network topologies or low-rank projections.

4. **Reproducibility effort.** The paper releases a standalone PyTorch implementation, a patch to the OLMo framework, and configuration files, enabling independent verification and extension.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to any existing communication-efficient baseline.** The paper's central claim is communication reduction, yet the only experimental baseline is AdamW with full gradient synchronization — the *maximum* communication setting. The related work discusses three families of communication-reduction techniques (quantization/sparsification, low-rank projection, Local-SGD/federated averaging), but none are used as experimental comparisons. Without positioning DeMo against existing methods at comparable compression ratios, the reader cannot assess whether the DCT-based approach offers a *better* trade-off between communication cost and convergence quality, or merely a *different* one. This is a structural gap for a paper whose primary contribution is a communication-reduction technique.

2. **Bandwidth-constrained evaluation promised but absent.** The introduction (Section 1) explicitly states: "To evaluate DeMo, we train a standard LLM architecture ... with DeMo under bandwidth constrained scenarios." The experiments, however, are all conducted on 64 H100 GPUs with high-speed interconnects. No bandwidth simulation, no throughput measurement, no wall-clock time comparison is reported. The paper reports per-GPU communication *requirements* (bytes per step) but never demonstrates that these translate to actual training speedup under constrained bandwidth. The central practical motivation of the paper — enabling training on "slow internet bandwidths" — remains entirely hypothetical.

3. **Only the signum variant is experimentally evaluated, not the core momentum-based algorithm.** Algorithm 1 describes DeMo using momentum accumulation with a decay rate β (recommended β=0.999 for LLMs). However, the experiments section states: "We performed experiments on the signum variant of DeMo." The signum variant (Section 3.3) replaces the parameter update with a sign-based step. This is a substantially different algorithm — the signum step is known to behave differently from momentum-based updates (it is invariant to gradient magnitude). The paper's conclusions about DeMo as a general method are drawn from experiments on a specific variant that may not generalize to the main algorithm.

4. **Core design rests on unverified conjectures with no diagnostic support.** The method's rationale depends on three conjectures (Section 3.1) about the spectral properties of momentum: that fast components are spatially auto-correlated with concentrated energy, have low temporal variance, and that slow components are important for long-term convergence. The paper provides no empirical evidence for any of these in the target setting — no DCT spectrum analysis of momentum during training, no demonstration of energy compaction, no ablation showing that the DCT-based extraction actually approximates a KLT as claimed. While the authors are transparent about not proving these conjectures formally, the absence of even basic diagnostic validation makes the algorithm's design rationale appear ad-hoc.

### Minor

1. **No statistical confidence.** All experiments are run once per configuration. For LLM pretraining, which is known to have non-trivial variance from random seed and data ordering, single-run results cannot establish whether the reported "equivalent or better" performance is significant or within noise range. (Acknowledged: multi-seed runs at this scale are expensive, but the paper should at minimum acknowledge this limitation.)

2. **Computational overhead of DCT not quantified.** The paper claims DCT overhead is "negligible" and "almost negligible if implemented correctly" (Sections 3.2.1, 5), but provides no measurements — no FLOP counts, no microseconds per step, no comparison of step times. For a 1B model, applying DCT to every momentum tensor at every step is a non-trivial operation; the claim of negligible overhead should be substantiated.

3. **Duplicate frequency synchronization is underspecified.** The paper states that after all-gather, "we average the amplitude of any duplicate frequencies" (Section 3.2.2). If different accelerators select different frequency indices (which they naturally will, since each runs on local decoupled momentum), the number of overlapping (duplicate) frequencies may be small or zero. The paper does not specify what happens when frequencies are unique to a single accelerator — whether they are discarded, included with their original amplitude, or handled differently. This is a non-trivial algorithmic detail.

4. **No wall-clock or throughput measurement.** The conclusion claims "no noticeable slowdown in convergence," but no step-time or total-training-time comparison between DeMo and AdamW is reported. Convergence measured in tokens processed may be comparable, but without wall-clock data the practical efficiency claim is incomplete.

5. **Hyperparameter sensitivity underexplored.** Only two chunk sizes (s=64 and 128) are tested; the range of k is not fully specified in the parsed text. No systematic study of the communication-quality trade-off as a function of s and k is provided, leaving practitioners without guidance for choosing these hyperparameters.

### Trivial

- Equation (3.3) writes the signum update as `θ_{t+1} = θ_t - η sign(η Q_t)`. Since η > 0, `sign(η Q_t) = sign(Q_t)`, making the inner η redundant. This is either a typo (should be `η sign(Q_t)`) or harmless but confusing notation.

## Nice-to-Haves

- **Comparison to a compression baseline at comparable compression ratio.** Adding top-k gradient sparsification or 1-bit quantization at a similar communication budget would dramatically strengthen the evaluation.
- **Diagnostic experiment validating Conjectures 3.1–3.3.** A short training run with DCT spectrum logging would show whether momentum energy is indeed concentrated in few components.
- **Bandwidth simulation.** Artificially limiting network bandwidth and measuring actual training throughput would directly validate the paper's central motivation.
- **Ablation: DeMo (momentum) vs. DeMo (signum).** Testing Algorithm 1 directly (with momentum) would clarify which components of the method matter.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper should include more seeds"** — weakened from a Major criticism to Minor, as single-run evaluations are standard for 100B-token LLM pretraining runs due to prohibitive compute costs.
2. **Criticism about the DCT being applied to "every parameter tensor at every step" as a weakness** — kept but moved from the reviewer's stronger framing to a Minor point about lack of overhead quantification.
3. **"The paper does not estimate the actual compute cost for a 1B model"** — subsumed by the more general "computational overhead not quantified" point above.
4. **Strength about "minimal overhead" from the Strength Finder** — the paper claims this but doesn't measure it, so the strength is misleading. This specific sub-claim is not supported by evidence.
5. **"The paper does not specify whether the indices are stored as integers or how they are communicated (all-gather on 'the last dimension of the extracted bins' is ambiguous)"** — the paper states "two tensors... one tensor representing the discrete frequency bins as integer indices, the other representing the amplitudes as a floating point number" (Section 3.2.1). The communication mechanism (all-gather on the last dimension) is standard and not ambiguous. This criticism misreads the paper.

## Novel Insights

The reviews collectively surface a structural mismatch between the paper's framing and its evaluation. The paper is framed as a solution to a systems problem (training under constrained bandwidth), but it is evaluated purely as an optimization algorithm (loss curves and downstream benchmarks on fast interconnects). Neither the human nor the automated reviews question the novelty of the core idea — DCT-based momentum decoupling is genuinely creative. The central tension is one of evidence-to-claim calibration: the paper asserts a practically-motivated advantage but only provides an optimization-quality argument. This suggests that the paper's most impactful revision path is not to add more model scales or benchmarks, but to bridge the gap between its algorithmic promise and its systems-level evidence by adding even simple bandwidth simulations and throughput measurements.

## Suggestions

1. **Add at least one communication-efficient baseline.** The most impactful addition would be top-k gradient sparsification or a quantized SGD baseline at a comparable compression ratio, alongside DeMo for the same model/training setup.
2. **Run a bandwidth-constrained simulation.** Artificially cap network bandwidth (e.g., via `tc` or NCCL environment variables) and measure actual training throughput for DeMo vs. AdamW. Even a single configuration demonstrating that DeMo remains compute-bound where AdamW becomes communication-bound would dramatically strengthen the paper.
3. **Provide diagnostic evidence for the conjectures.** Log the DCT spectrum of the momentum during a short training run and show that energy is concentrated in few coefficients. This would turn the conjectures from an act of faith into a supported claim.
4. **Acknowledge and discuss limitations explicitly.** The paper should state that only the signum variant was tested, that no bandwidth-constrained measurements were performed, and that the conjectures remain unverified. The conclusions should be tempered to reflect these gaps.
5. **Report step-time overhead.** Measure and report the DCT computation time per step to substantiate the "negligible overhead" claim.

## Score and Decision

The paper presents a genuinely novel and interesting approach to communication-efficient distributed training. The core idea — using DCT to decompose momentum and synchronize only dominant components — is creative and well-motivated. The preliminary experimental results at 300M and 1B scales are encouraging.

However, the evaluation has structural gaps that prevent the paper from meeting the bar for acceptance at a top-tier venue: (a) no comparison to any other communication-reduction method, despite the paper positioning itself in that space; (b) a promised bandwidth-constrained evaluation that is entirely absent; (c) only the signum variant tested, not the core algorithm; and (d) design conjectures with zero supporting evidence. These are not minor presentation issues — they affect whether the paper's central claims are supported.

With substantial additional work (comparisons to compression baselines, bandwidth simulation, diagnostic validation), the paper could be strong. In its current form, the evidence is insufficient.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>