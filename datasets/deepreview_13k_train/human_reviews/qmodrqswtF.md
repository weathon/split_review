# Concept-driven Off Policy Evaluation

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Evaluating off-policy decisions using batch data poses significant challenges due to limited sample sizes leading to high variance. To improve Off-Policy Evaluation (OPE), we must identify and address the sources of this variance. Recent research on Concept Bottleneck Models (CBMs) shows that using human-explainable concepts can improve predictions and provide better understanding. We propose incorporating concepts into OPE to reduce variance. Our work introduces a family of concept-based OPE estimators, proving that they remain unbiased and reduce variance when concepts are known and predefined. Since real-world applications often lack predefined concepts, we further develop an end-to-end algorithm to learn interpretable, concise, and diverse parameterized concepts optimized for variance reduction. Our experiments with synthetic and real-world datasets show that both known and learned concept-based estimators significantly improve OPE performance. Crucially, we show that, unlike other OPE methods, concept-based estimators are easily interpretable and allow for targeted interventions on specific concepts, further enhancing the quality of these estimators.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The works addresses the high variance of methods to estimate policy value in sequential decision-making problems from offline data. It proposes to summarize the state information into interpretable concepts, e.g. using concept bottleneck models. Aggregating states into concepts better aligns supports of evaluation and batch data and reduce variance of importance sampling estimators. The work proves unbiasedness and lower variance of concept-based estimates compared to state-based estimates for common estimators. Experiments on two environments, grid world and health data from MIMIC, show good improvements both in settings of known and learnt concepts.

---
## After the rebuttal

I acknowledging reading the rebuttal and the other reviewers' comments.

I thank the authors for a detailed rebuttal. It addresses most of my comments. However, I agree with Reviewer JpPf that the revision seems major which includes changes to the definition and introduction of a new Assumption 5.2 (which seems like it should appear in the theoretical results but it does not). It warrants a closer look at the paper which is outside the scope of the rebuttal phase in my view.

That said, I like the work and think it presents an innovative approach to reducing variance of OPE. Hence, I keep the score of 6 but given the need to look closely at the substantial updates I do not feel confident to recommend acceptance strongly.

### Strengths
Main strengths are
- Transforming states to concepts is an interesting and refreshing idea among the many variance reduction methods. It may improve applicability of methods to safety-critical domains via improved interpretability and ability to intervene to correct estimates of policy value.
- Proposal to use state abstractions was given by Pavse & Hanna 2022a, but the use of concept bottleneck models is novel to the best of my knowledge. Authors show that concepts are more intervenable and allows a human to correct the estimates.
- Evaluation is thoroughly done and clearly visualized. Metrics such as bias, variance, MSE, and ESS are reported which are good measures in context of OPEs.

### Weaknesses
Main weaknesses in my view are
- Presentation could be improved at places by providing more details on how concepts can help improve OPE estimation, definitions of concept-equivalent policies, and interventions on concepts. Specifically, the paper lacks a clear explanation of how the concept-equivalent policy is constructed and how it relates to the original policy. The definition in equation (1) is not intuitive, and it's unclear how the inverse is computed, especially in continuous state spaces. The intervention section is also vague, lacking a clear definition of 'human criteria' and 'qualitative intervention'.
- Comparisons to previous work on state abstractions by Pavse & Hanna 2022a, either in experiments or in terms of technical and conceptual contributions, should be clearly made. The paper does not sufficiently highlight the differences between the proposed method and existing state abstraction techniques, particularly regarding the theoretical guarantees and practical advantages of using concept bottleneck models. A more detailed comparison, both theoretically and empirically, is needed to justify the novelty of the approach.
- Some implementation details like the OPE cost in optimization and computing concept-equivalent policy for a given policy can be described. The paper lacks clarity on how the OPE cost is defined and used in the optimization process. It's also unclear how the concept-equivalent policy is obtained in practice, especially when dealing with infinite state spaces. The optimization process for learning the concept policies needs more detail, including the specific loss functions used and how they are balanced.

Important questions remain unanswered like how does imperfect concept discovery or inability to get a concept-equivalent policy affect the final estimates.

Evaluation against state abstractions e.g. method by Pavse & Hanna 2022a seemed necessary to show that dimensionality reduction by concept bottlenecks has unique advantages, perhaps in intervention evaluations.

Similarly, does model-based methods equipped with the same domain knowledge as concept bottleneck models, say the same parameterization of feature space, perform worse?

Where does the improvement in estimation metrics come from? Was it because of collapsing states with skewed propensity scores that caused high variance? A plot of propensity scores in state and concept feature spaces might be helpful.

### Questions
Questions for authors:

## On presentation,

The idea behind defining a policy as in eq (1) was not clear to me. It seems like a change of measure but there could have been other ways to define a concept-equivalent policy and a clear definition is missing. Does it take the same actions as the original policy would or the same value? 

