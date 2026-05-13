# Playbook: Scalable Discrete Skill Discovery from Unstructured Datasets for Long-Horizon Decision-Making Problems

- Decision: Reject
- Scores: 3, 6, 8

## Abstract
Skill discovery methods equip an agent with diverse skills necessary for solving challenging tasks through an unsupervised learning manner. However, making the pre-learned skills expandable for new tasks remains a challenge in existing research. To handle this limitation, we propose a scalable skill discovery algorithm, a playbook, which can accommodate unseen tasks by training new skills while maintaining previously learned ones. The playbook, characterized by discrete skills and an extendable structure, enables the extension of the skill set to cover new datasets. Since we design the playbook to have a finite number of skills, we can interpret a decision-making problem as a sequential skill classification problem, so we aim to learn additional skills of the playbook by applying the techniques of class-incremental learning. In addition, we also introduce skill planning schemes that can leverage both previously and newly learned skills to solve challenging tasks compounded by multiple sub-tasks. The proposed method is evaluated in the complex robotic manipulation benchmarks, and the results show that the playbook outperforms existing state-of-the-art methods that learn continuous skills.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, the authors present _Playbook_, which is an algorithm for discovering "skills" from offline, unlabeled behavior datasets. The goal of Playbook is to be able to take a large, unlabelled dataset, and learn skills – which can be think of as sub-policies – that can be then chained together to solve longer-horizon decision making. The authors evaluate the method in two simulated setups: the play-kitchen environment according to D4RL setup, and the CALVIN benchmark. They first evaluate the method on a static sized dataset, and then on CALVIN, they evaluate on an extending dataset.

### Strengths
The authors introduce a new way of thinking about learning skills from unstructured and unsupervised behavior datasets. In particular, the strengths of the paper are as follows:

1. The authors identify an interesting problem of learning skills from large behavior datasets without having access to labels. For example, a lot of large human behavior datasets could be composed of the demonstrators switching between multiple behavior modes, and being able to identify those modes properly will help learn behaviors more efficiently. The authors target the hierarchical learning problem, which can be relevant with the right algorithm.
2. Similarly, I can see the relevance of incremental learning in such a setup – especially in a life-long manner where relevant data may be coming in sequentially.
3. The algorithmic setup for learning a playbook, at a very high level, makes sense. I appreciate the quantization setup – which makes sense for learning a state-and-goal conditioned policy.
4. Finally, using the planning setup to select a play is also an interesting idea – especially if we have a reasonable model of the world. I think this idea is novel, and I have not seen this used in other works before.

### Weaknesses
However, there are many points where the work can improve. Some of the major points being:

1. The primary issue with this work is that it seems very much like a stream-of-consciousness work. The paper starts with a playbook learning method, then it talks about sequential learning of the plays, and finally, talks about the sequental planning with plays. All of these are interesting ideas in itself, and it feels like the paper doesn't give any of the ideas the proper time and explanation.

2. Expanding upon the previous point – just the skill playbook learning without even extensibility – requires 5 different continuous hyperparameters, even without considering the number of plays. Then the authors add the monte carlo tree search planning on top. This whole paper keeps stacking ideas one atop another until there is no scope for understanding what is _the_ contribution for this paper, and how to properly evaluate it.

3. Because the whole paper and the proposed method is so complex, the evaluations seem inadequate – only two sim environments, and on relatively small datasets as well. Evaluation on more environments would be helpful to make a case for this method.

4. The baselines seem inadequate – if the task is goal reaching, why are the evaluations only against offline RL methods, and not any goal conditioned BC methods? Similarly, the authors don't seem to compare against the SOTA methods on CALVIN either.

5. The method doesn't clarify all the assumptions it makes. For example, the planning requires a way to judge the "best final state", or some type of metric on the state space. It's not a trivial assumption, but the paper makes it look like no big deal. Similarly, it's not clear how the authors are using trajectory transformer on the CALVIN environment to learn a trajectory where the observations in CALVIN are RGB images.

6. Finally, the ablation studies need more details – for example, how the number of plays were picked is an important question.

### Questions
1. How did the authors pick the number of plays, and also the hyperparameters in eq 5?
2. Are there any issues on training this method stably?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework to handle skill discovery from offline datasets in a lifelong learning setup. The paper combines multiple existing works: during skill discovery, it combines vector quantization (VQ) and multiplicative compositional policies (MCP), where VQ network selects the skill embedding that applies to MCP primitives. When a new dataset incomes, the paper uses FOSTER to first expand the aforementioned VQ and MCP networks and then distill them back to the original size. Finally, during task learning, the paper uses planning to solve the goal state reaching task.

### Strengths
Lifelong skill discovery receive increasing attention these years and thus this paper focuses on an important topic. 

Meanwhile, while the paper uses a combination of prior techniques, to the best of my knowledge, the formulation of the skill selection policy (as the weight of MCQ) is novel.

