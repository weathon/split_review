### Summary

This paper proposes a semantic-aware implicit representation for image inpainting. The proposed method consists of two modules: a semantic implicit representation (SIR) for enhancing semantic embedding and an appearance implicit representation (AIR) for reconstructing the color of an arbitrary coordinate. The proposed method outperforms state-of-the-art approaches on the CelebAHQ and ADE20K datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is technically sound and the presentation is clear.
2. The proposed method outperforms state-of-the-art approaches on the CelebAHQ and ADE20K datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. The SIR and AIR modules are both based on the existing implicit neural function.
2. The proposed method is only evaluated on the image inpainting task. It would be better to evaluate the proposed method on other downstream tasks.

### Suggestions

The paper's primary weakness lies in the limited novelty of the proposed approach. While the combination of Semantic Implicit Representation (SIR) and Appearance Implicit Representation (AIR) modules is presented as a novel contribution, both modules fundamentally rely on existing implicit neural function architectures. The SIR module, while incorporating a modified CLIP model, still operates within the framework of implicit neural representations, and the AIR module directly applies an implicit function for color reconstruction. To strengthen the novelty claim, the authors should explore more significant modifications to the underlying implicit function architecture or demonstrate a novel way of integrating the SIR and AIR modules that goes beyond a simple concatenation or sequential application. For example, they could investigate incorporating attention mechanisms or cross-modal fusion techniques that allow for a more dynamic and adaptive interaction between the semantic and appearance information. Furthermore, a more thorough analysis of the limitations of existing implicit neural functions in the context of semantic-aware inpainting would be beneficial to justify the need for a new approach.

Another significant limitation is the narrow scope of the experimental evaluation. The proposed method is only evaluated on the image inpainting task, which, while important, does not fully demonstrate the potential of the proposed approach. To address this, the authors should evaluate the method on other downstream tasks that benefit from semantic-aware representations, such as image editing, style transfer, or object manipulation. For instance, the authors could explore how the learned semantic embeddings from the SIR module can be used to guide image editing operations, such as object insertion or attribute modification. Similarly, the AIR module could be used to generate novel appearances for objects based on their semantic context. Evaluating the method on these tasks would not only demonstrate the versatility of the proposed approach but also provide a more comprehensive assessment of its strengths and weaknesses. Furthermore, the authors should consider evaluating the method on datasets with more complex semantic structures and diverse object categories to better understand its limitations and potential for real-world applications.

Finally, the paper would benefit from a more detailed analysis of the computational cost and efficiency of the proposed method. While the authors mention that the method is efficient, a more thorough analysis of the computational complexity of the SIR and AIR modules, as well as the training and inference time, would be valuable. This analysis should include a comparison with existing state-of-the-art methods to demonstrate the trade-offs between performance and efficiency. Additionally, the authors should provide more details on the implementation of the method, including the specific hyperparameters used for training and the hardware used for experiments. This would allow other researchers to reproduce the results and build upon the proposed approach. Furthermore, a discussion on the scalability of the method to larger images and more complex scenes would be beneficial to understand its practical applicability.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
