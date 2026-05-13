# Robust Reinforcement Learning with Structured Adversarial Ensemble

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Although reinforcement learning (RL) is considered the gold standard for policy design, it may not always provide a robust solution in various scenarios. This can result in severe performance degradation when the environment is exposed to potential disturbances. Adversarial training using a two-player max-min game has been proven effective in enhancing the robustness of RL agents. However, we observe two severe problems pertaining to this approach: ($\textit{i}$) the potential $\textit{over-optimism}$ caused by the difficulty of the inner optimization problem, and ($\textit{ii}$) the potential $\textit{over-pessimism}$ caused by the selection of a candidate adversary set that may include unlikely scenarios. To this end, we extend the two-player game by introducing an adversarial ensemble, which involves a group of adversaries. We theoretically establish that an adversarial ensemble can efficiently and effectively obtain improved solutions to the inner optimization problem, alleviating the over-optimism. Then we address the over-pessimism by replacing the worst-case performance in the inner optimization with the average performance over the worst-$k$ adversaries. Our proposed algorithm significantly outperforms other robust RL algorithms that fail to address these two problems, corroborating the importance of the identified problems. Extensive experimental results demonstrate that the proposed algorithm consistently generate policies with enhanced robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper examines the limitations of reinforcement learning (RL) in robust policy design due to potential environmental disturbances. It identifies two key issues in adversarial training for RL: over-optimism from complex inner optimization and over-pessimism from the selection of adversarial scenarios. The authors propose an adversarial ensemble approach to address over-optimism and optimize average performance against the worst-k adversaries to mitigate over-pessimism. The theoretical underpinnings of this method are presented, and its efficacy is demonstrated through comprehensive experimental results.

### Strengths
1. **Structure and Clarity**: The paper is well-structured and provides clear explanations, enhancing readability and comprehension.
  
2. **Clear Motivation**: The authors articulate the significance of addressing both over-optimism and over-pessimism in adversarial training, which effectively establishes the paper's purpose.

3. **Theoretical Foundation**: The paper offers a solid theoretical analysis, bolstering the credibility of the proposed method.

4. **Experimental Validation**: The inclusion of extensive experimental results substantiates the claims and demonstrates the practical benefits of the proposed algorithm.

### Weaknesses
1. **Figure Clarity**: Figure 1, intended to aid in understanding, is unclear. A more straightforward illustration with an improved caption is needed.

2. **Explanation of Solution to Over-Pessimism**: The rationale behind using the average performance over the worst-k adversaries, as presented in Section 3.2, requires further clarification to be convincing. Can the authors elaborate on how the average performance optimization directly counteracts over-pessimism?

Overall, in my opinion, the paper contributes a thoughtful approach to improving the robustness of RL algorithms, which is substantiated by both theoretical analysis and experimental results. Despite some ambiguity in graphical representation and the need for additional explanations in certain sections, the paper is a good candidate for ICLR. Clarity improvements in the mentioned areas could enhance the paper's impact.

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Deep reinforcement learning (RL) has demonstrated its capability to generate optimal strategies for environments with intricate dynamics. However, there are inherent challenges: the vastness of the parameter search space and limited exploration during training can compromise the robustness and performance guarantees of resulting policies. One technique that bolsters the resilience of RL agents is robustness through adversarial training. In this method, a hostile agent (adversary) aims to minimize the RL agent's cumulative reward by causing disturbances in the environment. Although this framework has strengths, two primary issues emerge: over-optimism due to difficulties in solving inner optimization problems, and over-pessimism from broad, imprecise candidate adversary sets which may consider unrealistic disturbance scenarios. To address these challenges, this study introduces a structured adversarial ensemble where multiple adversaries operate concurrently. This ensemble approach both improves the estimation of worst-case scenarios and shifts the RL agent's objective from absolute worst-case performance to an average of the most challenging scenarios. The proposed method outperforms existing robust RL strategies, and experiments show that it consistently enhances robustness across different environmental disturbances.

### Strengths
This paper is well-written and easy-to-follow.

### Weaknesses
* Limit technical novelty. RARL with an adversarial population is not a novel idea. The difference between ROSE and RAP is very incremental.
* The theorems and lemmas fall short of providing insights into the theoretical justification of the algorithm design, for example, why to optimize the performance over the worst-$k$ adversaries, how to choose the $k$ value, etc.
* One important assumption is that the adversaries are distinct enough from each other. However, there is no component in the algorithm that aims to improve diversity explicitly, such as in ADR (Bhairav Mehta et al., 2020). Therefore, I don't think it would be considered a 'structured ensemble'.
* Missing related work:
    * Shen, Macheng, and Jonathan P. How. "Robust opponent modeling via adversarial ensemble reinforcement learning." Proceedings of the International Conference on Automated Planning and Scheduling. Vol. 31. 2021.
    * Huang, Peide, et al. "Robust reinforcement learning as a Stackelberg game via adaptively-regularized adversarial training." Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence (IJCAI-22).
    * Zhai, Peng, et al. "Robust adaptive ensemble adversary reinforcement learning." IEEE Robotics and Automation Letters 7.4 (2022): 12562-12568.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper solves the "robust RL" problem by noting two major difficulties - over-optimism and over-pessimism - in the previous state-of-the-art. The robust RL considered in this paper is adversarial training using a two-player max-min game. This paper provides justifications for the proposed approach and evaluate extensively on benchmarks.

