# DSR: Reinforcement Learning with Dynamical Skill Refinement

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Reinforcement learning with skills (RL with skills) is an efficient paradigm for solving sparse-reward tasks by extracting skills from demonstration datasets and learning high-level policy which selects skills. Because each selected skill by high-level policy is executed for multiple consecutive timesteps, the high-level policy is essentially learned in a temporally abstract Markov decision process (TA-MDP) built on the skills, which shortens the task horizon and reduces the exploration cost. However, these skills are usually sub-optimal because of the potential low quality and low coverage of the datasets, which causes the sub-optimal performance in the downstream task. Refining skills is intuitive, but the change of skills will in turn lead to the non-stationarity of the transition dynamics of TA-MDP which we name temporal abstraction shift. To address the dilemma of sub-optimal skills and temporal abstraction shift, we unify the optimization objectives of the entire hierarchical policy consisting of the high-level policy and the low-level policy whose latent space embeds the skills. We theoretically prove that the unified optimization objective guarantees the performance improvement in TA-MDP, and that optimizing the performance in TA-MDP is equivalent to optimizing a lower bound of the performance of the entire hierarchical policy in original MDP. Furthermore, in order to overcome the phenomenon of skill space collapse, we propose the dynamical skill refinement (DSR) mechanism which names our method. The experiment results empirically validate the effectiveness of our method, and show the advantages over the state-of-the-art (SOTA) methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Dynamical Skill Refinement (DSR), an on-policy reinforcement learning method designed to optimize hierarchical policies in environments with sparse rewards. The paper refines the skills in an on-policy manner and proves that the temporal abstraction shift is circumvented by simultaneously updating the high-level policy and skills. The method prevents skill space collapse, which can lead to performance issues, by incorporating a dynamical mechanism that refines skills without disrupting the latent space. Empirical results demonstrate that DSR outperforms state-of-the-art methods in complex sparse-reward robotic manipulation tasks.

### Strengths
1- The paper is well-written and easy to read.
2- The proofs for theorems are solid.
3- Good comparisons with SOTA methods.

### Weaknesses
 1- The main difference between your approach and ReSKILL is that yours handles the temporal abstraction shift but it is not shown in your theorems.
2- This method needs lots of extra parts such as an extra residual policy to avoid skill collapse. Also, using RND makes sure that a skill is refined enough but still you cannot make sure that modifying the skill does not impact the state of other skills in the same state. Moreover, RND is an approach that needs lots of tuning such as how you control the learning rate of the variable network and the threshold for being accurate enough for the refinement. This would impact the results and we expected to see an analysis of these parameters.

3- Usually we have complex navigation robotic environments in the experiments with skills as the macro-action to reach the subgoals or landmarks. We do not see any navigation environment here.

### Questions
1- Can you explain again how skills are extracted using VAE?
2- ReSKILL has a similar on-policy approach as your method. You said that ReSKILL cannot theoretically guarantee performance improvement, but you did not mention proof. Can you elaborate more on this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address two issues in RL with skills: **(1)** sub-optimal pretrained skills due to low quality and low coverage of the datasets, and **(2)** temporabl abstraction shift due to refining skills. The authors propose to unify the optimization objectives of both high-level and low-level policies as the future return and use random network distillation to dynamically adjust the weight of action refinement. The paper demonstrates the effectiveness of the proposed method by providing theoretical analysis and empirical results.

### Strengths
* The proposed method is well-motivated, theoretically grounded, and demonstrates better performance against several state-of-the-art RL-with-skills methods.
* The author uses multiple figures to improve the clarity of the paper.

### Weaknesses
While well-motivated, I have some questions about this work:

