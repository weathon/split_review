# General Graph Random Features

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
We propose a novel random walk-based algorithm for unbiased estimation of arbitrary functions of a weighted adjacency matrix, coined \emph{general graph random features} (g-GRFs). This includes many of the most popular examples of kernels defined on the nodes of a graph. Our algorithm enjoys subquadratic time complexity with respect to the number of nodes, overcoming the notoriously prohibitive cubic scaling of exact graph kernel evaluation. It can also be trivially distributed across machines, permitting learning on much larger networks. At the heart of the algorithm is a \emph{modulation function} which upweights or downweights the contribution from different random walks depending on their lengths. We show that by parameterising it with a neural network we can obtain g-GRFs that give higher-quality kernel estimates or perform efficient, scalable kernel learning. We provide robust theoretical analysis and support our findings with experiments including pointwise estimation of fixed graph kernels, solving non-homogeneous graph ordinary differential equations, node clustering and kernel regression on triangular meshes.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends a result of Choromanski (2023) in order to compute efficiently an approximation of any functions of a weighted adjacency matrix. The main idea is to add a so-called modulation function in an algorithm based on random walks in order to compute the feature projector.

###
After a discussion with the authors, I changed my ratings about soundness and contribution and my general rating as the authors clarified my mistake about the proof of their Theorem.

### Strengths
This result is a nice extension of the previous result due to Choromanski (2023) allowing us to compute approximations of a variety of graph kernels.

### Weaknesses
I do not understand the proof of the main Theorem 2.1 see below.

The experiments could be improved. The authors mainly compare the results given by their algorithm to the real kernel, i.e., measure the approximation error due to their algorithm. It would be more convincing to have used their algorithm on a 'real' graph problem with a large number of nodes and where standard kernel methods are not possible.

I think equation (19) in the appendix is not correct. This makes the proof of the main result Th 2.1 incorrect. Equation (19) involves only the modulation function evaluated on the total length of the walk, but in Algorithm 1 on line 8, the update for the feature vector uses all values of the modulation function evaluated at $k\leq$ length(walk).
You probably mean in the indicator function that $\omega_{iv}$ is a 'prefix' of the total walk?
But then, when you consider the full walk, you need to have a factor $p$ and not only $(1-p)^{len}$?

I find the term universal quite misleading. You are approximating arbitrary functions of the weighted adjacency matrix, but these are not all possible graph kernels. Indeed, it would be nice to have the expressive power of the kernel you are approximating if possible.

### Questions
I think equation (19) in the appendix is not correct. This makes the proof of the main result Th 2.1 incorrect. Equation (19) involves only the modulation function evaluated on the total length of the walk, but in Algorithm 1 on line 8, the update for the feature vector uses all values of the modulation function evaluated at $k\leq$ length(walk).
You probably mean in the indicator function that $\omega_{iv}$ is a 'prefix' of the total walk?
But then, when you consider the full walk, you need to have a factor $p$ and not only $(1-p)^len$?

I find the term universal quite misleading. You are approximating arbitrary functions of the weighted adjacency matrix, but these are not all possible graph kernels. Indeed, it would be nice to have the expressive power of the kernel you are approximating if possible.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces universal graph random features (u-GRFs) based on random walks in the graph. The authors show that u-GRFs can be used to unbiasedly approximate functions of the weighted adjacency matrix of a graph, which include popular graph kernels such as d-regularized Laplacian kernel, p-step random walk kernel and the heat diffusion kernel. In addition, the authors extend their algorithm for estimating fixed graph kernels to a learnable approach, parametrizing a fixed modulation function with a two-layer neural network. The authors provide a simple generalization bound for the corresponding class of learnable graph kernels. Finally, extensive experiments over various application settings are provided to demonstrate the good performance and potentially wide applicability of u-GRFs.

### Strengths
- This paper extends the recent work of Choromanski (2023) on random walk-based graph random features. Compared to the previous work, this paper has two notable innovations. The first is an introduction of a modulation function which enables estimation of arbitrary functions of the weighted adjacency matrix, the second is an extension to a parametrized setting with a generalization bound. While this work is not the first to study graph random features, it has an easy-to-identify contribution which I think makes it a nice addition to the community.

- The overall presentation and writing are clear and easy to follow. I enjoyed reading this paper.

- The experiments, though limited to a few small graphs, are reasonably extensive and showcase the potentially wide applicability of the proposed universal graph random features.

