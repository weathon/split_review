## Summary

The paper introduces pcLLM, a progressive consistency distillation paradigm that transforms autoregressive (AR) language models into efficient parallel decoders. The method uses a progressive noise schedule and noise-aware causal attention to train models to predict multiple future tokens per iteration. Combined with inference optimizations (rejection recycling and multi-block decoding), pcLLM achieves up to 3.6–4× wall-clock speedup on coding and math benchmarks with minimal quality degradation. The authors position pcLLM as a faster and more accurate alternative to diffusion-based LLMs for parallel decoding.

## Strengths

- **Novel training paradigm**: The progressive noise schedule is a well-motivated improvement over prior consistency distillation (CLLM). It addresses the difficulty of predicting long noisy contexts by exposing the model to controlled, increasing noise levels during training, which empirically yields better token acceptance.
- **Strong empirical speedups**: On coding benchmarks, pcLLM achieves 3.6× speedup over AR decoding on A100 and nearly 4× on H200, with small accuracy drops (e.g., ~3% on HumanEval). These gains are demonstrated with standard hardware and established base models.
- **Effective inference optimizations**: Rejection recycling and multi-block decoding are well-designed techniques that leverage the higher-quality draft tokens produced by pcLLM. The ablation studies (e.g., Figure 4) convincingly show that multi-block decoding yields the best fast-forward token counts.
- **Thorough ablation on training choices**: Tables 4 and 5 examine noise schedules and attention mask designs, providing useful insights for practitioners.

## Weaknesses

### Fatal

- **Misleading comparison with diffusion LLMs**: The paper’s title and abstract claim that AR models can be “faster and more accurate” than diffusion LLMs, but the experimental comparison is fundamentally unfair. The dLLM baselines (LLaDA-Instruct, Dream-Base, Fast-dLLM, D2F) are not fine-tuned for coding or math tasks, whereas pcLLM is built from task-specific instruct models further trained on domain data. Accuracy on HumanEval/MBPP for dLLMs is extremely low (e.g., 36–56%) because these models are not designed for code generation; comparing them to a model fine-tuned on code (Qwen2.5-Coder-Instruct) is not meaningful. The “more accurate” claim is unsupported and should be removed or the comparison should be controlled for base model capability.

### Major

- **Incomplete dLLM comparison**: Even the speed comparison is questionable. dLLMs such as Dream and LLaDA use different decoding procedures (iterative denoising with many steps) and are not optimized for the same block-wise parallel generation. The paper does not include state-of-the-art dLLMs on coding (e.g., CODED-Llama or domain-tuned dLLMs) nor does it control for inference cost in FLOPs or latency at equal quality. The strong speed advantage of pcLLM over dLLMs likely stems from the AR-based model infrastructure (e.g., KV caching) rather than a fundamental superiority.
- **Missing key experimental details**: The paper does not report training cost (GPU-hours), number of Jacobi trajectories collected, or the exact data mixing ratio between AR loss and consistency loss (weight \(w\) in Eq. 9). Without these, reproducibility is limited. The maximum block size used for inference (128 for most experiments) is mentioned, but the progressive training block sizes (16, then 32) are only briefly described.
- **Accuracy degradation not fully discussed**: On HumanEval, pcLLM drops from 87.8% to 84.8% (3% absolute), and on MBPP from 74.3% to 73.4%. While small, this is not zero-cost speedup. The paper should discuss whether this trade-off is acceptable in practice and whether further training could close the gap.
- **Unclear novelty over CLLM**: The paper states that CLLM’s speedup plateaus with larger block sizes (a known limitation), but the specific improvements—progressive noise schedule and sequence packing—are incremental. The noise-aware causal mask (Figure 1b) is a technical contribution, but its effectiveness is only partially ablated (Table 5). More analysis on why progressive noise schedule outperforms random schedule would strengthen the paper.

### Minor

- **Figure 4 legend inconsistency**: The caption for Figure 4 duplicates across pages and the labels are confusing (e.g., “Fast-Forward Performance: Speedup vs Block Size” but y-axis says “Speedup (vs. Custom)”). This makes interpretation harder.
- **Algorithm 1 is dense and could be better described**: While the pseudo-code is complete, the multi-block spawning and promotion logic is complex without a clear walkthrough. A simpler algorithmic overview would help.

### Trivial

- Some figure captions appear to be duplicated due to formatting issues (likely parser artifacts).

## Nice-to-Haves

- Include a fair dLLM baseline: compare pcLLM to a dLLM that is also fine-tuned on the same domain data (e.g., a dLLM trained on OpenCodeInstruct) and controlled for parameter count.
- Provide inference cost in terms of FLOPs or total GPU-seconds per output token, not just wall-clock speedup, to allow better comparison across methods.
- Analyze the quality of draft tokens more quantitatively (e.g., acceptance rate vs. position in block) to support the qualitative claim in Figure 2.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Reframe the paper to focus on AR parallel decoding via progressive consistency distillation, avoiding overclaims about superiority over dLLMs. Either remove the dLLM comparison entirely or restructure it as an alternative family with different trade-offs (e.g., dLLMs offer multicontrollability but lower speed at equal quality).
- Add training compute details and ablation on the ratio \(w\).
- Include additional baselines: compare pcLLM to speculative decoding methods (e.g., EAGLE-3) and self-speculative decoding at similar model scales, as promised in the appendix (which was stripped).
- Clarify the inference configuration search: show the sensitivity of multi-block parameters (number of blocks, verification size, threshold) across tasks.

## Score and Decision

MY FINAL SCORE: <score>5</score>  
MY FINAL DECISION: <decision>Reject</decision>

The paper presents a solid methodological contribution—progressive consistency distillation—and demonstrates meaningful speedups for AR generation. However, the central claim that AR models can be “faster and more accurate parallel decoders than diffusion LLMs” is not supported by the experimental evidence, as the dLLM baselines are not comparably trained for the evaluated tasks. This overreaching framing undermines the paper’s credibility. The core work on AR acceleration is valuable and could potentially be accepted after major revisions to scope and comparisons, but in its current form the conclusions are not justified. Score 5 reflects that the paper is at the reject level but not far from acceptability with substantial revision.