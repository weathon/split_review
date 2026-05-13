# New Algorithms for the Learning-Augmented k-means Problem

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
In this paper, we study the clustering problems in the learning-augmented setting, where predicted labels for a d-dimensional dataset with size m are given by an oracle to serve as auxiliary information to improve the clustering performance. Following the prior work, the given oracle is parameterized by some error rate α, which captures the accuracy of the oracle such that there are at most α fraction of false positives and false negatives in each predicted cluster. In this setting, the goal is to design fast and practical algorithms that can break the computational barriers of inapproximability. The current state-of-the-art learning-augmented k-means algorithm relies on sorting strategies to find good coordinates approximation, where a (1+O(α))-approximation can be achieved with near-linear running time in the data size. However, the computational demands for sorting may limit the scalability of the algorithm for handling large-scale datasets. To address this issue, in this paper, we propose new algorithms that can identify good coordinates approximation using sampling-based strategies, where (1+O(α))-approximation can be achieved with linear running time in the data size. To obtain a more practical algorithm for the problem with better clustering quality and running time, we propose a sampling-based heuristic which can directly find center approximations using sampling-based strategies. Empirical experiments show that our proposed methods are faster than the state-of-the-art learning-augmented k-means algorithms with comparable performances on clustering quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors provide asymptotically faster algorithms for the Learning-Augmented k-means problem by going beyond the initial sorting strategies and instead using sampling-based strategies. Their run time is $\mathcal{O}(m \cdot d) + \mathcal{O}_{\epsilon}(k\cdot d)$ from 
$\mathcal{O}(m \cdot d \log m)$. They further propose a heuristic algorithm using their sampling-based ideas that perform faster in real-world datasets compared to the existing learning-augmented methods.

### Strengths
The learning augmented K-Means problem seems like an interesting setting (even though considerably less studied/without clear applications), and in practical scenarios, a speed-up of  $\log m$ is a noticeable improvement. 

The authors clearly explain their ideas and results and provide several experimental results.

### Weaknesses
1. The run-time of the theoretically guaranteed algorithms provided by the authors *does not improve* for the experimental datasets used compared to the existing algorithms.

2. The authors provide a heuristic algorithm to improve their algorithms with guarantees that it has a faster runtime in practice; I think comparing its runtime with algorithms with theoretical guarantees seems unfair. There is a large (formal as well as informal) literature on many different variants of K-Means. One of the primary strengths of the papers by Ergun et al. and Nguyen et al. is that they have theoretical guarantees.

### Questions
1) What is the quality of the clustering output for the K-Means algorithms proposed in the paper and those used for reference with respect to the ground truth labeling of the datasets (such as NMI and/or ARI values)?  

2) When compared to K-Means++ (without any prediction), what is the improvement in performance on the Learning augmented K-Means algorithms on the datasets the authors have considered? (both in terms of K-Means cost as defined in the paper and ARI, NMI values w.r.t underlying ground truth labels)

### Soundness
3

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
3

### Summary
In the k-means problem, the input is a set P of m points in d-dimensional Euclidean space and the goal is to find a set C of k centers that minimizes the sum of the square of the distances from P to C. K-means is important problem in machine learning, and has been proven to NP-hard to find a solution with approximation ratio smaller than 1.07. Therefore, the popular practical algorithms for k-means have a large approximation ratio, while the algorithms that promise a small approximation ratio have exponential run-time. To overcome the barrier of inapproximability and still have a fast running speed, the learning-augmented k-means problem becomes popular these year. In the learning-augmented k-means problem, we are given an oracle that predict the label of points with an error rate alpha. The goal of the problem is to solve the k-means problem with the help of such oracle in short time and low approximation ratio.
In this paper, the authors propose three algorithms to improve the run-time compared to the previous research. The best result of previous research provides an algorithm that generates an (1+O(alpha))-approximation in O(md log m) time, while the algorithm in this paper achieves O(md) + ~O(kd/alpha) run-time. The novelty of their algorithms is that the author use a random sampling strategy to generate the solution, while the previous researches all use a sorting-based techniques, which inevitably induce a log m dependency for run-time.
In this paper, the authors first propose the Fast-Sampling algorithm that generates an (1+O(alpha))-approximation in O(md log (kd)) time. They decompose the problem in each dimension, find a good approximation of the coordinates of the centers and then compose the coordinates back to R^d. In Fast-Sampling algorithm, candidate coordinates closes to the coordinates of optimal solution is identified first, and then they use these candidate coordinates to define intervals that capture the optimal solution more precisely.
To further remove the log (kd) dependency in run-time, they propose their second algorithm Fast-Estimation, which generates an (1+O(alpha))-approximation in O(md) + ~O(kd/alpha) run-time. They use a sampling-based strategy to construct an estimator, which can give accurate estimation of cluster cost. With the help of such estimator, they succeed to achieve the O(md) + ~O(kd/alpha) run-time.
Although their algorithms have shorter run-time, the approximation ratio is worse than the algorithm in previous research. Hence, they give their third algorithm, Fast-Filtering, a heuristic that achieve low approximation ratio while still run fast. They also run experiments to test the performance of their algorithms.

