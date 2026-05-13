# Federated Offline Policy Learning with Heterogeneous Observational Data

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
We consider the problem of learning personalized decision policies from observational bandit feedback data across multiple heterogeneous data sources. Moreover, we examine the practical considerations of this problem in the federated setting where a central server aims to train a policy on data distributed across the heterogeneous sources, or clients, without collecting any of their raw data. We present a policy learning algorithm amenable to federation based on the aggregation of local policies trained with doubly robust offline policy evaluation and learning strategies. We provide a novel regret analysis for our approach that establishes a finite-sample upper bound on a notion of global regret against a mixture distribution of clients. In addition, for any individual client, we establish a corresponding local regret upper bound characterized by measures of relative distribution shift to all other clients. Our analysis and supporting experimental results provide insights into tradeoffs in the participation of heterogeneous data sources in policy learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an federated optimization procedure for off-policy learning over heterogeneous data sources, where the observational data is collected by multiple clients using different behaviour policies and stored only locally.
Specifically, the central server needs to maximize the doubly robust policy value estimator (Zhou et al. 2022b) over the (parametric) policy space, without transferring the raw observational data. In the proposed procedure, this is achieved by letting each client locally compute its model update by calling an online const-sensitive multi-class classification (CSMC) oracle and then the server performs a global update via a weighted average over the local model updates.

To the best of my knowledge, this is the first work that studies off-policy learning under federated setting.

### Strengths
The problem of off-policy learning in federated setting is well-motivated, and the authors have provided a solution with regret guarantee.

### Weaknesses
1. My main concern is the technical novelty, and I'd appreciate if the authors can provide more clarification on the contribution compared with the existing work mentioned below.

Based on my understanding, the main difference of this paper, compared with existing off-policy learning method using doubly robust estimator, e.g., Zhou et al. (2022b), lie in the optimization oracle. i.e., this paper needs to solve the CSMC problem over multiple heterogeneous clients to update the policy, instead of in a centralized setting. However, I am not sure if this has led to any technical challenge in obtaining the global regret bound in Theorem 1. Specifically, while the use of FedAvg is understandable, the paper does not clearly articulate the specific challenges that arise from the heterogeneous data distributions across clients when applying this method to the doubly robust estimator. The regret bound seems to follow standard analysis, and it's unclear what novel technical insights are gained from the federated setting beyond simply applying a distributed optimization algorithm. The paper would benefit from a more detailed explanation of how the heterogeneity impacts the regret analysis, and if there are any novel techniques required to handle this.

2. With CSC, we typically have a non-concave non-convex objective function to optimize, which makes finding the policy that maximizes Eq 8 difficult. Therefore, I expected the regret analysis to cover the situation where the FedAVG-CSMC procedure can only provide policy with certain approximation error. Moreover, even if the objective function is easy to optimize, it still seems to be unrealistic to assume we can obtain the exact maximizer of Eq 8 under federated setting, as this requires infinite number of iteration/communication rounds. I'd appreciate it if the authors can provide more insights on how the current analysis can be extended to allow for approximation error of Eq 8. The analysis currently assumes access to the exact maximizer, which is a strong assumption, and the paper does not discuss the practical implications of this assumption. It would be beneficial to see a discussion on how the regret bounds would change if the optimization procedure only converges to an approximate solution, and how the approximation error impacts the overall performance.

### Questions
In Section 3.2, notations like $X^{C}, Y^{C}$ are not formaly defined.

The author mentioned that Assumption 3 can be easilly satisfied under regularity assumption. Can the authors provide a more formal description of the regularity assumption?

### Soundness
3 good

### Presentation
4 excellent

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
This paper studies the problem of learning personalized decision policies from observational bandit feedback data across multiple heterogeneous data sources. In the federated setting, a central server aims to train a policy on data distributed across the data sources without directly accessing the raw data. The paper proposed a policy learning algorithm amenable to federation, based on the
federated averaging algorithm with local model updates provided by online cost-sensitive classification oracles.  Finite-sample upper bounds are provided for a notion of global regret, and local regrets for each agent. Empirical local and global regret bounds are compared across different experimental settings.

### Strengths
- Overall the paper is written with a good clarity. The authors studied a practically significant problem of learning personalized decision policies from multiple heterogeneous data sources, and demonstrated that the proposed algorithm can be extended to the federated setting. 
- The assumptions and the regret upper bound analysis were detailedly described. In particular the theoretical analysis on local regret was a good compliment to the analysis on global regret, and shows their discrepancy due to client heterogeneity. 
- The local and global regret bounds were compared empirically via simulated data.

### Weaknesses
 - The upper bounds were based on a few detailed data assumptions, such as local ignorability, unconfoundedness, and overlap. Although the paper mentioned that some of the assumptions can potentially be relaxed, there is a lack of details on the discussion, and which assumption may not be relaxed fundamentally. Specifically, the local ignorability assumption, which requires that within each data source, the treatment assignment is independent of the potential outcomes given the observed covariates, is a strong assumption that may not hold in many real-world scenarios. The paper does not adequately discuss the implications of violations of this assumption, nor does it provide guidance on how to assess the plausibility of this assumption in practice. Furthermore, the overlap assumption, which requires that for each data source, there is a non-zero probability of observing each treatment for any given covariate, is also a strong assumption that may be difficult to satisfy in practice, especially when dealing with high-dimensional covariate spaces. The paper should provide a more detailed discussion of the limitations imposed by these assumptions and how they might affect the practical applicability of the proposed method.
