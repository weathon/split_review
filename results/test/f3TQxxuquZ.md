Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me synthesize the final review.

---

## Summary

This paper addresses the computational inefficiency of Prompt-based Continual Learning (PCL), which requires two separate ViT forward passes (query ViT + backbone ViT). The authors propose **OS-Prompt**, a one-stage framework that uses intermediate layer token embeddings as prompt queries, eliminating the query ViT and reducing GFLOPs by ~50%. They further introduce **OS-Prompt++** with a Query-Pool Regularization (QR) loss that recovers the small accuracy loss without adding inference overhead, outperforming prior SOTA CodaPrompt by ~1.4% while maintaining 50.1% inference GFLOPs. Experiments on CIFAR-100, ImageNet-R, and DomainNet with comprehensive ablations support the claims.

## Strengths

1. **Significant and well-documented computational savings**: The paper achieves ~50% inference GFLOP reduction (Table 2: 17.6 vs 35.1 GFLOPs) and ~33% training GFLOP reduction for OS-Prompt. OS-Prompt++ maintains the same 50.1% inference savings while surpassing prior SOTA accuracy (e.g., 77.07 vs 76.51 on ImageNet-R Task-5, Table 1). The latency measurements (Figure 4) confirm these savings translate to real speedups across GPU setups.

2. **Empirically motivated design**: The stability analysis (Figure 2, Section 4.1) shows early-layer (1–5) token embeddings exhibit small feature distances (≤0.1) across sequential tasks, providing a principled basis for using intermediate embeddings as prompt queries. While this analysis is conducted under the two-stage CodaPrompt setting, it motivates the design, and the strong final results validate the approach.

3. **QR loss recovers accuracy at zero inference cost**: The QR loss (Eq. 4–5) is applied only during training, yet OS-Prompt++ surpasses CodaPrompt across multiple benchmarks while retaining the same 50.1% inference GFLOPs. This cleanly decouples training-time regularization from inference efficiency.

4. **Generality across prompt formation strategies**: Table 7 shows OS-Prompt integrated with L2P and DualPrompt also outperforms their two-stage counterparts (e.g., OS-Prompt (L2P) 73.43 vs Deep L2P 71.66 on Task-10), demonstrating the one-stage idea benefits multiple PCL frameworks.

5. **Comprehensive ablations**: The paper systematically ablates QR loss components (Table 5), hyperparameter sensitivity (Table 6), prompt count/length (Figure 5), and reference ViT depth trade-offs (Figure 6), providing strong empirical support for design choices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Stability analysis conducted under two-stage setting, not one-stage.** The motivating experiment (Figure 2) measures layer-wise feature distances *under CodaPrompt* (a frozen query ViT), not under the proposed OS-Prompt where intermediate embeddings are affected by prompts applied at earlier layers. The paper acknowledges this concern (Section 4.1: "token embeddings in the backbone ViT continually change as prompt tokens are updated") and the strong empirical results mitigate it, but direct evidence that the query embeddings themselves remain stable in the one-stage setting would close this logical gap more convincingly.

2. **Wall-clock training time not reported.** The paper provides GFLOPs and inference latency, but does not report actual training time. Given that the computational cost framing is a central contribution, reporting training wall-clock time (even for one configuration) would strengthen the practical claims, especially since OS-Prompt++ has identical training GFLOPs to prior methods but uses a reference ViT forward pass differently (Table 2 shows 100% training GFLOPs).

3. **QR loss evaluated only with soft-matching prompt formation.** The QR loss design (cosine similarity + softmax) is tailored to CodaPrompt's soft weighted-sum prompt formation. Its applicability to hard top-k selection methods (L2P, DualPrompt) is not explored; Table 7 shows OS-Prompt works with those methods but *without* QR loss. The paper briefly discusses this (Section 5.6) but does not attempt to adapt QR loss to hard matching, leaving an open question about its generality.

### Trivial
- None.

## Nice-to-Haves

- A brief note on the activation memory footprint of the reference ViT during OS-Prompt++ training (to address resource-constrained deployment considerations).
- A sensitivity analysis of how much query drift (cosine distance) is tolerable before accuracy degrades, to complement the stability analysis in Figure 2.

## Removed Points

- **"Abstract training cost claim is potentially misleading" (Harsh Critic Issue 2):** Removed because the abstract is factually accurate. It states the base one-stage design reduces *both* training and inference cost by ~50%, and then separately states that with QR loss, the approach maintains *inference* reduction and outperforms prior methods. The paper body (Table 2, Section 5.3) clearly distinguishes the two variants' training costs. A "casual reader could be confused" is speculation about reader interpretation, not a factual error in the paper.

- **"Stability analysis uses cosine distance; 0.1 distance could cause reordering":** This is a speculative concern without evidence that reordering actually occurs or harms accuracy. The paper's strong empirical results already demonstrate the approach works.

- **"Paper claims SOTA but only compares to methods up to 2023":** The hard rules forbid flagging missing related works because we cannot confirm their existence.

- **"The reference ViT is the same frozen query ViT used in prior methods":** This was noted as an asset by the critic, not a weakness. It does not belong in weaknesses.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that intermediate layer embeddings remain sufficiently stable across continual learning stages to serve as prompt queries — is clearly articulated and validated. The QR loss that aligns query-pool similarity patterns between intermediate and final layer embeddings is a clean technical contribution.

## Suggestions

1. **Add stability measurements for the one-stage setting itself.** Repeat the experiment from Figure 2 but with an OS-Prompt model: measure how the intermediate CLS token embeddings (used as queries at layers 1–5) drift between task 1 and later tasks. This would directly validate the central assumption.

2. **Report wall-clock training time** for OS-Prompt, OS-Prompt++, and CodaPrompt on at least one benchmark, alongside the GFLOPs and latency data.

3. **Sharpen the abstract's distinction between variants** by naming OS-Prompt and OS-Prompt++ explicitly (e.g., "our one-stage framework (OS-Prompt) achieves ~50% cost reduction for both training and inference; with our QR loss (OS-Prompt++), it maintains the inference reduction and outperforms prior methods"). The current version is accurate but could be clearer at a skim.

4. **Highlight the reference layer trade-off (Figure 6) as a practical recommendation.** Using layer 8 as the reference (vs. the final layer) nearly matches accuracy while reducing training GFLOPs — this is a useful design choice that could be called out more explicitly.

## Score and Decision

The paper presents a simple, well-motivated improvement to prompt-based continual learning with computational savings clearly validated across multiple benchmarks. The experiments are thorough, the ablations are comprehensive, and the claims are well-supported. The minor weaknesses (stability analysis gap, missing training wall-clock time, QR loss generality) do not undermine the core contribution. This is a solid incremental contribution that will be useful to the continual learning community.

**Score: 7.0** — A technically sound paper with a clear contribution, thorough evaluation, and no fatal or major flaws.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>