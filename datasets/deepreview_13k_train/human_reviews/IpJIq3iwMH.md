# Federated Binary Matrix Factorization using Proximal Optimization

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Identifying informative components in binary data is an essential task in many research areas, including life sciences, social sciences, and recommendation systems.
    Boolean matrix factorization (BMF) is a family of methods that performs this task by efficiently factorizing the data.
    In real-world settings, the data is often distributed across stakeholders and required to stay private, prohibiting the straightforward application of BMF.
    To adapt BMF to this context, we approach the problem from a federated-learning perspective, while building on a state-of-the-art continuous binary matrix factorization relaxation to BMF that enables efficient gradient-based optimization.
    We propose to only share the relaxed component matrices, which are aggregated centrally using a proximal operator that regularizes for binary outcomes.
    We show the convergence of our federated proximal gradient descent algorithm and provide differential privacy guarantees.
    Our extensive empirical evaluation demonstrates that our algorithm outperforms, in terms of quality and efficacy, federation schemes of state-of-the-art BMF methods on a diverse set of real-world and synthetic data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a novel method called Felb, which is a federated binary factorization algorithm based on proximal gradients along with the adaptive alternative Falb.

### Strengths
- the authors bring a novel algorithm designed for binary matrix factorization. The previous federated factorization algorithms were not for the binary/boolean matrices.
- the paper is well-written, easy to follow.

### Weaknesses
 - The contribution is limited to the binary matrices, unless a further performance analysis on the non-binary matrices are provided. (the most of the datasets selected are by default not boolean matrices but converted to boolean)

 - The potential disadvantages of having a proximal operator is not being discussed. 

 - The methods compared could be discussed further, for instance in Figure 6. the loss values for most of the models seem to be stuck at 1. What is the reason for that? What are the parameters used for these methods? How are they implemented? It might be possible that this is a bug. Similarly the recall values are zero. This is skeptical.

### Questions
- We demonstrate that our approach converges for a strictly monotonically increasing regularization rate.

Could authors elaborate more on this? How is this useful? What is the rate? Is there an ablation study on different rates? 

- Most of the recent research shows that preserving privacy inevitably brings a reduction in accuracy. The authors claim that the accuracy of the method is even higher than the methods that do not have a privacy component. What is the trade-off? computational complexity? scalability? time complexity? difficulty in implementation?

- What are the advantages that the proximal gradients bring to the problem? 

- Did the authors do any comparison with the new federated matrix factorization (Du et al., 2021) and federated non-negative matrix factorization (Li et al., 2021).

- Figure 6, is there a logical order of the datasets?

- Where is the differential privacy stated in the formulation?

- Is the lambda different for u and v? (Algorithm 1, line 4 and 5)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for federated binary matrix factorization.
It also considers differentially private variants of the proposed method, by adding noise to the local updates (offering local DP guarantees).

### Strengths
Presentation and clarity: The paper is overall well-motivated, the ideas are simple and easy to follow, and adequate background is given about binary matrix factorization, federated learning and differential privacy.
The method seems like a reasonable extension of existing methods to the federated setting.

### Weaknesses
The contribution of the paper seems limited. This is a straightforward extension of the method of Dalleiger et al. to the federated setting. Each client applies the same method, then the $V_i$ updates are aggregated on the server. The main algorithmic novelty seems to be to how aggregation is done, and the idea was to apply the proximal operator (the *same one used by Dalleiger et al.*) to the mean of the updates.

The theoretical result (convergence of the iterates in Proposition 4.1) has several issues.
First, the proof is wrong. It is argued that the gradients tend to 0, thus the iterates converge. This is not true (think of the sequence $x_k = 1/k$).
Even if the proof were to be corrected, the result is still very weak. It only claims that the process converges (to a binary solution) without saying anything about the limit's utility (for example whether this limit is close to the solution). Such a result can be obtained by a trivial algorithm (for example one that uses a step size of 0 after a finite number of steps).

The paper also seems completely unaware of the extensive literature on private matrix completion (it is claimed in the related work that "algorithms for matrix factorization seek computational efficiency while disregarding privacy aspects"). The problem has been studied (without the binary constraints) in a number of papers both in the central and federated settings [1-4]. Even though the exact setting is different (due to the binary constraints) the methods are closely related, and several ideas used in this paper were already proposed in prior work. For example, this paper proposes "partial sharing" (sharing the V factor but keeping the U_i factors local to each client), but this exact scheme was used in [1-5] (in the privacy literature this is referred to as joint-DP or sometimes as the billboard model of DP).

Other comments:
- What is the motivation to add binary constraints in recommender systems? This does not seem to be a common practice. (Related to this point: some of the recommendation data sets used in experiments were used in prior work on private matrix completion, without binary constraints. It would be good to compare.)
- In section 4, it is claimed that "Without the knowledge of $U_i$, the server cannot estimate specific attributes of individual users". This is not true. For example access to gradients can leak information about the client's data. This has been shown via reconstruction attacks (for example in [6] which looked specifically at matrix completion).
- Privacy-related experiments: it seems that in all cases, for epsilon up to roughly 10, the loss exceeds 1 (which if I understand the loss definition correctly, means the learned solution is worse than even a trivial solution of all 0). This seems surprising, it basically means that learning is impossible except for very large epsilon. This might indicate that the method has not been properly tuned. Perhaps the authors should carefully revisit these experiments.
- It is mentioned in the appendix that sensitivity was estimated by the maximum number of 1s in the input data. But note that this is a private quantity, and it should be estimated privately (not computed exactly), or you can perhaps set a maximum number then subsample each client to this number.
- [a comment that does not affect my evaluation] the authors included their code in the supplementary material, and this is commendable. However, including code without comments or instructions on running experiments makes it virtually impossible to reproduce the results. Ideally, one should include at least a readme file with instructions on how to run the methods (and how to get the data).

