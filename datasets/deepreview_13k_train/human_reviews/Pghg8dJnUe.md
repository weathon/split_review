# Random Feature Models with Learnable Activation Functions

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Current random feature models typically rely on fixed activation functions, limiting their ability to capture diverse patterns in data. To address this, we introduce the Random Feature model with Learnable Activation Functions (RFLAF), a novel model that significantly enhances the expressivity and interpretability of traditional random feature (RF) models. We begin by studying the RF model with a single radial basis function, where we discover a new kernel and provide the first theoretical analysis on it. By integrating the basis functions with learnable weights, we show that RFLAF can represent a broad class of random feature models whose activation functions belong in $C_c(\mathbb{R})$. Theoretically, we prove that the model requires only about twice the parameter number compared to a traditional RF model to achieve the significant leap in expressivity. Experimentally, RFLAF demonstrates two key advantages: (1) it performs better across various tasks compared to traditional RF model with the same number of parameters, and (2) the optimized weights offer interpretability, as the learned activation function can be directly inferred from these weights. Our model paves the way for developing more expressive and interpretable frameworks within random feature models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose the Random Feature Model with Learnable Activation Functions (RFLAF), a generalization of traditional random feature models. In RFLAF, the activation function is represented as a linear combination of radial basis functions (RBFs) with learnable weights, allowing the model to approximate arbitrary activation functions. The authors provide a closed-form kernel analysis for the case when the activation set consists of a single RBF, and they extend the theoretical analysis to scenarios with multiple RBFs. Experimental results on synthetic datasets demonstrate that RFLAF outperforms random feature models with fixed activation functions.

### Strengths
1. Generalization of Random Feature Models: The authors extend traditional random feature models by introducing learnable activation functions, increasing the model’s expressivity and flexibility.
2. Rigorous Mathematical Foundations: The paper provides a thorough theoretical analysis, including derivations of new kernels and bounds on approximation and generalization, which strengthens the model’s credibility.
3. Clear and Accessible Writing: The paper is well-written, with a logical structure and clear explanations that make complex concepts accessible to readers.

### Weaknesses
1. Lack of General Closed-Form Solution: While the introduction critiques spline-based models for lacking closed-form analytical kernels (see line 041-046 ), this paper also lacks a closed-form kernel for cases with multiple basis functions. The paper's claim that splines preclude closed-form analysis is not a sufficient distinction, as the proposed method also relies on numerical optimization (Adam) for learning the RBF weights, indicating an absence of a general closed-form solution in practical application. The theoretical analysis, while rigorous for a single RBF, does not extend to the more general case, limiting the practical applicability of the theoretical results.

2. Limited Experimental Validation: The model is tested only on synthetic data, with target functions that closely align with the proposed model’s structure. This limited evaluation raises significant questions about RFLAF’s applicability to real-world scenarios. The synthetic datasets used appear to be specifically designed to favor the RFLAF model, making it difficult to assess its performance on more complex, real-world data distributions. Validation on more practical datasets, such as tabular data or image classification tasks, is crucial to demonstrate the model's robustness and generalizability.

3. Insufficient Exploration of Expressivity and Interpretability: The paper briefly mentions enhanced expressivity and interpretability as benefits of the proposed model, but it does not adequately demonstrate these gains. The interpretability results presented are limited to synthetic data and do not show how the learned activation functions provide insights into real-world data. The paper needs to provide concrete examples of how the learned activation functions enhance interpretability compared to standard random feature models, especially on complex datasets. Without such examples, the claims of improved interpretability remain unsubstantiated.

### Questions
See weaknesses.

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
The paper presents an algorithm for learning activation functions in random feature map representations for neural network models. The authors demonstrate that their learnable variants outperform "static" counterparts, applying fixed nonlinear maps. They also provide theoretical analysis of some of the new random feature map mechanisms they introduce in the paper (Sec. 3: RANDOM FEATURE MODELS WITH A SINGLE RADIAL BASIS FUNCTION). Furthermore, the Authors show that the mechanisms introduced by them needs about twice the parameter number compared to a traditional RF model for substantial quality improvements.

