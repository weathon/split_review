# Policy Gradient with Tree Expansion

- Decision: Reject
- Scores: 8, 6, 3, 5

## Abstract
Policy gradient methods are notorious for having a large variance and high sample complexity. To mitigate this, we introduce SoftTreeMax---a generalization of softmax that employs planning. In SoftTreeMax, we extend the traditional logits with the multi-step discounted cumulative reward, topped with the logits of future states. We analyze SoftTreeMax and explain how tree expansion helps to reduce its gradient variance. We prove that the variance depends on the chosen tree-expansion policy. Specifically, we show that the closer the induced transitions are to being state-independent, the stronger the variance decay. With approximate forward models, we prove that the resulting gradient bias diminishes with the approximation error while retaining the same variance reduction. Ours is the first result to bound the gradient bias for an approximate model. In a practical implementation of SoftTreeMax we utilize a parallel GPU-based simulator for fast and efficient tree expansion. Using this implementation in Atari, we show that SoftTreeMax reduces the gradient variance by three orders of magnitude. This leads to better sample complexity and improved performance compared to distributed PPO.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel method to reduce variance in Policy Gradient (PG) methods by integrating Tree Search (TS) with a differentiable parametric policy. By incorporating planning into the PG procedure, the authors propose "SoftTreeMax," presented in two variants: C (exp-Expectation) and E (Expectation-exp). The paper offers a theoretical analysis demonstrating how this method reduces variance concerning tree expansion policy and environment parameters. It also analyzes the soundness of using an estimated model for planning, showing that the gradient bias correlates with model approximation error. The practical utility of this approach is demonstrated through experiments on Atari, employing a GPU-based simulator that efficiently utilizes distributed nature for tree expansion.

### Strengths
- The work introduces an innovative approach to integrating planning with policy search methods, supported by substantial theoretical analysis that highlights the benefits of this approach.
- The empirical results on Atari, using a GPU-based simulator, are highly promising.

### Weaknesses
 - The presentation of the two versions of SoftTreeMax (E and C) is unbalanced. While it is beneficial to discuss both, the paper does not adequately represent each. For instance, the Atari experiments focus on C-SoftTreeMax, the empirical demonstration of variance reduction (Figure 1) pertains to the E-version, the theoretical analysis in Section 4.2 is solely for the E version, and the discussion involving the forward model in Section 4.3 is exclusively for C-SoftTreeMax. This uneven representation can make the paper difficult to follow and raises questions about the rationale for using different versions. It also gives the impression that the work is incomplete. Additionally, guidance on which version to use is lacking; although the authors provide a motivation related to risk-aversion/safety for one version, it is not explored in detail.

- In the experiments, exact expectations are considered instead of sample-based methods. This seems limiting, given the appeal of PG methods in sampling-based scenarios. The absence of finite-sample variance components is a significant omission.

- The behavior/expansion policy $\pi_b$ is crucial in the approach. The paper sets the expansion policy to uniform, but this may not be realistic. Even with pruning, uniform expansion seems suboptimal for exploration. Moreover, how realistic is it to have a behavior policy that induces an irreducible and aperiodic transition matrix?

- Theorem 4.8: Additional insights on why the error scales linearly with $d$ would be valuable.

### Questions
- The behavior/expansion policy $\pi_b$ is crucial in the approach. The paper sets the expansion policy to uniform, but this may not be realistic. Even with pruning, uniform expansion seems suboptimal for exploration. Moreover, how realistic is it to have a behavior policy that induces an irreducible and aperiodic transition matrix?

- Theorem 4.8: Additional insights on why the error scales linearly with $d$ would be valuable.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel approach that replaces logits by the score of a trajectory starting from that state-action. Authors provide solid theoretical results showing their methods reduces the variance of policy gradient approach and validate it by conducting experiments on Atari games.

### Strengths
1. The paper presents a novel method that combines policy gradient techniques with tree search planning, offering a fresh perspective on reducing gradient variance in reinforcement learning.
2. The authors provide solid theoretical analysis, including variance bounds and proofs that show how the tree expansion policy affects variance reduction. They also address the gradient bias introduced by approximate models.
3. The experimental evaluation on Atari games shows significant reductions in gradient variance and improvements in performance, validating the effectiveness of the proposed methods.

