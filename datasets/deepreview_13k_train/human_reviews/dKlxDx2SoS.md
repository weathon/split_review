# Prompt Learning with Quaternion Networks

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Multimodal pre-trained models have shown impressive potential in enhancing performance on downstream tasks. However, existing fusion strategies for modalities primarily rely on explicit interaction structures that fail to capture the diverse aspects and patterns inherent in input data. This yields limited performance in zero-shot contexts, especially when fine-grained classifications and abstract interpretations are required. To address this, we propose an effective approach, namely Prompt Learning with Quaternion Networks (QNet), for semantic alignment across diverse modalities. QNet employs a quaternion hidden space where the mutually orthogonal imaginary axes capture rich intermodal semantic spatial correlations from various perspectives. Hierarchical features across multilayers are utilized to encode intricate interdependencies within various modalities with reduced parameters. Our experiments on 11 datasets demonstrate that QNet outperforms state-of-the-art prompt learning techniques in base-to-novel generalization, cross-dataset transfer, and domain transfer scenarios with fewer learnable parameters. The source code is available at https://github.com/VISION-SJTU/QNet.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the challenges and limitations of multimodal pre-trained models in capturing diverse and complementary features across different modalities. It introduces a novel approach called QNet, which utilizes quaternion networks to improve the modality fusion capacities of pre-trained models.

### Strengths
The use of quaternion networks to capture the intricate relationships among different modalities is a novel idea that sets this paper apart from existing methods. The paper provides a thorough analysis of the proposed method, including experimental results on various datasets and comparison with existing methods. The results are presented in a clear and concise manner.

The paper is well-written and organized, making it easy to follow the proposed approach and understand the experimental results.

### Weaknesses
Overall, this paper presents a sound framework. My main concern is that the authors should compare to the baseline scombining Quaternion Networks and the existing prompt learning method clearly. Besides, the benefits of QNet can be evaluated on more multimodal tasks.

### Questions
Please see my comments on the weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to improve the performance of a multi-modal pre-trained foundation model via prompt tunning. This work proposes to use Quaternion Networks to align the semantics across modalities while finetuning. Quaternion Network projects feature quaternion hidden space, where three mutually orthogonal imaginary axes, namely i, j, and k, allocate unique weights to various distribution features from diverse perspectives. Compared to previous prompt learning works, the major difference is introducing quaternion hidden space to fuse data modalities. This work conducts experiments on more than 10 datasets which is solid to some extent.

Pros:
- This work introduces quaternion hidden space to prompt learning for foundation models, which is new.
- Experiments cover a wide range of datasets.

Cons:
- Comparing the proposed method with previous prompt learning methods on computation overhead and latency is needed.
- Quaternion hidden space seems to be more sophisticated than linear space which might be better than linear projection. However, it's not obvious why Quaternion Networks is better than the previous prompting technique; or why tunning multimodal pre-trained networks needs quaternion hidden space. 


In-depth comparison with previous prompting methods and analysis of this quaternion network improve this work.

### Strengths
Pros:
- This work introduces quaternion hidden space to prompt learning for foundation models, which is new.
- Experiments cover a wide range of datasets.

### Weaknesses
Cons:
- Comparing the proposed method with previous prompt learning methods on computation overhead and latency is needed.
- Quaternion hidden space seems to be more sophisticated than linear space which might be better than linear projection. However, it's not obvious why Quaternion Networks is better than the previous prompting technique; or why tunning multimodal pre-trained networks needs quaternion hidden space.

### Questions
-

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper devised a method that combines a pre-trained model to achieve high performance in VL tasks even in situations where there is no training data. It also achieved excellent benchmark results in three validation tests: base-to-novel generalization, cross-dataset transfer, and domain transfer scenarios, even compared to MaPLE, one of the latest models.

### Strengths
Benchmark tests have been conducted and it has achieved excellent results compared to SOT methods. The benchmarks are also reasonable and provide excellent comparisons.

### Weaknesses
The structure of the model shown in Figure 2 is poorly explained, making it difficult to understand the difference between it and other models. I also got the impression that there was a lack of consideration as to why MaPLE achieved such excellent results. I would have liked a more detailed chapter to explain why this model is so good.

### Questions
None

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
