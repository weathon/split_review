## Human Reviewer 1

### Summary
The task the article solves is memory-constrained ANN search, where both RAM and SSD are used to store the data and the index structure. The method proposed in the article is a hierarchical $k$-means index where the residuals of the first level ($m$ clusters) are clustered at the second level ($n$ clusters) globally, so that $mn$ clusters are obtained but only $m + n$ cluster centers have to be stored in memory. The authors augment this basic scheme by an efficient disk layout of the cluster points, where the nearby clusters are stored in nearby memory locations, and by query-aware dynamic pruning where a quadratic polynomial model is used to predict the query coverage, and the search is terminated early if the predicted 99\% coverage is reached.  The experimental results of the article show that the proposed method is both faster and more memory-efficient than the competing methods, such as DiskANN and SPANN.

### Strengths
[S1] The proposed method is intuitive and straightforward.

[S2] According to the empirical results of the article, the proposed method seems to work well in practice.

### Weaknesses
[W1] The methodolofical novelty of the work is limited: the proposed hierarchical clustering method seems to be Non-orthogonal inverted multi-index (NO-IMI) by Babenko & Lempitsky (2016) (the authors correctly acknowledge this earlier work) and the disk layout scheme is a straightforward implementation detail. Only the query-aware dynamic pruning seems to have limited novelty; however, in the context of hybrid memory-disk ANN search, Chen et al., (2021) use a more simple query-aware dynamic pruning method, and in the context of regular ANN search, Li et al. (2020) also use a model-based method (with more features and a different model than the current work). 

[W2] The claim that the proposed method has to store only $\mathcal{O}(\sqrt{N})$ centroids in memory is based only on the fact the that the authors select the number of centroids to be $\mathcal{O}(\sqrt{N})$  ($N$ denotes the number of data set points). However, traditionally $\sqrt{N}$ (see, e.g, Douze et al., 2025, p. 9) is the number of clusters that is recommended for non-hierarchical $k$-means index (IVF).  Thus, the experimental results have two omissions: a) Full hyperparameter sweeps should be performed (and Pareto frontiers should be reported, see, e.g., Aumüller et al, 2020, for a correct methodogy) to ensure that the memory saving and the improved recall of the proposed method compared to the baselines is not just due to the choice of hyperparameters. b) An ablation experiment should be performed, where the proposed hierarchical $k$-means index is compared to the regular $k$-means index with the same number of centroids $\mathcal{O}(\sqrt{N})$ to verify that it can indeed obtain a more accurate clustering with the same number of centroids stored in memory (I believe this should be the case). 

[W3] The notation is sloppy. Even on the very few formulas contained there are mistakes. For instance, I believe that in lines 288-289 it should be $\||q - (S_k + T_l)\||^2$ instead of $\||q - S_k T_l\||^2$. Also, dot product or matrix multiplication notation should be used when vectors are multiplied, e.g., $\langle S_k, T_l\rangle$ or $S_k^T T_l$, instead of $S_k T_l$.

References:

Aumüller, Martin, Erik Bernhardsson, and Alexander Faithfull. "ANN-Benchmarks: A benchmarking tool for approximate nearest neighbor algorithms." Information Systems 87 (2020): 101374.

Babenko, Artem, and Victor Lempitsky. "Efficient indexing of billion-scale datasets of deep descriptors." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016.

Chen, Qi, et al. "Spann: Highly-efficient billion-scale approximate nearest neighborhood search." Advances in Neural Information Processing Systems 34 (2021): 5199-5212.

Douze, Matthijs, et al. "The faiss library." IEEE Transactions on Big Data (2025).

Li, Conglong, et al. "Improving approximate nearest neighbor search through learned adaptive early termination." Proceedings of the 2020 ACM SIGMOD International Conference on Management of Data. 2020.

### Questions
I do not have any questions for the authors.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper proposes DiskHIVF, a memory-disk hybrid ANNS algorithm based on a two-level hierarchical IVF clustering scheme, along with layout reorganization optimizations and query-aware dynamic pruning tailored for this algorithm. Compared to baselines, DiskHIVF achieves a 1.2–2.3× speedup while reducing memory usage by 10–30×.

### Strengths
1) The use of IVF clustering leads to memory savings and retrieval acceleration compared to graph-based indexes (DiskANN, Starling) and the SPANN clustering index that allows inter-cluster crossing.

2) A greedy algorithm is employed to reorder cluster centers, optimizing the disk layout.

3) Polynomial fitting functions are used to predict the remaining workload, enabling pruning during the retrieval process.

### Weaknesses
1) While the proposed method is based on IVF clustering, the compared state-of-the-art baselines are graph-based indexes. Comparisons with more recent IVF-based disk indexes (e.g., Faiss, arxiv'24) in terms of memory capacity and performance are necessary. When constraining the cluster size to at least *d*, IVF-based disk indexes can also achieve O(N) memory space complexity. Thus, it is essential to compare the performance of IVF and DiskHIVF when their memory usage is similar or even more favorable for IVF.
Furthermore, the in-memory portion of DiskHIVF corresponds to a special case of IVF-PQ retrieval with the number of sub-vector segments (typically denoted as M) set to 1, where *n* corresponds to the number of IVF clusters and *m* to the size of the PQ codebook. Compared to a standard IVF-PQ index, this work retains the original vectors instead of quantizing them to PQ cluster centers. Therefore, comparisons with existing IVF-PQ-based disk indexes under similar parameter settings would make the results more convincing.

2) In Figure 2(b), a quadratic function is used to fit the budget curve without justification. However, for small values on the horizontal axis, the predicted curve shows an opposite monotonicity trend compared to the actual curve and exhibits significant numerical deviations. Is the use of a quadratic function appropriate? Would other functions, such as exponential functions, be more suitable for fitting this curve?

