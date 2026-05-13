# DPaI: Differentiable Pruning at Initialization with Node-Path Balance Principle

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Pruning at Initialization (PaI) is a technique in neural network optimization characterized by the proactive elimination of weights before the network's training on designated tasks. This innovative strategy potentially reduces the costs for training and inference, significantly advancing computational efficiency. A key element of PaI's effectiveness is that it considers the significance of weights in an untrained network. It prioritizes the trainability and optimization potential of the pruned subnetworks. Recent methods can effectively prevent the formation of hard-to-optimize networks, e.g. through iterative adjustments at each network layer. However, this way often results in *large-scale discrete optimization problems*, which could make PaI further challenging. This paper introduces a novel method, called *DPaI*, that involves a differentiable optimization of the pruning mask. DPaI adopts a dynamic and adaptable pruning process, allowing easier optimisation processes and better solutions. More importantly, our differentiable formulation enables readily use of the existing rich body of efficient gradient-based methods for PaI. Our empirical results demonstrate that DPaI significantly outperforms current state-of-the-art PaI methods on various architectures, such as Convolutional Neural Networks and Vision-Transformers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DPaI (Differentiable Pruning at Initialization), a novel method for pruning neural networks at initialization using the Node-Path Balancing (NPB) principle. Unlike traditional methods, DPaI applies a differentiable approach to optimize pruning masks, enabling efficient gradient-based optimization of sparse networks without needing training data. By balancing the number of effective nodes and paths, DPaI maintains information flow in sparse networks, achieving superior accuracy at high sparsity levels. Experimental results show that DPaI outperforms state-of-the-art methods across various network architectures and datasets, including CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1K. DPaI also achieves lower pruning time and reduced FLOPs, demonstrating its efficiency and practical applicability.

### Strengths
1. Differentiable Optimization: DPaI introduces a differentiable approach, making pruning more efficient and compatible with standard neural network training, unlike discrete, layer-wise pruning methods.
2. High Performance at Extreme Sparsity: By balancing effective nodes and paths, DPaI maintains high accuracy even at sparsity levels of 96-99%, outperforming traditional methods.
3. Architecture-Agnostic: DPaI works effectively across different architectures, such as ResNet, VGG, and EfficientNet, making it broadly applicable.
4. Reduced Pruning Time and FLOPs: DPaI achieves low pruning times and significantly reduces FLOPs, enhancing computational efficiency compared to other methods.

### Weaknesses
1. Hyperparameter Sensitivity: I assume DPaI’s performance will depend on hyperparameters which may require tuning for different datasets and sparsity levels, as this usually happens to pruning at initialization methods.
2. Implementation Complexity: DPaI involves complex gradient calculations and differentiable mask updates, which may be harder to apply to different task or models.

### Questions
I currently hold a positive view of this work, but I’m somewhat lacking the sense of recent progress about pruning at initialization. I believe the most critical aspect is comparing it with other works in the same track, so I may further adjust my review after considering feedback from other reviewers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper extends Node-path Balancing Principle (NBP) into differentiable formulation by the learnable masks. To solve the gradient flow problem of top-k operation, authors introduce the Straight-Through Estimator (STE) technique during mask updating, while using Erdo ̋s-Rényi Kernel (ERK) technique to determine the layer-wise sparsity ratios.

### Strengths
1. The differentiable NPB formulation achieves competitive performance compared to previous Pruning at Initialization (PaI) methods.
2. The proposed method can be easily integrated into the previous gradient-based methods.

### Weaknesses
1. This paper employs methods that are well-established in prior works, such as the top-k operation with Straight Through Estimator (STE) [1, 2, 3], and the Erdős-Rényi Kernel (ERK) technique[4]. Although the differentiable masks have not been previously applied in the PaI domain, many methods[1, 2, 3, 5, 6] in pruning during/post training methods have used the differentiable masks for model compression. I suggest the authors provide a detailed discussion regarding the difference.

2. This paper uses the tanh activation function for the mask in the top-k with STE method, particularly when sigmoid and its variants are more commonly employed in previous works[1, 2, 3]. Therefore, what is the rationality of the tanh function. 

