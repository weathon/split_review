# SELU: Self-Learning Embodied MLLMs in Unknown Environments

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Recently, multimodal large language models (MLLMs) have demonstrated strong visual understanding and decision-making capabilities, enabling the exploration of autonomously improving MLLMs in unknown environments. However, external feedback like human or environmental feedback is not always available. To address this challenge, existing methods primarily focus on enhancing the decision-making capabilities of MLLMs through voting and scoring mechanisms, while little effort has been paid to improving the environmental comprehension of MLLMs in unknown environments. To fully unleash the self-learning potential of MLLMs, we propose a novel actor-critic self-learning paradigm, dubbed SELU, inspired by the actor-critic paradigm in reinforcement learning. The critic employs self-asking and hindsight relabeling to extract knowledge from interaction trajectories collected by the actor, thereby augmenting its environmental comprehension. Simultaneously, the actor is improved by the self-feedback provided by the critic, enhancing its decision-making. We evaluate our method in the AI2-THOR and VirtualHome environments, and SELU achieves critic improvements of approximately 28\% and 30\%, and actor improvements of about 20\% and 24\% via self-learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This submission proposes SELU, an implementation of the actor-critic idea into MLLMs. This framework consists of a critic MLLM and an actor MLLM. They are trained and improved iteratively with online environment interactions. Experiments on VirtualHome and AI2-THOR demonstrate competitive performance.

### Strengths
- The paper is clearly presented and easy to follow.
- The idea is straightforward and seems effective.
- Strong and competitive performance.

### Weaknesses
- The proposed framework is not novel. At its core it's a combination of different techniques which are originally adopted under RL context, such as the actor-critic framework and hindsight relabeling.
- Although authors claim the critic learning without any external feedback (e.g., reward) as a strength, I doubt the correctness of resulting critics. For actor-critic methods under RL context, the critic is usually updated with L2 loss between its value estimation and groundtruth. Otherwise, it can easily suffer from issues such as overestimation and hence hinder the actor learning. I can imagine the situation will become worse for MLLMs due to their hallucination.
- The submission claims "unknown environments". However, it's really not unknown per se. The evaluated environments are mostly indoor scenes, which are very common and familiar to LLMs. More practically, at L299 authors mention that MLLMs are first prompted to explore the environment, which really makes the tested environments not unknown.
- Evaluated tasks are too short-horizon with the maximum horizon being 10. Since the low-level action execution is abstracted away to MLLMs, ideally authors should compare on long-horizon tasks.
- Some details need to be clarified. For example, in table 6, what does it mean to evaluate critic but without critic (the third column)?

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work the authors contribute a self-improvement technique for embodied MLLMs, reminiscent of the actor-critic architecture in reinforcement learning, that does not rely on external human feedback or environmental rewards. Their proposed method (SELU) considers two separate MLLMs: an actor MLLM, responsible for generating action plans for the agent, and a critic MLLM, responsible for evaluating if trajectories are successful. The authors also propose to use hindsight relabelling on failed trajectories of the agent in order to improve the efficiency of the training of the critic. The authors evaluate SELU in two virtual environments across multiple physical tasks (e.g., pick up, open, break) and using two different MLLM models. The authors compare their approach against recently proposed methods for self-improvement of MLLMs and show a significant improvement in both task success evaluation (critic) and decision-making (actor). The authors also show an ablation study on the role of hindsight relabeling and self-asking for the performance of the method, as well as an hyperparameter analysis.

### Strengths
- **Originality**:
  - As highlighted by the authors in their related work section, there has been extensive work on embodied MLLMs in recent years. The authors distinguish their work by focusing on the self-improvement of these models, instead of relying on (expensive) human feedback signals or environmental rewards. In particular, the authors propose a new architecture that takes inspiration from the actor-critic method in reinforcement learning. Actor-critic methods have been extensively explored in the context of RL (e.g., [1], [2]). Actor-critic methods have also been explored in the past for LLM agents, (e.g., [3,4]), which reduces the novelty of the approach. Nonetheless, the use of hindsight relabelling to improve the efficiency of the training of the critic in MLLMs is, to the best of my knowledge, novel.

