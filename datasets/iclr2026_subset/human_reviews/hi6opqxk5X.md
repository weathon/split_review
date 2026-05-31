## Human Reviewer 1

### Summary
This paper proposes LSH-DBSCAN and LSH-HDBSCAN which are approximate versions of DBSCAN and HDBSCAN that can achieve provably subquadratic running time on high dimensional datasets. The main idea from the authors is to identify the core points via the LSH buckets and then form the clusters by an LSH assisted BFS that expands only within the buckets. The authors are proving this using theorems 3.1 and 3.2 along with the experimental results that were run on datasets MNIST, Fashion MNIST, ALOI and Glove. The experimental results were compared with exact DBSCAN and they reported the computation-count speedups and misalignment metric values which measures the discrepancy from exact DBSCAN.

### Strengths
The dataset assumptions are removed compared to Okkels et al paper.

The main algorithm is well written by dividing it into two phases making it easy to understand.

The preliminaries and theorems were also well written and explained and also proved in the appendix.

The SETH based lower bounds clarified that substantially better than quadratic exact algorithms are unlikely.

### Weaknesses
The authors compared the new algorithm only to exact DBSCAN. They were not compared to other implementations like DBSCAN++, DBSCAN with dimensionally reduced techniques like PCA/ UMAP, or HNSW. There are many algorithms claiming improved speed and accuracy in high dimensions.

The authors haven’t explained why there was a sudden decrease in the speedup in ALOI dataset when c = 7.0. Also, it shows a 53% misalignment which is very large compared to the other c value misalignments.
The authors haven’t mentioned anything regarding the space complexity and practical memory measurements.

The authors also use delta = 0.5 which is a very high failure probability value. They haven’t really explained why.

The authors also haven’t properly defined the variables. For example, in Definition 2.5, L is not defined. It is only later known what exactly is L.

There is nothing on practical performance. Which is unacceptable because there are already efficient version of dbscan available. The claim is on a provable speedup in high dimensions. But the algorithm is an approximate. So the claim should also be on accuracy with appropriate and fair comparisons.

Due to these important issues we think that this work is not of high impact at this current stage and more work is needed to highlight its importance.

### Questions
Could you please explain why there was a sudden decrease in speedup and also an increase in misalignment in the ALOI dataset when c=7.0?

Could you also include the comparisons with DBSCAN++, DBSCAN with dimensionally reduced techniques like PCA/ UMAP, or HNSW etc?

Could you also report the memory usage and also talk about the space complexity?

Also, could you provide a short theory or citation for the claimed linear time 2 approximation of Dmax in general metric spaces?

Also, could you please explain what is the base case C0? If Dmax gets over estimated, how does this affect the approximation mapping from definition 2.6?

Could you please explain the reason for choosing the value of 0.5 for failure probability value?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper presents fast algorithms for estimating DBSCAN* and HDBSCAN using LSH calculations.

### Strengths
The paper presents an algorithm to provably approximate DBSCAN and HDBSCAN clusterings in high-dimensional spaces, moving beyond the $O(dn^2)$ runtime to an $O(dn^{1 + 1/c^2})$ runtime for a $c$-approximation. This is a nice result and the speedups are correspondingly interesting. The experimental analysis is appropriate and the results are laid out in an intuitive manner.

### Weaknesses
I think this paper's primary weakness is that it operates within a vacuum and does not appropriately refer to the related work. Specifically, several of the results stated in the paper feel fairly straightforward as corollaries of known work but the present paper seems to re-derive them and present them as novel contributions. I present the intuition behind these ideas below.

First, there is the SIGMOD paper showing that HDBSCAN can be solved efficiently in a parallel setting [1]. Although the current work does not assume a parallel environment, many of the ideas around accelerating the connected component computation using fast distance estimation seems to carry over. Second, there is the work analyzing the theoretical properties of DBSCAN* (DBSCAN without border points) in [2]. This is the algorithm being analyzed in the present work as well, it seems. [2] shows that DBSCAN* operates under an ultrametric and implies that the bottleneck to calculating DBSCAN* clusterings is the calculation of this ultrametric. Thus, the authors' present work can be interpreted as a fast approximation of these ultrametric quantities. This then naturally coincides with [3], which shows that this ultrametric also extends to the HDBSCAN algorithm (and many other density-based clustering algorithms). Put simply, there is a set of references which suggest that producing the DBSCAN* and HDBSCAN clusterings reduces to calculating an MST under a specific distance metric.

