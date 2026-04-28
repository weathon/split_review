# Robust Multimodal Learning with Missing Modalities via Parameter-Efficient Adaptation

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Multimodal learning seeks to utilize data from multiple sources to improve the overall performance of downstream tasks. It is desirable for redundancies in the data to make multimodal systems robust to missing or corrupted observations in some correlated modalities. However, we observe that the performance of several existing multimodal networks significantly deteriorates if one or multiple modalities are absent at test time. To enable robustness to missing modalities, we propose a simple and parameter-efficient adaptation procedure for pretrained multimodal networks. In particular, we exploit modulation of intermediate features to compensate for the missing modalities. We demonstrate that such adaptation can partially bridge performance drop due to missing modalities and outperform independent, dedicated networks trained for the available modality combinations in some cases. The proposed adaptation requires extremely small number of parameters (e.g., fewer than 1\% of the total parameters) and applicable to a wide range of modality combinations and tasks. We conduct a series of experiments to highlight the missing modality robustness of our proposed method on five different multimodal tasks across seven datasets. Our proposed method demonstrates versatility across various tasks and datasets, and outperforms existing methods for robust multimodal learning with missing modalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for multimodal learning with missing modalities. The writing is good. The experiments are suffcient. However, the math behind it is not clear, and the author does not give a reason why the data with missing modalities is not considered in the training phase.

### Strengths
The writing is good. The experiments are suffcient.

### Weaknesses
The math behind this paper is not clear, specifically how the adaptation parameters are derived and updated. The description of the adaptation process lacks sufficient detail, making it difficult to understand the underlying mechanism. It's unclear how the adaptable layers are initialized and how they interact with the frozen layers during training. Furthermore, the paper does not provide a clear justification for why data with missing modalities is excluded during the initial training phase. This raises concerns about the generalizability of the learned representations, as the model is not exposed to the full spectrum of data variations during pre-training. The choice of datasets is also a limitation, as the experiments are primarily focused on segmentation and sentiment analysis. The lack of diversity in data types and tasks makes it difficult to assess the robustness and applicability of the proposed method to other multimodal learning problems. Finally, Figure 1 is not clear in its depiction of the adaptable layers and their interaction with the frozen layers, making it hard to grasp the overall architecture.

### Questions
The datasets are not diverse enough. The authors only considered segmentation and sentiment analysis problems, different types of data should be considered. Figure 1 is not clear.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a parameter-efficient adaptive method based on pre-trained multi-modal networks. This method recovers the missing modality by introducing a low-rank adaptive layer and a modulation scheme of intermediate features. Furthermore, this paper proves a simple linear operations can partially compensate for the performance degradation caused by missing modality. Finally, this paper conducts sufficient experiments on different datasets, showing the robustness and versatility of the proposed method.

### Strengths
1.This paper proposes an efficient approach to drive a multimodal model that adapts to different modality combinations, effectively addressing the performance degradation caused by missing modalities during testing. 

2.The proposed method introduces only 0.7% of model parameters and achieves comparable performance to dedicated models on certain datasets. 

3.Extensive experiments on multiple datasets demonstrate the superior performance of the proposed method compared to mainstream MML algorithms in handling the issue of missing modalities. 

4.The writing of this paper is coherent, presenting clear contributions.

### Weaknesses
1.The method only uses zero to replace missing modalities, lacking other compensation methods such as duplicating available modal data or utilizing cross-modal generation techniques to fully showcase the impact of missing modalities. Specifically, the paper does not explore the impact of using simple imputation techniques such as mean or median imputation, which could serve as a more robust baseline for comparison. Furthermore, the method does not consider more advanced techniques like generative models to synthesize missing modalities, which could potentially lead to a more comprehensive evaluation of the proposed approach.

2.The method's SSF strategy is an input-independent adaptation approach, it struggles to maintain reliable performance in scenarios with significant distribution differences between the training and testing sets. This input-agnostic nature of SSF may limit its ability to adapt to domain shifts or variations in the input data distribution, potentially leading to performance degradation when the testing data deviates significantly from the training data. The paper does not provide an analysis of the method's performance under such distribution shifts.

