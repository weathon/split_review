# Optimal Brain Apoptosis

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
The increasing complexity and parameter count of Convolutional Neural Networks (CNNs) and Transformers pose challenges in terms of computational efficiency and resource demands. Pruning has been identified as an effective strategy to address these challenges by removing redundant elements such as neurons, channels, or connections, thereby enhancing computational efficiency without heavily compromising performance. This paper builds on the foundational work of Optimal Brain Damage (OBD) by advancing the methodology of parameter importance estimation using the Hessian matrix. Unlike previous approaches that rely on approximations, we introduce Optimal Brain Apoptosis (OBA), a novel pruning method that calculates the Hessian-vector product value directly for each parameter. By decomposing the Hessian matrix across network layers and identifying conditions under which inter-layer Hessian submatrices are non-zero, we propose a highly efficient technique for computing the second-order Taylor expansion of parameters. This approach allows for a more precise pruning process, particularly in the context of CNNs and Transformers, as validated in our experiments including VGG19, ResNet32, ResNet50, and ViT-B/16 on CIFAR10, CIFAR100 and Imagenet datasets. Our code will be available soon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Optimal Brain Apoptosis (OBA), which appears to be a novel pruning method for neural networks that builds upon the principles of Optimal Brain Damage (OBD), which date back to 1980s and 1990s. Recognizing the limitations of previous pruning methods, OBA leverages the full Hessian-vector product to compute the importance of each parameter in the network accurately, moving beyond previous methods that relied on approximations. The authors first analyze the conditions under which Hessian submatrices between layers are nonzero and develop an approach to calculate the second-order Taylor expansion for each parameter (enabling precise pruning in both structured and unstructured settings). Empirical tests demonstrate that OBA effectively reduces computational overhead while maintaining model accuracy. The authors acknowledge that while OBA works well for architectures like CNNs and Transformers, extending it to more complex models like RNNs or State Space Models will require further research.

### Strengths
- Unlike previous methods that approximate the Hessian matrix, OBA calculates the full Hessian-vector product, providing a more accurate measure of parameter importance and leading to more precise pruning.
- OBA supports both structured pruning (removing entire neurons, channels, or layers) and unstructured pruning (removing individual weights). It's compatible with a wide range of architectures.
- The approach optimizes the calculation of the Hessian-vector product (reduced computational complexity).
- Showing adaptability to widely-used architectures in deep learning.
- The authors provide a solid theoretical basis for their approach, with clear proofs.

### Weaknesses
 - It seems like calculating the full Hessian-vector product, even with optimizations, can still be computationally expensive for larger and more complex networks.
- Extending this method to newer architectures seems to require additional work. 
-The method was tested on a specific set of architectures, and its generalizability across a wider range of tasks or domains is yet to be fully established.
- The experiments make the paper feel somewhat outdated, as the evaluations and datasets used are reminiscent of those from 7-8 years ago.

### Questions
Please see the weaknesses section. Providing feedback on those comments during rebuttal will be appreciated.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a tractable way of computing the Hessian of the loss function in feed-forward networks. This finding is very interesting, as it may have a wide range of applications, in particular, the one of pruning CNNs and transformers. The results are very promising, as they show some improvements, but these improvements do not seem to be very large.

### Strengths
An interesting new method for computing the Hessian of the loss function in feed-forward networks in a tractable way.

### Weaknesses
The improvements in accuracy and speed do not seem overwhelming. While the method introduces a tractable way to compute the Hessian, the practical gains in terms of model performance are not consistently significant across all experiments. Specifically, the reported improvements in accuracy, while present, are not substantial enough to clearly demonstrate a major advantage over existing methods. The gains in speed, similarly, do not seem to be transformative, raising questions about the overall practical impact of the proposed approach. The method's effectiveness appears to vary across different network architectures and pruning scenarios, indicating a potential sensitivity to specific configurations.

### Questions
Considering that recurrent neural networks use back-propagation through time, for a given time window, how tractable would be to extend your method to such networks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose a new method for neural network pruning called Optimal Brain Apoptosis (OBA) inspired by the prior work Optimal Brain Damage (Lecun et al., 1989). This method calculates the Hessian-vector product for each parameter and identify the conditions under which inter-layer Hessian submatrices are non-zero. The proposed method is able to prune models to increase model efficiency on 3 convolutional backbones and one vision transformers backbone on CIFAR10, CIFAR100 and ImageNet datasets.

### Strengths
1.	Pruning performance looks fairly promising. The method achieves consistent improvement on various datasets, using the most commonly-used backbones (ResNet and ViT), and on unstructured vs structured pruning.
2.	The results shown are quite comprehensive: pruning performance (accuracy, parameter reduction, FLOPs reduction, throughput increase), pruning cost (training and pruning time). Surprisingly, the pruning cost was not as high as I originally expected knowing that the method involves computation of the Hessian-vector product.

