# Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Attention layers are the core component of transformers, the current state-of-the-art neural network architecture. However, \softmaxx-based attention puts transformers' trainability at risk. Even \textit{at initialisation}, the propagation of signals and gradients through the random network can be pathological, resulting in known issues such as (i) vanishing/exploding gradients and (ii) \textit{rank collapse}, i.e. when all tokens converge to a single representation \textit{with depth}. This paper examines signal propagation in \textit{attention-only} transformers from a random matrix perspective, illuminating the origin of such issues, as well as unveiling a new phenomenon---(iii) rank collapse \textit{in width}. Modelling \softmaxx-based attention at initialisation with Random Markov matrices, our theoretical analysis reveals that a \textit{spectral gap} between the two largest singular values of the attention matrix causes (iii), which, in turn, exacerbates (i) and (ii). Building on this insight, we propose a novel, yet simple, practical solution to resolve rank collapse in width by removing the spectral gap. Moreover, we validate our findings and discuss the training benefits of the proposed fix through experiments that also motivate a revision of some of the default parameter scaling. Our attention model accurately describes the standard key-query attention in a single-layer transformer, making this work a significant first step towards a better understanding of the initialisation dynamics in the multi-layer case.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the issue of rank collapse in softmax attention. While the well-known rank collapse in depth is discussed, the authors also identify a new variant: rank collapse in width. By modeling softmax-based attention at initialization using Random Markov matrices, the paper pinpoints the root cause of the problem as the spectral gap between the two largest singular values of the attention matrices. By eliminating this spectral gap, the issue of rank collapse has been effectively resolved.

### Strengths
The finding is interesting and the solution is simple.

### Weaknesses
1. I propose that the current introduction section be divided into two distinct parts: an introduction section and a preliminary section. The introduction should encompass the existing situation, motivation, a succinct overview of the proposed solution, and the results obtained. The preliminary section should offer the necessary background knowledge essential for understanding the paper.

2. The phenomenon of width collapse is frequently observed in current transformer training, or it may necessitate specific data conditions to manifest. While transformers have been extensively utilized in domains such as computer vision (CV) and natural language processing (NLP) for several years, reports of width collapse remain absent. Given that the proposed method solely addresses this width collapse, I am interested in its actual efficacy in real-world applications.

3. The proposed solution involves the direct substitution of A with its variant within the attention layer. However, the performance implications of this adjustment have not been comprehensively validated. The author has provided only a comparison of training loss, indicating that this modification may influence the training loss curve. I would appreciate the inclusion of ablation studies conducted on actual transformer models in either language modeling (LM) or CV tasks. For example, in the case of LM, it is essential to supply benchmark results within controlled scenarios. Furthermore, it would be beneficial to understand how this modification may affect both training and inference speed.

4. I understand this paper only investigates the rank collapse in softmax attention transformers. However, I am curious whether this problem exists in other attention variants, such as linear attention.

### Questions
As above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, by analyzing the spectral gap in the eigenvalues of the attention matrix, we reveal the rank collapse in width that exists in the classical transformer structure, and point out that this phenomenon leads to the disappearance of the training gradient as well as the rank collapse, which in turn causes the training instability of the transformer, and subsequently The corresponding solutions are given in this paper.

### Strengths
1. The paper is logically organized, with a clear theoretical narrative and a high degree of readability
2. This paper approaches the issue of Transformer performance from a relatively rare angle, pointing out that rank collpase occurs not only as the number of layers (“depth”) of the transformer increases, but also as the “width” of the It is pointed out that rank collpase occurs not only with the increase of the number of layers (“depth”) of the transformer, but also with the increase of the “width”, and also leads to the emergence of training instability, and further pointed out the causes and solutions, which is of high theoretical significance.

### Weaknesses
1. What is discussed in this paper has strong theoretical implications, but is studied in the context of an extremely simplified Transformer model, and it is not possible to determine whether the phenomenon also exists for various types of Transformer model variants, such as linear transformer. It is also difficult to determine whether the problem also occurs in transformer models that add many tricks to mitigate rank collpase in depth.
2. Taking up the weakness 1, although this paper is of high theoretical significance, it is hoped that the authors' experiments will reflect whether the various Transformers in practical use have similar problems, or, under what circumstances similar problems may affect the results.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- The study reveals that softmax-based attention mechanisms during the initialization of Transformers can cause pathological signal and gradient propagation through the network, manifesting as vanishing/exploding gradients and rank collapse—where all tokens converge to a single representation at depth.
- This paper identifies and analyze rank collapse in width, which is caused by the spectral gap between the two largest singular values in the attention matrix.
- A solution is proposed to address the rank collapse and exploding gradients issues.

