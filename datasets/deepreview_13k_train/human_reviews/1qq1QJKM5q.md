# More Experts Than Galaxies: Conditionally-Overlapping Experts with Biologically-Inspired Fixed Routing

- Decision: Accept
- Scores: 6, 8, 3

## Abstract
The evolution of biological neural systems has led to both modularity
and sparse coding, which  
enables efficiency in energy usage, and robustness across the diversity of tasks in the lifespan. In contrast, standard neural networks rely on dense, non-specialized architectures, where all model parameters are simultaneously updated to learn multiple tasks, leading to representation interference. Current sparse neural network approaches aim to alleviate this issue, but are often hindered by limitations such as 1) trainable gating functions that cause representation collapse; 2) non-overlapping experts that result in redundant computation and slow learning; and 3) reliance on explicit input or task IDs that impose significant constraints on flexibility and scalability.
In this paper we propose Conditionally Overlapping Mixture of ExperTs (COMET), a general deep learning method that addresses these challenges by inducing a modular, sparse architecture with an exponential number of overlapping experts. COMET replaces the trainable gating function used in Sparse Mixture of Experts with a fixed, biologically inspired random projection applied to individual input representations. This design causes the degree of expert overlap to depend on input similarity, so that similar inputs tend to share more parameters. This facilitates positive knowledge transfer, resulting in faster learning and improved generalization. 
We demonstrate the effectiveness of COMET on a range of tasks, including image classification, language modeling, and regression, using several popular deep learning architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Conditionally Overlapping Mixture of ExperTs (COMET).
COMET uses biologically inspired, fixed random projections to generate binary masks that define subnetworks know as 'experts'.
The mask generation process is input-dependent, causing similar inputs to activate overlapping sets of experts.
The authors test the models on a range of benchmark tasks, finding that COMET performs well, particularly for large model sizes.

### Strengths
The paper is well written and the core idea is explained clearly. 

The authors demonstrate key properties of the COMET model, notably showing that similar inputs tend to activate overlapping experts, facilitated by the fixed gating mechanism.

The model is tested on a wide selection of benchmark tasks including computer vision, language modelling, and regression. 

The authors demonstrate the benefit of using COMET, particularly at large model sizes.

The use of COMET requires no additional trainable parameters which is quite advantageous.

### Weaknesses
In other works these gating functions can help alleviate catastrophic forgetting for tasks that are presented sequentially, but this is something that has not been tested in this paper. 

Given that previous work has similarly employed networks to determine gating, I am not entirely convinced that the novelty here is sufficient. However, I acknowledge that unlike prior approaches, which relied on trainable gates, this method uses fixed random projections.

There will be additional computational costs to using COMET but there is not an in-depth analysis of these costs in the paper. An analysis of training/inference times and GPU memory usage between COMET and the standard models would strengthen the submission.

### Questions
How does this model perform on a continual learning benchmark, such as permuted MNIST or split-CIFAR-100? 

What are the additional costs to using COMET in terms of training time and memory usage?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces COMET (Conditionally Overlapping Mixture of ExperTs), a new method for creating sparse neural networks. The authors show using fixed, biologically-inspired routing can create more efficient and effective neural networks, particularly for larger models, while avoiding common problems in sparse architectures like representation collapse and poor knowledge transfer. The key insight is that COMET creates input-dependent sparsity without needing to learn the routing mechanism. COMET uses a fixed, biologically-inspired random projection combined with a k-winner-take-all operation to route inputs through the network, rather than using trainable gating functions.

### Strengths
Unlike other methods, the proposed COMET method has no trainable gating functions (unlike standard Mixture of Experts) and avoids representation collapse.

Does not require explicit input/task IDs or pre-defined expert specialization.

Works across multiple architectures (MLPs, ViTs, GPT, MLP-Mixers).

The work is particularly similar to \cite{cheung2019superposition}, especially with the use of a random projection matrix V to handle the decision to mask. The justifications for using random projections in \cite{cheung2019superposition} seem to align well with the described capacity benefits of the COMET method in larger networks as compared to smaller networks. In particular, with a larger number of neurons, the probability of interference between masks rapidly decreases.

@article{cheung2019superposition,
  title={Superposition of many models into one},
  author={Cheung, Brian and Terekhov, Alexander and Chen, Yubei and Agrawal, Pulkit and Olshausen, Bruno},
  journal={Advances in neural information processing systems},
  volume={32},
  year={2019}
}

### Weaknesses
The arguments for the number of experts is based on the possible permutations of masks that can be created which gives an unrealistically large number of possible experts. But this does not account for interference issues and establishing a bound more grounded in reality would be very helpful. The theory work in \cite{cheung2019superposition} should help better define these bounds.

