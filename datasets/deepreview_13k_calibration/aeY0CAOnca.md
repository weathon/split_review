# Mitigating Suboptimality of Deterministic Policy Gradients in Complex Q-functions

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
In reinforcement learning, off-policy actor-critic approaches like DDPG and TD3 are based on the deterministic policy gradient. Herein, the Q-function is trained from off-policy environment data and the actor (policy) is trained to maximize the Q-function via gradient ascent. We observe that in complex tasks like dexterous manipulation and restricted locomotion, the Q-value is a complex function of action, having several local optima or discontinuities. This poses a challenge for gradient ascent to traverse and makes the actor prone to get stuck at local optima. To address this, we introduce a new actor architecture that combines two simple insights: (i) use multiple actors and evaluate the Q-value maximizing action, and (ii) learn surrogates to the Q-function that are simpler to optimize with gradient-based methods.
We evaluate tasks such as restricted locomotion, dexterous manipulation, and large discrete-action space recommender systems and show that our actor finds optimal actions more frequently and outperforms alternate actor architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the *Successive Actors for Value Optimization (SAVO)* algorithm, addressing the non-convex Q-function landscapes. The claim is that in high-dimensional and multimodal action spaces, Q-functions often exhibit numerous local optima, making it difficult for gradient ascent-based actors to discover globally optimal actions. This issue can lead to poor sample efficiency and suboptimal policy performance, even when the Q-function is accurate.

SAVO tackles both continuous and discrete action settings (recommender systems). However discrete actions are mapped to a continuous representation space.

SAVO employs two main techniques: 
- **Maximizer Actor**: It instroduces a maximizer actor $\mu_M(s)$ that selects actions from a set of action proposals based on the higher Q-value. Proof has been provied that this method converges in the tabular setting and show that $\mu_M(s)$ is at least as good as the base policy $\mu$ based on the policy improvement theorem. This leads to a multi-actor architecture.
- **Successive Surrogates to Simplify the Q-Landscape**: Inspired by tabu search, SAVO progressively filters out suboptimal regions in the Q-landscape. By “tabu-ing” low Q-value areas, it reduces the number of local optima, thereby making gradient ascent more effective.

### Strengths
- Ensemble of Actors: The ensemble-style actor, which combines policies and selects actions based on the highest Q-values, is novel afaik.
-  The surrogate Q-functions inspired by tabu search could potentially improve gradient-based optimization by reducing the number of local optima in the action space.
- The convergence proof for the maximizer actor in the tabular setting has been provided, although I did not have time to check in-depth.

### Weaknesses
 - Quality of Action Proposals: I'm wondering whether the quality of action proposals from additional policies $v_i$ could affect the effectiveness of the maximizer actor? If these proposals are not close to the optimal actions, the maximizer actor’s effectiveness is limited, as it can only select from the actions provided. In other words, the performance of the maximizer actor is capped by the quality of these action proposals.

- The effect of smoothing in highly dynamical environments : In rapidly changing Q-landscapes, the surrogate-based tabu regions may become outdated, potentially causing the actor to miss newly optimal regions. A sensitivity analysis on surrogate accuracy could clarify whether this might be happening (specially with the more complex and dynamical tasks where the performances are mediocre)

- Empirical Results: While results in Figure 8 show slight improvements on simpler tasks (e.g., Hopper, Inverted Pendulum), Figure 15 shows that SAVO’s performance on more complex tasks (e.g., Ant, HalfCheetah) is only on par with other methods, without demonstrating a clear advantage.
Same trend is observed for results on recommender system in Figure 20 and Figure 22.

Overall the empirical results in this paper are not compelling enough to show a clear advantage of SAVO over existing methods. Across tasks, the results show that SAVO often performs on par with or worse than baseline methods, failing to convincingly outperform them. Therefore it’s unclear to me whether the proposed strategy is genuinely addressing suboptimal behavior or simply matching baseline performance without significant improvement. This leaves some doubt about the effectiveness of the approach in achieving better optimization in complex Q-landscapes.

### Questions
- How is the quality of the surrogate Q-landscape monitored to avoid filtering out high-reward regions? Is there a mechanism to re-evaluate excluded areas if necessary?
- Figure 9 Plot: The third plot in Figure 9 appears misaligned, with lines and text outside the figure’s bounds.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary Of The Paper:

The paper develops a method to mitigate actors from getting stuck in a locally optimal Q value. Their proposed method considers producing surrogate estimates of the Q landscape based on the last seen maximum Q value, and restricts the actor from making actions in local optima through a successive actor architecture.

