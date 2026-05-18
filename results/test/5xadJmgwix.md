Now I have all the information needed to compile the final review. Let me synthesize everything.

---

## Summary

This paper introduces a scale-adaptive classifier-guided diffusion model for pixel-level sketch generation. The core idea is to dynamically optimize the classifier guidance scale at each sampling timestep using a scaling indicator (balancing recognizability and complexity) and a residual sketch (measuring per-pixel changes from guidance). A three-phase sampling strategy (warm-up unconditional steps → scale-adaptive guided sampling → end-up unconditional denoising) further improves diversity and quality. Experiments on QuickDraw (345 classes) show the method outperforms both vector-based (SketchRNN, ChiroDiff) and raster-based (StyleGAN2, DDIM, CFDG) baselines on FID, recall, and CLIP-based expressiveness metrics.

## Strengths

- **Dynamic scale optimization demonstrably improves over fixed-scale alternatives.** The ablation in Table 2b shows that replacing the adaptive scale selection with a constant scale ("No Adaptive") degrades FID, directly validating the paper's central mechanism. Figure 5 further visualizes how optimized residual sketches become cleaner and more structured.

- **Three-phase sampling is carefully ablated and each component contributes.** Table 2b systematically removes warm-up ("No Warm-up": worse FID and recall), adaptive scaling ("No Adaptive": worse FID), and end-up denoising ("No End-up": worse FID and recall, higher cost). This supports the claim that all three phases are beneficial and goes beyond a simple fixed-pipeline design.

- **Comprehensive evaluation against a diverse set of baselines.** The paper compares against 5 vector-based methods (SketchRNN, SketchHealer, SketchAA, SketchKnitter, ChiroDiff) and 3 raster-based methods (StyleGAN2, DDIM, CFDG) using FID, precision, recall, plus proposed CLIP-based expressiveness metrics. The proposed method leads on FID, recall, and both CLIP metrics.

- **Identifies and addresses a genuine domain-specific problem ("over-sketching").** The observation that larger classifier guidance scales cause repetitive strokes in sketches (Section 1, Figure 1a) — a phenomenon absent in photo generation — is well-motivated and drives the paper's technical contributions.

## Weaknesses

### Major

- **The complexity measure $c(x_{0|t})$ is mathematically underspecified.** The paper defines $c(x_{0|t}) = \frac{1}{HW} \sum_{HW} \|x_{0|t}\|_0$ as the "fraction of stroke pixels." However, $x_{0|t}$ is a continuous-valued image (floating-point pixel values), so the L0 norm without a threshold will count essentially all non-zero entries, giving a near-constant value regardless of actual stroke density. This undermines the scaling indicator's complexity term as written. The paper already uses a Sigmoid function $M(\cdot)$ for binarization in the residual sketch (Eq. 3), suggesting the authors understand the need for thresholding, but they do not apply it to the complexity measure. This is fixable (e.g., specify a threshold or apply $M(\cdot)$ before computing $c$) but as presented the mathematical definition does not produce a meaningful signal.

### Minor

- **Per-step SGD optimization details are missing.** The paper states that SGD is used to minimize $L_t(s)$ at each timestep but does not report: how many gradient steps per timestep, the learning rate for this inner loop, convergence criteria, or sensitivity to the initialization of $s$. The batch averaging trick (N=128) is mentioned as a cost-reduction strategy, and 5.74 s/sketch is reported for one ablation, but a full wall-clock comparison with fixed-scale baselines is not provided.

- **Rasterization procedure for vector baselines is not described.** Vector-based methods (SketchRNN, ChiroDiff, etc.) produce coordinate sequences, which must be rasterized for comparison. The paper does not describe the rasterization resolution, stroke width, or any resolution-control procedure, making the comparison against vector methods difficult to reproduce or evaluate for fairness.

