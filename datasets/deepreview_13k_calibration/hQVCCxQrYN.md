# Plan-Seq-Learn: Language Model Guided RL for Solving Long Horizon Robotics Tasks

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Large Language Models (LLMs) have been shown to be capable of performing high-level planning for long-horizon robotics tasks, yet existing methods require access to a pre-defined skill library (\textit{e.g.} picking, placing, pulling, pushing, navigating).
However, LLM planning does not address how to design or learn those behaviors, which remains challenging particularly in long-horizon settings.
Furthermore, for many tasks of interest, the robot needs to be able to adjust its behavior in a fine-grained manner, requiring the agent to be capable of modifying \textit{low-level} control actions. Can we instead use the internet-scale knowledge from LLMs for high-level policies, guiding reinforcement learning (RL) policies to efficiently solve robotic control tasks online without requiring a pre-determined set of skills? In this paper, we propose \textbf{Plan-Seq-Learn} (\our): a modular approach that uses motion planning to bridge the gap between abstract language and learned low-level control for solving long-horizon robotics tasks from scratch. We demonstrate that \our achieves state-of-the-art results on over \textbf{25} challenging robotics tasks with up to \textbf{10} stages. \our solves long-horizon tasks from raw visual input spanning four benchmarks at success rates of \textbf{over 85\%}, out-performing language-based, classical, and end-to-end approaches. 
Video results and code at 
\texttt{\href{https://mihdalal.io/planseqlearn/}{https://mihdalal.io/planseqlearn/}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method/framework called Plan-Seq-Learn (PSL) for solving long-horizon robotics tasks. The key idea is a decomposition of long robotic manipulation tasks, and then tackle each part using a reasonable method. Specifically, they combine LLM for highly abstract task planning, off-the-shelf visual pose estimator and motion planner (AIT*) for sequencing each sub-tasks, and RL for the sub-tasks. This allows PSL to leverage the advantage of each module. Extensive experiments show PSL can efficiently solve 20+ long-horizon robotics tasks, outperforming prior methods.

### Strengths
1. The approach is sensible and reasonable to leverage current popular methods for robot learning - LLM for high-level planning, classical motion planner for efficient collision-free path planning, and RL for the contact-rich manipulation stage.
2. The general framework is novel in combining these techniques although each part is not entirely new. And the paper clearly explains how to use their advantages in solving long-horizon tasks.
3. Extensive experiments show reasonable/good results regarding their claims and methods.

### Weaknesses
1. The long-horizon task seems to be divided into only 'grasp' and 'place' (from the paper and appendix), it is unclear if there are more sub-tasks / skills that the LLM divided. From the webpage, I find other tasks besides the pick-and-place series so wonder how to implement these.


### Questions
1. As the whole task is decomposed into stage 1, sequencing, stage 2, ..., stage n. Does it need to redesign the reward function of the RL process? Moreover, how does the sparse and dense reward influence the learning process?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In past works, people utilized LLM's internet-scale of knowledge to give robots sufficient information when planning for long-horizon tasks. However, the author believes that it is important for a robotic system to be capable of online improvement over at least low-level control policies at the same time. Otherwise, with the lack of a library for pre-trained skills in every other scenario, robots aren't able to learn very well. To this end, the paper proposes a framework, PLAN-SEQ-LEARN, that utilizes both LLM's ability to guide agent's planning and RL's ability for online improvement. The experiments show that not only did PSL's performance surpass SOTA visual-based RL methods through the help of LLM, but it also performed better than SayCan for its ability to improve with online learning.

### Strengths
**Motivation and intuition**
- Classical approaches to long-horizon robotics that can struggle with contact-rich interactions are convincing.
- Use LLM for high-level planning guiding RL policy to solve robotic tasks online without pre-determined skills.

​
**Novelty**
- The idea of utilizing RL to learn low-level skills under the framework of LLM planning is intuitive and convincing.
​

**Technical contribution**
- Integrates LLM task planning, motion planning, and RL techniques.
- Avoid cascading failures by learning online using RL algorithms.

​
**Clarity**
- The overall writing is clear. The authors utilize figures well to illustrate the ideas. Figure 2 clearly shows the whole idea of PSL.
- This paper provides a clear and detailed description of how to integrate the task planning module, motion planning module, and RL learning module.

**Related work**
- Give plenty of related works with short but clear descriptions.
​
**Experimental results**
- The overall performance on single-stage and multistage benchmark tasks is good.

### Weaknesses
 **Clarity**
- Although details of how LLM was used were clearly written inside Appendix D, I feel like the author could illustrate the details in the main paper and also a better explanation of how stage termination and training details are implemented. Since how LLM was involved in this work seems to be one of the contributions of this paper, I do feel like making this part intuitive is a must.


**Method**
- Trade-off: Planning without a library of pre-defined skills is mentioned as a strength in the paper, but this comes at the cost of relearning the whole process compared to other methods.
- Also the paper seems to overlook the fact that the learning might fail. Did not see how the method handles this situation.
- What would the PSL react to the situation when the agent failed to reach the termination condition?
- What would happen if there are more than enough terms for the LLM to choose from, for example, unlearnable skill terms that may confuse the LLM in choosing?


**Related work**
- Although Citing 'Inner Monologue' and 'Bootstrap Your Own Skills(BOSS)', they are not used for comparison or experiments, as these methods share many similarities. Therefore, it's a bit of a missed opportunity.


**Experimental conclusions**
- In section 4.3, the author noted that "For E2E and RAPS, we provide the learner access to a single global fixed view observation from O^global for simplicity and speed of execution, as we did not find meaningful performance improvement in these baselines by incorporating additional camera views.". However, this results in an unfair comparison because PSL has taken O^local as an additional input, and may cause some questionable issues. If performances are similar, I believe that adding O^local for E2E and RAPS would result in a more convincing conclusion that PSL performs better.

### Questions
As stated above.

### Soundness
3 good

### Presentation
3 good

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
The authors propose Plan-Seq-Learn (PSL) to address long-horizon robotics tasks from scratch with a modular approach using motion planning to bridge the gap between abstract language and low-level control learned by RL. The authors experiment with 20+ single and multi-stage robotics tasks from four benchmarks and report success rates of over 80% from raw visual input, out-performing previous approaches.

### Strengths
originality
The authors propose PSL: 1) breaks up the task into sub-sequences (Plan), 2) uses vision and motion planning to translate sub-sequences into initialization regions (Seq), 3) train local control policies using RL (Learn).

