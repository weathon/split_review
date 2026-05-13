# SheAttack: A Silhouette Score Motivated Restricted Black-Box Attack on Graphs

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Graph Neural Networks (GNNs) have gained large popularity in various applications, with their vulnerability against adversarial attacks also being brought up.
Despite the numerous graph attacks proposed, few have focused on the Restrict Black-box attack, where attackers only have access to node features and the graph structure.
Existing works in this setting aim to perform destructive attacks by degrading the quality of victim graphs yet imposing the homophily assumption or requiring high computational complexity. 
To address these challenges, we propose the Modified Silhouette Score (MSS) as a measure of a graph's quality, and demonstrate its generalizability across graphs of different homophily levels through theoretical analysis. 
Using MSS as the objective, we present SheAttack, an efficient attack that effectively reduces the distinguishability of nodes.
We conduct experiments on both synthetic and real-world graphs to validate the effectiveness of SheAttack in both homophilic and heterophilic settings.
We find that even without prior knowledge of labels or the victim model, our method shows comparable performance to split-unknown white-box attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the restricted black-box attack scenario where attackers only have access to node features and the graph structure. To solve this problem, the authors introduce the Modified Silhouette Score (MMS) to measure a graph’s quality and propose a Silhouette score-based attack. Extensive experiments are conducted.

### Strengths
1. The studied restricted black-box attack is a practical scenario and an important problem.
2. The motivation of this paper is clear and the idea of introducing the Silhouette Score to measure the quality of a graph is interesting.
3. Extensive experiments are conducted.

### Weaknesses
1. The proposed SheAttack depends on various hyper-parameters, which may significantly affect the performance of the proposed method and lack detailed theoretical support or empirical analysis. For example, the number of clusters $k$, the propagation layer/time on the adjacency matrix, and the $\lambda$ that balance the Shift Loss and Silhouette Score-based Loss. The sensitivity of the method to these parameters is not thoroughly explored, and the current justification for their selection seems insufficient. Specifically, the impact of varying $k$ on the quality of the clusters and the subsequent attack effectiveness is unclear. Similarly, the choice of propagation layers/time needs more justification, as it directly influences the information diffusion within the graph and thus the attack surface. The lack of theoretical grounding for these choices raises concerns about the method's robustness and generalizability.
2. The proposed method does not seem to be consistently effective in all scenarios in Tables 1&3. The performance fluctuations across different datasets and attack settings (evasion vs. poisoning) suggest that the method might be sensitive to specific graph properties or victim model architectures. For example, the method's performance on homophilic graphs compared to heterophilic graphs needs further investigation. It is not clear why the method performs well in some cases but not in others, and this inconsistency raises concerns about the method's reliability. A more in-depth analysis of the method's behavior under different graph characteristics is necessary.
3. The writing of this paper needs to be further improved. For example, the citation format of references in Introduction and Preliminaries seems strange. 'Aggreation function' should be 'Aggregation function’. The definition of poison attacks and evasion attacks on page 3 is confusing. The paper would benefit from a more precise and consistent use of terminology, and a clearer explanation of the different attack scenarios.

### Questions
1. In Figure 3, why do GRBCD and RandAttack show different Modified Silhouette Score at epoch 0?
2. How would the proposed method perform when the victim model is not a two-layer GNN? In other words, when the propagation layers/times in the proposed method and victim model are not the same, would the proposed method still be effective?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the problem of restrict black-box attacks (RBA) on GNNs. It first introduces the Silhouette Scores, which is used for quantifying the difficulty of a clustering problem, to the RBA attacks on GNNs. Then it introduces a RBA attack named SheAttack by minimizing the silhouette score of the graph. And a scalable version of SheAttack is also proposed for the large-scale graphs. The experimental results on homophily and heterophily graph benchmarks demonstrate its effectiveness compared to other RBA baselines.

### Strengths
1. This paper study the problem of restricted black-box attacks, which is both practical and noteworthy.
2. This proposed method is effective in both homophily and heterophily settings. And the scalable version of SheAttack can also work on the large-scale graphs.
3. The experimental results on both homophily and heterophily graphs show that SheAttack can outperform other RBA baselines.

### Weaknesses
1. Although the authors include the experimental results on large-scale graphs, the comparison between SheAttack and some existing powerful baselines, such as PRBCD, on the large-scale graphs is missing.
2. In this paper, the authors highlight that SheAttack is applicable to the heterophilic settings while existing RBA methods cannot. However, I think it would be better if some robust GNNs for heterophily graphs can be included during the comparison, such as [1]. 
3. I recommend the authors can include the comparison of the running time among different methods to verify the efficiency of SheAttack.

