# Hybrid Preference Optimization: Augmenting Direct Preference Optimization with Auxiliary Objectives

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
For aligning large language models (LLMs), prior work has leveraged reinforcement learning via human feedback (RLHF) or variations of direct preference optimization (DPO). While DPO offers a simpler framework based on maximum likelihood estimation, it compromises on the ability to tune language models to easily maximize non-differentiable and non-binary objectives according to the LLM designer's preferences (e.g., using simpler language or minimizing specific kinds of harmful content). These may neither align with user preferences nor even be able to be captured tractably by binary preference data. To leverage the simplicity and performance of DPO with the generalizability of RL, we propose a hybrid approach between DPO and RLHF. With a simple augmentation to the implicit reward decomposition of DPO, we allow for tuning LLMs to maximize a set of arbitrary auxiliary rewards using offline RL. The proposed method, Hybrid Preference Optimization (HPO), shows the ability to effectively generalize to both user preferences and auxiliary designer objectives, while preserving alignment performance across a range of challenging benchmarks and model sizes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
While Direct Preference Optimization (DPO) is simpler and more stable than Reinforcement Learning from Human Feedback (RLHF), it falls short when it comes to incorporating arbitrary non-differentiable objectives. RLHF, particularly with on-policy algorithms like Proximal Policy Optimization (PPO), can be unstable and requires sampling from the language model during training, which is computationally expensive. The authors introduce Hybrid Preference Optimization (HPO) which addressees these issues by combining DPO and RLHF. HPO combines the simplicity of DPO with the flexibility of RLHF, allowing LLMs to be tuned using arbitrary auxiliary objectives without the need for on-policy generation. This hybrid approach leverages the strengths of both methods, aiming to improve the alignment of LLMs with both user preferences and designer-specified objectives.

### Strengths
1. The paper presents a novel method for integrating arbitrary auxiliary objectives into the DPO framework. This enhances the versatility of DPO, making it more practical for tuning LLMs to meet specific goals beyond user preferences.
2. In Section 4.1, the authors provide solid motivation for incorporating auxiliary rewards, backed by proofs and examples.
3. Implementing HPO requires only about 10 additional lines of code on top of the existing $\Psi$PO algorithm.

### Weaknesses
1. The paper frequently references $\Psi$PO and KTO but doesn't adequately explain these concepts in the preliminary sections. The writing is a bit hard to follow, particularly for readers unfamiliar with these specific preference optimization techniques. A more thorough introduction or a brief overview of these methods would greatly improve the paper's accessibility. The lack of clarity surrounding these foundational methods makes it difficult to fully grasp the novelty and contribution of the proposed HPO approach.
2. The method involves training an extra value network which adds to the computational load. While the authors claim this overhead is minimal, a more detailed analysis of the computational cost, including memory usage and training time, would be beneficial. It is important to quantify the practical implications of this additional network, especially when considering the resource constraints often encountered in large language model training.
3. HPO depends on manually defining and constructing auxiliary rewards. This process can be time-consuming and may require domain expertise. The paper does not provide sufficient guidance on how to effectively design these rewards, potentially limiting the practical applicability of the method. The lack of a systematic approach to reward engineering could make it challenging for practitioners to leverage HPO effectively.
4. Tables 2a, 2c, and 2d are not referred and properly discussed in the text. The absence of a detailed discussion of these results undermines the overall analysis. The paper should explicitly reference and interpret the findings presented in these tables, highlighting their significance and relevance to the study's conclusions.
5. The performance evaluation relies solely on assessments from GPT-4. While GPT-4 is a powerful language model, relying solely on its evaluations introduces a potential bias. Incorporating additional metrics, such as evaluations using reward models like ArmoRM, would provide a more comprehensive evaluation and strengthen the validity of the findings. The lack of diverse evaluation metrics raises concerns about the robustness of the reported results.
6. The paper doesn't include a Pareto analysis of different auxiliary rewards. This would provide understanding how the method balances multiple objectives and where trade-offs might occur. Without such analysis, it is difficult to assess the practical implications of using different auxiliary rewards and their impact on overall performance.

### Questions
1. Could you explain what $L_2^{\tau}$ represents in Equation 12?
2. In Figure 4, what does "evaluation generation length relative to the chosen response" mean? Could you elaborate on this to clarify how it relates to your findings?

### Soundness
2

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
1

