# An Efficient Multi-Task Transformer for 3D Face Alignment

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
In the research of 3D face alignment, few prior works focus on information exchange among different vertices or 3DMM parameters in regression. On the other hand, there is a drawback that using high-resolution feature maps makes algorithms memory-consuming and not efficient. To solve these issues, we first propose a multi-task model equipped with two transformer-based branches which further enhances the information communication among different elements through self-attention and cross-attention mechanisms. To solve the problem of low efficiency of high-resolution feature maps and improve the accuracy of facial landmark detection, a lightweight module named query-aware memory (QAMem) is designed to enhance the discriminative ability of queries on low-resolution feature maps by assigning separate memory values to each query rather than a shared one. With the help of QAMem, our model is efficient because of removing the dependence on high-resolution feature maps and is still able to obtain superior accuracy. To further improve the robustness of the predicted landmarks, we introduce a multi-layer additive residual regression (MARR) module that can provide a more stable and reliable reference based on the average face model. Furthermore, the multi-information loss function with Euler Angles Loss is proposed to supervise the network with more effective information, making the model more robust to handle the case of atypical head poses. Extensive experiments on two public benchmarks show that our approach can achieve state-of-the-art performance. Besides, visualization results and ablation experiments verify the effectiveness of the proposed model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an efficient multi-task transformer for 3D face alignment, self-attention and corss-attention mechanisims were sused to enhance information communication among different elements of the network. Query aware memory (QAMem) is also designed to remove dependence on high-resolution feature maps. Experiments on two public benchmarks show that the approach can achieve resonable peformance.

### Strengths
The presentation is clear and easy to follow.
The experiments seem to be intensive and resonable results were achieved.

### Weaknesses
1) The contributions seem to be a combination of deep learning tricks like multi-task structure, QAMem module, MARR and Euler Angles Loss, the improvement of each module seems to be incremental and the combination of these incremental contributions, do not become a significant contribution. The multi-task structure, while common, doesn't present a novel approach to information sharing between the 3DMM parameter regression and 2D landmark prediction tasks. The QAMem module, while aiming for efficiency, appears to be a variation of existing memory-based attention mechanisms, and its novelty is not clearly established. Similarly, the application of MARR and Euler Angle Loss, while useful, are not fundamentally new techniques in the context of 3D face alignment.

2) The pose estimation results on AFLW2000-3D dataset, shown in Table 2, don't support that the proposed approach achieve better performance than SOTA. Th MAE, pitch and roll of the proposed approach are not as good as SynergyNet published in 2021.

3) The ablation study in Table 3 don't support the effeictiveness of proposed modules as well. For example, the performance of Cham Dist for Trans3DHead is not as good as the baseline. The ablation study should demonstrate a clear and consistent improvement with the addition of each proposed module. The fact that the Chamfer distance for Trans3DHead is worse than the baseline suggests that the proposed architecture may not be effectively learning the 3D shape representation, and the benefits of the proposed modules are not clearly demonstrated.

### Questions
Further discussion of the novelty of the work need to be elaborated, I don't thnk the contribution listed in the paper, make a good work for top conference like ICLR.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method for 3D face landmarks detection. The contributions are:
- The paper also jointly estimate 2D face landmarks. 
- The paper employs a DETR like approach and each estimated parameter is associated with a query embedding. This can help information communication in joint estimation of all the parameters. 
- The paper also proposes a module to improve the model efficiency using low resolution features. 
- The proposed method predicts residuals from the average face instead of directly predicting the original face. 
- And Euler Angles loss is proposed to improve the performance on atypical head poses. 

Experiments show the competitiveness of proposed method compared with baselines.

### Strengths
+ The presentation of the paper is good.
+ The use of query embeddings and cross attention can help information communication in joint estimation of all the parameters. And this is interesting and novel.
+ Visual demos show the effectiveness of the proposed method in 3D pose and landmarks estimation.

### Weaknesses
 - For the qualitative comparisons, only DAD-3DNet is compared with. From table 5, DAD-3DNet is already worse than the proposed method. While SynergyNet, which performs better than the proposed method, is not compared with in the visual demos.
