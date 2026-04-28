# Basis Sharing: Cross-Layer Parameter Sharing for Large Language Model Compression

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 8, 5

## Abstract
Large Language Models (LLMs) have achieved remarkable breakthroughs. However, the huge number of parameters in LLMs require significant amount of memory storage in inference, which prevents their practical deployment in many applications. 
To reduce memory storage of LLMs, singular value decomposition (SVD) provides a promising solution to approximate weight matrices for compressing LLMs. In this paper, we take a step further to explore parameter sharing across different layers with SVD to achieve more effective compression for LLMs. Specifically, weight matrices in different layers are decomposed and represented as a linear combination of a set of shared basis vectors and unique coefficients. The types of weight matrices and the layer selection for basis sharing are examined when compressing LLMs to maintain the performance. Comprehensive experiments demonstrate that 
Basis Sharing outperforms state-of-the-art SVD-based compression approaches and parameter sharing techniques, especially under large compression ratios

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces "Basis Sharing," a method for compressing Large Language Models (LLMs) by sharing basis vectors across different layers. This approach decomposes weight matrices into shared basis vectors and unique coefficients, aiming to reduce memory requirements.

### Strengths
1. The concept of concatenating weight matrices from multiple layers and sharing basis is interesting. It potentially increases the number of ranks to achieve a given compression rate.
2. The performance of the proposed method is better than previous methods on SVD like ASVD or SVD-LLM.

### Weaknesses
1. Seems the paper only considers the two-layer sharing case, it will be stronger if it can be expanded to multi-layers. The key drawback of the previous SVD method is that to achieve a 10% compression rate, for example, it requires pruning 55% of ranks. If more layers can be shared, this challenge can be mitigated to some extent.
2. The paper does not discuss how to allocate non-uniform ranks for SVD decomposition. Non-uniform allocation of ranks has been shown promising in recent works [1]. 
3. The final structure of the model is not presented in the paper. For example, what layers and what operations have been shared in the final compressed model?
4. Compared to pure SVD methods like SVD-LLM, a sharing basis can result in more memory costs or lower throughput since the proposed method can keep a higher rank and thus more active parameters at the inference time.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates the layer sharing of SVD bases across different layers and, based on these insights, proposes a new low-rank compression method. This method demonstrates improved performance compared to previous approaches under the same compression ratios. Plenty of ablation studies and end-to-end throughput are conducted to demonstrate the effectiveness of the proposed methods.

### Strengths
- The studies of basis sharing across different layers is interesting.

- The improvements shown in Table 1 is significant compared with previous baselines. 

- End-to-end throughput are reported to demonstrates the effectivenss of the proposed methods.

### Weaknesses
 - As shown in Table 1, while basis sharing can effectively enhance the performance of compressed models, some performance drop remains—such as a 0.04 decrease at 20% compression and a 0.07 decrease at 30%. Additionally, Figure 6 illustrates that only marginal throughput improvement is observed at a 20% compression ratio, which makes the proposed method less practical, as meaningful efficiency gains are accompanied by performance degradation. The performance drop is not only limited to perplexity, but also observed in common-sense reasoning tasks, which raises concerns about the practical utility of the method.

- It would be good to show whether LoRA fine-tuning can recover the performance on zero-shot common-sense reasoning tasks, rather than perplexity.

- The evaluted models should contains more recent ones, like llama-3.1/3.2.

- The proposed method seems like a layer-sharing and SVD co-design methods for LLM compression. How does such method compared with direct apply layer-sharing and SVD compression, e.g., applying layer-sharing, then SVD or reversely.

### Questions
Is there any insights on why different layers would share the same SVD basis?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces “Basis Sharing,” a method for compressing large language models by sharing basis vectors of SVD across layers, each with unique coefficients.  Basis Sharing significantly reduces model size while maintaining performance. Experiments demonstrate its superiority over traditional SVD-based techniques across various tasks and settings, achieving enhanced efficiency and accuracy at high compression ratios.

### Strengths
* This paper analyzes the feasibility of SVD for different modules and outliers in depth, and designs a simpler and more general SVD compression method for LLM: BASIS SHARING.

* The advantages and robustness of the proposed method are fully verified on various tasks, different scales, software and hardware Settings.

* The presentation of the technical discussion is accurate and well-organized.

### Weaknesses
 * It looks like BASIS SHARING will also have better acceleration in hardware, which I think would be better if compared to other SVD-based methods.

* In this paper, continuous groups are designed based on the interesting insights in 3.2. However, ablation experiments on discontinuous groups are still missing. Is it possible to realize CROSS-LAYER PARAMETER SHARING of functions (such as W_O) that are not suitable for continuous groups through discontinuous groups?

### Questions
* Can this method be used in conjunction with other compression methods (e.g. pruning, quantization, etc.) to go one step further?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel layer-sharing SVD compression strategy for LLMs, building upon previous SVD compression methods. The authors suggest that by sharing the left singular matrix across different layers, the model can achieve better performance. Experiments demonstrate that this method outperforms existing activation-aware SVD compression techniques.

### Strengths
1. The proposed idea of sharing the left singular matrix between layers is insightful. This approach significantly improves the compression ratio of the model.
2. The finding that model performance can be improved through layer sharing is intriguing.
3. The experiments are comprehensive.

### Weaknesses
1. While the paper claims that layer sharing can improve performance, it does not explain why. The paper lacks an explanation of the properties of the weight matrices that enable this improvement, making the conclusion somewhat abrupt and counterintuitive. Specifically, the paper does not discuss the spectral properties of the weight matrices, such as the distribution of singular values, and how these properties might be related to the observed performance gains when sharing singular vectors. A more detailed analysis of the mathematical characteristics of these matrices is needed to support the claims.
2. Sharing left singular vectors may not be applicable to all matrices in the model, which suggests that this is not a general approach. The paper does not provide in-depth analysis of this phenomenon. For instance, the paper should explore how the suitability of layer sharing varies across different types of layers (e.g., attention vs. feedforward) or different positions within the network. Without such analysis, it is unclear how broadly applicable this technique is.
3. Using layer sharing implies that the truncated ranks of both layers are identical, which could limit the model's performance. This constraint may prevent the model from allocating the optimal number of parameters to each layer, potentially leading to suboptimal performance. The paper does not investigate the impact of this rank constraint on model accuracy, nor does it explore alternative strategies for varying the rank across different layers while still sharing singular vectors.

### Questions
1. In the experiments section, the paper provides results for different compression ratios. However, I did not see an explanation in the paper on how the specific compression ratios were determined. Could you provide further clarification? And how did the authors determine the cutoff values ​​for different layers?
2. Could the authors analyze the properties of matrices that can be shared across layers, particularly their mathematical properties, and explain why performance is improved? This result seems should be sensitive to the training data and is counterintuitive, as, in theory, not sharing should provide a higher performance ceiling compared to sharing.
3. Could the authors provide the actual number of layers that can be shared in the model and the compression gains achieved through layer sharing?

### Soundness
3

### Presentation
3

### Contribution
3
