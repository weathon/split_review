# Outward Odyssey: Improving Reward Models with Proximal Policy Exploration for Preference-Based Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Reinforcement learning (RL) heavily depends on well-designed reward functions, which can be challenging to create and may introduce biases, especially for complex behaviors. Preference-based RL (PbRL) addresses this by using human feedback to construct a reward model that reflects human preferences, yet requiring considerable human involvement. To alleviate this, several PbRL methods aim to select queries that need minimal feedback. However, these methods do not directly enhance the data coverage within the preference buffer. In this paper, to emphasize the critical role of preference buffer coverage in determining the quality of the reward model, we first investigate and find that a reward model's evaluative accuracy is the highest for trajectories within the preference buffer's distribution and significantly decreases for out-of-distribution trajectories. Against this phenomenon, we introduce the **Proximal Policy Exploration (PPE)** algorithm, which consists of a *proximal-policy extension* method and a *mixture distribution query* method.
To achieve higher preference buffer coverage, the *proximal-policy extension* method encourages active exploration of data within near-policy regions that fall outside the preference buffer's distribution. To balance the inclusion of in-distribution and out-of-distribution data, the *mixture distribution query* method proactively selects a mix of data from both outside and within the preference buffer's distribution for querying. PPE not only expands the preference buffer's coverage but also ensures the reward model's evaluative capability for in-distribution data. Our comprehensive experiments demonstrate that PPE achieves significant improvement in both human feedback efficiency and RL sample efficiency, underscoring the importance of preference buffer coverage in PbRL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the issue of significant human involvement in preference-based reinforcement learning (PbRL), this work proposes the Proximal Policy Exploration (PPE) method, which is designed to purposefully explore and extend the coverage of the preference buffer, thereby enhancing the evaluation ability of the reward model and the subsequent value function in PbRL. This improvement aims to promote an unbiased transmission of human intentions to the agent's behavior. Specifically, this work first employs a Morse Neural Network to identify the distributional properties of interactive transition samples, jointly constructing a policy regularization objective that encourages the agent to explore targeted transitions. Finally, PPE introduces the mixture distribution query to balance the inclusion of both in-distribution and out-of-distribution data. The experiments demonstrate that PPE achieves significant improvements in both human feedback efficiency and sample efficiency.

### Strengths
This work addresses the accuracy of the reward model in preference-based reinforcement learning from a different perspective—by expanding the coverage of the preference buffer, which is a compelling and meaningful direction. The work specifically designs the proximal policy extension and mixture distribution query methods to explore policy behaviors outside the preference distribution but near the policy distribution, enabling the agent to effectively leverage both the existing preference distribution data and the unexplored state-action space beyond the preference buffer. Experimentally, compared to the state-of-the-art method QPA, PPE achieves significant performance improvements across DMC tasks of varying difficulty levels and includes extensive ablation studies on components and key parameters. Overall, the method in this work is highly reproducible, well-developed, and provides theoretical guarantees for certain conclusions, with a comprehensive experimental setup.

### Weaknesses
The overall originality and novelty of the specific methodology in this paper are relatively limited. The problem addressed here essentially relates to a common issue of OOD detection and balanced utilization. The distinguishing factor is its application to the preference-based reinforcement learning (PbRL) setting, specifically aiming to address inaccuracies in the learned reward model due to insufficient coverage in the preference buffer. Unfortunately, the methods adopted do not introduce particularly novel approaches to solve this challenge.
In detail, i）The paper applies a morse network to assess the distribution of each transition; however, this approach was previously introduced in "Offline Reinforcement Learning with Behavioral Supervisor Tuning."；ii）Secondly, the authors incorporate this network within a regularized policy objective, which encourages the agent to purposefully explore targeted transitions. However, the initial objective form is heavily based on prior work. The main contribution here is the proposal to tighten the constraints, enabling a more effective closed-form approximation of the original objective. iii）Lastly, the authors introduce a Mixture Distribution Query method that queries both in-distribution and out-of-distribution data, which is the main but limited contribution of this work.

Experimentally, the performance on the MetaWorld tasks is suboptimal, failing to achieve consistent performance improvements. Also, there are some deficiencies in the writing of this paper. For example, there is excessive verbosity, and some problem statements are not clearly expressed.

### Questions
1) In Section 3.1, some descriptions lack clarity. For instance, in Figure 1b, it is unclear why the variance of the reward model can be used to identify whether a transition sample belongs to the training region. Therefore, it is essential to provide additional explain or experimental evidence demonstrating the discriminative ability of the reward model variance with respect to the training data distribution before using the conclusion.

