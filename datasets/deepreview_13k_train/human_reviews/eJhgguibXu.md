# Using Approximate Models for Efficient Exploration in Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 3, 1

## Abstract
In model-based reinforcement learning, an agent uses a learned model of environment dynamics to improve a policy. Using a learned model of the environment to select actions has many benefits. It can be used to generate experience for learning a policy or simulate potential outcomes in planning. It allows flexible adaptation to new tasks and goals without having to relearn the underlying fundamentals of the environment from scratch. These sample efficiency and generalisation gains from model use are restricted by the model’s accuracy. An imperfect model can lead to failure if trusted by the agent in regions of the state space where predictions are inaccurate. It is well-documented in cognitive and developmental psychology that humans use approximate intuitive models of physics when navigating the world in everyday scenarios. These intuitive models, despite being imperfect, enable humans to reason flexibly about abstract physical concepts (for example, gravity, collisions and friction), and to apply these concepts to solve novel problems without having to relearn them from scratch. In other words, humans efficiently make use of imperfect models. In this paper, we learn dynamics models for intuitive physics tasks using graph neural networks that explicitly incorporate the abstract structure of objects, relations and events in their design. We demonstrate that these learned models can flexibly generalise to unseen tasks and, despite being imperfect, can improve the sample efficiency of policy learning through guiding exploration to useful regions of the state and action space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on utilizing learned models of the world for reinforcement learning. Planning with imagined data from an imperfect world model can lead to poor policies and bad value estimates.  

To avoid issues due to model inaccuracies, this work suggests using the imagined trajectories only to guide exploration and not for updates to the policy. Concretely, model-based imagination is only used to build a prior over actions, which is used to sample actions when a non-greedy/exploratory action needs to be taken in an epsilon-greedy approach.

Experiments in an intuitive physics environment show that the proposed approach can provide benefits over standard DDPG that adds noise in parameter space to explore.

### Strengths
**S1.** Leveraging imperfect models of the world for RL is an important problem that interests the research community. 

**S2.** The proposed approach of exploring by building action priors based on successful imagined trajectories is an interesting idea.

**S3.** Most of the paper is well-written and easy to follow.

### Weaknesses
 **W1.** A key weakness of the present submission is in the empirical evaluation.

It is not clear if planning with the learned model (using the world model to train DDPG) would actually be problematic in this setting, which was posed as a vital motivating factor for this work. The paper lacks a direct comparison showing the performance degradation of using the learned model for both planning and policy updates, making it difficult to assess the core claim that model inaccuracies are detrimental. Furthermore, the evaluation only compares the proposed approach to standard DDPG with parameter space noise. This is insufficient as many model-based exploration methods leverage learned models specifically for exploration. For instance, methods using prediction error or information gain as intrinsic rewards could be more effective at directing exploration in this setting [1, 2]. The paper does not discuss or compare to these alternative model-based exploration techniques, leaving the reader unsure of the relative benefits of the proposed method. It is unclear if model inaccuracies would impact curiosity-based exploration more than the approach presented here. The lack of comparison to these methods weakens the empirical support for the proposed approach.

Also see Q2.


**W2.** The paper makes some strong assumptions that limit the generality and applicability of the proposed approach. 

One strong assumption that the paper makes is to have a resettable ‘true’ environment, which allows multiple environment rollouts from the same environment state (point 3 on page 5). This limits the applicability of the method to environments where such resets are feasible. Another crucial assumption is the availability of subgoals in sparse reward environments. The method relies on having these subgoals to guide the imagined trajectories, but it is not clear how these subgoals are obtained in the first place, and this assumption severely limits the applicability of the approach in more complex tasks without well-defined subgoals. 

On a minor note, Figure 6 could be improved as it is currently hard to analyse. It would be better to use the same colors to denote approaches across the sub-figures.

### Questions
Q1. What are the subgoals in the tasks used for evaluation?

Q2. While the proposed idea shows some benefit over standard DDPG, the learning dynamics appear quite unstable in Figure 6. Can the authors explain why this might be the case?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper uses graph neural nets to learn the world model, then planning within the model for exploration. First pre-collect data by a random policy, then train a world model using GNN, then do planning towards subgoals (pre-defined) within the learned model, output high-rewards actions. Then exploration is performed by e-greedy. The idea is interesting, but there is still room for improvement. I would encourage authors to continually work on it. But currently, I think the paper is not ready yet for ICLR.

### Strengths
1. The idea is interesting, by only using the world model to guide exploration, even when the world model is very inaccurate, it will not affect the policy learning too much.

