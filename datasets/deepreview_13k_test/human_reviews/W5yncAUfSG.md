# Efficient Personalized Federated Learning via Adaptive Weight Clustering Pruning

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
This paper introduces a novel personalized federated learning approach, Adaptive Federated Weight Clustering Pruning (AdFedWCP), specifically designed to optimize communication efficiency in heterogeneous network environments. AdFedWCP innovatively combines adaptive weight clustering pruning techniques, effectively addressing data and bandwidth heterogeneity. By dynamically adjusting clustering centroids based on layer importance and client-specific data characteristics, it significantly reduces communication overhead. Experimental results show that AdFedWCP achieves a reduction in communication volume ranging from 87.54% to 87.82% in communication volume, surpassing the state-of-the-art work on reducing communication overhead in personalized federated learning. AdFedWCP also surpasses existing methods in terms of accuracy across multiple datasets, with improvements ranging from 9.13% to 21.79% over the baselines on EMNIST, CIFAR-10, and CIFAR-100. These results highlight AdFedWCP’s advantages in balancing communication efficiency and model accuracy, making it an ideal choice for resource-constrained federated learning environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an Adaptive Federated Weight Clustering Pruning (AdFedWCP) to address the data and communication heterogeneity issues. Specifically, an imprinting method is designed to calculate the importance level of each layer; then, the number of clustering centroids is determined by the server based on the client's data and communication information; finally, each client executes the weight clustering pruning. Experimental results based on three datasets show that the model accuracy of  AdFedWCP is boosted while the communication overhead is reduced compared to baselines.

### Strengths
1. There are both theoretical and experimental analyses.

2. The layer importance and weight cluster pruning are valuable research problems for heterogeneous federated learning.

### Weaknesses
1. More than half of the abstract's content is about the experimental result, while the experimental part of the paper is only two pages long. I suggest the abstract should summarize more key points and the main body should include more result analysis.

2. Authors claim many times that one main advantage of AdFedWCP is addressing the bandwidth heterogeneity problem that many other methods can not handle. However, there is no detailed explanation of the bandwidth heterogeneity problem and no clear definition of bandwidth heterogeneity.

3. The authors claim that their research problem is to minimize communication costs and address the bandwidth heterogeneity problem without compromising model accuracy. However, the optimization objective defined in section 3 is not related to communication costs/bandwidth heterogeneity.

4. Figure 1 should be refined to illustrate more clearly how these values are calculated and show the overall framework of  AdFedWCP.

5. Only the final results are in the experiment part, and the learning curves (e.g., communication cost vs. model accuracy) are missing.

6. The description of the client heterogeneity settings (lines 465-467) is not detailed enough. Since bandwidth heterogeneity is the key point in this paper, related experimental settings should be more carefully designed and described in more detail. For a client, will its bandwidth also change over time?

7. The limitations of AdFedWCP should also be discussed, except for the advantages.


8. For Table 1 and Table 2, the best value should be bolded, and the second best value should be underlined for better comparison and readability.

### Questions
1. There are several hyper-parameters in the proposed method, e.g., lines 130-131 and lines 366-367. Will different values of these hyper-parameters affect performance a lot? Why or why not? How to choose proper values for implmentations?

2. Can authors provide more learning curves (e.g., communication cost vs. model accuracy) of AdFedWCP and other baselines to show the stability and comparison?

3. How many clients will participate in the training among all clients? There is no such information.

4. For a client, will its bandwidth also change over time in the experiment?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a personalized federated learning method called AdFedWCP, which optimizes communication efficiency in heterogeneous networks through adaptive weight clustering pruning. The experimental results indicate that this method outperforms existing baseline methods in terms of both communication efficiency and accuracy across multiple datasets.

### Strengths
1)Innovation: The introduction of a dynamic weight clustering pruning mechanism effectively addresses issues related to bandwidth and data heterogeneity.
2)Theoretical Analysis: The paper provides detailed theoretical support, ensuring the validity of the proposed method.
3)Comprehensive Experimental Design: The experiments cover multiple datasets, validating the performance of the method.

