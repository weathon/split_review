# Large-Scale Spectral Graph Neural Networks via Laplacian Sparsification

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Graph Neural Networks (GNNs) play a pivotal role in graph-based tasks for their proficiency in representation learning.
Among the various GNN methods, spectral GNNs employing polynomial filters have shown promising performance on both homophilous and heterophilous graph structures.
The scalability of spectral GNNs is limited because forward propagation requires multiple graph propagation executions, corresponding to the degree of the polynomial.
On the other hand, scalable spectral GNNs detach the graph propagation and linear layers, allowing the message-passing phase to be pre-computed and ensuring effective scalability on large graphs. 
However, this pre-computation can disrupt end-to-end training, possibly impacting performance, and becomes impractical when dealing with high-dimensional input features.
In response to these challenges, we propose a novel graph spectral sparsification method to approximate the propagation pattern of spectral GNNs.
We prove that our proposed methods generate Laplacian sparsifiers for the random-walk matrix polynomial, incorporating both static and learnable polynomial coefficients.
By considering multi-hop neighbor interactions into one-hop operations, our approach facilitates the use of scalable techniques.
To empirically validate the effectiveness of our methods, we conduct an extensive experimental analysis on datasets spanning various graph scales and properties.
The results show that our method yields superior results in comparison with the corresponding approximated base models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new approach for scaling spectral graph neural networks. Unlike previous efforts that focused on preprocessing feature propagation steps, the proposal relies on Laplacian sparsification, which aims to obtain a sparse graph that retains the spectral properties of the original graph. Experiments using small-scale and large-scale node classification tasks aim to show the effectiveness of the proposal.

### Strengths
- The paper tackles the very relevant issue of the scalability of spectral graph neural networks --- the motivation is clear and strong;
- Results on Ogbn-papers100M demonstrate the scalability of the proposed method.

### Weaknesses
 - Overall, it is unclear if the proposed idea only applies to linear-in-the-parameters spectral GNNs. The definition of spectral GNNs (in the introduction) says they take the form $Y=g_w(L, f_{\theta}(X))$ where $g$ is a polynomial graph filter and $f$ is a linear layer. However, this formulation seems very restrictive and, for instance, does not encompass a simple 2-layer GCN. It remains unclear how the proposed sparsification method would interact with non-linearities and multiple layers of spectral filters, which are common in practice.
- Although the motivation focuses on scalability, the experiments only measure predictive performance. I expected to see an extensive comparison of memory usage and wall-clock time for different methods and datasets. Specifically, the paper should report the memory footprint of the original and sparsified graphs, as well as the training and inference time for different methods. In addition, the paper should report error bars for assessing statistical significance.
- The paper only applies the proposed idea to APPNP and GPR GNNs. I would like to see results for other spectral GNNs (e.g., JacobiConv) to demonstrate the broader applicability of the method. It is also important to compare against other methods that tackle the scalability of GNNs, such as sampling-based approaches.
- The theory does not seem particularly useful since implementing GNNs involves non-linearities, rendering gradient estimates biased. Furthermore, results stem almost directly from previous works. The theoretical analysis appears to only consider the approximation of the propagation matrix, but it does not analyze the impact of the sparsification on the final performance of the GNN, which includes non-linearities and multiple layers.

### Questions
1. We could also design spectral GNNs by stacking layers of polynomial spectral filters interleaved with ReLU activation functions. Does the proposed approach apply to such models? Would it affect the theoretical analysis?
2. What is the improvement in efficiency by applying the node-wise sampling method (section 3.3)? It would be useful to include some numbers in the Appendix.
3. Is the sampling (sparsification) procedure applied at each forward pass or only once before training?
4. The statement of Theorem 4.1 seems to be an imprecise version of Theorem 2.2 of Cheng et al. 2015 --- it is unclear what is the random variable in the modified statement.