### Strengths
They remove the log m dependency in the run-time compared to the previous algorithms, which is a huge improvement. Furthermore, they apply a new sampling-based technique to achieve such improvement, which is novel because the sorting-based technique is widely used for previous research. They provide both solid theoretical and practical support to verify their algorithms, which makes their algorithms very trustworthy.

### Weaknesses
Their Fast-Sampling and Fast-Estimation have worse approximation ratio compared to previous results. Specifically, while the previous state-of-the-art achieves a (1+O(alpha)) approximation, the proposed algorithms only guarantee this approximation within a constant factor, which could be significant in practice. Although their Fast-Filtering performs well in approximation ratio, it is a heuristic and there lacks theoretical support for Fast-Filtering. The lack of theoretical guarantees makes it difficult to assess the robustness and reliability of the Fast-Filtering algorithm in different scenarios. It is unclear how the performance of Fast-Filtering would degrade with increasing dataset size or different data distributions.

### Questions
The experiments are only run for Fast-Sampling and Fast-Filtering. What is the performance of Fast-Estimation?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper considers the learning-augmented $k$-means problem. In this problem, the input consists of a data set and a predicted partition $\{P_1,...,P_k\}$. It is assumed that $P_i$ has a symmetric difference at most $\alpha$ fraction to the $k$-th optimal cluster. The goal is still to find a set of $k$ centers to minimize the $k$-means objective (sum of the squared distance to the closest center). 

Existing results on this problem achieve a $1+O(\alpha)$ approximation with running time $O(md\log m)$ where $m$ is the size of the data set and $d$ is the dimension. The main contribution of this paper is to remove the $O(\log m)$ factor by introducing sampling-based algorithms. The authors show that one can use sampling to find a good candidate for every dimension of each optimal center by employing some nice properties of $k$-means objectives and the condition that $P_i$ overlaps a lot with the true cluster. Two results are presented, one runs $O(\epsilon^{-1/2} md\log (kd))$ and the other runs in $O(md+\alpha^{-1}\epsilon^{-5}kd)$. Experimental results also show about 6 times speedup upon existing algorithms.

I think this paper is a good addition to the study of learning-augmented $k$-means.

### Strengths
1. The running time is linear in the input size which improves previous results by avoiding using sorting.
2. Interesting techniques are used and the theoretical results look solid.
3. The algorithm is based on sampling and is easy to use in practice. The experiment also shows the improvement.

### Weaknesses
1. I am unsure if an $O(\log m)$ factor improvement on this problem is super attractive to the community since $O(md\log m)$ already sounds very fast in many cases. Can you explain why avoiding using sorting is so important in this problem?



### Questions
1. In Line 153, the range of $\alpha$ should be $(0,\frac{1}{3}-\frac{\epsilon}{3})$? Why $\alpha$ in the Sorting and Fast-Sampling algorithms can be 0 while in the Fast-Estimation case, it must be positive? Does that mean the formers can recover the ground truth (the optimal clusters) while the latter can not?

2. The techniques seem to be specific to $k$-means clustering. Can one obtain similar results for $k$-median?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies the learning-augmented k-means problem. It proposes three sampling-based algorithms that achieve faster running times compared to previous works. The paper provides theoretical proofs for the algorithms and experimentally tests their cost and time performance.

### Strengths
- The paper employs sampling-based techniques, which indeed improve the running time of existing algorithms.

- The paper includes sufficient theoretical analysis, and the experimental evaluation is also very comprehensive.

### Weaknesses
 - The paper's explanation and intuitive introduction to the learning-augmented k-means problem are not sufficient. I think (Nguyen et al., 2022) has a nice example on this front.

- I'm not an expert in this area, but the technical innovations presented in the paper seem somewhat limited. Intuitively, the algorithm simply performs some sampling operations first and then moves on to subsequent steps, which appears to be a straightforward idea for improving the algorithm's running time.

- Is this paper the first to use sampling techniques to improve the running time of the learning-augmented k-means problem? The paper does not mention other similar algorithms for comparison.

- In Figure 1, Nguyen clearly outperforms Fast-Estimation; however, in the results presented in the other tables, the two methods show similar performance. Could the authors provide an explanation for this discrepancy?

### Questions
- Is this paper the first to use sampling techniques to improve the running time of the learning-augmented k-means problem? The paper does not mention other similar algorithms for comparison.

- In Figure 1, Nguyen clearly outperforms Fast-Estimation; however, in the results presented in the other tables, the two methods show similar performance. Could the authors provide an explanation for this discrepancy?

### Soundness
3

### Presentation
2

### Contribution
2
