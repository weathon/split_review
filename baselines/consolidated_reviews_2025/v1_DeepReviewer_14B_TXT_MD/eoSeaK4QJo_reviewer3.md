### Summary

This paper proposes a pruning framework that combines unstructured weight pruning with unstructured neuron pruning to maximize the utilization of the sparsity of neuromorphic computing, thereby enhancing energy efficiency. The sparse network pruned by the proposed method with only 0.63% remaining connections can achieve a remarkable 91 times increase in energy efficiency compared to the original dense network, requiring only 8.5M SOPs for inference, with merely 2.19% accuracy loss on the CIFAR-10 dataset.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-organized and easy to follow. 
2. The proposed method is novel and effective. 
3. The experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on the CIFAR10 dataset. The generalization of the proposed method needs to be further verified on more datasets. Specifically, the performance on datasets with higher dimensionality and more complex data distributions, such as ImageNet or COCO, remains unclear. The current evaluation does not sufficiently demonstrate the robustness of the method across diverse scenarios.
2. The authors should provide more details about the training process, such as the number of time steps, the type of encoder used, and the specific training algorithm. The lack of these details makes it difficult to reproduce the results and assess the method's sensitivity to different training configurations. For example, the number of time steps directly impacts the temporal resolution of the SNN, and the encoder type influences how input data is converted into spike trains, both of which are crucial for performance.
3. The authors should provide more details about the experimental setup, such as the hardware and software environment, to ensure the reproducibility of the results. This includes the specific type of CPU/GPU used, the version of the deep learning framework, and any specific libraries or dependencies. Without this information, it is challenging to verify the reported performance gains.
4. The authors should discuss the limitations of the proposed method and suggest future research directions. This discussion should include potential challenges in deploying the method on real neuromorphic hardware, as well as the method's sensitivity to different network architectures and datasets. Identifying these limitations would help guide future research and improve the practical applicability of the method.

### Suggestions

To address the limited evaluation, the authors should extend their experiments to include more complex datasets such as ImageNet or COCO. This would provide a more comprehensive assessment of the method's generalization capabilities and robustness. Furthermore, it would be beneficial to analyze the performance of the method under different levels of sparsity, providing a more detailed understanding of the trade-off between accuracy and energy efficiency. The authors should also consider evaluating the method on different types of SNN architectures, such as those with different neuron models or synaptic dynamics, to assess its adaptability.

To improve the reproducibility of the results, the authors should provide a detailed description of the training process, including the number of time steps, the type of encoder used (e.g., Poisson encoder, temporal coding), and the specific training algorithm (e.g., backpropagation through time, spike-time dependent plasticity). They should also specify the optimization parameters, such as the learning rate, batch size, and the number of epochs. Additionally, the authors should provide details about the hardware and software environment used for the experiments, including the specific type of CPU/GPU, the version of the deep learning framework, and any specific libraries or dependencies. This information is crucial for other researchers to replicate the results and build upon this work. The authors should also consider releasing their code to further enhance reproducibility.

Finally, the authors should include a thorough discussion of the limitations of the proposed method and suggest future research directions. This discussion should include potential challenges in deploying the method on real neuromorphic hardware, such as the compatibility of the pruning strategy with specific hardware architectures and the impact of hardware constraints on the method's performance. The authors should also address the method's sensitivity to different network architectures and datasets, and identify potential areas for improvement. Furthermore, the authors should discuss the potential ethical implications of their work, such as the environmental impact of training large SNN models and the potential for bias in the pruned networks. This discussion would provide a more complete and nuanced understanding of the method's strengths and weaknesses.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
