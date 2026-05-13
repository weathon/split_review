# Dynamic LLM-Agent Network: An LLM-agent Collaboration Framework with Agent Team Optimization

- Decision: Reject
- Scores: 5, 3, 8, 6, 6, 5

## Abstract
Large language model (LLM) agents have been shown effective on a wide range of tasks, and by ensembling multiple LLM agents, their performances could be further improved. Existing approaches employ a fixed set of agents to interact with each other in a static architecture, which limits their generalizability to various tasks and requires strong human prior in designing these agents. In this work, we propose to construct a strategic team of agents communicating in a dynamic interaction architecture based on the task query. Specifically, we build a framework named Dynamic LLM-Agent Network (**DyLAN**) for LLM-agent collaboration on complicated tasks like reasoning and code generation. DyLAN enables agents to interact for multiple rounds in a dynamic architecture with inference-time agent selection and an early-stopping mechanism to improve performance and efficiency. We further design an automatic agent team optimization algorithm based on an unsupervised metric termed *Agent Importance Score*, enabling the selection of best agents based on the contribution each agent makes. Empirically, we demonstrate that DyLAN performs well in both reasoning and code generation tasks with reasonable computational cost. DyLAN achieves 13.0\% and 13.3\% improvement on MATH and HumanEval, respectively, compared to a single execution on GPT-35-turbo. On specific subjects of MMLU, agent team optimization in DyLAN increases accuracy by up to 25.0\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contributions of this paper are:

- Proposing a new framework called Dynamic LLM-Agent Network (DyLAN) for organizing collaboration between multiple LLM agents. DyLAN allows agents to interact over multiple rounds in a dynamic architecture.
- Introducing two key components in DyLAN - inference-time agent selection to filter out low-performing agents, and an early stopping mechanism based on Byzantine consensus theory to improve efficiency.
- Developing an unsupervised metric called Agent Importance Score to quantify each agent's contribution, which can then be used to automatically optimize the composition of the agent team for a given task.
- Demonstrating DyLAN's effectiveness on multiple tasks including reasoning, arithmetic and code generation, showing accuracy improvements and reasonable computational cost compared to baselines. Agent team optimization is shown to further boost performance on specific tasks/domains.

### Strengths
- The technical claims around the DyLAN framework and agent team optimization seem reasonably sound, though not groundbreaking. The core ideas build incrementally on related work.
- The experimental methodology is generally solid, with evaluations on multiple representative tasks using reasonable baselines. However, comparisons to some very latest multi-agent LLM methods are lacking.
- The central claims around DyLAN's performance are supported reasonably well by the experiments. The gains over baselines help validate the techniques.
- Analysis and insight could be deeper around why agent team optimization works and whether the proposed scoring method effectively captures agent contributions.
Overall the paper quality seems good. The techniques seem to work fairly well in practice. But the novelty and advancement over recent related work appears modest.

### Weaknesses
The core ideas around dynamically organizing LLM agent collaborations and automatically optimizing the agent team seem novel and could be of interest to the ICLR community. However, the paper is generally incremental work building on a lot of recent research around multi-agent LLMs. The techniques used, like inference-time pruning and unsupervised contribution scoring, are not completely new concepts either.
In more details:
- The experimental validation is reasonable but mainly incremental - evaluating on established datasets with existing baseline methods. More complex, real-world tasks could be illustrative. Specifically, the choice of datasets, while standard, does not fully demonstrate the dynamic capabilities of the proposed framework. For instance, tasks requiring iterative refinement of solutions or complex multi-step reasoning in open-ended environments would be more compelling.
- The paper claims efficient collaboration but the overhead of techniques like peer rating and consensus checks could be significant. More analysis on computational costs is needed. The analysis should include not just the number of API calls, but also the latency introduced by the peer rating and consensus mechanisms. A breakdown of the time spent on each stage of the DyLAN framework would be beneficial.
- There is limited ablation study or analysis into the agent scoring method. It is unclear if it is actually capturing meaningful contribution effectively. The paper should include experiments where the agent importance score is perturbed or randomized to assess its impact on performance. Furthermore, a more detailed analysis of the correlation between the agent importance score and actual contribution, perhaps using human evaluation, would strengthen the claims.
- Why was CodeT chosen as the baseline? This does not appear to be a reasonable baseline. CodeT is not a multi-agent framework for code generation. It works on the principle of generating more test cases in order to improve the ranking of the solutions. Stronger baselines should be chosen for a fairer comparison. The paper should compare against other multi-agent code generation methods, or at least justify why CodeT is a suitable baseline given its single-agent nature.
- The presentation seems repetitive in parts with previous sections being paraphrased. More clarity and conciseness in writing would strengthen the paper.

