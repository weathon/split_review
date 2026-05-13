# Gathering and Exploiting Higher-Order Information when Training Large Structured Models

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
When training large models, such as neural networks, 
the full derivatives of order 2 and beyond are usually inaccessible,
due to their computational cost.
This is why, among the second-order optimization methods, it is very common
to bypass the computation of the Hessian by using 
first-order information, such as the gradient of the parameters (e.g., quasi-Newton methods)
or the activations (e.g., K-FAC).

In this paper, we focus on the exact and explicit computation
of projections of the Hessian and higher-order derivatives on
well-chosen subspaces, which are relevant for optimization.
Namely, for a given partition of the set of parameters, 
it is possible to compute tensors which can be seen as
"higher-order derivatives according to the partition",
at a reasonable cost as long as the number of subsets of 
the partition remains small.

Then, we propose an optimization method exploiting
these tensors at order 2 and 3 with several interesting properties, including:
it outputs a learning rate per subset of parameters, which can
be used for hyperparameter tuning;
it takes into account long-range interactions
between the layers of the trained neural network, 
which is usually not the case in similar methods (e.g., K-FAC);
the trajectory of the optimization is invariant under 
affine layer-wise reparameterization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work considers building summaries of higher order loss derivatives, like the Hessian and the third-order Tensor, which bucket interactions at the level of layers or some arbitrary partitions, instead of each individual parameter. In particular, by considering a particular contraction (like with the all-ones vector or gradient direction), very compact higher-order summaries can be built (which scales polynomially in the number of layers, instead of parameters). As an application, they use it to derive a layerwise scaling of learning rates, which neatly interpolates between the two extremes of using Newton's method and Cauchy's steepest descent rule. The method is demonstrated on some very simple experimental setups.

### Strengths
- The paper is in general well motivated with the need to capture the interactions between parameters in different layers, which is often ignored by block-diagonal methods. This is operationalized in a natural way by studying the Hessian with suitable contractions. 

- The approach of getting layerwise learning rates through their layerwise grouping is neat. This offers a principled extension to the Cauchy's steepest descent rule. 

- The method could also find utility in studying the behaviour of feature learning across layers, and thus be used more than just in optimization.

### Weaknesses
 - The experimental section is quite weak. I understand that the authors themselves pitch it as a proof-of-concept, but I am not so sure about even if you can call it a proof of concept. The experiments are on small datasets like CIFAR, even over there none of the methods get the typical 90% and above accuracy, the test accuracy of their method is much worse than K-FAC.

 - More fundamentally, it is unclear to me where lies the bigger problem: correcting the curvature across layers, or that within the layers. It is well known that the Hessian tends to have a significant energy on its block diagonals, and thus maybe correcting across the layers, may not possess significantly more information.

 - Also, even for their method, I am curious what amount of the performance can be explained by simply estimating the scales of the Hessian on the diagonal blocks. In particular, if they instead use diag(\bar{H}), and then use it to get layerwise learning rates, how does that perform? This would form a test bed to showcase how crucial is it to capture cross-layer information.

 - Besides, I think in the vision setting the Hessian tends to be more homogeneous across the networks as opposed to that in Transformers with language modelling [1]. Hence, I think their approach might be more suited to that setting, and would be interesting to see if it can outperform methods like Adam-Mini [2].

 - There are very limited baselines considered by the authors. I would have liked to see the Cauchy step size, AdaHessian, and even a block-diagonal quasi Newton method.

 - The overall runtime cost can be quite large, as there are multiple Hessian vector products. Can the authors do a wall-clock comparison?

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to make second-order optimization computationally tractable by taking a coarse view of high-dimensional parameter spaces. The authors break the Hessian of a deep learning model into blocks, with one block for every pair of layers, and compute one summary scalar per block. This allows for modeling inter-layer interactions, unlike many other approaches to approximate second-order optimization that neglect these terms. The authors propose a cubic-regularized version of their algorithm, and present experimental evidence that inter-layer interactions in deep learning models are non-trivial. Ultimately, the experimental results of the authors' proposed method are mixed.

### Strengths
The authors present a very interesting idea, and thoroughly motivate the idea. It really is a big short-coming that many related papers on this topic neglect inter-layer interactions when designing optimization algorithms. And finding computationally tractable ways to "summarize" the Hessian is a very strong idea.

The discussion of related work is quite comprehensive and clear.

Generally the work feels quite thoughtful: considering what are the issues with Newton's method, and how to try to overcome them.

### Weaknesses
I think the method could potentially be introduced in a more straightforward way, and I want to suggest one way. I think the method could be viewed as a change of variables to a smaller set of local optimization variables. In particular, instead of viewing the loss as a function of general perturbations to all the weight tensors:

loss( W_1 + ∆W_1, W_2 + ∆W_2, ..., W_S + ∆W_S)

we can view the loss as as a function of scalar-parameterized perturbations to each layer:

loss( W_1 - η_1 * G_1 , W_2 - η_2 * G_2, ..., W_S - η_S * G_S)			(*)

