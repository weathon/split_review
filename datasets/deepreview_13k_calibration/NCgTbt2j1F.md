# Learning to Help in Multi-Class Settings

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Deploying complex machine learning models on resource-constrained devices is challenging due to limited computational power, memory, and model retrainability. To address these limitations, a hybrid system can be established by augmenting the local model with a server-side model, where samples are selectively deferred by a *rejector* and then sent to the server for processing. The hybrid system enables efficient use of computational resources while minimizing the overhead associated with server usage. The recently proposed Learning to Help (L2H) model proposed training a server model given a fixed local (client) model. This differs from the Learning to Defer (L2D) framework which trains the client for a fixed (expert) server. In both L2D and L2H, the training includes learning a rejector at the client to determine when to query the server. In this work, we extend the L2H model from binary to multi-class classification problems and demonstrate its applicability in a number of different scenarios of practical interest in which access to the server may be limited by cost, availability, or policy. We derive a stage-switching surrogate loss function that is differentiable, convex, and consistent with the Bayes rule corresponding to the 0-1 loss for the L2H model. Experiments show that our proposed methods offer an efficient and practical solution for multi-class classification in resource-constrained environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper extends the ``learning to help'' paradigm from binary classification to multi-class settings. Learning to help aims to learn a rejector for routing between edge legacy devices and server-side large models. This paper provides algorithms with theoretical analysis, followed by experiments on CIFAR-10 and SVHN.

### Strengths
The setting of learning to help is quite interesting and meaningful. The authors extend it to multi-class classification cases, which have extensive applications. The proposed method is theoretically guaranteed. Also, the presentation is good.

### Weaknesses
The main drawbacks of this paper may be in the experiment part.
- The datasets used are small, such as CIFAR-10 and SVHN. And there are only two datasets. Usually, evaluation on 3 datasets (or more) will be better.
- The used LeNet and AlexNet are tiny. Trending sota models like ViT can be considered.
- The learning to help scenarios can be very useful in large language model settings for on-device inference. Can the authors do some experiments on this? Or at least give a discussion.
- How do you partition the data for training the small legacy model and large server model? Is there any difference?
- I am just wondering about the costs of training the rejector and server model. Can the authors elaborate on this? If the costs are too much compared with the efficiency gains afterwards, why not use the server-side model solely?
- Can the authors do some case studies to show which samples need to be handled on the server instead of on the device? It will help to understand the system.
- Towards ``first principle'' to make the thing simple: for image classification tasks, one possible and simple solution is that during inference, check the prediction confidence (e.g., the softmax entropy) of the device model, and if the confidence is lower than a threshold (a predefined hyperparameter), send it to the server. Is this solution possible? It will not require any additional training for a rejector.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this manuscript, a hybrid system is introduced, wherein the local model is supplemented by a server-side model and the rejector selects data samples to be directed to either the client model or the server model. The manuscript presents three distinct scenarios: “pay-per-request”, “intermittent availability”, and “bounded reject rate”, which align with practical constraints related to cost, availability, and policy, respectively. To address these challenges, a differentiable and convex stage-switching surrogate loss function is developed to iteratively optimize both the “rejector function” and “server model”. Experimental results validate the superior performance of the proposed framework.

### Strengths
- The writing of this manuscript is clear, and easy to follow.
- This manuscript addresses three practical scenarios reflecting constraints related to cost, availability, and policy, and derives formal objective functions to represent them.

### Weaknesses
 - The authors state that they extend the “learning to help” framework to handle multi-class classification but do not explain the challenges involved in transitioning from binary-class to multi-class classification.
- In the Conclusion section, the authors state that the proposed framework opens new avenues for further exploration in multi-party collaboration. However, since the evaluation uses relatively simple networks, such as LeNet-5 and AlexNet, the authors should include more complex networks to thoroughly validate the framework's performance.
- Figure 2 illustrates that the hyper-parameters $ c_1$ and $c_2$ significantly affect the system's overall performance. Therefore, it is recommended that the authors evaluate the proposed framework's performance while varying $c_1$ and $c_2$ simultaneously. Additionally, the authors should provide guidance on achieving an optimal balance between $c_1$ and $c_2$.
- Table 1 shows that for the CIFAR-10 and SVHN datasets, when the rejector predicts “local”, the performance of $m(\cdot)$ is lower than $e(\cdot)$. Similarly, when the rejector predicts “remote”, $m(\cdot)$ still performs worse than $e(\cdot)$. Typically, the server model’s performance should surpass that of the local model when the rejector predicts “remote”. The authors should clarify this discrepancy.

### Questions
As presented in the "Weaknesses" section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper focuses on the collaboration between the client model and the server model by using a rejector. To train the rejector, client model, and server model, this paper derives a stage-switching surrogate loss function to allow the asynchronous training between the client model and the server model.

