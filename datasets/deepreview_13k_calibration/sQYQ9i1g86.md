# Constrained Exploitability Descent: Finding Mixed-Strategy Nash Equilibrium by Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
This paper presents Constrained Exploitability Descent (CED), a novel model-free offline reinforcement learning algorithm for solving adversarial Markov games. CED is a game-theoretic approach combined with policy constraint methods from offline RL. While policy constraints can perturb the optimal pure-strategy solutions in single-agent scenarios, we find this side effect can be mitigated when it comes to solving adversarial games, where the optimal policy can be a mixed-strategy Nash equilibrium. We theoretically prove that, under the uniform coverage assumption on the dataset, CED converges to a stationary point in deterministic two-player zero-sum Markov games. The min-player policy at the stationary point satisfies the necessary condition for making up an exact mixed-strategy Nash equilibrium, even when the offline dataset is fixed and finite. Compared to the model-based method of Exploitability Descent that optimizes the max-player policy, our convergence result no longer relies on the generalized gradient. Experiments in matrix games, a tree-form game, and an infinite-horizon soccer game verify that a single run of CED leads to an optimal min-player policy when the practical offline data guarantees uniform coverage. Besides, CED achieves significantly lower NashConv compared to an existing pessimism-based method and can gradually improve the behavior policy even under non-uniform coverage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents Constrained Exploitability Descent (CED), a novel model-free offline RL algorithm aimed at finding mixed-strategy Nash equilibria in two-player zero-sum Markov games. CED combines game-theoretic approaches with policy constraint methods from offline RL to find mixed-strategy NEs. The authors also provide theoretical results, showing that CED converges to an unexploitable policy under certain conditions. Finally, experiments in matrix games, a tree-form game, and a soccer game validate that CED outperforms existing methods in achieving lower NashConv. The algorithm is notable for its stability and effectiveness, even with limited offline data.

### Strengths
1.	The introduction of Constrained Exploitability Descent (CED) is an innovative contribution to offline reinforcement learning in adversarial two-player zero-sum Markov games. By combining the concepts of Exploitability Descent (ED) with policy constraints typically seen in offline RL, the paper introduces a new approach to handling distributional shifts in a competitive setting.

2.	The paper provides solid theoretical results, proving that for CED converges to a stationary point in deterministic two-player zero-sum Markov games under uniform data coverage assumptions.

3.	The empirical results are thorough and well-presented. The experiments span various scenarios, including matrix games, tree-form games, and a soccer game, demonstrating the practical applicability and effectiveness of CED in different settings.

### Weaknesses
1.	The convergence proof relies on the assumption of uniform data coverage, which may not always hold in real-world offline RL settings. This is a significant limitation because real-world datasets are often collected from diverse sources and may exhibit highly non-uniform distributions, potentially leading to poor performance or even divergence of the algorithm. The theoretical guarantees provided are therefore not applicable in many practical scenarios without further modifications or assumptions about the data distribution.

2.	The paper does not provide detailed insights into the computational complexity or scalability of CED, especially in environments with larger state or action spaces. This lack of analysis makes it difficult to assess the practical applicability of the algorithm to complex, real-world problems. Specifically, the computational cost associated with the policy constraint optimization and the exploitability descent steps is not discussed, which is crucial for understanding the algorithm's feasibility in high-dimensional settings. Furthermore, the memory requirements for storing and processing the offline dataset are not addressed, which could be a bottleneck for large-scale applications.

### Questions
As I’m not an expert in this area, I have listed my questions below. If there are any mistakes, please feel free to correct me.

Q1: The convergence proof of CED relies on uniform data coverage. Could you elaborate on how the algorithm performs when this assumption is not met, especially in cases of highly imbalanced or sparse datasets? Are there mechanisms within CED to mitigate these issues, or would it require additional modifications?

Q2: Could you provide more insights into the scalability of CED in larger games with high-dimensional state-action spaces or more complex multi-agent interactions? Or have you tested its computational efficiency or considered potential bottlenecks when scaling up to larger environments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the problem of offline learning Nash Equilibrium in model-free deterministic two-player zero-sum Markov games. It combines the techniques from exploitability descent and policy constraints in offline learning setting and proposed an algorithm CED. The authors further showed that, under suggested assumptions, the proposed algorithm might converge to a NE. This paper provided some numerical results to support their theorems.

### Strengths
1. The proposed algorithm achieves last-iterate convergence under suggested assumptions.
2. Numerical results and graphs are provided to support the proposed theorems.

### Weaknesses
 1. The theoretical novelty of this paper is limited.
