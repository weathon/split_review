# Towards Stable, Globally Expressive Graph Representations with Laplacian Eigenvectors

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Graph neural networks (GNNs) have achieved remarkable success in a variety of machine learning tasks over graph data. Existing GNNs usually rely on message passing, i.e., computing node representations by gathering information from the neighborhood, to build their underlying computational graphs. Such an approach has been shown fairly limited in expressive power, and often fails to capture global characteristics of graphs. To overcome the issue, a popular solution is to use Laplacian eigenvectors as additional node features, as they are known to contain global positional information of nodes, and can serve as extra node identifiers aiding GNNs to separate structurally similar nodes. Since eigenvectors naturally come with symmetries---namely, $O(p)$-group symmetry for every $p$ eigenvectors with equal eigenvalue, properly handling such symmetries is crucial for the stability and generalizability of Laplacian eigenvector augmented GNNs. However, using a naive $O(p)$-group invariant encoder for each $p$-dimensional eigenspace may not keep the full expressivity in the Laplacian eigenvectors. Moreover, computing such invariants inevitably entails a hard split of Laplacian eigenvalues according to their numerical identity, which suffers from great instability when the graph structure has small perturbations. 
    In this paper, we propose a novel method exploiting Laplacian eigenvectors to generate \textit{stable} and globally \textit{expressive} graph representations. The main difference from previous works is that (i) our method utilizes \textbf{learnable} $O(p)$-invariant representations for each Laplacian eigenspace of dimension $p$, which are built upon powerful orthogonal group equivariant neural network layers already well studied in the literature, and that (ii) our method deals with numerically close eigenvalues in a \textbf{smooth} fashion, ensuring its better robustness against perturbations. Experiments on various graph learning benchmarks witness the competitive performance of our method, especially its great potential to learn global properties of graphs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a robust orthogonal group-equivariant neural network designed to enhance graph representation using Laplacian vectors. Experiments conducted on various graphs demonstrate the competitive performance of the proposed approach.

### Strengths
- The writing is well-organized and generally reader-friendly.
- The theoretical analysis is comprehensive and detailed.

### Weaknesses
 - The datasets used in the experiments are somewhat limited. The proposed method would be more convincing if validated on a wider range of datasets, such as PATTERN, CLUSTER, or MolHIV.
- Additional illustrations, such as ablation or comparison experiments (e.g., investigating the impact of the continuous smoothing function *ρ*, or examining how the method captures global properties of graphs), would provide a more thorough and solid foundation for the study.

### Questions
* Could you elaborate on how taking inner products may potentially lead to a loss of the rich structural and positional information provided by vanilla Laplacian eigenvectors (line 85)?
* How does the method scale to large-scale graphs? Could you discuss its scalability?

### Soundness
2

### Presentation
3

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
This paper studies the improvement of positional encodings (PEs) based on Laplacian eigenvectors, commonly used as feature augmentations to enhance the expressivity and effectiveness of GNNs.
The paper points out that existing PEs, which deal with symmetries of Laplacian eigenvectors with naive $O(p)$-group invariant encoders, may lose the full expressivity in the eigenvectors. Moreover, the paper argues that the instability resulting from the properties of eigenvectors is ignored in most research. Thus, the paper proposes a novel encoder to generate expressive and stable positional embeddings by utilizing invariant point cloud networks and incorporating smooth function for "soft splitting". Theoretical analysis and extensive experiments demonstrate the effectiveness of the proposed positional encoder.

### Strengths
1. The paper is well-organized and easy to follow.
2. The experimental results seem promising.
3. Authors utilize a novel strategy to softly split the eigenvectors from different eigenspaces, solving the instability constraint of most existing work.

