# Structured Initialization for Attention in Vision Transformers

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
The training of vision transformer (ViT) networks on small-scale datasets poses a significant challenge. 
    By contrast, convolutional neural networks (CNNs) have an architectural inductive bias enabling them to perform well on such problems. 
    In this paper, we argue that the architectural bias inherent to CNNs can be reinterpreted as an initialization bias within ViT. 
    This insight is significant as it empowers ViTs to perform equally well on small-scale problems while maintaining their flexibility for large-scale applications. 
    Our inspiration for this ``structured'' initialization stems from our empirical observation that random impulse filters can achieve comparable performance to learned filters within CNNs. 
    Our approach achieves state-of-the-art performance for data-efficient ViT learning across numerous benchmarks including CIFAR-10, CIFAR-100, and SVHN. 
  \keywords{Attention mechanism \and Model initialization \and Transfomers}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of applying Vision Transformers (ViTs) to new domains with small datasets, where Convolutional Neural Networks (CNNs) typically excel due to their inherent architectural inductive bias. The authors propose a novel approach that reinterprets CNN's architectural bias as an initialization bias for ViTs, termed "structured initialization." Unlike traditional ViT initialization methods that rely on empirical results or attention weight distributions, this method is theoretically grounded and constructs structured attention maps. The paper demonstrates that this structured initialization enables ViTs to achieve performance comparable to CNNs on small-scale datasets while retaining the flexibility to perform well on larger-scale applications. The proposed method shows significant improvements over conventional ViT initialization across several small-scale benchmarks, including CIFAR-10, CIFAR-100, and SVHN, and maintains competitive performance on large-scale datasets like ImageNet-1K.

### Strengths
1.Theoretical Foundation: The structured initialization method is based on solid theoretical analysis rather than just empirical results, providing a strong rationale for its effectiveness.

2.Performance Improvements: The method consistently shows significant performance improvements over conventional ViT initialization methods in small-scale datasets, which is a notable achievement.

### Weaknesses
1. In terms of innovation, the Transformer architecture was initially designed to minimize inductive bias. The author's attempt to incorporate structural biases from CNNs into the Transformer seems to go against the original intent of the Transformer design, which could be seen as a step backward for the evolution of Transformer models.

2. The variety of experimental backbones is somewhat limited. It would be beneficial to conduct experiments with DeiT or Swin-Transformer to compare results. Furthermore, aside from classification tasks, it would be interesting to test the method on detection or segmentation tasks to further evaluate its versatility and effectiveness.

### Questions
Why not apply structured initialization to the value (V) component of self-attention? Additionally, how are the feed-forward network (FFN) layers, normalization layers, and projection layers initialized in the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an approach to initialize ViT through structured initialization of attention maps. By incorporating CNN-like inductive biases during initialization, it aims to combine the local spatial processing capabilities with the global relationship learning of attention mechanisms and take advantage of CNNs' inductive bias. Experimental results on several small-scale datasets validate its effectiveness.

### Strengths
- The paper is easy to follow.
- As much work has been trying to introduce convolutional design into the ViT model, this paper provides an interesting viewpoint that initializing the attention map as CNNs can also help to introduce the inductive bias and subsequentially improve the performance of trained ViT on small-scale datasets.
- A theoretical explanation is provided to show the connection between the structural initialization in ViT and inductive bias in CNNs.
- Some special designs like more heads and various initialization conv kernel sizes are adopted.

### Weaknesses
 - The fundamental approach of forcing attention maps to mimic convolutional kernels seems to contradict the core advantage of attention mechanisms, as their advantage is to learn flexible, dynamic global relationships. It would be better to justify why structured initialization is preferred over simply incorporating convolutional blocks into the architecture, which would be a more straightforward solution. 
- It would be better to provide more analysis of why this approach is better compared to well-established solutions: 
  - Transfer learning from large-scale pre-trained ViTs
  - Hybrid architectures combining convolution and attention
- The optimization process required for initializing attention maps introduces additional computational overhead during training, and one needs to further choose the optimizer for initialization and conv kernel size (as well as other hyperparameters for different model sizes), which makes it impractical.
- The improvement on the widely-used ImageNet benchmark appears marginal, suggesting limited practical benefit in scenarios where large datasets are available. Moreover, as shown in Figure 6, the attention maps of the model initialized with structured initialization lean toward a local attention pattern, even after training. It's unclear whether this localized attention will not limit the models' learning ability, and the current analysis lacks quantitative validation beyond classification performance.

### Questions
-  Does the structured initialization limit the model's ability to learn better representation? It would be better to provide some representation-level analysis using metrics like Centered Kernel Alignment (CKA) similarity [1].

