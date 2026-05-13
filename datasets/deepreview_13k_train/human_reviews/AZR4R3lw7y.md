# Boosting Multiple Views for pretrained-based Continual Learning

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Recent research has shown that Random Projection (RP) can effectively improve the performance of pre-trained models in Continual learning (CL). The authors hypothesized that using RP to map features onto a higher-dimensional space can make them more linearly separable. In this work, we theoretically analyze the role of RP and present its benefits for improving the model’s generalization ability
in each task and facilitating CL overall. Additionally, we take this result to the next level by proposing a Multi-View Random Projection scheme for a stronger ensemble classifier. In particular, we train a set of linear experts, among which diversity is encouraged based on the principle of AdaBoost, which was initially very challenging to apply to CL. Moreover, we employ a task-based adaptive backbone
with distinct prompts dedicated to each task for better representation learning. To properly select these task-specific components and mitigate potential feature shifts caused by misprediction, we introduce a simple yet effective technique called the self-improvement process. Experimentally, our method consistently outperforms state-of-the-art baselines across a wide range of datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers the random projection (RP) strategy for pre-trained models in CL. Motivated by the benefits of RP in high-dimensional space, a multi-view strategy for an efficient classifier is further proposed, in which the principle of Adaboost is adapted to 
overcome inherent obstacles and applied for the first time in CL. In addition, a self-improvement process technique, although simple, also shows significant effectiveness in selecting proper taskspecific prompts. The experimental results demonstrate a positive impact of the proposed method in improving model quality while only applying to linear classifiers.

### Strengths
(1)The proposed method BoostCL performs better than existing CL baselines, including Hide-prompt and ranpac.
(2)This work addressed the challenge when applied AdaBoost directly to CL.
(3)A self-improvement process, a simple but effective strategy is designed to help select prompts more accurately when inference.

### Weaknesses
As shown in Table 1, the proposed method takes no advantage in anti-forgetting, FFM metric.

### Questions
Does some ablation study be conducted on the proposed modules, Prompt selection process and Self-improvement process?

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
4

### Summary
This paper presents BoostCL, a method for pretrained-based continual learning that leverages multiple views and random projection (RP) to enhance performance. The authors theoretically analyze the benefits of RP in higher-dimensional spaces and demonstrate its effectiveness through experimental results.

### Strengths
1.	The paper provides a novel theoretical analysis of the benefits of random projection in higher-dimensional spaces for continual learning.
2.	The authors conduct a comprehensive set of experiments to evaluate the performance of their proposed method, BoostCL, across various tasks and datasets.
3.	The paper demonstrates the practicality of the proposed method by applying it to real-world continual learning scenarios.

### Weaknesses
1. The paper mentions the motivation behind using random projection, but it lacks a comprehensive discussion on why this approach is superior to other potential methods for feature transformation. Specifically, the paper does not explore alternatives such as learned transformations or non-linear projections, which could potentially offer better performance or more efficient representations. A more thorough analysis of the trade-offs between different feature transformation techniques is needed.
2. While the paper proposes a novel method for continual learning, it would be helpful to see a more in-depth comparison with other recent methods in the literature. Specifically, how does BoostCL differ from and improve upon existing approaches? The paper should include a detailed comparison with state-of-the-art continual learning methods, highlighting the specific advantages and disadvantages of BoostCL in different scenarios. It is not clear how BoostCL compares to methods that use replay buffers or regularization techniques.
3. The technical details of the proposed method are somewhat challenging to follow. The paper could benefit from a more clear and concise explanation of the algorithm and its components. For example, the interaction between the multiple views and the random projection is not clearly explained. The paper should provide a step-by-step breakdown of the algorithm, including the mathematical formulations and the implementation details.
4. Discussing the scalability of the proposed method to larger datasets or more complex models would be relevant. The paper does not address the computational cost of the random projection, especially when dealing with high-dimensional data. It is important to analyze the memory and time requirements of the proposed method and compare them with other continual learning methods. Furthermore, the paper should discuss the performance of the proposed method when applied to larger models with more parameters.
5. The author needs to further analyze the consumption of the proposed method compared to other methods in terms of computational resources and training time. A detailed analysis of the computational complexity of the proposed method is missing. The paper should provide a comparison of the training time and memory usage of BoostCL with other state-of-the-art methods. This analysis should include the time required for each step of the algorithm, such as the random projection and the training of the classification head.
6. The paper could benefit from a more organized and focused presentation of the material. The introduction could be more clearly tailored to motivate the problem and the proposed solution. Additionally, the paper includes several appendices that contain detailed proofs and additional experimental results. While these appendices provide valuable information, they could be more effectively integrated into the main text to enhance the clarity and readability of the paper.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This manuscript introduces "BoostCL", a novel approach to improve continual learning based on pre-trained models. The manuscript provides theoretical analysis to show that feature separability and model generalization ability benefit from random projection. Then a multi-view random projection is proposed to adapt AdaBoost for CL. A self-improvement process is also proposed for appropriately selecting prompts for each task sample. Empirical validation on multiple CL benchmarks is then conducted.

