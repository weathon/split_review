# Rehearsal-Free Continual Federated Learning with Synergistic Regularization

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Continual Federated Learning (CFL) allows distributed devices to collaboratively learn novel concepts from continuously shifting training data while avoiding \textit{knowledge forgetting} of previously seen tasks. 
To tackle this challenge, most current CFL approaches rely on extensive rehearsal of previous data. Despite effectiveness, rehearsal comes at a cost to memory, and it may also violate data privacy. 
Considering these, we seek to apply regularization techniques to CFL by considering their cost-efficient properties that do not require sample caching or rehearsal. Specifically, we first apply traditional regularization techniques to CFL and observe that existing regularization techniques, especially synaptic intelligence, can achieve promising results under homogeneous data distribution but fail when the data is heterogeneous. Based on this observation, we propose a simple yet effective regularization algorithm for CFL named \textbf{FedSSI}, which tailors the synaptic intelligence for the CFL with heterogeneous data settings. 
FedSSI can not only reduce computational overhead without rehearsal but also address the data heterogeneity issue. 
Extensive experiments show that FedSSI achieves superior performance compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Federated Synaptic Synergistic Intelligence (FedSSI), a continual federated learning (CFL) approach aimed at reducing catastrophic forgetting without relying on memory-intensive rehearsal techniques. FedSSI employs a regularization-based mechanism named personalized surrogate model (PSM) integrated with Synaptic Intelligence (SI) to handle data heterogeneity across clients in a federated setting. The approach is evaluated across several benchmarks, where it reportedly outperforms baseline CFL methods.

### Strengths
1. The paper addresses a well-known issue in CFL: catastrophic forgetting in the absence of a centralized memory. The rehearsal-free approach aligns well with the privacy and memory constraints of federated learning.

2. The authors validate FedSSI through extensive experiments across multiple benchmarks and tasks, including comparisons with several state-of-the-art CFL methods. The results consistently demonstrate FedSSI’s effectiveness, highlighting its potential as a valuable addition to the CFL landscape.

### Weaknesses
1. Clarity of the proposed method needs to be improved. The proposed method mainly consists of a new way to compute the contribution of the $i$-th parameter in client $k$ to the change of the loss function used in SI and tailored for the CFL problem. I find it very hard to understand intuitively or theoretically why the proposed method is able to address data heterogeneity. Without a strong theoretical justification or comprehensive analysis, the approach lacks depth and could be viewed as heuristic. Moreover,

2. The proposed FedSSI approach builds on well-known regularization techniques commonly used in continual learning, i.e., Synaptic Intelligence. The claim of being rehearsal-free as a unique contribution is underwhelming without showing a clear, unique mechanism that fundamentally sets FedSSI apart from similar approaches. The rehearsal-free property of the proposed method comes from the use of SI as well. By combining elements of personalization and regularization, FedSSI does not seem to introduce fundamentally new ideas but rather adapts existing ones for CFL. 

3. Minor: there are many reference issues in the paper.

### Questions
I suggest the authors to add an algorithm of the proposed method.

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
3

### Summary
The paper introduces FedSSI, a method for tackling Continual Federated Learning (CFL) in federated environments. In CFL, clients continuously learn from new data while retaining knowledge from previous tasks, all without directly sharing data to ensure privacy. A common solution to this problem involves data rehearsal, where past samples are stored and replayed to maintain learning continuity. However, this method can be impractical due to memory limitations. FedSSI addresses these issues by enhancing synaptic intelligence, a technique originally developed for continual learning, to work in CFL settings without the need for data rehearsal. FedSSI has  Personalized Surrogate Model (PSM), which allows each client to balance local data with global information during training. This dual knowledge approach helps clients to mitigate forgetting of previous tasks and enables efficient learning even with highly diverse data across clients. Through extensive experimentation, FedSSI demonstrates its effectiveness over existing methods, particularly in scenarios with significant data heterogeneity, where data differences between clients can be a major obstacle to model performance. By forgoing rehearsal and reducing memory overhead, FedSSI offers a more practical and resource-efficient solution to CFL, aligning well with the demands of real-world applications where data privacy, device limitations, and diverse client data must be managed concurrently.

### Strengths
1. FedSSI eliminates the need for data rehearsal, addressing reducing memory usage on client devices. This makes it highly suitable for resource-constrained environments in FL.

2. The proposed method effectively handles data heterogeneity across clients by introducing the personalized surrogate model (PSM). The model remains accurate and robust even when clients have significantly diverse data (non-IID).

3. Authors have included extensive experiments across diverse datasets and CFL task scenarios.

### Weaknesses
1. The core novelty is incremental rather than foundational. The work builds on known methods (SI) by adjusting them for CFL with a new model component (Personalized Surrogate Model). This makes the paper valuable but not groundbreaking. What are the unique challenges the author faced while applying SI to CFL (Apart from data heterogeneity (non-IID) and catastrophic forgetting)? Specifically, how does the inherent distributed nature of federated learning, with its communication constraints and asynchronous updates, interact with the core mechanisms of SI, which was originally designed for a centralized setting? The paper should delve deeper into these specific challenges beyond just addressing data heterogeneity and catastrophic forgetting.

