# Offline Safe Policy Optimization From Human Feedback

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Offline preference-based reinforcement learning (PbRL) learns rewards and policies aligned with human preferences without the need for extensive reward engineering and direct interaction with human annotators. However, ensuring safety remains a critical challenge across many domains and tasks. Previous works on safe RL from human feedback (RLHF) first learn reward and cost models from offline data, and then use constrained RL to optimize a safe policy. However, inaccuracies in the reward and cost learning can impair performance when used with constrained RL methods. To address these challenges, (a) we introduce a framework that learns a policy based on pairwise preferences regarding the agent’s behavior in terms of rewards, as well as binary labels indicating the safety of trajectory segments, without access to ground-truth rewards or costs; (b) we combine the preference learning module with safety alignment in a constrained optimization problem. This optimization problem is solved using a Lagrangian method that directly learns reward maximizing safe policy without explicitly learning reward and cost models, avoiding the need for constrained RL; (c) to evaluate our approach, we construct new datasets with synthetic human feedback, built upon a well-established offline safe RL benchmark. Empirically, our method successfully learns safe policies with high rewards, outperforming baselines with ground-truth reward and cost, as well as state-of-the-art RLHF approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of learning a safe policy from offline human feedback, which comprises both reward preferences and binary safety labels. To tackle this, it proposes a framework containing two parts: 1) maximizing rewards using traditional contrastive preference learning and 2) encouraging safety by guiding the policy toward generating safer trajectories with higher probability. These two methods are then integrated using a Lagrangian approach. Extensive experiments across diverse tasks demonstrate the effectiveness of this approach.

### Strengths
1. The paper is well-structured and easy to understand. The authors convey their settings, motivations, and methods clearly, presenting a logical flow.
2. The experiments on the simulation tasks are extensive, containing 29 tasks across two environments. The baseline methods include both conventional offline RL methods and PbRL methods, which is good.

### Weaknesses
1. The paper states that "it is relatively scarce and expensive to collect safety preferences." However, I believe that obtaining direct safety labels for each trajectory, especially perfectly accurate ones, is even more challenging and, in many cases, unrealistic. The assumption of perfect binary safety labels is a strong one, and the paper doesn't adequately address the potential impact of noisy or inaccurate labels on the performance of the proposed method. In real-world scenarios, safety labels are often subjective and can vary depending on the annotator or the specific context, making the assumption of perfect labels a significant limitation.
2. This paper is more like incremental work, primarily combining some existing methods (e.g., contrastive preference learning for preference alignment, human-aware losses for safety concerns) to solve a new offline PbRL setting with reward preferences and safety binal labels. While the practical importance of this problem setting is acknowledged, the novelty of the approach could be seen as limited. The core contribution seems to be the integration of existing techniques rather than the introduction of a fundamentally new approach to the problem of learning from reward preferences and safety labels.
3. The offline dataset contains both reward preferences and safety labels, which the paper addresses separately and later integrates in a final optimization step. Specifically, the proposed method uses reward preferences to promote a reward-maximizing policy, while safety labels are employed to encourage safer behaviors within the dataset. However, exploring methods that leverage these two types of feedback in a more unified manner, rather than treating them independently, could potentially eliminate the need for constrained optimization (via the Lagrange method), thus simplifying the optimization process and reducing computational complexity. The current approach of treating reward and safety separately might not be the most efficient way to learn a safe and performant policy.
4. Although the paper introduces many baseline methods, I think it is indeed unnecessary to compare so many offline RL methods with ground-truth reward and cost since the two settings are different. Instead, the authors should investigate more efficient offline RLHF methods with offline labels for fair comparison. Please see the following questions for details.

### Questions
1. Could the authors include additional offline RLHF methods for comparison? For instance, a unified preference label prioritizing safety could be designed, where safer trajectories (according to the safety label) and higher-reward trajectories (according to reward preference) are preferred. This unified preference could then be used for policy alignment through CPL or RLHF. Additionally, it may be feasible to train a cost model to predict the cost of state-action pairs based on the safety label, which could then be integrated into the RLHF phase.
2. How are the cost preferences for Safe-RLHF generated, given that the offline dataset contains only binary safety labels? I believe that each binary label per trajectory segment conveys more information than preference, and comparing with a different dataset is not fair.
3. Can the authors study the situation where the safety labels are not perfect?

