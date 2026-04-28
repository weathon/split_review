# Leveraging Large Language Models for Optimised Coordination in Textual Multi-Agent Reinforcement Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Cooperative multi-agent reinforcement learning (MARL) presents unique challenges, amongst which fostering general cooperative behaviour across various tasks is critical. Recently, large language models (LLMs) have excelled at dealing with challenges in the general RL paradigm, showcasing remarkable sample efficiency and adaptability across tasks through domain specific fine-tuning, or functional alignment. However, neither LLMs nor these fine-tuning approaches are designed with coordination-centric solutions in mind, and the challenge of how to achieve greater coordination, and hence performance, with LLMs in MARL has not yet been tackled. To address this, we introduce the 'Functionally-Aligned Multi-Agents' (FAMA) framework. FAMA harnesses LLMs' inherent knowledge for cooperative decision-making via two primary mechanisms. Firstly, it aligns the LLM with the necessary functional knowledge through a centralised on-policy MARL update rule. Secondly, it recognises the pivotal role of communication in coordination and exploits the linguistic strengths of LLMs for intuitive, natural language inter-agent message-passing. Evaluations of FAMA in two multi-agent textual environments, namely BabyAI-Text and an autonomous driving junction environment, over four coordination tasks show it consistently outperforms independent learning LLMs and traditional symbolic RL methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed FAMA which utilizes LLM-based agents in multi-agent settings, to solve the problems of sample inefficiency in online MARL training, policy generalization, and human interpretablity. Evaluations were done in two multi-agent textual environments.

### Strengths
It seems to be a novelty to consider LLM-based agents in MARL tasks, although the idea is straightforward in the context of LLM agent research.

### Weaknesses
From my viewpoint, there's a lack of deeper insights or discussion about why LLM-based agents work better in MAS tasks. See the Questions part.

1. Although using LLM agents in MAS is a straightforward idea, I am still wondering: do we really need multiple LLMs to solve the problems? (Especially considering that the game settings in the paper are not fully decentralized.) Could the agents in the MAS task just send their partial observations to a single central LLM, which will make all the decisions? In my opinion, the aim of multiple LLM agents is more about exploring the potential of LLM, for example, when facing a complicated task, using an explicit planner agent and an explicit executor agent is better than throwing all the problems to a single LLM agent. But in this paper, LLM agents are just the agents in MAS tasks.
2. Prompt function piV, is it a fixed one or a trainable one? 
3. Is there any idea about why policies output by finetuned LLMs perform better than the ones by traditional RL algorithms? After all, the experimental tasks are not complicated, and the RL algorithms should be specially designed for this.

### Questions
1. Although using LLM agents in MAS is a straightforward idea, I am still wondering: do we really need multiple LLMs to solve the problems? (Especially considering that the game settings in the paper are not fully decentralized.) Could the agents in the MAS task just send their partial observations to a single central LLM, which will make all the decisions? In my opinion, the aim of multiple LLM agents is more about exploring the potential of LLM, for example, when facing a complicated task, using an explicit planner agent and an explicit executor agent is better than throwing all the problems to a single LLM agent. But in this paper, LLM agents are just the agents in MAS tasks.
2. Prompt function piV, is it a fixed one or a trainable one? 
3. Is there any idea about why policies output by finetuned LLMs perform better than the ones by traditional RL algorithms? After all, the experimental tasks are not complicated, and the RL algorithms should be specially designed for this.

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper introduces the 'Functionally-Aligned Multi-Agents' (FAMA) framework towards better textual MARL agents, by tuning the LLM with MAPPO to act as a shared actor and centralized Critic, also integrating a communication module (using LLM) with discrete messages. The paper does experiments on the extended BabyAI-text environment and the traffic junction environment with Flan-T5-Base(small).

### Strengths
- The paper studies the important question of how to better leverage LLMs for cooperative MARL, and whether natural language communication between agents is useful for improving coordination and interpretability.

- The paper introduces a new framework to tune the pre-trained LLM with MAPPO to act as a shared actor and centralized Critic for better coordination functionality alignment and integrates a communication module with natural languages though in a discrete manner.

