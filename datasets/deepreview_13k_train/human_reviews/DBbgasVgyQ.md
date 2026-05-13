# Skill Discovery using Language Models

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
Large Language models (LLMs) possess remarkable ability to understand natural language descriptions of complex robotics environments. Earlier studies have shown that LLM agents can use a predefined set of skills for robot planning in long-horizon tasks. However, the requirement for prior knowledge of the skill set required for a given task constrains its applicability and flexibility. We present a novel approach L2S (short of Language2Skills) to leverage the generalization capabilities of LLMs to decompose the natural language task description of a complex task to definitions of reusable skills. Each skill is defined by an LLM-generated dense reward function and a termination condition, which in turn lead to effective skill policy training and chaining for task execution. To address the uncertainty surrounding the parameters used by the LLM agent in the generated reward and termination functions, L2S trains parameter-conditioned skill policies that performs well across a broad spectrum of parameter values. As the impact of these parameters for one skill on the overall task becomes apparent only when its following skills are trained, L2S selects the most suitable parameter value during the training of the subsequent skills to effectively mitigate the risk associated with incorrect parameter choices. During training, L2S autonomously accumulates a skill library from continuously presented tasks and their descriptions, leveraging guidance from the LLM agent to effectively apply this skill library in tackling novel tasks. Our experimental results show that L2S is capable of generating reusable skills to solve a wide range of robot manipulation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces an LLM-guided skill discovery framework for solving robotic tasks. For each given task, LLM decomposes into sub-tasks, and writes reward and terminate functions for the RL agent to learn the corresponding policy.

### Strengths
The skills are designed with parameters, which have the flexibility to be reusable for other tasks.

### Weaknesses
- L2S depends heavily on the accuracy of LLM-generated reward and termination functions. Without evolutionary search or some kind of verification method, I doubt the effectiveness of this method on new tasks --- the current success relies on the expert few-shot prompt enumerating successful termination conditions.
- Since the aim of the method is to solve given tasks by decomposing them into sub-tasks, "skill discovery" may not be proper here.
- The experimental scenarios are simple. It would be valuable if diverse environments were shown.
- The approach has only been evaluated in state-based environments, limiting its applicability in vision-based or real-world robotic settings without additional adjustments.

### Questions
- How is the baseline being compared? Is the "Listing 3 Additional environment knowledge" also available to those baselines? If not, the comparison would be far from fair for Eureka.
- How to generalize to new environments, e.g. what effort do users have to put in?

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
2

### Summary
The paper introduces **L2S (Language to Skills)**, a novel framework that utilizes large language models (LLMs) for skill discovery and reuse in robotics. Unlike prior approaches requiring predefined skill sets, L2S enables robots to autonomously generate skills from task descriptions, defined by LLM-generated dense reward functions and termination conditions. Each skill is parameter-conditioned to adapt across a range of conditions, with suitable parameters chosen during training of subsequent skills. This adaptive approach mitigates the challenge of incorrect parameter settings.

L2S builds a skill library progressively as it encounters new tasks, allowing it to efficiently tackle novel tasks by reusing previously learned skills. Experimentally, L2S demonstrates superior performance on sequential robotic manipulation tasks compared to baseline methods, achieving faster convergence and higher success rates in complex, multi-step tasks in *LORL-Meta-World* and *ManiSkill2* environments.

### Strengths
- The proposed framework, which involves training a set of primitive skills and planning on top of them, is novel.
- The performance improvements over previous state-of-the-art methods, such as T2R(Xie et al., 2023) and Eureka(Ma et al., 2023), are significant, particularly for tasks in the ManiSkill2 environment.
- The reusability of learned skills facilitates faster learning for downstream tasks, as demonstrated notably in the PickCube and StackCube tasks. The explanation behind these results is clear and intuitive.

