# Quantifying the Sensitivity of Inverse Reinforcement Learning to Misspecification

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Inverse reinforcement learning (IRL) aims to infer an agent's \emph{preferences} (represented as a reward function $R$) from their \emph{behaviour} (represented as a policy $\pi$). To do this, we need a \emph{behavioural model} of how $\pi$ relates to $R$. In the current literature, the most common behavioural models are \emph{optimality}, \emph{Boltzmann-rationality}, and \emph{causal entropy maximisation}. However, the true relationship between a human's preferences and their behaviour is much more complex than any of these behavioural models. This means that the behavioural models are \emph{misspecified}, which raises the concern that they may lead to systematic errors if applied to real data. In this paper, we analyse how sensitive the IRL problem is to misspecification of the behavioural model. 
Specifically, we provide necessary and sufficient conditions that completely characterise how the observed data may differ from the assumed behavioural model without incurring an error above a given threshold. In addition to this, we also characterise the conditions under which a behavioural model is robust to small perturbations of the observed policy, and we analyse how robust many behavioural models are to misspecification of their parameter values (such as e.g.\ the discount rate).
Our analysis suggests that the IRL problem is highly sensitive to misspecification, in the sense that very mild misspecification can lead to very large errors in the inferred reward function.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors investigate the question of robustness of an IRL algorithm against reward misspecification, i.e. if the expert follows a behavioural model (which computes $\pi$ from $r$) and an IRL algorithm assumes another behavioural model, when will the inferred reward be close to the true reward? To understand this, the authors use the STARC metric [1] to define closeness between two given rewards. The authors then identify necessary & sufficient conditions for robustness to hold when misspecification exists, and further discuss parameter misspecification, continuity of the behavioural model, etc. Overall, the paper is well written and provides useful insights fundamental to IRL, but is still less clear how these insights translate to practical rules for IRL practitioners.

### Strengths
Lots of good explanations, especially in the appendix

### Weaknesses
Lots of good explanations, especially in the appendix

Understanding the results in this paper takes multiple readings, and it is difficult to follow in a few places. This is due to choices that seem arbitrary, but are well explained later. For example, the choice of $sin(2arcsin(\epsilon/2))$ in Proposition 3 seems arbitrary, but is justified in the Appendix. Overall, the writing is good, but can be improved by providing more intuition about the theorems/propositions in the main text, possibly through more examples, rather than relegating all explanations to the appendix.



