# XLand-100B: A Large-Scale Multi-Task Dataset for In-Context Reinforcement Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Following the success of the in-context learning paradigm in large-scale language and computer vision models, the recently emerging field of in-context reinforcement learning is experiencing a rapid growth. However, its development has been held back by the lack of challenging benchmarks, as all the experiments have been carried out in simple environments and on small-scale datasets. We present \textbf{XLand-100B}, a large-scale dataset for in-context reinforcement learning based on the XLand-MiniGrid environment, as a first step to alleviate this problem. It contains complete learning histories for nearly $30,000$ different tasks, covering $100$B transitions and $2.5$B episodes. It took $50,000$ GPU hours to collect the dataset, which is beyond the reach of most academic labs. Along with the dataset, we provide the utilities to reproduce or expand it even further. With this substantial effort, we aim to democratize research in the rapidly growing field of in-context reinforcement learning and provide a solid foundation for further scaling. The code is open-source and available under Apache 2.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a dataset, XLand-100B, for training and testing in-context RL algorithms. In-context RL is the problem of predicting how to act in a task, given trajectories from the task, without any updates to the model weights. There is prior research in this field, but future progress is hindered by lack of open-source datasets/benchmarks where algorithms can be tested. The paper introduces a large scale dataset containing 100B transitions, 2.5B episodes from 30,000 (in effect, around 29,000 after filtering). The paper also tests two current algorithms, AD and DPT, to show that more progress/research is needed in the field.

### Strengths
1. The paper is a dataset paper, and I think it clearly motivates the need for such a dataset in the open-source community. In that way, it is a strong work, since the release of a dataset/hard enough benchmark can truly boost the research productivity in this important field. The release of the ImageNet benchmark accelerated the pace at which computer vision grew as a field, and a well-designed benchmark can do that for in-context RL as well, hence I support the acceptance of this paper.
2. The paper is nicely structured and well-written, giving insights and reasoning to the community.
3. As the authors claim, researchers in this field often need to generate their own data. This results in lack of reproducibility and wastage of computational resources. This paper can help mitigate some of those challenges.
4. The authors have spent significant effort in trying to compress the dataset while maintaining throughput for loading the dataset from the compressed version. This effort is highly appreciated!

### Weaknesses
1. Despite the enormous size of the dataset, it only contains one type of environment, based on the Mini-Grid set of tasks. While this is a starting point for research in this direction, adding tasks from more realistic domains, like robotics/other tasks that strictly require RL, would be appreciated. This is my main concern for not giving a higher score. The lack of diversity in environment dynamics and observation spaces limits the generalizability of models trained on this dataset. For instance, the Mini-Grid environment has a discrete action space and a grid-based observation space, which is quite different from the continuous action and high-dimensional observation spaces encountered in robotics. This discrepancy makes it unclear how well in-context RL algorithms trained on this dataset would perform in more complex, real-world scenarios.
2. Adding more visualizations of the tasks, trajectories, etc in the appendix might be helpful to understand the precise nature of the tasks, what does # rule 3 → # rule 9 actually mean for the hardness of the task, etc. The current description of the task structure is somewhat abstract, and concrete examples of the task variations would be beneficial. For example, showing how the task tree changes with an increasing number of rules, and how the optimal policy needs to adapt, would provide a clearer understanding of the dataset's complexity. Furthermore, visualizing a few example trajectories, especially for more complex tasks, would help researchers understand the exploration challenges involved.
3. The idea of collecting such a dataset is not novel, despite the importance of doing such work that can empower future novel research in this direction.

### Questions
Line 350

> In contrast to AD, which predicts next actions from the trajectory itself, DPT-like methods require access to optimal actions on each transition for prediction. However, for the most nontrivial or real-world problems, obtaining true optimal actions in large numbers is unlikely to be possible.

I am uncertain about this line. As shown by [1], one can use a fully finetuned RL policy for a task, that achieves good performance, to collect “expert” data. Why is that not the case for this paper’s tasks?

# References

[1] D4RL: Datasets for Deep Data-Driven Reinforcement Learning, https://arxiv.org/abs/2004.07219

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces new datasets “XLand-100B” and “XLand-Trivial-20B” intended for research on in-context reinforcement learning (ICRL). XLand-100B consists of 100B transitions spanning 30k different tasks from the XLand-MiniGrid environment. 

The authors argue that research in ICRL has been hampered by the lack of large & diverse datasets that are compatible with ICRL, as well as by the significant compute requirements in this domain, and discuss how their contribution aims to make this research more accessible, in particular for researchers with limited resources. They emphasize that compared to prior work (NetHack, Procgen, GATO,...), their dataset is larger, more diverse, and better suited for ICRL research since it contains full learning histories instead of unordered or solely optimal/expert trajectories.

