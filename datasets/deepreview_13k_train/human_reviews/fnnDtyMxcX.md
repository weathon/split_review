# HeNCler: Node Clustering in Heterophilous Graphs via Learned Asymmetric Similarity

- Decision: Reject
- Scores: 3, 6, 3, 1

## Abstract
Clustering nodes in heterophilous graphs presents unique challenges due to the asymmetric relationships often overlooked by traditional methods, which moreover assume that good clustering corresponds to high intra-cluster and low inter-cluster connectivity. To address these issues, we introduce \modelname—a novel approach for \underline{\textbf{He}}terophilous \underline{\textbf{N}}ode \underline{\textbf{Cl}}ust\underline{\textbf{er}}ing.
Our method begins by defining a weighted kernel singular value decomposition to create an \emph{asymmetric} similarity graph, applicable to both directed and undirected graphs. We further establish that the dual problem of this formulation aligns with asymmetric kernel spectral clustering, interpreting \emph{learned} graph similarities without relying on homophily. We demonstrate the ability to solve the primal problem directly, circumventing the computational difficulties of the dual approach. Experimental evidence confirms that \modelname significantly enhances performance in node clustering tasks within heterophilous graph contexts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a kernel spectral biclustering framework to learn an induced asymmetric similarity graph suited for node clustering of heterophilous graphs.

### Strengths
1. The proposed method is easy to understand.
2. It addresses an important problem.

### Weaknesses
1. The innovation seems limited, as graph rewiring is already a common approach to tackle heterophilous graphs, as seen in [1] and [2]. However, it would be beneficial for the authors to clarify how their kernel spectral biclustering approach meaningfully differs from existing graph rewiring techniques. Specifically, a comparison of how these methods address heterophily and clustering effectiveness would strengthen the argument for the novelty of their approach. By expanding on the specific advantages or unique contributions of kernel spectral biclustering over rewiring methods, the authors could better situate their work within the current landscape.

2. While the proposed method achieves the best performance in 11 out of 16 cases, the choice of only five baselines may limit the comprehensiveness of this evaluation. I suggest including additional baselines that are well-regarded in heterophilous graph clustering to provide a more robust comparison, like [4][5]. Additionally, reporting on the statistical significance of the observed improvements would help clarify whether these performance gains are practically meaningful or consistent across datasets.

3. More detailed analysis of Table 4 would improve the discussion of the results. Specifically, it would be helpful for the authors to discuss the relative impact of the different components (e.g., the kernel spectral biclustering loss vs. reconstruction losses) in achieving the overall performance. Additionally, an investigation into any observed trends or dependencies among these components would provide insights into the roles they play in model performance.

4. I recommend adding larger datasets, such as Ogbn-arxiv [3], to further validate the proposed method. Testing on larger datasets could help assess the scalability and robustness of the approach and reveal any computational challenges that might arise when handling high-dimensional data. This addition could provide a more comprehensive evaluation and help demonstrate the method's potential for broader applications.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Focusing on node clustering on heterophilous graph, this paper introduces an RMK-based framework for learning an asymmetric similarity. By incorporating wKSVD framework into graph clustering with two reconstruction loss, HeCler can optimize a bipartite graph with theoretical interpretability.  The experimental results and empirical analysis can demonstrate the effectiveness.

### Strengths
1. Novelty: Although the overall idea of learning a similarity matrix for heterophilous graph learning is not new, this paper proposed an interesting framework by observing the advantage of RMK framework.
2. The theoretical support brings interpretability to this framework.
3. The discussion could empirically interpret how the method works.

### Weaknesses
1. One weakness is the lack of literature on heterophyllous graph learning. The authors only list three works for heterophilous node clustering. Other methods for heterophyllous graph representation learning are suggested to be included on top of node clustering (such as heterophilous node classification, multi-view heterophilous node clustering, etc).

2. Analysis about the experimental results are somehow insufficient. The experimental results on undirected graphs seems not as good as directed graphs, such as Chamelon, squirrel. The authors should analyze this. In addition, the NMI in these datasets are very low (such as 9.67, 0.06, 6.73), which phenomenon indicates that the model even does not learn any clustering information. How to explain this?

### Questions
1. Can you provide a detailed analysis of why your method performs differently on directed vs undirected graphs, particularly for datasets like Chameleon and Squirrel?
2. The NMI scores for some datasets (e.g. 9.67, 0.06, 6.73) are very low. What might these low scores indicate about the model's performance or limitations on these particular datasets? Are there any insights to be gained from comparing these results to other methods or baseline performance on these challenging datasets?

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
The paper introduces HeNCler, a novel approach for clustering nodes in heterophilous graphs. Traditional clustering methods often assume homophily, where nodes with similar labels are more likely to be connected. HeNCler addresses this challenge by learning a similarity graph through a clustering-specific objective based on weighted kernel singular value decomposition. The authors claim that HeNCler significantly improves node clustering performance in heterophilous graph settings, highlighting the advantage of its asymmetric graph-learning framework.

