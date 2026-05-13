# Magnituder Layers for Implicit Neural Representations in 3D

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Improving the efficiency and performance of implicit neural representations in 3D, particularly Neural Radiance Fields (NeRF) and Signed Distance Fields (SDF) is crucial for enabling their use in real-time applications. These models, while capable of generating photo-realistic novel views and detailed 3D reconstructions, often suffer from high computational costs and slow inference times. To address this, we introduce a novel neural network layer called the ``magnituder", designed to reduce the number of training parameters in these models without sacrificing their expressive power. By integrating magnituders into standard feed-forward layer stacks, we achieve improved inference speed and adaptability. Furthermore, our approach enables a zero-shot performance boost in trained implicit neural representation models through layer-wise knowledge transfer without backpropagation, leading to more efficient scene reconstruction in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel neural network layer called the "Magnituder," designed to reduce the number of training parameters in implicit 3D representation models like NeRF and SDF. The proposed method can also be integrated into pretrained NeRF models without additional optimization. Extensive experiments on multiple datasets and tasks demonstrate that this approach achieves faster inference speed and reduced model size.

### Strengths
1. This paper performs extensive experiments to thoroughly demonstrate the capability of the proposed method.
2. The proposed method improves inference speed and reduces the model size of implicit 3D representations.

### Weaknesses
1. While the proposed neural network achieves speedup and compression, it does so at the cost of rendering quality. This seems more like a trade-off than a true improvement, as there are other methods in 3D representation, such as 3D Gaussian Splatting, Instant-NGP, and Neus2, that significantly increase inference speed (up to 10x) without compromising rendering quality. This limitation diminishes the significance of the contribution. The core issue is that the paper does not adequately address the fundamental trade-off between model size/inference speed and rendering quality. The gains in speed and model size are not particularly impressive compared to other methods, and the quality drop is a significant concern, especially since the paper focuses on 3D reconstruction where visual fidelity is paramount.
2. A simple baseline may achieve similar effects to the proposed method by reducing the number of layers in the original MLP. This approach could also reduce parameters and increase inference speed, potentially affecting rendering quality. The authors are encouraged to include this comparison. Specifically, the paper lacks a rigorous comparison against a baseline where the original MLP architecture is simply made shallower (i.e., reducing the number of layers) or narrower (i.e., reducing the number of neurons per layer) to match the parameter count of the proposed method. This is a critical omission as it is not clear if the proposed method offers any advantage over a simple reduction in network size.
3. The proposed Magnituder layer lacks any designs specifically for 3D tasks. As a general layer that can be integrated into MLPs, it could also be applied to other tasks like classification, or in models with MLP components like ResNet or Transformer. To fully demonstrate the benefits of this layer, it would be valuable to test it on other tasks as well. The paper should demonstrate the versatility of the proposed layer by evaluating its performance on tasks beyond implicit 3D representation. This would strengthen the claim that the proposed layer is a general-purpose building block for neural networks and not just a niche solution for implicit 3D representations.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents a new neural network layer, magnituder (MAG), to improve the efficiency of MLP models used on implicit neural representations (NeRF, SDF, etc.). Magnituder disentangles the weights and inputs of MLP layers by injecting a mapping function operating on the magnitude of the input. The design of magnituder is supported by the analysis of the approximation of kernel methods. Magnituder does provide improvements in inference speed and model size but not significant.

### Strengths
* The proposed method is well-analyzed through kernel estimation methods and the theoretical comparison with the prior approach SNNK. This makes the proposed method technically sound.
* The authors apply MAG-layers in multiple applications, which is appreciated.

### Weaknesses
Although the paper introduces an interesting new layer with some random features to speed up MLP models used in implicit neural representations, the improvements from their results are not that exciting (compared to other NeRF acceleration works in recent years). Other than the original NeRF, the proposed MAG layers can only provide less than 10% inference speed improvements. Besides, this marginal inference speedup is also at the cost of a quality drop.

Given the current trend towards neural 3D representations that use very few and tiny MLP layers or even no MLP layers (e.g., InstantNGP, 3DGS), the benefits of applying MAG-layers to such architectures would likely be very insignificant.

It would be better to see if the MAG-layers could be beneficial for other applications that use a lot of MLP layers, not just on implicit neural representations.

### Questions
1. As MAG is a lossy acceleration method, you can also reduce the number of parameters used in baseline NeRF MLP to make it faster but with a slightly lower quality. For example in Fig 3., you can reduce the hidden feature size in the baseline NeRF to match the random feature size in the corresponding red block in the MAG-NeRF. In this case, does MAG-NeRF still perform better in quality and speed?
2. How about the speedup on the training time?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel neural network layer, named MAG (magnituder), that is able to decouple the computation of inputting and weights parameters, thus accelerating the computation. The authors validate the effectiveness of MAG layers by inverse graphics (static, dynamic, and geometry) by reforming NeRF, Zip-NeRF, D-NeRF, and iSDF. The results show that the proposed MAG layers manage to accelerate the computation with small performance drop.

### Strengths
- The paper attempts to solve the problem of computational costs in the filed of Implicit Neural Representation, which is clearly motivated and significant for making INRs more scalable.
- The proposed MAG layers follow a plug-and-play fashion, making the integration into most of MLP-based INRs easy and fast, which would be greatly valued by the users. The core idea of simplifying the computation of FC layer is interesting.
- The experiments do showcase certain effectiveness of the MAG layers in terms of reducing the inference time at a cost of some performance.

### Weaknesses
 - The elaboration of the adopted methods (Sec.3) is somehow not sufficient to me. The authors are encouraged to include another illustration or pseudo code to better describe their method.
- Though the connection between MAG and SNNK is covered, such strategy for simplification still requires comparison between other well-known alternatives, e.g., distillation, pruning, and also separable convolution.
- The overall writing of this manuscript is not informative. For example, Sec.2 is a comprehensive but meaningless review of the applications of INRs, which is not closely related to the scope of the manuscript. Instead, the authors are supposed to include more strategies for simplifying or accelerating INRs.
- The quantitative results are not satisfactory enough to match the claimed contribution. A universal decline of performance can be witnessed across basically all use cases under all evaluation metrics while the acceleration is just marginal. Besides, the measure of computational costs should cover more aspects in addition to just time, which can be easily affected by complicated factors.

### Questions
Considering the aforementioned strengths and weaknesses, I tend to give a reject as the initial rating. The authors are also encouraged to refer to the weaknesses for rebuttal.
- I personally consider the effectiveness of MAG can be explained intuitively by dictionary learning. The $W$ can be seem as a learnable dictionary to model a sparse mapping from $x$ to the next layer. Can the authors provide more insights towards the mechanism of MAG? Also, is there any potential connection between MAG and separable convolution which decouples channels from tensors.
- Zip-NeRF is known for its large memory consumption (referring to NeRF-baselines). Is it possible to reduce the massive overheads by applying MAG layers or the improvement can only be time-wise?
- How does the proposed method perform compared to common acceleration techniques? The aim of this question is to confirm the contribution of MAG is not trivial and not easily achieved by other simple operations.
- How does the MAG-inserted MLP converge? Will there be a different tendency compared to vanilla MLP?

### Soundness
3

### Presentation
2

### Contribution
2
