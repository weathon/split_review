# Exact Path Kernels Naturally Decompose Model Predictions

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
This paper proposes a generalized exact path kernel gEPK which naturally decomposes model predictions into localized input gradients or parameter gradients. Many cutting edge out-of-distribution (OOD) detection methods are in effect projections onto a reduced representation of the gEPK parameter gradient subspace. This decomposition is also shown to map the significant modes of variation that define how model predictions depend on training input gradients at arbitrary test points. These local features are independent of architecture and can be directly compared between models. Furthermore this method also allows measurement of signal manifold dimension and can inform theoretically principled methods for OOD detection on pre-trained models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a decomposition of the prediction of differentiable models in terms of parameter gradients throughout training. It is shown that a subspace arising from this decomposition captures a significant portion of model prediction variations at a test point when perturbing training points. Some links are established with out-of-distribution detection methods and measuring the dimension of the signal manifold.

### Strengths
There are interesting connections between the provided decomposition and OOD/signal manifold dimension detection methods, which might be worth further exploration.

### Weaknesses
My main concern is that the theoretical results seem to follow directly from the arguments of Bell et al., 2023. Perhaps it could help if the authors added a discussion on the technically novel aspects of the analysis, or alternatively emphasized more on the applications of this decomposition as the main contribution.

While I am not an expert in OOD detection and thus cannot assess the work based on its applied contributions, I am wondering if it is possible to have experiments where additional intuitions gained from the analysis of this work concretely improve the performance of some methods.

There is some notational ambiguity and mathematical imprecision in the current version of the manuscript. Specific examples are provided in the questions section below.

### Questions
* Some examples for improving the clarity and rigor of the mathematical statements:
    * It might be more appropriate to write Eq. (1) in terms of the inner product notation $\langle \varphi_{s,t}(x), \varphi_{s,0}(x_i)\rangle$.
    * It could help the readers better understand the setting if the authors clarify the meaning of "$f$ has been trained by a series of discrete steps composed from a sum of loss gradients ...". If this is just training via gradient descent, it might be easier to simply write down the GD equation.
    * The input and output space of $f$ don't seem to be defined.
    * Making sense of Eq. (8) is not straightforward as the LHS is a vector in $\mathbb{R}^m$, while the RHS is a summation over $M$ scalars (if $\theta^j$ is supposed to denote the $j$th index of $\theta$).
    * The notation $\frac{dL(f(x_i,\theta_s),y_i)}{d\hat{y}_{\theta_s(0)}}$ does not seem to be immediately interpretable. If my understanding of the meaning of this expression is correct, my suggestion is to define something like $L'(\cdot,\cdot)$ as the derivative of $L(\cdot,\cdot)$ with respect to its first argument, and use $L'(f(x_i,\theta_s(0)),y_i)$ instead.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper offers valuable insights into the concept of exact path kernels, enabling us to interprete prediction through the utilization of input gradients over training trajectories. This methodology was first introduced by Bell et al. 2023. In addition, the paper extends the approach to provide a more generalized representation of the output of a test point under general loss functions. Moreover, it establishes a connection between exact path kernels and out-of-distribution (OOD) methods such as GradNorm, GradOrth, ReAct, DICE, and others, all of which rely on the utilization of parameter gradients. The paper also delves into the exploration of using a modified Singular Value Decomposition (SVD) to estimate the signal manifold.

### Strengths
- The paper gives several interesting insights of exact path kernels in the setting of OOD detection.
- Signal manifold estimation seems interesting.

### Weaknesses
 - The paper writing can be improved, i.g. punctuation for equations.
- I find that there is repetition like Bell et al. on Section 3, remark 1 and remark 2.That is, Bell et al. make the similar remarks on SGD and subsampling. Proving techniques resembles the approach in Bell et al.,
- While EPK gives a representation of test points in terms of a vector space where the basis is computed from gradients at every training step, most OOD methods consider the optimized parameter which is $\theta_S$ as the notation in the paper. This means that the existing OOD does not consider the parameter trajectories of optimization.
- $L_{CE}$ is not defined.

### Questions
Minor points
- $L_{CE}$ is not defined.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a generalized exact path kernel as well as its application in out-of-distribution detection.

### Strengths
1. The idea of the approach is intuitive and simple: the authors first establish the connection between the model prediction and the gradient of the loss function on the training data, then they perform spectral analysis on the subspace formed by the gradient vectors.
2. The proposed generalized exact path kernel provides a natural interpretation of the prediction in terms of the loss and parameter gradients.
3. Empirical results demonstrate the effectiveness of the method in identifying the signal manifold dimension.

### Weaknesses
1. Presentation of the manuscript can be improved: Some notations are not clearly defined. For example, \epsilon in Theorem 3.1 is not introduced but only mentioned in the proof as a constant. Similarly, \theta_s(t) is not defined properly and is not distinguished from \theta_s. From the context, s denotes the iteration and t denotes the training data index, does \theta_s(t) refer to a parameter specific to data point t?
2. Theorem 3.1 is the foundation of the proposal but the proof does not seem to be rigorous: it states that θ_{s+1} ≡ θ_s + dθ_{s(t)} / dt, is a step size missing there?
3. The OOD is obtained by analyzing the span of the linear subspace formed by the loss gradient vectors. However, the analysis may not take into account the nonlinearity.

### Questions
- What's the significance of \epsilon in Theorem 3.1 and how is it determined?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