Minor comments/suggestions:
1. The sentence "while keeping the number of non-zeros within an acceptable range" in Contribution is unclear. I would briefly explain the idea behind Laplacian sparsification in the introduction for clarity. One or two sentences should be enough.
2. I think the claim '[...] which is the first work tackling the scalability issue of spectral GNNs' is misleading since GCN can be viewed as a spectral GNN, and other works (e.g., SGC, LanczosNet) have tackled scalability issues of GCNs.
3. There is a significant overlap of ideas in section 3.1 and 1. I suggest reducing the overlap for readability.
4. Please point out the exact Theorem in the paper (Cheng et al. 2015) when saying: 'We have extended the original theorem proposed by (Cheng et. al, 2015) ...'. Also, I suggest creating a specific subsection to prove Theorem 3.2 (as you have done for Theorem 4.3) --- I found the discussion in A.1 overloaded.
5. Some notation is introduced in Algorithm 1, such as e_u and e_v. Is  e=(e_u, e_v) in step 1 of Algorithm 1?
6. 'Some of the early classic GNNs, like GCNs, employ static Laplacian polynomials as the graph filter.' This is questionable since the coefficients of the linear layer can be viewed as multi-head spectral coefficients --- in fact, GCNs were introduced this way.
7. What is $\alpha$ in Section 3.2.1?
8. $w$ has been used to denote both polynomial filter coefficients and weights in weighted graphs (Definition 3.1).
9. The first identity of Eq. (2) should be $L^k$ instead of $L^K$.
10. I would include the main algorithm (node-wise procedure) in the main text (btw, there is no appendix 8).
11. Could you elaborate on the last identity in Eq. (2)? Or provide pointers?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work leverages prior random-walk-based spectral sparsification for improving the scalability of GNNs. Compared with prior works, the proposed framework allows for end-to-end training of GNNs. This framework allows approximating the equivalent propagation matrix of Laplacian filters, making it compatible with existing scalable techniques. In addition, rigorous mathematical proofs have been provided to support the proposed method.

### Strengths
1. It is an interesting idea to leverage spectral sparsification for improving the scalability of the GNN training phase. 
2. Rigorous mathematical proofs have been provided to support the proposed method.

### Weaknesses
1. It would be helpful if there were more detailed discussions and explanations when claiming that "our models show a slight performance advantage over the corresponding base models" on the heterophilous datasets proposed by Lim et al. (2021), and when discussing "approximating the desired complex filters tailored to the heterophilous graphs."
2. The theoretical analysis in this work is mostly based on the prior work of "Dehua Cheng, Yu Cheng, Yan Liu, Richard Peng, and Shang-Hua Teng. Spectral sparsification of random-walk matrix polynomials. CoRR, abs/1502.03496, 2015," and is a bit incremental.
3. The proposed framework has many hyperparameters, which may make it impractical for use in real-world problems.
4. The writing of the paper should be significantly improved. There are even missing references, such as "... This sparsifier can be further reduced to O(n log n/ε2) by the existing works []." on page 7.
5. The experimental results are not encouraging: spectral sparsification only produces marginal improvement for a few heterophilic graph datasets but degraded performance for well-known datasets.

### Questions
1. What's the percentage of edges that were retained after using the proposed spectral sparsification technique in GNN training? 
2. Is there any reduction in the overall GNN training time?
2. How to determine the spectral similarity (\epsilon) in the spectral sparsification step?
3. What is the connection between spectral similarity for spectral sparsification and the final GNN performance (accuracy)?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for sparsifying polynomials of graph Laplacians by sampling random edges from some random walk shift operators. The goal is to speed up the applications of Laplacian polynomials in spectral GNNs. Experiments show that the approach sometimes improves performance on well known benchmarks.

### Strengths
The method is clearly explained. The method is analyzed theoretically, and the experiments indicate that the sparsification method often improves out-of-the-box GNN methods.

### Weaknesses
First, the method is mostly an application of a well known Laplacian polynomial sparsification method.

The main problem with the paper at its current form is that important related methods are not cited and compared against. It is hence difficult to judge the paper and understand where the proposed method sits with respect to other methods.

Let me write a partial list of missing papers that need to be compared against.

**Papers about subsampling graphs, motivated by scalability:**

J. Chen, T. Ma, and C. Xiao. FastGCN: Fast learning with graph convolutional networks via importance sampling. In International Conference on Learning Representations, 2018. 

W.-L. Chiang, X. Liu, S. Si, Y. Li, S. Bengio, and C.-J. Hsieh. Cluster-gcn: An efficient algorithm for training deep and large graph convolutional networks. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,

There are other papers along these lines. The authors need to survey the literature.

**Paper about precomputing diffusion before training:**

E Rossi, F Frasca, B Chamberlain, D Eynard, M Bronstein, F Monti
. SIGN: Scalable Inception Graph Neural Networks 

**Transferability/stability to subsampling:**

In addition, there are many theoretical papers about the stability/transferability of GNNs with respect to graph subsampling. The first important three papers are

N Keriven, A Bietti, S Vaiter. Convergence and Stability of Graph Convolutional Networks on Large Random Graphs

R Levie, W Huang, L Bucci, M Bronstein, G Kutyniok. Transferability of spectral graph convolutional neural networks 

L Ruiz, L Chamon, A Ribeiro. Graphon neural networks and the transferability of graph neural networks