The authors similarly omit any reference to calculating MSTs efficiently. It is known that EMSTs require $O(n^2)$ time, but that this can be accelerated using LSH and similar distance-estimation methods such as hierarchically well-separated trees (HSTs). [4] is an archetypal paper in this context, but there are many similar ones such as [5]. Indeed, [5] produces similar reductions to bichromatic matching as in the submitted paper.

As a consequence, it is difficult to understand whether the derivations in the present paper are re-discoveries of various pieces of known literature or if they are doing something new. It seems that the reductions have been shown in previous works and that the pieces exist around the literature. If the authors can convince me that what they have done is significantly dissimilar to the literature on (a) theoretical analyses of DBSCAN* and HDBSCAN, (b) calculations of MSTs and (c) existing reductions between these ideas and fast LSH or HST distance calculations, then I would be happy to raise my score. As it stands, however, I am unconvinced of the present paper's novelty.


References:
[1]: Wang, Yiqiu, et al. "Fast parallel algorithms for euclidean minimum spanning tree and hierarchical spatial clustering." Proceedings of the 2021 international conference on management of data. 2021.

[2]: Beer, Anna, et al. "Connecting the Dots--Density-Connectivity Distance unifies DBSCAN, k-Center and Spectral Clustering." Proceedings of the 29th ACM SIGKDD conference on knowledge discovery and data mining. 2023.

[3]: Draganov, Andrew, et al. "I Want'Em All (At Once)--Ultrametric Cluster Hierarchies." arXiv preprint arXiv:2502.14018 (2025).

[4]: March, William B., Parikshit Ram, and Alexander G. Gray. "Fast euclidean minimum spanning tree: algorithm, analysis, and applications." Proceedings of the 16th ACM SIGKDD international conference on Knowledge discovery and data mining. 2010.

[5]: Indyk, Piotr. "Algorithms for dynamic geometric problems over data streams." Proceedings of the thirty-sixth annual ACM Symposium on Theory of Computing. 2004.

### Questions
Most of my questions are implied throughout the "weaknesses" section. A few specific ones would be:
- Is it fair to say that the authors are presenting a fast mechanism for calculating the dc-dist between points?
- How does this differ from existing LSH- and HST-based MST calculation techniques?

Side note: I disagree with the statement that the results in the paper easily extend to the standard DBSCAN definition which also includes border points. Introducing border points breaks the ultrametric properties of the algorithm, making it (a) not compatible with HDBSCAN and (b) require additional computational steps. Although I think that DBSCAN* is a superior algorithm to DBSCAN, the authors present their work as if it is about DBSCAN. I disagree with this framing.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors present faster versions of DBSCAN and HDBSCAN based on LSH. 
While the basic versions are indeed slow, there is already a lot of research that accelerated them which the authors do not mention or compare to. Note that already ten years ago there were versions of DBSCAN with less than O(n^2), e.g., AnyDBC [0].
The experimental evaluation is very weak and the related work section has just a few lines that are not sufficient to cover the extensive related work in the field. 
The novelty is limited as LSH and DBSCAN both have been around for a while and DBSCAN has already been accelerated with LSH in other works, e.g., [1,2]. While the work is closely related to [3], the novel methods are not compared to it .
Furthermore, as the proofs are one of the main selling criteria, they should be contained in the main paper, at least as a proof sketch.


[0] Mai, S. T., Assent, I., & Storgaard, M. (2016, August). AnyDBC: An efficient anytime density-based clustering algorithm for very large complex datasets. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining (pp. 1025-1034).

[1] Shiqiu, Y., & Qingsheng, Z. (2019, October). DBSCAN clustering algorithm based on locality sensitive hashing. In Journal of Physics: Conference Series (Vol. 1314, No. 1, p. 012177). IOP Publishing.

[2] Keramatian, A., Gulisano, V., Papatriantafilou, M., & Tsigas, P. (2022, August). IP. LSH. DBSCAN: Integrated Parallel Density-Based Clustering Through Locality-Sensitive Hashing. In European Conference on Parallel Processing (pp. 268-284). Cham: Springer International Publishing.

[3] Okkels, C. B., Aumüller, M., Thomsen, V. B., & Zimek, A. (2025). High-dimensional density-based clustering using locality-sensitive hashing. In EDBT 2025 (pp. 694-706).

### Strengths
S1) The paper is well-written and easy to follow

