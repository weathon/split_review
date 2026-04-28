# Lasso Bandit with Compatibility Condition on Optimal Arm

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
<- trailing '%' for backward compatibility of .sty file
We consider a stochastic sparse linear bandit problem where only a sparse subset of context features affects the expected reward function, i.e., the unknown reward parameter has sparse structure.
In the existing Lasso bandit literature,
the compatibility conditions together with additional diversity conditions on the context features are imposed to 
achieve regret bounds that only depend logarithmically on the ambient dimension $d$.
In this paper, we demonstrate that even without the additional diversity assumptions, the compatibility condition \textit{only on the optimal arm} is sufficient to derive a regret bound that depends logarithmically on $d$, and our assumption is strictly weaker than those used in the lasso bandit literature under the single parameter setting.
We propose an algorithm that adapts the forced-sampling technique and prove that the proposed algorithm achieves $\mathcal{O}(\text{poly}\log dT)$ regret under the margin condition.
To our knowledge, the proposed algorithm requires the weakest assumptions among Lasso bandit algorithms under a single parameter setting that achieve $\mathcal{O}(\text{poly}\log dT)$ regret.
Through the numerical experiments, we confirm the superior performance of our proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper contributes to the high-dimensional bandits literature by relaxing the compatibility conditions required for analysis. Specifically, it reduces the need for compatibility conditions on all arms to only the optimal arm, thereby enhancing the generality of the results.

### Strengths
By weakening the compatibility condition from all arms to only the optimal arm and relaxing all other diversification requirement in other high-dimensional bandits papers, this paper makes a solid contribution that broadens the applicability of high-dimensional bandit algorithms. Figure 1 and Table 1 clearly sketched the comparison against existing literature.

### Weaknesses
 - While the paper criticizes other studies for unverifiable conditions, it does not clearly explain how the compatibility condition on the optimal arm (Assumption 3) is more verifiable in practice. Specifically, the paper does not provide any practical guidance or examples on how one would assess whether the optimal arm satisfies the compatibility condition in a real-world scenario. This lack of clarity weakens the argument against existing methods, as it is unclear if the proposed condition offers any practical advantage in terms of verifiability.

- The suggestion to treat the forced sampling iteration number  $M_0$  as a tuning parameter could also be applied to other methods where assumptions are stronger and cannot be easily verified as well. This undermines the significance of assuming compatibility for only the optimal arm, as the core issue of unverifiable assumptions is not effectively addressed. The paper does not provide a compelling argument as to why tuning $M_0$ is a more principled approach than tuning parameters in other methods with stronger assumptions.

- The proof sketch in Section 3.3 lacks sufficient emphasis on the techniques used to overcome the challenges posed by the weakened compatibility assumption. The paper does not clearly articulate how the analysis circumvents the need for a compatibility condition on all arms, which is a standard requirement in existing literature. Without a clear explanation of how the standard compatibility condition is avoided, readers may find it difficult to understand the paper’s methodological contributions, and the novelty of the approach is not fully apparent.

### Questions
See weakenesses.

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
The author devised an algorithm called FS-WLasso, which is based on a greedy algorithm with the addition of forced exploration. According to the authors, this algorithm demonstrates polylogarithmic regret even under the weakest assumptions in the context of sparse linear bandits in a stochastic environment. They also demonstrated the algorithm’s practical effectiveness through simulations.

### Strengths
- Soundness: In theoretical research, relaxing assumptions is undoubtedly meaningful. This work is particularly valuable in the sense that the authors united all various assumptions in sparse contextual linear bandits, and allows researchers to focus on a single general condition.

- Clarity: The authors clearly illustrated the relationship between their results and previous work using diagrams, and, through an extensive literature review, they included comparisons in multi-parameter setups to highlight the versatility of their setting (Remark 1). Additionally, their meticulous preparation is evident in the various remarks and supplementary materials to address anticipated questions (even the fixed arm set case) and to emphasize their significance/novelty.

- They also introduced a novel proof technique using induction - like a domino, they've constructed an interesting proof scheme to maintain their compatibility condition.

### Weaknesses
 - Their algorithm works on a more general 'environment', but to guarantee their performance the learning agent requires additional knowledge, such as the sparsity level $s_0$ or the gap $\Delta_0$. As they have mentioned, their result is not sparsity-agnostic. Even though they've mentioned in Appendix D, it is still true that they rely on the sparsity parameter $s_0$ and many other parameters, and I personally think this parameter is somewhat less general info than the noise level $\sigma$ or the norm bound of the context vector $x_{max}$.

- Why the exploration in Algorithm 1, line 5 should be a uniform one? I think the most intuitive exploration to guarantee the minimum eigenvalue is $a = argmax_{x\in x_t} \|\|x\|\|_{V_t^{-1}}$. 

- I don't understand why the fact that $M_0$ depends on multiple variables implies that it is a tunable parameter. Isn't it a worse situation, that a core parameter depends on multiple parameters (even $\Delta_*$ and $\phi_*$)? To compare it with Oh et al., 2021, it feels like 'an algorithm which is easy to run but should satisfy some strong assumptions on the environment' vs 'an algorithm which works on a weaker assumption but requires more information about the environment'. Some readers might think of this as an incremental improvement.

### Questions
- Why the exploration in Algorithm 1, line 5 should be a uniform one? I think the most intuitive exploration to guarantee the minimum eigenvalue is $a = argmax_{x\in x_t} \|\|x\|\|_{V_t^{-1}}$. 

- I don't understand why the fact that $M_0$ depends on multiple variables implies that it is a tunable parameter. Isn't it a worse situation, that a core parameter depends on multiple parameters (even $\Delta_*$ and $\phi_*$)? To compare it with Oh et al., 2021, it feels like 'an algorithm which is easy to run but should satisfy some strong assumptions on the environment' vs 'an algorithm which works on a weaker assumption but requires more information about the environment'. Some readers might think of this as an incremental improvement.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a weaker sufficient condition for high dimensional bandit algorithm. Under such weaker condition, the paper also proves regret bounds for bandit algorithms.

### Strengths
1. The authors provide a lot of intuitions for the algorithm design.
2. I think in general the weaker condition, and the algorithm induced, would be a good addition to the literature.

### Weaknesses
1. The paper needs to be restructured. If the key idea of this paper is the weaker condition proposed, then the main section and main results should be about this condition. Therefore, Appendix B should be the main part of the paper instead of just in the appendix. 
Besides, the novelty claimed, such as the cyclic induction (Lemma 6?), should be moved to the main text as well. It's hard to read and understand the novelty for the current version.
2. Assumption 3 is claimed to be "strictly weaker" than the existing conditions. Then, some counterexamples should be provided to show that Assumption 3 holds but not any of the existing conditions.

### Questions
N/A

### Soundness
3

### Presentation
1

### Contribution
2
