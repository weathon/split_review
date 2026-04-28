# Nonparametric Classification on Low Dimensional Manifolds using Overparameterized Convolutional Residual Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Convolutional residual neural networks (ConvResNets), though \emph{overparametersized}, achieve remarkable prediction performance in practice, which cannot be well explained by conventional wisdom. To bridge this gap, we study the performance of ConvResNeXts trained with weight decay, which cover ConvResNets as a special case,  from the perspective of nonparametric classification. Our analysis allows for infinitely many building blocks in ConvResNeXts, and shows that weight decay implicitly enforces sparsity on these blocks. Specifically, we consider a smooth target function supported on a low-dimensional manifold, then prove that ConvResNeXts can adapt to the function smoothness and low-dimensional structures and efficiently learn the function without suffering from the curse of dimensionality. Our findings partially justify the advantage of \emph{overparameterized} ConvResNeXts over conventional machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops the approximation and estimation theory of Convolutional Residual Neural Networks. This paper shows that ConvResNeXt networks can well adapt to a smooth function on a low-dimensional manifold both in approximation and generalization. The authors provide theoretical justification for the overparameterization of such networks as well as training such networks with weight decay.

### Strengths
- The authors perform strong, rigorous analysis and develop interesting theoretical guarantees for ConvResNeXt, a well-known network structure that has enjoyed remarkable performance on real applications. This paper is a great contribution to the understanding of such network structure. 
- The ideas of proof are novel and interesting to me.

### Weaknesses
 - The paper does not provide a direct comparison with prior research on different NN architectures and function spaces. It's not clear to me how this work different from prior ones, and what are the theoretical advantages of your network structure. Specifically, the paper should clarify how the analysis of ConvResNeXt differs from analyses of parallel feedforward networks or standard ResNets, especially regarding metric entropy bounds and the impact of overparameterization. The lack of a clear comparison makes it difficult to assess the novelty of the theoretical results.
- The paper is restricted to binary classification with empirical logistic loss. Are your findings extendable to other losses? It is unclear whether the theoretical guarantees hold for other commonly used loss functions, such as cross-entropy loss or mean squared error, and under what conditions these extensions are valid.
- The paper is not written in clear language. Some sentences are unfinished, for example the 4th line on page 7. This lack of clarity hinders the understanding of the technical details and makes the paper difficult to follow.
- No numerical experiments are conducted to support the theoretical findings. The absence of empirical validation makes it hard to assess the practical relevance of the theoretical results. The paper should include experiments that demonstrate the performance of ConvResNeXt networks in settings that align with the theoretical analysis, including the impact of weight decay and the behavior on low-dimensional manifolds.

### Questions
- For remark 1, it's not clear to me why there is only a small number of non-trivial blocks. It is also unclear to me why weight decay plays a crucial role here. 
- Why is there no curse of dimensionality in your problem setting? Is this because of the ConvResNeXt structure, the Besov function space or other assumptions? 
- The authors claim that ConvResNeXts can 'efficiently learn the function without suffering from the curse of dimensionality'. What does 'efficiency' here mean, sample efficiency or computational efficiency? 
- The authors claim that ConvResNexts learn Besov functions with a better convergence rate close to the minimax rate, which is significantly faster than NTK methods. What is the intuition behind this discovery?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies weight decay regularized training of overparameterized convolutional neural network through the lens of nonparametric classification. In particular, the authors consider ConvResNeXts, which cover ConvResNets, and show that such training induced sparsity. This explains why overparameterized neural networks generalize. The authors then prove that the estimation error of ConvResNeXts of functions supported on a smooth manifold deponds on their ambient dimensions. Thus, the curse of dimensionality does not occur.

### Strengths
- The paper is well-written, and the problem addressed is important to the community.
- I like the fact that the authors study overparameterization of ConvResNets, although not directly.

