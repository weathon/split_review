Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final consolidated review.

## Summary

This paper proposes PETRA, a method that uses reversible architectures to decouple forward and backward passes across stages distributed on different devices, enabling model parallelism without activation buffers or weight stashing. The core idea is that reversible stages can reconstruct inputs during the backward pass, removing the need to store intermediate activations. The paper provides theoretical complexity analysis (Table 1) and reports competitive accuracy on CIFAR-10, ImageNet-32, and ImageNet with RevNet-18/34/50 (e.g., 71.0% vs. 70.8% backprop on ImageNet with RevNet-18).

## Strengths

1. **Novel application of reversibility to parallelization**: Using reversible architectures to eliminate activation buffers in parallel training is a genuine and underexplored idea (Sec. 3.3). The paper correctly identifies that reversibility provides a path around the quadratic memory scaling of delayed-gradient methods, and the complexity comparison in Table 1 cleanly isolates this advantage (zero activation storage, constant parameter buffer of 1, mean time of 3 vs. 3J for backprop).

2. **Competitive accuracy on ImageNet-scale benchmarks**: Table 2 shows that PETRA matches or closely approaches backpropagation accuracy on ImageNet across three model sizes (e.g., RevNet-34: 73.5% PETRA vs. 73.2% backprop; RevNet-50: 74.8% vs. 75.6% backprop). This is non-trivial — many alternatives to backprop (local learning, synthetic gradients) struggle at this scale.

3. **Clear theoretical analysis of complexity**: Table 1 provides a principled side-by-side comparison of storage, communication volume, FLOPs, and mean time for backprop, reversible backprop, delayed gradients (with/without checkpointing), and PETRA. This helps position the method's expected advantages and overheads transparently.

4. **Principled treatment of non-reversible stages**: The paper explicitly acknowledges (lines 97–98, Algorithm 1) that non-reversible downsampling layers still need buffers and falls back to activation checkpointing for those stages, rather than overclaiming universality.

## Weaknesses

### Fatal
None.

### Major

1. **No distributed runtime measurements despite parallelism being the central claim.** The paper's title is "Parallel End-to-end Training," the introduction claims "a linear speedup compared to standard backpropagation with respect to the number J of stages" (line 25), and Contribution 3 states that the method "enables the parallelization of forward and backward pass computations across multiple devices... reducing training time." Yet there are zero wall-clock time, throughput, or speedup measurements on any multi-device setup. The only "speed" evidence is the theoretical mean-time-per-batch column in Table 1, which explicitly assumes identical stages, perfect scaling, and zero communication overhead. A method that purports to demonstrate parallel training benefits must provide at least a simple distributed benchmark (e.g., 2-device or 4-device comparison) confirming that the theoretical speedup materializes in practice. The models "can run on a single A100" (line 288) is not a substitute. This gap is the single most important weakness of the paper.

2. **The empirical accuracy comparison is confounded by effective batch size.** PETRA uses batch size 64 with gradient accumulation k up to 32 (effective batch size up to 2048), while the backprop baselines use batch sizes 128/256 (line 243). The learning rate is scaled for PETRA using the Goyal et al. large-batch recipe, but the backprop RevNet baselines are not subjected to the same large-batch training. This means the reported accuracy comparison conflates two effects: PETRA's delayed-gradient approximation and large-batch training dynamics. Figure 1 partially addresses this (showing that increasing k closes the gap to backprop), but the backprop baseline in that figure is not shown as a curve — only indicated as a horizontal target value in text. The paper would be substantially strengthened by a controlled comparison: PETRA with k=1 (no accumulation) vs. backprop at the same batch size, and PETRA at a given k vs. backprop at the equivalent effective batch size.

### Minor

1. **The method description has a textual vs. formal inconsistency about parameter update timing.** The text states "As parameters are updated between the forward and backward phases" (line 129), but the equations (Eq. 1–5, lines 121–126) show both forward and backward using the same θ_j^t, with the update appearing at the end. This is not a fatal flaw — the algorithm (Alg. 1) makes the actual semantics clear (gradients are accumulated over k steps, then parameters are updated) — but the disconnect between the prose explanation and the equations is confusing and should be resolved in revision.

