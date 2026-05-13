# FedGP: Buffer-based Gradient Projection for Continual Federated Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Continual Federated Learning (CFL) is essential for enabling real-world applications where multiple decentralized clients adaptively learn from continuous data streams. A significant challenge in CFL is mitigating catastrophic forgetting, where models lose previously acquired knowledge when learning new information. Existing approaches often face difficulties due to the constraints of device storage capacities and the heterogeneous nature of data distributions among clients. While some CFL algorithms have addressed these challenges, they frequently rely on unrealistic assumptions about the availability of task boundaries (i.e., knowing when new tasks begin). To address these limitations, we introduce \ours{}, a federated adaptation of the A-GEM method~\citep{AGEM}, which employs a buffer-based gradient projection approach. \ours{} alleviates catastrophic forgetting by leveraging local buffer samples and aggregated buffer gradients, thus preserving knowledge across multiple clients. Our method is combined with existing CFL techniques, enhancing their performance in the CFL context. Our experiments on standard benchmarks show consistent performance improvements across diverse scenarios. For example, in a task-incremental learning scenario using the CIFAR-100 dataset, our method can increase the accuracy by up to 27\%.
\nnfootnote{A preliminary version of this work was presented at the Federated Learning Systems (FLSys) Workshop @ Sixth Conference on Machine Learning and Systems, June 2023.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents FedGP, an approach that addresses the challenges of continual federated learning (CFL) by integrating techniques from both continual learning (CL) and federated learning (FL). At its core, FedGP conducts server aggregation of local buffer gradient to obtain a global buffer gradient. Then use the global buffer gradient to guide the local continual learning by gradient projection. Furthermore, in the federated context, FedGP preserves the knowledge across multiple tasks in a  non-iid and heterogeneous client data distribution. Through this integration, FedGP improves the performance of current CFL approaches.

### Strengths
The paper is easy to read and follow, and the extensive experiments show the resulting improvement spanning many datasets and baseline methods. The proposed methods also work with a large number of clients and partial client aggregation in FL.

### Weaknesses
1. While I'm familiar with FL and CL, I'm not a deep expert in CFL. Observing FedGP, it seems to be a federated take on A-GEM, where g_ref is replaced by a federated aggregation of local buffer gradients. Although FedGP shows promising results when combined with other methods, I'm still pondering its overall novelty and contribution.

2. In the experimental section, Table 1 presents the performance of all baseline methods. It's noticeable that, in the without FedGP column, even though CFL methods are designed for continual learning challenges, some, especially FL+iCaRL/L2P, performed better than CFL methods. Can the authors clarify the reasons behind these results?

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces FedGP, a buffer-based gradient projection method designed for continual federated learning. FedGP effectively tackles the challenge of catastrophic forgetting while amplifying the performance of the continual learning and continual federated learning techniques. Extensive experiments conducted on multiple benchmarks demonstrate the effectiveness of the proposed FedGP method.

### Strengths
1. This paper introduces a buffer-based gradient projection method to address the catastrophic forgetting in continual federated learning.
2. This work is straightforward and easily understandable, making it reader-friendly for potential readers.
3. Extensive experimental results demonstrated the effectiveness of the proposed FedGP method.

### Weaknesses
The paper focus on an interesting continual federated learning problem and has several issues that can be improved: The proposed FedGP method suffer from more communication costs than comparison methods. Moreover, additional gradients need to be uploaded to the server which increases the risk of the local data leakage. The gradient projection that conflict with the previous task update direction would aggravate forgetting, while directly drop it would impair the current task learning. The proposed method can be addressed the forgetting to some extent while ignoring its impact on the current task. In Table 3, the two times communication get an inferior performance than the equalized communication with FedGP in P-MNIST, can you give an explanation? The adopted comparison methods seem to be outdated, it is better to adopted the SOTA methods to further validate the effectiveness of the proposed FedGP method. The literature[1] also addressed the forgetting by using gradient projection, which has a strong connection with the proposed method. It is better to taken as a comparison method.

### Questions
(1) The gradient projection that conflict with the previous task update direction would aggravate forgetting, while directly drop it would impair the current task learning. The proposed method can be addressed the forgetting to some extent while ignoring its impact on the current task.

(2) In Table 3, the two times communication get an inferior performance than the equalized communication with FedGP in P-MNIST, can you give an explanation?

(3) The adopted comparison methods seem to be outdated, it is better to adopted the SOTA methods to further validate the effectiveness of the proposed FedGP method.

(4) The literature[1] also addressed the forgetting by using gradient projection, which has a strong connection with the proposed method. It is better to taken as a comparison method.

(5) Please see the weakness above.

[1] Gradient Projection Memory for Continual Learning, In ICLR 2021

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a approach called FedGP for addressing the challenge of catastrophic forgetting in Continual Federated Learning, where decentralized clients learn from continuous data streams. FedGP aims to preserve knowledge across clients by leveraging local buffer samples and aggregated buffer gradients. This method enhances the performance of existing continual learning and CFL techniques and demonstrates performance improvements on standard benchmarks.

### Strengths
The experiment part is comprehensive and solid. The authors compare the proposed method with various baselines on a number of tasks. The experiment details and results are well presented and explained. The authors also report the storage, communication, computation overhead of the proposed methods, which is great importance to show the efficiency of the proposed method.

### Weaknesses
1. The novelty of the proposed method is questionable. The key steps of the proposed FedGP algorithm, including using buffers and performing gradient projection, can all be found in previous works [1]. The only major difference, as far as I can tell, is to extend the centralized setup in [1] to a decentralized/federated setup.
2. The algorithm design of FedGP is mostly heuristic and not well motivated. For example,  the authors do not rigorously explain why the gradient projection operation and the buffer updating algorithm will solve the catastrophic forgetting problem and  fit into the FL setting. A theoretical analysis and more ablations on algorithm design will help to show the effectiveness of FedGP.
3. I am skeptical about whether the use of a buffer can solve the problem of catastrophic forgetting. Since the buffer size is limited, one is unable to store the entire past information in it, and has to discard stale information. According to Algorithm 4, when the buffer is full the algorithm randomly selects an old entry in the buffer and replace it with a new data point. How can this avoid discarding useful information, e.g., the data point stored in previous rounds?

### Questions
See the weaknesses part

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
