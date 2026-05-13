# Approximated Behavioral Metric-based State Projection for Federated Reinforcement Learning

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Federated reinforcement learning (FRL) methods usually share the encrypted local state or policy information and help each client to learn from others while preserving everyone's privacy.
In this work, we propose that sharing the approximated behavior metric-based state projection function is a promising way to enhance the performance of FRL and concurrently provides an effective protection of sensitive information.
We introduce FedRAG, a FRL framework to learn a computationally practical projection function of states for each client and aggregating the parameters of projection functions at a central server. 
The FedRAG approach shares no sensitive task-specific information, yet provides information gain for each client.
We conduct extensive experiments on the DeepMind Control Suite to demonstrate insightful results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a new Federated Reinforcement Learning(FRL) framework, FedRAG that shares the approximated behavior metric-based state projection function between clients to enhance performance. The framework learn a projection function of states for each client and aggregating the parameters of projection functions at a central server. The framework is further evaluated with experiments on the DeepMind Control Suite.

### Strengths
- Proposed a new algorithm that enhance the performance of FRL.
- The experiment show the effectiveness of the algorithm.

### Weaknesses
 - It would be better to have a problem formulation section with assumptions using in the algorithm.
- Section 3 could be improved, for example, it would be better to explain what global critic Q network will be used in the algorithm with a few more sentences.
- The presentation of the experiments could be better, for example, for each of the experiment in section 5.4, explain why algorithm proposed is better/similar/worse than the baselines. The plot can be a bit bigger as well.
- It remains unclear why increasing $\lambda$ does not enhance performance in the same environment. The paper lacks a theoretical explanation or further experiments to support this observation.

### Questions
- How many clients are there when evaluating the algorithm? and how does the number of clients affect the performance of the algorithm?
- In section 5.2, why increasing lambad can't improve the performance of the algorithm in the same environment? Shouldn't sharing parameters increase the training speed?

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
4

### Summary
This work considers the problem of federated reinforcement learning, i.e., training a set of RL agents in a distributed fashion by sharing certain model parameters. The authors propose a scheme that, instead of sharing the raw states and rewards or the raw policy / value network parameters, instead shares the parameters of a representation learning function that maps the raw state to a (lower-dimensional) vector.  To learn this representation, a behavioral metric is used to quantify the distance between two states. The authors propose a way of estimating this metric by replacing intractable quantities with neural networks. The method is compared with several local and federated RL strategies.  The authors argue that this method also provides effective protection of sensitive information.

### Strengths
S1. The proposed FedRAG technique is interesting, appears sound and (mostly) attains favorable results over the baselines.

S2. The paper is generally well-written and organised.

### Weaknesses
W1. The claims of the technique providing "effective protection of sensitive information" are tenuous and should be proven or otherwise removed. Even though the method does not share e.g. the raw states, in my opinion it is possible to devise a fairly straightforward attack to recover them. An attacker can use the exposed mapping function to find the representation of a given set of states, similar to the application of a hash function. If the state space is sufficiently small (or reasonable guesses can be generated), the original states can be recovered. While there is a certain degree of "obfuscation" over sharing the raw states, the method is not secure in a cryptographical sense. The authors should acknowledge that the method provides only a limited form of obfuscation, not true privacy, and that the representation function itself could be a target for adversarial attacks aiming to reconstruct the original state space.

W2. The Gaussianity assumptions for the reward and dynamics are very strong and we can expect there will be many enviroments that violate these assumptions. The method might still work in practice nevertheless given the use of the learned representations. To counter this point, the authors may want to show results for the method on some (toy) environments where this assumption is violated. The current experiments do not sufficiently address this concern, and it is important to demonstrate the method's robustness under non-Gaussian conditions. The authors should consider including experiments with environments that exhibit multi-modal reward distributions or non-linear dynamics to better assess the limitations of the Gaussian assumption.

W3. There are some presentational issues (detailed in the comments) that should be addressed.

### Questions
C1. The formulae in Section 3.2 are mostly identical to those in Section 3.1 except for the superscripts and specifying how the global critic network parameters are updated (Eq 8). It is probably better to only present the version in 3.2 to remove the duplication, and to use the space gained to present some of the results that were relegated to the appendix, especially the comparison with methods beyond local RL.

C2. A few remarks regarding notation:
- The notation $\phi_{\omega^k}$ is used in Section 3.2 in the presentation of FeSAC, which suggests that this method also uses the representation function. However, 4.1 specifies that using this encoding is something new that is introduced by your method, unlike FeSAC? This should be clarified as it is confusing.
- Use $\mathbb{E}$ instead of $E$ in Section 4 for consistency.
- Use $\approx$ instead of $=$ for Equation 13?
- Eq 17: $\theta$ already denotes the parameters of the critic network.

