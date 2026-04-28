# Constraint-Conditioned Actor-Critic for Offline Safe Reinforcement Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Offline safe reinforcement learning (OSRL) aims to learn policies with high rewards while satisfying safety constraints solely from data collected offline. However, the learned policies often struggle to handle states and actions that are not present or out-of-distribution (OOD) from the offline dataset, which can result in violation of the safety constraints or overly conservative behaviors during their online deployment. Moreover, many existing methods are unable to learn policies that can adapt to varying constraint thresholds. To address these challenges, we propose constraint-conditioned actor-critic (CCAC), a novel OSRL method that models the relationship between state-action distributions and safety constraints, and leverages this relationship to regularize critics and policy learning. CCAC learns policies that can effectively handle OOD data and adapt to varying constraint thresholds. Empirical evaluations on the $\texttt{DSRL}$ benchmarks show that CCAC significantly outperforms existing methods for learning adaptive, safe, and high-reward policies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a constraint-conditioned actor-critic method, which combines a constraint-conditioned variational autoencoder (CVAE) and a constraint-conditioned classifier to learn this relationship.

### Strengths
1. The paper is well-written and easy to follow.

2. The visualization of the offline datasets is quite intuitive, and the experimental design, along with the ablation study, adds significant value to the research.

3. The method can learn safe and high-reward policies from offline datasets, demonstrating better adaptability and robustness to distribution shifts.

### Weaknesses
1. The experimental environments are relatively simple and do not include more complex tasks, such as humanoid. In the experimental section, the authors use only three seeds, which I believe is insufficient. If possible, could you provide additional results using more seeds (at least five)?

2. Although the algorithm demonstrates performance compared to the baselines while maintaining safety, Figure 9 suggests that the algorithm's sample efficiency is not good.

### Questions
1. The training process of CCAC appears to separate the training of the CVAE and the policy (optional once). Why not consider continuing the training of the CVAE during the policy training process?

2. CCAC demonstrates zero-shot adaptation to different cost budgets. In addition to empirical evidence, could you provide some intuitive explanations for this capability?

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
In the context of offline safe reinforcement learning, this paper implements penalties for out-of-distribution (OOD) actions using a generative model, such as a conditional variational auto-encoder (CVAE). 
Then, the authors propose a method to train a policy that conditionally adapts to different cost budgets using overestimated cost Q functions.

### Strengths
- The paper is well-written and easy to read.
- The proposed method shows the best performance.
- Through various ablation studies, the paper effectively shows that the proposed method is robust to OOD scenarios and can generate adaptive behaviors across different cost budgets.
- Section 5.3 provides experimental justification for the usage of CVAE and good visualization of the overestimated $Q_C$.

### Weaknesses
 - In lines 46-53, the need for a varying threshold is highlighted, but this issue has been addressed in several studies [1,2]. 
It is crucial to motivate the proposed method by identifying shortcomings or potential improvements in the existing techniques on varying thresholds.

- In line 98 of Related Work, the statement “these methods overlook the dependence of actions on the constraints” seems to need to be toned down a bit. This seems obvious since the works mentioned by the authors are related to offline RL, not offline safe RL.

- The overview in Figure 1 needs to be further elaborated. It is difficult to understand what is being illustrated in the figure, as it does not clearly describe the inputs and outputs of each model and does not explain the learning flow. Also, the caption should include a description of each module and arrow.

- In lines 203-204, there is a need for a detailed explanation of the mechanism for generating out-of-distribution (OOD) data. According to the attached code, it appears that the $(s, a)$ pairs are generated through the CVAE using various Gaussian noise vectors $z$. Pairs, where the value of $h$ is less than $0.5$, are designated as OOD data. This process should be clearly explained in the paper.

- The TREBI paper [2] also deals with various cost budgets in offline environments. Unfortunately, the authors do not compare CCAC with this method, which deals with the same problem as the proposed method.



### Questions
- It appears that the policy is trained through Equation 9. In traditional offline reinforcement learning methods, a penalty term is added to a policy loss to ensure that the actions of the policy do not deviate from those in the dataset. However, the proposed method addresses this by solely using the overestimated $Q_C$. Is this correct?

