# Bellman Unbiasedness: Toward Provably Efficient Distributional Reinforcement Learning with General Value Function Approximation

- Decision: Reject
- Scores: 3, 6, 6, 6, 6

## Abstract
Distributional reinforcement learning improves performance by effectively capturing environmental stochasticity. 
However, existing research on its regret analysis has relied heavily on structural assumptions that are difficult to implement in practice.
In particular, there has been little attention to the infeasibility issue of dealing with the infinite-dimensionality of a distribution.
To overcome this infeasibility, we present a regret analysis of distributional reinforcement learning with general value function approximation in a finite episodic Markov decision process setting through *statistical functional dynamic programming*. 
We first introduce a key notion of *Bellman unbiasedness* which is essential for exactly learnable and provably efficient updates.
Our theoretical results demonstrate that the only way to exactly capture statistical information, including nonlinear statistical functionals, is by representing the infinite-dimensional return distribution with a finite number of moment functionals.
Secondly, we propose a provably efficient algorithm, *SF-LSVI*,  that achieves a tight regret bound of $\tilde{O}(d_E H^{\frac{3}{2}}\sqrt{K})$ where $H$ is the horizon, $K$ is the number of episodes, and $d_E$ is the eluder dimension of a function class.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper designs a distributional reinforcement learning algorithm with general function approximation, called SF-LSVI, under the assumption that the Eluder dimension of the function class is small. In particular, the SF-LSVI algorithm estimates the momentums of the expected return in addition to its mean (which is the standard Q-function). This paper proves that the SF-LSVI algorithm achieves a near-optimal regret bound.

### Strengths
-	As one of the major technical contributions, this paper studies the distributional RL problem with general reward functions, whereas prior works mostly focus on discretized rewards. This paper also identifies two key assumptions, Bellman closedness and Bellman unbiasedness, that allow statistically efficient learning algorithms. 
-	The choice of the particular choice of the sketch function, namely, the momentums, is theoretically justified by Theorem 4.6, which proves that “the only finite statistical functionals that are both Bellman unbiased and closed … is equal to the linear span of the set of moment functionals”.

### Weaknesses
-	While this paper studies distributional RL, the final metric for the performance of the algorithm is still the standard regret. In the main theorem (Theorem 6.5), there is no guarantee of whether the estimated momentum is close to the ground truth. In fact, estimating the momentums is purely an independent component in the algorithm, and is independent of learning the optimal policy.

### Questions
-	The justification for Bellman unbiasedness is confusing to me. Why is Bellman unbiasedness necessary in the finite sample regime? Is it a fundamental requirement (in other words, there are some statistical lower bounds if Bellman unbiasedness does not hold) or just a technical assumption required by the current analysis?

### Soundness
4

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
This paper improves the existing distributional reinforcement learning algorithm by introducing a new concept called "Bellman unbiasedness" which is  and revisit the framework through a statistical functional lens. The paper present a new algorithm, SF-LSVI, which is provably efficient and achieves the a tight regret upper bound $\tilde{O}(d_E H^{3/2} \sqrt{K})$.

### Strengths
1. This paper involve a novel framework "Bellman unbiasedness" which strictly contains the existing Bellman completness assumption, and addressing the infinite-dimensionality issue in DistRL.
2. The paper proposed novel theoretical analysis towards DistRL within more general assumptions, which is a nice contribution to the RL theory community.

### Weaknesses
1. I think it is better to discuss more about the technical contribution,e.g., detailed introduce the technical intuition of removing the dependency $\beta$ and why the dimension term is seperate from $\sqrt{K}$. 
2. It is not really clear that the relationship between the new "Bellman unbiasedness" assumption and the exist assumptions. Could you please present more comparison and examples?

### Questions
1. What is the notation "law" means in Lines 181 and 186.

### Soundness
3

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
3

### Summary
The paper introduces a novel concept in Distributional Reinforcement Learning (DistRL) called **Bellman unbiasedness**, which enables accurate and unbiased updates for statistical functionals in finite-dimensional spaces. This approach addresses the challenge of infinite-dimensional return distributions without requiring strict assumptions, such as distributional Bellman completeness. The authors propose **SF-LSVI**, an algorithm designed to achieve efficient learning with a favorable regret bound of $\tilde{O}(d_E H^{3/2} \sqrt{K})$, offering improvements over existing DistRL methods in terms of theoretical efficiency and robustness.

### Strengths
- **Originality**: The paper introduces Bellman unbiasedness, a novel concept that builds on Bellman closedness to allow unbiased estimation in finite-dimensional spaces. This approach opens new directions for efficient DistRL without requiring assumptions that are often infeasible in practical settings.
- **Theoretical Rigor**: The proofs and derivations are thorough and well-structured, lending strong theoretical support to the proposed SF-LSVI algorithm. The regret bound, $\tilde{O}(d_E H^{3/2} \sqrt{K})$, represents a competitive improvement within DistRL frameworks.
- **Clarity**: The paper is generally well-written, with each section logically building on the previous one. The background provided on limitations of prior approaches and the relevance of Bellman unbiasedness is helpful for contextualizing the contribution.
- **Significance**: This work could have broad implications in various applications requiring robust policy learning, such as robotics and finance, where DistRL has shown potential.

### Weaknesses
- **Lack of Empirical Validation**: The theoretical claims would be strengthened by empirical results on DistRL benchmarks, which could provide evidence of SF-LSVI’s practical effectiveness and robustness. Without this, the impact on real-world tasks remains speculative.
- **Completeness Assumption**: While the Statistical Functional Bellman Completeness assumption is less restrictive than full distributional completeness, it may still be challenging to meet in some environments. Further discussion on how widely this assumption holds in practical applications would be beneficial.
- **Accessibility**: Some sections, particularly the detailed theoretical derivations, may be challenging for readers not specialized in reinforcement learning. Simplifying these explanations or adding illustrative examples could make the work more accessible.

