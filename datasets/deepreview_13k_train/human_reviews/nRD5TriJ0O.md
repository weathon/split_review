# Know Your Neighbors: Subgraph Importance Sampling for Heterophilic Graph Active Learning

- Decision: Reject
- Scores: 6, 5, 1, 5, 6

## Abstract
Graph neural networks (GNNs) have shown superiority in various data mining tasks but rely heavily on extensively labeled nodes. To improve the training efficiency and select the most valuable nodes as the training set, graph active learning (GAL) has gained much attention. However, previous GAL methods are designed for homophilic graphs, and their effectiveness on heterophilic graphs is less examined. In this paper, we study active learning on heterophilic graphs, where nodes with the same labels are less likely to be connected. We are surprised to find that *previous GAL methods fail to outperform the naive random sampling on heterophilic graphs*. Through an insightful investigation, we find that previous GAL-selected training sets imply homophily even on heterophilic graphs, leading to their defectiveness. To address this issue, we propose the principle of *``Know Your Neighbors''* and design an active learning algorithm KyN specifically for heterophilic graphs. The primary idea of KyN is to let GNNs receive a correct homophily distribution by labeling nodes along with their neighbors. We build KyN based on subgraph sampling with probabilities proportional to $\ell_1$ Lewis weights, which has a solid theoretical guarantee. The effectiveness of KyN is evaluated on various real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the reason for the failure of active learning on heterophilic graphs -- selected sets show homophily. They argue that this is because nodes are queried without knowing neighbors, leading to isolated and homophilic nodes. With this motivation, they propose partitioning nodes into subgraph groups and designing representation using the Jordan Center. Through sampling subgraphs with probabilities proportional to l1 Lewis weights and adding all nodes in subgraphs to the training set, this paper provides guarantees over the gap between the objective function of the training set and the overall graph.

### Strengths
- The presentation and storytelling of this paper are smooth and attractive. 
- The phenomenon of GAL failing in heterogeneous graphs is first revealed and researched.
- Experiment result improvements are significant and convincing.

### Weaknesses
 - Please see questions.
- To support your claim, it would be better to provide a case study figure over selected nodes for different methods on a small graph, besides a toy example.

### Questions
- In Tab 1. Texas 20C, Uncertainty reaches 94.7 ± 1.4, while KyN is 93.2 ± 1.6. Is it a typo?
- In line 185: "When fed to GNNs, these isolated nodes are viewed as strongly homophilic nodes...". Can you clarify if it is true only for normal homophily-based GNNs, or the same for heterogeneous GNNs?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses graph active learning (GAL) on heterophilic graphs, a previously unexplored perspective. The authors argue that existing GAL methods underperform on heterophilic graphs due to their inability to preserve ground-truth local homophily distributions in the selected training set. To address this limitation, they propose selecting nodes along with their neighbors as the training set to better capture local homophily distribution. The proposed method, KyN, first clusters the input graph using METIS and identifies Jordan centers for each cluster. Cluster-level features are then constructed by concatenating center features with aggregated neighbor features. Clusters are subsequently sampled and labeled according to $\ell_1$ Lewis weights. Experimental results demonstrate the effectiveness of KyN on real-world homophilic graphs.

### Strengths
**S1**: The paper addresses an important gap in GAL research by focusing on homophilic graphs.

**S2**: The authors provide a novel perspective on why existing GAL methods fail on homophilic graphs, attributing it to inconsistencies in local homophily distribution estimation.

**S3**: The proposed method offers a simple, efficient solution by preserving ground-truth homophily degree through neighbor-aware labeling, demonstrating effectiveness across six real-world datasets.

### Weaknesses
**W1**: The central argument in this paper regarding the limitations of existing Graph Active Learning (GAL) methods lacks comprehensive empirical validation. The experimental methodology omits crucial details, particularly regarding GNN backbones and configurations. To establish a more convincing foundation, the analysis should incorporate results from both heterophilic GNN and MLP backbones. This expansion would provide stronger evidence for the claimed deficiencies in current approaches and demonstrate the broad applicability of the proposed solution across different GNN backbones. Specifically, the authors should include experiments with GNN architectures designed for heterophilic graphs, such as FAGCN and H2GCN, as well as a standard MLP baseline. This would help determine whether the observed limitations are specific to certain GNN types or a more general issue in GAL.

