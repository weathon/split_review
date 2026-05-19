### Summary

This paper proposes a new approach to object completion, named MaskComp. The core of MaskComp is an iterative mask denoising (IMD) process, which alternates between image generation and segmentation stages to progressively refine the object mask. The generation stage uses a modified ControlNet to generate complete object images conditioned on the visible portion and an object mask. The segmentation stage uses an off-the-shelf object segmentation model to segment the object mask within the generated images and aggregate these segmented masks to obtain a superior mask for the next iteration. The paper demonstrates the effectiveness of MaskComp on two datasets, AHP and DYCE, by comparing it with several state-of-the-art methods and conducting ablation studies.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to object completion by iteratively refining the object mask through alternating generation and segmentation stages. This approach is both interesting and effective.

2. The paper provides a comprehensive evaluation of MaskComp on two datasets, AHP and DYCE, and compares it with several state-of-the-art methods. The results show that MaskComp outperforms other methods in terms of image quality and object completeness.

3. The paper conducts thorough ablation studies to analyze the impact of different components and design choices of MaskComp, such as the number of IMD steps, the number of sampled images, and the choice of segmentation model. These studies provide valuable insights into the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of MaskComp. While the paper mentions that MaskComp is computationally expensive due to the inclusion of multiple diffusion processes in each IMD step, it does not provide a quantitative comparison of the running time with other methods. This makes it difficult to assess the practicality of MaskComp in real-world applications. Specifically, the paper lacks a breakdown of the time spent in each stage of the IMD process (generation, segmentation, and mask aggregation), which would be crucial for understanding the bottlenecks and potential areas for optimization. Furthermore, the paper does not discuss the memory requirements of the method, which is also an important factor for practical deployment.

2. The paper does not explore the potential of using MaskComp for other image editing tasks beyond object completion. While the paper mentions that object completion can enable more complicated editing tasks such as object layer switching, it does not provide any concrete examples or experiments to demonstrate this potential. It would be interesting to see how MaskComp can be applied to other tasks such as image inpainting, image composition, or style transfer. For example, could the iterative mask refinement be used to fill in missing regions in an image, or to seamlessly integrate objects from different images? The paper should provide a more thorough discussion of the potential applications and limitations of the proposed method.

3. The paper does not discuss the limitations of MaskComp in detail. For example, the paper does not analyze the performance of MaskComp on objects with complex shapes or textures, or on images with multiple objects or cluttered backgrounds. It would be helpful to understand the scenarios where MaskComp may not perform well and the potential solutions to address these limitations. Specifically, the paper should investigate how the quality of the initial mask affects the final completion result, and whether the method is robust to noisy or inaccurate initial masks. Additionally, the paper should explore the sensitivity of the method to the choice of hyperparameters, such as the number of IMD steps and the number of sampled images.

### Suggestions

The paper should include a detailed analysis of the computational cost of MaskComp, including a breakdown of the time spent in each stage of the IMD process (generation, segmentation, and mask aggregation) and a comparison with other methods. This analysis should also include a discussion of the memory requirements of the method. Furthermore, the paper should explore the potential of using MaskComp for other image editing tasks beyond object completion, such as image inpainting, image composition, or style transfer. This could involve adapting the method to different types of masks or incorporating additional constraints to guide the generation process. For example, the paper could explore how the iterative mask refinement can be used to fill in missing regions in an image, or to seamlessly integrate objects from different images. The paper should also discuss the limitations of MaskComp in detail, including an analysis of the performance of MaskComp on objects with complex shapes or textures, or on images with multiple objects or cluttered backgrounds. This analysis should investigate how the quality of the initial mask affects the final completion result, and whether the method is robust to noisy or inaccurate initial masks. Additionally, the paper should explore the sensitivity of the method to the choice of hyperparameters, such as the number of IMD steps and the number of sampled images. The paper should also discuss the potential for using different segmentation models and their impact on the overall performance of MaskComp.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the time spent in each stage of the IMD process. This should include the time for image generation, segmentation, and mask aggregation. A comparison of the running time with other methods, such as ControlNet and Stable Diffusion, should be included, with a clear indication of the hardware used for the experiments. Furthermore, the authors should discuss the memory requirements of their method, including the memory footprint of the models and the intermediate data structures. This analysis should be presented in a table or a figure, making it easy to understand the computational cost of MaskComp. The authors should also discuss potential optimizations to reduce the computational cost, such as reducing the number of sampling steps or using more efficient segmentation models.

To explore the potential of MaskComp for other image editing tasks, the authors should provide concrete examples and experiments. For instance, they could demonstrate how MaskComp can be used for image inpainting by providing a masked image and showing the completed result. Similarly, they could show how MaskComp can be used for image composition by integrating objects from different images. These experiments should be accompanied by a discussion of the challenges and limitations of applying MaskComp to these tasks. The authors should also discuss the potential for adapting the method to different types of masks or incorporating additional constraints to guide the generation process. For example, they could explore the use of edge masks or semantic masks to control the shape and texture of the completed object. The authors should also discuss the limitations of MaskComp in detail, including an analysis of the performance of MaskComp on objects with complex shapes or textures, or on images with multiple objects or cluttered backgrounds. This analysis should investigate how the quality of the initial mask affects the final completion result, and whether the method is robust to noisy or inaccurate initial masks. Additionally, the paper should explore the sensitivity of the method to the choice of hyperparameters, such as the number of IMD steps and the number of sampled images. The paper should also discuss the potential for using different segmentation models and their impact on the overall performance of MaskComp.

### Questions

1. Can MaskComp be used for other image editing tasks besides object completion? If so, what are the potential applications and challenges?

2. What is the computational cost of MaskComp compared to other methods? How can the computational cost be reduced without sacrificing performance?

3. How does MaskComp perform on objects with complex shapes or textures, or on images with multiple objects or cluttered backgrounds? What are the limitations of MaskComp in these scenarios?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
