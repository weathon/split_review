# Label Informativeness-based Minority Oversampling in Graphs (LIMO)

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 6, 3, 5, 5

## Abstract
Class imbalance is a pervasive issue in many real-world datasets, particularly in graph-structured data, where certain classes are significantly underrepresented. This imbalance can severely impact the performance of Graph Neural Networks (GNNs), leading to biased learning or over-fitting. The existing oversampling techniques often overlook the intrinsic properties of graphs, such as Label Informativeness (LI), which measures the amount of information a neighbor's label provides about a node's label. To address this, we propose Label Informativeness-based Minority Oversampling (LIMO), a novel algorithm that strategically oversamples minority class nodes by augmenting edges to maximize LI. This technique generates a balanced, synthetic graph that enhances GNN performance without significantly increasing data volume. Our theoretical analysis shows that the effectiveness of GNNs is directly proportional to label informativeness, with mutual information as a mediator. Additionally, we provide insights into how variations in the number of inter-class edges influence the LI by analyzing its derivative. Experimental results on various homophilous and heterophilous benchmark datasets demonstrate the effectiveness of LIMO in improving the performance of node classification for different imbalance ratios, with particularly significant improvements observed in heterophilous graph datasets. Our code is available at \url{https://anonymous.4open.science/r/limo-12CC/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an oversampling technique for imbalance classification in graph classification settings. The method is based on the label informativeness as the criteria to augment the minority class samples. The method started with the regular non-graph SMOTE technique for generating new samples. Then it uses LI criteria to determine which nodes are connected to the new samples, in such a way that maximizes the LI criteria. The authors then demonstrate the performance of the proposed model in the real experiments.

### Strengths
1. Interesting ideas on using label informativeness to help tacking imbalance dataset.
2. The is built on top of SMOTE, a well known upsampling technique, and augment it to graph setting.
3. The experiments demonstrate the claimed benefit of the proposed approach.

### Weaknesses
1. Presentation. In many places, terminologies/abbreviations/symbols/equations are used without explaining them. For examples:
    - “IR”. (Page 2)
    - “SMOTE”. (Page 3)
    - “Eq (6)”. (Page 4)
    - “Eq (7)”. (Page 4)
    - etc
2. Motivation. The motivation behind using LI for upsampling is not explained clearly. Why is using LI a good idea to do upsampling? Why is having high LIs desirable? etc.
3. Soundness. The data augmentation by creating new nodes with new features using SMOTE technique makes sense. However, the way the proposed method augments the edges by attaching the new nodes to potentially unrelated nodes (not a neighbor of the original node), does not necessarily make sense. I get that the goal is to improve the LI metric. However, edges in the original graph represent certain relationship patterns. Attaching the new nodes to unrelated nodes will create new relationship patterns that do not exist in the original graph. These relationship patterns in the graph are something that is not yet explored by the model.

### Questions
1. Please address the weaknesses mentioned above.
2. In the evaluation, is the accuracy of the prediction computed using the augmented graph (after upsampling), or is it just based on the original graph?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new method for resolving class imbalances in graph-structured data based on a labeled informativeness-based minority oversampling method, called LIMO. By increasing the edges in a way that maximizes the amount of label information, LIMO strategically samples nodes of minority classes. And satisfactory results are obtained in node categorization dataset.

### Strengths
1. The authors propose Label Informativeness-based Minority Oversampling and theoretically establish the relationship between label informativeness and model prediction accuracy in GNN.   
2. The authors analyze the effect of variation in the number of inter- and intra-class edges on LI.   
3. The manuscript is logical and well-structured. The methodology section is clearly presented.

### Weaknesses
1. At the end of the first section, the authors show LIMO only in the figure, but there is no corresponding textual description in the text.
2. The currently proposed Label Informativeness-based Minority Oversampling (LIMO) approach is indeed a novel idea to solve the graph imbalance problem, but the core differences with existing approaches can be further highlighted in the introduction section or related work section such as 10.1109/IJCNN60899.2024.10650494, 10.1109/ICASSP48485.2024.10448064.  
3. Discussion on the generalizability of LIMO is lacking in the manuscript, the authors only validate the performance effect of LIMO in GraphSAGE and lack discussion on LIMO in other GNNs such as Graph Convolutional Networks (GCN), Graph Attention Networks (GAT/ GAN). The authors need to provide a theoretical discussion of how LIMO might be generalized to other GNN architectures, or validated experimentally.  
4. The experimental results are not comprehensive enough, and oversampling methods that specifically address the problem of graph data imbalance are missing from the comparison methods. Therefore, it is suggested that the authors should add methods that target graph data correlation in the experimental section, e.g., 10.1109/IJCNN60899.2024.10650494, 10.1109/ICASSP48485.2024.10448064.
5. Although the authors mention the inherent cost of the LIMO approach in generating and evaluating new edges in the summary section, the authors do not mention whether the added computational cost is within an acceptable range. The authors should provide actual runtime comparisons between LIMO and baseline methods, or a theoretical complexity analysis.

### Questions
1. Compared to existing oversampling methods based on graph data, what research gaps are addressed by the method proposed in this paper?  
2. The authors proved Theorem 1 in the manuscript. Still, I am more interested in whether the variation of t for different problems affects the results of the experiments and how the optimal value of t is determined.
3. Is there a generalization of sacrificing significant computational cost to improve computational accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To alleviate the class-imbalanced issue, this paper propose a novel algorithm,  Label Informativeness-based Minority Oversampling (LIMO), aiming to strategically synthesize minority nodes by augmenting edges to maximize label informativeness. And the experiments conducted on various homophilous and heterophilous benchmark datasets show the improvements compared with the baselines.

### Strengths
1. The paper is easy-to-follow.

### Weaknesses
1. The novelty is limited. It seems just simply inject SMOTE with label informativeness, however, the label informativeness is borrowed from previous work without clear explanation. Specifically, what is the meaning of the definition of LI in Eq.2? What situation will the LI(G) increase? And when will LI(G) decrease? More importantly, how does LI(G) influence the performance of class-imbalanced learning?

2. This paper fails to demonstrate its strengths compared with previous works. In lines 81-87, the authors claim that the proposed method take label informativeness to handle class-imbalanced issue. But  they fail to illustrate the limitations of previous works, and how the proposed method can tackle the limitations? Why does the previous works, like GraphSMOTE [1], GraphENS[2] and TAM[3], can not improve the label informativeness? What is the strengths of LIMO compared with these methods?

3. In line 152, during the node generation, LIMO need to find "its nearest neighbor $u$ in the same class". Does node $u$ belong to the labeled training set or the unlabeled nodes? If it comes from the training set, will it lead to overfitting when the number of minority classes is too small? If $u$ is an unlabeled node, how to get a reliable pseudo-label in the class-imbalanced scenario?

4. Lack of complexity analysis of the proposed method. In lines 11-13 of Algorithm 1, for each minority node $v$, LIMO need to determine the edge between $s$ and $w$, and $w \in \mathcal{V}-\{v\}$. The computation cost seems pretty high.

5. In line 216, "Specifically, it suggests that enhancing the connectivity between classes (increasing inter-class edges) can improve the informativeness of the labels". This conclusion seems to contradict graph homophily  [4] (the foundation of GNN), i.e., the connected nodes often come from the same class. In my opinion, we always want to add edges between two nodes from the same class, so that the nodes can aggregate more information from the same class, thus helping the node classification, just like GraphSMOTE[1] does. I have some doubt about the conclusion of line 216.

6. In addition, the baselines is out-of-date, there are many related works should be taken into comparison, for example, the oversampling methods like GraphENS[2] and GraphSHA[5], the pseudo-labeling method like GraphSR[6] and the loss adjustment method TAM[3].  The experimental setup is inappropriate.  In line 729, "When the minority class had fewer than three nodes, we allocated one node each for training, validation, and testing.",  It is unreasonable to have only one node for validation and testing. Why is the experimental setting not consistent with the previous method?

### Questions
See weakness.

### Soundness
2

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
4

### Summary
This paper presents LIMO, an algorithm designed to tackle class imbalance in graph data. It works by adding synthetic edges between minority class nodes to increase Label Informativeness. It aims to improve the performance of GNNs on imbalanced datasets without significantly increasing the volume of data. The authors provide theoretical analysis and experimental results, showing LIMO outperforms existing methods, especially on heterophilous graphs.

### Strengths
* The paper is well-written and easy to understand.
* The paper focuses on the problem of class imbalance, a critical issue in many real-world applications.
* Rich experiments have been conducted on a variety of datasets, examining different aspects.

### Weaknesses
 * The paper lacks a discussion of several recent and relevant baselines for addressing class imbalance in graphs. Notably, recent methods such as GraphENS [1], TAM [2], and GraphSHA [3] are not included in the experimental comparisons. This omission makes it difficult to assess the true novelty and effectiveness of LIMO compared to the state-of-the-art.
* The theoretical proof with t=1.31167628 is derived from simulation, but the paper does not provide a detailed explanation or justification of the simulation settings used. This lack of transparency, specifically regarding the data generation process and the parameters used in the simulation, limits the reliability and reproducibility of this theoretical result. The paper should include a thorough description of the simulation setup, including the number of trials, the distribution of the simulated data, and the rationale behind the chosen parameters.
* While the paper theoretically claims that LI is directly proportional to GNN accuracy, experimental results do not consistently support this. For instance, in Figure 9, the correlation between LI and accuracy weakens when added_fraction > 0.5, especially at fraction = 0.75, where no strong positive correlation is observed. This discrepancy suggests that the relationship between LI and accuracy might be more complex than the theoretical analysis suggests, and that other factors might be at play when adding a large fraction of edges.

### Questions
* In the experiments, what does the imbalance ratio represent specifically set within the range of 0.1 to 0.6?
* Different dataset seems to show different performance. For example, in Table 10 when imbalance ratio = 0.1/0.2, while the LI of LIMO is the largest, the performances of RW and GS are better. Why?
* The experiment results can be further explained. For instance, in Figures 5 and 10, no significant correlation is observed once the fraction exceeds 0.25. Additionally, in Table 8, when the imbalance ratio is set to 0.1, ACC and F1-Score remain the same across four baseline methods.
* It is unclear whether the effectiveness stems more from well-synthesized node features or from the generated edges. Which one is more important? What are the appropriate $\delta$ values for interpolating node features?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates class imbalanced graph representation learning, where certain classes have significantly fewer nodes. Ignoring such kind of information will result in biased learning or overfitting. The authors claim that existing oversampling techniques overlook the label informativeness of the graphs, which measures the amount of information regarding to its neighbor’s labels. To this end, the authors propose LIMO to oversample minority class nodes by maximizing LI. Synthetic node features are generated with SMOTE, then edges are added by analyzing the derivative of its LI. Comprehensive experiments on both homophilous and heterophilous datasets demonstrate that the proposed model can outperform recent baselines under different imbalance ratios.

### Strengths
1.	The paper is generally well-written and easy to understand, meanwhile, the results appear to be promising.

2.	Experiments are conducted on both homophilous and heterophilous datasets, which broadens its application. 

3.	Various ablation studies are given to show the impacts of the synthesized nodes and generated edges.

### Weaknesses
1.	The calculation of $t$ value given in Theorem 1 is not rigorous, since the authors explore it in a certain range using predefined steps, which might not be the optimal value. The proof of Theorem 2 is also not convincing. Specifically, the method for determining the optimal threshold $t$ for edge creation based on the derivative of Label Informativeness (LI) is not clearly justified. The authors mention exploring a range of values, but without a more principled approach, it's unclear if the selected value is truly optimal or if it significantly impacts the performance. Furthermore, the proof of Theorem 2 lacks sufficient detail, making it difficult to assess its validity.

2.	The chosen baselines are too old, and some key baselines are not discussed and compared, e.g., GraphENS, and GraphSHA, etc. The experimental evaluation would benefit from comparisons against more recent and state-of-the-art methods for class-imbalanced graph representation learning. The absence of comparisons with methods like GraphENS and GraphSHA, which directly address the issue of imbalanced node classification on graphs, makes it difficult to fully assess the proposed method's contribution.

3.	No time and space complexity analyses are given to show the efficiency of the proposed model.

4.	The authors claim that the proposed model does not significantly increase the data volume. However, the authors synthesize nodes and edges in the graph, which indeed increases the data volume.

5.	The caption in Figure 1 does not provide any information, and the authors did not cite references appropriately. For instance, SMOTE was not cited upon its first mention.

6.	What labels are used in the Amazon datasets? The original datasets do not include labels for the user nodes.

### Questions
1.	The calculation of $t$ value given in Theorem 1 is not rigorous, since the authors explore it in a certain range using predefined steps, which might not be the optimal value. The proof of Theorem 2 is also not convincing.

2.	The chosen baselines are too old, and some key baselines are not discussed and compared, e.g., GraphENS [1], and GraphSHA [2], etc.

3.	No time and space complexity analyses are given to show the efficiency of the proposed model. 

4.	The authors claim that the proposed model does not significantly increase the data volume. However, the authors synthesize nodes and edges in the graph, which indeed increases the data volume.

5.	The caption in Figure 1 does not provide any information, and the authors did not cite references appropriately. For instance, SMOTE was not cited upon its first mention. 

6.	What labels are used in the Amazon datasets? The original datasets do not include labels for the user nodes.


References:

[1] Park J, Song J, Yang E. Graphens: Neighbor-aware ego network synthesis for class-imbalanced node classification[C]//International conference on learning representations. 2021.

[2] Li W Z, Wang C D, Xiong H, et al. Graphsha: Synthesizing harder samples for class-imbalanced node classification[C]//Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023: 1328-1340.

### Soundness
2

### Presentation
2

### Contribution
2
