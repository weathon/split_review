# SRSA: Skill Retrieval and Adaptation for Robotic Assembly Tasks

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Enabling robots to learn novel tasks in a data-efficient manner is a long-standing challenge. Common strategies involve carefully leveraging prior experiences, especially transition data collected on related tasks. Although much progress has been made in developing such strategies for general pick-and-place manipulation, far fewer studies have investigated contact-rich assembly tasks, where precise control is essential. In this work, we present SRSA (Skill Retrieval and Skill Adaptation), a novel framework designed to address this problem by utilizing a pre-existing skill library containing policies for diverse assembly tasks. The challenge lies in identifying which skill from the library is most relevant for fine-tuning on a new task. Our key hypothesis is that skills showing higher zero-shot success rates on a new task are better suited for rapid and effective fine-tuning on that task. To this end, we propose to predict the transfer success for all skills in the skill library on a novel task, and then use this prediction to guide the skill retrieval process. Through extensive experiments, we demonstrate that SRSA significantly outperforms the leading baseline, achieving a 22\% relative improvement in success rate, 3.7x higher stability, and 2.4x greater sample efficiency when retrieving and fine-tuning skills on unseen tasks. Moreover, in a continual learning setup, SRSA efficiently learns policies for new tasks and incorporates them into the skill library, enhancing future policy learning. Additionally, policies trained with SRSA in simulation achieve a 90% mean success rate when deployed in the real world. Please visit our project webpage at https://srsa2024.github.io/ for videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Skill retrieval and Skill Augmentation (SRSA) tackles the problem of quickly learning new tasks in task family. In the paper, the authors consider various insertion tasks from the AutoMate benchmark which share the same observation space, action space and reward function. The tasks differ in the geometries and thereby the transition dynamics and expert actions required.

The authors assume that an availability of a skill library containing expert policies for different insertion tasks. Skill retrieval is based on geometry similarity, transition dynamics and expert actions. Transition dynamics and expert actions are based on reverse trajectory generation. The similarity is predicted using a learnt function F, which is a 0-shot policy transfer success rate predictor trained on existing skill library. Given a new task, the policy with the highest 0-shot transfer prediction is used extracted and fine-tuned on the new task using Reinforcement Learning (PPO) with additional Self Imitation Learning (SIL) objective.

### Strengths
1. Strong simulation results
2. Insightful that we can train a 0-shot transfer predictor function using geometry, transition and expert action encodings
3. Results transfer to real robot

### Weaknesses
1. Assumption that that all tasks have the same observation space, action space and reward function
2. Based on Fig. 6 and Appendix Fig.16, it seems SRSA-geom is very comparable to SRSA. Hence, it seems geometry based skill retrieval might be sufficient. It's also easier as it doesn't require to collect disassembly trajectories and training a 0-shot transfer predictor function

### Questions
Should F use as input the success rate of the expert policy in the original task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the problem of learning to solve new assembly tasks efficiently while utilizing solutions to previously solved tasks (previously solved assembly problems). This paper achieves this using a skill retreival and adaptation approach. First, the paper assumes that there exists N set of skills where each skill can solve a particular assembly task (particular CAD model).  To solve a new task, it tries to retrieve the most similar previous CAD from the previous set of skills. This retrieval problem is solved by using a heuristic which assumes that two CADs are similar if the policy from source zero-shot solves the second task (or gives high reward in dense reward settings). This retrieval problem is used to construct a dataset to find similar tasks. This dataset is used to learn an embedding which can predict if the CAD models are similar or not (using labels from the reward heuristic).

Now for a new incoming task (or new CAD model), the best existing skill is extracted (using the learned embedding). This skill is then refined using RL. This library can then be used in a naive continual learning setting.

### Strengths
The paper is well written and easy to follow. Most of the proposed approach makes sense, the experimental results along with the ablations show good performance of the proposed approach.

### Weaknesses
 *Generality:* Unfortunately, I don’t think this approach is very general. This seems a bit too tailored for assembly tasks. This  paper might fit a robotics venue much better and would probably be appreciated more in that setting. However, this is not my decision and I don’t think this should in any way count as a negative for the paper.

*Sparse reward setting:* The retrieval approach cannot work if we are in sparse reward settings, since there can be some CAD model for which no other skill transfers 0 shot. How would this approach solve this problem? This is definitely very relevant for real-world setting where dense rewards can be quite hard.