### Soundness
2

### Presentation
3

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
This paper introduces a framework for offline safe preference-based reinforcement learning. It assumes access to safe preferences in the form of binary labels instead of comparisons between two trajectories. Additionally, it proposes conducting preference learning through contrastive preference learning (CPL) and achieving safe alignment based on human-aware losses (HALOs). Safety alignment is then transformed into a constraint on the feasible policy set and thus integrated into preference learning. Finally, the paper presents a series of experiments on DSRL to evaluate the effectiveness of the proposed method.

### Strengths
- The paper is well-motivated. Circumventing explicit reward and cost learning could streamline the process and mitigate potential issues arising from explicit reward learning. Representing safety via binary safe labels instead of trajectory comparisons seems like a more reasonable and practical setting.
- Employing HALO-based safety alignment is intuitive and well-designed.
- The empirical evaluation and ablation studies are comprehensive, carefully demonstrating the effectiveness of the proposed approach.
- The paper is well-written and well-organized, with implementation details that are easy to understand.

### Weaknesses
 - In Section 6.1, the paper generates labels based on cumulative rewards rather than estimated advantages. However, the original CPL paper shows the equivalence of advantage and optimal policy, based on which it uses an advantage that considers both reward and policy entropy to label the data. So I would like more justification as to why using cumulative rewards works here.
- To generate binary safety labels for trajectory segments, the paper uses reshaped thresholds based on segment length. It would be better to briefly discuss the influence of this approximation on safety performance. 
- I notice that the $\delta$ in Eq. (11) is set to 0.9 or 0.95 instead of 1. Could you briefly explain the criteria for this setting and its influence on performance?
- In Eq.(4), does the symbol $P_{\pi_\theta}$ mean substituting $\pi^*$ in Eq.(3) with $\pi_\theta$? I think it would be helpful to explain this explicitly.
- I agree that circumventing explicit reward or cost learning is meaningful and brings benefits. Yet, the paper mentions that inaccuracies during reward and cost learning could be significant for performance. I would like to know if there is any supportive related work or experimental evidence to help me better understand this claim.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel framework called Offline Safe Policy Optimization from Human Feedback (POHF), which studies the RLHF problem under the setting of offline safe RL. The entire framework can also be viewed as an adaptation of the safe RLHF concept from LLMs to continuous control in RL. The whole framework directly optimizes the policy using Lagrangian objective contained reward and cost constraint, without the need for explicitly learning the reward and cost functions. By constructing a dataset based on DSRL, the paper demonstrates the effectiveness of its approach across multiple tasks and compares it with existing baseline methods, achieving significant improvements.

### Strengths
1. Optimizing Policies Without Explicit Reward and Cost Models: The method proposed in this paper enable policy optimization solely based on human preferences and safety feedback, eliminating the need for traditional reward and cost models. This significantly simplifies the policy optimization process, reducing inaccuracies associated with learning reward and cost models.

2. Comprehensive Experimental Validation: This paper conducts extensive experiments across 29 continuous control tasks, encompassing diverse environments and challenges. The results demonstrate that the proposed method outperforms existing baselines in multiple tasks, confirming its effectiveness and robustness.

### Weaknesses
1. The overall writing logic of the paper is relatively disjointed, which hinders comprehension, and there is considerable room for improvement. For instance, the connection between the challenges presented and the corresponding solutions in the abstract is quite weak. It is recommended that the background section 5.1.1 be integrated with the preliminaries in section 4 to enhance the paper's coherence.

2. The final method proposed in this paper is a combination of other approaches (CPL, HALOs, and the Lagrange objective in safe RL) within the POHF framework. And the POHF setting appears to be a transfer of Safe RL from LLMs to continuous control. Overall, the paper features a considerable amount of incremental work.

### Questions
1. The citation format for CPL in line 204 does not follow the correct guidelines. Incorrect Citation Format for Ethayarajh2024 in Line 260. Missing Equation Number for Formula in Line 298. Incorrect Citation Format for DSRL in Line 737. Incorrect Table Numbering Order. Lagrange should be written as a unified English name in the paper.