2) The mixture distribution query process focuses on enhancing the coverage of the preference buffer and improving the evaluation capability of the reward model by combining in-distribution and out-of-distribution data. However, it remains unclear how the preference labels for newly explored trajectory pairs {τ0, τ1, y}^b_i=1 are generated. Does this process still require human involvement? This aspect is not addressed in the paper. If similarity metrics-based automatic labeling is used, there may be issues with accuracy, while if human intervention is still needed, this approach does not effectively solve the initial problem.

3) There is a potential but possibly flawed doubt here. In the mixture distribution query method, if there is a computationally intensive query operation, the prior policy regularization setup may seem less essential, as the agent would still have the capability to explore targeted transitions without any policy regularization. Distributed query on such naive policy exploration can also achieve similar effects. Hence, why is a mixture distribution query still necessary? Can similar functions or effects be achieved by coordinating the previous parameter λ or other possible adjustments?

4) Some descriptions and causal relationships in the manuscript are unclear. For example, in lines 180-181, "Therefore, the method proposed by Liang et al. (2022)...", what method has been proposed in the existing work? If so, it is difficult for us to understand the subsequent results based on the previous sentence. Finally, there are some repeated descriptions, such as lines 243-247, 275-278, etc., which can be appropriately simplified to express accurately and concisely.

5) Although the problem solved in this paper falls within the scope of PbRL, PbRL-related preliminaries are rarely involved in the method section, so this part can be simplified. In terms of formal description, the manuscript can focus more on the problem itself.

### Soundness
3

### Presentation
2

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
The paper proposes the Proximal Policy Exploration (PPE) algorithm to improve the quality of reward models in preference-based reinforcement learning (PbRL) by expanding the coverage of the preference buffer used to train the reward model. To achieve this, PPE has two components: a proximal-policy extension approach to encourage exploration in out-of-distribution transitions near the current policy and a mixture distribution query method for balancing in-distribution and out-of-distribution data in the buffer. The authors evaluate PPE on DMControl and MetaWorld benchmarks.

### Strengths
- **Novel Approach.** The proximal-policy extension and mixture distribution query methods decompose exploration and exploitation on learning the preference model for PbRL.
- **Empirical Results.**  The experimental results show some improvement over previous methods and the authors ablate some design choices.
- **Compatibility with Existing Frameworks.** PPE is compatible with previous PbRL methods.

### Weaknesses
 1. Line 48 states that PbRL "addresses these challenges." However, PbRL is also prone to human biases. It would be better to phrase it as "PbRL addresses some of these challenges."
2. Line 84 should read "summary" instead of "summery"
3. Figure 1(b) is missing one point for a training region of size 9.
4. While the OOD detection can be useful to encourage the agent to explore more informative (s,a) pairs, learning the function $f_\phi$ can be computationally expensive. The paper would benefit from a discussion on how training $f_\phi$ impacts wall-clock time and necessary computational resources compared to previous methods.
5. The paper does not discuss how the stopping time for feedback collection is decided. The manuscript would benefit from a further discussion on this and its impact on the training. For example, what happens in Figure 3(c) if one stops collecting feedback after 50% of training similarly to (a) and (b)? Alternatively, does RUNE outperform PPE the training is continued to $2 \times 10^6$ steps similarly to (a) and (b)?
6. Moreover, what does it mean to stop feedback collection after $1 \times 10^6$ steps in terms of number of preference queries?
7. In Algorithm 1 and 2, trajectory pairs $\tau_0, \tau_1$ are sampled from $P^{in/out}(\tau)$, however the latter is not a distribution, but rather just a real number. Could the authors clarify how the sampling is performed?
8. The paper claims that the proposed method learns better reward models because it has a larger coverage over the state-action spaces, however, there is no discussion on how the coverage differs between different algorithms. It would be interesting to have a measure of how much more of the state-action space is indeed covered.
9. Line 296 should state "the cardinality of" or "the size of" instead of "the quantity of".
10. PPE needs to maintain 4 buffers $\mathcal D, \mathcal D^{cp}, \mathcal D^p, \mathcal D^m$. This can be quite expensive in terms of memory. Moreover, what is $\mathcal D^{cp}$ exactly? How does it differ from other buffers? In Algorithm 2, line 5, in which buffer is the transition stored? What is the $\mathcal D$ buffer?
11. The plots are not properly explained. Are the authors plotting the average success rate over how many seeds? Are the shaded areas the standard deviation, standard error, or some other uncertainty measure?

