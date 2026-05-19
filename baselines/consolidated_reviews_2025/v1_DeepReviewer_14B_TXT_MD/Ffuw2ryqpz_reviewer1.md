### Summary

This paper proposes Real3D, a framework for training single-view large reconstruction models (LRMs) using real-world single-view images. The contributions of Real3D lie in three aspects: 1) It introduces a self-training framework that leverages both synthetic and real-world single-view images for training LRMs. 2) It proposes two unsupervised losses, cycle consistency rendering loss and semantic loss, to supervise LRMs at the pixel and semantic levels. 3) It develops an automatic data curation approach to collect high-quality examples from real-world images.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written, with clear explanations of concepts and methodologies. The authors provide sufficient background information and clearly state the problem they are addressing, making it easy for readers to follow the paper's logic.
2. The authors conduct extensive experiments to validate the effectiveness of Real3D. They evaluate the model on diverse datasets, including both real and synthetic data, and compare it with previous methods. The results demonstrate that Real3D outperforms prior work in various evaluation settings.
3. The paper provides detailed implementation details, including network architecture, training procedure, and evaluation metrics. The authors also release the code and model, which enhances the reproducibility of the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could provide more details about the data curation approach. How does the method handle noisy or low-quality images? Are there any specific criteria or thresholds used to filter out undesirable data points? Specifically, the paper lacks a detailed explanation of the instance segmentation process used to extract objects from real-world images. It is unclear how the segmentation model is trained, what its performance is, and how potential segmentation errors might affect the overall training of the LRM. Furthermore, the paper does not discuss the potential biases introduced by the selection of instances, and how these biases might impact the generalization capability of the model.
2. The paper could provide more insights into the choice of the specific unsupervised losses used for training LRMs. Are there any other potential unsupervised losses that could be explored in the future? The paper should discuss the limitations of the chosen cycle consistency and semantic losses. For example, the cycle consistency loss might not be sufficient to enforce geometric accuracy, and the semantic loss might not capture fine-grained details. The paper should also explore other potential unsupervised losses, such as adversarial losses or perceptual losses, and discuss why they were not chosen.
3. The paper could provide more analysis of the scalability of the proposed method. How does the performance of Real3D change as the amount of training data increases? Are there any limitations in terms of computational resources or training time? The paper lacks a detailed analysis of the computational cost of the proposed method. It should provide information about the training time, memory requirements, and the number of parameters of the model. Furthermore, the paper should discuss the potential challenges of scaling the method to larger datasets and more complex models.

### Suggestions

The paper should provide a more detailed explanation of the instance segmentation process used for data curation. This should include details about the segmentation model used, its training procedure, and its performance on the real-world images. The authors should also discuss how they handle segmentation errors and potential biases introduced by the selection of instances. For example, they could explore using a robust segmentation model trained on a diverse dataset, and they could implement a data augmentation strategy to mitigate biases. Furthermore, the paper should include a quantitative analysis of the quality of the segmented instances and how this quality affects the performance of the LRM. This would provide a more comprehensive understanding of the data curation process and its impact on the overall results.

The paper should also provide a more thorough discussion of the chosen unsupervised losses and their limitations. The authors should explore other potential unsupervised losses, such as adversarial losses or perceptual losses, and discuss why they were not chosen. They should also analyze the limitations of the cycle consistency and semantic losses, and discuss how these limitations might affect the performance of the model. For example, they could explore using a more robust geometric loss to enforce accuracy, and they could explore using a more fine-grained semantic loss to capture more details. Furthermore, the paper should include an ablation study to evaluate the contribution of each loss function to the overall performance of the model. This would provide a more comprehensive understanding of the effectiveness of the chosen losses and their potential limitations.

Finally, the paper should include a more detailed analysis of the scalability of the proposed method. This should include information about the training time, memory requirements, and the number of parameters of the model. The authors should also discuss the potential challenges of scaling the method to larger datasets and more complex models. For example, they could explore using more efficient training techniques, such as distributed training or mixed-precision training. Furthermore, the paper should include an analysis of the performance of the model as the amount of training data increases. This would provide a more comprehensive understanding of the scalability of the proposed method and its potential limitations.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
