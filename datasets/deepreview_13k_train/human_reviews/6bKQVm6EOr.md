# Spectral Graph Coarsening Using Inner Product Preservation and the Grassmann Manifold

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
In this work, we propose a new functorial graph coarsening approach that preserves inner products between node features. 
Existing graph coarsening methods often overlook the mutual relationships between node features, focusing primarily on the graph structure.
By treating node features as functions on the graph and preserving their inner products, our method ensures that the coarsened graph retains both structural and feature relationships, facilitating substantial benefits for downstream tasks. 
To this end, we present the Inner Product Error (IPE) that quantifies how well inner products between node features are preserved. By leveraging the underlying geometry of the problem on the Grassmann manifold, we formulate an optimization objective that minimizes the IPE, even for unseen smooth functions. We show that minimizing the IPE also promotes improvements in other standard coarsening metrics. We demonstrate the effectiveness of our method through visual examples that highlight its clustering ability. Additionally, empirical results on benchmarks for graph coarsening and node classification show superior performance compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel graph coarsening strategy for graph neural networks based on the ability of the polling to preserve the input features and in general smooth features defined on the nodes of the original graph. In particular, the coarsening is performed through a coarsening matrix C (over the Stiefel manifold?), which is optimized to minimize |X^T L X - X_C^T L_C X_C|, where X_C and L_C are the coarsened features and laplacian matrices. Moreover, a further additional term promotes the preservation of smooth functions by minimizing the distance of C from the first k smallest eigenvalues of the Laplacian on the Grassmann manifold. Two variants are tested (with and without feature preservation loss) and compared on general coarsening metrics and node classification tasks.

### Strengths
The paper is generally well-written and easy to follow. My only comment is about introducing the importance given to the Grassmann manifold in the background and the relatively low importance given to the second term of the loss using it. At first, I was confused, not understanding where the Grassman manifold was coming into play in the definition of the first loss, to which most of section 3 (at least 3 and 3.1) is dedicated.

The proposed methodology is sound and theoretically founded (except for the first term, see weaknesses). The authors made theoretical connections between the proposed loss and some of the metrics used for evaluating graph coarsening methods.

The method compares favorably with other coarsening methods in most datasets and metrics.

### Weaknesses
 * I’m not sure eq 6 can be seen as the dot product between signals over nodes. Do you have any references for this?  For instance,” x^T L y” would be zero for any constant value of x and y. It might be interpreted as capturing some relationship between the smoothness of x and y, but I’m not sure. The interpretation of  $x^T L y$ as a measure of signal smoothness is not immediately obvious, and the paper would benefit from a more detailed explanation of this connection. Specifically, while it's true that $x^T L x$ is related to the Dirichlet energy of the signal $x$, the paper should clarify how this relates to the notion of smoothness and why minimizing the difference in this quantity between the original and coarsened graphs is a meaningful objective.

* Coarsening is posed as an optimization problem. This might be a problem on larger graphs, making the whole point of graph coarsening methods fail. It would be nice to understand what graph size the method can work with and the convergence speed/time of the methods compared with others. The computational cost of the optimization procedure is a significant concern, especially for large graphs. The paper should provide a more thorough analysis of the time complexity of the proposed method, including the cost of computing the gradients and the number of iterations required for convergence. It would also be beneficial to compare the computational cost of the proposed method with other graph coarsening techniques, particularly those that do not rely on optimization.

### Questions
Considering my previous comment on eq 6, I would like to understand how important it is to consider the relation between different functions rather than just the trace of eq6. In this case, wouldn’t your formulation contrast with FGC?

Minor:
* Fix the bibliography by updating arXiv with the published version when it exists.
* is the definition of L_c missing in 12
* what is mathcal{C} in eq 11?
* ordering of terms is not consistent between appendix and main (e.g. eq 19 and 20)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel graph coarsening method and presents a new definition that quantifies the inner products of node features. This approach effectively preserves both the global structure of the graph and the interrelationships among node features during the coarsening process, addressing the issue in previous methods that focused on global structure while neglecting node features.

