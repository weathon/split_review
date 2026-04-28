# Optimization on Manifolds with Riemannian Jacobian Regularization

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Understanding the effectiveness of intrinsic geometry in enhancing a model's generalization ability, we draw upon prior works that apply geometric principles to optimization and present a novel approach to improve robustness and generalization for constrained optimization problems. This work aims to strengthen the sharpness-aware optimizers and proposes a novel Riemannian optimizer. We first present a theoretical analysis that characterizes the relationship between the general loss and the perturbation of the empirical loss in the context of Riemannian manifolds. Motivated by the result obtained from this analysis, we introduce our algorithm named Riemannian Jacobian Regularization (RJR), which explicitly regularizes the Riemannian gradient norm and the projected Hessian. To demonstrate RJR's ability to enhance generalization, we evaluate and contrast our algorithm on a broad set of problems, such as image classification and contrastive learning across different datasets with various architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an optimization approach called Riemannian Jacobian Regularization for improving model generalization and robustness in constrained optimization problems. The authors first provide theoretical analysis showing how the population loss relates to empirical loss through Riemannian gradients and projected Hessians on manifolds. Based on this analysis, they develop the RJR algorithm which explicitly regularizes both the Riemannian gradient norm and the Jacobian while optimizing on manifolds. The authors demonstrate RJR's effectiveness across multiple tasks including supervised learning, labeled self-supervised learning, and unlabeled self-supervised learning, testing on various datasets and model architectures.

### Strengths
The paper considers both theoretical justifications as well as algorithms motivated from the theoretical development. A number of experiments have been provided to justify to proposed algorithm.

### Weaknesses
Major comment:


1. The theorem 2 of the paper of Foret et al 2021b seems to be a Euclidean version of the Theorem 1 of this paper. Instead of having norms of gradients and hessians of the loss function, they have max_(|eps| < rho) L_S(theta+eps), i.e., the maximum empirical loss over a rho-neighborhood of the given parameter theta. One can imagine that if L_S is (locally) smooth with respect to theta then this term can be further bounded by norms of gradients and hessians using Taylor expansion arguments. On the other hand, L_S could have been non-smooth, e.g., it can be locally oscillating heavily but with small magnitudes, leading to Foret’s term still be bounded while the norms of gradients and hessians can explode. Do I miss something? If not, what are the benefits of working with a setting that needs a stronger assumption on local smoothness?
2. What do you mean by robustness? A priori one could think about robustness against adversarial pertubations in the input, distribution shift, randomness in the optimization dynamics, to name a few. Further, what set of experiments demonstrate the claim of “improving robustness”?

Minor comments:


1. The K-lipschitz assumption is in the restated version of Theorem 1 in the appendix but missing in the one in the main body.
2. Table 1 is somewhat hard to read. Perhaps keeping three significant figures would allow one to make the fonts larger - at any case, an accuracy 90.01 is not so different from 90.02.  Also, what are the numbers in parentheses in the last row? I presume it is the standard variance, but neither the caption nor the text in line 380 describes it.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a Riemannian Jacobian Regularization technique to improve the generalization ability of deep models. The authors argue that by incorporating the Jacobian regularization on a Riemannian manifold, they can better capture the geometric structure of the parameter space, leading to improved performance in terms of generalization error. The theoretical analysis provides bounds on the generalization error, and empirical results demonstrate the effectiveness of the proposed method.

### Strengths
(1) This work tackles an important problem in deep learning, i.e., enhancing generalization, which is crucial for improving the models' robustness in real-world applications.

(2) The theoretical framework builds on well-established concepts in Riemannian geometry, providing a mathematically sound approach to regularization.

(3) The experimental results on different benchmarking datasets in supervised and self-supervised settings show the effectiveness of using the proposed RJR.

### Weaknesses
 (1) Limited Theoretical Novelty: The theoretical contributions of this paper, e.g., Theorem 1, appear to rely on existing works (or experience) in the field of generalization theory, such as:
[a]. Hoffman, J., & Ma, Y. (2019). "Robust learning with Jacobian regularization." arXiv preprint arXiv:1907.05895.
[b]. Neyshabur, B., Tomioka, R., & Srebro, N. (2015). "Norm-based capacity control in neural networks." In Proceedings of the Conference on Learning Theory (COLT).
Hence, the lack of truly novel theoretical insights may weaken the originality of the paper. Addressing the limitations of current generalization bounds in the context of manifold-based regularization would be a meaningful addition.

(2) Methodological Contribution Needs Further Justification: Although the idea of Jacobian regularization on Riemannian manifolds is interesting, this paper lacks sufficient justification for why the proposed RJR would outperform or provide benefits compared to other regularization methods. Therefore, additional experiments comparing RJR to other regularization techniques (e.g., adversarial training, dropout) across a variety of tasks and architectures would help clarify its distinct advantages.

(3) Empirical Evaluation is limited: The experiments are conducted on a limited range of datasets and models. Expanding the empirical evaluation to include diverse datasets and model architectures would strengthen the paper. A key aspect is that this paper is about optimization on the Riemannian manifolds, but the authors do not applied the suggested RJR to Riemannian networks, such as SPDNet [c], SPDNetBN [d], GrNet [e], RResNet [f]. Additionally, it would be helpful to include ablation studies to show the sensitivity of the method to key hyperparameters, such as the choice of Riemannian manifolds, $\epsilon$, $\rho$.
[c] A riemannian network for spd matrix learning, AAAI, 2017.
[d] Riemannian batch normalization for SPD neural networks, NeurIPS, 2019
[e]  Building deep networks on grassmann manifolds, AAAI, 2018
[f] Riemannian residual neural networks, NeurIPS, 2023.