### Questions
- How does DyLAN's performance compare to other very recent works on multi-agent LLMs? The baselines used seem a bit outdated.
- Can you provide more analysis/insight into why agent team optimization works well? Is the Agent Importance Score capturing something meaningful?
- Have you experimented with DyLAN on more complex, open-ended tasks beyond the datasets used? How does it perform?
- Could DyLAN be extended to do online agent team optimization during inference as well?
- For early stopping via Byzantine consensus, how did you determine the optimal threshold for answer similarity? Was this tuned per task?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper suggests the creation of a tactical group of agents that communicate within a flexible interaction structure tailored to the specific task at hand. The approach involves developing a system called the Dynamic LLM-Agent Network (DyLAN), which facilitates collaboration among LLM agents on complex activities, including reasoning and generating code. DyLAN allows for multi-round interactions among agents within an adaptable framework, incorporating on-the-fly agent selection and a premature termination feature to enhance both performance and efficiency. Additionally, this paper introduces a method for the automatic optimization of the agent team, utilizing an unsupervised metric named the Agent Importance Score. This score helps in determining the most effective agents by evaluating the individual contributions of each agent.

### Strengths
Pros:
1. This paper proposes a framework DyLAN, which presents a novel structure for LLM-agent cooperation, assembling agents in a tiered, feed-forward network that features adaptive architecture, incorporating mechanisms for selecting agents during inference and halting the process prematurely when necessary. 
2. To optimize agent collaboration within DyLAN, this paper crafted a self-governing optimization algorithm that leverages an Agent Importance Score determined without supervision, aiming for a balance of performance and efficiency.
3. This paper claimed that DyLAN has been shown to deliver strong results in accuracy, efficiency, and consistency across a spectrum of tasks, including general reasoning, numerical problem-solving, and the generation of code.

### Weaknesses
Cons:
1. This paper cannot demonstrate that agent collaboration must perform better than single agent. For example, in Figure 6, the agent collaboration is totally unnecessary. The roles such as Programmer, Economist and Doctor are useless for the math reasoning problem.
2. The results are not convincing. For example, does agent collaboration really perform better than single agent on math reasoning? The example in Figure 6 does not show the benefit of agent collaboration on math reasoning.
3. The collaboration process is unclear. For example, in Figure 5, how does the algorithm developer and programmer collaborate together? It seems programmer can already finish the task very well.
4. It is suggested that the authors explain more clearly the function of Agent Importance Scores using examples. Otherwise, it is unclear why it is necessary. This paper says that “We ignore the peer rating scores in responses of agents for computing Agent Importance Scores.” In Figure 5. The author may not ignore the peer rating process.
5. The contribution is limited. The agent collaboration framework only use “role-playing” for different agents, which is proposed in the previous paper [1], and also discussed in many previous papers such as [2]. It is suggested that the authors could consider adding tool use. For example, it does not make sense to use LLMs as unit tester (in Figure 5).
6. Some important references are missing. It is worth noting that this paper does not cite the paper [1] which proposed “role-playing”.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed an approach called DyLAN to optimize the performance of an ensemble of LLMs when answering a query of interest. DyLAN enables better collective performance by having a collaboration framework where ensemble members interact for multiple iterations and rate each others' responses to the query. DyLAN then proposed (i) an **agent selection mechanism** that filters out a few ensemble members with the worst responses and (ii) an **early stopping mechanism** that stops interaction between ensemble members once 2/3 of the ensemble members agree on a common response.

The authors demonstrate that DyLAN achieves better accuracy than baselines in three tasks requiring the ensemble to reason or generate code. DyLAN was compared against representative works that also attempt to improve the performance of a collection of interacting LLMs. Ablation studies were also conducted to demonstrate the importance of various factors related to DyLAN's training process and its own agent selection and early-stopping mechanism.

### Strengths
**Minor Strength - Originality - Method Novelty** 

To the best of my limited knowledge about training an ensemble of LLMs, DyLAN seems to be a novel approach. At least compared to the methods provided in the related section of the work, DyLAN appears to have significant differences (i.e. with respect to the early stopping and agent selection mechanisms) with previous work, which seem plausible in further improving the performance of an ensemble of LLMs. Nonetheless, the topic of training a collection of interacting LLMs itself seems to have been explored by previous works already.

