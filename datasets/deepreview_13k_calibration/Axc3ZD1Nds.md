# Beyond Expected Returns: A Policy Gradient Algorithm for Cumulative Prospect Theoretic Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
The widely used expected utility theory has been shown to be empirically inconsistent with human preferences in the psychology and behavioral economy literatures. Cumulative Prospect Theory (CPT) has been developed to fill in this gap and provide a better model for human-based decision-making supported by empirical evidence. It allows to express a wide range of attitudes and perceptions towards risk, gains and losses. A few years ago, CPT has been combined with Reinforcement Learning (RL) to formulate a CPT policy optimization problem where the goal of the agent is to search for a policy generating long-term returns which are aligned with their preferences. In this work, we revisit this policy optimization problem and provide new insights on optimal policies and their nature depending on the utility function under consideration. We further derive a novel policy gradient theorem for the CPT policy optimization objective generalizing the seminal corresponding result in standard RL. This result enables us to design a model-free policy gradient algorithm to solve the CPT-RL problem. We illustrate the performance of our algorithm in simple examples motivated by traffic control and electricity management applications. We also demonstrate that our policy gradient algorithm scales better to larger state spaces compared to the existing zeroth order algorithm for solving the same problem.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel approach to reinforcement learning (RL) by leveraging Cumulative Prospect Theory (CPT) to account for human decision-making biases, moving beyond the traditional expected utility framework. It focuses on the policy optimization problem, where the objective is the CPT value of the random variable recording the cumulative discounted rewards (CPT-PO). Additionally, it considers the particular case of the expected utility objective, where only returns are distorted by the utility function (EUT-PO). This work derives a policy gradient (PG) theorem for CPT-based RL, presenting a model-free policy gradient algorithm for optimizing a CPT policy.

### Strengths
This paper addresses an objective that encompasses a broad class, including Conditional Value at Risk (CVaR), distortion risk measures, and expected utility.

The paper effectively explains various policy classes associated with different objectives, helping to clarify how these classes relate to CPT-RL versus standard RL approaches.

The derivation of a policy gradient theorem for CPT objectives is a significant extension of the traditional PG results in reinforcement learning, broadening its applicability in human-centered decision contexts.

### Weaknesses
The experimental section provides limited insight due to its use of relatively straightforward examples (traffic control and electricity management), which may not fully illustrate the complexities that arise in more realistic, high-stakes environments, such as finance or healthcare. The traffic control example, while demonstrating the influence of the probability distortion function, does not explore the performance of the resulting policy under different risk metrics, such as Conditional Value at Risk (CVaR). The electricity management example, although using real-world data, is still a simplified model that does not capture the full complexity of real-world energy markets.

In Section 5(a), the observation that different weight functions lead to different policies in the grid environment could be strengthened by assessing these policies against risk measures (such as CVaR) beyond expected return. Without this, it is unclear if the CPT-RL-PO policy outperforms standard RL-PO under any specific risk-sensitive criteria. The comparison is limited to a risk-averse probability weight function versus a risk-neutral one, without a more thorough evaluation against established risk-sensitive benchmarks.

The grid environment results are overly simplified and provide little substantive information. It would be beneficial to evaluate whether the derived policies' performance aligns meaningfully with their respective objectives. The scalability demonstration, while showing the advantage of the proposed policy gradient (PG) algorithm over a zeroth-order method, does not provide a comparison against other established policy gradient methods. The lack of comparison against risk-sensitive RL or distributional RL methods makes it difficult to ascertain the specific advantages of CPT learning. Although CPT is theoretically valuable, the empirical advantages of CPT over other risk-sensitive measures remain ambiguous in the presented results. The authors may consider including direct comparisons with risk-sensitive RL or distributional RL methods on the same tasks.

### Questions
Minor comment: On page 4, under Problem formulation: CPT-RL, the cumulative discounted rewards variable $X$ is referenced, but the definition provided does not discount the rewards. It would be clearer to either update the variable's definition to include discounting or adjust the notation accordingly to prevent confusion.

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
3

### Summary
This paper is a follow-up work to [L.A. et al., 2016] on Cumulative Prospect Theory (CPT) value optimization in reinforcement learning problems. The original paper utilized the simultaneous perturbation stochastic approximation (SPSA) method to update the policy, while this paper provides a policy gradient method. The policy gradient is evaluated and compared with the SPSA method in several domains.

### Strengths
+ Discussion on the optimal policies under CPT, showing that optimal policies are generally stochastic and non-Markovian when CPT is applied.
+ Policy gradient algorithm for CPT value optimization, compared to SPSA methods in the original paper.

