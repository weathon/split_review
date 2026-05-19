- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5
Now I have a thorough understanding of the paper and can verify all claims. Let me produce the final consolidated review.

## Summary

This paper investigates whether the locality inductive bias is necessary for vision Transformers. The authors propose Pixel Transformer (PiT), which treats individual pixels as tokens with learned position embeddings—completely removing locality bias from the architecture. Across three diverse tasks (supervised classification on CIFAR-100 and low-resolution ImageNet, self-supervised MAE pre-training on CIFAR-100, and class-conditional image generation with DiT on ImageNet latent tokens), PiT consistently matches or outperforms patch-based ViT baselines. The paper also contributes trend analyses that disentangle the effects of input size vs. sequence length, and ablation studies isolating patchification as the dominant source of locality in ViT.

## Strengths

1. **Systematic demonstration across three diverse tasks.** PiT outperforms comparable ViT baselines in supervised classification (CIFAR-100: 86.4% vs. 83.7% for PiT-S vs. ViT-S/2; ImageNet at 28×28: 74.1% vs. 72.9%), self-supervised MAE pre-training (CIFAR-100: 87.7% vs. 87.4%), and image generation (DiT on 32×32 latent tokens: FID 4.05 vs. 4.16). This breadth across discriminative and generative settings, raw pixels and latent representations, and standard vs. conditioned Transformer architectures provides converging evidence that the finding is not a fluke of one particular setup.

2. **The two-trend analysis (Figure 2) is a genuinely insightful analytical contribution.** By separately fixing sequence length (varying input size) and fixing input size (varying patch size), the paper reveals an important nuance that much prior work has overlooked: under fixed sequence length, PiT is the *worst* performer (because input size collapses), while under fixed input size, decreasing patch size monotonically improves accuracy with PiT as the endpoint. This clarifies that the success of pixel-level modeling is driven by increased resolution/token count, not by locality itself—a non-obvious and useful distinction for the community.

3. **Rigorous ablation isolating patchification as the dominant locality bias in ViT.** Section 6 systematically corrupts position embeddings and patchification separately. Removing position embeddings entirely drops accuracy by only 1.5% (82.8→81.2 on ImageNet), whereas aggressive pixel shuffling (T=25K swaps) drops accuracy by 25.2% (82.8→57.6). This cleanly demonstrates that patchification carries the bulk of the locality inductive bias in standard ViT, justifying the paper's focus on removing it entirely.

