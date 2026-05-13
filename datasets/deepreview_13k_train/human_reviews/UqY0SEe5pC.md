# Analyzing Neural Network Based Generative Diffusion Models via Convexification

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Diffusion models are gaining widespread use in cutting-edge image, video, and audio generation. Score-based diffusion models stand out among these methods, necessitating the estimation of  score function of the input data distribution. In this study, we present a theoretical framework to analyze two-layer neural network-based diffusion models by reframing score matching and denoising score matching as convex optimization. We prove that training shallow neural networks for score prediction can be done by solving a single convex program. Although most analyses of diffusion models operate in the asymptotic setting or rely on approximations, we characterize the exact predicted score function and establish convergence results for neural network-based diffusion models with finite data. Our results provide a precise characterization of what neural network-based diffusion models learn in non-asymptotic settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose to analyse diffusion models by reframing score matching as a convex optimization problem.

### Strengths
The score matching is generally viewed as a nonconvex problem, hence the guarantees in this sense for diffusion models are hard to obtain. The paper tries to develop a convex optimization approach, which could significantly improve theoretical understanding of these training procedures.

### Weaknesses
 The score matching is generally viewed as a nonconvex problem, hence the guarantees in this sense for diffusion models are hard to obtain. The paper tries to develop a convex optimization approach, which could significantly improve theoretical understanding of these training procedures.

 The general promise of the paper seems too ambitious, as of course, there is no way (yet) to obtain general convex optimisation formulation. The paper focuses on specific cases and somehow it has to be clarified for full transparency that the results apply to specific cases.

 The results of convexification relies on specific structure of the networks that makes sense. However, it is quite obvious that, also, these networks are not what's used in practice. It would be appropriate to update the text to reflect the limitations.

 The authors also didn't discuss the general difficulty of extending these results to more realistic networks. A discussion on this would be helpful. In fact, ReLU can be replaced with other basic units, would these results hold or easily extended to those cases?

 While authors mentioned the computational difficulty of score matching, it would be appropriate to discuss the numerical cost of this procedure and have a comparison with score matching in terms of runtimes for similar problems. Is it much more efficient?

Typos

- The word "Langevine" used in many parts of the paper instead of Langevin
- Section 3 can be incorporated as a subsection of Section 1.

### Questions
1- The results of convexification relies on specific structure of the networks that makes sense. However, it is quite obvious that, also, these networks are not what's used in practice. It would be appropriate to update the text to reflect the limitations.

2- The authors also didn't discuss the general difficulty of extending these results to more realistic networks. A discussion on this would be helpful. In fact, ReLU can be replaced with other basic units, would these results hold or easily extended to those cases?

3- While authors mentioned the computational difficulty of score matching, it would be appropriate to discuss the numerical cost of this procedure and have a comparison with score matching in terms of runtimes for similar problems. Is it much more efficient?

Typos

- The word "Langevine" used in many parts of the paper instead of Langevin
- Section 3 can be incorporated as a subsection of Section 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the score-matching and denoising score-matching objective functions used to learn the scores of distributions for diffusion models. The focus is on understanding what the vanilla score-matching objective with weight decay does for a two-layer neural network. The authors show that for a certain weight decay parameter regime, the problem can be cast as a convex optimization problem, and the global minimum always corresponds to a distribution close in KL to either a Gaussian or a Gaussian-Laplace distribution. The authors also show that under this regime, the Langevin algorithm can sample from the learned distribution.

### Strengths
- This paper attempts to study why score matching for two-layer neural networks can learn the score, which is an important and relevant question.

### Weaknesses
 - This paper is not well-motivated. The vanilla score-matching objective is not used in practice, and the convex program is not used to train the neural net in practice. So it's not clear why this particular problem is being studied.
- This paper studies a particular weight decay regime, in which the distribution converges to either a Gaussian or Gaussian-Laplace. However, in practice, there is no weight decay. Furthermore, the interesting thing about diffusion models is that they *can* learn more complicated distributions. The simplest example is the mixture of Gaussians, which *even* two-layer neural networks can represent the score of, and which this weight decay regime fails to capture. In practice, of course, the distributions being learned are far more interesting than a Gaussian-Laplace, or even a mixture of Gaussians, and this paper fails to explain any of this.
- There is a small section studying the denoising score-matching objective (the one actually used in practice), but it seems to again be in the uninteresting weight decay regime (this section is very short, and the results are difficult to interpret).
- More generally, the presentation is difficult to follow, and things are not well motivated. For instance thereom 4.1 is stated, but no intuition is provided for what it means. The matrices/vectors in the theorem are described in subsequent sections, but again, not much motivation/intuition is provided. It seems like a lot of this should just be pushed to the appendix.
- The Langevin algorithm is studied for sampling, while in practice, annealed Langevin is used after learning the score at multiple noise levels. None of this is explored in this paper. Furthermore, the sampling result itself seems to be a consequence of classical work, since the distribution learned is always very simple in the weight decay regime studied.