### Weaknesses
 - The experiments are carried over small graphs. It would be nice to include some experiments on larger graphs, e.g. N=10,000. For example, fix the Erdos-Renyi model but vary the number of nodes. I wonder if and how the approximation error would scale with N, while keeping everything else fixed. Specifically, it is unclear how the computational cost of the random walk approximation scales with the number of nodes, and whether the observed performance on small graphs would generalize to larger, more realistic networks. The current experiments do not provide sufficient evidence to support the claim of wide applicability.

- For experiments on node clustering, Table 2 shows the difference between u-GRFs and the exact kernel. It would be nice to have another table that shows the actual clustering accuracy when compared against the ground-truth information, given the ground-truth number of clusters in each graph. The current evaluation only shows the similarity between the approximated and exact kernels, but it does not directly measure the quality of the clustering produced by the approximated kernel in terms of standard clustering metrics such as normalized mutual information or adjusted rand index.

- Given Theorem 2.1 and Equation 4, as long as f_1 and f_2 satisfy Equation 4 we will have an unbiased estimator. In that case, what is particularly interesting/special about symmetric modulation functions? Does using symmetric modulation functions reduce estimator variance (either empirically or theoretically)? The paper does not provide a clear justification for the use of symmetric modulation functions, and it is unclear whether this choice is crucial for the performance of the method or if it is simply a design choice. A more detailed analysis of the impact of symmetric vs. asymmetric modulation functions is needed.

- Why did you use the pairwise metric in Equation 15 as opposed to node-wise accuracy compared with the clustering result using the exact kernel? The choice of the pairwise metric is not well justified, and it is unclear whether this metric is the most appropriate for evaluating the quality of the clustering. A comparison with node-wise accuracy would provide a more comprehensive evaluation of the clustering performance.

- If I understood correctly, the numbers in the parenthesis in Table 3 and Table 4 are standard deviations. Why are they integers? The notation for standard deviations is not standard and should be clarified.

### Questions
- Given Theorem 2.1 and Equation 4, as long as f_1 and f_2 satisfy Equation 4 we will have an unbiased estimator. In that case, what is particularly interesting/special about symmetric modulation functions? Does using symmetric modulation functions reduce estimator variance (either empirically or theoretically)?

- Why did you use the pairwise metric in Equation 15 as opposed to node-wise accuracy compared with the clustering result using the exact kernel?

- If I understood correctly, the numbers in the parenthesis in Table 3 and Table 4 are standard deviations. Why are they integers?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A large span of interesting problems involving graph data require to compute a function of the weighted adjacency matrix. In most cases, using a naive procedure to compute this function scales (at least) cubicly with the number of nodes in the graph. 

The authors propose a new algorithm to circumvent this computational limitation. Inspired by a recent work by Krzysztof Marcin Choromanski (KMC), the authors introduce a new algorithm to approximate the value of arbitrary functions of the weighted matrix of the graph by using graph random features. Graph random features rely on the possibility to write the function of the weighted adjacency matrix as the expectation of finite dimensional vectors. The former vectors are obtained by using random walks on the graph. Contrary to the KMC's work, the author introduce the notion of modulation function that controls each walker’s load as it traverses the graph. This extra modulation function allows the algorithm to approximate arbitrary functions of the weighted adjacency matrix.

The authors also show that this modulation function can be learned using neural network to solve some given task of interest.

### Strengths
- The paper brings two main contributions. First the introduction of the notion of modulation function and its use in a random walk algorithm to estimate arbitrary functions of the weighted adjacency matrix of a graph. Second, the possibility to learn using neural network this modularity function to automatically selects a graph representation well suited for some downstream task. 

Therefore, this work not only allows to reduce the computational burden to solve some important graph related questions using graph random features and the proposed algorithm, but the method can be used to automatically find the relevant graph representation for a task of interest.

- The paper includes both interesting theoretical results and several numerical experiments (such as node attribute prediction on triangular mesh graphs).

- The paper is well written and the authors pan to make their code publicly available in case their work is accepted.

### Weaknesses
- The authors highlight several times in the paper that one major issue regarding in terms of computational complexity is to inverse the matrix K(W) (where W is the weighted adjacency matrix of the graph). However, in the numerical experiments presented in the paper, the authors do not propose an example of application of their method to inverse such matrix K. It might be relevant to add such experiment in the paper. Specifically, demonstrating how the random features approximation can be leveraged to efficiently compute or approximate the inverse of K(W) would strengthen the practical applicability of the proposed method.