**W2**: The key insight behind the proposed method requires further elaboration. While the authors claim that labeling subgraphs better captures local homophily distribution, the mechanism by which this information enhances GNN performance remains unclear. The manuscript should explicitly address several key questions. How does the degree of local homophily influence GNN behavior? What specific advantages does this approach offer for fundamental homophily and heterophily GNNs? A detailed theoretical analysis would strengthen the paper's contribution and provide valuable insights for future research directions. For instance, providing a theoretical connection between the proposed subgraph sampling strategy and the optimization landscape of GNNs on heterophilic graphs would be beneficial.

**W3**: The experimental evaluation requires substantial enhancement in multiple dimensions:
- Comprehensive evaluation across diverse backbone architectures, specifically including heterophily GNN and MLP variants.
- Validation on large-scale datasets to substantiate efficiency claims and demonstrate practical applicability. The current datasets are relatively small, and testing on larger graphs like OGBN-Arxiv or Snap-Patents would provide a more realistic assessment of the method's scalability.
- Detailed ablation studies to isolate the impact of individual components. For example, comparing the performance with and without importance sampling, or with different feature concatenation strategies, would help understand the contribution of each element of the proposed method.

**W4**: The presentation requires significant improvement. The core principle of "know your neighbor" lacks precise definition and theoretical grounding. The relationship between local homophily distribution and active learning effectiveness requires clearer articulation. A substantial revision would enhance readability and impact. For example, formally defining the "know your neighbor" principle using graph-theoretic concepts and providing a mathematical formulation of how local homophily is captured and utilized would significantly improve clarity.

Overall, although heterophilic GAL presents an interesting research direction, the current manuscript has significant limitations in motivation evidence (W1), key insight (W2), experimental validation (W3), and presentation (W4).

### Questions
**Q1**: The experimental setup in Table 1 requires clarification regarding the feature combination mechanism in the backbone GNN. How are neighbor-aggregated features combined with target node features? Does the choice of combination method impact performance significantly?

**Q2**: The ablation study section requires expansion to validate the contribution of key components. How does the method perform when $\ell_1$ loss weights are excluded, such as in the case of randomly sampling a subgraph? What impact does the removal of concatenation operations from Equation (6) have on the model performance?

**Q3**: The experimental analysis in Figure 1 should be expanded, for example, by extending the labeling budget range to start from 2c to align with the standard GAL setting.

**Q4**: What is the performance comparison with a *sample-then-$k$-hop* approach? The terminology also needs revision (*sample* as verb vs. *k-hop* as noun).

**Q5**: How are node selections made when selected subgraphs exceed the budget? For example, the current budget is 2 and the selected subgraph contains 5 nodes, what selection criteria are applied?

**Q6**: Please supplement the $\ell_1$ Lewis weights computation algorithm and time complexity analysis.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper tried to bring attention to graph active learning for heterophilic graphs by making several claims that are not prudent as pointed out in the weaknesses. To conclude, the paper lacks severely on the experimentation and also on the way it has been conducted. Moreover the absolute improvements in results are just marginal, calculating percentages just inflates these values. Most importantly, the claims made in the paper are unjustified.

### Strengths
1.) The paper presents a technique for Graph Active Learning (GAL) where it samples subgraphs based on Lewis weights sampling by using them as probabilities and name it as “Know your Neighbors”.

2.) The paper claims to “investigate a new research problem, heterophilic graph active learning”. Although it is not correct as discussed below.

### Weaknesses
1.) The basic premise of the paper, i.e., the claim “previous GAL methods fail to outperform the naive random sampling on heterophilic graphs” is not substantial. Out the 6 reported heterophilic datasets, only for Roman-empire dataset, random sampling is better than the previous GAL methods, and for Minesweeper dataset, it is almost similar. So, this blanket statement should not have been made.

2.) It is not just the homophily that influences the performance of any GNN on a given graph but many other network properties and also the data split ratio and the random seed. Moreover, the definition of homophily itself is not just limited to node homophily and the edge homophily which the authors have referred to as local homophily and global homophily respectively, but many other homophily measures like improved homophily [1], adjusted homophily [2], effective homophily [3] and aggregated homophily [4]. When you take the average of homophily for all the nodes in the graph it becomes a global measure, i.e., node homophily, so referring to it as local homophily is not appropriate. The authors are suggested to incorporate these additional measures to have a better clarity.

