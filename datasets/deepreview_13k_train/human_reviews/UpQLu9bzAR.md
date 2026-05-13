# VICtoR: Learning Hierarchical Vision-Instruction Correlation Rewards for Long-horizon Manipulation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We study reward models for long-horizon manipulation tasks by learning from action-free videos and language instructions, which we term the visual-instruction correlation (VIC) problem. Recent advancements in cross-modality modeling have highlighted the potential of reward modeling through visual and language correlations. However, existing VIC methods face challenges in learning rewards for long-horizon tasks due to their lack of sub-stage awareness, difficulty in modeling task complexities, and inadequate object state estimation. To address these challenges, we introduce \projectname{}, a novel hierarchical VIC reward model capable of providing effective reward signals for long-horizon manipulation tasks. \projectname{} precisely assesses task progress at various levels through a novel stage detector and motion progress evaluator, offering insightful guidance for agents learning the task effectively. To validate the effectiveness of \projectname{}, we conducted extensive experiments in both simulated and real-world environments. The results suggest that \projectname{} outperformed the best existing VIC methods, achieving a 43\% improvement in success rates for long-horizon tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a hierarchical reward model that provides reward signals for long-horizon manipulation tasks. First, It proposes using a Task Knowledge Generator to decompose a task into stages and identify the necessary object states and motions for each stage. It then adopts a Stage Detector to detect the stage and object states given the visual observations. Finally, with a Motion Progress Evaluator that assesses motion completion within stages, the framework gives the overall reward for the long-horizon task. While the task knowledge generator leverages LLMs, the other parts are trained solely on primitive motion demonstrations. The paper shows that their proposed framework produces better rewards for long-horizon manipulation tasks, thus facilitating policy learning with methods such as PPO.

### Strengths
+ The approach explores how to leverage LLMs for providing task decomposition for long-horizon manipulation tasks by defining stages and motions as the task hierarchy. And it seems that LLMs such as GPT-4 work well for this setup.
+ The design of the modules sounds reasonable, i.e., leverage MDETR for stage and object status detection and leverage CLIP for motion progress evaluator. The training losses are well-motivated. The results are good.

### Weaknesses
 - The long-horizon tasks used to evaluate the proposed framework are a bit limited, e.g., even compared to a popular benchmark [1] proposed in 2020. A more diverse set of tasks would help to fully verify the usefulness and adaptability of this approach.

 - The lack of ablation studies for the three contrastive losses used in training the motion progress evaluator makes it difficult to assess the individual contribution of each loss to the overall reward quality.

 - The paper does not adequately discuss the relationship between the proposed motion decomposition and similar concepts used in prior work [2]. Specifically, it is unclear whether the approach could be applied at a more granular motion level, such as the subskills used in the Move Chair task in [2].

### Questions
+ I didn't find ablation studies of the three contrastive losses used in training the motion progress evaluator. It would be better to know their contributions to the overall quality of the generated reward.
+ The proposed approach utilizes motion decomposition of subtasks, a concept similar to the ones used in [2]. It would be helpful to add a discussion about it. In particular, I wonder will the proposed approach also works well at a potentially more granular motion level (e.g., a subskill in the Move Chair task in [2]).

[2] Chain-of-Thought Predictive Control

### Soundness
2

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
This paper proposes a method called VICtoR that utilizes LLM (GPT-4) and VLM (CLIP) to calculate the task rewards for long-horizon robotic manipulation. Specifically, it decomposes the language instructions to different stages with the help of GPT-4, and uses MDETR to detect objects and classify their states. Comparing the states with the desired states from GPT-4, the algorithm can determine if the stage has been completed. For the motions inside each stage, VICtoR trains the CLIP encoders with multiple contrastive losses to learn the task progress corresponding to the instruction. Combined with the above reward, a model is trained with self-constructed benchmarks and shows better performance compared to multiple baselines.

### Strengths
1. The method is intuitive. Decomposing a long-horizon task with LLM and utilizing VLM for the short-term progress evaluator are both reasonable and have been validated in previous works.
1. The visualizations are intuitive. I can easily get the idea of most figures and they help to understand the paper. The reward curves and t-SNE graph prove the effectiveness of the proposed reward design and contrastive loss designs.
1. The results shown in the paper are good, compared to other baseline methods.

### Weaknesses
1. The technical novelty is relatively limited. The proposed method mainly has two parts, LLM for decomposing the long-horizon task and CLIP for the short-term progress evaluator. These two parts have both been extensively explored. There have been multiple related works mentioned in the paper. Even in Line 186, the authors acknowledged that the differences are relatively nuanced. The combination of LLMs and VLMs for robotic tasks is becoming increasingly common, and the specific contribution of this work beyond a straightforward combination is not entirely clear. The use of contrastive losses with CLIP, while effective, is also not a novel concept in itself, and the paper needs to better articulate how the specific design of these losses contributes to the overall performance gains.

