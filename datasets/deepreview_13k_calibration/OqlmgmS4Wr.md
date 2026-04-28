# AgentTuning: Enabling Generalized Agent Abilities for LLMs

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Open large language models (LLMs) with great performance in various tasks have significantly advanced the development of LLMs. 
However, they are far inferior to commercial models such as ChatGPT and GPT-4 when acting as agents to tackle complex tasks in the real world.
These agent tasks employ LLMs as the central controller responsible for planning, memorization, and tool utilization, necessitating both fine-grained prompting methods and robust LLMs to achieve satisfactory performance.
Though many prompting methods have been proposed to complete particular agent tasks, there is lack of research focusing on improving the agent capabilities of LLMs themselves without compromising their general abilities. 
In this work, we present \textit{\method}, a simple and general method to enhance the agent abilities of LLMs while maintaining their general LLM capabilities. 
We construct \textit{\dataset}, a lightweight instruction-tuning dataset containing high-quality interaction trajectories. 
We employ a hybrid instruction-tuning strategy by combining \dataset with open-source instructions from general domains. 
\method is used to instruction-tune the Llama 2 series, resulting in \textit{\model}.
Our evaluations show that \method enables LLMs' agent capabilities without compromising general abilities. 
The \model-70B is comparable to GPT-3.5-turbo on unseen agent tasks, demonstrating generalized agent capabilities.

\hide{%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Recent advancements in large language models (LLMs) have ignited sparks for achieving artificial general intelligence (AGI).
LLMs have demonstrated continuous evolution in intelligence, surpassing human performance in many domains.
While existing open-source LLMs excel in traditional NLP tasks, they are far inferior to state-of-the-art commercial counterparts such as ChatGPT and GPT-4 when acting as agents to tackle complex tasks in the real world.
These agent tasks employ LLMs as central controller responsible for planning, memorization, and tool utilization, necessitating both fine-grained prompting methods and robust LLMs to achieve satisfactory performance.
Although many advanced prompting methods have been proposed to enhance existing models, limited research focus on improving the agent capabilities of the models themselves.
Furthermore, many studies have focused on specializing LLMs in particular domains, which often comes at the expense of losing their general capabilities and limits their applicability.
In this work, we introduce \textit{\method}, a general method to enhance the agent capabilities of LLMs while maintaining their general abilities. We first present \textit{\dataset}, a lightweight instruction-tuning dataset containing high-quality interaction trajectory by GPT-4.
We employ a hybrid instruction-tuning strategy by combining the \dataset with open-source datasets from general domains. This approach is used to train the Llama 2 series, resulting in \textit{\model}.
Extensive evaluations show that our method enables LLMs' agent capabilities without compromising general abilities.
The 70B \model nearly approaches GPT-4 on 6 held-in tasks and is comparable to ChatGPT on 6 held-out tasks, demonstrating  generalized agent capabilities.
We open source our datasets and models of 7B, 13B, and 70B scales, hoping they can be viable alternatives to API-based commercial models for agent tasks.
}
\begin{figure}[hbtp]
    \centering
\begin{subfigure}[t]{.45\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/head-figure-2}
    \caption{Overall score in our held-in and held-out tasks.}

\end{subfigure}
\begin{subfigure}[t]{.54\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figures/agent-bench-overall}
    \caption{Closed \& open LLMs on agent tasks~\citep{liu2023agentbench}}

\end{subfigure}
    \caption{
    (a) \textbf{\model exhibits superior performance}. \model is a series of models fine-tuned on the foundation of Llama 2 chat. Moreover, its generalization capability on held-out tasks is on par with GPT-3.5;  (b) This figure is directly re-printed from AgentBench~\citep{liu2023agentbench} with permission. \textbf{Open LLMs significantly underperforms API-based LLMs}.
    }
    \label{fig:head-image}
\end{figure}

\newpage

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents AgentTuning, a methodology designed to enhance the capabilities of Large Language Models (LLMs) when they are employed as agents, while preserving their broader language understanding and generation abilities. It introduces AgentInstruct, a specialized instruction-tuning dataset, and an integrated instruction-tuning approach that combines it with publicly accessible instructions spanning various domains. Through experimental evaluations conducted on AgentLLaMA (instruction-tuned LLaMA2 series), the paper demonstrates that AgentTuning substantially improves the performance of LLMs in agent roles while maintaining the LLMs' foundational language understanding and generation capabilities. Notably, AgentLLaMA-70B exhibits comparable performance to GPT-3.5-turbo on unseen agent-related tasks.

### Strengths
- The motivation to improve the agent ability of open-sourced LLM is good.
- It is well-written and the idea it presents is clear.
- The evaluation is extensive and the results look promising.

### Weaknesses
 - Some details of the dataset construction is unclear.
- The training strategy used for instruction-tuning is limited.
- The rationale behind some design choice needs more explanations.

