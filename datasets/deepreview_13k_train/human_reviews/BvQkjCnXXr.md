# Simple Yet Efficient Locality Sensitive Hashing with Theoretical Guarantee

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Locality-sensitive hashing (LSH) is an effective randomized technique widely used in many machine learning tasks such as outlier detection, neural network training and nearest neighbor search. The cost of hashing is the main performance bottleneck of these applications because the index construction functionality, a core component dominating the end-to-end latency, involves the evaluation of a large number of hash functions. Surprisingly, however, little work has been done to improve the efficiency of LSH computation. In this paper, we design a simple yet efficient LSH scheme, named FastLSH, by combining random sampling and random projection. FastLSH reduces the hashing complexity from $O(n)$ to $O(m)$ ($m<n$), where $n$ is the data dimensionality and $m$ is the number of sampled dimensions. More importantly, FastLSH has provable LSH property, which distinguishes it from the non-LSH fast sketches. To demonstrate its broad applicability, we conduct comprehensive experiments over three machine learning tasks, i.e., outlier detection, neural network training and nearest neighbor search. Experimental results show that algorithms powered by FastLSH provides up to 6.1x, 1.7x and 20x end-to-end speedup in anomaly detection latency, training time and index construction, respectively. The source code is available at https://anonymous.4open.science/r/FastLSHForMachineLearning-7CAC.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper focusses on making locality sensitive hashing (LSH) faster under the \ell_2 metric. The standard LSH scheme involves taking an inner product of the query with a random vector and bucketing the query according to the obtained value. The paper instead proposes to speed up this operation by first subsampling m coordinates of the vector and computing the inner product with the corresponding subsampled vector. It is shown that as m tends to infinity, the probability of collision under the proposed scheme is same as the standard LSH. The paper also shows the superior performance of the proposed scheme empirically.

### Strengths
Locality sensitive hashing is used widely, so any effort in speeding it up is welcome as it can have huge practical significance.

### Weaknesses
Dasgupta et. al. [1] came up with a two-step proposal to speed up the standard LSH using fast Johnson–Lindenstrauss transform. The LSH scheme proposed in this paper essentially removes the first step. However, this step is crucial especially when the dataset consists of sparse vectors. Thus, this paper seems to rediscover some of the ideas already present in [1], while missing the crucial ingredients.

More details: 
The hash function proposed in [1] consists of two steps: (i) First multiply the query vector by a diagonal matrix with diagonal entries chosen to be 1 or -1 equiprobably. Then hit the vector obtained by a Hadamard matrix. (ii) Subsample roughly m coordinates of the resulting vector uniformly at random (without replacement), take the inner product of the resulting subsampled vector with a random gaussian vector and finally bucket the query according to the obtained value (sub sampling is actually done by choosing each coordinate with some fixed probability q = m/d). The first step is crucial when the vectors involved are sparse. In that case, most of the contribution to the \ell_2 distance comes from very few non-zero coordinates. Therefore, for the subsampling to be effective, m will need to be very high, defeating the main purpose. The first step applies a norm-preserving rotation to the vectors, with the desirable property that the vector so obtained is dense, that is, no entry is too large with high probability.

The scheme proposed in this paper essentially applies the second step but where the subsampling is done with replacement. However, not applying the first step means m will need to be very large for sparse vectors. That is why the paper could only show asymptotic equivalence (for m going to infinity) between the proposed scheme and the standard LSH. In contrast, Dasgupta et.al. prove that the collision probability of their proposed scheme is close to the standard LSH for m = O(log d).

### Questions
Any clarification on points raised in the weaknesses section would be helpful.

### Soundness
1

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
This paper aims at the efficiency of LSH methods while not harming its effectiveness. It reduces the cost of computing hashing functions by random sampling. The authors verify the effectiveness of their methods.

### Strengths
S1. The method seems sound. 

S2. This paper studies important problems. 

S3. It is well written.

