### Summary

This paper proposes a novel 4D Gaussian Splatting method for dynamic scene representation and rendering. The authors introduce a 4D Gaussian parameterization that can represent the spatio-temporal volume of dynamic scenes. They also extend the traditional 3D Gaussian Splatting technique to the 4D domain, incorporating a 4D rotation matrix to handle scene dynamics. Additionally, they introduce 4D Spherical Harmonics to model the time-varying appearance of the Gaussians. The method is evaluated on both synthetic and real-world datasets, demonstrating superior visual quality and efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed method is conceptually simple and straightforward to implement.
- The paper is well-written and easy to follow.
- The experimental results demonstrate the effectiveness of the proposed method in dynamic novel view synthesis and rendering.

### Weaknesses

#### Some Related Works


#### comment

 - The technical novelty of the proposed method is limited. The core idea of using 4D Gaussians for dynamic scene representation is not new, and the paper primarily extends existing techniques such as 3D Gaussian splatting and spherical harmonics to the 4D domain. While the application to dynamic scene rendering is interesting, the technical contribution is incremental rather than groundbreaking.
- The experimental evaluation is not comprehensive enough to fully demonstrate the effectiveness of the proposed method. The paper primarily compares against methods that do not explicitly model the temporal dimension, which may not be a fair comparison. A more thorough evaluation would include comparisons with other 4D scene representation methods, if available, or at least with methods that explicitly model temporal dynamics. The lack of comparison with relevant baselines makes it difficult to assess the true performance gains of the proposed method.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors claim real-time rendering capabilities, there is no quantitative analysis of the computational complexity, memory usage, or rendering speed compared to other methods. This makes it difficult to assess the practical applicability of the method, especially for large-scale scenes or real-time applications with strict latency requirements.

### Suggestions

The paper would benefit significantly from a more thorough evaluation against existing methods that also model temporal dynamics in dynamic scene rendering. Specifically, the authors should consider comparing their approach with techniques that use explicit temporal modeling, such as recurrent neural networks or temporal convolutional networks, to better understand the advantages and disadvantages of their 4D Gaussian approach. This would provide a more comprehensive understanding of the method's performance relative to the state-of-the-art in dynamic scene rendering. Furthermore, the authors should include a detailed analysis of the computational cost of their method, including the time complexity of the optimization process, the memory usage, and the rendering speed. This analysis should be compared against other methods to provide a clear understanding of the trade-offs between rendering quality and computational efficiency. The authors should also investigate the sensitivity of their method to various parameters, such as the number of Gaussians, the resolution of the representation, and the optimization parameters. This would help to understand the robustness and generalizability of the method.

To address the limited technical novelty, the authors could explore more innovative ways to represent and model the 4D scene. For example, they could investigate the use of adaptive Gaussian kernels that can adjust their shape and size based on the local scene structure, or they could explore the use of more sophisticated basis functions for representing the time-varying appearance of the Gaussians. Additionally, the authors could consider incorporating other scene priors, such as smoothness constraints or temporal coherence, to further improve the quality of the rendering. The paper should also include a more detailed discussion of the limitations of the proposed method, such as its ability to handle complex occlusions, fast motion, or large-scale scenes. This would provide a more balanced and realistic assessment of the method's capabilities.

Finally, the authors should provide a more detailed explanation of the 4D Spherical Harmonics (4DSH) and their role in modeling the time-varying appearance of the Gaussians. Specifically, they should clarify how the 4DSH are parameterized, how they are learned, and how they interact with the 4D Gaussians. A more detailed explanation of the mathematical formulation and the implementation details would help to better understand the technical aspects of the proposed method. The authors should also provide a more thorough analysis of the impact of the 4DSH on the rendering quality and the computational cost. This would help to understand the trade-offs between the accuracy and efficiency of the method.

### Questions

- How does the proposed method handle occlusions and disocclusions in dynamic scenes?
- How does the method perform in scenes with fast motion or complex scene dynamics?
- How does the method handle large-scale scenes or real-time applications with strict latency requirements?

### Rating

6

### Confidence

4

**********
