# On the Convergence of FedProx with Extrapolation and Inexact Prox

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Enhancing the FedProx federated learning algorithm \citep{li2020federated} with server-side extrapolation, \citet{li2024power} recently introduced the {\FEDEXPROX} method.
   Their theoretical analysis, however, relies on the assumption that each client computes a certain proximal operator exactly, which is impractical since this is virtually never possible to do in real settings.
   In this paper, we investigate the behavior of {\FEDEXPROX} without this exactness assumption in the smooth and globally strongly convex setting.
   We establish a general convergence result, showing that inexactness leads to convergence to a neighborhood of the solution.
   Additionally, we demonstrate that, with careful control, the adverse effects of this inexactness can be mitigated.
   By linking inexactness to biased compression \citep{beznosikov2023biased}, we refine our analysis, highlighting robustness of extrapolation to inexact proximal updates.
   We also examine the local iteration complexity required by each client to achieved the required level of inexactness using various local optimizers.
   Our theoretical insights are validated through comprehensive numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the convergence behavior of FedExProx, a recent extension of the FedProx federated learning algorithm, which includes server-side extrapolation to improve performance in federated settings. A key issue with existing analyses of FedExProx is the assumption that each client can compute the proximal operator exactly, which is unrealistic in practical applications. This paper relaxes this assumption, examining the algorithm’s behavior in cases where the proximal operator is only computed approximately. The authors establish convergence results in smooth, globally strongly convex settings, demonstrating that the algorithm still converges, albeit to a neighborhood around the solution. They also show that careful control can reduce the negative impact of inexact proximal updates and draw connections to biased compression methods. Additionally, they provide an analysis of the local iteration complexity needed for clients to achieve a specific level of inexactness, with empirical validation of their findings through numerical experiments.

### Strengths
The paper addresses a significant gap in existing work on FedExProx by relaxing the exact proximal computation assumption. This makes the analysis more applicable to real-world federated learning systems, where inexact computations are the norm due to resource constraints.

### Weaknesses
 - The theoretical analysis is restricted to globally strongly convex problems, which may limit its applicability to a broader range of federated learning applications that involve non-convex objectives. Extending this analysis to non-convex cases would significantly increase the paper’s impact.

- The assumption of smoothness might not always hold in federated learning, particularly when clients have heterogeneous data distributions. A discussion on how the proposed approach might generalize or be adapted for non-smooth settings would strengthen the paper.

- The experimental part is the weakest part of this work...

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work sets to explore a recent algorithm in FL called FEDPROX. This algorithm leans on exact computation of what is called proximal operator.
The paper asks the following natural question: what if we do not fully solve the operator, but rather solve approximately?
In the smooth+strongly-convex case, this paper explore this questions assuming two kinds of approximations $\epsilon_1$ and $\epsilon_2$.

### Strengths
- The question is indeed natural and relevant to concurrent FL problems

- The authors cleverly define two kind of approximations and show that one is better then the other, allowing us to converge to the true optimum

- The writing is very clear and easy to follow

- Experiments are illustrative, and in a sense validate the theory

### Weaknesses
 - While the question is natural and important, the solution is quite straightforward, and does not introduce any novel tools or analysis. Excluding the  $\epsilon_2$ approximation which is nice.

- The paper does not consider stochastic gradients which is the more relevant case in practice, it is important to understand how will the results change in light of this?

### Questions
- What is the main challenge and main novelty in your paper?

- Why do you not take stochastic gradients into account? How will the results change assuming this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on a federated learning algorithm, called FedExProx, that requires each client to compute exactly a proximal operator. The authors analyze the FedExProx method when the proximal operators of each client is not computed exactly. Theoretical guarantees are provided in the strongly convex and smooth setting and the convergence rate of the algorithm is established. Moreover, the authors highlight a connection with the bias compression methods, that allows them to obtain more refined convergence guarantees. The iteration complexity of the local updates for gradient descent and accelerated gradient descent are also provided. Experimental results validate the theoretical results and showcase the effect of the different notions of inexactness in the computation of the proximal operator in the convergence of the method.

### Strengths
- The convergence is established under different notions of inexactness of the proximal operator.
- The paper recovers as a special case the results of the original paper on FedExProx, when the proximal operators are evaluated exactly.
- The connection with the biased compression is interesting.

### Weaknesses
 - Theorems 1, 2, 3 require the notion of interpolation. Even though an explanation of regimes that satisfy this condition is provided, considering that there are previous works [1], [2] that extend beyond that setting, this assumption seems to be an avenue for future work in this field. More specifically, the initial FedProx algorithm [1] is analyzed in the general non-interpolated setting. In addition, the follow-up work regarding the FedExProx algorithm [2] considers in the main paper the interpolated regime. However, the authors provide additionally an illustration of the algorithm's behaviour in the non-interpolated setting (see Appendix F.3 in [2]). In that sense, it would be useful to provide some additional details on the behaviour of the algorithm in the non-interpolated setting or to comment on the main challenges in extending the current proof technique beyond the interpolation framework, offering in that way a more complete picture and direction for future research. 
