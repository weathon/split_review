# Riemannian Optimization for Hyperbolic Prototypical Networks

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
This paper addresses the utilization of hyperbolic geometry within a Prototype Learning framework. Specifically, we introduce Riemannian optimization for Hyperbolic Prototypical Networks (RHPN), a novel approach that leverages Prototype Learning on Riemannian manifolds applied to the Poincare' ball. RHPN capitalizes on the efficiency and effectiveness of updating prototypes during training, coupled with a regularization term crucial to boost the performances. We set up an extensive experimentation that shows that RHPN is able to outperform the state-of-the-art in Prototype Learning, both in low and high dimensions, extending the impact of hyperbolic spaces to a wider range of scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Riemannian Hyperbolic Prototypical Networks for Prototype Learning. The method optimizes prototypes on Riemannian manifolds, specifically the Poincaré ball, leveraging hyperbolic geometry. The approach improves Prototype Learning by dynamically updating prototypes during training and incorporating a regularization term for embedding norms. Experimental results show the effectiveness of the proposed method.

### Strengths
1. Applying Riemannian optimization in hyperbolic spaces to prototype learning is interesting.

2. Experiments on various datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
1. More intuitive explanations for the methodology and mathematical concepts are needed for better accessibility.

2. The Riemannian optimization may add extra computational complexity to the model. which is better to also be investigated and discussed in the paper.

3. The slope parameter $\lambda$ plays a significant role, but its tuning can be complex, as demonstrated by the need for separate tuning across different datasets.

### Questions
I'm also curious about whether the method can and how the method performs on few-shot learning, where the prototype-based method is more commonly used.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Riemannian Optimization for Hyperbolic Prototypical Networks (RHPN), a novel approach that leverages hyperbolic geometry within a Prototype Learning framework.  Specifically, RHPN uses Riemannian optimization on the Poincaré ball to update prototypes during training, enhancing performance with a regularization term. Extensive experiments demonstrate RHPN's superiority over state-of-the-art methods in Prototype Learning across various dimensions.

### Strengths
1. The paper introduces the RHPN, a method that leverages the Poincaré ball model of hyperbolic geometry to dynamically update prototypes during training for enhances prototype learning. 

2. The paper provides a comprehensive experimental evaluation, demonstrating the effectiveness of RHPN across multiple datasets and embedding dimensions. The analysis of δ-hyperbolicity of the learned embeddings contributes to the understanding of how hyperbolic geometries align with the intrinsic structure of data, offering valuable insights into the geometric properties of the representations.

3. The framework's flexibility to be extended to other geometries is a significant strength, indicating the potential for future research and applications in diverse domains where different hyperbolic geometries might be more suitable.

### Weaknesses
1.This work aims to construct a prototype learning framework on generic Riemannian manifolds, with a particular emphasis on embedding prototype representations as network parameters within the Poincaré ball model. However, the paper's main contribution remains somewhat obscured. Although the related works section acknowledges existing studies on prototype learning in hyperbolic manifolds, the paper's unique focus on the application to image classification tasks, as highlighted on lines 049 and 119, is not clearly articulated, which diminishes the perceived novelty of the research. The specific novelty of applying Riemannian optimization for prototype updates within the Poincaré ball for image classification, as opposed to other applications or optimization methods, needs to be more explicitly defined.

2.The description of vanishing gradient problem in Riemannian SGD could be more explicit and comprehensive. It would significantly enhance the paper if the authors could provide a clearer illustration of this issue in Figure 3. The paper should detail how the geometry of the Poincaré ball contributes to this vanishing gradient issue, specifically how the curvature and the distance metric affect the gradient magnitudes as embeddings move towards the boundary of the ball. A more detailed explanation of why standard Euclidean optimization techniques are insufficient in this context is needed.


3.The discussion on the choice of hyperparameters, particularly the slope parameter , could be more detailed. It is noted that Figure 4(a) and Figure 4(b) illustrate a significant performance variance based on the value of 𝜆, especially when comparing high and low embedding dimensions. Clarifying the reasons behind these performance fluctuations would provide deeper insights into the sensitivity of the model to 𝜆. Furthermore, there seems to be the model collapse during training for 𝜆=0.1 and 𝜆=0.3 as depicted in Figure 4(b) is concerning. The paper should provide a more thorough analysis of the impact of different values of 𝜆 on the optimization process and the resulting prototype embeddings, including a discussion on why certain values lead to model collapse.


