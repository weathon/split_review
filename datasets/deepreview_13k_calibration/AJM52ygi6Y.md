# Decentralized Optimization with Coupled Constraints

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
We consider the decentralized minimization of a separable objective $\sum_{i=1}^{n} f_i(x_i)$, where the variables are coupled through an affine constraint $\sum_{i=1}^n\left(\mathbf{A}_i x_i - b_i\right) = 0$.
We assume that the functions $f_i$, matrices $\mathbf{A}_i$, and vectors $b_i$ are stored locally by the nodes of a computational network, and that the functions $f_i$ are smooth and strongly convex. 

This problem has significant applications in resource allocation and systems control and can also arise in distributed machine learning.
We propose lower complexity bounds for decentralized optimization problems with coupled constraints and a first-order algorithm achieving the lower bounds. To the best of our knowledge, our method is also the first linearly convergent first-order decentralized algorithm for problems with general affine coupled constraints.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies decentralized optimization with constraints. It establishes the lower bound for this problem, and develops algorithms to attain such lower bound. The main idea is to transform the original constrained decentralized problem into (20), and then rely on the algorithm APAPC to develop the optimal algorithm. Numerical algorithms are established to validate the theoretical findings.

### Strengths
This paper is well-written and presents several key strengths:

1. The reformulation from problem (1) to problem (20) is novel and insightful, providing a strong foundation for the development of an optimal algorithm.

2. It establishes the first lower bound for decentralized optimization under affine constraints.

3. The paper also develops an algorithm that attains this lower bound, demonstrating both the tightness of the bound and the optimal complexity of the proposed algorithm.

### Weaknesses
However, this paper has several notable weaknesses:

1. The novelty is limited. The core idea for constructing the optimal algorithm draws heavily from the APAPC algorithm (Salim et al. 2022a) and Chebyshev acceleration, a common technique in accelerated algorithms for unconstrained decentralized optimization. The authors combine these two techniques to create the proposed algorithm. While the combination is non-trivial, the individual components are well-established, and the paper does not sufficiently highlight the specific challenges in adapting these techniques to the constrained decentralized setting. The adaptation of Chebyshev acceleration, in particular, needs more justification, as it is not immediately obvious that it can be directly applied to the transformed problem (20) without additional considerations.

2. Another concern is the practical applicability of the proposed algorithm. While it achieves theoretical optimality, it is significantly more complex to implement than existing baselines. As shown in Algorithms 2-5, the proposed algorithm consists of multiple algorithmic blocks and introduces numerous hyperparameters—such as ρ, ν, δ, and p—that require tuning. The paper does not provide clear guidelines on how to choose these parameters in practice, and the sensitivity of the algorithm to these parameters is not explored. This lack of practical guidance significantly detracts from its value, as the theoretical optimality may not translate to good performance in real-world scenarios due to the difficulty of parameter tuning.

3. The numerical experiments are too trivial. The experiments are limited to a simple linear regression setup, which does not fully demonstrate the algorithm's capabilities or limitations. The experiments do not explore the performance of the algorithm on more complex problems, such as those involving non-convex objective functions or more complex constraint structures. Furthermore, the experiments do not provide sufficient evidence to support the theoretical claims, particularly the dependence on condition numbers. The lack of experiments on real-world datasets further limits the practical relevance of the numerical results.

### Questions
1. As noted in the introduction, unconstrained consensus optimization is a special case of problem (1). For this special case, can the complexity of Algorithm 2 be reduced to match the optimal complexity of the unconstrained consensus algorithm in (Scaman et al., 2017)?

2. In the simulation section, how do you tune the hyperparameters?

3. The simulation results appear somewhat limited. It is difficult to observe whether the complexity scales proportionally with $\sqrt{\kappa_f}$, $\sqrt{\kappa_A}$, and $\sqrt{\kappa_W}$, as established by Theorem 1. It would be beneficial to empirically validate the complexity of the proposed algorithm, particularly with respect to $\kappa_f$, $\kappa_A$, and $\kappa_W$.

4. It is recommended to evaluate the algorithm using more real-world datasets and more complex experiments, such as logistic regression.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the task of decentralized optimization under the coupled constraints setting. This setting is quite general, which recovers a wide range of existing problems such as the consensus problem, optimal exchange problem, etc. Using a multi-communication subroutine, the paper proposed a dual-loop algorithm that provably converges with fast and tight convergence guarantees.