- **Quality**:
   -  The authors successfully explain in detail their actor-critic approach and positioning against other recent works in embodied MLLMs. The authors also extensively evaluate their approach against relevant baselines, considering multiple MLLM backbones and in multiple simulation environments. Additionally, the authors present an ablation study and hyperparameter analysis that give further support to the claims of the paper and the importance of both the self-reflexive critic and the hindsight relabeling proposed method.

- **Clarity**:
   - The current version of the work is quite clear (except some sentences, as discussed in "Questions") and without any major typos. The authors clearly describe their proposed approach. The figures and tables also also of high-quality and are easily interpretable. Same details in regards to the experimental evaluation are currently missing (see "Questions").

- **Significance**:
   - The authors highlight a significant improvement of the ability of MLLMs to act in unseen environments and the experimental results appear to support the claims of the paper. As such, this work can be of some significant value to practitioners in the field.

**References**: 

- [1] Schulman, John, et al. "Proximal policy optimization algorithms." arXiv preprint arXiv:1707.06347 (2017).
- [2] Haarnoja, Tuomas, et al. "Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor." International conference on machine learning. PMLR, 2018.
- [3] Zhang, Bin, et al. "Controlling Large Language Model-based Agents for Large-Scale Decision-Making: An Actor-Critic Approach." ICLR 2024 Workshop on Large Language Model (LLM) Agents.
- [4] Kim, Byoungjip, et al. "Prospector: Improving LLM Agents with Self-Asking and Trajectory Ranking." NeurIPS 2023 Foundation Models for Decision Making Workshop.

### Weaknesses
My main concerns with the current version of the work are the following:
- In the current version of the work, significant details regarding the evaluation are missing (see "Questions" for details). There is no description of the evaluation methodology of SELU and the baselines, which would fit quite naturally as another subsection of Section 5.1. As such, it is hard to understand what the evaluation metrics are and how they were computed, and thus the full significance of the results.
- The proposed method employs only a self-reflective supervision signal, i.e., the model itself generates the reward signals to train the policy of the agent (in the form of selecting the successful/unsuccessful trajectories to further improve the MLLMs). However, without any other external reward signal, I'm not convinced that SELU can be robust to potential hallucinations (see "Question" 2).
- No computational code to replicate the results was provided.

### Questions
- **1** - How does your actor-critic method compare to the other actor-critic approaches for LLMs [1,2]? What are the main differences between SELU and these works (beyond just the use of multiple modalities)?
- **2** - In Section 4.1. (page 4), the authors state that if the detection result of a trajectory is a "yes" then the trajectory is directly added to the critic fine-tuning dataset. But what if that "yes" is, itself, an hallucination from the MLLM? How can your model cope with incorrect data in the training dataset?
- **3** In Section 4.1. (page 5), the authors describe their hindsight relabeling procedure and state that the they extract the "verb" of the action directly from the instruction. What if the agent performs another action (due to, for example, exploration of his environment) in that trajectory?
- **4** - What exactly is an action plan $l_{a, t}? It appears to not be defined in the paper.
- **5** - Why are some of the baselines (SC, Self-Refine, LMSI) missing from Table 3 and Table 4? What are the performance of these methods in AI2-THOR and VirtualHome, respectively?
- **6** - Why does SELU not outperform the baselines in task success detection on the "Sit" task in the VirtualHome environment? There is no discussion of this result in the current version of the work.
- **7** - In Section 5.4., the authors claim that "In Open tasks, we find that the lack of hindsight relabeling directly leads to the disappearance for some instructions, which causes the declined performance of success detection and decision-making.". Can you clarify what this statement means?
- **8** - What is the size of the replay buffer/dataset collected by each agent across the evaluations of Sections 5.2 and Sections 5.3? Is it the same for all baselines?
- **9** - How exactly you evaluate the task success detection metric for the baselines? Do you employ the same test dataset for every baseline? If not, how can you make sure that the performance of the critics is not biased towards easier task succession cases for some models? How many evaluation episodes did you consider? Is it the same for every model?
- **10** - In Section 5.5. (page 10) the authors claim that "our results indicate that multiple iterations of fine-tuning do not consistently improve SELU's performance". Did you collect a novel dataset after each iteration? Or did you reuse the same dataset?
- **11** - Are the MLLMs (LLaVA and Qwen-VL) pre-trained? If so, on what datasets and where did you get the weights? If not, how did you train the MLLMs?
- **12** - Can the authors clarify what is a "step" in this environment? Additionally, what actions are available to the agent? What actions do the agents actually perform on the tasks?
- **13** - How do the authors promote the "exploration" of the environment by the agents? How many steps of exploration are available to each agent? Is the instruction list/objects for each task the same for all agents?

