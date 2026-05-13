# General Compression Framework for Efficient Transformer Object Tracking

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Transformer-based trackers have established a dominant role in the field of visual object tracking. While these trackers exhibit promising performance, their deployment on resource-constrained devices remains challenging due to inefficiencies. To improve the inference efficiency and reduce the computation cost, prior approaches have aimed to either design lightweight trackers or distill knowledge from larger teacher models into more compact student trackers. However, these solutions often sacrifice accuracy for speed. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce the size of a pre-trained tracking model into a lightweight tracker with minimal performance degradation. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages, enabling the student model to emulate each corresponding teacher stage more effectively. Additionally, we also design a unique replacement training technique that involves randomly substituting specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. Our framework CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of CompressTracker. Our CompressTracker-4 with 4 transformer layers, which is compressed from OSTrack, retains about $\mathbf{96\%}$ performance on LaSOT ($\mathbf{66.1\%}$ AUC) while achieves $\mathbf{2.17\times}$ speed up.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors proposed a general model compression framework for efficient Transformer object tracking, named CompressTracker. The method adopts a novel stage partitioning strategy to divide the Transformer layers of the teacher model into different stages, enabling the student model to more effectively simulate each corresponding teacher stage. The authors also designed a unique replacement training technique, which involves randomly replacing specific stages in the student model with specific stages in the teacher model. Replacement training enhances the student model's ability to replicate the behavior of the teacher model. To further force the student model to simulate the teacher model, we combine predictive guidance and staged feature imitation to provide additional supervision during the compression process of the teacher model. The authors conducted a series of experiments to verify the effectiveness and generality of CompressTracker.

### Strengths
The author has clear ideas and the article is easy to understand. He proposes a general compression framework for single object tracking. This method can efficiently compress large object tracking models into small models. The author has conducted a large number of experiments to prove the effectiveness of this method.

### Weaknesses
1. The innovation is slightly insufficient. The author’s innovation focuses on replacement training, prediction guidance, and feature mimicking. The latter two are common methods of distillation and are not enough to be the innovation of this article. Therefore, the innovation of this article is more focused on the replacement training strategy, but the author’s explanation of the intuitive reasons why this strategy is useful is poor.
2. The author claims that the method is general compression framework, but the paper only experiments on OSTrack and MixFormerV2. However, there are many trackers based on transforemr, such as SimTrack, ODtrack, LoraT, etc. The reviewer thinks that it cannot be called general compression framework after only verifying two trackers.
3. The author only conducted experiments on GPUs with sufficient computing power. However, efficient trackers are more targeted at devices with insufficient computing power, such as CPUs and edge devices. The author did not conduct experiments on such devices to verify the term efficient.

### Questions
The application scenarios of efficient tracking models are mostly devices with insufficient examples. The author should provide the speed of the model on the CPU or edge device to verify the word "efficient", rather than just testing the speed on the GPU. For other issues, see weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents CompressTracker, a novel general model compression framework aimed at enhancing the efficiency of transformer-based object tracking models for deployment on resource-constrained devices. The framework employs a stage division strategy to segment the teacher model into distinct stages, which are then emulated by a lighter student model. CompressTracker introduces a replacement training technique, where student model stages are dynamically replaced with teacher model stages during training, enhancing the student's ability to replicate the teacher's behavior. Additionally, prediction guidance and stage-wise feature mimicking are incorporated to refine the learning process. The framework is structurally agnostic and compatible with various transformer architectures.

### Strengths
The paper proposes an innovative approach to segmenting transformer layers into stages, allowing for more granular knowledge transfer from a teacher model to a student model.

The experiments show that CompressTracker can achieve a substantial speedup while maintaining a high level of accuracy, which is crucial for real-world applications on resource-constrained devices.

The framework's compatibility with any transformer architecture is a significant advantage, as it increases its applicability and flexibility.

### Weaknesses
There is still a performance gap between the teacher and student models, indicating that there might be room for further improvement in the compression strategy to achieve lossless compression.

While the framework simplifies the compression process, the introduction of multiple training strategies might increase the complexity of the training regimen, which could be a barrier for some users.

### Questions
In the article, the framework proposed is added to OSTrack, where the search area pixels are 256× 256and the template pixels are 128× 128. What is the effect when the search area pixels are 384 × 384 and the template pixels are 192 × 192? Can tracking accuracy still be maintained?

What are the limitations of the stage division strategy, and how does it affect the generalization capabilities of the student model?

According to the experimental section, it can be seen that speed and accuracy cannot be achieved simultaneously. The faster the speed, the lower the accuracy. Taking OSTrack as an example, the encoder layer of OSTrack is 12 layers. Would it be possible to achieve a similar effect by reducing the number of layers appropriately? Will the compression method proposed in the article have more advantages in accuracy and speed?

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
This paper introduces a general model compression framework based on the teacher-student knowledge distillation method for efficient transformer object tracking, named CompressTracker, which designs a stage division strategy and a replacement training technique.

