Here is the consolidated final review.

---

## Summary

PETRA combines reversible architectures with an asynchronous forward-backward pipeline to eliminate both activation buffers (via reversibility) and parameter buffers (by updating parameters between forward and backward without weight stashing). The paper provides a clean algorithmic formulation and validates empirically that the resulting approximate gradient does not degrade convergence, achieving competitive accuracy on CIFAR-10, ImageNet-32, and ImageNet across RevNet-18/34/50 models — matching or nearly matching standard backpropagation.

## Strengths

- **Competitive accuracy on large-scale benchmarks.** On ImageNet with RevNet-18, PETRA achieves 71.0% top-1 accuracy versus 70.8% for standard backpropagation; similar parity holds across RevNet-34 (73.5 vs. 73.2) and RevNet-50 (74.8 vs. 75.4) (Table 2). The gap closes entirely with sufficient accumulation steps (k=32, Figure 3). These results are the paper's strongest evidence.

- **Memory reduction via reversible architectures.** PETRA requires zero activation storage (via reversibility) and no parameter buffers (by avoiding weight stashing). Table 4 shows 54.3% peak-memory reduction relative to a PipeDream-style baseline that stores both input and parameter buffers. The paper provides the raw data for all four buffer configurations, enabling readers to compute savings against any baseline.

- **First use of reversible architectures for parallelization.** The related work section (Section 2) correctly identifies that prior work on reversible architectures focused on memory savings and generative modeling, not on parallelizing gradient computation. The paper provides a concrete algorithmic formulation (Equations 4–8, Algorithm 1) achieving this novel synthesis.

- **Accumulation analysis validates the approximation.** Figure 3 systematically shows that increasing the accumulation factor k monotonically closes the accuracy gap with backpropagation, confirming that the staleness introduced by PETRA's decoupled forward/backward is controllable and vanishes with sufficient accumulation.

## Weaknesses

### Fatal
None.

### Major

- **The paper claims "linear speedup" and "effective model parallelism" as central results, but all experiments run on a single GPU with no distributed training, wall-clock time, throughput, or speedup measurements.** The abstract states "PETRA achieves a linear speedup compared to standard backpropagation with respect to the number J of stages" (line 25), and contribution (3) claims PETRA "enables the parallelization of forward and backward pass computations across multiple devices, effectively distributing the workload and reducing training time" (line 26). However, the experimental section evaluates only classification accuracy on a single A100 80GB GPU (line 288: "Our models can run on a single A100, 80GB"). There are no measurements of communication overhead, per-batch wall time, or actual speedup when stages are distributed across devices. The conclusion itself retreats to "has the potential to achieve linear speedup" (line 317), revealing the gap between the advertised claim and the evidence. Without distributed experiments, the paper reads as a validated gradient-approximation method with an unconfirmed parallelization benefit. This is the single most important missing component.

- **No accuracy comparison against existing parallel methods (delayed gradients, DSP, PipeMare) under comparable setups.** Table 2 compares PETRA only against standard backpropagation on ResNets and RevNets. The paper does not compare to delayed-gradient methods (Zhuang et al., 2020/2021), DSP (Xu et al., 2019), or PipeMare (Yang et al., 2021) — all mentioned in the related work — either in accuracy or memory under the same hardware. The complexity table (Table 1) compares theoretical properties, but there is no empirical evidence that PETRA's gradient approximation trains to comparable accuracy with other practical parallel methods in the same regime. This makes it difficult to assess PETRA's practical advantage over existing alternatives beyond the theoretical memory analysis.

### Minor

- **The complexity comparison (Table 1) shows PETRA is theoretically *slower* than delayed gradients (mean time 3 vs. 2) under the same ideal assumptions, but this trade-off is not discussed.** The table also shows PETRA's communication volume is 4 vs. 1 for delayed gradients. The paper presents these numbers without acknowledging that under the stated assumptions, PETRA trades (slightly) higher theoretical time and 4× communication volume for memory savings. A reader comparing PETRA to delayed gradients needs an explicit discussion of when the memory savings outweigh the communication and compute overheads.

- **The memory savings framing (Table 4) emphasizes 54.3% reduction relative to a PipeDream baseline, but the incremental gain over standard reversible backpropagation is only ~2% (rows 3→4: 21.2→20.3 GB).** The paper states "54.3% memory reduction over the base configuration of Delayed Gradients" (line 291), which is factually accurate for that baseline. However, since reversible architectures already eliminate activation storage, PETRA's unique contribution beyond reversible backprop is removing the parameter buffer — a ~2% saving. The paper should more clearly distinguish the saving attributable to reversibility itself (52.3%, row 3) from the saving attributable to PETRA's no-weight-stashing (2%, rows 3→4).

