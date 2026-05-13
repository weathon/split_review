# Task-Unaware Lifelong Robot Learning with Retrieval-based Weighted Local Adaptation

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Real-world environments require robots to continuously acquire new skills while retaining previously learned abilities, all without the need for clearly defined task boundaries. Storing all past data to prevent forgetting is impractical due to storage and privacy concerns. To address this, we propose a method that efficiently restores a robot's proficiency in previously learned tasks over its lifespan. Using an Episodic Memory (EM), our approach enables experience replay during training and retrieval during testing for local fine-tuning, allowing rapid adaptation to previously encountered problems without explicit task identifiers. Additionally, we introduce a selective weighting mechanism that emphasizes the most challenging segments of retrieved demonstrations, focusing local adaptation where it is most needed. This framework offers a scalable solution for lifelong learning in dynamic, task-unaware environments, combining retrieval-based adaptation with selective weighting to enhance robot performance in open-ended scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an imitation learning approach that enables a single network to learn from demonstrations of multiple tasks. It uses a vision language model and a local weighting mechanism to adapt the network towards the target task. The agent performs a few rollout episodes to assess policy performance, using this feedback for automatic selective weighting by comparing the rollouts with retrieved demonstrations without human intervention. The policy is subsequently adjusted to better align with the desired demonstrations.

### Strengths
1. The key idea has some merit, with some analogues to meta-learning approaches
2. The related work is an interesting compilation of papers
3. Figure 3 is well-illustrated, aiding in the exposition of the paper's ideas.
4. PCA Visualization based on SS Model is quite interesting (Figure 4b)

### Weaknesses
1. I have concerns regarding the overall presentation of the paper. While the idea holds merit as a novel imitation learning approach, the contributions are significantly overstated. In fact, I would argue that the paper does not fully address a lifelong learning setting. The authors should consider moderating their claims and clearly articulating the scope of their contribution.
2. Many keywords are mentioned but not defined. For instance, what is meant by lifelong learning in this context? Evaluating a lifelong learning agent over only 20 episodes, as done by the authors, seems insufficient and misaligned with the intended concept.
3. The discussion on unspecified task boundaries in real-world scenarios is also unclear and mischaracterized. Although the paper replaces a one-hot task encoding with an embedding from a vision-language model, this essentially still provides a form of task specification, albeit in a more implicit or 'fuzzy' manner. 
4. The related work section omits many papers that are highly relevant to the context. While the authors do include a few key references, surprisingly, there isn’t a single paper cited from more than five years ago. I'd recommend the authors to look at the following: [1-6]
5. There is no comparison of the concepts to meta-learning approaches such as [2]. I would argue that their approach resembles having a global network that is fine-tuned to the desired task during testing.
6. The description of the experiments and their results is vague and difficult to follow. While I am confident that the authors are skilled and fully understand their work, I encourage them to consider readers like myself, who may be less familiar with it, by providing a more detailed explanation of their setup. For example, what specific tasks are being solved? Are the demonstrations focused on particular tasks? Does each task in the testing phase have a corresponding relevant demonstration?
7. While the authors claim lifelong learning is important—a sentiment I share—it is unclear why their chosen evaluation setup suits this purpose. They could provide stronger justification for their design choices.

### Questions
1. Please refer to the weaknesses section for responses to earlier questions.  
2. Would you consider this approach a meta-learning method that aligns with the standard episodic reinforcement learning framework?  
3. Isn’t it true that the agent is aware of the task it’s solving, meaning there’s no true task boundary in the proposed evaluation?  
4. How would this approach perform if only partial task demonstrations were available? Could it potentially combine these fragments to form a complete solution?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework for lifelong robot learning that operates without explicit task boundaries or identifiers. The approach combines retrieval-based adaptation with selective weighting to help robots maintain and restore previously learned skills. The method uses episodic memory for both experience replay during training and local adaptation during testing. When encountering a task, the system retrieves relevant past demonstrations based on visual and language similarities, identifies challenging segments through preliminary rollouts, and applies weighted local adaptation. The approach is evaluated on LIBERO benchmark variants.

### Strengths
1. Originality:
- Novel approach to handling task boundaries without explicit task IDs
- Interesting combination of retrieval-based adaptation and selective weighting
- Dual use of episodic memory for training and testing phases

2. Quality:
- Comprehensive experimental evaluation across benchmarks
- Detailed ablation studies
- Clear documentation of implementation details

3. Clarity:
- Well-structured presentation
- Clear figures and visualizations
- Detailed appendices

4. Significance:
- Addresses a relevant challenge in robotics
- Shows potential for generalization across memory-based approaches
- Demonstrates improvements over baselines in controlled settings

