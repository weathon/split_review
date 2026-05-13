# Efficient Differentiable Approximation of the Generalized Low-rank Regularization

- Decision: Reject
- Scores: 5, 3, 8, 5, 5

## Abstract
Low-rank regularization (LRR) has been widely applied in various machine learning tasks, but the associated optimization is challenging. Directly optimizing the rank function under constraints is NP-hard in general. To overcome this difficulty, various relaxations of the rank function were studied. However, optimization of these relaxed LRRs typically depends on singular value decomposition, which is a time-consuming and nondifferentiable operator that cannot be optimized with gradient-based techniques. To address these challenges, in this paper we propose an efficient differentiable approximation of the generalized LRR. The considered LRR form subsumes many popular choices like the nuclear norm, the Schatten-$p$ norm, and various nonconvex relaxations. Our method enables LRR terms to be appended to loss functions in a plug-and-play fashion, and be conveniently optimized by off-the-shelf machine learning libraries. Furthermore, the proposed approximation solely depends on matrix multiplication, which is a GPU-friendly operation that enables efficient parallel implementation. In the experimental study, the proposed method is applied to various tasks, which demonstrates its versatility and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a very interesting ideal to represent the nuclear norm as well as non-convex low rank regularizes as Expectation of differentiable function, and use the differentiable low-rank regularization model for matrix completion and video foreground-background separation.

### Strengths
The results presented in this paper is novel and significant, especially for the equivalent expressions of nuclear norm and the non-convex singular value regularization functions.

### Weaknesses
1.	The writing of this paper is crude. The authors should present the detailed algorithms as well as convergence analysis when using the proposed model for specific applications such as matrix completion as well as video foreground and background separation.
2.	Some important related works such as [1-5] should be discussed and compared in this work as they are representative works that are dealing with the same problem as the current work.
3.	Some of the presentation is not correct, such as “…key problem of the matrix factorization is that it demands strong prior knowledge on the matrix rank…”. To my knowledge, the variational representation of the nuclear norm as well as the non-convex regularization do not need to know the exact rank, such as [1,2,4,5].
4.	The authors argue that the SVD is not differentiable, please refer to [6] for more information.
5.	Some of the experimental results are vague. Specifically, in Table 1, the running time of MSS is slower than IRNN. As for as I know, MSS is a representative factorization-based model which is much faster than the IRNN. Besides, the proposed model provides an equivalent representation of the nuclear norm and non-convex rank regularization function, the overall mathematic model is the same as the low rank regularization function implied on the original full matrix. Why does the performance of the proposed method present in Table 1 is much better than existing methods with the same mathematical model? Where does the performance gain come from?

### Questions
Please refer to the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an effective differentiable approximation method for solving the generalized low-rank regularization problem. By integrating the differentiable regularizer into the objective function, optimization becomes an automatic process when employing gradient-based machine learning libraries. The authors apply their approach to the machine learning tasks such as text removal and foreground-background separation.

### Strengths
S1 The authors incorporate Ben-Israel & Cohen's iterative method for computing the matrix pseudo-inverse into their problem of minimizing low-rank regularization.

S2 The authors incorporate the Newton-Schulz iteration for matrix square root computation into their problem of minimizing low-rank regularization.

S3. The authors perform a Taylor expansion or Laguerre expansion on the smooth low-rank regularization term to render the objective function differentiable, thus enabling the use of gradient descent.

### Weaknesses
W1. This paper introduces a smooth approximation technique for the rank function, which is a well-explored area in the literature, featuring numerous convex and nonconvex approximation methods. However, the paper lacks an optimality analysis of the proposed technique, leaving it unclear why this particular strategy is necessary. Specifically, the paper does not discuss the approximation error introduced by the Taylor or Laguerre expansions, nor does it compare the proposed approximation with existing methods in terms of approximation quality or computational cost. The lack of theoretical justification makes it difficult to assess the value of this specific approach compared to other well-established techniques.

W2. It is unclear whether the gradient descent algorithm will converge when another sub-iteration is introduced to estimate the matrix pseudo-inverse or matrix square root. The paper does not provide any theoretical analysis or proof of convergence for the overall iterative process, which combines gradient descent with iterative matrix computations. The interaction between these two iterative processes is not well-defined, and it is possible that the sub-iterations could interfere with the convergence of the gradient descent, leading to oscillations or divergence.