2. This model-guided exploration does seem to perform better than random exploration.

### Weaknesses
1. The paper assumes during the planning, a set of subgoals exist, I do think it is a strong assumption, it would be more realistic/interesting to somehow propose these sub-goals automatically. 
2. Baselines are not well picked (only compared with DDPG). More should be added. For example, after the world model is learned, the policy can be learned directly within the model. But if you argue the model is not accurate enough for direct policy learning, then you should compare with it (learning a policy using data sampled from the world model). I think it would also make sense to compare with direct planning using the model. 
3. Data for training the world model is pre-collected by a random policy, it works in very simple cases but wouldn’t work in more complicated tasks where you need better policy for data collection.

### Questions
1. The second step of computing rewarding actions is a bit like sampling-based planning, for example, CEM or MPPI. Why do you use clustering here instead of CEM or MPPI?
2. How do you sample subgoals?
3. If you first learn a model, why don’t you directly plan (for example, using MPC) in the world model, but using planning to guide the exploration, then learn a policy. Or directly do model-based reinforcement learning, since you already have a model. This combination, to me, would perform worse than planning and would be less efficient than MBRL. What’s the intuition for this combination?
4. Task descriptions are not presented, what are these tasks in Fig.3, how do they work, where are subgoals, etc.

Minior comments:
1. In section 2.2, second line, should be ‘state-action value’ instead of ‘action value’.
2. Presentation of figures is not consistent, for example, in Fig.6, some of them are with confidence intervals while some are not, some are smoothed and some are not. 
3. Explanations on Fig.4 are too little, you could elaborate more on details.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a graph neural network-based approach to approximately model the dynamics of intuitive physics-based tasks. Using this model, the paper proposes to identify high reward action distributions, which are then used to guide the agent’s exploration. Through physics-based puzzle games, the paper aims to show how the approach (a) learns in a task-agnostic manner and helps identify rewarding regions of the action space and (b) enables accelerated convergence by virtue of guided exploration.

### Strengths
The paper is mostly fairly easy to understand and aims to tackle an important issue of efficient exploration.

### Weaknesses
The paper is mostly fairly easy to understand and aims to tackle an important issue of efficient exploration.

The description of the experiments needs improvement. Moreover, the results are not very convincing. Further details are described below.

Figures 2,3 and 4 need more descriptive captions as well as better descriptions in the text.  For example, what do the symbols correspond to in Fig 3? Similarly, in Fig 4, a legend (along with better descriptions) would have made it much easier to interpret the results. 

Why is it that the relative Goal hits in Fig 5a are much higher compared to other tasks?

It is not immediately clear why the approach applies only to intuitive physics based tasks. I think this point needs to be emphasized better in the introduction.

Over how many trials were the experiments conducted in Fig 6? In general, from the learning curves, the learning does not look stable.

Doesn’t exploration epsilon=0 imply no model guidance? If so, for say, task 4, they both reach the same asymptotic performance. Why is this the case, while in some of the other tasks, the asymptotic  performances are very different?

Ablations showing the effect of $\epsilon_{threshold}$ are missing. 

As claimed in the last line on Page 7, why would the policy learning diverge? I believe that the learning would still occur (as DDPG learns off-policy) but due to a lack of exploitation, the learning curves would not reflect the learnt policy.

Perhaps the authors could have considered Phyre environments (https://ai.meta.com/tools/phyre/) to validate their approach.

In Fig 6, I assumed the orange color always corresponds to exploration epsilon of 0, but for task 6, the colors are swapped.

“By using…however uncertain” – This sentence towards the end of the introduction is too long and can be phrased better.

### Questions
1.	Figures 2,3 and 4 need more descriptive captions as well as better descriptions in the text.  For example, what do the symbols correspond to in Fig 3? Similarly, in Fig 4, a legend (along with better descriptions) would have made it much easier to interpret the results. 

2.	Why is it that the relative Goal hits in Fig 5a are much higher compared to other tasks?

3.	It is not immediately clear why the approach applies only to intuitive physics based tasks. I think this point needs to be emphasized better in the introduction.

4.	Over how many trials were the experiments conducted in Fig 6? In general, from the learning curves, the learning does not look stable.

5.	Doesn’t exploration epsilon=0 imply no model guidance? If so, for say, task 4, they both reach the same asymptotic performance. Why is this the case, while in some of the other tasks, the asymptotic  performances are very different?

6.	Ablations showing the effect of $\epsilon_{threshold}$ are missing. 

7.	As claimed in the last line on Page 7, why would the policy learning diverge? I believe that the learning would still occur (as DDPG learns off-policy) but due to a lack of exploitation, the learning curves would not reflect the learnt policy.

8.	Perhaps the authors could have considered Phyre environments (https://ai.meta.com/tools/phyre/) to validate their approach.

9.	In Fig 6, I assumed the orange color always corresponds to exploration epsilon of 0, but for task 6, the colors are swapped.

10.	“By using…however uncertain” – This sentence towards the end of the introduction is too long and can be phrased better.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of using approximate models in reinforcement learning (RL). RL training is broken into several stages:
1) Model learning: learns a graph neural network model (GNN) for world dynamics, then clusters actions taken in that world model into groups predicted to lead to high rewards
2) RL learning: trains an RL model (DDPG) to learn to perform the task. Search includes an exploration condition that samples from the above action clusters as part of epsilon-greedy search.