Section 7 on intervention is hard to follow as the goal of the section, and terms like human criteria and qualitative intervention are not clearly described.

What are the key differences from the theoretical results in Pavse & Hanna 2022a when adapted to concept-based representation?


## On implementation, 

How is the concept-equivalent policy obtained, particularly how is the inverse in eq (1) computed for infinite state space as in experiments? Relatedly, meaning of aligning a policy in line 345 was unclear. 

Describe how the cost for OPE-metric is defined in line 12 of Algorithm 1. Does some data have to held out to compute the cost? 

## On approach,

How is the concept-equivalent policy supposed to help evaluation - does it trade-off variance with bias or reduce variance by removing reward-irrelevant state information? What are pros and cons of this design choice?

I was expecting much more discussion in Sec 4.1 on the goals and consequences of changing representation to concepts.

Important questions remain unanswered like how does imperfect concept discovery or inability to get a concept-equivalent policy affect the final estimates.

## On evaluation,

Evaluation against state abstractions e.g. method by Pavse & Hanna 2022a seemed necessary to show that dimensionality reduction by concept bottlenecks has unique advantages, perhaps in intervention evaluations.

Similarly, does model-based methods equipped with the same domain knowledge as concept bottleneck models, say the same parameterization of feature space, perform worse?

Where does the improvement in estimation metrics come from? Was it because of collapsing states with skewed propensity scores that caused high variance? A plot of propensity scores in state and concept feature spaces might be helpful.

---

Minor comments (responses are not sought for the below):

Assumption 5.1 is explained backwards in text.

I would suggest to discuss balancing scores (https://www.jstor.org/stable/2288398), which like propensity scores are enough to get an unbiased value estimate when used to reweight rewards. Propensity scores are coarsest balancing score, however, it might be that concept-equivalent policies give another choice of balancing score.

Provide a reference for the meaning of Symbolic Representation in line 412.

Consider discussing interpretation of the four learnt concepts in MIMIC.

What is the reward in MIMIC? The term viral load was not clear and seems to refer to vitals and labs.

Authors should consider expanding the baselines and possibly the environments.

Correct typos like in line 481 cuase.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors consider the problem of off-policy evaluation in offline/batched reinforcement learning. The goal is to be able to determine the effectiveness of a policy different from the one that collected/generated the data. The paper proposes a concept-based approach. A concept is a higher-level feature of the states/actions etc. that is (ideally) more interpretable and can capture key aspects of the problem such as transition points, changing dynamics and so on. The paper constructs a sampling importance method using concepts -- either learned concepts or concepts defined by experts. They prove various properties of the estimators and compare against traditional importance sampling methods. Finally, they run experiments on the Windy GridWorld problem and the MIMIC dataset, both when having human-designed concepts and when learning concepts.

### Strengths
The paper proposes a useful idea in improving the interpretability of dynamics in RL which can give insights into the problem. Section 7 was very useful in illustrating this. The computational results overall are promising and show nice improvements over existing methods.

### Weaknesses
Theory: Additional discussion would be helpful for the theoretical results to explain the significance of these results. What kind of insights can we gain from the theory? Anything we can apply to improve/guide practical application and experimental results?

Additionally, how does the choice on the number of concepts affect the ability of evaluate policies? More concepts may be helpful in better partitioning state  space, but overall the process becomes less interpretable if we have too many concepts.

Experiments: More detail would be appreciated on the tasks. Please explain what the WindyGridworld and MIMIC problems are, discussion on the state/action space etc. How are the concepts you propose in section 5.2 related to these? How do you assume the data is generated? For example, at least cite what the PPO algorithm is in section 5.2.

It would be nice to have more synthetic experiments, besides only WindyGridworld, so we can observe bias, variance, mean squared error and the effective sample size (ESS) on more problems (since MIMIC is not, we can only compute variance -- it is still important to observe this variance metric on real-world data, so please do keep it).

Algorithm: The algorithm introduced (Algorithm 1) seems to be a fairly significant contribution of the paper. However, it is given very little attention, and as a result I found it difficult to follow. For example, from the discussion in section 6.1 I do not see how the term $c_t^i = w \cdot f(s_t)$ is connected to the algorithm. Please provide a clearer description of the algorithm.

### Questions
Please see my questions in the weaknesses section above. In addition,

1. How is learning concepts different from learning representations? For example the work in [1].

2. Overall, can you give more details and intuition behind definitions etc. so we can better follow. 

a) For example, in equation (1) $\phi^{-1}$ is never defined. Also initially $\phi$ is defined as a function of $a, r, s$ but $\phi^{-1}$ only acts on $c_t$. You later say that concepts are only a function of $c_t$.

b) Moreover, what is the steady-state distribution $d_{\pi}$? Steady-state of what distribution?	

3. Can you provide more background on importance sampling, which seems to be the main approach you extend? It would be useful to have in order to better gauge the contribution of your work. 



