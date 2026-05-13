# Clusters Agnostic Network Lasso Bandits

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
We consider a multi-task contextual bandit setting, where the learner is given a graph encoding relations between the bandit tasks. The tasks' preference vectors are assumed to be piecewise constant over the graph, forming clusters. At every round, we estimate the preference vectors by solving an online network lasso problem with a suitably chosen, time-dependent regularization parameter. We establish a novel oracle inequality relying on a convenient restricted eigenvalue assumption. Our theoretical findings highlight the importance of dense intra-cluster connections and sparse inter-cluster ones. That results in a sublinear regret bound significantly lower than its counterpart in the independent task learning setting. Finally, we support our theoretical findings by experimental evaluation against graph bandit multi-task learning and online clustering of bandits algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores a multi-task contextual bandit setting where tasks are connected by a graph structure, encoding relationships between them. Here, user preference vectors are assumed to form clusters within the graph, but the algorithm doesn’t explicitly determine these clusters. Instead, it uses a **network lasso** approach with a dynamic regularization parameter, promoting smoothness in preferences within clusters while allowing for distinct clusters across the graph.

### Strengths
Key contributions include:

1. **Oracle Inequality:** The authors establish an oracle inequality leveraging a restricted eigenvalue condition, which helps ensure the accuracy of preference vector estimations.
2. **Regret Bound:** The proposed approach achieves sublinear regret, showing improved performance over independent task models, especially in large-scale graphs with high-dimensional contexts.
3. **Theoretical and Empirical Results:** The paper provides theoretical bounds on estimation error and regret, supported by experiments comparing this method to other graph-based and clustering bandit algorithms, demonstrating its effectiveness in high-dimensional settings.

The work is relevant for recommendation systems and similar applications where user preferences are unknown initially but can be inferred from limited interactions, exploiting known relationships among tasks to enhance learning efficiency.

### Weaknesses
1. The paper mixes problem setting with algorithms which creates confusion: e.g., Eq. (2) about how $\hat \Theta$ is updated is not related to problem setting.
2. The paper sometimes refer to elements of $\mathcal V$ by task, sometimes by user (e.g. Line 129).

3. The setting is agnostic to the graph. It then becomes opaque to me why we must utilize the graph structure, and how utilizing the graph structure could benefit.
4. The paper seems to restrict their study to the particular algorithm of network Lasso. This choice seems not justified, and I'm not convinced by its importance. 
5. The regret bound seems to have no dependency on dimension $d$. This seems strange, e.g. if we plug in $|\mathcal V| =1$ to Theorem 3.

### Questions
1. How do I interpret your results and their dependence on various parameters associated with the clusters? You mention different types of network structures but the results are very opaque ( so are the implications of the assumptions).

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
2

### Summary
This paper propose a bandit algorithm based on network lasso and provide improved regret bound based on the technique.

### Strengths
Network lasso seems to be an interesting technique applied to bandit problems.

### Weaknesses
The paper presents an approach to solving the multi-task learning problem by partitioning tasks into clusters, stipulating that tasks within each cluster share the same reward model, meaning they utilize the same feature vector. This approach is particularly relevant in scenarios where the number of clusters exceeds the problem dimension $d$; otherwise, the problem effectively reduces to a low-rank multi-task learning problem, which has been extensively studied in the literature. Therefore, to assess the significance of the results, it is crucial to compare both the theoretical and experimental findings with those from low-rank multi-task learning studies. However, the simulations conducted only address cases where the number of clusters is greater than the dimension, which raises questions about the completeness of the experimental analysis. 

The relaxed symmetry and balanced covariance assumptions in Assumption 2, while borrowed from prior work, lack a thorough discussion regarding their implications for real-world applicability. Specifically, the paper does not provide sufficient justification for why these assumptions are reasonable in practical scenarios, or how violations of these assumptions might impact the performance of the proposed method. Furthermore, the paper's reliance on Assumption 3, which posits that tasks within the same cluster share identical reward parameters, is a strong assumption that limits the applicability of the method. While the authors suggest this is most relevant when the number of clusters exceeds the dimension $d$, the paper does not adequately explore the implications of this assumption in other settings, or provide a clear rationale for why such a strict condition is necessary. The experimental section lacks a comprehensive comparison with existing low-rank multi-task learning methods, particularly in scenarios where the number of clusters is less than or equal to the dimension $d$. This omission makes it difficult to assess the true contribution of the proposed method, as it is unclear whether the performance gains are due to the novel approach or simply a consequence of the low-rank structure of the problem.

### Questions
N/A

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
3

