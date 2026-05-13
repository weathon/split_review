# ARQ: A Mixed-Precision Quantization Framework for Accurate and Certifiably Robust DNNs

- Decision: Reject
- Scores: 8, 3, 3, 5

## Abstract
Mixed precision quantization has become an important technique for
enabling the execution of deep neural networks (DNNs) on limited resource computing platforms.
Traditional quantization methods have primarily concentrated on maintaining
neural network accuracy, either ignoring the impact of quantization on the
robustness of the network, or using only empirical techniques for improving
robustness. In contrast, techniques for robustness certification, which can
provide strong guarantees about the robustness of DNNs have not been used
during quantization due to their high computation cost. 

This paper introduces ARQ, an innovative mixed-precision quantization method that not only
preserves the clean accuracy of the smoothed classifiers but also maintains
their certified robustness. ARQ uses reinforcement learning to find accurate and robust
DNN quantization, while efficiently leveraging randomized smoothing,
a popular class of statistical DNN verification algorithms, to guide the search process. 
We compare ARQ with multiple state-of-the-art quantization techniques on
several DNN architectures commonly used in quantization studies: ResNet-20 on
CIFAR-10, ResNet-50 on ImageNet, and MobileNetV2 on ImageNet. 
We demonstrate that \Tool{} consistently performs better than these baselines
across all the benchmarks and the input perturbation levels. In many cases, the performance of ARQ quantized networks can reach that of the original DNN with floating-point weights, but with only$~1.5\%$ instructions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces ARQ (Accurate and Robust Quantization), a framework that addresses the critical challenge of deploying deep neural networks in resource-constrained environments while maintaining both accuracy and robustness. The framework's key innovation lies in its novel approach to mixed-precision quantization that directly optimizes for certified robustness, making it the first of its kind in the field. Through a sophisticated combination of reinforcement learning and randomized smoothing, ARQ achieves remarkable efficiency gains while preserving or even improving model performance compared to full-precision networks.

### Strengths
The use of average certified radius as an optimization objective is particularly novel, allowing simultaneous optimization of accuracy and robustness.
The quality of the research is evident in the comprehensive experimental validation across multiple architectures and datasets. The authors provide ablation studies and comparative analysis which gives valuable insights into the framework's behavior and advantages. The achievement of matching or exceeding full-precision performance with drastically reduced computational requirements is particularly impressive.

### Weaknesses
While the paper's contributions are substantial, there are areas that could benefit from further exploration. The current focus on convolutional neural networks and image classification, while well-executed, leaves open questions about generalization to other architectures and tasks. This limitation is acknowledged by the authors, but additional discussion of potential adaptation strategies would be valuable.
The paper would benefit from more detailed analysis of memory usage patterns during training, though the runtime analysis provided in Table 2 is helpful. Specifically, a breakdown of memory consumption by layer type (e.g., convolutional, fully connected) and by the different precision levels would be beneficial. Additionally, while the framework's theoretical foundations are strong, more discussion of practical hardware implementation considerations for mixed-precision inference would strengthen the work's immediate applicability. This should include discussion of memory access patterns and data layout for efficient inference on hardware accelerators.

### Questions
How might the ARQ framework be adapted for sequence models or transformers, particularly regarding the interaction between attention mechanisms and mixed-precision quantization?
What modifications to the incremental randomized smoothing approach might be necessary to support other certification methods while maintaining computational efficiency?
How does the framework handle the transition between different precision levels during inference, and what are the implications for hardware implementation?
Could the reinforcement learning approach be extended to dynamically adjust precision levels during inference based on input characteristics?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces ARQ, a novel mixed-precision quantization framework for executing deep neural networks (DNNs) on resource-constrained platforms while maintaining accuracy and certified robustness. ARQ employs reinforcement learning to find quantization policies that preserve a DNN's accuracy, enhance its robustness, and reduce computational costs, effectively utilizing random smoothing for guidance. The framework supports mixed-precision quantization, allowing different bit-widths for weights in each layer, providing fine-grained control over quantization policies. ARQ is the first to optimize for certified robustness in DNNs and includes random smoothing within its reinforcement learning loop. Experimental results on CIFAR-10 and ImageNet datasets demonstrate that ARQ outperforms state-of-the-art quantization techniques, often matching or exceeding the performance of original FP32 networks with significantly reduced operations. The paper acknowledges ARQ's limitations, such as dependence on the training of the original network and challenges in deploying mixed-precision inference, and suggests future work on applying ARQ to tasks beyond image classification.

### Strengths
The paper is easy to read.

