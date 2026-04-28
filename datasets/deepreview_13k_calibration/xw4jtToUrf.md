# Investigating Online RL in World Models

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 5, 3, 3

## Abstract
Significant advances in online reinforcement learning (RL) remain limited by the need for extensive environment interaction or accurate simulators. World models trained on large-scale uncurated *offline data* could provide a training paradigm for generalist AI agents which alleviates the need for task specific simulation environments. Unfortunately, current offline RL methods rely on truncated rollouts that can lead to value overestimation and limit out-of-sample exploration. Additioanlly, common offline RL datasets have been shows to have a bias towards healthy behavior which does not help with the development of generalizable methods. We propose an algorithm and a data curation method that addresses both of these concerns by demonstrating that effective *full-length rollout* training is possible *without hand-crafted penalties* by treating each member of the world model ensemble as a level in the Unsupervised Environment Design (UED) framework. Our method achieves competitive performance even with less transitions than the same online algorithms are traditionally trained on. We find that training a recurrent policy on an ensemble of world models is sufficient to ensure transfer to the original environment and match online PPO performance on standard offline-RL benchmarks while maintaining robust performance on our dataset, where conventional offline RL methods underperform.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel approach to online reinforcement learning. It is different from the typical approach to online interactions directly with the underlying environment (sim or real). Instead, this work studies RL methods within learned world models, attempting to mitigate common pitfalls of offline RL (reward exploitation, skewed datasets, etc.) and avoid the costly and sometimes infeasible samplings directly from the environments.

Under the settings where authors collected a more uniformly distributed dataset (in terms of state/action coverage compared to D4RL), this work trained PPO from an ensemble of independently trained world models, using Domain Randomization techniques (DR) and Unsupervised environment design (UED) methods. On the curated dataset, the experiment results suggest significant improvements over offline RL methods (CQL & SACn).

Overall, this work is novel and the results presented in the paper offers new insights to training RL agents purely from world models. If there are more experimental evidence from different tasks or environments to support the the claim that "full roll-out training inside world models is possible", and clarify the questions I have below, I would be willing to raise the score.

### Strengths
1. Originality:
- While the approach of using an ensemble of world models to reduce over-fitting and exploitation has been previously studied for model-based RL methods, this work differentiates itself by training entirely within the world model and on full-length roll-outs without any penalty terms inside learnt models.

2. Quality:
- The experiments are well-designed with clear assumptions and comparisons against multiple baselines. The use of different data scales and detailed ablation studies on the components of their method provides a thorough validation of their claims.

3. Clarity:
- The paper is well-organized with informative figures and tables. Especially figure 9 and 10, they explained how the curated dataset differs from the d4rl dataset. The writing is generally easy to follow. 

4. Significance:
- The proposed assumptions, settings, and methods are valuable to the RL research community as it shows preliminary positive results on smaller scale world models, which could potentially serve as basis for training RL agents within larger and more capable world models on more complex tasks.

### Weaknesses
1. While the paper presents results from multiple tasks (pendulum, half-cheetah, cartpole, hopper), there is a lack of extensive testing across a wider variety of environments and tasks. This raises some questions about the robustness and generalizability of the proposed method beyond the tested scenarios. Perhaps some tasks such as ant-maze or robot arm manipulation ones.

2. The ensembles of world models seems essential to the proposed method. A sweep over the numbers of world models in the ensemble v.s. tasks' performance could reveal more information on how many world models are needed to achieve certain level of task performance. It is unclear how sensitive the method is to the size of the ensemble, and whether there is a point of diminishing returns.

3. Minor typos:
- Line 131: This setting Furthermore
- Line 509: the type (of) increasingly available large-scale datasets

### Questions
1. "Each of the baselines is tuned by doing a grid search of the ranges documented in their respective papers:
- Is the grid search conducted over their original dataset and transferred to the curated dataset? Or is the grid search done on the curated dataset?

2. What would happen if the proposed method is trained and evaluated on the d4rl datasets? In the current paper, we see baseline methods do not perform as well as the proposed method under the paper's settings. The authors argued d4rl dataset is biased towards the baseline methods and provided visualizations. However, it would still be interesting to see how it impacts the proposed method.

3. "We open source all our code and data to facilitate further work in this exciting direction."
- I couldn't find a link to the code repo, or find any supplementary materials.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the potential of using uncurated offline data to train world models that can serve as a training ground for reinforcement learning. The primary goal is to enable the transfer of learned policies from these world models to the real world, thereby reducing the reliance on task-specific simulation environments. The authors demonstrate that by ensembling multiple independently trained world models, they can achieve robust transfer to the real world, even when the offline datasets are much smaller than those typically used in offline RL.

