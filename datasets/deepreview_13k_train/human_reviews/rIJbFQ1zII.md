# On the Convergence of Adam-Type Algorithms for Bilevel Optimization under Unbounded Smoothness

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
Adam has become one of the most popular optimizers for training modern deep neural networks, such as transformers. However, its applicability is largely restricted to single-level optimization problems. In this paper, we aim to extend vanilla Adam to tackle bilevel optimization problems, which have important applications in machine learning, such as meta-learning. In particular, we study stochastic bilevel optimization problems where the lower-level function is strongly convex and the upper-level objective is nonconvex with potentially unbounded smoothness. This unbounded smooth objective function covers a broad class of neural networks, including transformers, which may exhibit non-Lipschitz gradients. In this work, we first introduce AdamBO, a single-loop Adam-type method that achieves $\widetilde{O}(\epsilon^{-4})$ oracle complexity to find $\epsilon$-stationary points, where the oracle calls involve stochastic gradient or Hessian/Jacobian-vector product evaluations. The key to our analysis is a novel randomness decoupling lemma that provides refined control over the lower-level variable. Additionally, we propose VR-AdamBO, a variance-reduced version with an improved oracle complexity of $\widetilde{O}(\epsilon^{-3})$. The improved analysis is based on a novel stopping time approach and a careful treatment of the lower-level error. We conduct extensive experiments on various machine learning tasks involving bilevel formulations with recurrent neural networks (RNNs) and transformers, demonstrating the effectiveness of our proposed Adam-type algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a variant of Adam called AdamBO, specifically designed for bilevel optimization problems. AdamBO updates the parameters of both the lower-level and upper-level functions simultaneously within a single loop. The authors provide a theoretical convergence guarantee for the hypergradient under an unbounded smoothness condition, which os common in recent theoretical analyses. Additionally, the authors introduce a variance reduction version of AdamBO that achieves improved oracle complexity under stronger conditions.

### Strengths
- This paper gives the first study to investigate the convergence of Adam-type algorithms in the context of bilevel optimization problems. The assumptions made for the theoretical convergence analysis are mostly mild and standard. The results presented are convincing and well-supported by the explanations in the proof sketch.

- The writing in the introduction is relatively clear and comprehensive. Readers can easily follow the motivation behind this study, and the proposed algorithms are explained very clearly.

- In addition to the theoretical guarantees for gradient convergence, the authors provide convincing experimental results that support the performance of AdamBO in bilevel optimization problems.

### Weaknesses
 - The condition in Theorems 4.1 and 5.1 that states $\beta=\tilde \Theta(\epsilon^2)$ is unusual. The default setting for $\beta$ of Adam is 0.1 in Pytorch, and this condition appears to imply poor convergence results for such a default choice of $\beta$. This raises concerns about the practical applicability of the theoretical results, as the required $\beta$ is significantly smaller than what is commonly used in practice. It is not clear how sensitive the algorithm is to this parameter, and whether the theoretical guarantees hold for more practical values of $\beta$. The paper should include a discussion on how to choose this parameter in practice, or provide empirical evidence that the algorithm is robust to deviations from this theoretical requirement.

- Some variables are not provided a definition when introduced, which causes difficulties in understanding. For instance, notations related to stochastic gradients are not explained clearly: $\zeta^{(q,j)}$'s at line 151 seems undefined and a formal definition for this notation needs to be added, particularly regarding the meanings of the superscripts $q$ and $j$. The lack of clarity in the notation makes it difficult to follow the technical details of the analysis. Specifically, it is unclear whether $\zeta^{(q,j)}$ represents a single sample or a batch of samples, and how these samples are related across different values of $q$ and $j$. A more precise definition of the stochastic gradient estimator is needed to ensure the reproducibility and verifiability of the results.

### Questions
See weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper extends the Adam optimizer to address bilevel optimization problems. The authors introduce AdamBO, a single-loop, Adam-based algorithm for bilevel problems with a strongly convex lower-level function and a nonconvex upper-level function, achieving an iteration complexity of O(epsilon^{-4}). They also propose VR-AdamBO, a variance-reduced version that further improves oracle complexity to O(epsilon^{-3}). The proof utilized a randomness decoupling lemma and stopping time approach. The paper demonstrates the effectiveness of these algorithms on one meta-learning dataset.

### Strengths
Extend Adam to bilevel optimization problems, and provide some convergence anlysis.

