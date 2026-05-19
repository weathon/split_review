### Summary

This paper proposes a Large Reconstruction Model (LRM) that predicts the 3D model of an object from a single input image within just 5 seconds. The model is trained on massive multi-view data containing around 1 million objects, including both synthetic renderings from Objaverse and real captures from MVImgNet. The model adopts a highly scalable transformer-based architecture with 500 million learnable parameters to directly predict a neural radiance field (NeRF) from the input image. The paper demonstrates that the proposed method can reconstruct high-fidelity 3D shapes from a wide range of images captured in the real world, as well as images created by generative models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting. It is the first Large Reconstruction Model that predicts the 3D model of an object from a single input image within just 5 seconds.
3. The paper provides extensive qualitative results, demonstrating the effectiveness of the proposed method on various real-world images and images created by generative models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks quantitative comparisons with other state-of-the-art methods. It would be beneficial to compare the proposed method with existing approaches on standard benchmarks to demonstrate its effectiveness.
2. The paper does not provide any ablation studies to analyze the impact of different components of the proposed method on its performance. It would be helpful to conduct ablation studies to understand the contribution of each component to the overall performance of the method.
3. The paper does not discuss the limitations of the proposed method. It would be beneficial to discuss the potential failure cases and limitations of the method to provide a more comprehensive understanding of its capabilities.

### Suggestions

The lack of quantitative comparisons is a significant weakness. While qualitative results are useful for visual inspection, they are insufficient to establish the superiority of the proposed method over existing techniques. The paper should include a thorough quantitative evaluation on standard 3D reconstruction benchmarks, such as ShapeNet or other relevant datasets. This evaluation should include metrics like Chamfer distance, Earth Mover's Distance (EMD), or other relevant metrics that are commonly used in the field. Furthermore, the comparison should not only be against methods that use similar input modalities but also against state-of-the-art methods that achieve high-quality 3D reconstruction, even if they use different input types (e.g., multi-view images). This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses relative to the current state of the art. The absence of such comparisons makes it difficult to assess the true contribution of the work.

The absence of ablation studies is another critical issue. The paper proposes a complex architecture with multiple components, including a transformer-based encoder, a triplane representation, and a NeRF decoder. It is essential to understand the contribution of each of these components to the overall performance. For example, the paper should investigate the impact of different transformer architectures, the choice of triplane representation, and the specific design of the NeRF decoder. Ablation studies should systematically remove or replace each component and evaluate the resulting performance. This would not only provide insights into the importance of each component but also help identify potential areas for improvement. For instance, the impact of the number of layers in the transformer, the size of the triplane feature maps, or the specific activation functions used in the NeRF decoder should be analyzed. Without these studies, it is difficult to determine which parts of the architecture are most critical for achieving high-quality reconstruction.

Finally, the paper needs a more thorough discussion of its limitations. While the paper demonstrates impressive results on a variety of images, it is important to acknowledge the potential failure cases and limitations of the method. For example, the paper should discuss how the method performs on objects with complex geometries, objects with significant occlusions, or images with poor lighting conditions. It should also address the limitations of the triplane representation, such as its potential to lose fine details or its inability to represent certain types of surfaces accurately. Furthermore, the paper should discuss the computational cost of the method, including the training time and the inference time. This would provide a more balanced and realistic assessment of the proposed method's capabilities and limitations. A clear understanding of these limitations is crucial for guiding future research and for potential users of the method.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
