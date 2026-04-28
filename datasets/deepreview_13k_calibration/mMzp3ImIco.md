# Mini-batch kernel $k$-means

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
We present the first mini-batch kernel $k$-means algorithm, offering an order of magnitude improvement in running time compared to the full batch algorithm. A single iteration of our algorithm takes $\widetilde{O}(kb^2)$ time, significantly faster than the $O(n^2)$ time required by the full batch kernel $k$-means, where $n$ is the dataset size and $b$ is the batch size. Extensive experiments demonstrate that our algorithm consistently achieves a 10-100x speedup with minimal loss in quality, addressing the slow runtime that has limited kernel $k$-means adoption in practice. We further complement these results with a theoretical analysis under an early stopping condition, proving that with a batch size of $\bvaltilde$, the algorithm terminates in $O(\gamma^2/\eps)$ iterations with high probability, where $\gamma$ bounds the norm of points in feature space and $\epsilon$ is a termination threshold. Our analysis holds for any reasonable center initialization, and when using $k$-means++ initialization, the algorithm achieves an approximation ratio of $O(\log k)$ in expectation. For normalized kernels, such as Gaussian or Laplacian it holds that $\gamma=1$. Taking $\epsilon = O(1)$ and $b=\Theta(\log n)$, the algorithm terminates in $O(1)$ iterations, with each iteration running in $\widetilde{O}(k)$ time.

\iffalse
  We present the first mini-batch kernel $k$-means algorithm. Our algorithm achieves an order of magnitude improvement in running time compared to the full batch algorithm, with only a minor negative effect on the quality of the solution. Specifically, a single iteration of our algorithm requires only $\widetilde{O}(kb^2)$ time, compared to $O(n^2)$ for the full batch kernel $k$-means, where $n$ is the size of the dataset and $b$ is the batch size. We perform an extensive experimental evaluation of our algorithm and show it consistently achieves a 10-100x speedup over the full batch algorithm with almost no loss in quality. This is significant as the slow running time of kernel k-means has prevented widespread adoption.
  
  We complement our experimental results with a theoretical analysis for our algorithm with an early stopping condition. We show that if the batch is of size $\bvaltilde$, the algorithm must terminate within $O(\gamma^2/\eps)$ iterations with high probability, where $\gamma$ is the bound on the norm of points in the dataset in feature space,
and $\epsilon$ is a threshold parameter for termination. 
Our results hold for any reasonable initialization of centers. When the algorithm is initialized with the $k$-means++ initialization scheme, it
achieves an approximation ratio of $O(\log k)$ in expectation.

Many popular kernels are \emph{normalized} (e.g., Gaussian, Laplacian), which implies $\gamma=1$. For these kernels, taking $\eps$ to be a constant and  $b=\Theta(\log n)$,  our algorithm terminates within $O(1)$ iterations where each iteration takes time $\widetilde{O}(k)$. 
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a kernel mini-batch $k$-means algorithm. The authors provide theoretical analysis that shows that the number of iterations of their algorithm is dimension-independent. In addition, they provide experimantal results that suggest that their algorithm might be useful in practice.

### Strengths
The dimension-independent result seem to be interesting, though I'm not an expert in the field.

### Weaknesses
I'm not an expert in the area, and I might get some things wrong. So far it seems to me that the main difference of your analysis and the analysis of [Schwartzman (2023)] is your Lemma 12, that is very similar to their Lemma 10. These lemmas have almost identical proofs, except the last step, where both proofs use the Cauchy-Schwartz inequality, but in different spaces. This corresponds to your $\gamma^2$ and their $d$ in the number of iterations. Could you tell what are other important differences between your proof and their proof? If there are no other crucial differences, the technical contribution of this paper is not strong enough for ICLR.

### Questions
see Weaknesses above

### Soundness
3

### Presentation
3

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
This paper studies efficient implementations of the kernel k-means problems. In this problem, we are given $n$ datapoints $x_1, \ldots, x_n \in X$ and a kernel function $K : X \times X \to \mathbb{R}$ such that there exists a function $\varphi: X \rightarrow \mathcal{H}$, where $\mathcal{H}$ is a Hilbert space, satisfying $K(x, y) = \langle \varphi(x), \varphi(y)\rangle$ for all $x, y \in X$. The goal is to cluster the set of points $\varphi(x_1), \ldots, \varphi(x_n)$ using the usual $k$-means objective. One key issue here is that the outputs of $\varphi(\cdot)$ can be infinite dimensional. So, we would ideally want to work without ever needing to map the input points into the Hilbert space $\mathcal{H}$, The authors argue that, the $k$-means++ initialization and further iterations of Lloyd's can be implemented without ever needing to apply the map $\varphi(\cdot)$ on the input points. A key issue is that each iteration of the Lloyd's algorithm can take $O(n^2)$ time, since the centers in the intermediate iterations are possibly linear combinations of all the input points. 

