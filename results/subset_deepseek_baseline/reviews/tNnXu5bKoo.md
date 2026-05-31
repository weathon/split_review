## Summary
This paper proposes FuseGPT, a structured pruning paradigm for GPTs that reframes block removal as knowledge redistribution. Instead of discarding less salient transformer blocks, FuseGPT fuses their knowledge into neighboring blocks using a learnable low-rank fusion mechanism, guided by a fusion-aware importance metric called Macro Influence (MI). The method is iterative, uses lightweight group-level fine-tuning with a distillation loss, and is evaluated across LLaMA, LLaVA, and newer architectures, achieving superior perplexity and zero-shot accuracy compared to prior pruning and layer-merging methods.

## Strengths
- **Novel prune-and-fuse paradigm**: The core idea of recycling pruned blocks by grafting their knowledge into neighbors via learnable low-rank coefficients is a genuine conceptual advance over simple removal or static merging. This reframes pruning as knowledge redistribution rather than deletion.
- **Fusion-aware importance metric (MI)**: The MI score measures the global impact of block removal on final hidden states and is explicitly designed to identify blocks that can be effectively absorbed. Ablations show MI outperforms prior metrics (BI, SLEB score) even with far fewer calibration samples.
- **Comprehensive experiments**: The paper evaluates on multiple model families (LLaMA-2, LLaMA-3, LLaVA, Mistral, Qwen3, Phi-3.5) and tasks (perplexity, zero-shot benchmarks, multimodal) with consistent improvements over competitive baselines (ShortGPT, SliceGPT, SLEB, LaCo, MKA). The data efficiency (32 calibration + 1024 fine-tuning samples) is noteworthy.
- **Careful ablations**: The ablation in Table 6 isolates the contributions of the MI metric, LoRA fine-tuning, and the fusion mechanism, demonstrating that each component adds value and that fusion contributes beyond what fine-tuning alone achieves.
- **Orthogonality to quantization**: The paper shows FuseGPT can be combined with 4-bit GPTQ with only modest perplexity degradation, suggesting practical utility in extreme compression scenarios.

## Weaknesses
### Fatal
None.

### Major
- **Unusual distillation loss with limited justification**: The KL divergence loss (Eq. 6) computes softmax over the *batch dimension* of hidden states (dim=0), rather than over the vocabulary or a more standard feature-space loss. The authors provide no intuitive or theoretical motivation for this design, and it is not validated against alternatives (e.g., MSE on hidden states, cosine similarity, or standard logit-based KL). While the empirical results are strong, the soundness of this loss formulation is unclear and could be a critical issue for reproducibility or generalizability.
- **Unfair baseline comparison in main tables**: Table 1 and Table 2 compare FuseGPT (which uses 1024 fine-tuning samples) against ShortGPT, SLEB, and SliceGPT—methods that perform *no fine-tuning*. The ablation (Table 6) partially addresses this by adding LoRA to these baselines, but the paper does not explicitly highlight in the main text that the gains are partly due to fine-tuning and that the primary advantage comes from the fusion mechanism (as shown in ablations). This risks overstating the improvement.

### Minor
- **MI metric definition**: Equation (1) uses an expectation over $\mathbf{X}$ and $t$, but the sampling distribution for $\mathbf{X}$ (calibration set) is not formally defined in the main text. The notation $\mathbf{X}_{\mathcal{M},t}$ as the $t$-th row of the hidden state is also ambiguous (likely the token index). These details should be clarified.
- **Speedup numbers modest**: The reported 1.33× speedup at 25% sparsity is consistent with block removal, but the paper does not discuss how this scales with model size or hardware. A comparison with the theoretical maximum speedup would be informative.
- **Limited discussion of compute cost**: While inference speedup is reported, the cost of the fusion and fine-tuning process (e.g., GPU-hours, memory) is not discussed, which is important for practical adoption.

### Trivial
- In Table 1, ShortGPT at 30% sparsity on LLaMA-3-8B yields perplexity >8000, indicating near-total model collapse; this could be noted briefly for context.

## Nice-to-Haves
- An ablation comparing the proposed KL loss over the batch dimension with more standard distillation losses (MSE, KL over logits, cosine) on a representative setting.
- Analysis of the learned low-rank coefficients $\mathbf{C}$: do they exhibit interpretable patterns? Does the rank $r$ have a significant impact on fusion quality?
- A baseline that simply removes blocks and fine-tunes the remaining blocks with LoRA (without fusion) on the same partial groups, to further isolate the benefit of the fusion term.

## Novel Insights
The paper’s central insight—that structured pruning can be treated as knowledge redistribution via learnable fusion rather than removal—is genuinely novel. The MI metric’s design as a *forward-looking* importance score that identifies blocks easy to absorb is a nuanced and practical improvement over existing redundancy or similarity heuristics. The demonstration that lightweight, local fine-tuning can effectively integrate injected weights while preserving task performance is a valuable contribution for resource-constrained compression.

## Suggestions
1. Provide a clear justification or ablation for the KL loss over the batch dimension; if this design is empirically crucial, report comparisons with alternative losses.
2. Add a sentence in the main results section stating that one-shot baselines (ShortGPT, SLEB, SliceGPT) do not use any fine-tuning, and refer to the ablation for a controlled comparison with fine-tuned variants.
3. Clarify the notation in Eq. (1) and the exact procedure for computing MI (e.g., how many calibration samples, how $t$ is defined).

## Score and Decision
**Score**: 8/10  
**Decision**: Accept

The paper presents a well-motivated and technically novel contribution to structured pruning of large language models. The prune-and-fuse idea, the MI metric, and the learnable low-rank fusion are clearly explained and supported by extensive experiments. The weaknesses (unusual loss design, baseline comparison framing) are significant but not fatal—they can be addressed in the camera-ready and through discussion. Overall, the work offers a new direction for model compression with strong empirical support.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>