### Questions
This paper proposes the instruction-tuning dataset and hyprid instruction-tuning to improve the agent ability of open-sourced LLM (i.e., LLaMA2). I think it is a significant contribution to the LLM community. However, I have some concerns as the following.
- The authors claim that they use a reward $r$ to filter out low-quality trajectories, but how this reward is calculated/generated is unclear to me. Besides, as the trajectories are generated by GPT3.5/4, I think the trajectories may contain some misleading information. I wonder whether there is a human evaluation of the correctness of the trajectories.
- It leverages a hybrid instruction-tuning strategy, which is a simple multi-task training in essence. Based on my understanding, improving the agent ability while preserving the general language understanding ability is close to a continual learning scenario. So I think it is important to discuss some typical training strategies like weight regularization[1] and parameter allocation[2] used in continual learning. And it would be better if you can further provide some results when such strategies are applied to see whether these strategies can benefit training.
- The rationale behind some design choices is not well-explained. For example, why is the ratio of sampling between GPT3.5 and GPT4 set as 1:4 and why is the threshold of reward $r$ is set as 2/3? Are there any rules or experimental explanations for these choices?  

[1] Kirkpatrick et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences 2017.  
[2] Serra et al.  Overcoming catastrophic forgetting with hard attention to the task. ICML 2018.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present to fine-tuning LLMs for agent behaviors with a new dataset collected using demonstrations of GPT models, and demonstrated that LLAMA models achieve significantly better performance on the held-out test set after fine-tuning.

### Strengths
1. Agent tuning is an exciting and important direction to study for the LLMs as intelligent agents.
2. The authors' data/training/model have been well-documented. The results should be reproducible

### Weaknesses
1. Figure 1 (b), I don't think the message is fair for this figure, since you trained on AgentBench (although partly), but the other LLMs have not trained on AgentBench. One of the down-sides for open-source LLMs is the ability to generalize to `different' settings from training, but the proposed work has essentially made AgentBench in-distribution by training.
2. It seems that GPT models are heavily relied on for generating training data. Do we have some sense of how to go beyond GPT models? Suppose we want to push the boundaries of GPT-4, then GPT-4 data may not work as well.
3. I have concerns for generalization to other agent tasks that are distinct, but not captured in agent-bench. For example, driving or operating Minecraft.

Overall, my main concern is that the improvements might have come from better instruction following, not agent reasoning.

Minor issues:
- Figure 1 (a), Where does the overall score stand against GPT-4, from which you collected training data?

### Questions
1. How does AlfWorld results in table 4 compare to [1], which reported higher score than the highlighted best open-source model?




[1] Micheli, Vincent, and François Fleuret. "Language models are few-shot butlers." arXiv preprint arXiv:2104.07972 (2021).

### Soundness
2 fair

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies mixing state and action trajectories with general instruction tuning corpus to improve open-source LLM agents’ decision making capabilities while keeping their generalization performance. The authors propose a 3 stage approach: generating instructions, collecting trajectories, and filtering them based on task reward. For tasks where instructions are not already given, the paper uses similar auxiliary tasks or zero-shot prompts the LLM to construct a task input and outputs. Trajectories are collected by prompting the LLM agent using ReAct to generate actions, running in the environment to collect rewards and extra feedback, and continuing in a loop till an episode is terminated. Trajectories are filtered based on task specific thresholds. Finally, this trajectory corpus is combined with ShareGPT corpus to train a Llama-2 model. The authors show that the model improves baseline Llama-2 on decision making tasks while keeping its general capabilities and is competitive with GPT-4.

### Strengths
The paper is written well and easy to follow. It presents a set of expensive experiments, showcasing that open-source LLMs can be competitive with proprietary LLMs when trained on the right data.

### Weaknesses
While the empirical contribution is significant, the paper overall feels incremental with straightforward improvements over prior instruction tuning and knowledge distillation. Some of the design decisions are also not explained.

1. While the agent trajectories are very valuable and costly to collect, they are mainly extracted from public tasks/benchmarks by using ReAct with GPT models. The overall process with instruction generation, trajectory collection, and filtering can be useful for other data collection efforts but they are relatively straightforward. For example, ReAct/COT prompting is used with no significant change, reward filtering is also a standard practice in imitation learning. I suggest highlighting main challenges and how significant they are in addition to remedies that you introduced.

2. Using an already available corpora with ReAct and filtering trajectories based on a threshold seems to be reducing the size of the data drastically. For example, in Mind2Web, only a tiny fraction is kept. It is not clear if the benefit of COT annotated trajectories can overcome the reduction in the data size. Can you present results where you make use of the data as much as possible even if you can’t inject COT annotations?

3. How did you choose $\eta$? Given that it denotes the tradeoff between broader generalization vs agent-task performance, it is important to highlight its impact. Are your models sensitive to this parameter?

4. Similarly, how did you decide 1:4 ratio for GPT-4 vs GPT-3.5?

5. What is GPT-4’s interaction trajectory with the DB? How did you end up collecting multi-turn dialogues? Are you using rule-based turn generation to convert DB response into a prompt?

6. Is ShareGPT not leaking any of the test-time task data? It would be helpful to clarify.

### Questions
1. What are main challenges that you had and how significant they are?

2. Can you make use of the available data as much as possible? Would that improve the results even without the COT annotations?

3. How did you choose $\eta$ And 1:4 ratio?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
