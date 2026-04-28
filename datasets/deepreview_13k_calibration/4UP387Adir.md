# Weakly Supervised Graph Contrastive Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Graph Contrastive Learning (GCL) has recently gained popularity owing to its ability to learn efficient node representations in a self-supervised manner. These representations are typically used to train a downstream classifier. In several real-world datasets, it is difficult to acquire sufficient clean labels for classification and instead we have weak or noisy labels available. There is little known about the robustness of the node representations learnt by the current GCL methods in the presence of weak labels.
Moreover, GCL has been successfully adapted to a supervised setting where class labels are used to contrast between pairs of nodes. 
Can weak labels similarly be leveraged to learn better node embeddings? In this paper, we first empirically study the robustness of current GCL node representations to weak supervision. Then, we introduce Weakly Supervised Graph Contrastive Learning, WSNet, a novel method that incorporates signals from weak labels for the contrastive learning objective. We evaluate WSNet on five benchmark graph datasets comparing its performance with state-of-the-art GCL and noisy-label learning methods. We show that WSNet outperforms all baselines particularly in the high noise setting. We conclude that although current GCL methods show great promise in the weak supervision paradigm, they are still limited in their capacity to deal with label noise and utilizing signals from weak labels is an effective way to improve their performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel graph contrastive learning method, named WSNET, to learn node representations when weak or noisy labels are present. The authors conducted experiments to compare the robustness of current GCL node representation methods under weak supervision and found that incorporating weak label information into contrastive learning using WSNET can improve node representation learning.

### Strengths
The authors propose a novel approach to improve the node representation learning ability of GCL when there is noise in the node labels.

### Weaknesses
1. The authors spend too much space on Research Question 1, which evaluates the robustness of existing GCL methods. This is only a process of running baselines and cannot be the main innovation and contribution of the paper. The authors should focus more on the proposed method.
2. Even with the amount of space devoted to RQ1, I don't think the authors' analysis is deep enough. For example, the authors conclude from the experimental results that baselines that use neighborhood-based sampling of positive pairs perform better than others in the high noise setting. What is the reason for this, and the authors should provide some analysis.
3. The notations are inconsistent, which makes it difficult for readers to understand the algorithm. For example, in the first line of Algorithm 1, $\lambda_i$ looks like a scalar, but Section 3 says that $\lambda$ is a label function. Additionally, are $\Lambda_i$ and $\Lambda[V_i]$ representing the same vector?
4. Will the algorithm's results differ significantly depending on the community search algorithm used and the label aggregation method used? The authors should provide more experimental results to compare the possibilities.
5. Will the size of the negative samples $r$ have a significant impact on the results? The authors should provide a sensitivity analysis of the parameters.
6. I believe that the authors should introduce larger-scale datasets, such as OGB data, as the current experimental datasets cannot verify the effectiveness of the proposed method in real-world situations.

### Questions
1. It is unclear why only the node with the highest similarity is sampled as a positive sample for the $L_S$ loss. It would be interesting to investigate whether using a top-k sampling strategy would be feasible and potentially improve the results.
2. It is unclear why WSNET performs better in the High Noise setting than in the Medium Noise setting on the Texas dataset.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates node representation learning in Graph Contrastive Learning (GCL) under weak supervision. Firstly, the paper analyzes the robustness of node representations learned by existing methods under weak supervision and concludes that they are all affected by label noise. To mitigate this issue, this work leverages graph structures to identify more relevant positive sample pairs. Specifically, it identifies nodes belonging to the same community from the entire graph as positive sample pairs. 

Overall, I think the paper is good but not quite up to ICLR standards. Mainly, it lacks some necessary experiments, such as efficiency analysis, feasibility on large-scale graphs, and so on. Further analysis of the possible impacts of the work would be helpful.

### Strengths
1. The experimental performance is good.

2. The work conducts experiments on different levels of homogenous graph datasets, constructing positive sample pairs by selecting nodes belonging to the same community. I believe this is meaningful for graph contrastive learning.

### Weaknesses
1. Identifying nodes belonging to the same community from the entire graph is a computationally intensive operation. Including an analysis of efficiency would enhance the completeness of this work.

