## Human Reviewer 1

### Summary
The paper proposes GoalRank, a novel framework for training a single-stage, large-scale ranking model to replace the inefficient traditional two-stage Generator-Evaluator (G-E) paradigm. The G-E paradigm suffers from performance saturation due to the vast combinatorial ranking space. GoalRank introduces the Group-Relative Optimization Principle, using a pre-trained Reward Model and relative normalization within a group of lists to construct a Reference Policy. This allows the single-stage model to be trained effectively, achieving a superior approximation of the optimal policy. The framework is theoretically proven to surpass finite G-E systems and validated on a massive industrial platform, showing significant lifts in core business metrics.

### Strengths
1. This work provides a strong theoretical proof that a sufficiently large single-stage ranker can achieve a strictly lower approximation error than any finite two-stage system, confirming its strong potential for scaling laws.

2. The Group-Relative Optimization is an practical solution for training against the unobservable optimal policy in large-scale production environments.

3. It achieved significant and convincing lifts in key business metrics during large-scale online A/B testing on a platform with over 500 million daily active users.

### Weaknesses
1. The paper’s academic context is weakened by placing related work in the appendix, and its scope is blurred between the ranking and re-ranking domains, leading to an incomplete set of comparative baselines. See details in Questions 2

2. The theoretical proof is contingent on the optimal strategy $\pi^{*}$, which is substituted by an approximate Reward Model $\hat{r}$ in practice. While the paper claims robustness against bias in $\hat{r}$, the inherent difficulty in training a truly optimal reward model means this approximation gap remains a potential bottleneck, limiting the performance ceiling achievable in the real world.

3. The overall reproducibility is a concern and the scalability experiments fails to demonstrate that other, more sophisticated single-stage solutions (beyond simple DNNs) cannot also achieve similar or superior scaling behavior.

### Questions
1. Placing the Related Work section entirely in the appendix detracts from the integrity of the main paper structure, making it difficult for the reader to immediately contextualize the work against existing literature during the initial review.

2. The paper's claimed field focus is sometimes ambiguous. While positioned as a solution for ranking, many of its baselines and related works cited (e.g., DLCM, PRM) are strongly associated with the re-ranking. If the work truly aims to target the ranking field, it should include comparisons against more foundational CTR-prediction methods and other contemporary Large Ranking Model (LRM) approaches like RankMixer: Scaling Up Ranking Models in Industrial Recommenders. If this work focuses on reranking, why not use some datasets and experimental settings more commonly used in the reranking field, such as Avito and Kuaishou?

3. Key engineering details, such as the specific construction of the Auxiliary Ranking Policy Group ($\mathcal{B}$) and the exact large model architecture, are either simplified or omitted. 

4. The scalability experiments primarily focus on demonstrating superiority over the two-stage (G-E) paradigm, which quickly saturates. However, the comparison within the single-stage paradigm only includes simple DNN baselines. The paper fails to demonstrate that other, more sophisticated single-stage solutions (beyond simple DNNs) cannot also achieve similar or superior scaling behavior.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes GoalRank, a novel ranking framework that replaces the complex Multi-Generator-Evaluator paradigm with a single large generator model. The contributions are threefold: theoretically, it proves that a sufficiently large generator can better approximate the optimal ranking policy than any finite M-G-E system, with error decreasing via scaling laws; methodologically, it introduces group-relative optimization, which trains the generator using robust relative comparisons within list groups rather than absolute rewards; empirically, large-scale offline and online experiments demonstrate consistent and significant improvements over state-of-the-art baselines, validating the framework's effectiveness and scalability.

### Strengths
1.  The paper provides a rigorous theoretical proof that a single large generator can surpass any finite M-G-E system, with a clear scaling law. This theory is strongly supported by empirical results, creating a cohesive narrative.
2. The proposed group-relative optimization is an innovative solution for training large rankers. It effectively leverages relative comparisons within groups to create a robust training signal that is resilient to reward model bias.
3. The paper offers thorough validation, from offline benchmarks to large-scale online A/B tests on a major platform. The consistent and significant improvements across both academic and business metrics convincingly demonstrate real-world impact.