2. Can the author provide the scalability of the proposed method? What is the total number of clients on whom the method is tested? What if clients participate only partially, i.e., clients are not available for all global iterations? Authors can perform experiments on multiple clients, say 100, and 10% of the clients are available per iteration.  From here, it would be clear the proposed approach is applicable in cross-silo as well as cross-device FL scenarios. The scalability analysis should not only focus on the number of clients but also on the impact of varying client availability and the resulting effects on convergence and performance. This is crucial for real-world deployments where client participation is often unreliable.

3. In Table 3, what is the relation between $\alpha$ and $\lambda$? Can the authors explain it? Is there any theoretical relation between these two? The paper needs to clarify the interplay between the data heterogeneity parameter $\alpha$ and the PSM control coefficient $\lambda$. A more detailed explanation of how these parameters interact and influence the model's learning behavior is required. Is there a principled way to determine the optimal value of $\lambda$ given a specific level of $\alpha$, or is it purely empirical?

4. In Table 4, the authors evaluate the best test accuracy versus the communication rounds. Except for CIFAR100,  the proposed approach takes more communication rounds to achieve the best accuracy. Can the author explain why the proposed approach needs more communication rounds? Authors can provide a more detailed analysis of the trade-offs between communication rounds and accuracy. Authors can give an insight into the impact of the method's practical implementation in bandwidth-constrained environments. The analysis should also consider the computational overhead at each client, as well as the communication cost of transmitting model updates. A comprehensive analysis of these factors is necessary to fully assess the practical viability of the proposed approach.

### Questions
Asked in weakness.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the poor performance of Synaptic Intelligence in Non-IID scenarios within FL + CL contexts, where catastrophic forgetting remains significant. It attributes this to the failure of traditional global model-based surrogate loss methods due to data heterogeneity. Therefore, it introduces a personalized surrogate model to balance global and local knowledge during training.

### Strengths
1. The empirical results seem promising.
2. The proposed method is quite simple and the overall writing is clear.
3. The experimental analysis is abundant.

### Weaknesses
1. Some misunderstandings: A personalized surrogate model is introduced to balance global and local knowledge during training. However, it still requires data from previous tasks to update the personalized surrogate model, which seems to conflict with the "rehearsal-free" claim in the title. Especially in equation 5, the model needs the samples in last task to do the momentum updating in the new task. But I'm open to further discussions or authors' defending in their rebuttals.
2. Confusing definitions: I think it’s not accurate to conclude a class-incremental will share the same domain space. We can hardly say data from different classes will share a similar distribution. Despite that I do understand authors want to convey that data in class incremental setting would be data from one task, I think rewrite the definition part in 172-179 lines will be a wise choice.
3. Lack of in-depth analysis: The proposed method is more like a combination of existing techniques (personalized federated learning and Synaptic Intelligence). Plus, the analysis provided is not completely new to me as Synaptic Intelligence is a very matured technique in Continual Learning. From my perspective, the fact that data heterogeneity will harm the effects of regulation-based anti-forgetting techniques is also quite normal. I do not find adding a personalized surrogate model for each client and using Synaptic Intelligence technique is a challenge. Of course, I acknowledge that employing PSM module based on SI algorithm to further alleviate the catastrophic forgetting caused by data heterogeneity is somewhat new but it may not reach an ICLR standard.

### Questions
See the weakness.

### Soundness
2

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
The paper addresses the challenge of Continual Federated Learning (CFL), which involves distributed devices learning from streaming tasks while retaining knowledge from previous tasks. The authors identify the limitations of existing CFL approaches that rely on data rehearsal and propose an regularization method called FedSSI, which enhances Synaptic Intelligence (SI) by incorporating a Personalized Surrogate Model (PSM). This approach allows clients to leverage both local and global data distributions, improving performance in heterogeneous data environments. The results demonstrate that FedSSI outperforms state-of-the-art methods.

### Strengths
1.The paper tackles the significant problem of catastrophic forgetting in Continual Federated Learning (CFL), which is crucial for the practical deployment of federated learning systems in dynamic environments.

2.The paper includes comprehensive experiments on various datasets and CFL task scenarios (both Class-Incremental Learning and Domain-Incremental Learning), providing strong empirical evidence of the method's effectiveness.

3. The use of personalized alternative models (PSM) to enhance synaptic intelligence (SI) can mitigate knowledge forgetting, especially in non-IID data Settings.

### Weaknesses
1.	While the paper tells an interesting story in this paper, the core idea is an extension of existing methods . It seems like a combination of Synaptic Intelligence (SI) and Continual Federated Learning (CFL).

2.	Although the authors' goal is to solve the CFL problem, it is actually the well-studied Non-iid problem in Federated Learning. This is also evident from the authors' theoretical analysis. There is no way for the authors to discuss how PSM is different under CFL.

3. The proposed method heavily depends on SI. If SI has inherent limitations or does not perform well under certain conditions, FedSSI might inherit these shortcomings.

4. The combination of global and local models is a well-explored area in federated learning, and the authors do not discuss a model mixing approach better suited to the characteristics of CFL, except for PSM. Proposing a new mixing method would help to increase the contribution of the paper.

5. Although the proposed method avoids data rehearsal, introducing the PSM could add storage overhead or complexity that may not be practical for edge devices with limited resources. The paper may not sufficiently discuss the storage costs or provide strategies to mitigate them.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