[1] Kornblith, Simon et al. “Similarity of Neural Network Representations Revisited.” ICML 2019.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a novel method for improving the performance of ViTs when trained on small-scale datasets by incorporating structured initialization. The authors identify that ViTs struggle with small datasets compared to CNNs, which benefit from inherent inductive biases. By reinterpreting the architectural bias in CNNs as an initialization bias for ViTs, the authors propose a "structured initialization" method that results in structured attention maps for ViTs. The key contribution lies in the use of random convolutional impulse filters to guide the initialization process. The method is theoretically justified and empirically validated across serveral benchmarks. The paper demonstrates that structured initialization yields performance improvements on small datasets without compromising ViT’s flexibility on larger datasets.

### Strengths
Structured architecture achieves good performance across both small and large datasets, which demonstrates its scalability and flexibility.

### Weaknesses
1. The core argument of the method is that the convolutional structure can be transferred to the attention mechanism in transformers by initializing the attention maps with random impulse filters. However, this analogy between convolutional layers in CNNs and the attention mechanism in ViTs may be overly simplistic. CNNs' convolutional filters are spatially local and fixed in structure, while attention in ViTs is meant to capture long-range dependencies and is more flexible. This difference is crucial, and the method does not seem to fully address how imposing a rigid, convolution-like structure at initialization aligns with the flexibility that the attention mechanism needs. The convolution structure might limit the model's ability to learn long-range dependencies that are essential to the transformer. The claim that random impulse filters can replace learned convolutional filters is somewhat true for CNNs under certain conditions (like ConvMixers), but applying this to ViTs is more challenging. The attention mechanism is a more complex and dynamic operation compared to convolutions, and it’s unclear if the same approximation can hold. In practice, imposing a convolution-like structure might hinder the attention mechanism's ability to adapt during training.

2. The paper proposes that impulse filters, combined with the softmax operation, can initialize the attention maps. The softmax function ensures that all outputs are non-negative, which is a crucial difference from convolutions, which can have both positive and negative values. Random convolutional filters may contain both positive and negative values, while softmax output does not. This inconsistency could cause issues. The authors acknowledge this (stating the filters must be positive), but they do not provide a deep exploration of how this might affect the quality or flexibility of the learned attention maps. Relying on impulse filters could reduce the model's expressivity, especially if the initialized filters are too rigid and only positive-valued patterns are learned initially.

3. The authors propose an iterative optimization process to solve for the initial values of $Q_{init}$ and $K_{init}$ such that the resulting attention maps resemble impulse convolution filters. The optimization is based on a pseudo-input, which is generated from positional encodings rather than actual data. This could introduce an unwanted bias into the model's initial learning process. While using positional encoding as pseudo-input is an interesting idea, the paper does not adequately explore how different choices of pseudo-inputs affect the results or whether using actual training data for initialization would be a better alternative. The positional encodings themselves impose a fixed structure that might interfere with the model's ability to adapt dynamically to certain tasks, potentially hindering performance in scenarios where positional information conflicts with learned representations, such as tasks requiring permutation invariance.

4. The optimization process described is more computationally expensive (up to 10,000 iterations using Adam) compared with traditional initialization methods. This added complexity raises the question of whether the benefits of structured initialization outweigh the cost, especially given that the improvements on large datasets are marginal. There is no discussion of the computational cost vs. benefit of this method compared to standard initialization techniques.

5. The use of random impulse convolution filters assumes that locality is always important, but this assumption may not hold in tasks where global context is critical. In CNNs, locality is useful because of the hierarchical structure of learned features. However, in transformers, the attention mechanism is specifically designed to handle long-range dependencies. By forcing the model to start with local dependencies (via impulse filters), the authors may inadvertently restrict the model's ability to learn global features early in training, leading to potential issues in tasks where global context is key from the beginning.

6. The method relies on several hyperparameters, including filter size (3x3 or 5x5) and the number of iterations for optimization. However, the choice of these hyperparameters is not adequately justified or explored. The method's performance is likely sensitive to these parameters, but there is no thorough analysis of how variations in filter size or optimization parameters affect results. Given the complexity of the initialization process, these aspects should have been investigated in detail to ensure the method’s robustness.

### Questions
1. Why Impulse Filters? The reasoning behind choosing impulse filters (instead of other structured filters) for initializing attention maps could be explained in more detail. Are impulse filters the best possible choice, or could other filter types provide better generalization?

2. How does this structured initialization affect the deeper layers of ViTs after finetuning? Figure 3 is quite interesting. Do the constraints imposed by impulse filters affect the deeper layers’ ability to fine-tune long-range dependencies? The paper does not discuss the long-term effects of this initialization on the network’s convergence.

### Soundness
2

### Presentation
3

### Contribution
2
