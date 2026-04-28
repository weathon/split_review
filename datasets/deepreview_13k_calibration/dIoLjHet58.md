# Generalized Probabilistic Attention Mechanism in Transformers

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
The Transformer architecture has become widely adopted due to its demonstrated success, attributed to the attention mechanism at its core. Despite these successes, the attention mechanism of Transformers is associated with two well-known issues: rank-collapse and gradient vanishing. In this paper, we present a theoretical analysis that it is inherently difficult to address both issues  simultaneously in the conventional attention mechanism. To handle these issues, we introduce a novel class of attention mechanism, referred to as generalized probabilistic attention mechanism (GPAM), and its dual-attention implementation within the Transformer architecture. Unlike conventional attention mechanisms, GPAM allows for negative attention scores while preserving a fixed total sum. We provide theoretical evidence that the proposed dual-attention GPAM (daGPAM) effectively mitigates both the rank-collapse and gradient vanishing issues which are difficult to resolve simultaneously with the conventional attention mechanisms. Furthermore, we empirically validate this theoretical evidence, demonstrating the superiority of daGPAM compared to other alternative attention mechanisms that were proposed to address the same issues. Additionally, we demonstrate the practical benefits of GPAM in natural language processing tasks, such as language modeling and neural machine translation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new attention mechanism that replaces the attention scores. The attention scores in softmax for each query are a convex sum, so scores must be positive. They argue for using an affine sum which also sums to 1 but allows for negative scores.

They are motivated by rank collapse and gradient vanishing. Rank collapse is mitigated since the negative sums introduce more diversity. They show that gradient vanishing is a related problem.

To validate their method they perform several small scale benchmarks, namely perplexity and translation and find their methods improve against the baselines.

### Strengths
The method and presentation are good. They give intuitive, theoretical and experiential justification of the ideas.

The experiment results improve over the baseline.

### Weaknesses
The range of evaluations is pretty limited and extra computation is needed.

A benchmark against just increasing the number of attention heads would be useful.

### Questions
How does the method work in long context scenarios? Even a simple benchmark like Long Range Arena would be helpful. My intuition feels like there should be a larger improvement.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose daGPAM -- an attention module that computes an additional negative coefficient attention matrix aiming to solve rank collapse and vanishing gradients in transformers.

