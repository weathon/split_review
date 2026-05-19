### Summary

The paper proposes a masked image modeling based self-supervised neural architecture search method, which can search for transformer architecture without human experts. The proposed method is based on the one-shot NAS framework. The proposed method adopts a teacher-student architecture, where the teacher network is pre-trained by the masked image modeling, and the student network is trained by the knowledge distillation from the teacher network. The proposed method can be trained without human experts. The searched architecture can achieve the state-of-the-art accuracy on the large-scale dataset.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method can search for the transformer architecture without human experts.
2. The proposed method achieves the state-of-the-art accuracy on the large-scale dataset.
3. The proposed method is evaluated on the large-scale dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on the image classification task. The proposed method is not evaluated on the other tasks such as object detection and semantic segmentation.
2. The proposed method is only evaluated on the vision transformer architecture. The proposed method is not evaluated on the other architectures such as CNN and MLP-Mixer.

### Suggestions

The paper's focus on image classification is a limitation, and the method's applicability to other vision tasks remains unclear. While the authors demonstrate state-of-the-art results on ImageNet, it is crucial to evaluate the method's performance on tasks like object detection and semantic segmentation. These tasks have different evaluation metrics and require different architectural considerations. For example, object detection often relies on bounding box regression and classification, which are not directly addressed by the proposed method. Similarly, semantic segmentation requires pixel-level predictions, which may not be achievable with the current architecture search strategy. The authors should consider evaluating their method on standard benchmarks for these tasks to demonstrate its generalizability. This would involve adapting the search space to include convolutional layers and normalization layers, which are commonly used in object detection and segmentation architectures. Furthermore, the evaluation should include a comparison with existing NAS methods that are specifically designed for these tasks, providing a more comprehensive understanding of the proposed method's strengths and weaknesses.

Another significant limitation is the exclusive evaluation on vision transformers. The method's performance on other architectures, such as CNNs and MLP-Mixer, remains unexplored. This is a critical oversight, as these architectures have different inductive biases and are widely used in various applications. For instance, CNNs are known for their ability to capture local features, which are essential for many vision tasks. MLP-Mixer, on the other hand, uses multi-layer perceptrons to process image patches, which is a departure from the traditional transformer architecture. Evaluating the proposed method on these architectures would require adapting the search space to include different types of layers and connections. The authors should consider evaluating their method on these architectures to demonstrate its versatility and potential for broader adoption. This would also involve comparing the performance of the searched architectures with existing NAS methods that are specifically designed for these architectures, providing a more comprehensive understanding of the proposed method's strengths and weaknesses.

Finally, the paper lacks a detailed analysis of the computational cost and efficiency of the proposed method. While the authors demonstrate state-of-the-art accuracy, it is important to consider the computational resources required for training and inference. The proposed method involves training a teacher-student architecture, which can be computationally expensive. The authors should provide a detailed analysis of the computational cost of the proposed method, including the training time, memory usage, and inference time. This analysis should also compare the computational cost of the proposed method with existing NAS methods. Furthermore, the authors should investigate the scalability of the proposed method to larger datasets and more complex architectures. This would provide a more comprehensive understanding of the practical implications of the proposed method and its potential for real-world applications.

### Questions

1. The proposed method is only evaluated on the image classification task. The proposed method is not evaluated on the other tasks such as object detection and semantic segmentation.
2. The proposed method is only evaluated on the vision transformer architecture. The proposed method is not evaluated on the other architectures such as CNN and MLP-Mixer.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
