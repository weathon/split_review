# Learning guarantee of reward modeling using deep neural networks

- Decision: Reject
- Scores: 6, 6, 6, 5, 5

## Abstract
In this work, we study the learning theory of reward modeling using pairwise comparison data and deep neural networks. We establish a novel non-asymptotic regret bound for deep reward estimators in a non-parametric setting, which depends explicitly on the network architecture. Furthermore, to underscore the critical importance of clear human beliefs, we introduce a margin-type condition requiring the conditional winning probability of the optimal action in pairwise comparisons to be significantly distanced from 1/2. This condition enables a sharper regret bound, which substantiates the empirical efficiency in Reinforcement Learning from Human Feedback (RLHF) and highlights the role of clear human beliefs in its success. Notably, this improvement stems from high-quality pairwise comparison data under the margin-type condition and is independent of the specific estimators used, making it applicable to various learning algorithms and models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper gives a regret analysis of reward model learning that incorporates
1. An upper bound of average reward regret in terms of the L_2 functional error of the learned reward function, under a margin condition.
2. An L_2 functional error guarantee of the maximal-likelihood neural network reward function solution with the holder-smooth realizability condition.

### Strengths
The paper is clearly written and easy to follow. That includes
1. clear illustrations of the relationship between regret, functional error of the reward model, and the maximal-likelihood solution
2. clear statements of the assumptions 
3. clear proofs
The paper provides a good characteristic of the reward signal distribution that go beyond the BT models.

### Weaknesses
1. The assumptions in the paper may be restrictive, namely the realizability of the reward model (the existence of an underlying model) and the data coverage assumption (the 2nd smallest eigenvalue of the data coverage Laplacian). This happens to not to match current practice where the signal is sparse and there may not be a true reward model. Specifically, the assumption that a true reward function exists and can be perfectly represented by the chosen function class is a strong one. In many real-world scenarios, especially with human preferences, the underlying reward signal might be complex, noisy, or even non-existent, making the realizability assumption questionable. The data coverage assumption, relying on the second smallest eigenvalue of the data coverage Laplacian, also seems quite strong. It implies that the dataset must sufficiently explore the state-action space, which is often not the case in practice, particularly in sparse reward settings. The paper does not adequately address the implications of violating these assumptions, which could significantly limit the applicability of the theoretical results.

2. Many proofs in the paper seem standard in the literatures, especially the generalization analysis of holder-smooth neural networks. That reduces the contribution in novelty of the whole paper. While the paper does combine several existing techniques, the specific application to reward modeling with pairwise comparisons does not seem to introduce significant novel theoretical insights. The generalization analysis for Holder-smooth neural networks, while necessary, is not a new contribution in itself. The core argument relies on established error decomposition techniques, and the adaptation to the reward modeling setting, while technically sound, does not present a substantial leap in theoretical understanding. The paper could benefit from highlighting more clearly the novel aspects of the proof techniques and their specific relevance to the reward modeling problem.

### Questions
- A theoretical concern: is the inequality in line 960 only true when $\sum_{a}\hat{r}(s,a)-r^*(s,a)=0$? If so I cannot see why this is true.

Suggestions:
1. There are several links in the informal theorems that causes confusion to readers (e.g. links in theorem 2 to assumptions in the later part of the paper). It would be favorable if the assumptions can be described. Also Definition 1 should be ahead of Lemma 1 as it is required there.
2. The 2nd smallest eigenvalue should be proposed as an assumption in the paper to make theorem 4 comprehensible.

### Soundness
4

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
3

### Summary
The paper theoretically studies reward modeling using pairwise comparison
data and deep neural networks. They obtained a regret bound for deep neural network reward estimators which explicitly depends on network architectures such as width and depth. Moreover, they introduce a margin-type condition that measures the confidence of the human belief. This margin-type condition enables a sharper regret bound, which improves the regret bound from $\| r-r^*\|^{2/3}$ to  $\| r-r^*\|^2$ in the most extreme case.

