# Efficient Source-Free Time-Series Adaptation via Parameter Subspace Disentanglement

- Decision: Accept
- Avg Score: 6.17
- Scores: 6, 10, 5, 5, 6, 5

## Abstract
In this paper, we propose a framework for efficient Source-Free Domain Adaptation (SFDA) in the context of time-series, focusing on enhancing both parameter efficiency and data-sample utilization. Our approach introduces an improved paradigm for source-model preparation and target-side adaptation, aiming to enhance training efficiency during target adaptation. Specifically, we reparameterize the source model's weights in a Tucker-style decomposed manner, factorizing the model into a compact form during the source model preparation phase. During target-side adaptation, only a subset of these decomposed factors is fine-tuned, leading to significant improvements in training efficiency. We demonstrate using PAC Bayesian analysis that this selective fine-tuning strategy implicitly regularizes the adaptation process by constraining the model's learning capacity. Furthermore, this re-parameterization reduces the overall model size and enhances inference efficiency, making the approach particularly well suited for resource-constrained devices. Additionally, we demonstrate that our framework is compatible with various SFDA methods and achieves significant computational efficiency, reducing the number of fine-tuned parameters and inference overhead in terms of MACs by over 90\% while maintaining model performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presented a Tucker-style tensor factorization as a low-rank decomposition of source-pretrained models for time-series data. This method enables a selective fine-tuning of the core tensor on the target side, effectively improving the efficiency.

### Strengths
I think the topic of the article is cutting-edge. The article as a whole uses rich methods such as PAC-Bayes to expound the effectiveness of the proposed method. The supplementary materials are also very detailed in explaining the article, such as the derivation of the formal bound parameter distance. The experiments are sufficient, and the effects shown in the experiments are good. The elaboration and analysis of limitations are also very sufficient.

### Weaknesses
1. In my opinion, in the Related Work section, what is shown is more accurately ablations rather than the so-called observations in the title. Compared to this experimental result, it is more necessary to simply explain why Tucker-style decomposition is used instead of other decomposition methods you have exemplified.
2. I think the insights in lines 201-204 need a more complete explanation. From Equation 1, I can only understand that the linear operation in deep learning is the so-called sequence of linear suboperations in the forward process. However, I cannot directly confirm whether such a description is also accurate for the backward process. If there are relevant formula derivations or proofs, references can be provided. If not, considering the space limitation, it is best to prove it in the Appendix. Because this claim is the premise of Equations 4, 5, and 6 later, which is necessary and important for understanding this method.
3. A small mistake. In the sentence after Eq3, on line 221, after “where”, it should be an explanation of the symbol V in Equation 3 instead of U.
4. On line 238, “Building on these insights, we decompose the pre-trained source model weights using Tucker decomposition”. Although the expression here is rigorous. Logically, the former is a necessary condition for the latter. From the beginning of the article until now, there is no sufficient reason given for why Tucker decomposition is used instead of other decomposition methods. Even if it is mentioned earlier, it is better to emphasize it again here.

### Questions
Lines 248-252, why is fine-tuning for 2-3 epochs? Is this number closely related to the dataset and model scale? I am not very familiar with this field and hope that relatively rigorous evidence can be given here in the text.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This work introduces a method for source-free domain adaptation (SFDA) in the domain of time-series data. The task poses a challenge due to two main reasons: 1) the model has access only to unlabeled data and the source-pretrained model but not the source data, and 2) finetuning with small amounts of unlabeled data in this domain often results is overfitting. This papers explore the method of applying Tucker-style factorization, by breaking the parameters into two parts: core-tensors and factor matrices. By doing so and selectively finetune only on the core-tensor matrix, the model shows little signs of overfitting and improved generalization. Empirically, experiments from changing the rank fo the decomposed tensor to comparisons with current popular adaptor methods show the proposed method is effective at reducing overfitting and improving generalization with fewer parameters, achieving the best of both worlds. Finally, the authors provided a PAC-Bayes generalization bound, showing that the test loss is upper bounded by the empirical loss plus the regularization effect from the matrices learned.

### Strengths
The problem presented at this paper is of great significance, with considerations about the challenges of finetuning the full model and application of on-device settings. The authors have done a great job in both the introduction and method motivating the problem and stating the importance and relevance of this research problem. The method is clear, with definitions and equations clearly defined and laid-out. The method proposed itself is sound also. The authors also try to draw connections with related works to Lottery Ticket Hypothesis, as an attempt to justify why their method works well and is able to achieve the best of both worlds; This connection is a nice touch and welcomed. Experiments-wise, the paper has done a thorough job in demonstrating the effectiveness of their method, with sufficient number of datasets and models, and comparisons with state-of-the-art methods that show clear improvements.

### Weaknesses
A weakness of this work can be characterized as a missing link between the entire method and the time-series aspect of the problem. Specifically, it’s not entire clear why the method here is specifically applied to time-series, as the authors have setup here. Perhaps the authors can clarify how their method has leverage properties in time-series data to their advantage. If this connection is indeed not mentioned, then it seems reasonable to add a sentence or a section in the Appendix justifying this.

### Questions
1. Can the authors comment on the time for inference before and after factorization? Does the smaller number of parameters reduce the time required for inference? Or does the increased number of matrix factorization increase the time required?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers SFDA using Tucker style decomposed weights and selective fine tuning on target data. Some bounds are presented for this strategy and experimental results are shown.

### Strengths
The proposed method can be integrated with several baselines SFDA methods to improve adaptation efficiency.

