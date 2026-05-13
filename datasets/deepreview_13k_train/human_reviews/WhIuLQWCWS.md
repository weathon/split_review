# Differentially Private Federated $k$-Means with Server-Side Data

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Clustering has long been a cornerstone of data analysis. It is particularly suited to identifying coherent subgroups or substructures in unlabeled data, as are generated continuously in large amounts these days. However, in many cases traditional clustering methods are not applicable, because data are increasingly being produced and stored in a distributed way, e.g. on edge devices, and privacy concerns prevent it from being transferred to a central server. To address this challenge, we present FedDP-KMeans, a new algorithm for k-means clustering that is fully-federated as well as differentially private. Our approach leverages (potentially small and out-of-distribution) server-side data to overcome the primary challenge of differentially private clustering methods: the need for a good initialization. Combining our initialization with a simple federated DP-Lloyds algorithm we obtain an algorithm that achieves excellent results on synthetic and real-world benchmark tasks. We also provide a theoretical analysis of our method that provides bounds on the convergence speed and cluster identification success.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the problem of compute $k$-means clustering of edge devices by using the data at the server to compute the weights given to the clusters.

### Strengths
The paper gives an algorithm that uses server data to weight the client's cluster and give both theoretical as well as empirical evaluation of its results.

### Weaknesses
The idea of using projection to a low-dimensional subspace and perform clustering there is not new. It has been done in a lot of work. Also, for the idea to work, I think there is an implicit assumption that the server's data has the same distribution as the client's data. One can use any PPCA  matrices introduced in Cohen et al (STOC 2015) and this has been known for a really long time in the ML literature. Using Gaussian noise on top of PPCA has been also studied by several works on k-means and k-median clustering. So, I am not sure if this is a new idea. 

Using the server's data to find cluster center that clients can use to weigh its projected point is also studied (without privacy constraints) in the literature of randomized numerical linear algebra.  

The server's data is considered to be public. However, in real world, server cloud contains data that might be stored by some users or in a business setup, consist of private data pertaining to the firm. So, I am unsure if this assumption is reasonable.

### Questions
What are the assumptions made about the client's and server's data in this paper? 

What would be a reasonable setting to assume that the server's data is non-private?

Assuming that you are using \widehat n_r, if the value of n_r < log(n/\beta), then with reasonable probability you will have numerical instability. How do you make sure that does not happen?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose FedDP-KMeans, a novel algorithm combining federated learning and differential privacy to perform k-means clustering on decentralized, privacy-sensitive data. It introduces FedDP-Init to leverage small, server-side datasets for better initialization and FedDP-Lloyds to refine clusters while maintaining privacy. The method ensures high clustering accuracy with minimal communication rounds, addressing the privacy-utility trade-off by adding controlled noise. Experiments on synthetic and real-world datasets demonstrate its superiority over existing methods, making it a practical solution for applications like cross-device and cross-silo federated learning.

### Strengths
+. This paper integrates differential privacy with federated learning to address privacy issues in decentralized data environments.
+. The proposed FedDP-KMeans algorithm uses out-of-distribution, potentially small, server-side data to address the initialization challenge in DP k-means clustering. This innovation mitigates the impact of privacy noise and reduces the number of required Lloyd's steps, which is beneficial in reducing communication overhead.
+. The authors provide a theoretical analysis, proving that FedDP-KMeans converges exponentially to true cluster centers under Gaussian mixture data assumptions. In addition, empirical results built on both synthetic and real-world datasets show that FedDP-KMeans outperforms baseline approaches, especially when the server data is out-of-distribution, thus demonstrating robustness in realistic scenarios.

### Weaknesses
 -. This paper emphasizes the importance of good initialization, but it does not clearly articulate the impact that initialization can have. Specifically, it does not explain how different initializations specifically affect clustering quality in the context of differential privacy. The paper would benefit from a more detailed discussion on how poor initializations can lead to suboptimal cluster assignments, especially given the added noise from differential privacy mechanisms. For instance, it should elaborate on how a bad initial centroid might cause the algorithm to converge to a local minimum far from the true cluster center, and how this effect is exacerbated by the noise introduced for privacy.
