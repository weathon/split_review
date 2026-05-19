### Summary

This paper introduces a novel approach for controlling the motion of multiple entities in video generation using 3D trajectories. The proposed method, 3DTrajMaster, leverages a plug-and-play object injector to fuse entity descriptions with their corresponding 3D trajectories, enabling precise manipulation of object motion in 3D space. To address the lack of suitable training data, the authors construct a 360-Motion Dataset using Unreal Engine, incorporating advanced rendering techniques and GPT-generated trajectories. The method employs a domain adaptor during training and an annealed sampling strategy during inference to maintain video quality. Experimental results demonstrate that 3DTrajMaster achieves state-of-the-art performance in both accuracy and generalization for multi-entity 3D motion control.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach for controlling multi-entity 3D motion in video generation, which is a significant advancement over existing methods that primarily rely on 2D control signals.
2. The construction of the 360-Motion Dataset addresses the limitations of existing datasets by providing high-quality 3D motion data for a variety of entities, which is crucial for training and evaluating the proposed method.
3. The use of a gated self-attention mechanism for motion fusion is a technically sound approach that effectively integrates entity descriptions with their corresponding 3D trajectories.
4. The introduction of a domain adaptor and annealed sampling strategy demonstrates a thoughtful approach to mitigating video quality degradation and enhancing the overall performance of the model.
5. The paper provides extensive experimental results, including both quantitative and qualitative evaluations, which convincingly demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, particularly concerning the scalability of the approach to handle a large number of entities. Specifically, the paper lacks a breakdown of the time and memory requirements for the different components of the model, such as the object injector, the gated self-attention mechanism, and the diffusion model. This makes it difficult to assess the practical applicability of the method for complex scenes with many interacting entities. Furthermore, the paper does not discuss the potential bottlenecks in the pipeline that could limit its scalability.
2. While the paper introduces a novel approach for 3D motion control, it does not thoroughly compare its method with existing 3D-aware video generation techniques, particularly in terms of motion realism and diversity. The paper should include a more detailed comparison with methods that explicitly model 3D motion, such as those using neural radiance fields or 3D Gaussian splatting, to better contextualize the advantages and limitations of the proposed approach. A quantitative comparison of motion realism using metrics like the Fréchet Inception Distance (FID) or other relevant metrics would be beneficial.
3. The paper could benefit from a more in-depth discussion of the limitations of the proposed method, particularly regarding the types of motions that can be effectively controlled and the potential challenges in handling complex interactions between multiple entities. For example, the paper does not address how the method would handle scenarios where entities collide or interact physically, or how it would deal with occlusions. A discussion of these limitations would provide a more balanced view of the method's capabilities.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and memory requirements for each component of their model, including the object injector, the gated self-attention mechanism, and the diffusion model. This analysis should consider the impact of the number of entities on the overall computational cost. Specifically, the authors should report the inference time and memory usage for different numbers of entities, and identify the bottlenecks in the pipeline that limit scalability. Furthermore, the authors should discuss potential strategies for optimizing the model to handle a larger number of entities, such as using more efficient attention mechanisms or model parallelism. This would provide a more comprehensive understanding of the practical limitations of the proposed method and guide future research in this area.

To better contextualize the proposed method within the broader landscape of 3D-aware video generation, the authors should include a more thorough comparison with existing techniques that explicitly model 3D motion. This comparison should not only focus on the qualitative aspects of the generated videos but also include quantitative metrics for evaluating motion realism and diversity. For example, the authors could compare their method with techniques that use neural radiance fields or 3D Gaussian splatting, using metrics such as the Fréchet Inception Distance (FID) or other relevant metrics. This would provide a more objective assessment of the strengths and weaknesses of the proposed approach. Additionally, the authors should discuss the specific advantages and disadvantages of their method compared to these alternative approaches, highlighting the unique contributions of their work.

Finally, the authors should provide a more in-depth discussion of the limitations of their method, particularly regarding the types of motions that can be effectively controlled and the potential challenges in handling complex interactions between multiple entities. This discussion should include specific examples of scenarios where the method might struggle, such as when entities collide or interact physically, or when occlusions occur. The authors should also discuss potential strategies for addressing these limitations in future work, such as incorporating physics-based constraints or developing more sophisticated motion fusion techniques. This would provide a more balanced and realistic view of the method's capabilities and guide future research in this area.

### Questions

1. How does the proposed method handle scenarios where the input 3D trajectories are not perfectly aligned with the entity descriptions, and what mechanisms are in place to ensure robustness to such misalignments?
2. Can the authors provide more details on the performance of the method in terms of motion smoothness and temporal consistency, particularly in complex scenes with multiple interacting entities?
3. How does the proposed method compare to other state-of-the-art video generation techniques in terms of computational efficiency and resource requirements, especially when scaling to a large number of entities?

### Rating

6

### Confidence

4

**********
