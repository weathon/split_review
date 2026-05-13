# Multi-Agent Collaborative Data Selection for Efficient Language Model Pretraining

- Decision: Reject
- Scores: 5, 8, 6, 3

## Abstract
Efficient data selection is crucial to accelerate the pretraining of large language models (LLMs). While various methods have been proposed to enhance data efficiency, limited research has addressed the \textit{inherent conflicts} between these approaches to achieve optimal data selection for LLM pretraining. To tackle this problem, we propose a novel \textit{multi-agent collaborative data selection} mechanism. In this framework, each data selection method serves as an independent agent, and an agent console is designed to dynamically integrate the information from all agents throughout the training process. We conduct extensive empirical studies to evaluate our multi-agent framework. The experimental results demonstrate that our approach significantly improves data efficiency, accelerates convergence in LLM training, and achieves an average performance gain up to $10.5\%$ across multiple language model benchmarks compared to the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to a mechanism to select data into the training process based on 3 main measure (quality, domain and topic) of the data. The 3 measures are adjusted dynamically and aggregating together to determine whether data point can be selected during the training process. A RL paradigm is employed to realize the proposal. Good performance is demonstrated in the provided experiments.

### Strengths
• A good analysis of how different aspects influence the performance of LLM training.
• The experiment seems to demonstrate this kind of scoring of data points can help to improve the data deficiency and performance.

### Weaknesses
• The connection to agent or multi-agent paradigm seems weak to me. It might not be necessary to formulate the problem and the solution via "agent" concept. A direct stochastic optimization formulation might provide  more direct description and help audience better mastering what is the proposal.

• The definition of the loss function l in line 161 is unclear, and the explanation of the reward function is insufficient. It's not clear how the reward function relates to or differs from the standard LLM auto-regression loss or other common loss functions.

• In Algorithm 1, it is not clear whether the sampling distribution of the data changes from iteration to iteration (line 3). This lack of clarity makes it difficult to understand the dynamics of the data selection process.

• In line 275, a 373M parameter model is used in the ablation study. This is a relatively small model, and the conclusions drawn from it may not generalize to larger LLMs with billions of parameters. The study needs further justification to ensure the findings are applicable to the intended scale of models.

### Questions
1. Is it possible to not employ the agent or multi-agent metaphor to formulate the proposal? What is the truth power of the proposal? Is it a compossible and multi-step paradigm of stochastic optimization  based on 3 hand-crafted dimensions? 
2. Ine line 161, what is the loss function l? Also please explain more regarding the definition of the reward function. How is it different o related to the loss function of LLM auto-regression loss or other kinds of losses (if any other).
3. In Algorithm 1, please clarify whether the sampling distribution of the data are different from iteration to iteration (line 3). 
4. In line 275, 373M model is used in ablation study. It is pretty small a model. The conclusions drawn from it might not be transferrable to LLMs of billions of parameters. Please justify the study.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel multi-agent collaborative data selection mechanism aimed at enhancing data efficiency during the pretraining of large language models (LLMs). Recognizing that existing data selection methods often operate independently and may conflict with one another, the authors propose a framework where each data selection method functions as an independent agent. An agent console dynamically integrates the information from all agents throughout the training process. The agents adjust their weights based on reward signals derived from the model's performance on reference tasks. The framework is designed to flexibly and robustly combine various data selection strategies, such as data quality scoring, topic diversity, and domain information. Extensive experiments demonstrate that this multi-agent approach significantly accelerates convergence in LLM training and achieves an average performance gain of up to 10.5% across multiple benchmarks compared to state-of-the-art methods.

### Strengths
1. Introducing a multi-agent framework to collaboratively select pretraining data is a novel idea that addresses inherent conflicts among existing methods.
2. The empirical evaluation is extensive, comparing the proposed method against a wide range of baselines and demonstrating significant improvements.
3. The paper clearly articulates the motivation, methodology, and findings, making it accessible to readers.
4. Improving data efficiency in LLM pretraining is a critical challenge, and the proposed method offers a practical solution with demonstrable benefits.

### Weaknesses
1. While the experiments show promising results on models up to 1.3 billion parameters, it is unclear how the approach scales to larger models commonly used in practice. Specifically, the computational demands of the multi-agent system might become a bottleneck when dealing with models that have tens or hundreds of billions of parameters, and the paper lacks a detailed analysis of this aspect. Furthermore, the memory requirements for storing and updating agent states could also pose challenges at larger scales.
2. The choice of agents (quality, domain, topic) seems somewhat ad-hoc. A more rigorous justification for these specific agents is needed, and a discussion on how to generalize the selection of agents or include other data selection criteria would strengthen the paper. For instance, the paper does not explore agents based on data recency or difficulty, which could be relevant. The lack of a systematic approach to agent selection makes it difficult to assess the robustness of the framework.
3. While ablation studies are included, more detailed analysis on how each agent contributes to different types of tasks could provide deeper insights. For example, it would be beneficial to understand if certain agents are more effective for specific downstream tasks or if there are any interactions between agents that lead to synergistic or antagonistic effects. The current analysis does not provide a fine-grained understanding of agent-task relationships.

