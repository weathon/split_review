# MAST: model-agnostic sparsified training

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
We introduce a novel optimization problem formulation that departs from the conventional way of minimizing machine learning model loss as a black-box function. Unlike traditional formulations, the proposed approach explicitly incorporates an initially pre-trained model and random sketch operators, allowing for sparsification of both the model and gradient during training. We establish insightful properties of the proposed objective function and highlight its connections to the standard formulation. Furthermore, we present several variants of the Stochastic Gradient Descent (\SGD) method adapted to the new problem formulation, including \SGD\text{ }with general sampling, a distributed version, and \SGD\text{ }with variance reduction techniques. We achieve tighter convergence rates and relax assumptions, bridging the gap between theoretical principles and practical applications, covering several important techniques such as Dropout and Sparse training. This work presents promising opportunities to enhance the theoretical understanding of model training through a sparsification-aware optimization approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Model-Agnostic Sparsified Training (MAST), a novel optimization framework tailored for sparsification in model training. By defining a new objective that incorporates pre-trained models and random sketch operators, MAST allows for simultaneous model and gradient sparsification during training. The authors propose modified SGD-based algorithms to handle this objective, offering both single-node and distributed variants. Experimental results highlight the approach’s efficacy, showing MAST’s superior robustness to pruning compared to standard models.

### Strengths
1. **Theoretical contribution:** The framework introduces a structured approach to sparsification in training, with rigorous theoretical analysis of convergence for both convex and non-convex cases.

2. **Relevance:** This paper addresses a very relevant topic in the field.

3. **Scalability:** Extending the method to a distributed setting enables applications in federated learning and distributed subnetwork training.

4. **Experiments:** Experiments validate MAST’s practical benefits, showing improved performance and robustness over traditional approaches.

5. **Presentation:** The paper is very well-written, with clear explanations and a consistent, clean notation.

### Weaknesses
Although the assumptions for the theoretical results are standard, they are overly restrictive and may limit real-world applicability.

### Questions
Could the MAST framework potentially be extended to conditional computing approaches, such as mixture-of-experts models or sparse gating mechanisms in neural networks? Specifically, do you see any pathways for adapting MAST to support dynamic routing or conditional activation, as seen in these architectures?

### Soundness
3

### Presentation
4

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
This paper introduced a new optimization formulation called MAST that considers a modified loss function $\mathbb{E}[f_S(x)] =\mathbb{E}[f(v+S(x-v))] $ rather than a standard loss $f(x)$. Here, $S$ is a random matrix sampled from distribution $\mathcal{D}$, and $v$ can be viewed as a pre-trained model. The paper claims that this problem formulation can model various practical machine learning techniques including Dropout and Sparse training with a sparse matrix $S$.

Main theoretical results include comparisons between the modified loss formulation and the standard loss, as well as convergence analysis in both non-convex and (strongly) convex settings. The paper also extends convergence analysis in the distributed setup. Experimental studies are also provided to test the proposed algorithms and MAST properties.

### Strengths
The presentation of the paper is good, and all the proofs are well-organized and written clearly.

### Weaknesses
1. It is unclear why a linear transformation $v+S(x-v)$ in $f_S$ is good enough to model practical ML techniques that authors consider in this paper. The reason for putting such a linear transformation rather than more complicated nonlinear transformations is lacking.

2. Because of this simple linear transformation, the resulted comparison and convergence analysis are quite standard and lack novelties, so is for the distributed setup. The authors also admit that the convergence results are standard for convex and non-convex analysis. 

3. Rigorous mathematical connections between the model and Dropout and Sparse training are missing. Since both Dropout and Sparse training are techniques in the neural network training, it would be nice to quantitatively analyze how the model $f_S$ approximate the sparsified neural networks.

### Questions
1. I wonder if the convergence results could be extended under weaker assumptions on $f$, perhaps by assuming that $f$ only satisfies Lojasiewicz-type conditions?

2. Is it true that $f_{\mathcal{D}}^{inf}\geq f^{\inf}$? I don't see that in the second line of Theorem 1, but it is needed for (13), Theorem 3 and Corollary 1.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents MAST, which optimizes the expected value of a function $f$ composed with a sketching matrix $S$. The authors analyze theoretical properties and develop a solution algorithm, demonstrating its effectiveness for sparse neural network training. The authors also provide experiments to validate their method.

### Strengths
The paper is well motivated, and the formalization of the problem is interesting. The authors provide a thorough analysis of the problem properties and derive an algorithm based on SGD to solve it. The assumptions are clearly stated and the theoretical results are well proven.

### Weaknesses
While I appreciate this research, I have a few concerns and questions regarding the contribution and novelty of the work, which I explain in detail below. I hope that these remarks are helpful in improving the work and I am happy to discuss my evaluation.

