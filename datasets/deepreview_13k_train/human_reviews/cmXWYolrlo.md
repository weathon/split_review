# Geometric Inductive Biases of Deep Networks: The Role of Data and Architecture

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
In this paper, we propose the \textit{geometric invariance hypothesis (GIH)}, which argues that %the input-space geometry of a neural network 
when training a neural network, the input space curvature remains invariant under transformation in certain directions determined by its architecture. Starting with a simple non-linear binary classification problem residing on a plane in a high dimensional space, we observe that while an MLP can solve this problem regardless of the orientation of the plane, this is not the case for a ResNet. Motivated by this example, we define two maps that provide a compact \textit{architecture-dependent} summary of the input space geometry of a neural network and its evolution during training, which we dub the \textbf{\gname} and \textbf{\deltaname}, respectively. %By investigating these two maps through theoretical and empirical means, we show that GIH is caused by the \deltaname being close to the projection of data covariance onto \gname, resulting in an invariance property when the \gname is low-rank. 
By investigating \deltaname at initialization, we discover that the geometry of a neural network evolves according to the projection of data covariance onto \gname. As a result, in cases where the \gname is low-rank (such as in a ResNet), the geometry only changes in a subset of the input space. This causes an architecture-dependent invariance property in input-space curvature, which we dub GIH. Finally, we present extensive experimental results to observe the consequences of GIH and how it relates to generalization in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies how the geometry of neural network predictors evolves in the input space during training. It proposes the Geometric Invariance Hypothesis (GIH), which posits that this evolution occurs within a constrained subspace of the input space determined by the network architecture. The GIH is supported through experiments with MLPs, CNNs, and ViTs on a subset of CIFAR with binarized labels. The paper also studies the link between the GIH and generalization.

### Strengths
1. The introduction of the Geometric Invariance Hypothesis appears novel and extends findings of Neural Anisotropy Directions (Ortiz-Jimenez et al., 2021) to non-linear decision boundaries. This hypothesis has the potential to provide insights into the relationship between neural network architecture and the structure of data, contributing to our understanding of inductive biases in deep learning.

2. The experiments and the theoretical analysis are generally fair, although several imprecisions are present, and some clarifications are needed (see detailed points below).

3. The theoretical findings are tested using real networks (e.g., ResNets, ViTs) and datasets (CIFAR). These experiments appear to align with and support the GIH. Nevertheless, it is worth noting that the considered settings are highly overparameterized and relatively simple, which raises concerns regarding the broader validity and general significance of the results (see detailed points below).

### Weaknesses
The paper is quite dense. There are multiple points of confusion and imprecisions affecting both clarity and soundness. Specifically:

4.  The introduction and main text lack a comprehensive overview of the field and references to related work. Only a few broad papers are cited, despite the extended page limit of this year's edition. I strongly encourage the authors to move much of the discussion from Appendix A.1 into the main text to better place the work in context. In particular, NADs introduced in Ortiz-Jimenez et al. (2021) should be explicitly discussed in the main text, given how strongly related they are to this work.

5. Lines L058+ seem to confuse expressivity with generalization, i.e., approximation vs. statistical properties. The fact that an MLP is universal (as some deep and wide CNNs are) does not imply that it can generalize effectively. The authors should clarify that while a model may be capable of fitting the training data, this does not guarantee good performance on unseen data.

6. Assuming i.i.d. parameters is not enough to conclude that $G_F \propto I$. A Gaussian distribution with a non-zero mean is a counterexample. The authors need to explicitly state that they are assuming a zero-mean i.i.d. distribution for the parameters to reach this conclusion. This is a crucial detail that needs to be made clear in the main text.

7. The claim that MLPs have a lack of inductive bias (L210, L224, L249) is wrong. Even in the NTK regime, MLPs display a strong spectral bias for low modes. It may be more accurate to state that MLPs at initialization have no preferred directions in the input space, i.e., they have an isotropic prior in the input space. The authors should be more precise in their terminology and avoid overstating the lack of inductive bias in MLPs.

