## Human Reviewer 1

### Summary
This paper investigates the challenges of 1-bit Post-Training Quantization (PTQ) for Large Language Models (LLMs). The authors identify three key issues with existing output-matching approaches: (1) layer-wise optimization does not guarantee block-level improvement, (2) quantization errors accumulate across layers, causing the optimization target to drift, and (3) naive output alignment can degrade the attention mechanism. To address these, the paper proposes a new method that introduces two main components: a revised objective function (Eq. 3) that targets the true full-precision output, and an "Attention Matrix Preservation" (AMP) mechanism (Eq. 9) to mitigate attention degradation. This new output-alignment strategy is then selectively applied only to the final fully-connected layer of each transformer block, while retaining a weight-alignment method (ARB-RC) for all other layers.

### Strengths
- The paper's strength lies in its reasonable preliminary analysis. The investigation using Figures 1 and 2 provides why naive output alignment methods like ARB-X fail in the 1-bit regime. 

- The paper tackles the challenging and important problem of 1-bit LLM quantization. The idea of explicitly preserving the token-similarity matrix via the AMP mechanism is a novel approach to counteract the side effects of quantization.

- The paper generally articulates the identified problems and the proposed solutions. The motivations for each component of the method are well-explained.

### Weaknesses
- Lack of Robustness and Unaddressed Failure Cases: The method's stability is highly questionable. In Table 2, the proposed method ("Ours") results in a catastrophic failure on the LLaMA-2-13B model with the PTB dataset, yielding a PPL of 3166. This is a complete model collapse, far worse than the baseline ARB-RC (197.70) and the full-precision model (50.93). The authors fail to acknowledge, analyze, or explain this critical failure point, which undermines the reliability and robustness of the proposed method.

- Limited Scope and Generalizability: The entire paper, from its motivation to its experiments, is confined to the 1-bit case. It is unclear if the identified problems (especially the attention degradation) or the proposed solutions (AMP, selective alignment) are relevant, necessary, or effective for other low-bit settings (e.g., 2-bit, 3-bit, or 4-bit PTQ). This narrow focus significantly limits the generalizability and impact of the contribution.

- Marginal Performance Gains: While the method outperforms baselines in many settings, the significance of this improvement is often marginal. For example, in Table 1 for the OPT-30B model on the PTB dataset, the improvement over the ARB-RC baseline is only 0.13 PPL (16.88 vs. 16.75). This small gain may not justify the added complexity of the proposed method.

- Questionable Practical Utility: The results on modern models like LLaMA-3 (Table 2) show that while the proposed method is relatively better than other 1-bit techniques, the absolute performance is still extremely poor (e.g., PPL degrades from 6.14 to 27.20 on WikiText2). This raises the question of whether the method truly makes 1-bit quantization viable or merely provides a marginal improvement on a still-unusable result.

- Ambiguous Contribution and Complex Design: The proposed method is a complex hybrid. It relies on the baseline ARB-RC (a weight-alignment method) for most layers and applies its new output-alignment objective only to the final FC layer. This makes the true source of the improvement unclear: is it the new objective (Eq. 3 + AMP), or is it the selective hybrid strategy itself? Furthermore, the design feels ad hoc. The paper introduces a new objective (Eq. 3) to fix output alignment, but this objective still appears to have flaws (degrading attention), requiring a second complex "patch" (the AMP mechanism). This "patch-on-patch" design lacks simplicity and suggests that the underlying objective (Eq. 3) remains incomplete.

### Questions
- Could the authors please provide a detailed analysis of the catastrophic failure (PPL 3166) observed for LLaMA-2-13B on the PTB dataset? What causes this instability, and how does it affect the method's reliability?

- Why was the evaluation strictly limited to 1-bit quantization? Do the authors have any preliminary data or analysis on how this method (particularly the AMP mechanism) performs in 2-bit or 4-bit settings?

- To clarify the contribution: What is the performance if the new objective (Eq. 3 + AMP) is applied to all layers instead of just the final FC layer? This ablation is crucial to understand if the new objective is genuinely superior or if the hybrid strategy is simply masking its failures in other layers.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper addresses the challenge of 1-bit post-training quantization (PTQ) for large language models, where existing methods often suffer substantial performance drops. The authors analyze why output alignment strategies fail, identifying issues such as block-level mismatch, error accumulation, and disruption of attention patterns. To overcome these limitations, they propose a data-aware quantization framework that selectively applies output alignment at the block level, explicitly accounts for accumulated errors, and incorporates a novel Attention Matrix Preservation (AMP) mechanism to maintain attention behavior. Extensive experiments on OPT and LLaMA families demonstrate that the method consistently outperforms prior 1-bit PTQ approaches across perplexity and zero-shot evaluation benchmarks.

### Strengths
The paper provides a careful analysis of why naïve output alignment is insufficient for 1-bit PTQ and proposes a data-aware alternative. The ideas are clearly presented, and the experimental results on OPT and LLaMA suggest performance benefits over existing approaches.

