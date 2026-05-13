# A 2-Dimensional State Space Layer for Spatial Inductive Bias

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
A central objective in computer vision is to design models with appropriate 2-D inductive bias. Desiderata for 2-D inductive bias include two-dimensional position awareness, dynamic spatial locality, and translation and permutation invariance. To address these goals, we leverage an expressive variation of the multidimensional State Space Model (SSM). Our approach introduces efficient parameterization, accelerated computation, and a suitable normalization scheme. Empirically, we observe that incorporating our layer at the beginning of each transformer block of Vision Transformers (ViT), as well as when replacing the Conv2D filters of ConvNeXT with our proposed layers significantly  enhances performance for multiple backbones and across multiple datasets. The new layer is effective even with a negligible amount of additional parameters and inference time. Ablation studies and visualizations demonstrate that the layer has a strong 2-D inductive bias. For example, vision transformers equipped with our layer exhibit effective performance even without positional encoding. Our code is attached as supplementary.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper found that a 2D recurrent state space model (SSM) can be computed as convolution and proposed a SSM based layer which can be seamlessly plug into ViT.  Experiments show this new layer can improve ViT classification accuracy slightly.

### Strengths
1/ A new SSM based layer which has sound theoretical justification (I did not check the math carefully), and can be calculated as Convolutions.
2/ This SSM based layer can be easily plugged into ViT and good results are achieved.

### Weaknesses
Although it seems the new layer is based on sound theoretical justification, and experiment results show that it indeed works, the improvement is tiny and it's hard to see the real benefits of the proposed idea. Actually this tiny improvement may disappear when hyper parameters vary a little bit. Thus it is really a stretch to claim the benefits of the new layer. More experiments will be needed to justify.

### Questions
Besides image level classification, can you run experiments on pixel level tasks such as semantic segmentation or instance segmentation by plug in this new layer into, e.g., Mask2Former or Pyramid Vision Transformer?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission introduces a novel layer based on a variation of the multidimensional State Space Model (SSM), aimed at enhancing 2-D inductive bias in computer vision models. The 2D-SSM layer is designed to be integrated into Vision Transformers (ViT), contributing to improved model performance across various ViT backbones and datasets, without adding substantial parameters. The authors underscore the layer’s ability to bring about strong 2-D inductive bias, highlighting its performance even in the absence of positional encoding, and showcasing its robustness through ablation studies and visualizations.

### Strengths
The central innovation of this work is the 2D-SSM layer, which is grounded in Roesser’s model for multidimensional state space, and benefits from efficient parameterization, accelerated computation, and suitable normalization. The layer introduces a strong inductive bias toward 2-D neighborhood and locality, captures unrestricted controllable context, and is highly parameter-efficient, being able to express kernels of any length via just eight scalars. Through empirical evaluation, the authors demonstrate that their layer acts as a general-purpose booster for vision transformers, surpassing standard methods like positional encoding in effectively integrating positional bias, all the while maintaining efficiency in terms of parameters and computation at inference.

The work is well-grounded in control theory, with the authors providing theoretical analysis to show that their layer generalizes S4ND and exhibits greater expressiveness. The submission includes supplementary code, facilitating reproducibility and practical application of the proposed method. Overall, this work presents a significant contribution to the field of computer vision, introducing a novel layer that addresses key challenges in 2-D inductive bias and demonstrates notable performance enhancements for Vision Transformers.

### Weaknesses
1. **Extended Training Time**: The submission raises concerns about the extensive training time required for the proposed method. There is ambiguity regarding whether other methods, if given a comparable increase in computational resources, would yield indistinguishable results. The current results lack persuasive power as they do not strictly control factors, making it difficult to definitively attribute performance gains to the proposed method. Specifically, the paper does not provide a clear comparison of training time per epoch or total training time against baseline methods, making it difficult to assess the practical overhead of the proposed 2D-SSM layer. It is unclear if the reported training times include optimization of the baseline methods, or if the comparison is made against off-the-shelf implementations.

2. **Simplicity of Tasks**: The tasks used to evaluate the method are considered too simple, raising questions about whether the inductive bias introduced is specifically beneficial for such tasks. A more critical evaluation would involve assessing the performance of the baseline methods after large-scale pre-training to assess if the learned inductive bias during pretraining can obtain better performance in downstream tasks after finetuning (etc., prompt tuning). If such an approach yields better results, the practical significance of the proposed 2D-SSM becomes unclear. The current evaluation is limited to relatively small datasets and does not explore the behavior of the proposed layer on more complex, real-world datasets with higher resolution images or more diverse object categories. This raises concerns about the generalizability of the findings.

3. **Limited to Transformer-based Architectures**: The method primarily targets transformer structures that lack explicit inductive bias design. It is uncertain how well the method would perform on convolutional networks (ConvNets) and how it compares to similar inductive bias methods, such as ConvNeXt. A comprehensive evaluation across different network architectures and inductive bias strategies is needed to fully understand the method's applicability and effectiveness. The paper lacks a detailed analysis of how the 2D-SSM layer interacts with the inherent inductive biases of convolutional layers, and whether it provides complementary or redundant benefits.

