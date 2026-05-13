# A-Loc: Efficient Alternating Iterative Methods for Locating the $k$ Largest/Smallest Elements in a Factorized Tensor

- Decision: Reject
- Scores: 3, 1, 5, 1

## Abstract
Tensors, especially higher-order tensors, are typically represented in low-rank formats to preserve the main information of the high-dimensional data while saving memory space.  Locating the largest/smallest elements in a tensor with the low-rank format is a fundamental task in a large variety of applications. However, existing algorithms often suffer from low computational efficiency or poor accuracy. In this work, we propose a general continuous optimization model for this task, on top of which an alternating iterative method combined with the maximum block increasing (MBI) approach is presented. Then we develop a novel block-search strategy to further improve the accuracy. The theoretical analysis of the convergence behavior of the alternating iterative algorithm is also provided. Numerical experiments with tensors from synthetic and real-world applications demonstrate that our proposed algorithms achieve significant improvements in both accuracy and efficiency over the existing works.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors develop algorithms aimed at identifying the largest and smallest elements in a factorized tensor. They propose an alternating iterative algorithm, which is enhanced with a maximum block increasing approach and a novel block-search strategy. The validation of their method is provided through both theoretical analysis and experimental evaluations.

### Strengths
This paper presents a novel approach to a problem arising from tensor analysis - locating the largest/smallest elements in a tensor in the low-rank format. The strengths of the paper can be highlighted as follows:

1. The authors propose a continuous optimization model that is different from the existing methods. This model could be applied to various low-rank representations such as CP, Tucker, and TT formats.

2. The proposed method demonstrates significant improvements in both accuracy and efficiency over existing works in numerical experiments. This suggests that the method may be practically useful in real-world applications.

### Weaknesses
While the paper presents a novel approach to locating the largest/smallest elements in a tensor in a low-rank format, some weaknesses mainly related to the theoretical results can be identified:

1. Theorem 1 formulates an equivalent optimization problem for finding the largest element in a tensor, which is a crucial step in the authors' method. However, the paper does not provide an in-depth analysis of this equivalent problem. For example, it would be beneficial to understand the number of minimizers that this problem may have. Such analysis could provide insights into the complexity and potential pitfalls of the optimization problem, and could be critical for the algorithm's performance. Specifically, the paper lacks a discussion on the properties of the objective function, such as its convexity or concavity, which would be crucial for understanding the landscape of the optimization problem. Without this, it's difficult to assess the likelihood of the algorithm converging to a global minimum versus being trapped in a local minimum.

2. Theorem 2 shows that the proposed algorithm's subsequence converges to a stationary point of the optimization problem. However, it's unclear whether the entire sequence converges, and more importantly, whether it converges to the optimal solution. The absence of these guarantees may limit the algorithm's reliability and effectiveness in practice. The proof only demonstrates convergence of a subsequence, which does not guarantee that the entire sequence of iterates will converge. Furthermore, the paper does not address the possibility of limit cycles or other non-convergent behaviors that could arise from the alternating iterative nature of the algorithm. This is a critical gap in the theoretical analysis.

3. While Theorem 3 establishes a linear convergence rate to the optimal solution, it does so under the assumption that the initial point is sufficiently close to the optimal solution. Regrettably, the paper falls short in providing a discussion on how to obtain such an initial point. Furthermore, the paper does not explore the potential existence of multiple optimal solutions, a factor that could significantly affect the algorithm's convergence behavior. The assumption of a sufficiently close initial point is a strong one, and the paper provides no practical guidance on how to satisfy this condition. Moreover, the analysis does not consider the case where the optimization problem might have multiple local or global optima, which could lead to the algorithm converging to a suboptimal solution depending on the initialization.

### Questions
Please answer the questions in Weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach for computing the largest elements of a factorized tensor by means of alternating optimization.

### Strengths
+ The results regarding convergence of the method would make the approach valuable for a reasonably formulated problem.

### Weaknesses
 - The paper seems to obfuscate at least two major technical oversights:
    - The symmetric tensor eigenvalue formulation of the problem is used, by different factor matrices are optimized by alternating optimization. In the symmetric tensor eigenvalue problem, each component of the rank-1 factorization is typically set to be the same. Symmetry is mentioned in the problem definition in Section II, but never thereafter.
    - The proof of theorem 1 does not appear complete or correct to me. Convergence is considered based only the objective function, which is convergent for any method that has a nondecreasing and bounded objective. Hence, the contrast to convergence of standard alternating least squares does not make sense. See, Uschmajew, A. (2012). Local convergence of the alternating least squares algorithm for canonical tensor approximation. SIAM Journal on Matrix Analysis and Applications, 33(2), 639-652.

