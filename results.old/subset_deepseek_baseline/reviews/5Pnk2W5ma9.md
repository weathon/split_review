## Summary

The paper introduces ONNX-Bench, a large-scale benchmark (649,596 architecture-accuracy pairs) that unifies multiple NAS search spaces (NAS-Bench-101/201/301, NATS-Bench, hNAS-Bench-201, einspace) into a common ONNX representation with consistent CIFAR-10 evaluation. It also proposes ONNX-Net, a text-based encoding of ONNX graphs that feeds into a fine-tuned LLM (ModernBERT) for instant performance prediction. Experiments demonstrate zero-shot transfer between search spaces, with competitive performance compared to prior methods like FLAN and GENNAPE, and ablation studies analyze the contribution of different encoding components and backbone choices.

## Strengths

- **Unified benchmark across search spaces**: ONNX-Bench consolidates architectures from six different NAS benchmarks into a single ONNX format, enabling cross-space training and evaluation of predictors. This is a valuable resource for the community.
- **Flexible, search-space-agnostic encoding**: The text-based encoding can represent arbitrary ONNX graphs, including operator parameters and topology, without being tied to cell-based or fixed-topology spaces. This is a clear advance over prior graph-based encodings that are search-space-specific.
- **Thorough experimental evaluation**: The paper provides extensive zero-shot transfer experiments (Tables 2–5), ablation studies on encoding components (Table 6) and backbone models (Table 7), and cross-dataset generalization (Table 5). The analysis of diversity via Jensen-Shannon divergence (Figure 2) is informative.

## Weaknesses

### Fatal
None.

### Major
- **Zero-shot performance is not state-of-the-art**: GENNAPE achieves Spearman’s ρ = 0.815 for NAS-Bench-101 → NAS-Bench-201 transfer, while ONNX-Net reaches 0.747 (Table 3). The paper acknowledges this but attributes it to GENNAPE’s ensemble; however, the gap is substantial and the claim of “strong zero-shot performance” is relative. The generality advantage of ONNX-Net is not quantified against the performance loss.
- **Limited to CIFAR-10 and existing NAS benchmarks**: The benchmark only includes architectures from existing NAS benchmarks (mostly cell-based or hierarchical) and only CIFAR-10 accuracy. The claim of “universal representations” is overstated—transformers, attention-based architectures, and other modern designs are absent. The cross-dataset experiment (UnseenNAS) is within the einspace search space, not a truly novel task.
- **No comparison with Python-code-based encodings**: The paper motivates ONNX over Python code by arguing that ONNX yields fewer distinct encodings per model, but provides no empirical comparison. A direct experiment comparing ONNX-text vs. Python-code-text for the same architectures would strengthen the claim.
- **Computational cost of LLM fine-tuning is not reported**: The paper does not state training time, GPU hours, or inference speed for the ModernBERT predictor. This is important for reproducibility and for assessing the practicality of “instant” prediction.

### Minor
- **“Instant” claim is slightly misleading**: The predictor requires fine-tuning an LLM, which is not instant; only inference after training is fast. This is standard for surrogate models, but the phrasing could be clarified.
- **Encoding simplifications not rigorously justified**: Node removal and subgraph merging are described as “lossless” or “low-importance,” but no analysis is provided on how much information is discarded or how it affects prediction accuracy.
- **Table 2 shows only Kendall’s τ**: Including Spearman’s ρ would be consistent with other tables and provide a more complete picture.

### Trivial
None.

## Nice-to-Haves

- Include a comparison with Python-code-based encodings (e.g., from Gao et al. 2025 or Rahman et al. 2025) to empirically justify the ONNX advantage.
- Add experiments on more diverse architectures (e.g., transformers, attention-based models) to demonstrate true universality.
- Report the computational cost (GPU hours, training time) of fine-tuning the LLM predictor.
- Provide an analysis of how much the encoding simplifications affect the graph structure (e.g., node count reduction ratio).

## Novel Insights

The paper’s key insight is that ONNX provides a stable, unique representation of neural architectures that can be converted into a compact text encoding, enabling LLM-based performance prediction that generalizes across search spaces. The finding that input information (connectivity and weight shapes) is the most important encoding component (Table 6) and that encoder-based LMs (ModernBERT) outperform decoder-based ones (Qwen3) for this task (Table 7) are useful practical guidelines. The diversity analysis (Figure 2) quantitatively confirms that hierarchical spaces like einspace are much more diverse than cell-based spaces, motivating the need for a unified benchmark.

## Suggestions

- Provide a more detailed comparison with GENNAPE, including an analysis of the performance–generality trade-off. If ONNX-Net can be applied to architectures that GENNAPE cannot handle (e.g., non-cell-based), demonstrate this explicitly.
- Expand ONNX-Bench to include transformer-based architectures (e.g., from ViT or BERT search spaces) to strengthen the claim of universality.
- Report the training time and inference speed of the ModernBERT predictor to help practitioners assess its practicality.
- Include a small experiment comparing ONNX-text encoding with Python-code-text encoding on a subset of architectures to empirically validate the motivation.

## Score and Decision

**Score**: 6  
**Decision**: Accept

The paper makes a solid contribution by providing a unified benchmark and a flexible encoding method for NAS performance prediction. The benchmark is a valuable resource, and the text-based encoding is a step toward search-space-agnostic predictors. However, the performance is not state-of-the-art, the claims of universality are limited by the benchmark’s scope, and the computational cost is not reported. These issues prevent a higher score but do not invalidate the contribution.

MY FINAL SCORE: <score>6</score>  
MY FINAL DECISION: <decision>Accept</decision>