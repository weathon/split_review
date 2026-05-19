### Summary

The paper presents a semantic-aware implicit representation (SAIR) method for image inpainting. The proposed SAIR method consists of two modules, a semantic implicit representation (SIR) module and an appearance implicit representation (AIR) module. The SIR module is designed to infer semantic information from the given image, and the AIR module is designed to infer colors from the given image and the semantic information inferred by the SIR module. The authors show that the proposed method outperforms existing methods in image inpainting tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a detailed explanation of the proposed method, including the SIR and AIR modules, and the loss functions used for training.
3. The authors conduct extensive experiments on two datasets, CelebAHQ and ADE20K, and compare the proposed method with several state-of-the-art methods.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is similar to the existing implicit neural function-based inpainting methods, such as LIIF, in that both methods use implicit neural functions to represent images. The main difference is that the proposed method introduces a semantic-aware module, which is a simple addition to the existing implicit neural function-based inpainting methods.
2. The authors do not provide a clear motivation for why the proposed method is effective. The authors claim that the proposed method can handle severely degraded images, but they do not provide any evidence to support this claim. The authors should provide more analysis on why the proposed method is effective and how it differs from existing methods.
3. The authors do not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a comparison of the computational cost of the proposed method with existing methods.

### Suggestions

The paper would benefit from a more thorough justification of the proposed method's novelty and effectiveness. While the introduction of a semantic-aware module is a key aspect, the authors need to articulate more clearly why this specific module is crucial for handling severely degraded images, which is a central claim of the paper. A more detailed analysis of the limitations of existing implicit neural function-based methods in such scenarios would be beneficial. For instance, the authors could discuss how the lack of semantic information in traditional methods leads to artifacts or poor reconstruction quality in severely degraded images. Furthermore, the authors should provide a more in-depth explanation of how the proposed semantic module addresses these limitations, perhaps by analyzing the specific types of errors that the semantic module corrects. This could involve visualizing the semantic information inferred by the SIR module and demonstrating how it influences the color reconstruction in the AIR module. 

To strengthen the paper's contribution, the authors should also provide a more rigorous comparison with existing methods, including a detailed analysis of the computational cost. This comparison should not only focus on the final performance metrics but also on the convergence speed and the number of parameters required for each method. It would be helpful to see a breakdown of the computational cost associated with each module (SIR and AIR) to understand where the proposed method is more efficient or less efficient than existing approaches. Additionally, the authors should consider including ablation studies to evaluate the impact of each component of the proposed method, such as the specific architecture of the SIR and AIR modules, and the choice of loss functions. This would help to isolate the contributions of each component and provide a more comprehensive understanding of the method's performance. 

Finally, the authors should consider expanding the experimental evaluation to include a wider range of degradation types and severities. While the paper mentions handling severely degraded images, it would be valuable to see how the proposed method performs under different types of noise, blur, and other forms of image corruption. This would provide a more comprehensive assessment of the method's robustness and generalizability. Furthermore, the authors should consider evaluating the method on more challenging datasets that include a wider variety of scenes and objects. This would help to demonstrate the method's ability to handle real-world scenarios where images may be subject to various types of degradation. The authors should also provide a more detailed discussion of the limitations of the proposed method and potential avenues for future research.

### Questions

1. How does the proposed method handle images with complex semantic structures?
2. How does the proposed method handle images with different types of degradation?
3. What is the computational cost of the proposed method compared to existing methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
