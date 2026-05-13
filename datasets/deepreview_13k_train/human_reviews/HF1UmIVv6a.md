# ADAPT: Attentive Self-Distillation and Dual-Decoder Prediction Fusion for Continual Panoptic Segmentation

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Panoptic segmentation, which unifies semantic and instance segmentation into a single task, has witnessed considerable success on predefined tasks. However, traditional methods tend to struggle with catastrophic forgetting and poor generalization when learning from a continuous stream of new tasks. Continual learning, emerged to tackle these challenges, has garnered increasing attention in recent years. Nonetheless, our study reveals that existing continual panoptic segmentation (CPS) methods often suffer from efficiency or scalability issues. To address these limitations, we propose a novel dual-decoder framework that incorporates attentive self-distillation and prediction fusion to efficiently preserve prior knowledge while facilitating model generalization. Specifically, we freeze the majority of model weights up to the pixel decoder, which is shared between the teacher and student models, thus enabling efficient knowledge distillation with only a single forward pass. Attentive self-distillation then adaptively distills useful knowledge from the old classes without distracting from non-object regions, which mitigates the inherent bias toward newly learned tasks. Additionally, query-level fusion (QLF) is devised to seamlessly integrate the output of the dual decoders without incurring scale inconsistency. Crucially, the computational overhead of our approach remains nearly constant, regardless of the number of continual learning steps or the number of classes introduced at each step. Our method achieves state-of-the-art performance on the ADE20K benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenges in continual panoptic segmentation (CPS). In order to tackle catastrophic forgetting, the authors propose a dual-decoder Mask2Former framework combined with attentive self-distillation (called ADAPT) to efficiently retain past knowledge and generalize to new classes.

### Strengths
- The reviewer found the paper to be well-written and easy to understand.

- The reviewer likes the use of a dual-decoder framework that allows for knowledge retention with minimal computational costs.

- The paper also presents a solid self-distillation mechanism focuses on informative regions by down-weighting non-object areas, making knowledge retention more targeted. The reviewer finds the query-level fusion (QLF) strategy to eliminate the scale mismatch issues commonly found in probability-level fusion to be interesting.

### Weaknesses
 - Although the reviewer likes the idea of freezing the encoder as it reduces computational load and helps retain base knowledge, it may restrict the model's ability to adapt fully to new classes over very long sequences of tasks, particularly as the diversity or complexity of new classes increases. The authors can comment on this.

- On a similar note, while the authors report results with ResNet-50 backbone, it’s unclear to the reviewer how the method scales with larger models or higher-resolution images. The freezing and distillation mechanisms might still impose computational and memory limitations in more demanding setups.

- The author's might benefit from observing the effect of their method on open-vocab evaluation settings. Further, it may be interesting to evaluate on standard settings as well. For example, on COCO dataset with the number of classes growing in the number of tasks.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new method for continual panoptic segmentation. This task requires model to be able to adapt to new data and semantic classes, while maintaining the capabilities acquired from previous training stages. A key challenge in this task is catastrophic forgetting, which can result in significant performance degradation, especially for classes from earlier stages that are underrepresented in later stages. The method relies on mask transformer panoptic model and adresses the catastrophic forgetting by careful fine-tuning of only parts of the initial weights. Additionally, it enforces prediction consistency w.r.t. to earlier model instances while emphasizing the loss for informative queries. Finally, the predictions of the initial and the latest model are ensembled to maintain the balance between base and novel classes. The experiments are conducted on ADE20k panoptic dataset following continual learning setups from previous work.

### Strengths
The proposed method achieves state-of-the-art performance in continual panoptic segmentation on ADE20k dataset.

The method is computationally more efficient than related work. Due to the freezing of the backbone and the pixel decoder, teachers inference is consisted of only the transformer decoder. 

The ablation study reveals positive effects of the proposed contributions on the overall performance.

### Weaknesses
Paragraph describing query-level fusion should be better written. Implementation details or some equations might improve clarity of this part.