-. The paper emphasizes the utility of leveraging server-side data, but it does not explain why this is beneficial. Additionally, even if using server-side data is useful, this dependency could limit the applicability of FedDP-KMeans in cases where such data is unavailable or does not adequately represent the client data structure. If the data distributions differ significantly, the reliance on server-side data may introduce bias during clustering. The paper needs to clarify the specific mechanisms by which server-side data improves initialization, and to quantify the potential bias introduced when server data is significantly different from client data. It should also discuss scenarios where server-side data might be detrimental, leading to worse clustering performance than random initialization.
-. Additionally, the paper’s comparison with related work includes relatively outdated studies, as the baseline methods are from 2007, 2017, and 2021. It is recommended to incorporate comparisons with the latest research findings to provide a more current perspective on the proposed methods. The paper should include a more comprehensive comparison with state-of-the-art methods, especially those published in the last two years. This would provide a more accurate assessment of the proposed method's novelty and performance relative to current research.
-. The algorithm requires careful hyperparameter tuning for privacy budgets and sensitivity settings. This challenge is acknowledged but not fully addressed within the main content, making practical implementation more complex without further guidance. The paper should provide more specific guidance on how to choose appropriate privacy budgets and sensitivity parameters, including a discussion on the trade-offs between privacy and utility. It should also include a sensitivity analysis to show how different parameter choices affect the final clustering performance.

### Questions
Q1: What is the Exact Impact of Initialization?
Q2: Why Use Server-Side Data Specifically?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers the $k$-means in the federated learning setting, where there is a central server and multiple clients holding users' data. The objective is to design a differentially private algorithm that minimizes both the $k$-means cost and the communication cost. Assuming the central server owns a small amount of public data, the authors propose FedDP-Init to initialize the $k$ centers. They then privatize Lloyd's algorithm, resulting in FedDP-Lloyds, and refer to the entire algorithm as FedDP-KMeans.

Theoretically, they show that FedDP-KMeans performs well in the Gaussian mixture setting. The authors also conduct experiments on both synthetic and real-world datasets, using different initialization algorithms as baselines.

### Strengths
The paper tackles an interesting and practical problem.
The algorithm descriptions are clear and easy to understand.
The authors address both the theoretical aspects and provide empirical validation through experiments.

### Weaknesses
1. Typos and notation inconsistencies are present throughout the paper (see Questions below).
2. The assumption of public data on the server feels somewhat unrealistic or restrictive, and it would be helpful to explore alternatives or justify this assumption further.
3. I am not deeply familiar with Gaussian mixture models and did not verify the proof in detail. However, Definition 1 appears to rely on a strong assumption, and the proof of Theorem 2 seems to build heavily on existing results. As such, I am uncertain about the contribution and value of the theoretical proof.
4. The experimental results do not fully convince me.
For example, the rank of the subspace is specified as $k$, but this appears to be a critical hyperparameter that could benefit from more discussion, especially in the context of the experiments. Additionally, I would appreciate more discussion on certain design choices and experimental parameters to understand better their impact (see Questions for more details).

### Questions
1. Typos:
(1) Typo in line 120.
(2) Inconsistent notation between $P^j$ and $P_j$ in lines 142 and 145.
2. $\Pi \in \mathbb{R}^{d \times k}$ and $P^j \in \mathbb{R}^{n_j \times d}$. How is the product $\Pi P^j$ defined?
Similarly, how is the product $\Pi Q$ computed?
3. Why does Algorithm 2 use the basic composition for the privacy budget instead of the advanced composition?
4. The bound on Delta is a little strange. Why can we tolerate a larger radius of the domain when epsilon gets smaller?
5.  Could the authors clarify how the matrix $Q$ is generated in the experiments?
6. In Algorithm 1, the variable $r$ is not initialized or specified in line 20.
7.  Could the Johnson–Lindenstrauss lemma be applied as an alternative (more straightforward) approach for constructing the low-rank subspace?
8. I would suggest another baseline, such as transferring all client data to a central location and running private k-means clustering.

### Soundness
2

### Presentation
3

### Contribution
2