### Weaknesses
 - **Questions about the Parameters**

    Based on my understanding, the parameters for each skill play a crucial role in both the reusability of learned skills and in chaining these skills to solve tasks. However, certain aspects remain unclear, raising concerns about the generalizability of the proposed framework. I have the following questions:

    - **Who determines the semantic meaning of the parameters?**
      
        In the *“turn faucet left”* task, one possible semantic meaning of a parameter could be the distance to the handle. My question is: who chooses this dimension? Is it determined by a human or by the language model (LLM)? If decided by the LLM, what happens if the LLM produces unhelpful dimensions? Do you have any mechanism to prevent this from happening? For instance, the semantic dimension could be something less-related for solving the task, like the rotation of the handle or its distance from the ground. In such cases, trying out different parameters for parameter-conditioned policy might not accelerate training but could instead decrease sample efficiency. Additionally, could you clarify how the total number of parameters for each skill is determined and how this might impacts the training speed of L2S? I think including these details in the paper would be beneficial for better understanding.

    - **How is the parameter range chosen for the experimental results in Section 4?**

        According to the paper, the parameter distributions must be specified by the user. However, it seems challenging to determine the optimal mean and variance for training skills efficiently, especially since users need to specify these values prior to training. How can a user accurately define the parameter range before training begins?
        
        I understand that L2S can select the best values from the provided distribution during training using Equation (2) in line 305, even if the distribution is not perfectly chosen. However, I believe that choosing the right distribution would significantly reduce the sample needed to reach a certain performance level during training. Since the experiments section lacks detailed information on how the specific distributions \( q_{\phi_k} \), even though this choice greatly impacts training speed, I wonder how these distributions were chosen. I have a concern that if the distribution is chosen manually to have high mean and low variance distrubition around the ground-truth(or best performing) value, we have a possibility that increased training speed partly comes from this. 

- **Minor Corrections**
    - *Line 230-232:* The term *“processes”* is somewhat vague and colloquial, making it difficult to understand precisely what it refers to.
    - *Line 374:* Instead of *“converged,”* it might sound more natural to say *“the task is considered solved”* or *“the policy is considered converged.”*
    - *Figure 5:* Adding standard deviation would be helpful.

### Questions
Questions are provided in the weaknesses section. Please address these questions if possible!"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes L2S (Language to Skills) to leverage LLMs to decompose tasks into reusable skills with parameterized rewards and termination conditions​. With parameterized rewards and termination conditions, L2S can train parameter-conditioned skill policies and then autonomously accumulates a skill library for guiding continual skills learning.

However, the high-level idea of L2S is almost the same as a previous ICLR LLMAgent Workshop paper [1]. It limits the contribution of this paper. Also, this paper even didn't cite the previous paper. **The author needs to give sufficient explanation to show that it's just inadequate reference or any more serious problem.**

[1]. Li et al., LEAGUE++: EMPOWERING CONTINUAL ROBOT LEARNING THROUGH GUIDED SKILL ACQUISITION WITH LARGE LANGUAGE MODELS, 2024

### Strengths
1. Skill reuse between tasks can enhance the training efficiency for continual learning on new tasks.

2. Decompose tasks into smaller reusable skills reduce the difficulties to generate multi-stage dense rewards and enhance training efficiency.

3. The experimental results show that L2S not only solves continuously presented tasks much faster but also achieves higher success rates compared to state-of-the-art methods.

### Weaknesses
1. The high-level idea of this paper is almost the same as a previous ICLR Workshop paper [1]. League++ integrates LLMs, Task and Motion Planning (TAMP), and RL to guide continual skill acquisition through task decomposition, reward generation, and continual learning with skills library. Then, League++ can do autonomous training for long-horizon task and enhance training efficiency in other tasks. The overall ideas and contributions are very similar to L2S. However, This paper even didn't cite League++. **The author needs to give sufficient explanation to show that it's just inadequate reference or any more serious problem.** Anyway, the author needs to highlight the difference and show the novelty of this paper. On the other hand, Gen2Sim [2] is also utilizes LLMs to do task generation, task decomposition, and reward generations for skill learning. Please add more related work.

