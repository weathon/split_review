# Commute Your Domains: Trajectory Optimality Criterion for Multi-Domain Learning

- Decision: Reject
- Scores: 5, 5, 3, 6, 3

## Abstract
In multi-domain learning, a single model is trained on diverse data domains to leverage shared knowledge and improve generalization. The order in which the data from these domains is used for training can significantly affect the model's performance on each domain. However, this dependence is under-studied. In this paper, we investigate the influence of training order (or data mixing) in multi-domain learning using the concept of Lie bracket of gradient vector fields. By analyzing the infinitesimal effects of changing the training order, we identify regions in the parameter space where altering the order between two training domains can benefit the target loss. We validate the predictions of our theoretical framework on the influence of training order (or data mixing) both on a toy example and  bilingual LLM pre-training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies the effect of domain orders in the multi-domain learning problems. With the lens of vector field, it shows that the order of domain influences training dynamics. Furthermore, it proposes scheduling for weights to sample batch of each domain, which can benefit the target loss. Finally, it validates its theory with numerical experiments.

### Strengths
Disclaimer: I do not have proper knowledge to evaluate its theoretical analysis. It is hard to judge the significance of the theories the paper has provided.

- Provide theoretical analysis about effect of domain order. 

- Propose scheduling for weight to sample domain batches grounded on the theory.

- Validate the theoretical analysis with the numerical experiments.

### Weaknesses
- Hard to tell actual benefits of the proposed weight scheduling. Based on Figure 3, the constant domain weight schedule seems to work well. Better to elaborate the practical advantage of the proposed method.

- I think there are many relevant works. The final goal is to learn to minimize the total domain loss without interfering other domains, which is the goal of multi-task learning. It would be better to compare the proposed method against some well-known multi-task learning methods (such as [1,2,3,4]) and show its benefit compared to them.


[1] Navon, Aviv, et al. "Multi-Task Learning as a Bargaining Game." International Conference on Machine Learning. PMLR, 2022.

[2] Lee, Seanie, et al. "Sequential Reptile: Inter-Task Gradient Alignment for Multilingual Learning." International Conference on Learning Representations. 2022.

[3] Yu, Tianhe, et al. "Gradient surgery for multi-task learning." Advances in Neural Information Processing Systems 33 (2020): 5824-5836.

[4] Wang, Zirui, et al. "Gradient Vaccine: Investigating and Improving Multi-task Optimization in Massively Multilingual Models." International Conference on Learning Representations. 2021.

### Questions
- What is the benefit of using the proposed weight scheduling method? Does it converge faster or converge to better optima?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studied how the order of training on different data domains affects model performance in multi-domain setting. The authors develop a theoretical framework based on Lie bracket analysis of gradient vector fields to predict and understand the effects of changing domain training order. They introduce a trajectory optimality criterion that helps determine when to switch between domains during training. The framework is validated through experiments on both a toy quadratic optimization problem and a bilingual language model pre-training task.

### Strengths
1. The paper provides a theoretical foundation for analyzing domain ordering effects in multi-domain learning, an important but under-studied problem. 
2. The use of Lie bracket analysis is interesting and novel. Through the analyze of the commutable property of the gradient flow, the authors show the effect of different ordering. 
3. The theoretical framework successfully predicts directional changes in loss values when domain ordering is modified, as demonstrated in both synthetic and real-world experiments. 
4. The authors also provide clear geometric intuitions for their results through visualizations.

### Weaknesses
1. While the theoretical framework can predict the effects of changing domain order, it doesn't provide an explicit algorithm for finding optimal domain schedules. 

2. the current theory doesn't fully account for the effects of different optimizers (like Adam) or the stochastic nature of training, which are crucial in deep learning. The experiments, while supportive of the theory, show some discrepancies between predicted and actual values, particularly in the LLM pre-training case. 

3. The paper's analysis is limited to two-domain scenarios, and it's not clear how well the approach scales to settings with many domains. 

4. The practical applicability of the method may be limited by the computational cost of computing since the involving of the Hessian-vector products.

5. Presentation issue. Please use the correct citation command, for example \citep.

6. What are the key practical message that machine learning practitioner can use from the work?

7. A general question that the author could consider.  How does curriculum learning, where the ordering of training examples is crucial, related to the work?

### Questions
See the weakness section for details.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the problem of training orders in multi-domain learning. The authors introduce a theoretical framework based on the concept of Lie brackets of gradient vector fields to predict how changes in training order can influence model performance across domains. The theoretical insight is validated empirically through both a toy example and bilingual large language model (LLM) pre-training.

