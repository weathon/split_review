# FOSI: Hybrid First and Second Order Optimization

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Popular machine learning approaches forgo second-order information due to the difficulty of computing curvature in high dimensions.
We present FOSI, a novel meta-algorithm that improves the performance of any base first-order optimizer by efficiently incorporating second-order information during the optimization process.
In each iteration, FOSI implicitly splits the function into two quadratic functions defined on orthogonal subspaces, then uses a second-order method to minimize the first, and the base optimizer to minimize the other.
We formally analyze FOSI's convergence and the conditions under which it improves a base optimizer.
Our empirical evaluation demonstrates that FOSI improves the convergence rate and optimization time of first-order methods such as Heavy-Ball and Adam, and outperforms second-order methods (K-FAC and L-BFGS).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors presented a novel optimization method called FOSI, which is a hybrid optimizer algorithm that combines the first-order optimizer with Newton's method. They presented some theoretical analysis as well as some empirical results from the numerical experiments.

### Strengths
This submission is well-organized with clear language and structures. The authors gave detailed description and some theoretical analysis for the proposed algorithms. They also conduct a lot of numerical experiments on deep learning problems and these empirical results are pretty good compared with some state-of-art optimization methods. The idea is pretty interesting and enlightens some promising future direction for the optimization community.

### Weaknesses
There are some disadvantages regarding this submission.

The authors only gave the theoretical results for the stochastic optimization problem. What's the convergence rate for the general convex optimization problem? What is the convergence rate for the strongly convex setting? If the authors could add and present these theoretical analysis. This could significantly improve the quality of this submission.

It's better to put the detailed algorithm from the appendix to the main part of the paper.

It's better to put the section 5 related work part in the section 1 introduction part.

### Questions
Please check the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors present a hybrid method which addresses the challenge of incorporating second-order information in machine learning approaches due to the computational difficulty in high dimensions. This method first splits the space into two orthogonal subspace. Then, the author use first-order method to minimize one of the subspace and use second method to minimize the other one. They also analyze the convergence of FOSI and establish certain conditions under which the proposed method improves the base method. Numerical experiments illustrate the effectiveness of the proposed method.

### Strengths
The idea that splitting the raw space into two orthogonal spaces is interesting. The authors adopt the Lanczos to give a possible way to construct these spaces.

### Weaknesses
One of my major concern is that the memory consumption and computational complexity are very high especially for large-scale neural networks. This will limit the usage of the proposed method. Specifically, the repeated computation of the Hessian-vector product ($hvp$) within the Lanczos algorithm, and the storage of the resulting subspace basis $V$, pose significant memory and computational burdens, particularly as the dimensionality of the parameter space increases. Besides, it is not clear how to handle the communication cost  and the computation of $V$ in the distributed setting.

The scale of the network architecture used in the numerical experiments is limited. It will be more convincing if the authors can show the effectiveness of the proposed method in larger applications. The current experiments do not adequately demonstrate the scalability of the method to more complex models and datasets, which is crucial for practical applicability.

### Questions
In comparison with second-order methods, it is better to compare the proposed with KLBFGS but not LBFGS because the former method is designed specifically for deep learning tasks. It is suggested to add comparison with Shampoo[1] or NGPlus[2], which has good effectiveness in practice. 

it is better to tune the hyper-parameters of ADAM in numerical experiments to make the baseline strong enough. 

Why the curve of FOSI-HB decreases in Figure 2? 

Can randomized numerical algebra be combined in ESE procedure? This will help reduce the computational cost.

[1] Anil, Rohan, et al. "Scalable second order optimization for deep learning." arXiv preprint arXiv:2002.09018 (2020).
[2] Yang, Minghan, et al. "An efficient fisher matrix approximation method for large-scale neural network optimization." IEEE Transactions on Pattern Analysis and Machine Intelligence 45.5 (2022): 5391-5403.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes FOSI -  a novel meta-algorithm that improves the performance of any base 1st order optimizer
by efficiently incorporating 2nd-order information.

In each iteration, FOSI implicitly splits the function into two quadratic functions
defined on orthogonal subspaces, then uses a 2nd-order method to minimize
the first, and the base optimizer to minimize the other.

Empirical results shown on many tasks in real-world domain to show the efficacy of POSI.

### Strengths
Nice analytics with detailed derivations and explanation.

Large amount of empirical studies shown with experimental results.
Steps of the algorithm are clearly specified.

Enjoyed reading the paper.

### Weaknesses
A few failure cases may be discussed.

Although decomposing the problem into two parts may not specifically be novel,
FOSI’s inverse preconditioner seems to be quite a good idea.

Similar work on those lines of decomposing may be mentioned.

### Questions
In the statement (step 2m Lemma 1):
"The preconditioner P is symmetric and PD:.

Is it possible to use a different font for the matrix "P", which has no conflict of P (positive) in "PD" ?
or vice-versa.

Hope the code of the paper, to implement FOSI for any application of Optimization,
will be released soon by authors.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
his paper provides a novel algorithm to accelerate the first-order optimizers by incorporating second-order information. The proposed method is well-motivated and the experimental results show the efficiency of it.

### Strengths
The method is novel which incorporate the descent direction of first-order methods (base optimizer) with second-order information. The empirical study is comprehensive and show the efficiency of the proposed methods. This paper is an interesting attempt on accelerating the first-order methods by using second-order information.

### Weaknesses
The method requires to compute the extreme eigenvalues and vectors of Hessian by lanczos algorithm, it will raises much more computational cost per iteration than the first-order methods. Additionally, it is unknown how to choose $k$ and $l$ in the proposed algorithm. Neither the theoretical analysis and empirical study miss the part on evaluating how $k$ and $l$ affect the behavior of the methods. Besides, the parameters are too much, not only $k$, $l$ need to be chosen, Algorithm 2 also requires the parameter for learning rates $\alpha$, the learning rate for the base optimizer.

### Questions
1. There are some optimizers which also use the hybrid directions of first and second-order methods, or partial information of the Hessian. The author may need to compare and discuss them [1 ,2].

2. Can the authors provide some discussion and numerical evaluation on how to choose $k$ and $l$.


**Reference**

[1]. Zhang C, Ge D, Jiang B, et al. DRSOM: A Dimension Reduced Second-Order Method and Preliminary Analyses[J]. arXiv preprint arXiv:2208.00208, 2022.

[2]. Liu H, Li Z, Hall D, et al. Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training[J]. arXiv preprint arXiv:2305.14342, 2023.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