### Strengths
The paper presents a novel approach for training RL agents using world models derived from large-scale, uncurated offline data. By employing an ensemble of world models trained on the same dataset and leveraging them to create learning curricula through the Unsupervised Environment Design method, this work introduces a fresh perspective to RL.

### Weaknesses
 - In my view, the main issue with this paper is that it somewhat exaggerates the contributions of the proposed method. The title, "Investigating Online RL in World Models," is slightly misleading, as the study addresses an offline RL problem. Additionally, the term "world models" could be confusing. While the paper discusses many existing visual world model approaches (such as Ha and Schmidhuber's NIPS 2018 paper and recent interactive video generation studies), it does not actually work with visual data, instead focusing on fully observable MDPs in low-dimensional state spaces. I suggest the authors consider replacing the term "world models" to more accurately reflect the context.

- The organization of the paper is also disjointed, with an imbalanced structure. For example, Chapter 2 uses considerable space for background information, while the methods section in Chapter 3 is relatively brief. This structure makes it challenging for readers to fully grasp the paper's core contributions.

- In methodology, the authors treat world models trained on offline data of varying quality as different levels in an unsupervised environment design approach. I recommend that the authors discuss the motivation and rationale for this choice, explaining why this training method would lead to a robust and transferable policy. Specifically, the paper lacks a clear explanation of how varying the quality of offline data translates to a meaningful curriculum for policy learning. The connection between the diversity of the offline data and the resulting world models is not well-established, making it difficult to understand why this approach would lead to robust policies.

- While the paper outlines an ambitious story, it lacks sufficient experimental support: 
(1) The authors claim to use the D4RL dataset but do not provide comprehensive experimental results across different tasks. The focus on the relatively simple Hopper task is insufficient to support their claim. The paper should include results on a wider range of D4RL tasks to demonstrate the generalizability of the approach. 
(2) The paper lacks comparisons with recent offline RL methods, as well as more detailed model analysis, such as examining the impact of the number of world models --- The authors mention training 100 world models in line 77, which seems excessive for a simple Hopper task and introduces considerable training overhead, which raises questions about the method's practical use in real-world applications. The paper should include an ablation study on the number of world models to justify this choice and understand its impact on performance and computational cost.

### Questions
- Could the authors provide additional experiments on visual offline RL tasks to demonstrate the world model's generalizability in open-world or visual environments?
- I strongly suggest that the authors further discuss the impact of the number of world models on the experimental results and clarify the necessity of using 100 world models.
- If possible, please refine the methods section to more clearly highlight the core contributions of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper combined Unsupervised Environment Discovery (UED) and world model ensembles to provide a method for offline model-based RL that is sample-efficient. It treats different world models as levels within the PLR curriculum method in UED. It evaluates the method on vector-based cartpole, hopper, half cheetah, and pendulum tasks.

### Strengths
- the paper performs an interesting combination of UED and world models, considering each world model as a level in UED
- the method doesn't rely on online tuning in the environment (and uses held out world models to tune hyperparameters)
- the results demonstrate sample-efficiency gains compared to CQL and a vanilla world model baseline

### Weaknesses
 - The differences with other model-based offline RL methods like MOPO [1], MBPO [2], Planning with Diffusion [3] is not clear, especially since the world model in the experiments in this paper, unlike David Ha's work, is just a simple MLP. 
- It would be helpful to compare with other offline MBRL methods like the ones above as well as world model based approaches like IRIS [4] and Dreamer [5], particularly on more challenging environments with image observations than the vector observation based  locomotion environments. Detailing the differences with these world model based methods would also be useful
- Other papers to discuss in the related work include sample-efficient BC approaches that can work with very few demonstrations like ROT [6] and MCNN [7]. In summary, this work could use more comparisons (or atleast discussions comparing) to other works on offline MBRL, world models, and sample-efficient behavior cloning as well as evaluations in more challenging environments with image observations.

Minor comments:
- the return plotted for different methods is not normalized --- this makes it hard to determine its performance between random and expert and hard to compare with other papers
- confusingly, "inside world model" is referred to as "simulation" and "in simulation" is referred to as "real world"
- Appendix A.3 is empty

### Questions
Please see weaknesses above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates online reinforcement learning directly within world models without conservative constraints typically used in offline RL and proposes to combine ensemble world models and prioritized level replay to tackle this problem.

### Strengths
- The motivation to perform online RL directly in world models is timely and relevant.

### Weaknesses
1. The method is confusing. What is the $\delta$ in Equation (5)? Why the Equation (5) approximates the regret? The right side of Figure 1 is difficult to understand. I suggest adding pseudocode to clarify the algorithm.

2. The paper structure and writing need significant improvement. For example, the introduction lacks a clear statement of contributions. The relationship between contextual MDP subsection in Preliminaries and the reset of paper is unclear. The Preliminaries section is too long.

3. The dataset construction method appears similar to D4RL. Both record the encountered transitions from randomness to expertise during training. Why the authors claim that D4RL is adversarial in data coverage (line 55) and CQL and TD3+BC does not inform this (line 263)? The data coverage is a common concern when building offline RL datasets, and previous benchmarks typically offer choices with various data coverage (D4RL and Atari DQN-Replay[1]).

4. The checkpoint frequency seems uniform based on Figure 2, despite claims of heuristic selection. At the 5th ckpt, the agent has basically converged. The distribution perhaps change little after the subsequent sampling. Should the sampling frequency be increased between the first few ckpts?

5. The world model architecture (simple MLP with current state and action as input) seems overly simplistic compared to state-of-the-art approaches like RSSM, Transformer, or diffusion models. Since the authors assumes that learning is done within a generalist world model (line 58 and 87), the experiment results of MLP with no historical trajectory are not convincing. I even suspect that using a single SOTA architecture world model can already solve this problem.

6. Based on Figures 4-6, the DR methods perform well, and the proposed PLR methods do not show clear advantages.

7. Judging from the rendering results of the `ref` and `cite` commands, this paper does not use the ICLR 2025 template!

### Questions
1. What is the size of the collected dataset in terms of transitions?
2. Could you provide pseudocode for the algorithm to aid understanding?
3. Why were existing implementations of CQL[1] and SAC_N[2] not used?
4. There are numerous typos that hinder readability. Such as incorrect citation format (line 51 and 53), "This setting Furthermore, they showed ..." (line 131), "Therefore, the policy’s minimizes ..." (line 136), "Prioritized Level Replay as described in with an ..." (line 305) and so on.
5. The abstract states that "training inside world models is usually studied in the context of offline RL." However, many online RL algorithms (e.g., MBPO, Dreamer, TD-MPC, IRIS, TWM, STORM) train agents entirely with imagined trajectories (i.e., within world model). On the contrary, most of the offline model-based RL seems to be based on the Dyna framework, that is, using both offline datasets and world model imagination trajectories to train the agent.

[1] https://github.com/young-geng/JaxCQL

[2] https://github.com/Howuhh/sac-n-jax

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of training online RL models inside world models. For this they rely on an ensemble of world models to train agents in an online fashion, without any offline penalties. The proposed method is evaluated on robotics tasks including Cartpole, Halfcheetah and Hopper.

### Strengths
The paper investigates an interesting question, that is, whether RL agents can be trained online inside world models, without the need for constraints required in offline RL.

### Weaknesses
The presentation of this paper can be improved. For example, Figure 1 is confusing and lacks a detailed figure caption to explain what’s going on. Dataset distributions of offline RL datasets are criticised in the Discussion section, which feels out of place (also as this section comes after Related Work). Instead of bringing these results after the main experiments, they could be seen as a motivation before the main experiments (which would require experiments that support the motivation).

It is unclear where the proposed method starts and ends, or what the authors consider as their own method. Instead, 6 different variations (PLR, PLR_PVL, DR, DR_STEP, DR_PROB) of ensemble world models are tested against a single world model (WM).

In the current form, the paper lacks convincing empirical evidence. The main experiments are conducted on toy tasks like Cartpole, Pendulum, Acrobot, Hopper and Halfcheetah. Across most environments (Figure 4, 6, 7), the ensemble methods (PLR, DR, PLR_PVL, DR_STEP) tend to learn faster than a single model (WM) but reach the same level of performance. Furthermore, there is a lack of offline RL baselines (only CQL is provided). Also, there’s a lack of ablations on components of their method. For example, what is the effect of the size of the ensemble?

The proposed method relies on an ensemble of world models. Training an ensemble of world models is feasible in the toy tasks considered currently, but raises questions on scalability of the proposed methods to more complex environments, such as visual domains. Consequently, reporting information on the additional cost of training and during evaluation of those models would benefit the paper.

### Questions
- What is the size of the world model ensemble used in your experiments? What is the effect of the number of world models? 
- What is the additional cost of training and evaluating using an ensemble? 
- How does your method transfer to other benchmarks (e.g., Atari, Procgen, Meta-World, etc.) with regard to efficiency at training and inference time?

### Soundness
2

### Presentation
1

### Contribution
2
