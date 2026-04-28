# Stochastic Semi-Gradient Descent for Learning Mean Field Games with Population-Aware Function Approximation

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Mean field games (MFGs) model the interactions within a large-population multi-agent system using the population distribution.
	Traditional learning methods for MFGs are based on fixed-point iteration (FPI), which calculates best responses and induced population distribution separately and sequentially.
	However, FPI-type methods suffer from inefficiency and instability, due to oscillations caused by the forward-backward procedure.
	This paper considers an online learning method for MFGs, where an agent updates its policy and population estimates simultaneously and fully asynchronously, resulting in a simple stochastic gradient descent (SGD) type method called SemiSGD.
	Not only does SemiSGD exhibit numerical stability and efficiency, but it also provides a novel perspective by treating the value function and population distribution as a unified parameter.
	We theoretically show that SemiSGD directs this unified parameter along a descent direction to the mean field equilibrium.
	Motivated by this perspective, we develop a linear function approximation (LFA) for both the value function and the population distribution, resulting in the first population-aware LFA for MFGs on continuous state-action space.
	Finite-time convergence and approximation error analysis are provided for SemiSGD equipped with population-aware LFA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper primarily concentrates on the development of a stochastic gradient method for learning in mean-field games.
The proposed algorithm significantly reduces the computational cost associated with calculating the population distribution.
Moreover, the author demonstrates that under certain standard assumptions, the proposed algorithm converges to a stationary point.
Additionally, the algorithm's performance is validated experimentally in various mean-field games.

### Strengths
* The problem is well-motivated. Eliminating the forward-backward process of learning algorithms for mean-field games is significantly important.
* The proposed algorithm has a strong convergence guarantee with a rate.

### Weaknesses
My primary concern is that the definition of the mean-field equilibrium in this study differs from that in existing studies.
Specifically, this study considers the Bellman operator, as opposed to the commonly used Bellman optimality operator.
Hence, I believe that there is no guarantee for the agent to maximize the expected cumulative discounted reward in the mean field equilibria.
In the context of learning in multi-agent systems, it seems more natural to consider maximizing the expected cumulative discounted reward.
Consequently, I'm wondering why the current definition of equilibrium was considered in this study.
Is it possible to extend the provided theoretical results to the reward-maximizing setting?
If not, I don't think we can fairly compare this study with existing studies on mean-field games.

Additionally, I believe that a more detailed explanation of the numerical experiments is necessary.
For example, I'm curious why exploitability was reported for the flocking game, despite the fact that reward maximization is not the main focus of this study.



### Questions
My main concerns and questions are outlined in Weaknesses.
Additionally, I have the following question:
* I am not sure how Assumption 5 is relatively weaker than Assumption 4. Could you provide a more intuitive explanation of Assumption 5?

### Soundness
2

### Presentation
3

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
In this paper, a numerical method for mean field games is proposed. Mean field games games approximate Nash equilibria for games with many players. Here, the proposed method relies on stochastic semi-gradient updates. Theoretical convergence is proved and numerical illustrations are also given.

### Strengths
The paper is relatively clear and the algorithm is new, to the best of my knowledge. The convergence analysis includes sample complexity. The experiments cover different examples and contain a few baselines.

### Weaknesses
I understand that empirical convergence is observed beyond the assumptions, but still: it is not clear to me how to check these assumptions in practice.
In the numerical examples, the baselines could be explained more clearly.

### Questions
Q1: Theorem 2: Please provide an example satisfying the assumptions of this theorem.

Q2: Section 7: Can you please explain what is FPI+MD? Is it the same as the online mirror descent of (Perolat et al., 2021)? If not, please compare with this algorithm, which is known to empirically converge much faster than fictitious play-type iterations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript goes beyond existing fixed-point iteration (FPI) methods for solving mean field games, by treating the mean field and agent policy jointly instead of performing forward and backward updates. Here, FPI-type methods are understood as those computing the full forward and backward equations for mean field and optimal policies. The advantage is allowing asynchronous updates to both, which can lead to improved results. An analysis of the resulting semi-gradient descent method is performed under linear models and varying sets of assumptions. Empirically, the designed algorithms are further demonstrated on a variety of problems.

### Strengths
- The paper is well written and relatively clear despite the subject matter. 
- The analysis is novel, interesting and extensive, e.g., the combination of linear approximations with MFGs and producing finite-time error bounds, or the convergence results without (directly) assuming contractivity or monotonicity.
- Empirically, the approach appears to be able to outperform existing approaches in some of the demonstrated problems in terms of exploitability. Further, the method is practical, as it is applicable in an online manner to unknown models. 
- The introduction of synchronous updates as opposed to forward-backward computations seems somewhat significant to the study of MFG learning algorithms, as it allows for improved sample complexity and better empirical results.

