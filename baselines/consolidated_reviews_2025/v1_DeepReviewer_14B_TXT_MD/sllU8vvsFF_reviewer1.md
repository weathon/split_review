### Summary

This paper proposes a large-scale 3D reconstruction model (LRM) that predicts a 3D object from a single image. The image is first encoded using a ViT, and the resulting features are used to generate a triplane-NeRF representation through a transformer-based image-to-triplane decoder. The model is trained on massive multi-view data containing around 1 million objects, including both synthetic and real captures. The experiments show that the proposed method can reconstruct high-quality 3D shapes from various real-world images and images created by generative models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The use of a large transformer-based architecture allows the model to learn a generic 3D prior for reconstructing an object from a single image, which is a challenging task.
- The proposed method is efficient in both training and inference, taking only five seconds to render a high-fidelity 3D shape.

### Weaknesses

#### Some Related Works

[1] Instantmesh: Efficient 3d mesh generation from a single image with sparse-view large reconstruction models

#### comment

 - The reviewer's primary concern lies in the technical contributions of this paper, which appear to be limited. The proposed LRM framework bears a strong resemblance to InstantMesh[1], as both employ a DINO encoder and a transformer-based decoder. While the authors have emphasized that LRM is a foundational model that can be scaled up, the reviewer does not find any significant improvements in the overall pipeline compared to InstantMesh.

- The reviewer is also concerned about the lack of quantitative comparisons in this paper. Although the authors provide extensive qualitative results, they do not include any quantitative comparisons with other state-of-the-art methods, such as InstantNGP, Ego3D, and InstantMesh. This makes it difficult to assess the performance of the proposed method objectively.

- The reviewer notes that the paper lacks a detailed description of the camera parameter normalization process. While the authors mention that they normalize the camera poses to facilitate image-to-triplane modeling, they do not provide sufficient details on how this normalization is performed. Specifically, the transformation from arbitrary camera poses to normalized poses should be described using explicit equations, including the translation and rotation components. Furthermore, it is unclear whether the normalized camera parameters are used during inference, and if so, how the original camera parameters are accounted for.

- The reviewer observes that the 3D reconstruction results exhibit over-smoothing, which is a common limitation of NeRF-based methods. While the authors acknowledge this limitation, they do not provide any specific details on the number of input views used for training. The reviewer suggests that the authors should clarify the training setup, including the number of views used and the sampling strategy. Additionally, the authors should discuss potential methods to address the over-smoothing issue, such as incorporating a total variation loss or using a higher-resolution triplane representation.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing state-of-the-art methods, particularly InstantMesh. While the authors position LRM as a foundational model, the technical differences beyond scaling up the architecture need to be more clearly articulated. A detailed analysis of the architectural differences, such as the specific transformer decoder layers and their impact on performance, would strengthen the paper. Furthermore, the authors should provide a more rigorous justification for their design choices, explaining why their specific combination of DINO encoder and transformer-based decoder is superior to other possible architectures. This could involve ablation studies that analyze the impact of different components on the final reconstruction quality. The authors should also clarify the specific training data used by InstantMesh and other baselines to ensure a fair comparison, given that data scale can significantly impact performance.

To address the lack of quantitative comparisons, the authors should include standard metrics such as Chamfer distance, Earth Mover's Distance (EMD), and IoU on standard object datasets. While the authors argue that these benchmarks are category-specific and their model is category-agnostic, evaluating the model on a common benchmark would provide a valuable point of comparison with existing methods. The authors could also consider using a zero-shot evaluation approach, where the model is tested on a dataset it has not seen during training, to further demonstrate its generalization capabilities. Furthermore, the authors should provide a more detailed analysis of the model's performance on different types of objects, such as those with complex geometries or textures. This would help to identify the strengths and weaknesses of the proposed method and guide future research.

Finally, the paper needs a more detailed explanation of the camera parameter normalization process. The authors should provide explicit equations for the transformation from arbitrary camera poses to normalized poses, including the translation and rotation components. It is also crucial to clarify whether the normalized camera parameters are used during inference and, if so, how the original camera parameters are accounted for. The authors should also discuss the impact of camera parameter normalization on the model's performance and provide ablation studies to demonstrate the effectiveness of their approach. Additionally, the authors should provide more details on the number of input views used for training and discuss potential methods to address the over-smoothing issue, such as incorporating a total variation loss or using a higher-resolution triplane representation. The authors should also consider comparing their method with other NeRF-based methods that use sparse input views to provide a more comprehensive evaluation.

### Questions

- The reviewer is concerned about the lack of quantitative comparisons in this paper. Although the authors provide extensive qualitative results, they do not include any quantitative comparisons with other state-of-the-art methods, such as InstantNGP, Ego3D, and InstantMesh. This makes it difficult to assess the performance of the proposed method objectively.

- The reviewer notes that the paper lacks a detailed description of the camera parameter normalization process. While the authors mention that they normalize the camera poses to facilitate image-to-triplane modeling, they do not provide sufficient details on how this normalization is performed. Specifically, the transformation from arbitrary camera poses to normalized poses should be described using explicit equations, including the translation and rotation components. Furthermore, it is unclear whether the normalized camera parameters are used during inference, and if so, how the original camera parameters are accounted for.

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
