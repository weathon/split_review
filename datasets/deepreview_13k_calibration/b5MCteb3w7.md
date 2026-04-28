# Actions Speak Louder Than States: Going Beyond Bayesian Inference in In-Context Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3

## Abstract
In this paper, we investigate in-context learning (ICL) for reinforcement learning (RL), particularly extending beyond Bayesian inference to more advanced and richer learning paradigms in transformers. Transformers have shown promise for few-shot and zero-shot learning, but their capabilities for ICL in RL environments are not well explored. Our work studies the role of task diversity in RL environments on the downstream ICL capabilities of transformers. To do so, we introduce a novel RL benchmark, developed to provide a rich variety of tasks, essential for this exploration. Through this environment, we not only demonstrate the critical role of task diversity in facilitating advanced learning algorithms like transformers but also investigate the effects of model architecture, regularization, and other factors on the learning process. This study marks a pivotal advance in understanding the dynamics of ICL in RL, showcasing how diverse tasks can drive transformer models to surpass traditional learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an analysis of In-Context Learning (ICL) in Reinforcement Learning (RL) and introduces a new benchmark based on Omniglot for evaluating ICL in RL. Using this benchmark, the authors demonstrate how factors such as the number of tasks in the pretraining dataset, architectural hyperparameters of the transformer, and regularization techniques influence the ICL capabilities of a GPT-2-based transformer model trained to autoregressively predict the next action.

### Strengths
- The analysis of how the number of tasks in the pretraining dataset and model capacity impact ICL abilities in RL provides valuable insights into the effectiveness of framing RL as an autoregressive problem.

### Weaknesses
 - In addition to the factors considered in the paper, I think it would be beneficial to include an ablation study on the impact of sequence length on ICL abilities for RL.
- See the Questions section for additional clarifications.

### Questions
1. What is the specific sequence that is used as input to the transformer?

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
3

### Summary
This work discusses the factors affecting the generalization capabilities of an In-Context Learning (ICL) approach in the Reinforcement Learning setting. It especially focuses on how transformers can surpass Bayesian inference limitations for ICL. One of the main factors studied in this work is the task diversity. This factor has been studied theoretically and empirically, showing the importance of a diverse set of tasks to train the ICL algorithm. As mentioned, since the diversity of the existing RL environments (e.g., Mujoco) is not enough to show highly diverse tasks, this work proposed a novel benchmark based on the Omniglot dataset, offering unprecedented task diversity. Aside from task diversity, other factors like model capacity (Sec. 4.4.3), regularization techniques, and augmentation strategies (Sec. 4.4.4) have been studied. The empirical results have shown the importance of task diversity when learning an ICL algorithm with transformers.

### Strengths
- The problem discussed in this work is important. The motivation for the problem was relatively clear. 
- The empirical results were enough to show the importance of task diversity.
- The ablation studies were comprehensive illustrating the other important factors in designing an ICL algorithm in RL based on transformers.

### Weaknesses
1. The paper claims to work in in-context *reinforcement* learning setting. However, the authors prepend the task description (line 328) during the evaluation on the test data.

    On the contrary, the ICRL methods, such as AD [1] or DPT [2], do not precondition on the task. The whole idea of ICRL lies in the adaptation to the uncertainty (i.e. solving unseen tasks) without updating the model weights. In the proposed Omniglot environment, conditioning the model on the final state (task) leaves no uncertainty to adapt to, making the setting goal-conditioned. The core challenge in ICRL is to learn a policy that can adapt to new tasks from a distribution with minimal data, but by providing the goal state, the authors are bypassing this challenge, effectively turning the problem into a goal-conditioned RL problem rather than a meta-RL or ICRL problem.
    
