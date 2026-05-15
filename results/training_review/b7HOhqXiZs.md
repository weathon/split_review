Now I have a thorough understanding of both the paper and the reviews. Let me produce the consolidated review.

---

## Summary

DeMo proposes a decoupled momentum optimization algorithm for distributed training that: (1) removes the all-reduce on gradients, (2) applies a Discrete Cosine Transform (DCT) to the local momentum at each step to extract its most energetic spatial frequencies, (3) synchronizes only those compressed components across accelerators, and (4) keeps the residual ("slow") momentum local. The goal is to reduce per-step communication by orders of magnitude while maintaining convergence quality. Experiments on 300M and 1B decoder-only Transformers trained on 100B tokens of Dolma v1.5 show that a signum variant of DeMo matches (and sometimes slightly beats) a retrained AdamW baseline on loss and three downstream benchmarks, while drastically reducing per-GPU communication.

---

## Strengths

- **Orders-of-magnitude communication reduction.** Table 1 documents per-GPU communication volume for the tested configurations, showing a reduction of several orders of magnitude compared to the AdamW baseline's all-reduce. This is the paper's strongest quantitative result and is clearly relevant to the stated problem of expensive interconnects.

- **Empirical convergence parity under the tested conditions.** The 1B model trained with DeMo (signum variant) achieves a final loss of 2.354 vs. 2.361 for AdamW, and higher HellaSwag accuracy (37.1 vs. 36.7), on the same 100B-token budget. This demonstrates that massive compression does not catastrophically degrade quality in this setting.

- **Novel application of DCT to momentum compression.** Adapting the DCT (a fast, separable, basis-fixed transform) as a computationally efficient approximation of the KLT for decorrelating momentum tensors is a creative engineering choice that avoids the expensive SVD needed by low-rank projection methods.

- **Reproducibility effort.** The paper uses the OLMo framework, retrains the baseline under matched conditions (same 100B tokens, adjusted schedule), and states it will release code and configuration files.

---

## Weaknesses

### Fatal
None.

### Major

