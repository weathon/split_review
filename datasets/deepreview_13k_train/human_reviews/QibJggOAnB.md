# Fair Clustering via Alignment

- Decision: Reject
- Scores: 6, 8, 6, 5, 5

## Abstract
Algorithmic fairness in clustering aims to balance the proportions of instances assigned to each cluster with respect to a given sensitive attribute.
Recently, numerous algorithms have been developed for Fair Clustering (FC), most of which optimize a clustering objective under specifically designed fairness constraints.
However, the inherent complexity or approximation of constrained optimization problems makes it challenging to achieve the optimal trade-off between fairness level and clustering utility in practice.
For example, the obtained clustering utility by an existing FC algorithm might be suboptimal, or achieving a certain fairness level could be numerically unstable.
To resolve these limitations, we propose a new FC algorithm based on a novel decomposition of the fair $K$-means clustering objective function.
The proposed algorithm, called Fair Clustering via Alignment (FCA), operates by (i) finding a joint probability distribution to align the data from different protected groups, and (ii) optimizing cluster centers in the aligned space.
A key advantage of FCA is that it guarantees (local) optimal clustering utility for any given fairness level while avoiding the need to solve complex constrained optimization problems, thereby obtaining (local) optimal fair clustering in practice.
Experiments show that FCA offers several empirical benefits over existing methods such as (i) attaining the optimal trade-off between fairness level and clustering utility, and (ii) achieving near-perfect fairness level without numerical instability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a problem, called Fair Clustering via Alignments (FCA), which is a new formulation of the well-known Fair Clustering problem that optimizes clustering objective functions subject to fairness constraints, represented by the notion of the "balance" of different groups of data in each cluster. There are two factors concerning the objective cost: the alignment of points that guarantees fairness in clustering, and the cluster centers. The proposed algorithm take turns to fix one and optimize the other, until the solution converges. This method has improved performance over previous solutions while satisfying the fairness constraints.

### Strengths
The introduced problem is an interesting re-interpretation of a well-known problem. The method separates aligning points from different groups from the computation of clustering and also the centers, which might be useful intuition in practice. I'm not sure if it is the first of such iterative fair clustering approaches, but it seems novel to me.

En route this paper has also developed a more generalized formulation of the fair clustering problem with fractional cluster assignments and analyzed its properties. It has arguably made the optimization easier to solve. 

The algorithm has strong performance in utility, including clustering cost and fairness constraint, in numerical experiments.

### Weaknesses
Although this paper proposes an FCA algorithm that works in a Lloyd's k-means algorithm fashion, I think its main contribution is more conceptual rather than algorithmic. Indeed the optimal solution of FCA is guaranteed to be the optimal fair k-means solution subject to some fairness constraints; however this does not guarantee an algorithm that can efficiently find that solution. In that sense, the abstract is also slightly misleading. Judging from the discussion I don't think the given algorithm is guaranteed to find the global optimal solution, instead of converging to local optimum. 

I also feel there should be a thorough discussion on run-time and approximation guarantees of this new method. It could be slower than the fairlet-based approaches since it could take many iterations to converge despite better performance.

The decomposition cannot easily be extended to other clustering problems, even the k-clustering ones since it heavily depends on the $ell_2^2$ distance properties.

### Questions
The proposed algorithm, like Lloyd's, either fixes the centers and optimizes the alignments; or fixes the grouping and recompute the clustering. For Lloyd's we know certain seeding mechanisms for the initialization, such as the k-means++ mentioned in the paper, can improve performance guarantees. Do we know such things for the FCA algorithm?

I'm wondering what role is played by that decomposition of clustering objective function in the analysis and algorithm design. Is it mostly for the sake of separating the two terms 

Apart from the perfect fairness case, when is the optimal distribution guaranteed to be deterministic and when will the algorithm find deterministic solutions? If it is not deterministic, how do we round it to a solution that is deterministic?  

This paper separates the problem into two parts. It is essentially an iterative version of the fairlet-based method that keeps updating the fairlets themselves, at least when the clusters have the same balance as the original dataset. Although the decomposition might not hold for other k-clustering problems, is it possible to apply the same logic there?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a new algorithm for fair clustering (FC). The proposed method mainly focuses on the case the sensitive attribute is binary. This mean every sample is a pair $(x,s)$ where $x$ is a $d$-vector and $s$ (the sensitive label) is 0 or 1. The goal is to divide the samples into clusters, and ensure that the distribution of samples with $s=0$ or $1$ is consistent with the distribution in the whole data set.

