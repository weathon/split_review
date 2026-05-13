# FedRC: Tackling Diverse Distribution Shifts Challenge in Federated Learning by Robust Clustering

- Decision: Reject
- Scores: 8, 8, 5

## Abstract
Federated Learning (FL) is a machine learning paradigm that safeguards privacy by retaining client data on edge devices. However, optimizing FL in practice can be challenging due to the diverse and heterogeneous nature of the learning system.
    Though recent research has focused on improving the optimization of FL when distribution shifts occur among clients, ensuring global performance when multiple types of distribution shifts occur simultaneously among clients---such as feature distribution shift, label distribution shift, and concept shift---remain under-explored.
    In this paper, we identify the learning challenges posed by the simultaneous occurrence of diverse distribution shifts and propose a clustering principle to overcome these challenges.
    Through our research, we find that existing methods fail to address the clustering principle.
    Therefore, we propose a novel clustering algorithm framework, dubbed as \algfed, which adheres to our proposed clustering principle by incorporating a bi-level optimization problem and a novel objective function.
    Extensive experiments demonstrate that \algfed significantly outperforms other SOTA cluster-based FL methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes FedRC, a novel algorithm framework based on soft clustering, to ensure global model performance when multiple types of distribution shifts occur in clients' data, including feature shift, label shift, and concept shift. Specifically, FedRC addresses the challenges posed by distribution drift by combining the proposed clustering principles with a dual level optimization problem and a new objective function. The main contributions of this paper are: 
1) This paper proposes the principle of robust clustering to address the challenges posed by multiple data distribution drift.
2) This paper proposes that FedRC implement robust clustering principles and provides theoretical analysis.
3) This paper conducts experiments on multiple datasets to demonstrate the effectiveness of the proposed method and FedRC can be integrated with existing methods.

### Strengths
1)	The paper is technically well presented.
2)	The proposed method is well-motivated and novelty, the analysis of the related work is clear and convincing.
3)	The paper provides rigorous theoretical analysis of the proposed method. 
4)	The authors do a lot of experiments to prove that their method is good and compare it with many existing methods, the results seem convincing.

### Weaknesses
1) It will be clearer if there is a workflow diagram to explain the working principle of the proposed method. 
2) According to the robust clustering principle proposed by the author, clients with concept drift are classified into different categories. It will be more convincing if the division results are presented. 
3) In Tables 1, 2, and 4, some methods have very low accuracy on CIFAR100 or Tiny-ImageNet datasets. Authors should provide reasons for the very low accuracy in experimental analysis. 
4) The writing of some symbols should be unified. In Eq. (1), $x_{ij}$ and $y_{ij}$ should be $x_{I,j}$, and $y_{I,j}$.

### Questions
1) Concept shift has two cases: “same label different features” and “same feature different labels”, Can the FedRC ignore the difference between the two concept shifts in this paper? 
2) Figure 2 (a) is not mentioned in the main text. And according to the results in Figure 2 (a), there is concept drift in scenarios with significant improvement in FedRC. Is FedRC only more effective for concept drift? 
3) In section 4.1, the authors claim that If (x, y) exhibits the concept shift with respect to the distribution of cluster k, P (y | x; θ_k) will be small. Please give a detailed explanation.
4) In Algorithm 1, does each client need to calculate local update for each clustering model? If so, should loops be added to k models in local update? 
5) The title of Figure 5 mentions' Both groups have IID training and test datasets'. Does 'IID' here refer to the overall data distribution of all clients or the data distribution of each client? If the data distribution of the clients is IID, does it conflict with the settings of the participating clients?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies the learning challenges posed by the simultaneous occurrence of diverse distribution shifts and propose a clustering principle to overcome these challenges, i.e., separating clients with concept shifts into different clusters, while keeping clients without concept shifts in the same cluster.
The principle is further translated into a bi-level optimization problem which are provided with an efficient and convergent optimizer. 
Extensive experiments demonstrate that FedRC significantly outperforms other SOTA.

### Strengths
1. The paper identifies an important problem 'ensuring global performance when multiple types of distribution shifts occur simultaneously among clients'. The illustration of Figure 1 clearly shows the motivation.
2. The algorithm comes with theoretic analysis including convergence proof for FedRC as well as RobustCluster.
3. The experiments are presented with sufficient details, such as ablations and experiments on real-world concept shift data. Great effort.