- MAST bears a clear relationship to standard (stochastic) gradient descent. In supervised learning, the objective is to minimize the expected loss of a model with respect to the distribution of features and labels. Similarly, MAST aims to minimize the expected value of a function $f$ composed with a sketching matrix $S$, where the expectation is taken over the distribution of the sketching matrices. This could be made more clear in the paper.
- While Assumption 1 appears valid since it shows $S^T\nabla f(x)$ is an unbiased estimator of $\nabla f(x)$, there is a discrepancy in Example 1. The authors state their sketching matrix $S$ formulation models Dropout, but to the best of my knowledge, standard Dropout applies a binary mask to activations without rescaling weights. The connection between these approaches needs clarification in their problem formulation. Furthermore, the paper applies the mask to weights, not activations, which is another discrepancy with standard Dropout.
- The problem properties in section 3 appear to be correct. However, apart from Theorem 1,these are well known properties of smooth and strongly convex functions. It is not clear how novel the results in this section are, given that the proofs are rather elementary and known. Specifically, the proofs rely on standard properties of smooth and strongly convex functions, such as the linearity of expectation and the fact that composition with an affine mapping preserves convexity and smoothness. The application of these properties in the context of a stochastic optimization problem with a sketching matrix is not sufficiently novel.
- In Theorem 1, it is assumed that Assumption 2 and Assumption 3 hold, in particular that $f$ is strongly convex, implying there is a unique minimizer $x^*$. Why is then an optimal set of solutions $\mathcal{X}^*$ mentioned? By Lemma 3, the same should hold true for the solutions to the MAST problem. Can the theorem be simplified or made more precise?
- The paper is well written and the proofs appear to be correct. I find the setting interesting, especially that it allows modelling sparsification. However, it is not entirely clear to me how novel the results are, as many of the results are well known properties of smooth and strongly convex functions.

I appreciate the experiments, however there are a few points that could be improved:
- The plots in the experiments should have the same scale to allow for a comparison of the methods.
- Did the authors compare the method to standard gradient descent with Dropout? Since MAST introduces a rescaling of the gradient and that is not present in standard gradient descent with Dropout, it is not clear how the two methods compare to each other. Furthermore, the paper applies the mask to weights, not activations, which is another discrepancy with standard Dropout.
- Currently, the experiments seem to be somewhat limited. Can the authors provide more experiments, potentially at a larger scale?

### Questions
- The authors formulate MAST with a general sketch matrix $S$, but in the experiments they only consider diagonal matrices as sketching matrices. Could the authors provide examples of non-diagonal sketching matrices that could be useful in practice?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an optimization framework that incorporates model sparsification using pre-trained models and stochastic sketches for enhanced computational efficiency. The authors propose an objective function that departs from traditional approaches, aiming to improve convergence rates in stochastic gradient descent (SGD) for sparse or resource-constrained environments. They also provide theoretical analyses on the convergence of their proposed algorithms and demonstrate potential applications for both centralized and distributed machine learning scenarios.

### Strengths
The paper certainly brings a fresh perspective by introducing a sparsification-aware objective function that enables gradient sparsification during training. This idea is both innovative and timely, addressing the growing need for more efficient model training techniques.

On the theoretical side, the authors provide a strong mathematical foundation. They successfully derive convergence bounds for various setups, including challenging non-convex scenarios and methods that reduce variance, which adds significant depth to their work.

The experimental results are compelling and back up the theoretical claims. They show that the MAST method outperforms traditional approaches, especially when dealing with high levels of sparsity. This makes the findings relevant and applicable to real-world situations.

### Weaknesses
One downside is that the experimental setup doesn't include a wide range of comparisons to other sparsification or dropout methods beyond ERM. Adding these comparisons would help better highlight where MAST excels and where it might fall short. The experiments are also somewhat limited in terms of the neural network architectures tested. The study focuses on logistic regression and ResNet-50, but there's not a strong justification for this choice. Specifically, the lack of comparison to methods like variational dropout, or other structured sparsity techniques, makes it difficult to assess the true novelty and practical impact of MAST. Furthermore, while ResNet-50 is a common architecture, the experiments do not explore how MAST behaves with different layer types (e.g., recurrent layers) or model sizes, which limits the generalizability of the findings.

### Questions
1. Can you give an idea of computational and memory overheads of using sketch matrices and sparsification compared to traditional methods?

2. I'm curious about how MAST performs with larger, non-convex models like deep neural networks. Testing it on a complex neural network, even briefly, could demonstrate its applicability beyond logistic regression.

3. How robust is MAST to variations in hyperparameters like step size and sparsity, especially in heterogeneous distributed environments?

### Soundness
3

### Presentation
3

### Contribution
3
