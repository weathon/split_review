### Summary

This paper proposes an active learning algorithm for image segmentation, with the goal of reducing the labeling burden on the human oracles. The proposed framework identifies a batch of informative images, together with a list of semantic classes for each, and the human annotator merely has to answer whether a given semantic class is present or absent in a given image. The image and class selection is posed as a constrained optimization problem and a linear programming relaxation is derived to select a batch of (image-class) pairs.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

+ The proposed method is interesting and practical.
+ The paper is easy to follow.
+ The experiments on three datasets show the promising performance.

### Weaknesses

#### Some Related Works


#### comment

 - The authors claim that this is the first research effort to develop an active learning framework for image segmentation, which poses only binary (yes/no) queries to the users. However, I think the proposed method is just a simple extension of active learning to image segmentation. The technical contribution is not significant.
- The proposed method is quite simple and straightforward. The authors should discuss the limitations of the proposed method.
- The authors should discuss the relationship between the proposed method and other active learning methods in detail.
- The authors should discuss the computational complexity of the proposed method.
- The authors should provide the performance comparison with more recent methods in the field of active learning.
- The authors should provide the performance comparison with more recent methods in the field of image segmentation.

### Suggestions

The paper's core idea of applying binary queries within an active learning framework for image segmentation is interesting, but the technical novelty needs to be more clearly articulated. The authors should delve deeper into the specific challenges of adapting active learning to the image segmentation domain, particularly the high dimensionality of the output space and the computational cost of evaluating segmentation models. A more thorough discussion of how the proposed method addresses these challenges, beyond simply stating the use of binary queries, is needed. For instance, how does the method handle the inherent ambiguity in binary feedback for complex scenes with multiple objects? The paper should also explore the potential for incorporating uncertainty estimates from the segmentation model into the query selection process, which could lead to more informative binary queries. Furthermore, the authors should provide a more detailed analysis of the trade-offs between the simplicity of the binary feedback mechanism and the potential loss of fine-grained information compared to methods that utilize more detailed annotations.

To strengthen the paper, the authors should provide a more comprehensive discussion of the limitations of their approach. While the simplicity of the binary feedback is a strength, it may also be a limitation in scenarios where precise boundary information is crucial. The authors should explore how the proposed method performs in such cases and discuss potential strategies for mitigating these limitations. For example, could the method be extended to incorporate a small amount of pixel-level annotation to refine the segmentation boundaries after the initial binary queries? Additionally, the authors should discuss the sensitivity of the method to the choice of the base segmentation model and the impact of different segmentation architectures on the overall performance. A more detailed analysis of the computational cost of the proposed method, including the time required for query selection and model training, is also needed. This analysis should consider the scalability of the method to larger datasets and more complex segmentation tasks.

Finally, the paper would benefit from a more thorough comparison with existing active learning methods, particularly those that have been applied to image segmentation. The authors should not only compare the performance of their method with these baselines but also discuss the differences in their query selection strategies and the types of annotations they utilize. A detailed analysis of the strengths and weaknesses of each method would provide a more comprehensive understanding of the proposed approach's contribution to the field. Furthermore, the authors should consider comparing their method with recent weakly supervised segmentation techniques, as these methods also aim to reduce the annotation burden. A discussion of the similarities and differences between these approaches and the proposed method would help to clarify the unique contributions of this work. The authors should also consider including a discussion of the potential for combining the proposed method with other active learning techniques to further improve performance.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