The main idea of the proposed method (called FCA) is to formulate the FC problem as an optimization problem about the clustering center locations and a  joint distribution matrix. The process would alternatively optimize the distribution and the center location. Each step of optimization process is decomposed into two phases: first, one tries to find a one-to-many matching (represented by joint distribution matrix $Q$) from $0$ samples to $1$ samples. This can be formulated as a problem similar to the optimal transport (OT) and can be solved using linear programming. Then in the second phase, one finds tries to find a set of centers for the $k$-clustering, with the assumption that $0$ and $1$ samples are matched/"aligned" as specified by $Q$, and matched samples are to be put into the sample cluster, which enforce the fairness requirement. This can be done using standard clustering algorithms such as the K-means++ algorithm or gradient descent methods on the so called "aligned space" induced from $Q$.

While the above method assumes the strict fairness balance requirement, the paper also present an extension (call FCA-C) that allows control of the balance level. This relaxation is achieved by apply the standard K-means algorithm to some the samples and FCA to the others. This adds another sets of parameters (which specified which samples to apply standard k-means) to the optimization process.

### Strengths
This paper present a fairly strong theoretical result. The proposed algorithms and the analysis are quite non-trivial. The idea of aligning data from different sensitive groups looks quite interesting. This optimization process algo reveals an interesting relation between fair clustering and optimal transport.

### Weaknesses
 The discussion mainly focuses on the case that there are only two sensitive groups. It is not clear whether there is a possibility that the proposed method can be extended to multinary sensitive attributes. The result could be stronger if the authors could provide some hint on how some of the core ideas are not restricted to binary attributes setting.

The writing can be improved. The clustering problem setting is quite different from standard k-means clustering. More detailed explanation in the preliminary section is suggested. For example, it could be not immediately clear that why we need to consider the empirical distribution in a clustering problem.

### Questions
Which of the ideas in FCA/FCA-C do you believe are extendable to multinary sensitive attributes cases? Any thoughts on how the extension could possibly be achieved?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the fair clustering problem with the goal of optimizing a clustering objective under specifically designed fairness constraints. In practice, achieving the optimal trade-off between fairness level and clustering utility is challenging, and the existing fair clustering algorithms may yield suboptimal clustering utility or suffer from numerical instability in reaching a certain fairness level. This paper aims to address these challenges by developing a new in-processing algorithm that can achieve the optimal trade-off between fairness level and clustering utility without numerical instability. The main idea of this paper is to align data from two protected groups by transforming them into a common space (called the aligned space) and then applying a standard clustering algorithm in the aligned space. Authors prove that the optimal fair clustering is equivalent to the optimal clustering in the aligned space. Specifically, for the fair k-means clustering objective, authors propose a new fair clustering algorithm (called FCA) based on a novel decomposition. The proposed algorithm first operates by finding a joint probability distribution to align the data from different protected groups, and then optimizes cluster centers in the aligned space. The FCA algorithm ensures optimal clustering utility for any specified fairness level while avoiding the need to solve complex constrained optimization problems, thereby obtaining optimal fair clustering in practice. Experimental results show that the FCA algorithm outperforms existing baselines in terms of both the trade-off and numerical stability, and optimally controls the trade-off across various fairness levels.

### Strengths
This paper propose a novel decomposition method for the fair clustering cost, dividing it into two components: the transport cost with respect to a joint distribution between two protected groups, and the clustering cost with respect to cluster centers in the aligned space. Based on the proposed decomposition method, this paper develops a fair clustering algorithm FCA, which is transparent, stable, and can guarantee the convergence. Additionally, this paper theoretically proves that FCA achieves the optimal trade-off between fairness level and clustering utility.

### Weaknesses
While the proposed method performs well for two-group fairness, its applicability to multiple groups remains unclear. Specifically, the paper does not discuss how the alignment strategy would extend to more than two protected groups, which is a significant limitation given that real-world datasets often involve multiple sensitive attributes. Additionally, the theoretical analysis lacks the discussions on the relationship between cost and fairness level, making it difficult to assess the trade-off achieved. The paper introduces a method to control the trade-off, but it does not provide a theoretical characterization of how the cost changes as the fairness level is varied. Although FCA shows improved numerical stability in achieving perfect fairness, it is unclear whether this comes at the expense of clustering cost and to what extent. The paper demonstrates that FCA can achieve perfect fairness without numerical instability, but it does not analyze if this perfect fairness comes at the cost of reduced clustering quality. Finally, the experiments conducted in this paper are limited to small datasets, lacking evaluations on larger datasets and different $k$ values. The experimental validation is not comprehensive enough, as it only uses small datasets and a limited set of $k$ values, which makes it difficult to assess the scalability and robustness of the proposed method.

### Questions
Q1: While the proposed method can achieve the optimal trade-off between fairness level and clustering utility in practice on two protected groups, I am interested in whether this method can be extended to handle multiple groups, which is a more general case.