### Strengths
1. The paper addresses a significant and under-explored problem in the field of node clustering for heterophilous graphs. This is a practical and relevant issue, as many real-world graphs exhibit heterophily.
2. Leveraging weighted kernel singular value decomposition to learn a similarity graph for deep node clustering appears to be novel.
3. The whole objective combines the proposed wKSVD loss with a graph autoencoder. Ablation studies suggest that both components contribute to the overall performance of HeNCler.

### Weaknesses
1. The relationship between the proposed wKSVD loss and the characteristics of heterophilous graphs is unclear, which limits the soundness of the method. To my understanding, the most important part of wKSVD is its asymmetric similarity measure, which applies different projections to the pairs. However, it is a pretty trivial operation and this paper does not provide a in-depth explanation of how it helps in the context of heterophilous graphs. Specifically, while the asymmetric projection might capture different aspects of node relationships, it's not clear how this directly addresses the core challenge of heterophily, where connected nodes tend to have dissimilar labels. The paper lacks a theoretical justification for why this particular asymmetry is beneficial for heterophilous graphs, rather than just being a general similarity measure.
2. While the paper claims significant performance improvements, it does not compare with strong baselines or state-of-the-art methods for heterophilous graphs. There are various unsupervised heterophilous graph representation learning methods that could serve as competitive baselines, but the only competitor designed for heterophilous graphs is MUSE. The lack of comparison with other relevant methods makes it difficult to assess the true contribution of HeNCler. For instance, methods that explicitly model heterophily through techniques like edge sign prediction or neighborhood aggregation with attention mechanisms are not considered, which would provide a more comprehensive evaluation.
3. I don't agree with the claimed computational complexity improvement of HeNCler. According to _Optimizer, constraints, and cluster assignment_, cluster assignments are obtained by KMeans clustering on the final embeddings, so you need to include the complexity of KMenas in the overall complexity analysis. The paper only considers the complexity of the wKSVD and graph autoencoder parts, neglecting the potentially significant cost of KMeans, especially for large graphs and high dimensional embeddings. This omission undermines the validity of the computational complexity analysis.
4. The wKSVD-loss is based on the primal formulation of wKSVD, so it's unclear how most of Section 3.1 relates to the proposed method. The paper spends considerable space on the dual formulation of wKSVD, but the actual implementation uses the primal form. This disconnect between the theoretical exposition and the practical method creates confusion and raises questions about the relevance of the dual formulation to the proposed approach.

### Questions
1. Please provide more theoretical evidence to strengthen the effectiveness of wKSVD for heterophilous graphs.
2. Consider removing the dual formulation if it's unrelated to the proposed method.
3. Please add additional experiments comparing HeNCler with state-of-the-art methods for heterophilous graph clustering or representation learning.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
HeNCler employs weighted kernel singular value decomposition (wKSVD) to learn an induced asymmetric similarity graph, avoiding reliance on homophily and enabling more effective clustering in heterophilous settings.

### Strengths
1.The motivation is clear. 
2. The proposed method is sound to me.
3. The experimental results show the effectiveness of the proposed method.

### Weaknesses
1. The technique contribution is limited. The main contribution is the construction of asymmetric similarity, while the other method part is a combination of existing components.
2. The authors ignore many existing works, like [1] and [2].
3. The comparison methods are not enough to show their effectiveness. For example, the newest baselines S3GC and MUSE are from 2022 and 2023 respectively. Besides, S3GC focuses on homophilic and large graphs and MUSE focuses on multi-view graphs.
4. The application is limited. This work seems to focus only on heterophyllous graphs. From Table 6, it achieves poor performance on homophilous graphs. However, the homophily is unknown without the labeled data.

### Questions
1. There are a number of works that performs clustering on heterophilic graph, which should be cited or compared. To name a few, [1-4]
2. In fact, some existing methods also learn new similarity matrices from data for heterophilic graph [1-2], which share a similar idea with the proposed method.  


Refs:
[1] Beyond Homophily: Reconstructing Structure for Graph-agnostic Clustering, ICML 2023.
[2] Robust Graph Structure Learning under Heterophily, arXiv 2024.
[3] Homophily-enhanced structure learning for graph clustering. Proceedings of the 32nd ACM International Conference on Information and Knowledge Management. 2023.
[4] Homophily-Related: Adaptive Hybrid Graph Filter for Multi-View Graph Clustering. AAAI 2024.

### Soundness
3

### Presentation
3

### Contribution
2
