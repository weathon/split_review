# AgentGym: Evaluating and Evolving Large Language Model-based Agents across Diverse Envronments

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
Large language models (LLMs), with their generalized capabilities, are considered as a promising foundation to build generally-capable agents that can handle multi-turn decision-making tasks across various interactive environments. Previous attempts typically gather expert-provided trajectories and have LLM-based agents imitate these trajectories step-by-step. However, this supervised fine-tuning approach depends heavily on human supervision, limiting scalability and restricting the agent's exploration and learning in the environments. In this paper, we take the first step towards developing generally-capable LLM-based agents that can explore and evolve themselves across diverse environments. To achieve this, we identify a trinity of ingredients: 1) diverse interactive environments for agent exploration, 2) a trajectory set to equip agents with basic capabilities and prior knowledge, and 3) an effective and scalable approach for agent improvement across environments. We propose AgentGym, a new interactive framework featuring various real-world scenarios and environments for broad, unified, real-time, and concurrent agent exploration. AgentGym also includes a database with expanded instructions, high-quality trajectories, and a benchmark suite. Next, we investigate the potential of agent self-evolution across various environments with a derived exploration-learning method named AgentEvol. Experimental results show that the evolved agents can achieve results comparable to SOTA models. We will release the code, dataset, benchmark, and checkpoints.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
* Comprehensive framework designed to evaluate and evolve LLM based agents across diverse interactive environments
* Agents can explore and learn autonomously
* AGENTGYM includes a suite of 14 environments covering seven real-world scenarios, along with expanded instructions, a benchmark suite (AGENTEVAL), and high-quality trajectory datasets (AGENTTRAJ and AGENTTRAJ-L)
* Presents AGENTEVOL, an exploration-learning method derived from the RL as Inference framework, enabling agents to self-evolve across multiple environments
* Experimental results demonstrate that agents evolved using AGENTEVOL can achieve performance comparable to or exceeding state-of-the-art models

### Strengths
Comprehensive Framework: AGENTGYM provides a versatile and extensible platform for evaluating and training LLM-based agents across a wide range of tasks and environments. This breadth enhances the generalizability and practicality of the agents developed using this framework.

Innovative Methodology: The introduction of AGENTEVOL as an exploration-learning method allows agents to improve themselves based on environmental feedback, reducing reliance on human supervision and expert trajectories

Promising Experimental Results: The agents evolved using AGENTEVOL outperform baseline models and, in some cases, exceed the performance of state-of-the-art models like GPT-4-Turbo on several tasks

Addressing Scalability: The paper tackles the scalability issues inherent in SFT by allowing agents to explore and learn autonomously, which could lead to more efficient and scalable training processes

### Weaknesses
Scalability Concerns with Larger Models: The computational costs associated with running large LLMs in interactive environments are significant. The paper could benefit from a more detailed analysis of the scalability of AGENTEVOL when using larger models, specifically addressing memory consumption and inference latency as model size increases. It would be beneficial to see a breakdown of the computational resources required for different model sizes and how these costs scale with the number of environment interactions.

Comparative Analysis: The comparisons with other exploration-based methods, such as PPO and LLM-Planner, are brief. A more in-depth analysis could strengthen the validation of AGENTEVOL's effectiveness. The paper should include a more detailed comparison of the exploration strategies used by these methods, and how they compare to AGENTEVOL in terms of sample efficiency and the quality of the learned policies. Furthermore, a more thorough analysis of the types of environments where each method excels would be valuable.

Overfitting Risk: The potential for agents to overfit to specific environments or tasks during the self-evolution process is not thoroughly addressed. Strategies to mitigate overfitting would enhance the robustness of the approach. The paper should discuss the risk of the agent learning environment-specific heuristics that do not generalize well to unseen environments, and how the proposed method addresses this. It would be useful to see an analysis of the agent's performance on a held-out set of environments or tasks to evaluate its generalization capabilities.

### Questions
How does the method ensure safety and prevent harmful behaviors during self-modification? How do you put constraints on it during the evolution process?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an interactive framework that includes diverse scenarios and environments for LLM-based agents (AGENTGYM) and investigates self-evolution for LLM-based agents (AGENTEVOL) based on AGENTGYM.

### Strengths
1. The problem that this paper investigates, how to make LLMs explore and evolve themselves across diverse environments, is interesting.
2. The framework and the self-evolution method that this paper proposed make sense.

### Weaknesses
1. This paper would be better if the authors could provide better writing. In general, it would be better if the authors could discuss more about why they do that and mention some key technical features in the paper instead of putting a lot of technical details in the paper. For example, in section 3, the authors could discuss more about why you selected these environments and the AGENTGYM framework. The author could discuss less about the technical details and move them into the supplementary. If the author thinks some technical details are the key contributions of this paper,  the authors might make them as a separate section or subsection and discuss more details.
2. In the experiments section, the author could discuss more about the results they got. For example, in Table 3, why does their method work better than other LLMs in some environments (i.e., WebShop) while performing badly in other scenarios (i.e., Weather)? It would make this paper stronger if the authors could propose some hypothesis based on results instead of just describing what the table shows.