### Weaknesses
1. Conceptual Contradiction:
- Claims to be "task-unaware" but fundamentally relies on task-based retrieval
- Still requires matching current scenarios with previously stored demonstrations
- The evaluation is still conducted on clearly separated benchmark tasks

2. Experiment:
- All results are from simulation with no real-world validation
- No analysis of failure modes or edge cases

3. Technical:
- Limited discussion of the impact of different hyperparameters
- Memory requirements could become problematic with increasing task numbers
- No discussion of potential catastrophic forgetting during local adaptation

### Questions
- How is your approach fundamentally different from traditional task-based methods, given that it still relies on retrieving similar tasks?
- What happens when encountering truly novel scenarios that don't match any stored demonstrations?
- How do you justify the various manual thresholds in the selective weighting mechanism? Have you explored their sensitivity?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work develops a novel approach for robotic control in a lifelong learning, multitask context without clear boundaries between tasks, suitable for real-world use. It uses episodic memory for experience replay and testing, allowing rapid adaptation to previously encountered tasks without explicit task identifiers. It is experimentally validated on the LIBERO benchmark and shows a significant improvement over baseline methods.

### Strengths
This paper focuses discusses a very important topic, that is robot learning in scenarios where there is no sharp boundaries between tasks, which is important for robots that operate in complex and noisy real world environments. The method is technically sound, and the empirical evaluation shows very good results.

### Weaknesses
My main concern is the magnitude of the uncertainties in Table 1. One of the main results is a difference between 45.17 ± 31.86 and 34.08 ± 28.55, which does not seem statistically significant - similar problems appear in the other results as well.

Potentially related to that, lines 402-403 state that the algorithm is evaluated on three seeds: 1, 21, 42. This is a suspiciously arbitrary selection - why not 1, 2, 3? This makes me a bit concerned that the seeds were cherry-picked to select for the most convenient results.

### Questions
What is the practical computational cost of this method? As in, if I wanted to train a model using this approach, assuming I have all the code and hyperparameters, what kind of hardware and time would I need to go from nothing to replicating the paper's results?

Is it viable to run additional experiments to tighten the uncertainties reported in Tables 1 and 2? As I understand, the standard deviation is based on the three seeds, and with a standard deviation this large, a larger sample and a proper statistical analysis would be very valuable.

Can you comment on why the selected seeds are 1, 21 and 42? 


If my concern about the uncertainty and potentially cherry-picking the seeds is answered, I will be happy to increase my rating.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper investigates the problem of lifelong robot learning where catastrophic forgetting is a key issue. The paper proposes to do retrieval-based adaptation in lifelong learning process, finetuning the global policy model with memories of previous similar tasks. Despite the simplicity of the idea, the performance exceeds multiple baselines in the experiments. The paper is well-written, and the results support the claims well. I do have a few detailed questions hoping the authors could clarify during the discussion period.

### Strengths
1. The paper is well written and easy to follow, with the figures illustrative about core ideas. 
2. The idea proposed is simple yet effective, showing great potential. 
3. The results and benchmark comparisons are very well structured, clearly showing the support for certain questions outlined in Section 5. The ablation studies are also well structured with both quantitative and qualitative evidence. 
4. The introduction provides strong motivation for the lifelong robot learning problem.

### Weaknesses
1. Although the related work section is comprehensive, it lacks a clear description of how the current work distinguishes itself from the related work. I suggest authors add this information and the relationship between the current work with prior work in each subsection of the related work.

1.1. Another work that looks into lifelong robot learning from demonstration is [1]. Could the authors possibly compare with it either conceptually or empirically?

2. The description about “blurred task boundaries” a little misleading. One would have thought blurred task boundaries mean there are no clear temporal boundaries between different task executions. However, the paper seems to take language-described robot tasks as blurred tasks as opposed to task labels, and there are clearly separated demonstrations among different tasks. I hope the authors could make the definition of “blurred task boundaries” clearer.

3. I also find some parts of the methods are not precise. For example, it is unclear from Section 4.1 whether the retrieval is on the timestep-level or demonstration-level. It became clearer with later discussion that it should be demonstration-level, but adding a clearer pseudocode of the entire pipeline would be helpful.

4. The abstract mentioned storing past data to prevent forgetting has privacy concerns. However, according to my understanding, the proposed method also requires storing the demonstrations in memory M for retrieval, thus having a similar problem. Can the authors discuss how this is handled in the proposed method?

### Questions
Besides the points mentioned in weaknesses, 
1. How are the demonstrations generated? Did humans provide demonstrations or was the demonstrations generated by a well-trained RL policy? 
2. How are the hyperparameters tuned, especially the language and image distance weights $\alpha_v$ and $\alpha_l$?

### Soundness
4

### Presentation
4

### Contribution
3