8. Multiple terms are left undefined or used imprecisely: e.g., “SSE loss” and $y_{\mu}$. Some phrases are vague: What is the “input-space curvature”, and how can it depend on the training process (L011)? What is the “input geometry” of a neural network (L076, L521)? What does it mean for a dimension to be noise (L053)? What are “all the possible values of $\theta$” ( L145)? How are they distributed? Given that you consider gradient-flow in your analysis, how do you define the “first step” in L286?

### Questions
9. From Figure 1, it seems that simple (and standard) early stopping would solve the generalization gap problem and actually result in a lower test loss for dataset $D_B$ compared to dataset $D_A$. Can you comment on this? How general is this observation? 

10. What’s the underlying distribution over which you are taking the expectation at L227? It should be made explicit.

11. When you write “momentums” (L244, L246) do you mean “moments” instead?

12. Is the fact that $\Delta_F$ becomes label-independent purely due to the fact that you assume $\mathbb{E}_\theta [\theta]=0$ at initialization?

13. Could the phenomena observed in the paper, particularly when testing conjecture 2 about the GIH, be due to the fact that networks in all experiments are strongly overparameterized (even with CIFAR, the paper considers only a small fraction of the full dataset) and training in the “lazy” or NTK regime where weights stay close to their initial values? Did the authors measure the weight evolution throughout training? Would you expect the same results when training with more data, e.g., the full CIFAR10 dataset, and/or with tasks requiring learning latent features of the data that might be less dependent on the exact geometry and statistics in input space, e.g., more complex image datasets such as ImageNet?

14. Could the authors comment on Conjecture 2 in the case of linear regression? Intuitively, it seems it should hold in that simpler setting.

15. What is the motivation behind adding label noise (L406)? Would the same results or trends be observed in its absence?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In their paper, the authors argue for the link between input-space geometry and the ability of models to generalize. They propose the geometric invariance hypothesis (GIH) which states that, depending on the architecture of the model, the curvature of the input-space remains invariant under transformations in certain directions. They then attempt to prove and study this phenomenon by separating the changes in the input-space geometry during training into architecture-dependent changes and data-dependent changes. This resulted in finding the special cases where the invariance occurs, and they link this to the generalization ability of the model and where it collapses to reliance on noise and memory.

### Strengths
The paper is able to gradually build up to the main hypothesis being proposed while maintaining a clear chain of reasoning. The authors also provide extensive mathematical proofs for each step in the build-up and mention what assumptions are made and any limitations on what can be shown or derived. Finally, they are able to provide some insight into the effect of this hypothesis on an architecture's generalization ability while addressing any possible ideas with empirical results.

### Weaknesses
While the "performance" gains of the paper do seem marginal, I see these experiments as more of a proof of concept of the ideas and the proposed hypothesis. However, it would have been nice to see these experiments on multiple datasets to verify if the claims still hold, especially given the simplicity of the current model choices as well. The experiments, while insightful, are primarily conducted on relatively small datasets and with simple architectures. This raises concerns about the generalizability of the findings to more complex, real-world scenarios. Specifically, the reliance on datasets like CIFAR-10 and relatively shallow networks might not fully capture the nuances of input-space geometry in deeper models trained on larger, more diverse datasets. The paper would benefit from demonstrating the robustness of the Geometric Invariance Hypothesis (GIH) across a wider range of architectural choices and data complexities. Furthermore, the paper's analysis of the average geometry function, while mathematically sound, could be further validated by examining its behavior in the context of more complex optimization landscapes. The current experiments might not fully reveal the limitations of the approximations used in the analysis, especially when dealing with highly non-convex loss surfaces.

### Questions
Just as a small note, in line 211 you mention the interaction between two factors, specifically the data-dependent factor and another. I'm guessing this is the model's geometric inductive bias? If so, I think it could be written a bit clearer. 

Additionally, would you think this approach would be useful for architecture-based optimal dataset subsampling methodology?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces the geometric invariance hypothesis (GIH), which suggests that during the training of neural networks, the curvature of the input space remains invariant under transformations along specific directions determined by the network’s architecture. The authors begin by examining a non-linear binary classification problem situated on a hyperplane in a high-dimensional space. They observe that a multilayer perceptron (MLP) can solve this problem regardless of the hyperplane’s orientation, whereas a residual network (ResNet) cannot. Motivated by this finding, they define two architecture-dependent maps: the average geometry, which provides a compact summary of the network’s input-space geometry, and the average geometry evolution, which describes how this geometry changes during training. Through both theoretical analysis and empirical investigations, the paper demonstrates that GIH arises because the average geometry evolution closely approximates the projection of the data covariance onto the average geometry. This results in an invariance property, especially when the average geometry is low-rank. Finally, the authors present extensive experimental results to explore the consequences of GIH and its relationship to generalization in neural networks.