- Theorems 4, 5 seem to evaluate the inexactness achieved in each client. However, the inexactness is only with respect to the notion of the absolute approximation, for which we know that Theorem 1 is not optimal (since for the same amount of inexactness Theorem 3 gives convergence to the exact solution). Thus, it seems that a characterization of the inexactness in terms of the relative approximation would be also useful. Hence, providing similar theorems for the relative approximation case seems to be a nice addition to the current results. 
- Minor: The statement of Theorem 1 can be made shorter in order to increase the readability of the paper.
- Minor typo: In Figure 1, it is mentioned “Figure (c) demonstrates how varying values of $\epsilon_1$ affect FedExProx with relative approximation.” but as shown the varying values correspond to $\epsilon_2$.

### Questions
- Theorem 1 seems to provide convergence guarantees under the natural assumption of absolute approximation. However, the guarantee provided, as mentioned, includes a neighbourhood of convergence which is not optimal. On the other hand, the connection with biased compression provides a refined theorem (Theorem 3), establishing convergence to the exact solution. The amount of inexactness, though, in Theorem 3 is bounded. Do you think that one can achieve the best of both worlds, namely convergence to the exact solution but for arbitrary inexactness.
- How one can compute the relative inexactness $\epsilon_2$ in practice? Are there inherent computational tradeoffs or challenges in the computation of the relative inexactness $\epsilon_2$ in comparison to estimating the constant $\epsilon_1$? It would be nice also if you could comment on ways to approximate $\epsilon_2$ in practical federated learning problems.  
- Is it possible to raise the assumption on interpolation in the strongly convex setting by using a more refined proof technique or do you think that extrapolation might be beneficial only on that regime?

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
3

### Summary
The paper considers a finite-sum $\mu$-strongly convex problems for which the interpolation conditions holds, and where each client objective is convex and $L$-smooth.
The work then considers the FedExProx method, which combines proximal client updates with an extrapolated server step, and extends this work to handle inexactness of the client prox computations. Specifically:

- with fixed absolute inexactness they show that the method converges to a neighbourhood of the solution (using a factor $1/4$ smaller extrapolation step).
- with a type of relative inexactness (smaller than order $\mu^2/L^2$) they show exact convergence but for a restrictive extrapolation server stepsize $\alpha$.
- for relative inexactness with a more stringent condition (smaller than order $\mu/L$) they show that the same (large) extrapolation stepsize can be used as in the exact case.
- They provide convergence rate for the local strongly convex and smooth objective with gradient descent and Nesterov acceleration.

### Strengths
- The writing is very clear and transparent. They state how results are obtained (relative inexactness by using analysis from biased SGD and from compression) and discuss limitations.
- Considering relative inexactness for federated learning seems interesting

### Weaknesses
 - the work requires very strong assumptions: the solution needs to be unique (strong convexity) and shared amongst all clients (interpolation condition)
- There is a large body of work on relative inexactness for proximal methods starting with [1], where it is used to essentially inherent the nice properties of an exact proximal computation. Considering the strong assumptions (strong convexity and interpolation condition) it does not seem very surprising that one can extend to a multi-client setting. It would be good to cite this work and put it into context. 
- The work does not treat adaptive stepsizes and partial participation as in (exact) FedExProx (they do discuss the difficulty of client sampling in the appendix).

Minor:

- The local convergence rates are not new. It would be good to explicitly state this.
- After Theorem 2 when discussing the slowdown due to small $\alpha$, it would be informative to plug in $\varepsilon_2=c\mu^2/L_{max}^2$ for some $c<1$ and simplify the expression.
- It it possible to to get convergence not only to a neighborhood even for absolute inexactness. It might be worth choosing the $\varepsilon_1$ sufficiently small, to make the comparison with relative inexactness more direct (how does the choice effect the client steps and the communication rounds?).
- For absolute inexactness the server stepsize $\alpha$ is a factor ¼  smaller. Maybe stress that this affects the rate explicitly in Table 1.
- It is maybe worth stating how many iterations (e.g. with Nesterov) are needed to make $\varepsilon_2 =\mu/L$ vs $\varepsilon_2 =\mu^2/L^2$ to make the comparison/tradeoff more explicit between the two relative inexactness results.
- It seems like some concurrent work is treating absolute inexactness which might be worth mentioning [2]

Typos:

- Eq. 4 both f and $\phi$ are present

### Questions
- Fig. 1(a) indicates that inexactness can help whereas the theory predict otherwise. For inexact proximal gradient inexactness have shown to help for certain regimes (see e.g. page 5 of [3]). Is it possible that something analogue can be said in your setting?
- It is not very clear how much having a more stringent requirement on the relative inexactness ($\mu/L_{max}$ as compared with $\mu^2/L_{max}^2$) buys in terms of the global rate. Is it possible to explicitly compare $S(\varepsilon_2)$ with $(1-4\varepsilon_2 L_{max})$?

[3] https://proceedings.neurips.cc/paper_files/paper/2011/file/8f7d807e1f53eff5f9efbe5cb81090fb-Paper.pdf

### Soundness
2

### Presentation
2

### Contribution
2
