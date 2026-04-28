# DUALFormer: A Dual Graph Convolution and Attention Network for Node Classification

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Graph Transformers (GTs), adept at capturing the locality and globality of graphs, have shown promising potential in node classification tasks. Most state-of-the-art GTs succeed through integrating local Graph Neural Networks (GNNs) with their global Self-Attention (SA) modules to enhance structural awareness. Nonetheless, this architecture faces limitations arising from scalability challenges and the trade-off between capturing local and global information. On the one hand, the quadratic complexity associated with the SA modules poses a significant challenge for many GTs, particularly when scaling them to large-scale graphs. Numerous GTs necessitated a compromise, relinquishing certain aspects of their expressivity to garner computational efficiency. On the other hand, GTs face challenges in maintaining detailed local structural information while capturing long-range dependencies. As a result, they typically require significant computational costs to balance the local and global expressivity. To address these limitations, this paper introduces a novel GT architecture, dubbed DUALFormer, featuring a dual-dimensional design of its GNN and SA modules. Leveraging approximation theory from Linearized Transformers and treating the query as the surrogate representation of node features, DUALFormer \emph{efficiently} performs the computationally intensive global SA module on feature dimensions. Furthermore, by such a separation of local and global modules into dual dimensions, DUALFormer achieves a natural balance between local and global expressivity. In theory, DUALFormer can reduce intra-class variance, thereby enhancing the discriminability of node representations. Extensive experiments on eleven real-world datasets demonstrate its effectiveness and efficiency over existing state-of-the-art GTs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DUALFormer, a novel Graph Transformer model designed to address scalability challenges and improve local-global information fusion. The approach is both simple and theoretically grounded. Extensive experiments demonstrate DUALFormer’s effectiveness, scalability, and robustness.

### Strengths
1. This paper is well-motivated.
2. The proposed method is simple and effective.
3. The inclusion of theoretical analysis strengthens the work.
4. Extensive experiments show the effectiveness, scalability and robustness.
5. This paper is easy to follow.

### Weaknesses
1. The proposed method can be interpreted as "attention on attributes". I wonder how is it different from the standard self attention. Especially why it can perform better on node classification? And when it is expected to perform better and when not?
2. Can you provide further analysis, such as case studies, to further explain the semantic meanings of the "attention on attributes"?
3. Can you provide further analysis and empirical studies to show that the GNNs after the graph Transform can indeed learn the localities in graphs?

### Questions
N.A.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To address the scalability limitations of graph transformers (GTs) and the challenge of balancing local and global information, this paper introduces DualFormer, a novel GT architecture. DualFormer calculates global attention along the feature dimension, enabling the model to perform effectively and efficiently on large graphs while maintaining strong performance.

### Strengths
- The writing is generally clear and accessible, making the paper readable and easy to follow.
- The proposed method is both understandable and implementable, yet effective. It performs well on several datasets.
- The paper includes diverse experimental analyses, such as node classification, node property prediction, ablation studies, and parameter sensitivity analyses. Furthermore, the authors offer theoretical guarantees to support the method.

### Weaknesses
 - The motivation for the study is not fully convincing. Further details are provided in the questions below.
- Since the paper emphasizes the method’s scalability, additional experiments on larger graphs would reinforce this claim. Suggested datasets include *Roman-Empire*, *Question[1]*, *Wiki*, and *ogbn-papers100M*. Moreover, the GNN baselines in Tables 2 and 3 are outdated, which may reduce the persuasiveness of the results. For instance, the statement, “Most GTs consistently show superior performance over GNNs across all datasets” (line 451), would be more convincing if compared with recent GNN baselines, such as *ChebNetII[2]* and *OptBasis[3]*, to present a more comprehensive evaluation. Specifically, the performance gains over strong baselines such as ChebNetII and OptBasis are not clearly established, and it is unclear whether the proposed method offers a significant advantage over these more recent GNN architectures.
- Minor Issues: There are a few typographical errors, such as "abov" (line 182). Consistent notation throughout the paper is also preferable. For instance, in line 168, there is a "$\times$" symbol between a scalar and a matrix, but not in line 216. Additionally, line 191 includes a "$\cdot$" between matrices, whereas line 167 does not.