### Strengths
The paper is easy to read, and generally well written and is well motivated by the issue of converging to a local optima.

The idea of restricting local optimal using tabu search in this successive manner is very interesting.

The idea appears fairly novel. The closest work to this is probably SAC, although this paper is quite a bit different in motivation. This helps with novelty.

### Weaknesses
### Weaknesses

1. The complexity of the true underlying Q function should affect how many surrogates are needed. There should be an analysis or heuristic on how to determine the optimal or necessary number of surrogates needed for a particular task. This will also determine the computational viability of SAVO, in situations where we might require several surrogates to converge to global optima. The paper lacks a clear methodology for selecting the number of surrogates, and it's unclear how this choice impacts performance and computational cost. A more rigorous analysis is needed to understand the relationship between Q-function complexity and the required number of surrogates.

2. The experiment environments are quite simplistic with only one set of 3D environments. There needs to be more analysis on how this method works with high dimensional continuous state and action spaces, especially because here Q would be a function of these high dimensional parameters. In SAC’s original paper, they baseline with Ant and humanoid, and SAVO should be compared to those environments as well. Since SAC is another method that proposes to exit local optima with the stochastic actor and entropy objective, a full comparison between SAV + DDPG/TD3 and SAC (+ SAVO) should be done. The experiments should include a wider range of environments with varying complexities in both state and action spaces. The lack of comparison with SAC in more complex environments is a significant gap.

3. Surrogates are trained via L2 loss. How do we know if the surrogates have approximated modified Q function sufficiently? What if there are margins of errors that potentially result in the surrogates converging to local optima. Then how do we diagnose or detect these problems? It seems like SAVO involves increasing the number of hyperparameters that require tuning. How sensitive is the training regime of the surrogates, and at what point do they yield no benefit compared to the baseline architectures? How do the design choices of the surrogates impact the stability of training? This method adds a lot of overhead on top of something like DDPG. That's my biggest worry about the paper. The paper does not provide sufficient analysis on the accuracy of the surrogate Q-function approximations. The impact of approximation errors on the overall performance and stability of the method is not well understood. The sensitivity of the method to the surrogate training regime and design choices needs to be thoroughly investigated.

4. It would be nice to better understand the generalizability of SAVO to other environmental regimes. How does SAVO perform in sparse reward environments? It seems that SAVO is highly dependent on how well we estimate the truncated Q through surrogates. It would be helpful to see how SAVO can help with improving HER or other actor critic architectures. The paper lacks an analysis of SAVO's performance in sparse reward environments, which are common in real-world applications. The potential for SAVO to be combined with other actor-critic architectures, such as those using HER, is not explored, limiting the understanding of its broader applicability.

### Questions
Section 4.3 defines \nabla \Psi as a function of \nabla Q. Is \Psi simply Q + constant with the truncation term?

### Soundness
2

### Presentation
2

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
The paper presents a new actor architecture that combines multiple actors and simplified Q-function surrogates. The new method eases the challenge of maximizing Q-function in complex tasks like dexterous manipulation and restricted locomotion.

### Strengths
1. The paper has a clear motivation for the challenge of maximization Q-function in commonly used deterministic policy gradient algorithms. Figures 1-3 are all strong evidence of this problem. 
2. The paper is well-written. Especially for the transition from Section 3 to Section 4, the connection is quite natural. The introduction of the main method of SAVO is also clear. 
3. The extensive experiments (5 environments) also strongly prove the effectiveness of the SAVE architecture. 
4. It is very appreciated that the authors also mention about the potential limitations in the inference time of the proposed method. I think it's a nice trade-off between better optima and computational efficiency.

### Weaknesses
1. The surrogate value function also requires a smooth version to improve performance. Is it also possible to add smoothness to the origianl Q-value? It would be helpful to add it as a baseline.


### Questions
1. The diversity of policy function $\nu$ and surrogate value function $\Psi$ will have a large influence on the algorithm's final performance. For the policy, do special initialization techniques increase the diversity of the policy and improve its performance? For the value function introduced in 4.4, is $Q(s, a)$ different from $Q^{\mu_M}(s,a)$ with separate neural networks? Besides, both policy and value function requires conditional input on the previous action. How to deal with the variational number of inputs? 
2. If the action dimension is large, maximizing Q-function could be even harder. Do you recommend using the SAVO method could potentially require more agents?

### Soundness
2

### Presentation
3

### Contribution
3