### Questions
1. What if we have two IRL algorithms that differ in implementation but assume the same underlying behavioural model? Will this affect the results?
2. Does the IRL reward parameterization affect the results?
3. Are there more ways in which reward functions can be different but yield the same optimal policy? (except for potential shaping, S' redistribution, positive linear scaling)
4. Shouldn't a reward change of the type $R'=R+b$ where $b$ is a constant also lead to the same optimal policy? Is this discussed somewhere (may have missed it)?
5. Can these results be used to quantify unidentifiability better? For example, unidentifiabilty in RL/IRL states that there may exist multiple rewards that yield the same policy, so given a policy, an IRL algorithm can output multiple valid reward functions. But what is the size of a class of rewards that are equivalent in some way? What is this size affected by?

**Typos**
- Page 2, Paragraph 2, Line 6: "misspecifiaction" => "misspecification"
- Section 3 title: "rubustness" => "robustness"

**References**
1. Starc: A general framework for quantifying differences between reward functions, Skalse et al. (2023)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors analyze the sensitivity of inverse reinforcement learning, i.e., learning the reward model to misspecification of the behavior model adopted by the agent, i.e., the objective function that the agent is trying to optimize. The authors analyse robustness of IRL to misspecification in the behavior model by first quantifying the impact of misspecification of behavior model in terms of a pseudometric defined on the space of reward functions. Their first theorem states necessary and sufficient conditions for a behavior model to be $\epsilon$ robust to a defined family of behavior models. The authors then state the necessary and sufficient conditions under which a behavioral model is robust to perturbations as their second theorem. Their final theorems state conditions under which behavioral models with perturbations to their parameters are not robust in terms of learning a reward function that preserves preferences.

### Strengths
The authors present interesting propositions that will help characterise the robustness of IRL algorithms towards learning preferences.

### Weaknesses
1. I am not sure about the extent of novelty in this contribution. The problem of robustness of IRL to behavior model misspecification has been studied in the past as mentioned in the literature survey in the paper. The new pseudometric used by the authors has also been introduced in an earlier paper cited by the authors. If this is correct, and the analysis is the main novel contribution, then I would expect a more detailed comparison of the analysis with the other works in literature.
2. The main contribution of this paper is its theoretical results. The authors hhave stated the theorems, propositions and corollaries in the main paper without any proofs or even proof sketches. Furthermore, there are no numerical experiments conducted to demonstrate the impact of the theoretical findings.

### Questions
1. Can't the difference in observed versus predicted behavior of a human assuming a particular behavior model be explained by incorrect or incomplete optimization rather than incorrectness of the behavior model?
2. Doesn't the IRL method also need access to the environment to collect samples?
3. For a given dataset, can't two different behavioral models yield the same reward function? If so, isn't accuracy of reward prediction an insufficient criterion for estimating the validity of the behavioral model? In this paper, do the authors wish to learn a true reward function, albeit woith an incorrect behavior model, or do they wish to establish correctness of the behavior model as well?
4. Are the brackets correctly places in the definition of S' redistribution in the third paragraph of Sec 1.2? If so, I do not understand this definition. Can the authors please clarify?
5. In Point 3 of Defintion 1, should $R_1$ and $R_2$ be necessarily different? If so, why? What happens in the case when $f = g$?
6. Is the orderting of policies mentioned in Proposition 1 a partial ordering?
7. I did not understand the 2-norm of the first term in the equation written in Proposition 3. Can the authors please explain this?
8. What happens to IRL robustness when the true behavior model is Cumulative Prospect Theory and the assumed one is Boltzmann-rationality?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Inverse reinforcement learning aims to infer a reward function $R$ from a policy $\pi$. To achieve this, IRL needs to make an assumption on the underlying behavior model, which maps reward functions to policies and characterizes the relation between $R$ and $\pi$. However, the behavior model could be misspecified and differs from the true one. This paper is to contribute towards a theoretical understanding on the robustness of IRL to misspecification. First, this paper characterizes the sufficient and necessary condition to ensure that IRL is robust to a general misspecification. Then this paper considers a specific type of misspecification: the behavior model is a perturbation of the true one, and provides the corresponding sufficient and necessary condition. Finally, this paper considers another type of misspecification on the parameters of behavior models and provides a negative result that IRL is often not robust to such misspecification.

### Strengths
1. This paper indeed makes notable progress toward theoretical understandings of misspecification in IRL. This paper conducts a systematic analysis and provides complete answers to this problem. The main results are insightful and clean and can help deepen the understanding of IRL.
2. The paper is well-written and easy to follow. Although this paper is a theoretical paper, it provides many intuitive examples and explanations that can help readers easily understand the main results.

### Weaknesses
1. In this paper, the authors consider a general IRL procedure that outputs an arbitrary reward function $R$ from the class $\tilde{\mathcal{R}} = \{R_1: f (R_1) = \pi = g(R_2) \}$. However, in practice, we often run a specific IRL algorithm such as MaxEnt IRL [Ziebart, 2010], which performs reward selection and outputs the chosen reward. Therefore, it could be more meaningful to analyze the robustness of a specific IRL algorithm to misspecification. The analysis would benefit from considering how the specific inductive biases of algorithms like MaxEnt IRL affect the robustness results, particularly in cases where the behavior model is misspecified. The current analysis, while general, might not fully capture the nuances of practical IRL implementations.


### Questions
Typos:
1. In Proposition 3, $\\| R, t_n (R) \\|_2$ should be $\\| R - t_n (R) \\|_2$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a theoretical framework aimed at investigating the discrepancy or 'misspecification' between the assumed and actual behavioural models during the Inverse Reinforcement Learning (IRL) process. Moreover, it explores how this misspecification impacts the reward obtained through the IRL algorithm.

This research primarily concentrates on the most prevalent behavioural models, namely optimality, Boltzmann-rationality, and causal entropy maximisation.

In the initial segment of the theoretical framework, it introduces a formal definition of 'misspecification robustness' and the 'STARC-metric'. This metric is used to measure the differences between a reward function that remains invariant to potential shaping, redistribution, and possibly rescaling. Leveraging these definitions, the paper outlines the necessary and sufficient conditions for identifying the degree of robustness against misspecification between two behavioural models.

The second segment of the theoretical framework presumes a distance between the returns of behavioural models (policies). It examines the capability of the IRL algorithm to learn precise rewards under two conditions: 1) when the behavioural models are misspecified, and 2) when there is a gap in their returns. The findings suggest that no continuous behavioural model can maintain robustness against these two levels of misspecification.

