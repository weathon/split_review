# Active Fine-Tuning of Generalist Policies

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Pre-trained generalist policies are rapidly gaining relevance in robot learning due to their promise of fast adaptation to novel, in-domain tasks.
This adaptation often relies on collecting new demonstrations for a specific task of interest and applying imitation learning algorithms, such as behavioral cloning.
However, as soon as several tasks need to be learned, we must decide \emph{which tasks should be demonstrated and how often?}
We study this multi-task problem and explore an interactive framework in which the agent {\em adaptively} selects the tasks to be demonstrated.
We propose~\method (Active Multi-task Fine-tuning), an algorithm to maximize multi-task policy performance under a limited demonstration budget by collecting demonstrations yielding the largest information gain on the expert policy.
We derive performance guarantees for \method under regularity assumptions and demonstrate its empirical effectiveness to efficiently fine-tune neural policies in complex and high-dimensional environments.\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an algorithm designed for the scenario where a pretrained multitask policy needs to be fine-tuned with a limited number of additional demonstration rounds, denoted as N. The algorithm focuses on maximizing sample efficiency by strategically selecting a task at each round for demonstration. It employs proxies for mutual information between the expert and the current dataset, proving convergence under certain assumptions regarding the noisy expert policy and the environment MDP. The paper presents multitask performance results in a simple 2D reaching environment and two simulated robot environments, demonstrating that the proposed method outperforms a uniform task selection strategy at each rounds.

### Strengths
- The paper includes proofs demonstrating that the fine-tuned policy converges to the expert policy under specific assumptions about the noisy expert and the dynamics of the environment, thereby offering theoretical performance guarantees.
- This work could be relevant in the context of large-scale pretraining, as it aids in making informed decisions about what data to collect or include in subsequent training iterations.

### Weaknesses
 - The assumptions made about the expert policy and the noise in the expert policy significantly limit the method's applicability. In tasks involving physical robots, the expert policy is often humans which may not satisfy any of these assumptions. Specifically, the assumption of a noisy expert policy that is a perturbation of an optimal policy may not hold for human demonstrations, which can be suboptimal and inconsistent. Furthermore, the assumption that the noise is well-characterized and stationary is unlikely to be true in real-world scenarios where human behavior is complex and can vary significantly.
- The paper only compares the proposed method against one baseline that uniformly selects tasks at each round, demonstrating superior performance, particularly when the policy is pretrained on a skewed composition of tasks. However, it remains unclear how the proposed method compares to other baselines, e.g. a baseline that naively chooses tasks at each round with the goal of balancing task distributions across the entire dataset, including the pretraining dataset. The specific advantages of the proposed method over this natural alternative approach are not addressed. This is a critical omission, as simply balancing task distributions could be a strong and easily implementable baseline.
- In the simulated robot experiments, the individual tasks within each multitask suite are relatively disjoint. This raises questions about the proposed algorithm's effectiveness in scenarios where some tasks share structures, as simply balancing the trajectory count across tasks may not be the most effective strategy for leveraging the data collected thus far. For example, if two tasks require similar manipulation skills, focusing on one task might implicitly improve performance on the other, which is not captured by the proposed method.

### Questions
- What is the trajectory count for each task, including those from the pre-training phase, at the end of each round when executing the proposed algorithm? Is the algorithm doing anything beyond simply balancing the trajectory counts across tasks?
-  Has it been proved that the simulated robot environments and expert policies satisfy the assumptions in Section 4.1? If not, what implications might this have for the performance of the algorithm?

### Soundness
2

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
2

### Summary
This paper studies an interactive multi-task fine-tuning setting, where the agent can adaptively select which tasks to demonstrate, towards fine-tuning pre-trained generalist robot policies. The authors propose Active Multi-task Fine-tuning (AMF), which maximizes multi-task policy performance by selecting demonstrations that result in the largest information gain on the expert policy. Statistical guarantees for AMF are proven by extending the results on active learning from (Hübotter et al., 2024) to the sequential decision making setting. Results are demonstrated in simulation, including for a transformer model pre-trained on a large-scale real-world robotic dataset.

### Strengths
- The proposed approach AMF builds in principled prior work in active learning, and performance guarantees are proven, assuming some smoothness and regularity conditions. 

- The paper is generally well-written, and describes an approach from theory to practice.