### Weaknesses
1)Insufficient Support for Cluster Number Selection: While the idea of dynamically adjusting the number of clusters is novel, the paper lacks detailed theoretical justification and empirical data to support the selection criteria for the number of clusters. It is recommended to include relevant discussions.
2)Inadequate Analysis of Experimental Results: The interpretation of results is somewhat superficial and fails to explore the reasons for performance deficiencies on specific datasets (e.g., CIFAR-100). Particularly, the accuracy on CIFAR-10 and CIFAR-100 does not reach optimal levels, indicating that the method's performance on more complex datasets requires improvement.
3)Comparison with FedWCP on K Values: In the comparison with different K values of FedWCP, AdFedWCP did not consistently outperform other configurations, suggesting that the balance between model complexity and performance remains an issue.
4)Lack of Comparative Experiments: There is insufficient comparison with the latest related methods, such as [1], resulting in an inadequate assessment of AdFedWCP's effectiveness. Including comparisons with other advanced methods would strengthen the conclusions.
5)Inadequate Discussion of Limitations: The conclusion section does not address the limitations of AdFedWCP. It is recommended to analyze its performance in extremely heterogeneous environments and to provide suggestions for future research directions.
6)Insufficient Discussion on the Trade-off between Communication Efficiency and Model Performance: While the experimental results show improvements in communication efficiency, there is a lack of in-depth discussion on the trade-off between communication costs and model complexity, which may lead to insufficient understanding of the method's applicability.
7)Incomplete Ablation Study: The paper fails to adequately discuss the effectiveness of different layer importance evaluation strategies, particularly the comparison between the imprinting method and other evaluation methods (e.g. [2]). This is crucial for optimizing model compression strategies.
[1] Wu C, Wu F, Lyu L, et al. Communication-efficient federated learning via knowledge distillation[J]. Nature communications, 2022, 13(1): 2032.
[2] Ma X, Zhang J, Guo S, et al. Layer-wised model aggregation for personalized federated learning[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 10092-10101.

### Questions
See the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes AdFedWCP framework, aims to improve personalized federated learning in the face of local data and communication bandwidth heterogeneity while maintaining model performance and communication efficiency. AdFedWCP features a adaptive weight clustering pruning strategy to reduce the per-client model size based on each client’s characteristics. This mechanism dynamically adjusts cluster centroids per layer based on layer importance, client data, and communication constraints through an integrated adaptive scheme, effectively addressing bandwidth heterogeneity.

### Strengths
1.	Convergence analysis of the proposed method is provided.
2.	The proposed method achieves significant communication overhead reduction.

### Weaknesses
1.	The aim of this paper is to propose an efficient FL approach “for resource-constrained federated learning environments”. However, the main contribution of this paper is limited to the communication cost, which is insufficient to address the resource constraints of heterogeneous clients. It is not clear whether the overall resource consumption such as computational overhead will be reduced.
2.	In this paper, weight clustering and layer importance estimation are integrated, but the unique contributions of these two strategies compared to existing work are not clear. The novelty of simply converting these centralized strategies to distributed versions is limited.
3.	In this paper, three key components are designed for AdFedWCP: weight clustering pruning, layer importance estimation, and dynamic centroid optimization strategies. However, this paper does not discuss their resource consumption, which is important for efficient FL methods.
4.	The ablation study in this paper could be improved, especially the empirical results about resource consumption of weight clustering pruning, layer importance estimation and dynamic centroid optimization strategies.

### Questions
1. Is AdFedWCP applicable to heterogeneous clients with different resource capabilities (including computing resources, communication resources, storage resources, etc.)?
2. How does AdFedWCP handle the situation where the clients in the FL cannot afford the resource requirements of the weight clustering pruning, layer importance estimation, and dynamic centroid optimization policies?

### Soundness
2

### Presentation
2

### Contribution
2