4.The experimental results among datasets indicate an improvement in performance for the image classification task with increasing embedding dimensions. This trend is intriguing and warrants further exploration. Are there any potential bottlenecks or limitations associated with this observation? The paper should discuss whether this trend is expected based on theoretical properties of hyperbolic embeddings or if it is an empirical observation. It would be beneficial to analyze the computational cost and memory requirements associated with increasing embedding dimensions, and whether there are diminishing returns in performance beyond a certain dimensionality.

### Questions
Please refer to the weaknesses.

### Soundness
2

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
4

### Summary
This paper performs hyperbolic prototype learning, where the prototypes are made learnable. Moreover, the method adds clipping and regularization to improve performance. The resulting method is compared on four image classification datasets against several other prototype-based methods. They find reasonable improvements over these methods.

### Strengths
The structuring of the paper is clear, with an easy to understand presentation of the method and the results. Moreover, the paper contains many visualizations of the training behaviour of the model for various settings. 

The comparison between learnable prototypes and fixed prototype methods are interesting to see.

### Weaknesses
My main concern is that the paper has limited novelty. While the paper is the first to perform hyperbolic prototype learning with learnable prototypes, this type of setting has been explored before in the usual Euclidean prototype learning setting as mentioned by the authors. Moreover, learnable prototypes can easily be optimized using Riemannian optimization, similar to any other parameter of a hyperbolic model. So, exploring learnable prototypes in hyperbolic learning does not require any technical contributions. The clipping and regularization that the method uses are also coming from other papers, so it seems to me that the paper introduces no new ideas and simply applies existing concepts. 

The comparison between the hyperbolic method and the Euclidean method does not seem completely fair to me. RHPN* uses regularization, whereas it seems that ECL does not use any regularization. As such, the fair comparison for assessing the importance of hyperbolic geometry would be between ECL and RHPN. Indeed, when considering this comparison, the hyperbolic solution is a lot less favorable, even being considerably worse on CUB for large embedding dimension. Based on this, I think the choice for hyperbolic geometry is not well motivated, especially considering the increase in computational complexity. Lastly, hyperbolic space is locally similar to Euclidean space, so if you add a term that pushes everything towards the origin, then that is making your representations less hyperbolic, which is another argument against using hyperbolic space.

### Questions
Hyperbolic geometry is usually beneficial compared to Euclidean geometry when there is a clear hierarchical structure present in the data. Could the method potentially be changed to incorporate hierarchical knowledge in the prototypes that aids in training a classifier for example? That would make the choice for hyperbolic geometry more obvious and, possibly, more impactful.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method for optimizing prototypes in Riemannian manifolds. In addition to the contrastive loss, the authors add a regular term to push the data points away from the boundary. They use the Riemannian SGD method to learn backbone parameters and prototypes. The authors also conduct experiments on image classification. tasks.

### Strengths
Strength:
1. Learning in hyperbolic spaces is a promising direction.
2. The experiments have shown the method's effectiveness on the four datasets.

### Weaknesses
Weakness:
1. For me, the novelty is limited. Learning prototypes in hyperbolic spaces is not novel, such as [a,b,c,d]. What is the contribution in this paper about prototype learning.

[a] Hyperbolic Image Embeddings
[b] Curvature generation in curved spaces for few-shot learning
[c] Curvature-adaptive meta-learning for fast adaptation to manifold data

2. The experiments are weak. This paper only evaluates the performance of four image classification tasks. Few-shot learning, incremental learning, and zero-shot learning are also used to evaluate the performance of methods in hyperbolic space [e,f,g].
[e] Exploring data geometry for continual learning
[f] Kernel Methods in Hyperbolic Spaces
[g] Clipped Hyperbolic Classifiers Are Super-Hyperbolic Classifiers

3. Since the work focuses on Riemannian optimization, some Riemannian optimization methods should be added to the related work, and the difference between them and this work should be claimed. In addition, the novelty of the Riemannian optimization should be claimed.

### Questions
1. The regular term is an important component in this method. However, its motivation and effectiveness are less explored.

### Soundness
2

### Presentation
3

### Contribution
1
