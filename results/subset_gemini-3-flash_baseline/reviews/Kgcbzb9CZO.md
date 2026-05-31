## Summary
The paper proposes Distributional Input Projection Networks (DIPNet), a framework designed to improve neural network generalization by projecting inputs into learnable Gaussian distributions at each layer. This stochastic projection is motivated by variational inference and aims to implicitly promote smoothness in the loss landscape and reduce the model's Lipschitz constant. The authors provide theoretical bounds on the Lipschitz and smoothness properties of the resulting function and demonstrate empirical gains across Vision Transformers (ViTs) and Large Language Models (LLMs) on tasks involving standard generalization, adversarial robustness, and mathematical reasoning.

## Strengths
- The method is versatile and architecture-agnostic, demonstrated by its successful application to both Vision Transformers and a variety of modern LLMs (Qwen, Llama, Gemma).
- The theoretical analysis provides a solid motivation, specifically showing how the distributional projection can bound the Lipschitz constant even for non-Lipschitz base functions (Theorem 1) and reduce it for existing Lipschitz functions (Theorem 2).
- The empirical evaluation is comprehensive, covering standard classification, adversarial robustness (Gaussian and FGSM), and complex reasoning (GSM8K), showing consistent improvements over strong baselines like SAM and Randomized Smoothing.
- The inclusion of a distillation strategy (Algorithm 3) addresses the potential inference latency of stochastic networks, making the method more practical for real-world deployment.

## Weaknesses
### Fatal
None.

### Major
- **Clarity on Layer-wise Implementation:** While the paper claims to project inputs at *every* layer, the practical implementation details for complex architectures like LLMs or ViTs are sparse. It is unclear if the projection is applied before every Attention/MLP block or literally every linear layer. Given the high dimensionality of hidden states in a 12B model, the overhead of learning and storing $\Sigma_l$ for every layer could be significant, yet this is not discussed in detail.
- **Comparison with Variational Layers:** The method bears a strong resemblance to Bayesian Neural Networks (BNNs) or Variational Information Bottleneck (VIB) approaches where activations are treated as distributions. The paper would benefit from a clearer distinction or empirical comparison against standard VIB or "Stochastic Depth/DropConnect" variants which also introduce layer-wise stochasticity.

### Minor
- **Hyperparameter Sensitivity:** Table 3 shows that the stability penalty $\lambda$ has a significant impact on performance (e.g., accuracy dropping from ~52% to ~46% when $\lambda$ moves from 0 to 0.01). This suggests the method might require careful tuning to avoid performance degradation.
- **Distillation Gap:** In Figure 2, there is a noticeable gap between the "Distillation" performance and the "Multi-sample" performance at high $k$. While distillation is faster, the paper does not fully explore if the "smoothness" benefits are perfectly preserved through distillation or if some generalization is lost.

### Trivial
- The "Gemma-3" reference (Farabet & Warkentin, 2025) refers to a very recent/future release, which is unusual but noted as a parser-friendly observation.

## Nice-to-Haves
- A visualization of the loss landscape (e.g., 1D or 2D loss contours) comparing Standard training vs. DIPNet to empirically verify the "smoothness" claim.
- Analysis of the learned variances $\Sigma_l$ to see if the model learns to be "noisier" in earlier or later layers.

## Novel Insights
The core novelty lies in the transition from "Randomized Smoothing" (typically a fixed-noise input-level augmentation) to a "Learnable Layer-wise Projection" integrated into the architecture. The synthesis of variational inference (ELBO) with a stability penalty to specifically target the "instability" component of the generalization gap (as defined by Johnson & Zhang) provides a more principled approach to smoothing than heuristic noise injection.

## Suggestions
- Provide a more detailed breakdown of the parameter overhead added by the $\Sigma_l$ parameters.
- Clarify the exact placement of the DIPNet layers within the Transformer block (e.g., after the residual connection or before the non-linearity).
- Include an experiment on a dataset with natural distribution shifts (like ImageNet-C) to further bolster the OOD generalization claims.

## Score and Decision
The paper presents a well-motivated and theoretically grounded method for improving generalization. The empirical results across diverse architectures (ViT and LLM) are impressive and suggest that the method is robust. While there are some questions regarding the implementation details of the layer-wise projection in large models, the overall contribution is significant for the ICLR community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>