4. **Generalization to a different architecture and latent space.** The DiT experiment (Case Study #3) operates on 32×32 VQGAN latent tokens using a modulation-based architecture different from vanilla ViT. PiT-L still outperforms DiT-L/2 on 3 of 5 generation metrics and ties on the remaining 2. This shows the finding is not an artifact of a specific architecture design or input representation.

## Weaknesses

### Fatal
None.

### Major

1. **The paper's central claim ("locality is not a necessary inductive bias for vision") is broader than the evidence supports.** The supervised ImageNet experiments use 28×28 inputs (far from the standard 224×224 where vision architectures are deployed). The paper explicitly acknowledges this limitation ("Due to computation constraints"), and the conclusion states the "practicality and coverage of our current demonstrations remains limited." However, the title, abstract, and introduction make an unqualified claim that "locality is *not* a necessary inductive bias for model design"—without specifying the regime in which this has been demonstrated. At high resolutions with practical token counts (standard 224×224 inputs), PiT would require 50,176 tokens and the quadratic cost of self-attention becomes prohibitive; the paper does not test whether the claim holds in this regime. The fixed-sequence-length trend (Figure 2a) even suggests that when input size is forced down to keep tokens constant, PiT becomes the *worst* performer—a finding that further bounds the scope of the claim. A more defensible framing would be: "locality is not necessary when the input is small enough that individual pixels can be modeled as tokens at manageable sequence lengths."

### Minor

2. **The confound between locality removal and increased sequence length is not fully disentangled.** Under fixed input size (Figure 2b), decreasing patch size simultaneously (a) removes locality bias and (b) increases the number of tokens. The paper correctly notes that both change together, but does not include a control experiment that isolates locality at a fixed token count—for example, a ViT with 1×1 patches that uses local-window self-attention (restoring locality at the same token count). Such an experiment would determine whether the gains come from removing locality or simply from having more fine-grained tokens. Without it, the paper's claim rests on the observation that the *combined* effect (more tokens + no locality) is positive, which is interesting but less conclusive than the title suggests. The trend analyses mitigate this concern but do not resolve it.

3. **Several key comparisons show thin margins without variance estimates.** The MAE CIFAR-100 comparison (87.7% vs. 87.4%, +0.3%) and the ImageNet-B comparison (76.1% vs. 75.7%, +0.4%) have margins small enough that they may not be statistically significant, yet no standard deviations, confidence intervals, or multiple-run averages are reported. The DiT FID gap (4.05 vs. 4.16, -0.11) is also modest. The larger-margin comparisons (CIFAR-100: +1.5–2.7%, ImageNet-S: +1.2%) are more convincing, but the overall pattern would be strengthened by reporting variance.

4. **No quantitative analysis of computational cost.** The paper repeatedly notes that PiT is computationally expensive but never quantifies the cost relative to baselines. Reporting FLOPs, memory usage, and training time for each comparison would allow readers to assess the accuracy–efficiency trade-off and evaluate whether the improvements justify the additional cost. This is particularly relevant given the paper's stated goal of informing future architecture design.

### Trivial
None.

## Nice-to-Haves

- A control experiment that keeps token count constant while varying locality (e.g., local-window self-attention with 1×1 patches vs. PiT's global self-attention).
- Reporting standard deviations or confidence intervals for the key comparisons with thin margins.
- A cost–benefit analysis quantifying FLOPs, memory, and training time for PiT vs. ViT at each scale.
- MAE mask-ratio ablations for pixel-level tokens (the 75% ratio is taken from ViT without justification).
- A small-scale proof-of-concept at a more standard resolution (e.g., 128×128 crops with PiT-S trained for a limited number of epochs).

## Removed Points

- *"DiT baseline was retrained with a different recipe, making comparisons unfair"* — The paper is fully transparent about the recipe change and shows the no-guidance FID of 8.90 (DiT-L/2) vs. the original 10.67 (DiT-XL/2). The main comparison uses the same recipe for both DiT-L/2 and PiT-L, so the comparison is fair. **Removed** because the criticism is factually addressed by the paper.

- *"Permutation experiments undermine the main claim"* — The paper itself states: "translation equivariance remains important and should not be disregarded." The paper never claims that *no* inductive biases are needed—only that *locality* specifically is not necessary. **Removed** because the paper already makes this point explicitly.

- *"ViT-B/2 baseline on CIFAR-100 (72.6%) is poorly optimized"* — The paper acknowledges this citation comes from a different paper with a different setup, while all head-to-head comparisons (ViT-T vs. PiT-T, ViT-S vs. PiT-S) use models trained with the same recipe by the authors. **Removed** because the main comparisons are fair.

- *"iGPT discussion understates its relevance"* — The paper discusses iGPT in two separate paragraphs, noting its locality-free design and historical context. **Removed** because the discussion is adequate.

- *"Missing related works"* — Cannot verify without external sources. **Removed** per instructions.

- *Formatting/style nitpicks, typo claims, and requests for appendix content* — These are parser artifacts or scope-creep. **Removed** per instructions.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the permutation experiments suggest translation equivariance (rather than locality) is the more important inductive bias is already discussed explicitly in Section 6 of the paper.

## Suggestions

1. Revise the title, abstract, and introduction to scope the claim more precisely: "locality is not necessary under small input sizes where sufficient tokens are affordable" rather than the unqualified "locality is not a necessary inductive bias for vision."
2. Add a control experiment using local-window self-attention on 1×1 patches to isolate the effect of locality removal from sequence length increase.
3. Report standard deviations or confidence intervals for the thin-margin comparisons (MAE and ImageNet-B).
4. Include a table quantifying FLOPs, memory, and training time for each model configuration tested.