In the final part of the theoretical framework, the paper delves into the scenarios where the parameters of behavioural models are misspecified. The research primarily focuses on the discount parameter, demonstrating that behavioural models are, in principle, highly sensitive to even minor misspecifications of two of their core parameters.

### Strengths
1. The issue of misspecification between the assumed and actual behavioural models in IRL reresents a significant and underexplored challenge, to the best of the reviewer's knowledge.

2. The paper is logically structured and easily navigable, with definitions clearly articulated and supplemented by explanations. These help the reader to intuitively comprehend the main theses and their implications in terms of characterizing the robustness of misspecification in the IRL problem.

3. The theoretical framework is presented with clarity, and the main claims appear generally sound.

### Weaknesses
1. The inclusion of concrete examples of the transformation would be beneficial. Currently, it is challenging to image the types of transformations that would satisfy Proposition 3, and more importantly, how to interpret these transformations requires clarification. Specifically, the paper should provide a more intuitive explanation of the transformations, perhaps by illustrating how they affect the ordering of actions within a given state. The current geometric description in the proof of Proposition 3, while mathematically rigorous, lacks the necessary intuitive grounding for a broader audience. It would be helpful to see examples that show how these transformations can shift the relative desirability of actions and how such shifts impact the learned reward function in practice.

2. As per the reviewer's understanding, an MCE (Maximum Causal Entropy) policy corresponds to a Boltzmann-rational policy. Specifically, the optimal policy representation in soft-Q learning complies with Boltzmann-rationality. This point may warrant further verification. The distinction between MCE and Boltzmann-rational policies needs to be more clearly articulated, especially given their close relationship in the context of soft-Q learning. The paper should explicitly highlight the differences in their formulations, such as the use of soft Q-functions in MCE versus the optimal Q-function in Boltzmann rationality, and explain how these differences lead to distinct behaviors and sensitivities to misspecification. A more thorough discussion of these nuances is essential for the paper's theoretical claims.

3. It would be beneficial to present some empirical results, which could illuminate the consequences of failing to achieve robustness under the misspecification of behavioural models. While the theoretical framework is well-developed, the practical implications of the negative results (Theorems 3, 4, and 5) remain unclear without empirical validation. The paper should demonstrate through experiments how misspecifications in behavioral models impact the convergence and accuracy of IRL algorithms under different conditions. This would involve selecting appropriate environments, generating demonstration data with misspecified models, and observing the performance of IRL algorithms. Such experiments would provide crucial insights into the practical relevance of the theoretical findings.

### Questions
1. In proposition 3, what's the meaning of $\|R,t_n(R)\|_2$? Should it be |R-t_n(R)\|_2? 

2. According to the results of this paper, all the commonly applied behavior models are not $\epsilon/\delta$-separating, are there any behavior model is $\epsilon/\delta$, maybe under the mild relaxation on the distance under the reward and policy space?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
