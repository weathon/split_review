### Summary

This paper presents three methods for motion generation. The first one is DoubleTake, which is able to generate long motion sequences by iteratively combining short motions. The second one is ComMDM, which is able to generate two-person motion by training a communication module on the difference between two MDM predictions. The third one is DiffusionBlending, which is able to blend several fine-tuned models to enable fine-grained control over the body with any cross combinations of joints to be controlled.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper presents three methods for motion generation, including long motion generation, two-person motion generation, and fine-grained control of motion. The proposed methods are able to generate long motion sequences, generate two-person motion, and enable fine-grained control over the body with any cross combinations of joints to be controlled.
3. The paper presents extensive experiments to show the effectiveness of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison of the proposed methods with existing methods in terms of computational cost. It is important to understand the computational overhead of the proposed methods compared to existing approaches, especially when dealing with long motion sequences or complex two-person interactions. Without this information, it is difficult to assess the practical applicability of the proposed methods.
2. The paper does not provide a detailed analysis of the limitations of the proposed methods. It is crucial to understand the scenarios where the proposed methods might fail or underperform. For example, are there specific types of motion sequences or interactions that are particularly challenging for the proposed methods? A thorough discussion of these limitations would provide a more balanced view of the proposed methods.
3. The paper does not discuss the potential ethical implications of the proposed methods. Given that the methods are used for motion generation, there might be ethical concerns related to the generation of potentially harmful or inappropriate motions. A discussion of these ethical considerations is necessary to ensure responsible development and deployment of the proposed methods.

### Suggestions

The paper would benefit significantly from a more detailed analysis of the computational costs associated with the proposed methods. Specifically, the authors should provide a breakdown of the time and memory requirements for each step of the DoubleTake, ComMDM, and DiffusionBlending processes. This analysis should include a comparison with existing methods, such as those based on autoregressive models or other diffusion-based approaches. For instance, the authors could report the inference time per frame, the memory footprint of the models, and the computational cost of the communication module in ComMDM. Furthermore, it would be helpful to understand how these costs scale with the length of the motion sequence and the number of people involved. This information is crucial for researchers and practitioners to evaluate the feasibility of using these methods in real-world applications, such as virtual reality or animation software. The authors should also consider providing a theoretical analysis of the computational complexity of their methods, which would further strengthen the paper's claims.

In addition to computational cost, a more thorough discussion of the limitations of the proposed methods is needed. The authors should explore the scenarios where the methods might struggle, such as generating complex interactions between multiple people or handling long-range dependencies in motion sequences. For example, it would be valuable to understand how the DoubleTake method performs when generating very long motion sequences with intricate transitions between different segments. Similarly, the authors should investigate the limitations of ComMDM in handling more than two people or in generating motions that require a high degree of coordination. It would also be useful to analyze the sensitivity of the methods to different hyperparameters and to identify the parameter settings that lead to the best performance. A detailed analysis of these limitations would provide a more complete picture of the capabilities and shortcomings of the proposed methods, and it would help guide future research in this area.

Finally, the paper should address the potential ethical implications of the proposed methods. Given that the methods can generate human motion, there are concerns about the potential for misuse, such as creating unrealistic or harmful motions. The authors should discuss these ethical considerations and propose guidelines for responsible development and deployment of their methods. For example, they could discuss the potential for using these methods in virtual reality or animation software, and they could suggest ways to mitigate the risks of generating harmful or inappropriate motions. This discussion should also include an analysis of the potential for bias in the training data and how this bias might affect the generated motions. By addressing these ethical concerns, the authors can demonstrate a responsible approach to research and development in this field.

### Questions

1. How does the computational cost of the proposed methods compare to existing methods?
2. What are the limitations of the proposed methods?
3. What are the potential ethical implications of the proposed methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
