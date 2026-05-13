# Understanding the Design Principles of Link Prediction in Directed Settings

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Link prediction is a widely studied task in Graph Representation Learning (GRL) for modeling relational data. Early theories in GRL were based on the assumption of a symmetric adjacency matrix, reflecting an undirected setting. As a result, much of the following state-of-the-art research has continued to operate under this symmetry assumption, even though real-world data often involves crucial information conveyed through the direction of relationships. This oversight limits the ability of these models to fully capture the complexity of directed interactions. In this paper, we focus on the challenge of directed link prediction by evaluating key heuristics that have been successful in the undirected settings. We propose simple but effective adaptations of these heuristics to the directed link prediction task and demonstrate that these modifications yield competitive performance compared to leading Graph Neural Networks (GNNs) originally designed for undirected graphs. Through an extensive set of experiments, we derive insights that inform the development of a novel framework for directed link prediction, which not only surpasses baseline methods but also outperforms state-of-the-art GNNs on multiple benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a framework for understanding the directed link prediction problem with GNNs and how various changes to the underlying architecture can affect and then eventually enhance downstream performance. To test this, the authors run a series of experiments, both exploratory and ablative, to determine which practical components in directed link prediction architectures improve performance. After which, they construct their final framework to demonstrate it's superiority over common LP GNNs and heuristic methods.

### Strengths
* The intuition behind this problem is well-motivated, it is a common assumption within link prediction to assume that the input adjacency matrix is symmetric. Research, such as what the author's propose is necessary and potent for constructing GNN models that have more applicability in real-life scenarios where directed links and asymmetric adjacency matrices are more useful for end users.
* The authors integrate a variety of experiments in order to aid the reasoning for constructing their proposed framework. Since the design of these experiments is intuitive and easy-to-follow it makes the paper easier to read and provides clarity to the author's intent. 
* Additionally, the scope of the methodology, including the questions it asks, is comprehensive in how it integrates reasoning at a scale that bridges a necessary gap between symmetric/undirected link prediction and directed link prediction, which is important for the proposed level of understanding that the authors are attempting to achieve.
* The use of a robust metric like MRR is an excellent practical decision and lends credence to the author's overarching claims about directed link prediction.

### Weaknesses
 * There are concerns about intuition from the beginning, as seen in Figure 1. Why is it that practitioners should worry if the undirected or directed encoder captures varying levels of information? It is intuitive that more information can lead to better performance, especially given the experimental results, but the connection as to **why** the lack of directionality decreases performance is tantamount to improving understanding. For example, what can finer-levels of directed distance-encoding do in order to improve performance? Is there a stronger correlation between better expressiveness in directed networks and their performance than what is seen with undirected networks?
* The overlap in performance for many of the experiments is concerning, in order to determine the significance of whether or not varied encoders, decoders, labeling schemes are better than one another with confidence. Then p-values or interval tests should be conducted between the scoring distributions for all tested architectures to determine if there is an significant difference between the performance of these architectures. This is especially pertinent given the high-level of overlap between the reported scores in many of the experimental tables.
* The novelty of the framework is a concern given that the intent of this article is understanding how the design in directed link prediction can improve performance in more practical scenarios. What sort of insights does this paper provide that are not already evident within [1]? It seems that further investigation into directed distance encoding could provide a new level of insight.
* Although the overall scope of the preliminary experiments and ablation studies is comprehensive, the authors only tests the simpler and well-known baselines (heuristics, MLP, GAT, GCN, GraphSage) against DirLP. Why not include experiments that consider more advanced directed GNNs like MagNet [2] or DiGCN [3]? Or even additional directed autoencoders, given the preliminary questions explored in this article? The results about design principles remain inconclusive relative to integration of edge-wise structural feature extraction within DirLP without these sorts of considerations given that concepts which have been explored before in the directed GNN literature are not explored within this article. 
* I am certain that the authors are aware of this. But, there are numerous spelling mistakes in the article, including the use of 'principal' instead of 'principle'.
* What search space of hyperparameters was OPTUNA given for tuning the tested models? This is important for experimental reproduction, but not critical given the Tables 9-12.

### Questions
See 'Weaknesses' section of this review for questions.

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on extending link prediction techniques to directed graphs, addressing a gap in Graph Representation Learning (GRL). While much of the research in link prediction has concentrated on undirected settings, the authors emphasize the importance of capturing directionality in many real-world applications (e.g., transaction networks). They propose **DirLP**, a novel framework for directed link prediction, which outperforms both heuristic-based and Graph Neural Network (GNN)-based models across multiple benchmark datasets. DirLP shows state-of-the-art performance across six datasets, proving its effectiveness in capturing the directionality of relationships.

### Strengths
1. The paper addresses a critical gap in GRL by extending established principles to directed settings. 
2. The framework considers several key components such as asymmetric decoders, directed structural features, and labeling tricks to capture directionality effectively.The use of a modular design (e.g., DirGNN as encoder and CMLP as decoder) makes the framework adaptable to various graph structures.

