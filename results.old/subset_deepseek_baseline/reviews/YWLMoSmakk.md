## Summary
The paper addresses redundant transformations in middle-to-deep layers of Pre-Norm Transformer language models, attributing the problem to training paradigms that neglect the effectiveness of nonlinear transformations. It proposes a Coherence-based Redundancy (CR) measure to quantify redundancy between layer input and output, and introduces two schemes to reduce redundancy: tree-structured residual paths that enhance cross-layer information flow, and a coherence-based redundancy loss combined with an orthogonality loss. Pre-training experiments on a 130M-parameter Llama3 model with 11B tokens show that the proposed methods reduce perplexity, enabling a 12-layer model to outperform a 14-layer baseline.

## Strengths
- **Novel coherence-based metric**: The CR measure uses characteristic functions and frequency-domain coherence to capture statistical differences between layer input/output distributions, going beyond cosine similarity that only captures directional information. This provides a more principled way to detect both near-identity and near-irrelevant transformations.
- **Targeted regularization**: The coherence-based redundancy loss explicitly penalizes layer outputs whose coherence approaches 0 or 1, directly addressing the identified redundant transformation criteria. The tree-structured residual path is a simple yet effective modification to improve shallow-to-deep information flow.
- **Empirical validation on small model**: The paper conducts careful ablation studies (Figure 3) to justify hyperparameter choices (sharpening, target coherence value, scaling factors), showing that each component contributes to the final perplexity improvement.

## Weaknesses
### Fatal
None.

### Major
- **Limited experimental scale**: The method is validated only on a 130M-parameter model trained on a small subset (11B tokens) of The Pile. Claims about generalizing to large language models (e.g., "LLMs typically employ Pre-Norm") are unsupported. Without experiments on models of 1B+ parameters or evaluation on downstream tasks, the practical significance remains unclear.
- **Weak baseline comparison**: The 14-layer baseline is trained from scratch with the same hyperparameters, but the paper does not demonstrate that the 14-layer baseline is well-optimized (e.g., no learning rate tuning, no verification that 14 layers actually benefit from the extra capacity). The 0.1 perplexity advantage over the 14-layer baseline could be within noise or due to suboptimal baseline training. The improvement over the 12-layer baseline (0.45 perplexity) is more convincing but still requires replication.
- **Lack of rigorous validation of CR measure**: The paper asserts that coherence is superior to cosine similarity for detecting redundant transformations, but provides only a correlation plot (Figure 2a) showing similar trends. No controlled experiment demonstrates that using CR in the loss outperforms a loss based on cosine similarity or other alternatives. The claimed advantage (richer information from frequency domain) is not empirically supported.
- **Missing ablations on key components**: The tree-structured residual path is tested jointly with the regularization losses; its individual contribution is not isolated. The orthogonality loss is included but never ablated separately. The choice of which layers receive which loss (layers 2,4,6,8 CR loss; layers 3,5,7,9,10 orthogonality loss) appears arbitrary and is not justified or ablated.
- **Arbitrary design choices**: The specific binary tree structure (layer 0 and 1 as children, fixed assignment of even/odd indices) is not compared to alternative topologies (e.g., dense connections, different tree heights). The target coherence value of 0.35 is tuned on the same evaluation set, risking overfitting.

### Minor
- **CR computation details unclear**: The paper computes coherence per frequency but then plots "Coherence Mean" across frequencies without specifying the aggregation. The softmax-based distribution construction from normalized hidden states is defined but its sensitivity to scaling is not discussed.
- **Evaluation only on perplexity**: No downstream task evaluation (e.g., HellaSwag, ARC, MMLU) is provided. Perplexity improvements may not translate to task performance gains, especially given very small model size.

### Trivial
None.

## Nice-to-Haves
- Experiments on a larger model (e.g., 350M or 1B parameters) and/or a full pre-training run (more tokens) would significantly strengthen the claims.
- Comparison with alternative redundancy reduction methods such as dropout, stochastic depth, or LoRA-based training would help contextualize the gains.
- An analysis of whether the coherence-based loss generalizes across different random seeds or dataset splits.

## Novel Insights
Beyond the paper’s own contributions, the key insight is that layer redundancy can be framed as a distributional matching problem in the frequency domain, where coherence directly indicates whether a layer performs insufficient nonlinear transformation (coherence→1) or irrelevant transformation (coherence→0). This perspective connects signal-processing concepts to neural network training and offers a differentiable regularization signal. However, whether this insight materially outperforms simpler heuristics is not fully demonstrated.

## Suggestions
- Run additional experiments on at least one larger model (e.g., 350M or 1B) with the same pre-training recipe to show scalability.
- Include an ablation that replaces the CR loss with a cosine-similarity-based loss (e.g., penalizing cosine similarity near 1 or 0) to directly compare the benefit of coherence.
- Provide downstream task evaluation (e.g., commonsense reasoning benchmarks) to confirm that perplexity gains translate to improved capabilities.
- Perform a sensitivity analysis on the tree structure (e.g., random tree vs. binary tree vs. dense connections) and on the layer assignments for losses.

## Score and Decision
**Score**: 4.0 (borderline reject)

**Decision**: Reject

The paper introduces a conceptually interesting coherence-based approach to detecting and regularizing redundant transformations in Transformer layers. However, the experimental validation is far too limited—only one small model (130M parameters) on a small dataset, with no downstream evaluation and incomplete ablations. The claimed advantage over existing methods (e.g., pruning, dense connections) is not convincingly demonstrated. The core ideas may have merit, but the evidence presented does not meet the threshold for acceptance at ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>