### Strengths
1. The paper studies the theory of reward modeling, which is a very important question for LLMs.
2. The paper provides regret bound for neural network structures which is used in practice.
3. The paper introduced the margin condition which can quantify the confidence of the human preference which does not rely on the underlying reward model. The paper then obtained a sharper reward bound given the margin condition.

### Weaknesses
1. Although the theory looks solid, there is no/few surprise or new insights provided in this paper.
2. Arguably, the most important contribution in this paper is introducing the margin condition which can quantify the confidence of the human preference. However, an empirical verification of this assumption in real-world datasets is missing.

### Questions
Does example 1 or 2 satisfy assumption 1? If so, what is the corresponding alpha?

### Soundness
2

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
2

### Summary
This paper introduces a theoretical framework for understanding reward modeling in reinforcement learning (RL) based on pairwise comparisons and fully connected deep neural networks (DNNs) to estimate the reward function. When fine-tuning large language models, previous studies have used pairwise human feedback data to model rewards, enhancing sample efficiency and performance alignment with human preferences. The authors develop a non-asymptotic regret bound for DNN-based reward estimators, providing learning guarantees that explicitly account for neural network architecture parameters (i.e., width and depth). In Section 2, the authors develop learning guarantees under margin-type conditions, which ensure a significant margin in preference probabilities (i.e., the winning probability for an optimal action in comparisons) is well-separated from randomness. This condition enables sharper regret bounds. This result emphasizes the role of high-quality pairwise data in achieving efficient Reinforcement Learning from Human Feedback (RLHF) outcomes. In Section 3, the authors derive regret bounds that depend on DNN structure, demonstrating the role of network depth, width, and sample size in achieving high sample efficiency.

### Strengths
1. Theoretical results are “fine-grained,” as they consider specific neural network structures rather than relying on generalized assumptions about network properties.
2. Moreover, the paper addresses both stochastic and approximation error bounds, and provides guidance on achieving an optimal balance between these by designing the width and depth of DNNs. This is a nice attempt to bridge the theory to real-world model design.

### Weaknesses
1. The claimed extension (line 378-381) from DNNs to state-of-the-art architectures (such as BERT or GPT) is not fully convincing. While functionally similar, these architectures differ significantly in pipelines, loss design, training methods, and especially in their use of attention mechanisms and transformer layers, which are not addressed in your analysis. Consequently, I believe the gap between these theoretical results and the practical guidance needed for fine-tuning in RLHF remains significant. It would strengthen your claim if you could specifically address how these differences impact the applicability of your results or provide insights on adapting your analysis to accommodate these architectural and training nuances.

2. Even if we adopt the margin-type condition to data collection in practice, I am not sure how applicable it would be. Sometimes we encounter ambiguous or complex target data where a “clear human belief” is not always possible. Neither enforcing a clear preference nor ignoring the data point after identifying its difficulty is a good solution.

### Questions
1. Are there any toy experiments or future studies the authors can think of that would help validate the theoretical framework and findings? For example, could any experiments demonstrate the optimality of the claimed model depth and width, in terms of balancing stochastic and approximation errors? 

2. Related to the Weakness point 1, are there any versions of Theorem 4 that might extend beyond ReLU fully connected networks? Perhaps adaptations for attention mechanisms? Note that this possiblity is explicitly mentioned in line 378 - 381.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a new assumption on data, the margin-type condition, as a sufficient condition to achieve a sharp regret bound in reward modeling. The proposed assumption implies that experts exhibit a clear preference for the optimal action over others in most states, ensuring that the winning probability of the optimal action remains bounded away from 1/2. Under this assumption, the authors derive a tighter regret bound than existing results. Additionally, they establish regret bounds for reward modeling using deep neural networks, which explicitly depend on network structure and sample size.

