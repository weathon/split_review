# Joint Graph Rewiring and Feature Denoising via Spectral Resonance

- Decision: Accept
- Scores: 8, 8, 8, 8, 8

## Abstract
In graph learning the graph and the node features both contain noisy information about the node labels. In this paper we propose \textit{joint denoising and rewiring} (JDR)---an algorithm to jointly rewire the graph and denoise the features, which improves the performance of downstream node classification graph neural nets (GNNs). JDR improves the alignment between the leading eigenspaces of graph and feature matrices. To approximately solve the associated non-convex optimization problem, we propose a heuristic that efficiently handles real-world graph datasets with multiple classes and different levels of homophily or heterophily. We theoretically justify JDR in a stylized setting and verify the effectiveness of our approach through extensive experiments on synthetic and real-world graph datasets. The results show that JDR consistently outperforms existing rewiring methods on node classification using GNNs as downstream models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents Joint Denoising and Rewiring (JDR), a novel algorithm designed to simultaneously address noisy graph structures and node features, thereby enhancing node classification performance in graph neural networks (GNNs). The work proposed aims to address the issue of graph datasets that suffer from noise due to missing or spurious edges and misaligned node features. JDR counters this by iteratively refining both the graph structure and features to maximize the alignment between their leading eigenspaces, achieving what the authors call “spectral resonance,” which improves data representation for downstream GNN performance. The algorithm operates in three iterative steps: first, it decomposes the graph’s adjacency matrix and node feature matrix into eigen and singular vectors; then, it aligns the leading eigenvectors of the graph with the primary singular vectors of the feature matrix, creating a more cohesive representation; and finally, it synthesizes the updated graph for subsequent GNN tasks. The authors argue this iterative approach effectively enhances graph quality and feature clarity, especially in datasets exhibiting mixed homophily and heterophily, which are often challenging for GNNs. The proposed work provides extensive experiments show that JDR consistently outperforms existing rewiring methods on synthetic and real-world datasets, yielding better alignment and improved node classification accuracy. Additionally, JDR’s preprocessing method produces an enhanced graph that supports interpretability and reusability, unlike other methods that modify graphs solely during training. The paper highlights JDR’s scalability and versatility across different graph types, underscoring its potential in handling noisy real-world data and establishing it as a valuable advancement in preprocessing techniques for GNNs.

### Strengths
The primary novelty of JDR lies in its combined optimization of graph structure and node feature alignment, enhancing data quality by maximizing alignment between the spectral components of the graph and feature matrices. This unified approach addresses both structural and feature-level noise simultaneously, which is rare among existing methods that typically target these types of noise separately. A key concept introduced is “spectral resonance,” where optimal alignment between the graph’s leading eigenvectors and the feature matrix’s singular vectors is achieved, providing a measurable target for denoising and boosting node classification performance. To manage the challenging non-convex optimization, the paper presents an iterative heuristic based on alternating optimization, which simplifies alignment maximization and enables efficient processing of large, real-world graph datasets with multiple classes. Another advantage of JDR is that it outputs a modified graph in the preprocessing stage, enhancing interpretability and reusability for subsequent GNN applications—a contrast to end-to-end methods that alter the graph only during training. Lastly, JDR’s design allows it to adapt effectively to both homophilic and heterophilic graphs, expanding its applicability beyond previous methods, which often work best with specific types of graph structures, such as those with high homophily.

The paper is well-organized, systematically guiding the reader through the challenges, methodology, and outcomes of the proposed Joint Denoising and Rewiring (JDR) algorithm. It begins with an introduction that effectively frames the problem of noisy graph structures and features, establishing the need for an approach that addresses both in unison. The methodology section details the concept of spectral resonance and the iterative optimization heuristic that drives JDR, using clear mathematical definitions and visual aids to support understanding. Following this, a comprehensive experimental section validates the algorithm's effectiveness across synthetic and real-world datasets, offering detailed comparisons with state-of-the-art methods and highlighting the algorithm’s robustness across homophilic and heterophilic graph types. Finally, the paper provides an insightful discussion on related works, situating JDR within the broader landscape of graph preprocessing techniques, before concluding with a summary of contributions and potential directions for future research. Overall, the structure flows logically, with each section building on the previous one to reinforce the practical relevance and theoretical underpinnings of JDR.