### Weaknesses
1.  The training process itself is complex and resource-heavy, The proposed method shifts complexity to the training stage, requiring a costly and intricate pipeline, especially for large-scale industry recommendation systems. 
2. The architectural details and specific implementation of the generator model itself are not sufficiently elaborated, making it difficult to fully assess the proposed method's design choices and reproduce the results.
3. The monolithic generator is inherently less adaptable to new business objectives compared to the more modular M-G-E paradigm, which allows for quicker adjustments.

### Questions
1. If you need the model to optimize for a new goal (like promoting new content instead of maximizing watch time), how would you adapt GoalRank without having to retrain the whole model from scratch?
2. How important is the quality and variety of the helper models used to create the candidate lists? Could a poorly chosen set of helpers limit how good GoalRank can become?
3. Since GoalRank learns from the reward model's relative rankings, is there a risk that it could also learn and even amplify any biases that exist in that reward model?

### Soundness
4

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes GoalRank, a framework advocating for a shift from multi-stage Generator-Evaluator (G-E) ranking paradigms to a single-stage, "Generator-only" (G-only) model. The authors present a theoretical argument that a single large generator can better approximate the optimal ranking policy than any finite G-E system. For training, they introduce "Group-Relative Optimization," which uses a reward model to create a reference policy from a group of candidate lists, serving as a learning target.

### Strengths
1. Empirical Validation: The inclusion of a online A/B test on a major commercial platform is a significant strength, providing real-world evidence of the model's effectiveness in a production environment.   
2. Clarity and Scope: The paper is well-written, clearly articulating its motivation and methodology. The experiments are extensive, covering multiple datasets and demonstrating a clear scaling law, which adds valuable empirical data to the field.

### Weaknesses
1. Experimental Fairness: The experimental comparison between GoalRank and the G-E baselines raises fairness concerns.
- The GoalRank framework relies heavily on a powerful, pre-trained Reward Model to provide its training signal. This reward model is functionally equivalent to an evaluator, albeit used offline.   
- For a fair comparison, the G-E and MG-E baselines should have been equipped with the exact same reward model to serve as their online evaluator. Without this, the observed performance lift of GoalRank may not stem from the superiority of its "G-only" architecture but rather from the fact that it was trained by a more powerful "teacher" (the reward model) than the evaluators used by the baselines.
2. Positioning of the paper: The fundamental goal of both GoalRank and listwise learning to rank (LTR) is the same: to learn a function that can optimally order an entire list of items by considering the items collectively, rather than in isolation. What are the differences between them?
3. Practicality and Online Feasibility: While the paper demonstrates strong online performance, it omits a critical discussion of the training cost. The "Group Construction" step requires generating and evaluating multiple lists for every training sample, which implies a training cost that could be orders of magnitude higher than for the baseline models. This potentially prohibitive cost could severely limit the model's practical applicability in industrial settings that require frequent retraining.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes GoalRank, a single-stage large-model ranking method based on Group-Relative Optimization. The authors demonstrate that a sufficiently large generator model can more closely approximate the optimal ranking strategy compared to the traditional two-stage "generator-evaluator" framework. GoalRank is trained by constructing a reference policy using a reward model, significantly outperforming existing methods on multiple public datasets and industrial-grade online tests, and exhibiting good scaling law and improved real-world business performance.

### Strengths
Theoretically Superior: It has been theoretically proven that a single large-scale generator model can approach the optimal ranking strategy more closely than the traditional multi-generator-evaluator framework, and it exhibits scalability (scaling law).

Simpler Structure: Employing an end-to-end architecture with a single-stage generator eliminates the evaluator stage, avoiding inconsistencies between multiple stages and making model design and training processes more unified.

### Weaknesses
Limited Adaptability: As a single generator model, it lacks the flexibility of an independent evaluator. When business objectives or optimization metrics change frequently, model adjustment costs are high, making it less adaptable than a two-stage architecture.

Strong Dependence on Reward Model: The training process relies on a reward model trained based on user feedback. If the reward model is biased or noisy, it may lead to inaccurate reference strategies, affecting overall ranking quality.

High Training and Resource Costs: GoalRank's core advantage comes from large-scale models and group optimization, but this also means higher computational resources and training costs, making it less friendly to small- to medium-scale application scenarios.

Lack of Strong Baseline Comparisons: The lack of comparisons with baselines for solving large candidate ranking, such as Onerec and Tiger, makes the paper's experimental results less convincing.

The paper's writing is confusing and difficult to understand.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3