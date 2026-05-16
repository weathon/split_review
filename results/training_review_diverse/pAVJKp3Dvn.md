## Summary

This paper proposes a differentiable framework for learning structured weight matrices in DNNs. It introduces the Generalized Block-Low-Rank (GBLR) format, which unifies low-rank, block-sparse, and block-low-rank matrices under a single representation, and the Gaussian-Dirichlet (Gaudi) frequency-domain parameterization that enables gradient-based learning of structural parameters (block width and location). A proximal-gradient algorithm with \(\ell_1\) regularization on block widths is used to jointly learn structure and content. Experiments on ViT, MLP-Mixer, and GPT-2 show better accuracy–FLOPs trade-offs compared to hand-designed structured matrix baselines.

## Strengths

- **Unified representation of existing structured matrix formats (Theorem 1, Theorem 2).** The paper proves that low-rank, block-sparse, and block-low-rank matrices are special cases of the GBLR format, and that interpolation between GBLR matrices remains within the format. This is a clean theoretical contribution that formalizes what prior work treated as separate categories.

- **Differentiable parameterization of structural parameters via the Gaudi mask (Theorem 3, Corollary 1).** The frequency-domain construction using Dirichlet kernels with Gaussian smoothing yields bounded and nonzero derivatives with respect to width and location, including at width zero. This solves the differentiability problem that prevents gradient-based learning of discrete boxcar masks, and is the paper's core technical innovation.

- **Strong empirical accuracy–complexity trade-offs on realistic architectures.** On ImageNet fine-tuning (Figure \ref{fig:imagenet-finetune-vit-b}), Gaudi-GBLR preserves accuracy at 30% of dense FLOPs where hand-designed LR and Monarch degrade more. On ImageNet training from scratch (Table \ref{tab:imagenet_from_scratch}), Gaudi-GBLR achieves 78.51% accuracy at 5.65 GFLOPs vs. dense ViT-Base's 78.57% at 17.2 GFLOPs — a 67% FLOP reduction with negligible accuracy loss.

- **Automatic per-layer budget allocation (Table \ref{tab:flops-by-type}).** The framework automatically allocates different FLOPs to different layer types (Query: 4.2K–67.6K; MLP-FC2: 349.4K–1,175.2K), and the visualization in Figure \ref{fig:mask-visualization} shows learned block patterns that concentrate in head-specific regions rather than forming simple BSP or BLR patterns.

- **No inference overhead.** Once structural parameters are learned, the Gaudi masks are discarded and cropped content vectors are used directly, so inference requires no extra computation beyond the structured MVP.

## Weaknesses

### Fatal
None.

### Major

- **The advantage of learned block patterns vs. per-layer budget allocation is not disentangled.** The baselines (LR, Monarch, Pixelfly) use fixed structural parameters across all layers, while Gaudi-GBLR learns per-layer widths and locations. The reported gains could partly (or largely) come from automatically allocating more budget to critical layers — an advantage that simpler layer-wise budget search (e.g., per-layer rank selection for LR) might also provide. The paper does not include a baseline that allocates budget per layer using existing formats, nor an ablation where Gaudi-GBLR's structural parameters are frozen to random values while content is learned. This makes it impossible to attribute the gains specifically to *learned block patterns* as opposed to *learned per-layer budget allocation*. This gap directly affects the paper's central interpretive claim.

- **Main experiments lack variance information.** No error bars, confidence intervals, or multi-run statistics are reported for any of the key results: ImageNet fine-tuning (Figure \ref{fig:imagenet-finetune-vit-b}), CIFAR-10/100 training from scratch (Figure \ref{fig:cifar-scratch}), or GPT-2 perplexity (Table \ref{tab:gpt2}). Given that the perplexity improvement over the dense baseline is only ~0.6% relative, single-run results are not sufficient to judge whether the improvement is meaningful or within noise.

- **ResNet experiment mentioned but results not reported.** Line 322 states "In addition to ViT, we also tested GBLR matrices on ResNet" with no accompanying results, analysis, or even a reference to a table or figure. This incomplete reporting weakens the paper's thoroughness.

### Minor

- **The algorithm's theoretical justification is imprecise.** Algorithm 1 applies AdamW updates followed by soft shrinkage on widths and calls this "proximal gradient descent." Standard proximal gradient requires a gradient step (without momentum/adaptive scaling) before the proximal operator; using AdamW first breaks the theoretical convergence guarantees. While this hybrid is common in practice and the paper demonstrates empirical results, the naming is misleading and no empirical convergence analysis (e.g., loss curves) is provided.

- **Choice of \(K=n\) is not justified or ablated.** The number of blocks is set equal to the matrix dimension \(n\) for all experiments. No sensitivity analysis with different \(K\) values is provided, and the rationale is not discussed. Since the training-time parameter count scales with \(K\), this choice has implications for memory and could affect the comparison.

