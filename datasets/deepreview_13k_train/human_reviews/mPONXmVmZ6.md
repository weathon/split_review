# Multi-Agent Interpolated Policy Gradients

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Policy gradient method typically suffers high variance, which is further amplified in the multi-agent setting due to the exponential explosive growth of the joint action space.
While value factorization is a popular approach for efficiently reducing the complexity of the value function, integrating it with policy gradient to reduce variance is challenging, as bias is introduced due to the limitations of factorization structure.
This paper addresses the underexplored bias-variance trade-off problem by proposing a novel policy gradient method in MARL that uses a convex combination of joint Q-function and a factorized Q-function. This results in a policy gradient approach that balances stochastic and factorized deterministic policy gradients, enabling a more flexible trade-off between bias and variance. Theoretical results validate the effectiveness of our approach, showing that factorized value functions can effectively reduce variance while potentially maintaining low bias.
Empirical experiments on several benchmarks demonstrate that our approach outperforms existing state-of-the-art methods in terms of efficiency and stability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the setting of multi-agent reinforcement learning and proposes the method Multi-Agent Interpolated Policy Gradient which allows for trade-off between variance and bias. Theoretical analysis of the proposed method gives an expression for the variance of the gradient and shows the effectiveness of the method in reducing variance. An upper bound on the bias introduced by incorporating a factorized Q function is also given and it is shown how by tuning a parameter bias and variance can be balanced. Finally empirical results are presented that compare the performance of the proposed method with other baselines and also ablation studies are conducted that study the effect of various design choices.

### Strengths
The proposed method uses a control variate, in this case factorized Q function, to reduce the variance of the policy gradient. The idea has been explored in the setting of single agent reinforcement learning and the paper extends it to multi-agent setting. Although the idea behind the main method is not original it is still a solid one and the extension of the same to multi-agent setting is significant. 

The main body of the paper is presented clearly for most part and the flow of the contents is also natural.

### Weaknesses
The empirical results for the proposed method are not convincing. Although in GRF domain the proposed method gives better performance as compared to baselines the same is not true for the SMAC domain. If results on another benchmark could be provided it would make the empirical results stronger.



### Questions
1. In Algorithm 1, you mention that you use recurrent neural networks in policy networks $\pi_\theta$, state-value networks $V^\varphi$ and action-value networks $Q^\psi$. Given that in your setting each agent observes the whole state I don't see why you need it? Also, how would the performance be affected by its absence?

2. In proof of Proposition 2, you prove equation 19 first and then use that to rewrite eq. 10. What are the intermediate steps involved in this?

3. Effect of bias on the performance of the algorithm: Does a low value of $\nu$ give a better performance in most of the scenarios? I know that the effect of $\nu$ is investigated in ablation studies but since the number of experiments there is small I was wondering if the behavior seen in ablation studies holds in general or not.

4. For the GRF domain, QMIX was not included in the baselines. Is there a reason for this?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to explore the bias-variance trade-off of the policy gradient in MARL, this paper considers a convex combination of the joint Q-function (with coefficient $1- \nu$) and a factorized Q-function (with coefficient $\nu$) and applies the policy gradient to this new function. They then establish some bounds on the bias of this function ($\propto \nu$) and the variance of its gradient ($\propto (1 - \nu)^2$). Finally, they provide some experiments for different values of $v$ to support their results.

### Strengths
(1) The paper investigates the idea of using this convex combination for the multi-agent case, which, based on their claims, was only done before for the single-agent case.

(2) There is a good variety of experiments that support the arguments made in the paper and also show the algorithm is flexible in the sense that it can employ different value factorization methods.

### Weaknesses
 (1) Although this paper is for the multi-agent case and also employs a different approach in the implementation (on-policy instead of off-policy), the idea and the bounds are too similar to that of the single-agent paper referenced in section 5. In this review's opinion, this makes the result incremental and not novel and significant enough for consideration at this venue. The core idea of interpolating between a biased but low-variance estimator and an unbiased but high-variance estimator has been explored before, and while the multi-agent setting introduces some nuances, the fundamental approach and the resulting bias-variance trade-off analysis feel like a direct extension rather than a novel contribution. The theoretical results, while technically sound, do not offer a fundamentally new perspective on this trade-off in the multi-agent context.

(2) A number of inconsistencies with the notations that make it hard for the average reader to precisely follow the claims of the paper. For instance, the notations $\nabla J$ and $\nabla \hat{J}$ are used interchangeably whereas they are not the same (look at and compare equations (1), (10), and (12)). Also, $\hat{Q}$ is used in equation (12) despite it not being properly defined until equation (14). Plus, sometimes the notations $\hat{Q}$ and $Q^\mu$ are used interchangeably even though they are clearly different when $Q^\mu$ is not in the function class $\mathcal{Q}$. The lack of consistent notation makes it difficult to track the mathematical arguments and understand the precise meaning of each term, which significantly hinders the readability and clarity of the paper. For example, the distinction between the true Q-function, its approximation, and the factorized Q-function is not always clear, leading to potential confusion.