3.) The authors have just shown the homophily distribution (just the local homophily) plot in Fig.2 only for one dataset and inferred and made a claim that “previous GAL methods provide wrong, even opposite, information in the first place”. If we are to go by this claim, the results of previous GAL methods would yield gibberish which it is clearly not. I strongly recommend the authors to moderate their writing regarding the performance of previous GAL methods and provide more nuanced analysis instead of making harsh claims. The authors should provide homophily distribution plots for all other datasets as well to make their point.

4.) Also, for homophily calculations, you do not use the node itself resulting in a self loop. It is wrong, c.f. 183-189 that also forms the base of deriving the proposed technique. Moreover, it raises a serious question on the validity of the homophily distribution plot in Fig.2 that for the majority of the nodes selected through GAL which are isolated, value of local homophily of 1 is assumed.

5.) The paper talks about graph partitioning as the primary step and chooses METIS algorithm for the rest of the work. Why? It is a building block of the proposed technique, atleast a few different graph clustering/partitioning algorithms should have been discussed and experimented with.

6.) Similarly, for graph aggregation, GraphSAGE has been used which is again a rudimentary method just like the above chosen METIS.

7.) The statement “We want to point out that GAL methods can be used with all previously mentioned GNNs that designed for heterophilic graphs. We omit such combinations without loss of generality.” is troublesome. Solid experimentation needs to be performed to arrive at this claim and I suggest authors to provide extensive empirical evidence to support this claim.

8.) In Table1, the values for Average improvement correspond to which of the mentioned baselines? Is it with respect to the second best result?

9.) By the very principle of the proposed technique, it should work perfectly for homophilic graphs. Why is there no such discussion and the corresponding results?

10.) The two statements “We observe that KyN is robust to the choice of c.” and “This is normal since we do not tune c with the final accuracy to avoid data leakage.” are problematic. For many of the datasets, the accuracy fluctuates significantly by almost 10 absolute points, so how is KyN robust to the choice of c? Ofcourse, one does not tune hyperparameter with the final accuracy to avoid data leakage on the test set but it has to be done on the validation set. I recommend the authors to clarify their hyperparameter tuning process, particularly regarding the use of a validation set.

11.) The statement “In practice, we recommend choosing c around |V |/C , where C is the number of classes.”, what is the basis of the given statement?

12.) There are slight grammatical mistakes like “theoratical” in line 266 etc.

### Questions
Please see above in the weaknesses section.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The KYN model (Know Your Neighbors) is designed to address the limitations of traditional Graph Neural Networks (GNNs) in handling heterophilic graphs (graphs where nodes with the same labels are less likely to be connected). While existing Graph Active Learning (GAL) methods work well on homophilic graphs (where similar nodes are connected), they perform poorly on heterophilic graphs, often even worse than random sampling. The KYN model introduces a novel approach to solve this problem.And through theoretical analysis and experiments to demonstrate the effectiveness and superiority of the model.

### Strengths
1. The "Know Your Neighbors" approach is innovative and ensures that nodes and their neighbors are labeled together, providing GNNs with the correct local homophily distribution. This method may significantly enhance the learning performance on heterophilic graphs
2. Subgraph importance sampling: By leveraging ℓ1 Lewis weights (which offers theoretical guarantees for the quality of the sampled subgraphs.)for subgraph sampling, my understanding is that KYN selects subgraphs that are most informative, reducing the risk of overfitting to uninformative nodes and ensuring that the labeled nodes provide useful information for training. 
3. The theoretical guarantee proves the rationality and effectiveness of sampling strategy based on ℓ1 Lewis weight in graph learning; analyzes the influence of subgraph division and subgraph embedding strategy on node classification task in heterograph; and explains the advantages of separating self-embedding and neighbor embedding for model processing of heterograph.

