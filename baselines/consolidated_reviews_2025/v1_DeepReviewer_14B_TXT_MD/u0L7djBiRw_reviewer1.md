### Summary

This paper proposes a new embedding called Rademacher-like embedding (RLE), which is constructed by a smaller Rademacher matrix and several auxiliary random arrays. The construction allows fast computation via partial sums, with time complexity $O(n+k^2)$. This paper further proves that RLE satisfies the subspace embedding property for any $0<\epsilon<0.572$. Experiments show that RLE is 1.5-1.7x faster than Gaussian embedding and sparse sign embedding.

### Soundness

1

### Presentation

2

### Contribution

1

### Strengths

1. The proposed construction is simple and easy to implement.

2. The time complexity of the proposed method is linear in $n$ when $k$ is not larger than $O(n^{1/2})$.

### Weaknesses

#### Some Related Works

[1] Oblivious embeddings: Construction and applications
[2] Subspace embeddings for matrices with orthogonal structure

#### comment

1. The paper lacks a citation and comparison with a relevant work: [1] Lemanczyk, Sebastian, Jakub Madajewicz, and Magdalena Parys. "Oblivious embeddings: Construction and applications." International Conference on Algorithmic Algebra, Algorithms, and Error-Correcting Codes. Berlin, Heidelberg: Springer Berlin Heidelberg, 2015.

In this paper, the authors propose a construction of embedding matrices with $n$ rows and $m$ columns that achieves the subspace embedding property with high probability, using $O(mn/\log^2 m)$ non-zero entries. Notably, when $m=O(n^{1/2})$, the complexity of this construction is $O(n^{3/2}/\log n)$, which is linear in $n$.

The construction in [1] is based on a simpler approach by [2] Libert, Yonatan. "Subspace embeddings for matrices with orthogonal structure." Conference on Computational Complexity. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013.

Both [1] and [2] use fast transform techniques to accelerate matrix multiplication, similar to SRHT. However, they are not mentioned or compared with in this paper.

2. The proof of Theorem 6 is incorrect.

In the Appendix, the authors claim that the proof follows from Lemma 9 (concentration inequality for quadratic forms) and Lemma 10 (pairwise independence). However, Lemma 10 only shows that $|u_i^T \Theta u_i - u_i^T u_i| < \epsilon_1$ for any vector $u_i$. It does not demonstrate that $|u_i^T \Theta u_i - u_j^T \Theta u_j| < \epsilon_1$ for any two vectors $u_i$ and $u_j$.

To illustrate this issue more clearly, consider a simplified counterexample: Let $u_1 = (1, 0, \dots, 0)$ and $u_2 = (0, 1, \dots, 0)$. In this case, $u_1^T u_1 = 1$, $u_2^T u_2 = 1$, but $u_1^T \Theta u_1$ and $u_2^T \Theta u_2$ are independent and can take values $1/\sqrt{k}$ or $-1/\sqrt{k}$ with probability $1/2$ each. Thus, the difference $|u_1^T \Theta u_1 - u_2^T \Theta u_2|$ can be $0$ with probability $1/2$ or $2/\sqrt{k}$ with probability $1/2$, which does not satisfy the condition $|u_i^T \Theta u_i - u_j^T \Theta u_j| < \epsilon_1$.

3. The lower bound on the dimension $k$ in Theorem 6 is not optimal.

The authors state that "The lower bound for $k$ in Theorem 6 is the same as that for the Rademacher embedding." However, the result for Rademacher embedding is based on advanced spectral graph theory, which may not be necessary here.

The construction in this paper uses pairwise independent random variables $\theta_{i,j}$ taking values $\{1/\sqrt{k}, -1/\sqrt{k}\}$. In this case, $Var(\theta_{i,j}) = 1/k^2$ and $E(\theta_{i,j}^2) = 1/k$. By setting $X_{i,j} = \theta_{i,j}^2 - 1/k$, we have $E(X_{i,j}) = 0$ and $X_{i,j}^2 = \theta_{i,j}^2 - 2/k$. Applying Lemma 9, we get $E \sup_{\|x\|\le 1} | \sum \theta_{i,j}^2 x_j^2 - 1/k | \le 4 \sqrt{\sum E \theta_{i,j}^4} \le C \sqrt{m/n}$.

To achieve the subspace embedding property, we need $C \sqrt{m/n} \le \epsilon$. If we set $\epsilon < 0.572$, the required value of $k$ will be significantly smaller than the current bound.

### Suggestions

The paper should include a more thorough comparison with existing oblivious embedding constructions, particularly those based on fast transform techniques. The current literature review is insufficient, as it omits relevant works that achieve similar linear complexity under the condition $k=O(n^{1/2})$. Specifically, the construction in [1] achieves a complexity of $O(n^{3/2}/\log n)$, which is comparable to the proposed method, and should be discussed in detail. The authors should clarify the advantages and disadvantages of their approach compared to these existing methods, focusing on practical aspects such as constant factors and implementation complexity. Furthermore, the paper should discuss the trade-offs between the different approaches in terms of the achievable subspace embedding dimensions and the resulting approximation quality. A more comprehensive comparison would strengthen the paper's contribution and provide a clearer understanding of the proposed method's novelty and practical value.

The proof of Theorem 6 needs significant revision. The current argument relies on pairwise independence, which is insufficient to establish the subspace embedding property. The counterexample provided demonstrates that pairwise independence does not guarantee the required concentration for differences between quadratic forms. To correct this, the authors should consider using stronger forms of independence or alternative concentration inequalities that are applicable to sums of dependent random variables. One possible approach is to explore the use of hypercontractivity or higher-order independence properties of the Rademacher-like matrix. Additionally, the authors should carefully examine the dependencies introduced by their specific construction and adjust the proof strategy accordingly. A more rigorous proof is essential to ensure the validity of the theoretical results and the reliability of the proposed method.

Finally, the paper should explore the possibility of relaxing the lower bound on the dimension $k$ in Theorem 6. The current bound, which is stated to be the same as that for Rademacher embeddings, may be overly conservative. By leveraging the specific properties of the proposed Rademacher-like embedding, it might be possible to achieve a tighter bound. The authors should investigate whether the variance and fourth moment of the embedding entries can be bounded more tightly, potentially leading to a reduced requirement for $k$. This could involve a more detailed analysis of the random matrix's spectral properties or the use of more refined concentration inequalities. A smaller lower bound on $k$ would enhance the practical applicability of the proposed method, especially in scenarios with limited dimensionality.

### Questions

1. The authors state that "The lower bound for $k$ in Theorem 6 is the same as that for the Rademacher embedding." However, the result for Rademacher embedding is based on advanced spectral graph theory, which may not be necessary here.

The construction in this paper uses pairwise independent random variables $\theta_{i,j}$ taking values $\{1/\sqrt{k}, -1/\sqrt{k}\}$. In this case, $Var(\theta_{i,j}) = 1/k^2$ and $E(\theta_{i,j}^2) = 1/k$. By setting $X_{i,j} = \theta_{i,j}^2 - 1/k$, we have $E(X_{i,j}) = 0$ and $X_{i,j}^2 = \theta_{i,j}^2 - 2/k$. Applying Lemma 9, we get $E \sup_{\|x\|\le 1} | \sum \theta_{i,j}^2 x_j^2 - 1/k | \le 4 \sqrt{\sum E \theta_{i,j}^4} \le C \sqrt{m/n}$.

To achieve the subspace embedding property, we need $C \sqrt{m/n} \le \epsilon$. If we set $\epsilon < 0.572$, the required value of $k$ will be significantly smaller than the current bound.

### Rating

1

### Confidence

4

**********