### Strengths
1. The manuscript provides theoretical analysis of Random Projection, demonstrating how RP improves feature separability in high-dimensional space. 
2. The manuscript is clear and well organized. The formulas are presented in an unambiguous manner.

### Weaknesses
1. Although RP and multi-view strategies are theoretically shown to improve feature separability, there is limited discussion on the theoretical upper bound of generalization error.
2. The manuscript does not provide theoretical guidance on choosing the optimal projection dimension in RP, which can greatly impact model performance for different tasks.
3. The proposed self-improvement process for prompt selection could increase the model’s inference complexity, but this potential trade-off is not fully analyzed, especially in scenarios with many tasks.
4. Minor spelling errors, like “sammple” in line 250.
5. More experiment regarding hyper-parameters like number of views, projection dimensions, and threshold settings for the voting mechanism should be conducted.

### Questions
1. How to effectively choose the best projection dimension to make appropriate trade-off between performance and computational overhead.
2. How much gpu resource does the proposed method need, will the gpu memory usage increase rapidly by increasing projection dimension.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides some theoretical analysis on Random Projection (RP) which project features into a higher-dimensional space to improve their linear separability. Furthermore, this paper proposes a Multi-View Random Projection scheme to create a robust ensemble classifier motivated by AdaBoost. Then the proposed method is applied to prompt-based CL methods for a better performance. Experimental results demonstrate its efficacy in various continual learning settings.

### Strengths
1.	This paper provides theoretical insights into Random Projection (RP), reinforcing its foundation in an intuitive manner.

2.	The motivation for the proposed Multi-View Random Projection is clear and well-justified, demonstrating its potential to enhance performance.

3.	The paper is well-organized and easy to understand, addressing most of my queries within the main text or the appendix.

### Weaknesses
 **Major**

1.	The necessity of the huge views should be clarified. As mentioned in the paper, the subsequent atomic views aim to capture the complement knowledge of previous views. However, the final classifier only leverages a part of these views rather than all of them, which may omit some complement knowledge. It is not clear why a subset of views is sufficient, and how the selection of this subset impacts the overall performance. The paper should provide a more rigorous justification for this selective approach, perhaps by analyzing the information content of each view and its contribution to the final classification.

2.	The theoretical results are interesting, but the method is heuristic. For example, the design of the voting strategy and the self-improvement are quite complex. It seems that a lot of tricks are introduced directly to improve performance. The paper lacks a principled approach to these design choices. Specifically, the voting strategy, which combines predictions from different views, seems to be an ad-hoc approach. A more systematic way to combine these predictions, perhaps based on a theoretical analysis of their individual strengths and weaknesses, would be beneficial. Similarly, the self-improvement process lacks a clear theoretical basis, and its effectiveness is not well-explained.

3.	The design of the self-improvement process is not intuitive, which may accumulate errors in multiple-step prediction. Specifically, if an incorrect prompt is chosen in the first step, the model may become biased towards predicting the class associated with that wrong prompt, potentially leading to accumulated errors and hindering improvements in prompt prediction accuracy. The paper does not adequately address the potential for error propagation in this iterative process. A more robust approach, perhaps incorporating some form of error correction or regularization, would be necessary to mitigate this issue.

4.	The experiments do not include comparisons with simpler ensemble methods, such as randomly sampling views or using all views for the ensemble. Such comparisons can provide more intuitive insights to demonstrate the effectiveness of the proposed method. Without these comparisons, it is difficult to assess whether the proposed method is truly superior to simpler alternatives. The paper should include ablation studies to analyze the contribution of each component of the proposed method, including the view selection strategy and the self-improvement process.

**Minor**

1.	There are too many notations which may limit the fluency and readability. For example, in line 177, there is no description for the notation $\gamma (s,g,\mathbb{R}^d)$ and no explanation for the symbolic $g$. So please simplify the notations as much as possible.
2.	Typo in Corollary 4.4 (line 250), “sammple” should be “sample”.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
