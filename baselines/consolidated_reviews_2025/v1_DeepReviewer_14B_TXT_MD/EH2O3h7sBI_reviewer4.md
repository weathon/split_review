### Summary

This paper proposes a prompt gradient projection (PGP) for continual learning. The proposed method is based on the observation that prompt-tuning releases the necessity of task identifier for gradient projection method; and gradient projection provides theoretical guarantees against forgetting for prompt-tuning. The authors deduce that reaching the orthogonal condition for prompt gradient can effectively prevent forgetting via the self-attention mechanism in vision-transformer. The condition equations are then realized by conducting Singular Value Decomposition (SVD) on an element-wise sum space between input space and prompt space. The proposed method is validated on diverse datasets and experiments demonstrate the efficiency of reducing forgetting both in class incremental, online class incremental, and task incremental settings.

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
5. The authors only compare with the DualPrompt. It would be better to compare with more prompt tuning methods, such as CoOp and CoOp2, to further demonstrate the effectiveness of the proposed method.
6. The authors only compare with the class-incremental learning setting. It would be better to compare with the domain-incremental learning setting to further demonstrate the effectiveness of the proposed method.

### Suggestions

The paper introduces an interesting approach to continual learning by combining prompt tuning with gradient projection. However, the experimental evaluation is limited in several aspects, which needs to be addressed to strengthen the paper's claims. Specifically, the experiments are primarily conducted on small-scale datasets like CIFAR-100, which may not fully reflect the performance of the proposed method on more complex, real-world scenarios. It is crucial to evaluate the method on larger datasets, such as ImageNet, to assess its scalability and effectiveness in handling a greater number of classes and more diverse data distributions. Furthermore, the current evaluation focuses solely on image classification tasks. To demonstrate the broader applicability of the proposed method, it is necessary to evaluate it on more challenging vision tasks, such as object detection and semantic segmentation, which involve more complex data and require different types of reasoning. These additional experiments would provide a more comprehensive understanding of the method's capabilities and limitations.

Additionally, the experiments are limited to the Vision Transformer (ViT) architecture. While ViT is a popular choice, it is important to evaluate the proposed method on other widely used architectures, such as ResNet, to determine its generalizability across different model types. This is particularly important because the self-attention mechanism, which is central to the proposed method, is not present in all architectures. Evaluating the method on ResNet would help to understand how the gradient projection is adapted to different architectural components and whether the method can be effectively applied to convolutional neural networks. Moreover, the paper only compares the proposed method with other prompt tuning methods. To provide a more comprehensive evaluation, it is necessary to compare it with other continual learning methods, such as gradient-based and rehearsal-based approaches. This would help to understand the relative strengths and weaknesses of the proposed method compared to existing techniques and provide a clearer picture of its contribution to the field.

Finally, the paper only compares the proposed method with DualPrompt, which is a specific prompt tuning method. To provide a more thorough comparison within the prompt tuning domain, it is necessary to compare it with other state-of-the-art prompt tuning methods, such as CoOp and CoOp2. This would help to understand the relative performance of the proposed method compared to other approaches and provide a more comprehensive evaluation of its effectiveness. Furthermore, the paper only focuses on class-incremental learning. To demonstrate the method's ability to handle different types of distribution shifts, it is necessary to evaluate it in a domain-incremental learning setting. This would provide a more comprehensive understanding of the method's robustness and its ability to adapt to different types of continual learning scenarios.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