Q2: Since the proposed method provides a trade-off, is it theoretically possible to show the relation between the cost and the fairness level? 

Q3: The fairlet-based method by Chierichetti et al. is for the k-center and k-median problem in metric space, whereas the proposed method in this paper is designed for the Euclidean k-means problem. In Figure 1, the proposed method demonstrates a lower cost than that of Chierichetti et al. Is this comparison fair?

Q4: In Table 2, the authors compare the numerical stability of FCA and VFC when achieving the maximum balance. The experimental results show that FCA performs better in achieving perfect fairness. Whether this is achieved by sacrificing part of the clustering cost, and if so, to what extent?

Q5: Why the experiments are conducted on smaller datasets? Is it possible to test the proposed method on larger datasets, e.g., millions or even hundreds of millions? Additionally, testing more k values across different datasets will be beneficial.

### Soundness
3

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
This paper studies fair clustering problem and gives an algorithmic framework that takes a distributional view and transform the fair clustering problem into a variant of optimal transport problem. Once the relation to the optimal transport is established, one can formulate an LP and solve it in poly(n) time. Actually, I think the paper gives a new fair clustering objective/formulation (which is different to the widely used proportional fairness), particularly a notion called ``balance’’, which measures how close the conditional expectation with respect to any given sensitive attribute assignment, to the unconditional one. The new algorithm is designed for this objective.

This paper also conducts experiments to validate the effectiveness of the proposed algorithm, and it compares with several recent approximation algorithms for fair clustering as baselines. It seems the new algorithm can outperform baselines in their experiment setup. A further applications to visual clustering is showcased.

### Strengths
- The paper offers a new view to fair clustering
- Both theoretical and experimental results are presented
- This new formulation seems to evade the NP-hardness of proportional fair clustering, which may be a useful feature, though I might be wrong

### Weaknesses
 - The relation to the widely considered proportional fairness is not formally addressed
- It seems the method can only deal with a binary sensitive attribute, whereas many previous works can systematically solve arbitrary groups and sensitive attributes
- The case of general “balance” seems to be weak (Corollary 4.2), and no worst-case bound that only depends on the magnitude of input is given.

### Questions
- Your problem requires the input of a distribution of input. In many other fair clustering papers, the input is simply a point set and the optimization is done only on one input. How are the two settings related? Notice that in your experiments you do a comparison to those algorithms, then how do you set the input accordingly?

- For your phase 2, you mentioned that one could use k-means++ to update \mu. However, is there a formal treatment of this? In particular, does the O(\log k) approximation ratio carries on to your case?

- The FCA-C algorithm seems to use many more steps than FCA. How efficient can we implement this?

- How do you measure the balance of the baselines in the experiments? I don’t think they work with a distributional input

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the fair clustering problem and introduces a new algorithm, FCA, to address the trade-off between fairness and clustering utility in clustering algorithms. FCA aligns data from different protected groups into a common space, allowing for optimal clustering while adhering to fairness constraints. The authors prove that this approach achieves better clustering utility and stability compared to existing methods. Empirically, FCA outperforms baseline algorithms in cost-fairness tradeoff.

### Strengths
- The paper presents the FCA algorithm, which effectively balances fairness and clustering utility, achieving optimal results without compromising either aspect. This addresses a significant challenge in fair clustering.

- The paper provides a theoretical analysis of the FCA algorithm, proving that optimal fair clustering can be achieved through alignment in a common space.

- Empirically, FCA is shown to be robust against variations in data preprocessing, optimization algorithms, and initialization of cluster centers, ensuring consistent performance across different scenarios.

### Weaknesses
The FCA algorithm's optimality is not clear. It seems that the algorithm does not find the optimal fair clustering. I suggest including a detailed comparison of the notion of optimality and the commonly used optimal solution. Specifically, the paper should clarify whether FCA converges to a global optimum or a local optimum, and under what conditions. The current discussion lacks a rigorous definition of optimality in the context of fair clustering, making it difficult to assess the algorithm's performance against theoretical limits.

- Sec 3 mainly discusses the case of perfect fair clustering, in which we can construct mappings between different groups. However, it is more common that there is a group-wise lower and upper bound for the ratio of each group in a cluster. How do we handle this case? The paper needs to address how FCA can be adapted to handle scenarios where perfect fairness is not achievable or desired, and provide a clear explanation of how the algorithm behaves under such constraints. The current approach seems overly restrictive and lacks practical applicability to real-world datasets where perfect fairness is often an unrealistic goal.

### Questions
- Could you give examples of what settings FCA can actually find an optimal fair clustering and what settings it does not?

- Instead of perfect fair clustering, e.g., we only require the balance to be at least 0.8, is there any theoretical result?

### Soundness
2

### Presentation
3

### Contribution
3