### Strengths
1. The proposed method in the paper not only considers the interrelationships among node features but also maintains the global structure of the graph. Additionally, it leverages the properties of the Grassmann manifold to enhance the method's generalization capabilities. Experiments on graph coarsening and node classification demonstrate the effectiveness of this approach.
2. Building on the proposed INGC, the paper also introduces a simplified version, SINGC, which improves optimization efficiency. The node classification experiments in Section 4.3 further illustrate that SINGC performs well in clustering tasks involving large datasets.
3. The derivation of the formulas in the paper is presented in a clear and engaging manner. The notation is easy to understand, and the logical flow of the derivation is coherent and well-structured, supported by ample proofs and references.

### Weaknesses
1. In the experimental section of Chapter 4, the comparison methods for graph coarsening are limited to the FGC(2023) and the LVN and LVE(2018). This seems insufficient to demonstrate the effectiveness of the proposed method. It would be beneficial to include comparisons with additional methods, particularly those that also focus on preserving node feature relationships during coarsening, for a more comprehensive evaluation. The current selection of baselines does not fully explore the landscape of available graph coarsening techniques.
2. The paper lacks a complexity analysis. When introducing new definitions and solutions, it is important to provide corresponding analyses of time and space complexity. This is crucial for understanding the scalability and practical applicability of the proposed methods, especially when dealing with large-scale graphs. A detailed analysis should include the computational cost of each step in the algorithm.
3. The objective function (12) contains three hyperparameters: $\beta$, $\lambda$, and $\alpha$. The authors should explain how these parameters were selected and provide relevant parameter analysis experiments. The lack of a clear methodology for hyperparameter tuning makes it difficult to assess the robustness and generalizability of the results. It is essential to understand how sensitive the performance is to different parameter values.
4. The effects of the last two regularization terms in equation (12), $\lambda\| \boldsymbol{C}^{T} \|_{1, 2}^{2}$ and $\alpha\operatorname{l o g}{d e t} ( \boldsymbol{L}_{c}+\boldsymbol{J} )$, on the overall process are unclear, as there is a lack of relevant ablation experiments. Without these experiments, it is difficult to ascertain the individual contribution of each term and whether they are indeed necessary for achieving the reported performance.

### Questions
1. In Table 1 of Section 4.2, titled "GRAPH COARSENING METRICS," there is a metric labeled "INP," but the definition of this metric does not appear to be mentioned elsewhere in the text. Could you provide the specific mathematical expression for it?
2. Definition 5 states that the motivation for the Inner Product Error (IPE) is based on Theorem 1, which requires the graph to have (n−k) connected components. Do the datasets used in the experiments satisfy this condition? If the method is applied to other datasets, must they also meet this condition? If a dataset does not satisfy this requirement (i.e., if the graph has more or fewer than (n−k) connected components), how would that affect the experimental results?
3. We noticed that the coarsening rates chosen for the graph coarsening experiments (Table 1) and the node classification experiments (Table 2) differ. Should different experiments with various datasets have carefully selected coarsening rates? Would it be possible to conduct experiments with a uniform coarsening rate in the range of (0.3, 0.5, 0.7)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of simplifying large-scale graph data, crucial for fields such as social networks, biological systems, and recommendation systems, where graphs have become too large for traditional processing. The authors review existing graph reduction techniques: sparsification (removing edges and nodes), condensation (creating synthetic graphs for specific tasks), and coarsening (grouping similar nodes into super-nodes). While coarsening methods traditionally focus on structural properties, they often neglect node features, which are essential for many graph learning tasks. A recent approach, Featured Graph Coarsening (FGC), incorporates node features but still falls short of fully utilizing relationships between node attributes.

The authors propose a novel graph coarsening approach from a functorial perspective, treating node features as signals on the graph. Their method introduces a new metric, Inner Product Error (IPE), to measure preservation of inner product relationships between node features, aiming to maintain both structural consistency and feature relationships. This is achieved through an optimization process on the Grassmann manifold, enabling their model to generalize beyond observed features under a smoothness assumption. The method is validated through empirical results, showing that it not only maintains global structure but also outperforms state-of-the-art coarsening methods across several benchmarks, demonstrating improved utility and accuracy in graph coarsening and node classification tasks.

### Strengths
1. This paper introduces a functional perspective on graph coarsening by treating node features as functions (or signals) on the graph, a approach that differs significantly from traditional structural or feature-based coarsening methods. 

2. It seems the authors provide a rigorous formulation of their approach, deriving a new coarsening metric and implementing a gradient descent optimization process that aligns well with the theoretical framework. 

