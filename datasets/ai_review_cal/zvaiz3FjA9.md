- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper proposes CosNet, a ConvNet macro design built on parallel columnar convolutions with input replication, minimized $1\times1$ layers, and batched processing. The architecture is systematically derived from five explicit design sub-objectives (depth reduction, controlled parameter growth, low branching, high computational density, and uniform primitive operations). CosNet aims to produce concise models with favorable trade-offs across accuracy, depth, parameters, FLOPs, and latency, rivaling both simple ConvNets and advanced Transformer designs.

## Strengths

1. **Clear, well-motivated architecture design with explicit sub-objectives.** The paper derives CosNet from five concrete sub-objectives (Sec. 1), and each design element is explicitly linked to one or more of these objectives. For example, minimizing $1\times1$ convolutions is shown to achieve a **45% depth reduction** relative to a ResNet-like block at the same receptive field (Sec. 3.1, line 112–113). This systematic design rationale is a genuine strength — the architecture is not a bag of tricks but follows a coherent logic.

2. **Controlled parameter growth through parallel columnar convolutions.** The design restricts parameter growth when scaling by using $M$ columns with few kernels $N$. The paper provides concrete evidence: CosNet-B2 has 73% fewer parameters than RepVGG-B3 at similar depth while achieving higher accuracy (Sec. 4.2). This clearly demonstrates the parameter-control benefit over prior work.

3. **Batched processing yields effectively uni-branched architecture.** By combining parallel convolutions into batched operations, CosNet becomes uni-branched during both training and inference (Sec. 3.4–3.5). This is a practical advantage over multi-branch designs like RepVGG (which has high training complexity) and is supported by training walltime comparisons against VanillaNet.

4. **More controlled downstream experiment (DN-DETR).** The application of CosNet as a backbone in DN-DETR (Sec. 4.5) uses the same training settings for both CosNet and ResNet-50 baselines, providing a fairer comparison that shows improved inference speed and average precision. This is the most credible piece of controlled evidence in the paper.

5. **Simple instantiation with only three hyperparameters ($M, N, l$).** The design space is easy to navigate (Sec. 3.7), making the architecture practical for adoption and further exploration.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparisons undermine accuracy and latency claims.** The paper compares CosNet against powerful baselines (Swin-T, ConvNeXt, DeiT, EfficientViT, etc.) using published results, without retraining them under a common experimental pipeline. The paper states training is "consistent with recent VanillaNet" (line 182), which uses a different recipe than, e.g., ConvNeXt (300 epochs with heavy augmentation) or DeiT (distillation). While architectural comparisons (depth, parameters, FLOPs) are unaffected by training protocol, **accuracy and latency comparisons are**. The paper does not specify the GPU hardware, batch size, framework, or input resolution used for latency measurements, making it impossible to assess whether the reported speed advantages are meaningful. Notably, the DN-DETR experiment (Sec. 4.5) *does* provide a controlled comparison and supports the method's value — expanding this controlled evaluation paradigm to the primary ImageNet comparisons would substantially strengthen the paper. As written, the reader cannot distinguish architecture-driven improvements from training-recipe-driven ones.

2. **No ablation study in the main paper body.** The paper repeatedly defers ablations to the supplement (e.g., lines 118, 130, 145, 163). While the supplement presumably exists in the original submission, the main paper provides no isolation of design choices (number of columns $M$, number of kernels $N$, presence of projections, fusion strategy, effect of $1\times1$ minimization). For an architecture paper where the contribution is the specific design, the absence of even a brief ablation table in the main body is a significant omission — it prevents the reader from assessing which components drive the reported improvements.

### Minor

3. **Computational density and memory access cost are motivated but never measured.** Sub-objectives 4 and 5 in the introduction (high computational density, uniform primitive operations) are used to motivate the architecture, and batched processing is claimed to improve GPU utilization and reduce memory access cost (Sec. 3.4). However, no experiments measure GPU utilization, MAC, or computational density. These remain rhetorical claims.

4. **No statistical significance or variance reported.** The paper reports single-run accuracy numbers. ImageNet training runs can vary by 0.1–0.2%, and latency measurements are inherently noisy. Reporting mean and standard deviation over multiple runs (at least 3 seeds) would improve reliability.

5. **The claimed advantage of input replication after squeeze vs. before (as in ResNeXt) is not conclusively argued.** The paper states this is "one of the reasons that despite infrequent fusion... CosNet still performs better" (line 130), but the only supporting evidence is deferred to the supplement. A brief quantitative demonstration in the main paper would strengthen this claim.

### Trivial
None.

## Nice-to-Haves
- A controlled small-scale ImageNet experiment (e.g., 100-epoch training with identical augmentation for CosNet and a subset of key baselines) would greatly strengthen the comparative evidence.
- Profiling GPU utilization or MAC would validate the claimed computational density advantages.
- Specifying the exact GPU hardware, CUDA version, batch size, and input resolution used for latency benchmarks would improve reproducibility.

## Removed Points

- **"Table imagenet_300 not visible in parsed text"** — This is a parser artifact; the table exists in the original submission. Not a valid weakness.
- **"No mobile or edge comparison"** — The paper explicitly scopes out the mobile regime ("we do not aim for a mobile regime in this paper," line 213). Scope creep.
- **"Code and model definitions not provided"** — Reproducibility concern about practical artifacts not required in a conference submission. Weakened per instructions about trivial reproducibility nitpicks.
- **"The supplement is not included here"** — Supplements are stripped by the parser; they exist in the original submission. Removed per hard rules.
- **"The method incrementally combines known ideas"** — This is a general characterization, not a specific evidenced weakness. The paper clearly differentiates its design from prior work (Inception, ResNeXt, group convolutions) and provides quantitative comparisons.
- **"Key difference from ResNeXt may be a minor variation"** — Speculative opinion, not a verifiable weakness.
- **"Grad-CAM visualization is not strong evidence"** — Accepted as qualitative and supplementary; the paper does not over-claim for it. Not a substantive weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's architectural coherence and the strength of its experimental validation, but do not introduce new technical observations about the method itself.

## Suggestions

1. **Re-run at least 2–3 key baselines (ResNet-50, ConvNeXt-T, Swin-T) under the same training pipeline** used for CosNet, or alternatively train CosNet variants under each baseline's original recipe. This would directly address the most important weakness and transform the comparison from "plausible but unverified" to convincing.

2. **Include a main-paper ablation table** showing the effect of varying $M$, $N$, projections, and the $1\times1$ minimization. Even a compact table with 6–8 rows would substantially validate the design rationale.

3. **Specify the hardware and measurement protocol** for all latency/throughput experiments (GPU model, CUDA version, batch size, input resolution, framework). Report mean and std over at least 3 runs.

4. **Consider a controlled comparison at a smaller scale** (e.g., CIFAR-100 or a 100-class ImageNet subset with fixed training recipe) to provide direct evidence of the architecture's benefit independent of training recipe.