### Strengths
The authors provided a solid discussion on the related literature, which clearly explained the relative position of this paper with respect to multiple approaches in the prior works. The introduction also was able to convince me the generalizability and significance of this work.

The theoretical results offered by the authors, if correct, is tight and optimal.

The connection between FL and decentralized optimization has long been established. The coupled constraints setting considered in this paper can be a good starting point for technical understanding of VFL.

### Weaknesses
Although the upper bounds and lower bounds are provided in this paper and is shown to be tight. The lower bounds is only applicable to a narrow class of algorithms represented by the proposed algorithm. There are other class of algorithms which could have been discussed.

The proposed algorithm uses a multi-communication algorithm in a dual-loop approach, where a subproblem must be solved with communication. Although the process is accelerated such that it is optimal, there exist studies in the decentralized consensus literature that utilize tools such as gradient tracking, ADMM, etc., and prove convergence with single-loop algorithms. This is also preferable in practice since the communication bottleneck is more apparent for modern optimization tasks. 

A more complex experiment with real data and even neural networks would be appreciated for VFL. Though it is understandably omitted since it would not satisfy any of the technical assumptions, it would still be nicer to see.

### Questions
Currently, the lower bound is based on the algorithmic structure of the proposed algorithm, where the communication round lower bound is dependent on all three condition numbers. Is there a way to get an algorithm that only requires operations that only depend on their own respective condition number?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies decentralized optimization with (affine) coupled constraints. This general formulation encompasses different applications, from energy networks to vertical (model-partitioned) federated learning. A complexity lower bound is given for this problem, as well as a matching (and thus optimal) algorithm. Both the algorithm and the lower bound are obtained through a reduction to the standard decentralized case, which is usually solved by introducing coupled constraints (the parameters from different nodes should be equal), and solving the constrained problem with a (primal-)dual approach. As such, the algorithm is based on APAPC (Salim et. al., 2022), and the lower bound directly proceeds from standard lower bounds. Adding extra coupling constraints is extremely natural in this case, and it is not surprising that using the same approach as for decentralized unconstrained optimization leads to similar results. The only care should be taken in how these extra constraints are added to ensure that the right quantities are communicated. Experiments demonstrate the (expected) superiority of the approach.

### Strengths
- Tight analysis (optimal algorithm + lower bound) 
- Efficient off-the-shelf algorithm
- Authors clearly state their contributions and how they leverage previous work

I believe the main strength of the paper is that it uses the right tools to close a gap in the existing literature, so that non-experts can then use the algorithms.

### Weaknesses
 - Rather incremental contribution. All results directly derive from existing ones on the reformulation from (10), which is rather natural (though not straightforward).

In the end, I have mixed feelings about this paper. The contribution is not particularly innovative or technically challenging, but it has the merit of existing, and gives a well-rounded solution to this problem that people can then use. Therefore, I believe it should be published somewhere, though I am not completely sure this is the right venue, which is why I slightly lean towards acceptance. However, I am not too familiar with ICLR standards so I am looking forward to the discussion phase.

### Questions
- Could you precise the results obtained on vertical federated learning (giving a simple corollary in some standard specific case for instance) so that people can compare their results directly with yours? Does it just correspond to $\kappa_A = 1$? How does this result compare with existing work in model-partitioned distributed optimization then?  
- Have you tried tuning the value of r in the experiments? What would be the impact?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose an algorithm for decentralized optimization with coupled constrains. Compared by most methods with proximal oracle, it is a first-order approach with a lower computational burden. The algoorithm is motivated on Chebyshev acceleration and Proximal Alternating Predictor-Corrector. The authors also provide the convergence analysis of the proposed algorithm in strongly-convex scenario and also proves that the proposed algorithm can reach the lower bound.

### Strengths
1. first order iterations.
2. match the lower bound.
3. suitable for different kinds of problems.

### Weaknesses
1. The presentation need to be improved. The contribution of the paper should be highlighted. And maybe it is more friendly for readers if the main algorithm is in Section 4, followed by the introduction of Chebyshev acceleration and Proximal Alternating Predictor-Corrector.

2. It seems that some existing results like [1] do not need the strongly-convex assumption. And the author fails to provide the convergence analysis without strongly-convex assumption.

3.  More experiments should be involved, including more problems with different coupled constraints. Some necessary comparison with algorithms developed for one kinds of constraints, like EXTRA in consensus optimization, should also be taken.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
3
