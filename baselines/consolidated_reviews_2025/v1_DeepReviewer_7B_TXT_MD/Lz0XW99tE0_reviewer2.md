### Summary

This paper proposes a new method to generate crystal structures using Bayesian Flow Networks (BFN) with periodic boundary conditions and equivariance to rotations and reflections. The method is evaluated on several benchmark datasets and achieves state-of-the-art performance with significantly improved sampling efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method achieves state-of-the-art performance on several benchmark datasets.
3. The method is evaluated on several benchmark datasets, including Perov-5, Carbon-24, MP-20, and MPTS-52.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to discuss the potential failure cases and the scenarios where the method may not perform well.
2. The paper does not compare the proposed method with other state-of-the-art methods for crystal structure generation. It would be helpful to provide a more comprehensive comparison with other methods and to discuss the advantages and disadvantages of the proposed method.

### Suggestions

The authors should include a more thorough discussion of the limitations of their proposed method. Specifically, they should analyze scenarios where the model might fail to generate valid or realistic crystal structures. For instance, how does the model handle cases with very high or low coordination numbers, or materials with unusual bonding patterns? A detailed analysis of the model's performance on edge cases, such as materials with complex crystal structures or those with unusual bonding patterns, would be beneficial. Furthermore, the authors should discuss the sensitivity of the model to hyperparameter choices and provide guidance on how to select appropriate values for different types of crystal structures. This would help readers understand the robustness of the method and its applicability to a wide range of materials.

In addition to the limitations, the authors should provide a more comprehensive comparison with other state-of-the-art methods for crystal structure generation. This comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated structures. For example, the authors could compare the diversity of the generated structures, the accuracy of the predicted lattice parameters and fractional coordinates, and the physical plausibility of the generated materials. It would be helpful to include a discussion of the advantages and disadvantages of the proposed method compared to other approaches, highlighting the specific scenarios where the proposed method excels or falls short. This would provide a more complete picture of the contribution of the proposed method and its place in the existing literature. The authors should also discuss the computational cost of their method compared to other approaches, as this is an important factor for practical applications.

Finally, the authors should consider including a more detailed analysis of the training process. This could include a discussion of the convergence behavior of the model, the sensitivity of the results to different training parameters, and the computational resources required for training. This would help other researchers to reproduce the results and to apply the method to their own problems. The authors should also discuss the potential for extending the method to handle more complex crystal structures, such as those with defects or impurities. This would demonstrate the versatility of the method and its potential for future applications.

### Questions

1. How does the proposed method handle the challenges of generating realistic and stable crystal structures, such as avoiding the formation of unrealistic unit cells or violating physical constraints?
2. How does the proposed method compare to other state-of-the-art methods for crystal structure generation in terms of both accuracy and efficiency?

### Rating

6

### Confidence

2

**********
