# Dual-level Affinity Induced Embedding-free Multi-view Clustering with Joint-alignment

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Despite remarkable progress, there still exist several limitations in current multi-view clustering (MVC) techniques. Specially, they generally focus only on the affinity relationship between anchors and samples, while overlooking that between anchors. Moreover, due to the lack of data labels, the cluster order is inconsistent across views and accordingly anchors encounter misalignment issue,  which will confuse the graph structure and disorganize cluster representation. Even worse, it typically brings variance during forming embedding, degenerating the stability of clustering results.   In response to these concerns, in the paper we propose a MVC approach named DLA-EF-JA. Concretely, we explicitly exploit the geometric properties between anchors via  self-expression learning skill, and utilize topology learning strategy to feed captured anchor-anchor features into anchor-sample graph  so as to explore the manifold structure hidden within samples  more adequately.  To reduce the misalignment risk, we introduce a permutation mechanism for each view to jointly rearrange anchors according to respective view  characteristics. Besides not involving selecting the baseline view, it also can coordinate with anchors in the unified framework and thereby facilitate the learning of anchors.  Further, rather than forming embedding and then performing spectral  partitioning, based on the criterion that samples and clusters should be hard assignment, we manage to construct the cluster labels directly from original samples using the binary strategy,  not only preserving the data diversity but avoiding variance. Experiments on multiple publicly available datasets confirm the effectiveness of our DLA-EF-JA.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, a multi-view clustering method with joint anchor alignment was developed, which introduces dual-level affinity and achieves embedding-free clustering. The work is designed to address several problems due to the anchor misalignment issues. Therefore, the authors introduce a permutation mechanism for each view to jointly adjust the anchors. Besides, the method is free of learning the embedding by constructing the cluster labels directly from original samples. A self-expression learning structure is utilized on the anchors, which utilizes topology learning strategy to feed captured anchor-anchor features into anchor-sample graph. Extensive experiments validate the effectiveness of the proposed method.

### Strengths
1.	The paper is well-structured, and the authors conduct a relatively comprehensive review on existing literatures.
2.	The experimental results demonstrate the effectiveness of the work

### Weaknesses
1.	A core idea of the work is to introduce an anchor permutation matrix, while this idea has been widely adopted by previous works. Hence, the novelty of the paper might not be sufficient to be published.
2.	The comparison methods lack some latest works. Since the work is an anchor alignment based method, more related works with anchor alignment should be compared. For example, the reference Liu 2024 (in line 581) was discussed in this paper, which includes anchor alignment mechanism, but it is not compared with the proposed work.
3.	In Table 1, several compared methods exhibit extremely poor performance on some datasets (e.g., PMSC on Cora, AMGL on DeRMATO). It might be better if the authors could explain the possible reasons.
4.	Table 5 does not include all the symbols. The Methodology section might be too brief, which should be introduced with more details by explaining the reasons for the design of each component.

### Questions
1.	What is the difference between the anchor alignment module with those of existing works?
2.	Why do some compared methods exhibit extremely poor performance on some datasets?

### Soundness
3

### Presentation
3

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
This paper presents the DLA-EF-JA model, a multi-view clustering technique that leverages dual-level affinity to capture both anchor-sample and anchor-anchor relationships within data. The model introduces a joint-alignment mechanism to address the anchor misalignment problem across views, which eliminates the need for a baseline view. Unlike traditional embedding methods, DLA-EF-JA generates cluster labels directly, reducing variance and improving clustering stability. Extensive experiments across diverse datasets demonstrate that the proposed model achieves competitive performance compared to existing multi-view clustering methods.

### Strengths
1. The model’s dual-level affinity mechanism effectively captures both anchor-sample and anchor-anchor relationships, enhancing clustering accuracy by leveraging a fuller view of the data structure.
2. The flexible joint-alignment method addresses anchor misalignment issues without requiring a fixed baseline view, making the model versatile for clustering data from different sources.
3. The model's effectiveness is demonstrated through comprehensive evaluation on multiple datasets, highlighting its adaptability and strong performance across different data types and views.

### Weaknesses
1. **Limited Learning of Cross-View Complementarity:** While the model integrates anchor relations, it lacks complex constraints like the Schatten p-norm that could help capture deeper cross-view complementarities. This may limit the model’s ability to fully leverage unique, complementary information in views with highly distinct features or dimensions. How does the model handle scenarios where the quality of anchors varies significantly across different views? Specifically, if some views have noisy or poorly chosen anchors, how does the model prevent these anchors from negatively influencing the overall clustering result, given that all views contribute to the final consensus matrix?

