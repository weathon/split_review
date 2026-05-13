# Average Sensitivity of Hierarchical Clustering

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Hierarchical clustering is one of the most popular methods used to extract cluster structures in a dataset.
However, if the hierarchical clustering algorithm is sensitive to a small perturbation to the dataset, then the credibility and replicability of the output hierarchical clustering are compromised. 
To address this issue, we consider the average sensitivity of hierarchical clustering algorithms, which measures the change in the output hierarchical clustering upon deletion of a random data point from the dataset.
Then, we propose a divisive hierarchical clustering algorithm with which we can tune the average sensitivity.
Experimental results on benchmark and real-world datasets confirm that the proposed method is stable against the deletion of a few data points, while existing algorithms are not.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the design of algorithms for hierarchical clustering whose output does not change significantly if a random data point is deleted from the input.  Such an algorithm is said to have low average sensitivity.  After formally defining average sensitivity for hierarchical clustering algorithms the paper designs and analyzes such an algorithm with low sensitivity which uses the exponential mechanism from differential privacy in a recursive splitting procedure.  In particular, the bound on the average sensitivity for the algorithm is $O(D \lambda w_G / n + D \log(n w_G))$, where $D$ is an input parameter controlling the maximum depth, $\lambda$ is an input parameter for the exponential mechanism, and $w_G$ is the total weight in a weighted graph constructed by the algorithm (each such weight is in $[0,1]$, hence we get the bound $w_G = O(n^2)$).  This is extended to the case of shared randomness, i.e., the case in which we fix the string of random bits for both the original input and the input with a random data point deleted.  Finally, the paper complements the theoretical results with a thorough experimental analysis of the proposed algorithm.

### Strengths
- For the most part, the paper is cleanly written and easy to read.
- The algorithms and analysis are well motivated and clearly described.
- Experimental results are promising

### Weaknesses
My main issue with this paper as it is currently written is in the formulation.  The definition of average sensitivity seems to only require that the output distribution for similar inputs are in some sense close.  While the proposed algorithms are certainly non-trivial its not clear to me that:
1. a similar guarantee cannot be given for a simpler algorithm, and
2. the proposed algorithms are doing something desirable in the context of hierarchical clustering

For the first point, it would help to see some notion of lower bound to better understand the complexity of the problem.  Expounding on the second point further, I think it would help if the algorithm was also constrained to perform well on some notion of utility, e.g., the Dasgupta cost function that is used as a metric in the experiments.  I think it would greatly strengthen the paper to consider the tradeoff between average sensitivity and some notion of clustering cost or utility (again, the Dasgupta cost may be a good candidate to consider).

The average sensitivity seems to scale with the maximum allowable depth $D$.  Why not just set $D = 1$, or some other small value?  It feels like there should be a tension with some notion of clustering quality that benefits from using a tree with more depth.

### Questions
- The proposed algorithm makes use of the exponential mechanism from differential privacy.  How does average sensitivity relate to differential privacy?  Does one notion imply the other or vice versa?  Overall, these two notions both seem to capture the intuitive idea of "the output distribution for similar inputs should be similar".

- The average sensitivity seems to scale with the maximum allowable depth $D$.  Why not just set $D = 1$, or some other small value?  It feels like there should be a tension with some notion of clustering quality that benefits from using a tree with more depth.