There are many more papers along this line. The authors should survey subsequent papers by the authors of the above three papers and others. 

To get an $\epsilon$ approximation, these papers seem to need only $O(1/\epsilon^2)$ sampled nodes, which for dense graphs amounts to $O(1/\epsilon^4)$ edges. This is independent of the degree of the graph, while in your paper the number of edges is linear in the degree of the graph. You need to thoroughly compare your results to these papers. Is the different dependency on the order a result of using a different norm? If so, explain how to compare between the results by converting to the same norm. If your result fundamentally has worse dependency on the degree of the graph, you need to explain what you gain on account of this worse dependency. Without a thorough comparison to past works it is difficult to gauge the contribution of your paper.

There is also a whole field about matrix sketching methods which is relevant. One classic approach is to sample the rows of a large matrix randomly to reduce complexity.

The paper should compare against the above methods, and explain what is novel about the proposed approach with respect to past methods, what the proposed method improves, and what are the shortcomings of the new method with respect to past methods. If this comparison is long, a short version can be written in the main paper, and an extended section can be written as an appendix.

Moreover, note that in [Spectral sparsification of random-walk matrix polynomials
] they want to approximate the polynomial of the matrix itself, not the application of the polynomial of the matrix on the signal. In your work you are only interested in applying the polynomial filter on the signal. For this, you have simple efficient implementations if the graph is sparse: you apply $L$ on $L^kX$ by induction, $k=0,\ldots,K$ to compute all monomials filters $L^kX$ applied on $X$ in linear time in the number of edges (times the power $K$). You need to explain better what your method improves with respect also to this direct method.

Appendix A.1 about the proof of Theorem 3.2 is not clear, and does not seem to have a  rigorous proof. It would be better to write a proof inside a traditional proof environment. You should clearly state in what sense you extend the proof of (Cheng et al., 2015), and what is taken from (Cheng et al., 2015).

**Detailed (and minor) comments:**

Page 2, first paragraph, another big problem with the precomputation of L^k X is that the network can only have one layer. You cannot precompute the powers of the Laplacian on hidden layers.

Contribution:

“keeping the number of non-zeros within an acceptable range” Nonzeros of what? Write more explicitly. 


“Scalable method designing” “which is the first work tackling the scalability issue of spectral GNNs to the best of our knowledge” There are many papers that deal with that, including papers that you cite. Please say that you propose a new way for scalability.


Page 3, MOTIVATION: Use consistent notation. You sometimes use small $x$ and sometimes large $X$ for the input signal. This section mainly repeats things that were already written before. Especially the last paragraph.


Definition 3.1: correct “semi-definite” to “positive semi-definite.”


First line in Page 4 - you forgot period: “eigenvalues are in close correspondence.”

Equation (2): the first approximation is wrong. For example, take $K=1$ and $w_1=1$, and note that $P$ does not approximate $L$. Do you mean that there is a choice of DIFFERENT coefficients $w’_k$ for the polynomial in $P$ that gives an approximation? In that case, you can get an exact equality.
Also, the powers of $L$ should be small $k$.

Two lines below (2): change “desiring matrix” to “desired matrix”.

Theorem 3.2 is formulated in a confusing way. Writing ``we can construct an $\epsilon$ sparsifier’’ sounds like an existence claim, but what you are trying to say is that in probability $1-K/n$ Algorithm 1 gives an $\epsilon$ sparsifier.

There are other papers about subsampling graphs that get rid of the dependency on the degree of the graph. For example, see Theorem, 1 in [N Keriven, A Bietti, S Vaiter. Convergence and Stability of Graph Convolutional Networks on Large Random Graphs]. There, to get an $\epsilon$ error you need to sample $O(1/\epsilon^2)$ nodes, which is independent of the size of the graph. How do you explain the slower asymptotics in your results? What do you gain with respect to the past analyses on account of slower asymptotics? You need to discuss this in detail.

Why would computing random edges make things faster for sparse L? If the number of edges in L is O(n), then already computing $L_K$ takes O(Kn) operations. In your method you need $O(K^2n)$ operations to construct the whole polynomial.
Perhaps your method is only useful for dense graphs? More accurately, when the number of edges is >> the number of nodes? However, it is well known that you can approximate such dense graph shift operators via Monte Carlo sampling the nodes, as I wrote above. Please motivate your method accordingly.  For example, you can compare the complexity to methods that directly apply $L$ on $X$ as many times as needed for the polynomial, assuming that the number of edges is $m=O(n^a)$ where $n$ is the number of nodes and $a$ is between 1 and 2.

Section 4: please define effective resistance.

Page 7: please add the reference “This sparsifier can be further reduced to O(n log n/ε2 ) by the existing works []”

