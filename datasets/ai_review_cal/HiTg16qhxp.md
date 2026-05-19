- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 8, 3, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes Dynamic Neural Response Tuning (DNRT), a mechanism comprising two components: Response-Adaptive Activation (RAA), which adds an input-dependent scalar offset to the argument of an activation function (e.g., GELU), and Aggregated Response Regularization (ARR), which uses a momentum-updated per-class mean to regularize the L1 distance of features to their class mean. The authors evaluate DNRT across MLPs, ViTs, and CNNs on several image classification benchmarks, plus node classification and long-tailed recognition, reporting consistent but modest accuracy improvements.

## Strengths

- **Broad and consistent empirical evaluation across architectures and tasks.** DNRT improves top-1 accuracy over GELU baselines on MLP (e.g., CIFAR-10), ViT variants (e.g., ViT, DeiT, CaiT, PVT, TNT), and CNNs (AlexNet, VGG, ResNet, MobileNet, ShuffleNet) — spanning Tables 1–3. Gains extend to node classification (GCN/GraphSAGE on DGraph) and long-tailed CIFAR-10 (Table 4). While individual gains are modest, the consistency across many settings is evidence that the method has real, non-random effects.

- **Ablation study confirms both components contribute.** Table 5 (on a CIFAR-100 model) shows that both RAA alone and ARR alone improve over the baseline, and their combination yields further gains. This supports the claim that each proposed mechanism is individually helpful and that they are complementary.

- **Low computational overhead.** RAA introduces only a d-dimensional vector w and scalar b per activation (Eq. 4), and ARR stores K vectors for per-class moving means. The paper states "negligible parameters and computations" (Sec. 4.1) and that ARR "does not affect inference speed" (Sec. 4.2), which is a practical advantage.

- **Response visualizations align with the claimed mechanism.** Figure 2 shows qualitatively that RAA produces sparser activation responses (fewer erroneously activated channels) and that ARR concentrates the per-class aggregated response distributions, consistent with the paper's biological motivation and design goals.

## Weaknesses

### Fatal
None.

### Major

1. **Main experiments conflate RAA and ARR, making it impossible to attribute gains to the activation mechanism alone.** Tables 1–3 compare a baseline activation (e.g., GELU) against "DNRT," which simultaneously replaces the activation with RAA *and* adds the ARR loss. The central claim that RAA is a *superior activation mechanism* is not isolable from these results. The ablation (Table 5) does separate the components but is limited to a single dataset (CIFAR-100) and a single architecture (likely ViT-S based on context). A proper evaluation would compare RAA without ARR against baselines across the full set of architectures and datasets.

2. **No statistical significance or variance reporting.** All tables report single-run top-1 accuracy. Many improvements are under 0.5% (e.g., ViT-S on CIFAR-100). Without multiple seeds or error bars, small improvements could reflect training noise rather than true gains. This is a significant weakness for an empirical paper making comparative claims.

3. **ARR is presented as a novel contribution but is not compared to existing feature-regularization methods.** Constraining features to be close to per-class running means is related to center loss, L2-constrained features, and variance regularization — none of which are cited or compared. Without establishing what ARR offers beyond these known techniques, its novelty and incremental value are unclear. A comparison under the same settings (with and without the class-conditional running mean) is needed.

4. **Missing comparisons to simpler adaptive activation baselines.** RAA adds a learned linear function w^T x + b whose scalar output is added to all feature dimensions before the CDF. The paper does not compare to simpler alternatives such as per-channel learnable biases before activation, per-channel scale-and-shift (like a learned BN before activation), or learnable α in Eq. 2 (which is already a simpler adaptive version). These would help establish whether the vector-level linear mapping is justified.

### Minor

1. **The biological grounding is overstated relative to the actual mechanism.** The paper invokes per-neuron dynamic thresholds varying with environment (Observation 1), but RAA applies the *same* scalar offset (w^T x + b) to all d dimensions of a feature vector. The "per-neuron" story does not match the "shared scalar offset across all channels" implementation. The mechanism is better described as a simple input-dependent shift of the activation function's effective threshold.

