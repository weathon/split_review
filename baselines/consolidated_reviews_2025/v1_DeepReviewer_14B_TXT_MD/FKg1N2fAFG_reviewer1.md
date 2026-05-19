### Summary

This paper proposes several techniques to mitigate architecture overfitting in dataset distillation, which occurs when the performance of a distilled dataset is poor on network architectures different from the one used for distillation. The authors propose a DropPath variant with a three-phase keep rate, knowledge distillation from a smaller teacher network, a periodical learning rate scheduler, and a stronger data augmentation scheme. The paper evaluates these techniques on two dataset distillation algorithms (FRePo and MTT) and shows that they improve the performance of various network architectures (ResNet18, AlexNet, VGG11, ResNet50) when trained on the distilled datasets. The paper also demonstrates that these techniques improve the performance of training on limited real data.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper addresses the important issue of architecture overfitting in dataset distillation, which has not been explored much in previous works.
- The proposed techniques are generic and can be applied to different model architectures and training schemes.
- The paper conducts extensive experiments on different datasets, IPCs, and network architectures to demonstrate the effectiveness of the proposed methods.
- The paper is well-written and organized, with clear figures and tables.

### Weaknesses

#### Some Related Works

[1] Dataset Distillation via Factorization
[2] Remember the Past: Distilling Datasets into Addressable Memories for Neural Networks
[3] Dataset Distillation by Matching Training Trajectories
[4] CAFE: Channel Alignment for Efficient Dataset Distillation

#### comment

 - The paper does not compare with recent dataset distillation methods such as DAT [1], ReCa [2], MTD [3], and CAFE [4]. These methods may have addressed the issue of architecture overfitting or have better performance than the proposed methods.
- The proposed methods are not novel and are borrowed from other domains such as regularization, knowledge distillation, and optimization. The paper does not provide sufficient justification for why these methods are suitable for dataset distillation.
- The paper does not provide any theoretical analysis or bounds for the proposed methods. The paper relies solely on empirical results.
- The paper does not discuss the limitations or future directions of the proposed methods.

### Suggestions

The paper should provide a more thorough comparison with recent dataset distillation methods, especially those that address architecture overfitting. Specifically, the experimental section should include a comparison with DAT, ReCa, MTD, and CAFE, using the same experimental setup and metrics. This would allow for a more accurate assessment of the proposed method's performance relative to the state-of-the-art. Furthermore, the paper should analyze the performance of the proposed method on different datasets and network architectures to understand its generalization capabilities. It is important to determine if the method performs consistently across different settings or if it is sensitive to specific choices of datasets or architectures. The paper should also investigate the computational cost of the proposed method compared to other methods, as this is an important factor for practical applications.

To address the lack of novelty, the paper should provide a more detailed justification for why the chosen techniques are suitable for dataset distillation. The paper should explain how DropPath, knowledge distillation, periodical learning rate, and stronger data augmentation specifically address the challenges of dataset distillation, such as the need to preserve information in a small set of images. The paper should also discuss the potential limitations of these techniques in the context of dataset distillation. For example, how does DropPath affect the quality of the distilled images? How does the choice of teacher network affect the performance of knowledge distillation? The paper should also explore alternative techniques that may be more suitable for dataset distillation.

Finally, the paper should provide a theoretical analysis of the proposed methods. This could include an analysis of the convergence properties of the optimization algorithm, the generalization bounds of the distilled dataset, or the relationship between the distilled dataset and the original dataset. The paper should also discuss the limitations of the proposed methods and suggest future directions for research. For example, the paper could discuss the challenges of applying the proposed methods to larger and more complex datasets, or the potential for combining the proposed methods with other dataset distillation techniques. The paper should also discuss the ethical implications of dataset distillation, such as the potential for bias or misuse of distilled datasets.

### Questions

1. How does the proposed method compare with recent dataset distillation methods that address architecture overfitting, such as DAT [1], ReCa [2], MTD [3], and CAFE [4]?
2. What is the theoretical basis for the proposed methods? How do they affect the generalization bounds of the distilled dataset?
3. What are the limitations and future directions of the proposed methods? How can they be improved or extended?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