In addtion, despite that there are many component in the proposed lifelong skill discovery framework, the illustrative figures greatly improve clarity and help readers understand the proposed pipeline.

### Weaknesses
My main concern is the lack of discussion and comparison with prior works in lifelong imitation learning, such as [1].
I understand that there are many components and design choices in such a complex framework, but at least I would like to see if we replace a component in the proposed work with one from prior work, how it affects the performance. Maybe in this way, we can have a better understanding of what matters in a controlled way. For example,
1. The paper proposes to use MCQ to make action multi-modal, and in the ablative study, shows that using a single primitive decreases the performance. But in practice, many imitation learning work uses gaussian mixture model or diffusion to create multi-modal actions. Which of these two methods perform better?
2. When new datasets income, if there are demonstration that's similar to existing skills, LOTUS will also adjust existing skills with such samples. In contrast, IIUC, the proposed methods don't allow such adaption, and skills that are similar but slightly different to existing ones are likely to be added as new plays. This issue may make the playbook unnecessarily large. One potential support is that, in Fig 6, the use of old plays are quite low in Close Drawer and Move Slider Left. Even though they should share many similar skills with Open Drawer and Move Slider Right (I may be wrong, feel free to let me know if there are any other reasons for these low reusage values).

[1] Wan, Weikang, et al. "Lotus: Continual imitation learning for robot manipulation through unsupervised skill discovery." 2024 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2024.

### Questions
see weakness

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
2

### Summary
This paper proposes a new algorithmic technique for learning a set of reusable robot skills, called "plays", collecting them in an extensible "playbook", and planning using that playbook to complete tasks. The authors extend existing work on learning a set of motion primitives, and add the notion of a play, a mixture/weighting of these primitives. The list of plays and their weights can be learned end-to-end from demonstrations. The set of plays can be extended to learn new plays/primitives from a new dataset. The plays can also be used for beam search and Monte Carlo Tree Search to enable planning in two configurations - single-plan and mixed-plan. The authors show that in simulated robotics benchmarks, their technique can more frequently complete tasks with several subtasks than existing approaches.

### Strengths
* The problem being approached is valuable and the playbook concept is a good addition to the literature (significance).

* The technical approach is an impressively-novel combination of many existing techniques, plus the playbook concept, into a full pipeline. (originality)

* The ablation studies performed and progressively-harder experiments do a good job of showing the graceful degradation of the proposed approach and the improvements over prior work. (quality)

* The diagrams are useful (clarity).

### Weaknesses
* I found parts of the paper to be unclear to the point of causing me to doubt the technical details of the approach, although I confess that some of this may be due to unfamiliarity with some of the underlying techniques being utilized. See below:

	* I found the parallels to/usage of FOSTER to be confusing. Around line 245, the paper states "compresses the entire model grown to the original model size through the knowledge distillation technique". However, it also says that in FOSTER, "the size of the entire model is increased". Does the model increase in size, or not? A similar confusion happens in the description of the paper's own procesxs, saying around line 256, "the embedding model is reduced to its original network size", but then around line 318, it is stated that all models have to be maintained (i.e. increasing in size). The paper would be improved by clarifying exactly what "model" or list of models is being referred to, and when and if it is actually increasing or decreasing in size and/or expressiveness. This is an important point because the (non)scalability of the approach to (much) larger datasets is an important characteristic of the method, given the problem being solved.

	* the word "model" seems overused - metric model, planning model, etc. Consider replacing the term "metric model" (line 300) and other references to the same concept with a different term.

* As described around line 251, the approach adds the results of the new and existing embedded models. This does not seem like a valid combination, since primitives in MCP are designed to be combined multiplicatively, not additively. The paper would be better if it justified this choice.

**Style Notes**

* The title of section 5.2 would be clearer if the term "mixed play" were hyphenated, right now it is unclear if this is "mixed-play plan" or "mixed play-plan" from the title alone.

### Questions
* Regardless of whether or not the model/list of models are increasing in size during compounded training, does the number of primitives/plays also increase monotonically? The paper would seem to suggest this, but I wasn't sure if there was also some distillation/size reduction step being proposed for the plays and primitives.

* Why do the plan weights modify the primitives by exponentiation, and not multiplication? Since MCP is designed for multiplicative combination, it seems that a multiplicative weight might be more numerically stable to train.

* On line 294, it's stated that a Q-network measures the distance between two states, but Q networks require an action as well. Is it a value network, or if it is a Q network, where does the action come from? (in the final state, there is no action, what is done then?)

* Is there a requirement on the length of the demonstrations in the dataset (even if it is not a set length, do all demonstrations have to be the same length)? This seems like a requirement based on equations such as the goal state selection on line 304, but such a requirement doesn't seem to be explicitly stated anywhere. I believe H is the window size and must remain fixed, but this is only inferred and referenced in the appendices, and not in the main paper.

### Soundness
3

### Presentation
3

### Contribution
4