- **Classifier behavior on $x_{0|t}$ is not analyzed.** The recognizability term $f(x_{0|t}) = p_\phi(y|x_{0|t})$ and the warm-up termination (Eq. 5) both evaluate the classifier (trained on noisy data $x_t$) on the clean estimate $x_{0|t}$. Early in sampling, $x_{0|t}$ can be blurry and unlike any training input. While classifier-guided diffusion commonly uses such predictions and the paper's empirical results suggest the approach works, the paper provides no analysis (e.g., calibrated probability histograms across timesteps) to show the classifier outputs are reliable in this regime.

- **Data preprocessing (QuickDraw 28×28 → 64×64) is underspecified.** QuickDraw provides 28×28 grayscale sketches, but the paper uses 64×64 RGB images. How the sketches were upscaled and converted to RGB is not described, which matters because stroke density statistics and the complexity measure depend on resolution.

### Trivial

- The paper does not disclose the number of SGD iterations or learning rate used for the per-step scale optimization, which is needed for reproducibility.

- The CLIP-Fine score depends on a subjective distinction between "coarse" and "fine-grained" captions without reporting inter-annotator agreement or selection criteria.

## Nice-to-Haves

- **Comparison against classifier-free guidance with a dynamic schedule.** The paper already compares against vanilla CFDG. A natural extension would be to compare against CFDG with a hand-tuned dynamic scale schedule (e.g., linearly increasing then decreasing) to isolate whether the *adaptive mechanism itself* drives improvements or simply the *three-phase structure*.

- **A simpler complexity measure.** The L0-based measure could be replaced with a smooth proxy (e.g., total variation, or the mean of the Sigmoid-binarized image $M(x_{0|t})$) that is well-defined for continuous-valued inputs without additional thresholding.

- **Convergence analysis of per-step SGD** (number of iterations needed, sensitivity to initialization) would strengthen the reproducibility and practical applicability of the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not compare against classifier-free guidance"** — This is factually incorrect. The paper lists CFDG (Ho & Salimans, 2021) as a competitor in Table 1 and compares against it. The reviewer's intended point (CFDG with a dynamic scale) is valid but is a *variant* of CFDG, not CFDG itself, and is moved to Nice-to-Haves.

- **"CLIP-Score adds little without clear validation"** — This is a matter of opinion; CLIP metrics are presented as supplementary to FID/precision/recall (not replacements). The paper provides examples (Figure 14) showing alignment between generated sketches and retrieved captions. The criticism is weakened to a Trivial note.

- **"Code release is not mentioned; given the many heuristic components, code is essential"** — The lack of a code release is not itself a methodological weakness of the paper, and questioning reproducibility based on code not being mentioned goes beyond what can be evaluated from the paper itself. Moved here.

## Novel Insights

The reviews surface an important observation not fully articulated in the paper: the scaling indicator (Eq. 2) combines two terms — complexity and recognizability — but the complexity term as formally defined is likely non-functional in practice due to the L0-on-continuous issue. This means the reported empirical success of the adaptive mechanism may be driven *entirely* by the recognizability term and the residual-sketch matching, rather than by a genuine joint optimization of complexity and recognizability. If true, this simplifies the claimed contribution but does not invalidate it — the method still works, just perhaps for a simpler reason than claimed. The authors should clarify this in revision.

## Suggestions

1. Fix the complexity measure definition: specify a threshold (e.g., pixels > 0.5 after Sigmoid) before computing the L0 norm, or replace it with a well-defined continuous measure such as the mean of $M(x_{0|t})$.

2. Report the per-step SGD details: number of iterations, learning rate, initialization strategy for $s$, and wall-clock time vs. fixed-scale baselines.

3. Add an analysis of classifier probability histograms on $x_{0|t}$ across sampling timesteps to validate that the recognizability signal is meaningful, especially in early steps.

4. Describe the rasterization parameters used for vector-baseline comparisons and the upscaling procedure for QuickDraw data.

## Score and Decision

The paper tackles a genuine, underexplored problem (pixel-level sketch generation with controlled complexity) and presents a well-ablated, empirically strong solution. The main weakness — an underspecified complexity measure that as written would not produce the intended signal — is real but fixable without restructuring the paper. All other issues are missing details or minor concerns. The core contributions (adaptive scale selection, three-phase sampling) are empirically validated and produce state-of-the-art results on QuickDraw.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>