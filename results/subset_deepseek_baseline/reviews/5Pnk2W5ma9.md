## Summary

This paper introduces two contributions to neural architecture search: (1) ONNX-Bench, a large-scale benchmark that unifies over 600k architecture-accuracy pairs from multiple existing NAS benchmarks (NAS-Bench-101/201/301, NATS-Bench, hNAS-Bench-201, einspace) into a shared ONNX representation all evaluated on CIFAR-10; (2) ONNX-Net, a performance predictor that converts ONNX graphs into a condensed text description and fine-tunes an LLM (ModernBERT) to predict accuracy. The paper demonstrates zero-shot transfer between search spaces and ablates the text encoding components.

## Strengths

- **Unified benchmark creation.** ONNX-Bench consolidates six previously incompatible NAS benchmarks into a single format (ONNX) with consistent CIFAR-10 evaluation, enabling fair cross-search-space comparisons and training of general-purpose surrogate models. This is a valuable resource for the community.
- **Flexible encoding that captures operator details.** The ONNX-to-text representation goes beyond graph topology by including operation hyperparameters (kernel size, stride, padding, etc.), addressing a known limitation of bundle-based encodings. The ablation study (Table 6) confirms that enriching the encoding with input information and parameters improves performance.
- **Comprehensive ablation studies.** The paper systematically ablates encoding components (Table 6), LLM architectures (Table 7), and training data scaling (Figure 5), providing clear insight into what drives performance.
- **Low seed-to-seed variance.** In the zero-shot NB101→NB201 experiments (Figure 5), ONNX-Net shows substantially smaller error bars than FLAN variants, suggesting a more stable training procedure.

## Weaknesses

### Fatal

None.

### Major

1. **Evaluation scope is limited to a single dataset (CIFAR-10).** The entire benchmark and all experiments use CIFAR-10 only. The claim of "instant performance prediction" and "universal representations" is therefore highly restricted—the predictor is tied to this specific dataset and cannot generalize to new tasks without retraining. The cross-dataset experiments in Section 5.3 (UnseenNAS) are still classification tasks but the predictor was trained only on CIFAR-10; the modest performance (Kendall’s τ ≤ 0.58) underscores the dataset-specific nature of the learned mapping. Without evidence on a broader set of target datasets, the "universal" claim is unsubstantiated.

2. **No comparison to other universal approaches on the multi-space setting.** The paper compares ONNX-Net to FLAN and GENNAPE only on the single NB101→NB201 zero-shot task. For the more interesting multi-space setting where training data from all spaces is available (Table 2), there is no comparison to any prior work. It is therefore unclear whether ONNX-Net’s text-based encoding offers advantages over graph-based universal encoders (e.g., GENNAPE trained on multiple spaces, or a GNN trained on ONNX graphs directly). The paper claims that prior methods are tied to cell-based spaces, but the comparisons only use cell-based spaces for zero-shot transfer.

3. **The encoding’s claimed sample efficiency over Python-code representations is untested.** The paper hypothesises that ONNX representations are more sample-efficient than Python code representations (Section 2.1), but no experiment compares ONNX-text to Python-code-text. This claim is central to the motivation for using ONNX rather than source code, yet remains unvalidated.

4. **Limited architectural diversity.** Despite ONNX-Bench combining six benchmarks, all architectures are convolutional networks (CNNs) for image classification, and the set does not include transformers, attention-based designs, or other modern architectural families. The paper acknowledges this as future work. However, the title and claims imply universality, while the validation only covers a narrow (though diverse among CNNs) regime.

### Minor

- **Inconsistency in the best training mixture.** Table 2 shows that leaving out hNAS-Bench-201 from training *improves* transfer to hNAS-Bench-201 (Kendall’s τ 0.533→0.565), suggesting negative transfer from the full mixture. This is an important observation but is not explained or further investigated.
- **Zero-shot performance is not state-of-the-art.** On the standard NB101→NB201 benchmark, GENNAPE (which uses an ensemble of predictors) achieves Spearman’s ρ = 0.815 vs. ONNX-Net’s 0.747. The paper acknowledges this but does not compare to a simpler non-ensemble version of GENNAPE. The “strong” claim is relative only to FLAN.
- **Run-time analysis is missing.** The paper touts “instant” performance prediction but does not compare inference latency of the LLM-based predictor against GNN-based predictors. The LLM forward pass may be significantly slower.
- **The text encoding merges subgraphs, potentially losing information.** While this is necessary for context length, the impact of merging vs. preserving the full graph is not ablated.

### Trivial

- None significant.

## Nice-to-Haves

- Include experiments with non-CIFAR-10 target datasets to demonstrate true cross-dataset generality.
- Compare ONNX-text encoding to a Python-code-based text encoding on the same LLM backbone to validate the sample-efficiency claim.
- Provide runtime comparisons (ms per prediction) between ONNX-Net and graph-based predictors.
- Analyse the negative transfer effect observed for hNAS-Bench-201 (Table 2) and propose a mitigation (e.g., reweighting or data selection).

## Novel Insights

None beyond the paper’s own contributions. The key insight is that a text-based encoding derived from ONNX graphs, when paired with an encoder LLM, can serve as a search-space-agnostic input for performance prediction, and that adding input connectivity and parameter information is more important than output shapes. The paper also empirically shows that encoder-based LMs (ModernBERT) outperform decoder-based ones (Qwen3) for this structured prediction task.

## Suggestions

- Clarify in the title and abstract that the predictor is currently restricted to CIFAR-10 (or architectures evaluated on CIFAR-10), and mark the cross-dataset experiments as preliminary.
- Add a comparison to a GNN-based predictor trained on the same multi-space ONNX-Bench data, using the ONNX computational graph directly, to disentangle the effect of the encoding from the predictor architecture.
- Validate the choice of ONNX over Python code by including an ablation that converts architectures to Python code strings and trains the same LLM.
- Report the number of parameters and inference latency of the LLM vs. GNN baselines to contextualize “instant” prediction.

## Score and Decision

The paper introduces a valuable benchmark (ONNX-Bench) and a flexible encoding (ONNX-to-text). The experiments are carefully conducted and include useful ablations. However, the validation is restricted to a single dataset (CIFAR-10) and to architectures that are all CNNs, which undercuts the claim of “universal”. The comparison to prior work is limited to a single zero-shot transfer task, and the hypothesized advantage over Python code is not tested. These limitations are significant but not fatal. The paper makes a solid incremental contribution, but the scope of the claims exceeds the evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Borderline Accept</decision>