### Weaknesses
 - Two practical instantiations of AMF are introduced in the main paper, which parameterizes policies either using a Gaussian process or a neural network. Considering AMF-GP is only used for a simple 2D integrator task, and to help set up AMF-NN, I think it would be helpful to spend more space describing AMF-NN and moving some content for AMF-GP to the Appendix. Algorithm 1 could be replaced with a full description of AMF-NN, which also includes the design choices (kernel approximation, batch selection, parameter isolation) needed to obtain a working implementation.

 - AMF-NN relies on parameter isolation to work (results in Figure 5), and does not yield benefits over uniform task selection baseline when finetuning a pre-trained robot transformer model in Section 5.5. This reliance on parameter isolation effectively transforms the multi-task fine-tuning problem into a series of single-task fine-tuning problems, where each task has its own set of parameters. This approach may lead to overfitting on individual tasks, rather than learning a generalizable multi-task policy. The fact that AMF-NN with parameter isolation outperforms uniform selection suggests that the performance gain is likely due to this overfitting rather than a superior multi-task learning strategy.

 - From the updated Fig. 15, it looks like (AMF-NN, no parameter isolation) performs similarly to (Uniform, no parameter isolation). This means that the practical implementation of the proposed approach is *no better than the uniform baseline in the actual multi-task setting*, in the Octo/WidowX domain or on smaller scale models in FrankaKitchen and MetaWorld domains. This is a significant limitation, as the core motivation of the paper is to improve multi-task fine-tuning, and the empirical results do not demonstrate this improvement without relying on parameter isolation.

### Questions
L289: For AMF-NN, is Equation 2 optimized by also training a Gaussian Process? Could the conditional entropy be estimated by comparing samples from the initial pretrained policy? 

L351-352: How is the task-space partitioning done?  Is a different set of weights used for each task? If so, it does not seem accurate to claim that AMF-NN can be scaled to large task spaces, particularly when fine-tuning larger models. 

