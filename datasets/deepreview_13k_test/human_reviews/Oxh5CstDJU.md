# TD-MPC2: Scalable, Robust World Models for Continuous Control

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model. In this work, we present TD-MPC\textbf{2}: a series of improvements upon the TD-MPC algorithm. We demonstrate that TD-MPC\textbf{2} improves significantly over baselines across $\mathbf{104}$ online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single set of hyperparameters. We further show that agent capabilities increase with model and data size, and successfully train a single $317$M parameter agent to perform $\mathbf{80}$ tasks across multiple task domains, embodiments, and action spaces. We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC\textbf{2} agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces TD-MPC2, an extension of the TD-MPC algorithm that introduces a set of improvements. TD-MPC is a model-based algorithm that performs Model-Predictive Control (MPC) in the latent space of a learned world model, and bootstraps the value of the final state on the planning horizon with a learned value function obtained via a model-free RL algorithm.
The introduced improvements include novel architectural designs (e.g., Layer Norm), using maximum-entropy RL as the policy prior, and, most importantly, a multi-task world model capable of learning the dynamics of several tasks with a single set of parameters. The experiments evaluate TD-MPC2 with TD-MPC, as well as with model-based and model-free SOTA algorithms, on several multi-task settings.

### Strengths
* The paper is well-written and organized, and includes a thorough discussion of the relevant related works.

* The experimental results showcase impressive performance gains over the state-of-the-art on a wide range of robotics tasks (e.g., DM-Control, Meta-World) and settings (e.g., multi-task, few-shot learning).

* The authors provide model checkpoints, datasets, and code for training and evaluating their proposed method. This significantly facilitates reproducing the experimental results and extending the introduced method.

### Weaknesses
* The method is not directly applicable to domains with discrete action spaces.

* Because the proposed method relies on MPC, it inherits a few of its drawbacks (e.g., decision-time computational overhead, difficulty handling multi-modal transitions).

* A few algorithmic decisions of the method could be better motivated, e.g., by giving an intuitive explanation of why they are expected to bring benefits. For instance, the discussion on why using SimNorm and how it biases the representation towards sparsity could be improved with an intuitive explanation of Eq. (5).

### Questions
Below, I have a few question and constructive feedback to the authors:

1) Why did you decide to use the Mish activation function? Did it provide significant improvements compared to other commonly used activations, e.g., ReLU?

2) I am not sure that it is possible to claim that MPC is a closed-loop policy, even when it considers the terminal value function at time step $H$. For instance, if Eq. (6) was maximized over a sequence of policies $(\pi_t,...,\pi_{t+h})$ instead of a sequence of actions $(a_{t},...,a_{t+h})$, it could result in a higher value. See Eq. (2) of [1] as an example. I believe this could lead to sub-optimal behavior in highly stochastic or multi-modal environments.

3) Recently, [2] also showed performance gains via Layer Norm and Dropout. Is this related to how Layer Norm and Dropout were used on TD-MPC2? I suggest discussing these techniques in more depth.

4) “SAC and DreamerV3 are prone to numerical instabilities in Dog tasks”. Could you elaborate on which numerical instabilities, and why TD-MPC2 can avoid them?

5) “At the same time, extending TD-MPC2 to discrete action spaces remains an open problem.”
I suggest elaborating what are the challenges involved in applying TD-MPC2 on discrete action spaces.

Minor:
- Below Eq. (3), it is missing a $\gamma$ in the TD-target $q_t = r_t + \gamma Q$.

[1] Online Planning with Lookahead Policies. Yonathan Efroni et al. NeurIPS 2020.

[2] Dropout Q-Functions for Doubly Efficient Reinforcement Learning. Hiraoka et al. ICLR 2022.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents TD-MPC2, which is an upgrade for the model-based RL algorithm TD-MPC. The method is evaluated across a large number of RL tasks including multi-task RL benchmarks. The results show a significant boost of performance compared to other model-based RL baselines especially for Multi-task RL.

### Strengths
1. The method is evaluated on a large number of tasks in different domains. It's nice to see the huge boost of performance in multi-task scenarios.

2.  The model checkpoints and code are provided. All the hyperparameters are also provided in the appendix.

3. TD-MPC is one of the state-of-the-art model-based RL algorithms so it's great to see an upgrade to it.

### Weaknesses
From the results in appendix, it seems that in single task cases, TD-MPC2 is better than the original TD-MPC in terms of only a few more complicated tasks, is that true?

The novelty is somewhat limited as the modifications to TD-MPC seem to be all from some other existing methods.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces TD-MPC2, which incorporates improvements over a strong model-based RL baseline called TD-MPC. The improvements focus on generalization across tasks and action spaces. Experiment results show that TD-MPC2 is a viable method for continuous control tasks and is less sensitive to hyperparameters, and that it benefits from scaling both model and data sizes.