2. In the previous work Text2Reward [3], the reward generation requires human-in-loop training for generating better rewards. Although L2S uses methods similar to Text2Reward, this paper didn't show anything about it. It's unclear how L2S addresses the challenge of generating usable reward functions in a single attempt, given that Text2Reward often requires iterative refinement with human input to produce effective rewards. The paper should provide more details on how it achieves one-shot reward generation, especially considering the complexity of reward functions.

3. In the previous work Text2Reward [3], the generated reward code can be incorrect. As shown in the table 7 of this previous paper, the success rate is just 90%. Since L2S will generate several reward functions for different skills, the failure rates will exponential growth. (For example, if you have five skills, the success rate will be 90%^5=59%, which is pretty low) This paper didn't show how do they resolve this problem. Adding more explanations and ablation studies is helpful.

4. It's not convincing that only optimize the last skill parameters is enough. (For example, you have a task with three skills: open the cabinet, pick a hammer, and place the hammer to the cabinet. If the cabinet is not opened far enough, you cannot place the hammer successfully. At the moment, you need to update the parameters and termination of the first skill, not the last skill.) Some previous work refine all the skills start from the beginning.

5. The most long-horizon task in the experiments only has three stages: OpenDrawer, PlaceCubeDrawer and CloseDrawer. Since the idea for task decomposition and skill library are designed for long-horizon tasks, more experiments on them should benefit.

### Questions
1. In the previous work Text2Reward [1], the reward generation requires human-in-loop training for generating better rewards. It's hard to generate usable reward functions in one-shot. Although L2S uses methods similar to Text2Reward, this paper didn't show anything about it. How can you generate usable reward codes in one shot?

2. The comparison with Eureka [2] is confused for me. Different from T2R, Eureka is a two-stage method, which learns a dense rewards at first and then use it for RL training. How do you compare the training efficiency directly? Also, why the performance of a single skill like OpenDrawer is pretty low? (It shows great performance in much more complex tasks.)

3. The potential assumption of the skill library is that the similar skills' semantic description are similar. It's might be a correct assumption that skill with similar semantic description can be reused. However, it might not be sufficient. How about those skills have similar motions? (like place and insert might have similar motion somehow) How can we utilize them as reuse skills?

If the author can address those limitations and give enough explanation to the novelty, I will consider improve my score.

[1]. Xie et al., TEXT2REWARD: REWARD SHAPING WITH LANGUAGE MODELS FOR REINFORCEMENT LEARNING, 2024

[2]. Ma et al., Eureka: Human-Level Reward Design via Coding Large Language Models, 2024

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an approach called  Language2Skills that decomposes a natural language task description into reusable skills.  Each skill is defined by an LLM generated dense reward function, which can be used for skill policy training. L2S aims to make it easier for RL practitioners to develop reward and termination functions for training RL agents in multi-step problems.

### Strengths
- The proposed method is a novel extension of previous works like T2R and Eureka to the multi-step setting, which was a nontrivial extension due to the dependencies between skills which required an additional optimization step. 

- The results show that the proposed method (L2S) outperforms those baselines in many multi-step RL problems. 

- The problem formulation and method/algorithm were clearly described and mathematically precise.

### Weaknesses
 - The abstract was somewhat difficult to understand. Specifically the following sentence: “To address the uncertainty surrounding the parameters used by the LLM agent in the generated reward and termination functions, L2S trains parameter-conditioned skill policies that performs well across a broad spectrum of parameter values.” — What are the parameters being referred to here? Why is there uncertainty over them? I was able to understand the abstract after reading the paper, but it wasn’t a strong introduction to the material.

- I’m not following the author’s critique of existing skill chaining literature: “For example, learning a skill π1 to move an object towards a goal region cannot be learned well before mastering the skill π2 for object grasping, but skill chaining would require learning π1 first”. Why is this the case? Since all learning is done in a simulator, presumably the block could simply be initialized in the hand for training π1 before training π2.