### Questions
None

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a algorithm for locating the largest and smallest elements in a tensor with low-rank format. The algorithm combines an alternating iterative method and a maximum block increasing approach, along with a newly-designed block-search strategy. The proposed algorithm achieves improvements in accuracy and efficiency compared to existing methods, as demonstrated through numerical experiments. It also discusses the use of the algorithm in various low-rank representations and highlights its advantage of obtaining both the largest/smallest elements and their location simultaneously.

### Strengths
*1. Quality:*  The paper presents an algorithm that significantly improves upon existing methods by achieving remarkable advances in both accuracy and efficiency. The comparisons with existing methods underscore the superior performance of the proposed approach in terms of both accuracy and computational efficiency. Moreover, the paper discusses the algorithm's applicability to various low-rank representations, including CP, Tucker, and TT formats.

*2. Clarity:*  The authors employ precise mathematical notations consistently, facilitating the understanding of the proposed algorithm, theoretical analysis, and numerical experiments.

### Weaknesses
 - The paper takes known algorithms, and only connects them together in the special case of the problem of finding the extremum of CP-tensors.
 
- Comparisons in numerical examples are given with only two (and in the case of finding the minimum, only one) other method, which is clearly insufficient.
   * The coloring in the tables when both the presented method and its competitor are the best is given only for the presented method. It would be fair to color all cases when a particular method was the best. For example, in Table 2, color all cases of minimum for both functions, since they are equal for the presented method and for MInCPD. 

- Table 1, which compares methods for random vectors, is not entirely honest. Indeed, the _star sampling_ method can only find maximum (modulo) elements of CP-tensor. But once one is found, let its values be $m$, we can do a transformation $m \mathcal E - \mathcal A$ (very similar to the one described on page 2 in section 2 of the paper), which increases the CP-rank by only 1. Then the problem of finding the minimum in the initial tensor $\mathcal A$ reduces to finding the maximum in this tensor. Unfortunately, I haven't found open source code for the _star sampling_ method, but I suspect it would work (with this trick) just as well as the presented method. And in the problem of maximum finding the _star sampling_ algorithm, as the authors honestly write, already wins, so the the contribution made by this new approach may be considered negligible in this case.

- As for finding optima of the Rastrigin and Schwefel model functions, this and many other functions were used to test a similar algorithm optima_tt, which is cited in this paper as Chertkov et al. (2022). If we take the _optima_tt_ code, which is open source, and apply it to TT-tensors that exactly describe the two functions (with exact TT-ranks of 2 each) with the same parameters (n=4096, d=10), we get the following results for the minimum and for the maximum (I took the hyperparameter $k=5$):
Rastrigin: min: 0.0014192582... max: 403.5327475...
Schwefel min: 0.000725485....  max: 8379.65727....
Thus, for these two functions the combination of using CP-compression and the newly presented method is meaningless.

- No code is provided so that experiments can be repeated

- The Theorems in the paper are rather trivial, one of them is not proved at all (see below). Thus, there is no serious analysis of convergence. To be fair, it should be noted that there is no such analysis for many other similar methods.

- in the proof of Theorem 1, in the last equation in (A.1) it is not clear what "$x^{(n)}=1$" means. If it is a constant vector, how can we search for $\max$ w.r.t. it?
If it $\|x^{(n)}\|_2=1$ then (A.1) is not just equivalent (as the proof of the theorem states), but coincides with problem (2.3). 
But Theorem 1 asserts more than that. It asserts that for continuous values of $x^{(n)}$, i.e., $x^{(n)}\in\mathbb R^{I_n}$, the solution of the maximization problem (2.3) coincides with the maximum of CP-Tensor element, i.e., with the case where each vector $x^{(n)}$ are binary and represents (different) rows of the unit matrix. In this form, Theorem 1 has never been proved in the this paper.

- times in the Table 4 with experiments with "real-world" data are not relevant, because it will be much faster, for example, for COVID dataset expand it the full tensor, and then search the maximum. Moreover, the compression time of these real-world datasets into CP format is not taken into account.
    * link the mnist dataset is not valid -- login and password requires to access it.

- at the beginning (page 3) the paper says that the algorithm parameter-free. But then it turns out that the final Algorithm has an adjustable parameter $b$.