**Minor Strength - Quality - Method Soundness**

Except for some minor weaknesses (written in the section below), DyLAN's early stopping and agent selection mechanism seems generally sound from a multiagent systems perspective. Given the existence of a sufficient number of LLMs that can expertly handle an input query, I find it plausible that DyLAN should be able to identify a smaller number of LLMs whose response we can refer to once they achieve consensus.

**Major Strength - Quality - Experiment**

While I cannot comment much on the baseline selection following my limited knowledge of the topic, I find that the designed experiments were well designed to demonstrate DyLAN's advantages in terms of its overall accuracy and incurred cost during an interaction. At the same time, I highly appreciate the ablation study conducted by the authors to investigate the importance of the early-stopping and agent selection mechanisms. I especially like how it demonstrates the importance of the agent selection mechanism.

**Major Strength - Clarity - Experiment Analysis**

As a reader with less expertise in this topic, I also highly appreciate how the authors carefully outlined the different insights gained from each experiment. This helps in pinpointing the importance of the DyLAN's various components and in gaining an understanding of the capabilities achieved by DyLAN. Similarly, insights gained from comparison against different baselines were properly written down, also making it easier for a reader with less expertise in this topic.

### Weaknesses
 **Minor weakness - Clarity - Lack of Problem Formulation**

It was slightly tricky to grasp the type of queries being solved by the ensemble of LLMs and how they interact with each other. While it is unfortunate that it was relegated to the appendix, Figure 5 is an excellent figure that could have helped readers understand the problem being solved if it had been presented earlier. In place of Figure 5 which seems to take a lot of space, perhaps the authors could consider describing a formal model of the interaction between agents and decision-making problems just to give more context. Specifically, it's unclear what the input space of the queries is, what the output space is, and how the LLMs' individual outputs are structured before being aggregated. A more formal definition of the problem would greatly enhance clarity.

**Minor Weakness - Soundness - Expert LLMs being outnumbered by non-expert members of the ensemble**

I suppose one of the weaknesses of DyLAN is when the number of expert LLMs for dealing with a particular query is significantly lower than the number of non-experts. If somehow the number of non-expert LLMs selected during agent selection is still larger than the experts after agent selection, DyLAN can still yield poor accuracies. Perhaps it could be useful to have multiple rounds of agent selection until some average score/metric (ideally reflecting their capacity in solving the task) of the remaining LLMs is above a certain threshold. This is especially concerning if the initial ensemble is not carefully constructed to ensure a sufficient number of expert LLMs are present for each task.

**Minor Weakness - Soundness - Absence of reliable rankers**

Another possible pitfall occurs when DyLAN does not have a reliable ranker for agent selection, which results in the selection of possibly highly suboptimal members of the ensemble for the final decision. The paper does not sufficiently detail the properties of the ranker used, which makes it difficult to assess the robustness of the method. For instance, it's unclear how the ranker handles situations where multiple LLMs provide very similar responses, or how it deals with responses that are partially correct but contain subtle errors. The paper should provide more details on the ranker's performance characteristics and limitations.

### Questions
1. Is DyLAN equipped with a mechanism to deal with a severe imbalance between expert and non-expert agents?
2. Can you explain the rankers considered for DyLAN and why a specific ranker is chosen?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Dynamic LLM-Agent Network (DyLAN) for LLM-agent collaboration on complicated tasks like reasoning and code generation. It improves the efficiency and the performance of LLM-agent collaboration via inference-time agent selection at a middle-time step and byzantine consensus to terminate inference at a proper layer. They further design an automatic agent team optimization algorithm to optimize the composition of agents for DyLAN based on an unsupervised metric Agent Importance Score,

### Strengths
1. DyLAN properly combines multiple standard techniques to improve the performance and efficiency of LLM-agent collaboration on complicated tasks.
2. In the ablation studies section, the paper empirically shows how different strategies can individually and together contribute to improvement.

### Weaknesses
1. Novelty is somewhat limited since the framework is primarily a combination of standard technologies.
2. The baseline (i.e., random selection) for agent team optimization is very weak.