### Questions
See **Weaknesses**. Additionally:
1. In line 237, if $\mathcal{A}_{uni}$ simply the action space of the MDP? It might be clearer to write $a_u \sim \mathrm{Uniform}(\mathcal A)$ instead.
2. I am not sure the Equation 5 captures the desideratum in the preceding paragraph. From my understanding, the objective of $\pi_E$ is to take actions that take the agent to unexplored areas, i.e., areas that are classified as 0 by $M_\phi$, which can be achieved by minimizing $M_\phi$, maintaining the constraints of staying close to $\pi_T$. However, Equation 5 is a maximization problem. Could the authors clarify this?
3. In lines 285 - 287, the authors state that the query selection method should actively select OOD data to increase coverage while also selecting OOD data for query. Should it instead say that it should select in-distribution data for query? If not, why?
4. During training, what it means for data to be in and out-of distribution changes. Are the elements in $\mathcal D^M$ relabeled? In line 14 and 15 of Algorithm 2, the data in $\mathcal D$ and $\mathcal D^{cp}$ is relabeled but not $\mathcal D^M$.
5. Could the authors clarify why the SAC algorithm has been chosen in Algorithm 2?
6. In line 7 of Algorithm 2, what is $\tau$?
7. What is the difference between "iteration" and "interaction" in Algorithm 2?
8. How often is $M_\phi$ updated? For how many gradient steps? How does this impact wall-clock time?
9. What are the similarities and differences of the exploration mechanism of PPE compared to the exploration induced by model-based PbRL (e.g., "HIP-RL: Hallucinated Inputs for Preference-based Reinforcement Learning in Continuous Domains" or "Efficient Preference-Based Reinforcement Learning Using Learned Dynamics Models")? Is learning an exploration policy similar to learning a model of the dynamics and exploring optimistically in the learned dynamical model?

### Soundness
2

### Presentation
2

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
The authors introduce a novel PbRL method, that is based on the idea, that it is important to increase the OOD error of the reward model. Therefore, they introduce a query method that considers a mixture of OOD and ID samples. Futhermore, they employ a Morse network for obtaining well calibrated uncertainty estimates that allow for efficient OOD detection. The algorithm is evaluated on several locomation and robotics benchmark tasks and compared to 4 existing PbRL algorithm. The authors also included a ablation study wrt. two of the hyper parameters and the distinct modules of their algorithm.

### Strengths
The authors try to tackle a known problem with a new perspective. It is known, that PbRL is subject to a dual exploration problem: The policy space and the reward space. However, exploring the reward space via an explicit OOD detection is novel, as far as the reviewer knows. Furthermore, they utilize novel Morse networks, not applied in PbRL before. With a good benchmark set of test domains and algorithms, they establish the usefulness of the approach. Resultingly originality and impact are good. However, significance is limited due to clarity issues and some remaining research questions.

### Weaknesses
The most impactful weakness of the paper are issues of clarity. It seems, that the authors are not using a form of reward-based PbRL, but a variant of direct policy learning. (see A Survey of Preference-Based Reinforcement Learning Methods, Wirth, 2017) $M_\phi$ approximates an action distribution, according to Eq. 3, not a reward distribution, which is then used to modify a policy $\pi_T$ (Eq.6). However, the origin of $\pi_T$ is never discussed. Section 2 indicates that this may be a reward-based PbRL policy, but this is not clear. In case it is, this should be clarified and also explained which method is used to derive a policy from the learned reward. The according updates should be added to Alg.2. These issues also impacts the claim "Our method, as outlined in Section 3.2, is designed to be orthogonal and highly compatible with existing strategies", because the orthogonality is not visible. These clarity issues are probably not difficult to resolve, but are quite impactful. There are also some clarity issues wrt. the motivating example (see questions).

A second problem is, that this is difficult to attribute the performance gains to the coverage improvement. The coverage idea implicitly assumes that all parts of the trajectory space are equally important, which is usually not true. It is sufficient to obtain a reward function that induces the same optimal policy as the true reward and guides the policy learning process towards that policy. Therefore, methods combining expected reward and uncertainty are usually used (like RUNE). That it is better to "only" consider coverage would be a very interesting insight, but the algorithm deviates from conventional PbRL methods in two other aspects: The preference exploration is defined as a policy, not a reward scheme and the uncertainties are modelled using an RBF-kernel based method. Kernel methods are known to be better wrt. ODD uncertainty (as compared to e.g. ensembles, like used in RUNE). Therefore, the ablation studies using ensembles instead of Morse or defining the coverage bonus in the reward space are of major interest. However, the problem of unclear effect attribution is not substantial enough to prevent acceptance, as the benefit of the full method is sufficiently established. Although, it would greatly improve the contribution.