### Questions
Please refer to the weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to integrate spatial inductive biases into neural network architectures, such as Vision Transformers, through the application of a two-dimensional state space model (SSM). By incorporating certain assumptions, this method ensure that the computational complexity remains tractable. Experimental results demonstrate that the proposed method surpasses previous SSM baselines across a range of scenarios.

### Strengths
1. The introduction of a two-dimensional State Space Model (SSM) is an intuitive approach for incorporating spatial inductive biases within neural networks.
2. The suggested technique can be easily integrated into various neural network models.
3. Particularly in scenarios with small size of data, the proposed method demonstrates improved performance compared to baselines that are based on SSM.
4. I appreciate the comparison of the proposed method with S4ND in Section 4.1, as it effectively articulates the proposed method's strengths. Although a more generalized approach does not necessarily guarantee enhanced real-world expressiveness—occasionally it may even compromise the stability of the training process—the conducted experiments effectively demonstrate the proposed method's practicality.

### Weaknesses
1. One limitation of the proposed method, as highlighted in Section 6, is its computational complexity. The method approximately doubles the training time, imposing a considerable computational load. Furthermore, while the added complexity during inference may not substantially contribute to the overall computational demand, a detailed report of the actual inference times would be beneficial for a comprehensive understanding of the method's characteristics. It would be particularly useful to see a breakdown of the computational cost, detailing the time spent in the SSM layer versus the rest of the network, to better understand the bottleneck.
2. In the experiments, the proposed method is primarily benchmarked against SSM-based methods. However, various approaches employ convolution for embedding, for example in [1], and the use of convolutional layers or simple components for positional encoding is a common practice [2, 3, 4, 5]. It would be instructive to compare the proposed method with Vision Transformers that incorporate the methods to exploit spatial equivariance, which could serve as additional baselines. Furthermore, while it may not be a critical flaw, the implementation of the proposed method appears to be somewhat more complicated and less straightforward than simply employing convolutional layers. The complexity stems from the parameterization of the 2D kernel within a sub-vector space, which requires careful implementation and may not be as readily available in standard deep learning libraries as convolutional operations.
3. I believe that a larger model and dataset size would more effectively leverage strong spatial equivariance [6]. This implies that the proposed method may not be effective in environments with substantial data and model scales. Considering that training on datasets like IN1K with 'Base' or larger models has become a norm in the era of Vision Transformers, the applicability of the proposed method in such standard real-world scenarios could be limited. Additionally, the focus of the experiments on smaller datasets and models further suggests potential constraints in its utility for larger-scale tasks. The experiments should include a study of how the performance of the proposed method scales with the size of the model and dataset, particularly when compared to standard convolutional approaches.

### Questions
1. Why is the `D` omitted in Equation 2? Does its inclusion empirically reduce the performance? 
2. In Figure 4, it is observed that the 2-D SSM markedly enhances performance when 100% of the dataset is utilized, as opposed to 20% or less. This result is counterintuitive. Providing explanations for this phenomenon would enhance the comprehensiveness of the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on developing new method for injecting 2-D inductive bias into Vision Transformer for computer vision problems. To achieve this, the authors propose to leverage an expressive variation of the multidimensional State Space Model (SSM) with the proposed efficient parameterization, accelerated computation and suitable normalization scheme. The paper show that by incorporating the proposed layer at the beginning of each transformer block of ViT improves the performance of various ViT backbones, such as Mega, for various datasets for image classification. It is also shown that the method achieves effective results without positional encoding.

### Strengths
* The paper proposes a new method for encoding image-specific inductive bias for ViT in Computer vision problems.

* The proposed method is shown to be effective for Image Classification in various datasets with various ViT backbones with negligible amount of additional parameters and inference time. 

* The method can achieve good performance without positional encoding.

### Weaknesses
 * As mentioned by the authors, one major limitation of the method is its high training time cost. It can double the training time compared with the baseline, limiting its application to the training of large models on large benchmarks.

* The experiments limit to image classification problems and 2-D inductive bias can be very important for dense prediction. It would be better to also evaluate the proposed method for dense prediction problems like segmentation, depth estimation etc.

* The complex (C) variant of the proposed method may exhibit instability, obtaining very bad results, e.g. Table 1, Table 6. I would recommend the authors to include a detailed explanation of this situation and any potential ways of avoiding the instability.

### Questions
* I would suggest the authors to clearly explain each model in each table. For example, it would be much clear if the authors can explain what is 'ViT w/ MixFFN' and so on before describing the results. Also, are the results of the proposed method shown in Table 3 obtained by using SSM-r or SSM-c? 

* It is great to see the analysis of the inference cost. I would recommend to also give comparisons of the inference time in Table 1. It is also suggested to include comparisons of the memory cost in Table 1 and the details about the platform for experiments.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
