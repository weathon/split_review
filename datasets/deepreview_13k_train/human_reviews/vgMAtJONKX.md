# Towards Accurate Validation in Deep Clustering through Unified Embedding Learning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Deep clustering integrates deep neural networks into the clustering process, simultaneously learning embedding spaces and cluster assignments. However, significant challenges remain in evaluating and comparing the performance of different deep clustering algorithms—or even different training runs of the same algorithm. First, evaluating the clustering results from different models in the same high-dimensional input space is impractical due to the curse of dimensionality. Second, comparing the clustering results of different models in their respective learned embedding spaces introduces discrepancies, as existing validation measures are designed for comparisons within the same feature space. To address these issues, we propose a novel evaluation framework that learns a unified embedding space. This approach aligns different embedding spaces into a common space, enabling accurate comparison of clustering results across different models and training runs. Extensive experiments demonstrate the effectiveness of our framework, showing improved consistency and reliability in evaluating deep clustering performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a model that searches the common representations from multiple learned representations of different methods via clustering. Additionally, this architecture can serve as an evaluation metric for comparing various clustering methods. The paper is well-organized and easy to follow. However, I have some concerns. The techniques used in this paper, including all modules and evaluation metrics, do not appear novel.

### Strengths
1. The whole paper is easy to follow and well-organized.

2. The motivation is clear.

### Weaknesses
1. The model itself lacks originality; the unified similarity matrix learning module appears to be derived from [1], and the unified embedding space learning module closely resembles IDEC [2].

2. Equation (4) means that $U$ should more closely approximate $S^{(m)}$ as their Euclidean distance decreases. But all $S^{(m)}$ is learned during the optimization process, relying on the unreliable metric to decide their optimization trends, does this point make sense? It could cause performance to depend heavily on how to initialize the weight $w$.

3. Lacking clear evaluation details. The paper does not specify which variables were used to calculate the NMI and ACC scores.

4. Why do results from all spaces sometimes outperform those from the unified space, while in other cases, the unified space outperforms all spaces? Please analyze this point clearly.

5. The t-SNE visualization comparing the unified embedding with the coupled embeddings should be included.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new deep clustering evaluation framework, which aims to solve the problem that different deep clustering algorithms are difficult to compare and evaluate in high-dimensional space. Experimental results show that this method outperforms traditional methods in terms of accuracy and consistency of internal evaluation, which helps to more reliably evaluate clustering performance.

### Strengths
1. By unifying the embedding spaces of different models into a common space, the evaluation bias caused by different algorithms or parameters can be reduced, making the evaluation results more consistent.

2. Through experimental verification, the method in the paper shows higher reliability when using internal evaluation indicators (such as Silhouette score, Calinski-Harabasz index, etc.), and is highly correlated with external evaluation indicators (such as clustering accuracy).

3. Compared with traditional embedding methods that require frequent parameter adjustment, the main steps of the unified embedding space method do not rely on specific parameters, are simple to operate and easy to promote.

### Weaknesses
1) The font of the text in the figure should be consistent with the font of the text;


### Questions
1) this work relies on Euclidean distance as a similarity metric. In some deep clustering tasks, other distance metrics (such as cosine similarity) may perform better. Can your evaluation framework maintain consistent results under different similarity metrics?

2) the aothurs focus on preserving the local structure of the data to improve clustering accuracy. However, on some datasets, preserving the global structure may be equally important. In the process of generating the unified embedding space, have you considered balancing the impact of local and global structures? Does this method have limitations on datasets with particularly complex data distribution?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose a novel internal cluster quality measure for deep clustering algorithms. The key idea is to learn a unified embedding space that algins different embedding spaces learned by deep clustering models into a common space. The unified embedding is then used to compare the different clusterings with commonly used internal cluster evaluation methods, like the silhouette score.

### Strengths
**Originality**
- The idea of combining multiple embeddings learned from deep clustering methods to achieve a unified embedding to compare different clustering solutions is interesting.

**Quality**
- Evaluation across a wide range of diverse data sets and three different internal cluster evaluation methods provides good evidence for their proposed evaluation procedure.

**Clarity**
- The method description and Figure 1 illustrate the method clearly

**Significance**
- Internal cluster quality measures are of high significance for the deep clustering community. I would even say that it is one of the most pressing issues that holds back the application of deep clustering algorithms in practice. Currently, almost all deep clustering methods need to be tuned with access to ground truth labels, which is fine for method development, but is not a realistic use case for clustering in practice. Therefore, the presented  work is of high significance to the deep clustering community.

### Weaknesses
 **Originality**
- Existing work (Figure 4 in Lowe et al, 2024) provides already a large-scale analysis of internal cluster measures (silhouette score) for clustering methods in embedding spaces. Their work shows that there is a strong correlation between the AMI (Adjusted Mutual Information) and the silhouette score computed in the UMAP reduced embedding space. This work should be discussed in the related work section so that it is clear, why the proposed method is necessary and a simple UMAP reduction for each embedding would not work.