References:
- [1] Zhang, Bin, et al. "Controlling Large Language Model-based Agents for Large-Scale Decision-Making: An Actor-Critic Approach." ICLR 2024 Workshop on Large Language Model (LLM) Agents.
- [2] Kim, Byoungjip, et al. "Prospector: Improving LLM Agents with Self-Asking and Trajectory Ranking." NeurIPS 2023 Foundation Models for Decision Making Workshop.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Multimodal large language models (MLLMs) require external feedback from humans or the environment to improve decision-making capabilities in unknown environments. The authors propose a new self-improvement actor-critic-based method, primarily consisting of training the critic, prompting (self-asking and hindsight relabeling) for labels, and curating data for SFT the actor based on labels by the critic. This coupled method improves both environment comprehension and decision-making in the new environment. The authors ran experiments on AI2-THOR and VirtualHome environments with both LLAVA and Qwen-VL, with baseline comparisons and additional ablation studies. The results are promising.

### Strengths
1. The paper is clear and well-presented.
2. The experiments are thorough, and the ablation studies are informative. The authors also provide helpful analysis of the limitations and error modes.
3. The proposed method to couple comprehension and decision-making in an unfamiliar environment is interesting.

### Weaknesses
Just a few questions below.

### Questions
1. What do the error bars represent in Figure 3? Similarly, do you have uncertainty measurements (N/bootstrapped confidence interval) for those numbers reported in the tables? Adding those will help me or other readers interpret the numbers. 
2. In line 301, "we restrict the maximum step for all tasks to 10." Do all trajectories end with 10 steps, or are some trajectories shorter than 10 steps? I wonder whether ending early mixes in an implicit environment feedback of task success because the critic is conditioned only on the last frame.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new actor-critic self learning paradigm, i.e., SELU, for embodied MLLMs in unknown environments. SELU proposes to update both the actor and the critic, via in actor-critic fashion by self-asking. the authors evaluate the efficiency of the proposed method, in 2 simulation environments including AI2thor and virtual home.

### Strengths
The paper is well written. It is also a good idea to combine the topics like LLM-based agent and actor-critic style update.

### Weaknesses
The proposed method seems to be simple and not technically contributing. The experiments environments seem to be limited, some settings remain unclear to me (see below).

### Questions
1. For the environments, the author mentioned they “randomly sampled 2-3 objects for each type of task”. Can you further provide the details? Whether the object will be randomly replaced at the beginning of each epoch or not? How large is the internal state space, and action space of the environment? These information is useful to evaluate the performance of the agent.

2. the Figure 2 seems a little confusing to me. What does the yellow circles mean? what does the arrows in the critic part mean? why different trajectories are added in sequence? 

3. how do you perform the hindsight relabeling and find the actual task finished? In fig2, it seems the question to distinguish whether a trajectory is useful is to ask "which object is open", which seems to be hand-crafted and cannot be adapted to more complex tasks.

4. How long does it take to collect the dataset and updating for each experiment? By fine-tuning on so many data which is narrowly distributed, whether the MLLM will lost its capacity on general knowledge? Can you discussed the advantages and drawbacks of your method over RAG based method, which seems to be ignored in the related work section.

5. The proposed method SELU interact with the environment to collect 1k trajectories, while baseline (e.g., self-refine) is reported to interact 3 rounds before getting the final answer. How many data are LMSI used? I think it's important to ensure a fair comparison between baselines in terms of the number of interactions.

6. other methods that improves the LLM (MLLM) according to the interactions with the environments are omitted.

### Soundness
2

### Presentation
3

### Contribution
2
