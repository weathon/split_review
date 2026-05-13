# GLANCE: Global Actions in a Nutshell for Counterfactual Explainability

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
The widespread deployment of machine learning systems in critical real-world decision-making applications has highlighted the urgent need for counterfactual explainability methods that operate effectively. Global counterfactual explanations, expressed as actions to offer recourse, aim to provide succinct explanations and insights applicable to large population subgroups. Effectiveness is measured by the fraction of the population that is provided recourse, ensuring that the actions benefit as many individuals as possible. Keeping the cost of actions low ensures the proposed recourse actions remain practical and actionable. Limiting the number of actions that provide global counterfactuals is essential to maximize interpretability. The primary challenge, therefore, is balancing these trade-offs—maximizing effectiveness, minimizing cost, while maintaining a small number of actions. We introduce GLANCE, a versatile and adaptive framework, comprising two algorithms, that allows the careful balancing of the trade-offs among the three key objectives, with the size objective functioning as a tunable parameter to keep the actions few and easy to interpret. C-GLANCE employs a clustering approach that considers both the feature space and the space of counterfactual actions, thereby accounting for the distribution of points in a way that aligns with the structure of the model. T-GLANCE provides additional features to enhance flexibility. It employs a tree-based approach, that allows users to specify split features, to build a decision tree with a single counterfactual action at each node that can be used as a subgroup policy. Our extensive experimental evaluation demonstrates that our method consistently shows greater robustness and performance compared to existing methods across various datasets and models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces two heuristics for global counterfactual explanations, namely C-Glance and T-Glance. The idea of C-Glance is to cluster instances based on their similarity in the feature space or the possible recourse actions. T-Glance is a decision tree based method. For both the introduced techniques, the goal is to maximise effectiveness and minimise the cost, with a small number of actions.

### Strengths
1) The idea of clusters both based on the similarity in the feature space and the possible recourse actions is simple and very relevant.

2) Overall, the paper is clear and easy to follow.

### Weaknesses
1) The novelty of the proposed work is very limited, particularly the methodological novelty.

2) It is unclear what are the main innovations and differences with the existing literature (e.g., how is T-Glance different from Kanamori et al., 2022.  Is the idea of clustering according to both features and actions novel?)

3) The discussion of the proposed methods lacks completeness. For example, C-Glance depends on the number of candidate actions, the initial number of clusters, and the number of actions, but there is no adequate discussion on their impact on the results and on how to select them.

### Questions
Please, comment on weaknesses 2) and 3).

Furthermore, what is the definition of cost in the paper? It seems defined only for the toy example, is t the same employed in the whole paper?

### Soundness
3

### Presentation
2

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
This paper introduces new algorithms for finding global counterfactual explanations (GCE) as a small set of actions that can offer recourse to most of the affected population. Any solution to the GCE problem must navigate a tradeoff among the number of actions, the cost of implementing these actions, and the proportion of the population that can effectively use them for recourse. This work specifically examines the case where the number of actions is fixed and explores the tradeoff between cost and effectiveness.

The paper differentiates between explicit and implicit GCE and proposes two algorithmic frameworks for each. Given that solving GCE with a fixed size is NP-hard in general, the proposed solutions focus on finding efficient GCEs. Empirical evaluations on standard CE datasets show that the proposed approach outperforms existing GCE methods in terms of Pareto optimality and is also computationally efficient.

### Strengths
The proposed framework is intuitive, well-designed, and novel. Although it lacks theoretical guarantees, several design choices are particularly effective. For instance, in C-GLANCE, it is insightful to consider the similarity of actions rather than focusing solely on features.

I appreciate how the paper differentiates between explicit and implicit GCE.

The empirical results are strong.

### Weaknesses
I think the formulation of GCE as a set of actions rather than directions could benefit from further justification. My default understanding of GCE aligns with GLOBE-CE, which focuses on directions for recourse rather than the actions themselves.

The overall presentation of the paper could be significantly improved. The authors are encouraged to elaborate on the rationale behind certain design choices. I have asked clarification questions in the question section regarding this. In particular, I’m not sure I fully understand Section 4 (T-GLANCE).

I also found it challenging to understand average cost (avc) and the tradeoff with size. If an action is added to the action set C, the recourse cost (rc) for x in the previous C decreases. However, by definition, |X_C| increases, meaning new instances in X_C contribute positively to avc. As a result, it’s unclear how avc behaves as size(C) increases. I expected a definition that clearly illustrates this tradeoff. Given that the results hinge on this concept, further discussion on this choice would be beneficial.