- **Discretization of continuous structural parameters is not discussed.** The paper states that after training, Gaudi masks are "replaced by boxcar masks" for inference, but does not explain how the continuous learned widths and locations (in \([0,n]\)) are mapped to integer block boundaries, or whether this rounding affects accuracy.

- **GPT-2 perplexity result is presented without critical analysis.** Gaudi-GBLR achieves perplexity 19.24 vs. dense 19.36 at 43.7% FLOPs — a marginally better score at less than half the compute. The paper attributes this to the learned structure but does not discuss whether regularization from the structured parameterization or the \(\ell_1\) penalty could explain the improvement, nor does it compare against a dense model trained with analogous regularization.

- **No limitations or failure cases are discussed.** The paper reads as uniformly positive; a candid discussion of training-time memory overhead, sensitivity to the \(\lambda\) hyperparameter, or conditions under which the method underperforms would strengthen credibility.

### Trivial
- The connection between Theorem 1's conditions and experimental budget usage could be clarified.
- The paper could explicitly state that the gradient through the IFFT in the Gaudi mask is handled by autograd (this is routine, but worth noting).

## Nice-to-Haves

- A controlled baseline that allocates per-layer budget using existing formats (e.g., per-layer rank search for LR, per-layer block size for Monarch) would directly address the main interpretive ambiguity.
- An ablation with fixed random structural parameters (random widths/locations) would isolate the benefit of learning block patterns from the benefit of flexible budget allocation.
- Reporting standard deviations over 3 independent runs for the main results would substantially strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Gaudi-GBLR's perplexity improvement over dense is "highly suspicious" (Critical Issue 2).** This overstates the concern. Small improvements from structured compression are documented in the literature as a regularization effect. The real issue is lack of error bars, which is already captured in the Major section. The tone of "implausible" is unwarranted.

- **Criticism of "unfair baseline comparison" framed as a decisive flaw.** The comparison of learned (per-layer) structure vs. hand-designed (fixed) structure is appropriate for the paper's stated claim — that learning structure is better than hand-designing it. The comparison is not "unfair"; the missing piece is an ablation to disentangle *which aspect* of learning drives the gain, which is already noted as a Major weakness.

- **Criticism about gradient through IFFT.** Autograd handles complex-valued operations through the IFFT automatically; this is standard practice and not a substantive concern.

- **Pure formatting/style nitpicks and parser artifacts** (typos, missing appendix content that was stripped by the parser).

## Novel Insights

The reviews collectively highlight an important tension that the paper itself does not fully address: the GBLR framework conflates two distinct sources of improvement — (a) the ability to discover non-hand-designed block patterns and (b) the ability to allocate computational budget unevenly across layers. Most prior work on budget allocation (e.g., layer-wise low-rank compression) treats budget search as a separate bilevel or post-hoc procedure, while Gaudi-GBLR rolls both into a single end-to-end differentiable process. Whether this unification is necessary, or whether a two-stage pipeline (first allocate budgets per layer via simple search, then learn patterns within those budgets) would match the performance, is an open question that the paper's current evaluation cannot answer. This is a genuinely interesting empirical question that future work should address.

## Suggestions

1. **Add a layer-wise budget baseline.** For each layer, use the FLOPs budget that Gaudi-GBLR learned, but realize it with a simpler format (e.g., a single low-rank matrix of appropriate rank, or a Monarch matrix of appropriate block size). If Gaudi-GBLR still outperforms this baseline, the learned block patterns are genuinely beneficial.

2. **Add an ablation with frozen random structural parameters.** Train Gaudi-GBLR with the same total budget but random (non-learned) widths and locations. This isolates the value of learning locations and widths vs. simply having a flexible parametric family.

3. **Report error bars for all key results.** Even two or three seeds with min/max range would significantly improve credibility, especially for the perplexity result where the improvement over dense is within noise range.

4. **Include training loss curves** to demonstrate empirical convergence of the hybrid AdamW+shrinkage algorithm.

5. **Add a brief limitations paragraph** discussing training-time memory overhead (with \(K=n\), the content parameters use \(2n^2\) floats vs. \(n^2\) for dense), sensitivity to \(\lambda\), and the discretization step when transitioning from Gaudi masks to boxcar masks for inference.

## Score and Decision

The paper makes genuine contributions: the GBLR format provides a clean unified view of structured matrices, the Gaudi mask offers a principled solution to the differentiability problem for structural parameters, and the experimental results show clear improvements over hand-designed alternatives. However, the evaluation has a significant interpretive gap — the gains cannot be confidently attributed to learned block patterns vs. per-layer budget allocation — and the lack of variance reporting weakens the quantitative claims. These are addressable in revision but reduce confidence in the current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>