- Can the quality of the proposed algorithm be analyzed in terms of some cost or utility function (e.g., Dasgupta's cost function or the utility function due to Moseley and Wang)?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for hierarchical clustering that is robust to deletion of data points. Its stability is supported by theoretical results.

### Strengths
Hierarchical clustering is known to be unstable w.r.t. to removal of data points. The paper formalizes the concept of average sensitivity for hierarchical clustering methods that is used to assess their stability to such removal.

Algorithm SHC for stable hierarchical clustering is introduced whose average sensitivity is $O(\lambda D n)$ with $\lambda$ being an input parameter for exponential mechanism, $D$ depth of hierarchical clustering and $n$ the number of data samples.

### Weaknesses
SHC has time complexity $O(D n^3)$. This makes it impractical to moderate to large size data sets, which is perhaps the reason why experiments are conducted on mostly small data sets. I would like to see a more efficient algorithm, or at least an approximate one with proven theoretical bound.

The average sensitivity of SHC is $O(\lambda D n)$, which can be made small by setting $\lambda \ll 1$. In the experiments, this is not always the case, for instance in Section 8. This signifies that SHC in practice doesn't really have a low average sensitivity. The fact that a larger $\lambda$ sometimes yields better stability in experiments suggests that the theoretical bound is not tight, and the practical behavior of the algorithm is not well understood.

The data sets chosen in the experiments are way too small. This makes the results not so convincing. Specifically, the lack of experiments on larger datasets makes it difficult to assess the practical scalability and utility of the proposed method. The experiments should include datasets with a wider range of sizes to demonstrate the method's performance under more realistic conditions.

### Questions
SHC's time complexity is quadratic in data size. Could this be alleviated?

Why was $\lambda > 1$ used in the experiments?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the average sensitivity of hierarchical clustering. In the paper, two hierarchical clustering algorithms that consider the average sensitivity are proposed, noted as SHC and SHC-SR. The proposed algorithms are theoretically analyzed. The SHC is proved to have low average sensitivity, and the SHC-SR is proved to have average sensitivity under shared randomness.

### Strengths
1.	The paper is well-written, organized logically, and has a strong theoretical foundation. 
2.	This paper exhibits a degree of innovation in considering sensitivity within hierarchical clustering.

### Weaknesses
1.	The significance of this paper needs further clarification, especially regarding the unclear relationship between sensitivity and clustering performance. As illustrated in the example in Figure 1, the 10th sample can be considered as a boundary or noise sample, while the 4th sample can be considered as a central sample. These samples have varying impacts on the clustering tree. It can be anticipated that removing the 10th sample will result in minimal changes to the hierarchical tree, whereas removing the 4th sample will lead to significant changes. Why stable results are needed? The paper does not adequately address the practical implications of sensitivity in the context of hierarchical clustering. It remains unclear how the proposed sensitivity metrics directly translate to improved or more reliable clustering outcomes for real-world applications. The connection between a low average sensitivity and the actual utility of the resulting hierarchical structure is not well-established.
2.	The experimental analysis appears to be insufficient. Firstly, the experiments are conducted on three benchmark datasets and a single set of real-world data, which results in a relatively small dataset size. The choice of datasets seems limited and does not cover a wide range of data characteristics or complexities. Secondly, common external clustering performance evaluation metrics, such as NMI, ARI, and ACC, are not employed in the experiments. The absence of these standard metrics makes it difficult to compare the proposed algorithms with existing methods in terms of clustering quality. Lastly, there is no clear discernible consistent trend evident from Figure 2 and the related figures in the supplementary materials. The lack of a clear trend raises concerns about the robustness and generalizability of the proposed algorithms. The results appear to be highly dependent on specific parameter settings and datasets, which limits the practical applicability of the findings.

### Questions
1.	Why is sensitivity crucial for hierarchical clustering?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The average sensitivity of a randomized algorithm measures the distance between the distributions of the output of the algorithm when a random element of the input is deleted, where the distance is often the total variation distance or the earth mover distance. It can often be advantageous to minimize the average sensitivity of an algorithm so that small changes to the input may only result in small changes to the output. 

This paper studies the average sensitivity of algorithms for hierarchical clustering, defining a distance between hierarchical clusterings of a graph by the sizes of the symmetric differences at each level. The paper first proposes an algorithm for stable hierarchical clustering, which is based off recursively performing a stable sparsest cut subroutine that crucially utilizes the exponential mechanism from differential privacy. The paper then shows that if the randomness between multiple instances of the algorithm is shared, then a smaller average sensitivity can be induced by using a permutation-based sampling algorithm to replace the exponential mechanism. Finally, the paper performs a number of experiments showing tradeoffs between average sensitivity and the performance of the hierarchical clustering algorithms under the Dasgupta objective.

### Strengths
- Although average sensitivity is less studied than worst-case sensitivity for privacy, I believe the problem can still be well-motivated from the perspective of average-case data perturbations and therefore relevant to a theoretical subcommunity of ICLR
- The paper provides rigorous analysis upper bounding the average sensitivity of the proposed algorithms
- The experiments are performed over multiple datasets and clearly show a trade-off between average sensitivity and clustering cost
- The problem setup, the algorithm, and the intuition are all well-written and accessible to a general audience

### Weaknesses
 - Applications of methods from differential privacy, i.e., exponential mechanism, may not be as surprising as initially seemed, due to connections to the notion of worst-case sensitivity in differential privacy
- The main approximation guarantee for the stable-on-average hierarchical clustering algorithm seems to be in terms of the expected size of the sparsest cut, rather than the expected cost of the clustering
- Other hierarchical clustering objectives such as the Moseley-Wang or Cohen-Addad objectives are not considered

### Questions
- What can be said about the approximation guarantees of the main algorithm in terms of the Dasgupta objective? Can anything be said about the approximation guarantees of the algorithm given an $\alpha$-approximation algorithm for sparsest cut?
- Is it true that the random cut algorithm that provides a good approximation to the Moseley-Wang objective would also have low average sensitivity?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
