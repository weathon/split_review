# POTEC: Off-Policy Contextual Bandits for Large Action Spaces via Policy Decomposition

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
We study off-policy learning (OPL) of contextual bandit policies in large discrete action spaces where existing methods -- most of which rely crucially on reward-regression models or importance-weighted policy gradients -- fail due to excessive bias or variance. To overcome these issues in OPL, we propose a novel two-stage algorithm, called Policy Optimization via Two-Stage Policy Decomposition (POTEC). It leverages clustering in the action space and learns two different policies via policy- and regression-based approaches, respectively. In particular, we derive a novel low-variance gradient estimator that enables to learn a first-stage policy for cluster selection efficiently via a policy-based approach. To select a specific action within the cluster sampled by the first-stage policy, POTEC uses a second-stage policy derived from a regression-based approach within each cluster. We show that a local correctness condition, which only requires that the regression model preserves the relative expected reward differences of the actions within each cluster, ensures that our policy-gradient estimator is unbiased and the second-stage policy is optimal. We also show that POTEC provides a strict generalization of policy- and regression-based approaches and their associated assumptions. Comprehensive experiments demonstrate that POTEC provides substantial improvements in OPL effectiveness particularly in large and structured action spaces.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces POTEC, a novel off-policy learning (OPL) method designed to handle large action spaces, a common challenge in real-world recommendation systems. The algorithm decomposes the policy into two stages: a first-stage policy that selects promising action clusters, and a second-stage policy that chooses specific actions within the selected cluster. The paper provides theoretical analysis showing that POTEC achieves unbiased gradient estimation under a local correctness condition. It also shows its cluster-based importance weighting leads to substantially lower variance compared to traditional methods. The authors present a complete learning framework, including how to optimize both policies through a combination of policy-based and regression-based approaches. Through extensive experiments on both synthetic and real-world recommendation data, POTEC demonstrates superior performance compared to existing methods such as IPS-PG and DR-PG, particularly when dealing with sparse action observations in logged data and large action spaces.

### Strengths
The paper introduces a novel two-stage approach to address the challenges of large action spaces in off-policy learning.

It demonstrates high quality through rigorous theoretical proof of the unbiasedness of the POTEC gradient estimator under local correctness condition, and shows how cluster-level importance weighting effectively reduces variance.

The paper provides clear theoretical justification for the two-stage decomposition and progresses logically from the problem formulation to the solution.

the paper addresses fundamental challenges in large-scale off-policy learning by providing a unified framework with theoretical guarantees for the joint optimization of two-stage policies.

### Weaknesses
The paper did not specify how different clustering algorithm could impact the performance of POTEC from both theoretical point of view and empirical study.

There could be more details provided on how the test data is constructed in empirical study.



### Questions
How test data is constructed in empirical study (both synthetic and real world experiment)? For example, is there overlap of context between test data and training data, if so how much overlap?

What will happen if full cluster support condition is not met in logging policy? In the real world, how do you check if this condition is met?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors derive a novel theoretical framework for off policy contextual bandits that strictly generalizes the complementary approaches of policy based and value based methods via a two stage decomposition involving both. It is argued that this provides a non-trivial advantage in large and structured action spaces. The two stage decomposition involves first using a policy based parametrization to identify an action cluster, followed by a regression based approach within each cluster to discriminate between the fine grained individual actions.

### Strengths
- Novel general approach for combining policy and value based learning methods in a hierarchical fashion so as to avoid bias and variance simultaneously.
- The paper is very well written and a pleasure to read
- Good discussion of related literature and its context for the current work.

### Weaknesses
 - A good bit of the technical novelty in the current paper is shared with  prior work [Saito et. al. 2023] which the authors duly point out. Having said, that the prior work applies a similar idea for off policy estimation while the current work deals with policy optimization.

- No satisfactory general recipe to perform the right kind of clustering that can best exploit such a two stage decomposition.

- The main issue with a regression based approach is non-zero bias due to model capacity as the authors point out,  and in practice this error seems more plausible to have its source in an inability to fit within cluster, if at all, rather than across clusters. However, this is precisely what is assumed for a good performance in the second stage. If it is assumed to do sufficiently well in the second stage, wouldn't this somehow make the problem more likely to achieve a low error for a simple supervised learning global fit?

### Questions
- Clustering the action space based on the scalar embedding of averaged marginal rewards seems somewhat surprising and not justified even informally -- can you comment on this? Have you considered a random bucketing strategy as a baseline for the first stage, and if so, how much better does proposed method do over this baseline?


- Is there a typo in Equation (3)? -- should the third variance term on RHS be $\hat{q} (x, a) s_\theta (x, a)$ ? For easier verification, please consider adding a quick derivation of this to the appendix.