### Questions
- I invite the authors to reflect/comment on connections to prior work mentioned above.
- Do the authors think they can strength the theoretical analysis?

### Soundness
2 fair

### Presentation
3 good

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
This paper studies the Boolean matrix factorization problem, where you are given a Boolean matrix $A$, and you need to find two low-rank matrices $U$ and $V$ such that $A\approx U\circ V$, where the operations are over the Boolean semiring. This problem has many practical applications. However, it is NP-hard to solve it exactly. This paper considers a heuristic approach based on the proximal gradient descent. The main contribution of this paper is to propose a federated proximal-gradient-descent algorithm for BMF (FELB) and its adaptive version (FALB). In theory, it proves the convergence of these algorithms and shows some differential privacy guarantees. In experiments, it tests the new algorithms in several different datasets and demonstrates advantages in accuracy and efficiency over prior approaches.

### Strengths
The algorithm is the first of its kind in the field of federated BMF. It establishes a new benchmark for future studies in this area. Additionally, the algorithm works well empirically, which could be useful in many real-world applications. The experimental results are comprehensive and clearly stated in this paper.

### Weaknesses
The technical novelty of this paper is limited. The idea of using proximal gradient descent has been previously used by Dalleiger and Vreeken (2022). This paper merely transforms the previous algorithm into a federated version. The non-trivial part is the aggregation procedure. However, it is a heuristic and also increases the time complexity for the server. The paper does not theoretically show the convergence rate of the algorithm. Furthermore, the analysis relies on a strong assumption of the loss function. The writing of this paper could be improved. For example, more intuition for the proximal operator should be provided. The current manuscript is not self-contained, and it could be difficult for people outside of this field to understand.

* Eq. (2): why $A_{ij}$ or $[U\circ V]_{ij}$? It seems to be xor. 

* After Eq. (3): the definition of $R$ is confusing. It maps $\mathbb{R}^{n’\times m’}$ to $\mathbb{R}$. However, Eq. (3) applies it to $U$ and $V$, which are matrices with different dimensions.

* Eq. (4): it is unclear what it means for $x\in X$. Is $X$ a set of points, and $x$ is a vector? Or is $x$ a number? And what is $x-1$?

* Page 4: “Without the knowledge of $U_i$, the server cannot estimate specific attributes of individual users (assuming sufficiently large client datasets).” Can the sever learn $U$ from $A$ and $\hat{V}$? Is it proved in this paper to rule out such an attack? If so, a reference should be added here.

* Proposition 1: the symbol R should be replaced by some other symbol, as it has been used to denote the regularizer.

* Page 5, line 4: is it a typo for $\nabla_U\nabla_U$?

* Proposition 1: even if the gradient tends to zero, the loss function may not tend to zero without further assumption on the loss function. Is the loss function considered here convex? And how do we justify the assumption on the bounded gradient?

* Section 4.2: the differential privacy claims should have a formal statement with proof.

* Page 7: the index of the summation should be stated explicitly.

* (Chen et al. 2022) considers the symmetric and sparse version of BMF and shows a combinatorial algorithm for the average-case instances. It is interesting to see whether the method in this paper can be generalized to this regime.

### Questions
* Eq. (2): why $A_{ij}$ or $[U\circ V]_{ij}$? It seems to be xor. 

* After Eq. (3): the definition of $R$ is confusing. It maps $\mathbb{R}^{n’\times m’}$ to $\mathbb{R}$. However, Eq. (3) applies it to $U$ and $V$, which are matrices with different dimensions.

* Eq. (4): it is unclear what it means for $x\in X$. Is $X$ a set of points, and $x$ is a vector? Or is $x$ a number? And what is $x-1$?

* Page 4: “Without the knowledge of $U_i$, the server cannot estimate specific attributes of individual users (assuming sufficiently large client datasets).” Can the sever learn $U$ from $A$ and $\hat{V}$? Is it proved in this paper to rule out such an attack? If so, a reference should be added here.

* Proposition 1: the symbol R should be replaced by some other symbol, as it has been used to denote the regularizer.

* Page 5, line 4: is it a typo for $\nabla_U\nabla_U$?

* Proposition 1: even if the gradient tends to zero, the loss function may not tend to zero without further assumption on the loss function. Is the loss function considered here convex? And how do we justify the assumption on the bounded gradient?

* Section 4.2: the differential privacy claims should have a formal statement with proof.

* Page 7: the index of the summation should be stated explicitly.

* (Chen et al. 2022) considers the symmetric and sparse version of BMF and shows a combinatorial algorithm for the average-case instances. It is interesting to see whether the method in this paper can be generalized to this regime.

Chen, Sitan, et al. "Symmetric Sparse Boolean Matrix Factorization and Applications." 13th Innovations in Theoretical Computer Science Conference (ITCS 2022).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