### Strengths
1. TD-MPC2 is a strong model-based RL method that doesn't require significant task-specific hyperparameters tuning.
2. The paper is very well-written.
3. Extensive experiment results.

### Weaknesses
The study on multi-task learning is a bit unsatisfying, mainly due to the limited (and somewhat artificial) setup of the training data which was obtained from the replay buffers of the single-task TD-MPC2 agents. It would be great if the authors could consider extend their studies to more realistic training data distribution, e.g. mixture of few expert demonstrations and massive suboptimal data as prevalent in robotics.

### Questions
On multi-task setting:
1. Have you considered training the multi-task model online?
2. Have you explored other dataset setups, i.e. different random to expert ratios?
3. How about the impacts of task diversity, i.e. ablation on number of tasks in the training data?
4. How do the multitask model perform compared to single-task models on each individual tasks?
5. Have you considered leveraging offline RL techniques when learning from the fixed multi-task dataset? Do you think they can help?

Other questions:
1. The observation that TD-MPC's performance decreases as model and data sizes increase is very interesting. Do you have any hypothesis of why that's the case?
2. How did you do hyperparameter search?
3. Does TD-MPC2 benefit from model size scaling on single-task setting?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes TDMPC2, which is a series of improvements over TDMPC for model-based RL in continuous domains. As far as I can tell, the following are the key differences:

** Changes to make the algorithm multi-task **
- Adding e (learned task embedding) to all components of the TOLD model.
- Zero-padding invalid dimensions for observations and actions.
- Handling differing reward magnitude by using cross-entropy instead of squared error for reward and value prediction losses.

** Architectural changes **
- SimNorm
- Using an ensemble of Qs

** Other changes **
- Including an entropy bonus in policy optimization objective, following maximum entropy literature.

As far as I can tell, the planning algorithm remains unchanged.

(If I have missed anything important, please let me know.)

The proposed modifications lead to large improvements over TDMPC when scaled up to larger model sizes, and enable multi-task learning.

### Strengths
- The introductory figure on page 1 is a great idea, it works very well at describing the results at-a-glance and gets the reader interested to see more.
- The paper is organized well and provides clear descriptions of the approach.
- Experiments are thorough and convincing. Results are extremely favorable compared to other SOTA approaches like DreamerV3 and TDMPC. Ablations are also provided to delineate the impact of each modification.
- Figure 7 (right) is very interesting, thank you for providing this visualization of the task embeddings.
- Code, data, models are provided open-source. Training GPU costs being provided in Table 1 is also a plus.

### Weaknesses
I believe this paper should be accepted on the merit of the strong results and presentation. However, there are some major concerns I have that would be great to address in the next revision.

- My main suggestion, *highly recommended*, is for the authors to include in the main text a list of the differences from TDMPC. There will be many readers (like myself) who are familiar with TDMPC, and we'd like to be able to understand the differences at a glance. The way the paper is currently written, the authors have described the full algorithm from first principles, but this mixes together their contributions versus TDMPC's contributions. At best, this causes confusion, while at worst, a reader may incorrectly attribute credit for an idea to this paper rather than the original TDMPC paper. A concrete example is the section on the planning algorithm; rather than a  vague sentence at the end saying "Refer to [the TDMPC paper] for more details about the planning procedure" (which hides whether or not there are any differences), it would be good to start off with a direct statement like "The planning procedure is unchanged from [the TDMPC paper]; we re-describe it here so that this paper can be self-contained." Or, if there are minor changes, you can describe them candidly.

- Another smaller suggestion: There are some parts of the paper that feel like too much overselling of what is ultimately a couple of modifications from TDMPC. The sentence which got me feeling this way was "TDMPC2 marks the beginning of a new era for model-based RL". It's great if the authors feel that way about their own work, but in a scientific paper I would prefer the language to remain neutral, and to allow the reader to form their own judgment about these matters.

- I have included several smaller questions below that should be addressed in the next revision as well.

### Questions
- How does the DreamerV3 baseline work, doesn't that algorithm expect discrete action spaces (as discussed in Section 5)?
- I'd like some clarifications on the task embeddings e. Are they just trainable vectors that get passed as input to all components of the TOLD model? What forces them to be meaningfully diverse from each other in a way that is consistent with the semantics of the tasks? Is there some extra term in the loss function for them?
- "minimum of two randomly sub-sampled Q-functions" Why not just take the minimum over all 5?
- "reward and value prediction as a discrete regression" Are there limitations arising from this due to the resulting lack of expressivity? Or is the discretization fine enough that a wide enough range of value functions can be effectively learned? What are the tradeoffs of increasing or decreasing the granularity of this discretization?
- The SimNorm contribution is interesting. Is it fair to think of it as a different method of achieving the same effect as the vector-of-categoricals approach in Appendix G of the Director paper (https://arxiv.org/abs/2206.04114)?
- "extending TD-MPC2 to discrete action spaces remains an open problem" What are the challenges here?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
