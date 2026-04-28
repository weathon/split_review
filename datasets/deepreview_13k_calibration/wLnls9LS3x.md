# Improved Algorithms for Kernel Matrix-Vector Multiplication

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Motivated by the problem of fast processing of attention matrices, we study fast algorithms for computing matrix-vector products for asymmetric Gaussian Kernel matrices $K\in \mathbb{R}^{n\times n}$. 
$K$'s columns are indexed by a set of $n$ keys $k_1,k_2\ldots, k_n\in \mathbb{R}^d$, rows by a set of $n$ queries $q_1,q_2,\ldots,q_n\in \mathbb{R}^d $, and its $i,j$ entry is $K_{ij} = e^{-\|q_i-k_j\|_2^2/2\sigma^2}$ for some bandwidth parameter $\sigma>0$. Given a vector $x\in \mathbb{R}^n$ and error parameter $\epsilon>0$, our task is to output a $y\in \mathbb{R}^n$ such that $\|Kx-y\|_2\leq \epsilon \|x\|_2$ in time subquadratic in $n$ and linear in $d$. Our algorithms rely on the following modelling assumption about the matrices $K$: the sum of the entries of $K$ scales linearly in $n$, as opposed to worst case quadratic growth. We validate this assumption experimentally, for Gaussian kernel matrices encountered in various settings such as fast attention computation in LLMs. Under this assumption, we obtain the first subquadratic time algorithm for kernel matrix-vector multiplication for unrestricted vectors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
A wide variety of applications in machine learning and computational statistics, including the Kernel Density Estimation problem and the Attention subroutine of transformers, reduce to the problem of kernel matrix-vector multiplication (KMV). This paper studies an important subproblem that features kernel matrices with 1-norm scaling linearly in n (as opposed to the worst case quadratic growth). The authors performed experiments that evidence the prevalence of such matrices in the context of large language models, which intuitively reflects the fact that each token in the input sequence has high correlation with few other tokens. For this restricted type of kernel matrices, a new algorithm in o(n^2)*poly(d, 1/eps) time is provided, improving on the previous best [Backurs et al. ICML2021] in terms of both efficiency and applicability (in certain parameter regimes).

### Strengths
1. This paper points out an important subclass of kernel matrices that assumes faster algorithms, while being general enough to encompass many real-life datasets. It in addition motivates and sets the stage for the interesting task of finding subquadratic algorithms for this subclass in other parameter regimes (e.g. low-dimensional) that get around the fine-grained lower bounds for general kernel matrices.
2. This paper presents a separation between the additive-error model and the relative-error model. The authors give the first subquadratic algorithm for KMV that allows negative entries in the vector (wrt. the additive-error model), and provide formal argument on the inherent impossibility of achieving this in the relative-error setting (which is the focus of most previous literature including [Backurs et al.]).
3.  For certain KMV instances to which both [Backurs et al.] and the new algorithm are applicable, the latter outperforms with higher efficiency.

### Weaknesses
1. The algorithm can be viewed as a reduction from the proposed KMV subproblem to the general KMV problem. The core techniques such as finding heavy keys using LSH and random sampling, are slight adaptations of the ones developed in [Charikar et al. FOCS20] (or earlier).
2. Several fine-grained lower bounds for either the KMV problem or the Attention subroutine are known [Backurs et al. NeurIPS2017, Alman-Song NeurIPS2024, Alman-Guan CCC2024]. Showing how the new algorithm manages or fails to get around the known lower bounds might shed more light on the power and usefulness of the new subclass of kernel matrices.
3. While the paper introduces a novel algorithm for a specific subclass of kernel matrices, it does not fully explore the practical implications of this restriction. The paper would benefit from a more detailed analysis of how frequently these matrices appear in real-world applications, beyond the examples provided from large language models. A more thorough empirical analysis would help to justify the focus on this particular subclass.

### Questions
1. A few other subclasses of kernel matrices were proposed in recent years that correspond to easier KMV problems. One example is kernel matrices with stable rank constraints. How are those matrices compared to ones with weight distribution studied in this paper?
2. Several variants of KDE problems with different levels of hardness are mentioned in this paper – KMV with vector entries being (1) all 1, (2) all positive or (3) arbitrary. For the relative-error setting, (2) is strictly easier than (3). Is this true in the additive-error setting as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper designs an efficient algorithm for matrix-vector products of asymmetric Gaussian Kernel matrices $K \in \mathbb{R}^{n \times n}$. This problem is motivated by a recent work (Zandieh et al., 2023) that replaces attention matrices with Gaussian kernel matrices. Therefore, the efficient algorithm for kernel matrix vector product of Gaussian kernel matrices can be used to help with the attention optimization problem. The quadratic complexity $O(n^2 d)$ in attention computation limits the efficiency of the large language model. Studying attention optimization is crucial and interesting.

### Strengths
1. The most impressive strength of this paper is that, as mentioned by the authors, their algorithm is the first one that runs in sub-quadratic time for kernel matrix-vector multiplication for unrestricted vectors. It gives a more general solution than the previous works: Backurs et al. (2021) has to restrict the vector $x$ to be non-negative in order to obtain the running time $O(n^{1.173+ o (1)})$. 

