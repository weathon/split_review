### Summary

This paper proposes a masked image modeling based self-supervised neural architecture search method, termed as MaskTAS, which can search for transformer architecture without human experts. The proposed MaskTAS can achieve state-of-the-art accuracy on the large-scale dataset, such as ImageNet. The proposed MaskTAS can generalize well to various data domains by searching specialized transformer architectures in a self-supervised manner.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper proposes a masked image modeling based self-supervised neural architecture search method, termed as MaskTAS, which can search for transformer architecture without human experts. 
2. The proposed MaskTAS can achieve state-of-the-art accuracy on the large-scale dataset, such as ImageNet.
3. The proposed MaskTAS can generalize well to various data domains by searching specialized transformer architectures in a self-supervised manner.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed MaskTAS is only evaluated on the image classification task. The proposed MaskTAS is not evaluated on the other tasks such as object detection and semantic segmentation.
2. The proposed MaskTAS is only evaluated on the vision transformer architecture. The proposed MaskTAS is not evaluated on the other architectures such as CNN and MLP-Mixer.

### Suggestions

The paper introduces an interesting approach to self-supervised neural architecture search (NAS) using masked image modeling (MIM). However, the evaluation is limited to image classification, which does not fully demonstrate the potential of the proposed MaskTAS method. To strengthen the paper, it is crucial to evaluate the method on more complex tasks such as object detection and semantic segmentation. These tasks would provide a more comprehensive understanding of the method's capabilities and limitations. For object detection, the evaluation should include standard datasets like COCO, and for semantic segmentation, the performance on ADE20K should be reported. Furthermore, the evaluation should not only focus on accuracy but also on other metrics such as mean average precision (mAP) for object detection and pixel accuracy for semantic segmentation. This would provide a more complete picture of the method's performance across different tasks and datasets.

In addition to expanding the task scope, it is also important to evaluate the MaskTAS method on a wider range of architectures. While the paper demonstrates the effectiveness of the method on vision transformers (ViTs), it is essential to assess its performance on other architectures such as convolutional neural networks (CNNs) and MLP-Mixers. This would help to determine the generalizability of the method and its applicability to different types of neural networks. For CNNs, the evaluation should include popular architectures such as ResNet and EfficientNet. For MLP-Mixers, the evaluation should include different variants of the architecture. The evaluation should also consider the computational cost and efficiency of the different architectures. This would provide a more comprehensive understanding of the method's performance across different architectures and its potential for practical applications. It is also important to analyze the trade-offs between performance and computational cost for different architectures.

Finally, the paper should provide a more detailed analysis of the self-supervised training process. It would be beneficial to investigate the impact of different masking ratios and patch sizes on the performance of the method. This would provide insights into the optimal settings for the self-supervised training process. Furthermore, the paper should analyze the convergence behavior of the method and the sensitivity of the results to different hyperparameters. This would help to ensure the reproducibility of the results and provide a better understanding of the method's behavior. The paper should also discuss the limitations of the proposed method and suggest directions for future research. This would help to guide future work in the field of self-supervised NAS and provide a more complete picture of the method's potential and limitations.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
