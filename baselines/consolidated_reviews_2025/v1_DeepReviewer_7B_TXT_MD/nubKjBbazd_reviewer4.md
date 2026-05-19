### Summary

This paper proposes a new adversarial attack method, Adversarial Perturbation Dropout (APD), that can achieve significant transferability of adversarial examples. The APD method adopts the dropout mechanism on a set of adversarial images to break the synergy of the perturbations across different attention regions, which can maintain the attack effect for the target model even part of the perturbations are not in its attention regions.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The motivation is clear and the writing is easy to follow.
2. The experiments are sufficient.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is very similar to the input transformation method [1]. The core idea of both methods is to reduce the transferability of adversarial examples by transforming the input space. Specifically, the APD method uses a dropout mechanism on perturbations, which is conceptually similar to applying transformations that alter the input distribution. The paper does not sufficiently differentiate the proposed method from existing input transformation techniques, particularly in how the perturbation dropout mechanism fundamentally differs from other input space manipulations to reduce transferability.
2. The experiments are insufficient. The authors should compare the proposed method with more transfer attacks, such as MI-FGSM, DIM, TIM, SIM, and AA-TI-DIM. The current experiments lack a comprehensive comparison with a wide range of state-of-the-art transfer attacks, making it difficult to assess the true effectiveness and novelty of the proposed method. The absence of comparisons with methods like MI-FGSM, DIM, TIM, SIM, and AA-TI-DIM, which are well-established in the field, weakens the experimental validation.
3. The authors should compare the proposed method with more input transformation methods, such as DIM, TIM, SIM, and AA-TI-DIM. The paper only compares the proposed method with a limited set of input transformation methods, failing to demonstrate its superiority over a broader range of existing techniques. A more thorough comparison with methods like DIM, TIM, SIM, and AA-TI-DIM is necessary to establish the proposed method's contribution to the field.

### Suggestions

The paper needs to more clearly articulate the novelty of the proposed method in relation to existing input transformation techniques. While the dropout mechanism is presented as a key contribution, the paper does not provide a detailed analysis of how this mechanism fundamentally differs from other input space manipulations used in transfer attacks. A more rigorous comparison, including a theoretical analysis of the differences in the perturbation space, is needed to justify the proposed method's unique contribution. The authors should also explore the limitations of the proposed method and discuss scenarios where it might not be effective. Furthermore, the paper should include a more detailed explanation of the specific parameters used in the dropout mechanism and how these parameters affect the transferability of the adversarial examples. This would provide a more comprehensive understanding of the method's behavior and allow for better reproducibility.

To strengthen the experimental validation, the authors should include a more comprehensive set of comparisons with state-of-the-art transfer attacks. This should include not only methods like MI-FGSM, DIM, TIM, SIM, and AA-TI-DIM, but also other relevant techniques that have demonstrated strong performance in the field. The comparison should not only focus on the overall attack success rate but also analyze the transferability of the generated adversarial examples under different conditions. For example, the authors could investigate the impact of different perturbation sizes and the number of adversarial images used in the dropout mechanism on the transferability of the generated examples. This would provide a more nuanced understanding of the method's performance and allow for a more thorough evaluation of its effectiveness. Additionally, the authors should provide a more detailed analysis of the computational cost of the proposed method compared to other transfer attacks.

Finally, the paper should include a more comprehensive comparison with other input transformation methods. This comparison should not only focus on the attack success rate but also analyze the impact of different input transformations on the transferability of the adversarial examples. The authors should also discuss the limitations of the proposed method and compare it with other input transformation techniques in terms of their ability to reduce the transferability of adversarial examples. This would provide a more complete picture of the proposed method's contribution to the field and allow for a more informed assessment of its strengths and weaknesses. The authors should also consider exploring the use of adaptive input transformations that are tailored to the specific target model being attacked.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