S2) The speedup compared to baseline DBSCAN works very well and the method relies on less assumptions on the data than [3]

S3) Theoretically sound and proofs are given

### Weaknesses
W1) The experimental evaluation is not sufficient. 

a) Datasets like MNIST that consist of Gaussian clusters (with varying density) are not a good fit to density-based clustering. There exist a lot of benchmark datasets that actually contain density-based clusters, e.g. the DERIC benchmark (https://github.com/deric/clustering-benchmark), even if they are only low dimensional. For high-dimensional data, the COIL datasets work or also video data. Using only four datasets is not sufficient to show the quality and runtime in a statistically relevant way.

b) There is no comparison to competitors. Even if there are proofs in the paper, it is still important to see the behavior of your algorithms compared to related methods: Only then users can make an informed decision whether they want to use the accelerated version. 

W2) Related work is not discussed sufficiently, see in the summary. 

W3) Selection of parameters is not clear. How were the values for epsilon and minPts chosen? The authors state that they chose parameter values such that the results were "roughly consistent with ground truth clusters" - according to which measure? How close is roughly consistent? Were there several such settings?

### Questions
Q1) How did you chose the values for parameters? (see W3) 

Q2) How does your results compare in practice with similar methods (see Summary for suggestions)? In which (benchmark) datasets does it actually lead to an advantage to not have strong assumptions regarding the dataset? Can you provide real world datasets where the assumptions of [3] do not hold but your algorithm succeeds?

Q3) How did you choose the subset of ALOI data in the visualisation part?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
DBSCAN is a highly successful and well-known density-based clustering algorithm. However, due to its inherent computational complexity bottleneck, DBSCAN becomes impractical for large-scale datasets, particularly when the data reside in high-dimensional spaces. To address this limitation, the authors build upon the work of Okkels et al. (2025) and propose a c-approximation variant of DBSCAN, termed LSH-DBSCAN, which leverages the technique of locality-sensitive hashing (LSH) to achieve improved efficiency while maintaining approximate consistency with the results of the traditional DBSCAN in high-dimensional settings. Furthermore, the authors extend this approach to the hierarchical version and introduce LSH-HDBSCAN, which aims to provide an approximate yet computationally efficient counterpart to HDBSCAN with comparable theoretical guarantees.

### Strengths
**LSH-DBSCAN** and **LSH-HDBSCAN** are both highly intuitive and easy to understand, demonstrating strong reproducibility. Moreover, the authors provide solid theoretical backing for both methods, ensuring a certain level of cluster quality within a bounded computational complexity.

### Weaknesses
1. **Lack of methodological innovation**  
   The DBSCAN algorithm consists of two main components: *core point identification* and *cluster formation*. The computational complexity challenge primarily arises from the *core point identification* step. However, the authors closely followed the method proposed by Okkels et al. (2025) for this step, showing limited originality in their methodological contribution.

2. **Problems in the experimental design**  
   a) The experiments lack comparison with necessary baseline competitors. Many prior works have addressed improving the computational efficiency of DBSCAN, such as **DBSCAN++ [1]**, **sngDBSCAN [2]**, and more recently **sDBSCAN [3]** which specifically targets high-dimensional data. However, the authors only use the traditional DBSCAN as the baseline, failing to demonstrate the superiority of their proposed approach over existing methods.  

   b) The two evaluation metrics used in the experiments — *speed up* and *misalignment* — are not only difficult to interpret but also unintuitive. For time efficiency, it would be more straightforward to directly report the total runtime from start to finish. For cluster quality assessment, the authors should consider using common metrics from prior works, such as **Adjusted Rand Index (ARI)**, **Adjusted Mutual Information (AMI)**, and **normalized mutual information (NMI)**.

   c) Although **LSH-HDBSCAN** is mentioned as one of the main contributions, there is no corresponding evaluation of it in the experimental section.
   
   d) More large-scale high-dimensional datasets are also preferred to be shown in the experiment section, such as Pamap2 and Mnist8m.



3. **Overclaiming issues**  
   There are several instances of overclaiming throughout the paper. For example, in line 66, the authors state that their method “does not require any assumption on the dataset.” However, in Theorems 3.1 and 3.2, they explicitly assume that the dataset *P* is *LSH-friendly with quality $\rho$*. According to Definition 2.8, being LSH-friendly with quality $\rho$ requires satisfying $\rho(c) = \log(1/p_1) / \log(1/p_2)$.

   Second, in the abstract, the authors claim that their method provides “the *first provably* subquadratic runtime for approximate DBSCAN on arbitrary high-dimensional datasets.” However, Theorems 3.1 and 3.2 only guarantee *approximate results with high probability*, and similar-level theoretical guarantees have already been provided in previous works such as **sDBSCAN [3]**.