- section 3.2, the description about QA memory is not super clear. Does the proposed method use more features maps to trade for a lower resolution? What is the benefit in doing this? The description lacks details on how the query-aware mechanism operates and why it is beneficial for low-resolution feature maps. The paper does not clearly explain how the 1x1 convolutions with N groups provide discriminative values for different queries.
- Due to large variation of head poses and face shape, it might not be a good idea to compute the average face and predict the residuals. This approach might limit the model's ability to generalize to unseen face shapes and poses that deviate significantly from the average.
- The paper proposes a Euler Angles loss, but from figure 4, it requires an estimation of the Euler angles from predicted 3DMM parameters. Therefore another module needs to be introduced do the estimation. This module introduces additional errors and might not benefit the supervision for 3DMM parameters. The paper does not specify the exact method for extracting Euler angles from the 3DMM parameters, raising concerns about potential error propagation and its impact on the overall training process.
- From table 3, the QA module seems not to improve the accuracy compared with baseline. The results suggest that the QA module's contribution to overall performance is questionable, especially considering its added complexity.
- From table 5, the proposed method is not quantitatively better than SynergyNet 3DV 2021.

### Questions
- The paper first mentions "memory" in the second paragraph in section 3.1. But there is no context and explanation about it. What does memory mean? Which part does it correspond to in the network structure?
- Can the authors give more explanation and proof about the QA module and its effectiveness? Does the module use more feature maps to trade for lower resolution?
- From section 3.3, the paper uses multiple decoders. What are the decoders like? Why are multiple decoders used? Do they make it computationally less efficient? There are no explanation about the usage of multiple decoders. Maybe I miss something.
- section 3.4.1, how are Euler angles estimated from 3DMM parameters? Is a neural network used here?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a multi-task 3D face alignment framework based on a transformer. The objective is to overcome three main drawbacks of existing methods: (i) first, the 2D facial landmark detection task and the 3DMM parameters prediction task are parallelized in the form of two transformer branches. 3DMM parameters are regressed through Transformers, where the cross-attention mechanism is used to enhance the information communication among task-oriented queries and extracted feature maps in the designed decoder; (ii) A lightweight module named query-aware memory (QAMem) is proposed that makes up the accuracy loss from lower feature map resolutions. To enhance the robustness of the predicted landmarks, the average vertices coordinates of the training set are calculated, then a multi-layer additive residual regression (MARR) module is designed in the decoder to guide the detection under the reference of an average face model. (iii) A multi-information loss function is used to optimize the network.

### Strengths
The main contributions are:
- A Transformer-based multi-task framework is proposed for 3D face alignment, using a multi-task structure. 3DMM parameters are regressed through Transformers, where the cross-attention mechanism achieves the information communication among different elements.
- A Euler Angles Loss in introduced to the multi-information loss function for network optimization, which enhances the predictive ability in the case of atypical head poses.

### Weaknesses
 - The title of the paper is not appropriate in my opinion. The title emphasizes a face alignment contribution, while the content focuses more on face landmarks detection. 
- Table 2 indicates results that are comparable to the state-of-the-art but for some cases do not improve on it. 
- Parameters of a 3DMM are regressed in this work. However, it is not clear how much the choice of the 3DMM impacts on the results. Did the authors try with different 3DMMs? 
- In the ablation study it is not clear the impact of the 3DMM on the results. 
- An analysis of the computational cost of the method in comparison with other solutions is missing. For landmarks detection the capacity of the approach to work in real time is important. Authors should clarify this point.

### Questions
Q1: The contribution of the used 3DMM on hte final results is not clear. Did the authors try with different 3DMMs? Can they show results using different 3DMMs?
Q2: In the ablation study it is not clear the impact of the 3DMM on the results. 
Q3: Authors should discuss and illustrate the computational cost of the method in comparison with other solutions is missing.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors proposed the multi-task framework based on the transformer architecture to efficiently capture the high-resolution information in facial landmark detection task. Query-aware memory module is newly introduced and the multi-layer additive residual regression module and Euler angles loss are proposed. Experiments on two public benchmarks show the effectiveness of the proposed method showing the SOTA results.

### Strengths
QAMem module looks sound and it is well presented in the Figure 2.
MARR and Euler angles loss also look effective to tackle the targetted problem.
English and presentation are sufficiently good to understand the work.

### Weaknesses
Less qualitative results: only 1 dataset is used for qualitative results. More is required.
Even though the authors insist that the proposed method is efficient; while there is no report for the time complexity in their results.
In ablation study, when comparing Euler+QA and MARR+QA, the accuracy improvement is quite limited. It is unclear the accuracy improvement was due to the components, or not.
Explanations for some equations are rather blurry (for eqs 2 and 3).

### Questions
There is less explanation for how to proceed the equations from 2 to 3. 
Why in ablation study, the three combination only can improve the final accuracy, even though partial combination is not that effective?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