### Weaknesses
 - Since Theorem 4 depends on finding the global optimizer, I wonder if this is too strong of an assumption. Specifically, the analysis relies on the existence of a global minimizer for the regularized empirical risk, which is a significant assumption given the non-convex nature of neural network training. While weight decay does encourage sparsity and can lead to better generalization, it is not guaranteed to find the global optimum. The theoretical results would be more compelling if they could be tied to the behavior of practical optimization algorithms, such as stochastic gradient descent (SGD), which are not guaranteed to converge to global minima, especially in highly non-convex loss landscapes. The current analysis does not address the gap between the theoretical global optimum and the solutions found by practical training methods. This discrepancy raises questions about the practical relevance of the theoretical findings.


### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the capacity of Convolutional residual networks to approximate and estimate smooth (Besov) functions on smooth manifold. The paper focuses on the ConvResNext architecture, a convolutional network with residual connections and parallel modules. The paper shows that these networks can approximate arbitrary smooth target functions supported on a smooth manifold, without suffering from the curse of dimensionality, i.e. with no exponential dependence on the extrinsic dimension of the problem. The work also studies an estimation result, giving a generalization bound for ConvResNext architecture trained on smooth functions on manifolds.

### Strengths
The paper provides novel generalization and approximation results on residual convolutional networks fitting smooth functions on manifolds.

### Weaknesses
While both the approximation and generalization results seem novel, it is not clear to me whether the derived bounds are interesting in the context of learning with convolutional networks. In particular, it seems that the approximation results hold just as well for standard feedforward networks, and the main contribution of this work is transforming these bounds from densely connected networks to convolutional networks. The work relies on a result stating that any feedforward network can be reformulated as a convolutional network. Given this result, this just means that any property that holds for feedforward networks holds to some extent for a conv-nets. The property of approximating smooth functions on a manifold seems to be just a particular case where this argument applies. Conv-nets are typically used in cases where they display significant benefits over densely connected feedforward, and I believe this should be reflected in the theoretical results. I think the authors should clearly state the following:
1) Which of the results in the paper also apply to feedforward networks?
2) For the results that apply to feedforward networks, which of them are novel to this work? E.g., is the approximation bound on smooth functions on a manifold has been already established for feedforward networks?
3) In which results there is an actual benefit for using a convolutional networks compared to feedforward dense networks?

Another more minor issue is with the presentation of the approximation and generalization bounds. If I understand correctly, some of the constants in the bounds have exponential dependence on the intrinsic dimension of the manifold, and it is interesting to show this dependence explicitly.

Minor:
- Definition 6: there seems to be a typo, with some unclosed bracket.
- Bottom of page 5: "hyperparameters parameters" should be just "hyperparameters"?
- Top of page 7: "our This"

### Questions
See above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide a nonparametric analysis of ConvResNeXts---a generalisation of deep convolutional residual networks. In particular, the authors derive approximation and estimation bounds when the target function is in the Besov class, that is the class of functions supported on a low-dimensional differential manifold and having controlled smoothness. In particular, the estimation result shows that ConvResNeXts achieves a rate of error convergence close to the minimax rate.

### Strengths
The paper makes a good combination of several ideas on neural network construction and generalization estimation. The central results are clear and easy to locate. Most claims are well-supported and section 4 is extremely useful in understanding the proofs.

### Weaknesses
The lack of a strong comparison with previous works makes it difficult to appreciate the impact of the result. The adaptivity to the data distribution is a well-known property of fully connected networks of any depth (even in the kernel regime), which makes me doubt the necessity of developing a theory of ConvResNeXts. What insights do we get from the analysis that requires using ConvResNeXts?

Secondly, I found the definition of Besov spaces too dense and, hence, difficult to understand. Perhaps a few examples would help, as well as a more detailed account of how such spaces generalise Sobolev and Holder spaces, which are known to a wider audience.

### Questions
1. The brief definition of ConvResNeXts at the end of the second paragraph does not suffice to understand the architecture.

2. Adding a quick definition of Besov spaces when they are first mentioned in the third paragraph would improve readability. It is not reasonable that a reader unfamiliar with these spaces should wait until the conclusions to read a comment on their nature. In addition, the paragraph explaining besov spaces in the conclusions would benefit from further clarification, e.g. some way to understand why Holder and Sobolev is contained in Besov and concrete support to vague claims such as 'Besove spaces can capture important features such as edges'.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
