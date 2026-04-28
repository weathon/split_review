# Learning to Solve New sequential decision-making Tasks with In-Context Learning

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Training autonomous agents that can generalize to new tasks from a small number of demonstrations is a long-standing problem in machine learning.  Recently, transformers have displayed impressive few-shot learning capabilities on a wide range of domains in language and vision.  However, the sequential decision-making setting poses additional challenges and has a much lower tolerance for errors since the environment's stochasticity or the agent's wrong actions can lead to unseen (and sometimes unrecoverable) states. In this paper, we use an illustrative example to show that a naive approach to using transformers in sequential decision-making problems does not lead to few-shot learning. We then demonstrate how training on sequences of trajectories with certain distributional properties leads to few-shot learning in new sequential decision-making tasks. We investigate different design choices and find that larger model and dataset sizes, as well as more task diversity, environment stochasticity and trajectory burstiness, all result in better in-context learning of new out-of-distribution tasks. Our work demonstrates that by leveraging large offline pretraining datasets, our model is able to generalize to unseen MiniHack and Procgen tasks via in-context learning, from just a handful of expert demonstrations per task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of in-context learning for decision-making. A method of training transformers is proposed where expert demonstrations are generated across many tasks and the model is expected to predict expert behavior from this context. The method is demonstrated on procgen and nethack, two challenging RL settings.  It is shown that in-context learning can be achieved from a handful of demonstrations in order to generalize to new test tasks.

### Strengths
The problem is important and interesting: the in-context abilities of transformers for decision-making problems is comparatively understudied relative to supervised learning problems. This paper contributes to a growing understanding of decision-making with transformers.

The generalization of the method to entirely new tasks in procgen and nethack is impressive as these are challenging settings and each task is quite different from the others. There are really only a handful of training tasks.

The analytical studies are thorough and mostly informative, especially the one showing how the performance varies with the number of training tasks and the one on failure modes.

### Weaknesses
Overall, I think this is a good paper with a thorough analysis, but there are two main weaknesses of the paper: clarity and novelty/significance.

Clarity: both the problem setting and the methodology of the training are not very clear and this makes it difficult to understand the significance of the results.

- During testing, the agent is given a handful of expert demonstrations. Are these all demonstrations on the same task and same level? If not, how does this work for the baselines hashmap if they are using demos from different levels? If so, why is the transformers trained with several sequences of demos from different levels? Why not just train with demonstrations from the same level and task always?
- Related to this, how do I interpret this, which suggests that all demos in the context come from the same level: “we collect offline data from 11 Procgen tasks and train a transformer on Procgen sequences compromising of five episodes from the same level.” What does burstiness even mean here if the levels are never varied?
- What does it mean for BC-1 to condition on ‘one demonstration’? Does this mean you give it full demonstration in the same task and same level? In other words, does the context look like this: [expert demo, history observed so far]. How would this be different from your method if you were just limited to training on just two sequences?
- What is the maximal achievable reward in each of the environments? This could be helpful to better understand the final results.

It would further be helpful to distinguish the work from prior methods better. A more thorough comparison would help readers with a better understanding of the present problem setting and method.

- The method appears to be very similar to Prompt-DT [1] perhaps without the return conditioning. There’s already a short discussion in the related but this ought to be carefully dissected, I think.
- The method is also very similar to DPT [2], which also considered training and conditioning on expert demonstrations to solve new tasks. If there is a difference, both of these papers seem like highly relevant baselines.
- It is also likely worth distinguishing the method with other in-context RL works like [3] and [4].

Beyond transformers, there’s additional work on meta/few-shot imitation learning that could be helpful to discuss.

As a result, the overall takeaways are a bit hard to discern. It’s clear now that there are multiple solid contributions in this paper (a method and a thorough analysis), but I think the takeaways could be better communicated.

### Questions
See above section for specific questions. Misc:

- How long are each of these sequences? I.e. what is T?
- In what settings would you expect this method would work (or these analysis be useful) under the current assumptions, beyond gameplaying?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the use of transformers for generalization to new tasks from MiniHack and Procgen. Their experiments show that a model pre-trained on different levels and tasks of Procgen can learn a new task from a few demonstrations of the task. The transformer is trained with demonstration contexts that can either be from the same or different levels as the query. There is also additional empirical analysis on different variables, such as whether the context is from the same level, environment stochasticity, and task diversity.

### Strengths
- This work shows that transformers can perform few-shot imitation learning on new Procgen tasks, which has not been explicitly shown previously.

- The paper is written pretty well at a low-level and tries to be thorough in its experiments through additional experiments to understand failure modes and effect of different environmental and algorithmic factors.

- Given the significance of in-context learning in large language models, it seems timely and appropriate to study it in the context of decision-making.

- The environment stochasticity result is pretty interesting, i.e., that the model can learn copying behavior if the training environments are deterministic.

### Weaknesses
 - Existing papers such as Prompt-DT (Xu et al, 2022) and AdA (Team et al, 2023) have shown similar results (in some cases, with even less presumptive data than full demonstrations) though in different domains. So it's perhaps not too surprising that we see this type of generalization in Procgen as a result. The main result that models trained with demonstrations in the context can perform better than models without the demo context is also expected.