### Questions
- The first question concerns the reasonableness of applying softmax to the global correlations between features.

  - In standard self-attention, $ \mathbf{O} = \exp(\text{sim}(\mathbf{Q}, \mathbf{K}))\mathbf{V} $ (Eq. 6).
  - Through linearized attention, $ \mathbf{O} = \phi(\mathbf{Q}) \phi(\mathbf{K})^\top \mathbf{V} $ (Eq. 11), where each element in $ \phi(\mathbf{Q}) \phi(\mathbf{K})^\top $ is non-negative, representing attention weights (global dependencies between nodes).
  - By the commutative property of matrix multiplication, $ \mathbf{O} = \phi(\mathbf{Q}) (\phi(\mathbf{K})^\top \mathbf{V}) $, so we can interpret $ (\phi(\mathbf{K})^\top \mathbf{V}) $ as a correlation matrix (with elements that can be positive or negative).

  However, in Eq. 13, $ \mathbf{V} \text{softmax}(\mathbf{Q}^\top \mathbf{K}) $, i.e., $ \mathbf{Q} \text{softmax}(\mathbf{K}^\top \mathbf{V}) $, differs from $ \phi(\mathbf{Q}) (\phi(\mathbf{K})^\top \mathbf{V}) $ because elements in $\text{softmax}(\mathbf{K}^\top \mathbf{V}) $ are all non-negative, unlike those in $ (\phi(\mathbf{K})^\top \mathbf{V})$. Could you clarify these differences and explain why it is reasonable to replace $ \phi(\mathbf{Q}) (\phi(\mathbf{K})^\top \mathbf{V}) $ with $ \mathbf{Q} \text{softmax}(\mathbf{K}^\top \mathbf{V}) $?

- The second question pertains to the interpretation of the proposed global attention. The method appears to aggregate information along the feature dimension, unlike previous approaches that gather global information across all or most nodes in a graph. For a one-dimensional feature, $ \mathbf{V}  \text{softmax}(\mathbf{Q} \mathbf{K}^T) $ in Eq. 13 reduces to $ \mathbf{V} \cdot \alpha $, where $ \alpha $ is a scalar and $ \mathbf{V} \in \mathbb{R}^{n} $. How can this be understood as gathering information from a global perspective?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces DUALFormer, a graph transformer that tackles the challenges of the scalability and trade-off between local and global expressivity faced by current models. The motivation is to model the global dependencies among nodes by approximately characterizing the correlations between features. DUALFormer adopts a simple, intuitive design that includes local graph convolutional networks operating on the node dimension and a global self-attention mechanism operating on the feature dimension. The effectiveness and efficiency of the proposed DUALFormer are demonstrated in experimental evaluations across node classification and node property prediction tasks.

### Strengths
1) The motivation for the dual design of local and global modules in this paper is clear and interesting.
2) The model DUALFormer is simple and efficient with a solid theoretical foundation. 
3) The paper offers extensive experimental validation across various datasets. 
4) The paper is well-organized and easy to read.

### Weaknesses
1) The paper has some minor errors that need fixing. For example, Table 2 misses the mean value for the GraphGPS model on the Citeseer dataset. 
2) To enhance readability, Equation 13 should be split into two or three equations. 
3) The model DUALFormer places the GNN layers, such as the SGC layers, after the attention layers. What is the rationale behind this design? Is it possible to reverse this order? 
4) Figure 4 shows that the model utilizing APPNP outperforms the one using SGC in the Cora and Pubmed datasets. What accounts for this performance difference?
5) The effect of certain hyper-parameters, such as the parameter $\alpha$ in Equation 13, on performance has yet to be unverified. 
6) The paper does not mention any plans to open-source the code.