### Strengths
I think this work really pushes the adversarial RL community research efforts further by answering:

> can we design computationally efficient adversarial RL algorithms which are not pessimistic to unrealistic adversaries?

The main contribution of game-theoretic algorithm with solutions to two concerns (over-optimism and over-pessimism) raised in the adversarial problem setting is a really nice idea worthy for publication. My score reflect the weaknesses.

### Weaknesses
I have only a few weakness for this work as follows:

- In summary, this approach is finding appropriate number of adversaries (resolving over-optimism) to do a domain randomization (DR) step (averaging over worst-k adversaries) on top of these many adversaries. I see this paper mentions Mehta et al 2020 in related work but due credit to more DR works are missing. I am not sure of any DR-related works, but i'll appreciate if the authors can include more related works on these methodologies and discuss their differences with the current approach.

- Related work need to be better than combining all different settings into one paragraph:
> Subsequent works generalize the objective to unknown uncertainty sets, and formulate the uncertainty as perturbations/disturbance introduced into, or intrinsically inherited from, the environments, including perturbations in the constants which are used to define environmental dynamics (e.g., gravity, friction, mass) (Abraham et al., 2020; Mankowitz et al., 2019; Mehta et al., 2020; Pinto et al., 2017; Vinitsky et al., 2020a; Tessler et al., 2019; Vinitsky et al., 2020a;b), disturbance introduced to the observations (Zhang et al., 2020) and actions (Li et al., 2021; Tessler et al., 2019).

-- The current framework considers robustness against adversarial actions. Tessler et al., (2019) and thereafter are the closest to current work's setting. Of course then their algorithms need to be benchmarked against. 

-- Transition model perturbation can be justified in the framework mentioning the evolution of the environment depends on the adversarial actions. Model uncertainty in robust RL is defined in more generality [2-10]. So it will be better to include more detailed Related Works including [2-10] and more relevant works in the revision. I agree this work includes experiments with model uncertainty, and the baseline is M2TD3 that fits into [2-10] line of works. There also exists works on state uncertainty [1]. 

To summarize, major update on the related works is required. If published as is, due credit to appropriate works will be missed and misrepresented.
Side note: I've also stopped at '10' since you get the idea of inadequate related work discussion. 

I am open to discussions with the authors and reviewers to make sure the work quality matches the score, which I believe so at this point, but a potential reach to 8 definitely exists. All the best for future decisions!

[1] Robust Multi-Agent Reinforcement Learning with State Uncertainty Sihong He, Songyang Han, Sanbao Su, Shuo Han, Shaofeng Zou, and Fei Miao. Transactions on Machine Learning Research, June 2023.

[2] Xu. Z, Panaganti. K, Kalathil. D, Improved Sample Complexity Bounds for Distributionally Robust Reinforcement Learning. Artificial Intelligence and Statistics, 2023.

[3] Nilim, A. and El Ghaoui, L. (2005). Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798

[4] Iyengar, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280.

[5] Panaganti, K. and Kalathil, D. (2021). Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In Proceedings of the 38th International Conference on Machine Learning, pages 511–520.

[6] Panaganti, K. and Kalathil, D. (2022). Sample complexity of robust reinforcement learning with a generative model. In Proceedings of The 25th International Conference on Artificial Intelligence and Statistics, pages 9582–9602.

[7] Roy, A., Xu, H., and Pokutta, S. (2017). Reinforcement learning under model mismatch. In Advances in Neural Information Processing Systems, pages 3043–3052.

[8] Panaganti, K., Xu, Z., Kalathil, D., and Ghavamzadeh, M. (2022). Robust reinforcement learning using offline data. Advances in Neural Information Processing Systems (NeurIPS).

[9] Shi, L. and Chi, Y. (2022). Distributionally robust model-based offline reinforcement learning with near-optimal sample complexity. arXiv preprint arXiv:2208.05767

[10] L Shi, G Li, Y Wei, Y Chen, M Geist, Y Chi (2023) The Curious Price of Distributional Robustness in Reinforcement Learning with a Generative Model, NeurIPS 2023

### Questions
-na-

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
