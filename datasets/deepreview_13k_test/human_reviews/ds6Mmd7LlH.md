# GRADIENT-OPTIMIZED CONTRASTIVE LEARNING

- Decision: Reject
- Scores: 6, 6, 5, 6, 6

## Abstract
Contrastive learning is a crucial technique in representation learning, producing robust embeddings by distinguishing between similar and dissimilar pairs. In this paper, we introduce a novel framework, Gradient-Optimized Contrastive Learning (GOAL), which enhances network training by optimizing gradient updates during backpropagation as a bilevel optimization problem. Our approach offers three key insights that set it apart from existing methods: (1) Contrastive learning can be seen as an approximation of a one-class support vector machine (OC-SVM) using multiple neural tangent kernels (NTKs) in the network’s parameter space; (2) Hard triplet samples are vital for defining support vectors and outliers in OC-SVMs within NTK spaces, with their difficulty measured using Lagrangian multipliers; (3) Contrastive losses like InfoNCE provide efficient yet dense approximations of sparse Lagrangian multipliers by implicitly leveraging gradients. To address the computational complexity of GOAL, we propose a novel contrastive loss function, Sparse InfoNCE (SINCE), which improves the Lagrangian multiplier approximation by incorporating hard triplet sampling into InfoNCE. Our experimental results demonstrate the effectiveness and efficiency of SINCE in tasks such as image classification and point cloud completion. Demo code is attached in the supplementary file.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method that modifies InfoNCE but provides better gradient during training with SGD. From the observation that sample weights and network weights are coupled together, they tried to optimize both objectives via bilevel optimization. They connect sample weights optimization with one-class support vector machine then use these weights to optimize network weights, which is novel approach. They also provide practical version of this approach, namely SINCE, which is equivalent to thresholding with predefined threshold. They showed empirical performance on image classification and 3D point cloud completion.

### Strengths
1. I think the approach they provide is novel. As they mentioned in the introduction, they inherit the core motivation of previous negative sampling works but tried to connect these concepts with one-class support vector machine. 
2. The writing is clear and cohesive.
3. Empirical results are powerful.

### Weaknesses
1. I enjoyed reading upto section 3, however, the final form of SINCE seems too simple, arbitrary, and not tight. Now we need to find appropriate hyperparameters. According to Table2, SINCE performs way much poor than GOAL especially large triplet cases. Figure 3(a) it seems the performance is quite sensitive to these parameters

### Questions
1. Related to weakness: Is there a better way to better approximate GOAL, such as higher-order approximation? Since GOAL approach seems novel and powerful (from Table 2), I wish to witness better approximation showing better result than current SINCE. It doesn't need to be full experiments (Derivation with simple experiments would be fine). I would happy to raise my score if this concern is resolved.
2. I wish to check the triplets provided in Figure 2  - especially 7 peaks high in both cases and ~10 peaks that are only appeared with InfoNCE. Can we distinguish those samples in our eyes? In other words, are those separation corresponds to our inception?

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
The paper makes two contributions. First, it introduces a novel approach to contrastive learning known as Gradient-Optimized Contrastive Learning (GOAL), which reformulates the contrastive learning problem as a bilevel optimization challenge. Additionally, it enhances the computational efficiency of GOAL through the implementation of a new loss function called Sparse InfoNCE. Theoretically, the paper establishes the validity of this approach by establishing a lemma that shows the equivalence between contrastive learning and One-class Support Vector Machine (OC-SVM) using multiple Neural Tangent Kernels (NTKs). Empirically, the method is evaluated on tasks such as image classification and 3D point-cloud completion.

### Strengths
Overall, the paper is well-written and presents a fresh perspective on the contrastive learning problem by formulating it as a bilevel optimization challenge. While the derivation of the Upper Level (UL) is relatively straightforward, the formulation of the Lower Level (LL) as an OC-SVM problem is intriguing. This approach not only highlights the relationship between hard triplet samples and outliers in OC-SVMs but also adds depth to the theoretical framework. Furthermore, the paper introduces an easy-to-implement algorithm that is tested across a wide range of scenarios, demonstrating its versatility and effectiveness.

### Weaknesses
Firstly, the experimental results on image classification are limited to just three small datasets and two essentially similar architectures from the same ResNet base. To enhance this section, it would be beneficial to include results from more modern architectures, such as EfficientNet [1] and PyramidNet [2], as well as from more challenging datasets such as CIFAR100 or Stanford Cars [3]. Additionally, while the experiments on point-cloud completion cover a diverse range of settings, the proposed method shows only a modest improvement over InfoCD. Besides, other concerns are addressed in the questions below.

### Questions
+ In lines 177-178, it is stated that "the gradient $\triangle \omega_t$ is computed by a linear combination of triplet features. While this holds true for the InfoNCE loss as derived in the previous section, is it also applicable to state-of-the-art contrastive learning methods? Clarification on this point would be valuable.

