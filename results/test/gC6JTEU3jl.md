Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me write the final consolidated review.

## Summary

This paper proposes BESA (Blockwise Parameter-Efficient Sparsity Allocation), a framework for pruning large language models. The core idea is to replace layer-wise pruning (used in SparseGPT/Wanda) with block-wise reconstruction that jointly optimizes sparsity allocation across layers within each transformer block, using a small set of differentiable coefficients to represent layer sparsity. Experiments on LLaMA1/2 models from 7B to 70B show consistent perplexity and zero-shot accuracy improvements over SparseGPT and Wanda at 50% unstructured sparsity.

## Strengths

- **Differentiable block-wise sparsity allocation.** BESA replaces the manual per-layer sparsity tuning required by SparseGPT and Wanda with a learned allocation mechanism (Eqs. 5–8) using only ~2% extra parameters per block (row-wise) or ~0.0003% (layer-wise). This is a genuine architectural contribution — it eliminates hand-crafted sparsity schedules.

- **Consistent state-of-the-art perplexity across all LLaMA scales.** In Table 1, BESA achieves the lowest perplexity on WikiText2, C4, and PTB for every tested model (7B–70B), e.g., LLaMA-65B WikiText2: 4.33 vs. 4.60 for SparseGPT and Wanda. The improvement is small in absolute terms (0.2–0.3 perplexity points) but consistent across 21 comparisons.

- **Near-lossless zero-shot accuracy at scale.** Table 2 shows BESA averages 73.73% on LLaMA-65B vs. the dense model's 73.71%, demonstrating that the method can prune 50% of weights without degradation on downstream tasks. For 11 of 14 model–task configurations, BESA achieves the highest accuracy.

- **Practical computational cost.** Pruning LLaMA-65B takes 4.5 hours on a single A100 GPU, and LLaMA2-70B takes five hours — well within academic budgets and comparable to baseline methods.

## Weaknesses

### Fatal

None. The paper's core contribution (differentiable block-wise sparsity allocation with consistent empirical gains) is supported by evidence.

### Major

- **Joint compression experiment conflates pruning allocation with quantization optimization.** The "Joint" pipeline (BESA + OmniQuant) jointly optimizes both pruning masks and quantization clipping strengths $\{\gamma_0, \gamma_1\}$ via block-wise reconstruction (Section 3.3). The "Joint-Wanda" baseline applies Wanda pruning to a model that was quantized with *fixed* (non-optimized) clipping parameters. The gap in Table 3 (e.g., 7.00 vs. 7.44 on LLaMA-7B WikiText2) could therefore be driven by improved quantization parameters rather than superior pruning allocation. To claim that BESA's pruning alone is responsible for the gain, the authors would need an ablation where quantization parameters are held fixed or shared between the two pipelines. This does not invalidate the main pruning results (Tables 1–2) but weakens the joint compression claim as presented.

### Minor

- **Ambiguity about which sparsity-learning variant (row-wise vs. layer-wise) was used for main results.** The method section (line 140) states "By default, we learn sparsity for each row" and mentions that the lightweight layer-wise variant adds only $D$ parameters per layer. The experiments section never explicitly restates which variant produced Tables 1, 2, and 4. The paper *does* indicate the default, so the critic's claim that "the paper never states which one was actually used" is too strong — but the omission from the experiments section is a genuine clarity gap. If the row-wise variant was used (as "default" suggests), then the method adds millions of parameters trained on only 128 sequences; this is not necessarily problematic (the parameters are only for the sparsity coefficients, not the weights themselves), but it should be stated explicitly.

- **No measure of variance or statistical significance.** The paper does not report standard deviations, multiple seeds, or confidence intervals for any experiment. While this is standard practice in the LLM pruning literature (SparseGPT and Wanda also omit variance), the reviewer's concern is valid: with a calibration set of only 128 sequences, the variability of perplexity and zero-shot accuracy may be non-trivial, and the reported margins (0.2–0.3 perplexity points) are small. At minimum, reporting the range over a few runs would increase confidence that improvements are robust.