3. Extensive experiments across multiple datasets (CORA, CITESEER, BLOG, etc.) show the model’s superiority, providing statistical insights into performance.

### Weaknesses
1. The necessity of directed setting is not clear. Commonly directed graphs are transformed to undirected graphs as the authors mentioned, so an important question is that can the model on directed setting perform better than undirected setting. The paper shows DirGNN can perform better than GCN or SAGE on directed graph, but how is it compared to the performances of GCN or SAGE on correspondent undirected graphs? So I think the comparison with GNNs on correspondent undirected graphs is important. For example, the authors can include a specific experiment comparing DirLP to GCN/GraphSAGE on both directed and undirected versions of the same datasets.

2. Large datasets from OGB are not included, which limits the application of proposed model. For example, the OGB-citation2 is a citation network which is obviously directed in raw data. Or can the authors discuss any potential scalability challenges DirLP might face on larger graphs?

3. What's $\alpha$ for each dataset? It's not shown in the hyperparameter table. Can the authors add it in Table 12 and discuss something on how the value of $\alpha$ show the different properties of each dataset?

### Questions
See weaknesses.

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
The authors study the link prediction tasks in the directed settings. The authors conducted comprehensive experiments to compare the encoder, labeling tricks, structural features, decoder and negative sampling in both directed and undirected settings. Based on the observations from the experiments, the authors propose DirGNN targeting at performing link prediction tasks in the directed setting. Experiments across various benchmarks show that DirGNN can perform significantly better than the undirected sota methods.

### Strengths
[S1] The paper has a clear writing and easy to follow.

[S2] The authors conduct a comprehensive series of experiments on directed link prediction. It reveals which designs/components can improve the performance in the directed link prediction.

### Weaknesses
[W1] The benchmark datasets are small compared to most undirected link prediction methods. For example, OGB datasets, including Collab, PPA, and Citation2 are not used as benchmarks in this study. I would suggest including Citation2 as a benchmark since (1) it is large-scale, and (2) it is a directed graph dataset.

[W2] Directed GNN baselines are missing in the Table 6. The authors should include the popular directed GNNs (encoders) as baselines, like those discussed in the related work.

### Questions
[Q1] In Table 6, the authors can consider adding ablation studies to demonstrate how much each proposed directed component contributes to the overall performance improvement. 

[Q2] The recent studies about link prediction methods focus on those that both have superior performance and capability to scale to large graphs. I wonder what extra computational cost DirGNN has compared to undirected GNNs.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of directed link prediction within Graph Representation Learning (GRL), a task traditionally focused on undirected graphs. Recognizing that real-world data often contains crucial directional information, the authors highlight the limitations of using models designed for symmetric, undirected graphs in such settings. They adapt successful heuristics from undirected link prediction for directed graphs and demonstrate their effectiveness, particularly in comparison to state-of-the-art Graph Neural Networks (GNNs). Through extensive experiments, they present a new framework, DirLP, which consistently outperforms traditional and cutting-edge models in directed link prediction tasks.

### Strengths
1. The paper identifies and addresses a key gap in the current GRL literature by focusing on the complexities of directed interactions, which are often overlooked in favor of simpler, undirected models.
2. The authors provide a thorough comparison across heuristic, MLP, and GNN-based models for directed link prediction, offering insights into how directionality impacts predictive performance.
3. The novel DirLP framework not only adapts key design principles for directed graphs but also demonstrates superior performance over leading models on multiple benchmarks, making a significant contribution to the field.

### Weaknesses
1. The paper is lack of novelty. The key difference with the SEAL is the directed GNN and directed distance which is only minor modification on the original method. edge-wise structural feature extraction is a single extension of the Buddy method while without efficiency hashing method. 
2. The proposed method is inefficiency. The labeling trick is with O(N^3) time complexity and O(N^2) memory complexity
3. The benchmark datasets are problematic. The utilized dataset are quite small while none of the OGB graph is included despite some are also directed.  The Chameleon and squirrel datasets without filter has some repeat edges, which may lead to data leakage[1]
4. The baseline selected is out of dated, the lastest baseline is GAT in 2018, without any GNN for link prediction baseline and directed GNN baselines. 
5. The principal seems trivial that for all the components, the directed one is better than the undirected one as we focuses on the directed setting instead of undirected setting.

### Questions
1. Given the high computational complexity, how does the proposed labeling trick (O(N^3) time and O(N^2) memory complexity) impact the efficiency of the method in large-scale graphs?
2. Why were the benchmark datasets chosen relatively small, and why were OGB graphs (some of which are directed) not included in the evaluation?
3. How did the repeated edges in the Chameleon and Squirrel datasets affect the integrity of the results, particularly concerning potential data leakage?
4. Why were the baselines selected (the latest being GAT from 2018) not updated to include more recent GNNs or directed GNNs designed specifically for link prediction tasks?
5. How do the findings provide non-trivial insights, given that the result showing directed components outperforming undirected ones in directed settings might seem intuitive?

### Soundness
2

### Presentation
3

### Contribution
1
