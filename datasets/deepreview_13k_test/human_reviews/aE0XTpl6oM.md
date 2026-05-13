# GREC: Doubly Efficient Privacy-preserving Recommender Systems for Resource-Constrained Devices

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Federated recommender system (FedRec) has emerged as a solution to protect user data through collaborative training techniques. However, the real-world implementation of FedRec is hindered by two critical resource constraints of edge devices: a) limited upload bandwidth and b) limited user computational power and storage. Existing methods addressing the first issue, such as message compression techniques, often result in accuracy degradation or potential privacy leakage. For the second issue, most federated learning (FL) protocols assume that users must store and maintain the entire model locally for private inference, which is resource intensive. To address these challenges, we propose doubly efficient privacy-perserving recommender systems (GREC) consisting of both training and inference phase. To reduce communication costs during the training phase, we design a lossless secure aggregation (SecAgg) protocol based on functional secret sharing leveraging the sparsity of the update matrix. During the inference phase, we implement a user-side post-processing local differential privacy (LDP) algorithm to ensure privacy while shifting the bulk of computation to the cloud. Our framework reduces uplink communication costs by up to 90x compared to existing SecAgg protocols and decreases user-side computation time during inference by an average of 11x compared to full-model inference. This makes GREC a practical and scalable solution for deploying federated recommender systems on resource-constrained devices.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes GREC, doubly efficient privacy-preserving recommender systems consisting of both training and inference phase. The goal is to improve federated recommender systems with the constraints of upload bandwidth and limited user computational power and storage. For the training phase, the authors design a lossless secure aggregation protocol based on functional secret sharing. For the inference phase, a user sider post-processing local differential privacy algorithm is proposed to ensure privacy. Experimental results show significant communication cost reduction of GREC compared with general purpose SecAgg, as well as user-side computation time reduction.

### Strengths
This paper proposes a framework to solve an important problem: reducing communication cost and user-side computation time for federated recommender systems. Related papers are cited and discussed. The optimization on the training phase leverages functional secret sharing scheme for the point function. For the inference phase, an LDP with post-processing mechanism is proposed to enable users to make their data private and send the data to the server to reduce computation cost on the user-side. Experimental results are shown to support the effectiveness of the proposed framework.

### Weaknesses
* I found the contribution of this paper incremental. The functional secret sharing scheme for the point function mechanism is from previously published papers. The LDP with user-side post-processing mechanism is also similar to previous work that is cited. 
* It was stated in the introduction that there are other existing compression methods, but they "often result in non-negligible accuracy loss". However, there is no experimental comparison with these compression methods, but only with "general purpose" SecAgg methods.
* No error bars on the experimental results.

### Questions
* I'm a bit surprised that the inference accuracy on a single user's LDP data (without de-noise) is only ~40% higher than the non-privacy data. Usually a single user's data with LDP and reasonable (epsilon, delta) should have very large error.  Is it user-level or record level LDP?
* In section 4.1, it is mentioned that you "sample a portion of top users ranked in descending order by their number of rated items". Why not just sample the users uniformly at random to better represent the dataset? 
* Have you compared your framework with other compression algorithms?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a federated recommender system tailored for edge devices with limited computational and communication resources. The main technical contributions include a redesign for secure aggregation protocols, and a cloud inference approach with local differential privacy guarantee.

### Strengths
The paper proposes doubly efficient privacy-perserving recommender systems (GREC) consisting of both training
and inference phase. Both the SecAgg and LDP mechanisms are adapted thoughtfully to address specific limitations in edge environments.

### Weaknesses
1. While LDP is known to degrade model performance, GREC's method of user-side post-processing aims to minimize this. However, more detail on the denoising model’s training and its impact on utility in high-dimensional settings would strengthen the argument for its scalability and robustness.
2. While the GREC claims to have doubly efficiency approach, the relationship between its design for training and inference is not clear. The two parts seem to be independent. 
3. For LDP based approach, the evaluation only uses epsilon = 1 setting, which is not enough. Usually for DP related work, tradeoffs between different privacy budgets (e.g., epsilon = 0.1, 0.3, 0.5, 0.7) and performance is expected.
4. Although the work's contributions to efficient and privacy-preserving federated learning are relevant to the ML community, its main technical novelty lies in the cryptographic components, rather than algorithm design/utility.