To facilitate long horizon planning, the task is divided into a series of sub-goals that are solved sequentially. The GNN used as a world model incorporates several adjustments to apply to the particular task domain (allowing for dynamic edges, edges specific to object pairs, and encoding positions in relative coordinates). Evaluations compare against a random baseline model, showing improved probability to achieve goals in a physics-based puzzle domain.

### Strengths
# originality
The primary original contribution is technical: extracting clusters of promising actions leading from one sub-goal to a new sub-goal from a learned world model. The originality lies in mining the world model to bias action exploration, in lieu of the trained policy or purely random exploration.

The GNN modifications to handle these physics-based puzzles are new for this domain.

# quality
The experiments show the technique achieves a higher success rate than a random action model in achieving goals and subgoals. In most cases random actions fail to ever achieve goals, and rarely subgoals, while the method proposed achieves success on task goals with rates ranging between ~0.2% to ~16%.

# clarity
The paper compares the new method to a variety of related areas, though specific comparisons to the approach taken (separating model learning from RL training) are limited. The text is fairly clear to read.

# significance
Model-based RL has a substantial community of interest, particularly at ICLR. Providing new ways to use models for improved learning - particularly when models need not be highly accurate - has potential interest to this community.

### Weaknesses
 # originality
The novel components of the work are minor: training GNNs to model dynamics is well-studied (as referenced) and model-based RL is a well-studied field. The technique can be viewed as a form of exploration prior to favor exploitation of high value actions. Previous work on exploration techniques may be relevant, as these span a variety of ways to leverage approximate models for altering action selection (https://lilianweng.github.io/posts/2020-06-07-exploration-drl/ provides a survey). While those techniques are typically applied to modify rewards during learning, the core approximate models are closely related to the paper technique.

# quality
In absolute terms the success rate is low for goal success (ranging from ~0.2% to ~16%). Whether this is an improvement is not clear as the experiments only compare to a baseline of random action. No comparisons are made to SOTA on the task domain, nor are other models applied to this problem. Adding baseline methods from prior work would improve the paper quality by showing evidence of improvement. Comparisons would also benefit from including metrics on the computational costs needed for different methods and their time and memory complexity, providing a full picture of the performance of the algorithm beyond the final goal outcome.

# clarity
The paper would benefit from an algorithm listing and figure demonstrating the overall training process workflow. These are left implicit in the text and make it difficult to follow the core algorithm.

### Questions
- Figure 1: What is the figure depicting?
- Figure 2: This figure is probably not needed as the coordinate description is clear from the text.
- Figure 3: What are the icons in this figure?
	- What do these tasks illustrate as the task being accomplished?
- Figure 4: What do the icons in Task 1 and Task 2 mean compared to the colored blocks in the other tasks? 
	- What actions do these icons indicate? 
	- At what timestep(s) of the rollout?
- Figure 5:
	- Please add uncertainty estimates for the model success rates (for example, by running multiple seeds and computing the appropriate statistics). The results look clearly different, but it is hard to tell how much uncertainty there is in the models.
	- Consider adding other baseline models to compare. Random is a reasonable lower bound, but there are no other points of comparison to judge how the current work advances over other methods.
	- What performance do previous efforts on CREATE report?
- Figure 6:
	- What do the shaded areas represent?
- To strengthen the results, consider adding some ablations of the core technique.
	- For example, how does the GNN perform without distinct edge update functions for different object pairs or without dynamic edge activations?
	- This will strengthen the claims about the need for these modifications and further will clarify how much a model can be approximate and still be useful to RL learning.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