### Strengths
- The paper includes theory on how daGPAM can reduce rank collapse and vanishing gradients. It does so by showing the residual norm of daGPAM and also its gradient is greater than the respective values for vanilla attention (the original values for attention having been computed by [[Dong et al](https://proceedings.mlr.press/v139/dong21a.html)]).
- The paper is well written and easy to follow, and contextualizes relevant work well.

### Weaknesses
 - I think the downstream experiments for this paper could be fleshed out more. I appreciate that some sort of comparison with alternative attention mechanisms like CoDA is present, but I think only having these comparisons on PTB is insufficient. So many attention variants have been proposed over the years, and none have really taken hold, so I think the empirical bar should be high for current and future variants. Even though this paper shows evidence of reducing rank collapse, rank collapse is ultimately something that matters as it reflects in downstream performance, so I think rank collapse on its own is not enough in the absence of strong empirical results. I think this could be addressed by the authors including more attention variants (CoDA etc) in the LM and NMT experiments.

 - I think the connection between rank collapse and downstream performance needs to be more explicitly demonstrated. While the paper provides theoretical arguments and some empirical evidence of reduced rank collapse, the practical implications for downstream tasks are not sufficiently clear. The paper would benefit from a more direct analysis showing how the degree of rank collapse correlates with performance on downstream tasks. Without this direct correlation, it is difficult to assess the practical value of the proposed method.

### Questions
- Do the authors believe other attention variants solve the rank collapse / vanishing gradients problem, and can this be experimentally validated?
- How does rank collapse (Figure 4) reflect in downstream performance? It would be interesting to see that a higher degree of rank collapse results in lower downstream results, but without this correlation it is hard to reason about the value of reducing rank collapse.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces GPAM, an attention mechanism that allows negative attention scores while maintaining a fixed sum, addressing both rank-collapse and gradient vanishing problems in Transformers. Their proposed dual-attention GPAM (daGPAM), adds a negative attention matrix computation alongside the original one, requiring small additional parameters. The authors show the theoretical advantage of their model and examine their models on language tasks.

### Strengths
1. The writing is easy to follow
2. The paper shows quite interesting results gradient vanishing and rank-collapse is hard to solve simultaneously total norm of gradients is maximized can lead to rank-collapse.
3. The authors theoretically show that their method can mitigate both the rank-collapse issue and reduce the the gradient vanishing problem.

### Weaknesses
My main concerns are:
1. The improvement of daGPAM is very marginal, and not significant in both Language modeling (on Wikitext-103 and Enwiki8, the improvement is around 0,5 PPL) and machine translation tasks (on IWSLT14 and WMT14, maximum improvement is around 0.7% BLEU score.) The reported perplexity improvements of 0.5 PPL on Wikitext-103 and Enwiki8 are not substantial enough to justify the added complexity. Similarly, the 0.7% BLEU score increase on IWSLT14 and WMT14 is also quite small and could be attributed to random variation or hyperparameter tuning of the baseline models. The lack of significant gains raises questions about the practical utility of the proposed method.
2. Computational cost: the dual-attention structure requires computing two attention matrices instead of one, which is very inefficient. The marginal improvement does not justify this performance-efficiency trade-off. The computational overhead of calculating two attention matrices, instead of one, significantly increases the processing time and memory requirements. Given the small performance gains, this added computational cost makes the daGPAM approach less practical for real-world applications, especially when compared to standard attention mechanisms.

### Questions
1. The optimal $\lambda^{+}$ and $\lambda^{-}$ values seem to vary across different tasks. Can the authors provide an ablation study on choosing different settings of the hyper-params. 
2. Can the authors provide the inference time and memory cost of the model?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Despite the success of Transformers, the standard attention mechanism is associated with two well-known issues: rank-collapse and gradient vanishing. This paper proposed generalized probabilistic attention mechanism (GPAM) to mitigate both the rank-collapse and gradient vanishing issues simultaneously. Evaluation results on real-world datasets demonstrate the effectiveness of GPAM.

### Strengths
This paper studies how to alleviate the rank-collapse and gradient vanishing problems in standard attention mechanism, which is an important problem of profound implication in practice. Authors provided a concrete analysis on the intrinsic trade-offs between avoiding rank-collapse and gradient vanishing in standard attention mechanism and showed that GPAM is able to mitigate both problems simultaneously. The theoretical analysis in this paper seems solid and the presentation is clear.

### Weaknesses
Evaluation in this work can be significantly improved. Given the prevalent success of Large Language Models (LLMs) on various advanced tasks (e.g., solving math and coding problems), evaluation on only small language models (20M-200M) and classic NLP tasks (e.g., neural machine translation) seems insufficient. More evaluation results on open-sourced LLMs (e.g., Llama-3 or Phi-3 family) and widely used benchmarks (e.g., MMLU or GSM8K) will add great values to this paper. The current evaluation does not fully demonstrate the practical impact of the proposed method, especially considering the computational overhead of the dual-attention mechanism. The reported 1% improvement in perplexity is marginal, and it is not clear if this improvement justifies the added complexity and computational cost of the proposed approach. Specifically, a roughly 1% improvement on PPL is not significant enough given that the proposed approach has approximately 1% more parameters (Line 450-451). Furthermore, the paper lacks a detailed analysis of the computational cost associated with the proposed generalized probabilistic attention mechanism (GPAM), particularly the dual-attention variant (daGPAM). This is crucial because the added complexity might limit its applicability in resource-constrained environments or large-scale models. The paper should also explore the sensitivity of the model to the hyperparameter λ, as the performance might vary significantly with different values of λ. In Line 250, the range for PG should be [1 - \lambda^-, 1 + \lambda^+].

### Questions
Q1. Empirical improvements seem quite marginal according to Table 1. Specifically, a roughly 1% improvement on PPL is not significant enough given that the proposed approach has approximately 1% more parameters (Line 450-451).

Q2. In Line 250, the range for PG should be [1 - \lambda^-, 1 + \lambda^+].

### Soundness
3

### Presentation
3

### Contribution
3