### Weaknesses
 - The approach seems to be limited to stationary mean field games, i.e. ones with time-stationary mean fields. This does not match with the compared / referenced literature, of which most are for non-stationary cases. 
- For the theoretical results, there remain limits in terms of significance, as also discussed by the authors. The significance of theoretical results is limited due to the requirement of strong assumptions such as linear models and regularized solutions.
- Some minor issues (incomplete / TeX errors) in references.
- Some points remained unclear to me, see questions below.

### Questions
- Uniqueness of solutions seems to not be required. How it is possible that we obtain convergence in the presence of non-unique MFE? Does the theory imply convergence to multiple MFE, or is uniqueness implicitly assumed?
- What is the reasoning behind replacing $M_*$ (the non-unique? unknown MFE) by bootstrap estimates under the current policy (before Eq. (3))? Why can the current policy produce estimates for the mean field $M_*$ of the MFE?
- The methodology does not directly optimize exploitability, what is the difficulty in instead using "true" gradients on the unified parameters to minimize exploitability?
- Can you extend similar techniques to non-time-stationary MFGs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies learning equilibrium policy in mean-field game. The authors propose semiSGD, a SGD style online algorithm, where they treat the policy and population as a unified parameter. For linear MFGs, under small Lipschitz factor case, they establish convergence analysis. Besides, when the Lipschitz factor of the problem is relative large, they show the algorithm converges to the neighborhood of Nash, whose radius scales with the Lipschitz factors.

### Strengths
It seems interesting to me the idea that considers the policy and population parameters as a unified parameter to optimize.

The assumptions are clearly stated, and some explanations are provided. 

Numerical experiments are provided.

The comparison in Table 2 provides a good summary.

### Weaknesses
1. **About assumptions**: I think the authors should provide some justification about why it is reasonable to consider Assumption 2. In the more standard MFG setting, the equilibrium policy is defined to be the policy that no agent can deviate and increase its value, which correspond to the setting $\Gamma_\pi(Q)(\cdot|s) := \arg\max_a Q(s,a)$. However, Assumption 2 can not cover this setting with finite $L_\pi$, because of the discountinuity of the argmax operator.

    As implied by Assumption 2, the paper seems to consider a "smooth" version of standard Nash equilibrium. It is unclear that why this objective is of interests to study, and also what's the relationship between it and the standard Nash equilibrium. The authors should clarify whether this smooth version is an approximation to the standard Nash equilibrium, and if so, under what conditions this approximation is valid. Furthermore, it would be helpful to discuss the practical implications of using a smooth policy operator, especially in scenarios where the true underlying policy is inherently non-smooth.

2. **Comparison with Assumptions in previous work**: this paper consider contraction style assumptions to establish the convergence. Although in remark 2, the authors provide some discussion to justify the assumptions, it is still unclear to me how they compare with previous works. For example, does the contractivity assumption in [1] can be recovered as a special case by choosing some specific parameters in Assumption 2 and 4? Or maybe comparing with [2], which ensures contractivity by introducing the regularization, would Assumption 2 or 4 be satisfied by introducing large enough regularization? A more detailed comparison is needed, specifically outlining how the Lipschitz constants in Assumptions 2 and 4 relate to the regularization parameters used in prior work. It would also be beneficial to discuss whether the assumptions in this paper are more or less restrictive than those in existing literature, and under what conditions each set of assumptions is more appropriate.

3. **When Theorem 2 is meaningful?** Theorem 2 suggests the convergence with bounded bias. I think it is necessary to have some discussion about the magnitude of the bias term comparing with another algorithm randomly compute $\xi_T$. For instance, can you provide some examples when the bias term can be (much) lower than $\|\xi^*\|$, which suggests the algorithm is better than a random guess by directly assigning $\xi_T = 0$. It is also unclear how the magnitude of the bias term scales with the problem parameters. A more detailed analysis is needed to determine the conditions under which the bias term is small enough to ensure meaningful convergence. Furthermore, the authors should provide some intuition about how the algorithm behaves when the bias term is large, and whether there are any strategies to mitigate the impact of a large bias. 

    It is also unclear how large $\bar{w}$ is. Given that $\bar{w}$ is a problem-dependent constant, can you explain when $\bar{w}$ can be large or small? That would be helpful to understand when Theorem 2 is meaningful and when it is vacuous. Specifically, what properties of the problem (e.g., the state space, action space, reward function, or transition dynamics) influence the magnitude of $\bar{w}$? Are there any practical examples where $\bar{w}$ is known to be either very large or very small, and what are the implications for the convergence of the algorithm in these cases?

### Questions
1. In Assumption 5, $w$ is introduced to denote the upper bound of $\bar{w}$. However, it does not appears in Theorem 2. So what's the reason to mention such an upper bound?

### Soundness
2

### Presentation
3

### Contribution
3