### Strengths
The motivation of this paper is clear and it has certain innovation.

### Weaknesses
Two classical models are only used to verify the effectiveness of the proposed CompressTracker, which are not enough to demonstrate its applicability and scalability.

1. OSTrack and MixFormer are only used to verify the effectiveness of the proposed CompressTracker. As a general model compression framework, this is far from enough.
2. This paper proposes a novel stage division strategy. To demonstrate its effectiveness, the corresponding ablation experimental results are shown in Table 8. It can be seen from Table 8 that the even dividing strategy is better than the uneven dividing strategy, but it cannot indicate that the performance of model with the stage division strategy is better than that without the stage division strategy.
3. What is the difference of the ablation experiments in Table 9 and 10?
4. Does CompressTracker only apply to the model with several same feature extractor modules? If the structures of different stages are different, does it work?
5. The format of Table 5 is non-standard. A table should not contain other tables.
6. There is spelling mistake, such as "Stucture Limitation" in Page 1.

### Questions
1. OSTrack and MixFormer are only used to verify the effectiveness of the proposed CompressTracker. As a general model compression framework, this is far from enough.
2. This paper proposes a novel stage division strategy. To demonstrate its effectiveness, the corresponding ablation experimental results are shown in Table 8. It can be seen from Table 8 that the even dividing strategy is better than the uneven dividing strategy, but it cannot indicate that the performance of model with the stage division strategy is better than that without the stage division strategy.
3. What is the difference of the ablation experiments in Table 9 and 10?
4. Does CompressTracker only apply to the model with several same feature extractor modules? If the structures of different stages are different, does it work?
5. The format of Table 5 is non-standard. A table should not contain other tables.
6. There is spelling mistake, such as "Stucture Limitation" in Page 1.

### Soundness
2

### Presentation
2

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
The paper presents CompressTracker, a framework for general model compression designed to enhance the efficiency of transformer-based object-tracking models. This approach utilizes a unique stage partitioning strategy that divides the transformer layers of the teacher model into distinct stages, allowing the student model to simulate each corresponding stage better.

Furthermore, the authors introduced a replacement training technique, where specific stages in the student model are randomly replaced with those from the teacher model. This strategy, combined with predictive guidance and staged feature imitation, provides additional supervision to help the student model mimic the teacher model more effectively during the compression process.

Extensive experiments on vit-based trackers were conducted, which show the proposed method can lightweight the trackers while main a comparable performance.

### Strengths
1. The author clearly presents a framework for compressing single object tracking models, effectively reducing larger models to smaller, efficient versions. Extensive experiments demonstrate the method's effectiveness.

2. One of the main benefits of the proposed framework is its structural agnosticism, meaning it can work with any transformer architecture. This adaptability allows CompressTracker to fit different student model configurations, making it suitable for various deployment environments and computational limits.

3. The paper shows through extensive experiments that CompressTracker strikes an impressive balance between inference speed and tracking accuracy. It significantly speeds up the tracking process while preserving high performance, achieving nearly 96% of the original accuracy with a 2.17× increase in speed.

### Weaknesses
1. The primary drawback of this method lies in its dependence on various distillation techniques, such as different training strategies, feature mimicking, and loss guidance. This lack of a clear, consistent framework among these techniques may undermine the generalization ability and transferability of the proposed approach, despite the author's assertions to the contrary. The specific implementation details of each distillation component, such as the loss functions used for feature mimicking and prediction guidance, are not clearly defined, making it difficult to assess their individual contributions and potential interactions. Furthermore, the method's reliance on multiple, seemingly independent techniques raises concerns about its robustness to different tracking scenarios and datasets.

2. Moreover, the overall complexity of the method raises concerns about its usability for other researchers. For instance, when applied to Mixformer V2, which has only two layers, the improvement in performance is minimal, while the processing speed remains unchanged. Such results indicate possible limitations of the method, as the intricate techniques lead to only marginal benefits. The lack of substantial improvement on a simpler architecture like Mixformer V2 suggests that the proposed framework might be overly complex for models with fewer layers, and the overhead of the multiple distillation techniques might outweigh their benefits. This raises questions about the practical applicability of the method to a wide range of transformer-based trackers.

3. The proposed techniques (stage division, progressive replacement, Replacement Training, Prediction Guidance, and Stage-wise Feature Mimicking) appear to be independent. The title "General Framework" raises my expectations significantly. The lack of clear interdependencies between these techniques makes it difficult to understand how they collectively contribute to the overall performance of the framework. The absence of a unified theoretical framework that explains the interactions between these techniques further weakens the claim of a general framework.

### Questions
See weakness.  Moreover, the paper does not compare with other model compression techniques, such as knowledge distillation, model quantization, and pruning. It helps if you provide some comparisons or analysis.

### Soundness
3

### Presentation
3

### Contribution
3
