- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 6, 8, 5
I have all the information I need. Let me now write the consolidated review.

## Summary

This paper proposes Perceptual Group Tokenizer (PGT), a vision backbone built entirely around iterative perceptual grouping operations rather than self-attention or convolution. The model uses learned group tokens to iteratively bind and refine patch representations via cross-attention-style grouping, trained with a DINO-style self-supervised loss. On ImageNet-1K linear probe evaluation, PGT achieves 80.3% top-1 accuracy, competitive with DINO ViT-B/8 (80.1%), while offering unique properties: adaptive computation (varying group token count at test time without retraining) and interpretable multi-head grouping visualizations.

## Strengths

1. **Competitive self-supervised performance from a grouping-only architecture**: PGT achieves 80.3% top-1 accuracy on ImageNet-1K linear probe (Table 1), matching DINO ViT-B/8 (80.1%) and outperforming DINO ViT-B/16 (78.2%). This is the strongest evidence to date that a backbone built purely from grouping operations can rival standard transformer and ConvNet architectures at scale, which is a genuinely novel result.

2. **Adaptive computation is well-documented and empirically robust**: Table 4 (Table \ref{tab:ood}) provides a comprehensive grid of training/inference token count combinations, showing that models trained with M group tokens can productively use a different number N at inference. Notably, using *more* tokens at inference than training (e.g., 64→128: 61.7→62.6%) improves accuracy despite being out-of-distribution, and the model degrades gracefully even at 12.5% of training tokens (79.7%→72.1%). This property genuinely distinguishes PGT from standard ViT.

3. **Interpretable multi-head grouping**: Figure 3 shows attention maps where different heads capture distinct semantic information (color, spatial location, texture) and group tokens separate object parts (apple, jar, handle; camel, human, legs). This goes beyond the single-[CLS]-token interpretability of DINO ViT and demonstrates that the grouping mechanism yields structured, part-level representations.

4. **Multi-head grouping ablation is clean and informative**: Section 4.2 shows a controlled comparison (6 heads × 128 tokens vs. 1 head × 768 tokens, matched total capacity) where multi-head improves accuracy from 62.2% to 66.3% (+4.1%), isolating the benefit of multiple grouping perspectives.

5. **Memory efficiency under fine-grained patches**: Table \ref{tab:mem} shows PGT-B uses only 4.6% of ViT-B's peak memory at the same 4×4 patch resolution, demonstrating a real advantage for high-resolution processing.

## Weaknesses

### Fatal
None.

### Major

1. **The headline comparison confounds architecture with token budget and compute.** PGT uses 4×4 patches (56×56 = 3136 tokens) while the main ViT comparison is ViT-B/8 with 8×8 patches (28×28 = 784 tokens). PGT therefore processes 4× more input tokens. A cleaner comparison would either (a) evaluate PGT at coarser patch sizes (e.g., 8×8 or 16×16) to see if the grouping mechanism itself — not just the extra input detail — drives performance, or (b) compare against a ViT variant that can handle 4×4 patches efficiently (e.g., Swin with window attention). Without this, readers cannot fully attribute the results to the grouping principle versus the benefit of finer-grained inputs. That said, this is not a fatal flaw because PGT's ability to handle 4×4 patches efficiently is itself an architectural advantage — this is more about evaluation completeness than invalidity.

2. **No FLOPs or throughput comparison.** The paper reports peak memory but omits FLOPs and wall-clock speed, which are the primary practical constraints. PGT's iterative grouping (K=3 iterations per layer × 30 layers) plus cross-attention at 3136 input tokens is not obviously cheaper than ViT-B/8's self-attention at 784 tokens. A FLOPs table comparing PGT and ViT at matched task performance would be critical for assessing practical value, and its absence weakens the efficiency claims.

3. **No direct comparison to the closest related architectures (Slot Attention, Perceiver) under the same self-supervised pipeline.** The paper cites both Slot Attention (locatello2020object) and Perceiver (jaegle2021perceiver) in related work but does not compare against them experimentally. Since PGT's grouping operation is structurally a cross-attention mechanism with learned latent tokens — the same core idea as Perceiver IO and Slot Attention with iterative refinement — a head-to-head comparison under the DINO loss (with matched token budgets) would be the strongest way to demonstrate that PGT's specific design choices (multi-head grouping, distribution sampling, implicit differentiation) add value over existing cross-attention architectures. Without it, the novelty claim is partially speculative.

### Minor

