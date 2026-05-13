# Multi-Task Best Arm Identification with Risk Constraint

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
Best Arm Identification is a very challenging problem in sequential decision-making with many real-world applications. Existing works typically assume that all arms are feasible or/and deal with expectation-based constraints with strong assumptions, loose sample complexity bounds, and non-optimal algorithms. This paper introduces a multi-task best arm identification problem with risk constraint in the fixed-confidence setting, where each arm has multiple performance metrics. The agent aims to optimize one metric while ensuring that the quantiles of other metrics remain below specified thresholds for each task. We first derive a tight, instance-dependent lower bound on sample complexity. Based on this bound, we establish optimality conditions for the static optimal sampling ratio and illustrate how it balances among different tasks and constraints, while addressing the trade-off between optimality and feasibility. We derive a Track-and-Stop strategy with asymptotically optimal sample complexity and a computationally efficient strategy that iteratively solves the optimality conditions.  Finally, we extend our results to the linear bandit setting. Numerical experiments show that our algorithm performs relatively well.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper tackles the complex problem of Best Arm Identification in sequential decision-making, focusing on multi-task scenarios with risk constraints. The authors derive a tight lower bound on sample complexity and propose a Track-and-Stop strategy with optimal performance. Their approach balances tasks and constraints effectively, and results demonstrate strong performance in numerical experiments, extending findings to the linear bandit setting.

### Strengths
1. The methodology employed is robust, featuring a detailed analysis across several variants: the foundational algorithm is presented in Section 4.1, an optimized version in Section 4.2, and an adaptation to linear settings discussed in Section 5.

2. The numerical experiments conducted are thorough, employing ESR, ASR, and FWSR as benchmark algorithms.

### Weaknesses
The technical innovation presented in this paper appears to be limited. Algorithm 1 essentially replicates the Track-and-stop method referenced in [1]. Consequently, the paper's novelty should primarily be evaluated based on the efficient sampling rule introduced in Section 4.2. Nevertheless, this sampling rule closely resembles the BestChallenger method detailed in [1, Section 6], and Equation (17) directly corresponds to the definition of BestChallenger within this setting. Furthermore, the authors should have cited the BestChallenger method in Section 4.2 to acknowledge the previous researchers' efforts.

### Questions
see Weaknesses.

### Soundness
3

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
3

### Summary
This paper introduces a multi-task best arm identification problem with risk constraint in the fixed-confidence setting, where each arm has multiple performance metrics. The agent aims to optimize one metric, while ensuring that the quantiles of other metrics remain below specified thresholds for each task. The authors first build a tight, instance-dependent lower bound on sample complexity. Based on this bound, the authors establish optimality conditions for the static optimal sampling ratio, and illustrate how it balances among different tasks and constraints, while addressing the tradeoff between optimality and feasibility. In addition, the authors design a Track-and-Stop strategy with asymptotically optimal sample complexity, and a computationally efficient strategy that iteratively solves the optimality conditions. Finally, the authors extend their results to the linear bandit setting. Numerical experiments show that the proposed algorithm performs relatively well.

### Strengths
1.	The authors propose a multi-task BAI problem with risk constraint applicable to various real-world problems. The authors establish a tight, instance-dependent lower bound on the sample complexity required to guarantee a high probability identification of the feasible and optimal arm for each task.
2.	Based on the lower bound, the authors derive the optimality conditions for the static optimal sampling ratio, and discuss how this ratio balances the difficulty across different tasks and constraints, illustrating the trade-off between optimality and feasibility. In addition, the authors present a closed-form formula for the problem’s hardness by analyzing some challenging instances.
3.	The authors develop a Track-and-Stop strategy for the multi-task BAI problem with risk constraint, achieving asymptotically optimal sample complexity and a computationally efficient strategy that iteratively solves the optimality conditions. What’s more, the authors also extend their sample complexity results to the linear bandit setting. Numerical experiments show that the proposed algorithm performs well in comparison to several benchmarks.
4.	This paper is overall well-written and clearly organized.

### Weaknesses
1.	The motivation of the proposed problem formulation is not very clear. Can the authors describe 1-2 concrete application scenarios for the proposed problem formulation, in particular, connect the risk constraint formulation with real-world requirements on risk management.
2.	It is a little surprising that the sample complexity of Algorithm 1 (Theorem 3) perfectly matches the lower bound for the multi-task best arm identification problem with risk constraints, even for logarithmic factors. Can the authors give the intuition on why Algorithm 1 can avoid a union bound over the number of arms and tasks in the logarithmic factor?
3.	The formulas and notations in this paper are dense. The authors should add more intuition behind the algorithm design and theoretical results.

### Questions
Please see the weaknesses above.

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
This paper studies the problem of best arm identification with fixed confidence in a multi-task multi-objective constrained optimization setting. For each task and an arm, there are multiple metrics to consider with one primary metric that needs to be optimized while satisfying the quantile constraint for other metrics. At each time, the agent can choose a (task, metric, arm) tuple to sample, and receives the reward feedback of this specific chosen tuple, and no feedback from other metrics can be observed. The goal is to find for each task the best arm a^* which maximizes the primary metric while satisfying the constraint for all other metrics. The paper first provide and study a lower bound on the sample complexity from which the oracle static sampling strategy can be computed which requires the knowledge of the ground-truth reward of all arms, tasks and metrics. Then, the paper uses the same idea as [1] to convert the lower bound into a track-and-stop algorithm with asymptotic optimality guarantee. Computationally efficient algorithm and extension to linear bandits are also studied.