2. Theorem 1 only provides asymptotic convergence analysis, which is sharp contrast even with the direct previous work [1].
3. The proof of theorem 1 relies on the assumption that $\frac{1}{\epsilon} \to 0$. However, in the provided numerical experiments, all $\epsilon$ are set to be small (e.g. $1, 0.1, 10^{-3}, 10^{-4}$).
4. Theorem 2 relies on the assumption that the final stationary point $\bar{\mu}(s)$ lies in the interior of the feasibility set $\Pi(s)$. However, it seems to be a relative strong assumption, for example, it requires the Markov game to have a NE with full support. The paper claims that previous work [1] posed the same assumption but I couldn't find any reference in [1] regarding this assumption. I would be grateful if the authors can specifically indicate where the assumption is specifically stated during their rebuttal.
5. This work establish the convergence to NE by stating that $Q^{\mu, \hat{\nu}} \approx Q^{\mu_{\beta}, \hat{\nu}} \approx Q^{\hat{\mu}, \hat{\nu}}$ and reach the conclusion that $(\hat{\mu}, \hat{\nu})$ forms a NE (386-387). I believe that more rigorous mathmatical statements are required to reach this conclusion, for example, can the error bound  $||\mu_{\beta} - \hat{\mu}||$ be provided?
6. Behavior policies are not provided in numerical results.
7. In line 203 the regularizing term should be $+ \epsilon D(\pi(s), \pi_{\beta}(s))$ instead of negative.

### Questions
1. In the last line of  proof of lemma 4, I don't see why the term $\frac{y^2}{|A|}$ disappears.
2. In lemma 4 it is stated that $(\bar{\mu}(s, a) + p^s_a)_{a \in A}$ stays in the probability simplex. However, it is not clear to me why this is the case. I would appreciate if the authors can provide some insights during their rebuttal.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Constrained Exploitability Descent (CED), a novel model-free offline reinforcement learning algorithm designed to find mixed-strategy Nash equilibria in adversarial Markov games. The key contributions of the paper are:

1. The authors propose CED, which combines game-theoretic approaches with policy constraint methods from offline RL to address the challenge of learning in adversarial settings, where the optimal policy can be a mixed-strategy Nash equilibrium.
2. In contrast to previously proposed model-based methods, CED no longer relies on generalized gradient computation.
3. The authors provide experimental validation of CED in matrix games, a tree-form game, and an infinite-horizon soccer game. The results demonstrate that CED can effectively find optimal min-player policies when practical offline data guarantees uniform coverage and achieves significantly lower NashConv compared to existing pessimism-based methods.

### Strengths
The primary strengths of this paper can be summarized in the following two aspects:

1. The authors present a novel model-free offline reinforcement learning algorithm that improves upon previously proposed methods for solving adversarial Markov games.  
2. The paper provides both rigorous theoretical analysis and thorough empirical validation.

### Weaknesses
Here are the major weaknesses from my perspective:

1. While I acknowledge the authors' contribution in improving the performance of Exploitability Descent, they only compare their method to one RL algorithm for solving adversarial Markov games. This limits the contribution, as the authors have not compared their method to other previously proposed approaches, both from a theoretical and empirical standpoint. Specifically, the paper lacks a comparison to other offline reinforcement learning algorithms designed for adversarial settings, such as those based on robust optimization or distributionally robust approaches. A more comprehensive comparison would involve evaluating against a wider range of algorithms, including those that handle partial observability or non-stationary opponents, to better contextualize the performance of CED.

2. In the experimental implementation, the authors only evaluate their algorithm on games with relatively simple structures. This raises uncertainty about whether the proposed algorithm achieves significant improvement over existing methods in more complex, practical tasks. The experiments, while demonstrating the algorithm's functionality, do not explore the scalability of CED to high-dimensional state and action spaces, or games with longer horizons. For example, the soccer game, while an infinite-horizon game, is still a relatively simple environment. It would be beneficial to see results on more complex games, such as those with more agents, more complex action spaces, or more intricate reward structures, to assess the practical applicability of CED.

3. The discussion on the coverage condition is insufficient. The assumption of uniform coverage seems quite strong in the offline RL literature, and the authors have not explored how their algorithm performs under other, less restrictive coverage conditions. In particular, the paper does not address how the performance of CED degrades under non-uniform coverage, or how the algorithm might be adapted to handle situations where the offline data is biased or incomplete. The lack of analysis on the sensitivity of CED to coverage assumptions is a significant weakness, as real-world offline datasets are rarely uniformly distributed.

### Questions
Based on the discussion of the paper's strengths and weaknesses, I have the following questions for the authors:

1. Is the uniform coverage assumption essential for the analysis? Could the proposed algorithm also work under different coverage conditions?
2. Can the proposed method be extended to other game-theoretic settings, such as multi-agent general-sum games?
3. Does CED outperform other algorithms for adversarial zero-sum Markov games beyond Exploitability Descent (ED)?

### Soundness
3

### Presentation
3

### Contribution
3
