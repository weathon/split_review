# Non-negative Tensor Mixture Learning for Discrete Density Estimation

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
\pdfbookmark[-1]{Tensor Mixture Learning}{top}
We present an expectation-maximization (EM) based unified framework for non-negative tensor decomposition that optimizes the Kullback-Leibler divergence. To avoid iterations in each M-step and learning rate tuning, we establish a general relationship between low-rank decomposition and many-body approximation. Using this connection, we exploit that the closed-form solution of the many-body approximation can be used to update all parameters simultaneously in the M-step. Our framework not only offers a unified methodology for a variety of low-rank structures, including CP, Tucker, and Train decompositions, but also their combinations forming mixtures of tensors as well as robust adaptive noise modeling. Empirically, we demonstrate that our framework provides superior generalization for discrete density estimation compared to conventional tensor-based approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies negative tensor decomposition that optimizes the Kullback-Leibler divergence. To avoid iterations in each M-step and learning rate tuning, they establish a general relationship between low-rank decomposition and many-body approximation. The framework offers not only a unified methodology for a variety of low-rank structures, including CP, Tucker, and Train decompositions, but also their combinations, forming mixtures of low-rank tensors. The weights of each low-rank tensor in the mixture can be learned from the data, which eliminates the need to carefully choose a single low- rank structure in advance

### Strengths
The logic of the paper is reasonable to me that they want to optimize each block in an alternating minimization/maximization way, the experiments look good and rich, demonstrating the benefit of the proposed algorithm.

### Weaknesses
I don't see novel contribution in this paper, to me, the nonnegative tensor factorization is well studied in both distance and divergence. The author find the optimal solutions by making use of EM or alternating method including weights $\eta$'s, which is well known.



### Questions
Is there any theoretical guarantee that your updating algorithm can converge to local minimal or global minimal. Though the objective is nonconvex, but there exists a wide class of factorization problem that local minimal is also global.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents an expectation-maximization (EM) based unified framework for nonnegative tensor decomposition that optimizes the Kullback-Leibler divergence, and further establishes a general relationship between low-rank decomposition and many-body approximation. The proposed framework offers a unified methodology for a variety of low-rank structures, including CP,
Tucker, and Train decompositions, and their combinations. A series of experiments are carried out to illustrate the merits of the developed methodology.

### Strengths
1. A unified methodology has been developed to deal with a variety of low-rank structures, including CP, Tucker, Train decompositions, and  their combinations, forming mixtures of low-rank tensors. 
2. A mixture of low-rank tensor modeling procedure is developed  to empirically demonstrates inferential robustness and improved generalization.
3. Both theoretical analysis and numerical comparisons are provided to show the merits of the proposed methodology.

### Weaknesses
1. The convergence analysis seems overly coarse and somewhat redundant, as it only demonstrates that negative cross-entropy increases with iterations—an expected result given the maximization objective. More importantly, the analysis should address how negative cross-entropy could converge to the true value, and ideally provide bounds on the suboptimality of the solution. The current analysis lacks any guarantee of convergence to a global or even a local optimum, which is a critical aspect for the practical application of the proposed method.

2. Please note that the computational cost of the proposed algorithm increases significantly with the size of the tensor. Kindly provide the specific order of computational complexity and compare it with the complexity orders of related algorithms. It is essential to detail the computational cost in terms of tensor dimensions, rank parameters, and the number of iterations. A comparison with existing methods should also consider memory requirements, not just time complexity, as this can be a limiting factor for large-scale tensor decompositions.

3. The compared baselines are not SOTA. Please consider some recent methods for numerical comparisons. The experimental section should include a broader range of state-of-the-art methods to properly benchmark the proposed approach. The selection of baselines should be justified, and the experimental results should clearly demonstrate the advantages of the proposed method over the most relevant alternatives.

4. Please provide a detailed description of the convergence conditions in Algorithm 1. It is not sufficient to state that the algorithm converges; the specific criteria used to determine convergence, such as a threshold on the change in the objective function or the parameters, should be explicitly stated. The impact of these conditions on the convergence speed and the quality of the solution should also be discussed.

### Questions
Is there a specific general mathematical expression for the many-body approximation?

### Soundness
3

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
3

### Summary
This paper aims to parsimoniously unify a variety of low-rank tensor decomposition structures and address discrete density estimation using a novel mixture of decompositions method. The method permits mixtures of CP, Tucker, and tensor-train decompositions to model non-negative data. The authors derive a computationally efficient expectation-maximization (EM) algorithm for performing inference in their model. The inference algorithm allows for learning of the mixture weights of the components, which are tensor decompositions. In addition to establishing a unifying framework for low-rank tensor decompositions, the authors demonstrate their method’s effectiveness in estimating discrete mass functions by comparing a specific instance of their method, EMCPTrain, to a large body of existing ones. Their method achieves marginally better negative-log-likelihood per sample than existing methods.

### Strengths
The contribution of closed-form maximization updates for the specific EM algorithm is a strength. The computational efficiency, in some instances of the method (such as EMCPTrain), are useful. The unifying framework across low-rank tensor decompositions is parsimonious, and leveraging the parsimony of mixture models is a neat idea. I particularly like how the authors show that one may learn the weights of their mixture model, removing the need to choose between low-rank structures in advance of training.

### Weaknesses
The approach, while unifying in theory and a neat idea, yields very incremental empirical results at best. The empirical gains are modest. When more baselines are taken into account, as in Table 6, the gains are further reduced. The comparisons and evaluations are not well-organized, making the aggregate contribution difficult to evaluate across the many tables in Section 5 and Appendix C. There are some section of the paper that came across as unclear that first time I read it. In particular, the paper refers to “many-body approximation” many times in the first two sections of the paper without a clear definition. A formal definition in Section 1 would help clarify how the paper aims to leverage the many-body approximation representation.

