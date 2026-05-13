# SYMPOL: Symbolic Tree-Based On-Policy Reinforcement Learning

- Decision: Accept
- Avg Score: 7.20
- Scores: 5, 5, 8, 10, 8

## Abstract
Reinforcement learning (RL) has seen significant success across various domains, but its adoption is often limited by the black-box nature of neural network policies, making them difficult to interpret. In contrast, symbolic policies allow representing decision-making strategies in a compact and interpretable way. However, learning symbolic policies directly within on-policy methods remains challenging.
In this paper, we introduce SYMPOL, a novel method for SYMbolic tree-based on-POLicy RL. SYMPOL employs a tree-based model integrated with a policy gradient method, enabling the agent to learn and adapt its actions while maintaining a high level of interpretability.
We evaluate SYMPOL on a set of benchmark RL tasks, demonstrating its superiority over alternative tree-based RL approaches in terms of performance and interpretability. To the best of our knowledge, this is the first method, that allows a gradient-based end-to-end learning of interpretable, axis-aligned decision trees within existing on-policy RL algorithms. Therefore, SYMPOL can become the foundation for a new class of interpretable RL based on decision trees.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work employs a tree-based model integrated with on-policy RL, like PPO, to maintain better interpretability with less information loss.
On a set of benchmark RL tasks, it demonstrates its superiority over alternative tree-based RL approaches in terms of performance and interoperability.

### Strengths
1. The motivation is good, aiming to improve the interpretability of RL, which is a key factor for deployment due to its adoption of DNNs. 
2. The authors try to improve the stability of DTs as a policy via more implemented skills.

### Weaknesses
1. This work evaluates its experiments on a series of toy tasks that could be easily solved. Can it achieve competitive performance in complex tasks, like Mujoco and Atari games?
2. This work is also hard to follow, the contribution and the method should be highlighted and stated.
3. Please abatement the contribution of this work. This work is not the first to use DT to represent RL policy, i.e., the work "MIXRTs: Toward interpretable multi-agent reinforcement learning via mixing recurrent soft decision trees", arXiv:2305.10091, 2022. They utilized SDT in multi-agent RL complex tasks two years ago.
4. There are some typos in References.

### Questions
1. line 414- 415: "In RL, especially for smaller policies, the runtime is mainly determined by the actor-environment interaction..." - This sentence is hard to follow. Can the authors unpack this sentence?
2. Did this work simply incorporate GradTree into the PPO framework?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a differentiable tree-structured model that can be optimized via RL algorithms. The proposed method includes a tree-structure actor and a neural network critic. Experiments are conducted on several RL benchmarks include discrete and continuous action spaces, compared with previous tree-based methods.

### Strengths
1. The proposed method can be applied into both discrete and continuous action spaces.

2. The proposed method improves interpretability of RL policies.

### Weaknesses
The reviewer is not convinced with the claim of "first method that trains a DT via stochastic policy gradient in an end-to-end manner". Making the learning of DTs differentiable has been investigated for a long time, such as [1]. It is safe to make this claim through a thorough literature review.

There are some other works focusing on learning a differentiable symbolic policy which is based on first-order logic, such as [2,3], which is not compared and discussed in this paper.

Looks like that defining the syntax and semantics of DTs relies on human knowledge, maybe the reviewer is wrong, which can be clarified during rebuttal.

The information loss experiments, described in Fig 1 and Table 3, are confusing. It is unclear if the test reward is evaluated on the same environment as the trained one. If so, why is there a performance drop of (Silva et al. (2020))? It is suspected that the trained model has a stochastic probability while the test model is greedy, selecting the action with the maximum Q, but this needs to be clarified.

### Questions
The reviewer is confused about the information loss experiments, described in Fig 1 and Table 3. Is the test reward on the same environment as the trained one? If so, why is there a performance drop of (Silva et al. (2020))? Did you mean the trained model has a stochastic probability while the test model is greedy that is, selecting the action with the maximum Q?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents SYMPOL, a method for online RL using decision trees as policies. 
The authors include the GradTree into PPO, thus backpropagating from a neural critic to an arithmetic decision tree-based actor.
They evaluate their method on different continuous and discrete environments, and demonstrate that SYMPOL allow to detect and correct misalignments problem that SIMPOL allows to find.

