# Theory on Mixture-of-Experts in Continual Learning

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Continual learning (CL) has garnered significant attention because of its ability to adapt to new tasks that arrive over time. Catastrophic forgetting (of old tasks) has been identified as a major issue in CL, as the model adapts to new tasks.
The Mixture-of-Experts (MoE) model has recently been shown to effectively mitigate catastrophic forgetting in CL, by employing a gating network to sparsify and distribute diverse tasks among multiple experts.
However, there is a lack of theoretical analysis of MoE and its impact on the learning performance in CL. 
This paper provides the first theoretical results to characterize the impact of MoE in CL via the lens of overparameterized linear regression tasks. 
We establish the benefit of MoE over a single expert by proving that the MoE model can diversify its experts to specialize in different tasks, while its router learns to select the right expert for each task and balance the loads across all experts. Our study further suggests an intriguing fact that the MoE in CL needs to terminate the update of the gating network after sufficient training rounds to attain system convergence, which is not needed in the existing MoE studies that do not consider the continual task arrival. 
Furthermore, we provide explicit expressions for the expected forgetting and overall generalization error to characterize the benefit of MoE in the learning performance in CL. Interestingly, adding more experts requires additional rounds before convergence, which may not enhance the learning performance. Finally, we conduct experiments on both synthetic and real datasets to extend these insights from linear models to deep neural networks (DNNs), which also shed light on the practical algorithm design for MoE in CL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a theoretical study of Mixture-of-Experts (MoE) models for Continual Learning (CL). Specifically, it examines the CL of linear regression tasks in an overparameterized regime. The benefit of this regime is that each task has multiple possible solutions, increasing the likelihood of expert specialization and transfer.

This paper implements a one-layer MoE architecture with the following design choices:

- **Experts**: Each expert is implemented as a linear model.
- **Router**: A top-1 router is implemented as a linear model.
- **Router Training**: The router is trained using gradient descent.
- **Expert Parameters**: Expert parameters are found through a closed-form solution
- **Training regime**: routing is performed at a per-task level, at each new trainign iteration a new task is sampled from a limited pool of tasks. 

Authors propose two key design choices to facilitate learning in their MoE:
	
- Training loss: in addition to the standard load balancing loss (eq. 7), they propose to use a **locality loss** (is a novel contribution afaik), that facilitates routing of the similar tasks to the same experts
- Early termination: intuitively, once an expert has specialized sufficiently (expected to be the case after T_1 updates), further updates of the routing parameters can result in instabilities. This is achieved by terminating training of the router if the current expert's routing "dominates sufficiently" the other experts' routing.

Authors address the following setting:
- at each update step t, a feature matrix X is randomly sampled following the data generating process described in Definition 1
- among the s_t examples in the feature matrix, there is one example that contains the feature signal
- in the addressed setting, identical tasks can reoccur, as tasks are sampled independently in each update step

Authors derive the following properties of the MoE with previously mentioned design choices:
- the router routes experts primarily based on feature signal, and all experts can be clustered into experts sets, with specialized experts in each expert set
- therefore, under the proposed algorithm (due to the locality loss and termination criteria), experts will likely specialize on certain task clusters after sufficient training round T_1 minimizing the effect of forgetting
- if no termination criteria is applied, proposition 2 states that the specialization will break at round t_2 (the gap between any two experts is predicted to be the same)
- if early termination is applied, then experts within the same expert set are chosen uniformly after T2 updates

The authors derive upper bounds on forgetting and generalization error for the MoE, showcasing that **both are reduced compared to a monolithic single-expert model**. When there are more tasks than experts, forgetting is bounded due to the router’s tendency to route similar tasks to the same experts.

Overall, the intuition that MoE models, with correct routing and module specialization, can address the challenges of CL is natural and compelling. This paper effectively demonstrates how this intuition can be implemented and validated in a controlled, toy setting. The findings can offer a useful starting point for scaling these ideas to settings more relevant for practical AI applications, a very relevant work in this context is [2].

