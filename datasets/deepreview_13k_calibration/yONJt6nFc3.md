# Node Duplication Improves Cold-start Link Prediction

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Graph Neural Networks (GNNs) are prominent in graph machine learning and have shown state-of-the-art performance in Link Prediction (LP) tasks. Nonetheless, recent studies show that GNNs struggle to produce good results on low-degree nodes despite their overall strong performance. In practical applications of LP, like recommendation systems, improving performance on low-degree nodes is critical, as it amounts to tackling the cold-start problem of improving the experiences of users with few observed interactions. In this paper, we investigate improving GNNs' LP performance on low-degree nodes while preserving their performance on high-degree nodes and propose a simple yet surprisingly effective augmentation technique called \ours. Specifically, \ours duplicates low-degree nodes and creates links between nodes and their own duplicates before following the standard supervised LP training scheme. By leveraging a ``multi-view'' perspective for low-degree nodes, \ours shows significant LP performance improvements on low-degree nodes without compromising any performance on high-degree nodes. Additionally, as a plug-and-play augmentation module, \ours can be easily applied on existing GNNs with very light computational cost. Extensive experiments show that \ours achieves \textbf{38.49\%}, \textbf{13.34\%}, and \textbf{6.76\%} improvements on isolated, low-degree, and warm nodes, respectively, on average across all datasets compared to GNNs and state-of-the-art cold-start methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an augmentation-based method (i.e., NodeDup) tailored for the isolated and low-degree nodes in the link prediction task. The proposed method can not only significantly improve the prediction performance on cold nodes, but also can maintain the overall prediction capability. By simply duplicating the cold nodes, the proposed method exhibits faster running speed than the previous methods based on augmentation. Comparing with the vanilla GNN models, the cold-start models, and the graph data augmentation models, the experimental results are sufficient to demonstrate the superiority of NodeDup. Additionally, NodeDup is a light plug-and-play method which is able to collaborate with almost all decoders and encoders for link prediction task.

### Strengths
S1: The cold-start problem towards graph data is meaningful and challenging, whose difficulty mainly lies on the isolated and low-degree nodes. The proposed method NodeDup succeeds in improving the prediction capability on the cold node, without damage to the overall performance at meantime.
S2: Extensive experiments are conducted. The ablation study on duplication times and nodes facilitates the understanding of when NodeDup is effective.
S3: The compatibility of NodeDup is exceptional. The prediction capability consistently outperforms different types of baselines, when combines with GraphSAGE, GAT, and JKNet encoders.

### Weaknesses
W1: The major concern is the definition of cold nodes or long-tailed nodes. (1) After checking the paper several times, I am quite surprised to see that the threshold lambda is set to 2 over all datasets. Considering the difference of number of nodes/edges/communities/densities in different graphs, it would be much better if authors could carefully define and investigate the definition of code nodes. Specifically, the impact of varying this threshold on the performance of NodeDup should be explored. A fixed threshold across diverse datasets seems overly simplistic and may not capture the nuances of cold nodes in each graph. (2) I am wondering whether it is proper to define code nodes based on the 1-st order degree instead of high-order connectivity. For example, given two nodes: m has 2 connected neighbors but has 200 two-hop neighbors while n has 10 connected neighbors but only has 10 two-hop neighbors. Based on hop-wise message passing used in GNNs, I think node m would attend to more neighborhood information, while node n might be more cold. Hence, it would be much better if authors could explain more on the definition of cold nodes. The current definition, relying solely on direct neighbors, might not accurately reflect the information scarcity experienced by nodes in a graph, particularly when considering the influence of higher-order neighbors.

W2: Based on the claim in the introduction: they are under-represented in standard supervised LP training due to their few (if any) connections, a straightforward strategy is to change the distribution of node sampling to ensure more tail nodes could join the training process. In my humble opinion, as NODEDUP only duplicate code nodes and connected them to the original ones, it essentially only changes the distribution of batch sampling. I notice that in E.3, authors only present the performance compared with upsampling, while the discussions of experimental results are missing. It would be much better to clarify the reasons why NODEDUP is effective instead of numbers. The paper needs a more thorough analysis of why simply duplicating nodes and connecting them back to the originals leads to improved performance, beyond just altering the sampling distribution. The mechanism by which this duplication provides a more effective learning signal needs to be more clearly articulated.

W3: Another concern is the baselines. First, the old-fashioned link prediction baselines are missing, including but not limited to common neighbors (CN), Jaccard, preferential attachment (PA), Adamic-Adar (AA), resource allocation (RA), Katz, PageRank (PR), and SimRank (SR). (2) Some SOTA models are also needed such as SEAL (Link Prediction Based on Graph Neural Networks). (3) The studied problem is similar to the degree-bias in GNNs. Please consider to add baselines such as `` On Generalized Degree Fairness in Graph Neural Networks’’.

