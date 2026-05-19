### Summary

This paper studies the problem of multi-armed bandits in matching markets with indifference. The authors propose a centralized algorithm that achieves a regret bound of $O(NK\log(T)/\Delta^2)$, where $N$ is the number of players, $K$ is the number of arms, $T$ is the total time horizon, and $\Delta$ is the minimum non-zero preference gap. The authors also provide experiments to validate the effectiveness of the proposed algorithm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The problem of multi-armed bandits in matching markets with indifference is well-motivated and interesting.
3. The proposed algorithm achieves a regret bound of $O(NK\log(T)/\Delta^2)$, which is close to the lower bound of $\Omega(N\log(T)/\Delta^2)$.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the algorithm is limited. The proposed algorithm is a variant of the explore-then-Gale-Shapley algorithm, and its design is not particularly innovative.
2. The lower bound in (Sankararaman et al., 2021) is established for the decentralized setting, while the upper bound in this paper is established for the centralized setting. These two results are not comparable, and the authors should not highlight the near-optimal results of the proposed algorithm.
3. The paper lacks a discussion of the lower bound for the setting with indifference. It is unclear whether the lower bound for the decentralized setting can be extended to the setting with indifference.
4. The paper does not discuss the optimality of the proposed algorithm for the decentralized setting, which is a significant limitation.

### Suggestions

The paper would benefit from a more thorough discussion of the algorithm's novelty. While the authors position it as a variant of explore-then-Gale-Shapley, a more detailed comparison to existing algorithms in the matching market literature is needed. Specifically, the authors should clarify what specific challenges in the indifference setting their algorithm addresses that are not addressed by existing methods. A more detailed explanation of how the arm-guided adaptive exploration strategy differs from existing exploration strategies in matching markets would also be beneficial. Furthermore, the authors should provide a more rigorous justification for the specific design choices in their algorithm, such as the exploration schedule and the method for eliminating suboptimal arms. This would help to establish the algorithm's novelty and contribution to the field.

To address the issue of comparability with the lower bound, the authors should provide a more detailed discussion of the differences between the centralized and decentralized settings. They should explain why the lower bound for the decentralized setting does not apply to their centralized algorithm. Furthermore, the authors should discuss the challenges of extending their algorithm to the decentralized setting and what modifications would be needed. This would help to clarify the limitations of their current work and provide a roadmap for future research. The authors should also discuss the possibility of deriving a lower bound for the centralized setting, which would provide a more meaningful comparison for their algorithm's performance.

Finally, the paper needs a more in-depth discussion of the lower bound for the setting with indifference. The authors should explore whether the existing lower bound for the decentralized setting can be extended to the indifference setting, and if not, what the challenges are in deriving such a bound. They should also discuss the implications of the lack of a lower bound for the indifference setting on the evaluation of their algorithm's performance. Furthermore, the authors should discuss the optimality of their algorithm for the decentralized setting, even if they do not provide a concrete algorithm or analysis. This would help to clarify the potential for improvement and guide future research in this area.

### Questions

Please see the weaknesses above.

### Rating

5

### Confidence

3

**********
