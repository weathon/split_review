# Sparsistency for inverse optimal transport

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
Optimal Transport is a useful metric to compare probability distributions and to compute a pairing given a ground cost. Its entropic regularization  variant (eOT) is crucial to have fast algorithms and reflect fuzzy/noisy matchings. This work focuses on Inverse Optimal Transport (iOT), the problem of inferring the ground cost from samples drawn from a coupling that solves an eOT problem. It is a relevant problem that can be used to infer unobserved/missing links, and to obtain meaningful information about the structure of the ground cost yielding the pairing. On one side, iOT benefits from convexity, but on the other side, being ill-posed, it requires regularization to handle the sampling noise. This work presents an in-depth theoretical study of the $\ell_1$ regularization to model for instance Euclidean costs with sparse interactions between features. 
Specifically, we derive a sufficient condition for the robust recovery of the sparsity of the ground cost that can be seen as a far reaching generalization of the Lasso’s celebrated ``Irrepresentability Condition’’. To provide additional insight into this condition, we work out in detail the Gaussian case. We show that as the entropic penalty varies, the iOT problem  interpolates between a graphical Lasso and a classical Lasso, thereby establishing a connection between iOT and graph estimation, an important problem in ML.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is about inverse optimal transport (iOT), that is the task of inferring a ground cost from the sampling of an (entropy-regularized) optimal transport plan.
For linear parametrizations of the cose, iOT is a convex inverse problem (Dupuy et al 2019), that the authors propose to regularize with the $\ell_1$ penalty.

The paper first derives an irrepresentability condition (IC) for the iOT problem,
based on non degeneracy of a "precertificate" (Def 1).
First, the authors show that the solution of the regularized "infinite samples" problem shares the same sign as the true parameters under IC, for low enough regularization value (Thm 3).
Then the more interesting "Sparsistency" results are then derived: in the finite sample case, the correct support is still recovered (under IC) for small regularization values and sufficiently many samples (Theorem 7).

Additional details in the case of Gaussian distributions are provided, with interpretation as Lasso and Graphical Lasso respectively for vanishing or exploding entropic regularization strength.
Experiments on limited size graphs (80 nodes) conclude this theoretical paper.

### Strengths
Inverse optimal transport has recently attracted attention in the community due to its potential impact in ML.
Proposing better alternatives to solve this nonlinear inverse problem is thus of interest.
The paper provides results on both "full distribution" and finite sample problems.
I did not spot any mathematical error, but could not check all of the paper.

### Weaknesses
 The authors could really afford to improve the pedagogy of the paper, which is quite heavy in terms of notation. Theory is quite involved, require background references to other works such as Carlier or Galichon. The experiment description is a big block which, in my opinion, does not bring as many insights as it could.

 Questions:
- why does Proposition 8 imply that $z_\infty$ is nondegenerate? Why, given its definition 1 line above, is it of the form written in (PrC)?
- In prop 9 shouldn't the limit of $\epsilon_n$ be $\infty$?


