### Summary

This paper proposes three methods for motion generation, including long sequence generation, two-person generation, and fine-grained control. The authors leverage pretrained diffusion-based motion generation models to achieve these tasks. The first method, DoubleTake, tackles the challenge of long sequence generation by iteratively composing two generated motions in time, with the help of a handcrafted "handshake" to ensure temporal consistency. The second method, ComMDM, addresses the challenge of two-person generation by training a simple communication block on the difference between two pretrained motion diffusion models. The third method, DiffusionBlending, enables fine-grained control over the body by blending several fine-tuned models. The authors conduct extensive experiments on various datasets and tasks to demonstrate the effectiveness of their proposed methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed methods are novel and interesting.
- The paper conducts extensive experiments to demonstrate the effectiveness of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed analysis of the limitations of the proposed methods. For example, it would be helpful to discuss the scenarios where the proposed methods might fail or underperform. Specifically, the paper does not address the potential for error accumulation in the DoubleTake method, where small inconsistencies in the "handshake" could propagate and lead to noticeable artifacts in longer sequences. Furthermore, the paper does not explore the sensitivity of the ComMDM method to the choice of the communication block architecture or the training data used for the two-person motion generation task. The paper also lacks a discussion on the computational cost of the proposed methods, especially for long sequence generation.
- The paper does not discuss the potential ethical implications of the proposed methods. Given that the methods are used for motion generation, there might be ethical concerns related to the generation of potentially harmful or inappropriate motions. The paper should discuss the potential for misuse of the proposed methods and propose guidelines for responsible development and deployment. For example, the paper should discuss the potential for generating unrealistic or harmful motions and the measures that can be taken to mitigate these risks.

### Suggestions

The paper would benefit from a more thorough analysis of the limitations of the proposed methods. Specifically, the authors should investigate the error accumulation in the DoubleTake method. This could involve analyzing the impact of small inconsistencies in the "handshake" on the quality of the generated long sequences. For example, the authors could conduct experiments where the "handshake" is intentionally perturbed to observe the resulting artifacts. Additionally, the authors should explore the sensitivity of the ComMDM method to the choice of the communication block architecture and the training data. This could involve experimenting with different architectures for the communication block and different datasets for training the two-person motion generation task. The authors should also discuss the computational cost of the proposed methods, especially for long sequence generation. This could involve providing a detailed analysis of the time and memory requirements of each method and comparing them to existing approaches. Furthermore, the authors should discuss the potential for error accumulation in the DoubleTake method, where small inconsistencies in the "handshake" could propagate and lead to noticeable artifacts in longer sequences. This could involve analyzing the impact of small inconsistencies in the "handshake" on the quality of the generated long sequences. 

To address the ethical concerns, the authors should discuss the potential for misuse of the proposed methods and propose guidelines for responsible development and deployment. This could involve discussing the potential for generating unrealistic or harmful motions and the measures that can be taken to mitigate these risks. For example, the authors could discuss the use of techniques such as adversarial training to prevent the generation of harmful motions. The authors should also discuss the potential for generating motions that are not realistic or that violate physical laws. This could involve analyzing the generated motions to ensure that they are physically plausible. The authors should also discuss the potential for generating motions that are not safe or that could cause harm to humans or other animals. This could involve analyzing the generated motions to ensure that they are safe and do not cause harm. 

Finally, the authors should provide more details on the implementation of the proposed methods. This could involve providing more details on the architecture of the communication block, the training procedure for the two-person motion generation task, and the fine-tuning procedure for the DiffusionBlending method. The authors should also provide more details on the datasets used for training and evaluation. This would allow other researchers to reproduce the results and build upon the proposed methods. The authors should also consider releasing their code and models to the public, which would further enhance the reproducibility and impact of their work.

### Questions

- How does the proposed method handle the case where the input text prompts are not well-defined or ambiguous?
- How does the proposed method handle the case where the input text prompts are not well-defined or ambiguous?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
