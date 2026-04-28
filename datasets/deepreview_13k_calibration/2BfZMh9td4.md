# Beyond One-Preference-for-All: Multi-Objective Direct Preference Optimization

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 1, 6, 5

## Abstract
Language models (LMs), despite aligning well with an average labeler through reinforcement learning from human feedback (RLHF), may not universally suit diverse human preferences. Recent approaches therefore opt for customization by collecting multi-dimensional feedback and creating distinct rewards for each dimension (e.g., helpfulness, harmlessness, honesty). LMs can then be tailored to different preferences using multi-objective RL (MORL) with different reward weightings. Yet, RL fine-tuning is unstable and resource-heavy, especially for MORLHF with diverse and usually conflicting objectives. In this paper, we present Multi-Objective Direct Preference Optimization (MODPO), an RL-free algorithm that extends Direct Preference Optimization (DPO) for multiple alignment objectives. Essentially, MODPO trains different LMs to represent different collective reward models that combine all objectives with specific weightings. With a simple cross-entropy loss, the LMs optimized against the MODPO objective are analytically the exact solutions of the original MORLHF objective. Empirical results in safety alignment and long-form question answering confirm that MODPO matches or outperforms existing methods, efficiently producing a Pareto-optimal set of LMs that cater to diverse preferences with 3 times less computational resources compared with MORLHF.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends Direct Preference Optimization (DPO)  to Multi-Objective Direct Preference Optimization (MODPO) directly. MODPO trains different LMs to represent different collective reward models that combine all objectives with specific weightings. With a simple cross-entropy loss, the LMs optimized against the MODPO objective are analytically the exact solutions of the original MORLHF objective.

### Strengths
This paper extends DPO to MODPO directly for solving the multi-objective problems with LM.

### Weaknesses
1. The contribution is limited because it is just a direct extension of an existing method.
2. The experiment fails to show multiple objectives, i.e., no less than three objectives. 
3. This paper fails to evaluate the proposed method on real-world datasets like the TripAdvisor Hotel Review Dataset, which naturally includes multiple feedback scores from multiple aspects.

### Questions
1. I suggest the authors add experiments on more than two objectives on real-world datasets like the TripAdvisor Hotel Review Dataset, which naturally includes multiple feedback scores from multiple aspects.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper present MODPO, a fine-tuning method for large language models without reinforcement learning. 

The method suits for human-in-the-loop setting, where human preference has diversity and only pareto optimal solutions are available while no universal optimal solutions can be found. The RL-free algorithm extends Direct Preference Optimization (DPO) for multiple alignment objectives. 

The purpose and exprimental results show out-performance by producing a Pareto-optimal set of LMs that cater for diverse preferences with much less computation resources compared with RL-based method.

### Strengths
- Overall this paper is well-written with clear motivation - to overcome the resource-intensive RL-based fine-tuning methods for LMs, a RL-free framework that can fit better to a real-world situation where resources are limited.

- Clear notations and detailed implementation and ablation examples in the Appendix. These add value to the communication to a wider community 

- The impact of the proposed algorithm is convincing - by conducting KL-controlled experiments.

### Weaknesses
 - An adoption of DPO for fine-tuning LMs results in convincing results, however, conditions for delivering such results, and requirements in collecting datasets.


### Questions
- In Figure 1, the proposed MODPO is positioned as a marginalized reward formulation for fine-tuning LMs. This is generally in line with the well-known advantage of discriminative learning techniques in leveraging small datasets. What are the pros and cons of adopting this technique to deliver the Pareto-optimal solution? Are there alternative techniques available?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Language models aligned with average human preferences may not suit diverse preferences. Recent approaches collect multi-dimensional feedback and train models on distinct rewards per dimension to customize for preferences. Multi-objective reinforcement learning for this is unstable and inefficient. This paper presents Multi-Objective Direct Preference Optimization (MODPO), an RL-free algorithm extending Direct Preference Optimization to multiple alignment objectives. MODPO efficiently produces a Pareto-optimal set of customized language models for diverse preferences, demonstrated in safety alignment and question-answering tasks.

### Strengths
* MODOPO enables customized language models without needing complex, unstable multi-objective reinforcement learning. The integration of linear scalarization into preference modeling is a creative way to reuse standard pipelines.
* The paper is technically strong, with a formal problem definition, clear methodology, and mathematical proofs demonstrating that MODPO optimizes the desired objective. Experiments across two tasks verify that MODPO matches or exceeds prior methods in quality and efficiency.
* MODPO provides an efficient way to produce customized language models catering to diverse user preferences. This enhances accessibility and avoids a one-size-fits-all approach.

### Weaknesses
 * The experiments, while showing compute savings, are still limited in scale and scope. Testing on more alignment objectives, model sizes, and tasks would strengthen claims of efficiency and customization ability. ablation studies could isolate benefits.
* The choice to focus on two objectives may undersimplify real-world diversity of preferences. Experiments with 3+ objectives could reveal whether MODPO scales effectively.

### Questions
* Could you provide more intuition on why the multi-stage training provides benefits like stability and efficiency? Some analysis or ablation study isolating the impact would strengthen this claim.
* For the safe response examples, could you discuss if the responses seem "too safe" - is there a way to steer generation away from trivial safest responses?
* What scaling limitations have you found in practice when increasing the number of objectives beyond 2? Experiments on 3+ objectives could reveal interesting trends.
* You mention MODPO could be used online by training on unlabeled data - could you elaborate on this idea more? Seems interesting for wider applicability.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper examines the issue of fine-tuning large language models (LLMs) based on human preferences for multiple objectives. To align these objectives and optimize LLMs, the authors introduce MODPO, a method that does not rely on reinforcement learning (RL). Instead, it builds upon DPO [1] and trains using pairwise comparison data. The MODPO pipeline consists of two stages: reward modeling for each objective and preference optimization with a specific preference configuration (represented by a weight vector of rewards). Experimental results on safety alignment and long-form QA tasks show the effectiveness of MODPO.

[1] Rafailov R, Sharma A, Mitchell E, et al. Direct preference optimization: Your language model is secretly a reward model[J]. arXiv preprint arXiv:2305.18290, 2023.

### Strengths
1. Aligning LLMs with human preferences of multiple objectives is a promising research direction. To the best of my knowledge, this work represents one of the early efforts in this area.
2. The authors present comprehensive results to support the proposed methods.
3. The paper is easy to follow.

### Weaknesses
1. One of the greatest advantages of DPO is that it avoid reward modeling. MODPO, however, requires reward modeling to perform preference optimization. This makes me question if MODPO is the appropriate extension of DPO to the multi-objective setting.
2. If I understand correctly, DPO variants cannot be compared to MODPO, MORLHF, and Best-of-n in the experiments. This is because these variants only use pairwise comparison data, while MODPO utilizes both rewards and pairwise comparison data. This difference in data usage makes a direct comparison problematic, potentially favoring MODPO due to the richer information it leverages.
3. Building on the previous question, I am curious if MODPO will significantly underperform when rule-based rewards are unavailable. If rewards are learned from pairwise comparison data, will it outperform DPO LW in this scenario?

### Questions
1. In Figure 3, some data points of MODPO are far from the pareto frontier. Does it contradict with the claim that it "shows evidence of strong and reliable customizations"?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