### Questions
1. Add detail on the impact on utility of LDP in high-dimensional settings is needed. That's when LDP would usually greatly degrade utility. 
2. Explicitly discuss how the training and inference components interact or complement each other.
3. More evaluation regarding tradeoffs between different privacy budgets  (e.g., epsilon = 0.1, 0.3, 0.5, 0.7) and performance is expected.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers two key challenges in secure federated recommendation systems (FRS) for resource-constraint devices: minimizing communication costs and reducing computation/storage costs on edge devices. To address the first challenges, the proposed method, named GREC, introduces a functional secret sharing (FSS)-based Secure Aggregation (SecAgg) protocol that leverages the sparsity of item embeddings to improve communication efficiency. For the second challenge, GREC employs a user-side post-processing local differential privacy (LDP) mechanism during inference phase. This paper empirically demonstrates that GREC can reduce communication costs by up to 90x and user-side inference time by 11x compared to existing baselines.

### Strengths
- This paper considers a timely and important problem in FRS with privacy enhancements (secagg and DP).
- This paper use a funcional secret sharing (FSS) for secure aggregation on top of lerveraging the sparsity of item embeddings, which is both novel and practical. This allows GREC to significantly reduce the communication burden without sacrificing model performance or privacy.
- The introduction of a post-processing LDP mechanism that shifts much of the computation to the cloud, while maintaining privacy guarantees, is a practical and thoughtful contribution. The approach provides a good balance between privacy protection and computational/storage complexities.

### Weaknesses
- The comparison between GREC and general-purpose SecAgg in Section 3.1.3 and Table 1 may not be entirely fair, as only GREC takes advantage of the sparsity of item embeddings. Other works, such as Liu, Tao, et al. (2023) also leveraged sparsity to reduce communication costs of the secure aggregation protocol. For a fair assessment, GREC should be compared to such approaches both in asymptotic analysis and experiments.
  - Liu, Tao, et al. "Efficient and secure federated learning for financial applications." Applied Sciences 13.10 (2023): 5877.
- While the paper provides a detailed privacy analysis for the training phase, the analysis for the inference phase, especially in the context of cloud-based inference, could be more thorough. The paper assumes that the cloud environment is fully secure, but this assumption may not always hold in real-world deployments, which could compromise the overall privacy guarantees.

### Questions
- In the paper, the authors assume that $m'$ (the number of rated items) and $\mathcal{I}_u$ (the set of rated items for user $u$) remain fixed. Could the authors clarify how the system handles scenarios where a user rates new items, leading to changes in $\mathcal{I}_u$? Specifically, how does this affect the secure aggregation process and communication overhead?
- While the paper focuses on user-side privacy, a more detailed discussion on the assumptions about the security of cloud-based servers during inference would add depth to the privacy analysis. It would be beneficial to explore potential scenarios where the server could be compromised and how GREC might mitigate such risks.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes a privacy-preserving federated recommendation system method that aims to alleviate communication and computational bottlenecks that arise on resource-constrained edge devices. Communication costs are reduced via a functional secret sharing method, computational costs are reduced by shifting inference to the cloud, and privacy is ensured through a local differential privacy (LDP) mechanism. Empirical results showcase a reduction in memory while also reducing test RMSE.

### Strengths
I enjoy the idea of leveraging the central server for both privacy benefits (via the FSS) and computational costs. More FL algorithms should think about leveraging the central server for computational costs instead of vice-versa. 

This method seems to be applicable to many other ML/FL applications where there are sparse updates to embedding layers.

The empirical reduction in communication costs is impressive and the reduction in RMSE is only very marginal.

The paper, while pretty technical, is well-written with nice presentation.

### Weaknesses
There aren't any true test accuracy results, could the authors report classification accuracy?

Is the method scalable, since the server has to receive FSS updates, perform secure aggregation, update the model, and perform inference all at once? It seems that there would be quite a bottleneck once the number of devices increase to realistic numbers.

### Questions
It would be nice if the authors could include the Related Works section within the main body. It would be easier for people, like me, to better grasp the problem and see other works if it is available in the main body.

If server's collude, will FSS fail in terms of privacy? What would motivate two separate servers to participate in training and take on extra computational burdens? In most settings, one single company would act as the server. When would two separate servers be a realistic setting?

For clarification, is $m$ simply the number of items that can be recommended? I was curious when the inequality $m′ < mbd/ ((λ + 2) log m + bd)$ would fail to hold. Is this ever a concern?

I know that there are some works that leverage locality-sensitive hashing approaches (LSH) to efficiently perform large-scale recommender system training. These include SLIDE and MONGOOSE (Chen et al. 2020/2021). Other works have leveraged these methods for LSH RecSys training in the edge setting, namely "Adaptive Sparse Federated Learning in Large Output Spaces via Hashing" (Xu et al. 2022) and "Large-Scale Distributed Learning via Private On-Device Locality-Sensitive Hashing" (Rabbani et al. 2023). These works might not be crucial to compare against, but they are another method for efficient RecSys training! Hope these can be interesting reads for you.

### Soundness
3

### Presentation
3

### Contribution
3
