# Neural Network Adaptive Quantization based on Bayesian Deep Learning

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
We propose a novel approach to solve the adaptive quantization problem in neural networks based on epistemic uncertainty analysis. The quantized model is treated as a Bayesian neural network with stochastic weights, where the mean values are employed to estimate the corresponding weights. Standard deviations serve as an indicator of uncertainty and the number of corresponding bits — i.e., a larger number of bits indicate lower uncertainty, and vice versa. We perform an extensive analysis of several algorithms within a novel framework for different convolutional and fully connected neural networks based on open datasets demonstrating the main advantages of the proposed approach. In particular, we introduce two novel algorithms for mixed-precision quantization. Quantile Inform utilizes uncertainty to allocate bit-width across layers, while Random Bits employs stochastic gradient-based optimization techniques to maximize the full likelihood of quantization. Using our approach, we reduce the average bit-width of the VGG-16 model to 3.05 with the 90.5% accuracy on the CIFAR-10 dataset compared to 91.9% for the non-quantized model. For the LeNet model trained on the MNIST dataset, we reduce the average bit-width to 3.16 and achieve 99.0% accuracy, almost equal to 99.2% for the non-quantized model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel approach to solve the adaptive quantization problem in neural networks based on Bayesian neural networks and uncertainty analysis. Two new algorithms are presented: QuantileInform, which utilizes uncertainty to allocate bit-width across layers based on informativeness, and RandomBits, which employs stochastic gradient-based optimization techniques to maximize the full likelihood of quantization. The paper demonstrates the effectiveness of these approaches through experiments on MNIST and CIFAR-10 datasets, showing that the methods can achieve comparable or better accuracy than existing quantization methods while using fewer bits. For instance, they reduce the average bit-width of the VGG16 model to 3.05 with 90.5% accuracy on CIFAR-10 compared to 91.9% for the non-quantized model.

### Strengths
The paper demonstrates several notable strengths in its approach to neural network quantization. A key strength is the novel utilization of Bayesian neural networks to determine optimal bit-width allocation, departing from traditional fixed-width quantization methods. The authors present a mathematically rigorous foundation for their approach, with clear derivations and well-justified methodological choices. Their innovative interpretation of bits as random discrete variables enables the application of gradient optimization techniques, representing a creative solution to the optimization challenge. The presentation is particularly strong, with clear mathematical notation and well-designed figures that effectively communicate both methodology and results. The experimental results show promising performance on the MNIST and CIFAR-10 datasets, demonstrating the practical utility of their approach in reducing model size while maintaining accuracy. The paper's thorough treatment of the theoretical underpinnings, combined with practical implementation considerations, provides a comprehensive view of the proposed solution. Additionally, the authors' explicit acknowledgment of limitations and potential areas for future work demonstrates scientific rigor and transparency in their research approach.

### Weaknesses
Despite its strengths, the paper has several areas that could be improved. A significant limitation is the restricted scope of experimental validation, with testing limited to MNIST and CIFAR-10 datasets. More extensive evaluation on larger, more complex datasets, such as ImageNet or a similarly challenging benchmark, would be necessary to fully demonstrate the scalability and robustness of the proposed algorithms. The authors make claims about computational efficiency and linear memory requirements compared to methods using Hessian computation, but these claims lack rigorous theoretical proof or experimental validation. Specifically, the paper does not provide a detailed analysis of the computational cost associated with the Bayesian inference process, which could be a bottleneck for larger models. The comparison with state-of-the-art methods could be more comprehensive, particularly with respect to recent approaches like AMC or HAWQ. The paper would benefit from a more detailed analysis of computational overhead and practical implementation considerations, especially for larger models and datasets. A theoretical analysis of runtime complexity is notably absent, which would be valuable for understanding the scalability of the approach. While the mathematical foundations are sound, some of the more complex derivations, particularly in the appendix, could benefit from additional clarification and simplification to improve accessibility. These limitations, while not invalidating the paper's contributions, represent opportunities for strengthening the work and its potential impact on the field.

### Questions
Could you provide more extensive comparisons with state-of-the-art methods like AMC and HAWQ?
What is the theoretical and practical runtime complexity of your algorithms?
How does the approach scale with larger datasets and more complex architectures?
Can you provide empirical evidence for the claimed linear memory requirements?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces algorithms that leverage uncertainty analysis in Bayesian Neural Networks (BNNs) to assess the importance of weights and apply it into mixed-precision quantization to determine optimal bit-width of each layer.

### Strengths
The paper propose a mixed-precision quantization, achieving comparable performance compared to traditional Quantization-Aware Training (QAT) algorithms. 

The concepts are well-explained.

### Weaknesses
1. The approach builds on well-established methods, particularly drawing from prior work [1] on measuring weight importance in pruning and applying it to quantization. This reduces the novelty of the contribution, as the techniques have been previously discussed in [1]. However, the paper does extend this work effectively into the domain of mixed-precision quantization, applying the importance metrics in a novel context. Despite this extension, the core idea remains closely tied to existing pruning methods, which limits the originality of the contribution.

[1] Blundell, Charles, et al. "Weight uncertainty in neural network." International conference on machine learning. PMLR, 2015.

2. The proposed algorithms lack sufficient evaluation on state-of-the-art models, making it challenging to assess how powerful they are in real-world applications. Without benchmarking against modern models such as LLMs or using more diverse and complex datasets, it becomes difficult to measure the true effectiveness and robustness of the approach. 
In addition, a comparison with the latest quantization algorithms is necessary.

3. The method relies heavily on BNNs, making it unsuitable for models that are not trained within a BNN, thereby restricting its applicability.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The article presents a novel approach to adaptive quantization in neural networks, leveraging epistemic uncertainty analysis. By treating the quantized model as a Bayesian neural network with stochastic weights, the method utilizes mean values for weight estimation and standard deviations to indicate uncertainty—where more bits signify lower uncertainty. The authors introduce two new algorithms for mixed-precision quantization: QuantileInform, which allocates bit-width based on uncertainty across layers, and RandomBits, which uses stochastic gradient-based optimization to enhance quantization likelihood.

### Strengths
1.Innovative Approach: The integration of epistemic uncertainty analysis into quantization offers a fresh perspective on optimizing neural networks.

2.Mixed-Precision Algorithms: The introduction of two new algorithms allows for flexible bit-width allocation, enhancing model efficiency.

### Weaknesses
1.Limited Experimental Scope: Lacks experiments on Transformer and larger datasets like ImageNet.

2.Lack of Benchmarking: No comparison with state-of-the-art methods obscures performance insights,like Adabin.

3.The actual acceleration effect is not shown in the experiment.

### Questions
1. Does your method only quantize the weights?

2.Why introduce uncertainty to quantize models? What are the advantages?

3.How do you ensure that your entire algorithm can be implemented on low-bitwidth hardware?

### Soundness
2

### Presentation
2

### Contribution
2