[2] Rypeść, Grzegorz, et al. "Divide and not forget: Ensemble of selectively trained experts in Continual Learning." arXiv preprint arXiv:2401.10191 (2024).

### Strengths
**Originality**: 
- the idea that forgetting in MoE can be mitigated solely through specialized experts and correct routing is not entirely new, e.g. see [1]
- this paper is original in its theoretical contribution (to the best of my knowledge), providing proofs and bounds on Cl metrics with MoEs
- the proposed locality loss and load balancing loss provide clear mechanisms for task clustering and specialization (even though load balancing loss is not a contribution of this work)

**Quality**: 
I think the quality of this work is decent, due to the rigorous theoretical work and relevant experiments. Even though the focus of the work is mainly on the theoretical side, further validation on more complex datasets would be interesting and benefit the credibility of the paper's contributions. 

**Clarity**: while the theoretical analysis appears to be rigorous and well presented, I think the presentation would benefit a lot from incorporating more **intuitive explanations**. E.g. authors could explicitly state the idea that forgetting may be prevented solely through correct routing. Also the MNIST experiment's design is somewhat hard to follow.

**Significance**:
Despite the small scale of the experiments, I think this paper opers some interesting directions for future research, mainly among the lines of scaling these ideas to larger systems.

Overall, I appreciate how this paper demonstrates how under proper specialization and routing CL can be addressed with modular solutions like MoEs.

[1] Ostapenko, Oleksiy, et al. "From IID to the Independent Mechanisms assumption in continual learning." AAAI Bridge Program on Continual Causality. PMLR, 2023.

### Weaknesses
 - the scale of the experiments is small, while one has to uknowledge that the contributions are mainly theoretical
- I would appreciate more intuitive lingo and explanations
- the current implementation is essentially on the one extreme of the parameter sharing trade-off where no transfer happens between tasks?
- it is not exactly clear how these ideas can be extended to large scale MoE with multiple expert layers and per-token routing, where correct routing as well as expert specialization is not guaranteed

### Questions
-  is expert specialization necessary for CL with MoEs? 
- are modern-day large-scale AI systems operating in an overparameterized regime?
- for load balancing loss, why not use entropy maximization? What are the benefits of the proposed load balancing loss compared to entropy maximization?
- is cross-expert and cross-task transfer possible in the proposed system design?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Theory on Mixture-of-Experts in Continual Learning" analyzes the Mixture-of-Experts (MoE) model's effectiveness in addressing catastrophic forgetting in continual learning (CL). It establishes that MoE can enhance learning by diversifying expert specialization through a gating network, which routes tasks efficiently. The study provides theoretical insights into expected forgetting and generalization error, demonstrating that MoE outperforms single-expert models, especially with diverse data distributions. However, it notes that adding more experts requires additional training rounds before achieving convergence. Empirical results support the theoretical claims, extending the findings to deep neural networks (DNNs) for practical algorithms

### Strengths
1) Theoretical Foundations: The paper provides a comprehensive theoretical analysis of MoE in the context of continual learning, establishing clear benefits over single-expert models through explicit expressions for expected forgetting and generalization error.

2) Load Balancing: The model ensures balanced utilization of experts, which can lead to improved generalization performance as it reduces the risk of overloading any single expert with too many tasks.

3) Empirical Validation: Experiments conducted on both synthetic and real datasets support the theoretical findings, demonstrating that MoE can effectively improve learning performance across diverse scenarios. It is interesting to note that even with a higher number of experts than tasks, the model might not perform well.

### Weaknesses
1) Validity of Proposition (4): The model gap term ∑n≠n′∥wn−wn′∥2\sum_{n \neq n'} \|w_n - w_{n'}\|^2∑n=n′​∥wn​−wn′​∥2 only considers the Euclidean distance between weights. This may not fully capture the complex relationships between tasks. In practice, tasks could overlap in non-trivial ways (e.g., in feature space or output space), and simple weight differences do not reflect true "task divergence" accurately. Specifically, the Euclidean distance treats all weight differences equally, failing to account for the varying importance of different weights in the network. For instance, changes in weights associated with critical features might have a larger impact on task performance than changes in weights associated with less relevant features. This limitation could lead to an inaccurate assessment of the true model gap and its impact on forgetting.