- **No statistical significance or confidence intervals for larger datasets (ImageNet-32, ImageNet).** The paper reports variance <0.1 for CIFAR-10 (3 runs) but does not provide standard deviations for ImageNet-32 or ImageNet results (single run, presumably). Given that PETRA sometimes numerically exceeds backprop (e.g., 71.0 vs. 70.8 on RevNet18 ImageNet), the lack of reported variance makes it unclear whether results are within noise.

- **Unclear which non-reversible stages exist and how they affect the claims.** The paper notes that non-reversible downsampling blocks require buffers and activation checkpointing (lines 97–98, 201, 208–210), but does not specify how many stages fall into this category for the architectures tested. Since the memory and parallelism claims depend on reversibility, the number and impact of non-reversible stages should be quantified.

### Trivial
None.

## Nice-to-Haves

- **A formal or empirical analysis of the gradient approximation error** comparing PETRA's error (from both stale parameters *and* approximate reconstruction) to delayed-gradient methods (stale parameters only). This would strengthen the theoretical understanding of the method.

- **Ablation separating parameter staleness from reconstruction error.** An oracle that uses the *same* parameters for forward and backward (no update between F and B) would isolate the effect of the approximate inversion from the staleness effect, clarifying the source of any accuracy gap.

- **A discussion of the architectural constraints.** Not all architectures are easily reversible; ResNet modifications double input channels for residual blocks. The paper could discuss which layers in the tested architectures are non-reversible and how this affects the practical applicability.

## Removed Points

- "The abstract oversells communication efficiency by not mentioning the doubling of communication volume early enough" — removed as a minor presentation nitpick that is later clarified in the paper (line 95: "doubles the cost of backward communications").
- "PETRA sometimes exceeds backprop accuracy and is not explained" — removed; stochasticity within noise is the obvious explanation and the paper reports variance on CIFAR-10.
- "No limitations section" — the paper has a conclusion; this is a formatting preference, not a substantive weakness.
- "The interaction between gradient accumulation and staleness is not analyzed" — demoted to nice-to-have; Figure 3 provides the empirical analysis.
- "The paper would need substantial additional experiments to substantiate its primary contribution" / "I recommend rejection" — these are the harsh critic's opinion, not a specific verifiable weakness. Replaced with the concrete Major weakness above.
- Strength "Linear parallel speedup" — removed because it conflicts with the verified weakness that no distributed experiments support this claim; the evidence is theoretical only.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface an insight that the paper itself does not already articulate, though the tension between the paper's ambitious parallelism claims and its single-GPU experimental validation is worth highlighting. The core tension — that PETRA's gradient approximation is convincingly shown not to hurt accuracy, but the parallelization benefit is entirely theoretical — is the key structural observation that emerges from reading the paper alongside the reviews.

## Suggestions

1. **Reframe the claims to match the evidence.** Change "achieves a linear speedup" to "theoretical potential for linear speedup" or "enables model parallelism with linear speedup in an idealized setting" throughout the abstract and introduction. This brings the paper's narrative in line with what is actually demonstrated.

2. **Conduct distributed experiments** with stages placed on separate devices (e.g., 2–8 GPUs). Report wall-clock time per batch, epoch time, and speedup relative to: (a) single-device reversible backpropagation, and (b) a standard delayed-gradient baseline (DSP or PipeMare) under the same hardware setup. Report communication overhead as a fraction of total time.

3. **Add at least one delayed-gradient baseline to the accuracy comparison** (e.g., DSP with checkpointing) to show that PETRA's gradient quality is competitive with existing parallel methods, not just with sequential backpropagation.

4. **Clarify the memory framing.** When stating the 54.3% savings, explicitly note the decomposition: ~52% from reversibility (removing activation buffers) and ~2% from no weight stashing (removing parameter buffers). Report also the saving relative to standard reversible backpropagation.

5. **Report standard deviations** for ImageNet-32 and ImageNet results, or state the number of seeds used.

## Score and Decision

The paper introduces a clean and novel idea — combining reversible architectures with asynchronous forward/backward to eliminate buffers in model parallelism — and validates convincingly that the resulting gradient approximation does not degrade accuracy across multiple datasets and model sizes. These are real contributions. However, the paper's central advertised benefit (effective parallelism with linear speedup) is not empirically supported: all experiments are on a single GPU, there are no wall-clock or throughput measurements, and there are no accuracy comparisons against existing delayed-gradient methods. The gap between claim and evidence is significant but not fatal (the accuracy results stand independently). A revised version with distributed experiments and reframed claims would be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>