1. In the introduction, the authors mention that previous works (e.g., SPiRL [1]) assumes near-optimal dataset to pretrain the skills. However, even if the skill contains some sub-optimal behavors, could the high-level policy still learns to avoid choosing the bad skills as it aims to maximize the reward? Specifically, if the high-level policy learns a low probability for the sub-optimal skills, isn't this sufficient to mitigate the problem of sub-optimal skills?
2. From the theoretical perspective, how is DSR different from the classic online hierarchical RL methods? For instance, [2] updates both high-level and low-level policies with RL objective with representation learning, and also provides the optimization objective bound. A similar bound is provided in [3] for offline settings. These two bounds actually quantify the exact form of sub-optimality, hence I think they are stronger than Theorem 3 in this work. I would appreciate it if the authors could discuss these methods in the paper. Furthermore, the bound in Theorem 3 seems to be a rather straightforward application of the Bellman equation, and it is unclear how it provides any novel insights into the optimization process of hierarchical policies.
3. How well does DSR can transfer skills to new tasks? I think one promise of skill-based RL is that it can conbine the learned skills to novel tasks, as mentioned in [1]. I am wondering if the authors could show some results in their experimental setting, such as training on data from one task and evaluating on other tasks. It would be beneficial to see a more comprehensive evaluation of the transfer learning capabilities of the proposed method, particularly in scenarios where the task distribution shifts significantly.

### Questions
There are some questions and concerns, which I have outlined in the previous section.

### Soundness
3

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
4

### Summary
This paper addresses the problem of the sub-optimal dataset in the skill-based reinforcement learning settings. The authors propose a unified optimization objective to train a hierarchical skill structure, providing a mathematical proof within the TA-MDP. Additionally, the authors introduce a dynamic skill refinement approach to mitigate potential collapse in the skill space.

### Strengths
- Learning skills from sub-optimal datasets and overcoming skill space collapse are crucial challenges in skill-based reinforcement learning scenarios.

### Weaknesses
 - I am not fully convinced how the unified optimization objective addresses the issue of sub-optimality in the datasets. DSR learns the low-level policy, making it more likely to optimize the action sequence for the downstream policy. If this is the case, the authors should emphasize more on mitigating the collapse in the skill space. 
- The contribution on dynamic skill refinement (Section 5.2) seems minimal, and its benefits are not fully demonstrated in Ablation 6.2, as DirectRefinement also shows comparable performance. Otherwise, the authors should provide more ablation studies on the learning of TA-MDP.
- In Section 6.1, the authors mention that DSR improves performance by avoiding skill space collapse. However, in Ablation 6.2, skill space collapse appears to occur only in the PyramidStack task. If the authors want to emphasize their contributions regarding skill space collapse, they should create more scenarios similar to PyramidStack and elaborate on why these tasks cause the collapse, and why it does not occur in other tasks.
- The presentation could be further improved. Figure 4 is smaller compared to Figure 2, and Figure 3 could be replaced with an equation for better clarity. For clarity, it would be better to include the pseudocode in the main manuscript rather than in Appendix C.

### Questions
- As the paper addresses the problem arising from the sub-optimality (low quality and low coverage) of the datasets, the authors should elaborate more on their dataset collection regarding to its sub-optimality.
-  In Figure 6, the y-axis denotes the episodic return. How is the episodic return computed? Additionally, can the authors elaborate more on their sparse reward setting? Is a reward given only upon task completion?
- In Ablation 6.2, what do the authors mean by "the extracted skills are not well initialized"? In Appendix D.2, the authors mention using datasets collected from TableCleanup, SlipperyPush, and PyramidStack, but why does only the PyramidStack task show this performance gap in Ablation 6.2?
- According to the original ReSkill paper, ReSkill achieves an average return of over 15 in the PyramidStack task. However, in Figure 6, ReSkill achieves only an average return of 10. The authors mentioned that the experimental settings are equivalent to those in ReSkill as described in Appendix D.2. Why is there a performance gap?
- It would be benificial, if the authors provide more ablation studies on their learning mechanism of TA-MDP. (Section 4)
- Can the authors provide additional experiments on other robotic manipulation environments, including long-horizon scenarios such as MetaWorld or Franka Kitchen?

### Soundness
2

### Presentation
2

### Contribution
3