2. Why were experiments conducted on continuous control tasks, and is this method applicable and effective in discrete environments? 
 Please discuss the potential challenges or modifications required to apply this method in discrete environments, or explain the specific focus on continuous control tasks.

3. Given the algorithm's moderate performance and robustness, have potential improvements been considered?

4.  Are there particular aspects of the method that could benefit from theoretical analysis or guarantees?

### Soundness
2

### Presentation
1

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
This paper presents PreSa, for optimizing safe policies in offline reinforcement learning using human feedback. PreSa combines pairwise preference learning and safety alignment via binary safety labels, bypassing the need for explicit reward and cost models. The policy is optimized using a Lagrangian method within a constrained optimization framework. Empirical evaluations on synthetic human feedback demonstrate that PreSa outperforms state-of-the-art baselines in achieving high rewards while adhering to safety constraints across multiple tasks.

### Strengths
PreSa introduces a principled integration of preference and safety alignment, offering a novel method for offline safe RL. The technique eliminates the need for explicit reward and cost model learning, addressing the challenges of model inaccuracies.

### Weaknesses
1. Although PreSa avoids model inaccuracies without inferring the reward and cost model, uncertainty in offline datasets also leads to misspecifications. It is unfair to compare the two approaches without considering inaccuracies in your approach. I recommend the authors discuss specific types of uncertainties or misspecifications that might arise in their approach, such as distributional shift between the offline data and the online environment, or the impact of noisy or biased human preferences, and how these compare to the inaccuracies in reward and cost model learning. This would provide a more balanced comparison.
2. Why do pairwise preferences of trajectory segments only consider rewards when costs exist in a CMDP environment? I notice the dataset is split into ‘safe’ and ‘unsafe’ subsets, but do rewards really matter when a constraint has already been violated in the unsafe subset? It seems that focusing solely on reward within the unsafe subset could lead to optimizing for behaviors that are both unsafe and potentially less desirable overall. The authors should clarify the rationale behind this design choice, and discuss how it might affect the learned policy.
3. Such binary safety labels only consider hard constraint scenarios (correct me if I am wrong). Do the authors consider soft constraint scenarios where visiting an ‘unsafe’ trajectory segment after a sufficiently long number of steps would actually be safe, as indicated by the discounted cumulative version of constraint in Eq. (1)? I invite the authors to present a discussion on how PreSa might be adapted to handle soft constraints or discounted cumulative constraints, and what challenges this might present, such as how to define a suitable safety threshold or how to incorporate temporal dependencies in the safety assessment.
4. The experiments mainly include SafetyGym and BulletGym. I invite the authors to validate their results on more complicated environments, like CommonRoad, which offers a highly realistic simulation environment for developing and testing policies for autonomous systems in practical, safety-critical environments. The current evaluation lacks the complexity to fully demonstrate the robustness and generalizability of the proposed approach.

### Questions
1. It would be highly beneficial if the authors could also discuss the strategy for tuning the Lagrange multipliers used in Eq. 14. Since Eq. 14 employs a Lagrangian objective, tuning the updates of the Lagrange multipliers (such as the learning rate or initial values) poses significant challenges. Providing guidance on how to tune these parameters effectively would offer valuable insights to the community. I invite the authors to provide specific guidelines or heuristics they used for tuning the Lagrange multipliers or to discuss any challenges they encountered in this process.
2. Further, the Lagrangian methods do not necessarily guarantee safety, and it is challenging to recognize whether the optimum is reached. I invite the authors to comment on this point. I invite the authors to discuss potential strategies for addressing this limitation, such as incorporating additional safety checks or exploring alternative optimization techniques.
3. In Equation 14, it seems that some assumptions (e.g., Salter's condition) should be made to guarantee the existence of the strong duality. Do the authors miss this point? I invite the authors to explicitly state and justify the assumptions underlying their use of the Lagrangian method and to discuss how these assumptions might impact the applicability of their approach in different scenarios.

### Soundness
2

### Presentation
2

### Contribution
2