- **The speedup evaluation (Section 4.5) has limited practical relevance.** The paper uses a ViTCoD accelerator simulator rather than real hardware, and acknowledges that BESA produces unstructured sparsity that cannot exploit NVIDIA's cuSPARSELt $n{:}m$ patterns. This is transparently stated, but it means the speedup comparison tells us little about practical deployment. The baselines (SparseGPT, Wanda) are typically evaluated with $2{:}4$ structured sparsity on real GPUs, where they achieve meaningful speedups — the simulator comparison does not speak to this regime.

- **Missing hyperparameter discussion.** The sparsity penalty weight $\lambda$ (Eq. 1) is a critical hyperparameter that trades off reconstruction fidelity against the target sparsity. The paper says only "we find works well" (line 75) with no sensitivity analysis or justification for the chosen value. The construction of the candidate pruning rates $\{p_d\}_{d=1}^D$ is also underspecified — the paper sets $D=100$ (line 142) but does not describe how the candidate rates are spaced (uniform, logarithmic, etc.), which could affect the granularity of sparsity allocation.

### Trivial

- **"First differentiable pruning algorithm for LLMs" (line 33).** This priority claim is unnecessary and hard to verify. The paper would be equally strong without it, since the contribution stands on its technical merits.

## Nice-to-Haves

- **Visualization of learned sparsity distributions.** A figure showing how sparsity varies across blocks and layers for a representative model (e.g., LLaMA-7B) would strengthen the explanatory power of the method. Currently only aggregate per-layer-type sparsities are given (Table 5), which is insufficient to understand depth-dependent patterns.

- **Ablation separating block-wise reconstruction from learned sparsity allocation.** The cleanest experiment would compare: (a) full BESA, (b) BESA with fixed uniform sparsity per block (block reconstruction alone), and (c) BESA with layer-wise reconstruction instead of block-wise reconstruction (learned sparsity alone). This would isolate which component drives the improvement.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Algorithm 1 X_fp initialization inconsistency.** The critic notes that the printed algorithm initializes only $\mathbf{X}_p$ but then uses $\mathbf{X}_{fp}$ on line 174. The commented-out version (line 150) initializes both. Given the paper's formatting context, this is consistent with a parser artifact where a line was dropped during extraction — the original submission almost certainly initializes both variables.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important observation: the value of block-wise reconstruction in LLM pruning may come as much from the optimization of quantization parameters as from the sparsity allocation itself. The joint compression confound suggests a natural follow-up: evaluate BESA pruning with a fixed, pre-optimized quantizer to isolate the pruning contribution.

## Suggestions

1. **Explicitly state which sparsity-learning variant** (row-wise or layer-wise) produced each reported result. If row-wise was used, add a brief discussion of the parameter count and whether the 128-sequence calibration set raises overfitting concerns. A simple ablation comparing the two variants on one or two model sizes would resolve the ambiguity entirely.

2. **Add a controlled joint compression baseline.** Either (a) apply BESA pruning to weights quantized with fixed (non-optimized) OmniQuant parameters, or (b) also learn quantization clipping strengths for the Joint-Wanda baseline. This would isolate whether the gain comes from better pruning allocation or better quantization.

3. **Report variance** for at least one representative setting (e.g., LLaMA-7B, WikiText2 perplexity over 3 runs) to establish that the margins over baselines are outside noise.

4. **Provide $\lambda$ sensitivity analysis** and describe how $\{p_d\}_{d=1}^D$ is constructed. These details significantly affect reproducibility.

## Score and Decision

The paper makes a solid contribution — differentiable block-wise sparsity allocation is a well-motivated improvement over uniform layer-wise pruning, and the empirical results consistently favor BESA across model scales. The main weaknesses (the joint compression confound, the row-wise/layer-wise ambiguity, and the lack of variance reporting) are addressable and do not undermine the primary pruning results. With clarifications and a controlled joint compression ablation, the paper would be a strong contribution to the LLM pruning literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>