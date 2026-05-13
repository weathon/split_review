# RegQ: Convergent Q-Learning with Linear Function Approximation using Regularization

- Decision: Reject
- Scores: 8, 6, 5, 5

## Abstract
Q-learning is widely used algorithm in reinforcement learning community. Under the lookup table setting, its convergence is well established. However, its behavior is known to be unstable with the linear function approximation case. This paper develops a new Q-learning algorithm, called RegQ, that converges when linear function approximation is used. We prove that simply adding an appropriate regularization term ensures convergence of the algorithm. Its stability is established using a recent analysis tool based on switching system models. Moreover, we experimentally show that RegQ converges in environments where Q-learning with linear function approximation has known to diverge. An error bound on the solution where the algorithm converges is also given.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of instability of $Q$-learning with linear function approximation. The paper shows that the ridge regularization of the parameters is enough to guarantee convergence of $Q$-learning. The quality of the solution is the upper-bounded.

### Strengths
This paper shows that simply regularizing the $Q$-learning with linear function approximation update by penalizing the weights in the 2-norm is enough to guarantee convergence. Even though other works had hinted at this insight, specifically Zhang~2021, in this work the contribution is distilled, in the sense that previous work had not only the ridge regularization but also other additions to the update. 

The paper is clearly written and easy to follow. The switching systems technique used is also less common than just using the o.d.e. analysis, which makes the paper possibly technically more interesting.

### Weaknesses
While there is an upper bound on the quality of the regularized solution, it is important to understand if the regularization can make $Q$-learning useful in non-trivial environments. The experiments only show convergence to the correct solution in trivial environments. Nevertheless, this experimental validation could be seen as future work. 

The work of Chen 2022 as hinted that regularizing the $Q$-learning objective can sometimes be seen as lowering the discount factor. If this is the case, it is uninspiring because low discount factors are known to lead to the convergence of $Q$-learning. These insights are not discussed in the paper.

Minor: the related work discussion in the introduction is confusing. Comparison with related work appears on the second, third, fourth and fifth paragraph, and some times it is repetitive. I think the paper would benefit from using the introduction for motivation and context and having a separate section for discussion with related work.

### Questions
- do the authors believe the method will be useful in practice, or that the regularization introduced will harm the quality too much? Have the authors performed more experiments to understand this?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new algorithm called regQ for reinforcement learning. The existence and uniqueness of the associated stochastic approximation problem is proved. By leveraging recent ODE-based analysis, the authors show the convergence of the updating rule. Numerical experiments are conducted to evaluate the algorithm performance.

### Strengths
1. The paper is overall well-written and easy to follow.
2. The paper proposes a new algorithm, and the authors analyze the convergence.
3. Numerical experiments are provided.

### Weaknesses
1. Seemingly, the novelty is an additional regularization term in the TD error to ensure the existence and uniqueness of the solution. It is unclear whether this new algorithm is better than vanilla Q-learning.
2. Although convergence of the regQ is provided, the paper does not show whether one can learn the optimal state-action value function $Q^*$ well. Indeed, we do not know whether the $Q$-value associated with $\eta > 0$ converges to the optimal $Q^*$ of the MDP problem when $\eta$ goes to zero.
3. The experiment setting cannot reflect the practical need. More comprehensive comparison with benchmarks is necessary.

### Questions
1. It is not clear whether linear function approximation makes analysis much harder. What are the technical difficulties in the convergence analysis?
2. Do you have a sample complexity analysis of regQ? For Q-learning algorithms, both asymptotic and non-asymptotic analyses are well-understood.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on the Q-learning algorithm solving the problem of finite-state finite action MDP with linear approximation. Although the convergence of the lookup table based Q-learning is well-established, the linear approximation based Q-learning is known to be unstable for certain cases/examples. This paper proposes a new Q-learning algorithm by adding an additional regularization term to stabilize the learning process and proves that it will converge to a unique solution asymptotically. The author/s also show the proposed algorithm's effectiveness in solving the examples that previous Q-learning algorithm usually fails to converge.

### Strengths
1. The new proposed Q-learning algorithm is proven to be stable and asymptotically converge to a unique solution compared to the previous Q-learning methods in linear approximation setup.
2. The paper also gives a bound on the error between the estimated action value function and the optimal one, which consists of two terms: the error originated from the added regularization term and the error from the difference between the optimal Q value function and the one after feature vector projection.

### Weaknesses
1. Although it's good to have a new algorithm in linear approximation Q-learning to converge to a unique solution asymptotically, the added regularization term increases the error bound between the estimated action value function and the optimal one. Based on the result in Lemma 3.2, it's not clear how the \eta parameter should be chosen. A relatively small \eta could potentially have very small denominator in the RHS, causing big error bound. Instead, if the \eta is chosen super big, the error tends to remain the same. The experiment in the Appendix also shows the larger \eta helps with the convergence rate. Does that mean we should always use a super big \eta? 
2. The added regularization + asymptotic analysis seems not requiring that much effort given the previous works on Q-learning about O.D.E. analysis, switching system, and off-policy TD-learning.

### Questions
Based on the experiment in the Appendix, larger \eta seems to be helping increase convergence rate and reduce the estimation error. Does that mean we should always go with larger \eta value?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces RegQ algorithm for Q-learning with linear function approximation. They introduced a regularization term in the Q-learning update (based on project bellman equation), which renders existence of solution to the modified target equation. They then proved boundedness (stability) and convergence of  their proposed algorithm. They also demonstrated their algorithm converges faster on some examples (the Baird star example).

### Strengths
quality: They used linear switching system theory to prove stability of the proposed RegQ algorithm (Thm 5.1), while many convergence proofs of Q-learning algorithms need to assume stability.

### Weaknesses
novelty and significance:
1. Adding regularization term to linear system to obtain/enhance solution is a common idea. I believe the real question is the performance of the resulting solution in terms of cumulative rewards or policy performance, which is ultimately what we care about. This paper only shows convergence of the algorithm to some solution, but the quality of that target solution resulting from regularized projected Bellman equation is not analyzed.

related work:
The paper missed some recent results on Q-learning with linear function approximation. S. Meyn showed existence of solution to projected Bellman equation with linear function approximation (and a stable algorithm) under assumptions of behavior policy.

ref:
S. Meyn, Stability of Q-Learning Through Design and Optimism, https://arxiv.org/abs/2307.02632, 2023

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