### Weaknesses
The experiment results are not very convincing.

- In Figure 3, there seems no significant difference between the proposed method and the baseline on the Junction Environment (individual agents!), which largely weakens the effectiveness of the proposed method from my perspective.

- If I'm not misunderstanding it,  only for experiments in Figure 3 Junction Environment the Small size version of the Flan-T5 is used. Then why is a larger size model (Base) used in Figure 4 with ablations?

- To answer the Q2 raised in the paper, the current results in Figure 4 are not enough to me, more analysis on the discrete message selected is needed.

- More training details on the baselines are needed.

- The environment experimented on seems simple and toysome with short horizons. It would strengthen the paper to have more experiments on harder envs.

The presentation is poor

- Figures need further improvements. Eg. In Figures 1 and 2, the text under the image is too small, in Figure 3, the text is too small and hard to tell whether a higher or lower metric is better.

- The notation used in sec 4.1 is not always consistent.

- There are many typos in the paper, especially the citations are in a weird format.

- How's the communication done when there are more than 2 agents (as shown in Figure 2 b)? How are the discrete messages selected in the first place and how does that affect the performance?

- Only using a simple textual agent identifier with a shared actor network may not work when the agents are not homogeneous

### Questions
Please address the concerns mentioned in the weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method(FAMA) facilitating coordination for textual multi-agent reinforcement learning by leveraging LLM. FAMA consists of an actor where LLM can be used to infer probability of each action, a communication module to enhance agent-to-agent coordination and a functional alignment step to fine-tune the LLM with a critic head.

The experiments results are promising and FAMA beats benchmarks  in most environments. Communication module is particularly studied where its sample efficiency is demonstrated and ablation study reinforces its contribution.

### Strengths
Applying LLM to RL in general is a relatively new and interesting topic. This work extends LLM to multi-agent setting where natural language exhibits a. nature role in "communication" among agents.

The experiments are not complicated environments but solid enough to me to demonstrate proposed method's superiority.

### Weaknesses
1. The paper is in general not well written, especially in section 4. Notation is difficult to understand and sometimes with ambiguity. For example, in section 4.2, what are parameters of \hat{p}_i_V? And in section 4.3, are those m_i^V are automatically generated or pre-selected and using LLM to get its likelihood? It might be better to give a couple of examples  for 4.2, 4.3 to demonstrate how those steps are conducted.

2. Since it's a paper without any theoretical justification, more environments results might be more convincing.

### Questions
Stated in weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Functionally-Aligned Multi-Agents (FAMA) framework to improve coordination in Multi-Agent Reinforcement Learning (MARL) using Large Language Models (LLMs). FAMA innovatively employs LLMs for action selection and inter-agent communication, extends traditional game models to better suit text-based environments, and addresses key research questions about the role of LLMs and natural language in MARL. The framework aims to offer a structured approach for enhanced decision-making and coordination among agents.

### Strengths
1. The use of Large Language Models (LLMs) as policy mechanisms in Multi-Agent Systems (MAS) is highly innovative. This unique approach sets the paper apart and introduces a new dimension to the field.

2. The paper excels in the design aspects, particularly in the formulation of prompts. The detailed approach in this area adds depth and rigor to the research, enhancing its overall quality.

### Weaknesses
1. While the paper offers a novel approach by combining reinforcement learning and LLMs, the alignment strategy doesn't seem to differ significantly from past CTDE methods. This raises questions about the contribution of the work.

2. The paper employs a text-based environment, which limits the applicability of using LLMs as policies in general RL tasks where text cannot be directly used for actions with the environment. This constraint could limit the generalizability of the method.

3. While the paper shows that communication improves performance, it doesn't provide a comparative analysis to quantify how much better the performance is when using natural language for communication as opposed to non-natural language methods.

### Questions
1. If the method to solve the multi-agent problem still relies on the CTDE's credit assignment approach, then where does the advantage of LLMs manifest, apart from the part where it can communicate using natural language?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
