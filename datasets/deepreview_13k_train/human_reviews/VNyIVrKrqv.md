# Constrained Reinforcement Learning as Wasserstein Variational Inference: Formal Methods for Interpretability

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Reinforcement learning can provide effective reasoning for sequential decision-making problems with variable dynamics. Such reasoning in practical implementation, however, poses a persistent challenge in interpreting the reward function and corresponding optimal policy. Consequently, representing sequential decision-making problems as probabilistic inference can have considerable value, as, in principle, the inference offers diverse and powerful mathematical tools to infer the stochastic dynamics whilst suggesting a probabilistic interpretation of policy optimization. In this study, we propose a novel Adaptive Wasserstein Variational Optimization, namely AWaVO, to tackle these interpretability challenges. Our approach uses formal methods to achieve the interpretability of guaranteed convergence, training transparency, and sequential decisions. To demonstrate its practicality, we showcase guaranteed interpretability including a global convergence rate $\Theta(1/\sqrt{T})$ not only in simulation but also in real-world robotic tasks. In comparison with state-of-the-art benchmarks including TRPO-IPO, PCPO and CRPO, we empirically verify that AWaVO offers a reasonable trade-off between high performance and sufficient interpretability. The real-world hardware implementation is demonstrated via an anonymous video.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a distributional approach to infer a policy in the constrained reinforcement learning setting. The central idea is to alternatively perform Wasserstein variational inference (WVI) and distributional policy optimization (PPO-DR). WVI learns a variational approximation $q(a)$ to the optimality likelihood $p(O|\tau)$ (similar to the control as inference framework [1]) while PPO-DR maximizes the expected reward within the feasible region, and minimizes the expected constraint outside the feasible region (using distributional networks). The variational approximation $q(a)$ is represented by the critic distribution, while the Wasserstein distance is computed using the hypersurfaces given by the actor distribution. Overall, the idea of using adaptive GSWD for distributional constrained RL is interesting, and supported by theoretical and empirical results, but the work can be improved in terms of clarity.

### Strengths
1. Extensive discussion on convergence results
2. The variational inference process is interesting, and it minimizes a Wasserstein distance (better for distributional RL) while ensuring that the actor distribution is used in computing the distance.
3. Real world experiments

### Weaknesses
On page 3, last line: "where, upon satisfying the constraints, the agent enters a state considered as safe". In my understanding, in the expected constraint formulation (Equation 2), if the constraints are satisfied, then the policy is considered "safe". "Safe/unsafe" states typically refer to a CMDP formulation with constraint sets, i.e. a part of the state-action space is safe, and the rest is unsafe. While it is useful to obtain a graphical model framework equivalent to the control as inference framework [1], a more appropriate justification of Figure 1 should have been that the optimality variables are influenced by the constraint, rather than saying that the agent enters a safe state. This means that $p(\tau|O)$ becomes 0 as soon as the constraint is not satisfied in expectation. The authors do not model the probability in this way, but rather learn a policy by maximizing reward when within the feasible region, and minimizing constraint when outside the feasible region (to get within the feasible region). This makes sense intuitively, but equivalence to constrained RL (equation 2) is not formally established. The notion of optimality, as framed by the distribution $p(O|\tau)$, seems to conflate the idea of maximizing reward with satisfying constraints, yet these are separate objectives in constrained RL. Specifically, in the control as inference framework [1], the optimality variable is typically linked to the reward function, where $p(O_t = 1 | s_t, a_t) \propto e^{r(s_t, a_t)}$. It's unclear how this formulation is extended to incorporate constraints, especially when constraints are expected values over trajectories, rather than per-step conditions. The paper's approach of using a distributional policy optimization to minimize constraint violations outside the feasible region, while intuitive, does not directly translate to a probabilistic interpretation of optimality under constraints, as suggested by the graphical model in Figure 1. The optimality distribution $p(O|\tau)$ should ideally reflect the probability of a trajectory being both optimal in terms of reward and compliant with the expected constraints, which is not clearly formulated in the current approach. The current formulation seems to treat constraint satisfaction as a binary condition rather than a probabilistic one within the optimality framework.

### Questions
1. In Equation 1, isn't it more appropriate to use $p(\tau|\theta)$ instead of $p(s,a|\theta)$ for the second term of the right hand side? 
2. In equation 2, what is $b_i$? Maybe I missed it, but why are there two thresholds?
3. (Suggestion) Page 4, after equation 3: "$\tilde \theta$ are the returns from the actor networks" could be re-worded. Returns have a specific meaning in RL literature, and in this context, I think return just means the output of the actor network, and not the usual return. (please ignore if my understanding is incorrect)
4. Maybe I missed this, but how are the individual $p(L_i|D)$ obtained (in the flight task setup)?

**References**