### Weaknesses
1. The evaluation is limited to OPT and early LLaMA families; it is uncertain whether the method extends to newer and more competitive open-source models (e.g., Qwen3, Qwen2.5).
2. Although the proposed Attention Matrix Preservation (AMP) is intuitively appealing, its ablation results are somewhat limited, leaving open how much it contributes across diverse tasks and model sizes.
3. The approach focuses primarily on perplexity and a few zero-shot tasks; broader evaluations, such as some math or code tasks, could better demonstrate practical value.
4. The paper provides less discussion on computational overhead and scalability, particularly how the data-aware strategy affects quantization cost for very large models.

### Questions
1. Can the authors evaluate their method on newer open-source LLMs such as Qwen3 or Qwen2.5 to demonstrate broader applicability?
2. Could the authors provide more detailed ablations on the AMP component, especially across different tasks and model sizes, to better establish its contribution?
3. How does the method perform on more diverse benchmarks, for example, math reasoning or code generation tasks, beyond perplexity and basic zero-shot evaluations?
4. Can the authors elaborate on the computational overhead and scalability of the proposed data-aware strategy, particularly when applied to very large models?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper investigates the problem of 1-bit PTQ for LLMs. The authors revisit the commonly adopted output alignment objective and analyze why naive layer-wise output matching (ARB-X) fails to improve block-level performance. They identify three key factors—accumulated quantization error, inter-layer dependency, and attention distortion—and propose a selective layer-wise output alignment strategy combined with an AMP mechanism. Experimental results on OPT and LLaMA models show consistent perplexity reductions and modest zero-shot QA improvements over recent 1-bit PTQ baselines (ARB-X, ARB-RC, BiLLM, PB-LLM).

### Strengths
The paper provides a empirical and analytical investigation of why prior output-alignment–based 1-bit PTQ methods (e.g., ARB-X) fail, which is well-motivated.

### Weaknesses
- The proposed method appears incremental over ARB-X rather than conceptually new.
- The so-called selective layer-wise output alignment is effectively applied only to the last fully connected layer in each block. While this choice is empirically justified, it is unclear whether such a fixed single-layer focus warrants the term “selective.”
- Although framed as a 1-bit quantization method, the overall design and mathematical formulation (e.g., output-error objective, AMP) are not inherently specific to the binary regime. The method may generalize to general PTQ settings, which somewhat weakens the claimed “1-bit-only” contribution.
- The experimental scope is relatively narrow: evaluation relies mainly on perplexity metrics and a few commonsense QA datasets. Broader open-ended generation or reasoning tasks could strengthen the claim that the method fundamentally mitigates 1-bit quantization degradation in realistic LLM usage.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This work combines ARB-X and ARB-RC, partially addressing ARB-RC's inability to aware calibration data through approximate solutions. Furthermore, the authors revise the quantization objective to make the quantized output more closely match that of the full-precision version. In addition, they incorporate an AMP mask into the updated formula to prevent performance decline in the attention mechanism. Finally, the authors apply their approach to the last fully connected layer of each block, while keeping ARB-RC in all other layers. Experiments demonstrate that this approach attains a marginal improvement over ARB-RC.

### Strengths
1. The authors provide a thorough analysis of the errors introduced by quantization, revealing that smaller layer-wise errors do not necessarily translate into smaller block-wise errors, which more accurately reflect the model's ultimate performance.
2. The article provides a detailed derivation of the formulas, with rigorous notation.

### Weaknesses
1. The final performance improvement compared to the previous state-of-the-art method was only 0.78%, raising concerns about the effectiveness of the method.
2. The proposed method was only applied to the last fully connected layer in each transformer block; all other layers still used ARB-RC. In the ablation experiments in Table 5, the authors' method performed even worse than ARB-RC when applied to layers other than the final FC layer, demonstrating the limitations of their proposed method.

### Questions
1. The analysis of the impact of quantization error on the attention mechanism in Section 3.3 is confusing. The true attention mechanism's token similarity is calculated by mapping token representations using two different matrices, W_q and W_k . The authors simplify this analysis by reducing the calculation of token similarity to the result of a single matrix mapping. Is this a reasonable approximation? Does it reflect the impact of quantization on the true attention mechanism?
2. The ablation experiments on AMP in Table 3 show that the update method without AMP even leads to larger errors than ARB-RC, particularly on LLaMA-2-7B. Do the authors have a reasonable explanation for this?
3. Does the hyperparameter k in Table 8 correspond to the number of iterations? More explanation is needed to clarify this.
4. Regarding the time cost of quantization, do the authors use 5 iterations for their method, while the comparison method uses 15? Perhaps a comparison using the same number of iterations would be more reasonable. Since their method is much more complex than ARB-RC, the speedup achieved by quantization (Table 6) is confusing.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5
