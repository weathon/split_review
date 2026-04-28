# Semi-Anchored Gradient Methods for Nonconvex-Nonconcave Minimax Problems

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Nonconvex-nonconcave minimax problems are difficult to optimize by gradient methods. The extragradient method, proven to outperform the gradient descent ascent, has become standard but there is still room for improvement. On the other hand, under a bilinear setting, the primal-dual hybrid gradient (PDHG) method is one of the most popular methods. This was studied on a general convex-concave problem, but it has not been found useful in a more general nonconvex-nonconcave minimax problem. In this paper, we demonstrate its natural extension to a structured nonconvex-nonconcave minimax problem, whose saddle-subdifferential operator satisfies the weak Minty variational inequality condition, showing its potential. This new nonlinear variant of PDHG, named semi-anchored (SA) gradient method,
is built upon the theory of Bregman proximal point method. This consequently provides a worst-case convergence rate, in terms of a new optimality measure for nonconvex-nonconcave minimax optimization, making it interesting on its own. We further illustrate the potential of the semi-anchoring by providing a numerical experiment on fair classification problem, in comparison with the extragradient.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work for the first time extends the primal-dual hybrid gradient (PDHG) method from convex-concave minimax optimization problem to nonconvex-nonconcave minimax optimization problem. The 4 versions of PDHG (with/without projection and with/without max oracle) obtain the same gradient convergence rate $\mathcal{O}(1/k)$ as the existing extragradient methods, and PDHG without projection and with max oracle upper bounds Bragman distance that is larger than the squared norm measure in the convergence rate of the existing extragradient methods, which yields faster empirical convergence of PDHG without projection and with max over extragradient methods as shown in the experiments.

### Strengths
Originality: This work for the first time extends the primal-dual hybrid gradient (PDHG) method from convex-concave minimax optimization problem to nonconvex-nonconcave minimax optimization problem. 

Quality: The theoretical and experimental results make sense. 

Clarity: Generally I can well understand this paper. 

Significance: PDHG without projection and with max oracle upper bounds Bragman distance that is larger than the squared norm measure in the convergence rate of the existing extragradient methods, which yields faster empirical convergence of PDHG without projection and with max over extragradient methods as shown in the experiments.

### Weaknesses
The major weakness is the weak advantage of the proposed method over existing works, especially EG+ and CEG+, as elaborated in my questions 1-3 below. While the theoretical results demonstrate a convergence rate of O(1/k), similar to existing extragradient methods, the practical implications and advantages need further clarification. The claim that PDHG without projection and with max oracle upper bounds a larger Bregman distance than the squared norm measure used in the convergence rate of existing extragradient methods is interesting, but its significance in practice is not fully convincing without a more direct comparison with EG+ and CEG+.

Some typos and unclear points are listed in the questions below.

### Questions
(1) In Table 1, is it possible to add some columns to reveal your advantage over EG+ and CEG+? The advantage over EG+ and CEG+ in bounding the larger Bregman distance seems to disappear for SA-GDAmax with projection (Theorem 4) and the inexact SA-MGDA methods (Theorems 5 and 6). Other advantages? Also, I think the practical inexact SA-MGDA methods should also be included in the experiments. 

(2) The drawbacks of extragradient and advantages of PDHG could be briefly mentioned in the abstract and the beginning of the Introduction, instead of ''there is still room for improvement''. Also, in the abstract, is the ''worst-case convergence rate'' lacking in extragradient methods? If yes, you could mention this in the abstract. 

(3) What's your advantage over the works ''Fast extra gradient methods for smooth structured nonconvex-nonconcave minimax problems'' and ''Stable Nonconvex-Nonconcave Training via Linear Interpolation''? You may cite the latter. 

(4) In ''This was studied on a general convex-concave problem, but it has not been found useful in a more general nonconvex-nonconcave minimax problem. In this paper, we demonstrate its natural extension to a structured nonconvex-nonconcave minimax problem'' in the abstract, ''it' and ''its'' are far away from PDHG and thus could be replaced by PDHG. 

(5) At the end of the second paragraph of the introduction, "a new nonlinear variant of the PDHG, named semi-anchored (SA) gradient method" could be clearer. 

(6) In page 4, in the sentence ''the GDmax minimizes the equivalent minimization problem'', ''minimizes'' could be changed to ''solves''. 

(7) How to compute $R(x)$? You could explain or cite in your paper. Can $R(x)$ be exactly solved? If not, it is recommended to include such an error in the convergence results. 

