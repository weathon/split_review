### Summary

This paper proposes a novel self-supervised neural architecture search method, Masked Distillation, which leverages masked image modeling to automatically design efficient transformer architectures. By eliminating the need for data labeling, Masked Distillation significantly reduces the high costs associated with supervised learning and facilitates the efficient training of transformer supernets. The proposed siamese teacher-student architecture and the unsupervised evaluation metric based evolutionary search algorithm further enhance the learning efficiency and accuracy of the search process.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

* This paper is well-written and well-organized. The method is clearly described.
* The proposed method is technically sound.
* The experimental results on CIFAR-10, CIFAR-100, and ImageNet datasets demonstrate that the method achieves state-of-the-art accuracy without using manual labels.

### Weaknesses

#### Some Related Works


#### comment

 * The technical contribution is incremental. The proposed method is a combination of existing methods.
* The evaluation is insufficient. The proposed method should be evaluated on more downstream tasks.
* The proposed method seems to be very computationally expensive. The computational cost should be reported and compared with other methods.

### Suggestions

The paper's primary weakness lies in its incremental technical contribution. While the combination of masked image modeling (MIM) and knowledge distillation (KD) for neural architecture search (NAS) is presented as novel, the core components are established techniques. The paper should more clearly articulate the specific novelty in their combination and why this particular approach is superior to other possible integrations of MIM and KD for NAS. A more detailed analysis of the specific challenges in applying MIM to supernet training, and how the proposed method addresses these challenges, would strengthen the contribution. For example, the paper could discuss the specific difficulties in training a supernet with MIM loss alone, and how the addition of KD loss mitigates these issues, providing a more in-depth understanding of the method's technical merit. Furthermore, a comparison with other existing methods that use MIM for training, and a discussion of why those methods are not directly applicable to NAS, would be beneficial.

To address the insufficient evaluation, the paper should include a more comprehensive set of downstream tasks. While the classification results on CIFAR, CIFAR-100, and ImageNet are promising, these datasets are relatively similar in nature. Evaluating the method on more diverse datasets, such as those with different modalities (e.g., text, audio) or tasks (e.g., object detection, segmentation), would provide a more robust assessment of the method's generalization capabilities. Specifically, the paper should consider evaluating on datasets with different characteristics, such as those with imbalanced classes, or those with a smaller number of training samples. This would help to demonstrate the robustness of the proposed method. Additionally, the paper should provide a more detailed analysis of the performance of the searched architectures on these downstream tasks, including a comparison with manually designed architectures.

Finally, the paper needs to provide a more thorough analysis of the computational cost of the proposed method. While the paper mentions the efficiency of the method, it lacks a detailed comparison with other NAS methods. The paper should report the total training time, GPU hours, and FLOPs for the proposed method and compare these metrics with other state-of-the-art NAS methods. This comparison should include both the training time for the supernet and the evaluation time for the searched architectures. Furthermore, the paper should discuss the scalability of the method to larger datasets and more complex architectures. This would help to understand the practical limitations of the proposed method and its applicability to real-world problems.

### Questions

Please refer to the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