### Weaknesses
1.	The performance of ARQ is heavily reliant on the quality of the training of the original DNN. If the original network is not properly trained or lacks Gaussian augmentation, the quantized network may not meet expected performance.
2.	ARQ has only been evaluated on image classification tasks. Its performance and effectiveness on other types of tasks have not been validated.
3.	While ARQ performs well in the experiments, its generalizability across different network architectures and datasets remains an open question and requires further research for validation.
4.	The performance of ARQ may be sensitive to hyperparameter choices, which could require additional tuning efforts to ensure optimal performance across different networks and datasets.
5.	The presentation of the paper is poor. For examples, the statement of robustness is not clear, adversarial inputs or what? If it is adversarial inputs, why not provide the details for adversarial methods? PGD or FGSM?
6.	The method is not novel, and too complex. The results are also not convincing.
7.	The main limitations are experiments, i.e., more datasets (COCO2017, VOC), more larger networks (e.g., VIT, GPT-2, Efficientnet), more tasks (detection, segmentation, VQA), and more validation for robustness.
8.	Why not compare with more competitors[1-3]? 
[1] SDQ: Stochastic Differentiable Quantization with Mixed Precision
[2] EMQ: Evolving Training-free Proxies for Automated Mixed Precision Quantization
[3] OMPQ: Orthogonal Mixed Precision Quantization

### Questions
1. What is the definition of robustness for MPQ?
2. What is certified robustness?
3. In your paper, you argue that traditional quantization methods have primarily concentrated on maintaining neural network accuracy, this is not accurate. The goal of MPQ is to study how to reduce the network's parameters, namely, obtaining the trade-off between accuracy and complexity. They have at least two objectives to learn.
4. Why use reinforcement learning?
5. In your paper, you state two objectives, i.e.,  accuracy, and robustness. Why not consider complexity? Maybe you don't understand the MPQ.

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
4

### Summary
This paper introduces a mixed-precision quantization framework ARQ which optimizes both DNN’s accuracy and certified robustness under computational resource constraint. ARQ employs reinforcement learning to optimize quantization policies and leverage incremental randomized smoothing (IRS) within the reinforcement learning loop, allowing it to efficiently guide the search for quantization policies that maximize the average certified radius (ACR) of the DNN.

### Strengths
ARQ has better accuracy and robustness, i.e., ACR, than other compared methods.

### Weaknesses
1. The authors didn’t compare ARQ with any robustness-aware quantization methods as listed in Table5.
2. The authorsdidn’t compare with other advanced fixed-precision or mixed-precision quantization algorithms, such as LSQ[1], LSQ+[2], or HAWQ[3][4].
3. Although ARQ has better accuracy and robustness, it consumes much longer time than other methods as shown in Table2. What is the impact of search time on the final accuracy.
4. The authors only use BitOps as the constraints. What about the model size?  
5. The techniques proposed in the paper seem incremental. The authors need to provide more explanation on the novelty of the method.

### Questions
Please refer to the weakness for questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces ARQ, a mixed-precision quantization framework for deep neural networks that focuses on robustness of quantization technique. ARQ incorporates robustness certification techniques directly into the quantization process, addressing the limitations of conventional methods that solely focus on accuracy. It leverages randomized smoothing to estimate the certified radius, which reflects the network's resilience to input perturbations. ARQ frames the quantization problem as a reinforcement learning task, where an agent searches for optimal bit-width assignments for each layer, maximizing the average certified radius while adhering to resource constraints.

### Strengths
1. Strong motivation: Modern quantization techniques, even though they show less quality drop on specific models and tasks, show large quality drop on adversarial inputs which means reduced robustness of quantized network. This work targets the problem of making quantization technique which makes truly optimized network with high robustness that can widely adopted on the overall models.
2. Well explained background.
3. Novelty of methodology: Although ARQ adopts most of its robustness concept from existing works, its own optimization objective of mixed precision quantization is unique since many existing works haven’t explored the robustness in terms of utilizing diverse bit-width in a model.

### Weaknesses
1. Weak baseline: Beyond robustness aware mixed precision quantization, there are several methods [1,2,3] that shows much less accuracy degradation on both ResNets and Mobilenets in Imagenet scale. What is the comparative advantage of ARQ compared to these methods even with accuracy degradation? For thorough comparison, shouldn't the authors include comparisons with various types of mixed precision quantization method? The current comparison only focuses on a single baseline, NIPQ, which does not fully address the landscape of mixed-precision quantization techniques. A more comprehensive evaluation should include methods that achieve higher accuracy with similar or lower bit-widths, even if they do not explicitly target robustness.
2. Comparison with existing robustness aware MPQ: Within robustness aware quantization, the current metrics cannot justify the benefit of ARQ in the aspect of robustness compared to existing robustness aware MPQ (in Table5). The comparison lacks a clear demonstration of ARQ's superiority in certified robustness over other methods that also consider robustness during quantization. The current metrics, such as average certified radius, do not sufficiently highlight the specific advantages of ARQ in this domain. It is unclear if the gains are significant enough to justify the complexity of the proposed method.
3. Algorithm: Lack of explanation of several terms in Algorithm1 makes bad readability, i.e., FullRobustCertify, IncrementalRobustCertify. The algorithm description lacks clarity, making it difficult to understand the implementation details and reproduce the results. The specific roles and implementations of `FullRobustCertify` and `IncrementalRobustCertify` are not well-defined, which hinders the understanding of the core methodology.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
4

### Contribution
3