- My other comments or suggestions for improvements are mainly related to the experiment section. While the experiments are valuable, they lack a direct connection to real-world scenarios. Additionally, a more in-depth analysis of parameter choices and their impact on performance, especially in the context of sparse graphs, would enhance the practical value of the work.

### Questions
I thank the authors for their nice work. Here are my questions and comments.

- The authors did a good job in providing several experiments to illustrate their method. Nevertheless, I think it would have been good to propose an experiment on real data that tackles one of the main applications mentioned in the introduction (such as community detection or recommender systems). 

In particular, it is still an ongoing research question to find the right representation of a graph to use spectral methods for community detection. Indeed, using the adjacency matrix is known to be suboptimal in particular when dealing with sparse graphs. That's why people have proposed to use the non-backtracking matrix or the Bethe-Hessian. Since the authors show the interesting possibility to learn the modularity function to automatically selects a graph representation well suited for some downstream task, I think that a very interesting experiment would be to use their method to automatically select a good kernel for community detection. In particular, does the algorithm converge to a representation close to the non backtracking matrix ?


- The authors do not discuss really how some parameters of the method are chosen in practice (such as the parameter $p_{halt}$), and how these choices influence the performance of the algorithm.

- Real world graphs are known to be sparse. It would be interesting to comment of the influence on the algorithm when dealing with sparse graphs. A possibility would be to conduct simulated experiments by varying the sparsity level of the graph and see the impact of the performance.

Here are some typos and additional comments: 

- In Eq.(9), I think a notation is missing since $\alpha$ is not appearing in the mapping $x\mapsto w^{\top} \psi_{K}(x)$. I think the correction would be $x\mapsto w^{\top} \psi_{K_{\alpha}}(x)$.

- At the first line in section 3.1, I think a "for" is missing. It should be "do indeed give unbiased estimates for the graph kernels".

- Between Eq.(13) and Eq.(14), I think there is an issue with the notations. Should $\Phi$ depend on $\tau_j$ ? Based on what I could understand, $\Phi$ is a rectangular matrix of size $n\times N$ where the $j$-th row is $\Phi_j = ((t-\tau_j) \phi(i))_{i=1}^N$.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces techniques to approximate a family of kernels for comparing the nodes of a graph. The methods rely on modulation functions that are either analytically derived from the original kernel, or learned from data by optimizing the downstream task.
Experiments show that as the representation grows the performance improves and that the learned kernels perform well in inductive tasks too.

### Strengths
- The proposed method allows approximating the entire family of kernels based on weighted adjacency matrices.
- Learning the modulation function shows how to successfully retrieve effective kernels within the considered family.
- Examples show how to apply the proposed methods in different scenarios and tasks.
- The paper reads well, and the contribution w.r.t. prior work is fair and clearly stated.

### Weaknesses
 - The proposed method is an extension of previous works, in particular, the random feature mechanism for unbiased approximation of the d-regularised Laplace kernel. While the authors extend this to allow unbiased approximation of any function of a weighted adjacency matrix, the novelty could be better emphasized.
- The experiments do not clearly show the price that one has to pay in terms of compute time when requesting better accuracy. Experiments show only relations between the number of walks and the accuracy/error. Linking accuracy and execution time (e.g., in standard machines) would have given a better sense of the relevance of the proposed methods. A more comprehensive analysis demonstrating the trade-off between computational cost and accuracy, possibly with benchmarks against standard hardware, would be highly beneficial.
- The kernels apply only to weighted graphs without node and edge attributes. This limitation significantly restricts the applicability of the proposed method to real-world scenarios where graphs often contain rich node and edge information.
- The use of the term 'universal' is therefore misleading; as the authors say, the provided random features can approximate only kernels from a specific family. The term 'general' might be more appropriate.

### Questions
- Alg. 1: shouldn't the normalization be $1/\sqrt{m}$ instead of $1/m$?
- Fig. 3: please specify if the extremely narrow shaded area around the lines refers to +/- one standard deviation.
- Sec. 3.4: it is claimed that the modulation function learned on one data set can be effectively applied to other graphs, referring to Tab. 3. However, I don't see specified how the table has been generated. Please provide more details.
- Tab. 3 and 4: I suggest introducing the notation used for the standard deviation.
- I suggest discussing the impact of the fact that the sum in Eq. 2 is not always well-defined - an aspect that is only briefly mentioned in the paper.
- I suggest discussing the pros and cons of symmetric vs asymmetric approaches.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