Model merging (https://arxiv.org/abs/2310.01362) could be an alternative solution to the strategies evaluated in Figure 14. 

Figure 5, Figure 7: Why is parameter isolation ablation only done for uniform? How well does AMF perform without parameter isolation?

What tasks are selected by AMF over each round? Does this change over fine-tuning? Would be nice to see a plot of this alongside the success rates for each task.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces AMF (Active Multi-task Fine-tuning), an algorithm for efficiently fine-tuning pre-trained "generalist" robot policies to perform multiple tasks. Given a limited demonstration budget, AMF actively selects which tasks to request demonstrations for, aiming to maximize overall multi-task performance.  It does this by selecting tasks that yield the largest information gain about the expert policy, focusing on areas where the current policy is most uncertain. 

The authors provide theoretical performance guarantees for AMF under regularity assumptions, showing that it converges to the expert policy in sufficiently smooth MDPs. They also demonstrate AMF's effectiveness in practice, applying it to some robotic manipulation tasks with neural network policies. Experiments in simulated robotic environments like FrankaKitchen and Metaworld show that AMF significantly outperforms uniform task sampling, especially when the pre-training data is skewed towards a subset of tasks. The authors also demonstrated that AMF can be applied to off-the-shelf models like Octo, though the improvement over the naive baseline is marginal.

### Strengths
- The paper studies the timely problem of efficiently fine-tuning generalist robot policies, which are becoming increasingly important in robotics.

- The authors provide performance guarantees for AMF under certain regularity assumptions, proving its convergence to the expert policy in smooth MDPs. This adds to the credibility and understanding of the algorithm's behavior.

- AMF demonstrates improvements over uniform sampling, particularly when the pre-training data is biased towards a subset of tasks. This is an advantage as real-world pre-training datasets are sometimes unevenly distributed.

- The algorithm can be applied to some robotic environments with high-dimensional observation and action spaces, using neural network policies. This demonstrates its practical applicability in realistic scenarios.

### Weaknesses
### Major

- FrankaKitchen and MetaWorld are relatively simple robotic benchmarks due to their narrow initial state distributions and short task horizons of each task. Future evaluations would benefit from testing on more challenging robotic benchmarks such as RLBench [1], RoboSuite [2], ManiSkill [3], and BiGym [4], which offer greater complexity and variability. Specifically, these environments often involve a limited set of initial object poses and goal configurations, which does not fully capture the complexities of real-world manipulation scenarios. The short task horizons also limit the evaluation of long-term planning and error recovery capabilities of the learned policies. Testing on benchmarks with more diverse initial states, longer task horizons, and more complex object interactions would provide a more comprehensive assessment of the proposed method.

- The effectiveness of AMF, especially with neural networks (AMF-NN), hinges on accurate uncertainty estimation. While the proposed loss-gradient embedding approach works well empirically, uncertainty quantification in neural networks remains a challenging open problem. The performance can degrade if the uncertainty estimates are unreliable. Specifically, the loss-gradient embedding may not accurately capture the true uncertainty of the policy, especially in regions of the state space that are not well-represented in the training data. This could lead to the selection of tasks that do not provide significant information gain, thus hindering the overall performance of the algorithm. Furthermore, the method does not explicitly address the issue of overconfident predictions, which is a common problem in neural networks.

- While AMF shows certain improvements in skewed pre-training scenarios, its advantage diminishes when the pre-training data is uniformly distributed across tasks. In such cases, simpler methods like uniform sampling might suffice. This suggests that the proposed method may not be necessary in scenarios where the pre-training data is already well-balanced across tasks. The added complexity of AMF may not justify the marginal gains in performance compared to simpler baselines in such cases.

- Evaluating the information gain criterion can be computationally expensive, especially with a large number of tasks or long trajectories.  The authors propose some approximations to mitigate this, but the computational cost can still be a concern in large-scale applications. The computation of loss gradients for each task and the subsequent embedding process can be particularly demanding, especially when dealing with high-dimensional observation and action spaces. This computational overhead could limit the scalability of the proposed method to more complex robotic systems and tasks.

- While parameter isolation helps mitigate forgetting, it also prevents positive transfer learning across tasks. In addition, parameter isolation also adds more parameters to the final policy. The lack of positive transfer could limit the ability of the policy to generalize to new tasks or adapt to changes in the environment. The increased number of parameters also increases the memory footprint of the model, which may be a concern in resource-constrained environments.

- The experiments with the Octo model are limited in scope, only fine-tuning the action head and focusing on a scenario with a relatively uniform pre-training distribution. More extensive evaluation with large-scale, generalist policies is beneficial to fully assess AMF's potential. The fact that only the action head is fine-tuned may not fully leverage the potential of the pre-trained model. Furthermore, the evaluation on a uniform pre-training distribution does not fully demonstrate the benefits of AMF in scenarios where the pre-training data is skewed towards a subset of tasks.


### Minor

- The points in Figure 2 are not well aligned.

### Questions
- In Figure 4, why does the red curve always drop in the first round? This phenomenon occurs in all tasks.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors aim to apply active learning to a multi-task behavior cloning setup. In their problem setting, the agent is allowed to request demonstrations for the next task it wants to see a demonstration for. The expert policy provides this demonstration, and the goal is to define a strategy that maximizes expected return over a final evaluated task distribution (typically uniform over all tasks).

To do so, they use a Bayesian perspective, assuming that expert demonstrations have some independent sampled noise $\epsilon$, using a Gaussian process to model the policy. The method's goal is to maximize information gain per sample, given the history of prior trajectories + tasks. Under some assumption of Lipschitz continuity, they show the optimality gap can be bounded to decay in $O(infogain * n^{-1/2})$.

However, exactly optimizing the info gain for selecting a new task $c$ is not tractable as given, so we must instead use various approximations. Maximizing mutual info $\mathcal{I}(\pi(s_t,c); \tau(c'))$ over the next context $c'$ is the same as minimizing $\mathcal{H}(\pi(s_t,c) | c', \tau', history)$ over trajectories $\tau'$ sampled from the distribution of expert trajectories given task $c'$.

This is then made practical in two ways. First, to estimate sampling a new trajectory $\tau$, we apply importance weighting to the previous $n-1$ demos collected so far, using our current policy $\pi$ to generate importance weights. For entropy, since the policy is represented by a Gaussian process, we can leverage existing techniques from that literature for estimating entropy.

Last, to deal with forgetting, the authors apply "parameter isolation". The task-space is partitioned into $K$ sets, and $K$ copies of finetuning weights are initialized, each one only updated on tasks that lie within its partition.

In experiments, the authors find that active learning is most effective when the initial task distribution is skewed, with the gap between it and uniform sampling narrowing as the pretraining distribution becomes closer to uniform.

### Strengths
The authors provide a compelling justification for why active learning could be useful to robot learning, noting that several prior works use more bespoke methods for deciding on task distributions. The method is adjusted to be applicable to deep learning based policies, and shows promise, especially in scenarios with unbalanced tasks.

### Weaknesses
I find it somewhat concerning that parameter isolation (having separate weights per task) is so critical to final performance. My understanding was that existing models for Franka kitchen, Metaworld, etc. did not need to do this, and successfully trained models that could handle all contexts (tasks) at once.

The increase in performance from using AMF is relatively low in many settings, even the friendliest settings where task distributions are skewed. The gap often closes in skewed settings once we reach 10 rounds of data (see Figure 4).

With many ablations maxing out at a 20 demonstration budget, I am a little skeptical that the empirical importance weights are any good. It feels like 20 examples is too few to really get a good approximation of a high-dimensional trajectory space...

### Questions
I am curious about comparisons to other simpler sampling schemes. For example, something like "sample the context $c$ that appears least often in the history", or other similar schemes that use less machinery than estimating importance weights, info gain, etc.

### Soundness
3

### Presentation
3

### Contribution
2