### Weaknesses
1. The novelty of the method is somewhat limited, especially the direct application of existing invariant point cloud networks over the eigenvectors without any transfer challenge. The paper does not adequately address the nuances of adapting point cloud networks, which are typically designed for fixed-dimensional data (e.g., 3D coordinates), to handle the variable dimensionalities of Laplacian eigenspaces. This requires more than a simple application of existing architectures; it necessitates a careful re-design and justification for the specific choices made.
2. The paper doesn’t provide any detail about instance models of $\rho$, $\phi$, and $\psi$ (in Equations 6 and 7) implemented in the experiments, and doesn’t discuss the Lipschitz continuity of these practical models. The lack of specific details about the practical implementations of $\rho$, $\phi$, and $\psi$, especially in the context of neural networks, makes it difficult to assess the stability claims. The paper should provide specific architectural details and discuss the Lipschitz constants of these functions or the overall stability of the implemented algorithm.
3. There is no detail about how OGE-Aug deals with the sign ambiguity of eigenvectors.
4. Authors ignore some essential experiments.
    - Authors don’t verify the stability of the OGE-Aug on OOD benchmarks such as DrugOOD [1], where SPE [2] is validated on this dataset.
    - There is no ablation study on the effectiveness of the proposed “soft splitting” strategy. I think it’ll be better to conduct experiments on Vanilla OGE-Aug as a control group.
    - There is no experiment studying the sensitivity of hyperparameters. For example, the authors don’t explore how different shapes of ρ influence the effectiveness and stability of the positional encodings.
    - The paper doesn’t report the running time of different positional encoding methods.
5. As mentioned in Line 346, insisting on the universality of invariant representation function f may hurt the stability of the positional encoder, however, there is no quantitative analysis nor experimental guidance about how to trade off university and stability.

### Questions
See weaknesses.

### Soundness
2

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
4

### Summary
This paper addresses the problem (established in [2]) of how to incorporate Laplacian eigenvectors into message-passing neural networks (MPNNs) to enhance expressivity while maintaining invariance to the symmetric group. The authors propose two main architectures to achieve this.

First, they present a natural method for integrating equivariant point cloud architectures into existing MPNNs. They then show that when using this method with a universal point cloud architecture, a universal GNN model can be constructed.

The paper then tackles the recently established problem (see [1]) of handling these eigenvectors in a stable manner. They propose a second architecture that, while sacrificing some expressivity compared to the first model, achieves provable stability bounds.

The paper concludes with empirical validation, showing that the second architecture achieves competitive, and in some cases state-of-the-art results across several standard graph benchmarks. 

[1]  Yinan Huang, William Lu, Joshua Robinson, Yu Yang, Muhan Zhang, Stefanie Jegelka, and Pan Li. On the stability of expressive
positional encodings for graph neural networks. arXiv preprint arXiv:2310.02579, 2023.

[2] Derek Lim, Joshua Robinson, Lingxiao Zhao, Tess Smidt, Suvrit Sra, Haggai Maron, and Stefanie Jegelka. Sign and basis invariant networks for spectral graph representation learning. arXiv preprint arXiv:2202.13013, 2022.

### Strengths
1. The paper offers a simple and straightforward way to incorporate Laplacian eigenvectors into GNNs, making it easy to apply to existing architectures.

2. The theoretical result showing that the first approach can achieve universality with a model complexity of $n \cdot \exp(\text{max}(\mu))$ leverages the sparsity of natural graphs in an interesting way (most graphs have low values of $\mu$).

3. The approach is validated with competitive, and in some cases state-of-the-art, results across several common graph benchmarks, supporting its practical usefulness.

### Weaknesses
1. The paper's novelty is somewhat limited. The idea of incorporating Laplacian eigenvectors into MPNNs while respecting the symmetries of the orthogonal group $O(d)$ was already discussed in [2], making the use of point cloud architectures a natural but not particularly novel approach. Similarly, the importance of stability when dealing with Laplacian eigenvectors was pointed out in [1], and the way the second model is derived from the first resembles the approach proposed in [1] as well. Specifically, the core idea of using a smoothing function applied to the eigenvectors before processing them, as a way to achieve stability, is very similar to the approach in [1], which raises questions about the incremental contribution of this work.

2. The introduction and title of the paper emphasize improved global performance, but this is not explored in depth throughout the rest of the paper. A more convincing theoretical argument explaining why the proposed model enhances "global expressivity" would be beneficial. Additionally, synthetic experiments demonstrating that the model outperforms others in learning global properties of graphs would strengthen the claims. Lastly, a brief recap of the types of global information that can be inferred from Laplacian eigenvalues and eigenvectors would provide useful context and support the discussion. For example, while the paper mentions that the eigenvectors can capture positional information, it does not discuss how this relates to global graph properties such as diameter or betweenness centrality.

3. The theory section could be more cohesive. The paper introduces a first model, notes its likely instability, and then replaces it with a second model that is provably stable but less expressive. All experiments are then performed on the second model. However, the discussion regarding expressivity primarily focuses on the first model, leaving the expressivity of the second under explored despite being the one used in practice. Additionally, the authors define stability in one way but then prove the stability of their model using a slightly different notion. This could benefit from clearer alignment and explanation. Specifically, the definition of stability should be directly aligned with the stability result, and the implications of this specific definition should be discussed in more detail.