2) Limited Experiments: Though the main contribution is to present the theoretical analysis of forgetting and generalization error for MoE in CL, the main objective of the model is to reduce catastrophic forgetting. Without presenting enough empirical evaluation in terms of accuracy in continual learning settings for benchmark datasets like CIFAR10/100, ImageNet is not enough. I would encourage the authors to extend the simulation to the more complex dataset. For example, SEED [1] uses a mixture of expert networks and selects a single expert to finetune downstream tasks. If the authors could provide details of this work by forgetting a generalization error it would provide better judgment of where the current state-of-the-art MoE methods for CL stands in terms of forgetting and generalization error and strengthen the contribution of the work. The lack of experiments on standard continual learning benchmarks makes it difficult to assess the practical applicability of the theoretical findings. The experiments should also include a comparison with other state-of-the-art continual learning methods, not just a single-expert baseline, to provide a more comprehensive evaluation of the proposed MoE approach.

### Questions
1) Line 56-57 “One learning task arrives in each round and its dataset is generated with ground truth randomly drawn from a shared pool encompassing N unknown linear model”. What is the intuition behind generating the ground truth from the linear model?

2) It might make sense if the number of experts is less than the number of tasks But in Line Line 69 if M > N implies the number of experts more than the number of tasks. This is not continual learning if you are training task-specific experts. Furthermore, in Section 4, you have done the main study with more experts than tasks (Line 296).

3) In Figure 2, on which datasets the experiment is performed?

4) For MNIST which DNN model is used? As from the setup number of task N = 3, how did the 10 classes were split?


## After Reading Comments

I raised my score to 6 as an experiment on MNIST and CIFAR10 is not enough.

Again, thank you for your contributions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work studies the theoretical understanding of mixture-of-experts (MoEs) module in continual learning. To examine the role of MoEs, the authors conduct experiments on overparameterized linear regression tasks. Theoretically, this work identifies the importance of the gating network update’s termination and analyzes the catastrophic forgetting and generalization.

### Strengths
This work is written clearly and well structured. Overall, the theoretical analysis over MoEs is necessary in developing MoE-based large models, and this work discusses some insights into the catastrophic forgetting and generalization. The experiments include the overparameterized linear regression and MNIST cases.

### Weaknesses
(1) The scope of this work seems a bit wide according to the title. I suggest to use terms like “theoretical understanding” to modify.

(2) The theoretical analysis is mainly on overparameterized linear regression cases, which might be a limitation in this work as nonlinear deep neural network cases can be more practical.

(3) There are some related work on MoE theories, continual learning with MoEs or MoEs for adaptation in the field that require discussions [1-4].

(4) In Line 76-78, it sates the MoE enhances performance over the single expert case, which seems trivial. Is the condition, such as with the same model complexity, missing in the statement?

(5) In Line221-224, it seems the update of model parameterizes use the inversion matrix, which brings more computational overhead over gradient-based methods.

(6) In Line 293-294, it seems the early termination achieves stable convergence, but the motivation is also related to overfitting for alleviating imbalanced loads. So does the early termination improve balanced loads?

(7) In Line 532, “the first theoretical analysis of MoE” is overstated considering the existing work [1]. And I am also wondering how the developed strategy works in more complicated experiments.

### Questions
(1) In Line 76-78, it sates the MoE enhances performance over the single expert case, which seems trivial. Is the condition, such as with the same model complexity, missing in the statement?

(2) In Line221-224, it seems the update of model parameterizes use the inversion matrix, which brings more computational overhead over gradient-based methods.

(3) In Line 293-294, it seems the early termination achieves stable convergence, but the motivation is also related to overfitting for alleviating imbalanced loads. So does the early termination improve balanced loads?

(4) In Line 532, “the first theoretical analysis of MoE” is overstated considering the existing work [1]. And I am also wondering how the developed strategy works in more complicated experiments.

### Soundness
3

### Presentation
3

### Contribution
3