Addressing the limitations of the proposed approach is appreciated

The illustrations provided in the work, both in the body and abstract, are informative and well done as well as qualitatively informative.

 The use of the appendix is also well done in providing explicit discussion of the proposed algorithm 

The paper has a robust experimental section with compelling results working in favor of the approaches proposed

### Weaknesses
JDR depends on the availability of informative node features for effective rewiring and denoising, which restricts its applicability to settings with substantial node feature information; this reliance could limit its effectiveness in networks that primarily encode structural data. Specifically, the method's performance is likely to degrade significantly in scenarios where node features are sparse, noisy, or irrelevant to the underlying graph structure. The algorithm’s design is also tailored to node-level tasks, making it less suited for graph-level tasks like graph classification, where global structure matters more than node-specific features. The core optimization of JDR focuses on aligning node features with local graph structure, which may not capture the complex, hierarchical dependencies crucial for graph-level analysis. This limitation is particularly relevant for tasks where the overall graph topology and global patterns are the primary determinants of classification, rather than individual node characteristics.

### Questions
could timing comparisons of the proposed methods, more explicitly and beyond just complexity comparison, be provided to observe computational benefits/limitations?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes to  jointly consider graph rewiring and feature denoising to improve the performance of GNNs for downstream classification tasks.  The proposed method improves the performance of a numer of GNNs on a number of popular datasets in the experiments.

### Strengths
1. The proposed method is general and can be applied to a wide range of GNNs for downstream classification tasks. 

2. The proposed method jointly considers graph rewiring and feature denoising.

3. The proposed method improves the performance of a numer of GNNs on a number of popular datasets in the experiments.

### Weaknesses
1. The solution is somewhat incremental and its novelty is low, although it appears to be sound.

2. There is no theoretical guarantee on the degree of improvement using JDR.

3. The experiments were conducted on a small number of datasets that cannot be considered as an evidence that the proposed method is really effective.

### Questions
My main concern with this work is that although the proposed method looks to be sound, there is really no theorectical ground on its effectiveness in general when applied to a wider range of datasets. Also, the datasets used are very small and I'm not sure how useful and how scalable the method is in practice. It would significantly strengthen the work if the authors can either theoretically show how much improvement can be obtained using their method or empirically demonstration the effectiveness on a wide range of datasets, not just on common datasets that we have already seen too many papers claiming their effectiveness over others. I believe the contributions of such work are rather limited.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the graph rewiring problem and feature denoising problem to improve the graph node classification task.
This paper utilizes cSBM modeling to optimize both graph structures and graph features to make them have better alignment, then proposes the JDR method to effectively optimize the alignment function.

### Strengths
- This paper uses cSBMs as a key framework to build intuition about the graph rewiring and denoising problem, providing the theoretical foundation for the alignment target.
- The empirical verification using synthetic data is clear.
- The method is evaluated on both homophilic graphs and heterophilic graphs, showing its generalizability.

### Weaknesses
 - The proposed method involves graph structure matrix and graph feature matrix decomposition, which can be computationally challenging on extremely large real-world graph data, limiting the practicability of the proposed method. Specifically, the reliance on SVD for decomposition, even if only for top-k components, introduces a significant computational bottleneck. While the authors mention sparsity, the practical impact of this on very large graphs with millions of nodes and edges needs more rigorous justification. The assumption that the average degree *d* does not scale with *N* may not hold true for all real-world graphs, and this needs to be explicitly addressed with empirical evidence on the types of graphs where this assumption is valid.
- As the SVD decomposition can have time complexity of $O(N^3)$, it may be not accurate to say the proposed JDR has time complexity of $O(N)$. The claim that using the power method for top-k eigenvectors reduces the complexity to $O(N)$ needs more detailed explanation and justification. The practical performance of the power method can vary significantly depending on the spectral gap of the matrix, and this variability should be discussed. Furthermore, the number of iterations required for convergence in the power method is an important factor that should be considered in the overall time complexity analysis.

### Questions
- As the computation overhead of the proposed method seems large, can it be applied to large graphs, e.g. ogbn-products?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents a structural rewiring algorithm, with consideration of structural alignment with node features, supported by theoretical investigation on cSBM model.

