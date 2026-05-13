# Temporal Difference Learning: Why It Can Be Fast and How It Will Be Faster

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Temporal difference (TD) learning represents a fascinating paradox: It is the prime example of a divergent algorithm that has not vanished after its instability was proven. On the contrary, TD continues to thrive in reinforcement learning (RL), suggesting that it provides significant compensatory benefits. Empirical evidence supports this, as many RL tasks require substantial computational resources, and TD delivers a crucial speed advantage that makes these tasks solvable. However, it is limited to cases where the divergence issues are absent or negligible for unknown reasons. So far, the theoretical foundations behind the speed-up are also unclear. In our work, we address these shortcomings of TD by employing techniques for analyzing iterative schemes developed over the past century. Our analysis reveals that TD possesses a mechanism enabling efficient mapping into the smallest eigenspace—an operation previously thought to necessitate costly matrix inversion. Notably, this effect is independent of the conditioning of the problem, making it particularly well-suited for RL tasks characterized by rapidly increasing condition numbers through delayed rewards. Our novel theoretical understanding allows us to develop a scalable algorithm that integrates TD’s speed with the reliable convergence of gradient descent (GD). We additionally validate these improvements through a rigorous mathematical proof in two dimensions, as well as experiments on problems where TD and GD falter, providing valuable insights into the future of optimization techniques in artificial intelligence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a theoretical analysis to understand the speed benefits of TD and the convergent properties of GD. It proposes a method that combines the benefits of each to have a faster and convergent algorithm. It presents a theoretical analysis and empirical results on toy domains.

### Strengths
- The proposed method of combining TD and GD is simple and reasonable.
- The paper includes nice visualizations to understand the intuition behind the trajectories of the algorithms.
- The toy domains illustrate the idea reasonably well. It is nice to include results on Figure 4.

### Weaknesses
 - While not an empirical paper, I think some comparison to methods like GTD (gradient TD) would be useful to get a sense of the rate of convergence of other similar algorithms. I think just evaluating TD and GD in Section 5 is limited. Specifically, it would be beneficial to see how the proposed method compares to GTD in terms of convergence speed, especially since GTD is designed to address some of the instability issues of TD. The current evaluation only highlights the differences between TD and GD, but doesn't provide a comprehensive view of the landscape of temporal difference learning algorithms.
- Perhaps it would be useful to also evaluate the proposed methods on other toy domains known to exhibit convergence like the full Baird counter example like Figure 11.1 from Sutton and Barto [1] and Figure 1a from [2]. This would help to further validate the robustness of the proposed method in scenarios where TD is known to struggle. The current toy domains are helpful for intuition, but additional experiments on more challenging and well-known examples would strengthen the empirical support.
- I think the paper can do better at improving intuition in terms of language. The attempt of 3.4 is nice of giving the complete picture, but I think the broader implications are still missing and the details are still too narrowly focused on technical details. It would be nice to include some broader implication on future design of such algorithms based on the theoretical results. The current discussion is too focused on the specific mathematical derivations, and it would be useful to have a more high-level discussion of how these results can be used to guide the development of new algorithms or improve existing ones. The paper needs to bridge the gap between the theoretical findings and their practical implications.

### Questions
- While there are some details in the related works, I am having a tough time placing this work in the context of others. Currently, the paper is written as though no one else has worked on this problem since Baird’s 1999 papers. Is this actually true? While the proposed method may be new, Theorem 1 and 2 seem quite fundamental and it's interesting that other works have not explicitly tried to address this. This question may be due to just my unfamiliarity with the literature, and so I would defer to other reviewers on the value of the proposed insights. 
- The paper cites Gallici et al. 2024 for their use of layer norm to address TD divergence. I am curious whether the authors think this itself is sufficient for getting both a convergent and fast algorithm? If layernorm enables TD to converge, we don’t necessarily need to rely on GD’s convergence benefits right?

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
3

### Summary
This paper does a comparative analysis of the parameter updates when using gradient descent (GD) and temporal difference (TD) approaches. They focus on the one-step Bellman equation as the optimization target in both cases. In this analysis, the paper posits that GD methods have a high condition number, leading to slow convergence. It then focuses on TD updates when the Hessian matrix involved in the update is a combination of symmetric and skew-symmetric matrices.

Here the paper shows that as the skew-symmetric component of the Hessian grows, the eigenvalues start converging. With the eigenvalues closer together, the paper shows that the iteration scheme will progress more uniformly and lead to faster convergence. But this speed-up is capped by the largest learning rate that can be used.

The above analysis leads to a new method that uses the sign of GD and the magnitude of TD, called GDS-TDM in this paper. Theoretical analysis here shows that there exists a maximal learning rate under which convergence in guaranteed, and also specified the rate of convergence.

Finally, empirical evaluation on a simplified version of Baird's counter-example and a 10x10 grid world show stable learning, faster convergence, and lower error when using GDS-TDM compared to GD or TD