### Weaknesses
i) The paper requires the coefficient of the learning rate to be 1/(sqrt{v} + lambda) where lambda >0 (it is often called epsilon in Adam papers).
  i.1) This makes the analysis rather weak. In fact, with a positive lambda, the analysis will avoid a major challenge of lower bounding sqrt{v}, making the analysis much easier.
  i.2) There are quite a few constants that depend on lambda >0:
   a) beta < O(lambda);
   b) stepsize eta < O(lambda^1.5 beta) = O(lambda^2.5).
  This makes the effective stepsize always super small (it can be proved that the effective stepsize eta/(sqrt{v} + beta) < eta/beta < lamda^1.5). Then it is somewhat easy to prove Adam converges with an upper bounded stepsize.

ii) The paper requires beta (which is 1 - beta1) to be very small, i.e. the typical beta1 is very close to 1, and the new gradient information comes very slowly. This is a very special variant of Adam, making the result not applicable to general Adam. This significantly weakens the claim of the paper that "Adam-based  bilevel algorithm is proved to converge".

iii) Experiments are relatively weak. AUC minimization of binary text classification is not a common task,and it only uses 3-layer RNN and transformers. Meta-learning on  SNLI with 3-layer RNN and transformers is not that convincing.

### Questions
i) Why do you require beta to be very small? Can you get around the assumption? 

ii) Can you get around the asumption of lambda > 0, or remove the dependence of eta on lambda?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors extend to Adam to solve bilevel optimization problems. The authors proposed two Adam-type algorithms, AdamBO and VR-AdamBO that is a variance-reduced version with an improved oracle complexity of the first one. The authors analysis a novel decoupling lemma that provides refined control over the lower-level variable. Finally, the authors test the effectiveness of their proposed algorithms on some machine learning tasks.

### Strengths
1. the authors provide solid theoretical guarantees for the convergence of their proposed Adam-type algorithms under the unbounded smoothness assumption and other standard assumptions in current bilevel optimization analysis.

2. A novel random decoupling lemma that is proposed by the authors provides a technical tool to control the lower-level error without concerns about the dependency issues from the upper-level randomness. This lemma can be extended to other analysis of Adam-type algorithms for bilevel optimizaition problems.

### Weaknesses
1. The author did not provide a clear comparison of the assumptions and the complexity of the newly proposed algorithms with popular algorithms that appeared in previous literature in the paper.

2. The theoretical convergence results provided by the author, whether in AdamBO or VR-AdamBO algorithms, cannot guarantee that the first-order momentum coefficient is a constant, that is, the coefficient depends on the accuracy level $\epsilon$. This dependence on $\epsilon$ for the momentum parameter is a significant limitation, as it requires a precise tuning of the parameter based on the desired accuracy, which is often unknown beforehand. This makes the practical application of the proposed algorithms more challenging, as a fixed momentum parameter would be more desirable for ease of use and robustness.


### Questions
1. In your assumption 3.5: “….. almost surely ”, what does “almost surely” mean?

2. In the part of VR-AdamBO, you state that “VR-AdamBO can be regarded as a generalization of the AccBO….., with the key difference being that AccBO uses normalized SGD with momentum for the upper-level update,…”, so do you mean that you adopted the same variance reduction technique as AccBO, the only difference being the way you update the upper level variables?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents AdamBO, a novel extension of the Adam optimizer designed for bilevel optimization problems, particularly when the upper-level function exhibits unbounded smoothness. The authors address the challenges inherent in bilevel optimization, such as the dependency between the upper-level hypergradient and lower-level variable. The work also introduces VR-AdamBO, a variance-reduced variant, to enhance convergence efficiency. Both algorithms demonstrate provable theoretical convergence guarantees and are validated through experiments on tasks involving RNNs and transformers, showing significant performance improvements.

The authors also proves that AdamBO converges to $\varepsilon$-stationary points with $O(\varepsilon^{-4})$ oracle complexity. The variance-reduced variant VR-AdamBO has an improved oracle complexity of $O(\varepsilon^{-3})$.

### Strengths
1. The authors provide comprehensive and solid convergence proofs for both AdamBO and VR-AdamBO, incorporating novel elements such as a randomness decoupling lemma and stopping-time analysis for variance reduction. These theoretical insights are significant and may be of independent interest for future research.
2. The algorithms are tested on relevant machine learning tasks, including meta-learning and deep AUC maximization, showing strong empirical performance.

### Weaknesses
1. Instead of stacking all the assumptions and lemmas, I think a better way to present your theoretical results is that placing the detailed proof sketch in the main text and moving some assumptions and lemmas to the appendix. Also, it would be better if you can clearly state the difficult part of the proofs as well as the comparison and difference with other relevant works. The current version is quite difficult for the audience to understand the entire line of the proof.

### Questions
Please refer to the "weaknesses" part for the questions.

### Soundness
3

### Presentation
2

### Contribution
3