### Questions
1. Can the authors provide empirical validation to demonstrate SF-LSVI’s practical performance and potential advantages over existing methods?
2. How restrictive is the Statistical Functional Bellman Completeness assumption in practical settings? Could the authors discuss specific environments where this assumption may or may not hold?
3. Are there any potential limitations or specific scenarios where Bellman unbiasedness may not provide advantages or could introduce new challenges?

### Soundness
4

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
This paper introduces the concept of Bellman unbiasedness to address limitations in distributional reinforcement learning  regarding infinite-dimensionality and model misspecification. The authors propose an algorithm, Statistical Functional Least Squares Value Iteration, that operates within a finite-dimensional space, achieving tighter regret bounds under a weaker assumption called Statistical Functional Bellman Completeness. The work leverages moment functionals as finite approximations for the distribution of returns, demonstrating that only these functionals can maintain both Bellman closedness and unbiasedness.

### Strengths
- Introducing Bellman unbiasedness provides a new perspective on maintaining efficiency in DistRL, specifically addressing the challenge of high-dimensional distributions.
- Theoretical rigor is high, with comprehensive proofs and well-justified assumptions.
- Key terms like Bellman closedness and unbiasedness are well-defined, and the authors provide visual aids to clarify functional relationships.

### Weaknesses
-  The dense theoretical sections, particularly around statistical functionals and Bellman properties, may be challenging for readers not well-versed in DistRL. Additional illustrations or simplified explanations might improve comprehension.
- The motivation of using DistRL algorithm for RL with GVFA is not strong enough. The authors provide a regret bound for the proposed algorithm, but the benifits of DistRL methods over non-DistRL methods are not shown. In addition, the comparsion to V-EST-LSR (Chen et al.,2024) may not suffice to justify the effectiveness of DistRL, given that  V-EST-LSR is designed to solve risk-sensitive tasks.
- While the paper includes theoretical analysis and basic examples, empirical validation would better demonstrate SF-LSVI’s practical utility.

### Questions
- How to choose $N$? How does $N$ affects the sample efficieny and computational efficiency?
- The author claims the provable efficiency of the proposed algorithm. How does the computational complexity of the proposed algorithm scale with the size of the state and action spaces, and $N$?

minor questions / comments
- Fig 1 Yellow should be Blue? why is categorical unbiased and not closed?
- Defiition 4.4, what is x_k?
- the example below Definition 4.4 seems to not involve state transition

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a regret analysis for distributional reinforcement learning (RL) with general value function approximation in finite episodic Markov decision processes (MDPs), using statistical functional dynamic programming.

Initially, it introduces the concept of Bellman unbiasedness, proving that the moment functional is the unique structure within a class that includes nonlinear statistical functionals.

The paper then addresses a new challenge related to the inherent difficulty of managing the infinite dimensionality of a distribution, offering a theoretical analysis of how hidden approximation errors hinder the development of provably efficient algorithms. The authors also revisit the distributional Bellman Completeness assumption.

Lastly, it proposes a provably efficient distributional RL algorithm named SF-LSVI, which achieves a regret bound of O(d_E H^{3/2} sqrt K) . The results are tighter and rely on weaker assumptions.

### Strengths
The paper is generally easy to follow.

The concept of Bellman unbiasedness is novel and interesting.

Theoretical results are achievable without assumptions of discretized rewards, small-loss bounds, or Lipschitz continuity. Compared to previous works, the regret bound is tighter, as illustrated in Table 1.

### Weaknesses
The purpose behind introducing the Bellman unbiasedness concept is unclear.

Assumption 4.8 appears to lack sufficient motivation. Although Bellman unbiasedness is discussed earlier in the paper, there seems to be a disconnect between it and Assumption 4.8.

It is also unclear how the model misspecification term, zeta, would enter the bounds if Assumption 4.8 does not hold. It would be worthwhile to investigate whether this would lead to a polynomial or exponential blowup.

### Questions
The term “Bellman closedness” generally refers to the standard RL setting (i.e., not the distributional RL setting). A brief clarification on this would be helpful.

References:

Error Bounds for Approximate Policy Iteration

Finite-Time Bounds for Fitted Value Iteration

Finite-Time Bounds for Sampling-Based Fitted Value Iteration

Information-Theoretic Considerations in Batch Reinforcement Learning

The Bellman unbiasedness concept is new to me. Does a similar concept exist in the standard RL setting? If so, is it meaningful within that context?

It seems that this paper assumes a deterministic reward. If so, can the Bellman unbiasedness concept and theoretical guarantees be extended to a stochastic reward scenario? In standard RL, extending to deterministic rewards is relatively straightforward, but I’m uncertain about how this would apply in the distributional RL setting.

In Table 1, the terms "finitely representable" and "exactly learnable" are a bit unclear. It seems these properties might limit the applicability of SF-LSVI, which could be seen as a drawback of the algorithm.

The abstract mentions "Our theoretical results demonstrate that the only way to exactly capture statistical information, including nonlinear statistical functionals, is to represent the infinite-dimensional return distribution with a finite number of moment functionals." I think it refers to Definition 4.5 and Theorem 4.6. Could you clarify its meaning?

The term "law" is unclear.

"Additional sketch" seems ambiguous.

In Definition 4.7, why is the infinity norm used? Would it be possible to use the L2 norm instead?

H' in Lemma 6.3 appears to be a typo.

What is the Dcal-norm? It is defined in the appendix but not mentioned in the main text, and it’s unclear what d represents in the appendix.

### Soundness
3

### Presentation
2

### Contribution
2
