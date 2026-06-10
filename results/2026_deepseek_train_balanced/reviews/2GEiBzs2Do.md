## Summary

This paper proposes SFCNN, a CNN architecture that uses only stacked 3×3 depthwise convolutions in a thin-and-deep design. The key ideas are: (1) favoring depth over width under fixed FLOPs to enlarge the receptive field through more small convolutions; (2) a two-DWConv bottleneck; and (3) a Global Sigmoid Linear Unit (GSiLU = x × σ(GAP(x))) as a parameter-free channel gating mechanism. Experiments on ImageNet-1K classification, COCO instance segmentation, and ADE20K semantic segmentation show competitive accuracy with favorable FLOPs and deployment throughput across four hardware metrics.

## Strengths

- **Comprehensive four-metric hardware evaluation (Figure 1):** The paper benchmarks SFCNN against large-kernel CNNs across FLOPs, PyTorch GPU throughput, TensorRT latency, and iPhone Core ML latency. This goes well beyond the typical FLOPs-only or single-metric comparison and concretely demonstrates that the small-kernel design yields real deployment-speed advantages, not just theoretical FLOP reductions. SFCNN sits at or near the Pareto frontier on all four metrics.

- **Controlled depth-vs-width ablation with receptive field quantification (Tables 2 and 9):** The paper designs models with identical FLOPs but systematically varying depth vs. width. Table 2 shows the deepest variant achieves a receptive field exceeding the 224×224 input resolution by stage two, while shallower models of similar FLOPs remain local. Table 9 shows deeper models achieve better accuracy up to a non-monotonic optimum. This controlled experiment directly supports the central design thesis — that stacking more 3×3 DWConvs under fixed compute can substitute for large kernels.

- **Consistent positive results across three tasks (Tables 3, 5, 6):** SFCNN achieves competitive or better accuracy than large-kernel CNNs and ViTs on ImageNet-1K (SFCNN-B 84.6% vs MogaNet-B 84.3%, 8.7G vs 9.9G FLOPs), COCO (Mask R-CNN + SFCNN-B AP^b 49.3, 334G FLOPs vs Swin-S 48.5, 359G), and ADE20K (SFCNN-T 48.4 MS mIoU vs Swin-T 45.8). These cross-task results substantiate that the architecture's efficiency advantage transfers beyond classification.

- **GSiLU ablation against SE and other activations (Table 8):** The paper compares GSiLU against SiLU, Swish, ReLU, and the SE module. GSiLU adds +0.2–0.3% top-1 over SiLU with zero additional parameters, while SE performs slightly better but adds parameters. The ablation cleanly isolates the contribution of parameter-free global pooling conditioning versus parametric channel attention.

- **Effective receptive field visualization (Figure 3):** The ERF visualization shows SFCNN captures long-range dependencies alongside fine local details, while ConvNeXt captures primarily local information and other large-kernel methods introduce global noise. This provides visual support for the claim that stacked 3×3 depthwise convolutions can achieve the receptive-field benefits of large kernels without their drawbacks.

## Weaknesses

### Fatal

None.

### Major

- **GSiLU is overclaimed as a "novel activation function" (Section 3.5):** GSiLU = x × σ(GAP(x)) is a channel-wise gating mechanism where every spatial position in a channel is scaled by the same scalar from global average pooling. This is structurally different from element-wise activation functions like SiLU (x × σ(x)), where each position gates itself independently. The paper acknowledges the similarity to Squeeze-and-Excitation (line 251) and Table 8 shows SE actually performs slightly better, with the defense being only "it is a non-parametric module." Calling GSiLU a "novel activation function" overstates the contribution; it is more accurately described as a parameter-free channel gating mechanism. The empirical result is legitimate, but the framing inflates the novelty.