Minor issues: page 3 (computationally efficiently -> efficient), page 5 (min in Problem 1 can be misread as a min of the set), page 8 (can you avoid using red and purple in Table 1? It's hard for me to distinguish them visually)

### Questions
When calculating the distance between two clusters, why do you focus only on the distance between the average actions in each cluster? I’m curious if the average is the right summary statistic in this context.

Additionally, when merging clusters, do you retain all of their respective actions? Wouldn’t it be beneficial to prune the action set as part of the merging process?

I’m also unclear on why the evaluations of implicit and explicit GCE are not separated. Further elaboration here could help clarify the distinction between explicit and implicit GCE.

Finally, you might consider using additional metrics beyond Pareto dominance. For instance, Tables 2 and 3 suggest that Fast AReS and GLANCE perform similarly, but Table 1 gives the impression that GLANCE has notably better effectiveness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new framework for the global counterfactual explanation problem, which is a task of assigning actions to a given set of individuals by considering their effectiveness, cost, and size. The authors propose two algorithms: C-GLANCE and T-GRANCE. The former first partitions individuals into some clusters and then merges them by taking into account not only the dissimilarity of their centroids but also that of actions generated for the centroids. The latter algorithm recursively partitions individuals like CART, where the best split condition is determined by the improvement in the effectiveness score after splitting. By extensive experiments, the authors demonstrated the effectiveness of the proposed methods compared to the existing baselines, including AReS and CET.

### Strengths
Overall, I think this is a good paper, and the authors make solid contributions to the research area of counterfactual explanation. 
- S1. This paper is well-written, well-organized, and easy to read. 
- S2. I think the proposed framework is simple but effective. The proposed algorithms have only intuitive hyper-parameters, which may be a  desirable advantage compared to AReS and CET whose hyper-parameters are hard to tune. 
- S3. The effectiveness of the proposed method was demonstrated through extensive experiments with major baselines for the global counterfactual explanation.

### Weaknesses
While the efficacy of the proposed methods is well demonstrated empirically, I believe the following concerns should be addressed to improve the quality of this paper. 
- W1. One of my concerns is the computation cost of the proposed algorithms. For both algorithms, we need to generate diverse actions for each centroid many times. In particular, Algorithm 2 needs to compute the total effectiveness gain for all the candidates of split conditions in Line 9, which may incur a significantly high computational cost. To compute the total effectiveness gain for one split condition, we have to generate actions for two centroids after splitting and then compute each effectiveness value. In addition, we need to repeat such a heavy procedure for all the candidate split conditions. Although I recognize the average running times of the proposed algorithms in the experiments were less than roughly a few minutes in Appendix F, I am worried about their scalability when we have more candidates of split conditions and larger datasets. The paper does not provide a clear analysis of how the number of candidate split conditions impacts the runtime, which is a critical aspect for practical applications.
- W2. Another concern is that this paper includes no theoretical result on the proposed method. I am aware that Theorem 3 in Appendix A shows the hardness of the global counterfactual explanation problem. However, the proposed algorithms are heuristic without theoretical perspectives, and there is no guarantee for the quality of their obtained solution. In addition, there is no analysis of the time complexity of the proposed algorithms as well. While the authors mention the multi-objective nature of the problem, they do not provide any theoretical bounds or guarantees on the solution quality, which is a significant limitation. The lack of theoretical analysis makes it difficult to assess the robustness and generalizability of the proposed algorithms.

### Questions
- Q1. How were the candidates of split conditions of Algorithm 2 determined in the experiments?
- Q2. Could you show analyses of the time complexity of the proposed algorithms?
- Q3 (optional). As far as I remember, AReS and CET have several hyper-parameters. How were these values determined in the experiments?
- Q4 (optional). As the authors mention in Line 285, we can use any dissimilarity score as two distances $d_1$ and $d_2$ in Algorithm 1. What dissimilarity score could be considered appropriate, especially for $d_2$? Also, how do they affect the solution, i.e., partition and actions?
- Q5 (optional). Is there any way to compute the total effectiveness gain more efficiently? For example, in the case of the popular CART-like algorithms, we can compute the information gain for each candidate split condition in an amortized constant time if we have sorted training samples by the value of each feature in advance. In a similar way, can we efficiently calculate the total effectiveness gain?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes GLANCE,  a technique used to provide actionable feedback to individuals impacted by machine learning decisions. The framework focuses on creating global counterfactual explanations (GCE) that can be applied across larger groups instead of individual cases, making it more useful for real-world applications like loan approvals or hiring. The GLANCE framework optimizes three factors for effective recourse: minimizing the number of actions to keep it interpretable, ensuring the actions are cost-effective, and maximizing coverage so that most individuals benefit from these actions.

GLANCE consists of two algorithms: C-GLANCE, which clusters individuals based on features and counterfactual actions to create generalizable solutions, and T-GLANCE, which uses a tree structure for more flexible and interpretable group-specific actions.

### Strengths
The paper addresses a problem relevant to many real-world users of explanation systems.

The work is easy to read and seems mathematically sound. The experiment section is sane and all the claims in the intially sections seem to be justified through the paper.

I like the premise of this paper. I'm willing to increase my score if the authors do the suggested work.

### Weaknesses
It seems that Equi-explanation maps[1] also divides the feature subspace into regions that have similar recourse options, but in a top down manner. They also seem to compute sub-space centroids, nearest decision boundary points etc and even merge the clusters under certain constraints. Given that these works are very similar, I think it is important that the authors place their work against Equi-explanation maps, at least in the related work section, and preferably treat it as a competing system. 

Additionally, I think it would be good to evaluate the effectiveness of such algorithms via a user study. While recourse cost is a good human-engineered metric, it would be interesting to see if the recourse computed by different algorithms were equally helpful to end users.

### Questions
Why did you prefer a clustering approach over a top-down division approach in order to create subspaces? Can you discuss the pros and cons of each approach for solving the recourse problem in explanations?

What would a user study design, to test the real world effectiveness of this algorithm as compared to competing algorithms look like?

If deployed in the real world today, what would bad edge cases for the proposed algorithm look like? Are there scenarios where the recourse algorithm can malfunction? Can it suggest incorrect recourse in any case?

### Soundness
3

### Presentation
3

### Contribution
3
