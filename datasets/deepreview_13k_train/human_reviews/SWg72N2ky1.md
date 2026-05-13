# Maximum Noise Level as Third Optimality Criterion in Black-box Optimization Problem

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
This paper is devoted to the study (common in many applications) of the black-box optimization problem, where the black-box represents a gradient-free oracle $\tilde{f}_p = f(x) + \xi_p$ providing the objective function value with some stochastic noise. Assuming that the objective function is $\mu$-strongly convex, and also not just $L$-smooth, but has a higher order of smoothness ($\beta \geq 2$) we provide a novel optimization method: _Zero-Order Accelerated Batched Stochastic Gradient Descent_, whose theoretical analysis closes the question regarding the iteration complexity, _achieving optimal estimates_. Moreover, we provide a thorough analysis of the maximum noise level, and show under which condition the maximum noise level will take into account information about batch size $B$ as well as information about the smoothness order of the function $\beta$. Finally, we show the importance of considering the maximum noise level $\Delta$ as a third optimality criterion along with the standard two on the example of a numerical experiment of interest to the machine learning community, where we compare with SOTA gradient-free algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper analyzes the zeroth order method with a biased oracle for strongly convex functions with higher-order smoothness. The author introduces ZO Accelerated batched SGD and demonstrates that it achieves the optimal iteration complexity. The paper highlights that its results provide estimates of  the maximum noise level required for the algorithm to converge.

### Strengths
The paper extends the analysis of the first-order Accelerated SGD to a setting with a biased gradient oracle and the use of mini-batches. Further, It combines this result with the estimated gradients from zeroth-order orcale.

### Weaknesses
1. The paper’s writing is problematic. Symbols are introduced before their definitions, such as $e$ and $r$ in Definition 1.3. The first-order Accelerated SGD algorithm is presented without a definition. Furthermore, Figure 1 seems unnecessary for a theoretical work in this field.

2. Technically, the contribution is limited. The convergence of Accelerated SGD has been proven, and extending it to the biased and mini-batch settings appears straightforward. Additionally, the estimations of bias and second moment of the zeroth-order oracle are well-established in the literature.

3. The motivation behind considering the maximum noise level is unclear. Previous work assumed a constant $\Delta$ and showed convergence to minima. This work considers $\Delta$ diminishing with the target accuracy, and does not converge to minima with constant $\Delta$. I fail to see the advantage of considering this case. Furthermore, Table 1 does not provide a fair comparison since $\Delta$ depends on $\epsilon$ in this work. Moreover, Table 1 reports iteration complexity, while the proposed algorithm utilizes mini-batches, which also leads to an unfair comparison. The oracle complexity should be the more relevant measure in this context.

### Questions
1. Could the author clarify the technical challenges in this work and address the third point in Weakness?

2. Regarding the Zeroth order oracle, how can we guarantee that $\xi_1 \neq \xi_2$? If we know their values, we can already get the true function value.

3. In Figure 2 b), why does the red curve converge to minimizers even in the case of bias?

4. In the numerical experiment section, what noise is used? Why is the final accuracy of ZO-VARAG large, given that the noise level is already set to be small?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper generalizes the analysis of an accelerated SGD algorithm in Vaswani et al. (2019) to allow for biased gradient oracle ands mini-batch data. Base on this contribution, this paper develops a zeroth-order method based on Kernel approximation and prove new convergence results. Experiments show that this new method is effective.

### Strengths
1. This paper generalizes an existing accelerated SGD method in Vaswani et al. (2019) to the case with bised gradient noise.

### Weaknesses
1. Biased noise has been studied in existing works such as Akhavan, Chzhen, Pontil, Tsybakov (2023), see their assumption B. Thus, this is not new at least for zeroth order method. 
2. The convergence rate is achieved by taking $\Delta$ linear in target accuracy $\epsilon$, which makes it hard to compare with other listed works which treat $\Delta$ as some $\epsilon$-independent problem-dependent constant. 
3. The writing of this paper is not smooth, some terms come up without definition.

