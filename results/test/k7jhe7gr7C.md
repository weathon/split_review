Now I have all the information needed to write the final consolidated review.

---

## Summary

This paper proposes HASTE, a plug-and-play convolution module that uses locality-sensitive hashing (LSH) to detect redundant channels in CNN feature maps at test time, merges similar channels (by averaging inputs and summing corresponding filter channels), and performs convolutions on the reduced depth to achieve FLOPs savings. The key selling point is that it requires **no training data, no fine-tuning, and no retraining** — the module can be swapped into a pre-trained model and yield immediate FLOPs reduction. Experiments on CIFAR-10 and ImageNet across multiple architectures (ResNet, VGG, WideResNet) show substantial FLOPs reductions (up to ~47% on ResNet34 CIFAR-10) with moderate accuracy drops.

## Strengths

- **First training-free and data-free structured pruning method with these guarantees.** While other pruning approaches require either custom training procedures (e.g., DMCP, DGNet, FTWT) or post-pruning fine-tuning (PFEC, SSL, FPGM), HASTE demonstrably requires neither (Table 1). This is a clean, well-defined niche and the paper successfully demonstrates it.

- **Meaningful empirical results on standard benchmarks.** The method achieves a 46.72% FLOPs reduction on ResNet34 (CIFAR-10) with only 1.25% accuracy drop, and 18.69% FLOPs reduction on ResNet34 (ImageNet) with 1.25% accuracy drop — all without any retraining. These results are credible evidence that the approach works across architectures and dataset scales.

- **Dynamic, input-dependent compression.** Unlike static pruning methods that fix which channels to remove, HASTE's compression ratio varies per patch and per image (Figure 3(b)), adapting to the actual redundancy in each input. This is a genuine structural advantage enabled by the LSH mechanism.

- **Simple hyperparameter-controlled trade-off.** The single hyperparameter \(L\) (number of hyperplanes) provides a continuous knob between accuracy and FLOPs reduction (Figure 2(b)), allowing multiple model variants to be generated from one baseline without retraining.

- **Computationally efficient hashing design.** The sparse random projections (using vectors with entries in \(\{1,0,-1\}\) at sparsity \(s\)) turn expensive multiplications into cheap additions (Section 3.1), which directly mitigates the overhead of the redundancy detection step.

## Weaknesses

### Fatal

None.

### Major

- **No wall-clock timing or latency measurements.** The paper's central claim is "instant reduction of inference cost," yet all results are reported exclusively in FLOPs reduction. The HASTE module introduces non-trivial overhead: per-patch hashing of all \(C_{in}\) channels, per-patch input merging, and per-patch filter merging repeated \(C_{out}\) times. For pointwise (1×1) convolutions, the paper itself notes that "the cost overhead of the hashing and merging steps is higher relative to the baseline" (Section 4.3), but provides no data quantifying this. Without wall-clock measurements on a representative device (CPU, edge GPU, or even a standard GPU), the practical speed claim remains unsubstantiated — the method could plausibly slow down inference on some architectures despite reducing FLOPs. This is the most significant gap in the paper's evaluation.

- **The VGG19-BN "outperforms all other methods" claim is overstated due to mismatched baselines.** On CIFAR-10 VGG19-BN, the paper states it "outperform[s] all other methods with 38.83% FLOPs reduction" compared to DMCP's 34.14%. However, HASTE's baseline accuracy (93.95%) is 1.76 percentage points higher than DMCP's baseline (92.19%), and HASTE's accuracy drop (1.63 pp) is substantially larger than DMCP's (0.25 pp). At a more comparable accuracy loss, the FLOPs reduction would likely be smaller. The claim is technically true on the numbers presented but gives a misleading impression of relative performance. The paper should either baseline-normalize these comparisons or temper the claim.

### Minor

