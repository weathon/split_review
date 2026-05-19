### Summary

This paper presents a quantization-aware training method to increase the accuracy of IMC systems affected by ADC quantization. The authors propose adjusting the weight and activation distributions to improve the SQNR of the ADC input and augment the training with different ADC bit precision. The proposed method is evaluated on several tasks, including image classification, object detection, and NLP.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well written and easy to follow.
- The experiments are extensive and thorough, including several tasks and comparisons in the literature.
- The results are convincing and significant, improving the accuracy of several models up to 3% with 8-bit ADC.

### Weaknesses

#### Some Related Works


#### comment

 - The main drawback of the proposed method is the training complexity. The last author states that the training is done in two stages, where the second stage takes around 20% of the total training time. However, quantization-aware training already requires longer training than post-training quantization methods. In the light of this, the proposed method increases even more the training complexity of QAT, which makes it less practical.
- The authors only evaluate the accuracy of the models but do not provide any evaluation of the effectiveness of the method in the context of IMC. Specifically, the paper lacks any analysis of how the proposed training method affects the actual IMC hardware performance, such as energy consumption, latency, or throughput. The method's impact on the ADC input distribution is only indirectly inferred from accuracy improvements, rather than directly measured or analyzed in the context of IMC hardware.
- The kurtosis loss is not new and was already proposed for weight quantization in "On the Quantization of Neural Networks for ReRAM Based In-Memory Computing". The authors should clarify how their approach differs from the existing work and why it is novel in the context of output quantization. The paper needs to provide a more detailed explanation of the differences in the kurtosis loss formulation and its application to output quantization, as opposed to weight quantization, to justify the novelty of their approach.
- The A-shift method is not clear to me. The authors say that they exploit the fact that quantizing the activations as an unsigned or signed number does not have much impact on the performance. However, in the equation, they choose to quantize the activation as an unsigned number. Then, they shift the quantized activation to treat it as a signed number. My question is, why did they choose to quantize the activation as an unsigned number in the first place? The explanation of the A-shift method lacks clarity regarding the initial choice of unsigned quantization and the subsequent shift to signed representation. The motivation behind this specific sequence of operations is not adequately justified.

### Suggestions

The paper should provide a more thorough analysis of the training time overhead introduced by the proposed method. While the authors mention a two-stage training process, they should quantify the exact additional computational cost compared to standard QAT and post-training quantization methods. This should include a breakdown of the time spent in each stage and a discussion of the practical implications of this increased training complexity. Furthermore, the authors should explore and discuss potential strategies to mitigate the training overhead, such as techniques for efficient kurtosis loss calculation or optimized training schedules. A detailed analysis of the computational resources required for training, including GPU memory usage and training time per epoch, would also be beneficial for assessing the practical feasibility of the proposed method.

To strengthen the paper's relevance to IMC, the authors should include an evaluation of the method's impact on IMC-specific metrics. This should go beyond simply reporting accuracy and include an analysis of the ADC input distribution, energy consumption, and latency. The authors could, for example, measure the SQNR of the ADC input with and without the proposed method and correlate this with the observed accuracy improvements. Furthermore, the authors should provide a more detailed discussion of how the proposed method affects the hardware implementation of IMC, including the impact on ADC design and the overall system performance. This could involve simulations or analytical models of IMC hardware to demonstrate the practical benefits of the proposed method in a real-world setting. The paper should also discuss the trade-offs between accuracy, energy consumption, and latency, providing a more comprehensive evaluation of the method's effectiveness in the context of IMC.

The authors should provide a more detailed explanation of the kurtosis loss and A-shift method, clarifying the differences from existing work and the rationale behind their design choices. Specifically, the authors should explain how their kurtosis loss differs from the one proposed in "On the Quantization of Neural Networks for ReRAM Based In-Memory Computing", and why applying it to output quantization is novel. The explanation of the A-shift method should clearly articulate the reasons for initially quantizing activations as unsigned numbers and the subsequent shift to a signed representation. The authors should also provide a more detailed analysis of the impact of these choices on the distribution of activations and the overall performance of the model. A more thorough discussion of the theoretical underpinnings of these methods and their practical implications would significantly improve the paper's clarity and contribution.

### Questions

- How does the proposed method affect the training time?
- How does the proposed method affect the ADC input distribution and the effectiveness of IMC systems?
- How is the proposed kurtosis loss different from the one proposed in "On the Quantization of Neural Networks for ReRAM Based In-Memory Computing"?
- Why did the authors choose to quantize the activation as an unsigned number in the A-shift method?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
