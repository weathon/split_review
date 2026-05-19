### Summary

This paper addresses the challenge of delayed treatment responses in heterogeneous treatment effect (HTE) estimation. The authors present a novel framework, CFR-DF (Counterfactual Regression with Delayed Feedback), which accounts for potential response times in addition to eventual outcomes. They establish theoretical identifiability results for potential outcomes and response times, then implement an EM algorithm to jointly estimate these quantities. The method is evaluated through experiments on simulated and real-world datasets, demonstrating its effectiveness in scenarios with delayed feedback.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper formalizes the delayed response problem in HTE estimation and proposes a method to address it, which is an important problem in many areas.
2. The paper provides theoretical guarantees for identifiability and proposes a practical algorithm to solve the problem.
3. The experiment is well-designed and shows the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Estimating Counterfactual Treatment Responses in User Behavior Time Series with Recurrent Neural Networks
[2] Causal Imitation Learning with Delayed and Noisy Reward
[3] DeR-CFR: Countering Delayed Feedback in Heterogeneous Causal Effect Estimation
[4] Dealing with delayed responses in stochastic bandit optimization
[5] A/B testing with delayed feedback: A matching-based approach

#### comment

1. The paper does not sufficiently discuss some important related works. For example, [1, 2, 3] also study the problem of delayed feedback. Specifically, the authors should discuss the difference between their work and these papers, and include them in the experiment. It is important to clarify how the proposed method differs from these existing approaches, particularly in terms of the assumptions made and the types of delayed feedback they can handle. For instance, [1] focuses on time-series data and uses RNNs, while [2] addresses noisy rewards in imitation learning, and [3] specifically targets heterogeneous causal effect estimation with delayed feedback. The authors need to clearly articulate the novelty of their approach in the context of these related works.
2. The methods section could benefit from a more intuitive explanation. It would be helpful to clarify the authors' reasoning for using an EM algorithm to solve the problem. Specifically, the connection between the EM algorithm and the identifiability results should be made more explicit. The authors should explain why the EM algorithm is a suitable choice for this particular problem, and how the E-step and M-step are derived from the problem formulation. A more detailed explanation of the algorithm's convergence properties and limitations would also be beneficial.
3. The paper's assumptions require further discussion. For example, the authors should explain in detail when the monotonicity and principal ignorability assumptions hold. The monotonicity assumption, which implies that treatment never harms an individual, is a strong assumption that may not hold in all scenarios. The authors should provide examples of when this assumption is valid and when it is not. Similarly, the principal ignorability assumption, which is related to the unconfoundedness assumption, needs to be discussed in more detail, including its implications and limitations. The authors should also discuss the sensitivity of their results to violations of these assumptions.
4. The authors propose a method for estimating HTE with delayed feedback, but it is not clear how they validate the identifiability of potential response times. It would be helpful if they could provide more insights into this aspect. While the paper provides theoretical identifiability results, it lacks empirical validation of these results. The authors should discuss how they can verify that the potential response times are indeed identifiable in practice, and how this identifiability affects the performance of their method. It would be beneficial to include experiments that specifically test the identifiability of response times, perhaps by simulating data with known response times and evaluating the accuracy of the estimated response times.
5. The authors should also discuss the relationship between their work and other related areas, such as delayed feedback in bandits [4] and A/B testing [5]. The authors should clarify how their work differs from these areas, and whether their method can be applied to these settings. For example, the delayed feedback in bandits [4] often deals with sequential decision-making, while A/B testing with delayed feedback [5] focuses on observational data. The authors should discuss the similarities and differences between these settings and their proposed method.

### Suggestions

The paper addresses an important problem in heterogeneous treatment effect estimation, specifically the challenge of delayed treatment responses. However, the paper could be significantly improved by providing a more thorough discussion of related work and a more intuitive explanation of the proposed method. The authors should explicitly compare their approach with existing methods that address delayed feedback, such as those using recurrent neural networks for time-series data [1], methods for causal imitation learning with noisy rewards [2], and methods for heterogeneous causal effect estimation with delayed feedback [3]. A detailed comparison should highlight the specific assumptions and limitations of each approach, and clearly articulate the novelty of the proposed method. Furthermore, the authors should include these existing methods in their experimental evaluation to demonstrate the superiority of their approach.

To enhance the clarity of the methods section, the authors should provide a more intuitive explanation of why an EM algorithm is used to solve the problem. The connection between the identifiability results and the EM algorithm should be made explicit. The authors should explain how the E-step and M-step are derived from the problem formulation, and why the EM algorithm is a suitable choice for this particular problem. A more detailed explanation of the algorithm's convergence properties and limitations would also be beneficial. For example, the authors could discuss the conditions under which the EM algorithm is guaranteed to converge to a local optimum, and how the choice of initialization affects the final solution. Additionally, the authors should provide a more detailed explanation of the practical implementation of the algorithm, including the choice of hyperparameters and the computational cost.

Finally, the authors should provide a more detailed discussion of the assumptions made in their work, particularly the monotonicity and principal ignorability assumptions. The authors should explain when these assumptions are likely to hold and when they might be violated. For example, the monotonicity assumption, which implies that treatment never harms an individual, is a strong assumption that may not hold in all scenarios. The authors should provide examples of when this assumption is valid and when it is not. Similarly, the principal ignorability assumption, which is related to the unconfoundedness assumption, needs to be discussed in more detail, including its implications and limitations. The authors should also discuss the sensitivity of their results to violations of these assumptions. Furthermore, the authors should discuss the relationship between their work and other related areas, such as delayed feedback in bandits and A/B testing, and clarify how their work differs from these areas.

### Questions

Please see the weakness part.

### Rating

5

### Confidence

4

**********
