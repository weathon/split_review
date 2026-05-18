I now have a comprehensive understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces DeMo (Decoupled Momentum Optimization), a distributed optimizer that reduces inter-accelerator communication by decoupling momentum across GPUs and synchronizing only the "fast moving components" extracted via a Discrete Cosine Transform (DCT) applied to chunked momentum tensors. The slow-moving residual momentum is left unsynchronized. The method is evaluated by training 1B and 300M parameter decoder-only transformers for 100B tokens on Dolma v1.5, showing comparable training loss and downstream scores (HellaSwag, ARC-Easy, PiQA) to a re-trained AdamW baseline while reporting per-GPU communication as low as ~0.002 GiB per step.

## Strengths

1. **Novel approach combining momentum decoupling with DCT-based compression.** The idea of keeping momentum decoupled across accelerators and using a signal-processing-style frequency decomposition (DCT) to extract synchronizable components is genuinely novel and well-motivated. The paper correctly identifies that the DCT is a computationally efficient approximation of the KLT (with fixed basis, separable computation, and pre-computable transition matrices), making it practical for billion-parameter models (§3.2.1).

2. **Meaningful theoretical communication reduction.** Table 1 reports per-GPU communication of ~0.002 GiB per step for a 1B model — several orders of magnitude below the ~4 GiB that full-gradient synchronization would require. This reduction is derived transparently from the hyperparameters *k* (top frequencies) and chunk size *s*, and the calculation is easy to verify.

3. **Competitive empirical results on a standard setup.** On all three evaluated benchmarks (HellaSwag, ARC-Easy, PiQA) and on training loss, DeMo matches or slightly exceeds the AdamW baseline (e.g., HellaSwag 46.68% vs. 46.32%, training loss 3.091 vs. 3.097 for the 1B model with *k*=20, *s*=64). The training loss curves (Figure 1/2, though only the caption is extractable) show convergence parity across multiple hyperparameter configurations.

4. **Memory efficiency and reproducibility commitment.** The signum variant avoids storing a second moment, using less optimizer memory than AdamW (§3.3). The paper releases a standalone PyTorch implementation, a minimal OLMo patch, and configuration files (§6).

## Weaknesses

### Fatal
None.

### Major

1. **Core assumption about DCT applicability to momentum is unvalidated.** The entire method rests on Conjecture 3.1 — that momentum tensors exhibit spatial auto-correlation making DCT a good proxy for the KLT — but the paper provides no direct evidence for this. The authors state "we will not formally prove any of these conjectures in this work" and only assert that "empirically, we found that using the DCT alone is enough" (§3.2.1). However, no analysis of the actual frequency/energy distribution of real training momentum is presented, no comparison to an alternative transform (e.g., a random orthogonal projection, which would serve as a null hypothesis) is given, and no ablation checks whether the DCT extraction isolates behavior that is meaningfully different from stochastic compression. Without validating this assumption, it is unclear whether the DCT machinery is adding value or whether simpler compression (random projection, basic sparsification, or temporal downsampling) would achieve equivalent results.

2. **No evaluation under bandwidth-constrained conditions.** The paper's headline claim is that DeMo "bypasses the need for high-speed interconnects" and "potentially enable[s] future training ... on slow internet bandwidths" (abstract, §1), and the introduction states the authors evaluate DeMo "under bandwidth constrained scenarios" (line 16). Yet the experiments are performed on 64 H100 GPUs with standard (fast) interconnects, and no wall-clock timing, throughput measurement under throttled bandwidth, or latency breakdown is reported. The "per-GPU communication" numbers in Table 1 are theoretical tensor sizes — they demonstrate *potential* for savings but do not show that these savings translate into practical benefits under realistic bandwidth constraints. This is the central empirical gap relative to the paper's own claims.

3. **Insufficient baselines.** DeMo is compared only to AdamW. The paper does not compare against standard communication-efficient alternatives such as gradient quantization (1-bit SGD), Top-*k* gradient sparsification, or Local-SGD with tuned synchronization intervals. Without these comparisons, it is impossible to assess whether DeMo's particular form of compression (DCT on momentum) is *better* than existing approaches at the same communication budget. The paper discusses these methods in §2.1–§2.3 but does not include them as experimental baselines.

4. **Limited evaluation scope.** Experiments train for 100B tokens (vs. the full 3T tokens typical for OLMo-1B), evaluate on only 3 downstream tasks (HellaSwag, ARC-Easy, PiQA), and report results from a single seed with no error bars. The paper acknowledges the compute constraint, but the limited scale makes it difficult to assess whether the method would maintain convergence parity over full pre-training or on a broader set of benchmarks (e.g., MMLU, GSM8K, LAMBADA). The 300M model experiment helps but does not fully address scale concerns.

### Minor

1. **Learning rate schedule for DeMo not specified.** The paper states that for DeMo, the "learning rate schedule [was] adjusted accordingly" (line 153), but does not report what the adjusted schedule was. This makes it impossible to distinguish whether DeMo's competitive results come from the algorithm or from hyperparameter tuning.