Thus, the authors propose using mini-batches in each iteration. Instead of using all the points in every iteration, sample only $b$ points in each iteration and update the centers slightly in the centers determined by the Lloyd's update rule. The learning rate parameters set as $\sqrt{b^j/b}$, where $b^j$ is the number of points sampled from the cluster $j$. This was proposed in an earlier work by Schwartzman et al. Using a dynamic programming algorithm, the authors show that this update rule can then be implemented in $O(n \cdot b)$ time. To improve the run time further, the authors propose truncation, whereby a truncated representation of centers is stored instead of storing them all as linear combinations of (possibly all the $n$ points). They show that the quality hit with truncation is not large.

### Strengths
The main contributions of the work:
1. A simple dp algorithm to decrease the cost of mini-batch lloyd's iterations.
2. Truncation to further decrease the cost of each iteration.
3. Experiments implementing their algorithm.

### Weaknesses
Utility and correctness issues I describe in the section below,

1. I do not think the proof of Lemma 15 is correct. The way $\bar{\mathcal{C}}_{{i+1}}$ is defined in line 379 uses, $\alpha_j^i = \sqrt{b^i_j / b}$ values which themselves are functions of the samples $B_i$. So how can you claim that $\bar{\mathcal{C}}_{i+1}$ is independent of $B_i$? Please clarify if I misunderstood anything. I'm willing to update my evaluation after this clarification.
2. While the experimental results do show that the algorithm generates reasonable clusters, I am unconvinced that the iteration bound for minibatch algorithms is super illuminating. Consider an algorithm which outputs the cluster centers unchanged. That algorithm will always terminate in a single iteration by this stopping criteria. So, why should someone (theoretically) care about iteration bound with respect to this stopping criteria (i.e., the value decrease is small) though I understand that the sklearn library uses this stopping criteria and since we are sure that the Lloyd's algorithm only makes progress in terms of the loss, it is a useful criteria to stop the algorithm when the progress is small.
3. In Lemma 13, where is probability coming from?
4. Definition of $\alpha^j_i$ must be highlighted.
5. The analysis is extremely similar to earlier work, which makes the results in this work seem only a marginal advancement over previous work. The core algorithm, including the learning rate, appears to be identical to prior approaches, raising concerns about the novelty of the contribution beyond the truncation step.
6. All the experiments seem to use a fixed number of 200 iterations. It is unclear if the full batch k-means converges to the loss quicker, or if the mini-batch k-means remains close to full-batch throughout. The paper lacks a thorough analysis of the convergence behavior, and it is not clear if there are instances where there is a clear gap between the loss attained by full-batch vs mini-batch. A more extensive experimental analysis would be beneficial to understand the practical implications of the proposed method.

### Questions
1. I do not think the proof of Lemma 15 is correct. The way $\bar{\mathcal{C}}\_{{i+1}}$ is defined in line 379 uses, $\alpha_j^i = \sqrt{b^i_j / b}$ values which themselves are functions of the samples $B_i$. So how can you claim that $\bar{\mathcal{C}}_{i+1}$ is independent of $B_i$? Please clarify if I misunderstood anything. I'm willing to update my evaluation after this clarification.
2. While the experimental results do show that the algorithm generates reasonable clusters, I am unconvinced that the iteration bound for minibatch algorithms is super illuminating. Consider an algorithm which outputs the cluster centers unchanged. That algorithm will always terminate in a single iteration by this stopping criteria. So, why should someone (theoretically) care about iteration bound with respect to this stopping criteria (i.e., the value decrease is small) though I understand that the sklearn library uses this stopping criteria and since we are sure that the Lloyd's algorithm only makes progress in terms of the loss, it is a useful criteria to stop the algorithm when the progress is small.
3. In Lemma 13, where is probability coming from? 
4. Definition of $\alpha^j_i$ must be highlighted. 

I will update my evaluation based on the answers for these questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a mini-batch kernel k-means algorithm designed to accelerate the clustering process by operating on small, randomly selected data subsets rather than the entire dataset in each iteration. A detailed theoretical analysis of the per-iteration computational complexity is provided, along with an examination of the algorithm's convergence behavior under early stopping criteria, batch size considerations, and kernel selection. The findings demonstrate that the proposed method achieves accuracy comparable to that of full-batch kernel k-means, particularly when initialized with k-means++. Empirical results across multiple datasets validate the significant performance gains in terms of execution speed.

### Strengths
1\. The paper is well-structured and easy to follow.

2\. The work represents a natural extension of mini-batch k-means to its kernelized version, incorporating tailored analysis for infinite-dimensional feature spaces.

### Weaknesses
 - 1. Inconsistencies in the Empirical Results:
    
      - For the `mnist_784` dataset, the Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI) scores of the mini-batch kernel method surpass those of the full-batch kernel method, which seems counterintuitive. Is there any explanation for this anomaly?
    
      - In the case of the `letter` dataset, the truncated \(\beta\)-mini-batch kernel method did not achieve significant acceleration in runtime as shown in Figure 1. Moreover, it appears slower in Figure 9 when \(\tau = 300\). Could you provide an explanation for this inconsistency?

 - 2. The theoretical analysis on batch size for termination guarantees is well-constructed. However, given the wide range of batch sizes available for practical use, do you have any recommendations for selecting an appropriate batch size in real-world implementations?

### Questions
See the weakness.

### Soundness
4

### Presentation
3

### Contribution
3