2. Additionally, the empirical results from this paper are also very interesting and significant. It shows that the assumptions presented in this work do work well in practice in the setting of transformer-based large language models. It supports that the theoretical work in this paper is applicable to the transformers.

### Weaknesses
1. The empirical validation of the modeling assumption is currently limited to a pre-trained BERT model. The introduction broadly claims applicability to "modern transformer-based language models," but the scope of this claim is not fully substantiated. While the BERT model provides initial evidence, it is crucial to investigate whether the core assumption holds for a wider range of architectures, such as RoBERTa and GPT, to truly establish the generalizability of the proposed algorithm.

2. The paper lacks experimental results demonstrating the actual running time improvement. While the theoretical contribution of a sub-quadratic time algorithm is significant, practical validation is necessary. Without empirical evidence, it is difficult to assess the real-world impact of the theoretical speedup. Including experiments that compare the running time of the proposed algorithm with existing methods would significantly strengthen the paper.

3. The paper could benefit from a more thorough comparison with the work of Alman & Song [1]. While the authors acknowledge that Alman & Song [1] achieve a nearly linear running time of O(n^{1 + o(1)}) for approximating attention computation, they highlight the stricter assumption of d = O(log n) compared to d = o(log^2 n) in Zandieh et al. [2]. However, the practical implications of this difference in assumptions are not adequately discussed. Given that the primary motivation is to improve the efficiency of attention computation, a detailed analysis of the trade-off between running time and the constraint on the hidden dimension d is essential. Specifically, the authors should address the question: If Alman & Song [1] already provide a nearly linear time algorithm, why is there a need for a kernel density estimation approach with a less efficient running time, even if it allows for a slightly larger d?

One minor comment:

Alman & Song [1] was published in NeurIPS 2023, but in the paper, the authors cite it as Alman & Song (2024).

### Questions
In Zandieh et al. (2023), their results (Theorem 3.5) hold for any arbitrary $Q, K, V \in \mathbb{R}^{n \times d}$ to approximate the attention computation, and it does not seem that their Theorem 3.5 rely on the non-negative constraint. How does the result of this paper help with the attention approximation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a novel approach for accelerating Gaussian kernel matrices with general vectors, at a time complexity subquadratic in the number of tokens $n$. It is based on preprocessing the vector to explicitly calculate the contribution from its largest entries, finding the ‘heavy’ keys for each query using a hashing scheme, then randomly estimating the contribution from the remaining ‘light’ keys by uniform sampling. Under the assumption that the sum of entries in the kernel matrix grows linearly with matrix dimension, the method is $\widetilde{\mathcal{O}}(d n^{1.89}/\epsilon^2)$ (where $\epsilon$ is a parameter related to the quality of the approximation) with probability $p=0.99$. The authors are motivated by LLMs, so test their kernel assumption experimentally in this setting.

### Strengths
Thanks for the nice paper. The work enjoys a strong practical motivation and brings technical novelty, especially improving upon Backurs (2021) and contributing to the growing literature on hashing-based algorithms for kernel computation on high-dimensional points. It is broadly well-written and validating your assumptions on BERT is a nice touch. I think the efficient transformer and kernel density estimation communities would enjoy this work.

### Weaknesses
1. *In places, contributions seem overstated*. The authors describe their algorithm as ‘the first algorithm for high dimensional approximate kernel-matrix vector multiplication, that runs in subquadratic time for general vectors’ (110), and similar elsewhere in the text. I agree that they make a nice contribution to fast linear algebra under assumptions on the structure of $K$ but this particular claim is overblown – e.g. taking a low rank decomposition to the kernel using random Fourier features achieves the same, though with a different set of assumptions and guarantees. I’d consider phrasing this a little more carefully to orient the contributions in the broader literature.
2. *How practical is the algorithm?* It would be nice to actually see the algorithm in action with some wall clock times for real or synthetic data, to verify the subquadratic scaling with dimensionality. I suspect it will be slower than vanilla matrix vector multiplication for small $n$, but become faster at some sequence length. Roughly when does this occur? It’s fine if this is a big number, but I think it’s important to give readers a sense of how practical your scheme is. Subquadratic time complexity is not the same as a fast algorithm. The lack of empirical validation makes it difficult to assess the real-world applicability of the proposed method. It's crucial to demonstrate that the theoretical subquadratic scaling translates to actual performance gains, especially when compared to standard matrix multiplication techniques. Without this, the practical value of the algorithm remains questionable.
3. *Do you really test assumption A?* My reading of your core assumption is that the ratio of the sum of all but the largest $n$ entries of K by the sum of the largest $n$ entries of K is at most a constant $c$, independent of the sequence length $n$. Great idea to test this on BERT, but to convince the reader I think you need to show how the maximum of this ratio changes as you vary sequence length, rather than just reporting its maximum value over all sequence lengths. I can’t see any evidence that it’s (approximately) independent of $n$. Another nice idea (which might be harder) would be proving whether your assumption holds under different data distributions (queries and keys that are uniform on a hypersphere, Gaussian etc.), to get a sense of whether we should be surprised that it empirically holds in LLMs or whether this is a general property of the Gaussian kernel.
4. *Presentation*. This is a stylistic point. I would consider bringing Alg. 3 or a related schematic to Sec. 1.3. It feels a bit weird to wait until page 9 to see a clear presentation of your entire algorithm. I would also swap the order of Secs 3 and 4.