- **Classification improvements are modest and reported without any measure of variance (Section 4.1):** The headline classification gains are 0.3–0.4% (SFCNN-N vs SMT-T: 82.6% vs 82.2%; SFCNN-B vs MogaNet-B: 84.6% vs 84.3%). These are single-run results. On ImageNet-1K with 300-epoch training, run-to-run variance for models of this capacity can reach 0.2–0.4% from stochasticity in augmentation, dropout, and initialization. Without multiple seeds or confidence intervals, the claimed advantages over strong baselines like MogaNet and SMT cannot be distinguished from noise. The dense prediction results (COCO +0.8 AP^b, ADE20K +2.6 mIoU) are larger and less vulnerable to this criticism, but the classification evidence specifically would be strengthened by multi-run reporting.

### Minor

- **Speed benchmark methodology is underspecified (Figure 1):** The paper reports throughput, TensorRT latency, and iPhone latency but omits critical methodological details: batch size, numerical precision (FP32/FP16/AMP), number of warmup and measurement iterations, whether torch.compile or graph optimizations were used, and any CPU/GPU pinning settings. These details are essential for reproducibility of deployment-speed claims, which are a central selling point.

- **No limitations or failure case discussion (Section 5):** The conclusion contains no self-critical reflection on the method's limitations, failure modes, or directions for future work. Every architecture has trade-offs (e.g., does the thin-and-deep design hurt training stability? are there tasks where the narrower channels become a bottleneck?), and the absence of any such discussion is a quality gap.

- **No incremental ablation from a ConvNeXt-style baseline:** The paper ablates DWConv count, GSiLU, and depth-vs-width separately, but does not start from a ConvNeXt-like baseline (single 7×7 DWConv, SiLU, standard depth ratio) and add each SFCNN component incrementally. Such an ablation would be the most informative experiment for attributing the gains to specific design choices.

### Trivial

None.

## Nice-to-Haves

- Reporting ImageNet-1K results with at least 3 random seeds (mean ± std) for the primary comparisons.
- Adding speed benchmark details (batch size, precision, measurement protocol) to the main text or appendix.
- Including a limitations paragraph in the conclusion.
- An incremental ablation from ConvNeXt-style baseline to SFCNN would strengthen attribution of gains.

## Removed Points

These points from the reviews are flagged to be removed — treat them with caution:

- **"Thin-and-deep principle contradicted by own ablation":** The paper honestly reports a non-monotonic relationship (line 326: "the deepest model has a much thinner channel width, which will lose information and even get a -0.2% performance"). This is a nuanced finding, not a contradiction. **Removed as strawman.**

- **"Missing comparison with ConvNeXt":** ConvNeXt IS compared in Figure 1 and cited throughout the paper as the primary baseline. **Removed as factually incorrect.**

- **"ViTs hardware limitations claim lacks citation":** The paper cites Zhang et al. (2023) at line 163. **Removed as factually incorrect.**

- **"Theoretical vs effective RF gap not addressed":** The paper provides ERF visualizations in Figure 3 to directly address this. **Removed as factually incorrect.**

- **"Well-known fact about two 3×3 = one 5×5 presented as contribution":** This is presented as background knowledge cited from Zhang et al. (2023), not as a paper contribution. **Removed as strawman.**

- **"Comparison set in Figure 1 is limited to large-kernel CNNs":** The paper explicitly scopes this comparison: "compared to other large-kernel CNNs" (line 85). Broader comparisons are in Table 3. **Removed as scope creep.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe GSiLU as a "parameter-free channel gating mechanism" or "global attention module" rather than a "novel activation function." The empirical value is in its parameter efficiency vs. SE, not in being a new activation family.
2. Report ImageNet-1K results with standard deviation across at least 3 seeds for the main comparisons. This is especially important given the 0.3–0.4% margins against strong baselines.
3. Provide speed benchmark methodology details: batch size, precision mode (FP16/FP32/AMP), number of warmup/measurement iterations, and whether any graph compilation was used.
4. Add an explicit limitations paragraph to the conclusion discussing when / why the thin-and-deep design might underperform.
5. Consider adding an ablation experiment that starts from a ConvNeXt-T baseline and incrementally adds each SFCNN component (dual-DWConv bottleneck → GSiLU → thin-and-deep reallocation) to directly attribute the accuracy gains.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>