There's a claim of "improved generalization through enhanced forward transfer", but it's unclear what experiments in this paper demonstrates better transfer learning.

Figure 4 shows a strange result where the smaller_model performs consistently as well as the standard_model even for fairly low p_k values. It's unclear to me why there would be a benefit for COMET if at the neurons=3000, the smaller_network at pk=.1 will perform as well as the standard_model.  What is being gained here?

Is there any reason to believe this phenomenon does not already occur in large networks? \cite{elhage2022toy} describe a situation where neural networks encode the phenomenon observed in \cite{cheung2019superposition} during the course of training. Are there advantages of explicitly creating the superposition?

### Questions
Is there any reason to believe this phenomenon does not already occur in large networks? \cite{elhage2022toy} describe a situation where neural networks encode the phenomenon observed in \cite{cheung2019superposition} during the course of training. Are there advantages of explicitly creating the superposition?

Figure 4 shows a strange result where the smaller_model performs consistently as well as the standard_model even for fairly low p_k values. It's unclear to me why there would be a benefit for COMET if at the neurons=3000, the smaller_network at pk=.1 will perform as well as the standard_model.  What is being gained here?

@article{elhage2022toy,
  title={Toy models of superposition},
  author={Elhage, Nelson and Hume, Tristan and Olsson, Catherine and Schiefer, Nicholas and Henighan, Tom and Kravec, Shauna and Hatfield-Dodds, Zac and Lasenby, Robert and Drain, Dawn and Chen, Carol and others},
  journal={arXiv preprint arXiv:2209.10652},
  year={2022}
}

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper, titled Conditionally Overlapping Mixture of Experts (COMET), proposes a method aimed at overcoming limitations in existing sparse neural network architectures. COMET introduces a modular, sparse structure with a biologically inspired fixed routing approach that eliminates the need for task IDs and trainable gating functions, commonly associated with representation collapse and redundancy. Instead, the authors implement a k-winner-take-all cap operation, enabling experts to overlap based on input similarity. This approach aims to improve generalization and facilitate faster learning, validated across various tasks and architectures, including MLPs, Vision Transformers, and GPT-based models.

### Strengths
1. COMET presents a novel routing method that replaces trainable gating functions with fixed, biologically inspired routing, which is rare in modular neural network approaches.

2. The proposed method is tested across diverse architectures and tasks, such as image classification, language modeling, and regression, suggesting versatility.

### Weaknesses
1. Section 3 lacks crucial methodological details necessary for a complete understanding of the proposed COMET approach. For instance, it is unclear which specific design elements in COMET were directly influenced by the concept of biological random projections. Specifically, the paper does not clearly articulate how the fixed random projections are generated, what their dimensionality is relative to the input and expert dimensions, and how the k-winner-take-all operation is applied in conjunction with these projections. The lack of clarity around these implementation details makes it difficult to assess the novelty and potential impact of the approach.

2. The paper’s writing lacks clarity, making it difficult to fully understand the design of COMET. I recommend including a preliminary section that outlines the foundational Mixture of Experts (MoE) framework, followed by a clear discussion on how COMET’s design diverges from and improves upon existing methods. The current presentation assumes a level of familiarity with MoE that may not be universal, and it does not adequately highlight the specific innovations of COMET in relation to existing sparse activation techniques. A more detailed explanation of how COMET addresses the limitations of standard MoE architectures, such as representation collapse and redundancy, would be beneficial.

3. While COMET is designed to improve modularity and interpretability, the authors do not demonstrate how the model’s interpretability has improved. More extensive interpretability metrics or qualitative evaluations would support the claimed benefits of COMET. The paper claims that the fixed routing mechanism enhances interpretability, but it does not provide any empirical evidence to support this claim. For example, the authors could have analyzed the activation patterns of different experts for various inputs to demonstrate how the model’s modular structure leads to more interpretable representations. Without such analysis, the claim of improved interpretability remains unsubstantiated.

4. The absence of code and essential implementation details significantly hampers reproducibility and raises concerns about the robustness of the results. The paper lacks crucial details such as the specific activation functions used, the initialization strategies for the random projections, and the precise implementation of the k-winner-take-all operation. This lack of transparency makes it difficult for other researchers to replicate the findings and validate the claims made in the paper.

### Questions
1. Which components of COMET are inspired by the concept of biological random projection?

2. How should the hyperparameter $k$ in Equation (3) be determined?

### Soundness
2

### Presentation
2

### Contribution
2
