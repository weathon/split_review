# nGPT: Normalized Transformer with Representation Learning on the Hypersphere

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
We propose a novel neural network architecture, the normalized Transformer (nGPT) with representation learning on the hypersphere. In nGPT, all vectors forming the embeddings, MLP, attention matrices and hidden states are unit norm normalized. The input stream of tokens travels on the surface of a hypersphere, with each layer contributing a displacement towards the target output predictions. These displacements are defined by the MLP and attention blocks, whose vector components also reside on the same hypersphere. Experiments show that nGPT learns much faster, reducing the number of training steps required to achieve the same accuracy by a factor of 4 to 20, depending on the sequence length.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Motivated by previous findings on the advantages of representation learning on a hypersphere, the authors propose a novel neural network architecture called the normalized Transformer (nGPT). In nGPT, all vectors—including embeddings, MLP outputs, attention matrices, and hidden states—are normalized to ensure they reside on the same hypersphere. This setup ensures that each token in the input sequence, during optimization, starts at a position on the hypersphere defined by its input embedding and moves on the surface of the hypersphere to a point that best predicts the embedding of the next token. Experiments on the OpenWebText dataset demonstrate that nGPT learns significantly faster, reducing the number of training steps needed to achieve performance comparable to baseline models.

### Strengths
The paper is well-written and well-structured. The pair-wise comparisons in Section 2 make it easy to understand the architectural modifications, with clear motivation and explanations for each change.

The comprehensive experiments and ablation studies effectively demonstrate the method's effectiveness. The experimental results are impressive.

### Weaknesses
Minor: The per-step time of nGPT is approximately 80% higher for a 4k context and 60% higher for an 8k context, primarily due to additional normalization steps. However, Table 6 shows that removing the normalization for q and k only slightly affects performance, suggesting a potential way to reduce overhead.



### Questions
**Q1:** The authors comment on the average magnitudes of $\alpha_A$ and $\alpha_M$, noting that $\alpha_M$ has a higher average magnitude than $\alpha_A$, implying their suggestions more precise. could the authors the authors elaborate on this point in more detail?

**Q2:** Previous research has demonstrated that representation learning on a hypersphere enhances training stability, with experiments and ablations confirming stable activations, gradients, and weights, as well as showing gradient descent acting as a meta-optimizer. The 4-20x speedup achieved by the normalized Transformer is impressive, and further intuition or analysis on the factors contributing to this acceleration would be valuable.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel neural network architecture, the normalized Transformer (nGPT) with representation learning on the hypersphere, and empirically shows that nGPT learns significantly faster, cutting down the training steps needed to reach comparable accuracy levels.

### Strengths
- The paper is well-written, and the related work section is presented clearly.

- The experimental results are solid and convincing.

### Weaknesses
 - I do not find any major weaknesses. My only concern is that, in essence, the method involves normalizing everything to unit, functioning as an embedding layer within architectures, with empirical results demonstrating its effectiveness. Although hypersphere normalization in representation learning is introduced and applied, the paper provides a clear discussion of related papers.

### Questions
I have no question.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel architecture called the normalized Transformer (nGPT), which performs learning on a hypersphere. By normalizing parameters and output features, such as embeddings, MLPs, and attention layers, and introducing learnable scale parameters, the model enables effective representation learning on the hypersphere. The model demonstrates faster convergence compared to GPT, even without using conventional techniques like weight decay and learning rate warmup, in models with 0.5B and 1B parameters.

### Strengths
- Fast convergence in training is practically important for saving computational power, and this paper aims to offer a meaningful solution through the proposed architecture, nGPT.
- The model is carefully designed to prevent loss of expressiveness by introducing appropriate scaling parameters when applying existing results on the effectiveness of representation learning on the hypersphere on Transformers.
- Detailed ablation studies are conducted on the newly introduced learnable parameters, $\mathbf{s}_{qk}$, $\mathbf{s}_u$, $\mathbf{s}_v$, and $\mathbf{s}_z$, demonstrating that nGPT is robust to the introduced scale parameters.

### Weaknesses
 - Many variations of the Transformer architecture have been proposed, but they have generally failed to successfully replace the original Transformer. This is because they have not demonstrated the scalability inherent in the original Transformer. In this paper, scalability also cannot be verified as performance has not been tested on models widely used at the 7B parameter scale or above.
- As the authors mentioned, nGPT requires an additional computation time of 80% for 4k and 60% for 8k context in a single iteration. While the authors argue that this can be reduced through code optimization, such as fused ops, the normalization of all matrices and embeddings at the beginning of each step would not benefit from fused ops, and GPU communication costs would arise with larger models. Verification of actual wall-clock time on larger models is necessary.
- The authors experimentally show that nGPT has length extrapolation ability in addition to fast convergence, but there is no discussion as to why nGPT possesses this property. Adding insights into this aspect could greatly benefit future research.

### Questions
- There are existing studies, such as Bachlechner et al. (2021), that demonstrate fast convergence speeds in Transformer. It would be helpful to see how nGPT compares with these previous studies.
  - Bachlechner et al., “ReZero is All You Need: Fast Convergence at Large Depth”, UAI 2021