### Weaknesses
W1. The experiments focus on LSH based methods for ANNS, outlier detection. However, there are other methods such as proximity graphs for ANNS and OD. Besides, LSH based methods are not the SOTA for both of them. Even though LSH methods are enhanced, it does not really make a progress to ANNS and OD. The paper does not adequately address why focusing on LSH is the most impactful direction, especially given the existence of more accurate methods for these tasks. The experiments should include a comparison with a broader range of state-of-the-art techniques, not just LSH-based ones, to justify the contribution of this work in the context of the wider field. The current evaluation is limited to showing improvements within the LSH paradigm, but it does not demonstrate how these improvements translate to overall advancements in ANNS and outlier detection compared to other methods.

### Questions
Q1. I would see more experiments to demonstrate the the method in this paper outperform the SOTA method for ANNS and outlier detection.

### Soundness
2

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
3

### Summary
This paper introduces FastLSH, a novel locality-sensitive hashing scheme that combines random sampling and random projection to reduce the hashing complexity from $O(n)$ to $O(m)$, where $m$ is the number of samplings and $m<n$. 
FastLSH is claimed to preserve the LSH properties, i.e., the collision probability can be calculated like that in E2LSH. 
The faster hash computations in FastLSH make it well-suited for tasks like anomaly detection, neural network training, and nearest neighbor search.

### Strengths
1. FastLSH is simple, it can be easily implemented and can be seamlessly integrated into existing LSH-based applications.

2. The paper provides rigorous theoretical proofs that FastLSH retains the desirable LSH properties.

### Weaknesses
1. The theoretical guarantees hold only when the number of sampled dimensions, $m$, approaches infinity. 
In real-world applications, it is possible to construct dense data sets on which FastLSH may fail. For example, consider a data set in which a large proportion of dimensions are the same, with only a few being non-trivial. 
In such cases, FastLSH is likely to miss the non-trivial dimensions during the sampling process and end up hashing all data points into the same bucket. This raises concerns about potential theoretical flaw in FastLSH. 
Therefore, it would be beneficial for the authors to demonstrate the effectiveness of FastLSH on relatively rare and challenging scenarios, as exemplified above.

2. While FastLSH reduces the cost of hash function computations and index construction time, it does not speed up the query process itself. This limits its broader impact on applications where query speed is critical.

3. The paper does not sufficiently explore the effect of varying the parameter $m$, the number of sampled dimensions, on both the efficiency and accuracy of FastLSH. 
Since $m$ plays a crucial role in balancing computational savings with hashing accuracy, understanding its impact across a range of values is essential. 
Without a thorough parameter study, it remains unclear how to optimally set $m$ for different datasets or applications.

### Questions
1. How does FastLSH handle scenarios where only a few dimensions carry critical information, while others are redundant? Could you provide experiments on such challenging data sets? (W1)

2. Moreover, is there a mechanism in FastLSH to adaptively select informative dimensions during sampling? There are existing methods that adaptively sample the dimensions based on their informativeness, with a non-uniform distribution. (W1)

3. Could you include a parameter study showing how different values of $m$ affect performance across various data sets? (W3)

4. Furthermore, could you provide guidelines or heuristics on how to choose $m$ for a given application? (W3)

### Soundness
3

### Presentation
3

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
This paper proposes a new LSH method, named FastLSH, which aims to accelerate the indexing process of traditional LSH. The authors provide theoretical analysis to argue that their approach retains the fundamental LSH property: that the closer two points are, the higher the probability they will collide in the same hash bucket. The empirical contribution is presented through three groups of experiments, where FastLSH is applied in outlier detection, specialized neural network training (SLIDE) using LSH, and nearest neighbor search.

### Strengths
This paper presents a new approach, FastLSH, which introduces  a new improvement to the indexing process of canonical LSH. The idea of selectively sampling dimensions to accelerate indexing is well-motivated, and the authors attempt to show they retain the core LSH property through both theoretical analysis and empirical validation. They do extensive experiments. The paper is easy to understand.

### Weaknesses
 **W1. Weak Justification of the Research Problem’s Value**

The paper does not sufficiently establish the practical importance of accelerating the indexing process for LSH. Hashing-based methods are already among the fastest algorithms for indexing when compared to quantization-, tree-, and graph-based methods. Among these, LSH is known for fast indexing. From the three applications discussed (outlier detection, neural network training, and nearest neighbor search), it is not evident that further improving LSH indexing speed is a critical need.

