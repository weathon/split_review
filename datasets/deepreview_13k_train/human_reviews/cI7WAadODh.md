# An Invex Relaxation Approach for Minimizing Polarization from Fully and Partially Observed Initial Opinions

- Decision: Reject
- Scores: 1, 8, 3

## Abstract
This paper investigates the problem of minimizing polarization within a network, operating under the foundational assumption that the evolution of underlying opinions adheres to the most prevalent model, the Friedkin-Johnson (FJ) model.  We show that this optimization problem under integrality constraints is $\mathcal{NP}$-Hard. Furthermore, we establish that the objective function fits into a specialized category of nonconvex functions called invex, where every local minimum is a global minimum. We extend this characterization to encompass a comprehensive class of matrix functions, including those pertinent to polarization and multiperiod polarization, even when addressing scenarios involving stubborn actors. We propose a novel nonconvex framework for this class of matrix functions with theoretical guarantees and demonstrate its practical efficacy for minimizing polarization without getting stuck at local minima. Through empirical assessments conducted in real-world network scenarios, our proposed approach consistently outperforms existing state-of-the-art methodologies. Moreover, we extend our work to encompass a novel problem setting that has not been previously studied, wherein the observer possesses access solely to a subset of initial opinions. Within this agnostic framework, we introduce a nonconvex relaxation methodology, which provides similar theoretical guarantees as outlined earlier and effectively mitigates polarization.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of minimizing polarization in Friedkin-Johnson (FJ) model, where polarization simply measures how close the given network is to consensus. In particular, given an adjacency matrix on an undirected graph, the problem at hand is to find a new adjacency matrix which only differs from the original by a given budget and minimizes the polarization. It is expected that this problem is difficult in nature (due to the sparse/zero norm constraints), which is what is stated. The authors then provide a nonconvex relaxation and show that this relaxation falls into the category of an invex function minimization, and naturally use this to provide a trackable formulation.

### Strengths
The paper is not suitable for this venue.

### Weaknesses
Regardless of the merits of the contributions, the paper is not suitable for ICLR.

The problem is also not well motivated, and does not appear to be addressing a fundamental issue or question; the problem seems to be defined in a way that its relaxation fits to an invex function minimization problem. The related literature is not well surveyed; there is a wide range of optimization problems on graph Laplacian learning that could be relevant here, and the literature on Friedkin-Johnson (FJ) model is far from complete. The specific choice of the objective function, involving the inverse of the Laplacian squared, is not sufficiently justified. It's unclear why this particular form is crucial for minimizing polarization, and how it relates to other common measures of network consensus or agreement. The paper lacks a clear explanation of why this specific functional form is necessary, and how it compares to alternative formulations that might achieve similar goals with different mathematical properties. Furthermore, the practical implications of minimizing this specific objective are not thoroughly discussed, raising concerns about the real-world relevance of the proposed approach.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new approach for two problems related reducing polarization in a network. In the one variant, opinions are assumed to be observed for all participants in the network, while in another variant, only a subset of opinions are observed. There are assumed to be weights between pairs of users that can be modified by the social network platform, and opinions are assumed to evolve via the Friedkin-Johnsen model. The goal is to minimize the polarization of the network by making changes to the weights of the network, subject to a budget constraint. The authors show that polarization is an invex function, and develop an invex relaxation approach to solve this problem. Computational results are presented on both synthetic and real data.

### Strengths
The method provided by the authors is original, and addresses an interesting problem. The computational experiments are reasonable, and demonstrate that the method provides value.The paper is mostly clearly written, other than a couple of points that I mention in the weaknesses.

### Weaknesses
It was unclear to me exactly which optimization problem the authors are trying to solve. Is it problem (3) or is it problem (5)? The problem (5) is presented as a relaxation of problem (3), so I am assuming that this work is ultimately intended to solve problem (3). However, as far as I can tell, the procedure proposed by the authors does not guarantee that the resulting solution is feasible for problem (3). The authors should clarify this.

Some of the content presented in the paper seems superfluous, including the material related to polarization under stubbornness and multi-period polarization.

The assumptions that the authors make about the distribution of the unknown opinions seems to be quite strong. The authors could make their work stronger by providing stronger justification for this assumption or by examining how this assumption affects their results. For example, the authors could provide computational experiments where these assumptions are violated.

The authors do not report required computational time of their method.

The computational experiments in the case where some opinions are unknown could be stronger. The only comparison method that the authors provide is one that ignores all known opinions. It would be good to also apply some of the other existing methods, such as the coordinate descent approach where the unknown opinions are mean imputated.

### Questions
What, exactly is the optimization problem that you are trying to solve?
If you are trying to solve problem (3), how do you ensure feasibility?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed an invex relaxation approach for minimizing polarization over a network. It is proved in Section 4 that many types of polarization all fall into the invex function class, whose local minimum is a global minimum. Then this paper proposes to use projected gradient descent to solve a relaxed problem.

### Strengths
1. The paper is well written.
2. Invexity is provably identified for many types of polarization. It shows that polarization minimization regardless of constraints is similar to convex optimization.

### Weaknesses
My main concern is on the contribution of the relaxation and the framework to solve it.
 1. The relaxation seems to be straightforward. It is standard in optimization to relax $\ell_0$-norm into $\ell_1$-norm. And I think it cannot be viewed as a contribution of this work. Other modifications, including replacing the adjacency matrix with Laplacian (then the variable in the loss function and in the constraint become the same), as well as relaxing the constraint from $\le 2k$ to $\le 4k$, are also very slight, from my point of view. The relaxation from $\ell_0$ to $\ell_1$ norm, while common, often comes with a trade-off in solution quality. The paper does not adequately discuss the implications of this relaxation on the final solution, specifically how the $\ell_1$ norm solution relates to the original $\ell_0$ problem. It is unclear if the relaxed solution provides a good approximation, and if so, under what conditions. Furthermore, the modifications to the adjacency matrix and constraint, while seemingly minor, should be justified with more than just convenience. There needs to be a discussion of how these changes affect the problem's landscape and the solution's interpretability. For example, does using the Laplacian introduce any bias or change the nature of the polarization being minimized?
2. What is the contribution of the proposed framework to solve this problem? It seems to be the use of projected gradient descent. But I think the projected gradient descent is also very standard in optimization. So what is the novelty of this method? The paper does not provide sufficient justification for using projected gradient descent beyond its standard application. The analysis should delve into why this method is particularly well-suited for the specific problem structure. Are there any convergence guarantees specific to the invexity of the problem? Or are there any specific properties of the problem that make projected gradient descent more efficient than other first-order methods? The paper should also discuss the computational complexity of the proposed method, especially in the context of large-scale networks. Without a deeper analysis of the method's performance, it is difficult to assess its practical value.
3. It is my first time to see polarization minimization. So my confidence is only 2.

### Questions
See the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