### Strengths
- Formulating the intuitive idea that clear human feedback aids reward modeling into a margin-type condition was intriguing. As a result, the authors achieved a tighter regret bound for decision-making agents on data satisfying the margin-type condition. This outcome aligns with results in the contextual bandit literature, where margin conditions lead to tighter regret bounds [1, 2] .
-  Although the reviewer did not rigorously verify all proofs, the non-asymptotic excess risk bound for deep neural networks is also interesting. The authors provide theoretical guidance on the required network structure (width, depth) to attain a fast regret bound.

---
__Rerferences__

[1] Goldenshluger, Alexander, and Assaf Zeevi. "A linear response bandit problem." Stochastic Systems 3.1 (2013): 230-261.

[2] Bastani, Hamsa, and Mohsen Bayati. "Online decision making with high-dimensional covariates." Operations Research 68.1 (2020): 276-294.

### Weaknesses
 - The paper seems to lack a sufficient literature review on non-asymptotic generalization error bounds for deep neural networks. There is insufficient discussion comparing the presented bound with prior works (e.g., [3]), identifying the challenges encountered, and clarifying the technical novelties.
- The neural network bound presented requires computation of an exact minimizer for the empirical loss (Eq. 3), which may be difficult to obtain in practice.


### Questions
1. What issues arise in the margin condition when $\alpha = 0$?

2. The structure of the neural network used to guarantee the results in Theorem 3 depends on $\beta$ (the Hölder class parameter). How can the $\beta$ of the reward model being estimated be determined? Is it assumed to be prior knowledge?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work developed a regret bound (Thm.4) for RLHF when one approximates the true reward function with a deep neural network model (specifically, multi-layer perceptron) using MLE (Eq.(3)). It shows that having a margin condition (Assumption 1) can result in a faster rate (Thm.1 versus Cor 1) and these results could help readers identify better model architecture for reward modelling.

### Strengths
The paper provides a non-asymptotic regret bound through theoretical analysis, under assumptions on the preference margin (A1), finite true reward (A2) and some regularity conditions (A3).

### Weaknesses
1. The practicality of the result remains unclear. This work is mainly theoretical and there is no empirical evidence to show how useful the result would be. For example, L228 mentioned that “Our analysis provides implications for practitioners on how to choose the neural network parameters and construct high-quality comparison datasets to achieve effective reward modeling.” It would be much more convincing if the paper could provide some actual examples here. It is challenging to understand whether the required width and depth in Thm.4 are actually useful to design reward models and achieve better performance in practice. Specifically, the paper should discuss how the theoretical requirements for network width and depth translate into practical design choices. What are the trade-offs between model complexity and the regret bound? How can practitioners determine the optimal network architecture based on their specific dataset and computational resources?

2. The writing and presentation can be improved.

- It would be better to explain A1 using Examples 1 and 2. For example, what alpha and $c_g$ do we have in these two examples? Providing concrete values for these parameters in the context of the examples would significantly enhance the reader's understanding of the margin condition and its implications.

- L196 mentioned that this bound is “information-theoretically optimal”, but it remains unclear why. A more detailed explanation is needed to justify this claim. What specific aspects of the bound make it optimal? How does it compare to other potential bounds in terms of tightness and achievability?

- The overall structure of the paper is not easy to follow. Sec.2 looks more like an overlong overview of the whole paper, followed by Sec.3, which actually provides more technical details for the result in Sec.2. This is more common for long journal papers but does not work very well for a conference paper. It would be better to streamline the presentation by integrating the technical details into a more cohesive narrative. For instance, the key results and their implications could be presented in Sec. 2, while Sec. 3 could focus on the technical proofs and derivations.

Minor

- L107: $r$ depends on $\pi_r$? Isn’t this reversed?

- L292: output of $H^{(i)}$ should be of the linear output?

### Questions
Q1. How useful is the main theorem in terms of practical algorithm design and achieving good empirical performance?

Q2. Why Thm.1 is “information-theoretically optimal”?

### Soundness
3

### Presentation
2

### Contribution
2