4. The paper [3] provides a similar analysis, outlining expressivity bounds of previous methods using laplacian eigenvectors and proposing a new architecture. A comparison between the results of that work and the current paper could offer valuable insights and strengthen the positioning of this paper’s contributions. The absence of a detailed comparison with this work leaves a gap in understanding the relative advantages and disadvantages of the proposed approach.

5. While the results on the QM9 benchmark are promising, it would be helpful to include a comparison with other methods that also use Laplacian eigenvectors on this dataset. This would provide a more comprehensive view of the performance of the proposed method relative to other spectral methods.

### Questions
The paper states that "taking inner products can potentially lose much of the rich structural and positional information carried by vanilla Laplacian eigenvectors." However, it seems to me that the inner product, which serves as a projection matrix onto the corresponding eigenspace, should preserve all the information about that space. I thought that the added expressivity comes from using more expressive point cloud architectures rather than the inner product itself.  Could the authors provide a more detailed explanation or proof of what specific information, if any, is lost when taking inner products of eigenvectors compared to using the raw eigenvectors? Additionally could the authors clarify whether the increased expressivity comes primarily from the expressive power of point cloud architectures rather than avoiding inner products?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper improves GNNs by incorporating Laplacian eigenvectors to capture global graph properties, addressing limitations in local message-passing approaches.  The proposed method uses learnable O(p)-invariant representations for each Laplacian eigenspace of dimension p and handles close eigenvalues in a smooth fashion, enhancing robustness and expressivity. Experiments show competitive performance, especially in capturing global graph characteristics.

### Strengths
1. The proposed OGE-Aug method is theoretically robust, demonstrating strong expressiveness and stability. The underlying motivation is both novel and compelling.
2.  Empirical experiments indicate that OGE-Aug performs competitively and holds promise for real-world applications.
3. The theoretical contributions of this paper are sufficient, and the proofs appear sound.

### Weaknesses
1. The proposed OGE-Aug method is intricate, highly complex, and challenging to implement. In this paper, the authors present a simplified version using a Cartesian tensor-based point cloud network, which introduces a gap between the theoretical framework and practical implementation. The simplification to a Cartesian tensor-based point cloud network, while perhaps necessary for computational feasibility, raises concerns about whether the implemented model truly captures the theoretical properties of the proposed OGE-Aug method. Specifically, the theoretical framework suggests a universal point cloud network operating directly on the Laplacian eigenvectors, whereas the implementation uses a more constrained architecture. This discrepancy needs further justification and analysis.
2. This paper's writing is rough and difficult to read and follow. First, I recommend that the authors adopt the notation guidelines suggested by the ICLR template. In the current version, symbols such as V are used interchangeably to represent different elements, like sets and matrices, which makes the paper challenging to interpret. Second, the implementation of OGE-Aug should be presented with more detail, ideally including a pseudocode. The lack of a clear pseudocode makes it difficult to understand the precise steps involved in the practical implementation of OGE-Aug. The description of the Cartesian tensor-based point cloud network is also somewhat vague, lacking specifics on the tensor order and how it relates to the number of Laplacian eigenvectors used. This ambiguity hinders reproducibility and a deeper understanding of the method.
3. There is no available code to reproduce the results or gain a deeper understanding of the method’s details.
4. In the experiments, the primary baselines are Laplacian-based embedding methods, but some recent state-of-the-art methods, such as Exphormer [1] on the PCQM-Contact dataset, are missing. The absence of comparisons with state-of-the-art methods like Exphormer [1] limits the ability to assess the true performance of the proposed method. The choice of baselines seems biased towards Laplacian-based approaches, which may not provide a comprehensive evaluation of the method's capabilities.
5. While the experiments include four different datasets or benchmarks, incorporating additional datasets or widely-used benchmarks, such as the OGB benchmark (e.g., ogbg-molhiv, ogbg-molpcba), could further strengthen the evaluation. The limited number of datasets and the lack of commonly used benchmarks like OGB raise concerns about the generalizability of the results. The inclusion of more diverse datasets would provide a more robust assessment of the method's performance across different graph structures and tasks.

### Questions
1. Please begin by clarifying the weaknesses section.
2. Could the authors provide an empirical comparison of training costs with the most competitive baselines?

### Soundness
3

### Presentation
2

### Contribution
2