1. **The adaptive computation mechanism is not analyzed.** The paper shows empirically that varying the number of group tokens at inference works, but does not investigate *why*. Is it simply a capacity effect (more clusters = finer partitioning)? Does the initialization distribution matter critically? Can this property be exploited for cost-accuracy tradeoffs in practice? The paper would be strengthened by even a simple analysis (e.g., does the assignment entropy change meaningfully with more tokens?).

2. **No reported variance or confidence intervals.** All results (ImageNet linear probe, ADE20k mIoU) are reported as single numbers. While single-run evaluation is common for large-scale benchmarks, the margin over ViT-B/8 is tiny (0.2–0.3%), so variance information would help assess significance.

3. **Ablation study uses a tiny model (10M params, 6 layers) whose findings may not transfer to the main model (70–115M, 30 layers).** The paper acknowledges this implicitly but key decisions (e.g., 3 grouping iterations, 6 heads, flat token layout) are validated only on the tiny model. An iteration-count ablation or head-count ablation on the main model would increase confidence.

4. **Minor overstatement in framing.** The phrase "establishing a new milestone for this paradigm" (abstract) is hyperbolic given that the best result (80.3%) uses 115M params with flow-based initialization and 1024 inference tokens, exceeding ViT-B/8's 85M params and 784 tokens. The Gaussian variant at 70M params matches ViT-B/8 at 80.1%, which is competitive but not a "milestone."

### Trivial
None.

## Nice-to-Haves

- A FLOPs comparison table (as noted above).
- Quantitative evaluation of grouping interpretability (e.g., against part segmentation masks on PASCAL-Parts).
- Ablation of the number of grouping iterations K on the main model.
- Comparison with a Perceiver variant under the DINO loss.

## Removed Points

*(These points were flagged by reviewers but are removed from the main assessment for the reasons given below. Treat with caution.)*

- **"The memory comparison is a strawman — no one would use ViT at 4×4 patches."** — REMOVED. The comparison is valid: it demonstrates PGT's advantage in handling fine-grained patches that ViT cannot practically process. This is a genuine strength of PGT, not a flaw in the evaluation. The paper is showing that grouping operations are more memory-efficient than self-attention at the *same* resolution, which is a fair apples-to-apples comparison at the operation level.

- **"The method is not free of self-attention; it is cross-attention."** — REMOVED. The paper never claims the method is "free of attention." It claims it is "entirely driven by grouping operations" and explicitly discusses the relationship to self-attention in Section 3.4: "if each input token is solely assigned to a different group token ... the perceptual grouping layer is equivalent to one self attention layer." The paper is transparent about the connection. The novelty lies in reframing and extending attention-as-grouping with multi-head iterative refinement, distribution sampling, and implicit differentiation, not in claiming attention-free computation.

- **"The characterization of Perceiver is inaccurate — Perceiver does refine latents iteratively."** — REMOVED. The paper says Perceiver "only uses cross attention without refining the *patch feature space*" (emphasis added), which is correct. Perceiver uses cross-attention to project to latents, then refines latents — it never refines the *patch* features. The critic misread "patch feature space" as "latent space."

- **"Increasing ViT's number of attention heads at test time as a baseline for adaptive computation."** — REMOVED. This is not a meaningful baseline; increasing attention heads in ViT at inference changes the model's dimensionality in a way that typically breaks the architecture. The comparison is not analogous.

- **"The segmentation baseline citation (Zheng et al. 2021 SETR) is not a standard DINO reference."** — REMOVED. Zheng et al. is cited for the segmentation protocol, not for DINO. DINO + ViT-B/16 is the method. This is standard practice.

- **Pure style/format nitpicks and reproducibility complaints about unspecified hyperparameters.** — REMOVED per Hard Rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. **Add a controlled patch-size experiment.** Evaluate PGT with 8×8 or 16×16 patches (fewer input tokens) and compare to ViT at the same resolution. This would isolate the architecture's effect from the token-count effect and directly answer the main concern.

2. **Add FLOPs and throughput comparison** across PGT variants and ViT baselines at matched performance levels, not just matched patch sizes.

3. **Add a Perceiver/Slot Attention baseline** under the DINO training pipeline with comparable token budgets. This would substantiate the claim that PGT's specific design choices (multi-head, distribution sampling, implicit differentiation) outperform vanilla cross-attention architectures.

4. **Report variance** for at least the main ImageNet linear probe results (e.g., 3 seeds) to establish significance of the ~0.2% margin over ViT-B/8.

5. **Analyze the adaptive computation mechanism**: show whether the improvement from more test-time tokens is simply finer-grained clustering by measuring assignment entropy, or test whether training with the same high token count gives even better results (confirming the OOD generalization is genuine).
