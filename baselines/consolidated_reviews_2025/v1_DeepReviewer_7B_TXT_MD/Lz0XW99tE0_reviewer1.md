### Summary

This paper proposes a novel method for generating crystal structures, which is an important task in material discovery. The authors extend Bayesian Flow Networks (BFN) to handle crystal structures by incorporating periodic boundary conditions and equivariance to rotations and reflections. This is achieved by using a von Mises distribution for fractional coordinates and a Gaussian distribution for lattice parameters. The method achieves state-of-the-art performance on several benchmark datasets, with significantly improved sampling efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- Crystal structure generation is an important task in material discovery, and the proposed method achieves state-of-the-art performance on several benchmark datasets.
- The authors extend BFN to handle crystal structures by incorporating periodic boundary conditions and equivariance to rotations and reflections, which are important properties of crystal structures.
- The proposed method achieves significantly improved sampling efficiency compared to previous methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is very technical and may be difficult for readers without a background in crystallography or Bayesian methods to understand. The authors should provide more intuitive explanations of the key concepts and methods.
- The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the potential failure cases and the scenarios where the method may not perform well.
- The paper does not compare the proposed method with other state-of-the-art methods for crystal structure generation. It would be helpful to provide a more comprehensive comparison with other methods and to discuss the advantages and disadvantages of the proposed method.

### Suggestions

The authors should consider adding a dedicated section or subsection that provides a more accessible explanation of the core concepts, particularly for readers less familiar with crystallographic data and Bayesian methods. This section could include illustrative examples, simplified mathematical explanations, and visual aids to help clarify the periodic boundary conditions, equivariance, and the von Mises and Gaussian distributions used in the method. For instance, a step-by-step walkthrough of how the method handles a simple crystal structure, highlighting the role of each component, would be beneficial. Furthermore, the authors should explicitly state the assumptions made by the model and discuss how these assumptions might affect the generated crystal structures. This would help readers understand the scope and limitations of the proposed approach.

To address the lack of detailed analysis of limitations, the authors should include a section that specifically discusses potential failure cases. This could involve analyzing scenarios where the model might struggle, such as generating unstable or unrealistic crystal structures, or failing to converge for certain types of materials. The authors should also discuss the sensitivity of the model to hyperparameter choices and provide guidance on how to select appropriate values for different types of crystal structures. For example, they could investigate how the model performs on materials with varying unit cell sizes or chemical compositions. A discussion of the computational cost of the method, especially in comparison to other approaches, would also be valuable. This would help readers understand the trade-offs between accuracy and computational efficiency.

Finally, the authors should provide a more comprehensive comparison with other state-of-the-art methods for crystal structure generation. This comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated structures. For example, the authors could compare the diversity of the generated structures, the accuracy of the predicted lattice parameters and fractional coordinates, and the physical plausibility of the generated materials. It would be helpful to include a discussion of the advantages and disadvantages of the proposed method compared to other approaches, highlighting the specific scenarios where the proposed method excels or falls short. This would provide a more complete picture of the contribution of the proposed method and its place in the existing literature.

### Questions

- How does the proposed method handle the challenges of generating realistic and stable crystal structures, such as avoiding the formation of unrealistic unit cells or violating physical constraints?
- How does the proposed method compare to other state-of-the-art methods for crystal structure generation in terms of both accuracy and efficiency?

### Rating

6

### Confidence

2

**********