### Strengths
The introduction of the geometric invariance hypothesis (GIH) offers a fresh and innovative perspective on the interplay between neural network architectures and the geometry of the input space during training. By proposing the concepts of average geometry and average geometry evolution, the authors provide novel tools for quantifying how different architectures influence learning dynamics. This approach moves beyond traditional analyses by directly linking architectural properties to geometric transformations in the input space, which is a significant conceptual advancement in understanding deep learning models.

### Weaknesses
While the paper makes significant contributions, there are areas that could be improved:

- Lack of Intuitive Explanation: It is challenging to develop an intuition for why ResNets behave differently from MLPs. Providing more intuitive explanations or illustrative examples before introducing the mathematical formalism would help readers grasp the core concepts and follow the subsequent analysis more effectively. Specifically, the paper could benefit from a more detailed discussion of how the skip connections in ResNets influence the geometry of the input space compared to the direct mapping of MLPs. A concrete example demonstrating how these architectural differences lead to different curvature behaviors would be beneficial.

- Limited Architectural Comparison: The focus on ResNets without discussing other architectures like AlexNet leaves some gaps. Clarifying whether the observed behaviors are due to specific features like skip connections or are common across different architectures would strengthen the generality of the findings. It would be valuable to see an analysis of architectures with varying depths and connection patterns to determine if the GIH holds true across a broader spectrum of network designs. For example, examining the behavior of networks with dense connections or those with different types of pooling layers could provide further insight.

### Questions
I am interested in how your observations are affected by different training dynamics, specifically when using stochastic gradient descent (SGD) with large learning rates—a common practice for achieving high prediction accuracy. Have you explored how the geometric invariance hypothesis (GIH) and the behavior of average geometry and its evolution manifest under such training conditions?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors study the input-space geometry of neural networks, i.e., the decision boundaries and loss surface at each point in the input space. They give mathematical characterizations of the expected geometry and dynamics of the geometry under gradient flow at initialization. They make some intuitive conjectures about how the geometry evolves under training, one of which is the Geometric Invariance Hypothesis, which says that the geometry of the model remains invariant in "un-important" directions of the input space while training. They then experimentally verify parts of their conjectures using some representative architectures on both synthetic data and smaller-scale real data.

### Strengths
- The examination of input-space geometry of neural networks is a more novel approach: other more mainstream approaches such as NTK and AGOP consider the parameter-space geometry.
- The conclusions are interesting, and to some degree, sensible: if there are directions in the input space which do not support the training data distribution, then the training dynamics may not move the input-space geometry in these directions.
- The paper does a good job motivating a very theoretical research direction with plausible practical implications in Section 5.
- The paper is reasonably well-written; despite the material being technically dense, it mostly makes sense after a thorough read.

### Weaknesses
 - The definitions of geometry in this work are based on expected second moments of the data. This captures the smallest supporting subspace of the data. But data can have very large linear dimension while having small intrinsic dimension, cf "manifold hypothesis". The theory here does not seem to capture this more involved geometric aspect, but this assumption has been hypothesized to be more realistic for real data. The lack of understanding here makes the experiments less likely to track with the theory and may preclude more prescriptive insights, beyond those generated by the preliminary experiments in Section 5.
- More minor: There is not much intuition provided about why the predictions made at initialization should transfer reasonably well to training, and thus (in my opinion) not too much motivation for the Conjectures (which are about training dynamics).

### Questions
- The experiments remove normalization from the neural networks. Is this crucial? Does the trend totally deteriorate with normalization? Is there any hypothesis made by the theory as to why?
- Regarding the Conjectures 1 and 2 about dynamics: Is there an infinite- or large-width assumption being implicitly made, for instance? Should readers interpret the Conjectures as holding in appropriate scaling limits or should they hold at reasonable scales?

### Soundness
4

### Presentation
2

### Contribution
3