Presentation of the ablation and validation experiments could be of higher quality. I dont understand the necessity of subsection 4.5. The first table referenced in text is actually table 5, which makes it a bit confusing.

The advantages regarding the computational efficiency are not supported with any experimental results or analysis. Some table comparing training time or FLOPs in a single training iteration with the literature would make this more convincing. Similar analysis would be beneficial for the test-time inference as well. Dual-decoder prediction fusion obviously causes some computational overhead, and this is not measured in any way.

Dual decoder prediction fusion heavily relies on the assumption that most of the data and classes were available in the initial phase. What if this is not the case? Is a setup where most of the data and classes become available in some intermediate step possible in real applications? Perhaps this should be discussed.

The technical novelty of the presented contributions is limited. Self-distillation and weight freezing have already been considered in continual panoptic segmentation.

### Questions
Recently, vision-language models such as CLIP caused significant improvements in open-vocabulary panoptic segmentation (e.g. [1])? Would such design solve some technical challenges in continual panoptic segmentation (e.g. adding new classes)? Perhaps this approach trained in a regular way could represent another baseline for CPS?

[1] Yu, Q., He, J., Deng, X., Shen, X., & Chen, L. C. (2023). Convolutions die hard: Open-vocabulary segmentation with single frozen convolutional clip. Advances in Neural Information Processing Systems, 36, 32215-32234.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to resolve the efficiency or scalability issues in continual panoptic segmentation methods. A dual-decoder framework is proposed that incorporates attentive self-distillation and prediction fusion to preserve prior knowledge while facilitating model generalization. The majority of pixel decoder's weights are fixed and shared between the teacher and student models. Thus a single forward pass for efficient knowledge distillation can be achieved. Moreover, an attentive self-distillation is introduced to distill useful knowledge from the old classes without distracting from non-object regions. Additionally, a query-level fusion is introduced. to seamlessly integrate the outputs. Experimental evaluation is conducted on ADE20K dataset.

### Strengths
1. Clear figure illustration for methods.
2. Interesting idea for probability-level  fusion and query-level fusion.

### Weaknesses
Weaknesses: 

1. Lack of evidence for Computational Costs and Generalization

2. Need for Experimental Comparison on Computational Overhead

3. Limited Experimental Validation

4. Need for Further Improvement in Table Presentation

These concerns collectively emphasize the need for additional theoretical or experimental evidence and broader validation of the proposed method's claims and generalizability.

### Questions
1. [Line 057-058] Is the "raising computational costs" only occur during training? If so, does the computational cost of inference remain same? [Line 060-063] Why continuously introducing additional learnable query features and embeddings for new task is not good? Why this strategy "constrains the model's capacity to generalize to new tasks due to restricted plasticity"? Overall, the reviewer believes that if there are no theoretical or numerical experimental evidence, it would be better to do not judge methods from other areas.
2. [Line 138-139] Since there are many claims that "most of these methods require separate forward passes for the teacher and student models, resulting in considerable computational overhead.", please give clear comparison and experimental results to support.
3. Why the experiments are only conducted on one benchmark? At least two datasets should be involved to validate the generalization ability of the proposed method.
4. It is recommended to adjust the table size and position distribution.

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
5

### Summary
This paper introduces a novel approach for continual panoptic segmentation, addressing efficiency and scalability challenges faced by existing methods (e.g., CoMFormer’s computational limitations and ECLIPSE’s scalability issues). The authors propose an adaptation strategy that minimizes parameter updates by freezing the majority of model parameters, selectively fine-tuning cross-attention and feedforward layers in the transformer decoder. This is coupled with an attentive self-distillation mechanism to balance plasticity and rigidity effectively. Additionally, a dual-decoder prediction fusion strategy at the query level further enhances model performance. The proposed method, termed ADAPT, is empirically evaluated on the ADE20K dataset, showing improved performance in terms of both plasticity and rigidity over existing approaches.

### Strengths
## 1. Strong Motivation and Meaningful Contributions