- In the theoretical analysis part (section 4-5), the main innovation part for the algorithm / estimator design and regret analysis in comparison to prior works was not clearly highlighted. The paper presents a federated version of existing offline policy learning techniques, but it does not clearly articulate what specific novelties are introduced in the algorithm design or the regret analysis. The theoretical results appear to be a straightforward extension of existing results to the federated setting, and the paper does not clearly identify the key technical challenges that were overcome in this extension. A more detailed discussion of the technical innovations and the specific challenges addressed by the proposed approach is needed.
- The empirical evaluation did not include any comparisons with other baselines, or any real dataset, and the heterogeneous setting was fairly simply constructed. The experiments only compare the proposed federated approach to a non-federated approach, which does not provide a comprehensive evaluation of the method's performance. The paper should include comparisons with other relevant baselines, such as federated learning algorithms that are not specifically designed for offline policy learning, or other methods for handling heterogeneous data sources. Furthermore, the use of simulated data limits the generalizability of the results, and the paper should include experiments on real-world datasets to demonstrate the practical applicability of the proposed method. The heterogeneous setting in the simulation is also quite simple, and the paper should explore more complex heterogeneous settings to better understand the method's performance under different conditions.

### Questions
- Can the nuisance parameters be learnt jointly instead of being required to be separately known or estimated in the policy value estimates?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of learning personalized policies from heterogeneous data sources in the federated setting.
They proposed a federated policy learning algorithm that averages locally trained policies with doubly robust policy evaluation. And, they provided finite-sample analysis on global and local regret bounds in terms of a mixture of distribution of clients and a relative distribution shift to all other clients, respectively.

### Strengths
1. This work provides finite-time regret upper bounds of the proposed policy learning algorithm in global and local perspectives, which characterize the effect of client skewness and client heterogeneity on global policy learning and individual policy learning of clients, respectively.
2. This work empirically demonstrated the effect of client heterogeneity on federated policy learning and suggested a skewed mixture for global policy training to overcome the performance degradation due to distribution shift.

### Weaknesses
1. The proposed algorithm appears to be a straightforward application of FedAvg to the CSMC setting. While the paper presents a federated policy learning algorithm, it lacks a clear articulation of the unique challenges encountered when extending offline policy learning to the federated setting with FedAvg. A more in-depth discussion is needed to highlight the novel aspects of this approach compared to existing federated learning or federated reinforcement learning (RL) literature. For instance, how does the heterogeneity of data across clients impact the convergence properties of the algorithm in this specific context, compared to standard supervised learning tasks? Are there specific challenges related to the two-stage process of estimating nuisance functions before defining the optimization objective in a federated setting?

2. The regret analysis hinges on the assumption that the algorithm converges to the optimal policy, which may not always hold true. The authors suggest that achieving optimal policies is possible via some additive term and appropriate policy class selection. However, this claim is vague and lacks sufficient justification. A more rigorous explanation is required to clarify how the algorithm can achieve the optimal policy for general policy classes beyond the linear case. Specifically, what are the properties of the policy class that guarantee convergence to the optimal policy? How does the choice of the policy class interact with the federated nature of the learning problem?

3. Assumption 1-(c) seems to necessitate a full exploration of all actions, which is a strong requirement. While some offline RL works suggest that full coverage of the state-action space may not be strictly necessary, this assumption appears to contradict those findings. A more detailed discussion is needed to justify the necessity of this assumption in the context of federated policy learning. Does the federated setting introduce specific challenges that necessitate full exploration? How does this assumption impact the applicability of the algorithm to real-world scenarios where full exploration might be infeasible?

4. The experimental validation of the algorithm is limited to very specific settings. It remains unclear whether the proposed approach can be effectively applied to more general and realistic scenarios. Expanding the experimental evaluation to encompass a wider range of environments and tasks would strengthen the paper's contributions. Furthermore, a comparative analysis against other baseline algorithms is crucial to demonstrate the superiority of the proposed method. For instance, how does the performance compare to a centralized approach where all data is pooled together? How does it compare to other federated learning algorithms adapted to the policy learning setting?

### Questions
See the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of learning personalized policies on observational data collected from heterogeneous multiple sources. To ensure privacy and other data safety requirements, this paper studies the problem under a specific federated setting with a central server that collects no raw data from individual data sources. 

First, based on a federated averaging algorithm, this paper proposes a policy learning algorithm that abides by the federation requirement. 

Then a regret analysis is provided for the algorithm, which considers two notions called global regret and local regret. For both notions, finite sample regret upper bounds depending on quantified heterogeneity are presented. 

Finally, experimental results verify the dependence of the regret on the client heterogeneity.

### Strengths
**Significance**: this paper studies offline learning under heterogeneous data sources, an important problem setting in machine learning

**Quality**: the quality of the paper is good. Definitions are introduced without ambiguity; theoretical results looks solid to me; experimental details are given.

**Originality**: this paper considers the federation under the problem setting, which I deem as original

**Clarity**: this paper is very well written and easy for the readers to follow.

### Weaknesses
I did not detect any major technical flaw or major weakness in this paper. 

Still, I have a few questions I hope the author can address. Please see the Questions session. 

Furthermore, I think this paper, as a theoretical work, would significantly benefit from adding a sketch of proof for its main results.

### Questions
I think the problem setting is original. However, it is unclear to me what the technical novelty of this paper is. 

Specifically, in the analysis/proof of the theorems, does there exist any technical challenge and how are they resolved? 

Any novel trick adopted?

It would be great if the author could elaborate on this.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