*Generalist approach (ablation):* Do you have any intuition on why the generalist approach fails? Would better feature learning or better multi-task policies help a generalist approach. Clearly, a generalist policy trained on all tasks is way more appealing. Also, curious to hear any thoughts on why the generalist policy does not perform well on all tasks. Is this because some of the assembly tasks can be very different?

*Learning embeddings for retrieval:* Given that there are less than 100 samples to learn the embedding function which uses high-dimensional input (such as point cloud embeddings). Did you find any challenges in learning this function. 

*Reward heuristic:* While the simulation lemma is used as a motivation for the reward heuristic to be used in a zero-shot setting, I think there is a difference here. If two MDPs share same transition dynamics and initial state distributions then same policy will give high rewards for both. But this does not necessarily go the other way around, i.e., one policy can gives high rewards for two MDPs *does not* mean that they share similar T and S_0. I think this is an important point that should be clarified in the paper. Thus, the use of transfer should be seen as a heuristic and not a theoretical justification.

### Questions
see above

### Soundness
3

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
This paper introduces a method for more effective learning of RL policies for robotic assembly tasks. It first uses Skill Retrieval to retrieve the most relevant policy from the skill library, a set of available policies that solve similar types of tasks. The retrieval is done based on the predicted zero-shot transfer success rate using object geometry, dynamics and expert-action features. The retrieved policy is then fine-tuned on the new task, facilitating more efficient learning when compared to learning to solve this task from scratch. The authors also showcase how their method could be used for continual learning by progressively expanding the skill library. The experiments show improved performance when compared to baselines, while the ablation studies provide valuable insights about the proposed method.

### Strengths
- Paper is well written and motivated.
- The proposed method is simple, elegant and easy to understand.
- Using geometry, dynamics and expert-action features for retrieval is a nice idea that incorporates different aspects of the underlying tasks.
- Experiments are conducted well and the ablation studies provide valuable insights into the method.
- Real-world experiments are appreciated.

### Weaknesses
 - Line 217 - what does being similar with a high value mean? Maybe this sentence could be rephrased for clarity.
- Equations could be formatted better (e.g. not to overflow) and also it would be useful if they were numbered and referred to in the text when needed.
- References to the Appendix are broken as it's a separate file. This, I believe, will be addressed for the camera-ready version, just wanted to point it out.
- Using zero-shot transfer success rate as a proxy for retrieval is intuitive, but, I believe, it doesn’t accurately reflect the expected value for tasks with dense rewards. Could authors provide more details as to why using a zero-shot transfer success rate is sufficient? Would it be beneficial to use additional metrics as well?
- If the difference in expected value when applying the same policy to different tasks depends only on their difference in transition dynamics and initial state distributions that are captured by geometry, dynamics and expert-action features, why do you need to approximate the zero-shot transfer success rate at all? Wouldn't comparing these features using some distance metric be enough? Maybe authors could do some experiments on this or justify why such an approach is not appropriate.
- Relying on disassembly paths seems to restrict the method’s applicability to simple insertion tasks on a plane. Could the authors more clearly point out such a limitation and/or propose solutions to it in the paper?
- In a supervised learning setting, the loss function is usually positive. Why the objective function (line 287) is negative?
- Referring to different tasks in the experiment section using their ID number (e.g. 01125) doesn’t provide any information as to why they are hard or easy. Adding some text or image information about these tasks would benefit the understanding of the experimental results.
- In the experiments, improvements in the success rate over the baselines are provided in percentage points, which can be hard to understand given that success rate can also be expressed in percentages. For example, does a 22% increase mean a +22% or 22% increase when compared to the base? This is especially strange when seeing an 181% increase (given that the success rate is capped at 100%). Maybe the authors can clarify that, or (as I would encourage) use a different metric.
- It would be beneficial to discuss the main difference between the proposed method and the AutoMate baseline (not including the retrieval part). It would then be easier to understand the experimental results (e.g. AutoMate’s instability, line 427).
- The paper would benefit from a discussion on using visual observations, rather than object poses, and whether the proposed method would be better than fine-tuning a generalist policy that would have the capacity to generalise implicitly. 
- It would also be interesting to see whether fine-tuning or learning a residual on top of the retrieved policy is more efficient. Although, this might be outside the scope of the current approach.

### Questions
See the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
