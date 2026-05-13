# DipDNN: Decomposed Invertible Pathway Deep Neural Networks

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Deep neural networks (DNNs) enable highly accurate one-way inferences from inputs to outputs. However, there is an elevated need for consistency in bi-directional inferences, such as state estimation, signal recovery, privacy preservation, and reasoning. Since standard DNNs are not inherently invertible, previous works use multiple DNNs in a nested manner to obtain consistent and analytical forms of inverse solutions. However, such a design is not only computationally expensive due to DNN compositions, but also forces splitting the input/output equally, which is inapplicable in many applications. To reduce the restriction, other works use fixed-point iterations to enable approximation of one-to-one mapping, but the numerical approximation leads to reconstruction errors compared with the analytical inverse. To preserve the analytical form with minimum computational redundancy, we proposed decomposed-invertible-pathway DNNs (DipDNN) that decompose the nested design. We enforce one-to-one mapping in each layer by minimally adjusting the weights and activation functions of standard dense DNNs. We prove that such an adjustment guarantees strict invertibility without hurting the universal approximation. As our design relaxes the alternative stacking of nested DNNs, the proposed method does not need a fixed splitting of inputs/outputs, making it applicable for general inverse problems. To further boost the two-way learning accuracy, we show that the proposed DipDNN is easily integrated into a parallel structure. With the analytical invertibility, bi-Lipschitz stability regularization naturally fits into the scheme to avoid numerical issues. Numerical results show that DipDNN can recover the input exactly and quickly in diverse systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study the problem of designing deep neural network (DNN) strctures that is invertible. As a main contribution, the decomposed-invertible-pathway DNN structure is designed to mitigate the computational redundancy of existing invertible DNN designs. Besides, a parallel DNN structure is introduced to add regularization to the invertible DNN to improve the prediction accuracy. Simulations on over a number of test cases, inlcuding the image processing and state estimation in power systems, are conducted to show the effectiveness of the proposed DNN design.

### Strengths
1. The problem investigated in the paper is important and interesting.
2. The idea of paper for contructing an invertible DNN is novel.

### Weaknesses
1. The paper is not easy to follow. See the comments below.

2. The contribution of the paper is not clear.

3. The theoretical analysis in the paper is not sufficient. See the comments below.

### Questions
1. The paper is hard to follow. The authors are suggested to re-organize the contents and polish the expressions in order to make it easier to read. 

2. The contribution of the paper is vague. The authors are suggested to explain the advantage of the proposed approach as compared to state-of-the-art invertible DNN designs clearly. If the contribution of the proposed approach is having lower complexity, a run-time complexity analysis should be given in the paper.

3. In paragraph 3 of Sec. 3.1, the authors mention "Although the nonlinear DNN is nested in the middle, some interconnections among variables are eliminated due to the separated input/output groups, for which the comparison with regular NN is in Appendix A.1.." This is not easy to follow. The authors are suggested to explain why some interconnections among variables are eliminated in a more clear way.

4. It is not clear why fixed spliting the input and output is a important disadvantage of eisting invertible DNN designs. The authors are suggested to give some illustration and toy examples to show it.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Targeted on the bi-directional inference demands, such as state estimation, signal recovery, privacy preservation, and reasoning, the paper presents a novel Deep Neural Network design, decomposed-invertible-pathway DNNs (DipDNN), that decomposes the nested structure to avoid the inapplicable requirement of splitting input/output equally, while ensures strict invertibility and minimum computational redundancy without hurting the universal approximation.

In general, the problem this article focuses on,  the inconsistency in bi-directional inferences, is important. Due to the inherent irreversibility of DNNs, the problem is quite challenging; the paper presents a well-designed invertible DNN architecture with rigorous theoretical analysis. However, since the datasets in the experiments are relatively small, as well as the model architecture; the scalability of the proposed method is not well illustrated.

### Strengths
Overall, this paper is well structured, and the idea has been explained clearly.

This paper focuses on a problem that has important practical implications but lacks effective approaches in the deep learning field. It designs a novel methodology that maintains the consistent and analytical forms of inverse solutions with the nested DNNs while reducing the computational expense and relaxing the restrictions on invertible architecture.

The paper presents a rigorous theoretical analysis to prove the strict invertibility of the DipDNN model without hurting the universal approximation. This theoretical grounding provides a strong foundation for the model's validity.

The paper conducts numerical experiments on several practical applications, including image construction and face completion, power system (PS) state estimation, etc., which show that DipDNN can recover the input exactly and quickly in diverse systems.

### Weaknesses
Although the proposed method appears to be significantly superior to the methods compared, I found that the baseline methods seem somehow outdated (the latest one, i-ResNet, was proposed in 2019). 

The datasets in the experiments are pretty small; the DNN is also simple. For image datasets, I believe that providing some results on CIFAR10/100 (ImageNet may be impossible) and comparing them with i-ResNet can better illustrate the effectiveness of the proposed method. Specifically, the current experiments do not fully demonstrate the model's ability to handle high-dimensional inputs or complex, real-world data distributions. The use of relatively small datasets and simple network architectures raises concerns about the generalizability and scalability of the proposed DipDNN to more challenging scenarios. The experiments, while showing promising results, lack the necessary complexity to fully validate the claims of the paper.