[1] Representation Matters: Offline Pretraining for Sequential Decision Making, Mengjiao Yang, Ofir Nachum ICML 2021

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The goal of off-policy evaluation is to estimate the performance of an evaluation policy using data that is collected under a different behavior policy. Standard approaches to OPE can suffer from high variance. This work proposes a family of concept-based OPE estimators that reduce variance relative to standard importance-weighting estimators. They also develop an end-to-end algorithm for learning parametrized concepts, which are interpretable and can be used for off policy evaluation.

### Strengths
The authors study an important problem – it is well-known that off-policy evaluation estimators can suffer from high variance, so the idea of using concepts as a form of dimensionality reduction of the state-action space can yield empirical benefits.

### Weaknesses
The paper has some clarity / conceptual issues: The proposal of this paper is to use a concept bottleneck model to learn interpretable concepts and derive importance-weighting estimators based on these concepts. The idea of simplifying the state-action space using concepts is a promising one, but there are many technical details that are not clear from the paper.

- The authors posit that a concept at time-step $t$ can be obtained from a function $\phi$ that takes the entire trajectory from time-step $0$ to time-step $t$ as input, i.e. one can pass $(s_{t}, a_{0:t-1}, r_{0:t-1}, s_{0:t-1})$ to $\phi$. However, later in the paragraph the authors write that “In this work, we consider concepts $c_{t}$ to be just functions of current state $s_{t}$, and thus…” This is a bit confusing because $\phi$ is initially introduced as taking entire trajectories as input. Furthermore, if concepts $c_{t}$ are just functions of the current state $s_{t}$, I wonder if it would be reasonable to interpret concepts as a way of allowing us to do dimensionality reduction on the states? It's unclear how this concept representation differs from standard state abstractions, and the paper doesn't sufficiently address this point.
- Suppose that we have a standard policy $\pi(a |s)$ and we compute a concept policy $\pi^{c}(a|c)$. The policy value function $V_{\pi}(s)$ is a function of state $s$, it is not clear to me from the paper how we can compute the analogous quantity for $V_{\pi^{c}}(s)$ or if such a quantity is even well-defined. The paper does not clearly define how the concept-based policy relates to the original policy in terms of value functions, making it difficult to assess the validity of the proposed approach. Specifically, it is not clear if $V_{\pi^c}(s)$ is even a meaningful quantity, and if so, how it would be computed or interpreted.
- Assumption 5.1 seems to require that any action-state pair that is possible under the evaluation policy must also be possible under the behavior policy. However, the written interpretation of the assumption is the  opposite.

### Questions
How can $\phi$ adapt to input trajectories of different length? Furthermore, in Equation (1), the authors appear to be able to invert the map $\phi$. How is this possible?

### Soundness
2

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
2

### Summary
The paper introduces concept-driven off-policy evaluation (OPE). This approach mirrors the structure of concept bottleneck models, where the prediction task is split into two stages: first, predicting a set of human-interpretable concepts, and then using these concepts to complete the prediction task. The paper applies this concept-driven approach to OPE. Specifically, it maps trajectories to a concept space, derives a policy for each concept value, and uses the concept equivalent behavior and evaluation policies to calculate the importance sampling ratio. When concepts are not known in advance, the paper presents an algorithm to learn them. The evaluation is performed for specific policies on both synthetic and real datasets.

### Strengths
Importance smapling methods for OPE can suffer from high variance and using a concept bottelenck can reduce the variance. The concepts can also improve the interpretability of the evaluation task. The proposed idea is novel to the best of my knowledge.

### Weaknesses
I found this paper challenging to read due to numerous typos and mathematical inconsistencies. For example, in Section 4.1, $\phi$ is first introduced as a function of state, action, reward, and next state. Later, it’s interpreted as a function of the full trajectory. However, in Equation 1, $\phi^{-1}$ appears to return a state, creating confusion. Additionally, there’s a typo in the definition of w in Equation 1.
Theoretical results are presented with virtually no explanation. In both Sections 5.1 and 6.2, four theorems are listed in row without any discussion, making it difficult to follow or interpret the results and understand their limitations (for instance, Theorem 5.2 suggests that concept-driven evaluation is biased, which doesn’t align with the evaluations). It’s generally known that IS estimators can exhibit high variance, and various methods have been proposed to reduce this variance at the cost of extra bias. This paper’s proposed method falls into this category, though this is not clearly acknowledged.

There are also choices in the paper that lack justification. For instance, it uses an approximate nearest-neighbor policy with the MIMIC-III dataset. Having worked extensively with this dataset and reviewed recent studies on it across different tasks, I am not aware of any example where such a policy is applied. Additionally, this experiment employs a concept space of size $10^{15}$, which does not seem to offer interpretability and appears far removed from the motivating example in Figure 1.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