1. Reinforcement learning and control as probabilistic inference: Tutorial and review, Levine (2018)

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Treating RL problems in terms of variational inference is a promising approach
to building interpretable policies, but it suffers from high computational
expense. In particular, the cost of computing distance metrics between
probability distributions over high dimensional spaces is intractable. This
paper proposes a new metric (A-GWSD) on probability distributions which can be
computed efficiently and used to solve RL-as-inference problems. This metric is
used to solve constrained RL problems. This algorithm is shown to theoretically
satisfy a global convergence property, and empirically achieves similar rewards
and constraint violation rates to state-of-the-art safe RL algorithms. In
addition, the proposed approach yields a clear interpretation of policy actions
based on conditional probability evaluation.

### Strengths
Interpretability is a key challenge in reinforcement learning, and this paper
offers a promising approach to providing explanations for agent behavior.

Constraints are also important in real-world reinforcement learning. This paper
proposes a way to extend a popular RL framework (RL as inference) to the
constrained setting.

The experimental results show that improvements in interpretability can be
achieved with minimal sacrifices in terms of rewards or constraint violations.

### Weaknesses
Given that the main improvement over prior work is in intpretability, I would
have liked to see more discussion of interpretability in the experimental
results. There is some information in Figure 4 (but see the questions below),
but I think the paper would benefit from some discussion of intepretability in
the other environments.

I found it difficult to understand Figure 4, which is where the key advantage of
this approach over prior work is shown. Some explanation of why this diagram is
evidence of improved interpretability would be helpful. I can see that roughly
speaking, when the wind estimation in 4(a) is higher, the probability in 4(b) is
higher as well, which demonstrates some sensitivity to the wind. But the two
graphs do not line up that closely and I'm not sure if I'm interpreting them
correctly. What should I be looking for in this figure?

### Questions
I found it difficult to understand Figure 4, which is where the key advantage of
this approach over prior work is shown. Some explanation of why this diagram is
evidence of improved interpretability would be helpful. I can see that roughly
speaking, when the wind estimation in 4(a) is higher, the probability in 4(b) is
higher as well, which demonstrates some sensitivity to the wind. But the two
graphs do not line up that closely and I'm not sure if I'm interpreting them
correctly. What should I be looking for in this figure?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the methodology of addressing constrained reinforcement learning by framing sequential decision-making problems as probabilistic inference problems. The focus is on utilizing the Wasserstein distance as a measure to discern the difference between the approximate posterior distribution of the trajectories and the posterior conditioned on the optimality operator. However, due to the computational intractability of the Wasserstein distance, the study employs the Generalized Sliced Wasserstein Distance (GSWD) as a proxy for the original distance. This is subsequently expanded by incorporating a neural network to determine the hyperparameters in GSWD, resulting in a metric named the Adaptive Generalized Sliced Wasserstein Distance (AGSWD).

In the development of the algorithm, the paper introduces a distributional representation to represent the cumulative rewards' distribution. The Distributional Bellman operator is then utilized to upate the critic function within the algorithm. The paper also provides theoretical results for the method, demonstrating that AGSWD is a metric and justifying the global convergence as well as the convergence rate.

Moreover, the paper conducts empirical studies on the performance of the proposed algorithm within both a simulated robotic control environment and a realistic Unmanned Aerial Vehicle control environment. These results highlight a leading convergence rate and robust, safe control performance.

### Strengths
1. The overall structure of the paper is generally easy to follow.

2. The paper adeptly integrates a multitude of concepts such as Wasserstein distance approximation, interpretability, distributional Reinforcement Learning (RL), variational inference, constrained RL, and probabilistic inference. These topics have been at the forefront of recent research trends.

3. The empirical results emphasize the superior performance of the proposed Adaptive Wasserstein Variational Optimization (AWaVO) relative to other baseline models in both simulated and realistic environments. This underscores the practical effectiveness of the proposed methodology in real-world applications.

### Weaknesses
1. This paper covers a wide variety of concepts. However, there seems to be issues with key definitions and notations, which remain ambiguous or undefined, thus making several key ideas challenging to comprehend. For instance:

- In Formula 2), the subscript 'i' is left undefined, and $b_i$ is also undefined. It is unclear if $b_i$ represents a fixed constraint limit or a dynamic tolerance level, and how these values are determined for different tasks.

-  In Section 4.1, the definition of $q_\theta$ appears flawed. There seems to be a duplicate probability over '$a$'. The second term should likely be $p(s|a,\theta)$ instead. The current formulation of $q_\theta(\tau) = q(a)p(s,a|\theta)p_D(\theta)$ is not a valid probability distribution over trajectories, and the role of $q(a)$ as an approximation of the optimality likelihood is not clearly derived.

- In Section 4.1, the definition of $p(\tau|O)$ seems incorrect. The term "equivalence" should likely be replaced with "proportional to" (please refer to formula (1)). The use of "equivalence" is mathematically inaccurate, as the posterior is proportional to the product of the likelihood and prior, not strictly equivalent.

- Formula 3) is incomprehensible without the definitions provided in the appendix. The hyperparameter $l$ and the function $\mathcal(G)$ are undefined in the formula and its introductory explanation. It would be helpful to move this content from the appendix into the main body of the paper. The lack of clarity hinders understanding of how the Generalized Sliced Wasserstein Distance (GSWD) is applied.