### Questions
Q1: What is the key innovation of NodeDup? According to the manuscript, it seems that NodeDup is almost the standard node duplicate technique. More discussions about the existing node duplicate works are recommended.
Q2: What is the main difference between NodeDup(L) and self-loop in GNN? During the experiment, does the GraphSAGE (and GAT, JKNet) baseline introduce self-loop process? If no, the authors may want to add more experimental explanations. If yes, why NodeDup(L) is more effective than vanilla GNN models?
Q3: Why NodeDup(L) is more effective than NodeDup towards warm nodes in almost all scenarios? From my perspective, the two methods conduct the same operation on the warm nodes. The authors may want to add more discussions.
Q4: In light of the similarity to self-distillation mentioned in section 3.3, the comparison between NodeDup and self-distillation technique is recommended.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose to improve cold-start link prediction performance by duplicating tail nodes in the graph. Besides, they present NodeDup (L) that reduces duplicated nodes by self-loops to speed up the learning process. The experiments on several benchmark datasets demonstrate that the proposed method can serve as a plug-and-play approach to improve conventional GNN methods in link prediction. The authors also conduct several experiments to show that the comparisons in effectiveness and efficiency with other cold-start and augmentation methods.

### Strengths
* S1: The proposed method is simple and easy to be applied to arbitrary methods.

* S2: Compared to conventional cold-start methods, the proposed method achieves better performance in link prediction.

* S3: The authors conducted several ablation studies to demonstrate the effectiveness and efficiency of the proposed method in different settings and scenarios.

### Weaknesses
 * W1: The whole idea of the paper is about self-augmentation while the addition of self-loops (i.e., NodeDup (L)) would be a nature form without increasing model parameters. However, augmentation and adding self-loops are not novel in either link prediction [a, b, c, d].

* W2: The experimental settings are problematic. The authors randomly sampled nodes as negative references, but the setup is unrealistic while those references would almost be easy negatives. All of the remaining nodes should be considered as ranking candidates. 

* W3: Many performance metrics are inconsistent or contradict with existing studies.

* W4: Large-scale datasets are not included in the experiments. 

* W5: Some minor writing flaws exist, such as inconsistent terms without citing each other like inductive and production settings.

### Questions
* Q1: The improvements reported in the paper are astonishing. I wonder if the authors conduct any significance test on the improvements and the corresponding confidence levels, especially for the isolated and low-degree cases.

* Q2: Following Q1, it is surprising that all categories of nodes get benefited a lot after duplicating (or adding self-loops for) cold nodes. 

* Q3: Compared to Hits@10, Hits@1 could be more critical in the real-world applications, especially for tail nodes with very few neighbors. I wonder if the authors can also provide the Hits@1 performance.

* Q4: Following W2, the authors should consider conducting a set of experiments using all remaining nodes as candidates for link prediction, thereby alleviating the bias on easy negatives and achieving more fair comparisons.

* Q5: Following W3, I wonder why so many reported metrics are contradict with existing studies. For instance, Cold-brew even underperforms the original GSage across all metrics on Cora/Citeseer and most of metrics on other datasets in Table 1. As the authors do not use the identical setup and data partitions to previous studies, it should be better to have some elaboration on this part.

* Q6: Following W4, in Appendix C, the authors claimed some reasons to not conduct experiments on some large-scale graphs. However, given the improvements on all node categories, I believe it is still worth to verify the performance on the large-scale datasets. Besides, `IGB` is not really *large-scale* while some datasets like `ogbn-products` and `ogbn-papers100M` have millions or handred millions of nodes.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article proposes an augmentation technique to improve the performance of GNNs on low-degree nodes and observes that cold node LP performance typically suffers because they have too few connections resulting in underrepresentation in LP training. This article proposes the NODEDUP method, which utilizes a multi-view approach to improve the fitting of cold node nodes.

### Strengths
1. This method improves the performance of cold nodes without affecting warm nodes, which is a good improvement for the overall results.
2.  A multi-view method is proposed to enhance the fitting of cold nodes during model training. Through a large number of experiments, it is proved that this method can improve the performance of three kinds of nodes.
3. NODEDUP can be easily combined with the GNNs model, which is very inspiring for the subsequent work.

### Weaknesses
1. There are some spelling and grammar problems in the article, please pay attention to check.
2. In the analysis of the same type of augmentation methods, the reasons for the performance improvement can be analyzed in depth. 
3. More case studies for low-degree nodes are needed. Why such augmentation is really meaningful but fitting.

### Questions
1. Why such augmentation is really meaningful but fitting in this task?
2. GNNs have a hard time achieving good results on low-degree nodes. This may not always be true. Justify it more clearly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
