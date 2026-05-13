# Harmony World Models: Boosting Sample Efficiency for Model-based Reinforcement Learning

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Model-based reinforcement learning (MBRL) holds the promise of sample-efficient learning by utilizing a world model, which models how the environment works and typically encompasses components for two tasks: observation modeling and reward modeling. In this paper, through a dedicated empirical investigation, we gain a deeper understanding of the role each task plays in world models and uncover the overlooked potential of more efficient MBRL by harmonizing the interference between observation and reward modeling. Our key insight is that while prevalent approaches of explicit MBRL attempt to restore abundant details of the environment through observation models, it is difficult due to the environment's complexity and limited model capacity. On the other hand, reward models, while dominating in implicit MBRL and adept at learning task-centric dynamics, are inadequate for sample-efficient learning without richer learning signals. Capitalizing on these insights and discoveries, we propose a simple yet effective method, Harmony World Models (HarmonyWM), that introduces a lightweight harmonizer to maintain a dynamic equilibrium between the two tasks in world model learning. Our experiments on three visual control domains show that the base MBRL method equipped with HarmonyWM gains 10%-55% absolute performance boosts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Typical MBRL methods optimize for two tasks - observation modeling (aka explicit MRL) and reward modeling (aka implicit MBRL). The paper hypothesizes that there is interference between the two tasks and proposed an alternate scheme for weighing the losses corresponding to the two tasks.

### Strengths
1. The paper is well written and flows nicely.

2. The authors experiment with 4 set of environments and the results look reasonable

### Weaknesses
1. The paper calls out the following as it contribution: "To the best of our knowledge, our work, for the first time, systematically identifies the multitask essence of world models and analyzes the disharmonious interference between different tasks, which is unexpectedly overlooked by most previous work". While I agree that MBRL can be formulated could be multi-task RL problem (it is clearly multi-objective problem), the paper does not do a through job at analyzing "the disharmonious interference between different tasks". e.g. they do not study if and why there is an interference between different tasks. Note that in the multi-task literature, interference often refers to progress on one task, hindering the progress of another task. What the authors show is that adhoc setting of scalars for the different losses can hurt the performance on the RL task but they do not show that it hurts the performance on the tasks being directly optimized for. The distinction is important in the multi-task setup (which is what the paper uses).

2. While the paper formulates the problem as a multi-task problem, they do not compare with any multi-task baseline that could balance between the different losses in equation 3. So while they show that adjusting the loss coefficients help, they do not show if their approach is better than other multi-task approaches.

### Questions
Listing some questions (to make sure I better understand the paper) and potential areas of improvement. Looking forward to engaging with the authors on these questions and the points in the weakness section.

1. In equation 1, the input to the representation model $q_{\theta}$ should be $o_t$ right ?
2. The paper seems to suggest that "observation modeling" task is a new task. Is that correct ?
3. The word "harmony" in HWM - does it come from some mathematical properties or it refer to "harmony" (tuning) between the losses?
4. Regarding "the scale of L r is two orders of magnitude smaller than that of L o, which usually aggregates H × W × C dimensions", it usually doesnt matter what the dimensions of output are as the loss is averaged over the dimensions.
5. Are the findings 1, 2, 3 are new findings ?

### Soundness
3 good

### Presentation
3 good

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
This paper proposes viewing model learning from a multi-task perspective and introduces a method to adjust the trade-off between observation loss and reward loss to train the world model. Combined with DreamerV2, the proposed Harmony World Model achieves a noticeable performance improvement over DreamerV2 in several domains.

### Strengths
1. The proposed method is novel and interesting.
2. Compared to DreamerV2, there is a significant improvement in performance.
3. The paper is well-written and easy to follow.

### Weaknesses
1. Although the method proposed in this paper is novel, DreamerV3 has already addressed the issue of differing scales in reconstructing inputs and predicting rewards using Symlog Predictions. This paper primarily conducts extensive experiments in comparison with DreamerV2 and lacks more comparisons and discussions with DreamerV3. This significantly diminishes the contributions of this paper.