The data was collected by first pretraining a PPO multi-task policy on 65k tasks for 25B transitions and then finetuning it on a subset of 30k tasks. The dataset was only collected during the latter phase (for XLand-100B). The authors show that the pretrained policy performs well in the zero-shot setting, and that using it as a starting point for finetuning yields a very large performance boost compared to training a single-task policy from scratch (on hard tasks).

Finally, the authors benchmark Algorithm Distillation (AD) and Decision-Pretrained Transformer (DPT) on their dataset. They show promising results with AD, which displays an emergent ICL ability. However, they note that they were unable to show the same for DPT. The authors hypothesize that DPT performs poorly in POMDP settings as its lack of positional encoding prevents it from leveraging useful historical information from the current episode.

### Strengths
Overall, the paper makes a substantial contribution to in-context RL research (and RL research in general). The authors argue clearly what distinguishes their work from the many existing datasets and benchmarks, and as such, the design of the benchmark is very well-motivated. The paper is also well-written and the presentation is good. 

Some strengths worth highlighting:

1. I particularly appreciate the level of detail regarding data collection, the dataset format, and other implementation/engineering methodology.
2. The authors made significant effort to make the benchmark easy to use (e.g. tuning the data compression to balance dataset size and sampling speed, and providing estimated optimal actions which are needed by methods such as DPT).
3. Including the lighter XLand-Trivial-20B dataset should make the benchmark significantly more accessible to researchers with limited resources.

I would be happy to increase the score, pending clarification on some of my concerns below.

### Weaknesses
I don’t believe there to be any significant weaknesses relating to the dataset (the main contribution) itself, apart from the limitations mentioned in the paper.

Regarding the AD & DPT baselines:

1. My understanding is that DPT, in contrast to AD, is unable to reason in POMDP settings because its transformer doesn’t include a positional encoding. Have you considered the modification of applying a positional encoding to just the transitions from the current (ongoing) episode? This wouldn’t significantly change the DPT formulation but would remove the limitation of not being able to use historical information from the current episode. The DPT experiment as it stands does not seem like a fair comparison to AD as its poor performance likely doesn’t come from the method itself but the observation space (lack of historical context).
2. It is stated that evaluation is performed for 512 episodes with a context length of k=1024/2048/4096. My understanding is that the context is initially empty and that at the end of evaluation, the context contains the most recent k transitions (potentially from multiple episodes). It’s unclear how often the context actually includes data from multiple episodes. What is the median episode length?
3. Have you performed experiments (with AD) where the context only contains data from the current episode? From Appendix H, it is clear that knowledge of the current episode history is essential for solving some of the partially-observable tasks (e.g. knowing whether you have already picked up a key). Including data from previous episodes could make it more difficult since the policy would need to distinguish whether a key pick-up happened in the current or previous episode.
4. Do you have any insight on why longer context lengths perform strictly worse with AD? Could it be related to the issue mentioned in my previous question (3.)?

Minor:

5. Figure 8 is a bit unclear as there is no label/legend for the colors. The 1024 context length could be confused with the 1024 unseen tasks used for evaluation.

### Questions
1. Why did you choose to use recurrent PPO with GRU for data generation over using a transformer (as in the two ICRL experiments)?
2. Evaluation is performed for 500 episodes and the score averaged across 1024 tasks. Am I correctly understanding this as performing 1024 separate single-task evaluations (each 500 episodes long) and then averaging scores across tasks? I.e., the transformer context never contains data from multiple tasks.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces XLand-100B, a large-scale data set for in-context reinforcement learning containing 100B transitions across 30,000 different tasks. The dataset includes complete learning histories of agents trained with PPO in the XLand-MiniGrid environment. The authors evaluate two common in-context RL algorithms on the dataset, showing the limitations of these methods with complex tasks. The work aims to democratize in-context RL research by providing a standardized, large-scale benchmark.

### Strengths
- The paper is well written.
- There do not seem to be any major issues with the method or the data set.
- Authors appear to have taken reproducibility seriously.
- The technical presentation of the data set, including relevant specifications, is comprehensive and clear.
- The work addresses an important gap that is hindering progress in an area of reinforcement learning of growing interest.

### Weaknesses
The paper has no critical weaknesses. However, for the sake of constructive academic discussion, I include some drawbacks below:

- The dataset exclusively uses PPO to generate learning histories, without theoretical or empirical justification for why PPO is especially suited for ICRL compared to other RL algorithms. Given the diversity of RL methods—each with distinct exploration strategies, convergence behaviors, and learning dynamics—relying solely on PPO risks biasing the dataset toward a specific style of learning history. This may inadvertently limit the dataset’s utility for evaluating ICRL methods that could benefit from more varied demonstration patterns. For instance, algorithms that rely on more diverse exploration, such as those using entropy regularization or count-based exploration, might find the PPO-generated data less informative compared to data generated by an algorithm with those characteristics. The lack of diversity in the learning histories could also make the dataset less representative of the full spectrum of possible agent behaviors and learning trajectories.
- The dataset’s approach to ensuring high-quality demonstrations is primarily based on filtering out tasks with low final returns, which does not fully address whether all included histories are genuinely informative or relevant for ICRL. While high returns are indicative of successful task completion, they do not guarantee that the learning trajectory is optimal or even particularly insightful for in-context learning. A policy that achieves a high return might do so through a circuitous route or by exploiting specific environmental quirks, rather than by demonstrating a generalizable problem-solving strategy. The filtering process could inadvertently remove learning histories that, while not achieving the highest returns, might contain valuable information about exploration, adaptation, or recovery from suboptimal states.
- The use of approximate expert actions for labeling could compromise action fidelity, particularly for complex tasks, which may impact models that rely on high-quality expert demonstrations. The PPO policy, even when well-trained, is still an approximation of the optimal policy, and thus the actions it generates may not always be the most informative or efficient. This is especially true in complex environments where the action space is large and the optimal policy is difficult to learn. The use of these approximate expert actions could introduce noise into the dataset, potentially hindering the performance of models that rely on precise action sequences for in-context learning. Furthermore, the dataset does not provide any measure of the approximation error, making it difficult to assess the impact of this potential source of noise.

### Questions
- Could you clarify the rationale for choosing PPO as the sole algorithm for generating learning histories? How might the dataset be affected if other RL methods with different exploration and learning characteristics were incorporated?

- How do you ensure that filtered tasks with low returns are adequate proxies for high-quality demonstrations in ICRL?

- How might labeling inaccuracies impact the performance of models relying on these demonstrations?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In recent years, there have been some efforts on in-context reinforcement learning (ICRL). According to the authors, most ICRL research has been done on simple environments, and the lack of challenging benchmarks limits progress of the field. To address this, the paper proposes XLand-100B, a large scale dataset for in-context learning in gridworlds, comprising 30K tasks and 2.5B episodes.

### Strengths
The paper highlights an important limitation of current ICRL research, which is often focused on simple benchmarks such as gridworlds and small datasets. To this end, the authors generate a large-scale dataset and make it publicly available. The dataset contains episodes from 28K tasks, which is larger than other ICRL datasets. The authors make good design decisions in terms of their storage format (hdf5, compression levels, chunk size) and data collection strategy. As such, the dataset may be useful to the broader ICRL community.

### Weaknesses
While the paper highlights, that current ICRL research is focusing on simple environments, the gridworld environment they consider also seems simplistic. The generated dataset seems to be specific for a 5x5 single-room grid (not the multi-room in Figure 1? See questions). Generally, the environment seems similar to Dark-Room/Key-Door, and can be seen as a more advanced grid-world (with more than 2 objects) to test ICRL in toy environments. Therefore, it is unclear how well future findings on this dataset would transfer to other settings like robotics.

To the best of our understanding, there is a maximum of 9 rules in this environment, which correspond to reaching different objects in order. It would help the paper to provide a visual illustration of those rules for the reader to get an understanding of how diverse those tasks are (especially as it is a 5x5 grid). Due to those 9 rules, many different tasks can be produced. However, while there are 28K tasks in the generated dataset, it is unclear how much overlap or diversity there is between tasks. Therefore, it is possible that ICRL agents do not benefit from training on additional tasks. We suggest conducting an ablation study, in which agents are trained on 100/1000/10000/all tasks to evaluate the effect on ICRL abilities. This is currently missing.

While the authors release a large dataset with lots of tasks, from the perspective of a user it is unclear where to start. This is due to the lack of a clear benchmark split. The authors should clarify on what tasks to train on and what to evaluate on. This could be by number of pre-training tasks (as mentioned above) or number of rules etc. This point is important and needs significant revision and empirical evaluation of the considered methods.

In Figures 12 and 13 the learning curves (over 8K and 15K episodes) across all tasks are provided. The agents reach optimal performance quickly, only after a coupled hundred steps. Therefore, there is little learning progress in the remaining 14K updates. This may be a reason why AD and DPT do not exhibit meaningful in-context improvement during evaluation (Figure 7, 17, 20). Generally, there seems to be little in-context improvement by any ICRL method, which is different from previous ICRL works. This raises the question, whether the problem lies in the algorithms or the datasets, and should be discussed in the paper.

### Questions
- Can you clarify whether the dataset is collected on a 5x5 grid or on the grid visualized in Figure 1? If so, it is important to update Figure 1 to show the actual environment. 
- In Figure 5, it seems that there is not much difference in learning performance from 1 to 7 rules, but a larger jump to 9 rules. Can you clarify why this is the case? 
- Why does AD not exhibit in-context improvement in Figure 7 (only slightly for 1 rule)? Can you provide empirical evidence if this is a property of the data or the algorithm?
- In Figure 8, AD performance decreases with a larger context length. Why is that? Can you clarify how many episodes the context comprises?

### Soundness
2

### Presentation
2

### Contribution
2