- Is there a fundamental reason for the theory to only work with the policy at the base stage and value at the second stage? A footnote on page 4 is discussing this, but the implication is unclear for whether this is a fundamental difference. The point about the importance weights being an issue doesn't seem convincing since the same reasoning applies to the first stage in the current proposal.

### Soundness
4

### Presentation
4

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
This work studies the problem of off-policy learning for contextual bandit policies in large discrete action spaces. The authors propose an approach that decomposes the overall policy into two components: a cluster-selection policy and a conditional action-selection policy. To optimize the cluster-selection policy, they derive a policy gradient, while a pairwise regression procedure is used to learn the conditional action-selection policy. The authors provide a thorough analysis of the bias and variance of the proposed policy gradient estimator, which makes the work more solid and convincing. The authors perform comprehensive numerical studies to demonstrate the performance of the proposed algorithm compared to several baselines.

### Strengths
1. The authors study an important problem of off-policy learning for contextual bandit policies in large discrete action spaces.
2. The theoretical analysis of the bias and variance for policy gradient estimator makes the work more solid and convincing.
3. The authors perform comprehensive numerical studies to demonstrate the performance of the proposed algorithm

### Weaknesses
The clarity of the writing could be further improved by providing more details on certain aspects, such as practicability of the algorithm and experiment settings. See Questions section.

### Questions
1.	The selection of the number of clusters is a crucial aspect of the proposed method, as illustrated in the numerical studies. The author could provide more details on how to select the number of clusters in the real-world applications.
2.	Please provide more details on how to incorporate context-dependent clustering into the algorithm.
3.	The authors could compare the proposed method with Saito et al.,2023, highlighting performance differences and potential advantages/disadvantages.
4.	Please provide more details on data generating mechanism in the real-world experiment.
5.	The authors could consider mentioning potential limitations of the proposed method.

### Soundness
3

### Presentation
3

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
This paper provides a solution to off-policy learning for large action spaces through a two-stage policy. The action space is first clustered with action embedding (reward). Then, the first-stage policy selects an action cluster, and the second-stage policy selects an action within the cluster. The two-stage policy is updated with the policy gradient method, providing a bias and variance analysis of the gradient. They show that the bias of the gradient is controlled by the relative difference in the reward estimation and can be further reduced with a pairwise regression if possible. Also, they show that the variance of the gradient is significantly smaller than the gradient of the original action space (which is straightforward). Empirical studies demonstrate its effectiveness.

### Strengths
1, propose a novel new two-stage policy for OPL for bandits with large action space and the intuition/motivation is well-justified.

2, provide a variance and bias analysis of the gradient of the proposed algorithm and connect with the algorithm. Also, the proposed gradient has a smaller variance than the IPS method. 

3, the paper is well-written, solid, easy to follow.

### Weaknesses
1, The paper did not provide very detailed description of the clustering algorithm. More details will be preferred. Specifically, the paper should clarify the distance metric used for clustering, the specific clustering algorithm (e.g., k-means, hierarchical), and how the action embeddings are initialized before clustering. The current description lacks the necessary detail for reproducibility.

2, The paper did not discuss how the number of the cluster 'C' can affect the performance of the algorithm. While the paper mentions that the cluster size controls the reliance on policy-based or regression-based components, it does not provide a clear guideline on how to choose the optimal number of clusters for a given problem. A more thorough analysis of the trade-offs associated with different cluster sizes is needed.

3, They did not experiment with other logging policy settings. The paper focuses on a specific logging policy that aligns with the two-stage structure of the proposed method. However, it is unclear how the algorithm would perform with more general logging policies that do not explicitly consider the cluster structure. This is a significant limitation as real-world datasets often come from diverse logging policies.

4, Others, see questions.

### Questions
1, How do you choose the number of cluster C? 

2, how do you get the embedding of action a? Is it from the reward estimation? (more details of the clustering is beneficial)

3, do you assume the logging policy $\pi_0$ known? What if it is not known?

4, Is the logging dataset sampled based on the ground-truth cluster? If I understand correctly when creating the logging dataset, you first cluster the action based on the reward of $(x,a_i)$, and then you have a reward for both cluster r(x,c_a) and r(x,a|c). What if the reward is not in this hierarchy way? For example, if the reward function is just defined as r(x,a) instead of the reward of cluster + reward of the action. Or, in other words, what if the logging policy is not defined as Eq.(11)? I believe that this algorithm might benefit from the logging policy and reward definition while it might not work that well in a more general logging policy. Because the logging policy itself is somehow a two-stage policy.

I am willing to further raise my score if these questions are addressed.

### Soundness
3

### Presentation
3

### Contribution
3