### Questions
In my experience, adding a noise (or constant tensor) term to a non-negative tensor decomposition can significantly improve model fit, and the empirical results shown in Table 2 mostly demonstrate this phenomena. How much of the empirical improvements in negative log-likelihood are from the adaptive noise term? I view the ability to seamlessly learn the noise term from the data as an advantage of this method, although I am concerned it is the only substantial advantage of this method in practice. 
When would it be useful to include a Tucker component in practice? EMTucker is computationally expensive, scaling as R^D. While EMTuckerN beats existing methods in Table 5, it generally performs worse than EMCPTrainN.

### Soundness
2

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
3

### Summary
The work deals with a nonnegative tensor decomposition algorithm for discrete density estimation. The framework is based on expectation maximization algorithm from KL divergence minimization perspective. Unlike the existing KL divergence-based nonnegative tensor decomposition algorithms for this problem that used gradient-based iterative steps for parameter updates, the proposed approach leverages the insights from the many-body approximation problem. Consequently, the updates of the parameters in the M-step boils down to closed form expressions, reminiscent of the updates derived in (Huang & Sidiropoulos,2017; Yeredor & Haardt, 2019) .

### Strengths
Strengths:

1.	The proposed tensor decomposition method is a general framework that can handle different types of tensor decomposition models like CP, Tucker and tensor train, innovatively utilizing the many body approximation technique from the (Ghalamkari et al.,2023). The closed-form updates of the parameters in the M-step of the EM algorithm is also attractive as it avoid tuning of any hyperparameters, which is often practically inconvenient

### Weaknesses
Weakness:

1.	The paper organization has lot of room for improvement. From the start of the paper, a clear description of problem is missing. Section 4 introduces the problem statement, while section 3 starts describing the approach (many-body approximation). Then, it is confusing to connect and understand that some of the terms have been obtained from the previous step of the algorithm.

2.	The problem formulation and the application of the solution itself is debatable. The tensor ${\cal T}$ is an empirical distribution tensor which is of the dimension of the categorical features. The entire solution of discrete density learning depends on the accuracy of the empirical tensor, which is hard to make sure due to curse of dimensionality. The method's reliance on a high-dimensional empirical tensor makes it susceptible to noise and inaccuracies, especially when the number of samples is not sufficiently large compared to the dimensionality of the categorical features. This is a fundamental limitation that needs to be addressed with more robust techniques.

3.	The problem is hardly scalable as it deals with the many-body approximation tensor ${\cal M}$ whose dimension is much larger than that of even the empirical tensor ${\cal T}$. While the authors claim that the many-body approximation tensor is sparse, the practical implications of this sparsity on computational complexity are not fully explored. The memory requirements for storing and processing this tensor, even if sparse, could still be prohibitive for high-dimensional data. Furthermore, the computational cost of performing operations on this sparse tensor, such as the expectation step in the EM algorithm, needs to be analyzed in more detail.

4.	The experiments and major baselines are lacking. In discrete density estimation, there are works using second and third order marginals, that can mitigate the curse of dimensionality problem to an extent.

a.	Kargas, Nikos & Sidiropoulos, N.D. & Fu, Xiao. (2017). Tensors, Learning, and “Kolmogorov Extension” for Finite-Alphabet Random Vectors. IEEE Transactions on Signal Processing. 66. 10.1109/TSP.2018.2862383.

b.	S. Ibrahim and X. Fu, "Recovering Joint Probability of Discrete Random Variables From Pairwise Marginals," in IEEE Transactions on Signal Processing, vol. 69, pp. 4116-4131, 2021, doi: 10.1109/TSP.2021.3090960

Discussions and comparisons with these baselines would help readers understand the strength of the approach (if any). The lack of comparison with methods that use marginals, such as those in [1, 2], makes it difficult to assess the proposed method's performance in mitigating the curse of dimensionality. The authors should include these baselines to provide a more comprehensive evaluation.

### Questions
Questions/Comments:

1.	Writing and Organization: It is important to introduce the low-rank tensor structures when discussing it in the introduction. 

2.	It is commented that “it always converges regardless of the choice of the low-rank structure assumed in the model.” EM convergence is hard to establish unless it is well initialized. Hence, it is not easy to claim convergence for the proposed method

3.	While there is a technique introduced to reduce the computational complexity of tensor train decomposition as presented in Section 4.2, computational complexity of Tucker remains the same which becomes dominant especially the case of K>1 mixture cases. The convergence speed curves should be presented with time in x axis to understand where it stands with respect to the baselines. Due to the computational complexity, it is also challenging to utilize the mixture model in practice. Once may need to choose the component of the mixtures (the type of tensor decomposition) , rather than allowing the model to learn by itself. A detailed discussion on the limitation of the approach (in the main section) would help here. 

4.	It is unclear how does the adaptive noise term guarantees the ``convexity” and convergence as claimed in Section 4.4. What do you mean by convexity here? How do you learn the noise parameter here? Do you learn different noise parameter for different low-rank tensor models?

5.	Experiments are limited to showing negative log likelihood. While it shows the dynamics of the algorithm, it does not show how does the approach learn the ground-truth. Simulation studies would help understand how well the method learns the true discrete density. In real data experiments, missing value prediction should be a better approach to understand the applicability of the approach.

6.	Minor typos: “distribution underlying the data” in Page 5, notation $\eta^k$ is confusing with $\eta$ raised to kth power.

### Soundness
2

### Presentation
2

### Contribution
3
