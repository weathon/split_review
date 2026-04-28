# Adaptive In-conversation Team Building for Language Model Agents

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Leveraging multiple large language model (LLM) agents has shown to be a promising approach for tackling complex tasks, while the effective design of multiple agents for a particular application remains an art. It is thus intriguing to answer a critical question: \textit{Given a task, how can we build a team of LLM agents to solve it effectively?} Our new adaptive team-building paradigm offers a flexible solution, realized through a novel agent design named \emph{\Ours}. It dynamically forms and manages teams for each step of a task-solving process, utilizing nested group conversations and reflection to ensure diverse expertise and prevent stereotypical outputs, allowing for a flexible yet structured approach to problem-solving. A comprehensive evaluation across six real-world scenarios demonstrates that \Ours significantly outperforms existing multi-agent methods with 21.94\% improvement in average accuracy, providing outstanding performance without requiring task-specific prompt engineering. Our exploration of different backbone LLM and cost analysis further shows that \Ours can improve the conversation quality of weak LLM and achieve competitive performance with extremely low cost, which illuminates the application of multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Multi-agent systems (MAS) has shown to be superior to single agent system if constructed properly. However, designing a perfect MAS requires carefully designing the agents involved, tool integrated, communication mechanism and etc. The process can be labour-intensive and time-consuming with the outcome of a MAS comes after the execution and refine the designed system need trial-and-error as well. This paper aims to tackle this annoying issue by proposing a adaptive team building method. It introduce a captain agents dynamically forms a team and utilizes the nested group chat mechanism with a reflection agent to provide a flexible and structured approach to task-solving.

### Strengths
1. The paper conducts a comprehensive evaluation on their approach. Including six real-world scenarios showing that there method is superior to various baseline and they also carry out a series of ablation study on 1) static team building vs adaptive team building 2) w and w/o tool library or agent library 3) the effect of  different backbone llm 4) cost analysis.

2. The paper provides a comprehensive overview of relevant studies, effectively situating the current research within broader literature landscape.

Though the paper present certain limitations (see Weaknesses), I would rate it a 6 due to its strong empirical results. I would also be open to increasing the score if the authors address the questions and concerns raised.

### Weaknesses
The paper conducts an extensive set of experiments and provides a thorough analysis of its approach within the context of Multi-Agent Systems (MAS). However, the main limitation appears to be in the novelty of the proposed contributions.

1. If I understand correctly, the proposed approach heavily relies on an existing MAS framework, AutoGen, which is already designed with scalability and flexibility in mind. While this paper extends AutoGen by adding new features, these additions may lack sufficient originality to distinguish the work from the underlying framework. A clearer differentiation or unique contribution would enhance the paper's impact.

Additionally, there are some experimental details that are not fully addressed, and some claims are made without adequate supporting evidence.

1. Figure 3: It is unclear what the main distinction is between "agent retrieval" and "agent selection." If the subtask involves retrieving an agent and tool, why is this set not directly utilized to complete the subtask and need the selection process?

2. Line 230 (Cached Team): The concept of a "cached team" needs further clarification. Is the cache meant to store the entire chat history or only the configuration? And, when invoked, does the cached team resume task-solving with its prior memory?

3. Line 243 (Nested Group Conversations): The term "nested group conversation" lacks sufficient explanation. Why is it called "nested"? Does this entail initiating a sub-group conversation? Additionally, how is the order of agent's speaking determine (Do they speak sequentially or simultaneously)? Lastly, does the subtask require the captain agent to decompose it further into sub-subtasks?

4. Section 2.4 (Adaptability): Does the approach dynamically alter the agent framework or workflow during addressing specific instances? Or does "adaptive" here mean that while the team composition can be configured based on instructions, it remains fixed once problem-solving begins?

5. Line 374 (AutoGen Assistant with a fixed system message is hard to complete.): Given that the proposed method is substantially built upon AutoGen, the authors should clearly highlight the key differences. A case study illustrating the features unique to this method, and absent in AutoGen, would benefit readers.

6. Section 3.4 (Static Team Construction): Additional information is needed on how the task-specific static team is constructed.

7. Section 3.4.2 (Predefined Tool and Agent Usage): Can it be inferred that the predefined tools and agents play a significant role, and that the auto-generation of agents contributes minimally?

8. Line 534: The statement that "this new paradigm helps ensure diversity, prevents limited knowledge extraction, and reduces stereotypical outputs" requires clarification. Specifically, what do "limited knowledge extraction" and "stereotypical outputs" mean in this context? Additionally, is there supporting evidence for this claim?

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces "Captain Agent," an adaptive multi-agent system designed for dynamically building and managing LLM-based agent teams to handle complex tasks. The "Adaptive Build" paradigm, driven by Captain Agent, aims to outperform static approaches by tailoring agent teams to evolving task demands. Evaluations across six real-world scenarios reportedly show significant accuracy improvements, particularly without intensive prompt engineering.

### Strengths
1. The adaptive team-building approach is novel and well-designed, allowing for dynamic adjustments based on task requirements.
2. The paper provides a comprehensive evaluation, demonstrating Captain Agent's effectiveness in varied tasks, from data analysis to programming.
3. The design aims to perform well with minimal prompt customization, enhancing scalability.