2. The paper lacks diagrams/figures, training details, or efficiency analysis.

3. Theoretical analysis in this paper is insufficient.

4. The dataset used in this work is relatively small. The authors mention in the paper that this work can be extended to larger datasets. Conducting experiments on larger datasets,  such as the OGB dataset, would further demonstrate the effectiveness of the work. Additionally, analyzing the feasibility of identifying positive sample pairs on large graphs with acceptable efficiency is worth considering.

5. The paper proposes a way to improve the learning of node embeddings learned with graph contrastive under weak supervision. The paper also provides some experiments that show that their model can achieve good performance. However, the experiments are not sufficient, and the innovativeness is not up to ICLR standards.

### Questions
1. Which labeling functions (LFs) were used to derive the weak label matrix, Lambda? As far as I remember, the famous citation network triplet (Cora, Citeseer, and Pubmed) does not come with such weak labels. Furthermore, in the context of Majority Voting, how is a tie among LFs resolved?
2. The Louvain algorithm [1] identifies exclusive communities, implying each node associates with only one community. This exclusivity is often incongruent with real-world scenarios. For instance, individuals in social networks typically affiliate with multiple groups, such as family, friends, and colleagues. Similarly, in biological contexts, genes or proteins often participate in multiple pathways. Furthermore, the Louvain method can yield poorly connected communities [2]. Could you elucidate further on the algorithm's application, such as the number of communities detected versus class count and how effective it helps with “finding nodes with a similar graph structure”? Why not opt for other superior methods, such as the Leiden algorithm? 
3. Hard samples, particularly hard negatives, are pivotal for representation learning under the Contrastive framework [3]. The Supervised Contrastive Loss study [4] further emphasizes the significance of hard samples over easy ones. Could you provide further insight into L-supcon, given its centrality in your method?
4. The proposed loss combines Self-Supervised Contrastive Loss L-s and Supervised Contrastive Loss L-supcon. This combination suggests equal influence from both losses, yet intuitively, L-supcon seems more potent than L-s. Do you think it is necessary to account for their respective contributions to representation learning, perhaps by introducing and searching for a hyperparameter?
5. In PI-GNN [5], the authors employ noise ratios of 0.0, 0.2, 0.4, 0.6, and 0.8, which appear more intuitive. Despite PI-GNN focusing on image datasets and WSNET on graph datasets, The chosen noise ratios in this study (High 53%, Medium 32%, Low 10%) are notably specific. Could you elucidate the rationale behind these values and explain your approach to introducing noise to the original labels?
6. How do you account for the enhanced performance on non-homophilous graphs? Might this improvement be ascribed to the community detection algorithm?
7. In the paper, it is mentioned that weak labels have accuracies set at 47\%, 68\%, and 90\%. I am curious about how these weak labels are generated and how their accuracies are controlled.

**Typos, Formatting Issues, and Grammatical Errors:**
1. In abstract sentence 3, add a comma after “instead”, before “particularly” in sentence 10, and before “and” in sentence 11.
2. In Section 1, paragraph 3, sentence 7, add a comma before “or”, and “citations” should be in its singular form to align with “networks”.
3. In section 1, paragraph 5, sentence 5, “are” should be “is” to agree with “answering these questions”.
4. In section 2, paragraph PWS, sentence 3, add a comma before “and”.
5. In section 2, paragraph PWS, sentence 6, “straight-forward” should be “straightforward”.
6. In section 2, paragraph PWS, sentence 8, “to study” should be “on studying” to align with “on weak label aggregation”.
7. In section 2, paragraph NLL, sentence 1, “straight-forward” should be “straightforward”.
8. In section 2, paragraph NLL, sentence 3, “Most” should be “The most”.
9. In Section 4, Paragraph 1, in sentence “Here, we sample a node’s positive from the set of nodes that has it’s same aggregated label and negatives from the remaining nodes”, “it’s” seems redundant and erroneous.