2. **The reported memory savings (54.3%) are dominated by a property inherited from reversible architectures, not from the PETRA scheduling itself.** Table 3 shows that 52.3% of the saving comes from not storing input buffers (a property of reversible architectures, also achieved by standard reversible backprop), while the additional 2% comes from PETRA's removal of the parameter buffer. The paper acknowledges this in the text (lines 307–308) but the headline number implies more novelty than is warranted. The comparison should also benchmark against the most memory-efficient delayed-gradient method (e.g., DSP with checkpointing, which also uses a single parameter buffer) to show PETRA's *incremental* advantage.

3. **In Figure 1, the backpropagation baseline accuracy is only indicated as a horizontal line value in the caption/text rather than plotted as a training curve.** The reader cannot visually compare the convergence dynamics. Including the backprop training curve at the same effective batch size would make the figure much more informative.

4. **The choice of accumulation factor k for each reported result in Table 2 is not disclosed.** The paper states "best value (picked on the training set)" (line 249) but does not report which k was chosen for each model/dataset combination. This is a transparency issue: different k values have different effective batch sizes and computational profiles.

### Trivial
- Line 243 contains a typographical duplication ("256 on ImageNet32" where ImageNet is meant).
- The sentence on line 243 ("batch size of 128 on ImageNet32 and CIFAR-10, and 256 on ImageNet32") has the second "ImageNet32" as a clear artifact; should be "ImageNet."

## Nice-to-Haves
- A single proof-of-concept on a non-vision architecture (e.g., a reversible transformer on a language task) would substantially strengthen claims of generality. The paper mentions Reformers as future work (line 320); including even a small-scale result would be valuable.
- A memory measurement on real hardware (rather than theoretical estimation in Table 3) would be a useful validation.
- Variance for the single-run ImageNet results would help assess significance, especially given the small gaps (≤0.8%) to backprop.

## Removed Points
These were flagged by reviewers but removed after verification against the paper:
- *"Inconsistency is fatal — method may reduce to standard reversible backprop without parallelism"*: Removed. This overstates the severity. The equations are a simplified abstraction with consistent time indexing; the algorithm (Alg. 1) clearly describes the parallel scheduling with gradient accumulation. The textual inconsistency is real but minor, not method-invalidating.
- *"Memory savings comparison against base configuration of Delayed Gradients is stacked"*: Partially removed. The paper acknowledges what each row represents (line 307: "Only storing inputs into buffers would correspond to the approach in [xu2019dsp, kosson2021pipelined]"). Retained as a minor weakness about framing, not removed entirely.
- *"Complexity analysis is a thought experiment"*: Removed. The analysis explicitly states its assumptions ("homogeneous setting," "ideal setting for one stage") and is clearly labeled as theoretical. It is standard practice to provide such analysis alongside empirical validation.

## Novel Insights
None beyond the paper's own contributions. The observation that most of the "54.3% memory saving" is inherited from reversibility rather than from the PETRA scheduling is a surface-level point that the paper itself partly acknowledges.

## Suggestions
1. **Run a minimal distributed experiment.** Even a 2-GPU or 4-GPU test on CIFAR-10 comparing wall-clock time per epoch for PETRA vs. backprop vs. a delayed-gradient baseline would validate the core speedup claim. Without this, the title claim ("Parallel End-to-end Training") is unsupported.
2. **Disentangle batch size from the PETRA approximation.** Compare PETRA at k=1 (no accumulation, batch=64) against backprop at batch=64. Then compare PETRA at k=32 (batch=64, effective batch=2048) against backprop at batch=2048 with the same LR scaling recipe. This would isolate whether the approximation itself causes any accuracy loss independent of large-batch training effects.
3. **Report the chosen k per experimental entry** in Table 2 and plot the backprop baseline as a training curve in Figure 1.
4. **Clarify the parameter update timing** by either rewriting the prose to match the equations or adding a time index that distinguishes the version used in reconstruction from the version used in forward.