For example, in the nearest neighbor search application, the authors report that indexing the GIST1M dataset (960-dimension, 1 million points) takes under 30 seconds—which is already sufficiently fast for most applications. The paper’s focus on indexing overlooks a more pressing issue: search efficiency, where LSH typically performs poorly compared to recent graph-based methods such as HNSW [1]. Improving search efficiency would address a more significant problem, which is why little effort in the literature is devoted to accelerating LSH indexing. While the SLIDE framework may benefit from faster indexing due to frequent re-indexing, it is a specialized case, and more examples are needed to justify the broader value of this work.

**W2. Theoretical Flaws and Insufficient Justification**

The theoretical analysis contains several potential flaws and requires further rigorous justifications to support the authors' claims:

**W2.1 Central Limit Theorem (CLT) Application:**

In Lemma 4.1, the authors apply the CLT, but the conditions for its use are not fully satisfied. CLT assumes i.i.d. samples, yet the proposed method ensures only that the selected dimensions are independently sampled. The elements within each dimension may not be i.i.d. since the authors assume only finite mean and variance for the distribution of  $(u_i-v_i)^2$. Since the underlying distribution is unknown, more justification is needed to ensure that the CLT applies. This step is crucial since it forms the foundation for the entire theoretical framework.

**W2.2 Asymptotic Convergence of Characteristic Functions:**

In Theorem 4.6, the authors aim to demonstrate that the ratio of the characteristic functions of the original and transformed distributions converges to 1 as $m\rightarrow \infty $. However, the convergence depends on the behavior of the input to the characteristic function, x. The authors must show that the ratio of the characteristic functions converge for all values of x. The claim that $x^2\leq O(m^{-1})$ is “obvious” is problematic, as no rigorous justification is provided. This is critical since the convergence ratio will diverge for non-zero x if this condition does not hold.

**W2.3 Practicality of the Asymptotic Results:**

Even if Theorem 4.6 holds, the requirement that $m\rightarrow \infty $ raises practical concerns. Since the authors propose using fewer dimensions (m < n), they must demonstrate that the asymptotic results still hold in practice. Specifically, the authors should quantify how far the transformed distribution deviates from the target distribution under finite m and provide a lower bound for the distribution distance under a suitable metric. Section 4.3 contains only heuristic arguments, making it unclear to what extent the LSH property is preserved after dimension sampling. A more rigorous analysis is required to confirm that the proposed method retains the LSH property, or at least an approximate version of it.

**W3. Weaknesses in Experimental Design and Results**

Several flaws in the experimental design limit the contribution of this paper:

**W3.1 Application Scenarios Are Not Well-Aligned with Claims:**

The authors argue that their method is beneficial for scenarios requiring frequent re-indexing. However, the experiments do not reflect such settings. For example, no experiments are conducted on streaming data, which would be a more relevant use case. Moreover, the authors should compare their method to state-of-the-art approaches for high-dimensional data streams, such as [2][3].

**W3.2 Incomplete Use of Standard Datasets:**

The authors use well-known datasets such as SIFT, Glove, and GIST, but they do not utilize all queries in these datasets. For instance, the SIFT dataset contains 10,000 queries, yet only 200 were used in the experiments. This is unusual, and the paper provides no justification for this choice. The authors should explain how the subset was selected and whether this affects the search performance.

**W3.3 Diverse Speedup in Outlier Detection Task:**

The reported speedup of FastLSH over baseline methods varies significantly across datasets, especially in the outlier detection task. This raises concerns about whether the proposed method introduces distortions in the Hamming distances or requires dataset-specific hyper-parameter tuning. Either issue would limit the generality of the method and should be thoroughly investigated and reported.

### Questions
S1: Strengthen the theoretical analysis and address the problems in W2
S2: Add suitable experiments and give proper analysis to demonstrate the strengths of this paper to reach ICLR standard.
S3. Justify the research value of this problem with broad use cases.

### Soundness
2

### Presentation
2

### Contribution
2