### Summary
This paper studies a multi-task linear contextual bandits setting. The tasks are embedded in a graph $G=(V,E)$. The paper shows the regret bound for the network Lasso policy, which updates the parameter estimation in a predefined way, and presents numerical experiment results to show the effectiveness of the network Lasso policy.

### Strengths
This paper gives a rather complete analysis to the network Lasso policy.

### Weaknesses
1. The paper mixes problem setting with algorithms which creates confusion: e.g., Eq. (2) about how $\hat \Theta$ is updated is not related to problem setting.
2. The paper sometimes refer to elements of $\mathcal V$ by task, sometimes by user (e.g. Line 129).

### Questions
1. The setting is agnostic to the graph. It then becomes opaque to me why we must utilize the graph structure, and how utilizing the graph structure could benefit.
3. The paper seems to restrict their study to the particular algorithm of network Lasso. This choice seems not justified, and I'm not convinced by its importance. 
3. The regret bound seems to have no dependency on dimension $d$. This seems strange, e.g. if we plug in $|\mathcal V| =1$ to Theorem 3. (Update: I'm better understanding the paper after the authors' response. Basically, to compare this with linear bandits, I think the polynomial dependency in $d$ becomes the polynomial dependency in a param that's related to the graph structure. I'd raise my score.)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates multi-task contextual bandit settings, wherein the learner is provided with a graph that encodes the relationships among the bandit tasks. It is assumed that the preference vectors for these tasks are piecewise constant over the graph, thereby forming distinct clusters. To estimate the reward parameters, the paper formulates and solves a network lasso problem in each learning round.

### Strengths
The paper addresses federated multi-task learning, a growing area of interest due to its collaborative nature that enhances the effectiveness of the learning process. The paper presents both theoretical and experimental results.

### Weaknesses
The paper presents an approach to solving the multi-task learning problem by partitioning tasks into clusters, stipulating that tasks within each cluster share the same reward model, meaning they utilize the same feature vector. This approach is particularly relevant in scenarios where the number of clusters exceeds the problem dimension $d$; otherwise, the problem effectively reduces to a low-rank multi-task learning problem, which has been extensively studied in the literature. Therefore, to assess the significance of the results, it is crucial to compare both the theoretical and experimental findings with those from low-rank multi-task learning studies. However, the simulations conducted only address cases where the number of clusters is greater than the dimension, which raises questions about the completeness of the experimental analysis.

### Questions
1. What are the relaxed symmetry and balanced covariance assumptions in Assumption 2, and how do these assumptions impact the practical applicability of the method?

2. Assumption 3 states that tasks within the same cluster share the same reward parameter. Under this condition, the problem aligns with the well-explored domain of low-rank multi-task learning. As noted in the paper, the only justification for this approach is when the number of clusters exceeds the dimension d. However, this scenario is typically uncommon and may limit the broader applicability of the method. To this end, 

     a) Please clarify how the approach differs from or improves upon low-rank multi-task learning methods when the number of clusters exceeds d.

    b)  Also, discuss potential applications or scenarios where having more clusters than dimensions would be relevant.

3. In all the experiments conducted, the number of clusters is smaller than $d$, effectively reducing the problem to a low-rank multi-task learning problem, as studied in works such as Yang et al. and Lin et al. Therefore, the significance of the contribution needs to be reassessed, as it aligns with existing literature on low-rank multi-task learning. Some relevant representative works are:
Yang et al. Impact of representation learning in linear bandits, arXiv:2010.06531, 2020.
Lin et al., Fast and Sample Efficient Multi-Task Representation Learning in Stochastic Contextual, ICML, 2024.

    a) Can you include experimental comparisons with low-rank multi-task learning methods for the scenarios presented in Figure 1?

    b) Can you add experiments where the number of clusters exceeds d to demonstrate the unique benefits of their approach in those cases?

4. Can you provide an experimental comparison with the low-rank multi-task learning results presented in Yang et al. and Lin et al., given that all the plots in Figure 1 correspond to a low-rank case?

5. Can you compare the proposed approach with the low-rank multi-task learning results specifically for settings where the number of clusters exceeds the problem dimension? This comparison is crucial to demonstrate the effectiveness of the proposed method, as the paper emphasizes these scenarios.

6. Can you provide a table or figure comparing the regret bounds of the proposed approach in this paper with those of the relevant baseline methods? This comparison would help to clarify how the proposed method performs relative to established approaches in terms of regret guarantees. Further, can you discuss the implications of any differences in the regret bounds, particularly for cases where the number of clusters exceeds d?

### Soundness
3

### Presentation
2

### Contribution
3
