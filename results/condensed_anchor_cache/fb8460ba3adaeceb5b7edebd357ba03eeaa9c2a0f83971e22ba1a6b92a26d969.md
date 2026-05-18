- Decision: Accept
- Scores: 6, 6, 6, 6

## Merged Review

### Summary
The paper proposes a 2D State Space Model (SSM) layer based on Roesser’s multidimensional SSM, computed as convolution, to inject 2-D inductive bias into Vision Transformers and ConvNeXT. It introduces efficient parameterization, accelerated computation, and normalization. Empirical results show performance improvements with negligible extra parameters and inference time, even without positional encoding. Code is provided.

### Strengths
- Sound theoretical justification grounded in control theory (R1, R2); the layer is shown to generalize S4ND and has greater expressiveness (R2, R3).
- Can be computed as convolution, enabling efficient implementation (R1).
- Easily pluggable into ViT and other backbones (ViT, Mega, ConvNeXT) with negligible additional parameters and inference time (R1, R4).
- Highly parameter-efficient: expresses kernels of any length via just eight scalars (R2).
- Provides strong 2-D inductive bias: works without positional encoding (R2, R4).
- Outperforms previous SSM baselines (e.g., S4ND) across multiple datasets and regimes (R3).
- Particularly effective in small data regimes (R3).
- Includes supplementary code for reproducibility (R2).
- Ablation studies and visualizations confirm strong 2-D inductive bias (R2).

### Weaknesses
1. **Marginal performance improvement**: Gains are tiny and may disappear with hyperparameter variation; more experiments are needed to justify the benefits (R1).
2. **High training time cost**: Training time approximately doubles compared to baselines (R2, R3, R4). It is unclear if comparable extra compute given to baselines would yield indistinguishable results (R2). A breakdown of computational cost (SSM layer vs. rest) and actual inference times would be useful (R3). The paper lacks per-epoch or total training time comparison and does not clarify if baseline optimization is controlled (R2). Inference time and memory cost should also be reported in Table 1 (R4).
3. **Limited task scope**: Evaluated only on image classification. Dense prediction tasks (semantic segmentation, instance segmentation, depth estimation) would better assess 2-D inductive bias (R1, R2, R4).
4. **Limited architectural scope and baselines**: 
   - Performance on ConvNets (e.g., ConvNeXt) and comparison with simpler inductive bias methods (convolutional layers, alternative positional encodings [2,3,4,5]) are needed (R2, R3). 
   - Uncertain how the layer interacts with inherent inductive biases of convolutional layers (R2).
5. **Instability of the complex variant (SSM-c)**: The complex variant obtains very bad results in Tables 1 and 6; explanation and potential mitigation are required (R4).
6. **Scalability concerns**: Implementation is more complicated than straightforward convolutional layers (R3). The method may not scale effectively to larger models (e.g., Base size on ImageNet-1K) and larger datasets; scaling behavior should be studied (R3). 
7. **Ambiguities in experimental reporting**:
   - It is unclear whether the version used in Table 3 is SSM-r or SSM-c (R4).
   - Models in tables (e.g., “ViT w/ MixFFN”) are not defined (R4).
   - Why is the `D` term omitted in Equation 2? Does its inclusion reduce performance? (R3)
   - Figure 4 shows larger relative benefit at 100% data than at 20% or less, which is counterintuitive; explanation needed (R3).
8. **Lack of large-scale pretraining evaluation**: The paper does not evaluate whether pretraining on large datasets with the proposed layer yields better downstream finetuning performance compared to baseline; if not, practical significance is unclear (R2).