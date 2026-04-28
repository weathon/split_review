# SimUSER: When Language Models Pretend to Be Believable Users in Recommender Systems

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Recommender systems play a central role in numerous real-life applications, yet evaluating their performance remains a significant challenge due to the gap between offline metrics and online behaviors. We introduce SimUSER, an agent framework that serves as believable and cost-effective human proxies for the evaluation of recommender systems. Leveraging the inductive bias of foundation models, SimUSER emulates synthetic users by first identifying self-consistent personas from historical data, enriching user profiles with unique backgrounds and personalities. Then, central to this evaluation are users equipped with persona, memory, perception, and brain modules, engaging in interactions with the recommender system. Specifically, the memory module consists of an episodic memory to log interactions and preferences, and a knowledge-graph memory that captures relationships between users and items. The perception module enables visual-driven reasoning, while the brain module translates retrieved information into actionable plans. We demonstrate through ablation studies that the components of our agent architecture contribute to the believability of user behavior. Across a set of recommendation domains, SimUSER exhibits closer alignment with genuine humans than prior state-of-the-art, both at micro and macro levels. Additionally, we conduct insightful experiments to explore the effects of thumbnails on click rates, the exposure effect, and the impact of reviews on user engagement. The source code is released at https://github.com/SimUSER-paper/SimUSER.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a better agent framework for simulating users in recommender systems. The agent is framed using multiple modules like brains, and memories, and extracts persona from the user's historical interactions. Experiments are conducted on three public dataset to demonstrate the effectiveness of the proposed framework.

### Strengths
1. Timely study on areas including user simulation through generative agents, the gap between offline evaluations and real-world user experiences in recommender systems, and the use of simulators for recommender system evaluation.
2. The paper is well-structured, making it easy to follow and understand.
3. Experiments are conducted across three public datasets.
4. The authors perform significance tests to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Limited Insights: Using LLMs or generative agents to simulate users in recommender systems is not new. This paper’s primary contribution appears to be an improved agent that better leverages additional signals (e.g., historical interactions, images, KG). While the experimental results may indicate a more effective and believable agent, the paper offers limited new insights to the research community.
2. Overclaiming and Misalignment Between Motivation and Conclusions:
    1. The main motivation is the discrepancy between offline evaluation metrics and real-world dynamics in recommender systems. The authors claim that they introduce an agent framework that can act as a "believable and cost-effective human proxy" for recommender system evaluation. However, no experiments demonstrate that this agent framework effectively improves recommender system evaluation or provides a clear advantage over traditional offline metrics.
    2. The experiments in this paper are also conducted in an offline setting, where datasets are split into training, validation, and test sets to evaluate models. This is ironic for a paper that critiques offline evaluations but only tests its own method in offline conditions.
    3. Unrealistic Evaluation Setting: The authors split the dataset in an 8/1/1 ratio, seemingly without considering timestamps. Randomly splitting interactions ignores the distribution shift across different time periods, which is a major challenge in offline evaluations for recommender systems. As a result, the evaluation here does not adequately reflect temporal distribution shifts.
    4. Lack of Human-in-the-Loop Simulation: A significant issue with offline evaluations in recommender systems is the absence of a human-in-the-loop process. Recommender systems typically evolve as users interact with them, generating new data for system improvements. While simulators could potentially model this process, the experiments in this paper fail to reflect such dynamics.
3. Inadequate Ablation Study: The proposed agent framework integrates numerous heuristic components (e.g., Brain, Memory) and multiple signals (e.g., KG, images). However, the ablation study is insufficiently detailed, only comparing variants with and without persona and "zero or sim". This leaves the audience unclear on whether such a complex framework is necessary or if so many modules are essential for creating believable agents.
4. Dependence on Abundant User Interactions: Constructing the agent requires users to have a substantial history of interactions for persona generation and memory functions. This dependency may affect simulation performance based on the amount of historical interaction data. It would be better for the authors to discuss and analyze how varying levels of user interactions impact the simulation’s performance.
5. Clarity of Figures 1 and 3: Figures 1 and 3 are not vectorized, resulting in low clarity and readability.
6. Code Availability: Code is not available during the reviewing phase. Although the authors provided a link, it currently points to nothing.

### Questions
Please refer to "Weaknesses" for details.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes SimUSER, a framework that simulates the real user behaviors in recommender systems. SimUSER incorporates two new and crucial components: visual information and knowledge graph memory. The whole framework of SimUSER is similar to Agent4Rec [1] and the contribution is marginal. Moreover, the effectiveness of visual information is not verified and the concept of knowledge graph is wrongly used.

[1] Zhang, An, et al. "On generative agents in recommendation." *Proceedings of the 47th international ACM SIGIR conference on research and development in Information Retrieval*. 2024.

### Strengths
1. The experiments in this paper are abundant. Experiments in this paper include: user preference alignment, rating prediction, rating distribution, LLM evaluation, and recommendation strategy evaluation, etc. These experiments showcase the effectiveness of the proposed method.
2. This paper is easy to understand.

### Weaknesses
1. The contributions of this paper are marginal and incremental. The framework of SimUSER is similar to Agent4Rec [1] and the novelty lies in the incorporation of visual information and memory design, which is incremental.
2. The role of visual information is unknown. While the main contribution of this paper comes from the knowledge-graph memory and visual-driven reasoning, the ablation study does not explicitly verify the effectiveness. In Table 10, w/o perception module and w perception exhibit similar performance, and the implementation detail of w/o perception is unknown. More importantly, given the sample number of 1000 users, the improvements are impossible to be significant (i.e., p < 0.05). These experiment results are questionable.
3. Some concepts are wrongly used. For example, the knowledge graph in this paper is actually the widely used user-item interaction graph [2] in collaborative filtering, which is significantly different from KG [3]. Please carefully check this concept and refine the writing.
4. The link to the code is expired.