### Weaknesses
1. Section 6, it seems 'future work' has already been done by the appendix. Better find 'real' future work or change the title of the last section.
The same goes for 'Limitations'.
2. It seems that FedRC outperforms previous SOTA by a large margin. The success of FedRC seems lie in the objective funtion eq. (8). However, there is a lack of theoretic comparison between eq. (8) and the obj. func of existing methods.

### Questions
no

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the federated learning problem with heterogeneous data induced by multiple types of distribution shifts, e.g., feature shift, label shift, and concept shift. To solve this problem, this paper introduced a principle of robust clustering where clients with concept shifts should be clustered together. Then, it proposed a novel FedRC approach (as well as its centralized version RobustCluster) to find the clusters based on the types of distribution shifts. The convergence of RobustCluster was also theoretically analyzed.

### Strengths
**Originality:** This paper studied a more challenging clustered FL setting where multiple types of distribution shifts existed in local clients. It pointed out that the clusters with concept shifts might not learn a common decision boundary, and existing clustered FL approaches failed in handling the concept shifts. This paper then proposed a novel FedRC with concept shift aware objective function. Experiments demonstrated that FedRC achieved better performance than clustered FL baselines in various data sets.

**Quality:** The motivating example in Figures 3&4 clearly illustrated the principles of robust clustering in handling concept shifts. Then the principles of robust clustering also guided the design of the objective function in Eq. (1). The clients with concept shifts were expected to clustered in different groups. The experiments verified the effectiveness of FedRC with respect to local and global generalization performance.

**Clarity:** The motivation of this paper is clear. Different from feature or label shift, concept shift essentially affects the clustering structure. The objective function in Eq. (1) aims to avoid generating clusters with concept shifts. Experiments show that the proposed FedRC significantly outperforms existing clustered FL methods.

**Significance:** The problem studied in this paper is practical but challenging. In real scenarios, different types of distribution shifts occur simultaneously among clients. As a result, adaptively generating clusters based on the types of distribution shifts can be applied to solve real-world federated learning problems.

### Weaknesses
**W1:** The impact of feature and label shifts on clustering can be further explained. The goal of the proposed clustered method is to separate clients with concept shifts into different clusters. It might consider clients with feature and label shifts into a single cluster. Thus, the clustering quality can also be affected by the feature and label shifts. For example, a single model might fail to hand clients with large label shifts.

**W2:** The optimization of Eq. (2) is unclear. 
- Firstly, the definition of $\tilde{\mathcal{I}}(\mathbf{x}, y; \theta_k)$ is confusing. It is defined over the weights $\gamma_{i,j; k}$, but $\gamma_{i,j; k}$ is also defined over $\tilde{\mathcal{I}}(\mathbf{x}, y; \theta_k)$ in Eq. (4). 
- Secondly, the updating in Eqs. (4)(5) are not associated with $\lambda_i$ in Eq. (2). Then how would the second term of Eq. (2) affect the optimization?

**W3:** The convergence of FedRC is not provided. Theorem 4.3 shows the convergence of the centralized version of FedRC. Can it also hold for federated learning scenarios?

**W4:** Step 2 in Algorithm 1 is not explained. It is unclear why checking and removing models are necessary for FedRC during training.

### Questions
**Q1:** Figure 1 is hard to follow. It is confusing how label shift and concept shift are involved in Figure 1.

**Q2:** Section 3 compares different clustered FL algorithms in Figure 3. It shows that existing approaches, e.g., FeSEM, IFCA, are not robust to feature and label shifts. But it is confusing how these observations are indicated in Figure 3.

**Q3:** Does FedRC in Algorithm 1 update $\gamma_{i,j; k}, w_{i; k}$ once and $\theta_{i; k}$ for $\Gamma$ local steps?

**Q4:** How are the models of nonparticipating clients generated during testing in the experiments?

**Q5:** Figure 6(d) shows that FedRC outperforms FedAvg and retains robustness when there is only one concept. When there is only one concept, would FedRC exactly recover FedAvg?

**Q6:** Figure 6(c) shows that FedRC with hard clustering consistently outperforms that with soft clustering. Besides, hard clustering can better satisfy the principles of robust clustering by separating clients with concept shifts into different clusters. In this case, It is confusing why not simply apply hard clustering when optimizing FedRC.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