- The paper is well-motivated, addressing key limitations in current methodologies: (1) CoMFormer’s limited rigidity and computational inefficiency, and (2) ECLIPSE’s restricted plasticity and scalability challenges.
- The proposed solution addresses these limitations effectively. Specifically, the selective fine-tuning of cross-attention and feedforward layers is a meaningful contribution that demonstrates the improved balance between model plasticity and rigidity.


## 2. Impressive Experimental Results

- ADAPT achieves state-of-the-art performance, significantly outperforming existing methods in continual panoptic segmentation tasks. 
- The experimental results demonstrate the effectiveness of the proposed solution, with a notable performance margin over alternative approaches.

### Weaknesses
# Weaknesses

## 1. Limited Insight into Mechanism Behind Parameter Freezing (L.209)

- While cross-attention layers and feedforward networks are activated, self-attention layers are frozen, as detailed in L.209. 
- However, the authors provide only empirical results (Table 2) without an in-depth analysis or hypothesis to support this choice. 
- A theoretical justification would strengthen the contribution. Specifically, it is unclear why freezing the self-attention layers, which are crucial for capturing long-range dependencies within the feature maps, would not hinder the model's ability to adapt to new tasks. The authors should provide a more detailed explanation of the underlying assumptions and potential trade-offs associated with this design choice.

## 2. Lack of Qualitative Analysis

- The paper would benefit from qualitative analysis to complement the quantitative results. 
- Such insights would enhance the reader’s understanding and provide explicit visual support for the model’s performance. For instance, visualizing segmentation masks for both base and novel classes would offer a clearer picture of the model's ability to maintain performance on previously learned classes while adapting to new ones. This is especially important in panoptic segmentation, where both semantic and instance-level accuracy are crucial.

## 3. Absence of Comparative Analysis on Training Efficiency

- Given that efficiency is one of the claimed contributions, a comparative analysis on training efficiency, such as training iteration throughput or GPU memory usage, would strengthen the paper. 
- A comparison between ADAPT, CoMFormer, and ECLIPSE on these training efficiency metrics would provide a fuller view of ADAPT’s performance. This should include a breakdown of the computational cost associated with each component of the model, such as the cross-attention, feedforward, and self-attention layers, to better understand the source of the efficiency gains.

## 4. Insufficient Details in Figure 2

- Figure 2 lacks clarity, particularly regarding color representations (e.g., which color represents a query or a specific class, such as sky). 
- It is also unclear which instances are misclassified in L.315-23. 
- Section 3.4 does not clarify (despite having 8 queries in the query-level fusion,) why the probability distribution includes only 4 scores.
- More detailed descriptions of the example base class set, new class set, and the query and color representations would aid comprehension. The authors should also clarify how the query-level fusion handles overlapping instances and how the final segmentation masks are generated from the fused query representations.

## 5. Ambiguity in Baseline Setting (Table 5)

- Table 5 lacks clarity regarding the baseline setting. 
- The baseline results without any additional components appear identical to CoMFormer’s results. 
- Clarification on whether this is a coincidence or an intentional baseline setting using CoMFormer would help clarify the impact of each proposed component.

## 6. Probability Inconsistency Analysis

- It is unclear which activation function was used to obtain class probabilities. 
- Mask2Former and CoMFormer use softmax, whereas ECLIPSE utilizes sigmoid. 
- If softmax was used, probability inconsistency may arise due to its relative scoring.
- But, If sigmoid was used, probability inconsistency may reduced.
-  An analysis comparing softmax and sigmoid’s impact on class probability consistency would be beneficial.

### Questions
Please check the weaknesses.

## Justification.

Overall, this paper makes significant contributions to the field of continual panoptic segmentation, demonstrating state-of-the-art results in both plasticity and rigidity. However, several areas require additional refinement to meet the high standards expected at ICLR, including more rigorous analysis, qualitative insights, and additional experimental details.

## Recommendation

Although my initial recommendation is 5: marginally below the acceptance threshold, my real rating is the Borderline.
My final decision will depend on the authors' rebuttal and any revisions addressing the outlined weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
