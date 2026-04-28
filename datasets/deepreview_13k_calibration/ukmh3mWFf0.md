# Attributed Graph Clustering via Coarsening with Modularity

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 5, 3, 3, 3

## Abstract
Graph clustering is a widely used technique for partitioning graphs, community detection, and other tasks. Recent graph clustering algorithms depend on combinations of the features and adjacency matrix, or solely on the adjacency matrix. However, in order to achieve high-quality clustering, it is necessary to consider all these components. In this paper, we propose a novel unsupervised learning framework that incorporates modularity with graph coarsening techniques and important graph regularization terms that improve the clustering performance. Furthermore, we also take into account Dirichlet energies for smoothness of signals, spectral similarity, and coarsening reconstructional error. The proposed framework is solved efficiently by leveraging block majorization-minimization, $\log\det$ of the Laplacian, smoothness and modularity, and is readily integrable with deep learning architectures such as GCNs and VGAEs in the form of losses. Extensive theoretical analysis and experiments with benchmark datasets elucidate the proposed framework’s efficacy in graph clustering over existing state-of-the-art methods on both attributed and non-attributed graphs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A new graph clustering method is proposed that combines graph coarsening with a modularity regularization term. They show how the objective can be optimized within a GNN-based architecture. They show experiments that show that the method performs well on several datasets.

### Strengths
The paper combines many machine learning techniques.

The resulting method seems to outperform existing methods in the experiments.

### Weaknesses
I don't know whether this paper is intended to be read by people from the field of community detection, but I can confirm that this paper is very hard to understand for someone with that background.

The introduction gives a bad overview of community detection. It does not refer to a good reference for modularity [1]. And it mentions that "In theory, a higher value of modularity is associated with better quality clusters.", which is a puzzling statement because modularity is a heuristic that does not have a strong theoretical underpinning. In addition, the paper mentions that the usage of modularity maximization has "plummeted over the years because they rely solely on the topological information", which I don't think is the case. Modularity maximization is still one of the most widely-used community detection methods, despite theoretical shortcomings [2,3]. Finally, it is mentioned that modularity maximization "requires intensive computations", but the Louvain algorithm runs in nearly linear time, and you can't really go faster than that.

The "Deep Graph Clustering" paragraph of the introduction is incredibly difficult to understand. It uses a lot abbreviations like ARGA, ARVGA, DAEGC, SDCN that are not (properly) introduced. After reading it, I still have no idea what is meant with "Deep graph clustering".

The NMI measure is biased towards fine-grained clusterings [4], while ARI also has its disadvantages [5]. I would recommend to use AMI and/or the correlation coefficient to measure the similarity between clusterings [5].

The paper contains many typo's, language and notation errors. 

They refer to Supplementary D for a summary of the datasets, but Supplementary D does not describe datasets at all.

### Questions
What is the difference between graph clustering, community detection and graph coarsening? The way I understand it, community detection is merely clustering of graph nodes based on the graph topology. Graph coarsening (as described in this paper) seems to be similar to blockmodeling [1]. At any rate, the differences between these three things (that seem to be combined in this paper), need to be clearly explained.

The method makes use of the constraint $X=C\tilde{X}$. If we substitute this constraint into the first term of (5), it would simplify to
$\text{tr}(\tilde{X}^\top C^\top\Theta C\tilde{X})=\text{tr}(X^\top\Theta X)$, which would simplify the optimization significantly. However, instead of enforcing this constraint exactly, the paper simply introduces an error term $\|X-C\tilde{X}\|$, which seems unelegant to me. Why don't you enforce this constraint exactly?

You mention that the log determinant term can be written as the sum of the log of the eigenvalues, and that this ensures that a 'minimal' number of eigenvalues are zero. However, doesn't this ensure that *not a single* eigenvalue is zero?

Is the complexity that is described in the "Complexity analysis" paragraph the complexity of a single iteration or of all the iterations until convergence?

