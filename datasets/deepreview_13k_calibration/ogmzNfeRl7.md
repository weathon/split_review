# Correlations Are Ruining Your Gradient Descent

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 3, 5

## Abstract
Herein the topics of (natural) gradient descent, data decorrelation, and approximate methods for backpropagation are brought into a common discussion.
  Natural gradient descent illuminates how gradient vectors, pointing at directions of steepest descent, can be improved by considering the local curvature of loss landscapes.
  We extend this perspective and show that to fully solve the problem illuminated by natural gradients in neural networks, one must recognise that correlations in the data at any linear transformation, including node responses at every layer of a neural network, cause a non-orthonormal relationship between the model's parameters.
  To solve this requires a method for decorrelating inputs at each individual layer of a neural network.
  We describe a range of methods which have been proposed for decorrelation and whitening of node output, and expand on these to provide a novel method specifically useful for distributed computing and computational neuroscience.
  Implementing decorrelation within multi-layer neural networks, we can show that not only is training via backpropagation sped up significantly but also existing approximations of backpropagation, which have failed catastrophically in the past, benefit significantly in their accuracy and convergence speed.
  This has the potential to provide a route forward for approximate gradient descent methods which have previously been discarded, training approaches for analogue and neuromorphic hardware, and potentially insights as to the efficacy and utility of decorrelation processes in the brain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Starting from natural gradient descent, the authors show that correlations in data can cause non-orthonormal relationship between the model's parameters. To mitigate this, they propose a decorrelation mechanism that uses only local information. They demonstrate that this mechanism improves BP accuracy, but also notably improves results for alternate training methods such as feedback alignment, and node perturbation.

### Strengths
- The focus on the input correlation part of natural gradient descent is novel, as is the proposed decorrelation mechanism.
- The observation that this improves performance for BP alternatives is very significant, since these methods have the potential to be more efficient for training
- The narrative exposition was easy to follow, and the concepts are explained very clearly
- The (almost) empirical evaluation supports the conclusions of the paper
- connections to biology is interesting

### Weaknesses
 - The discussion of methods from computational neuroscience is very cursory, and would benefit from more details such as forms of specific learning rules. For example, the authors could elaborate on the specific biological plausibility of the decorrelation mechanism, such as how it relates to known neural processes like lateral inhibition or synaptic plasticity rules. A more detailed discussion of the biological underpinnings would strengthen the connection to neuroscience.
- The recurrence aspect of the decorrelation rule could be discussed in more depth in the main text. The authors should clarify the specific dynamics of the recurrent system, including the update equations and the conditions for convergence. It is unclear how the recurrent implementation affects the stability and speed of the decorrelation process. Furthermore, the relationship between the recurrent formulation and the single weight matrix multiplication should be made more explicit, including a discussion of the conditions under which they are equivalent.
- It's not clear if the proposed decorrelation method only has a recurrent formulation, or can be efficiently implemented without recurrence as well. The authors should provide a more detailed analysis of the computational cost of the decorrelation method, particularly in terms of memory and time complexity. This should include a comparison to standard backpropagation and other optimization methods. The practical implications of the quadratic increase in parameters for large networks should also be addressed.
- There are second order methods which seem to have gotten some traction such as shampoo [1, 3] and K-FAC [2]. The statement in the first paragraph against 2nd order methods needs more nuance. The authors should clarify the specific limitations of existing second-order methods that their approach aims to address, and how their method compares in terms of computational cost and performance.

### Questions
- What is the computational cost of the proposed decorrelation method?
-  What are the implications of having a recurrent formulation for computational efficiency and implementation?
- There are second order methods which seem to have gotten some traction such as shampoo [1, 3] and K-FAC [2]. The statement in the first paragraph against 2nd order methods needs more nuance.

[1] Vineet Gupta, Tomer Koren, and Yoram Singer. Shampoo: Preconditioned stochastic tensor optimization. In International Conference on Machine Learning, pp. 1842–1850. PMLR, 2018.
[2] Yi Ren and Donald Goldfarb. Tensor normal training for deep learning models. Advances in Neural Information Processing Systems, 34:26040–26052, 2021.
[3] Vyas, N., Morwani, D., Zhao, R., Shapira, I., Brandfonbrener, D., Janson, L., and Kakade, S. (2024). SOAP: Improving and Stabilizing Shampoo using Adam. Preprint at arXiv, https://doi.org/10.48550/arXiv.2409.11321 https://doi.org/10.48550/arXiv.2409.11321.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, the authors address the challenge of data correlations impacting neural activity and the learning process within neural networks. They take a comprehensive approach, beginning with an analysis that connects data correlations to the non-Euclidean geometry of the parameter space. Specifically, they demonstrate that correlations in input data lead to longer paths through parameter space during learning. This observation is rooted in the theory of Natural Gradient Descent, as originally developed by Amari in the late 90's, where parameter space is considered curved and defined locally by the inverse Fisher information matrix. The authors provide evidence that input correlations influence these longer paths.
Next, they propose an incremental learning rule capable of decorrelating inputs within each neural network layer. This rule facilitates a linear transformation to reduce input correlations progressively. The authors demonstrate that employing such a decorrelation mechanism accelerates learning and potentially improves generalization across several learning paradigms, including standard backpropagation, Node Perturbation, and Feedback Alignment. The concluding part of the paper discusses the implications of removing correlations in biological and artificial settings.

### Strengths
• The initial sections of the paper provide an insightful overview of Natural Gradient Descent and offer a compelling perspective on how Amari’s theoretical framework can be contextualized within deep learning. While typical applications of Natural Gradients focus on Bayesian inference, where the Fisher information naturally defines the metric, the authors present an innovative interpretation that broadens its relevance.