### Strengths
**The method is well motivated.**
GBRL, the only interpretable tree-based method that directly learns tree instead of distilling them after training, leads to huge and many trees. 

**The potential impact of online learning of trees is huge for interpretable RL.**
The online learning of transparent policies could allow for detection of misalignment during training, and potentially correction of the misalignment during training. Distillation methods do not have this advantage.

**The structure of the paper makes it easy to follow**. Most of the paper is clear, in terms of structure, particularly the experimental evaluation. The bold points, together with the clear figures and tables, allow the reader to quickly grasp most of the experimental evaluation, even if it took me a bit of time to understand that SA-DT is an implementation of Dagger/VIPER.

### Weaknesses
 **The difference between SYMPOL and other baselines is not clear.**
The preliminaries section would benefit for a bigger explanation on GradTree, as its integration to PPO is the main contribution and what distinguish this work from many existing interepretable baselines such as NUDGE, INSIGHT, GBRL and SCoBots [1]. Specifically, the mechanism by which GradTree allows backpropagation from a neural critic to a decision tree actor needs more detailed explanation. It's unclear how the gradients are computed and propagated through the discrete structure of the decision tree. The paper should clarify if the decision tree is fully differentiable or if some form of approximation is used. Furthermore, the connection between the GradTree and the PPO algorithm should be more explicit, detailing how the policy gradients are used to update the tree structure and parameters. It also took me quite some time to understand that SA-DT is equivalent to running Dagger or VIPER with their MLP.

**Evaluation seems weird.** It feels like the baselines are underperforming, compared to what is reported in the literature. For example, the D-SDT is underperforming compared to what VIPER reports (with a few node). I don't know why, as it is okay if their baselines would perform worse than distilled ones. Directly learning trees in an online fashion, could allow for e.g. LLM guidance to provide the trees with correct inductive biases, that would avoid e.g. misalignment problems during learning. The paper should include a more detailed analysis of why the baselines are not reaching the performance levels reported in other studies. It is important to understand if this is due to implementation details, hyperparameter settings, or some other factor. A comparison of the training curves for the baselines with those reported in the literature would be beneficial to identify any discrepancies. The paper should also discuss the potential limitations of the baselines used and why they may not be suitable for the specific environments used in this study.

**Missing litterature on misgeneralisation (and interpretable RL).**
On misgeneralisation, NNs have been shown to systematically misgeneralize on different Atari environment [2], even when the environment is simplified [3], and DT-based policies have been shown to allow to mitigate it [1]. The paper should discuss the potential of SYMPOL to address misgeneralization issues, particularly in the context of the environments used in the evaluation. It should also include a discussion of how the interpretability of the decision tree policies can help in identifying and correcting misgeneralization problems. The paper should also discuss the limitations of decision trees in addressing misgeneralization, especially in complex environments.

### Questions
* Why is it that the extracted trees are performing so low in comparison to what is reported by the VIPER's authors ?
* Is there any reason why you are not using the set of Object Centric Atari environments in your evaluation ? It would allow to compare with other deep and interpretable baselines such as NUDGE, INSIGHT, SCoBots, ...

I'm willing to revise my scores if experiments that compare SYMPOL to these interpretable methods on some Atari games are reported. It would allow the reader to compare these methods. Even if SYMPOL slightly underperforms, for interpretability, game scores are not the most important focus.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
Authors propose SYMPOL. SYMPOL alleviates previous challenges of using RL to learn decision tree policies by using a differentiable tree representation. They also increase training stability by collecting longer rollouts at the end of training and using large batch sizes. The paper is well written. However, with the current experiments, it is unclear to me if the good experimental results are due to the use of GradTree or to the stabilizing of the training or both. But in any case, the contribution is not clear.

### Strengths
The related work and preliminary sections are excellent. Misgeneralization experiment and information loss experiments are insightful. Topic of interpretability is crucial.

### Weaknesses
There are two main weaknesses to this paper.

1) Contributions. Is the contribution plugging GradTree into PPO ? 

I do find the ablation study insightful on why the training process needs strong stabilyzing and digging this further could be a nice contribution. Similarly, it seems to me that Silva et al 2020 is very similar to GradTree in the sense that GradTree is a differentiable formulation of DTs and Silva et al is too. I would have liked a more in depth comparison of the two!

2) Experiments (just the section 5.2). Baselines seem underperforming. 