2. The main metric authors use for making conclusions about in-context abilities is the L2-loss on the test tasks. This approach is known to be inconclusive [3]. Instead, it is better to report total return over a trajectory, given the work is claimed to be exploring the RL setting. The use of L2 loss on pixel space is particularly problematic, as it is not directly indicative of task success or policy quality. A small L2 loss could correspond to a visually similar but semantically incorrect trajectory, and vice versa. This makes it difficult to assess whether the model is truly learning to solve the tasks in-context.
3. In some places in the paper, the authors report “Reward” (I guess it is actually a return, total sum of rewards on a trajectory). However, it is hard to estimate how well the model solves the tasks based on MSE. It is more common to use mean success rate [1, 2] or some n-th percentile success rate [4]. For the reason it is a challenging task to construct a success rate for such an environment, the Omniglot benchmark may not be a good choice. The lack of a clear success metric makes it difficult to compare the performance of the proposed method with existing ICRL or meta-RL approaches. A success rate, even if approximated, would provide a more intuitive understanding of the model's ability to complete the tasks.
4. In Appendix C, the authors claim they show how transformer changes its regime from Bayesian inference by training on increasing number of tasks. However, I am not quite satisfied with this argument. Indeed, when the number of tasks increases, transformer learns to reason in-context, rather than to replicate strokes from its weights. At the same time, this effect has no connection with Bayesian inference, but it is an example of overfitting. Surely, a sufficiently large model can learn to copy a small dataset, but one would not call it Bayesian inference. The authors' interpretation of the observed behavior as a transition to Bayesian inference is not well-supported by the evidence. The observed behavior could be explained by the model's capacity to memorize training data, rather than a fundamental shift in its reasoning mechanism.
5. Authors claim to offer a benchmark with “unprecedented task diversity”, however, the datasets and benchmarks with at least similar diversity exist. For example, XLand [4] (and its open sourced analogue XLand-Minigrid [5] with datasets [6]) offers a tree-like structure of tasks, which is considered challenging. The claim of unprecedented task diversity is not substantiated, as other benchmarks offer comparable or even greater diversity. The lack of a rigorous comparison with existing benchmarks makes it difficult to assess the true novelty and challenge of the proposed environment.
6. The statement given on line 85 concerning slow adaptation of Meta-RL vs. ICRL is not true.  Сonversely, if one consider AD [1] and VariBAD [7], the latter method requires much less episodes to converge to the optimal solution in Dark Room environment, which highlights the effectiveness of Meta-RL methods over ICRL.

### Questions
I have mainly one important question besides some requests I provided in the weaknesses section:
- **What measure of task diversity has been used in this work?** This is crucial to understand the benefit of introducing the novel ICL benchmark and the limitations of the existing RL environments. I understand from the theoretical section that diversity is about covering the true set of pre-training task distribution, but empirically, it is unclear.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the emergence of in-context reinforcement learning (ICRL) in transformer models, presenting a quantitative analysis on the task variety, model depth and data augmentation techniques required for ICRL to emerge. The authors also propose a new benchmark, which as they claim, surpasses other available datasets and environments in task diversity. Also, authors theoretically show that the performance of the in-context methods is indeed bounded by the diversity of task in the training dataset.

### Strengths
- Theoretical contribution: decomposition of pretraining data into two task coverage classes and showing the performance bounds.
- To my knowledge, the first attempt to explore scaling of in-context *reinforcement* learning models, so it is a valuable engineering contribution.
- The paper is generally well-written, the theoretical part is clearly explained.

### Weaknesses
While the premise looks promising, I believe that this paper needs more refinement and revision before it can be helpful.
* I found it difficult to understand what $M_{\theta}^{E-PS}$ looks like in practice. Neither $\mathbfcal{T}$ (the true set of train+test tasks) nor $\hat{g}(\cdot|\cdot)$ (prior/posterior over tasks) seem to be available in practice. Perhaps it would be helpful to include an algorithm for each of $M_{\theta}^{E-PS}$ and $M_{\theta}^{F-PS}$ in the appendix.
* There is a large disconnect between §3.1/3.2 and §4. In §3.1.2, we are introduced to two different action predictors $M_{\theta}^{E-PS}$ and $M_{\theta}^{F-PS}$, and we study their regret behavior in §3.2. But where do these two go in §4? There is no mention, comparison, or even justification for why one might not have been possible. Perhaps the authors should add a few paragraphs to connect these two sections, e.g., how do the findings in §3 help the implementation in §4, etc.

    I would be happy to learn how these are connected, or be notified that this question is already answered in the paper.
* I found it difficult to understand the Omniglot-based benchmark, and had to reread §4.1 several times before I understood it. It would be very helpful to include a visualization of the Omniglot task, even if in the appendix. For example, for 3-5 "trajectories", show what the corresponding states, actions and rewards would be. This visualization is independent of the transformer + ICL based approach that you propose.
* While the comparison to MAML is appreciated, there are other relevant baselines to compare to. To start with, see [1, 2]. As of now, there are few things to learn from the evaluation. The general lesson is that to lower the test loss of this specific technique, we need higher task diversity, larger models and more regularization/augmentation. Unfortunately, these points are not surprising. What would be interesting would be to see that while this specific technique benefits from larger model capacity, baselines do not. Or that more diversity does not change baseline behavior while this technique benefits from it.

### Questions
1. Following Weakness #1 and the statement give on line 317, why do authors consider the task impossible to achieve without seeing the goal? Would not it be enough to learn to follow the reward signal, as it is done in many prior ICRL methods?
2. In the MAML experiment, the model sees the last five strokes, while the transformer contains last 2 **episodes** in its context. Why do authors choose MAML to compare with Meta-RL, given it is not a memory-model? To my mind, the paper would benefit from the comparison with the recent SOTA in Meta-RL: Amago [8].
3. For the main plots (Fig. 3, Fig. 5) the authors report it would be beneficial to see multi-seed averaging. This information would be helpful to access the stability of in-context models.
4. Can the authors release the training hyperparameters in a single table? I understand that there were plenty of experiments, but I would appreciate seeing hyperparameters of the best performing models at least.
5. In AD [1], it is reported that enlarging sequence length can also be beneficial to in-context abilities of transformer. Such an experiment with different sequence sizes would maybe shed some more light on the question of in-context emergence. Comparing tradeoffs between sequence size vs. task diversity is also an interesting detail.
6. I am colorblind, cannot see one graph. Appreciate if in the next revision the style would change.

