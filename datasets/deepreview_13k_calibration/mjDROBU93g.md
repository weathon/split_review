# DISTA: DENOISING SPIKING TRANSFORMER WITH INTRINSIC PLASTICITY AND SPATIOTEMPORAL ATTENTION

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
Among the array of neural network architectures, the Vision Transformer (ViT) stands out as a prominent choice, acclaimed for its exceptional expressiveness and consistent high performance in various vision applications. Recently, the emerging Spiking ViT approach has endeavored to harness spiking neurons, paving the way for a more brain-inspired transformer architecture that thrives in ultra-low power operations on dedicated neuromorphic hardware. Nevertheless, this approach remains confined to spatial self-attention and doesn't fully unlock the potential of spiking neural networks.
We introduce DISTA, a Denoising Spiking Transformer with Intrinsic Plasticity and SpatioTemporal Attention, designed to maximize the spatiotemporal computational prowess of spiking neurons, particularly for vision applications. DISTA explores two types of spatiotemporal attentions: intrinsic neuron-level attention and network-level attention with explicit memory. Additionally, DISTA incorporates an efficient nonlinear denoising mechanism to quell the noise inherent in computed spatiotemporal attention maps, thereby resulting in further performance gains. Our DISTA transformer undergoes joint training involving synaptic plasticity (i.e., weight tuning) and intrinsic plasticity (i.e., membrane time constant tuning) and delivers state-of-the-art performances across several static image and dynamic neuromorphic datasets. With only 6 time steps, DISTA achieves remarkable top-1 accuracy on CIFAR10 (96.26\%) and CIFAR100 (79.15\%), as well as 79.1\% on CIFAR10-DVS using 10 time steps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have tackled a rather interesting and important problem, which is to design/improve spiking neural networks-based vision transformers. More specifically, the authors have proposed a spiking transformer model that provides node-level and network-wide spatiotemporal attention with denoising. In this work, they consider, a simple yet effective, neuromorphic model called Leaky Integrate-and-Fire that makes use of the temporal information that decays over time. They incorporated a learnable time constant to be used in LIF and a thresholding-based efficient denoising technique. The experiments show a significant improvement over their predecessor, Spikformer.

### Strengths
Originality 
- Incorporating spiking neural networks with the vision transformers is a very recent yet challenging issue. The authors are expanding on the work of Spikformer [1]. Even that work is very recent. The main objective of the paper is to make efficient spiking transformers that take advantage of temporal information.  Previous work is lacking in this regard; however, the authors have tackled this issue and improved the approach. They also involve a denoising technique for the accumulated spatiotemporal maps since they do not use a rather complicated function Softmax. Therefore, I believe this work is reasonably new and the concept itself deserves more attention. 

Quality
- Spiking neural networks, more or less, mimic biological networks. Of course, it all depends on the biological plausibility of the models. For example, leaky integrate and fire models are very efficient neuromorphic models; however, compared to the Hodgkin-Huxley model, they are comparatively less biologically plausible. Thus said, current neuromorphic hardware does take advantage of the concept of LIF models to develop an SNN-based chip, and these models are not just space-efficient but also energy-efficient.
- Given the progression in transformers, the authors of this paper have shown that making transformers more biologically plausible can indeed have significant advantages over the other neuromorphic approaches. They do so by comparing against the most recent Spikformer [1], and other neuromorphic approaches with variable time steps.
- Specifically, the authors have integrated learnable time-constant (tau), which is a very important parameter in LIF that decides the significance of the input at the current time-step to the future ones. Further, to make the spatiotemporal attention mechanism less computationally expensive, the spiking networks have discarded Softmax masking, instead, the authors have used a threshold-based masking technique that significantly reduces the computational overhead.
- The authors have shown significant improvement over the other baseline approaches, and have done extensive ablation studies. 

Clarity
- The paper is well-written and straightforward. The objective is clearly stated and tackled reasonably well throughout the paper.

Significance
- Since this approach is tackling a very recent and significant challenge of making neural networks more energy-efficient using spiking neural networks, it could have a good impact on the current research.

References:
1. Zhou, Zhaokun, Yuesheng Zhu, Chao He, Yaowei Wang, Shuicheng Yan, Yonghong Tian, and Li Yuan. "Spikformer: When spiking neural network meets transformer." arXiv preprint arXiv:2209.15425 (2022).

### Weaknesses
Concerns:
- There are a few things that the authors discussed in the paper; however, are not fully tackled. 
  - Spiking networks by nature use less energy to function since they take advantage of the temporal coding. The authors have discussed this and it is one of the core reasons the community is interested in this, it would be interesting to perform a comparative analysis on hardware to test this approach. The authors have only discussed the accuracy of the approach. Specifically, a detailed analysis of power consumption, latency, and throughput on neuromorphic hardware would be valuable to demonstrate the practical advantages of the proposed method. This should include comparisons with other SNN implementations and traditional deep learning models.
  - Another thing would be space complexity. There should also be a comparative analysis of the space complexity of the approach. This should include the number of parameters, memory footprint during inference, and the impact of the learnable time constant on model size. A comparison with other transformer-based models, both spiking and non-spiking, would be beneficial.
- To get a better idea of the significance of the approach, comparative analysis on large benchmarks such as ImageNet would also be interesting to observe. While the authors have shown improvements on smaller datasets, the performance on a large-scale dataset like ImageNet is crucial to assess the scalability and generalization ability of the proposed model. This should include a comparison with state-of-the-art vision transformers and other SNN models.
  - There are many hyperparameters involved: 𝜭, u, t, etc. The paper lacks a detailed discussion on the sensitivity of the model to these hyperparameters. An analysis of how the performance varies with different settings of these parameters, and a discussion on the optimal selection strategy, would be beneficial.