(4) Insufficient explanation: The role of the second term in $sigma_t$ (line 248) is unknown. In Section 5.2, the authors mentioned that enforcing orthogonality on the convolutional filters has some benefits, such as alleviating gradient vanishing. However, the basic reason is unknown, making the applicability of the proposed RJR unconvincing. Again, the authors are suggested to evaluate the effectiveness of RJR under end-to-end Riemannian networks when compared with RSGD and RSAM.

(5) Another limitation of this paper is that the English writing is obscure, especially in the proposed method section. In other word, it is  challenging for readers who are not already familiar with Riemannian geometry and Riemannian optimization.

(6) In line 356, $s$ means what?. In Fig. 2, why select $\lambda_5$. Figs. 2 and 3 are not vector graphics.

### Questions
Please refer to the weaknesses part for detailed information.

### Soundness
3

### Presentation
2

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
This paper introduces Riemannian Jacobian Regularization (RJR), a method that combines sharpness-aware and Jacobian regularization on Riemannian manifolds to improve generalization and robustness. The approach is tested on various supervised and self-supervised tasks.

### Strengths
RJR presents a straightforward optimization technique that improves generalization by explicitly controlling sharpness on Riemannian manifolds.

### Weaknesses
1. In Thm.1, why there is an ambient inner product, instead of the Riemannian ones? Will this cause the loss of some information?
2. Experiments are not convincing
   - Most datasets are small
   - The reason for not comparing it with RSAM under the same datasets as the original paper is unclear.
   - A common counterpart is the trivialization [1]. Trivializations could be faster and sometimes even better than the Riemannian ones. The missing comparison makes the empirical validation not convincing.
   - For the orthogonal constraints, why do not compare with some orthogonal tricks [2] is not clear
   - There are Riemannian networks, where data and parameters naturally lie in the manifold, such as SPD [3-4], Grassmannian [5-6], Lie groups [7], and hyperbolic [8]. How about the effects on these networks? Some works prefer to use trivialization, such as [6] and its previous work.
3. Some description lacks clarity:
   - some abbreviations come without their full name, such as SWA.
   - Typos: $\theta$ and $\mathcal{T}_\theta$​ in lines 120
   - L152: $\langle, \rangle$​ is the Euclidean one in the ambient space.
   - The readability of some proofs are poor. use \stackrel for each (key) derivation is a good habit (such as L974-992).

### Questions
1. L 982-985: how to transform the Riemannian metric into the ambient inner product?
2. could we do  (Jacobian) regularization by trivialization? if so what is the advantage of Riemannian regularization?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, a theoretical analysis that characterizes the relationship between the general loss and the perturbation of the empirical loss in the context of Riemannian manifolds is presented. Motivated by the result obtained from this analysis, the authors introduce an algorithm named Riemannian Jacobian Regularization (RJR), which explicitly regularizes the Riemannian gradient norm and the projected Hessian. Some experiments have been conducted to verify the performance of the proposed method.

### Strengths
1.	A theoretical analysis that expresses the relationship between the general loss and the empirical loss via the Riemannian gradient and the projected Hessian is provided. 
2.	A Riemannian Jacobian Regularization (RJR) method is introduced to strengthen the Jacobian regularization techniques to Riemannian manifolds.

### Weaknesses
1.	The contributions of the work is not enough with only a theoretic analysis and a proposed method. I suggest the authors give more description about the proposed method, such as the role of each component played in the method. Specifically, the paper lacks a detailed explanation of how the Riemannian gradient norm and the projected Hessian interact within the RJR algorithm. It's unclear how each term contributes to the overall optimization process and how their relative importance is balanced. A more thorough discussion of the algorithm's mechanics is needed to understand its practical implications.
2.	On page three, line 113, the definition of the Euclidean norm of a vector is not standardized. It would be beneficial to explicitly state that the Euclidean norm is being used and to use the standard notation, such as ||.||_2, to avoid ambiguity.
3.	Why are some formulas not numbered, while others are? The lack of consistent numbering makes it difficult to refer to specific equations in the text, hindering the clarity of the theoretical development. All equations that are part of the main argument should be numbered for easy reference.
4.	Only four compared methods are used, just from two references in 2013 and 2023. How to effectively validate the SOTA performance of this method? The following methods can be compared “Riemannian Manifold Learning, TPAMI, 2008”, “Generalized Learning Riemannian Space Quantization: A Case Study on Riemannian Manifold of SPD Matrices, TNNLS, 2021”, “Kernel Methods on Riemannian Manifolds with Gaussian RBF Kernels, TPAMI, 2015”. The experimental section needs to be significantly expanded to include a wider range of state-of-the-art methods on Riemannian manifolds to properly assess the performance of the proposed RJR method. The current comparisons are insufficient to demonstrate its effectiveness.
5.	What is the Lemma 2 in the Appendix (A.2)? No related contents are described in the main contents of the paper. The given Lemma 2 in A. 2 is just already existed in Ref. Lee et al. (2023), as the authors described. The purpose and relevance of Lemma 2 in the appendix are unclear, especially since it is not referenced in the main text. If it is a known result, its inclusion should be justified, or it should be removed if it does not contribute to the paper's core argument.
6.	How to obtain the first inequality on page 19, line 974? Similar as in the third inequality? The derivation of the first inequality on page 19, line 974, is not clear. The paper should provide a step-by-step derivation, similar to the third inequality, to ensure the reader can follow the logic.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