**References**\
[1] Blondel, Vincent D; Guillaume, Jean-Loup; Lambiotte, Renaud; Lefebvre, Etienne (9 October 2008). Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment. 2008 (10): P10008.\
[2] Traag, V.A., Waltman, L. & van Eck, N.J. From Louvain to Leiden: guaranteeing well-connected communities. Sci Rep 9, 5233 (2019).\
[3] Khosla, P., Teterwak, P., Wang, C., Sarna, A., Tian, Y., Isola, P., Maschinot, A., Liu, C., & Krishnan, D. (2020). Supervised Contrastive Learning.\
[4] Kalantidis, Y., Sariyildiz, M.B., Pion, N., Weinzaepfel, P., & Larlus, D. (2020). Hard Negative Mixing for Contrastive Learning. \
[5] Du, X., Bian, T., Rong, Y., Han, B., Liu, T., Xu, T., Huang, W., Li, Y., & Huang, J. (2021). Noise-robust Graph Learning by Estimating and Leveraging Pairwise Interactions.\
[6] "Grammarly." Wikipedia, Wikimedia Foundation, 27 September 2023, en.wikipedia.org/wiki/Grammarly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a noisy-label learning method for graph contrastive learning which incorporates signals from weak labels. The  authors aim to explore the robustness of GCL methods to label noise and combine weak labels with graph communities to obtain better node representations. Extensive experiments illustrate the robustness of the node representations learned using GCL to weakly supervised classification and the effectveness of using weak labels to learn more robust embeddings.

### Strengths
1.  The description and formulation of the proposed algorithm are clear. The idea of combining the weak labels with graph communities to learn node representations  is novel. 

2. The experimental analysis is extensive and the article provides a comprehensive evaluation of the proposed algorithm on multiple benchmark datasets, demonstrating its effectiveness in various noise settings. 

3. The authors have provided sufficient details about the datasets and the experimental setup, which is commendable.

### Weaknesses
1. How does the weak label be generated? The author only state that the weak label is generated by the labeling function but without no more elaboration. If the label is not given, then how the weak label can be generated with a certain accuracy? A comparison on different labeling function could also be helpful. 

2. The definition of robustness of GCL to label noise is very confusing. 1) Is label noise meaning the inaccuracy of true label or generated weak label? 2) It follows a logical intution that when there is a high level of lable noise in a dataset, the accuracy of a model trained on this dataset is likely to be low. If the label noise in a dataset as high as 53%, ahieveing high accuracy could be somewhat meaningless. 

3. The idea of this paper is very similar to cluster-based graph contrastive learning such as [1] which utilize the cluster or community information as auxiliary information for learning objective.  Thus, the author should concentrate on comparining with these baselines. 

4. The methods should be evaluated on more large-scale datasets such as ogbn datasets or Aminer-CS datasets. The datasets containing only hundreds or thousands of nodes are less convincing. 

5. The presentation of the paper should be improved. For example, the caption of table should apperaove above the table; It is better not to place any context between two tables.

### Questions
See weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper targets the weak/noisy label contrastive learning task. The contributions lie in two perspectives: Under the context of weak label  graph representation learning 1) the authors demonstrate that prior graph contrastive learning works do not show obvious robustness across different levels of noise; 2) the authors propose WSNet, which shows relatively superior robustness over weak/noisy labels. The authors also conduct ablation experiments to prove the necessity of the combination of the two defined losses.

### Strengths
1.	The paper is well-written. It is very easy to follow, and the authors provide thorough details about the problem setting, loss definition, as well as experimental settings.
2.	The experiments are extensive under the weak/noisy label setting.
3. The authors provide codes for reproduction.

### Weaknesses
1. The weak/noisy label setting appears to be confined to a limited context, especially on graphs. While I acknowledge the contribution of this paper in this specific area, its applicable generality to real-world graph datasets is questionable.
2. The analysis to the baseline GCL methods performance under noisy settings are shallow to some extent. The authors may consider some further analysis. For example, how well would each baseline perform under different types of classifier? What are the samples in common that are "robust" to such weak/noisy labels for each baseline?
3. An MLP is widely-used classifier as well. The authors may consider adding it to the experiments.

### Questions
Refer to weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