### Weaknesses
1.	Since pruning is not my area of expertise, I am unsure whether the authors used fair baselines for comparison. The proposed method is mainly compared against 7 methods from 3 papers, respectively in 2016, 2017 and 2019. A simple literature search gave me a few methods that claim to have achieved better pruning performances and are fairly well cited and fairly highly stared: https://arxiv.org/abs/2203.04248, https://arxiv.org/abs/2208.11580, https://arxiv.org/abs/2210.04092, https://arxiv.org/abs/2112.00029. I would encourage the authors to either compare to some of the latest works, or provide a justification on not considering these more recent works --- meanwhile, I would resort to reviewers with more experience in pruning on their opinions regarding this matter.

### Questions
1.	Please refer to Weakness 1.
2.	Minor suggestion. For LaTeX notations, the subscripts (especially subscripts of superscripts) can be wrapped in text format. What I mean is instead of $\mathbb{R}^{l_out}$, using $\mathbb{R}^{l_\textrm{out}}$ might give you a better looking symbol.
3.	What do a, b, c, d, e respectively mean in Equation 3? Could the authors define them or point to the text where they are defined?

### Soundness
3

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
4

### Summary
The paper concerns the importance of pruning to reduce computational burden of neural network inference. The structure of the Hessian matrix is analysed with a productive derivation of structure for  feedforward nets with so-called series and parallel connectivity. Empirical results are presented for standard (vision) CNNs.

### Strengths
The paper’s most prominent strength is the set of Hessian structures derived for series and parallel connectivity. The empirical results are promising showing significant reductions in FLOPS for virtually unchanged performance.

### Weaknesses
1) The field is very busy with many results going back to the early 90s. Computational results and simplifying structure of the Hessian for feedforward network are found in many papers including
•	Wille, J., 1997, June. On the structure of the Hessian matrix in feedforward networks and second derivative methods. In Proceedings of International Conference on Neural Networks (ICNN'97) (Vol. 3, pp. 1851-1855). IEEE.
•	Buntine, W.L. and Weigend, A.S., 1994. Computing second derivatives in feed-forward networks: A review. IEEE transactions on Neural Networks, 5(3), pp.480-488.
•	Wu, Y., Zhu, X., Wu, C., Wang, A. and Ge, R., 2020. Dissecting hessian: Understanding common structure of hessian in neural networks. arXiv preprint arXiv:2010.04261
•	Singh, S.P., Bachmann, G. and Hofmann, T., 2021. Analytic insights into structure and rank of neural network hessian maps. Advances in Neural Information Processing Systems, 34, pp.23914-23927.

The paper presents a reduced complexity calculation of Hessian x vector, this is well-known - see work by Barak Pearlmutter for example; Pearlmutter, B.A., 1994. Fast exact multiplication by the Hessian. Neural computation, 6(1), pp.147-160.

•	In general the context of related work is not sufficient. I am not a fan of placing context related work in an appendix.

2) The paper does not adequately address the first-order term in the Taylor expansion used for pruning. While the authors align with prior Hessian-based methods by omitting this term, the justification for doing so is weak, especially when considering that networks are rarely trained to a perfect minimum. This omission introduces a potential uncontrolled error, particularly when using SGD-based training methods where the first-order term may not be negligible. The authors should provide a more robust argument for neglecting this term, or ideally, include it in their importance calculation for greater rigor.

3) L058-9 The description of the OBS method is inaccurate. OBS does not discard second-order derivative information, but rather approximates it using the Fisher information matrix. This distinction is important and should be corrected to accurately represent the method.

4) L095 The claim that the Gauss-Newton approximation is insufficient lacks supporting evidence. The authors need to provide a more detailed explanation of why this approximation is inadequate for their specific application, potentially including empirical comparisons or theoretical justifications.


### Questions
1)	Empirical evidence: While the results for CNNs are impressive, please consider transformers. There is much interest in pruning and redundancy in transformers e.g.  
a.	Men, X., Xu, M., Zhang, Q., Wang, B., Lin, H., Lu, Y., Han, X. and Chen, W., 2024. Shortgpt: Layers in large language models are more redundant than you expect. arXiv preprint arXiv:2403.03853.
b.	Lad, V., Gurnee, W. and Tegmark, M., 2024. The Remarkable Robustness of LLMs: Stages of Inference?. arXiv preprint arXiv:2406.19384.

2)	L652 Consider setting the scene, motivation and related work as an integral part of the paper. With due refence to early work on pruning and Hessian structure

3)	L058-9 The OBS method is only different from OBD when the non-diagonal Hessian is used, i.e they do not ignore the off-diagonal terms in OBS

4)	L095 You mention that the Gauss.Newton approximation is in-sufficient what is the evidence?

5)	L087 Do you keep track of the first order term (which is assumed zero in OBD/OBS)?

### Soundness
3

### Presentation
2

### Contribution
2
