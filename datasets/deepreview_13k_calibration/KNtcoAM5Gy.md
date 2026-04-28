# BaFTA: Backprop-Free Test-Time Adaptation for Zero-shot Vision Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Large-scale pretrained vision-language models like CLIP have demonstrated remarkable zero-shot image classification capabilities across diverse domains. To enhance CLIP's performance while preserving the zero-shot paradigm, various test-time prompt tuning methods have been introduced to refine class embeddings through unsupervised learning objectives during inference. However, these methods often encounter challenges in selecting appropriate learning rates to prevent collapsed training in the absence of validation data during test-time adaptation. 
    In this study, we propose a novel backpropagation-free algorithm BaFTA for test-time adaptation of vision-language models. Instead of fine-tuning text prompts to refine class embeddings, our approach directly estimates class centroids using online clustering within a projected embedding space that aligns text and visual embeddings. We dynamically aggregate predictions from both estimated and original class embeddings, as well as from distinct augmented views, by assessing the reliability of each prediction using Rényi entropy.
    Through extensive experiments, we demonstrate that BaFTA consistently outperforms state-of-the-art test-time adaptation methods in both effectiveness and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses the challenges faced by test-time prompt tuning methods in enhancing the performance of large-scale pretrained vision-language models. The authors a novel backpropagation-free method for test-time adaptation in vision-language models, focusing on estimating class centroids through online clustering in a projected embedding space that aligns text and visual embeddings. The approach dynamically aggregates predictions from both estimated and original class embeddings, as well as distinct augmented views, while assessing prediction reliability using Renyi entropy. The authors claim that the proposed method reaches the state-of-the-art test-time adaptation methods significantly.

### Strengths
- The authors use of a backpropagation-free approach instead of employing prompt-tuning is novel than before approach.

- The main contributions are clearly stated.

### Weaknesses
 - The experimental setting parameters are not the same with TPT and no fair experiment is conducted. The paper of Implementation Details shows: In line with the TPT implementation, we utilize a simple combination of RandomResizedCrop and RandomFlip to prepare 63 augmented views, constituting a mini-batch of 64 images for each test image. Actually, TPT only uses random resized crops to augmented views. Besides, “and adaptation In line with the TPT” seems less a “.”

- Although the authors' approach can use multiple prompts compared to TPT only use single prompt, the paper lacks ablation experiments on prompt

- Authors can present results in more forms of Effectiveness of Projected Embedding Space, such as t-SNE.

### Questions
Although the authors use of a backpropagation-free approach instead of employing prompt-tuning is novel, some experiments are still needed to prove the effectiveness of the method.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of enhancing zero-shot classification in vision-language models (VLMs) during inference. It introduces a novel approach called Backpropagation-Free Test-time Adaptation (BaFTA) that significantly improves zero-shot classification capabilities without requiring labeled examples or backpropagation training. BaFTA leverages online clustering algorithms to directly refine class embeddings within the unified visual-text space of VLMs. The authors also propose a method to combine clustering-based predictions with those from augmented views and evaluate their reliability using Renyi entropy. Comprehensive experiments validate BaFTA's effectiveness in enhancing zero-shot classification accuracy during inference.

### Strengths
+This paper excels in originality by introducing the Backpropagation-Free Test-time Adaptation (BaFTA) algorithm, a novel approach to enhancing zero-shot classification in vision-language models without labeled data or backpropagation. 
+ The quality is evident through comprehensive experiments and the sound methodology of the online clustering technique. 
+ Clarity is maintained in the well-structured introduction and clear explanations of the methodology. 
+ The significance of the paper lies in its practical relevance, potential wider applicability, and the introduction of a technique for dynamically aggregating predictions using Renyi entropy, enhancing the robustness and accuracy of predictions in machine learning tasks.

### Weaknesses
 - Efficiency plays a pivotal role in test-time adaptation, as the ability to swiftly adapt to novel environments is of paramount importance. The paper should explicitly report and compare inference time metrics for BaFTA with existing methods like TPT. This can be done by measuring the time required for BaFTA to adapt to new data during inference and comparing it with the time taken by TPT or other relevant methods. Providing quantitative results and possibly a comparison table would be valuable for the readers.