### Questions
- What is the motivation for studying this problem?
- Is there anything you can say when there is no weight decay?
- Can you provide more detail in the section studying the denoising score matching objective?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzed the score-matching and denoting score-matching objective with two-layer neural networks as the fitting function. For univariate training data, they show that such optimization problems can be reformulated as convex optimization. They establish the Langevin dynamics converges to Gaussian or Gaussian-Laplace distribution. The result is extended to high-dimensional data.

### Strengths
This is the first paper that proposes a convex formulation for the score matching with two-layer neural networks. It provides concrete theoretical guarantees.

### Weaknesses
1. It seems unnatural to add a regularization term along with the SM or DSM objective function. By adding the regularization term, the minimizer of the SM/DSM objective function (population version) will not be the intended score function, so the generated samples from such diffusion models will not follow the distribution of the training data. Indeed, Theorem 6.1 and 6.2 show that the obtained sample will follow Gaussian/Gaussian-Laplace distribution, no matter which distribution the training data is from. This defeats the original purpose of diffusion generative modeling. The issue is that the regularization term, while potentially helpful for optimization, fundamentally alters the objective, causing the learned score function to deviate from the true score of the data distribution. This is not just a minor perturbation; it changes the target distribution of the generative process.
2. The convex program in 1 dimension is efficiently solvable (the regularized objective). However, in high dimensions, the convex objective function involves combinatorial sums, which is not efficiently computable. Specifically, the number of sign patterns grows exponentially with the dimension and number of data points, making the optimization intractable for even moderately sized datasets. The paper mentions that the program takes $O((r(n/r)^{r}d^2)^3)$ time, which is computationally prohibitive for high-dimensional data. The authors should acknowledge that this computational complexity severely limits the practical applicability of the proposed approach in high dimensions.

Minor:
In the statement of Theorem 4.2, $D_j = D_j$ when ... and $D_j = 2 D_j - 1$ when ... is not a serious statement.

### Questions
Could you respond to the two weaknesses above?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies neural network-based score matching objective. For univariate data, the authors show that the regularized SM can be formulated as a convex optimization problem. The optimal solution to the convex programming can be explicitly obtained and used to recover the neural network parameters. The results are then extended to the multivariate data case. The authors also study the convex optimization problems associated with the regularized denoising score matching loss under both univariate and multivariate data inputs. Finally, the authors investigate the convergence of Langevine MC with the score estimator obtained from the above convex formulation. Numerical experiments are conducted to verify the theoretical results.

### Strengths
1. The authors prove that regularized SM and DSM can be viewed as a convex optimization even using neural score estimators. The formulation is obtained under both univariate and multivariate data inputs. 
2. The authors study the convergence of Langevin MC with the score estimator obtained from the convex formulation.
3. Numerical experiments are organized to evaluate the performance of score estimator.

### Weaknesses
1. The paper considers the regularized score matching loss rather than the standard one. This regularization, while potentially helpful for optimization, deviates from the typical score matching objective and may limit the direct applicability of the results to scenarios where such regularization is not used. The specific impact of this regularization on the quality of the learned score function and its downstream performance is not fully explored.
2. The paper studies the convergence of Langevine dynamics rather than the more widely used backward process in DDPM papers. While Langevin dynamics is a valid approach for sampling, the connection to the backward process used in diffusion models is not clearly established. This makes it difficult to directly assess the relevance of the results to the broader field of diffusion-based generative modeling. The theoretical analysis should also consider the convergence of the score estimator to the true score function, not just the convergence of the sampling procedure.
3. The Gaussian data distribution in experiments look too simple compared to the ones in practice. The use of a simple Gaussian distribution for the experiments, while useful for verifying the theoretical results, does not adequately demonstrate the practical applicability of the proposed method to more complex, real-world data distributions. The experiments should include more challenging datasets to evaluate the robustness and effectiveness of the approach.

### Questions
1. I am curious how the convexity arises. Is it because of the regularization term in the SM and DSM objectives?
2. In many convergence theory, we hope to have a score estimator close to the ground truth score function in $L^2$ sense. Although the optimization objective is derived, it is not clear whether the optimal solution can have good generalization ability in population loss. 
3. For Gaussian data distribution, the score function is actually linear. I am surprised in Figure 4 that the non-convex neural estimator trained by DSM cannot recover the ground truth score function. Could you provide some intuition?
4. The writing can be significantly improved. I suggest adding more interpretations after each theoretical result.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