- No error bars in figure 5 and no statistical analysis for any of the results.

- It looks like getting this to work required a considerable amount of task-specific prompt engineering. I’m concerned that such a system is not able to generalize to new tasks without significant additional “tips and tricks” added into the prompt:
“1.) Tasks about moving mug are considered successful when mug is moved at least 0.1 meter towards the correct direction compared with the object's initial position. 2.) Tasks about turning faucet are considered successful when faucet is turned at least np.pi/4 radian towards the correct direction compared with the object initial position. 3.) Tasks about opening or closing drawer are considered successful when drawer box is fully open or fully closes. Drawer fully open means drawer box position is smaller than -0.15 meter. Drawer fully closed means drawer box position is greater than -0.01 meter.“ 
I’m concerned that the trial-and-error process required to create these sorts of prompts might be more difficult than directly writing the reward and termination functions.

- There is no supplementary code, as encouraged by ICLR, which makes reproducibility difficult to assess.

Grammatical Issues:

- Abstract: "Large Language models (LLMs) possess remarkable ability" should be "Large Language Models (LLMs) possess a remarkable ability" (article "a" is needed before "remarkable ability").

- Abstract: "short of Language2Skills" should be "short for Language2Skills.”

- Page 1: "However, it is known prone to inefficient task decomposition..." should be "However, it is known to be prone to inefficient task decomposition...” known prone -> known to be prone

- Page 2: "L2S adopts a strategy of training a skill policy that performs well across a broad spectrum of parameter values and select the most suitable parameter value during the training of subsequent skills." select -> selects

- Page 2: "turn fauccet left" -> "turn faucet left”

- The assumption that each skill only depends on the skill after it is a strong one, and it is not clear that this assumption will hold in many real-world tasks. The fact that “optimizing the parameters of all prior skills simultaneously can degrade the performance of some skills” is a limitation of this particular method on tasks where the assumption doesn't hold. This should be listed as a limitation.

- The extensive prompt engineering required to get this system to work should be listed as one of the limitations. For example, the success condition “Tasks about moving mug are considered successful when mug is moved at least 0.1 meter towards the correct direction compared with the object's initial position” is an extremely task-specific piece of context.

### Questions
- In section 3.2 the authors state that they do few-shot prompting with examples, pointing to Appendix E for details. However, I don’t see any examples in Appendix E. Appendix F is titled “Examples of Reward Functions and Termination Condition Functions”, but it seems like those are examples of the LLM output rather than examples used in the prompt?

- How are the “user-selected” variances for the skill parameters determined? Wouldn’t the variances be task and subtask-specific? I would imagine if the variances are too big, the policy may not learn anything and if the variances are too small the skill would not generalize. 

- In equation 1, wouldn’t optimizing \phi_{i-1} and \varphi_{i-1} potentially lead those variables to be out of distribution for the frozen policy \pi_{i-1}?

- In the unnumbered equation between equations 1 and 2, how do you handle policies that don’t terminate? It looks like i(\tao, \beta) is undefined in that case. Is there an implicit assumption that all policies will eventually terminate? How is that enforced?

- Why make the assumption that the parameters for each skill only depend on the skill after them? What if there are constraints across non-adjacent skills in the chain? For example, if the fingers needed to be closed to push a button, the sequence may be 1.) move to button, 2.) Close fingers, 3.) Push button. However, the “move to button” parameters could not be changed when training the push button skill.

- Why optimize the parameters and the policy separately in an iterative process rather than together?

Overall, the paper introduces a novel and interesting approach with favorable comparisons to baselines. I would be happy to increase my score if the authors address my questions, include error bars or statistical analysis in their comparisons, improve readability, and provide code for reproducibility.

### Soundness
3

### Presentation
2

### Contribution
3
