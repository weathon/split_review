## Summary
The paper introduces **pcLLM**, a training and inference framework that transforms standard Autoregressive (AR) models into efficient parallel decoders using a novel **progressive consistency distillation** paradigm. The method addresses the scalability limitations of prior consistency-based models (like CLLM) by employing a progressive noise schedule, noise-aware causal attention masks, and iterative training with increasing block sizes. To further capitalize on the model's ability to generate high-quality "future" tokens even under noisy conditions, the authors propose **multi-block decoding with rejection recycling**, achieving up to $3.95\times$ wall-clock speedup on H200 GPUs while maintaining high accuracy on coding and math benchmarks.

## Strengths
- **Strong Empirical Results:** The paper demonstrates significant speedups ($3.5\times$ to $4\times$) across multiple benchmarks (HumanEval, MBPP, GSM8K, MATH) while maintaining competitive accuracy. It notably outperforms recent diffusion-based LLMs (dLLMs) in both speed and task performance.
- **Novel Training Paradigm:** The "Progressive Noise Schedule" and "Noise-aware Causal Attention" are well-motivated solutions to the difficulty of learning long-range dependencies in consistency distillation. The sequence packing technique (Figure 1) provides a clever way to optimize training efficiency.
- **Inference Innovation:** The introduction of "Multi-block Decoding with Rejection Recycling" is a clever adaptation of speculative decoding principles to the Jacobi decoding framework. It effectively utilizes the "stationary tokens" observed in the pcLLM trajectories.
- **Hardware-Aware Analysis:** The paper includes practical analysis of FLOPs utilization on modern hardware (A100/H200), showing that the proposed parallel verification does not incur significant latency penalties within certain block-size regimes.

## Weaknesses
### Major
- **Performance Degradation on Coding Tasks:** While the speedup is impressive, there is a noticeable drop in accuracy on HumanEval (87.8% $\rightarrow$ 84.8%) and MBPP (74.3% $\rightarrow$ 73.4%). For high-stakes coding tasks, a 3% absolute drop in pass@1 is significant. The paper mentions this degradation briefly but does not provide a deep analysis of why the consistency objective harms the base model's reasoning capabilities or how to mitigate it further.
- **Comparison with Speculative Decoding:** The paper positions pcLLM primarily against dLLMs and Jacobi-based methods. However, Speculative Decoding (e.g., EAGLE-3, Medusa) is the industry standard for AR acceleration. While the authors mention a comparison in the appendix (which is stripped in this version), the main text lacks a head-to-head discussion of why pcLLM is preferable to a well-tuned EAGLE-3 setup, which often achieves similar speedups without sacrificing accuracy.

### Minor
- **Complexity of the Training Pipeline:** The method requires multiple rounds of trajectory generation and training with increasing block sizes. This makes the recipe significantly more computationally expensive and complex to implement compared to training-free methods or single-stage distillation.
- **Hyperparameter Sensitivity:** The performance seems highly dependent on the noise schedule window size and the "spawn ratio" $r$. While ablated, the robustness of these parameters across different model scales (e.g., 70B+) is not explored.

## Nice-to-Haves
- Evaluation on more general-purpose benchmarks (e.g., MMLU or MT-Bench) to ensure the distillation doesn't cause "catastrophic forgetting" of general knowledge.
- A breakdown of the training cost (GPU hours) compared to standard SFT.

## Novel Insights
The core novel insight is that the bottleneck in consistency distillation for large block sizes is the "noise dependency span." By progressively increasing noise and using a noise-aware mask, the model learns to "denoise" future tokens more effectively than standard Jacobi-based training. Furthermore, the observation that pcLLM produces stable $n$-gram segments in the "tail" of the Jacobi trajectory allows for a hybrid approach—combining fixed-point iteration with rejection-based recycling—which bridges the gap between Jacobi decoding and speculative decoding.

## Suggestions
- Provide a more detailed error analysis for the 3% drop in HumanEval. Are the errors due to syntax issues (suggesting the parallel decoding is breaking structure) or logic issues?
- Clarify the "rejection recycling" mechanism: specifically, how the $n$-gram pool is managed to prevent it from growing indefinitely or becoming stale.

## Score and Decision
The paper presents a very strong case for AR models as parallel decoders. It is technically sound, provides significant speedups on high-end hardware, and offers a clear algorithmic improvement over CLLM. Despite the slight accuracy trade-off, the contribution to the efficiency of LLM inference is substantial and highly relevant to the ICLR community.

MY FINAL SCORE: 8.0
MY FINAL DECISION: Accept