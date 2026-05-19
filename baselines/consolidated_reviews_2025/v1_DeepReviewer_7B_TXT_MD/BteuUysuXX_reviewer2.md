### Summary

This paper proposes a method to induce high energy-latency cost for VLMs. The authors propose three loss functions to encourage the model to generate longer sequences, and they optimize the perturbation of the input image to achieve this goal. The proposed method is evaluated on four VLMs.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of crafting an image to increase the inference cost of VLMs is interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation is unclear. The authors aim to induce high energy-latency cost for VLMs. However, the proposed method is based on crafting adversarial examples, which can degrade the performance of VLMs on other tasks. This raises a fundamental question: if the goal is to increase the cost of VLMs, why not simply modify the inference engine instead of compromising their performance on other tasks? The paper does not adequately address why optimizing for adversarial robustness, which inherently involves degrading performance on clean inputs, is a suitable approach for increasing inference cost, especially when the goal is to make VLMs more expensive to use rather than to make them more robust in a security sense.

2. The paper lacks a clear definition of "high energy-latency cost." While the authors mention that energy consumption and latency time are positively correlated, they do not provide a precise mathematical relationship or a clear justification for why this correlation holds. The paper should either provide a theoretical argument or empirical evidence to support this claim. Furthermore, the paper does not discuss the potential non-linearities that might exist between energy consumption and latency, which could invalidate the simple linear relationship assumed.

3. The proposed method is not novel. The three loss functions are not new. The first loss function is similar to the one proposed in [1], which aims to make the model generate longer sequences by penalizing the probability of the end-of-sequence token. The second loss function is a standard KL divergence loss, which is commonly used to encourage diversity in the generated sequences. The third loss function, which aims to increase the rank of the hidden states, is also not novel and has been explored in other contexts. The paper does not clearly articulate the novelty of combining these existing loss functions for the specific task of crafting adversarial examples for VLMs.

4. The evaluation is insufficient. The authors only evaluate their method on four VLMs and two datasets. The paper should include more VLMs, especially those with different architectures and training data, to demonstrate the generalizability of the proposed method. Additionally, the paper should include more metrics to evaluate the performance of VLMs, such as the quality of the generated captions and the diversity of the generated sequences. The current evaluation is too limited to draw any strong conclusions about the effectiveness of the proposed method.

5. The paper lacks a discussion of the limitations of the proposed method. For example, the paper does not discuss the computational cost of crafting the adversarial examples, which could be a significant barrier to practical deployment. The paper also does not discuss the potential for the proposed method to be used for malicious purposes, such as to create fake news or to manipulate the behavior of VLMs.

### Suggestions

The paper needs to clarify the motivation for using adversarial examples to increase the inference cost of VLMs. The authors should explain why they chose to degrade the performance of VLMs on clean inputs, rather than simply modifying the inference engine to increase the cost. A more detailed discussion of the potential use cases for this approach is needed. For example, the authors could discuss scenarios where it is desirable to make VLMs more expensive to use, such as in a pay-per-use model. However, they should also acknowledge the potential downsides of this approach, such as the risk of misuse. The paper should also provide a more rigorous justification for the claim that energy consumption and latency time are positively correlated. This could involve a theoretical analysis or a more extensive empirical study that considers different types of VLMs and different input data. The authors should also discuss the potential non-linearities that might exist between energy consumption and latency, and how these non-linearities might affect the proposed method. Without a clear definition of 'high energy-latency cost', it is difficult to assess the effectiveness of the proposed method.

To address the lack of novelty, the authors should clearly articulate the specific contributions of their work. They should explain how their combination of loss functions is different from existing approaches and why this combination is particularly effective for crafting adversarial examples for VLMs. The authors should also provide a more detailed analysis of the individual contributions of each loss function. For example, they could conduct ablation studies to evaluate the impact of each loss function on the overall performance of the proposed method. This would help to clarify the novelty of their approach and to identify the key factors that contribute to its effectiveness. Furthermore, the authors should provide a more detailed explanation of the mathematical formulation of each loss function, including the specific parameters and hyperparameters used in their experiments. This would allow other researchers to reproduce their results and to build upon their work. The paper should also discuss the limitations of the proposed method, such as the computational cost of crafting the adversarial examples and the potential for the proposed method to be used for malicious purposes. The authors should also discuss the ethical implications of their work and how they have addressed these concerns.

Finally, the evaluation of the proposed method needs to be significantly expanded. The authors should include more VLMs, especially those with different architectures and training data, to demonstrate the generalizability of the proposed method. They should also include more metrics to evaluate the performance of VLMs, such as the quality of the generated captions and the diversity of the generated sequences. The current evaluation is too limited to draw any strong conclusions about the effectiveness of the proposed method. The authors should also provide a more detailed analysis of the results, including a comparison of the performance of the proposed method with other baseline methods. The paper should also include a discussion of the limitations of the proposed method, such as the computational cost of crafting the adversarial examples and the potential for the proposed method to be used for malicious purposes.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
