### Summary

This paper proposes to represent dynamic scenes with 4D Gaussians, which are 3D Gaussians extended to the time dimension. In detail, a 4D Gaussian is defined by its mean $\mu=(\mu_x, \mu_y, \mu_z, \mu_t)$ and covariance matrix $\Sigma = R S S^T R^T$, where $S$ is a scaling matrix inscribed by its diagonal elements $S=\text{diag}(s_x,s_y,s_z,s_t)$ and $R$ is a 4D rotation matrix constructed by two isotropic rotations $R = L(q_l) R(q_r)$. The conditional 3D Gaussian can be derived from the properties of the multivariate Gaussian. In addition, the paper proposes to exploit 4D spherindrical harmonics, which are constructed by merging 3D spherical harmonics with 1D basis functions, to model the time-evolving appearance of each Gaussian. The paper compares favorably against previous dynamic scene modeling methods on the Plenoptic Video dataset and D-NeRF dataset, achieving state-of-the-art rendering quality and real-time rendering speed.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

4 excellent

### Strengths

- The paper proposes a novel representation of dynamic scenes with 4D Gaussians, which can model both spatial and temporal dynamics of the scene. The 4D Gaussian is well-defined and can be derived from the properties of the multivariate Gaussian.
- The paper proposes to exploit 4D sphericular harmonics to model the time-evolving appearance of each Gaussian, which can capture the changing appearance of the scene over time.
- The paper is technically sound, well-written, and easy to follow.
- The paper compares favorably against previous dynamic scene modeling methods on the Plenoptic Video dataset and D-NeRF dataset, achieving state-of-the-art rendering quality and real-time rendering speed.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the limitations of the proposed method. It would be beneficial to discuss the potential failure cases of the method and the challenges in applying the method to real-world scenarios.
- The paper does not discuss the computational cost of the proposed method. It would be beneficial to discuss the computational complexity of the method and how it scales with the size of the scene and the number of Gaussians.

### Suggestions

The paper should include a more detailed discussion of the limitations of the proposed 4D Gaussian representation. Specifically, it would be beneficial to analyze scenarios where the method might struggle, such as scenes with very complex or discontinuous motion, or scenes with significant occlusions. For example, how does the method handle situations where objects move in and out of view rapidly, or when there are sudden changes in lighting or viewpoint? A discussion of these failure cases would provide a more complete understanding of the method's capabilities and limitations. Furthermore, it would be useful to explore the sensitivity of the method to the initialization of the Gaussian parameters, and how this might affect the final reconstruction quality. It is also important to consider the potential for artifacts or inaccuracies in the reconstructed scene, and how these might manifest in the rendered output. 

In addition to the limitations, the paper should provide a more thorough analysis of the computational cost of the proposed method. While the paper mentions real-time rendering speed, it lacks a detailed discussion of the computational complexity of the different stages of the pipeline, such as the Gaussian parameter estimation, the 4D spherindrical harmonics computation, and the rendering process. It would be beneficial to provide a breakdown of the time spent on each of these stages, and how the computational cost scales with the number of Gaussians, the size of the scene, and the resolution of the rendered images. For example, how does the computational cost of the 4D rotation matrix calculation scale with the number of Gaussians? What is the memory footprint of the Gaussian parameters and the harmonics coefficients? A detailed analysis of these factors would provide a better understanding of the practical applicability of the method, and how it compares to other dynamic scene modeling techniques.

Finally, the paper should also discuss the potential for future improvements and extensions of the proposed method. For example, could the method be extended to handle more complex scene dynamics, such as non-rigid deformations or topological changes? Could the method be combined with other techniques, such as neural rendering or implicit representations, to further improve the rendering quality or efficiency? It would also be useful to explore the potential for using the 4D Gaussian representation for other tasks, such as scene editing or animation. A discussion of these potential future directions would help to position the method within the broader context of dynamic scene modeling research.

### Questions

Please refer to the Weaknesses section.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
