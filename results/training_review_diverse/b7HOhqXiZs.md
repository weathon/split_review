Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes DeMo (Decoupled Momentum Optimization), a distributed optimizer that reduces inter-accelerator communication by using the Discrete Cosine Transform (DCT) to extract and synchronize only the "fast components" of the momentum across accelerators while keeping slower components local. The method is evaluated on OLMo (1B and 300M parameter models) trained on 100B tokens of Dolma v1.5, showing competitive loss and downstream evaluation scores against AdamW while reducing per-GPU communication by orders of magnitude.

## Strengths

- **Orders-of-magnitude communication reduction with plausible retention of model quality.** The per-GPU communication numbers reported in Table 1 demonstrate a dramatic reduction (several orders of magnitude) compared to full-gradient all-reduce, while the training loss curves and downstream evaluation on HellaSwag, ARC-Easy, and PiQA suggest DeMo keeps pace with AdamW. This combination — large compression with non-degraded training — is the paper's central claim and is the most interesting finding.

- **Novel application of DCT for momentum compression in distributed training.** The idea of treating momentum tensors as spatially auto-correlated signals and using a fixed-basis decorrelating transform (DCT) to extract principal components is elegant and avoids the per-step SVD cost of prior low-rank projection methods (Section 3.2.1). The approach is architecture-agnostic and the precomputed transform matrices make per-step overhead plausibly low.

- **Open-source release and reproducibility effort.** The authors release a standalone PyTorch implementation, the minimal patch to OLMo, and configuration files (Section 4, Reproducibility Statement), facilitating independent verification.

- **Network-topology agnosticism.** DeMo supports centralized clock-synchronous training without requiring specialized networking topologies (Abstract, Section 2), which broadens its applicability compared to methods that rely on specific hardware configurations.

## Weaknesses

### Major

- **No wall-clock or throughput measurements, despite practical motivation being central.** The paper's stated motivation is enabling training "on slow internet bandwidths" and "without specialized high-speed interconnects" — yet it reports only communication *volume* (bytes per GPU), never actual training time or throughput under bandwidth-limited conditions. A 128× reduction in bytes does not guarantee a 128× reduction in training time: DCT computation, all-gather overhead, synchronization patterns, and straggler effects all matter. The introduction claims the method was evaluated "under bandwidth constrained scenarios" (Section 1), but Section 4 describes no such simulation — training ran on 64 H100 GPUs (presumably with fast interconnects). Without timing experiments (e.g., measuring step time under simulated bandwidth limits), the practical benefit is unsubstantiated.

- **No experimental comparison to existing communication-efficient methods.** The related work (Section 2) discusses quantization/sparsification, low-rank projection (SVD-based), and federated averaging, but none are run as baselines. A reader cannot tell whether DeMo's performance is attributable to its specific DCT-based extraction or simply to the use of signum with a high momentum decay. Comparisons against PowerSGD, QSGD, or Local SGD at comparable communication budgets are needed to isolate DeMo's contribution.

- **Limited training scale undermines convergence claims.** Models are trained for only 100B tokens (≈3% of the Dolma dataset's 3T tokens). The paper acknowledges compute constraints (Section 4), but the sweeping claim that DeMo "match[es] or surpass[es] the performance of equal models trained with AdamW" is drawn from a single training regime. Convergence at 100B tokens may not reflect behavior up to 3T tokens, and it is well known that early training dynamics can favor different optimizers than long-term behavior.

- **The experimental setup conflates optimizer change with communication reduction.** The baseline is AdamW. DeMo is a signum-based optimizer (no second moment estimate) with DCT compression. There is no ablation isolating whether the retained performance comes from the optimizer change (signum vs. AdamW) or from the compression scheme. A signum-only baseline with full communication, or an AdamW baseline with the same compression, would disentangle these effects. The paper calls DeMo a "drop-in replacement" (Section 5), but changing the optimizer class (AdamW → signum) is not a trivial swap.

- **No profiling of DCT compute or memory overhead.** The paper asserts "negligible compute and memory overhead" (Abstract, Section 3.2.1) with no empirical support. For a 1B-parameter model with chunk size 64, the DCT is applied per step to every parameter tensor. Without wall-clock step times or FLOP counts, this claim is unverified.

### Minor

- **Single training run per configuration.** Results are reported from one run with no error bars or standard deviations (Section 4). Given noise in downstream evaluation scores, a single run cannot convincingly demonstrate equivalence or superiority.

- **No verification of the three core conjectures.** The algorithm's design critically depends on Conjectures 3.1–3.3 (spatial autocorrelation, temporal variance, importance of slow components), but none are independently measured. The paper is upfront that these are not proven ("We will not formally prove any of these conjectures in this work"), but independent evidence (e.g., momentum covariance spectrum, energy compaction measurements) would substantially strengthen confidence in the approach.

- **No hyperparameter guidance for $s$ and $k$.** Results are shown for $s \in \{64, 128\}$ and varying $k$, but no heuristic or sensitivity analysis is provided for choosing these values for different model sizes or architectures.

- **Overclaiming in the abstract.** The abstract claims it "is possible to even improve convergence compared to previous state of the art optimizers," but the paper only compares to AdamW. AdamW is widely used but not the only SOTA optimizer; many recent optimizers (e.g., Lion, Sophia) have shown advantages. The claim should be scoped to AdamW.

### Trivial

None.

## Nice-to-Haves

- A simple analysis showing conditions under which the DCT-extracted update direction is an unbiased or approximately unbiased estimator of the full-gradient update.
- Discussion of straggler mitigation for heterogeneous network speeds, since all-gather latency is proportional to the worst node.
- Sensitivity analysis for chunk size $s$ across more values.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison to Local SGD"** (from harsh critic's "Other Observations"): The paper discusses federated averaging (Local SGD) extensively in Section 2.3. The critic's more general point about missing experimental baselines is already covered above.
- **"The paper does not acknowledge that any sign-based optimizer would have this memory advantage"**: The paper explicitly acknowledges this in Section 3.3 ("Since the second moment is not computed here, this variant of DeMo uses less memory for optimizer states as compared to AdamW"), so the criticism of non-acknowledgment is inaccurate.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's ambitious claims and its thin experimental basis, but do not offer fundamentally new insight about the method itself.

## Suggestions

1. **Add wall-clock timing experiments.** Measure per-step time under simulated bandwidth constraints (e.g., 1 Gbps, 10 Gbps, 100 Gbps per GPU) to translate the byte-count reduction into actual training speedup.
2. **Add baseline comparisons to at least one communication-efficient method** (e.g., PowerSGD or signum with no compression) at a comparable communication budget.
3. **Run multiple seeds** (at least 2–3) for a selected configuration to provide error bars on loss and downstream scores.
4. **Profile the DCT overhead** as a percentage of forward+backward step time, and report peak memory usage for DeMo vs. AdamW.
5. **Scale at least one experiment to 500B–1T tokens**, or argue convincingly why 100B tokens is representative for the convergence claim.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>