### Questions
1. When mentioning Kernel approximation in the introduction, can you briefly discuss the advantage of using this approximation? 
2. In definition 1.3, $e$ and $r$ are undefined. Do you mean there are two queries at the same point $x_k$?
3. The lemma 2.4 and lemma 2.5 presented results for an algorithm not described? And what is $\eta, \tilde{R}$, why the third with $\tilde{R}$ does not affect much? Can you revise and text and make these clear?
4. Can the authors briefly discuss what new tricks used in this paper to allow biased noise oracles?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is devoted to the study of the black-box optimization problem and the objective function value contains stochastic noise. For the case where the objective function is strongly convex and exhibits higher-order smoothness, the authors propose a novel zeroth-order accelerated batch stochastic gradient descent algorithm (ZO-ABSGD). The authors generalize existing convergence results for accelerated stochastic gradient descent to the case where the gradient oracle is biased. In addition, the authors provide improved iteration complexity through theoretical analysis and conduct a detailed examination of the maximum noise level. Finally, the authors demonstrate the performance of the proposed algorithm through experiments.

### Strengths
1.Compared to previous studies, the proposed algorithm improves iteration complexity and provides a thorough analysis of the maximum noise level.

2.The authors provide solid proof details to support their proposed theory.

### Weaknesses
1.I have some unclear aspects regarding certain writing details in this paper.

2.The experiments are insufficient; it is recommended that the authors provide additional experiments.

### Questions
1.The experiments demonstrate that the proposed ZO-ABSGD outperforms the ZO-VARAG algorithm on the a9a dataset, while exhibiting comparable performance to the ARDFDS algorithm. It is hoped that the authors can explain the unique practical advantages of the ZO-ABSGD algorithm in comparison to the ARDFDS algorithm.

2.I understand that the authors' main contribution lies in the theoretical aspects; however, the authors should attempt to conduct experiments on more datasets to demonstrate the efficiency of the ZO-ABSGD algorithm.

3.In section 4, the authors propose ''we show the importance of considering the maximum noise level ∆ as a third optimality criterion along with the standard two.'' It is hoped that the authors can provide a more detailed description of what "third optimality criterion" and "the standard two" specifically refer to, as well as how they are represented in the experiments.

### Soundness
2

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
2

### Summary
This paper presents a comprehensive technique for creating a gradient-free algorithm that leverages increased function smoothness through kernel approximation, which generalizes convergence results for accelerated stochastic gradient descent to cases where the gradient oracle is biased and illustrates how bias accumulates in the algorithm's convergence. 

This paper also resolves the question of iteration complexity by providing an improved estimate (as shown in Table 1) that is optimal. It determines the maximum noise level ∆ at which the algorithm can still achieve the desired accuracy ε (see Table 1 and Theorem 3.1). 

Furthermore, the paper emphasizes the importance of considering the maximum noise level ∆ as a third optimality criterion alongside the standard two.

### Strengths
The work seems to be solid.

The paper is organized clearly.

An interesting idea on Kernel approximation is presented. A novel algorithm is given for zero-order optimization. Numerical experiments are conducted to illustrate the advantages of the proposed algorithm.

### Weaknesses
The definition of Oracle complexity should be introduced in the introduction, explaining its difference from Iteration complexity.

I am still unsure about the necessity of the strong convexity assumption. While the authors focus on global convergence, it's unclear if the proposed algorithm's performance would degrade significantly on convex or even non-convex problems that satisfy weaker conditions, such as the Polyak-Lojasiewicz (PL) condition. The paper should discuss the potential limitations of the strong convexity assumption and how it might affect the applicability of the results in broader scenarios.

The bounded bias assumption, Assumption 2.3, while standard, could be more thoroughly justified. The paper should provide a more detailed discussion on the implications of this assumption and whether it is too restrictive for practical applications. Specifically, how does the constant bound on the bias affect the algorithm's performance when the bias might vary with the iteration or the gradient norm? The paper should explore the potential impact of different bias constraints on the convergence behavior of the algorithm. 

I am sorry I am not very familiar with this topic. I will change my score based on the comments of other more senior reviewers.

### Questions
Is the strong convexity assumption necessary? Is it possible that the proposed algorithm will perform equally well on convex or non-convex problems?

Is the bounded bias assumption, Assumption2.3, too strong?

### Soundness
3

### Presentation
3

### Contribution
3
