# A Game-theoretic Approach to Personalized Federated Learning Based on Target Interpolation

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Contrary to classical Federated Learning (FL) that focuses on collaborative learning of a shared global model via a central server, Personalized Federated Learning (PFL) trains a separate model for each user in order to address data heterogeneity and meet local demands. This paper proposes pFedGT, a method for personalized Federated Learning based on a Game-theoretic approach, that adopts a novel formulation termed "Target interpolation." In specific, each user solves a local optimization problem that comprises of a weighted average of two terms: one for the local loss (based on the user's data) and one for the global loss (based on all the data in the system). The latter is, of course, not accessible to the users (due to the large data volumes and privacy concerns) and it is approximated using second-order expansion which allows for an efficient federated implementation. In pFedGT, the users play a game (by minimizing their local problems), and the algorithm supports partial participation in each round. We prove existence and uniqueness of a Nash equilibrium and establish a linear convergence rate under standard assumptions. Extensive experiments on real datasets under variable levels of statistical heterogeneity are used to portray the merits of the proposed solution. In particular, our method achieves on average 2.6\% and 3.0\% higher accuracy on CIFAR-10 and CIFAR-100 datasets, and 3.17\% on HAR dataset than leading baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposed a new personalized federated learning model based on a weighted average of local and global loss, and further approximate it into a game formulation. The proposed model attains Nash equilibrium, the corresponding algorithm attains linear convergence. Extensive numerical experiments further showcased the superiority of the algorithm.

### Strengths
1. New model for PFL
2. The proposed algorithm outperforms existing works in the experiments.

### Weaknesses
1. The introduced regularization term $\frac{\rho}{2}||w_i||^2$ appears to be primarily for theoretical convenience, specifically to ensure strong convexity, which facilitates the proof of Nash equilibrium existence and linear convergence. While this approach is not entirely novel, drawing parallels to techniques like those in FedProx [1], the paper could benefit from a more thorough justification of this term's practical implications. The necessity of making the function strongly convex should be further discussed, particularly in the context of non-convex optimization landscapes common in deep learning.

2. The proposed model introduces several hyperparameters ($\mu, L, \gamma_i$) that require careful tuning. This raises concerns about the practical applicability of the method, especially when compared to classical federated learning algorithms that typically involve fewer parameters. A more detailed discussion on the sensitivity of the model's performance to these hyperparameters and guidelines for their selection in different scenarios would enhance the paper's practical value.

3. There is an apparent mismatch between the theoretical requirements and the experimental setup. Specifically, the theory necessitates $\rho > L$, yet the experiments suggest that $\rho=0$ not only works but also outperforms other values. This discrepancy needs to be explicitly addressed and thoroughly discussed. A deeper analysis of why the theoretical constraints do not seem to hold in practice would provide valuable insights into the model's behavior and potentially reveal interesting avenues for further research.

4. The reliance on game theory to frame the proposed algorithm warrants further scrutiny. Given that the additional regularization term, which seems to be the primary link to the game-theoretic framework, appears unnecessary in practice (as suggested by the $\rho=0$ case), one might question whether the game theory perspective is essential for the paper. Exploring whether the algorithm can be effectively presented and analyzed within a standard optimization framework, potentially focusing on convergence to stationarity in the non-convex case, could be a worthwhile direction. This could potentially simplify the paper's narrative and make it more accessible to a broader audience.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an interesting personalized Federated Learning method. In this method, the local objective functions are modeled through a combination of the objective functions from all clients. Additionally, the authors present an approximation technique that allows for the estimation of objective functions from other clients without the necessity of transmitting local data. Experimental results demonstrate the effectiveness of the proposed approach.

### Strengths
1. Modeling clients' objective functions as a composite of individual clients' objective functions is promising. 
2. The existence and uniqueness of a Nash equilibrium are provided.
3. The experiments demonstrate the proposed method is useful.

### Weaknesses
1. The hyper-parameter $\gamma$ is a crucial element controlling the strength of the objective functions of other clients. Nevertheless, the authors have not conducted adequate experiments to elucidate how algorithm performance varies with different values of $\gamma$. Specifically, the paper lacks a systematic analysis of how different $\gamma$ values affect the convergence rate and final performance for individual clients, especially in heterogeneous data scenarios. It's unclear if a single $\gamma$ value is optimal for all clients or if personalized $\gamma$ values are needed.
2. In the case of Theorem 2, it appears that when $\gamma = 1$ (indicating no collaboration), the algorithms achieve the most favorable convergence results. This raises concerns about the practical utility of the proposed method, as it suggests that collaboration, which is the core of the method, might actually hinder convergence.
3. The formulation of Theorem 2 seems to address the convergence rate with only one local step, which suggests it may be more relevant to traditional distributed algorithms rather than federated learning algorithms. The theorem does not explicitly account for the multiple local updates that are typical in federated learning, making its relevance to the proposed method questionable.
4. Assumption 2 is not common in PFL. It would be better if more justification is provided. The assumption lacks a clear connection to practical federated learning scenarios, and it's unclear how this assumption would hold in real-world settings with diverse client data distributions and varying levels of local computation.
5. The hyper-parameter $\rho$ plays a pivotal role in Theorem 2, and the theorems are only valid when $\rho \ge \max_{i} (L \cdot L_{F_i})$. However, the results in Figure 10 indicate that setting $\rho = 0$ consistently yields favorable results. While I understand the authors' choice to ensure strong-convexity by setting $\rho \ge \max_{i} (L \cdot L_{F_i})" for theoretical purposes, it introduces a significant disparity between theory and experimental outcomes. This discrepancy between theory and practice undermines the practical relevance of the theoretical analysis.
6. Regarding Algorithm 1, the communication overhead seems heavy, as there is an additional $c^t$ that needs to be exchanged between server and clients, besides the model. This additional communication cost could be a significant bottleneck in resource-constrained federated learning environments.

### Questions
1. Could the authors give more explanations about Theorem 2?
2. Could the authors provide more discussions on the $\rho$ and $\gamma$?
3. Could the authors provide more details about the experiment settings? Additionally, the number of clients should be increased.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the personalized federated learning (PFL) problem where local agents do not completely follow the global model and keep local models for their local demands. The authors claim they address the problem using the game-theoretic approach to model the PFL problem with a target interpolation (a linear combination of local objective and global objective), where the local deployed model parameters are considered the agents' strategies in the game. The authors then show that after adding a sufficiently strong L2 regularizer to the local objective, the PFL problem using the pFedGT algorithm will converge to a unique solution (Nash equilibrium).

### Strengths
The authors provides a complete story with problem formulation, algorithm pseudo code, theoretical convergence guarantee and numerical experiments showing the performance of pFedGT on the PFL problem defined in this paper.

### Weaknesses
1. The rationale for formulating this PFL problem within a game-theoretic framework is not adequately justified. While the updating dynamics bear resemblance to FedAvg, the modification of replacing the "local loss" with a "linear combination of local loss and global loss" appears to enhance collaboration rather than induce strategic non-cooperation. Consequently, the application of a game theory framework does not seem to offer significant advantages in terms of intuition or analytical clarity. It is not immediately obvious how the agents' strategic behavior, as modeled in this framework, differs substantially from standard federated learning scenarios where agents aim to minimize their local losses. A more detailed explanation of the strategic interactions and the resulting equilibrium would be beneficial.
2. There are areas within the paper where the presentation could be substantially improved. For instance:
(1). The definition and significance of the heterogeneity level \\alpha in Figure 1 are unclear. Is it synonymous with the \\alpha in Theorem 2? Providing a visual representation or a more intuitive explanation of how \\alpha influences data distribution and its relationship to the theoretical results would greatly enhance understanding.
(2). The discussion regarding the utilization of 'c' on page 4 is initially confusing. Explicitly directing readers to Algorithm 2 and elaborating on the role and implications of 'c' within the algorithm's context would improve clarity.
3. The assertion that Assumption 1 is the sole assumption is debatable. The requirement for a sufficiently strong regularizer to ensure strong convexity raises concerns about the practical applicability of the method beyond specific scenarios like Cifar classification. Furthermore, under the conditions of Lipschitz continuity and strong convexity, the uniqueness of the solution and convergence are relatively straightforward, diminishing the need for novel proof techniques. The reliance on a strong regularizer might limit the applicability of the proposed method in scenarios where such strong regularization is undesirable or impractical.
4. The theoretical results do not delve into how the aggregation interval and the partial participation schemes impact convergence. This omission leaves a gap in understanding the practical implications of these factors on the algorithm's performance.
5. The distinctions between this work's setting and results compared to previous works are not readily apparent. Incorporating a comparative table that outlines the setting, assumptions, solution existence and uniqueness, and convergence guarantees of related works would significantly aid in contextualizing the contributions of this paper.

### Questions
1. Is the game theoretic framework a necessity? If so, why is that? 
2. If the agents strategically change \gamma_i and only optimize the local loss, can your framework generalize to that and how may the results look like?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the issue of Personalized Federated Learning and proposes pFedGT, a method for personalized Federated Learning based on a Game-theoretic approach, that adopts a formulation termed “Target interpolation.” This paper conducts detailed experiments on the proposed algorithm, and the experimental results demonstrate that the algorithm achieves better performance on multiple datasets.

### Strengths
1. The experimental section of this paper is shown in detail, comparing the performance of the proposed algorithm with other algorithms on multiple datasets. The results indicate superior performance.

### Weaknesses
1. My major concern is the lack of novelty. The proposed idea of target interpolation in this papers seems to bear some resemblance to the concept of model interpolation presented in 'Three Approaches for Personalization with Applications to Federated Learning'(Mansour et al). From the algorithmic perspective, the essence of the algorithm proposed in this paper is still the introduction of a new regularization technique, unrelated to the game-theoretic approach.

2. Although this paper emphasizes that its algorithm is a game-theoretic approach, in reality, both the algorithm design and theoretical analysis lack the incorporation and analysis of game-theoretic principles. In fact, only a single sentence at the end of Section 3.1 briefly mentions the concept of Nash equilibrium and claims that each user iteratively solves the problem to achieve Nash equilibrium, which I doubt. I hope the authors can provide more theoretical and experimental analysis about game theory instead of merely mentioning the concept of Nash equilibrium.

3. The algorithm lacks protection for user model privacy. Unlike most federated learning approaches that update models by transmitting gradients in each round, the algorithm proposed in this paper transmits information c_i between the agent and server, where c_i is the gradient subtracted by the user's own model parameters. For most users, transmitting their own model parameters to the server is not acceptable compared to algorithms that only transmit gradients. (This is likely to happen when the user's model gradually converges, and c_i is approximately equal to μ w_i. Users who value model privacy are unlikely to accept this situation.)

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