### Strengths
1. The theoretical framework is well formulated, and the illustrations are intuitive.

2. The writing is clear and structured.

### Weaknesses
1. The authors do not provide a clear explanation about how the studied problem is different from the rich literature of multi-task learning (MTL). In MTL, there exists many methods to balance the training of data from different mixtures, and many of them can be provably applied to reach the desired optimum based on loss combinations. It is unclear how results in the paper are different from those.

2. The utility of the theoretical results is limited. The theoretical part essentially provides a way to predict the performance given weight schedule. However, this does not provide a very accurate prediction due to the stochastic nature of optimization, and the computational cost is non-negligible.

### Questions
I wonder if the authors could provide some comments about the connection with the literature of gradual domain adaptation (GDA) [1,2,3]? The idea is quite relevant, as GDA studies the problem of gradual distribution shift from the source to target domains. There exists algorithms [2,3] that interpolate between source and target domains to construct a path along which the model iteratively improves. This is similar to the gradually changing mixture weights mentioned in the paper.

[1] Understanding Self-Training for Gradual Domain Adaptation. Kumar et al. 2020.
[2] Gradual Domain Adaptation: Theory and Algorithms. He et al. 2023.
[3] Gradual Domain Adaptation via Gradient Flow. Zhuang et al. 2024.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper investigates the effects of training order on model performance in multi-domain learning contexts, where a model learns from diverse data sources. Recognizing that the sequence of domain exposure can significantly impact outcomes, the authors propose a theoretical framework using the Lie bracket of gradient vector fields. This framework identifies areas in parameter space where modifying the training order may improve target loss. The authors demonstrate the theoretical framework's predictions with both a controlled "toy" example and a bilingual large language model (LLM) pre-training task, providing insights into optimizing training order for enhanced performance across domains.

### Strengths
1. The paper introduces an original theoretical approach to training order optimization in multi-domain learning, leveraging Lie bracket analysis of gradient vector fields.

2. Methodologically robust, the paper validates its theoretical insights through both synthetic and realistic experiments, particularly a bilingual LLM pre-training task.

3. The work is significant for practical and theoretical advancements.

### Weaknesses
1. The paper assumes gradient and Hessian computations that may not account for stochasticity and optimizers like Adam, which is commonly used in deep learning and could affect convergence behavior. This might lead to inaccuracies in predicting training outcomes.

2. While the theoretical framework using Lie brackets provides insight into training order in multi-domain learning, it lacks direct, actionable guidance for practitioners. The method suggests a direction for optimizing the training sequence but doesn’t provide a concrete algorithm for determining an optimal sequence.

### Questions
1. Do you have suggestions for efficient approximation methods for Hessian calculations, or could you discuss any empirical limits encountered in terms of model size and domain count?

2. Could you address the potential discrepancy introduced by stochastic gradients and adaptive optimizers in practical applications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The order of adaptation domains used for training is important. The paper considers a scenario where the amount of data is fixed and the examples from different domains can be adjusted. They study the training order using a theoretical framework of a toy example and bilingual LLM pre-training. Overall, there are some limitations to the current version, I would like to raise the score if these limitations can be solved in the feedback.

### Strengths
1. The paper investigates an interesting idea that is important for multi-domain learning. 
2. The paper proposes a theoretical framework to analyze the influence of the training order. 
3. The paper is written clearly and well-organized.

### Weaknesses
Just as the authors stated in the limitation, there are still some weaknesses:

1. There are no concrete algorithms to solve the problems proposed in the paper. There are only some insights from the paper. 

2. The experimental results are not strong enough. I am worried the conclusions can be generalized to LLM models, especially for other multi-domain scenarios.

### Questions
1. The introduction is a little short. This makes the motivations of the paper not strong enough. refer to https://arxiv.org/pdf/2104.08786

2. Although the order is important for multi-domain setup, there is still a "catastrophic forgetting" issue. In this case, I am not sure if it is necessary to target "order" analysis in the multi-domain. Could you explain a little bit if the theoretical analysis in the paper is useful for catastrophic forgetting issues?  

3. There are only bilingual experimental results in the paper, could you show some results based on 5 more languages or multi-tasks results? refer to the paper:https://arxiv.org/abs/2405.11157. 

4. GPT2 model is a "smaller" model, I would like to see some experimental results based on LLama-7b or 13b.

### Soundness
2

### Presentation
3

### Contribution
2