+ In lines 183-184, could you elaborate on the motivation for mentioning "when the calculation of each $\alpha^{(t)}_{(x, x^+, x^-)}$ relies on the triplet features"? According to Equation (3), it appears that $\alpha$ does not depend on the triplet features, and further explanation would help clarify this statement.

+ Could you provide additional context for using the dual regularized OC-SVM as the Lower Level (LL) objective to find the optimal $\alpha^*_{i, j, k}$? Including a few sentences about this motivation before Equation (5) would enhance the communication of the idea, along with a derivation of the dual form or a reference to the dual form of the classical OC-SVM problem, as presented in Equation (6).

+ It seems that there was a slight mathematical mismatching between Lemma 1 and Eq. (8). In particular, the minimum of the LHS should be equal to the maximum of the summation  

$$\max \sum \eta_t [\sum \alpha^{(t)}_{ijk} \kappa (\cdot,\cdot)]$$ 

instead of the summation of the maximum 

$$\sum \eta_t [\max (\sum \alpha^{(t)}_{ijk} \kappa (\cdot,\cdot))]$$

+ Could you clarify why the two results in Table 2 were omitted? Additionally, it appears that some entries in this table, such as the results for GOAL with 20 and 40 triplets, may have been mistakenly bolded.

+ Could you provide more detail on how the function $f$ was selected for the image classification task?

**References:**

[1] Tan, M., & Le, R. P. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. arXiv preprint arXiv:1905.11946.

[2] Han, D., Wang, J., & Yin, S. (2017). PyramidNet: Nested deep learning models for image classification. arXiv preprint arXiv:1610.02915.

[3] K. Krause, H. Stark, J. Deng, & L. Fei-Fei. (2013). 3D Object Representations for Fine-Grained Categorization. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*. Retrieved from http://ai.stanford.edu/~jkrause/cars/car_dataset.html

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
The paper titled "Gradient-Optimized Contrastive Learning" (GOAL) introduces a contrastive learning framework aimed at improving gradient during backpropagation. GOAL reinterprets contrastive learning as a one-class support vector machine (OC-SVM) problem in neural tangent kernel (NTK) space, focusing on hard triplet samples to enhance model robustness. To this end, the authors propose a contrastive loss, Sparse InfoNCE (SINCE), which integrates hard triplet sampling for efficient learning. Experiments in image classification and point cloud completion demonstrate that SINCE enhances contrastive learning by making gradient updates more efficient and effective, achieving competitive results across multiple datasets.

### Strengths
1. Strong Empirical Results:
GOAL and SINCE demonstrate superior performance on benchmark datasets in both image classification and 3D point cloud completion. The results indicate that the proposed method outperforms traditional InfoNCE-based approaches, particularly in settings requiring robust gradient optimization.

2. Clear Contributions to Contrastive Learning:
The paper provides a strong conceptual link between contrastive learning and sparse kernel machines. This insight offers a fresh view that could impact future research in unsupervised and semi-supervised representation learning by enabling more efficient contrastive frameworks.

3. Comprehensive Evaluation:
Extensive experiments across multiple benchmark datasets, including CIFAR-10, STL-10, and ShapeNet-Part, showcase the robustness and adaptability of the proposed approach across different types of data and tasks (classification and point cloud completion), underscoring its versatility.

### Weaknesses
1. Insufficient Link Between Motivation and Proposed Solution:
In the motivation subsection (L035-053), the authors present various perspectives on contrastive learning, emphasizing the importance of hard-negative samples. However, the subsequent question posed—"How should we optimize the gradients in contrastive learning effectively and efficiently?"—lacks a clear justification. For example, from the analysis of Tian et al (2022) , it is unclear what is the specific issue taht motivates gradient optimization within contrastive learning. The rationale for optimizing gradients and how this links to the concerns raised in the motivation are not sufficiently clarified.

Similarly, the proposed approach in the "Approach" subsection (L065-080) could benefit from further explanation of why certain strategies or assumptions are adopted. For instance, while the authors introduce a bi-level optimization framework, it would be helpful to understand why this framework is necessary and what limitations of current methods necessitate this choice. A clearer justification of the selected strategy would aid in understanding and appreciating the method. Overall, establishing a stronger connection between the problem raised in the motivation and how the proposed approach addresses it would improve clarity. Additionally, the methods section could more explicitly address why each methodological choice is made, rather than focusing solely on what the choices are.

2. Structural Suggestions for Improved Clarity:
In the methods section (L182-189), the authors begin discussing the core problem; however, addressing this at the beginning of the paper might set a more coherent foundation for readers. In L188-189, the question "What if \(\alpha_{x, x^{+}, x^{-}}\) does not have an explicit form of \(\omega\)?" would benefit from a discussion of the conditions under which this situation might arise and why it is significant.
From lines L190-194, introducing and explaining the bi-level optimization framework in general would improve clarity. Specifically, a brief explanation of the upper-level and lower-level problems could help readers unfamiliar with the framework to understand the significance of this choice.