### Weaknesses
1. The quality of subgraph division depends on the clustering algorithm: KYN uses a graph clustering algorithm (such as METIS) to divide subgraphs, and the performance and effect of these clustering algorithms directly affect the representation of subgraph and subsequent model training. If the clustering results are not of high quality, it may lead to the subgraph internal structure is not compact, which will affect the overall model performance. I think it is necessary to further discuss the performance of the clustering algorithm used in the partition subgraphs.
2. Lack of clear description of the algorithm steps: When introducing the execution steps of KYN model, there may be some operational details not detailed, especially some key processes (such as specific implementation of subgraph division, calculation of Lewis weight, etc.) without clear pseudo code or algorithm block diagram. This may leave the reader for difficulty in actually reproducing or understanding the algorithm.
3. Insufficient explanation of the dataset: When introducing the dataset used for the experiment, the article does not fully explain the structure, characteristics, and the degree of graph heterogeneity of each dataset. This information is essential for understanding the experimental results as well as the applicability of KYN.
In addition, to further verify the robustness of the KYN model, experiments may be conducted on more graph types, such as:Large-scale graphs、Dynamic graphs、graphs with different connection densities.
4. A small detail problem, when Texas data set 20C, Uncertainty (the second row in the table) corresponds to the best result, not KyN

### Questions
See the above weakness

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work points out the limitation of previous Graph Active Learning (GAL), which mainly focused on the homophilic graph. Consequently, they fail to outperform the naive random sampling algorithms, degrading the generalization ability of the GNNs. To solve this limitation, the author suggests a novel concept of "Know your neighbors" (KyN) with theoretical guarantee, which calculates $l_1$ Lewis weights and then samples the subgraph based on these probabilities. Extensive experiments on real-world datasets show the effectiveness of the proposed scheme.

### Strengths
**S1.** This work handles the limitation of GAL, which fail to perform well under heterophilic settings.

**S2.** The authors introduced some app appropriate examples, e.g., Figure 2 or 3, which helps to improve the readability of this paper.

**S3.** The proposed scheme (subgraph sampling with Lewis weight) has a fair theoretical guarantee.

### Weaknesses
 **W1.** The KyN primarily targets heterogeneous graphs, but it employs GraphSAGE as a baseline. Fundamentally, GraphSAGE utilizes a mean aggregator (aggregation with positive edge weights lead to node convergence), which is less effective for heterogeneous edges, and therefore, the KyN may enhance performance under such conditions. The key point is that if the KyN can demonstrate its capabilities when integrated with heterogeneous GNN algorithms [2, 3]. Since the KyN introduces additional computational costs, if it fails to improve the quality of these baselines, it is questionable whether to apply the proposed GAL method in this community.
  * [1]: Beyond low-frequency information in graph convolutional networks, AAAI '21
  * [2]: Finding global homophily in graph neural networks when meeting heterophily, NeurIPS '22

Q1) Could you please run the experiments using the heterophilic GNN algorithms as above?


**W2.** The experiments could be further enhanced. For instance, in Table 1, the author should consider incorporating more baselines, such as GreedyET, and evaluate the node classification accuracy as demonstrated in [1]. Moreover, the paper neglects to utilize widely employed homophilic networks (e.g., Cora, Citeseer, and PubMed). As illustrated in Figure 2, the proposed KyN exhibits poor performance under high local homophily (1.0). It would be beneficial to investigate these values under homophilic networks.
  * [3] Cost-effective data labeling for graph neural networks, WWW '24

Q2) Could you use more baselines (e.g., GreedyET) and run the experiments under benchmark homophilic graphs (Cora, ...) as well?

**W3.** As illustrated in Figure 2, most nodes are concentrated around a homophily ratio of 0.5, from which the sampled subgraphs will be drawn, and KyN utilizes all nodes within these networks for training. In Theorem 3.4, the author proves that the sampling error converges to the coreset, which is acceptable. However, it remains unclear how the sampled subgraphs with low homophily (less than 0.5) contribute to enhancing the overall performance. Specifically, what happens if the homophily of most subgraphs is very low? According to [4,5], even low-homophily subgraphs can contribute to the node classification task by discovering patterns among neighboring nodes. Nevertheless, since KyN employs GraphSAGE, which involves positive message-passing, the neighboring nodes are smoothed during aggregation rather than being separated. Consequently, for KyN to improve classification accuracy, the sampled subgraphs with the same homophily ratio should ideally share the same class distribution, which may not be feasible. 

  * [4] Is Heterophily A Real Nightmare For Graph Neural Networks To Do Node Classification?, arXiv '20
  * [5] Beyond homophily in graph neural networks: Current limitations and effective designs, NeurIPS '20

Q3) Could you provide a theoretical guarantee that the sampled subgraphs can still contribute to the overall performance despite having a low homophily ratio?

### Questions
Please refer to the weaknesses above

### Soundness
3

### Presentation
3

### Contribution
2