### Questions
Please check the weakness section.

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
The authors propose AgentGym, an interactive framework with various environments, which includes a database with expanded instructions, high-quality trajectories AGENTTRAJ and AGENTTRAJ-L, and a benchmark suite AGENTEVAL. The authors also design AgentEvol, an exploration-learning self-evolution method. The authors conduct experiments

### Strengths
As in the summary, the paper is very comprehensive, including many aspects about LLM-based agents.

### Weaknesses
The paper include both an interactive framework AgentGym, which is composed of several components, and self-evolution method AgentEvol.
It is not clear what the focus is.

ReAct may not be the best reference approach to build LLM-based agents. 
In industrial practice, it has been adopted for around 1.5 years. What are the successful LLM-based agents?
In academic research, there are recent papers for better reasoning / planning capacity, e.g.,
Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking, COLM 2024
AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training, ICML 2024

There are actually papers criticizing the reasoning / planning capacity of LLMs, which is the foundation of agents, e.g.,

GSM-Symbolic- Understanding the Limitations of Mathematical Reasoning in Large Language Models https://arxiv.org/abs/2410.05229

LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench
https://arxiv.org/abs/2409.13373


Agents are about optimal sequential decision making. 
Why only success rate?
Does the LLM-based agent community care about optimal solutions?


AGENTEVOL is one particular RL approach, which may fit some tasks but not others.
As a comprehensive framework, it is desirable to explore various RL approaches.

LLM-based agents are not able to handle the basic grid world problems.
How about including some problems the current RL can handle well in the benchmark?

Figure 1 appears cool (for something like a cartoon book). However, it does not provide more info than the caption, i.e., it is not quite necessary, for a top tier AI conference paper.

### Questions
See weakness

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
4

### Summary
The authors present AgentGym, a global framework for training LLM agents. AgentGym contains a software infrastructure to train an agent onto a set of varied environments, the environments themselves, a benchmark made of a set of instructions (AgentEval), two datasets of expert curated trajectories of different size (AgentTraj and AgentTraj-L), and finally a method to train agents with a behavioral cloning (BC) part and a fine-tuning part based on exploration and learning (AgentEvol). The paper presents the whole framework over the first 3pages, then the rest is dedicated to AgentEvol with a presentation of the method and a experimental study.

I have slightly increased my score as I appreciate the effort of the authors, but I still believe they should make two good papers out of their work.

### Strengths
- building the AgentGym framework is an impressive and useful piece of engineering, that needs to be properly advertized
- the AgentEvol method might be a useful piece of research with interesting capabilities to improve the performance of LLM agents, if properly evaluated with a stronger methodology

### Weaknesses
 - the AgentGym framework part is mostly presented as an engineering effort and is of low interest in the context of a scientific research paper.
- the AgentEvol method is not devoted enough space and is not evaluated thoroughly enough

- If I were the authors, I would merge Section 2 into Section 4.
- When looking at the final update equations, it seems that the AgentEvol method corresponds to the Reward Weighted Regression (RWR) algorithm. See 
* Peters, J., & Schaal, S. (2007, June). Reinforcement learning by reward-weighted regression for operational space control. In Proceedings of the 24th international conference on Machine learning (pp. 745-750).

for the initial reference, and many other papers for more details. If this intuition is correct, then this raises numerous questions about the method: is the author’s derivation original, how does it compare to other derivations of RWR? RWR is quite old and more advanced algorithms such as AWR or AWAC have been published since then: how does AgentEvol compare to these more recent methods?
- the authors suddenly introduce a non-negative reward halfway in the methods: they should rather have a "problem statement" section upfront where they specify that their method only works for non-negative rewards.
- I think the authors should integrate the results of Fig. 4 and Table 5 into Table 3, even if this results in partial lines.
- in the experiments, the authors only perform M=4 iterations. Is the learning process very long?
- could the authors be more explicit on the methodology in the experimental section: do they separate for each environment a train set and a test set?
- what about general purpose agents such as GATO, OpenVLA, etc. ?
- in Table 3, AgentEvol does not seem to improve at all with respect to BC_base in WD and WT. Can the authors explain why?
- training a LLAMA-2-Chat-7B agent (or any other large size LLM) with PPO is not an easy task. Can the authors be more explicit about their methodology here? Do they use LORA tuning? See several papers about applying RL on LLM agents in text worlds, such as for instance:
* Carta, T., Romac, C., Wolf, T., Lamprier, S., Sigaud, O., & Oudeyer, P. Y. (2023, July). Grounding large language models in interactive environments with online reinforcement learning. In International Conference on Machine Learning (pp. 3676-3713). PMLR.
* Tan, W., Zhang, W., Liu, S., Zheng, L., Wang, X., & An, B. (2024). True knowledge comes from practice: Aligning llms with embodied environments via reinforcement learning. arXiv preprint arXiv:2401.14151.
Being a reinforcement learning expert, I'm aware that lot of details are missing in the results corresponding to Figure 4. I suspect this is also the case for all other studies. The authors should devote a full section (in the appendix?) to provide all the details that are missing about the methodology for each method, including theirs.
- In more details, about Figure 4 studies, I would be glad to see e.g. the learning curves, to figure out which methods are stable or not. I would also be glad to see which environments are used for training, and which are kept for testing, particularly in Baby-AI and ALFworld that I know better. In short, the results of Figure 4 may deserve a paper in themselves, the high level overview that we get here does not facilitate scientific evaluation of the work done.
- What do “interaction rounds” mean in Appendix E.1? I’m surprised by the very low numbers.
- Are the SOTA models (as said in the introduction) mentioned in Table 3 still SOTA?
- the abstract and introduction insist on the fact that a lot of works use BC, but the selection of baselines does not support this message: some baselines are zero-shot, some others use RL, this is not much consistent.