“Note that the proposed bound is much tighter than what is practically required. In practice, the sampling number can be set rather small to achieve the desired performance”  - you mean, the proposed bound is much higher than…?

### Questions
**Detailed (and minor) comments:**

Page 2, first paragraph, another big problem with the precomputation of L^k X is that the network can only have one layer. You cannot precompute the powers of the Laplacian on hidden layers.

Contribution:

“keeping the number of non-zeros within an acceptable range” Nonzeros of what? Write more explicitly. 


“Scalable method designing” “which is the first work tackling the scalability issue of spectral GNNs to the best of our knowledge” There are many papers that deal with that, including papers that you cite. Please say that you propose a new way for scalability.


Page 3, MOTIVATION: Use consistent notation. You sometimes use small $x$ and sometimes large $X$ for the input signal. This section mainly repeats things that were already written before. Especially the last paragraph.


Definition 3.1: correct “semi-definite” to “positive semi-definite.”


First line in Page 4 - you forgot period: “eigenvalues are in close correspondence.”

Equation (2): the first approximation is wrong. For example, take $K=1$ and $w_1=1$, and note that $P$ does not approximate $L$. Do you mean that there is a choice of DIFFERENT coefficients $w’_k$ for the polynomial in $P$ that gives an approximation? In that case, you can get an exact equality.
Also, the powers of $L$ should be small $k$.

Two lines below (2): change “desiring matrix” to “desired matrix”.

Theorem 3.2 is formulated in a confusing way. Writing ``we can construct an $\epsilon$ sparsifier’’ sounds like an existence claim, but what you are trying to say is that in probability $1-K/n$ Algorithm 1 gives an $\epsilon$ sparsifier.

There are other papers about subsampling graphs that get rid of the dependency on the degree of the graph. For example, see Theorem, 1 in [N Keriven, A Bietti, S Vaiter. Convergence and Stability of Graph Convolutional Networks on Large Random Graphs]. There, to get an $\epsilon$ error you need to sample $O(1/\epsilon^2)$ nodes, which is independent of the size of the graph. How do you explain the slower asymptotics in your results? What do you gain with respect to the past analyses on account of slower asymptotics? You need to discuss this in detail.

Why would computing random edges make things faster for sparse L? If the number of edges in L is O(n), then already computing $L_K$ takes O(Kn) operations. In your method you need $O(K^2n)$ operations to construct the whole polynomial.
Perhaps your method is only useful for dense graphs? More accurately, when the number of edges is >> the number of nodes? However, it is well known that you can approximate such dense graph shift operators via Monte Carlo sampling the nodes, as I wrote above. Please motivate your method accordingly.  For example, you can compare the complexity to methods that directly apply $L$ on $X$ as many times as needed for the polynomial, assuming that the number of edges is $m=O(n^a)$ where $n$ is the number of nodes and $a$ is between 1 and 2.


Section 4: please define effective resistance.

Page 7: please add the reference “This sparsifier can be further reduced to O(n log n/ε2 ) by the existing works []”

“Note that the proposed bound is much tighter than what is practically required. In practice, the sampling number can be set rather small to achieve the desired performance”  - you mean, the proposed bound is much higher than…?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a spectral sparsification approach to improve the scalability of spectral graph neural networks, which avoids detaching and enables end-to-end training. The authors also test the efficacy of the spectral sparsification for different datasets, including a very large-scale graph dataset.

### Strengths
The experiments cover datasets of different sizes, including very big ones, which is a strong point.

### Weaknesses
The theory is a rather simple application of the results of Daniel A. Spielman et al.’s theory. The theory only shows some relations between the original graph and the sparsified graph. However, it does not give any results about the performance of GNNs. The theory is disconnected from the GNN theme of this paper.

Spectral sparsification for GNNs has been used widely in GNNs; the authors seem to ignore all related works that use spectral sparsification in the context of GNNs.

Instead of using spectral sparsification, the paper “Johannes Gasteiger, Stefan Weißenberger, Stephan Günnemann, Diffusion Improves Graph Learning, NeurIPS 2019” uses a thresholding approach for spectral approaches. Can the authors comment on this and provide some comparisons?

The authors should include the computational complexity analysis for both memory and computational time. When taking the spectral sparsification step into account, the proposed approach seems also to require a very large memory footprint.

Numerical comparisons with the detached approach are missing.

The authors may consider comparing against other approaches for scalable GNNs, e.g. Clustered GCNs.

Report standard deviation - the improvement seems rather small; perhaps within the standard deviation.

### Questions
See the questions I mentioned in the weaknesses part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