- In Table 1, COptiDICE shows significant constraint violations, but in its original paper, COptiDICE reported low violations in similar tasks. 
An explanation for this discrepancy is needed. 
In line 323, the authors mentioned that this is due to biased estimation. Still, this explanation is not entirely convincing since COptiDICE itself includes a component that trains the policy by overestimating the cost of OOD data.

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
4

### Summary
This paper focused on offline safe RL. The authors proposed CCAC that can learn with adaptive constraint budgets. CCAC first trained a binary classifier to distinguish OOD state-action pairs with constraint budgets acting as labels. The OOD distribution was then used for constrained optimization for the actor and critic. The authors provided theoretical justification and comprehensive empirical investigation.

### Strengths
The paper is well-written in general. The idea is interesting and technical details easy to follow. The authors conducted extensive experiments showing CCAC performed favorably against the existing methds.

### Weaknesses
My concern is that the paper seems to blur the boundary between out-of-distribution and out-of-budget (OOB) state-action pairs. If we assume all OOD state-action pairs are unsafe, then it means the algorithm cannot generalize to unseen state-action pairs since their costs are lower bounded by $\epsilon$. This seems at odds with the standard offline RL setting which seeks to generalize and improve upon the behavior policy and beyond the dataset. 
If we recall that the key issue of offline RL lies in that incorrect action values of unseen state-action pairs cannot be corrected, then in my opinion mixing OOD and OOB runs the risk of not generalizing beyond the dataset $\mathcal{D}$ since safe unseen $(s,a)$ always have $Q_c \geq \epsilon$. If this is true, then later analysis like Theorem 4.1 is not very meaningful (which itself is an variant of CQL derivation imo). The core issue is that the OOD label assigned by $h(s,a|\kappa)$ is solely determined by whether the cumulative constraint exceeds the threshold. Even if the label is 0, it doesn't necessarily mean the sample is not OOD, but rather only not OOB. Consequently, the agent is presented with a tuple (?, low risk), lacking information about the value, which risks the original OOD problem. This approach may work when high-risk actions also have low value, but it's unclear how it would perform when high-value, low-risk OOD actions exist.

### Questions
Please refer to the above for questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the challenge of safe offline reinforcement learning (RL) and introduces a novel approach termed Constraint Conditioned Actor Critic (CCAC). CCAC is designed to facilitate adaptive policy learning under various constraint limits while ensuring high rewards and minimizing distributional shifts. To achieve this, CCAC employs a cost-to-goal conditional Variational Autoencoder (CVAE) to model the adaptive behavior across different safety constraint intensities. Additionally, a discriminator is utilized to autonomously evaluate the safety levels. By integrating the discriminator with the CVAE, CCAC establishes an Out-of-Distribution (OOD) detector, \( v(s,a|k) \), that assesses both distributional shift and safety performance concurrently. Utilizing this framework, CCAC executes standard actor-critic updates to develop a constraint-aware critic and policy. The effectiveness of CCAC has been demonstrated through evaluations on the DSRL benchmark and extensive ablation studies.

### Strengths
1. The concept of CCAC is intuitively straightforward and easy to implement.

2. This paper is well-written, clearly highlighting the challenges, motivations and contributions.

3. CCAC achieves SOTA performance in several DSRL envs.

4. The ablation studies are comprehensive, clearly demonstrating the advantages of CCAC over other baseline methods. Notably, CCAC exhibits constraint-aware behavior that guarantees strong performance (high rewards and low costs below the constraint limit). Furthermore, CCAC demonstrates robustness across varying quantities of data.

### Weaknesses
Several minor weaknesses are present in the study. Addressing these concerns could significantly improve my evaluation of the manuscript:

1. Limited evaluation environments. The DSRL benchmark offers over 30 environments, but this paper only conducts experiments on solely 9 envs. Including more scenarios can substantially enhance the paper quality.

2. Some assumption. CCAC utilizes the trained CVAE to augment the dataset and annotates these data with their original cost/reward values. While this approach is acceptable, it may introduce some errors if the reward/cost functions are not smooth across the spatial space, which then will introduce some annotating errors.

3. The overconservative behavior of FISOR is primarily attributed to the use of hard constraint, rather than its use of the largest feasible region as claimed by the authors in line 323. In fact, using the largest feasible region will include more actionable actions for policy optimization and so can reduce the overconservatism.

### Questions
See weaknesses for details.

### Soundness
3

### Presentation
3

### Contribution
3
