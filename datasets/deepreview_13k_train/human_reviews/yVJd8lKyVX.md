# Hybrid Sharing for Multi-Label Image Classification

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Existing multi-label classification methods have long suffered from label heterogeneity, where learning a label obscures another. By modeling multi-label classification as a multi-task problem, this issue can be regarded as a negative transfer, which indicates challenges to achieve simultaneously satisfied performance across multiple tasks. In this work, we propose the Hybrid Sharing Query (HSQ), a transformer-based model that introduces the mixture-of-experts architecture to image multi-label classification. HSQ is designed to leverage label correlations while mitigating heterogeneity effectively. To this end, HSQ is incorporated with a fusion expert framework that enables it to optimally combine the strengths of task-specialized experts with shared experts, ultimately enhancing multi-label classification performance across most labels. Extensive experiments are conducted on two benchmark datasets, with the results demonstrating that the proposed method achieves state-of-the-art performance and yields simultaneous improvements across most labels. The code is available at https://github.com/zihao-yin/HSQ

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the issue of heterogeneity in the multi-label learning process. It transforms multi-label tasks into multi-task learning and innovatively incorporates the MoE model into visual classification tasks. Drawing inspiration from models like MMoE and PLE, the authors employed multiple experts and gating theories to learn various labels in their experiments. To prevent negative transfer during the model learning process, they also employed a shared expert approach to learn label correlations. Finally, the authors conducted experiments on the VOC and MS-COCO datasets and achieved outstanding performance.

### Strengths
1. Innovatively introducing the MoE model from the NLP field into the domain of computer vision, the paper achieved outstanding results. The use of gating and expert effectively enhanced the model's capacity for relationship modeling in multi-label tasks.
2. The paper's algorithmic description is concise and clear, with pseudo-code illustrating the core model workflow.
3. The experiments are comprehensive, including model comparisons, ablation studies, and visualizations.

### Weaknesses
1. In the ablation experiments section, there is a lack of explanation for the decrease in experimental performance, particularly why the performance declines when n_t is 1 and n_s is 0. The paper does not sufficiently explore the impact of varying quantities of n_s and n_t on the results, specifically, whether there is a saturation point or an optimal ratio between the two. The ablation study should include a more granular analysis of the performance impact when varying these parameters independently and in combination.
2. There is a lack of visualization of how different experts in the model process images. The paper would benefit from visualizing the feature maps or activation patterns of different experts for a given input image, to understand what each expert is learning and how they contribute to the final prediction. This would provide a more intuitive understanding of the model's inner workings.
3. Contribution 1 and Contribution 2 appear quite similar. The experiments on heterogeneity are not sufficiently intuitive, why is it solely demonstrated through experiments rather than being theoretically proven? The paper does not provide a theoretical justification for why the proposed method should be effective in addressing heterogeneity, relying solely on empirical results. A theoretical analysis, even a simplified one, would strengthen the claims.
4. The paper uses extensive textual descriptions in the methodology section; using formulas would provide a more concise representation. The methodology section is overly verbose and could be significantly condensed by using mathematical notation to describe the model architecture and the computations involved. This would improve clarity and conciseness.
5. Although the paper incorporates the MoE model, it has relatively few innovative aspects of its own. The application of MoE to multi-label classification is not novel in itself, and the paper does not introduce significant modifications or extensions to the MoE framework. The paper needs to clearly articulate the specific novel contributions beyond the mere application of an existing technique.

### Questions
1. What is the significance of Figure 6? The reduction in image resolution implies a decrease in information, which may lead to a decline in the model's performance. How does this relate to robustness?
2. What is the difference between hybrid experts and attention mechanisms? Is the model's good performance due to the introduction of a large number of parameters? Does MoE in the paper improve training speed? It is recommended to conduct an efficiency experiment to verify this question.
3. MoE models generally encounter the issue of load balancing. Is there a possibility that certain experts consistently dominate during the model training process? It is recommended to conduct an experiment to verify this question.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, the authors regard the multi-label image recognition task as a multi-task problem. To address the "label heterogeneity", the authors propose a transformer-based model, Hybrid Sharing Query (HSQ), that introduces the mixture-of-experts architecture to multilabel classification, which leverages label correlations while mitigating heterogeneity effectively. As presented in their experiment results, the proposed framework achieves state-of-the-art performance, which demonstrates the effectiveness of the proposed method.

### Strengths
1. It is novel that presenting a "mixture of experts" to the multi-label image recognition task, which is ignored in previous MLR works.
2. The design of the proposed framework is technically clear, and the experiment results demonstrate its effectiveness.

### Weaknesses
1. As the core motivation, the authors should provide a detailed and comprehensive discussion about "label heterogeneity" in MLR. Specifically, the paper needs to articulate how the feature space varies across different labels, leading to potential conflicts during joint training. A more thorough explanation of the underlying causes of this heterogeneity, such as variations in object appearance, context, or semantic relationships, would strengthen the motivation.
2. In the hybrid sharing layer, the distinction between task-specialized experts and semantic features in other MLR works is unclear. It is crucial to explain how these task-specific experts differ from standard feature representations used in other multi-label recognition models. Furthermore, the role and implementation of the shared experts group require more clarification. What specific mechanisms are in place to ensure these shared experts capture inter-label correlations effectively, and how does this differ from simply using a shared feature space?
3. The claim that "shared experts help to extract correlations between tasks, encourage positive correlation sharing and suppress negative transfer" needs more substantial evidence. While the ablation study shows a performance drop when shared experts are removed, it doesn't provide insight into *how* the shared experts achieve this. Visualizations or quantitative analyses demonstrating the specific features or patterns learned by the shared experts, and how these relate to different labels, would be beneficial.

### Questions
Please see the above weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a transformer-based approach with mixture-of-experts design for multi-label classification task.  The approach is design for better leveraging semantic correlation and heterogeneity among labels. The experiments on Pascal Voc and MSCOCO datasets show the effectiveness of the propose approach and get SoTA performance.

### Strengths
+ The paper offers valuable insights on multi-label classification, the solution based on MoE is a pretty novel view.

+ The approach achieves good results.

+ The paper is well-organized and have clear figures and demonstrations.

### Weaknesses
The main concern I have is in the experiment section.

1). The author missed some important experiments on MS-COCO.  The latest paper chosen for comparison is the ML-Decoder. However, the author didn't choose the same model backbone and the same image resolution to make a fair comparison. Besides, the model backbone pretraining details can also be an important factor in the model performance, so what's the difference between these methods?.

2). The ML-Decoder's code is available for years, the author should also fill the blanks in (CF1 OF1 CF1 OF1).

3). The ML-Decoder's paper and code is publicly available on arxiv at 2021, they didn't make any change to their best results even when they published to WACV 2023. This means all the results you compared with are before or in 2021, so why not choose some latest methods in 2022 and 2023 for comparison?

4). Please indicate the Flops and Parameters in the experiments and compared with the mentioned methods.

5). MSCOCO is a relatively small dataset with well annotated labels in the multi-label classification task. Why not using NUS-WIDE or OpenImages Dataset which are stronger benchmark and can also show the robustness of the model under the case with more labels and more data?

### Questions
Please answer the questions in [weaknesses].

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