3.Table 9 shows that there is still a gap compared to other adaptation method (BitFit), which makes the advantages of the proposed SSF strategy not obvious enough. The performance difference, while small, raises questions about the practical advantages of SSF over existing parameter-efficient fine-tuning methods, especially given that BitFit is a simpler approach. The paper should provide a more detailed analysis of the trade-offs between SSF and BitFit in terms of performance, computational cost, and ease of implementation.

4.In Table 8 of the experimental section, the proposed method still exhibits a considerable performance gap compared to dedicated models. Can increasing the number of adaptation layer parameters further improve performance? The paper does not explore the impact of varying the number of adaptation layers or the dimensionality of the low-rank matrices used in the adaptation process. This lack of ablation studies makes it difficult to assess the sensitivity of the method to the choice of these hyperparameters.

### Questions
See above weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the problem of missing modalities at test time for multimodal learning. The motivation is to introduce small number of (new) parameters as much as possible during adpatation of a pre-trained model. The paper proposes parameter-efficient adpatation of multimodal networks.  Three different parameter-efficient adaptation techniques, including low-rank adpatation, scaling and shifting of features, and BitFit, have been investigated towards learning a model robust to missing modalities. Given a pre-trained network, in order to adapt this model to a subset of modalities, small set of parameters (as a layer) are introduced after each layer of the network. During adaptation to this subset of modality combination, only these small set of parameters are trained. Experiments have been performed with two different base networks for the task of multimodal semantic segmentation and multimodal sentiment analyses. Results claim to achieve better performance than competing robust methods and often surpass dedicated models.

### Strengths
- Development of multimodal learning algorithms robust to missing modalities is crucial since observations from some modality could go often be missing due to sensor/hardware failure.

- The proposed method is effective and importantly efficient as it introduces a very small set of parameters towards making a pre-trained model robust to missing modalities.

- The paper is mostly well-written and easier to read.

- Experiments have been performed on two different tasks of multimodal semantic segmentation and multimodal sentiment analyses. Results claim to surpass the existing methods and (often) dedicated methods when the modalities are missing at test time.

### Weaknesses
 - Although the idea is simple and effective for achieving parameter-efficient adaptation of models, the application of existing techniques (i.e. low rank adaptation, scale and shift transformations, and BitFit) to adapt a pre-trained model on a subset of modalities seems low from novelty aspect.


- There is no insight and/or analyses into how the proposed paramater-efficient is helpful towards making the model robust to missing modalities. It is important to develop the grounding of the proposed method since only showing improvements over the baseline with empirical results doesn't help much towards this.

- The paper doesn’t mention any clear justification on why SSA was chosen over the LoRA and BitFit to report the results in the paper.

- Comparison is missing with any of the existing method for the task of multimodal sentiment analyses. 

- Why CMU-MOSI and CMU-MSEI datasets were chosen to evaluate and report the performance of the method?

### Questions
- There is no study that fairly compares the parameter efficiency of the proposed method with competing methods?

- What are the possible reasons for relatively lower performance of other adaptation strategies, compared to SSA, in Table 4? Some explanation would be helpful to better understand their comparison in missing modalities scenario.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces parameter-efficient adaptation to make multi-modal segmentation more robust in the face of missing modalities, and it compares various methods, demonstrating promising results.

### Strengths
1, The method in this paper utilizes parameter-efficient fine-tuning to make the model adapt to modality loss, which I find relatively straightforward. The performance is also quite good.

2, The paper is well-written and relatively easy to read.

### Weaknesses
1, The method proposed in this paper may not be directly applicable to scenarios where the training set has missing modalities. Specifically, the approach relies on fine-tuning a pre-trained model, which implicitly assumes that all modalities are present during the initial pre-training phase. This limits its applicability in real-world scenarios where certain modalities might be consistently absent during training.

2, The method proposed in this paper lacks extensive comparisons with other methods~(for example, [1,2,3]) in the context of multimodal classification tasks, which significantly undermines the persuasiveness of Table 5. The absence of comparisons with methods that explicitly address missing modalities, such as those employing shared-specific feature modeling or robust fusion strategies, makes it difficult to assess the true novelty and effectiveness of the proposed approach. The current evaluation is limited to ablation studies and comparisons with a baseline model, which is insufficient to demonstrate state-of-the-art performance.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
