Now I have all the information needed. Let me write the final consolidated review.

## Summary

PETRA proposes a method to parallelize training of reversible neural networks by combining reversible architectures with delayed gradient computation. The key idea is to decouple forward and backward passes across stages so that each stage on its own device can compute independently, using the reversibility property to reconstruct activations during the backward pass (eliminating activation buffers) and updating parameters between forward and backward (eliminating parameter buffers). Results on CIFAR-10, ImageNet32, and ImageNet show competitive accuracy with standard backpropagation (within 0.1–0.6 percentage points), a 54.3% memory reduction over delayed-gradient baselines, and wall-clock speedups of 2.4–3.0× over non-overlapped model parallelism.

## Strengths

- **Competitive accuracy with backpropagation across multiple benchmarks** (Table 2): PETRA matches or nearly matches backpropagation accuracy across RevNet18/34/50 on CIFAR-10, ImageNet32, and full ImageNet. For example, RevNet18 on ImageNet: PETRA 71.0% vs Backprop 70.8%. This directly supports the claim that PETRA is an effective training method.

- **Substantial and well-characterized memory reduction** (Table 3, line 273): PETRA achieves 54.3% memory savings over the full-buffer delayed-gradient configuration for RevNet50 on ImageNet. The paper clearly maps each buffer configuration to specific prior work (PipeDream for both buffers, Xu et al./Kosson et al. for input-only), making the comparison interpretable.

- **Measured wall-clock speedup from parallelism** (Table 5): Speedups of 3.0× (RevNet-18 on 10 GPUs) and 2.4× (RevNet-34 on 18 GPUs) over reversible backpropagation with model parallelism. While not ideal linear scaling, the speedups are tangible and demonstrate the practical benefit of the approach.

- **Informative ablation on the staleness-accuracy trade-off** (Figure 4): The clear demonstration that increasing the accumulation factor \(k\) monotonically closes the accuracy gap with backpropagation on ImageNet (from ~0.5% gap at \(k=1\) to near-zero at \(k=32\)) provides direct evidence that the stale gradient approximation introduced by PETRA is controllable.

- **Clear theoretical complexity analysis** (Table 1): The paper provides a clean comparison of PETRA against backpropagation, reversible backpropagation, and delayed gradients + checkpointing across storage, communication, FLOPs, and time, formalizing the claim of linear speedup under ideal homogeneous conditions.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to practical parallel training methods.** The paper compares PETRA's throughput only to "basic model parallelism" (reversible backpropagation without overlapping), which is a strawman baseline — any parallel method would outperform sequential execution on the same hardware count. The paper positions PETRA as addressing "challenges in parallelizing deep model training," yet provides no empirical comparison to pipeline parallelism (GPipe, PipeDream) or other delayed-gradient methods on wall-clock training time. Without such comparisons, the practical contribution relative to the large existing body of parallel training work is unclear. The memory comparison in Table 3 partially compensates by comparing against PipeDream and Xu et al. configurations, but the throughput experiments lack this context. This is an evidential gap that significantly weakens the paper's core claim.

### Minor

- **Linear speedup claim in the abstract is unqualified relative to empirical results.** The abstract states that "PETRA achieves a linear speedup compared to standard backpropagation with respect to the number \(J\) of stages." The empirical speedups in Table 5 are 3.0× on 10 stages and 2.4× on 18 stages — far from linear (10× and 18×, respectively). The paper notes that stages are "unbalanced" in the experimental section, but the abstract-level claim is unconditional. The linear speedup is supported as a theoretical complexity result (Table 1) under ideal homogeneous assumptions, but this context is missing from the abstract, creating a misleading first impression.

- **Accumulation factor \(k\) selected on training set accuracy.** The paper reports "the best value (picked on the training set) of accumulation steps within {1, 2, 4, 8, 16, 32}" (line 217). Selecting hyperparameters on the training set is unusual and could lead to overly optimistic accuracy estimates, though the impact is limited in practice since Figure 4 shows the accuracy-\(k\) relationship is monotonic on validation data.

- **Throughput measurements only on CIFAR-10.** Table 5 reports speedup only for CIFAR-10, not for ImageNet. Since ImageNet involves larger activations and potentially different communication/computation ratios, it is unclear whether the speedups transfer.

- **Table 4 ablation uses only \(k=1\).** The ablation on buffer configurations (CIFAR-100, Table 4) tests only \(k=1\), while the main ImageNet results use larger \(k\) values. The interaction between buffer configuration and accumulation is therefore not explored under the conditions of the main results.

### Trivial

- **Throughput numbers lack statistical variance.** The wall-clock measurements (Table 5) are reported as point estimates without standard deviation or confidence intervals, making it hard to assess the reliability of the reported speedups.