where η_1, η_2, ..., η_S are a collection of scalars and G_1, G_2, ..., G_S are the gradients of the loss with respect to each weight tensor, evaluated at the point W_1, W_2, ..., W_S. We can consider (*) to be a loss function with S variables η_1, η_2, ..., η_S. It's then clear that Hessian of this "reduced-dimensionality" loss is an S x S matrix. And we can throw any of a wide range of optimization methods toward solving this local S-dimensional optimization problem.

I also think the title could possibly be improved. What about something like "Multi-Tensor Optimization via Second-Order Scalar Summaries"?

Algorithmically, there is a weakness in the method that it only searches in the gradient direction for each tensor. This means the method would miss Shampoo-style [1] changes to the gradient direction which have been found to speed up deep learning training empirically. Specifically, the method restricts its search to a subspace spanned by the gradients, which is a significant limitation. This prevents the algorithm from exploring other potentially beneficial directions in the parameter space that are not aligned with the gradient. For instance, preconditioning the gradient with an approximation of the inverse Hessian, as done in methods like Shampoo, can lead to faster convergence by adapting the search direction to the local curvature of the loss landscape. By only considering scalar multiples of the gradient, the proposed method may be unable to exploit such curvature information.

The experimental results are mixed and perhaps not terribly promising at the moment. But it's good that you are open and up front about this. I think it's unlikely the broader community would focus on the paper too closely without more thorough experimental results.

Some light proof-reading of the writing would be helpful in places. For example line 90--91 "This is typically what is done by Dangel (2023), despite it does not go beyond the second-order derivative."

### Questions
See weaknesses section. Do the authors agree with this perspective?

### Soundness
4

### Presentation
3

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
The authors suggest a layer-wise partitioning of order $d$ derivatives, that transforms the $R^{p^d}$ tensor to a $R^{S^d}$ tensor which is computationally tractable even in deep networks.  The authors then leverage this partitioning to first compute empirically the Hessian for some deep neural networks, and subsequently suggest a second order method based on partitioning for optimization.

### Strengths
The paper has several strengths:

1) The interest in efficient computational schemes of higher order information for deep neural networks is significant, and improved methods of estimating the Hessian, as well as higher order terms could help improve interpretability and shed light on what neural networks learn during optimization.
2) The partitioning scheme is the main contribution of this paper, and seems to be novel as far as I know, with possible applications to many interesting avenues.

### Weaknesses
In spite of the strengths, the paper has some clear drawbacks in my opinion:

1) The paper is not written well enough, with a substantial lack of a literature survey on properties of Hessians in deep networks, as well as works on second order methods from recent years. In terms of the writing itself, all of the equations on page 5 are unnumbered making them hard to refer to, and the chosen notation for tensor contraction $A[ u, u... u]$ is not standard and never explained. It must be understood from context in the main text or the appendices.
2) The main contribution - the fast computation of lower complexity tensor containing similar information as the original tensor is not given in detail in the main text, and even in the appendix should be explained explicitly.
3) In general, I believe the focus of the paper is completely misguided. It seems clear that the suggestion of the second order optimization method is not superior (at least in its current form) to other simple gradient based methods, and should then not be the focus of the paper. Instead, if the paper focused on the partitioning/computation methods and then applied this to real-world or even particular solvable examples, extending Sec. 5.1, the paper would be much stronger.



### Questions
1) L43 - I'm not sure this is correct, assuming unlimited compute, and a perfectly known Hessian, even if the Hessian is singular you can still invert it on the nonsingular subspace, using SVD and find the pseudo-inverse.
2) L71 - Why do the authors need to regularize instead of computing just the pseudo inverse? is it inefficient? this should be stated explicitly
3) L76 - "so its preserves "
4) L218-220 seems wrong, the d-derivative is a map from $\mathbb{R}$ to $\mathbb{R}^{p^d}$ and not the other way around, even if the intention was a map from weight space to the operator output it should be from $\mathbb{R}^p$ to $\mathbb{R}^{p^d}$, so this is unclear to me. Additionally, the second term is unclear, $u$ are not defined at this point and the brackets $[.]$ are undefined as well. In the appendix it seems clear that the intention is tensor contraction between the previous term and the brackets but this is not standard.
5) L258 - "Therefore, the tensors $D_\theta^d(u)$ extract more information than the naive Taylor terms, while keeping a reasonable computational cost. " why is this statement obvious "therefore"? is the statement that regular Taylor terms lose the layer-wise structure of the network? I understand that the equality between Taylor and this decomposition is only obtained after tracing out the $s_i$ indices, but what is the intuition? it would be useful to show explicitly for a low $d$ derivative with a fixed number of parameters to illustrate the difference.
6) the authors don't comment on the compute time of their method compared to single gradient based method (Which seem to be better so far), it would seem like $t*p*S$ vs $t*p$, making it substantially slower for deep networks. 
7) While the method provided in this text is not shown to be superior to standard algorithms, it might be interesting to consider the computation method in the context of sharpness aware minimization.

### Soundness
2

### Presentation
2

### Contribution
2
