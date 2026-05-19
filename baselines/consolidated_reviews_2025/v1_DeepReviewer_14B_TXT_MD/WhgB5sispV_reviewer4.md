### Summary

This paper proposes a novel approach to representing dynamic scenes using 4D Gaussian primitives. The key innovation is the introduction of a 4D Gaussian representation that integrates both spatial and temporal dimensions, enabling coherent modeling of dynamic scenes. The method also introduces 4D spherindrical harmonics to model the time evolution of appearance in dynamic scenes. The authors demonstrate the effectiveness of their approach through extensive experiments on various benchmarks, including monocular and multi-view scenarios, showing superior visual quality and efficiency compared to previous methods. The proposed method achieves real-time rendering of high-resolution, photorealistic novel views in complex dynamic scenes.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

4 excellent

### Strengths

- The paper introduces a novel and effective approach to representing dynamic scenes using 4D Gaussian primitives, which is a significant advancement in the field.
- The proposed method achieves state-of-the-art rendering quality and efficiency, outperforming existing methods on various benchmarks.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its advantages.
- The authors provide extensive experimental results and ablation studies to demonstrate the effectiveness of their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the limitations of the proposed method in detail. It would be beneficial to explore potential failure cases or scenarios where the method might not perform well.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational complexity of the method with existing approaches.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed 4D Gaussian representation. While the method demonstrates impressive results on the presented datasets, it is crucial to understand its boundaries. For instance, how does the method handle scenes with significant occlusions or rapid changes in viewpoint? Are there specific types of motion or scene complexity that pose challenges to the 4D Gaussian primitive representation? A detailed analysis of these failure cases, perhaps with illustrative examples, would provide a more complete picture of the method's capabilities and limitations. Furthermore, it would be beneficial to explore the sensitivity of the method to the choice of hyperparameters, such as the number of Gaussians or the bandwidth parameter, and how these choices affect the rendering quality and computational cost. This would provide valuable insights for practitioners looking to apply the method in different scenarios.

Regarding the computational cost, a more detailed analysis is needed to understand the practical implications of the proposed method. While the paper mentions real-time rendering, it lacks a quantitative comparison of the computational complexity with existing approaches. Specifically, it would be helpful to provide a breakdown of the computational cost associated with different stages of the pipeline, such as Gaussian parameter estimation, splatting, and rendering. This analysis should include a comparison of the time and memory requirements of the proposed method with other state-of-the-art techniques, such as NeRF-based methods or other explicit scene representations. Furthermore, it would be beneficial to discuss the scalability of the method with respect to the number of Gaussians and the resolution of the rendered images. This would help to assess the practical applicability of the method for large-scale or high-resolution dynamic scenes.

Finally, the paper could benefit from a more in-depth discussion of the 4D spherindrical harmonics used to model the time evolution of appearance. While the paper introduces this concept, it would be helpful to provide more details on the choice of the harmonic basis and its impact on the representation capacity. For example, how does the number of harmonics affect the accuracy of the appearance modeling? Are there specific types of appearance changes that are difficult to capture with the proposed harmonics? A more detailed analysis of these aspects would provide a better understanding of the strengths and limitations of the proposed appearance modeling technique. Additionally, it would be useful to compare the performance of the 4D spherindrical harmonics with other methods for modeling time-varying appearance, such as neural networks or other parametric models.

### Questions

- How does the proposed method handle scenes with significant occlusions or rapid changes in viewpoint?
- What are the potential failure cases or scenarios where the proposed method might not perform well?
- How does the computational cost of the proposed method compare to existing approaches in terms of training time, rendering time, and memory usage?
- How does the proposed method handle changes in lighting conditions over time?

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