### Questions
1. What is the space complexity of your algorithm? I assume quadratic in $n$. This is not a reason for rejection, but running OOM is a real practical concern so it would be good to flag to readers whether or not you help here. 
2. Lemma 3.1 is applied to the attention matrix to obtain a related Gaussian matrix. Why not simply use $K_{S.M.} = \text{diag}(\exp(q_i^2/2)) K_{G} \text{diag}(\exp(k_j^2/2))$? Diagonal matrix multiplication is trivially linear. Your guarantees might need to be tweaked slightly. Would this be simpler, or are there good reasons to prefer the current formulation?
3. Presumably one can trade off the time complexity and probability that the estimate is accurate, changing the exponent on $n$ and the value of $p$. Can the authors comment more on this? 

Notwithstanding my comments above, this is a nice paper. I would be happy to raise my score if the authors can test assumption A more carefully and give some wall-clock run times, or convince me that these things shouldn’t matter. I thank them again for their time and efforts.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work obtains a faster algorithm for evaluating matrix-vector products when the matrix is a kernel matrix which additionally satisfies a “heaviness” assumption. This assumption is newly introduced by the authors, and empirically validated for kernel matrices derived from attention matrices arising in transformers trained in practice. The techniques of this paper extend methods from the literature of kernel density estimation algorithms, largely based on hashing and sampling methods.

### Strengths
This paper works on a highly practical problem of speeding up kernel matrix vector products, which has applications to fast transformers, with improvements based on randomized algorithmic techniques such as hashing and sampling. The authors also find a nice structural assumption which helps in getting fast algorithms, while being a practical and realistic one, as the authors show.

### Weaknesses
While the result is highly practical, the authors unfortunately don’t take it all the way to evaluate the speed up implications of this result for transformers (although this is a lot to ask for).

- It may be worth emphasizing the new assumption in the title, since the title suggests an unconditionally faster algorithm for kernel matrix-vector multiplication, which is somewhat misleading.
- How does the running time of the algorithm scale with the constant $c$ made in assumption A? Is the running time something like $\exp(\mathrm{poly}(c)) \cdot dn^{1.89}/\epsilon^2$? It would be good to mention this so readers can have an awareness of what happens if their matrix encountered in practice has values of $c$ that are a bit larger than what is assumed in this work (e.g. what if it’s 10? 50?)
- Theorem 1.1: you state the theorem as a constant probability statement, but is there a way to boost the probability of this procedure with logarithmic dependence on the failure probability? Typically we need to compute many matrix-vector products, so this is an important point to consider. For example, training transformers would need a huge number of such products, and inference when serving the model could be even larger. It is also unclear how this subroutine would perform when used as part of an algorithm for power method (perhaps the authors might consider working out this corollary if they think it gives improvements?)
- Line 151: should be $\lVert …\rVert_2^2$ rather than $\lVert …\rVert_2$
- Do your results imply improved results for the special case of KDE? power method?
- Maybe too much to ask for of the authors since this is largely a theoretical contribution, but it would have been more convincing if there were experiments which showed that this new algorithm could be used to speed up the KDEformer application of Zandieh et al. Again, that's ok though since this is a theoretical paper.

### Questions
- It may be worth emphasizing the new assumption in the title, since the title suggests an unconditionally faster algorithm for kernel matrix-vector multiplication, which is somewhat misleading.
- How does the running time of the algorithm scale with the constant $c$ made in assumption A? Is the running time something like $\exp(\mathrm{poly}(c)) \cdot dn^{1.89}/\epsilon^2$? It would be good to mention this so readers can have an awareness of what happens if their matrix encountered in practice has values of $c$ that are a bit larger than what is assumed in this work (e.g. what if it’s 10? 50?)
- Theorem 1.1: you state the theorem as a constant probability statement, but is there a way to boost the probability of this procedure with logarithmic dependence on the failure probability? Typically we need to compute many matrix-vector products, so this is an important point to consider. For example, training transformers would need a huge number of such products, and inference when serving the model could be even larger. It is also unclear how this subroutine would perform when used as part of an algorithm for power method (perhaps the authors might consider working out this corollary if they think it gives improvements?)
- Line 151: should be $\lVert …\rVert_2^2$ rather than $\lVert …\rVert_2$
- Do your results imply improved results for the special case of KDE? power method?
- Maybe too much to ask for of the authors since this is largely a theoretical contribution, but it would have been more convincing if there were experiments which showed that this new algorithm could be used to speed up the KDEformer application of Zandieh et al. Again, that's ok though since this is a theoretical paper.

### Soundness
3

### Presentation
3

### Contribution
2