### Questions
Update after carefully reviewing the authors' responses: no further concerns

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper develop a new architecture based on GNNs and modified Transformers. The authors conduct expensive experiments as well as theoretical analysis to show the effectiveness of the proposed method.

### Strengths
1.  This paper is easy to follow.
2.  The authors provide the theoretical analysis.
3.  The results on various datasets seem to be promising.

### Weaknesses
1.  The comparison of efficiency study seems to be not reasonable.
2.  The key contributions of the proposed method are not clear.
3.  The complexity analysis of the proposed method seems to be wrong. 
4.  As the authors claim in Eq. 13, the proposed method only captures the feature-to-feature correlations. In my opinion, it is not the global information on the graph since it is unable to capture the relations between nodes. Why do authors claim the proposed method can capture the global information on the graph?
5.  According to the paper, the efficiency is the most important contribution of the proposed method. I think the authors express this point in a wrong way. Firstly, the authors claim that the computational complexity of the proposed method is $O(n)$ which is obviously wrong. Based on Eq. 14, the calculation involves the adjacency matrix. Hence, the computational complexity of this part is $O(E)$ and it is cannot be ignored since $|E|>|N|$ （even $|E|>>|N|$ on some graphs). Then, the authors only compare the time cost of each epoch to demonstrate the efficiency which is not reasonable. I think the total training time cost is the most important metric to demonstrate the efficiency of a method. So, the authors should report the overall training cost of each method for efficiency study, especially on large-scale graphs.  Maybe authors can refer to the settings in NAGphormer. For instance, can the proposed method achieve more efficient and more powerful performance than NAGphormer on Aminer, Reddit and Amazon2M?
6.  As shown in Section 4.2,  DUALFormer relies on the sampling strategy to perform on large-scale graphs, just like advanced linear graph Transformers. Hence, I think the GPU memory comparison is questionable since it is largely related to the batchsize. Do authors set the same batch for each method?
7.  The analysis of the $\alpha$ is missing. According to Table 5, the performance of DUALFormer could be sensitive to the value of $\alpha$. So, the parameter analysis of $\alpha$ should be added into the experiment section.

### Questions
I have the following questions:
1.  As the authors claim in Eq. 13, the proposed method only captures the feature-to-feature correlations. In my opinion, it is not the global information on the graph since it is unable to capture the relations between nodes. Why do authors claim the proposed method can capture the global information on the graph?
2.  According to the paper, the efficiency is the most important contribution of the proposed method. I think the authors express this point in a wrong way. Firstly, the authors claim that the computational complexity of the proposed method is $O(n)$ which is obviously wrong. Based on Eq. 14, the calculation involves the adjacency matrix. Hence, the computational complexity of this part is $O(E)$ and it is cannot be ignored since $|E|>|N|$ （even $|E|>>|N|$ on some graphs). Then, the authors only compare the time cost of each epoch to demonstrate the efficiency which is not reasonable. I think the total training time cost is the most important metric to demonstrate the efficiency of a method. So, the authors should report the overall training cost of each method for efficiency study, especially on large-scale graphs.  Maybe authors can refer to the settings in NAGphormer. For instance, can the proposed method achieve more efficient and more powerful performance than NAGphormer on Aminer, Reddit and Amazon2M?
3.  As shown in Section 4.2,  DUALFormer relies on the sampling strategy to perform on large-scale graphs, just like advanced linear graph Transformers. Hence, I think the GPU memory comparison is questionable since it is largely related to the batchsize. Do authors set the same batch for each method?
4.  The analysis of the $\alpha$ is missing. According to Table 5, the performance of DUALFormer could be sensitive to the value of $\alpha$. So, the parameter analysis of $\alpha$ should be added into the experiment section.

### Soundness
3

### Presentation
3

### Contribution
2
