# Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 6, 10

## Abstract
Aligning to human preferences and/or intentions is an important requirement for contemporary foundation models. To ensure alignment, popular approaches such as reinforcement learning with human feedback (RLHF) break down the task into three stages: (i) a model is computed with supervised fine-tuning (SFT) based upon large demonstrations data, (ii) a reward model (RM) is estimated based upon human feedback data, and (iii) reinforcement learning (RL) is used to further refine the SFT model by optimizing the estimated reward model.  Demonstrations and human feedback data reflect human user preferences in different ways. As a result, the reward model estimate obtained from only human feedback data is likely not as accurate as a reward model estimate obtained from both demonstration and human feedback data. A policy model that optimizes the reward model estimate obtained from both demonstration and human feedback data will likely exhibit better alignment performance. We introduce a tractable algorithm for finding the reward and policy models and provide a finite-time performance guarantee. Additionally, we demonstrate the efficiency of the proposed solution with extensive experiments including alignment problems in LLMs and robotic control problems in MuJoCo. We observe that the proposed solutions outperform the existing alignment algorithm by large margins, especially when the amounts of demonstration and preference data are unbalanced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces the Alignment with Integrated Human Feedback (AIHF) framework for learning a policy from both demonstrations and preferences. AIHF poses reward and policy learning as a single bi-level optimization problem where the outer loop maximizes optimizes the policy to fit the demonstrations and the reward to fit the preferences and the inner optimizes the policy with respect to the learned reward. The paper illustrates how AIHF connects to prior alignment algorithms and proposes a concrete instantiation of AIHF. Empirically, AIHF improves the alignment over standard RLHF.

### Strengths
1. The single stage-learning of reward and policy from AIHF learns a more robust reward model that leverages both demonstrations and preferences compared to two stage approaches that first learn a reward function from only preference data.

1. The paper demonstrates how the AIHF framework can be specialized to an RLHF, DPO, or self-play like approach. This shows that AIHF offers a more general alignment formulation.

1. Section 3.4 theoretical and numerical evidence for why AIHF is superior to a two-stage alignment process like in standard RLHF.

1. The paper provides performance guarantees for the proposed AIHF algorithm. 

1. AIHF outperforms RLHF and regular SFT on the Anthropic-HH dataset across several Pythia model sizes. 

1. AIHF with the DPO and Self-Play instantiation improves the performance of an RLHF model when trained with the Ultrafeedback-binary preference dataset and Ultrachat200k demonstration dataset.

1. Results in the supplementary also show AIHF improves performance relative to RLHF for continuous control tasks.

### Weaknesses
1. The paper claims that AIHF outperforms existing alignment methods when the data is unbalanced (L78, L322), but this claim does not appear supported by the results in Section 5. The results in Figure 4 right show AIHF suffering as the preference and demonstrations become unbalanced. Contrary to the caption in Figure 4, these results also do not test if AIHF outperforms RLHF with different demonstration ratios since no RLHF result is displayed in Figure 4 right. This leaves it unclear if AIHF does have any benefit over existing alignment algorithms in unbalanced datasets.

2. The evaluation of AIHF in Section 5 is hard to follow. Figure 2 evaluates the performance of the proposed AIHF algorithm from Section 4, but Figure 3 evaluates the DPO and Self-Play versions. This makes it difficult to evaluate the empirical significance of the AIHF algorithm proposed in Section 4.


3. Insufficient empirical comparison to prior work. The paper does not evaluate the performance of the specialized variants of AIHF against the existing versions of the algorithms such as DPO and SPIN. These comparisons are crucial for evaluating the benefits of the AIHF framework. Additional comparisons to other existing such as IPO [1] would also strengthen the results.

4. The paper does not clearly discuss the limitations of AIHF. 

5. The MuJoCo results in Appendix A.2.1 are missing important comparisons. Again, Figure 5 does not compare against existing alignment algorithms like DPO. Additional results comparing the quality and balance of this preference and demonstration data would also strengthen these results. This would confirm if RLHF is indeed suffering due to low-quality preference data as claimed. 

