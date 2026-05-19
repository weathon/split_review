### Summary

The paper proposes a large reconstruction model (LRM) that predicts a triplane representation of a scene from a single image. The model is trained on a large amount of data, including synthetic data from Objaverse and real-world data from MVImgNet. The model is capable of reconstructing 3D objects from single images in real-time.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper proposes a large reconstruction model (LRM) that predicts a triplane representation of a scene from a single image. The model is trained on a large amount of data, including synthetic data from Objaverse and real-world data from MVImgNet. The model is capable of reconstructing 3D objects from single images in real-time.
3. The paper provides a comprehensive evaluation of the proposed method, including quantitative and qualitative results.

### Weaknesses

#### Some Related Works

[1] LERF: Large Reconstruction Environment Fields
[2] LERF++: Large Reconstruction Environment Fields with Improved Geometry
[3] LERF++: Large Reconstruction Environment Fields with Improved Geometry and Appearance
[4] LERF++: Large Reconstruction Environment Fields with Improved Geometry, Appearance and Generalization

#### comment

1. The paper does not provide a detailed comparison with existing methods, such as LERF [1], LERF++ [2], LERF++ [3], and LERF++ [4]. Specifically, the paper lacks a quantitative comparison of reconstruction quality, such as PSNR, SSIM, and LPIPS, against these methods on a common dataset. A qualitative comparison, showing side-by-side visualizations of the reconstructed meshes, would also be beneficial to highlight the strengths and weaknesses of the proposed approach relative to existing techniques. The absence of this comparison makes it difficult to assess the novelty and effectiveness of the proposed method.
2. The paper does not discuss the limitations of the proposed method. For example, the paper does not discuss the types of scenes or objects that the model struggles to reconstruct. It would be beneficial to include a discussion of the failure cases of the model, such as scenes with complex geometry, occlusions, or reflective surfaces. This would provide a more complete understanding of the model's capabilities and limitations.
3. The paper does not discuss the computational cost of the proposed method. The paper should provide details on the training time, inference time, and memory requirements of the model. This information is crucial for assessing the practical applicability of the method. It would also be useful to compare the computational cost of the proposed method with existing methods.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing state-of-the-art methods for single-image 3D reconstruction. Specifically, the authors should include a quantitative comparison of their method against LERF [1], LERF++ [2], LERF++ [3], and LERF++ [4] using standard metrics such as PSNR, SSIM, and LPIPS on a common dataset. This comparison should not only focus on the final rendered images but also on the accuracy of the reconstructed 3D meshes. For example, the authors could report the Chamfer distance or other mesh similarity metrics to quantify the geometric accuracy of the reconstructions. Furthermore, a qualitative comparison, showing side-by-side visualizations of the reconstructed meshes from different methods, would provide a more intuitive understanding of the strengths and weaknesses of the proposed approach. This would help to highlight the specific scenarios where the proposed method excels or falls short compared to existing techniques. The authors should also consider including a discussion of the computational cost of each method, including training time, inference time, and memory requirements, to provide a more complete picture of the trade-offs involved.

In addition to the quantitative and qualitative comparisons, the paper should also include a discussion of the limitations of the proposed method. This discussion should include an analysis of the types of scenes or objects that the model struggles to reconstruct. For example, the authors should discuss how the model performs on scenes with complex geometry, occlusions, or reflective surfaces. It would be beneficial to include specific examples of failure cases, such as images with severe occlusions or reflective surfaces, and to discuss the reasons for these failures. This would provide a more complete understanding of the model's capabilities and limitations and would help to guide future research in this area. The authors should also discuss the potential impact of the training data on the model's performance. For example, if the training data is biased towards certain types of scenes or objects, the model may not generalize well to other types of data. A discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

Finally, the paper should include a more detailed discussion of the training process. This should include details on the optimization algorithm used, the learning rate schedule, and the batch size. It would also be useful to discuss the specific data augmentation techniques used during training and how they contribute to the model's performance. The authors should also provide details on the hardware used for training and inference, including the type of GPU and the amount of memory available. This information is crucial for other researchers who want to reproduce the results of the paper. Furthermore, the authors should discuss the sensitivity of the model to different hyperparameters and provide guidance on how to choose the optimal hyperparameters for different datasets. This would make the method more accessible and easier to use for other researchers.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