**Quality**
- The selection of DEPICT and JULE for evaluation experiments is not well motivated. There are many more “foundational” deep clustering methods that are widely used and have inspired many follow-ups, e.g., DEC (Xie et al, 2016), IDEC (Guo et al, 2017), DCN (Yang et al, 2017). Further, only autoencoder-based methods are compared and no recent contrastive methods, like Contrastive Clustering (Li et al, 2021), SCAN (Van Gansbeke et al, 2020) or SeCu (Qi 2023). I understand that it is not feasible to compare with every deep clustering method there is, but the selection of methods in your experiment section should be clearly motivated. For example, take one or two methods from each deep clustering family, like k-means based, hierarchical clustering based, density based… and with different representation learning objectives, like autoencoder and contrastive learning.

**Significance**
- My concern with the proposed method is that it might not be very useful in practice, as it requires multiple embedded spaces that need to be learned first with deep clustering methods. This makes it quite expensive to compare clustering solutions. Furthermore, the method's practical utility is questionable since it necessitates multiple runs of the same deep clustering algorithm to generate diverse embeddings, which is computationally expensive. The paper lacks an ablation study demonstrating how many candidate embedding spaces are required to achieve reliable performance.

### Questions
- Are the internal cluster measures in the comparison representations (“all spaces”, “coupled spaces” and “raw space”) computed in a t-SNE reduced space or in the higher dimensional representation space? 

- How many embedding spaces are needed to learn a sufficiently representative “unified embedding”?

- Please justify the selection of JULE and DEPICT for your main experiments. If possible, add further deep clustering methods to your evaluation. See discussed weakness.

- Please explain how your approach relates to the results in Lowe et al. (2024). I would like to see a clear motivation of why your method is needed and a simpler baseline like UMAP reduced embeddings does not work. See also the corresponding discussed weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses challenges in evaluating deep clustering methods, particularly discrepancies in comparing clustering results across different models due to varying learned embedding spaces. The authors propose a novel evaluation framework that introduces a unified embedding space for more accurate comparisons. This unified space aligns embeddings from multiple clustering results into a consistent representation, making internal validation measures more reliable and reducing inconsistencies. The proposed approach is empirically validated across several datasets, demonstrating improved accuracy in ranking clustering results.

### Strengths
- The authors provide thorough theoretical analyses of the limitations of traditional clustering evaluation approaches. They highlight the pitfalls of using internal validation measures in high-dimensional input spaces due to the curse of dimensionality and demonstrate the inconsistencies that arise when using these measures on coupled embedding spaces generated by different clustering models.
- The proposed method is evaluated extensively across several benchmark datasets, including MNIST, COIL, UMist, and others. The empirical results consistently show that the unified embedding framework outperforms traditional approaches (i.e., raw space, coupled space, and averaging across all spaces) in terms of rank correlation with external validation metrics.

### Weaknesses
 - The proposed approach resembles multi-view learning methods, particularly in S1 where a fusion weight and unified similarity matrix are learned, and S2 where a low-dimensional multi-view fused embedding is developed. This raises the question: Could most multi-view learning methods achieve similar unified spaces? If so, what differentiates the proposed method from existing multi-view techniques? The core issue is that the paper does not adequately clarify the novelty of their approach compared to existing multi-view methods that also aim to learn a unified embedding space. Specifically, the paper lacks a detailed comparison of the proposed method's optimization procedure with those used in established multi-view learning techniques. Without this, it's difficult to assess whether the proposed method offers a significant advancement over existing approaches.
- The quality of the unified embedding space may directly impact the framework’s ability to compare clustering models. If the unified space is not well-learned, how would this influence the reliability of the evaluations? The paper does not provide a clear mechanism to detect or mitigate the impact of a poorly learned unified space. The reliability of the entire evaluation framework hinges on the quality of this unified space, and without a method to assess its quality, the results could be misleading. For instance, if the unified space collapses to a trivial solution, the evaluation results would be meaningless.
- The framework requires several optimization steps, such as learning the unified similarity matrix and the unified embedding space, which may be challenging for large datasets. S1, in particular, might not scale well for massive datasets. How does the proposed approach address these scalability concerns? The authors’ claim that datasets of more than 10,000 samples represent a sufficiently large scale is not convincing—evaluation on larger datasets (e.g., the complete MNIST dataset) is strongly recommended. The computational complexity of the proposed method, particularly the pairwise distance calculations, could become a bottleneck when dealing with large datasets. The paper does not provide a detailed analysis of the computational cost and memory requirements for large-scale datasets. Furthermore, the lack of empirical validation on datasets larger than 10,000 samples raises concerns about the practical applicability of the proposed method.
- Comparisons are limited to only two clustering methods. To fully demonstrate the robustness of the evaluation approach, at least three different clustering models should be included. The paper does not provide sufficient evidence that the proposed evaluation framework is robust across a diverse range of clustering algorithms. The use of only two methods limits the generalizability of the results. It is crucial to demonstrate that the proposed framework can consistently rank clustering results across different types of algorithms, not just those within similar families.

### Questions
- How does the proposed method differ from standard multi-view learning methods, particularly those that also learn a unified embedding space by combining multiple views? Would it be possible to benchmark against a few of these existing multi-view learning methods (e.g., Completer, cvpr'21) to clarify the distinctions?
- Are there any existing clustering evaluation frameworks that could be used as baselines for comparison to better highlight the strengths of the proposed approach?

### Soundness
3

### Presentation
3

### Contribution
2