### Strengths
1. The theoretical analysis of this paper is solid, which extends the binary classification setting of L2H to general multi-class settings.

2. The problem is important and the proposed method uses a surrogate loss to asynchronously train client and server model, which is simple yet theoretically effective.

### Weaknesses
The experiments are limited. Experiments are mainly composed of hyper-parameter sensitive analysis evaluations, which lack comparison to baselines. For example, this paper should compare the proposed method with those using the synchronous training method or different surrogate loss functions in terms of overall performance. The current experimental setup does not sufficiently demonstrate the advantages of the proposed asynchronous training approach over simpler, more established methods. The absence of comparisons with alternative strategies, such as a random uploading strategy or a classification-confidence-based uploading strategy, makes it difficult to assess the true effectiveness of the proposed method. The paper also lacks a thorough investigation into the sensitivity of the proposed method to different choices of the rejector model architecture and its impact on overall performance.

### Questions
1. What's the process during the inference stage with the surrogate loss?

2. What's the convergence rate difference between the asynchronous and synchronous methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper extends the L2H model from binary classification to multi-class settings, enabling collaboration between a local (client) model and a remote (server) model, particularly tailored for resource-constrained environments. A stage-switching surrogate loss function is developed to train the server model and a rejector, which facilitates selective sample deferral to the server, thereby optimizing overall performance.

### Strengths
+ This paper contributes by extending the L2H framework to multi-class classification, which enhances the applicability of client-server cooperation in environments with limited resources.

+ The surrogate loss function supports asynchronous training, which aligns with scenarios of intermittent server access, beneficial for distributed learning settings.

+ This paper provides a solid theoretical foundation for the proposed method, supporting its validity and enhancing confidence in its application.

### Weaknesses
 - The client-server setup involves data offloading, raising potential privacy risks. The paper lacks a discussion on privacy-preserving methods, such as differential privacy, which are common in federated learning. Specifically, the paper does not address how the client's data could be protected during the offloading process, especially if the server is not fully trusted. The absence of mechanisms like local differential privacy or secure multi-party computation protocols raises concerns about the practical deployment of the proposed system in privacy-sensitive applications.

- While the surrogate loss aims to approximate the Bayes optimal classifier, the paper does not provide rigorous proofs for its consistency or convergence in multi-class settings, particularly under non-IID data distributions, a common issue in federated learning. The theoretical analysis lacks a detailed examination of how the surrogate loss function behaves when the data distribution varies across clients, which is a realistic scenario in distributed learning. The paper needs to demonstrate that the surrogate loss function converges to the optimal solution even when the data is not identically distributed.

- The approach assumes IID data, which may not reflect real-world federated learning scenarios. Non-IID data could impair the rejector’s effectiveness in making deferral decisions, limiting the model's applicability. The rejector's performance might degrade significantly if the client's data distribution differs substantially from the server's, leading to suboptimal deferral decisions and reduced overall accuracy. This is a critical limitation that needs to be addressed for practical use.

- While the asynchronous training algorithm partially addresses intermittent server availability, it does not fully address the issues of model drift or maintain accuracy under unstable connectivity. Adaptive adjustments for synchronization frequency and performance are not fully explored. The paper does not discuss how the model's performance is affected by varying degrees of asynchrony or how the system can adapt to changes in network conditions, which are common in real-world deployments.

- Relying on a fixed client classifier limits its ability to adapt to new data distributions or improve through collaborative training, potentially degrading performance over time and increasing dependency on the server model. The client classifier's inability to learn from new data or collaborate with the server model can lead to performance degradation over time, especially if the data distribution shifts. This inflexibility is a significant limitation.

- The experimental setup involves relatively simple architectures (LeNet-5 for the client and AlexNet for the server). This limits the generalization of the framework to applications involving more complex models, such as those used in large-scale real-world systems. Additionally, the conclusion’s mention of "multi-party collaboration in hybrid machine learning systems, especially in the era of LLMs." could be misleading, as the paper does not provide any experiments or detailed discussion about large language models.

### Questions
- Could the authors consider privacy-preserving techniques, such as differential privacy, to mitigate potential privacy risks? Additionally, how would these methods impact the proposed approach's effectiveness?

- Can the paper provide theoretical justifications for the surrogate loss's consistency and convergence properties, especially in non-IID data conditions?

- How could the framework adapt to handle non-IID data distributions across clients? Could the rejector's decision-making process be adjusted for such scenarios?

- For asynchronous training, could a method be introduced to adaptively adjust synchronization interval $S$, improving applicability to real-world deployments?

- Is there a way to make the client classifier adaptable to changing data distributions over time?

- Would the method be effective with more complex models, such as GPT-2, as hinted in the conclusion?

### Soundness
2

### Presentation
3

### Contribution
2