Minor:
1. L476 should explicitly reference Figure 4. When first reading, it was unclear where this study was located.

2. Figure 3 should provide exact numbers of the bars in the chart for more detailed empirical comparisons since many of the results are very close.

### Questions
1. In Section 6, Why not compare all of AIHF, Self-Play-AIHF, and AIHF-DPO in Figures 2 and 3? Does the algorithm proposed in Section 4 empirically outperform AIHF-DPO and Self-Play-AIHF? 

1. Are the improvements of AIHF over the bsae Zephyr-Beta model significant? It appears the average improvement is only a couple of percent?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel learning framework that provides a unified view for reinforcement learning, learning from demonstration, and preference learning. The key idea is to solve all three components simultaneously instead of following the staged approach of typical reinforcement learning with human feedback. The paper discusses many interesting insights, such as framing other algorithms as a special version of the proposed framework, insights into why the proposed method works better, and so on. The proposed work is validated mainly on LLM training problems, but also Mujoco simulated environments are also discussed in the appendix.

### Strengths
* The paper presented a novel perspective for preference learning + reinforcement learning problems to approach them simultaneously rather than solving them as separate stages.
* The paper proposed a practical learning algorithm and evaluated it on large-scale LLM data.
* The paper provides numerous interesting insights.

### Weaknesses
 * In my humble opinion, Section 3.4. WHY AIHF CAN OUTPERFORM TWO-STAGE ALIGNMENT APPROACHES can be improved. Overall, it discusses some mathematical reasons why AIHF works better than RLHF. However, I feel like it depends on several assumptions, such as |D| >> |P|. But is it always true? I always thought preference data was much cheaper than demonstration because it is only a yes/no binary question. 
* Also, eventually, RL will dominate, and it can achieve the desirable performance no matter what kinds of data are provided. 
* The section is not written concisely compared to its importance. I think it would be better if there was one paragraph that summarized general insights.

### Questions
I would appreciate it if the authors could resolve my questions above.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the limitations of current alignment methods, particularly highlighting that the reward model may not be sufficiently well-trained and that demonstrations contain additional information valuable for reward models. The authors then propose a joint learning framework for both reward and policy models to mitigate these issues, demonstrating that their approach can outperform existing RLHF solutions.

### Strengths
This paper offers comprehensive theoretical proofs and thorough explanations.

### Weaknesses
1. Policy used during preference collection: It is unclear which policy is used during this phase. Based on my understanding, the LLM employs the SFT model to gather human feedback. Meanwhile, the proposed approach seems to assume that the preference dataset is pre-existing before training. In other words, please explicitly state which policy is used to generate samples for human feedback and clarify if a pre-existing preference dataset is assumed to be available or it will be generated during the training process.

2. Unbalanced data claim: The claim that the proposed method performs better with unbalanced data is questionable. Typically, data preprocessing can effectively address this issue. Please provide more evidence supporting this claim, such as by comparing the method to baseline approaches that employ standard data preprocessing techniques for handling imbalanced datasets. Specifically, the paper should clarify whether the 'unbalanced data' refers to imbalanced labels within the preference data or an imbalance between the size of the preference data and the demonstration data. If it is the latter, this needs to be explicitly stated and justified, as it is not a standard definition of unbalanced data in machine learning.

3. Reward model improvement assumption: The framework assumes that incorporating demonstrations leads to a better-trained reward model. However, the paper lacks direct evidence showing that the reward model improves as a result. It would be beneficial to include an analysis of the reward model's performance, such as by evaluating its correlation with human preferences or by using a benchmark dataset designed for reward model evaluation. Without such evidence, it is difficult to validate the claim that demonstrations contribute to a better reward model.