(8) In Section 4.3, you said ''This has several advantages over the standard BPP, which will be detailed later. '' Later I found only one advantage of a larger range of $\rho$. Any other advantages? 

(9) In Section 5.1,  can we replace $\widehat{L}$ with the previously defined $\gamma$? 

(10) Right after as ''it resembles GDmax'', you could indicate that we can also obtain SA-GDmax with projection using BPP with projection (4) using h in (5). 

(11) In Theorem 3, ''SA-GDmax (i.e., SA-MGDA with $J=\infty$)'' looks clearer. In Theorem 4, should it be ''SA-GDmax with projection''? 

(12) In the toy example, what's the function $\phi$? Should it be $+\frac{L^2\rho}{4}u^2$ and $-\frac{L^2\rho}{4}v^2$ to correspond to $+f(u)$ and $-g(v)$ in the problem (1)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed semi-anchored gradient methods to a structured nonconvex-nonconcave minimax problem under certain assumption, namely the weakly Minty variational inequality (MVI). The proposed algorithm is based on the Bregman proximal point (BPP) algorithm, also resembles the primal-dual hybrid gradient (PDHG) method. The proposed algorithm consists of u and v substeps where the authors proposed using FISTA to solve the v substep approximately. Theoretical convergence is studied for this SA-MDGD algorithm and numerical experiments were provided to show the efficacy of the proposed method.

### Strengths
The paper is well-rounded and well-motivated. The authors analyzed the theoretical convergence of the general BPP method for a broader class of problems and then proceed to the specific structured problem. The work also addresses the concern of the practicality of the v substep and proposed an inexact SA-MGDA method to carry out the proposed method in practice.

### Weaknesses
It remains unclear how the proposed algorithm performs comparing to the existing works, especially on the theoretical rate of convergence under similar assumptions.

(Please respond to the questions section directly) It remains unclear how the proposed algorithm performs comparing to the existing works, especially on the theoretical rate of convergence under similar assumptions.

### Questions
1. As mentioned in the Weakness section, a comprehensive comparison with GDmax and other algorithms, especially in theoretical convergence rate seems necessary. Is the sublinear rate as in Theorem 4, 5 or 6 show improvements over existing methods or achieve certain lower bounds? For example [1] seems to achieve similar sublinear rate. The authors could consider illustrating this in their Table 1.

2. In numerical experiments, I’m not sure if the authors implemented their SA-GDmax or the more practical SA-MGDA algorithm. If it’s SA-GDmax as in (7), then how did the authors conduct the v substep precisely? Also for Figure 2, the authors claimed the parameter $\tau=0.01$ in section 7.2 but presented two choices of $\tau$, and from the left figure in Figure 2, $\tau=0.01$ didn’t show a statistical advantage of SA-GDmax over other works. Last, the authors didn’t compare with a lot of the methods in Table 1, for which they should consider adding more numerical comparisons.

References:
[1] Diakonikolas, Jelena, Constantinos Daskalakis, and Michael I. Jordan. "Efficient methods for structured nonconvex-nonconcave min-max optimization." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper consider Bregman divergence based methods for weak Minty variational inequalities. They show convergence of the Bregman divergence between two consecutive iterates for the Bregman proximal point (BPP) method by expressing the scheme as a preconditioned resolvent. By applying the hyperplane projection step of Solodov & Svaiter 1999 they increase the range of $\rho$ (showing convergence in terms of the tangent residual). By modifying the preconditioner further they obtain a scheme which alternatingly computes a proximal gradient for the min-player and solves a proximal (implicit) update for the max-player. They immediately obtain convergence from the previous results. Finally they consider inexactness of the max-player for which they show convergence for the tangent residual.

### Strengths
The paper is easy to follow, provides an in depth overview of the relevant literature, and the statements appears correct.

### Weaknesses
My main concern is with the relevance of the results, particularly in the context of the broader landscape of methods for solving variational inequalities.

The only result that seems to exploit the Bregman divergence is regarding the (implicit) BPP without hyperplane projection (Thm. 1 and Thm. 3), and this follows almost immediately from the monotone case. The extension to weak Minty variational inequalities (weak MVI) is valuable, but the practical implications of relying solely on the implicit BPP method are unclear, especially when considering its computational cost.