### Weaknesses
1. Cite and compare with:
- Tang et al, Source-Free Domain Adaptation with Frozen Multimodal Foundation Model, CVPR 2024
- Litrico et al, Guiding pseudo-labels with uncertainty estimation for source-free unsupervised domain adaptation, CVPR 2023
- Tang et al, Source-free domain adaptation via target prediction distribution searching, ICLR 2023
- Gao et al, UNITS: A Unified Multi-Task Time Series Model, NeurIPS 2024
- Ding et al, Source-Free Domain Adaptation via Distribution Estimation, CVPR 2022
It's important to compare against foundation model style approaches since they offer SoTA adaptation efficiency.

2. Writing needs to be improved. The tables with results and plots are very very tiny, and zoom 200% is needed to read them and evaluate. Please choose the most important results to present.

3. The loss functions for target adaptation are not presented, please be specific and self-contained.

4. The method is not time series specific. Why not compare with vision models and datasets to show universality of the method?

5. The authors do not compare against Lokra, Lora with the same style of parameter block freezing and tuning. This would improve fairness of comparisons.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel domain adaptation approach for time series modeling using tensor decomposition. It decomposes source model weights and only finetunes the tensor core components for target data adaptation. The authors provide PAC-based generalization bounds for the adaptation task and demonstrate computational efficiency through experiments.

### Strengths
- New application of tensor decomposition for domain adaptation in time series, building upon concepts from Monarch architecture and block tensor train methods used in NLP transformer models
- Comprehensive experimental results across multiple datasets clearly demonstrate computational benefits

### Weaknesses
1. While the theoretical analysis provides valuable insights into the trade-off between target data fit and source-target distribution divergence, the assumptions have limitations:

- The posterior $Q(S)$ is assumed to be an isotropic Gaussian with variance matching the prior $P$. This assumption doesn't reflect real-world scenarios and is more like a typical variational inference solutions. A more realistic upper bound should incorporate: (1) Weight differences; (2) Distance between isotropic Gaussian posterior and true posterior. While such an extension appears feasible, the distance metric between isotropic Gaussian and true posterior remains undefined

-  The performance of SFDA compared to LoRA aligns with expected outcomes based on existing work in Monarch and Tensor Train architectures, making it somewhat incremental

### Questions
Related Work:
The paper would benefit from discussing connections to recent NLP transformer architectures, particularly:

- Dao et al. (2022), "Monarch: Expressive Structured Matrices for Efficient and Accurate Training"
- Qiu et al. (2024), "Compute Better Spent: Replacing Dense Layers with Structured Matrices"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the topic of Source-Free Time-Series Adaptation. To make the model adaptation more efficient, this paper proposes to decompose the model into core tensor and factor matrices.  When adaptation, only core tensors are selectively fine-tuned. The method can reduce the overall model size and enhance inference efficiency by decomposing and selective fine-tuning.

### Strengths
The paper proposes to use Tucker-style factorization for the model decomposition. This decomposition raises a new perspective (at least for me) beyond the conventional feature selection and  BN adaptation methods. 

The results are solid. A PAC-Bayes generalization bound is provided for the selective fine-tuning stage. The method is evaluated on the real-world dataset such as AdaTime benchmark.

### Weaknesses
I am only curious about some points listed below:

1) Some domain adaptation methods only adapt the BN layers [1],  normalization [2], or only feature modules [3]. They also selectively fine-tune the model, what is the relations between them and the proposed one. Can the proposed method explain or unify these methods in some cases?

2) Can the proposed method be transferred to the general DA task? If not, could you please explain the reasons?

3) It seems that the proposed theorem can be applied to any method with selective fine-tuning. What is the advantage of the proposed decomposition method analyzed from this theorem?

### Questions
Please refer to the weaknesses part. Overall, I think it is a good paper with new thoughts.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates source-free domain adaptation problem. The authors introduce a straightforward yet efficient framework that decomposes the parameter matrices using Tucker-style factorization, allowing the model to adjust only a subset of parameters during target adaptation. Extensive experiments conducted across various datasets and settings demonstrate the superiority of the proposed method over existing baseline models and high sample efficiency.

### Strengths
1. The proposed metric decomposition-based approach for efficient target domain adaptation is simple and efficient. 
2. The experiments are very detailed and thorough, clearly demonstrating the effectiveness and efficiency of the proposed method. That is appreciated. 
3. The manuscript is well-structured and clearly written, facilitating easy comprehension for readers.

### Weaknesses
1. The connection between the proposed method and the characteristics of time-series data is somewhat weak. The method appears to be a general SFDA approach rather than being specifically tailored for time-series data. The justification for using channel-wise decomposition, while potentially effective, lacks a strong theoretical grounding in the specific properties of time-series data. It's unclear why this particular decomposition is more suitable for time-series than other forms of data, or other decomposition strategies.
2. The novelty of the approach is limited, as parameter decomposition for domain adaptation is a prevalent technique. While the specific combination of Tucker decomposition and selective fine-tuning might be novel, the core idea of reducing parameter space through decomposition is not new. The paper needs to better articulate the specific novel contribution beyond a simple combination of existing techniques.
3. The description of target domain adaptation is insufficient. Specifically, which loss function is utilised? And how to optimise the parameters? The paper lacks crucial details on the adaptation process, such as the specific loss functions used for fine-tuning on the target domain, the optimization algorithm, and the hyperparameter settings. Without these details, it is difficult to reproduce the results or assess the method's robustness.

### Questions
1. Could the author explain the rationality of replacing $P$ (the prior distribution) and $S$ (sampled data) with $\mathcal{W}{src}$ (the pre-trained network) and $\mathcal{W}_{trg}$ (fine-tuned network), respectively, in the context of PAC-Bayesian generalization theory? The original theory is designed to measure the generalization error between the empirical and expect loss, but for the same distribution.
2. Could the author include an ERM baseline in Table 1 to provide readers with a clearer understanding of the performance improvements achieved by the proposed method?

### Soundness
3

### Presentation
3

### Contribution
1