I see that you rescaled the NMI, ARI and modularity to percentages. This is okay for NMI (though I'm not a fan of it), but for ARI it is confusing because ARI can be negative. For modularity, I have no idea how this rescaling is done, because the upper bound of modularity is smaller than 1 (and incredibly expensive to compute).

Why do you draw lines in Figure 2b instead of making a table? The points that are connected don't correspond to consecutive things.

[1] Peixoto, T. P. (2019). Bayesian stochastic blockmodeling. Advances in network clustering and blockmodeling, 289-332.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article develops a framework for unsupervised learning relying on modularity maximization jointly with attributed graph coarsening to solve a task of clustering of graph.
The main points are 1) to propose that in an optimization-based approach, where a Block Majorization-Minimization algorithm allows to solve the problem. Then, 2) the method is also integrated in GNN architectures for graph clustering. 
The work describes several aspects of related works, and conducts extensive numerical experiments to check the usefulness of the method.

### Strengths
- The idea of using modularity for graph coarsening is not novel (it dates back to 20 years),  yet its incorporation in on coarsening techniques, in an integrated way, appears to be novel and interestong.

- The article contains extensive numerical experiments, assessing when the proposed method works well. 

- There are good theoretical results on the method in Section 4. 

- Showing that the method integrates with GNNs is relevant and useful (even though it's, on my opinion), a little bit too detailed.

### Weaknesses
 - The idea of using modularity for graph coarsening is not novel (it dates back to 20 years),  yet its incorporation in on coarsening techniques, in an integrated way, appears to be novel and interestong.

- The article contains extensive numerical experiments, assessing when the proposed method works well. 

- There are good theoretical results on the method in Section 4. 

- Showing that the method integrates with GNNs is relevant and useful (even though it's, on my opinion), a little bit too detailed.

### weaknesses:
 - The results are a little bit disappointing as, according to Fig 4(b) and the final results, the full loss of eq (6) is not really needed. The modularity term does already a good job by itself, and the others appear to merely modify the results slightly -- even in a weird way as using only 1 term (relaxation of the constraint  or the $\ell_{1,2}$ norm regularizer) degrades the performance.

- The article is written is a dense way, possibly too dense, and one has trouble to identify the saillant points. 
I am not sure that the description of the integration of the method in 3 different deep learning methods for graphs is needed in the main text. The most relevant would be enough and it would leave more space to answer the questions asked underneath.

- the literature on modularity maximization does not appear to be well quoted. In this context, quoting 1 or 2 of the existing surveys would be expected and useful for the readers. Also there is a body of literature showing the limitations of the modularity, from its intrinsic resolution limit to it being considered 'harmful', and the present article does not say a word on that and on the impact of the weaknesses of the modularity to the present work.

### Questions
- In Fig 4(b) : why are the cases \alpha + \beta or \beta + \lambda so worse as compared to \beta alone ?

- There is always the possibility that the structure, E, are not aligned with the features, X. What would then happen ? The methods forces the smoothness of X on (V,E); is it always the case ? If it's not, is this supposition detrimental ? 

- What would happen if the clusters happen to be affected by the mentioned limits of the modularity ? 


- On the other side, modularity has been improved in the mast 10 years using the Non-backtracking random walks, then the Bethe-Hessian ansatz and several variations around that, to detect better clusters or modules. Could these improvements

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a node clustering model based on modularity maximization for attributed graphs. The clustering process is modeled as an optimization-based graph coarsening problem, and the final pseudo labels are retrieved from supernode relationships. However, despite the progress made in this work, I cannot recommend acceptance for it to be present at top-tier conferences such as ICLR. See my comments below for details.

### Strengths
* The literature review part is pretty detailed and comprehensive.
* The paper is well-organized and easy to follow.
* The proposed method is flexible and can be combined with various representation learning backbones.
* Promising clustering performances are obtained on widely used graph datasets.

### Weaknesses
 * The proposed clustering model (problem (5)) is a trivial combination of different previous works, none of (5) is designed by the authors, so the technical contribution of this work is marginal.
* The experiments are not inspiring. The authors conducted different experiments but presented their results without analyzing the reasons behind the scenes. See "Questions" below for a few ones I raised.
* The ablation studies part is trivial and not informative at all.
    * Visualization and Comparison of running times are generally not regarded as ablation studies.
    * Modularity Metric Comparison is interesting but its conclusion is pretty trivial:
> Even though modularity is a good metric to optimize for,
maximum modularity labelling of a graph does not always correspond to the ground truth labelling.
For this reason, it is important to have the other terms in our formulation as well.

      This is a common sense known as the "no free lunch theorem" in machine learning. We generally would like the ablation studies to uncover special and important characteristics of the proposed method, rather than trivial observations. The modularity comparison, while showing that the modularity term does contribute, doesn't provide any insight into the specific behavior of the proposed method, such as how the different loss terms interact or how the latent space evolves with different model choices. The analysis lacks depth and fails to provide a nuanced understanding of the method's inner workings.

### Questions
* In problem (5), why do you propose to optimize both $\tilde{X}$ and $C$ and use $\lVert C\tilde{X}-X\rVert_F^2$ to encourage the consistency, rather than optimizing $C$ only as K-means does?
* Keep the last question in mind, why do you optimize $C$ only in Section 4.2? That makes the experiments inconsistent with your proposal. In addition, what's the difference between the two strategies in terms of clustering performance?
* In Figure 2(b), what makes the proposed Q-GMM-VGAE faster than its backbone model GMM-VGAE? Are the experimental settings fair?
* In Table 1, SCGC and MVGRL have better performance but you marked the proposed method bold, why? Is it a typo?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel framework called Q-FGC for attributed graph clustering and its integration with deep learning-based architectures such as Q-GCN, Q-VGAE, and Q-GMM-VGAE. The authors conducted experiments on real-world benchmark datasets and demonstrated that incorporating modularity and graph regularizations into the coarsening framework improves clustering performance. Furthermore, integrating the proposed method with deep learning-based architectures significantly enhances clustering performance. The algorithms proposed in this paper are proven to be convergent and faster than existing state-of-the-art algorithms.

### Strengths
1) The authors proposed a novel optimization-based attributed graph clustering framework called Q-FGC.

2) The proposed algorithms are provably convergent and much faster than state-of-the-art algorithms.