2. The experiments are conducted on a self-collected dataset, not the widely adopted CALVIN benchmark. As mentioned in Line 343-346, the proposed method has critical limitations when dealing with some meticulous actions like rotations. This reliance on a custom dataset makes it difficult to compare the method's performance against existing state-of-the-art approaches on a standardized benchmark. The lack of evaluation on CALVIN, which includes more complex manipulation tasks and a wider range of object interactions, raises concerns about the generalizability of the proposed method. The limitations regarding rotation actions, which are common in many manipulation tasks, further restrict the applicability of the method in more complex scenarios.

3. Some technical details are confusing and need further clarification. Please see the questions part below.

4. Minors. Typo in Line 143 (as as)

### Questions
1. Line 160, how are the objects states autonomously annotated during real-world experiments?
1. Line 205-208, What if the object detector fails? Will using cropped images for object states classification have certain problems? For example, some object states are positional relationships that need a larger visual field to accurately determine them. What is the model structure for the classifier P?
1. Line 471, why the curves are called ``potential curves''? Are the rewards calculated with collected videos? Do you use the rewards for action rollouts?
1. How do you deal with the long inference time of LLM, when you are training the policy with the proposed design?

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
4

### Summary
This paper introduces a hierarchical vision-instruction correlation method to estimate rewards for long-horizon robotic manipulation tasks. Specifically, the approach initially identifies task-aware objects and employs GPT-4V to associate the object status with the corresponding motion stage. Additionally, this paper proposes a contrastive learning-based method that evaluates the reward of visual observations by calculating the similarity between visual observations and language instructions. Experimental results validate the efficacy of this method.

### Strengths
1. This paper proposes a hierarchical reward estimation method to provide vision-based reward for long-horizon manipulation tasks.
2. This paper describes this method clearly.
3. The simulation and real-world experiments prove the effectiveness of this method.

### Weaknesses
1. The method requires lots of relevant data for estimating visual object information, which makes it struggle to generalize to new task scenarios due to reliance on the object status classifier. Could this method generalize to any novel task? 

2. The comparison results are unfair. This method utilizes the robotic manipulation videos of the same tasks to train the contrastive learning method, while the compared methods such as LIV are pretrained encoders.  Would these vision-language correlation methods achieve comparable results when the encoder is fine-tuned on the target tasks?

3. The conservative learning method for vision-language reward estimation is common. The stage and motion detection method seems to simply achieve state-based rewards through visual models by overfitting on specific manipulation tasks.

### Questions
Please refer to the weakness.

My questions are:
1. Could this method generalize to novel tasks?
2. Could other methods achieve comparable results when fine-tuned on the target task?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes VICtoR, a hierarchical reward model for long-horizon manipulation tasks that learns from action-free videos and language instructions. The proposed approach addresses challenges in task complexity, sub-stage awareness, and object state estimation through a stage detector and motion progress evaluator. VICtoR outperforms existing models by using a novel stage detector and motion progress evaluator, achieving a 43% improvement in success rates for complex tasks.

### Strengths
- The paper effectively advances research by integrating LLMs for high-level hierarchical planning, which allows the model to assess the robot’s progress at each step.
- It incorporates an innovative approach to extract relevant information from short video clips, enabling the system to understand key aspects of the task without viewing the entire sequence.
- The methodology section is well-structured, clearly outlining the three core components of the proposed approach, aiding reader comprehension.
- Results in the experiments section demonstrate substantial improvements over previous methods in complex task settings, showcasing the effectiveness of the hierarchical framework.
- Reward visualizations effectively illustrate the approach’s ability to accurately assess performance.

### Weaknesses
 - A more thorough evaluation of each individual component would clarify its contribution to the overall system’s performance.
- Additional evaluations on zero-shot capabilities, specifically with unseen trajectories, would be valuable in understanding the approach’s generalization.
- The paper lacks an assessment of the computational cost and resource requirements of the proposed method.
- The reliance on GPT-4 could pose potential challenges, which are not thoroughly addressed; analyzing GPT-4 outputs in greater detail could reveal possible limitations.
- A comparative discussion of other methods for long-horizon manipulation, such as hierarchical reinforcement learning (HRL) and task and motion planning (TAMP), is missing and would have enriched the analysis.
- While the authors mention using data from XSkill3 for real-world experiments, they do not provide sufficient details on the dataset’s size, diversity, or the types of tasks involved.

### Questions
Refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