- There are a couple of claims that do not seem sufficiently supported: (1) meta-RL methods "tend to be difficult to use in practice and require more than a handful of demonstrations or extensive fine-tuning," (2) "in sequential decision-making it is crucial for the context to contain full trajectories (or sequences of predictions) to cover the potentially wide range of states the agent may find itself in at deployment" (see Questions).

- The concepts of burstiness from Chan et al and trajectory burstiness have a pretty weak relation. In the case of this paper, it seems pretty clear from the get-go that demonstration contexts from the same level as the query would be more relevant than from any other levels.

### Questions
- What does trajectory burstiness mean for the zero-shot model in Fig. 6(a)?

- "[Meta-RL methods] tend to be difficult to use in practice and require more than a handful of demonstrations or extensive fine-tuning" --> Including some of these comparisons in the experiments would be help support this statement.

- "Our key finding is that in contrast to (self-)supervised learning where the context can simply contain a few different examples (or predictions), in sequential decision-making it is crucial for the context to contain full trajectories (or sequences of predictions)
to cover the potentially wide range of states the agent may find itself in at deployment." --> Full trajectories as opposed to what? The experiments only show comparisons between full demos vs no demos, and didn't study other potential contexts, such as partial demos or non-expert trajectories. I think a study of different potential contexts and what is required for in-context learning would be interesting.

- "This means that the agent manages to perform well on the new task even without copying actions from its context. This suggests the model is leveraging information stored in its weights during training, also referred to as in-weights learning" --> Could you elaborate on how not copying the context actions suggests in-weights learning as opposed to ICL? This conclusion seems to equate ICL with the ability to copy context actions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work targets the setting of zero-shot and few-shot learning, where the train and test MDPs contain completely separate games (tasks) - in contrast to previous works where the train and test sets contain the same game but with different levels.  The paper proposes to adapt the causal transformer model to this few-shot setting by first training expert agents on each of the training tasks, and then collecting a dataset from the experts’ trajectories to train the transformer model. The authors propose to train the transformer using multi-trajectory sequences rather than single-trajectory sequences and to construct the multi-trajectory training so that the context contains at least one trajectory from the same level as the query. At test time, for the few-shot setting, the transformer is conditioned on 1-7 full expert trajectories, while for the zero-shot setting the transformer is not conditioned on any expert trajectories.

The authors compare their results to two baselines: BC and hashmap, and performed an extensive ablation study containing the dataset sizes, task diversity, environment stochasticity, and trajectory burstiness.

### Strengths
* The paper suggests a new setting that has not been studied before - to test on games withheld during training by utilizing expert policies that were trained on the training set (a separate set of games).  

* The results show a clear advantage to the proposed approach over the baselines and the authors performed an extensive ablation study.

### Weaknesses
 * The proposed approach seems as a small adaptation of pre-existing approaches, i.e. causal transformer with multi-trajectory training, to new benchmarks (MiniHack and Procgen) in the offline setting.

* There is no comparison to other offline methods such as CQL [1]

* It is mentioned in the paper that all the results are produced using 3 seeds. In my opinion, for such noisy benchmarks evaluating on only 3 seeds is not enough to reliably estimate the mean and variance. 

* The results are not clear to me - for example, in Figure 4 the episodic return is very low compared to the score reported by [2].

### Questions
I would like to ask the author to address the following questions: 

1. For the few-shot evaluation (when testing the model): is the expert policy, which creates the few trajectories (1-7) for conditioning the transformer, trained on the test games or the training games? 
2. Are the above few trajectories (1-7) sampled from the same level as the query level? 
3. Why is the return in Figure 4 so low compared to the return reported in [2]?
4. Is the Procgen dataset evaluated on the easy or hard difficulty mode?
5. Are the results in Figure 3 normalized?


A technical detail: 
* In the first paragraph of the background - /mu the initial state distribution is not defined.





[1] Kumar, Aviral, et al. "Conservative q-learning for offline reinforcement learning." Advances in Neural Information Processing Systems (2020): 1179-1191.

[2] Cobbe, Karl, et al. "Leveraging procedural generation to benchmark reinforcement learning." International conference on machine learning. PMLR, 2020

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of in-context learning in sequential decision-making settings. The paper finds that it is important for the context to contain full trajectories to cover potential situations at deployment time. The authors provide experiments on MiniHack and Procgen benchmarks, showing the method can generalize to new tasks with just a few expert demonstrations, without weight updates. The work claims to be the first to demonstrate that transformers can generalize to entirely new tasks in these benchmarks using in-context learning.

### Strengths
- The paper is well written and easy to follow.
- The paper shows some nice experiments on the MiniHack and Procgen environments, showing how in-context learning can perform well on unseen tasks.
- The paper's setting of in-context learning in decision-making problems is an interesting problem to study.

### Weaknesses
 - The paper highlights the ability to perform well on unseen tasks but this actually relies on having a lot of demos from related tasks. Can the authors better clarify the relationship between the data they train on and the unseen tasks they evaluate on?
- Novelty-wise, the method is very similar to works like Prompt-DT, except actually requires stronger data assumptions (full expert demos).
- A lot of the insights in the empirical study are not that interesting, e.g. the paper highlights results like showing that in-context learning improves with trajectory burstiness, but it is not surprising that having demos similar to the query inside the context improves the performance. Can the authors give more clarity on what the most surprising, interesting takeaways are from the study?

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
