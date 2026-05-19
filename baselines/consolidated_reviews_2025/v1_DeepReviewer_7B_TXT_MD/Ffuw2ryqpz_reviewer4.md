### Summary

This paper introduces Real3D, a novel framework for training large reconstruction models (LRMs) using single-view images. The key innovation lies in leveraging real-world single-view images alongside synthetic multi-view data for training. The framework employs two unsupervised losses: cycle-consistency rendering loss and semantic rendering loss. The cycle-consistency loss ensures consistency between rendered novel views and the original input, while the semantic loss aligns the semantic content of the rendered views with the input. Additionally, the paper presents an automatic data curation method to select high-quality single-view images from in-the-wild datasets, enhancing the model's robustness and generalization. The framework demonstrates superior performance across various datasets, including real and synthetic data, and outperforms previous methods in both in-domain and out-of-domain settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the proposed methodology and understand the contributions.
2. The proposed framework addresses a significant gap in the field by enabling the training of LRMs with single-view images, which are more readily available than multi-view data.
3. The self-training framework is innovative, leveraging both synthetic and real-world data to improve model performance and generalization.
4. The cycle-consistency and semantic losses are well-designed and contribute to the model's ability to generate high-quality 3D reconstructions without ground-truth 3D supervision.
5. The automatic data curation method effectively selects high-quality single-view images, enhancing the model's robustness and generalization capabilities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. It would be beneficial to include a comparison of training times and resource requirements with existing methods, especially given the complexity of the self-training framework and the use of CLIP. Specifically, the paper lacks a breakdown of the time spent on each stage of the training process, such as the cycle-consistency loss calculation, semantic loss calculation, and the actual training of the LRM. This makes it difficult to assess the practical feasibility of the method, particularly for large-scale datasets or real-time applications.
2. While the paper demonstrates strong performance on in-distribution datasets, it does not thoroughly explore the model's robustness to out-of-distribution data or variations in input conditions, such as lighting and viewpoint changes. The evaluation primarily focuses on datasets with similar characteristics to the training data, which limits the understanding of the model's generalization capabilities. For example, the paper does not evaluate the model's performance on datasets with significant domain shifts, such as different object categories or varying levels of occlusion. Furthermore, the paper does not analyze the model's sensitivity to changes in lighting conditions or viewpoint angles, which are common challenges in real-world scenarios.
3. The paper does not discuss the limitations of the proposed method, such as potential biases in the training data or scenarios where the model might fail to produce accurate reconstructions. For instance, the paper does not address how the model handles objects with complex geometries or textures, or how it performs on objects with varying levels of detail. Additionally, the paper does not discuss the potential impact of the training data's domain shift on the model's generalization capabilities. This lack of discussion makes it difficult to assess the practical applicability of the method in diverse scenarios.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the training time for each component of their framework, including the cycle-consistency loss calculation, semantic loss calculation, and the actual training of the LRM. This should include the time spent on each stage of the training process, as well as the memory requirements for each component. Furthermore, a comparison of the computational cost with existing methods, such as those that use multi-view data, would be beneficial. This would allow readers to better understand the trade-offs between performance and computational resources. The authors should also explore techniques to optimize the computational efficiency of their method, such as using more efficient rendering algorithms or model architectures. This would make the method more practical for large-scale datasets or real-time applications.

To improve the evaluation of the model's robustness, the authors should conduct experiments on datasets that exhibit significant domain shifts and variations in input conditions. This could include datasets with different object categories, varying levels of occlusion, and different lighting conditions. The evaluation should also include a quantitative analysis of the model's performance under these challenging conditions, using appropriate metrics such as PSNR, SSIM, and LPIPS. Furthermore, the authors should analyze the model's sensitivity to changes in lighting conditions and viewpoint angles, and discuss the limitations of the model in these scenarios. This would provide a more comprehensive understanding of the model's generalization capabilities and its practical applicability in real-world scenarios. The authors should also consider using techniques such as domain adaptation or adversarial training to improve the model's robustness to out-of-distribution data.

Finally, the authors should provide a more detailed discussion of the limitations of their proposed method, including potential biases in the training data and scenarios where the model might fail to produce accurate reconstructions. This discussion should include an analysis of the model's performance on objects with complex geometries or textures, and how it handles objects with varying levels of detail. The authors should also discuss the potential impact of the training data's domain shift on the model's generalization capabilities. This would provide a more balanced and realistic assessment of the method's capabilities and limitations. The authors should also consider using techniques such as data augmentation or regularization to mitigate potential biases in the training data.

### Questions

1. Could you provide more details on the computational cost of the proposed method, including training time and resource requirements, and compare it with existing methods?
2. How does the model perform on out-of-distribution data or under varying input conditions, such as lighting and viewpoint changes?
3. What are the limitations of the proposed method, and how might these be addressed in future work?

### Rating

8

### Confidence

3

**********