### Questions
In addition to empirical results, do you have any insights to explain why Shapley Value is not a good metric?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Dynamic LLM-Agent Network (DyLAN), a framework for improving LLM agents collaboration. DyLAN structures the interaction between agents in a feed-forward manner, with an early-exit mechanism and inference time agent selection. It also provides a 3-step agent optimization algorithm (with a metric called Agent Important Score). The framework is evaluated on a number of tasks and has shown performance improvement over a single agent.

### Strengths
- As far as I know, formulating the LLM agent interaction as a feed-forward network seems novel. 
- The proposed method agent selection method and early exit method seem to improve performance and reduce the number of communication rounds.

### Weaknesses
 - It would be beneficial if some of the details of the method were discussed more clearly. For example, how are the agents different from each other? Did you manually create a list of agents before running the experiments? 
- It seems the agent team optimization part is an additional step to the inference, how many rounds of communication and "training" are required to get a specific task ready for inference with high accuracy? Do you need like 10% or more of the dataset for this optimization before you can use it for inference?

### Questions
- When top k agents are selected for the inference agent selection, how is the k selected?
- Are the prompts the same between the agents when queried? Some of the existing methods assign fixed roles, which will guide the LLM to specialize in certain tasks/subtasks, how is the proposed method able to do that?
- In the evaluation section, for Table 4, it seems the gain from your method to the baseline is smaller when using GPT-4 (than GPT3.5). Will this method still be effective when the single LLM model performance improves?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a feedforward dynamic LLM agent network which can collaborate to improve the performance on reasoning and coding tasks. Previous work often include a static set of agents, which does not generalise to various tasks and requires strong human priors. In contrast, DyLAN (Dynamic LLM-Agent Network) has the following advantages with their design: 1. agents with different roles can exchange messages via the feedforward network 2. early-stopping when the agents reach consensus 3. automatic team optimisation by propagation (rating their predecessors in the network), aggregation (aggregate ratings from successors to quantify an agent's contribution) and selection (selecting top performing agents according to their scores derived from the propagation and aggregation steps). Finally, the model is evaluated on reasoning and coding tasks and demonstrates improved performance with reasonable computation cost.

### Strengths
- The paper is written clearly and is easy to follow. The comparison with baseline methods are clearly illustrated in table 1.
- The design of the feedforward communication and dynamic optimisation structure seems straightforward to implement and easily generalisable to various different types of tasks which require multi-agent collaboration and does not require strong human prior.
- The case study (Figure 5) is helpful to understanding practical use cases of the model, and draw a connection of the proposed multi-agent feedforward interaction network to real-world software development scenarios where human developers are assigned different roles to collaborate in improving code quality.

### Weaknesses
One limitation, which seems to be also shared with the compared baselines, is the performance gain compared with computation cost increase, especially when compared with the single execution. For example, in table 2-4, the Overall performance improved 4% but required 7 API calls (MATH dataset), 4 API calls (MMLU dataset) and 15 API calls (HumanEval dataset) compared to 1 API call with the single execution baseline.

For the coding case study, I think it is clear to me why such a multi-agent collaboration is helpful in improving the code performance. However, in the general reasoning task provided (Figure 6), it is unclear to me why it would require the language model to act 4 different roles? I see that on some topic which is debatable, perspectives from agents with diverse roles would help, but it is unclear if that is necessary on some topics which has a single correct solution?
- If an agent is assigned the role of a doctor for solving the example mathematics problem, is the underlying language model deliberately trying to act as if it doesn't know how to solve the problem despite the fact that the same language model underlies the role of the mathematician?
- For example, if we started with a majority of non-experts and a minority of experts, could the system potentially produce a wrong solution due to the non-experts reaching a consensus on a wrong solution and being the majority of the multi-agent system?

On Page 1, in the last paragraph, what does sensitivity mean?

### Questions
For the coding case study, I think it is clear to me why such a multi-agent collaboration is helpful in improving the code performance. However, in the general reasoning task provided (Figure 6), it is unclear to me why it would require the language model to act 4 different roles? I see that on some topic which is debatable, perspectives from agents with diverse roles would help, but it is unclear if that is necessary on some topics which has a single correct solution?
- If an agent is assigned the role of a doctor for solving the example mathematics problem, is the underlying language model deliberately trying to act as if it doesn't know how to solve the problem despite the fact that the same language model underlies the role of the mathematician?
- For example, if we started with a majority of non-experts and a minority of experts, could the system potentially produce a wrong solution due to the non-experts reaching a consensus on a wrong solution and being the majority of the multi-agent system?

On Page 1, in the last paragraph, what does sensitivity mean?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
