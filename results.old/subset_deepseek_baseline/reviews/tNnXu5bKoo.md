## Summary

FuseGPT introduces a "prune-and-fuse" compression paradigm for GPT models that reframes structured pruning as knowledge redistribution rather than simple removal. Instead of discarding less salient transformer blocks, FuseGPT recycles them by fusing their knowledge into neighboring blocks via a learnable low-rank fusion mechanism guided by a novel Macro Influence (MI) importance metric. The method achieves superior perplexity and zero-shot task performance compared to prior pruning and layer-merging approaches across LLaMA, LLaVA, and other model families, using as few as 32 calibration and 1024 fine-tuning samples.

## Strengths

- **Novel conceptual framing**: The paper reframes structured pruning as knowledge redistribution rather than removal, which is a genuinely different perspective from prior work. The "prune-and-fuse" idea of recycling rather than discarding parameters is conceptually elegant and well-motivated.

- **Strong empirical results**: FuseGPT consistently outperforms multiple strong baselines (ShortGPT, SliceGPT, SLEB, LaCo, MKA) across diverse model families (LLaMA-2/3, LLaVA, Qwen3, Mistral-NeMo, Phi-3.5) and multiple evaluation metrics (perplexity, zero-shot tasks, MMLU). The improvements are substantial and systematic, not marginal.

- **Data efficiency**: The method achieves strong results with only 32 calibration samples and 1024 fine-tuning samples, which is remarkably lightweight for model compression. This practical advantage is clearly demonstrated in ablation studies.

- **Orthogonality to quantization**: The demonstration that FuseGPT can be combined with 4-bit GPTQ quantization (achieving 52.1% total compression with modest perplexity increase) shows practical applicability for extreme compression scenarios.

- **Comprehensive evaluation**: The paper evaluates on both language-only and multimodal models, includes head-to-head comparisons with layer-merging methods, ablation studies on each component, and latency measurements. The evaluation is thorough and well-designed.

## Weaknesses

### Fatal
None.

### Major
- **Limited novelty of MI metric relative to SLEB**: The Macro Influence (MI) metric measures cosine similarity between last hidden states of the original and pruned model. This is conceptually very similar to SLEB's approach of measuring token prediction loss after block removal. While the paper argues that soft targets (cosine similarity) are better than hard targets (token prediction loss), the difference is incremental rather than fundamental. The paper claims MI is "fusion-aware" but the metric itself does not explicitly model fusion—it simply measures block importance, and fusion happens in a separate stage.

- **Computational cost concerns**: The iterative nature of the algorithm (prune one block at a time, recompute MI scores, perform fusion and fine-tuning for each block) raises questions about total computational cost. For pruning 25% of blocks in a 32-block model, this requires 8 iterations of MI computation and group-level fine-tuning. The paper does not report total runtime or computational budget for the full pruning process, making it difficult to assess practical deployment cost.

- **Limited analysis of fusion mechanism behavior**: The learnable low-rank fusion (Equation 3-4) is a core contribution, but the paper provides no analysis of what the learned coefficients look like, how they vary across layers or blocks, or whether certain patterns emerge. Without this analysis, it's unclear whether the mechanism is genuinely learning meaningful knowledge redistribution or simply providing additional trainable parameters that help fine-tuning.

### Minor
- **Group size selection**: The paper uses G=7 throughout but provides no ablation on this hyperparameter. The group size determines how many blocks are updated per iteration and directly impacts computational cost. A sensitivity analysis would strengthen the paper.

- **Comparison fairness with MKA**: Table 4 compares FuseGPT at 25% compression with MKA at 43.8% compression. While the paper notes this difference, the comparison is inherently unfair to MKA since higher compression typically degrades performance more. A comparison at matched compression ratios would be more informative.

- **Limited discussion of failure cases**: The paper reports strong results across many settings but does not discuss scenarios where FuseGPT might underperform or fail. For example, at 30% sparsity on LLaMA-3-8B, perplexity jumps significantly (from 9.24 to 10.61 on WikiText-2), suggesting potential degradation patterns worth analyzing.

### Trivial
- The paper uses "A1ZD" in Table 3 but the correct dataset name is "AI2D" (AI2 Diagrams).

## Nice-to-Haves

- Analysis of learned fusion coefficients (e.g., visualization of C matrices, rank analysis, patterns across layers)
- Ablation on group size G
- Total computational cost comparison (GPU-hours) with baselines
- Analysis of which blocks tend to be pruned (early vs. late layers) and whether this pattern is consistent
- Discussion of when the method might fail or underperform

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add an ablation study on the group size hyperparameter G to show sensitivity and guide practitioners
- Report total computational cost (GPU-hours) for the full pruning process to enable practical comparison
- Include analysis of learned fusion coefficients to demonstrate that the mechanism is genuinely learning meaningful knowledge redistribution rather than just providing extra parameters for fine-tuning
- Add matched-compression-ratio comparisons with MKA for fairer evaluation
- Discuss potential failure cases or limitations more explicitly

## Score and Decision

The paper presents a genuinely novel approach to structured pruning with strong empirical results across multiple model families and tasks. The "prune-and-fuse" framing is conceptually interesting and practically effective. The main limitations are the incremental nature of the MI metric relative to prior work and the lack of analysis on computational cost and fusion mechanism behavior. However, these do not invalidate the core contribution. The paper is well-written, the experiments are thorough, and the results convincingly demonstrate the value of the approach.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>