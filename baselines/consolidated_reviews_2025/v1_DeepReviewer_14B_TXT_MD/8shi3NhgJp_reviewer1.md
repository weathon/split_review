### Summary

The paper proposes a Bayesian method for continual learning under specific trade-offs (CLuST) that allows for zero-shot model generation. The method maintains a knowledge base of model parameter distributions and generates new models via convex combinations of these distributions based on user preferences. The paper presents experiments on image classification and NLP benchmarks, showing improved performance and constant training overhead.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method formulates a new problem of CL under specific trade-offs (CLuST), which asks for efficiency upon a large number of preferences.

2. The proposed method, IBCL, is a Bayesian CL algorithm to solve the CLuST problem. IBCL updates the knowledge base in the form of a convex set of distributions with finitely many extreme elements (the elements that cannot be written as convex combinations of one another), called a finitely generated credal set (FGCS). IBCL has constant training overhead per task (to update the FGCS), independent of the number of preferences.

### Weaknesses

#### Some Related Works


#### comment

1. The problem setup seems too restricted. The paper only considers domain-incremental learning for classification models. However, in continual learning, task-incremental learning and class-incremental learning are more important. The focus on domain-incremental learning limits the applicability of the proposed method to scenarios where the task distribution changes but the output space remains the same. This is a significant limitation, as many real-world continual learning problems involve the introduction of new classes or tasks over time, which is not addressed by the current formulation.

2. The assumption of task similarity is too strong. In the Assumption 1, the paper assumes that all tasks are similar to each other. However, in real-world scenarios, tasks can be very different. This assumption is not justified and may not hold in many practical applications. The paper does not provide any analysis of how the performance of the method degrades when the tasks are dissimilar, which is a critical aspect to consider for the robustness of the approach. The use of a Wasserstein distance threshold to control the addition of new distributions to the knowledge base does not fully address the issue of task dissimilarity, as the initial assumption still restricts the scope of the method.

3. The paper does not provide any theoretical analysis of the proposed method. The paper only provides empirical results. However, theoretical analysis is important to understand the properties of the method. The lack of theoretical guarantees makes it difficult to assess the convergence, stability, and generalization capabilities of the proposed method. Without theoretical analysis, it is hard to understand the conditions under which the method is expected to perform well and when it might fail.

4. The paper does not compare the proposed method with other state-of-the-art continual learning methods. The paper only compares with some baselines that are not state-of-the-art. This makes it difficult to assess the performance of the proposed method compared to existing approaches. The baselines used are not representative of the current state-of-the-art in continual learning, particularly in the areas of task-incremental and class-incremental learning, which makes the empirical evaluation less convincing.

### Suggestions

The paper should broaden its scope to include task-incremental and class-incremental learning scenarios, which are more relevant to many real-world applications of continual learning. This would involve modifying the problem formulation to handle the introduction of new tasks or classes over time. The current approach, which focuses solely on domain-incremental learning, is too restrictive and limits the practical applicability of the proposed method. The authors could consider using techniques such as dynamic expansion of the output layer or task-specific modules to handle the introduction of new classes or tasks. Furthermore, the evaluation should include benchmarks that are commonly used in task-incremental and class-incremental learning to provide a more comprehensive assessment of the method's performance.

The assumption of task similarity needs to be relaxed or justified with a more thorough analysis. The paper should explore how the method performs when tasks are dissimilar and provide a clear explanation of the limitations of the approach under such conditions. The authors could consider using a more robust measure of task similarity or explore techniques for adapting the method to handle dissimilar tasks. For example, they could investigate the use of meta-learning techniques to learn how to adapt to new tasks, even if they are dissimilar to previous ones. Additionally, the paper should provide a more detailed analysis of the impact of the Wasserstein distance threshold on the performance of the method, as this parameter plays a crucial role in controlling the addition of new distributions to the knowledge base.

The paper should include a theoretical analysis of the proposed method to provide a better understanding of its properties. This analysis should include proofs of convergence, stability, and generalization guarantees. The authors could consider using tools from Bayesian non-parametrics or statistical learning theory to derive theoretical results. Furthermore, the paper should compare the proposed method with state-of-the-art continual learning methods, including those based on replay, regularization, and parameter isolation. This would provide a more comprehensive assessment of the method's performance and allow for a more meaningful comparison with existing approaches. The baselines used should be representative of the current state-of-the-art in continual learning, and the evaluation should include a variety of benchmarks to provide a more robust assessment of the method's performance.

### Questions

Please see the weaknesses.

### Rating

3

### Confidence

5

**********