quality
Experiments show that the proposed method outperforms previous methods in simulation.


clarity
The paper is basically well-organized and clearly written.

significance
As an LLM-based approach, the authors have made some progress.

### Weaknesses
It is a paper about robotics. However, experiments are based on simulations only.

It is about long horizon robotics tasks. However, the largest number of stages is 5 in the experiments.

From the perspective of long horizon robotics tasks, it is not clear how the method may proceed forward. See detail below.

1.
"Large Language Models (LLMs) are highly capable of performing planning for long-horizon robotics tasks"
This is very arguable. There are evidences that it is not the case. And if it is so, there is no need to write the paper.

See e.g., 
On the Planning Abilities of Large Language Models--A Critical Investigation, 2023.
Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks, 2023

2.
"Language models can leverage internet scale knowledge to break down long-horizon tasks (Ahn et al., 2022; Huang et al., 2022a) into achievable sub-goals"
How valid is such claim? Why is it so? What if the tasks are not available or not frequent in Internet texts?

How can we guarantee the decomposition of tasks always work?
What if it does not work?
How can we guarantee the optimality of the decomposition of tasks?
What if it is not optimal?
The current work uses simulations to validate the proposed method. There will be sim2real gap. How to bridge such gap?

How to improve the current work? If there is something wrong in the task decomposition stage, it is hard or impossible to make improvements, and a pre-trained or fine-tuned LM may be called for. It is beyond the current work. However, the point is, it is not clear how the proposed method deal with such issues.


3.
End-to-end vs hierarchical approaches, there are tradeoffs. The paper focuses on the advantages of hierarchical approaches and disadvantages of end-to-end approaches. Desirable to discuss from both sides.

4.
"This simplifies the training setup and allowing the agent to account for future decisions as well as inaccuracies in the Sequencing Module." 
For some mistakes at the higher level, a lower level RL can not deal with.

5.
Table 2, Multistage (Long-horizon) results. 5 stages are not quite long-horizon, and the success rate may be as low as .67 ± .22

### Questions
1.
"Large Language Models (LLMs) are highly capable of performing planning for long-horizon robotics tasks"
This is very arguable. There are evidences that it is not the case. And if it is so, there is no need to write the paper.

See e.g., 
On the Planning Abilities of Large Language Models--A Critical Investigation, 2023.
Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks, 2023

2.
"Language models can leverage internet scale knowledge to break down long-horizon tasks (Ahn et al., 2022; Huang et al., 2022a) into achievable sub-goals"
How valid is such claim? Why is it so? What if the tasks are not available or not frequent in Internet texts?

How can we guarantee the decomposition of tasks always work?
What if it does not work?
How can we guarantee the optimality of the decomposition of tasks?
What if it is not optimal?
The current work uses simulations to validate the proposed method. There will be sim2real gap. How to bridge such gap? 

How to improve the current work? If there is something wrong in the task decomposition stage, it is hard or impossible to make improvements, and a pre-trained or fine-tuned LM may be called for. It is beyond the current work. However, the point is, it is not clear how the proposed method deal with such issues. 


3.
End-to-end vs hierarchical approaches, there are tradeoffs. The paper focuses on the advantages of hierarchical approaches and disadvantages of end-to-end approaches. Desirable to discuss from both sides.

4.
"This simplifies the training setup and allowing the agent to account for future decisions as well as inaccuracies in the Sequencing Module." 
For some mistakes at the higher level, a lower level RL can not deal with.

5.
Table 2, Multistage (Long-horizon) results. 5 stages are not quite long-horizon, and the success rate may be as low as .67 ± .22

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