- An interesting aspect of nGPT is the linear interpolation between the output of the attention and MLP blocks and the hidden state $h$ in Section 2.2.2. The authors used linear interpolation as shown in Equation (7), but I am curious why they did not consider directly using geodesic interpolation from Equation (6).
- It seems that the bold $\alpha$ in Equation (9) should be corrected as $\alpha$.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed the normalized Transformer (nGPT), which normalizes all vectors forming the embeddings, MLP, attention matrices, and hidden states into unit norm to travel the tokens on the surface of a hypersphere via optimal scaling factors, trainable scaling parameters, and a variable-metric optimizer, resulting in faster convergence.

### Strengths
* The proposed method was well explained, and it is clear how to convert the original Transformer to the normalized Transformer.

* The correctness of each component of the proposed methods was validated through the comparison of experimental results with the original method.

* This paper proposed a variable-metric optimizer that employs LERP and eigen learning rates. This method allows the optimizer to identify an effective learning rate and discard the weight decay.

* This paper identified the appropriate scaling factor to mitigate potential risks associated with applying diverse normalization in Transformer. The proposed approach appears to improve the convergence rate of normalized Transformer.

### Weaknesses
 **Weakness 1.** *Section 1. Introduction* provided a general overview of normalization and representation learning on the hypersphere within the context of Transformer. However, the research problem that this paper addresses and the rationale behind its significance are not sufficiently highlighted. It should be considered to emphasize these aspects before introducing the paper's contributions.

**Weakness 2.** This paper presents two novel components: one is LERP and eigen learning rates, and the other is the identification of an appropriate scaling factor. The other components, such as the normalization of all matrices and the trainable scaling factor, could be regarded as an integration of diverse normalization techniques (Weight Normalization [1], Feature Normalization [2], NormFormer [3]) and scaling parameter tuning on normalized vectors [1,4]. To further enhance the novelty of this paper, it is recommended that the novel components be validated theoretically or experimentally (e.g., experimentally validate how much the LERP approximates the SLERP after training) and that the normalized Transformer be compared with previous normalization methods, (i.e., describes the difference with other normalization techniques)

**Weakness 3.** This paper proposed numerous ablation experiments to investigate the impact of scaling factors and learnable scaling parameters on model performance. However, it seems essential to conduct an ablation study of the components of the normalized Transformer to gain a comprehensive understanding of the influence of each component on model performance.

### Questions
**Question 1.** Why nGPT converges faster than the original Transformer? Experimentally, the faster convergence of the normalized Transformer was confirmed, but it was not clearly explained why

**Question 2.** The rationale behind the approximation of the SLERP by LERP needs to be clarified. While the motivation and theoretical background are well explained, the purpose and reason behind this approximation still need to be clarified. Is there any reason not to use SLERP with normalization? Or, is there any benefit to using LERP instead of SLERP?

**Question 3.** The benchmarks used in the experiments solely encompass common sense reasoning and word/sentence prediction. Are the authors convinced that the experimental results are enough to indicate the versatility of the normalized Transformer in other NLP tasks? If so, I would like to know the rationale behind this conclusion.

---

**Things to improve the paper that did not impact the score**:

* [line 88] nGPT appeared before defining what it is

* This paper explained how to build it, summarized the modifications, and described hyperparameter settings in detail. Also, the normalized Transformer is easy to be implemented. However, it is recommended to publicly open the code for reproducing the paper's results.

* The structure of the paper -- which divides the proposed method into its constituent components and presents these as separate sections, and then introduces and compares the proposed method in a sequential manner -- is not a common one. This structure facilitates the reader's comprehension of the proposed method as comparing it with the baseline. However, this structure may be perceived as somewhat akin to that of a technical report. It would be advisable to restructure the paper.

* In [4], the use of a single trainable scale parameter on normalized vectors within a matrix has potential to facilitate an examination of the training behavior exhibited by the model. It may be advantageous to consider the implementation of a single trainable scale parameter for each layer or attention within the normalized Transformer. Could this method result in the generation of superior outcomes compared to those observed previously?

---

[1] Salimans, T., & Kingma, D. P. (2016). Weight normalization: A simple reparameterization to accelerate training of deep neural networks. _Advances in neural information processing systems_, _29_.

[2] Yaras, C., Wang, P., Zhu, Z., Balzano, L., & Qu, Q. (2022). Neural collapse with normalized features: A geometric analysis over the riemannian manifold. _Advances in neural information processing systems_, _35_, 11547-11560.

[3] Shleifer, S., Weston, J., & Ott, M. (2021). Normformer: Improved transformer pretraining with extra normalization. _arXiv preprint arXiv:2110.09456_

[4] Hoffer, E., Hubara, I., & Soudry, D. (2018). Fix your classifier: the marginal value of training the last weight layer. _arXiv preprint arXiv:1801.04540_.

### Soundness
3

### Presentation
3

### Contribution
3