2. Moreover, as TDMPC is mentioned in the paper as one of the Implicit MBRL methods, I believe it should also be considered as one of the important baselines for comparisons across different benchmarks.

3. The experimental environments chosen in the paper are all easy tasks from different domains. I think experiments should be conducted in more challenging environments, such as Hopper-hop and Quadruped-run in DMC, Assembly and Stick-pull in MetaWorld, etc. Moreover, given the current trend in the community to conduct large-scale experiments, having results from only eight environments seems somewhat limited.

### Questions
See weaknesses above.

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
This paper identifies the multi-task essence (the dynamics and the reward) of world models and analyzes the disharmonious interference between different tasks. The authors empirically find that adjusting the coefficient of reward loss (which is overlooked by most previous works) can emphasize task-relevant information and improve sample efficiency. To adaptively balance the reward and the dynamic losses, the authors propose a harmonious loss function that learns a global reciprocal of the loss scale using uncertainty. The experiments show that the proposed method outperforms Dreamerv2 with a considerable gap and has better generality than DreamerV3 and DreamerPro.

### Strengths
This paper systematically identifies the multi-tasking essence of world models, which is essential to model-based methods and is overlooked by most previous work. The whole paper is well-written and easy to follow.

> The proposed method has generality to other model-based RL algorithms and significantly improves the sample efficiency.

### Weaknesses
> The novelty of the proposed method is limited. The authors build the optimization process of world models as a multi-task optimization and then use uncertainty weighting to harmonize loss scales among tasks. More state-of-the-art methods, e.g., multi-objective optimization or multi-agent learning methods, can be considered and may further improve the performance.

### Questions
> In Fig.15 & 16, HarmonyWM $ w_d=1 $ learns faster than Harmony WM at the beginning of some tasks. Could the authors give some explanations about this?

> The authors claim "the root cause as the disharmonious interference between two tasks in explicit world model learning: due to *overload of redundant observation signals* ...". Why does, for example, Denoised MDP, which identifies the information that can be safely discarded as noises, serve as a baseline in the experiments?

>  Is there a sufficient reason why the reward modeling and the observation modeling tasks are scaled to the same constant? Should we maintain the equilibrium between these tasks? Or can we emphasize some tasks at some specific states?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Harmony World Models: Boosting Sample Efficiency for Model-based Reinforcement Learning

In this paper, the authors observe that the coefficients of reward loss and dynamic loss, if not chosen carefully, could affect the performance of the final model-based RL algorithm.
And the authors propose to use a set of learnable parameters to approximate loss scale to balance the loss.
There are performance improvements introduced as shown in the experiments.

### Strengths
1. The paper is well written and easy to understand.
2. The proposed method is quite straight-forward, making it reproducible and easy to apply to existing algorithms.

### Weaknesses
1. There’s no good ablation experiments on different reward blending schemes.

    The chosen method for blending/weighting the loss terms looks reasonable, but not necessarily the best method or even the most reliable one. 

    There needs to be some other weighting methods tested in the experiment sections.

    Some simple weighting methods should be compared, which include for example the one in [1] and some other straight-forward heuristic methods.

2. It would also be helpful to show how sensitive the proposed method is. 

    Does it require separate tuning for each task? 
    
    If it needs to be tuned, how much effort is needed? Is it stable across random seeds?

3. More baselines and environments are needed.

    The proposed method is only compared against dreamerV2 in a small subset of tasks. 

    What will happen if it is compared to MuZero, TD-MPC and SimPle etc as mentioned in the paper?

    And what will happen if the algorithm is tested in similar environments such as GO, those atari environments or locomotion control tasks from image?

### Questions
The performance of DreamerV2 seems too bad in some environments like Cheetah Run, Walker Run, which is hard to figure out why considering DreamerV2 was applied to far harder problems and succeeded and DreamerV1 has better performance with the same number of training samples.

Why does it happen?

[1] Kendall, Alex, Yarin Gal, and Roberto Cipolla. "Multi-task learning using uncertainty to weigh losses for scene geometry and semantics." In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 7482-7491. 2018.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
