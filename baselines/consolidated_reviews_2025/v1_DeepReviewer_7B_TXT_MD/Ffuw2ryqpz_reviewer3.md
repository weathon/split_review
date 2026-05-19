### Summary

This paper proposes a new framework, Real3D, for training large reconstruction models (LRMs) using single-view images. The framework introduces a self-training strategy that leverages both synthetic and real-world data to improve model performance. It also incorporates two unsupervised losses: a cycle-consistency rendering loss and a semantic loss based on CLIP, which help guide the model without relying on ground-truth 3D data. Additionally, the authors develop an automatic data curation method to select high-quality single-view images from in-the-wild datasets, enhancing the model's robustness and generalization capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to training LRMs using single-view images, addressing a significant gap in the field. The introduction of self-training with both synthetic and real-world data is innovative and demonstrates a practical solution for leveraging readily available single-view data.

2. The paper is well-structured and clearly written, making it easy to follow the proposed methodology and understand the contributions. The authors provide sufficient detail on the implementation and experimental setup, allowing for reproducibility.

3. The proposed method achieves state-of-the-art performance on multiple datasets, demonstrating its effectiveness and potential impact in the field of 3D reconstruction.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. It would be beneficial to include a comparison of training times and resource requirements with existing methods, especially given the complexity of the self-training framework and the use of CLIP. Specifically, the paper lacks details on the GPU memory usage during training, the number of iterations required for convergence, and the inference time for generating novel views. This information is crucial for assessing the practical applicability of the method, particularly in resource-constrained environments.

2. While the paper demonstrates strong performance on in-distribution datasets, it does not thoroughly explore the model's robustness to out-of-distribution data or variations in input conditions, such as lighting and viewpoint changes. The evaluation primarily focuses on datasets with similar characteristics to the training data, which limits the understanding of the model's generalization capabilities. A more comprehensive evaluation should include datasets with significant domain shifts and varying environmental conditions to assess the model's resilience.

3. The paper does not discuss the limitations of the proposed method, such as potential biases in the training data or scenarios where the model might fail to produce accurate reconstructions. For instance, the paper does not address how the model performs on objects with complex geometries or textures, or how it handles occlusions. A thorough discussion of these limitations is essential for a balanced assessment of the method's capabilities and potential areas for improvement.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the training and inference times, including the time required for each stage of the self-training framework. This should include the time for rendering novel views, the time for the cycle-consistency and semantic losses, and the overall training time. Furthermore, the authors should report the GPU memory usage during training, the number of iterations required for convergence, and the inference time for generating novel views. This information should be compared with existing methods to provide a clear understanding of the computational overhead of the proposed approach. It would also be beneficial to explore techniques for optimizing the computational efficiency of the method, such as using more efficient rendering algorithms or model architectures.

To improve the evaluation of the model's robustness, the authors should conduct experiments on datasets that exhibit significant domain shifts and variations in input conditions. This could include datasets with different lighting conditions, viewpoints, and object categories. The evaluation should also include a quantitative analysis of the model's performance under these challenging conditions, using appropriate metrics such as PSNR, SSIM, and LPIPS. Furthermore, the authors should analyze the model's performance on objects with complex geometries and textures, and discuss how it handles occlusions. This analysis should include both quantitative and qualitative results, providing a comprehensive understanding of the model's strengths and weaknesses.

Finally, the authors should provide a thorough discussion of the limitations of the proposed method, including potential biases in the training data and scenarios where the model might fail to produce accurate reconstructions. This discussion should include an analysis of the model's performance on objects with complex geometries or textures, and how it handles occlusions. The authors should also discuss the potential impact of the training data's domain shift on the model's generalization capabilities. This discussion should be supported by experimental results and analysis, providing a balanced assessment of the method's capabilities and potential areas for improvement.

### Questions

1. How does the proposed method handle objects with complex geometries or textures that are not well represented in the training data?

2. What are the limitations of the proposed method in terms of handling occlusions or partial views in the input images?

3. How does the model perform on objects with varying levels of detail or complexity?

### Rating

6

### Confidence

3

**********