(3) There seems to be a mistake in the proof of Proposition 4. The upper bounds $\frac{1}{2} L \sigma^2$ and $L \sqrt{mn}$ are supposed to be on the absolute value of the difference of $Q^\mu (s,a)$ and its first order estimate (initialed at $\mu(s)$); however, they are apparently used as upper bounds on $(Q^\mu (s,a) - \overline{Q}(s,a))^2$. So it seems the result should have been something like $c_1 L^2 \sigma^4 + L^2 mn \sigma^2$ instead of $c_1 L \sigma^2 + L \sqrt{mn} \sigma^2$ which would change the final bound as well. On another note, the absolute value should be outside the expectation for the second term in the last inequality of equation (27), and that is what makes the last argument of the proof (Proposition 4) possible.

### Questions
None.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce an approach to interpolate between using a joint Q function and factorised Q function in order to find a better balance in the variance bias trade-off. The idea is supported by some theoretical results that study the bias produced by the new objective in comparison with the original MARL objective.

### Strengths
The paper is well written and the idea, though being intuitive, seems novel and an effective tool for tackling an important problem in MARL. The authors have put effort into studying the properties of their proposed method with the theoretical analysis offering some useful insights.

The empirical results show that the method does deliver improvements in performance.

### Weaknesses
Despite the fact that the idea is novel, it is hard to fully evaluate the benefits of the contribution given some relevant work has seemingly been missed by the authors; specifically, these works seem highly relevant:

[1] Kuba, Jakub Grudzien, et al. "Settling the variance of multi-agent policy gradients." Advances in Neural Information Processing Systems 34 (2021): 13458-13470.

[2] Rashid, Tabish, et al. "Weighted qmix: Expanding monotonic value function factorisation for deep multi-agent reinforcement learning." Advances in neural information processing systems 33 (2020): 10199-10210.

[3] Mguni, David Henry, et al. "MANSA: learning fast and slow in multi-agent systems." International Conference on Machine Learning. PMLR, 2023.

Though [2] tackles value-based methods I think it is still worth discussing. Similarly, the method in [3] learns the best set of states to switch from using a decentralized critic to centralized critic. I caveat this with the fact that the specific algorithms involved in [3] are value-based methods but given that it is plug & play, the method seemingly captures gradient methods.Without having included a discussion on [3], it is hard to know how much this approach could be useful since the authors' approach has a fixed weighting parameter for all states whereas the approach in [3] can be viewed as a weighting variable whose optimal value {0,1} is learned for each state. 

The theoretical analysis though insightful didn't allow me to fully grasp an improvement in the performance of the proposed method with regard to variance and bias. I was expecting to see some results that indicate that for a given variance, the method achieves a reduced level of bias and similarly, for given level of bias the method would achieve a lower variance as compared to the standard objective. This has been shown nicely in the ablation study but I didn't see the corresponding analytic statements for this. 

It is not clear if there are situations where this method would under-perform. For example, I can see a potential for choosing greedily over either $Q^\pi$ or $Q^\nu$ yielding locally optimal actions but doing the same over their convex combination yielding a poor action. I would like to have seen a discussion on whether this is possible and under what conditions. 

My main concern remains as it seems that reference [3] seems to do something similar to solving this problem but allows the value of $\nu$ to vary at each state which seems to be a more powerful approach. In light of this I would like to have seen some statements as to why this paper is a useful contribution given [3].

My concern here is that the method introduced here seems to lead to biased solutions (and maybe even in the asymptotic training regime) - using this method it seems we lose convergence guarantees to any useful stable point. If so, because in general the stable points/equilibra of multi-agent systems are extremely sensitive to the objective parameters we could end up converging to a point a long way from any sort of local optimum (with arbitrarily bad solutions). This seems to be a significant issue. 

I would like to see at the very least some analysis on the conditions when this bias would be relatively small. Alternatively, if the authors could show that the bias is small in a vast number of randomly generated games that could help.

Minor

On page 6 it is written that the assumption of the Lipschitz smoothness of the gradient is reasonable since "Q functions tend to be smooth in most environments". I think this is slightly problematic since in many RL environments, the reward is sparse in these environments, so even the Q function is not so smooth. Besides, the smoothness of the Q functions does not suggest smoothness of its gradient.

### Questions
* What are the benefits/weaknesses as compared to [3]?

* For a given variance can it be shown analytically that the method achieves a reduced level of bias and similarly, for given level of bias does the method achieve a lower variance as compared to the standard objective?

* Can the authors discuss how this method would perform in situations, if they exist, where $Q^\pi$ and $Q^\nu$ may have different maxima. A coordination game such as the stag-hunt may be one such situation.



[3] Mguni, David Henry, et al. "MANSA: learning fast and slow in multi-agent systems." International Conference on Machine Learning. PMLR, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