### Questions
This section does not only contain questions, but also remarks and advices for submitting better papers next time. Note also that I knew this work before becoming a reviewer of this paper, so I cannot make as if I was discovering it.
After reading the paper and given my knowledge of the AgentGym repository, I’m convinced that the authors are making a publication strategy mistake : they should split their paper into two contributions:
- one about the AgentGym framework, presenting all the engineering contributions, the datasets, etc. In their ICLR submission, to avoid disclosing their identity, the authors are obliged to state that the framework will be open-sourced after publication, while it is already available and it already has users. This paper will be useful as the framework looks great, but I don’t believe it should be sent to a top scientific machine learning conference, as it is mostly engineering. Doing so would also save a lot of space to present the scientific contribution (AgentEvol) in more details. This paper would contain a part of the introduction, Section 3, and Appendices B, C and D. In this paper, the authors might give more details on the way they collect instructions when they rely on an AI-based, automated method.
- and one about the AgentEvol method. The rest of my review will focus mostly on this latter part.

# Comments about AgentEvol and the methodology
- If I were the authors, I would merge Section 2 into Section 4.
- When looking at the final update equations, it seems that the AgentEvol method corresponds to the Reward Weighted Regression (RWR) algorithm. See 
* Peters, J., & Schaal, S. (2007, June). Reinforcement learning by reward-weighted regression for operational space control. In Proceedings of the 24th international conference on Machine learning (pp. 745-750).

for the initial reference, and many other papers for more details. If this intuition is correct, then this raises numerous questions about the method: is the author’s derivation original, how does it compare to other derivations of RWR? RWR is quite old and more advanced algorithms such as AWR or AWAC have been published since then: how does AgentEvol compare to these more recent methods?
- the authors suddenly introduce a non-negative reward halfway in the methods: they should rather have a "problem statement" section upfront where they specify that their method only works for non-negative rewards.
- I think the authors should integrate the results of Fig. 4 and Table 5 into Table 3, even if this results in partial lines.
- in the experiments, the authors only perform M=4 iterations. Is the learning process very long?
- could the authors be more explicit on the methodology in the experimental section: do they separate for each environment a train set and a test set?
- what about general purpose agents such as GATO, OpenVLA, etc. ?
- in Table 3, AgentEvol does not seem to improve at all with respect to BC_base in WD and WT. Can the authors explain why?
- training a LLAMA-2-Chat-7B agent (or any other large size LLM) with PPO is not an easy task. Can the authors be more explicit about their methodology here? Do they use LORA tuning? See several papers about applying RL on LLM agents in text worlds, such as for instance:
* Carta, T., Romac, C., Wolf, T., Lamprier, S., Sigaud, O., & Oudeyer, P. Y. (2023, July). Grounding large language models in interactive environments with online reinforcement learning. In International Conference on Machine Learning (pp. 3676-3713). PMLR.
* Tan, W., Zhang, W., Liu, S., Zheng, L., Wang, X., & An, B. (2024). True knowledge comes from practice: Aligning llms with embodied environments via reinforcement learning. arXiv preprint arXiv:2401.14151.
Being a reinforcement learning expert, I'm aware that lot of details are missing in the results corresponding to Figure 4. I suspect this is also the case for all other studies. The authors should devote a full section (in the appendix?) to provide all the details that are missing about the methodology for each method, including theirs.
- In more details, about Figure 4 studies, I would be glad to see e.g. the learning curves, to figure out which methods are stable or not. I would also be glad to see which environments are used for training, and which are kept for testing, particularly in Baby-AI and ALFworld that I know better. In short, the results of Figure 4 may deserve a paper in themselves, the high level overview that we get here does not facilitate scientific evaluation of the work done.
- What do “interaction rounds” mean in Appendix E.1? I’m surprised by the very low numbers.
- Are the SOTA models (as said in the introduction) mentioned in Table 3 still SOTA?
- the abstract and introduction insist on the fact that a lot of works use BC, but the selection of baselines does not support this message: some baselines are zero-shot, some others use RL, this is not much consistent.

# Typos, minor errors:
- there is a typo in the title (envronments)!
- p.5 the authors mention “golden trajectories” without specifying what it means
- p.5 Then, We → we 
- p.5 rigorously filtered → filter (the rest is at the present tense)
- p.6 , We → we
- p.6 “The former step” → The first step. Then “The latter step” → The second step
- p.6 The step of J(q, \pi…) → the step of doing what exactly? Please be explicit.

### Soundness
2

### Presentation
2

### Contribution
3