- **The core approximation (Eq. 1) has no theoretical error analysis.** The paper motivates the approximation by the distributive property of convolution but provides no bound on the approximation error in terms of channel similarity or hash collision probability. While the extensive empirical evaluation partially addresses this, a principled characterization of when the method might fail (e.g., a threshold below which accuracy drops catastrophically) would strengthen the contribution. As it stands, the method's reliability is validated only for the specific architectures and datasets tested.

- **Hyperparameter choices are dataset-dependent.** The sparsity \(s\) and the starting layer for pruning are tuned per dataset (\(s=2/3\) for CIFAR-10, \(s=1/2\) for ImageNet; different starting layers). This undercuts the "data-free" framing slightly — while no training data is needed, the method does require meta-knowledge about dataset complexity to set hyperparameters. The paper does not provide a principled, data-free procedure for choosing these values.

- **Limited analysis of hashing overhead.** The paper claims the overhead is "outweighed" by savings (Section 3.3) but does not provide a breakdown of the added FLOPs from hashing and merging vs. the savings from the reduced convolution. An explicit accounting would allow readers to assess where the method is most beneficial and where overhead dominates.

### Trivial

- The description of patch rasterization ("patches of size \(K+2\) with an overlap of two pixels on each side") is slightly confusing. A concrete example would improve clarity.
- The paper does not report the average bucket size or distribution of hash collisions across layers, which would help explain the observed compression ratios.

## Nice-to-Haves

- A formal bound on the approximation error of Eq. (1) in terms of cosine similarity between grouped channels and the collision probability of the LSH scheme, which would turn the heuristic into a more principled method.
- Wall-clock timing on a representative edge device (e.g., NVIDIA Jetson, Raspberry Pi, or CPU) to validate that FLOPs reduction translates to real speedup.
- An ablation study comparing different merging strategies (mean vs. sum for both inputs and filters) to justify the current choice.
- An analysis of one case where the method fails (e.g., a shallow network or fine-grained classification task) to help users understand its limitations.

## Removed Points

- **"Comparisons to prior work are misleadingly presented"** — Removed. The paper explicitly acknowledges "we cannot give a direct comparison" (line 180), separates methods into distinct columns in tables (Tuning-Based, Training-Based, Data-Free), and does not claim to compete with trained methods on ImageNet. The presentation is transparent and the context is useful.
- **"Standard deviations indicate instability"** — Removed. A standard deviation of ±0.99% for FLOPs reduction on a single configuration is small and does not indicate meaningful instability.
- **"Positive scaling behavior may simply reflect more redundant channels"** — Removed. The paper's own explanation (line 342) already states this: "We relate this to the fact that larger models typically exhibit more redundancies." This is not a weakness; it is the paper's interpretation.
- **"Missing ablation on merging strategy"** — Moved to Nice-to-Haves. It would be nice to see, but its absence does not undermine the core claims.

## Novel Insights

None beyond the paper's own contributions. The key insight — using LSH for on-the-fly channel redundancy detection in CNNs — is already well articulated by the paper.

## Suggestions

1. Measure and report wall-clock inference time (at minimum on the NVIDIA T4 GPU already used for evaluation) for several architectures, with a breakdown of time spent on hashing, merging, and the reduced convolution. This is essential to validate the practical utility of the method.
2. Add a simple error bound or discussion of when the approximation in Eq. (1) degrades (e.g., as a function of within-bucket channel variance). Even an empirical analysis (plot error vs. within-bucket cosine similarity) would be informative.
3. Temper the "outperforms all other methods" claim on VGG19-BN by noting the different baselines and larger accuracy drop, or normalize the comparison to a common baseline.
4. Report average bucket sizes / hash collision statistics across layers to help readers understand where compression is actually happening.

## Score and Decision

The paper presents a genuinely novel idea with a clean niche (data-free, training-free pruning) and provides convincing empirical evidence across multiple architectures and two datasets. The main limitation — absence of wall-clock timing — is significant because the method's overhead could erode the practical benefits, but it does not invalidate the FLOPs savings demonstrated. The paper is well-written, transparent about its limitations, and makes a clear contribution to the pruning literature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>