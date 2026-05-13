# GNNs Getting ComFy: Community and Feature Similarity Guided Rewiring

- Decision: Accept
- Scores: 3, 6, 6, 6

## Abstract
Maximizing the spectral gap through graph rewiring has been proposed to enhance the performance of message-passing graph neural networks (GNNs) by addressing over-squashing. However, as we show, minimizing the spectral gap can also improve generalization. To explain this, we analyze how rewiring can benefit GNNs within the context of stochastic block models. Since spectral gap optimization primarily influences community strength, it improves performance when the community structure aligns with node labels. Building on this insight, we propose three distinct rewiring strategies that explicitly target community structure, node labels, and their alignment: (a) community structure-based rewiring (ComMa), a more computationally efficient alternative to spectral gap optimization that achieves similar goals; (b) feature similarity-based rewiring (FeaSt), which focuses on maximizing global homophily; and (c) a hybrid approach (ComFy), which enhances local feature similarity while preserving community structure to optimize label-community alignment. Extensive experiments confirm the effectiveness of these strategies and support our theoretical insights.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
While the existing rewiring technique aims to maximize the spectral gap, this paper aims to minimize the spectral gap.
This paper explains the benefit of minimization through the example of a stochastic block model.
Based on the analysis, this paper proposed three rewiring strategies: comma, feast, and comfy.
This paper demonstrates the effectiveness of the proposed methods.

### Strengths
The extensive experimental results.

### Weaknesses
Thm. 1 seems to be very incremental; in which part do the authors claim the result is novel? The second eigenvalue of the Laplacian of the expected SMB is almost folklore.

Right below the Thm.1, the authors claim as follows; " increasing q and decreasing p increases the spectral gap but makes the community structure less pronounced, and vice versa"

However, if we believe that the spectral gap is proportional to q-p/q+p, the gap is larger when p=0.3 and q=0.0001 than when p=0.9 and q=0.1. However, it is intuitive that the former provides the more pronounced community structure, albeit the larger spectral gap. If the rest of the authors' observations are based on this result, how can I believe that the larger spectral gap is less pronounced community structure?

Thm. 2 seems that the features do not have assumption. However, its proof immediately assumes that the the feature follows normal distribution. Therefore, the proof of the Thm.2 seems  incomplete. 

In Sec. 3, the authors' proposed three algorithms based on the theoretical observations; however, I wasn't able to pull out which part of the algorithm reflects the theoretical observations. Part of which may be due to the algorithms are in Appendix, which also may be the major formatting issue of this paper. 

Since the theoretical results are not reliable, and the algorithmic improvement is unclear, I vote for rejection.

### Questions
See weakness section.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a hybrid graph rewiring method to increase classification performance on node-level classification tasks. Motivated by theoretical finidings on the planted partition model with features, the authors show that the desired edge addition and deletion strategies change deopending on whether the graph structure is homophilic or heterophilic and how strongly the targets are aligned with the structure of the graph. Therefore, the authors present ComFy, which performs the rewiring independently for each pair of communities thereby respecting the graph structure and more evenly spreading the edits over the graph.

### Strengths
- Good theoretical motivation through planted partition model.
- Extensive experiments on many benchmark datasets show the methods efficacy against the competition.

### Weaknesses
 - Comfy is actually missing from the main text - not only the algorithm but also a textual explanation is very lacking.
- Planted partition model with only 2 communities is very simple and does not reflect real-world datasets.
- The elected competitors are highly related to the proposed method. A More diverse competition would be beneficial.

### Questions
- How do the proposed methods scale with increasing graph size? (Computing pairwise feature similarity may already be a problem for large graphs.) Are there optimizations or approximations that can make them more efficient for large-scale graphs?
- How robust are these methods when dealing with noisy or incomplete data? Do they still perform well when node features or labels contain errors?
- How sensitive to hyperparameters are the models? Both concerning the buget for rewiring and the hyperparameters of the GCN?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors introduced three novel graph rewiring techniques designed to improve the performance of Graph Neural Networks by focusing on the alignment between the graph structure and the target task. Experiments confirm the effectiveness of these strategies and support theoretical insights.

### Strengths
(1) The author established a systematic theoretical framework through the Random Block Model and analyzed the impact of community strength and graph task alignment on GNN performance. To some extent this paper enriched relevant theoretical research.
(2) The proposed FeaSt and ComFy  integrate feature similarity into graph rewiring methods, exploring how to optimize the performance of GNN by considering node features.
(3) In addition to theoretical analysis, the paper also demonstrated the performance changes of GNN under different alignment levels of graph tasks by generating Random Block Model (SBM) graphs with different alignment levels. The proposed methods have a certain degree of scalability.

### Weaknesses
 (1) The article is mainly based on the Random Block Model (SBM) for theoretical analysis, but real-world graph data often has more complex structures and dynamic changes, and the assumptions of SBM may not fully capture these complexities. Specifically, the SBM assumes a clear community structure, which is often not the case in real-world networks where communities can be overlapping, hierarchical, or have varying densities. This limits the generalizability of the theoretical findings to more complex graph structures.