## Nice-to-Haves

- Comparison to pipeline parallelism (even a simple one) would contextualize the speedup numbers.
- A convergence curve (training loss vs. epochs) for PETRA vs. backpropagation on ImageNet would help assess stability.
- Measurement of communication vs. computation time across stages.
- Reporting the fraction of non-reversible stages and their contribution to total memory.
- A more realistic complexity model for the theoretical analysis (Table 1) that accounts for communication overhead.

## Removed Points

- **"Unclear memory comparison and missing details":** REMOVED because the paper explicitly states (line 273) that "Storing both inputs and parameters into a buffer corresponds to the PipeDream approach... while only storing inputs would correspond to the approach in Xu et al. (2019); Kosson et al. (2021)." The critic's concern about "0 activation storage" is also addressed: the "0" refers to cross-stage activation buffers, which is the standard meaning in this context (reversible backpropagation also shows "0" in Table 1).

- **"Related work omits activation checkpointing for pipeline parallelism":** REMOVED because the paper does discuss this (line 54): "Some implementations propose to limit this overhead by combining activation checkpointing (Chen et al., 2016) with pipelining (Kim et al., 2020; Liu et al., 2023)."

- **"Introduction and Contributions are too broad":** REMOVED as a vague criticism without a specific anchor in the paper. The contributions list (items 1–6) is appropriately structured for the scope.

- **"Complexity analysis needs more realistic model":** MOVED to Nice-to-Haves. Suggesting a more involved model is a reasonable request but not a weakness of the current analysis, which is transparent about its assumptions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate or acknowledge.

## Suggestions

1. Add a comparison to at least one pipeline parallelism method (e.g., a simple implementation of PipeDream-style training) on the same GPU count and model size for wall-clock throughput. This is the single change that would most strengthen the paper, as it directly addresses the central claim about parallel training.

2. Qualify the "linear speedup" claim in the abstract to indicate it holds under ideal homogeneous conditions, and explicitly note the empirical results show substantial but sub-linear speedup due to stage imbalance.

3. Report throughput on ImageNet in addition to CIFAR-10 for a more representative picture of scalability.

4. Add standard deviations to the throughput measurements.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OFgOmMlVUY.md | 2.50 | 1 | Weaker — withdrawn paper, unclear contribution |
| 1MHgMGoqsH.md | 3.00 | 1 | Weaker — MPC framework for BP/FF unification, limited empirical support |
| MCQdWMs5iA.md | 3.00 | 1 | Weaker — withdrawn paper, explicit optimization approach |
| 6cDEcJsE1Y.md | 3.00 | 1 | Weaker — quantum ML, different domain |
| **97dJ3Jp5P4.md** (Moonwalk) | **4.75** | 1,2 | **Weaker** — similar topic (alternatives to backprop for reversible nets), but tested only on tiny models (3 blocks), lacks parallel training evaluation. PETRA has stronger empirical validation. |
| **wcKGK0tRHD.md** (The Trifecta) | **5.00** | 1,2 | **Weaker** — FF algorithm improvements, only reaches CIFAR-10. PETRA shows ImageNet results and more principled contribution. |
| **kC5i5X9xrn.md** (LightSeq) | **5.00** | 2 | **Comparable** — sequence parallelism system, also lacks some baselines. PETRA has stronger accuracy validation but narrower parallel scope. |
| **yqIJoALgdD.md** (Zero Mem SNN) | **5.75** | 1,2 | **Comparable/slightly stronger** — reversible SNN training, one strong (8) review but others cited limited dataset scope. |
| **Ng1r9kTep4.md** (InvAct) | **6.33** | 2 | **Stronger** — simpler, more broadly applicable memory reduction method; cleaner evaluation. |
| tyEyYT267x.md | 8.00 | 1 | Much stronger — oral-level paper, different topic |
| PdaPky8MUn.md | 8.00 | 1 | Much stronger — oral-level paper, different topic |

**Round-1 bracket:** 3.5–7.5 (clearly above the ~3.0 weak papers, clearly below the ~8.0 oral-level papers).

**Round-2 narrowing:** PETRA is stronger than Moonwalk (4.75) and The Trifecta (5.00), comparable to LightSeq (5.00) and Zero Memory SNN (5.75), and weaker than Inverted Activations (6.33). The main gap to the upper part of this bracket is the absence of comparison to actual parallel training methods.

**Final score:** 5.5 — a genuine contribution with a clean theoretical framing and solid accuracy/memory results, but the central claim about parallel training effectiveness is under-supported by the experimental design (no comparison to practical parallel methods). This places the paper in the "marginally below acceptance threshold" range, needing a significant experimental addition.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>