A further improvement can be achieved by a bit more extensive discussion of Morse networks, as they should not be considered an established method (there seems to be only an arxiv short paper, nothing peer reviewed). Foremost is the question, how scalable Morse networks are. Most PbRL methods abstain from using Kernel-based approaches, despite their advantages, due to the costly scaling wrt. number training data points. 

Lastly, the structure of the paper could be improved a bit moving the related work discussion in the introduction to the related work section and the OOD detection from preliminaries to method.

### Questions
- Preliminaries: $y_p$ is not defined, but seems to be restricted to strict preference?
- Motivation Example: Are region 1-9 sizes (as indicated by line 171) or an index?
- Motivating Example: What is the is the evaluation region for used for 1d?
- This implies that $\hat{a} = a$ only when the pair (s, a) originates from the preference buffer. This claim depend on the form of $f$, e.g. a linear approximator may not ensure this. Is this ensured by the Morse network?
- Some baseline results deviate from reported literature (e.g. SURF, QPA drawer-open). Is the statement "we also made use of the official code repositories" true for all baselines or are some re-implemented?
- The method seems quite sensitive against hyperparameter changes (4.2). Is there a set of reasonable hyperparameters for unseen tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on developing a preference-based RL algorithm that increases the data coverage with a preference buffer. More specifically, it is found that the reward model cannot accurately predict rewards for trajectories that are out of distribution from the original training set. Therefore, the authors propose the Proximal Policy Exploration (PPE) algorithm that encourages the agent to explore data that falls outside of the preference data distribution, but close to the agent’s current policy.

### Strengths
1. The motivating example in Section 3 helps demonstrate the OOD issue. 
2. I think it was interesting to evaluate the reward model by comparing the ground truth return and the learned return via the Spearman correlation coefficient in Section 3.1. 
3. Performing OOD Dection seems like a novel addition to the PbRL algorithm.

### Weaknesses
Similar to prior work/findings:

1.  PPE seems extremely similar to QPA [1]. Both methods seem to be focused on selecting queries that are close to the agent’s current policy. However, the authors only briefly mention this work in the related works. For example, lines 249-251 from this paper state,“We have designed the [PPE] method, to actively encourage the agent to explore data that falls outside of the preference buffer distribution but within the vicinity of the current policy’s distribution”. 
Snippet taken from [1] “In particular, it is crucial to ensure that the pairs of segments (σ0, σ1 ) selected for preference queries stay close to the current policy’s visitation distribution”. 
The authors need to more clearly outline how their work is different from QPA.
2. The authors’ third contribution is about the reward model’s accuracy on out-of-distribution data. In particular, the reward model can only output accurate values for trajectories it has previously trained on. However, I’m not convinced this is a new finding. The reward models are trained via supervised learning, therefore this seems like an overfitting/generalization issue, which has been heavily studied before.


Lack of Experimental Details:

The authors refer the readers to Appendix G for a complete understanding of the experimental details, but Appendix G only contains hyperparameter details. There is no mention of:

1. How were preferences elicited? I’m assuming preferences were obtained through a scripted teacher but it does not mention it anywhere in the text.

2. How many seeds were run?

3. What are the error bars being visualized in Figures 2 and 3?


Lack of Supporting Evidence for the Effectiveness of the Proposed Algorithm:

1. PPE was evaluated in 9 environments, however, PPE only appeared to have distinctly higher performance in Humanioid-stand. There are significant overlaps in error bars in all other environments.  

2. In addition, the authors did not perform statistical analysis on any evaluation metrics such as final performance or area under the curve. 

3. Did any experiments involve actual human preferences? The authors note that PPE achieves significant improvement in human feedback efficiency, however, I’m not sure if any humans were involved. I don’t think any claims can be made about human teachers if only simulated/scripted teachers were used. 

4. Unclear why PPE was integrated with QPA. See Question 1. 

Minor comments:

The authors note “We selected six distinct complex tasks from DMControl”, however, I would argue that (Walker-walk and Walker-run), and (Quadruped-walk and Quadruped-run) are not distinct. I think this claim is a bit too strong.

### Questions
1. Why is PPE being integrated with QPA and not PEBBLE? Both RUNE and SURF are integrated on top of PEBBLE. Therefore, it seems like an unfair advantage to PPE if it is being added on top of a more advanced PbRL algorithm. Or put differently, why did the authors not integrate the other PbRL baselines on top of QPA? In the QPA paper, the authors note that it can be integrated on top of any off-policy PbRL algorithm, including SURF and RUNE. 

2. Does PPE improve performance if it is added on top of other PbRL algorithms, as the authors mention it is highly compatible with existing strategies and frameworks.

### Soundness
1

### Presentation
2

### Contribution
2