[1] Garivier, Aurélien, and Emilie Kaufmann. "Optimal best arm identification with fixed confidence." Conference on Learning Theory. PMLR, 2016.

### Strengths
This paper formulates the multi-task multi-metric best arm identification problem which models a wide range of applications. The study of quantile constraints as risk measure is of novelty in the best arm identification literature which generalizes the traditional constrained bandit problems which focus purely on expectation. The theoretical lower bound and a track-and-stop based matching algorithm are provided with provable guarantees. The paper also provides some insights towards instance-dependent hardness of the problem through analysis of the lower bound and the sample complexity. Lemma 1, Lemma2, and Proposition 1 provides some understanding on how the sub-optimality gaps and variances affect the problem hardness, and how the sample complexity scales with the number of tasks, arms, and metrics. Computationally efficient algorithms are also proposed in the paper which shows good performance in simulation results.

### Weaknesses
1. Presentation: The main body presentation of this paper is somewhat not satisfactory due to 1) the studied problem is unnecessarily complicated (also see 2. Formulation) which has too many variables and quantities, and 2) the notation system is not well established and the abuse of notation is quite frequent without declaration in the main body. The notations and equations in the main body are much too involved for general readers and the authors should reconsider to simplify the paper presentation structure and avoid unnecessary notations in the main body.

2. Formulation: The multi-task problem seems unnecessarily complicated. Even though the authors does not make very clear whether there is correlation between tasks and metrics in section 2, it seems in the paper's formulation, each task is independent of one another (even in the linear bandit formulation), and therefore the agent can solve the best arm identification problem of each task independently with certain confidence \delta' one-by-one, and combine the tasks together in the end with the help of independence among tasks. It also seems in the lower bound Theorem. 1, the inverse of complexity constant H^* is defined by equalizing the complexity of each task a, which essentially equalizes the probability of error for each individual task in asymptotic regime, which makes calculating the probability of error for each individual task possible.

3. Algorithm and Analysis: The paper follows a standard track-and-stop algorithm development and analysis machinery and naturally inherits the downside of track-and-stop type algorithms [1], i.e., the proposed Algorithm 1 needs to exactly solve a min-max problem at each step, which is computationally heavy and cannot be used in practice, and the provable guarantee Theorem 3 only holds for asymptotic regimes where \delta -> 0 which does not imply finite-time guarantees (which is also why ESR is worse than SEQSR in simulation). Based on the vast amount of track-and-stop literature in various bandits[1][2][3][4] and RL problems[5][6], the proposed algorithm and performance guarantees are somewhat expected. Even though computationally effecient algorithm is provided, it does not have provable sample complexity guarantee even in simplified models.

### Questions
1. Is there any specific reason that the best arm identification problem of all tasks need to be considered and solved all-together?
2. Is it possible to derive performance guarantees (asymptotic or finite-time) for the SEQSR algorithm which can be quantitatively compared with H^* or H in proposition 1?
3. The formulation that the agent needs to choose a metric at each time-step and only observes the reward of this metric lacks motivation. Even though this formulation is statistically harder, it also produces enough variables \omega in Theorem 1, so that one could convert the lower bound to the optimality condition in Theorem 2. The reviewer is curious on whether the algorithm development and analysis framework will still work for the setting where the reward of all metrics can be observed once an arm is pulled, i.e., Theorem 5. Is the algorithm development framework in the main body still applicable to Theorem 5? is it possible to derive the optimality condition for Theorem 5 analogous to Theorem 2?

Typo: line 409 ESR -> USR (seems this is correct according to the figure)

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel approach to the multi-task best arm identification (BAI) problem with risk constraints in a fixed-confidence setting. The authors derive a lower bound on sample complexity, establish optimality conditions for sampling ratios, and extend the Track-and-Stop strategy. They provide numerical experiments demonstrating the performance of their proposed algorithm.

### Strengths
1. The introduction of a multi-task BAI problem with risk constraints is a significant contribution to the literature. The problem is well-motivated with real-world applications.

2. The derivation of tight, instance-dependent lower bounds on sample complexity and optimality conditions provides a solid theoretical foundation for the proposed approach.

3. The experiments validate the algorithm's performance, showcasing its effectiveness compared to existing benchmarks.

### Weaknesses
(1) While the paper claims to address a multi-task best arm identification (BAI) problem with risk constraints by extending the work of Garivier & Kaufmann (2016), the contributions seem to overlap with existing works in BAI with safety constraints, such as the study by Wang et al. (2022). Specifically, the paper does not clearly articulate how the multi-task aspect fundamentally changes the problem compared to single-task BAI with safety constraints. The risk constraints, as presented, appear to be similar to safety constraints considered in other works, and the paper needs to provide a more detailed explanation of the novelty in their approach. It would be beneficial for the authors to more explicitly differentiate their approach from previous studies, providing a clearer rationale for the novelty of their contributions, particularly in how the multi-task setting interacts with risk constraints in a way that is not already addressed by existing literature on BAI with safety constraints. 

(2) There are missing periods at the end of formulas, such as in equations (8), (9), and (16). Please ensure all equations are properly punctuated for consistency and clarity.

### Questions
1.  How do you envision incorporating additional constraints, such as fairness, into your model? Are there specific challenges you anticipate?

2. Can you provide insights into the robustness of your results under varying conditions, such as experiments with different configurations?

### Soundness
4

### Presentation
4

### Contribution
4