Minor:
- In theorem 3, $\hat A$ is such that $\hat \pi = \text{Sink}(\hat A, \epsilon$; this has been introduced earlier but given the large number of variables defined in the paper, it may not hurt to recall it here; in addition, before, Sink was applied to $c$, so it should be $\text{Sink}(c_{\hat A}, \epsilon$. In prop 10, prop 11 the order of the arguments is reversed.
- can the authors explain the name "precertificate" (what's "pre" about it? Is there a difference with what Dunner and coauthors call "Dual certificate" in https://arxiv.org/abs/1602.05205)?
- The authors refer to "condition PrC", but that is just an equality. Condition PrC would be that the dual norm of the precertificate outside the support is $< \lambda$
- what's "the convex dual of W (A)"? convex conjugate of a function (as in Proposition 4)/convex dual of a convex optimization problem?
- is the notation $\langle c, A \rangle$ for a non scalar result?
- In theorem 7 I spent quite some time looking for what the number $m$ was in other parts of the paper (because of the analogy $m/n$ in compressed sensing) before realizing that it was a free paramert; maybe replacing it by $\ln(1/\delta)$ is more common (that is only a suggestion).
- below 9, in $A_n$ definition, both $\epsilon$'s should be $\epsilon_n$? Same in Prop 11
- it follows (see e.g. Hiriart-Urruty et al. (1993)) : can you point to a specific result in the book? Also in the bibliography, the authors names appear twice for this book.

Typos:
- the paper does not seem to use the unmodified iclr template, the font differs from that of other papers
- in Problem iOT L1 hat Pi, the first argument of L should be $A$ not $c_A$ (see def of L 2 equations above)
-  The iOT problem of iOT
- in a series of paper*s*
- Thm 3: the solution ... satisf*ies*
-  minimial norm
- sufficinetly$
- result above implies that for provided that the number
- as exposed in Section ??
- Cauchy Schwartz
- see Proposition PrC (it's an equation not a proposition, and I don't see why pRC shows that W is $C^2$)

### Questions
Questions:
- why does Proposition 8 imply that $z_\infty$ is nondegenerate? Why, given its definition 1 line above, is it of the form written in (PrC)?
- In prop 9 shouldn't the limit of $\epsilon_n$ be $\infty$?


Minor:
- In theorem 3, $\hat A$ is such that $\hat \pi = \text{Sink}(\hat A, \epsilon$; this has been introduced earlier but given the large number of variables defined in the paper, it may not hurt to recall it here; in addition, before, Sink was applied to $c$, so it should be $\text{Sink}(c_{\hat A}, \epsilon$. In prop 10, prop 11 the order of the arguments is reversed.
- can the authors explain the name "precertificate" (what's "pre" about it? Is there a difference with what Dunner and coauthors call "Dual certificate" in https://arxiv.org/abs/1602.05205)?
- The authors refer to "condition PrC", but that is just an equality. Condition PrC would be that the dual norm of the precertificate outside the support is $< \lambda$
- what's "the convex dual of W (A)"? convex conjugate of a function (as in Proposition 4)/convex dual of a convex optimization problem?
- is the notation $\langle c, A \rangle$ for a non scalar result?
- In theorem 7 I spent quite some time looking for what the number $m$ was in other parts of the paper (because of the analogy $m/n$ in compressed sensing) before realizing that it was a free paramert; maybe replacing it by $\ln(1/\delta)$ is more common (that is only a suggestion).
- below 9, in $A_n$ definition, both $\epsilon$'s should be $\epsilon_n$? Same in Prop 11
- it follows (see e.g. Hiriart-Urruty et al. (1993)) : can you point to a specific result in the book? Also in the bibliography, the authors names appear twice for this book.

Typos:
- the paper does not seem to use the unmodified iclr template, the font differs from that of other papers
- in Problem iOT L1 hat Pi, the first argument of L should be $A$ not $c_A$ (see def of L 2 equations above)
-  The iOT problem of iOT
- in a series of paper*s*
- Thm 3: the solution ... satisf*ies*
-  minimial norm
- sufficinetly$
- result above implies that for provided that the number
- as exposed in Section ??
- Cauchy Schwartz
- see Proposition PrC (it's an equation not a proposition, and I don't see why pRC shows that W is $C^2$)

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the regularized inverse entropic optimal transport problem. Inverse optimal transport (iOT) is the problem of recovering the ground cost given samples from the (potentially, noisy) joint distribution. Recent works have proposed solvers to solve the primal and dual formulations of the iOT and regularized iOT problem. This paper studies the recovery guarantees for the L1-regularized iOT problem. They further explore a special case where the densities are Gaussian, and show that in some cases, iOT results in the graphical LASSO problem.

### Strengths
- Inverse optimal transport is an interesting problem and an interesting take on the metric learning problem, this work takes a significant step forward in establishing a theoretical grounding for the regularized iOT problem.
- I really enjoyed reading the paper, the writing is very clear, the background, method, and the results are well presented.
- Showing that graphical LASSO as a special case of inverse OT is very interesting and makes sense.

### Weaknesses
 - Nothing that I can think of.

### Questions
- How practical is inverse OT? I understand that the current work considers linear cost functions. Can one, albeit without strong theoretical guarantees, learn a general (perhaps, regular) cost function from the samples drawn from the coupling?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper deals with the problem of inverse optimal transport on compact (but not necessarily finite) state space to find the cost function from a given empirical probability coupling. It establishes a connection to lasso and produces the sample complexity of solving the corresponding primal-dual method.

### Strengths
Finding the cost function from the empirical process induced by the optimal transport algorithm is an important open question. In that respect, this paper addresses an important open question. The connection of the non-degenerate precertificate assumption with irrepresentability assumption in lasso is an interesting insight. Finally, I found the connections to the SVD of the covariance matrix illuminating. The gaussian example also serves to demonstrate the theory through the lenses of an example.

### Weaknesses
Although the sample complexity bound is good, there was no discussion about the tightness of the said bound. I wonder if the $1/\sqrt{n}$ is also the best lower bound. Observing that the empirical density acts like a ``plug-in" for the unknown true coupled density, can the statistical guarantees of the plug-in be translated to the guarantees for the cost function? Specifically, it's unclear how the convergence rate of the empirical measure to the true measure impacts the convergence rate of the estimated cost function. Furthermore, the paper does not address the potential impact of the choice of basis functions on the convergence rate. The choice of basis functions could significantly affect the approximation quality and thus the sample complexity. It would be beneficial to discuss the conditions under which the chosen basis functions provide a good approximation of the true cost function. 

Also, the role of the penalty term $\lambda$ needs further clarification. While the paper mentions it is a regularization parameter, it does not provide sufficient guidance on how to choose it in practice. Is $\lambda$ a hyperparameter that needs to be tuned for each problem instance? How does the choice of $\lambda$ affect the bias-variance trade-off in the estimation of the cost function? The paper also does not discuss the computational cost of solving the primal-dual method, especially in high-dimensional settings. It would be useful to provide some insights into the scalability of the proposed approach.

Finally, while the paper assumes access to samples from the coupled empirical density, it does not discuss how these samples are obtained in practice. Do we assume that we have access to the optimal transport plan, or do we only have access to samples from the marginal distributions? If we only have access to samples from the marginal distributions, how does this affect the sample complexity and the convergence rate?

### Questions
Can the authors please elaborate more on the penalty term $\lambda$? Is $\lambda$ given for a given problem? Is it shrinking with $n$? 

Also, do the authors implicitly assume that we can sample from the coupled empirical density? Or do we just have access to some samples?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article addresses the problem of inverse optimal transport, which involves estimating the transport cost from an optimal (noisy) transport plan. The authors focus on the 'penalized' $\ell_1$ cost formulation, parametrized by a matrix of parameters (the cost is parametrized as linear combination of individual costs, such as in the Mahalanobis setting). The article provides two types of guarantees:

The first type of guarantee, referred to as the "finite sample case," is an estimation guarantee obtained from dual certificates when the observed transport plan is an entropic regularized plan between two empirical measures.

The second type, in the "Gaussian case," deals with the scenario where the measures involved are Gaussian distributions (a well-known case in transport that admits a closed-form solution). In this case, the article demonstrates that the cost estimation can be solved as a graphical lasso problem, especially when the entropic regularization is small.

### Strengths
- I find the introduction and contextualization of the article to be very well done. The related work appears comprehensive, and the problem is well-situated.

- The theoretical results in this article are interesting. For the discrete case, the authors demonstrate that, with a small $\ell_1$ regularization and a sufficiently large number of samples, the ill-posed problem of invOT can indeed recover the costs.

- The connections between graphical lasso and invOT are also intriguing and interesting.

### Weaknesses
 - I find that the article doesn't put in enough effort to explain the practical implications of the various theoretical results, which remain somewhat abstract. It's quite challenging to understand how these results can be practically applied.

Firstly, the concept of a pre-certificate condition is rather very abstract (unlike the case of Lasso that we can somehow interpret). It would be interesting to provide the reader with a bit more guidance to offer a small interpretation of this quantity.

Another example is Proposition 8. It's difficult for me to extract something from this result, aside from the qualitative interpretation that "for small regularization, under somewhat abstract assumptions of certificates, and with a sufficiently large number of samples, solving the invOT problem yields a good solution." To make these results more applicable in practice, it would be helpful to either provide experiments or guarantees that demonstrate how to understand these pre-certificate assumptions or ensure that the level of regularization is appropriate. I realize that these may be challenging questions, but I find that not much intuition is given, and the practical use of these results does not appear straightforward.

- My main criticism concerns the experiments section. I find the experiments too limited and somewhat confusing, making it difficult to obtain meaningful information.

First, only the Gaussian with an identity covariance is considered. The idea is to study the impact of entropic regularization on invOT estimation. The presentation is somewhat unclear, and I struggle to understand from Figure 1 how it quantifies the influence of $\epsilon$ on the estimation. There is no legend for the y-axis, and while it's understood to be the certificate value between two nodes, it's unclear how it serves as a good performance measure for the invOT problem. 

Figure 2 is equally unenlightening. It aims to determine the influence of the number of samples on the estimation in the very simple case of a circular graph and Gaussian measures. However, what is the x-axis on these three figures? Is it the number of iterations? The geodesic distance? If it's the geodesic distance, it's not clear because the y-axis is a global performance measure over C, while the x-axis appears to be a local measure, so it's unclear how one evolves with the other.

The conclusion appears to be that the estimation is "good" when the entropic regularization is sufficiently large, and the number of samples is also large. More importantly, there seems to be a significant gap: when $\epsilon \leq 10$, the estimation is consistently poor. Is this a result expected by the theory regarding $\epsilon$?

### Questions
I'm curious to know whether the Gaussian results really require entropic regularization. Without regularization we also have a closed form: can't we deduce good invOT estimation guarantees in the non-regularized case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