### Weaknesses
1. The paper primarily considers softmax parameterization for policies, which is restrictive, especially when considering environments with continuous action spaces. The method's reliance on softmax limits its applicability to scenarios where more flexible policy representations are needed, such as Gaussian policies commonly used in continuous control tasks. This constraint could hinder the method's performance in complex environments requiring nuanced action selection.
2. The proposed methods rely on the model dynamcis, which need to be infer from the interactions. When employed on offline setting, this may introduce extra bias. The necessity of accurate model dynamics, whether learned or provided, poses a significant challenge, particularly in offline settings where the data distribution may not fully represent the environment. This reliance on potentially biased or inaccurate models could lead to suboptimal policy learning and generalization issues.
3. Tree expansion, especially with deeper trees, can be computationally intensive. The paper could benefit from a more detailed analysis of the computational costs and how they impact practical deployment. The computational overhead associated with tree search, especially as the depth and breadth of the tree increase, raises concerns about the practical scalability of the method. A thorough analysis of the trade-offs between computational cost and performance gains is crucial for assessing the method's viability in real-world applications.

### Questions
1. Is this tree expansion limited to softmax parameterization?
2. Is the method designed only for discrete action space?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims to integrate a novel tree search methodology with policy gradient with the goal of reducing the variance and improving the performance of PG agents.

### Strengths
1. The experiments show significant improvements over the chosen baseline.
2. The methodology is supported with theoretical results.
3. The paper implements a parallel version of BFS using GPUs that seems to be scalable.

### Weaknesses
1. The novelty of the methodology seems quite limited. Eq. (2) is supposed to be the logit of the policy but I cannot see any difference from the definition of a q-value function, which would entail that the paper is proposing a slight variation of AlphaZero.
2. The authors only compare against PPO. Given that the proposed algorithm is a tree search model-based algorithm, it would be more appropriate to compare against model-based methods, ideally MuZero.

### Questions
1. Can you further explain how the proposed method is different from the AlphaZero/MuZero?
2. Why was PPO the only baseline?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes SoftTreeMax, a novel policy gradient method that integrates tree search (TS) and policy gradient (PG) techniques to reduce the variance of policy gradients, a common issue in traditional PG methods. The SoftTreeMax approach uses a differentiable policy that extends standard softmax by incorporating planning, leading to improved sample efficiency and performance.  Theoretical analysis shows that the variance reduction depends on the choice of the tree expansion policy, with deeper tree expansions leading to lower variance. Furthermore, the authors provide bounds on the gradient bias when using approximate models.

### Strengths
1. An Interesting and important question.
2. Comprehensive conceptual and theoretical analysis.

### Weaknesses
I am much concerned about the empirical evaluations.
1. The wall time is much affected by implementational details. These should be, at the very least, appropriately discussed.
	1. For example, [1] reports very high fps, exceeding what is obtained in the paper.
2. I do not see details of the network used. 
3. It is not clear what the pruning is and how it affects training
4. **important**: It is not clear if the advantage of the proposed method stems from the variance reduction (as claimed) or increased computations per action. E.g., what would happen if the baseline had a bigger network? 
5. The algorithm is a model-based one; thus, having a baseline from this realm is also desirable.

The literature on embedding search as an inductive bias is quite broad and is completely missing in the related work section. Eg. value iteration networks, A3Tree etc.

### Questions
1. In many cases (Sec B.3), the SoftTree max policies start with a lower score than PPO; why is that so?
2. Why did the performance on Krull decrease (PPO)?
3. How is your work related to [1]
4. Could you provide an explicit formula for calculating the logits with the full tree expansion?
5. Following footnote 1 on page 8. I am unsure if extending the proposed algorithm to stochastic environments is that easy.

[1] https://arxiv.org/abs/1710.11417

### Soundness
1

### Presentation
3

### Contribution
3
