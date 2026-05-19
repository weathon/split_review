### Summary

This paper presents a pruning framework for SNNs. The framework combines unstructured weight pruning with unstructured neuron pruning to maximize the utilization of the sparsity of neuromorphic computing.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method achieves impressive energy efficiency gains.
3. The experiments are solid and convincing.

### Weaknesses

#### Some Related Works

[1] Are we doing the right thing (and doing it right) in SNNs?

#### comment

1. The authors should provide more details about the training process, such as the number of time steps, the type of encoder used, and the specific training algorithm. The lack of these details makes it difficult to reproduce the results and assess the method's sensitivity to different training configurations. For example, the number of time steps directly impacts the temporal resolution of the SNN, and the encoder type influences how input data is converted into spike trains, both of which are crucial for performance.
2. The experiments are mainly conducted on CIFAR datasets, which may not be sufficient to demonstrate the effectiveness of the proposed method. It would be better to evaluate the method on more complex datasets, such as ImageNet. The CIFAR datasets are relatively small and may not fully capture the challenges of real-world applications. Testing on a larger, more complex dataset like ImageNet would provide a more robust evaluation of the method's scalability and generalization capabilities.
3. The authors should provide a more detailed comparison with other state-of-the-art pruning methods for SNNs, including both quantitative and qualitative results. A more comprehensive comparison should include metrics such as parameter count, computational cost, and memory footprint, in addition to accuracy. Furthermore, a qualitative analysis of the pruned network's structure could provide insights into the method's pruning behavior.
4. It would be better if the authors could discuss the limitations of the proposed method and suggest future research directions. This discussion should include potential challenges in deploying the method on real neuromorphic hardware, as well as the method's sensitivity to different network architectures and datasets. Identifying these limitations would help guide future research and improve the practical applicability of the method.
5. The authors should discuss the potential impact of their work on the SNN research community and the broader field of neuromorphic computing. This discussion should address how the proposed method advances the state-of-the-art in SNN pruning and how it could contribute to the development of more energy-efficient and high-performance neuromorphic systems. It would also be beneficial to discuss the potential societal implications of this research.
6. The authors should also discuss the potential ethical concerns related to their work, such as the potential for bias in the pruned networks or the environmental impact of training large SNN models. It is important to consider how the pruning process might inadvertently introduce or amplify biases present in the training data, and to address the energy consumption associated with training and deploying these models.
7. The authors should also compare their method with other SNN training algorithms, such as TET [1]. A direct comparison with other training methods would help to understand the relative strengths and weaknesses of the proposed pruning framework in the context of different training paradigms.

### Suggestions

To address the lack of detail regarding the training process, the authors should include a comprehensive description of all relevant parameters and procedures. This should include the specific number of time steps used during both training and inference, the exact type of encoder (e.g., a fixed or learned encoder, and its specific implementation), and the detailed training algorithm, including the optimization method, learning rate schedule, and loss function. Furthermore, the authors should specify the initialization method for network weights and the thresholding strategy for the neurons. Providing these details will significantly enhance the reproducibility of the results and allow other researchers to build upon this work. It would also be beneficial to include an ablation study to analyze the sensitivity of the method to different training parameters, such as the number of time steps and the learning rate, which would provide a deeper understanding of the method's behavior.

To strengthen the experimental evaluation, the authors should conduct experiments on more complex datasets, such as ImageNet, to demonstrate the scalability and generalization capabilities of the proposed method. In addition to reporting accuracy, the authors should provide a detailed comparison with other state-of-the-art pruning methods for SNNs, including both quantitative and qualitative results. This comparison should include metrics such as the number of parameters, computational cost (e.g., floating-point operations per second, FLOPS), memory footprint, and energy consumption. Furthermore, a qualitative analysis of the pruned network's structure, such as the distribution of remaining weights and neurons, could provide valuable insights into the method's pruning behavior. The authors should also consider comparing their method with other SNN training algorithms, such as TET [1], to understand the relative strengths and weaknesses of the proposed pruning framework in the context of different training paradigms. This would provide a more comprehensive evaluation of the method's effectiveness.

Finally, the authors should discuss the limitations of the proposed method and suggest future research directions. This discussion should include potential challenges in deploying the method on real neuromorphic hardware, such as the compatibility of the pruning strategy with specific hardware architectures and the impact of hardware constraints on the method's performance. The authors should also address the method's sensitivity to different network architectures and datasets, and identify potential areas for improvement. Furthermore, the authors should discuss the potential impact of their work on the SNN research community and the broader field of neuromorphic computing, including the potential societal implications and ethical concerns related to their work. This discussion should address how the proposed method advances the state-of-the-art in SNN pruning and how it could contribute to the development of more energy-efficient and high-performance neuromorphic systems. It would also be beneficial to discuss the potential environmental impact of training large SNN models and how the proposed pruning method can help mitigate this impact.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