2. **No ablation of the signum variant vs. standard DeMo.** All experiments use the signum variant (§3.3), but there is no comparison to DeMo without signum (real-valued updates). The relationship between the DCT-based component extraction and the sign operation is not investigated.

3. **No analysis of decoupled slow components.** A central design choice is to leave "slow moving" momentum components unsynchronized across accelerators (§3.2.2). The paper does not analyze whether these components drift over time or how this drift affects convergence. At minimum, training loss divergence over longer horizons would help establish that the decoupling is safe.

4. **Architecture-generality claim untested.** The paper states DeMo is "agnostic to network topology and neural network architecture" (abstract) but evaluates only on decoder-only Transformers. Testing on at least one non-transformer architecture (e.g., ResNet on ImageNet) would substantially strengthen this claim.

### Trivial
- Table 1 would benefit from including the baseline AdamW per-GPU communication cost explicitly, so the reader can directly read off the reduction factor rather than computing it.
- Algorithm 1 uses the function `ExtractFastComponents` without fully specifying the DCT scattering/averaging logic in the pseudocode; the prose in §3.2.1–3.2.2 provides the details, but unifying them would improve clarity.

## Nice-to-Haves
- An empirical validation of the DCT assumption: compute the DCT of real momentum tensors from an AdamW training run, plot the frequency-energy distribution, and compare to a PCA/KLT decomposition to show that the energy compaction is indeed meaningful.
- A wall-clock throughput comparison under simulated bandwidth constraints (e.g., 1 Gbps, 10 Gbps).
- A comparison to at least one simple alternative: e.g., synchronize full momentum every *T* steps (Local-SGD variant) at the same communication budget as DeMo.

## Removed Points
- **"DCT assumption likely invalid for non-spatial data / no local ordering in parameter space"** — The paper explicitly states this as Conjecture 3.1 and does not claim it as proven fact. The criticism is valid as a demand for validation but overstates by asserting "likely invalid" without evidence. The core concern (lack of validation) is preserved in Major weakness #1.
- **"Pseudo-code incomplete" complaint about missing implementation details** — The prose in §3.2.1 and §3.2.2 describes the DCT extraction, all-gather on the last dimension, and duplicate frequency averaging in sufficient detail. Algorithm 1 is a high-level description; this is standard practice.
- **"0.0012 GB meaningless without units"** — Table 1 reports per-GPU communication with units; the reduction factor is calculable from model size and the reported values. This is an exaggeration.
- **"Signum introduced abruptly"** — Signum has its own subsection (§3.3) and is a natural variant. Not abrupt.
- **"Missing convergence analysis"** — This is an empirical systems paper, not a theory paper. Demanding formal convergence proofs is scope creep.
- **"Learning rate not given"** is already in Minor weaknesses.
- The Strength Finder's claim about "architecture-agnostic and topology-agnostic design with minimal integration overhead" is kept as a design claim but downgraded because it conflicts with the verified weakness that this claim is untested beyond Transformers.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the central tension well: the idea is novel and promising, but the empirical validation falls short of the claims. The most interesting unresolved question is whether the DCT is genuinely exploiting structure in momentum or is simply acting as an arbitrary compression basis — a question the paper itself acknowledges (Conjecture 3.1) but does not resolve.

## Suggestions
- Add a direct validation experiment for the DCT assumption: take momentum snapshots from a reference training run, compute DCT energy compaction, and compare against PCA or a random orthogonal basis.
- Run experiments under at least one throttled-bandwidth condition (e.g., using `tc` to limit inter-node bandwidth) and report wall-clock time per step alongside the baseline.
- Include at least one alternative compression baseline: gradient quantization (e.g., 1-bit or 8-bit) or Top-*k* sparsification at a comparable communication budget.
- Report results with 3 seeds and include confidence intervals or standard deviations for the key metrics.
- Specify the learning rate schedule used for DeMo explicitly; ideally, show that the same schedule works across multiple *k* values without per-configuration tuning.
- Show training loss curves for longer training horizons (even a single run to 300B+ tokens) to verify that convergence holds beyond 100B tokens.

## Score and Decision

The paper proposes a genuinely novel approach to reducing distributed training communication. The core idea — using DCT-based frequency extraction on decoupled momentum — is creative and well-motivated from signal processing principles. The results, though limited, suggest the method can match AdamW on standard benchmarks while transmitting dramatically less data.

However, the paper has significant gaps that prevent it from being convincing at its current level of evidence: (1) the central assumption about DCT applicability to momentum is unvalidated; (2) the headline claim about bypassing high-speed interconnects is not empirically tested under constrained bandwidth; (3) the baseline comparison is too narrow (only AdamW, no other compression methods); and (4) the evaluation is limited to 100B tokens, single seed, and three tasks. These gaps collectively mean the paper's strongest claims remain speculative rather than demonstrated.

The idea is valuable enough to warrant further development, but the paper in its current form requires major additions to substantiate its claims. It would need at minimum a validation of the DCT assumption, bandwidth-constrained measurements, and additional baselines to be a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>