### Questions
*Question 1:* Can the authors provide a more detailed explanation of how your proposed algorithms significantly differ from existing methods in both conceptual and theoretical aspects? Are there specific aspects of your approach that are novel and distinct from prior work that you draw inspiration from?

*Question 2:* Could the authors elaborate on potential applications or extensions of your method beyond the specific task of low-rank tensors? How might it contribute to broader machine learning challenges? What are the limitations of your method in terms of scalability or adaptability to different problem domains?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper takes several well-known ideas, in particular maximization/minimization over a continuous $x$ in a discrete problem, and what the paper calls block-search strategy (a.k.a. top-k). These approaches are used to simultaneously find the minimum or maximum of a CP-tensor. Several theorems in the paper do not fully shed light on the accuracy of the method, the evaluation of which remains more empirical. Numerical experiments are set on random low-dimensional CP-tensors, CP-factorization of two well-known model fucntions, and CP-factorization of several small real-world datasets.

### Strengths
- The paper is generally well structured and written
- In some cases good results are obtained when searching for CP-tensors minimum

### Weaknesses
- The paper takes known algorithms, and only connects them together in the special case of the problem of finding the extremum of CP-tensors.
 
- Comparisons in numerical examples are given with only two (and in the case of finding the minimum, only one) other method, which is clearly insufficient.
   * The coloring in the tables when both the presented method and its competitor are the best is given only for the presented method. It would be fair to color all cases when a particular method was the best. For example, in Table 2, color all cases of minimum for both functions, since they are equal for the presented method and for MInCPD. 

- Table 1, which compares methods for random vectors, is not entirely honest. Indeed, the _star sampling_ method can only find maximum (modulo) elements of CP-tensor. But once one is found, let its values be $m$, we can do a transformation $m \mathcal E - \mathcal A$ (very similar to the one described on page 2 in section 2 of the paper), which increases the CP-rank by only 1. Then the problem of finding the minimum in the initial tensor $\mathcal A$ reduces to finding the maximum in this tensor. Unfortunately, I haven't found open source code for the _star sampling_ method, but I suspect it would work (with this trick) just as well as the presented method. And in the problem of maximum finding the _star sampling_ algorithm, as the authors honestly write, already wins, so the the contribution made by this new approach may be considered negligible in this case.

- As for finding optima of the Rastrigin and Schwefel model functions, this and many other functions were used to test a similar algorithm optima_tt, which is cited in this paper as Chertkov et al. (2022). If we take the _optima_tt_ code, which is open source, and apply it to TT-tensors that exactly describe the two functions (with exact TT-ranks of 2 each) with the same parameters (n=4096, d=10), we get the following results for the minimum and for the maximum (I took the hyperparameter $k=5$):
Rastrigin: min: 0.0014192582... max: 403.5327475...
Schwefel min: 0.000725485....  max: 8379.65727....
Thus, for these two functions the combination of using CP-compression and the newly presented method is meaningless.

- No code is provided so that experiments can be repeated

- The Theorems in the paper are rather trivial, one of them is not proved at all (see below). Thus, there is no serious analysis of convergence. To be fair, it should be noted that there is no such analysis for many other similar methods.

- in the proof of Theorem 1, in the last equation in (A.1) it is not clear what "$x^{(n)}=1$" means. If it is a constant vector, how can we search for $\max$ w.r.t. it?
If it $\||x^{(n)}\||_2=1$ then (A.1) is not just equivalent (as the proof of the theorem states), but coincides with problem (2.3). 
But Theorem 1 asserts more than that. It asserts that for continuous values of $x^{(n)}$, i.e., $x^{(n)}\in\mathbb R^{I_n}$, the solution of the maximization problem (2.3) coincides with the maximum of CP-Tensor element, i.e., with the case where each vector $x^{(n)}$ are binary and represents (different) rows of the unit matrix. In this form, Theorem 1 has never been proved in the this paper.

- times in the Table 4 with experiments with "real-world" data are not relevant, because it will be much faster, for example, for COVID dataset expand it the full tensor, and then search the maximum. Moreover, the compression time of these real-world datasets into CP format is not taken into account.
    * link the mnist dataset is not valid -- login and password requires to access it.

- at the beginning (page 3) the paper says that the algorithm parameter-free. But then it turns out that the final Algorithm has an adjustable parameter $b$.

Minor:

Suggestion:  put brackets around formula references (use "\eqref" instead of "\ref").

### Questions
- Have you tried experiments on model functions other than Rastrigin and Schwefel?
- Have you tried scaling the method to significantly higher dimensions ($N=100,1000$), which overcome the curse of dimensionality?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