• The simulations included in the study convincingly demonstrate that implementing decorrelation at each layer significantly enhances training efficiency, particularly within the Feedback Alignment framework.

• The paper offers a comprehensive overview of the impact of data correlations on training dynamics, which serves to enrich the reader’s understanding of this often underexplored aspect of deep learning optimization.

### Weaknesses
The primary issue with this paper is its limited coherence and lack of substantial innovation. The manuscript presents small incremental contributions across several topics and attempts to integrate them into a unified framework. This approach results in a paper that straddles the line between a review and an opinion piece, which does not align well with the expectations for an ICLR submission. Below, I outline the specific areas where the paper falls short in terms of novelty:
1. **Review of Natural Gradient Descent**: The first section provides a summary of Natural Gradient Descent, highlighting that input correlations can be inferred from the derivation of the metric tensor. However, this observation is neither surprising nor particularly useful, as it merely reiterates that input correlations are intrinsic to Natural Gradient theory. Moreover, the concept of learning dynamics in curved parameter spaces is not applied or built upon in subsequent sections, limiting the relevance of this part of the paper to the overall narrative.

2. **Derivation of a Local Learning Rule**: The second section presents a derivation for a local learning rule intended to decorrelate inputs to neural network layers. While the authors point out the novelty of their incremental rule (line 340), this rule closely resembles existing methods such as recursive least squares (e.g., Sussillo and Abbott, 2009), which also stem from the goal of decorrelating neural activity. The resemblance is even clearer when studying the derivation of the proposed decorrelation learning rule in Appendix C. Notably, the proposed rule introduces a novel scalar rescaling that maintains the norm. However, this addition is minor, and the overall innovation is minimal.

3. **Numerical Experiments on Layer-wise Decorrelation**: The third section includes numerical results showing the advantages of input decorrelation for training deep networks. Prior work has already demonstrated that input decorrelation accelerates learning in frameworks such as backpropagation and Node Perturbation. Consequently, the main novelty here is the improved performance observed in the Feedback Alignment framework. However, the paper does not provide sufficient explanation or analysis to elucidate why decorrelation significantly enhances Feedback Alignment, nor does the performance match standard backpropagation. This omission limits the impact of this result, rendering it another incremental contribution.

Collectively, these points suggest that the novelty presented in this work does not meet the standards expected for ICLR.

Finally, the discussion section of the paper, while extensive, lacks coherence and leans heavily on speculation. For instance, the portion discussing biological plausibility is unclear in its message. Although the authors correctly note that decorrelation is observed in various neural circuits, the connection between these observations and the mechanisms or theories presented in the paper remains ambiguous. Additionally, the claim that decorrelation improves generalization (line 479) is inadequately supported by the data. The training curves in Figure 4 do not appear to reach convergence, as indicated by the non-saturating test accuracy. This raises doubts about the robustness of the claimed generalization improvements.

### Questions
To better align this work with the standards and expectations of an ICLR paper, the authors need to sharpen their message and clearly articulate the novel contributions of each section. Specifically, the authors may consider addressing the following questions:
1. How does the consideration of Natural Gradient Descent and the dynamics in curved parameter space contribute to the understanding or derivation of the incremental learning rule? Can this rule be directly derived from the principles of the Natural Gradient theorem?
2. What differentiates the proposed learning rule from existing frameworks for decorrelating neural activity, such as Recursive Least Squares? If there are differences, what are the specific theoretical or practical advantages of the proposed rule?
3. Could the authors provide more extensive numerical analyses to demonstrate whether the benefits of their approach extend beyond faster learning to improved generalization? While Natural Gradient theory primarily explains accelerated convergence, do the authors observe any substantial gains in generalization performance?

Lastly, I want to note that I enjoyed reading the paper and its broad review, which connects the concept of natural gradients to deep network training. However, this discussion currently feels more suited to an opinion piece.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission didactically draws together approximate gradient methods, natural gradient descent, and decorrelation methods, to ultimately improve approximate gradient methods. More specifically the paper shows how natural gradients defined with respect to changes in the loss function highlight the importance of data correlation in determining the alignment between GD and natural gradient updates. With this insight in hand, approximate gradient descent methods are shown to be improved by decorrelating the network activations.

### Strengths
I believe this is an original synthesis of concepts resulting in an original and significant modification to approximate gradient methods. 
This paper is extremely well written, and generally of high clarity and quality throughout.

### Weaknesses
- It is not clear that the alignment to natural gradients is what is underlying the improved performance. 
- No assessment of how successful the decorrelation updates are in aligning regular updates to the natural updates. How big is the contribution of gradient correlations? 
- While the improvements in FA and NP are striking, the experimental results are not finely tuned. It is possible with GD to obtain better results than those shown, and it is unknown if FA and NP will match this improvement. 
- To verify decorrelated FA scales, harder experiments would strengthen the paper (e.g those in Bartunov 2018. Assessing the Scalability of Biologically-Motivated Deep Learning Algorithms and Architectures for ANNs.)
- Given biological relevance, showing application and relevance to recurrent networks would improve the paper.

### Questions
- typo optimization 153
- Assumption on 182 that NGD independent layers, how serious is this?
- 163, should the expectations on G not be over y too?  
- 251 skewed is being used non-technically? 
- 260 type orthogonal 
- 264 citation missing, gradient correlations
- What is the connection between natural gradients and the approximate gradient methods. Why in particular should the approximate methods benefit from natural gradients?
- The discussion of the orthonormal basis of parameters (page 5) induced by data correlations does not make sense to me. Are the parameters already not orthornormal?

### Soundness
3

### Presentation
4

### Contribution
3