### Weaknesses
 + The algorithm is only validated in a few small domains, making it difficult to assess the performance of this policy gradient in more complex tasks. The experiments lack the complexity to demonstrate the practical advantages of the proposed method over existing risk-sensitive RL techniques. The grid world and electricity management scenarios, while illustrative, do not fully capture the challenges of high-dimensional state and action spaces often encountered in real-world applications. Specifically, the absence of experiments in standard benchmark environments, such as those available in Mujoco, makes it challenging to evaluate the scalability and robustness of the proposed policy gradient approach.
+ The computation of the integral for the CPT value appears complex and time-consuming due to the use of Monte Carlo sampling. While Monte Carlo sampling is a common technique, the additional step of quantile estimation, which requires sorting the sampled returns, adds computational overhead. The paper does not provide a detailed analysis of the computational complexity of this step, nor does it discuss potential optimizations or approximations to reduce the computational burden. Furthermore, the reliance on Monte Carlo sampling introduces variance in the gradient estimates, which may affect the stability and convergence of the learning process. The paper would benefit from a more thorough discussion of these computational aspects.


### Questions
+ $\phi(R(\tau))$ in line 295, 303, 305 should be $\varphi(R(\tau))$ in Theorem 6? 

+ How to choose the proper utility function for different problems?

+ The policy gradient calculation depends on the property that the function $u$ is non-decreasing. Can we work with other $u$ where non-decreasing is not guaranteed?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper makes three key contributions to the field of cumulative-prospect-theory (CPT)-based reinforcement learning, a framework where the agent aims to maximize not the raw cumulative reward but a transformed version of it. This transformation involves both a utility function and a probability weighting function, introduced to better reflect human value assessments of rewards (e.g., monetary amounts converted into perceived value). The objective is to find a policy that maximizes this transformed cumulative reward.

CPT-based reinforcement learning generalizes various prior approaches, including: (1) the standard RL framework, (2) risk-sensitive RL with an exponential utility function (e.g., as in Noorani et al., 2022), (3) optimization based on VaR/CVaR of the total reward, and (4) the case studied by Kahneman and Tversky (1992).

The first contribution presents new insights into the characteristics of optimal policies within CPT-based reinforcement learning. These findings include: (1) deterministic, history-dependent optimal policies may not always exist; (2) in the absence of weighting functions, a deterministic, non-stationary optimal policy exists that depends on the current state and past cumulative reward; and (3) without weighting functions, a Markovian, non-stationary optimal policy exists if and only if the utility function is either affine or exponential.

The second contribution introduces a policy gradient theorem and a novel algorithm for CPT-based reinforcement learning.

The third contribution is an empirical evaluation of the proposed algorithm. This study includes (1) a performance comparison with CPT-SPSA-G, an existing RL algorithm for CPT problems, across various grid-world environments, demonstrating the proposed algorithm's advantages, particularly in larger environments; and (2) an exploration of different behaviors under varying utility and weighting functions.

### Strengths
The theoretical and algorithmic contributions are original and clear. If one believes that CPT-based RL problems are important, then these contributions are also significant. 

The paper did a very nice job relating its studied problem with other related problem settings studied previously, making it easy for readers to understand the position of this paper in the literature.

The paper's presentation is clear.

### Weaknesses
While I appreciate the contributions the authors made to CPT-based RL problems, I am not convinced of the importance of CPT-based RL problems by reading this paper. The paper cites another paper "... this is particularly important in applications directly involving humans
in the loop such as e-commerce, crowdsourcing and recommendation to name a few" to argue that this class of problems has important applications. However, it is not clear from the cited paper whether other formulations that take into account human behavior can also handle these applications well. In fact, compared with CPT, I feel that a more principled way that considers human behavior is trajectory-based reward RL problems (one reward for the entire trajectory) with human preferences, like RLHF in large language models. While CPT assumes a structure of the final reward (the final metric to optimize involves a weight function, a utility function, and a summation of rewards), these weight functions are unknown and must be learned from data. In contrast, in trajectory-based reward RL problems, there is no assumption on the structure of the metric being optimized. And the metric is learned with human preference data. I wonder how authors think about the pros and cons of CPT in terms of its applications compared to trajectory-based reward RL problem settings.

Another weakness is related to the empirical study of the paper. The experiments only demonstrate the effectiveness of the proposed algorithm but do not include those justifying the necessity of the CPT problem. It would be much better if the authors could demonstrate that in some applications, the data shows that human behavior can be accurately predicted with CPT but not other theories.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3