### Weaknesses
1) The submitted title in the system (Attributed Graph Clustering via Coarsening with Modularity) is different from the title in the paper (ATTRIBUTED GRAPH CLUSTERING VIA MODULARITY AIDED COARSENING).

2) The research motivation is not sufficiently novel or clearly expressed. Additionally, there is an inconsistency between the motivation presented in the introduction and the abstract. For example, Dirichlet energies are stated in the Abstract, but they are not mentioned in Section Introduction. Besides, the reasons for using them are not explained. Reorganizing the abstract and introduction is recommended, particularly in the section discussing the motivation.

3) The novelty of this paper is not strong. The proposed method for improving the performance of graph clustering relies on modifying the existing FGC method. Furthermore, the paper fails to explain the shortcomings of the current FGC method and how incorporating modularity would enhance its performance. Overall, the impact of this paper on the field is not significant.

4) The related work section is not comprehensive enough. For instance, the paper does not cite important references such as Kumar M, Sharma A, Saxena S, et al. "Featured Graph Coarsening with Similarity Guarantees" presented at ICML 2023.

5) The experimental section lacks sufficient detail in its description. For example, the experimental setup is missing information. More specifically, the authors did not provide detailed experimental settings for the baselines. Additionally, the experimental section merely presents the experimental results without providing an explanation for the superior performance of the proposed algorithm in this paper.

6) The writing of the paper needs to be improved. There are also some typos in this paper.
- The algorithm (Feature Graph Coarsening (FGC)) is first given, but no references are given.
- There is a lack of punctuation in many parts of the paper. For example, “We compare the performance of our method against three types of existing state-of-the-art methods based on the provided input and type of architecture: a) methods that use only the node attributes b) methods that only use graph-structure c) methods that use both graph-structure and node attributes. The last category can be further subdivided into three sets: i) graph coarsening methods ii) GCN-based architecures iii) VGAE-based architectures and contrastive methods iv) largely modified VGAE architectures” should be “We compare the performance of our method against three types of existing state-of-the-art methods based on the provided input and type of architecture: a) methods that use only the node attributes; b) methods that only use graph-structure; c) methods that use both graph-structure and node attributes. The last category can be further subdivided into three sets: i) graph coarsening methods; ii) GCN-based architectures; iii) VGAE-based architectures and contrastive methods; iv) largely modified VGAE architectures.”).
- Several algorithms in Table 1 are missing references, and some do not provide experimental results.
- Figure 2 and Figure 4 do not have a caption (it is suggested to separate the tables in Figure 2(a) and Figure 4(a) from the figure itself).
- Equation 8 and Eqn. 8 => Eq. (8)
- Table 2a  => Table 2(a)
- In Section 5.2, the authors state that “Q-GCN is composed of 3 GCN layers”, but only two hidden sizes of 128 and 64 are provided.
- In section 5.2: “We surpass all existing methods…”  => “Our proposed model surpasses all existing methods...”
- The font size of the x-axis values in Figure 4(b) is too small.
- In section 5.1, “GCN-based architecures”   => “GCN-based architectures”