### Questions
Refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work concentrates on a very interesting and essential task: user simulation in recommendation. Compared with recent LLM-based recommendation user simulators such as Agent4Rec/RecAgent, the proposed SimUSER brings in the self-consistent personas from historical data, and designs both an episodic memory and a knowledge-graph memory for the memory module. Furthermore, they also introduce the visual information to the framework as multimodal recommenders for more comprehensive understandings. In experiments, the authors conduct extensive evaluations on different simulation tasks as well as analyses on various components in the framework, where the proposed model achieves the best performance compared to other LLM-based agent simulators.

### Strengths
1)	This work focuses on a challenging task and the proposed framework is sound and clear.
2)	The authors have conducted extensive experiments in Appendix to verify the effectiveness of different designs.
3)	The detailed prompts and other information are given for reproducibility.

### Weaknesses
1) This work proposes an overall framework for user simulation with lots of technics (which may require different types of related data). We can find that the proposed framework achieves consistently better results compared to Agent4Rec/RecAgent. However, it is unclear that whether the comparisons are fair enough. For example, how are the baselines trained? Whether the proposed framework uses additional information (e.g., at least the visual information)? The authors are suggested to give a table containing the detailed data used in each model. We know the data are essential for good performance in LLM-based methods.
2) The authors mainly compare with LLM-based simulators, while what are the results of other conventional simulators without LLMs? The authors could give a discussion on these possible models in Experiment. For example, it is not that challenging for conventional ID-based models to find top1 item among 10 randomly selected candidates.
3) For the user persona, will there be more informative features that should be included in the persona? For example, the classical user favorite tag/category/word that often exist in conventional user profiles.
4) It is noticed that the users have relatively long historical behaviors in the datasets. However, practical users usually do not have too many recorded behaviors (e.g., cold-start or few-shot users). The few-shot user scenarios should be noted and discussed/evaluated.
5) The overall framework involves lots of components. Although the authors have conducted extensive evaluations in Appendix, it is still unclear that which techniques are the dominating reason for such improvement. I suggest that the authors could give a brief analysis in the main content, focusing on the insight of which techniques are the most essential ones. For example, the “pickness” strategy in Section 3.2.1 is essential for rating tasks, and the user CF like strategy in Section 3.2.3 is also beneficial and have already been verified in classical recommendation methods. If the main improvements largely derive from such “tricky” points that ignored in previous baselines, or from additional information, the contribution of this work will be discounted.
6) The current simulation task is not challenging enough (9 randomly selected negative samples is not that hard in recommendation). It is suggested that the authors could evaluate on other recommendation datasets that contains real-world exposed but unclicked samples (i.e., explicit negative feedback, which is harder than random negative samples). Good simulation results on such settings are much more persuasive.

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper designs SimUser, a user simulation environment with LLM as its core to bridge the gap between offline evaluation metrics and online testing of recommender systems. SimUser conducts some experiments on item selection, rating prediction an LLM evaluation to validate the effectiveness of their framework.

### Strengths
1. The motivation of this work is good.
2. The method is easy to understand.

### Weaknesses
1. The abstract mentions "leveraging the inductive bias of foundation models," which is an intriguing idea. However, the paper does not provide enough detail on this in the main body. It would be helpful to explain what inductive bias refers to in the context of foundation models and how it can benefit recommendation systems. Offering more clarity on this point would enhance the overall strength of the paper.

2. To my knowledge, the primary contributions of SimUser are the introduction of several improved modules built upon existing frameworks: (1) a more refined user profiling mechanism, (2) a richer memory mechanism, and (3) enabling visual input. These modules are extensively discussed in the main body of the paper. However, the ablation study in the experimental section is overly simplified, and there are no corresponding experiments to verify the effectiveness of these newly introduced modules. This raises doubts about the validity of the contributions and leaves it unclear where the superior performance compared to the baseline originates from. Additionally, the ablation study is only conducted on the rating alignment experiment, with no exploration or validation of these components' effects on user preference alignment.

3. The paper lacks important details in certain areas. For example, while the authors emphasize the significance of visual information and present its integration as a key contribution of their method, they do not provide sufficient explanation on how the visual data is utilized or stored. A more detailed description of this process would improve the clarity and rigor of the paper.

4. In the main experiment (Table 1), as the ratio of positive to negative samples decreases, Precision unexpectedly increases across all three datasets, while Recall drops significantly. This outcome seems counterintuitive, and I would recommend the authors carefully verify the reliability of the experiments.

5. There are several points in the presentation of the paper that are somewhat confusing:
(1) There is an incorrect citation on line 57.
(2) The "Related Work" section could benefit from reorganization. The discussion on "simulating users in recommendation" should include content related to large models, rather than being separated from the section on "LLMs in Recommender Systems."
(3) In Equation (5), given that Px->y denotes a path from x to y, the subscript Px->x is unclear and may cause confusion.
(4) In Table 3, the third column of evaluation metrics contains some incorrectly bolded and underlined values.
(5) In Table 1, some data points are incorrectly bolded.

6. One potential weakness of this paper is the approach of summarizing user profiles, such as age and occupation, based on their interaction history. This method may risk introducing bias, labeling, and weakening the personalization.

7. In conclusion, I do not see a significant difference between SimUser and existing user simulation methods utilizing LLM on the recommender system. And the experiment section of this paper is incremental and far from solid.

### Questions
Please refer to Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2