3) Performance is measured using average request latency (Section 4.3). However, according to Appendix A.2, on the DEEP dataset, although each cell is expected to contain only 10 points on average, the largest cell may contain up to 9000 points. Given the load imbalance across different cells resulting from this distribution, using tail latency as a performance evaluation metric would be more reasonable than average latency.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper proposes a two-layer hierarchical inverted index for billion-scale approximate nearest neighbor (ANN) search, aiming to reduce memory consumption. Experimental results indicate a 10–30× memory reduction compared to state-of-the-art methods.

### Strengths
Demonstrates impressive memory savings for billion-scale vector indices.

### Weaknesses
1.	Similarity to Existing Approaches
The proposed method appears conceptually similar to IVF+G+P, which also employs two-layer hierarchical clustering. IVF+G+P partitions data into K inverted regions and applies memory-efficient subregion grouping using a learned scalar α to interpolate new centroids. The paper should clarify the key differences and justify why the proposed approach is preferable. A direct comparison with other hierarchical inverted index methods would strengthen the contribution.
2.	Handling Skewed Data
Real-world datasets are often skewed, leading to imbalanced clusters. The paper does not address how the method handles skewed distributions or provide experiments on skewed datasets (e.g., SpaceV1B). This omission limits the practical applicability of the approach.
3.	Distance Metric Generalization
The design and optimization focus solely on L2 distance. It is unclear how the method adapts to other similarity measures (e.g., inner product). Including experiments on datasets requiring different distance types would improve generality.
4.	Limited Performance Metrics
The evaluation only reports average latency and recall. In real-world scenarios, tail latency and throughput are also critical. Based on disk access counts in Table 3, the proposed method may have lower throughput compared to DiskANN and SPANN since both algorithms are IOPS-bound. A more comprehensive performance analysis is needed.
5.	Incomplete Ablation Study
The pruning ablation study should include comparisons with alternative pruning techniques to better understand its advantage.
6.	Real-Time Updates
Modern vector indices often require real-time updates. The paper does not discuss how the proposed method supports dynamic insertions or deletions.

### Questions
1. Could you explain the rationale behind the final parameter setting: n=sqrt(N/10)×2.5 and  m=sqrt(N/10)/2.5?
2. What are the index build cost and time? Given that n and m remain large for clustering 10% of 1B data, what is the clustering overhead?
3. How does the proposed method perform in terms of tail latency and throughput compared to state-of-the-art solutions?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
The authors propose a new method for large-scale approximate nearest neighbor search. The proposed method, named DiskHIVF, uses the well-known Inverted File (IVF) approach where the data is clustered, and nearest neighbor queries are answered by only exploring certain number of clusters closest to the query.

Specifically, in their method, the authors propose using a hierarchical clustering and storing the points in the clusters on disk. This approach scales to large datasets because only the centroids need to be kept in memory, and the number of centroids is limited since the second-level centroids are shared in the hierarchical clustering. The authors perform their experiments on two million-scale and two billion-scale datasets.

### Strengths
The paper studies an important topic, and the proposed method achieves a low memory usage. The method is validated against appropriate baseline methods, and the experiments are performed on standard benchmark datasets, two of which are billion-scale datasets.

### Weaknesses
The work seems incremental, and the experiments are not particularly convincing. The core idea is similar to SPANN: use hierarchical clustering and store the clusters (inverted lists) on disk (storing the inverted lists on disk isa of course also otherwise a widely used practice, e.g. Faiss has OnDiskInvertedLists). The main difference is the type of hierarchical clustering used which reduces the number of centroids that have to be be kept in memory.

However, the proposed hierarchical clustering strongly resembles the NO-IMI structure [1, Section 3] which the authors cite but do not discuss the relation to. Moreover, SPANN (as well as DiskANN and Starling) already uses only 32GB of memory for a billion-scale dataset which is very reasonable (also, while the the authors write that "SPANN requires retaining approximately 16\% of vectors as centroids in memory", of course you can use less centroids even if performance saturates at 16\%).

As the proposed method is a combination of different ad hoc tweaks, it would be necessary to figure out which of these tweaks potentially give your method an edge. The correct way to do that would be to e.g. keep everything else the same except change your proposed clustering method to the hierarchical balanced clustering method used in SPANN. Additionally, e.g. cluster pruning strategies have been previously studied in more detail [2].

Finally, the experimental results are not convincing: you do not compare the number of I/O operations or the indexing times between the methods, and only SIFT1M is used for ablation studies. The experimental results for SPANN and Starling seem worse than at least those presented in their original papers, although it is difficult to compare results across papers (you should at least mention the type of CPUs used).

[1] Babenko and Lempitsky. Efficient Indexing of Billion-Scale datasets of deep descriptors. CVPR 2016.

[2] Busolin et al. Early Exit Strategies for Approximate $k$-NN Search in Dense Retrieval. CIKM 2024.

### Questions
- How is your proposed hierarchical clustering method related to NO-IMI?

- In Appendix A.2. you write that you cache frequently accessed large cells in memory. Is that strategy in use in the experiments and do the other compared methods use a similar strategy?

- How does the indexing time of DiskHIVF compare to the indexing times of the other methods?

- Can you list all the query hyperparameters in your method that need to be tuned for each dataset?

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4