4. Effect of human feedback vs. demonstrations: In typical LLM training, the number of demonstrations is orders of magnitude larger than the human feedback dataset. The reviewer is concerned that, during joint training of the reward and policy models, the influence of human feedback might be diminished. Please discuss strategies for balancing the influence of demonstrations and human feedback during joint training, or provide experiments that illustrate the relative impact of each data source on the final model performance. The paper should consider the potential for the reward model to overfit to the demonstration data, thereby reducing the impact of the human preference data.

There are also a few minor issues with the paper that need attention:

(1). The notation for human feedback data in line 099 is identical to the notation used for the trajectory in line 088, which may cause confusion.

(2). Line 232 defines V_theta, but it does not seem to be utilized anywhere in the rest of the paper (except appendix).

### Questions
1. The joint training is implemented using a shared parameter θ for both the policy and reward models, which is somewhat unclear. Would it be possible to decouple this into two independent parameters for each model, or are the two models intended to share parameters entirely? This distinction needs further clarification.

2. Figure 2 presents a performance comparison of Pythia models with varying parameter sizes. As the number of parameters increases, the performance gap appears to narrow. Is there any further analysis or explanation provided for this observation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes a new framework that utilizes both demonstration data and preference data for better alignment. This idea is novel and interesting. Moreover, the paper also provides a general theoretical bi-level formulation that not only induces the proposed AIHF, but also can reduce to some major RLHF and IRL methods as special cases. The paper proposes an efficient single-loop algorithm to solve the bi-level optimization problem and theoretically guarantee the finite-time convergence of the proposed algorithm. Extensive empirical evaluations are provided to validate the effectiveness of the proposed method.

### Strengths
This paper proposes a novel and effective integration of IRL and RLHF to improvement alignment. I am actually very happy with this paper due to this novel integration and the associated theoretical framework. Moreover, I think that this paper opens a door for future research on the integration of IRL and RLHF for better alignment. The strengths of this paper include:
1. Novel and interesting idea of the integration of IRL and RLHF for better alignment.
2. A general bi-level formulation of this integration which can also reduce to some major IRL and RLHF methods as special cases.
3. Excellent presentation where the authors explicitly deliver their ideas. More importantly, the authors provide insights to help readers better understand why the proposed framework can lead to better alignment. These insights in Section 3.4 are very helpful for readers to get an initial understanding of the advantages of the proposed framework.
4. Solid theoretical guarantee for the proposed algorithm.

In general, I think that this paper can contribute to the RLHF and IRL community.

### Weaknesses
There is no obvious weakness of this paper. Please see questions.

### Questions
1. In the introduction (lines 63-64), it is said that "a joint approach to learning reward and policy models may improve alignment at
the expense of potentially significant additional computational effort". At that time, I expected that this method would require additional demonstration data, compared to the standard two-stage RLHF method. However, Figure 1 shows that the demonstration data in AIHF is the demonstration data used for SFT in the standard RLHF, so that there is no additional demonstration data needed? Then I am not sure why the proposed method may potentially lead to additional computation. Of course, the computation is higher compared to RLHF using preference data only. However, RLHF also needs demonstration data to first compute SFT policy. If we compare "AIHF" and "SFT+RLHF", intuitively "SFT+RLHF" will be more computationally expensive because it uses the same amount data as AIHF and it solves two separate optimization problems. The counterpart of AIHF is not RLHF but RLHF+SFT, right? So that we need to compare AIHF and RLHF+SFT.

2. In Section 3.4, it is shown that AIHF policy is somehow a weighted average of IRL policy from demonstrations and RLHF policy from preferences, therefore the AIHF policy reduces variance. I agree that this average can reduce variance. Suppose the demonstration needed for SFT is the same demonstration data in AIHF, the standard RLHF has a KL regularization $D_{KL}(\pi||\pi_{SFT})$ (which relates the learned policy $\pi$ to the policy $\pi_{SFT}$ learned from demonstration data). If we linearize the KL regularization, this may also lead to a (weight) average of $\pi_{SFT}$ (demonstration) and the RLHF policy learned from preference?

### Soundness
4

### Presentation
4

### Contribution
4