3. The models and datasets employed in the paper are predominantly small-scale validations. How does the method proposed in this paper perform on larger-scale models and datasets, such as experiments using Resnet-50 on ImageNet-1k?

4. In Fig.3, why does the proposed pruning method in the paper take more time in the Resnet20 on CIFAR-10 experiments compared to other methods, while it takes less time in the Resnet18 on Tiny-ImageNet and VGG19 on CIFAR-100 experiments? 

5. I suggest including a brief introduction or citation for the abbreviations of previous methods used in this paper, as relying solely on abbreviations from related work can reduce the readability of the paper for readers who are not fully familiar with PaI-related research.

[1] Disentangled Differentiable Network Pruning.
[2] Growing Efficient Deep Networks by Structured Continuous Sparsification.
[3] Learning sparse neural networks through l_0 regularization.
[4] The unreasonable effectiveness of random pruning: Return of the most naive baseline for sparse training.
[5] Filter Pruning for Efficient CNNs via Knowledge-driven Differential Filter Sampler.
[6] Convolutional Networks with Adaptive Inference Graphs.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
(+) The authors propose a novel pruning method referred to as Differentiable Pruning at Initialization (DPaI), which involves differentiable optimization of the pruning mask. DPaI adopts a dynamic and adaptable pruning process, allowing easier optimization processes and better solutions. 

(+) DPaI’s differentiable formulation enables easy use of the gradient-based methods for Pruning at Initialization (PaI). 

(+) The empirical results demonstrate that DPaI significantly outperforms current state-of-the-art PaI methods on various architectures, including Convolutional Neural  Networks (CNN) and Vision-Transformers (ViT).

### Strengths
(+) The author analyzes the interpretations of the proposed method (DPaI) and proves its behavior using convergence theory.

Please see the strength of the paper in summarization further.

### Weaknesses
(-) It isn't easy to follow how the proposed method (DPaI) finds the best nodes and paths using only an importance score. 

Through extensive ablation studies on the update rule (line 8) stated in Algorithm 1, the authors should show the effectiveness: the importance of nodes and paths seems to depend only on score s_{i,j}. The empirical observations (small neural networks) with the ablation studies help us understand the contributions of the proposed method, DPaI, and the convergence theory. 

(-) What about pre-trained model-based DPaI performances of ViT?

### Questions
Please see the above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Update:
Thanks for the authors' feedback. My concerns have been fully addressed.

----- original review -----
The authors propose a novel differentiable algorithm for deep network pruning at initialization. The key idea of the algorithm is to optimize the number of effective paths and nodes while pruning the network parameters. The non-differentiable issue can be addressed by Straight-Through Estimator. The authors demonstrate the superiority of the proposed method on several popular benchmark datasets.

### Strengths
The proposed algorithm presents a novel approach to Node-Path Balancing in network pruning. It distinguishes itself by incorporating this methodology into a differentiable framework. Additionally, the article provides extensive numerical results for various vision tasks and includes detailed ablation studies, offering readers valuable insights into the performance of the proposed algorithm under different conditions. Furthermore, the authors provide some convergence analysis, which can be useful for those interested in understanding the underlying principles of the method.

### Weaknesses
* The experiments are mostly for vision models. It would be nice to see some LLM experiments. For exmaple, how does the method perform on Llama-3.2-90B?
*  It is unclear why choosing logarithm in maximizing NPB principle. For example, why not using square root or other functions? Please suggest the theoretical support of this choice, and conduct numerical ablation studies to verify the optimality of this design. A possible approach is to make this loss function learnable, then find an optimized loss function on a set of small datasets, finally generalize to larger datasets.

* Using STE to convert non-differentiable optimization to differentiable one has been proposed in many previous works. Please justify the novelty of this approach when appling STE to this work. Any special adaptation to make STE more efficient / robust in this problem?

### Questions
* Why choosing logarithm in NPB principle? Is logarithm loss an optimal design in this problem?
* Is the method applicable to LLM? How it performs on popular LLMs such as Llama-3.2 families?
* Why using STE while there are several possible methods to relax the differentiable issue? For example the popular [0,1] + L1 norm relaxation seems a good choice too.

### Soundness
3

### Presentation
3

### Contribution
3
