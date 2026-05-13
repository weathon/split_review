# V-Former: Offline RL with Temporally-Extended Actions

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
In this paper, we propose an offline reinforcement learning (RL) method that learns to take temporally extended actions, can handle narrow data distributions such as those produced by mixtures of multi-task demonstrations, and can train on data with different control frequencies. This combination of properties makes our proposed method especially well-suited for robotic offline RL, where datasets might consist of (narrow) demonstration data mixed with (broader) suboptimal data, and control frequencies can present a particularly significant challenge. We derive our method starting from a continuous time formulation of RL, and show that offline RL with temporally extended “action chunks” can be performed efficiently by extending the implicit Q-learning (IQL) approach, in combination with expressive Transformer-based policies for representing temporally extended open-loop action sequences. Our experiments show that our method both improves over prior approaches on simulated robotic demonstration data and outperforms prior works that aim to learn from data at multiple frequencies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on handling data with different qualities (suboptimal) and different frequencies. The paper proposes a method, V-former, which utilizes the idea of “action trunks” and a transformer-based policy. Concretely, it extends the value function of Implicit Value Learning to bootstrap with multiple steps actions and uses the transformer policy to roll out multiple steps. In five robomimic tasks with different data qualities and kitchen tasks with different data frequencies, the proposed method shows better performance than baselines.

### Strengths
- The paper is well-organized and clear.

 - The method section is easy to follow.

### Weaknesses
 - The method is straightforward, and the contribution is limited. The main technical contribution of the paper is extending the value function of IVL and making it consider the outcome of multiple timesteps, which I believe is not significant enough. The underlying insight that modeling multiple steps to help handle multimodality is already known in the literature.

 - The experiment evaluation is not thorough enough. The baselines are mostly ablation of the proposed method. Moreover, there are other existing offline RL methods that also can be applied to the problem of interest, such as IQL. The limited set of experiments makes the significance of the proposed method hard to evaluate.

### Questions
- The evaluation in Table 1 is interesting and shows that VF can achieve good performance if proper N and k are selected. However, the optimal N and k may be quite different for different tasks. Instead of manually selecting them, will there be a general way to derive them from the offline dataset?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes V-Former, an offline RL algorithm to learn from suboptimal, multi-modal, and non-Markovian data with different control frequencies. To address these challenges, the authors first extend implicit V-learning to arbitrary frequencies, and then train a Transformer policy with advantage reweighting to produce temporally extended actions. The empirical results show that V-Former can adapt to time-heterogeneous datasets and outperform its per-timestep or BC variants.

### Strengths
This paper aims to address some important questions in offline RL. It is clearly written and the proposed algorithm is novel to my knowledge. The idea of using Transformer to generate temporally extended "action chunks" sounds interesting.

### Weaknesses
While well-motivated, I have some major concerns about the methodology and experiments of this work:

1. What value is $V_\psi(s)$ modeling in value learning? According to Equation 5-9, it seems that $V_\psi(s)$ is trying to approximate the value of the optimal single-step policy with the n-step Bellman equation. However, $V_\psi(s)$ is proposed to model the value of arbitrary action frequencies or action lengths that should have different values, which is confusing to me.
2. Compared to previous offline hierarchical RL works, what's the advantage of the proposed method? These works [1, 2, 3] also aim to solve similar tasks.
3. I am worried that the experiments are insufficient to support that V-Former is a strong baseline for offline RL, as we can only see ablations of V-Former on action chunking and advantage weighting, missing the performance of other state-of-the-art offline RL and offline HRL baselines. Moreover, Section 5.3 shows that the optimal action chunk size is around 3 in Robomimic tasks, which makes it hard to distinguish the effect of temporally extended actions. Therefore, I suggest authors compare the performance of V-Former and other baselines on tasks that may benefit from longer horizon control, such as *antmaze* and *kitchen* in D4RL.

Minor questions:

1. How to choose the hyper-parameter N? It is unclear to me the criteria for choosing N in different environments during evaluation.
2. The results in Section 5.1 and 5.3 indicate that open-loop control can achieve the best performance. However, Section 5.2 uses a close-loop VF for evaluation. Can authors provide some intuitions behind this choice?

### Questions
There are some questions and concerns, which I have outlined in the previous section.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present an offline RL approach built on implicit Q/V-learning, extending the original formulation to n-steps, enabling offline value learning from arbitrary-length actions. They further formulate the Bellman equation in a continuous-time MDP, therefore supporting learning over multiple datasets with distinct temporal frequencies, as is commonly available in robotics. The authors train open loop, multistep transformer policies, taking temporally extended actions, with advantage weighted regression, learning from suboptimal data, outperforming prior approaches on robotic benchmarks w/wo multiple temporal frequencies.

### Strengths
1) Extending implicit V-learning to n-steps is intuitive and well motivated.
2) Results are impressive, especially on increasingly suboptimal datasets.
3) Table 4 ablation study is appreciated.
4) Paper is well written and the approach should be simple to implement and adopt by the wider community.

### Weaknesses
1) The authors do not report confidence intervals in many of their results
2) Only 3 random seeds were ran, which is very low
3) Setting the action chunking length as a hyperparameter seems restrictive. Wouldn’t it be better to learn dynamic chunking lengths, based on the task and state? E.g., wouldn’t something more akin to “options” [1,2] work better here?

### Questions
Could the authors comment on what the choice of ‘n’ in Eq 9 has during learning?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a transformer-based offline RL method. It first introduces an "implicit V-learning" algorithm (similar to IQL) that can be extended to multiple timesteps. It then learns a transformer-based policy via a weighted behavior cloning objective, where the weight depends on the temporally extended learned value function. The method is evaluated on several continuous control benchmarks including the Robomimic and Franka Kitchen.

### Strengths
**originality**: Although the idea of "implicit V-learning" has been used in several prior works, this paper proposes to extend the learning objective to multiple timesteps. Moreover, the combination of IVL and transformer-based policy learning is novel.

**clarity**: I find this paper generally well written and easy to follow.

### Weaknesses
My main concern is on the experiments, which I don't find sufficient enough to demonstrate the strength of the proposed method as an offline RL algorithm.

First, the evaluation was conducted against some variants of the proposed method (which seems more like ablation studies to me) but didn't consider any existing offline RL baselines (which I don't see any limitations in the settings that prevent one from doing so).

Second, the experiments were conducted only on expert datasets, and *suboptimal datasets* (expert + random data) which were a bit artificial. While it's known that the performance of offline RL / imitation learning methods varies drastically depending on the data quality, it's important to evaluate the method on datasets of various optimality, and especially on those which are similar to real-world settings, e.g. the multi-human datasets from Robomimic.

Lastly, the proposed method seems sensitive (task depedent) to certain critical hyperparameters, including the "action chunk size". But experiments only cover a small range of those parameters. I believe more extensive ablation studies would be helpful to show if the method is robust and generally applicable to various continuous control problems.

### Questions
1. Why not including established baselines, e.g. BC-RNN, BCQ, CQL (which were used as baselines in the Robomimic paper), and transformer-based baselines like Decision Transformer and Trajectory Transformer?

2. How are the success rates in Fig 3 normalized? Why are some greater than 1?

3. The expert + random datasets seem a bit artificial. Why not evaluating on the existing multi-human datasets (which were generated by human operators of different level of proficiency on the tasks) from Robomimic instead?

4. What's your intuition on selecting an optimal range of N?

5. As noted in the appendix, different weight functions f(x) were used in the Robomimic and FrankaKitchen experiments. It would be nice to include an ablation table for both f(x) on both environments to show how sensitive the method is to f(x). 

6. Have you tried evaluating the method on tasks with discrete action spaces, e.g. maze?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