Although I assess this work as a rejection, I would be happy to discuss the paper during the rebuttal to understand authors’ motivation and then to revise my score.

[8] Grigsby, Jake, Linxi Fan, and Yuke Zhu. "Amago: Scalable in-context reinforcement learning for adaptive agents.”

### Soundness
2

### Presentation
2

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
This paper focuses on in-context RL, where a transformer model has to predict next actions for a pseudo-optimal policy, given the trajectory so far. The transformer is pre-trained on logged data from a optimal policies in a set of MDPs. This work proposes that such architectures can surpass traditional bayesian inference and generalize beyond the MDPs observed at training time. They repurpose the Omniglot dataset to form a new benchmark for evaluating their ideas.

### Strengths
* This work focuses on a timely problem regarding in-context RL.
* A new benchmark is created for in-context multi-task reinforcement learning, which the community could benefit from.
* This work includes a detailed regret analysis of two proposed techniques.

### Weaknesses
While the premise looks promising, I believe that this paper needs more refinement and revision before it can be helpful.
* I found it difficult to understand what $M_{\theta}^{E-PS}$ looks like in practice. Neither $\mathbfcal{T}$ (the true set of train+test tasks) nor $\hat{g}(\cdot|\cdot)$ (prior/posterior over tasks) seem to be available in practice. Perhaps it would be helpful to include an algorithm for each of $M_{\theta}^{E-PS}$ and $M_{\theta}^{F-PS}$ in the appendix.
* There is a large disconnect between §3.1/3.2 and §4. In §3.1.2, we are introduced to two different action predictors $M_{\theta}^{E-PS}$ and $M_{\theta}^{F-PS}$, and we study their regret behavior in §3.2. But where do these two go in §4? There is no mention, comparison, or even justification for why one might not have been possible. Perhaps the authors should add a few paragraphs to connect these two sections, e.g., how do the findings in §3 help the implementation in §4, etc.

    I would be happy to learn how these are connected, or be notified that this question is already answered in the paper.
* I found it difficult to understand the Omniglot-based benchmark, and had to reread §4.1 several times before I understood it. It would be very helpful to include a visualization of the Omniglot task, even if in the appendix. For example, for 3-5 "trajectories", show what the corresponding states, actions and rewards would be. This visualization is independent of the transformer + ICL based approach that you propose.
* While the comparison to MAML is appreciated, there are other relevant baselines to compare to. To start with, see [1, 2]. As of now, there are few things to learn from the evaluation. The general lesson is that to lower the test loss of this specific technique, we need higher task diversity, larger models and more regularization/augmentation. Unfortunately, these points are not surprising. What would be interesting would be to see that while this specific technique benefits from larger model capacity, baselines do not. Or that more diversity does not change baseline behavior while this technique benefits from it.

[1] Laskin, M., Wang, L., Oh, J., Parisotto, E., Spencer, S., Steigerwald, R., ... & Mnih, V. (2022). In-context reinforcement learning with algorithm distillation. arXiv preprint arXiv:2210.14215.

[2] Sodhani, S., Zhang, A., & Pineau, J. (2021, July). Multi-task reinforcement learning with context-based representations. In International Conference on Machine Learning (pp. 9767-9779). PMLR.

### Questions
* If I understand correctly, there is an implicit assumption in §3 that the task identity is latent, correct? If so, a justification would be appreciated, perhaps by mentioning several problem settings and applications where in-context learning with latent task identities makes sense.
* In §3.1.2 and line 196 it is stated that "This time it is not straightforward to know how the model would behave when prompted with context from tasks that do not appear in $\mathcal{D}_{pre}$". Were out-of-distribution tasks ever considered in §3.1.1? 
* What is $\mathbfcal{T}$ in Eq. 4? Is it the same $\mathbfcal{T}$ in line 204? Why does the $M_{\theta}^{E-PS}$ predictor have access to it?
* What is $\hat{g}(\cdot|\cdot)$ in Eq. 4? If it is a posterior over the task, where did the prior come from? Shouldn't the regret performance of $M_{\theta}^{E-PS}$ depend on how well the prior matches the true prior?
* Do the descriptions in lines 339-345 relate to the fine-tuning of the ResNet model, or a change in the training methodology for the full stack (ResNet + transformer + RL)?

### Soundness
2

### Presentation
1

### Contribution
1