### Questions
The approach signifies the importance of spiking transformers; however, to fully exploit the potential of this approach, I believe, there are certain things to be considered:
- As mentioned in the weakness section, the paper does lack a rather important comparative analysis of energy-efficiency as mentioned. Please consider that as a measure of performance since it is one of the most crucial properties of the SNNs. 
- I believe, with further analysis of the efficiency, this paper could be a good contribution to the vision community.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces DISTA, a novel architecture for spiking neural networks (SNNs) aiming to improve their performance on vision tasks by utilizing spatiotemporal attention mechanisms.

### Strengths
+ Innovative Architecture: DISTA innovates by integrating spatiotemporal attention at both neuron and network levels, along with a denoising mechanism, which leads to state-of-the-art performance on several datasets.

+ Energy Efficiency: By leveraging the inherent efficiencies of SNNs and denoising mechanisms, DISTA promises to improve energy efficiency, which is crucial for neuromorphic computing.

+ Biologically Inspired: The approach takes inspiration from the biological brain, potentially opening up new avenues for understanding neural processing.

+ High Accuracy: DISTA achieves remarkable accuracy improvements on the CIFAR10 and CIFAR100 datasets, demonstrating the potential of SNNs in complex tasks.

+ Backpropagation Integration: The paper integrates backpropagation-based synaptic and intrinsic plasticity into SNNs, enhancing their learning capabilities.

### Weaknesses
 - Novelty: While the paper draws inspiration from the Spikeformer, the adaptation of the temporal attention window raises concerns. The increase in the number of parameters, potentially leading to the observed accuracy improvements, needs further investigation. It is unclear whether the temporal attention mechanism itself is the primary driver of these gains. The absence of results on the ImageNet dataset is notable. It's possible that the computational demands of temporal attention become prohibitive for larger datasets, limiting the scalability of the proposed approach. Clarifying the scalability and discussing the limitations, especially concerning parameter explosion in larger datasets like ImageNet, would strengthen the paper.

- Specificity of Application: The paper demonstrates significant improvements in vision tasks using CIFAR10 and CIFAR100 datasets. However, the adaptability of DISTA to other types of tasks remains unexplored. A discussion on the potential applicability of the proposed spatiotemporal attention mechanisms and denoising techniques to other domains, such as natural language processing or time-series analysis, would broaden the paper's impact.

- Overfitting Risk: The increased model complexity due to multiple attention mechanisms introduces a potential risk of overfitting. While not explicitly addressed, providing insights into the measures taken to mitigate this risk, such as regularization techniques or validation strategies, would enhance the paper's rigor.

- Energy Efficiency Claims: The paper claims improved energy efficiency, which is crucial for neuromorphic computing. However, a more detailed analysis of energy consumption, possibly using spiking hardware simulator tools, would be valuable. A quantitative or at least qualitative discussion on the expected sparsity advantages at the compute level or memory storage reduction from a hardware perspective would help substantiate these claims.

### Questions
see weaknesses above. I am giving a rating of 6 mainly because of novelty concerns. If the authors can provide suitable justification, I ll change my rating.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces DISTA, a novel neural network architecture that synergizes the strengths of Vision Transformer (ViT) with the potential of spiking neurons. DISTA stands out with its "Denoising Spiking Transformer" design that integrates Intrinsic Plasticity and Spatiotemporal Attention, optimizing its computational prowess for vision tasks. A distinct innovation lies in its noise-reducing mechanism for computed spatiotemporal attention maps, ensuring more refined performance. Demonstrating its efficacy, DISTA yields notable results on benchmark datasets such as CIFAR10 and CIFAR10-DVS.

### Strengths
1.	It changed the Linear layer into production of matrix, and the complexity is indeed O(ND^2) or O(TND^2).
2.	This work adopted PLIF to improve the performances.
3.	This work explores two types of spatiotemporal attentions.
4.	This paper is well written.

### Weaknesses
The biggest flaw is training for 1000 Epochs on CIFAR100 and CIFAR10. This suggests potential inefficiencies in the model's architecture or optimization process, as other models might achieve comparable results with fewer epochs. While the algorithm demonstrates improvements on both CIFAR10 and CIFAR100 datasets, the improvement on CIFAR100 is not as substantial as one might expect given the extended training time. Furthermore, the lack of evaluation on larger datasets like ImageNet raises concerns about the model's scalability and generalizability to more complex, real-world scenarios. The paper also lacks detailed analysis regarding model complexity, such as the number of parameters and computational cost, which are crucial for understanding the practical applicability of the proposed architecture.

### Questions
Why the model converge so slow (1000 Epochs)

How's the performance on ImageNet

Is there any improvements on PLIF or just grab it without any changes

Please add the analysis on complexity, parameters etc

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
this work introduces a Denoising Spiking Transformer with Intrinsic Plasticity and SpatioTemporal Attention. The work did experiments on Cifar.

### Strengths
1. the work provides two types of spatiotemporal attentions: intrinsic neuron-level attention and network-level attention.
2.  the work also provides an efficient nonlinear denoising mechanism.

### Weaknesses
1. The main weakness of the paper is the novelty, the  SpatioTemporal Attention has been proposed in prior work[1].
2. The imagenet dataset is widely used in the SNN field, but the work misses it.
3. Other results in the SPIKFORMER should be compared in the work.
4. Some recent work is missing, e.g., [2,3]

### Questions
see weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