- **Conceptual justification is incoherent.** The paper grounds the algorithm in Conjectures 3.1–3.3, which describe "fast moving" and "slow moving" components of the momentum in *temporal* terms (low vs. high temporal variance). The DCT, however, is a *spatial* decorrelating transform applied to a single time step — it identifies high-energy spatial frequencies, not temporally fast-varying modes. The paper never bridges this gap: it does not argue or show that the spatial principal components identified by the DCT correspond to components with low temporal variance. The three conjectures could be true or false independently of the DCT extraction scheme, and the paper provides no evidence connecting them. This makes the core motivation feel ad-hoc. (The algorithm might work for other reasons, e.g., as a structured compression scheme, but the paper's narrative is unsupported.)

- **Experiments test only the signum variant, not the main algorithm described.** Algorithm 1 presents a momentum-based update (gradient descent step with `Q_t`), but Section 4 explicitly states "We performed experiments on the signum variant of DeMo." The signum variant (Section 3.3) replaces the gradient step with `sign(η Q_t)` and does not use the second moment. The paper offers only a one-sentence justification ("to improve convergence") for this substitution and does not report results for the primary algorithm. Readers cannot tell whether the results are attributable to DeMo's core idea or to the switch to signum dynamics.

- **No comparison to any existing communication-efficient method.** The paper surveys quantization, sparsification, low-rank projection, and federated averaging in Section 2, giving qualitative reasons each is limited, but never benchmarks DeMo against any of them at the same compression ratio. Without such comparisons, the stronger claims ("entirely bypasses the need for high-speed interconnects") are unsubstantiated — the relevant question is not whether DeMo matches AdamW, but whether it outperforms *practical alternatives* (e.g., top-k sparsification, low-rank projection via gradient SVD, or QSGD) at the same communication budget.

- **Missing controlled ablations to isolate the optimizer effect from the communication savings.** DeMo changes both the optimizer (decoupled momentum, DCT extraction, signum update) and the communication pattern (partial sync). To attribute the results to communication efficiency rather than different optimization dynamics, two controls are needed: (a) DeMo with *full* synchronization of the extracted components (same volume as baseline) and (b) the baseline using DeMo's update rule with full gradient sync. Without these, the observed performance could reflect a different optimizer trajectory rather than the benefits of compression.

- **Limited architecture scope, training budget, and evaluation.** Only one architecture family (decoder-only Transformer) at two sizes (300M, 1B), on one dataset (Dolma), trained to 100B out of 3T tokens, and evaluated on only three relatively simple benchmarks (HellaSwag, ARC-Easy, PiQA). The paper claims DeMo is "agnostic to the neural network architecture" and suitable for "pre-training large scale foundation models," but the evidence does not yet support this breadth. Moreover, training only 100B tokens leaves open the question of whether long-term convergence (e.g., over 1T+ tokens) matches AdamW.

### Minor

- **No wall-clock, throughput, or memory measurements.** The paper claims "negligible compute and memory overhead" and "no noticeable slowdown in convergence," but provides no timing data, tokens-per-second throughput comparisons, or peak memory profiling. The DCT on all parameter chunks, even with precomputed matrices, is not obviously free for very large models with many tensors.

- **No variance or confidence intervals.** Results are reported as single numbers. While multiple runs at this scale are expensive, the absence of any variance reporting makes it impossible to assess statistical significance of the small observed differences (e.g., 2.354 vs. 2.361 loss).

- **Hyperparameter sensitivity is underexplored.** The paper tests two values of chunk size `s` (64, 128) and a few values of `k`, but does not study the interaction between `s`, `k`, momentum decay `β`, or learning rate, making it hard to judge how robust the method is.

- **Limited description of implementation details.** The description of how 1D tensors are handled, how the separable DCT is applied to different tensor dimensionalities, and how the all-gather on the last dimension works in practice could be clearer.

### Trivial
None.

---

## Nice-to-Haves

- Wall-clock measurements under realistic bandwidth constraints (e.g., simulated 1 Gbps Ethernet vs. InfiniBand) would substantially strengthen the practical claims.
- A visualization of the DCT-extracted components vs. the residual over training steps would help make the method tangible.
- Testing on at least one non-language modality (e.g., vision) would broaden the architecture-agnostic claim.
- An empirical analysis of the temporal autocorrelation of DCT coefficient sets across steps could directly address the conceptual gap.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Figure/table content not included in the text, making evaluation impossible."** — The parser stripped image placeholders; the original submission contains the figures and tables as intended. This is a parser artifact, not an author error.
- **"Does not state whether communication volume is in bytes or messages."** — The paper labels "per-GPU communication requirements" in the context of model parameter sizes (MB), which is clear.
- **"Paper states Figure 2 for downstream scores but caption says Figure 2, creating confusion."** — Both the reference and the caption say "Figure 2" (line 166). No confusion exists.
- **"No appendix content."** — Parser artifact; the original submission contains an appendix.
- **"Orders of magnitude reduction not backed by concrete per-step byte counts."** — Table 1 (present in the original) reports per-GPU communication volume. The numbers exist in the table image.
- **Missing related works.** — Per policy, I cannot confirm the absence of a relevant work without external sources.
- **Formatting/style nitpicks about typos or grammar.** — These reflect parser artifacts, not author errors.

---

## Novel Insights

The harsh critic's most incisive observation is the conceptual mismatch between the temporal language of the conjectures and the spatial nature of the DCT. This is a real flaw in the paper's framing. However, a more charitable reading is that the algorithm does not actually need the temporal narrative: it can be understood as a structured compression scheme that uses DCT-based energy compaction to identify the most informative (highest-energy) spatial modes of the momentum, synchronizes those across nodes, and leaves the residual local. The "fast moving" / "slow moving" terminology is a post-hoc metaphor that the paper does not validate. The reviewer identifies this gap correctly, and the paper would be strengthened by either removing the temporal language or providing empirical evidence (e.g., tracking DCT coefficient overlap across steps) that validates it. Notably, the paper's own empirical results do not depend on this narrative being true — they stand or fall on whether the compression scheme preserves training quality — but the narrative as written is misleading.

---

## Suggestions

1. **Reframe the motivation.** Remove or substantially revise the temporal framing ("fast/slow moving" components) unless empirical evidence connecting DCT spatial coefficients to temporal behavior is provided. Instead, present the method as a structured compression scheme using DCT energy compaction, with the residual kept local as an error-feedback mechanism.
2. **Run experiments on the momentum-based algorithm (Algorithm 1), not just signum, or explain why signum is the primary variant.**
3. **Add controlled ablations:** DeMo with full synchronization and the baseline with DeMo's update rule.
4. **Benchmark against at least one existing method** at the same compression ratio (e.g., top-k sparsification or low-rank projection).
5. **Report wall-clock throughput and memory usage** for the tested configurations.
6. **Expand evaluation** to at least one larger model (e.g., 7B), longer training (500B+ tokens), and a broader set of benchmarks.
7. **Provide confidence intervals** or report results from multiple seeds where feasible.

---

## Score and Decision

The paper identifies a genuinely relevant problem (communication bottlenecks in distributed training) and proposes a creative approach (DCT-based momentum compression). The preliminary empirical results are promising. However, the paper has significant weaknesses: the conceptual motivation is incoherent, the experiments test only a variant of the algorithm (signum) and include no comparisons to existing communication-efficient methods, key ablations are missing, and the evaluation scope is too narrow to support the broad claims. These issues collectively prevent the paper from being accepted in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>