(2) The method proposed in the article does not clearly explain and analyze the impact of adding or removing edges on model performance. While the authors propose methods for adding or deleting edges based on feature similarity and community structure, the specific mechanisms through which these changes affect the information flow and node representations within the GNN are not thoroughly investigated. It remains unclear how these rewiring strategies interact with the GNN's message-passing mechanism.
(3) The article did not discuss in detail how the proposed rewiring strategy performs in situations where the community structure is unclear or there is some noise. The performance of community-based rewiring methods is likely to degrade when the underlying community structure is weak or noisy. The authors should provide a more detailed analysis of the robustness of their approach under such conditions, including a discussion of how the feature-based rewiring component interacts with the community-based component when community information is unreliable.

### Questions
(1) Could the authors further explain the setting of hyper-parameters, such as increasing or deleting the number of edges, and how it affects the performance of the model?

(2) Will the performance of ComFy strategy decrease due to the unclear structure of the original community? The authors should better discuss this situation.

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
The authors propose different network rewiring approaches as a preprocessing step to align network structure with downstream tasks. More specifically, they consider adding or removing edges guided by the network's community structure as determined through modularity maximisation with Louvain. They also consider adding and removing links guided by the nodes' attributes. This approach is guided by the idea of presenting graph neural networks, which use the network itself as their computation graph, with more meaningful edges. By doing so, the authors hope to combat issues such as oversmooting and squashing. They evaluate their approach empirically on a set of real-world networks with homophilic and heterophil link patterns. They achieve better node classification performance than some baselines on some of those networks.

I find the paper well written and easy to follow, however, there are a few points that remained unclear to me.

### Strengths
- The motivation behind the work is clear and the authors demonstrate that their contribution improves the performance on one downstream task, namely node classification.
- The authors' claims are supported with theorems, proofs and extensive empirical experiments.

### Weaknesses
 - Many results are presented in the paper, however, I find that it is not always clear what the specific message of each figure and table is. For example, I find that Fig. 1 does not have a strong message, and Fig. 5 could have been summarised more succinctly in a short paragraph.
- Only one downstream task is considered, namely node classification. Therefore, it remains unclear how the proposed approaches affect the performance in other tasks.
- While the proposed approach seems to improve node classification performance in some settings, I am concerned that this is only due to the fact that the authors essentially consider community detection, supported by modifying the network such that the communities become clearer. The rewiring process, particularly with ComMa, seems heavily biased towards enhancing the modularity of the graph, which inherently favors better performance on tasks that align with community structure. This raises concerns about the generalizability of the approach to scenarios where community structure is not a strong indicator of node labels.
- The authors' approach appears to rely on knowing the network's community structure, which is unknown in real-world networks. The use of the Louvain algorithm provides an estimate, but the quality of this estimate directly impacts the efficacy of the rewiring. The paper does not sufficiently address the sensitivity of the proposed methods to inaccuracies in community detection, which is a critical consideration for practical applications.



### Questions
- What task is actually considered in the paper? While the authors discuss node classification, it seems very close to community detection to me. In that case, I don't find it surprising that node classification performance improves as the network is modified such that community structure becomes stronger. Could the authors clarify how they are doing node classification? For example, is it done in a semi-supervised fashion where 80% of the nodes have labels and the remaining 20% should be predicted by the GCN, or similar? If that is so, are ground-truth labels required for the approach to work? If labels are not used and node classification is done in an unsupervised fashion, how is it different from community detection?
- What about using other GNN architectures besides GCN or other aggregation functions besides sum aggregation? Can we expect that the proposed rewiring approaches help in those settings or are they limited to GCN and sum aggregation? I would recommend trying other architectures such as GIN or SAGE, perhaps even a MLP to check whether the rewiring might make graph neural network superfluous.
- Is there a reason why NMI was used to measure the agreement between community structures and not AMI, which has become the preferred measure in network science because it adjusts for chance?
- If I understood correctly, rewiring with FeaSt is based on the assumption that there is a correlation between nodes' community memberships and their features. But what if this is not the case? In real-world networks, it could be that the "wrong" features have been recorded. Or more generally, how do you determine whether the nodes' features are informative? Is there perhaps a "simple test" that can tell the practitioner whether FeaST will work well for their data?
- Related to the previous question, it seems that, given that there is a strong correlation between nodes' community memberships and their features, ComMa and FeaSt should not be that different. Is that correct?
- Theorem 1 assumes an SBM with exactly two equally sized blocks. How does the theorem generalise to networks with more blocks that have different sizes? And how well does the proposed insight translate to real networks?
- In Fig. 4, do the point labels denote the number of added edges?
- I find that using the Louvain algorithm to detect communities might need some more motivation or at least a discussion of its limitations. For example, modularity maximisation suffers from the well-known resolution limit, which is often "addressed" by using a resolution parameter. How does this limitation affect ComMa and ComFy?
- I think a table summarising the used datasets' statistics should be included in the paper. As of now, it is unclear how large the large networks are.

Minor points
- I think there is a typo in line 182: "grain"
- The labels in Fig. 3b are somewhat messy and I would suggest cleaning them up a bit so that they don't overlap.
- I have a hard time imagining what the approximate proportion of misclassified nodes (Theorem 3) looks like. It would have been nice to see a plot.

### Soundness
2

### Presentation
3

### Contribution
2