- The paper assumes that the visual embeddings from CLIP are often discriminative enough for effective classification. A more detailed discussion or evidence regarding this assumption would strengthen the paper's argument. Specifically, while CLIP embeddings have shown strong performance, their suitability for *unsupervised* clustering-based adaptation needs more justification. The paper should address potential scenarios where the visual embeddings might not be sufficiently separable for the online clustering to work effectively. For example, what happens when the visual features of different classes are very close in the embedding space?
- BaFTA's success seems to depend on parameters such as the projection space and the Renyi entropy threshold. The paper could provide more insights on how these parameters are chosen, tuned, and their sensitivity to results. A sensitivity analysis or parameter ablation study could be included. It is not clear how the projection space is determined, and if the dimensionality of this space affects the performance. The Renyi entropy threshold is also a critical parameter, and the paper should discuss how this threshold is selected and how robust the method is to different choices of this threshold.

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use centroids of visual embedding to improve the test time performance of CLIP. The proposed method is training-free.

### Strengths
- 1. It is interesting to see such a training-free method achieves good performance compared to previous tuning methods like TPT. 

- 2. The proposed method is training-free. The authors managed to combine different components to make them work well.

### Weaknesses
 - 1. A more comprehensive ablation of different components in the system is needed. In algorithm 1, the authors use $Eq.3$, online clustering, weighted aggregation, etc. I am confused about the contributions of different components. For example, in Table 5, the authors can add results of a simple average of BaFTA-OC + CLIP text predictions. This may help us understand the effectiveness of Renyi Aggregation more clearly. Other detailed ablations are also needed.

 - 2. The core idea of the proposed method is to use visual centroids to help classifications. The online updating paradigm also assumes the test data come from the same distribution. In practice, this may not be the case. For instance, test samples may come from different distributions. One possible case is samples come from mixed distributions, e.g., mix of ImageNet-A&ImageNet-V2&ImageNet-R. I think the method will not work in such a circumstance.
    - 2.1 The proposed method will not work in an open scenario, for example, the number of classes is not fixed.

 - 3. How about the inference time of the proposed method? The time cost of one step in Algorithm 1 from $for$ to $end for$.

### Questions
Please check Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new backpropagation-free method for test-time adaptation in vision-language models. Instead of fine-tuning text prompts, this paper employs online clustering within a projected embedding space that aligns text and visual embeddings to estimate class centroids. To reliably evaluate predictions, the paper utilizes Renyi entropy, which ensures accuracy and robustness. Experiments demonstrate that the method improves zero-shot classification accuracy and outperforms SOTA test-time adaptation methods.

### Strengths
1. This paper provides a clear introduction to the challenges of test-time prompt tuning methods and introduces the state-of-the-art method TPT. To address these issues, this paper proposes BaFTA, which is highly motivated.

2. The algorithm proposed in this paper is simple, lightweight, and its description is also very clear.

### Weaknesses
1. In the part of Projected Online Clustering, the main distinction between your approach and ReCLIP[1] is that your clustering is conducted online, while ReCLIP's clustering is done offline. Furthermore, due to your Test-Time adaptation setting, your clustering must be conducted online. So I think this may not represent a particularly solid innovation.

2. The experiments are insufficient. In Table 3 and Table 4, I suggest that the authors include additional methods such as CoCoOp[2], TPT+CoCoOp, BaFTA+CoCoOp, and Sus-X [3] and [4].

3. The ablation study on entropy order α should be more comprehensive. In Table 7, when entropy order equals 0.25, the result is 70.52, and when it equals 0.5, the result is 70.53. So, what about when it equals 0.4 or 0.6? Therefore, the authors should conduct more fine-grained experiments.

### Questions
1. The method proposed in this paper has persistence? In other words, can I save the results at a certain moment for later updates?

2. In Table 6, the authors discuss the effectiveness of projection P*. Is there any explanation regarding how projection P* can improve the embedding distribution?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