### Summary
The paper introduces a method called Hybrid Preference Optimization (HPO) to align large language models more effectively. HPO combines the efficiency of direct preference optimization (DPO) with the flexibility of reinforcement learning from human feedback (RLHF), enabling stable, computationally efficient training that focus on the capability of maximizing arbitrary non-differentiable and non-binary objectives. 
The experimental results show that HPO outperforms traditional alignment methods, including DPO, RLHF, and other multi-objective approaches, in aligning language models with user preferences. HPO demonstrated marked improvements in optimizing auxiliary objectives, particularly for safety and readability, with lower violation rates on safety benchmarks and better readability scores compared to baselines.

### Strengths
The method is straightforward, requiring only a minor adjustment to KTO, yet it greatly enhances the optimization of key auxiliary objectives.

### Weaknesses
Although the authors performed impressively on different benchmarks, I have some concerns. I would be happy to discuss them with the authors further.

1.  **Lack of comparision**. The first concern is about the methods selected for comparison. I think the authors need to select better methods that are aligned with their hypothesis, like safe-RLHF. Also, The proposed method is similar to the Direct Reward Optimization (DRO) method. It would be great if the authors considered these methods as competitors.

2.  **Old models**. Another concern is outdated models. I suggest using the new versions of the LLaMA, Mistral, or Gemma-2 models.

3.  **Lack of exploration on hyperparameters**.DPO, KTO, and other optimization methods are very sensitive to different hyperparameters like beta, batch size, and learning rate. So, I encourage the authors to compare the methods using their best hyperparameters.

### Questions
n/a

### Soundness
3

### Presentation
4

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
In this paper, the authors propose a new multi-objective preference optimization method. The main advantage of this method is that it is a one-step fine-tuning method that performs well on multiobjectives. They compare this method with offline reinforcement learning methods like oPPO and direct preference methods like KTO and DPO. They indicate that this method outperforms others on all objectives.

### Strengths
It is interesting to propose a new multiobjective direct preference optimization method. This paper also focuses on broad experiments and analysis, which is the main strength of this paper.

### Weaknesses
1. The proposed method introduces an additional term in the objective to optimize auxiliary rewards, while most of the baselines only optimize towards the preference dataset. There could be straight-forward approaches to incorporate the auxiliary reward to the single-objective baselines, e.g., fit a reward model on the compound reward and use it to construct preference pairs. Further, the authors also barely discuss their choice of the auxiliary loss with other variants (see point 2).

2. Optimizing the reverse KL in equation (8) in offline setting is investigated in [1], where using self-normalized importance sampling with proper weight leads to better performance than optimizing the forward KL. The authors should discuss and compare with this related approach. 

3. A crucial aspect of multi-objective alignment is to evaluate the frontier of multiple objectives. However, the paper did not compare with the multi-objective baselines in terms of this aspect.

### Questions
All concerns and suggestions are mentioned in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposed Hybrid Preference optimization which optimizes the human preference along side with weighted auxiliary rewards, e.g., toxicity, readability, etc. Specifically, the authors augment the preference loss with an advantage-weighted maximum likelihood objective and use expectile regression to train the value network. In the experiment, the authors consider several auxiliary objectives, e.g., reading level and safety.

### Strengths
The author conduct extensive experiments in the setting of preference learning with auxiliary objectives, together with several ablation studies on effect of varying hyperparameters, reward weights.

### Weaknesses
1. The proposed method introduces an additional term in the objective to optimize auxiliary rewards, while most of the baselines only optimize towards the preference dataset. There could be straight-forward approaches to incorporate the auxiliary reward to the single-objective baselines, e.g., fit a reward model on the compound reward and use it to construct preference pairs. Further, the authors also barely discuss their choice of the auxiliary loss with other variants (see point 2).

2. Optimizing the reverse KL in equation (8) in offline setting is investigated in [1], where using self-normalized importance sampling with proper weight leads to better performance than optimizing the forward KL. The authors should discuss and compare with this related approach. 

3. A crucial aspect of multi-objective alignment is to evaluate the frontier of multiple objectives. However, the paper did not compare with the multi-objective baselines in terms of this aspect.

[1] Ji, Haozhe, et al. "Towards efficient and exact optimization of language model alignment." ICML (2024).

### Questions
1. Could the authors incorporate the auxiliary rewards into the preference learning baselines for a fair comparison?

2. Could the authors compare with other variants of implementing the auxiliary objective, e.g., [1] that directly optimizes the reverse KL.

3. Could the authors compare their method with multi-objective baselines in terms of trade-offs among objectives?

### Soundness
3

### Presentation
3

### Contribution
2