### Questions
1) In the Motivation of the introduction section, when stating that "We aim to utilize the feature graph coarsening framework (which does not perform well on clustering, as seen in the results) for graph clustering.", does the phrase "the results" refer to the experimental results in the experimental section? It is recommended to provide specific details on which results are being referred. Also, why does the feature graph coarsening framework not perform well on clustering?

2) Can more analysis be done in the experimental section on experiment settings? For example, could you please provide the experimental settings for the baselines and the hyperparameter settings for the proposed method, including learning rate, number of training iterations, dataset partitioning, and so on?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new method for clustering attributed graphs. The method is heavily based on a recent graph coarsening method, termed Featured Graph Coarsening (FGC), which was proposed by Kumar et al (2023) for coarsening attributed graphs. The authors in this paper introduces a modularity-based regularization term to the original optimization objective of FGC, and empirically show that the new formulation is useful for clustering attributed graphs. In addition, the authors demonstrate graph neural networks (GNNs) can be integrated in the proposed framework to further enhance the clustering performance.

### Strengths
The empirical comparisons presented in the main text, especially those in Table 1, are extensive.

### Weaknesses
 - Given that the proposed optimization objective in Equation 5 comes from simply adding a modularity-based regularization term $\mbox{tr}(C^TBC)$ to the original objective function of FGC (Kumar et al, 2023), the originality of this work is very limited, both methodology-wise and technical-wise. It looks like this paper simply (1) adds a regularization term to an existing work and (2) conducts some experiments on a few selected datasets. If there is something very novel, I would recommend the authors emphasize on those aspects.

- The overall quality/clarity of this paper can be significantly improved. First of all, there are a couple of ambiguous statements and overstatements. Here are some examples:
  - On page 1, in the second paragraph, the authors say that "... the Fiedler vector (the eigenvector of the second smallest eigenvalue of the Laplacian) produces a graph cut minimal in the weights of the edges (Fiedler, 1973)." As a reader I find it difficult to understand what "a graph cut minimal in the weights of the edges" means in this context. If the authors mean minimum cut, then I don't think this statement is correct. The relationship between the Fiedler vector and the minimum cut is not mentioned in the original paper (Fiedler, 1973), and in general it does not give rise to a minimum cut.
  - On page 1, in the second paragraph, the authors say that "... they assume each node gets mapped to one cluster, which is not consistent with real graph data." This is a clear overstatement. As far as I know, most of the node classification benchmarks used by the GNN community has non-overlapping clusters/classes. These include the 3 citations networks in Table 1, and several other attributed datasets from Table 3 in the appendix.

  In addition, the presentation can be greatly improved if proper definitions/citations are provided in the right place. Here are some examples:
    -  The term Feature Graph Coarsening (FGC) first appears at the end of page 1 without a citation. The authors should cite Kumar et al (2023) here.
    - Similarly, the abbreviation GNN appears at the end of page 1, but the full definition "Graph Neural Network (GNN)" only appears much later in Section 2, at the end of page 2.
    - In the first paragraph of Section 3.3, it is unclear what "the volume of inter-cluster edges" means. The authors should define it.
    - In Equation 1, the expression $\delta(c_i,c_j)$ is not defined.
    - In the first paragraph of Section 4.1, it is unclear what "the original graph is smooth" means. If the authors mean that the graph has smooth signals, they should just say "the original graph has smooth signals".

  There are also many typos and misplacements of mathematical symbols. I highly recommend the authors read the paper thoroughly and fix all the typos.

- Empirically, even though the authors compared with a number of other methods as shown in Table 1, the experiments are only carried over 3 small datasets. Table 3 in the appendix has more results on other datasets, but the authors only compare with two other methods, and one of them is just FGC.

- The proposed method has a lot of parameters, i.e. $\alpha,\beta,\gamma,\lambda$ in Equation 5. It is unclear how to select these parameters and how robust are the results with respect to the choice of these parameters.

### Questions
In the experiments, how did you pick the parameters $\alpha,\beta,\gamma,\lambda$? How robust are the clustering results with respect to the choice of the parameters?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