### Strengths
1.The overall structure is well organized and easy to understand, especially the diagram demonstrations are very helpful.
2.The problem formulation is clearly presented.
3.Experiments are comprehensive and convincing.

### Weaknesses
1. The theoretical framework seems convincing to me, while how the real data sets fit the parametric model needs further investigation, otherwise the heuristic of denoising features might not be applicable. Specifically, the assumption that real-world graph data conforms to the cSBM, with its inherent block structure and signal-to-noise ratio, needs more rigorous justification. The paper should provide a more detailed analysis of how deviations from this model might affect the performance of the proposed rewiring algorithm. For example, what happens when the community structure is not clear or when the noise is not random but structured?
2. More explanation is needed on the insights of where the rationale of denoising comes from, e.g. lines 159-190. The connection between the optimization problem and the spectral properties of the adjacency matrix and feature matrix is not fully clear. The paper should elaborate on why the leading eigenvectors and singular vectors are aligned with the underlying class structure and how this alignment justifies the denoising procedure. A more detailed explanation of the quadratic and bilinear forms in equation (2) is needed, specifically how they lead to the selection of leading eigenvectors/singular vectors.
3. Since the eigendecomposition is applied on adjacency, the comparison of training and inference time costs between the vanilla GNN and with the add-on of the proposal is needed. The computational overhead of the eigendecomposition, especially for large graphs, could be a significant bottleneck. The paper needs to provide a clear comparison of the time complexity of the proposed method versus standard GNN training and inference, including a breakdown of the time spent on the eigendecomposition step.

### Questions
1. In Figure 2, why do the two subgraphs compare w.r.t. amplitude and normalized amplitude, respectively?
2. Regarding section 2.2, can you explain more about how the structure is revealed parametrically? In line 137, $|\lambda|$ is considered the signal-to-noise ratio, when it can also be considered the degree of homophility?
3. The remark below definition 1, ''the information about the labels is indeed contained in the leading vectors of V and U'', is unclear.Because usually the decomposition of a matrix gives a support space, the weights of each support, and the coefficient of reconstructing the matrix using the support, which leads to the insufficiency of the leading support vectors to be representative.
This should be relevant for W2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposes a method (JDR) to jointly perform graph rewiring and feature denoising. The method is derived from cSBM to maximize alignment between the eigenspaces of features and the graph. The authors tested the performance of the methods in various datasets and showed the advantages of the proposed JDR method.

### Strengths
1. The method is well inspired and can achieve better performance than several other graph rewiring methods.
2. An impressive amount of experiments were implemented.

### Weaknesses
1. The paper should better discuss previous works on GNN versus MLP, and the connection between heterophily and graph noise. [1-4] investigated the phenomena that MLP sometimes perform better than GNN (especially GCN) for heterophilic graphs. In particular, [4] proposed a metric that well correlates with empirical GNN performance, and also discussed the connection between heterophily and graph noise. A better discussion (acknowledgement?) of [4] is needed due to its high relevance to this paper.

2. The comparison between JDR and graph rewiring methods seems not perfectly fair as the authors also mention themselves. Moreover, if JDR indeed achieves optimal denoising, then the graph may no longer be needed in later training. This (JDR(X) + MLP) seems uncovered by the ablation settings. 

3. The authors should check if the rewired graph structures degenerate, which may be a natural consequence of combining matrix factorization scheme and thresholding. Specifically, it's important to examine if the rewired graphs become disconnected or if the adjacency matrices become low-rank after the matrix factorization and thresholding steps. This could indicate a loss of structural information.

4. The hyperparameter tuning was not performed for the GNN backbone. This is questionable as the optimal backbone hyperparameter is anticipated to vary across different rewired graphs (and potentially different denoised features). This may matter because the performance gap between JDR and other methods seems small in most cases.

5. Some paragraphs are unclear and not readable. In particular, it is unclear what “findings” in the sentence “The Gaussian adjacency equivalence conjecture (Shi et al., 2024) suggests a generalization of the findings to the true binary adjacency case.” is referring to. The whole section (as well as the proof) needs to be polished.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2