From looking at Silva et al 2020 and VIPER 2018, I feel like SA-DT (d=5) and D-SDT should be able to solve CartPole contrary to what you show in your table 1. Also why isn't SA-DT called VIPER? 

If I were you I would rewrite the section 5 centered around two questions: why use direct tree optimization rather than post hoc distillation of a neural net like VIPER? After showing that direct optim might be better than post hoc fitting of trees, you should ask which of the two sota direct optim is better and why: Silva et al or SYMPOL?

### Questions
Could you remove fig 2 that does not bring anything to the paper and replace it with appendix results (such as figure 10)? Even better, could you summarize the section 4.1 or GradTree in a schematic and replace the current figure 2 with it please? If you decide to put figure 10 in the main paper instead of the schematic at figure 2, please smooth your curves.

Could you please remove figure 3 and replace it with somehting more useful? I think one does not need a plot to understand your rollout schedule.

Could you write a dedicated parargaph that explains the difference between SYMPOL and Silva et. al. 2020 ? I think your work is actually very similar to their.?

Bonus, add CUSTARD (Topin et al 2021) as a baseline in your table 1.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents SYMPOL, a new approach to learning interpretable policies for reinforcement learning problems by building on recent works facilitating gradient-based training of decision tree architectures. SYMPOL performs much better than prior methods for producing decision tree policies (such as discretizing policies or behavior-cloning a decision tree from a replay buffer), and includes a few tricks for improving the stability of training tree-based models.

SYMPOL is evaluated on several RL problems, largely simpler problems such as mountain car or lunar lander, as well as a MiniGrid environment. Finally, the interpretability of SYMPOL policies is displayed using a case study on policy generalization, in which the authors inspect a learned policy, identify areas for improvement or weaknesses in the policy, and then re-train to fix these weaknesses.

### Strengths
* The paper builds on very recent work and adequately cites the prior work, making sure to clearly draw the line between novel contributions and techniques which already exist.
* The SYMPOL framework is clearly explained, and the tricks used to improve training stability are highlighted (as opposed to being buried in the appendix). I feel like I could re-implement this from the paper alone.
* The results are compelling. SYMPOL performs quite well (final performance numbers/returns are superior to baselines) while also generalizing well to new versions of the problems (as shown by the Cohen's D experiments)
* The case study on interpretability is compelling, showing the power of an interpretable RL framework such as SYMPOL. 

Overall, the paper is very well written, the framework is clearly described, makes intuitive sense, and does not require significant hand-tuning, and the results and discussion sections are strong.

### Weaknesses
 * SYMPOL is mentioned to have 50+ nodes, which could become quite unwieldy or difficult to interpret, but we do not see such examples in the paper. It would be illustrative to see a standard SYMPOL policy in addition to the cleaned up versions in Figures 7/9. Furthermore, the paper does not discuss the computational cost of evaluating such large trees, which could be a concern for real-time applications.
* While the framework is sound and the results are strong, the overall novelty of the framework is limited. Apart from introducing a dynamically growing replay buffer, the technical contributions are largely a combination of existing techniques. The core idea of using a differentiable decision tree within a reinforcement learning loop, while effective, is not entirely novel in itself, and the paper could benefit from a more thorough discussion of the specific challenges and solutions that arise from this combination.
* As the paper relies heavily on the contribution of GradTree, it would be helpful to have an overview of that work here, so that the finished paper reads as a more self-contained work. The current description of GradTree is insufficient to fully understand the method's inner workings, and a more detailed explanation of its gradient calculation and tree structure would be beneficial.
* The comparisons across all works are not entirely 1-1, as the number of nodes in each tree is not consistent (however, the authors make note of this in the text). This makes it difficult to directly compare the performance of SYMPOL with other methods, as the tree size is a significant factor in both performance and interpretability.

### Questions
* There is no ablation on the automated pruning, but automated pruning is mentioned a few times in the work. What are the effects of this on the resulting policy, and at what point are the node automatically pruned? If they are not pruned during training, do they complicate gradient flow?
* How is misaligned behavior detected, as in the case study shown in Section 6? It seems that, because the network's parameters are 1D feature vectors, you would need to reverse engineer the input states for each node, then plot out the resulting tree? Is there another way, or is this manually done?
* Would SYMPOL extend naturally to continuous action spaces or unstructured input (e.g., images)?

### Soundness
4

### Presentation
4

### Contribution
3