### Questions
1.	Could you please provide some comparisons between PRBCD/PRBCD-shuffle with SheAttack on large-scale graphs? 
2.	Please add the experimental results of SheAttack against RobustGNN for heterophily graphs.
3.	Please include the comparison of running time among different methods.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a new black box attack on the graph structure that uses a variant of the silhouette score as one component of the attacker's loss. This captures distances between intra-class/cluster and inter-class/cluster instances and reflects the difficulty of the classification problem. The authors argue that this loss is agnostic to whether the graph is homophilic or heterophilic. Their attack does not require knowledge of the node labels.

### Strengths
The theoretical insights are interesting even though they rely on several simplifying assumptions.

The attack can scale to larger graphs such as ogbn-arxiv and ogbn-products.

The black box threat model is relevant and interesting to study but has received relatively less attention in the past.

### Weaknesses
The threat model only enforces a global budget, and completely ignores any local constraints e.g. w.r.t. the degree of the nodes. This is likely to lead to unrealistic and noticeable attacks. While the authors perform an empirical analysis in section G and conclude that "unnoticability of SheAttack is in an acceptable range." I do not necessarily agree. First, the averaged results in Table 22 can be misleading since there is likely a big skew in the distribution of changes, and second the mean values are already large.

The experimental evaluation focuses on a fixed perturbation ratio (mostly 0.2 and sometimes 0.1) which can be considered unrealistically large. An in-depth ablation study w.r.t. different perturbation budgets is missing.

The paper would benefit from formalizing and describing the threat model in much more detail. For example, the authors state "only training inputs excluding node labels, are known to attackers." Does this mean that the attacker also does not have access to the training node labels. I assume that this is the case. If yes, a reasonable baseline would be to compare previous (adaptive) attacks [1] using clusters as a surrogate for labels.

If I am wrong and the attacker does have access to training node labels, then they can train a surrogate and use the predictions for the test labels (instead of true labels) which is likely to work much better than using the unsupervised clusters, and likely also better than using "node embeddings generated by supervised GCN as input to generate clusters".

### Questions
1. How does the attack peform when introducing local budget constraints (e.g. relative to the node degree)?
2. How does the attack compare to an attack where instead of the true labels we use the predictions from the victim model?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new method, SheAttack, for attacking Graph Neural Networks (GNNs) in the Restrict Black-box attack setting. This method aims to diminish the quality of graph data by manipulating node distinguishability. The approach utilizes a Modified Silhouette Score (MSS) to assess graph quality across various homophily levels. Experiments show that SheAttack performs effectively on both homophilic and heterophilic graphs and offers comparable results to more knowledge-intensive white-box attacks.

### Strengths
**Clarity**: The paper is well written and clear to understand.

**Quality**: The assumptions made about real-world scenarios and RBA are well-considered.

**Significance**: The problem addressed is significant due to the growing need to detect vulnerabilities in graph neural network models. The problem setting in this paper (RBA) seems more aligned with real-world scenarios compared to white-box and grey-box attacks.

### Weaknesses
 * The attack proposed relies heavily on node features to achieve a quality cluster to replace ground-truth labels when calculating the Silhouette score. This dependence is a significant vulnerability. If one adds noise to features and incorporates a de-noising mechanism within the base model, the attack's efficacy could be undermined since the attacker wouldn't know about the noise or how to de-noise the features.

* Given that the attacker has access to node features, it might be more impactful to target both the structure and features. Not leveraging this information seems like a missed opportunity.

* The attack lacks a theoretical foundation; it's mainly empirical. There are no guarantees about the efficacy of the attack.

* The paper seems to have limited novelty. The idea of using clustering due to the absence of label information in RBA and the shift loss has been previously explored. The primary innovation appears to be the modification of the Silhouette score, which has its challenges.

* In Section 3.2, the authors propose modifications in $a$ and $b$ to accommodate the absence of ground-truth labels. However, the later modifications in $b$ do not address the issue of pushing nodes of different classes further apart.

* The parameter $\Delta$ plays a significant role in the problem definition (Section 2), yet it isn't discussed in the methodology or experiment sections. It's unclear how much perturbation is excessive or how this was determined and verified.

* Please ensure notation consistency. In Section 2, both notations $f_\theta(X;A)$ and $f_\theta(X,A)$ are used.

* The related work section mentions interesting algorithms not used as benchmarks. Specifically, the absence of some RL-based methods was noticeable. Why were they excluded? Modifications to the benchmark could also be applied to other methods.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