### Weaknesses
1. Performance improvements heavily rely on using GPT-4-0125-preview for Captain Agent, raising questions about whether the gains stem from model strength rather than the proposed team-building design.
2. Using GPT-4-0125-preview as the backbone for Captain Agent but not for all baselines could create an advantage that does not necessarily reflect the paradigm's effectiveness. Ensuring baselines operate with equivalent model capabilities would strengthen the fairness of the comparisons.
3. The absence of ablation studies using weaker LLM backbones for Captain Agent limits clarity on whether performance gains come from the design itself or the underlying model. The limited dataset size, with only 257 data samples, further emphasizes the need for a more thorough analysis of the framework's components, such as the Reflector LLM and memory cache, to understand their individual contributions.

### Questions
As in weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors are working in the domain of multi-agent interaction with LLMs. They mention that previous frameworks are either 1) inefficient by giving duplicate work or 2) not able to adapt as the tasks become more complex. Due to this the authors propose a multi-agent team-building paradigm called adaptive build that will not only select relevant agents and tools but also give feedback to the main builder to adjust the set of LLMs as the tasks progresses. 

They name their method Captain Agent which first identifies a subtask, lists the roles needed for this subtask, puts together a team of agents (LLMs) and tools. The agents will talk to each other to try to solve the task. Once the task is complete there is a separate LLM called the reflector that provides feedback on whether to adjust the team of agents or subtask or output the results.

The authors run Captain Agent on real-world scenarios like math, data analysis, programming, science problem solving and world information retrieval. They compare their setup against other popular agent building platforms and show they outperform these frameworks in terms of accuracy.

The authors also run some ablation studies: 1) how does performance change without the agent/tool library and 2) how does performance change with different LLMs as the builder manager (gpt-4, gpt-4o, Llama etc). Additionally the authors show that their framework can be more cost effective in terms of how much it costs calling these model APIs.

### Strengths
1) The authors are tackling a very challenging problem and are proposing what seems to be a novel solution to this domain. The most significant contribution to me is the Reflector LLM that provides feedback to the agent builder such that it can learn a more efficient team. I also think it's great that the authors did cost analysis; however, it would be good to see what are other costs that could be measured such as latency. Is there a large increase in latency given the multitude of steps.

2) The authors do compare against a strong set of baselines. They mention some of the differences between their framework and previous ones in Appendix C which I think should be referenced in the actual text. Also it was good to see that the authors ran their framework on a diverse set of scenarios.

### Weaknesses
I think there can be much more clarity in the presentation of the paper and more discussion regarding certain components of the Captain Agent framework.

Regarding discussion of certain components:

1) There isn't much discussion on the impact of the Reflector LLM. I would like to know what are specific examples of errors caught by this component and quantitative results showing its impact on overall performance.

2) Also there was a mention of a memory cache, but it's unclear how it was used in the framework. I would also like to see quantitative results showing its impact on overall performance.

3) Also analysis like the number of turns in the conversation before completing the task, the number of cycles Captain Agent had to go through before completing the task.

Regarding clarity:

1) I think Figure 4 in the Appendix is great to have. It made the high-level understanding of the framework easier and should be referenced in the main text.

2) I would like to know more detail regarding how was the agent library constructed. Additionally, how much effort is required to adapt the library for a new task domain?

3) Also some notation is unclear such as what is "agent_1_3" mean.

### Questions
I listed my questions and suggestions in the Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the problem of the auto-building of LLM-based multi-agent systems. This work proposes an adaptive team-building paradigm, where a Captain Agent dynamically forms and manages a group of agents for different decomposed steps of a given task instruction. Experimental results on six datasets validate the effectiveness and cost efficiency of the proposed Captain Agent.

### Strengths
1. Propose a new LLM-based multi-agent framework for real-world problem-solving, which is well-motivated by the real-world team building.
2. Introduce the nested group conversation and reflection schemes among agents.
3. Experimental results on six datasets validate the effectiveness and cost-efficiency of the proposed Captain Agent.

### Weaknesses
1. The idea of adaptive building is kind of incremental from the idea of auto building, by just adding more "specialized" agents with tailored prompting schemes. 
2. The overall framework (as shown in Fig.3) is really complicated, which may introduce high variance on the final performance due to the prompt sensitivity of LLMs. The reproducibility of the results will also be questionable. 
3. The presentation of the experimental results is a bit confusing, such as the choice of datasets in different analysis, the backbone of LLMs for different frameworks, etc. (More in the questions)

### Questions
1. How is the respective performance on the agent retrieval and agent selection? The ablation study only shows the performance without the library.
2. Why different datasets are adopted for different analysis? For example, only the GAIA is adopted for the analysis of the agent/tool library, but the rest are used for the analysis of dynmic team-building.
3. In the cost analysis, how did you compute the cost in terms of different backbones? Is that fair? Should we focus on the cost comparison between different frameworks with the same backbones?
4. The results in other tables also contain a mix of frameworks with different backbones. It makes the results kind of confusing on whether the performance gain is from the backbone or the framework.

### Soundness
3

### Presentation
3

### Contribution
2