### Strengths
- The paper is clearly written and well organized
- This paper provides a novel concept named rank collapse in width, advancing understanding of initialization issues. I.e, the gap between the largest eigen value and other eigen value bulk will lead to rank collapse, preventing the processing of input tokens.
- Rigorous analysis is provided about the reasons of gap, how gap leads to randk collapse and exploding gradients.
- A reasonable solution is proposed to deal with the rank collapse, in which, rank-one perturbation is removed from every attention matrix to close the gap. The effectiveness of this solution is analyzed in Proposition 5, 6.
- extensive experiments are provided to support the analysis.

### Weaknesses
 - The analysis is based on simple model structure with attention-only single-head transformer. Analysis on more complex models with multiple layers, skip connections and layernorm is preferred. Specifically, the impact of these architectural choices on the spectral gap and rank collapse should be investigated. For instance, how does the presence of skip connections, which introduce a direct path for information flow, affect the convergence of token representations? Similarly, the role of layer normalization in stabilizing the variance of activations and its interplay with the observed rank collapse warrants further exploration.
- The paper assumes Gaussian-distributed initialization for parameters, which is not always optimal in practice. Transformers often use Xavier or He initialization, will the results still hold? The analysis should consider how different initialization schemes affect the spectral properties of the attention matrices and the resulting rank collapse. For example, Xavier initialization, which aims to maintain consistent variance across layers, might have a different impact on the spectral gap compared to Gaussian initialization. It is important to understand if the observed phenomena are robust across different initialization strategies.
- lack empirical validation. Most experiments are conducted to evaluate the rank collapse, gradient exploding and loss curve, there are limited experiments on real datasets and across different tasks. The paper should include experiments on benchmark datasets for tasks such as machine translation or text classification to demonstrate the practical implications of the proposed analysis and solution. The current experiments, while insightful, do not provide sufficient evidence of the real-world applicability of the findings.
- The paper analyzes the initialization stage of transformers without considering parameter updating during training. Spectral properties change over training, and over multi-layer transformers, which may significantly affect rank collapse and gradient stability analysis in this paper. The analysis should consider how the spectral gap evolves during training and how this affects the stability and convergence of the model. For instance, does the spectral gap tend to close or widen during training, and how does this relate to the model's performance?

### Questions
Does the rank collapse and gradient exploding also exist in the existing pre-trained large language models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript studies the self-attention mechanism at initialization through free probability and random matrix theory. Free probability deals with non-commuting random variables such as random matrices, making it a good fit for the analysis of attention matrices in transformers. The attention matrices are usually large due to numerous tokens, thus the corresponding spectral properties become predictable. In particular, the eigenvalues of softmax-attention matrix at the first layer are similar to the ones of the random Markov matrix - there is an outlier eigenvalue that equals one while the remaining eigenvalues form a bulk centered at zero with radius $T^{-0.5}$. The manuscript then links this discrepancy in eigenvalues, referred to as spectral gap, with rank collapse and exploding gradients. Fixing these issues could improve the optimization. Thus, the manuscript proposes a solution that adapts the softmax-attention matrix in order to remove the spectral gap. Namely, 1/T is subtracted from each element of the square attention matrix, where T is the matrix dimension. This solution is validated in toy experiments with multi-layer transformers. The experiments indicate that the proposed solution is effective in slowing rank collapse when the spectrum contains a single outlier.

### Strengths
S1. Viewing softmax-attention matrices as random Markov matrices and analysing them via free probability seems like a sound approach.

S2. Explaining rank collapse and exploding gradient with the spectral gap (i.e. discrepancy in eigenvalues) is an interesting takeaway.

S3. The proposed solution for mitigating the spectral gap is convenient and easy to implement.

S4. Experiments indicate that the proposed solution slows the rank collapse.

### Weaknesses
W1. The proposed analysis holds only for the first layer attention matrix. This limits the usefulness of the proposed analysis. Could the proposed analysis incorporate the attention matrices in deeper layers? What are the key issues?

W2. Removing the spectral gap does not benefit optimization in transformers with two layers, as indicated by the bottom row of Figure 6. What happens in the case of even deeper transformers? Does the removal of the spectral gap have any practical relevance?

W3. Figure 8 and the corresponding text raise questions about the validity of Xavier's initialization. However, this analysis is conducted only for a single-layer transformer (line 488). Can we observe the same issues with initialization in deeper transformers?

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