**Reference**

[1] Jang, J., & Jiang, H. (2019, May). DBSCAN++: Towards fast and scalable density clustering. In International conference on machine learning (pp. 3019-3029). PMLR.

[2] Jiang, H., Jang, J., & Lacki, J. (2020). Faster DBSCAN via subsampled similarity queries. Advances in Neural Information Processing Systems, 33, 22407-22419.

[3] Xu, H., & Pham, N. (2024). Scalable DBSCAN with random projections. Advances in Neural Information Processing Systems, 37, 27978-28008.

### Questions
According to Theorem 3.2, the time complexity of LSH-DBSCAN is $O(d \cdot n^{1 + 1/(2c^2 - 1) + o(1)})$, where a larger value of c should correspond to lower computational cost. However, although I do not fully understand how the *computational speedup* is calculated, the results in Table 2 for the ALOI dataset appear anomalous. Specifically, for the ALOI dataset, when \(c = 7.0\), the speedup is unexpectedly lower than that for both \(c = 6.0\) and \(c = 8.0\), while the misalignment is unusually high, reaching 0.53. Could you please explain why this is happened?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 5

### Summary
The authors present a fast algorithm for the DBSCAN problem based on Locality-Sensitive Hashing (LSH). They provide a provably sub-quadratic runtime for computing an approximate DBSCAN clustering in high-dimensional settings. To further extend their approach, they also propose an efficient approximation of the popular hierarchical variant, HDBSCAN. The paper provides both theoretical guarantees and empirical evaluations on benchmark datasets, showing computational speedups while maintaining low clustering error.

### Strengths
This paper provides the provably subquadratic-time algorithm for approximate DBSCAN and HDBSCAN in arbitrary high-dimensional spaces. The DBSCAN and HDBSCAN algorithms are easy to understand and implement. Experiments on 4 real-world datasets show that the proposed methods achieve speedups with minimal loss in clustering accuracy.

### Weaknesses
1. The authors state in Lines 64–66 that their algorithm does not rely on any dataset-specific assumptions. However, the time complexity in Theorems 3.1 and 3.2 depend on the assumptions that both the MinPts parameter m and the aspect ratio Δ are constant. The aspect ratio is typically assumed to be polynomially bounded in the input size n [1], and in the worst case, it can be exponentially large, up to 2^{n^{o(1)}} [2]. 

2. Okkels et al. (2025) have already applied LSH techniques to accelerate DBSCAN. The authors adopt a similar approach and extends it to the hierarchical setting of HDBSCAN, which represents only an incremental improvement.

3. To address the challenges of high-dimensional or general metric space, Mo et al. (2024) [3] recently proposed both exact and c-approximate DBSCAN algorithms with provable linear-time guarantees under low intrinsic dimensionality assumptions. This prior work is neither cited nor discussed in the current paper, and it is also missing from the experimental evaluation. 

[1] Bhaskara, A., Vadgama, S., and Xu, H. Greedy sampling for approximate clustering in the presence of outliers. In Proceedings of the 33rd International Conference on Neural Information Processing Systems, pp. 11146–11155, 2019.

[2] Cohen-Addad, V. Approximation schemes for capacitated clustering in doubling metrics. In Proceedings of the 31st Annual Symposium on Discrete Algorithms, pp. 2241–2259, 2020.

[3] Mo G, Song S, Ding H. Towards metric DBSCAN: exact, approximate, and streaming algorithms[J]. Proceedings of the ACM on Management of Data, 2024, 2(3): 1-25.

### Questions
1. Given that Δ can be as large as 2^{n^{o(1)}} in the worst case, how does the algorithm's runtime scale in such situations? Is the claimed sub-quadratic complexity still valid? 

2. Could the authors provide empirical evidence that Δ remains small in the datasets used for evaluation? Otherwise, how can we be confident that the reported runtime reflects the theoretical guarantees? 

3. The authors should provide comparative experiments with standard HDBSCAN.

4. The authors should include Mo et al. (2024) as a baseline to provide a more comprehensive evaluation.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
4

### Confidence
4