3.  By introducing IPE and optimizing on the Grassmann manifold, it seems this work potentially open doors for incorporating node feature relationships into coarsening, especially for applications like node classification that depend heavily on feature fidelity.

### Weaknesses
1. It is not clear why Inner Product Error (IPE), for preserving feature relationships in the coarsened graph, has the practical impact in real-world applications could be more comprehensively discussed.  For example, the authors could further clarify how preserving inner products between node features directly benefits graph-based tasks, like link prediction or graph classification.

2. The approach relies on a smoothness assumption for node features on the Grassmann manifold. However, this may limit its applicability to graphs with less smooth or heterogeneous node features. A discussion or experiment showing how the method performs under various levels of feature smoothness could clarify its robustness and potential limitations.

3. The paper's innovation is limited. It is an incremental improvement from several previous work such as presented in Loucas 2019, Kumar et al 2023, and some theoretical results are repeated from the above papers. See my questions below.

4. It seems the paper was written well overall, but some details are not clear or mistaken/wrong.  See questions below.

### Questions
1. The notation used in Equation (10) lacks coherence. For instance, it appears that the vector or matrix norm-0 represents the number of non-zero elements. If C_{:,i}​ denotes the i-th column of C, then by this notation, C^\top_{:,i} would be a corresponding (row) vector. Consequently, their norm-0 values should be identical. Therefore, having two conditions— one with ≥1 and another with =1— introduces a degree of inconsistency.   Please refer to Kumar et al (2023) for more exact definition

2. Theorem 1 is the repeat of Proposition 2.4 in Loucas 2019. No need to prove it again.

3. Traditional notation for matrix Frobenius norm \| M\|_F  means the square root of the sum of sqaured elements. Thus the term of Frobenous in eq (11) etc needs a square.

4. Could you please  elaboration on the second term (trace) in equation (11)?   That is your key point different from the objective used in Kumar et al (2023).  In my opinion the original objective in Kumar et al (2023) (without your first term) is more meaningful, as your first term condition is too strong.

5. Could you please given a more exact definition of l_{1,2}-norm used in the paper.  The l_{1,2} matrix norm is standard term which is defined as the sum of l_2 norms of all row (or column) vectors.  If this is the case, your derivative formula in Line 870 is incorrect.   Also I checked Kumar et al (2023) paper, I think it was defined as the sum of squared sum of rows.  Of course that was not correct too.  This way does not specify group-sparsity.  Taking sum in Kumar's case is because it was assumed for positive-element matrix. In your case, when the positive condition removed in (12) (from (10)), you need absolute operation, thus it makes your objective non-differentiable. 

6. In Theorem 3, although \kappa was introduced in your proof in Appendix, but it is better to define it Theorem 3. 

7. In Line 485, "we evaluate the classification performance on the original graph".  Can you give more details how this was done on the original graph?

8. You miss x in Line 783

### Soundness
2

### Presentation
2

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
The paper proposed a method for graph coarsening that preserves the information of graph structure and node features simultaneously.

### Strengths
1. The idea of using IPE for graph coarsening is new.
2. The proposed method outperformed the baselines in most cases.
3. The paper also includes some theoretical results.

### Weaknesses
 1. The implication of Theorem 3 hasn't been sufficiently explained. Particularly, is the $x_c$ in the theorem derived from the optimal solution of (12)?
2. Convergence analysis for Algorithms 1 and 2 is missing.
3. The computational complexity of the proposed algorithm hasn't been analyzed.  In addition, in Section 4.3, the authors should report the time costs of graph coarsening and GNN training (on the original graph and coarsened graph). If the time cost of coarsening is significantly higher than that of GNN training, graph coarsening is useless for accelerating GNN training.
4. The proposed algorithm has a few hyperparameters to tune but the authors haven't shown their influence and the related ablation study.


### Questions
1. In line 257, it was stated that the first term in (11) is not differentiable with respect to $C$. Why? 
2. As the $\ell_{1,2}$ norm is nonsmooth, how did the author handle this in the optimization?
3. More explanation about the role of the second term (beta-related) in (11) should be provided.
4. What is the advantage of IPE compared to ||X^TX-Xc^TX_c|| _F^2?

### Soundness
3

### Presentation
3

### Contribution
3