- In Formula 3), it's unclear what the omitted term in $\cdot$ is. According to the appendix, it's supposed to be a hyperparameter $l$. If that's the case, it's generally inappropriate to omit the hyperparameter in the formula. This omission creates ambiguity and makes the mathematical formulation difficult to follow.

- The definition of $R_\mu(l,\tilde{\theta})$ in the appendix is also confusing. Please verify whether the $x$ in the formula should be $\mu$ and provide clarification. The use of $x$ in the definition is inconsistent with the notation used elsewhere, and it is unclear why the integration is over $x$ rather than $\mu$.

- In Section 4.2, for consistency with the expectation in the objective (4), there should be an expectation in the definition of the trajectory reward $\tilde{r}(\tau)$. Or is it intended to be the random variable of cumulative rewards, with the aim being to estimate the distribution? If so, perhaps it should not be termed a function. The lack of clarity on whether $\tilde{r}(\tau)$ is a deterministic function or a random variable makes the objective function ambiguous.

- The inference step of $p(\theta|D)$ in Algorithm 2 needs clarification. Its reference cannot be found in Section 3. Please specify the exact location or formula. Please also distinguish between $\theta$, $\theta^\mu$, and $\theta^Q$. The rationale behind employing different updating methods for $\theta$ and the others also needs to be elucidated. The algorithm description lacks sufficient detail on how the parameters are updated, and the distinction between the different parameter sets is unclear.

Typos:
- The "hupersurface" before the formula (3) -> hypersurface.
-  In Section 4.2, the defintion of $\tilde{g}_i(\tau)$ lacks a square bracket on the right.


2. The theoretical results appear to lack key assumptions. Many conclusions are questionable and would benefit from further contemplation.

- The proof of Proposition 1 claims that A-GSWD is a pseudometric rather than a metric. More significantly, it's questionable whether the proof can leverage the fact that "Wasserstein distance is a metric," given that A-GSWD is defined between $\mu$ and $\nu$, not $\mathcal{G}\mu$ and $\mathcal{G}\nu$. If you swap $\mu$ and $\nu$, their corresponding hyperparameters in $\mathcal{G}$ (as output by the neural network) will not be interchanged. Thus, symmetry might not generally hold. The proof of symmetry is not rigorous, as the neural network parameters are not considered when interchanging $\mu$ and $\nu$.

- In the proof of Proposition 3, the expectation following the max operator should be eliminated. If the action is selected based on an existing policy, the max operator becomes irrelevant. The presence of the max operator is inconsistent with the policy evaluation step, as the expectation should be over the current policy, not the optimal one.

- In Equation (16), the first inequality does not generally hold. It often holds when $\pi_{new}$ corresponds to the argmax Q in the Bellman optimality function. This point needs clarification. The inequality is not valid for arbitrary policies and requires specific conditions, which are not stated.

- The Wasserstein distance cannot be related to the discrepancy between quantiles in (18) unless $p$ (parameter) and $d$ (dimension) are both 1 in Wasserstein distance. The connection between the Wasserstein distance and the quantile discrepancy is not generally valid and requires specific assumptions on the dimensionality of the distributions.

- In Formula (19), Lemma 5.1 in Cai et al. (2019) relies on the linearity of the action-value function, which does not generally apply in value networks. The application of Lemma 5.1 is not justified, as it relies on a linearity assumption that is not generally satisfied by neural network value functions.

3. The empirical results lack certain key definitions, and their credibility is questionable in several respects:

- The constraint limit in the plots is undefined. Is this intended to represent the tolerance? The meaning of the constraint limit is not clear, and it is not explained how this limit is related to the task constraints.

- In Figure 3, the plots for cartpole, walker, and guard do not seem to demonstrate signs of convergence. The curves are still rising. An early stop might give the impression that the baseline methods are inferior, but they could potentially surpass the proposed method in the end. The incomplete nature of these experiments means that no definitive conclusions can be drawn. The experiments do not provide sufficient evidence to support the claims of superior performance, as the convergence is not clearly demonstrated.

4. **Motivation.** The implementation of distributional Reinforcement Learning (RL) in this paper lacks a clear rationale. Despite its application, it remains unclear why it's necessary and what benefits it brings to the study.

5. **Novelty.** While the introduction of AGSWD stands as a significant contribution, given that GSWD has already been investigated, simply integrating GSWD with neural network outputs doesn't constitute a major advancement in the field.

### Questions
- How should we interpret $g_{rl}$? Its role in Formula (3) isn't clear. Is it intended to be a hyperparameter that defines the plane on which $\Tilde{\theta}$ lies? Or is it a term returned by the RL algorithm?

- In the proof of Proposition 3, what is the relationship between the operators and the new and old policies? Is the output of the operators meant to be the new policy? And, what does $\pi^{\prime}$ represent?

- In Formula (18), what does the symbol $H$ denote?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