3. Interpretation of Key Inferences:
In lines L240-243, the authors infer that "Our bilevel formulation also indicates that hard triplet samples ...". However, this inference is not readily apparent from the preceding discussion. It would be valuable if the authors could elaborate on the indicators leading to this conclusion and provide a more explicit description.

4. Clarity in the Learning Process Description:
The description of the algorithm in sections 3 and 4 would benefit from additional clarity, specifically regarding the overall learning process. A pseudo-code algorithm summarizing the training pipeline could help to practically illustrate the proposed method.

5. Efficiency Considerations:
In Table 2, including a discussion of the overall wall-clock time, FLOPs, or MACs for the proposed approach would provide insights into the efficiency-performance trade-offs. Additionally, it raises questions about inefficiency compared to the standard InfoNCE version, as bi-level optimization methods are generally known to be computationally intensive.

6. Emphasis on Why Over What:
In its current form, the paper predominantly addresses *what* is being done rather than *why*. Strengthening the paper’s focus on the core problem being solved, while clearly linking the proposed solution to this problem, would significantly enhance its readability and impact.

### Questions
1. Could you offer more context on why specific assumptions and strategies (e.g., bi-level optimization) were chosen, as well as any alternatives they considered?

2. Could the authors provide additional details on the efficiency of the proposed method? For example, a comparison of wall-clock time, FLOPs, or MACs relative to the standard InfoNCE implementation would offer insights into potential performance-efficiency trade-offs.

3. In the bilevel formulation, the authors conclude that hard triplet samples serve as support vectors and outliers. Could the authors elaborate on this inference, including which indicators are being referenced and how they lead to this conclusion?

### Soundness
2

### Presentation
2

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
This paper focuses on contrastive learning, where the authors propose a gradient-optimized contrastive learning framework, which enhances network training by optimizing gradient updates during backpropagation as a bilevel optimization problem. To address the
computational complexity of GOAL, they also develop propose a Sparse InfoNCE (SINCE) learning framework, which improves the Lagrangian multiplier approximation by incorporating hard triplet sampling into InfoNCE.

### Strengths
1. The proposed learning framework which enhances network training by optimizing gradient updates during backpropagation as a bilevel optimization problem provides some interesting insights.
2. The mathematical formulation and the theoretical grounding provided are thorough and robust. It advances the understanding of the mechanics behind gradient updates and their optimization in neural networks.

### Weaknesses
1. The learning framework proposed in the experimental section does not seem to have significant gains compared to existing frameworks. In addition, the experimental dataset is relatively small and the network structure is single (ResNet), so it is recommended to further supplement with larger benchmark sets and experiments with different network structures.
2. While the paper addresses computational efficiency, the actual computational cost, in terms of time and resources, required for implementing these models in a real-world setting is not thoroughly explored. For large-scale deployment, the computational overhead could still be a limiting factor, which may not be fully mitigated by the proposed Sparse InfoNCE loss.
3. While the paper compares the proposed method with some existing approaches, a broader comparison with other state-of-the-art methods could have been included to position the paper within the current research landscape more clearly.

### Questions
Besides the Weaknesses above, I also have the following questions:
1. In this paper, the authors use the UL problem to update network weights, while the LL problem to learn optimal gradients for SGD.  My question is, can the two be reversed? Why?
2. In the proposed Sparse InforaNCE, a predefined threshold is required. How does it choose? Is there a challenge in its choice?Suggestions for supplementing relevant sensitivity analysis experiments.
3. Is there anything missing from Table 3? I did not capture any information about SINCE.
4. In Section 3.3, the authors mentioned using OC-SVM to optimize gradients. My question is: what impact will different kernel functions have on performance? Suggest supplementing relevant experiments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is motivated by the $(\phi, \varphi)$ formulation of contrastive losses from Tian (2022), consider the gradient weighted by a linear combination of triplet gradient features, and address issues for easy triplets weighting down more important triplets. The paper connects this with OC-SVM to determine the gradient weights. The paper also introduce a more computational efficient approximation which applies hard triplet sampling. Report performance improvements over contrastive baselines on image-classification and 3d point cloud completion.

### Strengths
1. The paper is comprehensive and well-structured.
2. Addresses relevant issue in contrastive learning which is the weighting of triplets/pairs in the gradient.   
3. The paper report good performance results over the contrastive InfoCD (Lin et.al, 2023) on 3d cloud completion.

### Weaknesses
1. The image classification results are too low compared to Peng et., (2022), Chen et.al., (2020a), Yeh et.al, (2021), which the authors base implementations details on, and to Max-Margin Contrastive Learning (Shah et al., 2022). It would more relevant if you could use the original datasets, train to convergence, and show improvement over the mentioned work with similar settings. The final results on ImageNet100 are also not included in Table 3.
2. GOAL presents computational difficulties and can rarely be realized fully in practice. The approximation SINCE develop into a hard negative sampling strategy (thresholding before normalizing) which, I think, is not more than a simple modification to the InfoNCE loss.

### Questions
See first point weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