### Questions
1. How large can this model structure scale to, and how will DipDNN with deeper and wider layers perform on complex data sets such as CIFAR?

2. As for experiments, are all the DNN architectures the same through different tasks, i.e., the DNNs on Image Construction and Face Completion and System Identification-based State Estimation?

3. In which part of the experiment the effectiveness of the proposed parallel structure for physical regularization over DipDNN are tested? Is the model performance sensitive to the hyperparameters, i.e., λ_Phy and λ_DipDNN?

4. As for the parallel structure for physical regularization over DipDNN, for physical systems with unknown priors, is the model such as equation learner jointly trained together with DipDNN?

Maybe a typo: the line below the Figure3: f(x) = λ_Phy f1(x) + λ_DipDNN f2(x), should be  f(x) = λ_DiPDNN f1(x) + λ_Phy f2(x)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a novel model DipDNN for the intent of solving bi-directional inference problems. The model enforces bijectivity by using coupling layers, inspired by the work of  Dinh et al., 2014, to construct an analytical inverse, which is easy to compute and does not restrict the model's capacity shown in theorem 1. In addition, the proposed method reduces computation time by utilizing upper and lower triangular weight matrices in the model, which is demonstrated in Figure 2. Lastly, the proposed method is empirically validated for a variety of inverse problems, including image construction competition and system identification-based state estimation.

### Strengths
1). Diversity in types of experiments, the authors evaluated the proposed wide range of applications.

2). The results of the proposed method are empirically promising in the system identification-based state estimation experiments.

### Weaknesses
1). The paper lacks some important details that make the paper challenging to evaluate.
*  The training objective of the proposed method is not articulated clearly mathematically. The paper should clearly state the objective 
    function and what parameters are being optimized. Specifically, the loss function is not clearly defined in terms of the forward and inverse mappings, making it difficult to understand how the model is trained to achieve bi-directional inference. The paper should clarify if the loss is applied to both forward and inverse mappings simultaneously or sequentially, and how the parameters are shared or updated across these mappings.
* Objective function defined in section 2.1 the set g is an element of is not defined. The paper should explicitly define the set \mathcal{G} to clarify the space of functions being considered for the inverse mapping. Without this, the reader cannot fully grasp the scope of the optimization problem.
* Figures 1 and 2 lack a legend/an explanation of the operations. What are the blue lines and red dots? The paper should provide a detailed explanation of the operations within the figures, including the meaning of the blue lines (e.g., linear transformations, specific layer connections) and the red dots (e.g., activation functions, specific nonlinear operations). The lack of explanation makes it difficult to understand the architecture of the proposed model and its differences from existing methods.
* Similar to training the objective function for inference is not stated. How are the inference problems being solved? What is the mathematical objective? The paper needs to specify the mathematical objective for inference, detailing how the learned model is used to solve the inverse problem. It is not clear if the inference step involves a separate optimization or a direct application of the trained inverse mapping. The mathematical formulation of the inference process is crucial for understanding the method's practical application.

2). Authors should provide an explanation of why they chose an additive coupling layer over coupling methods, i.e. Affine or spline coupling layers. Normalizing flow models have made significant progress in the area of coupling layers, so the authors should justify why they're choosing additive over another type. The paper should discuss the trade-offs between additive coupling layers and other types of coupling layers, such as affine or spline coupling layers, in the context of the specific inverse problems being addressed. The justification should go beyond simply stating that additive coupling layers are invertible and should address the potential impact on model capacity and performance.

3). Novelty of theoretical contribution
* The results of Theorem 1 are heavily dependent on the contribution of Duan et al., 2023. The paper should clearly articulate the novel aspects of Theorem 1 beyond the existing work of Duan et al., 2023. It is not sufficient to simply state that the theorem builds upon previous results; the paper should highlight the specific contributions and insights that are unique to this work.
* Coupling layers have been proven to be universal approximations [Coupling-based Invertible Neural Networks Are
Universal Diffeomorphism Approximators](https://proceedings.neurips.cc/paper/2020/file/2290a7385ed77cc5592dc2153229f082-Paper.pdf) Nuerips 2020. The paper should acknowledge and discuss the existing literature on the universal approximation capabilities of coupling layers, particularly in the context of diffeomorphism approximation. The paper should clarify how the proposed method differs from these existing approaches and what specific advantages it offers in the context of bi-directional inference.


4). Image Construction and Face Completion experiments
* Figure 6 Based on the eye test it is challenging to see the improvements in the DipDNN over the Additive Coupling. The paper should provide a more detailed quantitative analysis of the results in Figure 6, rather than relying solely on visual inspection. The paper should include metrics such as PSNR, SSIM, or other relevant measures to objectively assess the performance of the proposed method compared to the additive coupling baseline.
* Based on Figure 7 Results B i-Resnet outperforms the proposed method, but the authors do not make a comment about this result in the paper. The paper should provide an explanation of why i-ResNet outperforms the proposed method in the specific context of Figure 7(b). The authors should discuss the potential reasons for this difference in performance and address the implications for the broader applicability of the proposed method.

### Questions
Questions are addressed in the weakness section.

Main questions:
* Could the authors state the objective functions for both training and inference of the proposed method?
* Could authors please state the theoretical contributions and the insight they provide to the paper?
* Please provide justification or explanation on i-Resnet outperforming the proposed method in Figure 7 b.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