## Score and Decision

**Bracketing (Round 1):** Queried on related topics (reversible architectures, pipeline parallelism, delayed gradient methods). The closest anchors were: Clapping (3.00, Reject — pipeline parallelism with communication compression, no wall-clock speedup), AMDP (5.50, Reject — asynchronous pipeline parallelism with actual distributed experiments), DiffusionBlocks (6.00, Accept — block-wise training with novel theory but no wall-time measurements), and Learning without Global BP (3.50, Withdrawn — backprop alternative on small-scale only). **Initial bracket: 4.0 – 6.0.**

**Narrowing (Round 2):** Queried for narrower bands within the bracket. Key comparisons:
- **AMDP (5.50, Reject)** — Similar topic (asynchronous pipeline parallelism with staleness). AMDP has *actual* distributed experiments (8×A800, throughput measurements, baseline comparisons) which PETRA lacks entirely. However, PETRA's idea (using reversibility) is more novel than AMDP's scheduling optimization. PETRA is weaker overall.
- **Learning without Global BP (3.50, Withdrawn)** — Also an alternative to backprop. Smaller datasets only (CIFAR-10/100, Tiny-ImageNet), no ImageNet. PETRA is clearly stronger (ImageNet results, competitive accuracy). PETRA is stronger.
- **DiffusionBlocks (6.00, Accept)** — Block-wise training. Novel theory, multiple tasks, but also lacked wall-time measurements per some reviewers. The scope of validation (vision, diffusion, autoregressive, text generation) is broader than PETRA. PETRA is slightly weaker.
- **Equilibrium Propagation (4.50, Accept)** — Alternative to backprop, accepted as poster. Comparable novelty level.
- **Partial Parameter Updates (4.00, Reject)** — Distributed training efficiency. Limited experiments. PETRA is stronger.

**Final score after calibration: 4.5.** PETRA has a genuinely novel idea and competitive accuracy on ImageNet, but the lack of any distributed runtime measurements is a critical gap for a paper whose central claim is parallel speedup. The paper is stronger than Learning without Global BP (3.5) and Clapping (3.0), comparable to the Equilibrium Propagation paper (4.5), but weaker than AMDP (5.5) because AMDP validates its speed claims empirically. The evaluation is incomplete for the claims made.

**Anchors consulted (all rounds):**
1. Clapping (yOkek71cG5) — 3.00, R1 — pipeline parallelism with compression, no wall-clock speedup
2. AMDP (cfZNOO6ZHf) — 5.50, R1/R2 — asynchronous pipeline parallelism, has distributed experiments, rejected
3. DiffusionBlocks (pwVSmK71cS) — 6.00, R2 — block-wise training via diffusion, broader validation
4. Learning without Global BP (uA33x2ghIC) — 3.50, R2 — backprop alternative, small-scale only
5. Equilibrium Propagation (e5l1sD0nk2) — 4.50, R2 — biologically plausible learning, accepted poster
6. Partial Parameter Updates (vU7pcaDypQ) — 4.00, R1 — distributed training efficiency
7. MT-DAO (5yPP238v4c) — 6.50, R1 — distributed adaptive optimizers, strong theory + empirical
8. PipeTune (NlizdhvhvM) — 4.50, R2 — pipeline parallelism for VLMs
9. TAH-Quant (cEkVJeMwSd) — 4.50, R2 — activation quantization in pipeline parallelism
10. Reversible GNS (Lu7WPPkmOq) — 4.50, R2 — reversible architectures for physics
11. Forward Target Propagation (jMZpXvDDbB) — 4.50, R2 — backprop alternative
12. ePC (lQhBWz59qW) — 4.00, R2 — alternative to backprop for PC networks
13. Parallel Training in SNNs (RGxDhp3m0I) — 3.50, R2 — parallel training of spiking NNs

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>