### Strengths
* The paper states that they have two contributions: theoretical analysis validating why TD can converge fast, and a unification of GD and TD that seeks to combine the positive attributes of both. From my perspective, both of these contributions are partially justified. I go into more detail on the positives below and where I might need more convincing in the following sections.
* This paper presents an interesting analysis of the GD and TD updates based on their condition number and convergence rates. The breakdown of the TD Hessian into symmetric and skew-symmetric matrices seems to be novel and leads to the subsequent analysis in the paper.
* Figure 1 is well done and gets the idea across well.
* Section 3, which focuses on the first contribution, does a good job in analyzing a simpler problem and then generalizing the result in Theorem 1. The analysis of the eigenvalues as the Hessian is skewed more in Theorem 2 is interesting and communicated well via Figure 2.
* I have checked the proofs of Theorems 1 and 2 and I did not catch any major issues (minor quibbles in the Questions section).
* The proposed modification in Section 4 seems to be simple, and the experiments bear out some of the qualities that the paper advertises, namely, faster convergence than GD and more stable learning than TD.
* The proposed modification is extremely simple.

### Weaknesses
Overall I really like the idea behind the paper, but I feel like there are bits and pieces that left me feeling confused. Below I try to write down these bits:
* As mentioned briefly above, I am not completely convinced that the contributions have been sufficiently justified. I appreciate that while this is a theoretical paper, the authors have attempted to empirically validate their technique. But the experiments both seem to show situations where TD is unstable, and GD is slow, and how GDS-TDM converges more stably compared to TD, and faster than GD. What of a setting where TD converges to the right solution? How does GDS-TDM compare there? Also, it is unclear why TD diverges in the grid-world example. The data is on-policy (from the optimal policy while performing policy evaluation), with what seems like not undue state aliasing. Why then does TD diverge?
* In the sub-section *Ill-Conditioning in Reinforcement Learning*, the paper indicates why GD methods have a large condition number with delayed rewards. Though it only refers to a reference book and doesn't really explain the mechanism by which the condition number is so large. Could you provide a brief explanation as to why the condition numbers would be large with delayed rewards? It would help a reader to better grasp the problem.
* The thread leading to Equation 4 is abruptly cut off with no clear takeaway for a non-expert reader. What does the update shown in Equation 4 mean for the condition number, or for the optimization problem? Why does it fail?
* I wasn't able to follow some of the notation in Section 4. I have added particular confusions in the Questions section.
* There are some other notation typos and confusions. Clarifying in the Questions section.
* End of section 1, Typo: `demonstrate with a simple method *what* a unification of GD and TD preserving their positive attributes can look like`.
* The related work has captured a lot of important references, particularly focusing on the unification of GD and TD, but has missed certain recent approaches that attempt to analyze or mitigate the instability of TD by empirically regularizing the gradient [2], or reframing the problem via an optimization lens [1]. These references might be useful to look at. I am not suggesting they be added to the related work, since it is clearly organized in a way that does not seek to exhaustively reference all previous attempts to improve the TD update.


### Questions
* Beginning of Section 3, The Hessian for TD is correctly identified as not being symmetric. Why is the conclusion that the subsequent matrix has a skew-symmetric component, and not any other type of asymmetry? Perhaps a quick clarification here might be helpful.
* In equation 8, where does the $\eta$ come from? Is it the learning rate? I thought we were looking for the eigenvalues of $H$, and not $1 - \eta H$. Which brings me to the possible incorrectness in the value of $\lambda_{1/2}$. Where does the $1$ come from?
* Equation 9 seems to have a misplaced $k$. Is it supposed to be $t$?
* Does $I_k$ in theorem 1 indicate an identity matrix?
* definition of $S$ in Theorem 3 confuses me a little bit. Does it imply [-1, -1], [0, 0], [1, 1] are all valid values for s?
* This theorem is for 2 dimensional matrices and hence only two parameters. What would be needed for a more general proof?
* How many times was the experiment repeated, what is the 95% confidence interval in Figures 4 (c) and 5 bottom?
* The proposed solution is really simple. Could you elaborate more on why these specific experiments were chosen? Perhaps experiments in more canonical RL tasks like mountain car or cart pole which have implementations online could be easily evaluated with the new technique? This would add a comparison in a control setting where TD does not diverge, where the discount factor is not 1, where the function approximation is established, and compare the empirical speed of learning and final solution reached for both TD, GD, and GDS-TDM.

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
The paper deals with convergence problems in reinforcement learning. The convergence problems of temporal difference (TD) learning and the sometimes very slow learning behavior of gradient descent (GD) are considered. The paper introduces a new way of looking at the problems, which is based on the consideration of the size of eigenvalues. An explanation is provided and a simple modification is presented which is a synthesis of TD and GD. For this purpose, the sign of the GD update vector and the magnitude of the TD update vector are used. The considerations are supported by proofs and illustrated application to small but pathological examples.

### Strengths
* The paper is excellently written. A real pleasure to read.
* If everything the authors present is correct, then this is a groundbreaking work that solves a problem that has been unsolved since Baird's time.

### Weaknesses
I cannot identify any weaknesses.

I must say, however, that I am not capable of reliably verifying that all the claims are correct.

### Questions
* Why is the advantage of GDS-TDM not demonstrated using difficult, high-dimensional benchmarks?
* What should be considered when using GDS-TDM together with neural networks as Q-function in difficult, high-dimensional environments?
* Are the ideas from [1] relevant for the present work?
* Should [1] be cited and discussed?

[1] Wang & Ueda, Convergent and Efficient Deep Q Network Algorithm, 2022

### Soundness
3

### Presentation
4

### Contribution
3