W3.The authors suggest employing Laguerre expansion to handle the low-rank regularization function, with $\alpha_{k,p}$ representing the polynomial coefficients. The authors mention that these necessary coefficients can be computed using readily available tools like Mathematica; however, the complexity of computing these coefficients remains unclear. Furthermore, the paper does not discuss specific ranges for $k$ and $p$. The paper should provide a more detailed analysis of how the choice of $k$ and $p$ affects the accuracy and computational cost of the approximation, and how these parameters should be chosen in practice. The lack of clarity on these points makes it difficult to reproduce the results and assess the practical applicability of the method.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper shows that matrix rank-function and its common surrogates can be approximated by a stochastic formulation (i.e. they can be described using means of random variables). This formulation allows approximating the rank function with a differentiable surrogate, which in turn allows the rank function to be optimized in any framework supporting gradient-descent optimization.

### Strengths
The method is applicable to a wide array of applications and can be plugged into any low-rank optimization/regulatization scenario.
It is fairly simple to implement.

### Weaknesses
It would have been nice to see some results on the approximation errors that one gets as one truncates the infinite sums in equations 6 and 7. Specifically, the paper lacks a discussion on how the choice of the truncation point N affects the accuracy of the rank approximation. The practical implications of this truncation, such as the trade-off between computational cost and approximation fidelity, are not explored. Furthermore, it is unclear how the error introduced by truncation interacts with the overall optimization process, and whether this error is bounded or can lead to instability in certain scenarios. A more detailed analysis of the convergence properties of the truncated series would be beneficial.

### Questions
None that I can think of.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a differentiable approximation of low-rank priors. The idea is to use a finite number of differentiable iterative steps to approximate the pseudo-inverse or the square root of a matrix. This differentiable approximations are used to approach low-rank regularizers in three different inverse problems. The resulting penalty function is minimized with gradient-based optimization algorithms via automatic differentiation.

### Strengths
- The paper is generally comprehensible, effectively written, and presents a logical flow that is easy to follow. The main contribution is clearly articulated and appropriately positioned in relation to existing literature.
- The proposed differentiable prior is novel and the idea is interesting.
- Experiments on 3 different applications prove the efficiency of the method. In particular, I find interesting the ability to stabilize the denoiser w.r.t the noise level.

### Weaknesses
 - The optimization algorithm to minimize (1) is not explicitly presented. Although it is understood that a gradient descent or a variant is utilized, it lacks explicit clarification. Furthermore, the regularization now differentiable, but does it have Lipschitz gradient? More broadly, does the gradient descent algorithm employed to minimize (1) offer any guarantees of convergence? I believe this is a significant concern in this work, especially when mentioning that other concurrent approaches “require the loss function to be convex, which severely limits their applicability.”
- How do you compare, in performance, w.r.t computing directly (without taking care of the differentiability) the nuclear norm / Schatten-p norm with automatic differentiation ? In this case, automatic differentiation is likely to compute (approximate) subgradients.  Given the fact that the proposed method is also based on approximations, the authors should compare both approach with more details. 
- There are still many specific details that are missing and that I would like to obtain (refer to the questions section).

### Questions
- How to you compute the power of the matrix in (6) or (7) ?
- How do you truncate the Taylor and Laguere series ? 
- I would find it useful to have the precise algorithm you use in practice to compute (6) with the different approximations and the different parameters.
- Have the authors considered efficient backward pass via implicit differentiation of the fixed-point iterations ? 
- In the DNN application, it is not clear if the regularization is applied during or after training.
- Do you train a different model for each sigma parameter, or do you use sigma as a parameter of the model ?
- Why the low-rank structure is only applicable to the entire image ? 
- For the denoising applications, which regularizer do you use ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this paper have introduced a novel approach to address the challenges associated with low-rank regularization (LRR) in the context of various machine-learning tasks. LRR has found widespread application, but the optimization of these relaxed LRRs has typically relied on singular value decomposition, a time-consuming and non-differentiable operator that cannot be optimized using gradient-based techniques.
In response to these challenges, the authors have presented an efficient and differentiable approximation of generalized LRR. This form of LRR encompasses well-known options like the nuclear norm, the Schatten-p norm, and various nonconvex relaxations. Their proposed method allows for the seamless integration of LRR terms into loss functions, making it compatible with off-the-shelf machine-learning libraries for convenient optimization. Moreover, this approximation relies solely on matrix multiplication, a GPU-friendly operation that facilitates efficient parallel implementation.

### Strengths
The paper is well-written with a clear structure, making it easy for readers to follow.

### Weaknesses
However, it lacks some essential details, such as specifying the objective function for different problems and explaining how their algorithm derives the corresponding regularization. The conclusion is overly simplistic.

In section 4.1, there are five different variations of the author's algorithm compared to other methods, which raises questions about whether there is randomness in the application of a particular method for matrix completion. Sections 4.2 and 4.3 also fall short by not providing comparisons with similar methods in the field.

### Questions
In section 4.1, there are five different variations of the author's algorithm compared to other methods, which raises questions about whether there is randomness in the application of a particular method for matrix completion. Sections 4.2 and 4.3 also fall short by not providing comparisons with similar methods in the field.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