All remaining results in the paper instead shows rates for the _tangent residual_ (as soon as either inexactness appears or the hyperplane projection is used). If we are interested in the tangent residual in the first place, then a  $\mathcal O(1/k)$ rate can be achieved by an _explicit_ scheme  _without_ (inexact) max-oracles by a primal-dual extragradient scheme. For instance, Algorithm 3 and the associated Theorem 8.2 of [1] demonstrate that, in the absence of stochasticity, a $\mathcal O(1/k)$ rate is achievable for the tangent residual. Furthermore, Algorithm 3 could be simplified by omitting the bias correction term in the deterministic setting.

This leads to several critical questions:

1. What is the purpose of considering hyperplane projection and inexactness if we cannot provide guarantees in terms of Bregman divergence? The shift to analyzing the tangent residual seems to dilute the initial focus on Bregman-based methods.

2. Why not consider the setting without Bregman, and study a nonlinear variant of PDHG (which seemed to be the original motivation in the abstract and which variants for the convex-concave case is mentioned on page 4)? This would essential be an optimistic variant of the PDEG scheme mentioned above. The current approach seems to be a less efficient alternative, especially when considering the availability of methods like the one presented in [1] that achieve a $\mathcal O(1/k)$ rate for the tangent residual without requiring a max-oracle.

3. I'm surprised that a bounded domain is needed in Thm. 5. Is it not possible to use that inexact proximal point is (approximately) nonexpansive up to an error you can control (through the approximate subsolver of the max-oracle)? This could potentially eliminate the need for the bounded domain assumption, broadening the applicability of the result.

### Questions
- I'm surprised that bounded domain is needed in Thm. 5. Is it not possible to use that inexact proximal point is (approximately) nonexpansive up to an error you can control (through the approximate subsolver of the max-oracle)?

### Soundness
3 good

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
This paper focuses on nonconvex-nonconcave minimax problems. It introduces a new method called the semi-anchored (SA) gradient method, which extend the idea of PDHG to the nonlinear setting by incorperating the certain Bregman distance as a preconditioner. With a designed Legendre function, the SA-GDmax and its practical version SA-MGDA are studied with convergence result and suitable optimality measure.

### Strengths
The convergence theorem of proposed algorithm is presented, along with an inexact practical version. Numerical results validate the effectiveness of the proposed algorithm in solving problems that satisfy the weak MVI condition, showing performance comparable to extragradient-type algorithms.

### Weaknesses
The paper's motivation should be elucidated in greater detail. Additionally, it is advisable to compare the proposed algorithm with recent papers on nonconvex-nonconcave minimax problems that are based on various regularity conditions, such as dominant conditions and the PL inequality, in order to demonstrate the competitiveness of the proposed approach.

The paper is centered on the one-sided extrapolation-based PDHG method, and while all theoretical performance are similar to the extragradient method under weak MVI conditions, the motivation behind introducing this method may benefit from further clarification. The author also alludes to the potential for improving the extragradient method; providing more specific details on such improvements would enhance the paper.

In Theorems 5 and 6, the use of gradient computational cost may not be ideal. The $\mathcal{O}(\log(1/\epsilon))$ cost pertains to the iteration cost of the proximal gradient descent method, where the computational cost of the proximal operator is neglected. Additionally,  the worst computational cost for this class of functions can be  $\mathcal{O}(1/\epsilon)$ as mentioned in arxiv:2101.11041.

Verifying weak MVI conditions can be challenging, and the need for each stationary point to meet this requirement in the derived theorems could be a limiting factor.

### Questions
1. The paper is centered on the one-sided extrapolation-based PDHG method, and while all theoretical performance are similar to the extragradient method under weak MVI conditions, the motivation behind introducing this method may benefit from further clarification. The author also alludes to the potential for improving the extragradient method; providing more specific details on such improvements would enhance the paper.
2. In Theorems 5 and 6, the use of gradient computational cost may not be ideal. The $\mathcal{O}(\log(1/\epsilon))$ cost pertains to the iteration cost of the proximal gradient descent method, where the computational cost of the proximal operator is neglected. Additionally,  the worst computational cost for this class of functions can be  $\mathcal{O}(1/\epsilon)$ as mentioned in arxiv:2101.11041.
3. What is the numerical performance of the algorithm for nonconvex-nonconcave problems without the weak MVI condition? If it performs well in such cases, it may be worth exploring the possibility of relaxing certain conditions to accommodate a broader range of problems. Verifying weak MVI conditions can be challenging, and the need for each stationary point to meet this requirement in the derived theorems could be a limiting factor.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