### Questions
1. How does the proposed framework perform when scaling up to larger models (e.g., 10B+ parameters) and datasets (e.g., trillions of tokens)?
2. Can you provide a more detailed analysis of the computational overhead introduced by the multi-agent system compared to baseline methods? 
3. What guidelines can be provided for selecting or designing agents for other data selection criteria? Is the framework flexible enough to incorporate new agents easily? How sensitive is the method to the choice of number and types of agents?
4. How sensitive is the performance to the choice of reference tasks used for calculating rewards in the influence functions?
5. Can you elaborate on how the dynamic adjustment of agent weights impacts the learning process over time? Are there scenarios where this adjustment could lead to suboptimal data selection?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a multi-agent approach to strategically select data for pretraining LLMs. The paper motivates the need for a multi-agent design by sharing a case study on the SlimPajama pretraining dataset. They illustrate that the most common data set considerations (and their corresponding metrics), including data quality, topic diversity, data impact, and data domain are not straightforward to jointly optimize. Therefore, they propose a multi-agent system, where each data selection method/metric is represented as an agent. Through this multi-agent approach, these methods can be mixed via multi-agent collaboration, forming a highly adaptive approach in data selection. They show that their multi-agent approach is effective: the data curated by their method leads to faster convergence in training and improved benchmark performance.

### Strengths
-Mixing data quality and data selection techniques is a challenging problem: they show in their case study that typical data curation techniques can conflict and naively combining them is not sufficient.

-Unlike many off-the-shelf multi-agent systems, they are proposing optimization of each agent’s weights (stored in memory) based on reward signals from the model undergoing pretraining.

-Results show that their multi-agent data selection produces the best performance. Ablations show the three agents in collaboration outperform all other permutations of the agents (with and without collaboration) and strongly outperform the setting with no agents at all. 

Originality:
I am not aware of another multi-agent approach for data selection in pretraining - so this appears to be a novel application of multi-agent systems.

Quality:
All key components covered - clear literature review, motivation, experiment design, results. It would have been better if they made their contribution differentiations clear in the literature review - for ex, confirming if they are indeed the first multi-agent approach for data selection. And if not, how are they different.

Clarity: 
The paper was generally well written and easy to read.

Significance:
Pretraining is the most critical and expensive operation for LLMs. To make the best use of your pretraining, optimizing the data is key.

### Weaknesses
 -Figures can be improved, see my comments below.

-Experiments only on 1B model. It would be interesting to see the impacts across more model sizes (smaller and larger) and model architectures to see which range of models really benefit from this. 

-This shows a lot of potential already, but the point would be very strongly proven if they could show comparison to other 1B model performances (DeepSeek, TinyLlama, etc.), showing that their approach yields superior models in general.

-Should this really be considered a multi-agent system or is this really a multi-step process? I don’t see any use of reasoning or decision making here. It seems at each step, each agent is systemically called/updated and each data point is labeled with a combination of scores from the “agents”. What is “agentic” about this?

-Does your approach add significant additional latency to the pretraining stage? 

-Is your approach particularly valuable for small models?

### Questions
-Figure 2 could be more clear to show that each agent has its own memory. Consider focusing only on the Domain Agent’s flow of work to make it easier to follow.

-In Table 1, it would be best to bold the top results so it’s easier to see that your approach is indeed among the best.

-Should this really be considered a multi-agent system or is this really a multi-step process? I don’t see any use of reasoning or decision making here. It seems at each step, each agent is systemically called/updated and each data point is labeled with a combination of scores from the “agents”. What is “agentic” about this? The approach is still valuable, just questioning whether it falls under “agents”.

-Does your approach add significant additional latency to the pretraining stage? 

-Is your approach particularly valuable for small models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors argue that training data selection is an important component in LLM training. The various techniques that had been proposed might be conflicting in their recommendations. The authors are proposing a technique in which the different data selection algorithms are considered independent agents, with an "agent console" integrating the recommendations. The approach enable the dynamic adjustment of contributions of the agents during the training process of the LLM. The SlimPajama dataset is used as the working example.

### Strengths
* A case study validates the initial claim of the paper, that the quality, diversity and influence scores of data are not strongly correlated with each other.
* Relatively extensive experiments were conducted with the training of a 1.3B LLAMA LLM.

### Weaknesses
 * The fact that the diversity of topics, quality of material, and influence on the trained LLMs are different metrics is not a surprising observation - these are obviously very different things. A strong correlation between them would be the surprise. 
* The term "agent" has a relatively clear definition in the AI literature, as an autonomous entity, that takes actions in an environment, in the pursuit of a goal. The fact that the authors have to introduce a definition for the term "agent" and "agent console" and define them in terms of "data selection method" makes the paper difficult to follow. It doesn't seem that these "agents" are taking any actions, or have any autonomy. 
* In practice, the proposed approach appears to be a way to make a decision about what training data to include based on weighting three pre-existing metrics about the data sources. This decision process could have been easily written without introducing agent language. In fact, practitioners very likely are already making such judgements.

Considerations after reading the answers: despite the authors providing very long rebuttals, the answers contain nothing concrete that would change the evaluation.

### Questions
* How does the definition of the agent used in this paper relates to the term agent used in other fields of AI? Such as multi-agent RL, or the type of work usually published in AAMAS? 
* The term "console" is usually applied to a component that is used by a human operator. Is the term agent console in the paper related to it?

NOTE about answers:
- This reviewer is obviously familiar with the Russel-Norvig book, that overall takes an agent view to AI. Nevertheless, what the authors propose here are not agents, as pointed out by other reviewers as well. 
- The answers contain references to the consoles in Salesforce etc. But if the authors would have checked what those products are, they are intended for the human operator.

### Soundness
2

### Presentation
3

### Contribution
2
