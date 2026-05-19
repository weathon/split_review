### Summary

This paper proposes a prompt gradient projection (PGP) method to reduce forgetting in continual learning. Specifically, the authors first derive the orthogonal condition of anti-forgetting for prompt gradient and then conduct Singular Value Decomposition (SVD) on an element-wise sum space between input space and prompt space to obtain the gradient projection matrix. The proposed method is validated on four benchmark datasets under three incremental settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. It is the first work to study the anti-forgetting mechanism of prompt tuning.
2. The authors provide a theoretical guarantee for the proposed method.
3. The authors conduct comprehensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only conduct experiments on small-scale datasets. It would be better to conduct experiments on large-scale datasets, such as ImageNet, to further demonstrate the effectiveness of the proposed method.
2. The authors only conduct experiments on image classification tasks. It would be better to conduct experiments on more challenging vision tasks, such as object detection and semantic segmentation, to further demonstrate the effectiveness of the proposed method.
3. The authors only conduct experiments on ViT. It would be better to conduct experiments on more architectures, such as ResNet, to further demonstrate the effectiveness of the proposed method.
4. The authors only compare with the prompt tuning method. It would be better to compare with other continual learning methods, such as gradient-based and rehearsal-based methods, to further demonstrate the effectiveness of the proposed method.
5. The authors only compare with DualPrompt. It would be better to compare with more prompt tuning methods, such as CoOp and CoOp2, to further demonstrate the effectiveness of the proposed method.
6. The authors only compare with the class-incremental learning setting. It would be better to compare with the domain-incremental learning setting to further demonstrate the effectiveness of the proposed method.

### Suggestions

The paper introduces an interesting prompt gradient projection method for continual learning, but its evaluation is limited in several key aspects. The experiments are primarily conducted on small-scale image classification datasets using ViT architectures and compared only against other prompt tuning methods. To strengthen the paper, it is crucial to evaluate the proposed method on larger, more complex datasets such as ImageNet, which would provide a more robust assessment of its scalability and effectiveness. Furthermore, the evaluation should be extended to more challenging vision tasks like object detection and semantic segmentation. These tasks often involve more complex data and require more sophisticated models, which would provide a more comprehensive understanding of the method's capabilities and limitations. The current evaluation is insufficient to demonstrate the broad applicability of the proposed method.

Additionally, the paper should explore the performance of the proposed method with different architectures, such as ResNet, which is widely used in computer vision. This would help to determine whether the method is specific to ViT or if it can be generalized to other architectures. The current focus on ViT limits the scope of the findings and makes it difficult to assess the method's practical relevance. Furthermore, the comparison with other continual learning methods is lacking. The paper should include comparisons with gradient-based and rehearsal-based methods, which are commonly used in continual learning. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses relative to existing approaches. The current comparison only with prompt tuning methods does not provide a complete picture of the method's performance.

Finally, the evaluation should be expanded to include more prompt tuning methods, such as CoOp and CoOp2, which are state-of-the-art in prompt tuning. This would provide a more thorough comparison within the prompt tuning domain. The current comparison only with DualPrompt is insufficient to demonstrate the method's superiority over other prompt tuning approaches. Moreover, the evaluation should include the domain-incremental learning setting, which is a more challenging scenario than class-incremental learning. This would provide a more comprehensive understanding of the method's ability to handle different types of distribution shifts. The current focus on class-incremental learning limits the scope of the findings and makes it difficult to assess the method's practical relevance in real-world scenarios.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
