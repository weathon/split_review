# Select to Perfect: Imitating desired behavior from large multi-agent data

- Decision: Accept
- Scores: 5, 8, 8, 8, 6

## Abstract
AI agents are commonly trained with large datasets of demonstrations of human behavior.
However, not all behaviors are equally safe or desirable.
Desired characteristics for an AI agent can be expressed by assigning desirability scores, which we assume are not assigned to individual behaviors but to collective trajectories.
For example, in a dataset of vehicle interactions, these scores might relate to the number of incidents that occurred. 
We first assess the effect of each individual agent's behavior on the collective desirability score, e.g., assessing how likely an agent is to cause incidents.
This allows us to selectively imitate agents with a positive effect, e.g., only imitating agents that are unlikely to cause incidents. 
To enable this, we propose the concept of an agent's \textit{Exchange Value}, which quantifies an individual agent's contribution to the collective desirability score. 
The Exchange Value is the expected change in desirability score when substituting the agent for a randomly selected agent.
We propose additional methods for estimating Exchange Values from real-world datasets, enabling us to learn desired imitation policies that outperform relevant baselines. The project website can be found at {\small \url{https://tinyurl.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper "Who to Imitate: Imitating Desired Behavior from Diverse Multi-Agent Datasets" proposes a novel imitation learning framework. It enables AI agents to learn desirable behaviors from large, mixed-quality multi-agent datasets by using a metric called Exchange Value (EV) to evaluate and imitate only those agents contributing positively to collective outcomes. The technique involves EV-Clustering to handle incomplete data and an Exchange Value based Behavior Cloning (EV2BC) method for learning policies aligned with desired outcomes. The approach is shown to outperform baselines and has applications in aligning AI behavior with human values in complex environments.

### Strengths
Innovative Metric for Agent Evaluation: The introduction of Exchange Values (EVs) as a metric to compute individual agents' contributions to a collective value function is a significant contribution. EVs offer a method for identifying and imitating desirable behaviors within multi-agent systems, providing a novel way to approach imitation learning.

Effective Handling of Incomplete Data: The paper presents EV-Clustering, a method that estimates contributions from incomplete datasets. This addresses a common challenge in real-world scenarios where datasets are rarely comprehensive, enabling more accurate modeling of agent behavior.

Alignment with Desirable Outcomes: Through Exchange Value based Behavior Cloning (EV2BC), the paper proposes a mechanism to align the learning process with a Desired Value Function (DVF). This ensures that the learned policies reflect desirable outcomes, which is crucial for the practical application of AI systems trained on human data.

### Weaknesses
1.  **Quantification of Desirability**: The process of quantifying the desired value function (DVF) is a complex task and an active area of research. The paper's methods depend on the DVF to guide the imitation learning process, so any limitations in accurately defining this function could impact the effectiveness of the approach. Specifically, the paper does not address how the DVF is constructed, which is a critical component for the practical application of the method. The choice of DVF can significantly influence the learned policy, and without a clear methodology for its definition, the generalizability of the approach is questionable. For example, in a complex environment, a poorly defined DVF could lead to the imitation of unintended behaviors, even if the agents are contributing positively to the collective outcome according to the chosen DVF.

2.  **Assumption of Consistent Agent Behavior**: The framework assumes that individual agents behave similarly across multiple trajectories. This assumption may not always hold true in complex, dynamic environments where agent behavior can vary significantly based on context. This is a strong assumption that limits the applicability of the method to real-world scenarios where agents might adapt their behavior based on the specific situation or the actions of other agents. For instance, in a competitive setting, an agent's behavior might drastically change depending on the opponent's strategy, which would not be captured by the current framework.

3.  **Utilization of Undesired Behavior Data**: The paper points out that further research could explore how to utilize data on undesired behavior more effectively, such as developing policies that are explicitly constrained to avoid undesirable actions. The current approach focuses solely on imitating positive contributions, but it does not actively learn to avoid negative behaviors. This could lead to policies that, while achieving the desired outcome, might still exhibit undesirable actions that were not explicitly addressed during training. For example, an agent might learn to reach a goal but also exhibit aggressive or unsafe behaviors that were present in the training data but not explicitly penalized.

### Questions
1. Given that the quantification of what is considered desirable behavior is central to the proposed framework, can the authors provide additional insights into how the Desired Value Function (DVF) is defined and quantified across different environments and datasets?

2. The paper assumes consistent behavior from individual agents across multiple trajectories. Could the authors discuss the potential implications of this assumption in environments where agent behavior is more dynamic and context-dependent?

3. The paper suggests the potential for utilizing data on undesired behavior more effectively. Could the authors elaborate on possible approaches for leveraging this type of data to enhance the imitation learning process?

4. How does the framework adapt to different environments, and what are the limitations when applying the proposed EV-Clustering and EV2BC methods to datasets that significantly differ from the ones used in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
### Problem Statement
The paper tackles the challenge of extracting and imitating desirable behaviors from large multi-agent datasets, where desirability is quantified via collective trajectory scores. The problem arises as these scores reflect collective outcomes, making it difficult to ascertain individual agents' contributions, especially in real-world scenarios with fixed group sizes, incomplete datasets, and fully anonymized data.

### Main Contributions
The key contributions include
1. The introduction of "Exchange Values" (EVs) to quantify an individual agent's contribution to collective desirability.
2. The proposal of "EV-Clustering" to estimate these values from incomplete datasets
3. The development of "Exchange Value based Behavior Cloning" (EV2BC), a method that selectively imitates agents with high EVs estimated from anonymized data, thus aligning learned policies with desired characteristics, outperforming relevant baselines.

### Methodology
The authors propose "Exchange Values", a modification to Shapley value computation that compares the Desired Value Function values between agent groups of the same size, making it amenable to games that have group size constraints. Based on the Exchange Values, clustering of agents can be done by maximizing inter-cluster EV variance, which is particularly useful for fully-anonymized data. Behavior cloning (BC) can be then confined to only mimicking agents with high Exchange Values.

### Experiments
Two environments are used to evaluate the methods, namely the "Tragedy of Commons" and "Overcooked". Both synthesized and human generated data are used. The experiments show that the estimated EV values are meaningful and superior BC performance is attained with the guidance of EV for selecting trajectories to imitate.

### Strengths
### Originality and Significance
Evaluating the agent quality / contribution from desirability scores of collective trajectories is a very realistic and meaningful problem. The proposed method is well-motivated and elegantly extending the well-known Shapley Value, which is innovative.

### Quality
The problems the authors address are important and practical and the questions they try to answer are insightful.

### Writing
The mathematical explanations of complex concepts are precise and consistent. In addition, the authors provide insightful intuition to help readers understand.

### Weaknesses
### Limited Environments
Only two environments are studied, while there are many environments that can further highlight the real-world value of the proposed method, e.g. public traffic. The current environments, while useful for initial validation, do not fully capture the complexities of real-world multi-agent systems where agents might have diverse action spaces, partial observability, and long-term dependencies. For instance, the 'Tragedy of Commons' and 'Overcooked' environments are relatively simple in terms of agent interaction and environmental dynamics. A more complex environment, such as autonomous driving in a simulated city with diverse traffic patterns and pedestrian behaviors, would provide a more rigorous test of the method's applicability and scalability.

### Lack of more theoretical analysis of the properties of EV
Shapley Values are know to have good properties, e.g. symmetry, dummy (zero value for null players), additivity etc, which make it interpretable, appealing, and useful. It would be interesting to see analysis of Exchange Values with respect to these properties. Specifically, it is not clear how the Exchange Value behaves when agents are not fully interchangeable or when the value function is non-linear. A formal analysis of the Exchange Value's sensitivity to these factors would be beneficial. Furthermore, it would be useful to explore if the Exchange Value satisfies any other desirable properties beyond those of the Shapley value, or if it introduces any new limitations.

### Lack of interpretation of EV
More detailed analysis can be added to the main text with respect to how different EV values can be connected to various behavior patterns. In particular, I think the $\lambda$ values in both "Tragedy of Commons" and "Overcooked" can be linked to the estimated EVs to validate the method. The paper would benefit from a more in-depth analysis of how different EV values correlate with specific agent behaviors. For example, in the 'Overcooked' environment, it would be insightful to examine how agents with high EV values coordinate their actions compared to those with low EV values. Similarly, in the 'Tragedy of Commons' environment, a detailed analysis of how EV values relate to agents' resource consumption strategies would be valuable. This would provide a more intuitive understanding of what the EV values actually represent in terms of agent behavior.

### Lack of baseline
I understand that this is the first work tackling this specific problem setup, but I'm interested to see whether Shapley values could be similarly useful for guiding imitation learning in multi-agent dataset when the group size constraint is absent (which should be possible in many cases, e.g. the Tragedy of the Commons). It would be beneficial to compare the performance of the proposed method against a baseline that uses Shapley values directly, when applicable. This would help to isolate the impact of the proposed Exchange Value modification and demonstrate its advantages over existing methods. Furthermore, it would be useful to explore whether the proposed method could be combined with other imitation learning techniques to further improve performance.

### Writing
Although I in general enjoyed reading the paper, I still find many sentences throughout the article a bit repetitive and convoluted.

### Questions
- What does the $m$ in line 220 denote? Is it a fixed value or can it take multiple possible values (since $m \in M$). Why must $k \geq m$? Should $k$ change when $m$ takes a different value?
- Could authors further explain the definition of the "cluster-centroid agents $C \subseteq K$" in line 223?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a way to imitate the correct agents in a multi-agent setting, where correctness is measured by how an agent impacts the collective. This is termed the exchange value, and is formally presented as a way to quantify an agent’s contribution as the expected change in desirability when substituting the agent randomly. EVs require that different combination of agents are seen in the dataset. To counteract low-data regimes, EV-clustering is proposed. With this exchange values estimated for all agents in a dataset, the authors device EV2BC method learns behaviour cloning policies good agents only. Evaluation is performed on tragedy of commons and on the dataset collected from the Overcooked environment with diverse agent behaviours.

### Strengths
- The work is well motivated and seems to solve practical issues in Shapely Values. 

- The presentation of the work is clear enough, and relatively easy to follow. I thought Sections 3 and 4 to be quite well written.

- The results seem quite strong and convincing compared to other baseline methods. I thought Figure 4 (right) was quite convincing in showing the importance of clustering for the degenerate case.

### Weaknesses
 - How scalable would this method be to let's say a dataset of multi-agent driving scenes? It seems to me like scalability is an issue here, specifically due to clustering. The computational cost of calculating exchange values for each agent, especially with large datasets and numerous agents, is a concern. The clustering step, whether behavioral or EV-based, also adds to the computational burden, and the paper doesn't sufficiently address the practical limitations of these steps for very large-scale problems. This brings me to an important point, the weaknesses of the proposed approach should be addressed. 

- I'm still left confused by the differences between behavioural clustering and EV-clustering. I understand the differences in the approaches, but the ablation study seems to point to behavioural clustering being more stable in low-data regiments. I see that the ablation study says to look at section 5.1 to show why behavioural clustering is not sufficient by itself, but I do not see the supporting results. The paper needs to more clearly articulate the specific scenarios where EV-clustering is superior, and provide concrete examples where behavioral clustering fails. The current discussion lacks the necessary detail to fully justify the choice of EV-clustering as the primary method.

### Questions
- I'm a little confused about some experimental details. Specifically, the number of agents in the datasets, and the exact composition of the dataset is unclear. Can you clarify the composition of the $D^\text{adv}$? Are there really two different types of agents, but $n=100$ agents?

- In my opinion, the paper would be better organized by moving more results from the appendix into the main paper. One simple way of improvement is to move Figure 3 to the appendix and add the ablation study on the EV-clustering vs. Behavior clustering.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of learning aligned imitation policies from multi-agent datasets containing unaligned agents. The authors argue that existing methods for estimating demonstrator expertise in single-agent settings do not translate to the multi-agent setting due to the challenge of credit assignment. This paper proposes a method for learning aligned imitation policies that takes into account the collective value function of the agents. Empirical evidence shows that their proposed method outperforms relevant baselines.

### Strengths
Learning human-aligned policies from a mixed multi-agent dataset is an important area of research that is relevant to a diverse set of applications, including autonomous driving. The proposed method takes into account the collective value function of the agents and is designed to address the challenge of credit assignment in multi-agent settings. 

This work introduces a new metric called the Exchange Value (EV), which is used to estimate the individual contributions of agents to the collective value function. The paper provides empirical evidence that the proposed method outperforms relevant baselines, by showing that it can be applied to a social dilemma game and a cooperative task.

### Weaknesses
The proposed method assumes that the collective value function can be expressed as a sum of individual contributions. The authors should comment more on the class of problems that this is applicable to. 

Experiments evaluate the proposed method on a limited set of environments and tasks, and it is unclear how well the method would generalize to other domains and tasks.The authors motivated with a mixed driving dataset, and it would be useful to see how this method applies to driving benchmarks.

### Questions
Is EV a good measure if there exist complex/bipolar dynamics between agent behaviors? e.g. two agents work well if they are both in the team but horribly if only one present?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for imitating desired behavior from diverse multi-agent datasets. It introduces the concept of Exchange (EVs), which measures the individual contribution of an agent to a collective value function, and shows how they are related to Shapley Values. It further develops EV-clustering, a technique to estimate EVs from incomplete or anonymized datasets, by maximizing the variance of EVs across clusters of agents. It presents EV-based Behavior Cloning (EV2BC), an imitation learning method that only imitates the actions of agents with high EVs, and demonstrates its effectiveness in two domains: Tragedy of the Commons and Overcooked.

### Strengths
- It introduces the concept of Exchange Values, which measure the individual contribution of an agent to a collective value function, and shows how they are related to Shapley Values.
- It develops EV-Clustering, a technique to estimate Exchange Values from incomplete or anonymized datasets, by maximizing the variance of Exchange Values across clusters of agents.
- It presents EV based Behavior Cloning, an imitation learning method that only imitates the actions of agents with high Exchange Values, and demonstrates its effectiveness in two domains: Tragedy of the Commons and Overcooked.

### Weaknesses
 - For the results, it is necessary to provide some reference for a better understanding of the performance, e.g., reporting the results using the ground truth identification, or the results using the shapely value or other credit assignment methods. 
- The paper uses a limited number of environments and datasets to evaluate the proposed method and does not consider more complex or realistic scenarios that involve heterogeneous agents, partial observability, communication, or coordination, e.g., applying the exchange value in proactive multi-camera cooperation[1] or SMAC[2].

### Questions
- How do you deal with the uncertainty or variability in the EV estimates, especially when the data is incomplete or anonymized? How robust is your method to noise or outliers in the data?
- How do you justify the choice of the DVF for each domain? How do you ensure that the DVF is aligned with the desired behavior and does not have any unintended consequences or biases?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