2. **Necessity of Anchor Alignment:** The reliance on anchor alignment to maintain cross-view consistency introduces additional computational steps. Although this approach appears beneficial, some recent multi-view clustering methods successfully avoid alignment through feature space fusion or shared representations. It would be useful for the authors to elaborate on the essential role of anchor alignment in this model and under what conditions it might be adapted or simplified. Are there specific conditions or datasets where the necessity of anchor alignment might be relaxed or modified? For example, are there scenarios where the computational cost of alignment outweighs its benefits, or where simpler methods might achieve comparable results?

3. **Complexity of the Model:** The model is somewhat complex, introducing more variables and mathematical processes. A more detailed explanation of the transition from Equation 2 to Equation 3 would enhance reader understanding of the methodology. The introduction of multiple transformation matrices and weighting parameters increases the model's complexity, potentially making it harder to interpret and optimize. A clearer explanation of the rationale behind each step would be beneficial.

4. **Hyperparameter Tuning Requirement:** The model’s performance is sensitive to carefully tuned hyperparameters, such as λ and β. Can the authors provide further insights into the potential effects of anchor noise and how it could be mitigated to improve robustness? It would be beneficial to understand how the model's performance varies with different hyperparameter settings and how these settings interact with the quality and quantity of the input data. Additionally, how does the model address the challenge of selecting optimal hyperparameters, especially when dealing with noisy or high-dimensional data?

### Questions
Same as weaknesses section

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
5

### Summary
This paper aims to address these problems: (1) they existing methods focus only on the affinity relationship between anchors and samples, while overlooking that between anchors; (2) the cluster order is inconsistent across views and accordingly anchors encounter misalignment issue due to the lack of data labels. The proposed method explicitly exploits the geometric properties between anchors via self-expression learning skill, and utilizes topology learning strategy to feed captured anchor-anchor features into anchor-sample graph so as to explore the manifold structure hidden within samples more adequately. Experiments on multiple publicly available datasets confirm the effectiveness of the proposed method.

### Strengths
(1)  The proposed method considers the affinity relationship between anchors.
(2) The proposed method devises a joint-alignment mechanism that not only eliminates the need for selecting the baseline view but also coordinates well with the generation of anchors.
(3) The proposed method has linear complexity for the loss function.

### Weaknesses
 (1)  The novelty of this work is limited since the involved components have been widely used for anchor learning and spectral clustering. The authors only perform these components on the anchor data.
(2) The authors do not compare the proposed method with theses popular deep learning ones.

### Questions
The authors should check the data since some methods, such as OrthNTF and GSC, since the performance of these new methods is very poor.

### Soundness
3

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
5

### Summary
This paper proposes a dual-level affinity induced embedding-free multi-view clustering method with joint alignment, called DLA-EF-JA. Based on previous anchor based multi-view clustering, it further considers the relations among anchors by learning an affinity matrix that are used to guide the anchor matrix learning with graph Laplacian. The multi-view anchors are adaptively aligned. The discrete cluster indicator is also jointly learned.

### Strengths
1.	This paper is easy to read.
2.	Extensive experiments are conducted to show the effectiveness of the method as well as efficiency.

### Weaknesses
1.	The novelty of this paper is incremental. The authors consider the relations among samples by self-expression affinity learning, and add a graph based Laplacian for anchor matrix regularization. However, the self-expression affinity learning and graph based Laplacian are widely used in existing subspace clustering works. It also remains unclear why the anchor self-expression enhances the quality of anchors. Specifically, while self-expression is used to capture sample relationships in subspace clustering, it is not clear how applying it to anchors, which are representative points, provides a similar benefit. The paper lacks a clear explanation of how the self-expression of anchors contributes to better anchor selection or a more robust clustering solution. The connection between anchor self-expression and improved clustering performance is not well-established theoretically or empirically.

2.	Why learn an anchor affinity matrix $S_p$ for each view separately? It seems to overlook inter-view interactions. Why not directly learn a consensus anchor affinity matrix? Will it improve the performance? The current approach treats each view's anchor affinity independently, which may miss crucial cross-view relationships that could enhance the clustering. It's not clear why the authors chose to learn separate affinity matrices instead of exploring a joint affinity matrix that captures the shared structure across views. This raises questions about the potential suboptimality of the current approach and whether a consensus affinity matrix would lead to better performance by leveraging inter-view consistency.

3.	How do you set the number of anchors $k$? What is the influence of it?

4.	The experimental results are not convincing. For instance, OrthNTF achieves 69.4% Acc and 68.6% NMI values on the Reuters dataset, while this paper only reports 28.67% Acc and 3.07% NMI.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
