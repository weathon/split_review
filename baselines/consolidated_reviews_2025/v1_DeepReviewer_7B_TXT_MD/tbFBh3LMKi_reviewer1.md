### Summary

The paper introduces a novel method Uni-O4, which unifies offline and online reinforcement learning (RL) within a single framework. Uni-O4 leverages an ensemble of policies to address the mismatch between estimated behavior policies and the actual dataset, enabling multi-step policy improvement. The method also incorporates an offline policy evaluation (OPE) approach called AM-Q to avoid the need for online evaluation. The authors claim that Uni-O4 achieves competitive performance in both offline and offline-to-online fine-tuning tasks, outperforming several state-of-the-art baselines in various simulated benchmarks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses the important problem of bridging the gap between offline and online RL, which is crucial for real-world applications of RL.
- The use of an ensemble of policies to handle multi-modality and the introduction of AM-Q for offline OPE are interesting technical contributions.
- The paper includes experiments on both simulated and real-world robot tasks, demonstrating the practical applicability of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear and concise problem formulation, making it difficult to understand the specific challenges being addressed. A formal definition of the offline-to-online RL problem and the goals of the proposed method would greatly improve clarity.
- The paper does not provide a strong justification for why the proposed method should work. The connection between the ensemble policy and the offline-to-online setting is not well-explained, and the theoretical motivation for using AM-Q is weak.
- The paper does not adequately address the potential limitations of the proposed method. For example, how does the method handle environments with sparse rewards or high-dimensional state spaces? What are the computational costs associated with training the ensemble of policies?
- The experimental evaluation is not comprehensive enough. The paper should include comparisons with a wider range of state-of-the-art offline-to-online RL methods, and the results should be analyzed in more detail. For example, the paper should investigate the sensitivity of the method to hyperparameter settings and the quality of the offline dataset.
- The paper does not provide sufficient details on the implementation of the proposed method. For example, the paper should specify the architecture of the policy and value networks, the optimization algorithm used, and the hyperparameter settings.

### Suggestions

The paper would benefit significantly from a more rigorous problem formulation. The authors should clearly define the offline-to-online RL problem they are addressing, including the assumptions made about the offline dataset and the online environment. This should include a formal definition of the state and action spaces, the reward function, and the transition dynamics. Furthermore, the authors should specify the objective of the proposed method, such as minimizing regret or maximizing cumulative reward, and how this objective relates to the offline-to-online setting. A clear problem formulation would provide a solid foundation for the rest of the paper and make it easier for readers to understand the contributions and limitations of the proposed method. The authors should also consider including a diagram or a table that summarizes the key notations and definitions used in the paper.

To strengthen the paper's technical contributions, the authors need to provide a more compelling justification for their method. The connection between the ensemble policy and the offline-to-online setting is not sufficiently explained. The authors should provide a theoretical analysis of why the ensemble policy is expected to perform well in this setting, and how it addresses the challenges of mismatch between the estimated behavior policy and the actual dataset. The theoretical motivation for using AM-Q should also be strengthened. The authors should explain why AM-Q is a suitable choice for offline policy evaluation, and how it avoids the need for online evaluation. A more detailed explanation of the theoretical underpinnings of the method would make the paper more convincing and impactful. The authors should also consider providing some intuition behind the design choices, and how they relate to the problem being addressed.

Finally, the experimental evaluation needs to be more comprehensive and rigorous. The authors should include comparisons with a wider range of state-of-the-art offline-to-online RL methods, and the results should be analyzed in more detail. This should include a comparison with methods that use different approaches, such as model-based methods or methods that do not use an ensemble of policies. The authors should also investigate the sensitivity of the method to hyperparameter settings and the quality of the offline dataset. For example, how does the performance of the method vary with different sizes of the offline dataset, or with different hyperparameter settings? The authors should also provide more details on the implementation of the proposed method, such as the architecture of the policy and value networks, the optimization algorithm used, and the hyperparameter settings. This would make it easier for other researchers to reproduce the results and build upon the proposed method.

### Questions

- How does the proposed method handle environments with sparse rewards or high-dimensional state spaces?
- What are the computational costs associated with training the ensemble of policies?
- How does the method ensure that the ensemble policy is diverse enough to cover the state-action space effectively?
- How does the method handle situations where the offline dataset is biased or incomplete?

### Rating

3

### Confidence

4

**********