C3. Regarding the figures:
- The result figures are a bit hard to parse, I'd suggest separating the "same environment" and "other environment" in different subplots so they are easier to distinguish. You should also make sure the colors are consistent across plots (e.g. in Figure 7 the colors for FedRAG differ from those used in the main text).
- In Fig 4, the highest point for the "Local_other_env" curve is higher than that of "FedRAG_other_env", which is not consistent with the interpretation in the text.

C4. L530 mentions that further results are presented in the appendix. You should briefly summarise what experiments were ran and what were the high level conclusions. Additionally, I would strongly encourage (see also C1) making some room for part of the results in the appendix in the main text. In my opinion, the results for the evaluation compared to baselines are more important than the results for tuning $\lambda$. 

C5. Typos and small nitpicks
- Space missing before citation on L39
- L180: are you referring to the optimal policy here? If so, it is the policy that achieves the highest reward in expectation
- "As follow" -> "As follows" (L189, L221, possibly elsewhere)
- L378: "sever"
- L427: space missing before DMC acronym introduction

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes FedRAG, a federated reinforcement learning (FRL) framework designed to improve generalization across clients with heterogeneous environments. FedRAG’s primary innovation is sharing a behavioral metric-based state projection function, rather than raw states or policies, to achieve privacy-preserving federated reinforcement learning. Experiments on tasks from the DeepMind Control Suite indicate potential improvements in generalization and performance across environments.

### Strengths
+The approach of sharing behavioral metric-based state projections in a federated reinforcement learning (FRL) setting is an innovative idea.

+Addressing privacy in FRL through state projections based on behavioral metrics could make a significant contribution, given the growing concerns around data privacy in federated setups.

### Weaknesses
After a close review, I am inclined to recommend rejection due to key issues in theoretical rigor, completeness of related work, and empirical validation.

1. Novelty and Related Work: 

The paper overlooks critical related work in FedRL, especially recent developments that are highly relevant to FedRAG’s contributions. Notably, Fan et al. [1] formulates the objectives of FedRL under homogeneous environments. How does FedRAG’s objective differ from that? Are you working for the same objective but just for heterogeneous environment? A clear comparison with that or similar work is essential to establish whether FedRAG advances beyond its approach, particularly in terms of generalization mechanisms. This omission diminishes the reader’s ability to assess the incremental value FedRAG brings over existing methods. Similarly, Jin et al. (2022) [2], which the authors also reference, studies FedRL under diverse environments with a focus on handling client heterogeneity. However, the differences between FedRAG and this approach are not adequately explained, leaving the novelty of FedRAG’s method ambiguous. A more comprehensive discussion of these related works is needed to contextualize FedRAG’s scholarly contribution, thereby emphasizing its novelty and addressing gaps in prior research.


2. Theoretical Justification and Privacy Guarantees. FedRAG’s claim of privacy-preserving state projections lacks both theoretical analysis and empirical privacy guarantees:

a. Although FedRAG claims privacy benefits by sharing behavioral projections, the paper does not analyze the resilience of these projections against known privacy attacks, such as gradient leakage or inference attacks. Without this, the paper’s privacy claims are incomplete: i) The privacy analysis via Bayesian inference is overly simplified; ii) Claims about privacy preservation being a "side effect" are not rigorously justified. Formal guarantees about information leakage through projection parameters are needed to support the claims.

b. The paper claimed “with theoretical guarantees” as one contribution in the introduction. however, no convergence analysis is provided, and neither are the formal guarantees about approximation quality. 

c. After reading the manuscript, it remains unclear how FedRAG’s state projection mechanism affects convergence across clients with varying dynamics. It is also unclear how the method scales with environment complexity. A theoretical discussion, or at least some empirical convergence tests under heterogeneous settings, would strengthen the rigor of the method.


3. insufficient empirical validation on generalization.

The paper claims to improve generalization through the FedRAG method. However, all the experiments report episode rewards without specific metrics to measure generalization across environments. Incorporating quantitative metrics to assess generalization quality, such as task adaptation scores or cross-environment similarity, would provide a more robust evaluation of FedRAG’s contributions regarding generalization.

### Questions
In what ways do the objectives of this paper differ from or advance beyond the existing literature?

### Soundness
1

### Presentation
3

### Contribution
2