2. **Observations in Section 3 are purely qualitative.** The claims about "truncated response distributions" and "high Gaussian variances" are stated without quantitative measurements (e.g., what fraction of channels are truncated, what the variance values are). Figure 2 provides visualization but only for one model and one dataset.

3. **Key hyperparameters λ (ARR loss weight) and J (number of layers with ARR) are not specified.** The momentum m = 0.2 is given, but λ and J are absent from the experimental settings. No sensitivity analysis for these hyperparameters is provided, making it harder to assess robustness.

4. **Generalization experiments (Table 4) lack comparison to task-specific methods.** The node classification results compare DNRT against a single baseline (GELU) within the same GCN/GraphSAGE architecture, but do not compare against specialized methods for these tasks (e.g., re-weighting or oversampling for long-tailed classification, or other GNN training techniques). The results are therefore hard to contextualize.

### Trivial

- The notation in Eq. 4 applies the scalar CDF Φ to a vector offset by a scalar; clarifying this operation (element-wise application of Φ to each component) would improve readability.

## Nice-to-Haves

- A sensitivity analysis on momentum m and loss weight λ would strengthen the paper.
- Reporting inference-time cost (e.g., throughput or latency) would substantiate the "negligible overhead" claim beyond parameter count.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh critic point that RAA offset is "fixed at inference" (from Point 2).** The critic writes: "the offset is a deterministic linear function of the input that is learned once and then fixed at inference." While w and b are learned parameters, the offset w^T x + b varies with each input x at inference — the mechanism is input-dependent, making it "dynamic" in the relevant sense. The critic's phrasing suggests the offset is constant at inference, which is not the case. *Removed as factually misleading.*

2. **Harsh critic's specific ablation numbers (81.52% to 81.68%, a 0.16% gain).** These numbers do not match the values reported in the strength finder (which gives 75.87 vs. 74.61 for RAA alone, a 1.26% gain on a different setup). Since the actual table values are in an image, I cannot verify either set, but the critic's numbers appear to conflate Table 2 ViT-S CIFAR-100 results with the ablation. *Removed due to likely factual inaccuracy; the structural criticism (limited ablation scope) is retained above.*

3. **Harsh critic's claim about "unfair comparison" framing.** Not applicable — the critic did not claim unfair asymmetry favoring the baseline.

4. **Strength finder's strengths about "importance of the problem" or generic praise.** The strengths kept are concrete and specific to the paper's evidence. Generic framing (e.g., "addressing an important problem") has been filtered out.

## Novel Insights

None beyond the paper's own contributions. The two reviews (harsh critic and strength finder) largely converge on what the paper does well (broad evaluation, low overhead) and where it falls short (conflated evaluation of RAA vs. ARR, missing baselines, no error bars). The most actionable insight from synthesizing the two is that the paper's central claim — RAA is a superior activation — could be rescued by a clean ablation isolating RAA across the full architecture zoo, but the current evidence is insufficient to support that claim at the level of novelty the paper asserts.

## Suggestions

- Isolate RAA (without ARR) across all architectures and datasets in Tables 1–3 to directly support the claim that the activation modification alone improves performance. This is the single most impactful change.
- Add at least 3 random seeds with mean ± std for all accuracy results, especially for comparisons where gains are <1%.
- Compare ARR against center loss and L2 feature regularization under the same settings to establish its distinct contribution.
- Compare RAA against simpler learnable-activation baselines (per-channel bias before activation, per-channel scale, or the scalar-only α variant in Eq. 2) to justify the vector-level linear mapping design.
- Specify λ and J, or provide a sensitivity analysis for λ over a reasonable range.
- Add quantitative support for the observations in Section 3 (e.g., fraction of truncated channels, measured variance before and after DNRT).