### Strengths
- detailed theoretical analysis of the model with a single radial basis function
- an elegant extension of the regular non-learnable random feature map mechanism
- generalization bounds and sample complexity of learning make the theoretical section even more complete

### Weaknesses
There are several issues I am concerned about:

1. The paper in general is not very well written. The paper talks about learnable random feature map representations, but from reading the experimental section it is not clear whether the conducted experiments are for MLP layers or activation functions in the linear low-rank attention mechanisms for Transformers (that are mentioned in the related-work part). If the latter is true, I am confused why the comparison does not include also positive random feature map mechanisms that are applied to unbiasedly approximate softmax kernel. The mention of low-rank linear attention and softmax kernel in the related work section (l.82) further exacerbates this confusion, as it suggests a connection to attention mechanisms that is not clearly addressed in the experimental setup.

2. The idea of the learnable random feature map representation is not new. In fact, there is a vast literature on positive random feature map mechanisms for the unbiased estimation of the softmax kernel and the most general of those mechanisms do indeed have learnable parameters.

3. The experimental section is very compact. It is really hard to draw any far-reaching conclusions regarding the performance of the method, based on the presented results. Besides, as mentioned above, they are poorly reported. The lack of large-scale experiments, particularly on tasks relevant to the broader community, is a significant concern. The absence of experiments with Transformer models, which could greatly benefit from novel random feature mechanisms, is a missed opportunity.

4. The Authors claim that the mechanisms presented by them introduces about twice the parameter number compared to a traditional RF model for substantial quality gains. This is actually a lot. In the paper it is not reported how this affects speed of training and inference. It is also not clear whether the comparison in the experimental section is with the models of approximately the same of two times smaller number of parameters.

### Questions
1. Is the main experimental testbed set up in the attention or MLP setting ?
2. What is the impact on speed of inference and training of the newly introduced parameters ?
3. Can the Authors conduct comprehesive experiments with their models in the attention setting, including also various positive random feature map mechanisms for the unbiased softmax kernel estimation (also the variations with learnable parameters) ?

### Soundness
3

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
This paper proposes a class of random feature models with activation functions formed by trainable superpositions of radial basis functions.

### Strengths
The paper is clearly written, and the mathematics appears correct (though mostly consisting of slight extensions of standard results). However, as I detail below under *Weaknesses*, I'm struggling to muster much enthusiasm for this paper because I think it fails to answer the central question of why one would use these models rather than a standard MLP.

### Weaknesses
As mentioned above, I have one major concern with this paper, which overshadows everything else. I will thus be brief. In its current form, the manuscript does not provide any compelling reason why one would use the proposed class of RF models with adaptive activation functions rather than just training the weights (i.e., using an MLP). The experiments provide no comparison against an MLP baseline, and I'm not convinced by the authors' argument that their models will be more interpretable. To understand the nature of signal processing by these networks, one must understand the filtering properties of the random weights as well as the activation function. The theoretical results do not outweigh these concerns, as they are mostly minor modifications of standard RF model analyses. Specifically, the theoretical contributions lack depth, as they do not address the crucial question of how the trainable activation functions interact with the random features to influence the model's inductive bias. The analysis is limited to standard generalization bounds, without exploring the more nuanced aspects of the interplay between the learned activation parameters and the fixed random weights. Without any clear comparison to an ordinary neural network, and without a more compelling theoretical justification, this is for me a clear reject, without further critique required.

### Questions
- The discussion after Theorem 5.1 mentions the question of tightness of the bounds on the number of features required in Rudi & Rosasco; the authors might find the corresponding commentary in https://arxiv.org/abs/2405.15699 to be of interest.

### Soundness
2

### Presentation
3

### Contribution
2
