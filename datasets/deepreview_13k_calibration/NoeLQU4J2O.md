# Soon Filter: Advancing Feed-Forward Neural Architectures for Inference at the Edge

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
As Deep Neural Networks become more complex and computationally demanding, efficient models for inference at the edge, particularly multiplication-free ones, have gained significant attention. The Ultra Low-Energy Edge Neural Network (ULEEN) is a notable architecture optimized for feed-forward designs. ULEEN uniquely employs Bloom Filters with binary values to compute neuron activation, boasting better efficiency metrics than Binary Neural Networks (BNNs). This work uncovers a gradient back-propagation bottleneck within ULEEN's Bloom filters and introduces introduces a simplified version of it as a solution: the "Soon Filter". Both theoretically and empirically, we demonstrate that our approach improves gradient back-propagation efficiency. Tests on various UCI datasets and MNIST, which are standard benchmarks for feed-forward models, reveal that our method surpasses ULEEN, BNN, and DeepShift. Notably, with MNIST, we achieve 98.6% with only 98KiB, while ULEEN, BNN and DeepShift achieves 98.5% with 262KiB, 98.5% with 355KiB and 98.3% with 408KiB respectively. Furthermore, when using MLPerf Tiny datasets, which are typically more appropriate for CNNs, we consistently outperform other models when they are implemented as Multilayer Perceptrons. This results underscores the promising potential of our solution for efficient inference at the edge in applications that rely on feed-forward architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study primarily aims to reveal a noteworthy bottleneck in the gradient back-propagation process of ULEEN. This bottleneck is attributed to the continuous relaxation of Bloom filters, which hinders the learning process. Drawing inspiration from the principles emphasized in ResNet, which stress the benefits of fine-tuning network architecture to enhance gradient flow, this study introduces a solution known as the "Soon filter." Theoretical and empirical results demonstrate that this proposed solution substantially enhances the smooth back-propagation of gradients to filter locations. Consequently, it establishes a new state-of-the-art benchmark for multiplication-free feed-forward models.

### Strengths
1. The paper is well-structured and easy to follow.

2. The primary goal is to set a new state-of-the-art benchmark for multiplication-free feed-forward models.

3. The introduction of the "Soon filter" addresses the gradient flow issue.

### Weaknesses
1. Incorporating additional visual aids and illustrations within the section on related work would greatly enhance the clarity and comprehensibility of the paper. These visuals can provide readers with a more comprehensive understanding of the prior research landscape in the field.

2. While the central contribution of the paper revolves around the introduction of the "Soon Filter," it is essential to consider augmenting this with supplementary contributions or by providing more extensive exploration and insights to enrich the overall content and scholarly impact.

### Questions
1. Based on Figure 1 and the main content, is the primary distinction between these methods solely attributable to the replacement of the OR operation with the SUM operation?

2. Regarding the VWW dataset, have you evaluated the performance of these methods on smaller models like MCUNetV1 [1] and MCUNetV2 [2]? Such an analysis could provide insights into the accuracy reduction when transitioning from multiplication-based models and offer valuable insights.


[1] MCUNet: Tiny Deep Learning on IoT Devices 

[2] MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a multiplication-free neural network based on bloom filters, making it suitable for deployment on ultra-constrained edge/IOT devices. In fact, the paper focuses on a specific optimization to bloom filters and prior work (ULEEN) by replacing a non-differentiable logic function (AND) with a summation operation. This helps gradient flow and trainability making the NN achieve higher accuracy on an assortment of tasks.

### Strengths
The paper is clearly-written and well-motivated and the empirical improvements are consistent on a number of tasks.

### Weaknesses
This paper is interesting and I learned something new about multiplication-free circuits. However, the proposed modification is very small (compared to ULEEN), the application is quite niche and not well demonstrated, the improvements are very small, and the evaluation is inadequate. This work is promising but there are more questions that need to be answered to provide a compelling argument for the presented approach.

### Questions
- How does your performance compare to CNNs?
- How general is your approach? Can it be applied to CNNs, attention, other tasks, other NN sizes?
- DId you deploy this on a challenging edge device? how does end-to-end performance compare to alternatives?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a set of technique to realize an implementation of neural networks that are as simple as binary neural networks. Rather than binarization, the authors use hashing functions, inspired from earlier works that have considered filtering techniques. The novelty proposed by the authors is to slightly modify the gradient formulation for back-propagation. A problem with regular STE convergence is identified when using ULEEN, whereby the use of minimum function causes a bottleneck. As an alternative, the authors propose to use the sum function for approximating AND resulting in an always 1 gradient. Experimental results on tiny datasets are provided.

### Strengths
The paper is well written, and the exposition of the problem is clear. The presented analysis is clear to follow, and interesting.

### Weaknesses
Several issues with this paper can be noted:

-- The main objective of the paper is to reduce the complexity of implementation using hashing and filtering. However, very little is done to measure this complexity. Only the model size is reported, as proxy to complexity. But what about the overhead of implementing hashing and filtering? Specifically, what are the computational costs associated with the hash function, and how does the memory footprint of the hash table compare to the model parameters themselves? How does that compare to regular binarization where values are simply clipped to +/-1? How does that compare to low bit width implementation (e.g., 4-bit or 8-bit)? A detailed analysis of the computational and memory costs of the proposed hashing and filtering approach is needed, including a breakdown of the operations involved and a comparison against standard binarization and low-bit quantization techniques. I found the discussion on hardware benefits and limitations of the method very weak.

-- The utilized benchmarks are extremely trivial. The authors have only tested their work on tiny models and datasets. Does the method work on models more relevant to the community in this day and age? E.g., large vision and language models? Even for those tiny datasets, the accuracy is not even close to the state-of-the-art, such as for CIFAR-10 where the authors report accuracies close to 50%. The lack of experiments on more challenging datasets and larger models makes it difficult to assess the practical applicability of the proposed method. The reported accuracy on CIFAR-10 is significantly below what is achievable with other methods, raising concerns about the effectiveness of the approach.

### Questions
Please address questions provided in the above section. Specifically:

-- More nuanced discussion on the hardware implications of the method.

-- More relevant empirical results on typical baselines employed in the ML community in 2023.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
