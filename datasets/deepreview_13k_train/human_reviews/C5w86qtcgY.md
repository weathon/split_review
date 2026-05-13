# Decentralized Finite-Sum Optimization over Time-Varying Networks

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
We consider decentralized time-varying stochastic optimization problems where each of the functions held by the nodes has a finite sum structure. Such problems can be efficiently solved using variance reduction techniques. Our aim is to explore the lower complexity bounds (for communication and number of stochastic oracle calls) and find optimal algorithms. The paper studies strongly convex and nonconvex scenarios. To the best of our knowledge, variance reduced schemes and lower bounds for time-varying graphs have not been studied in the literature. For nonconvex objectives, we obtain lower bounds and develop an optimal method GT-PAGE. For strongly convex objectives, we propose the first decentralized time-varying variance-reduction method ADOM+VR and establish lower bound in this scenario, highlighting the open question of matching the algorithms complexity and lower bounds even in static network case.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies decentralized finite-sum optimization problem over time-varying graphs. Theorem 4.3 and Theorem 4.5 establish lower bounds on computational and communication complexities, resp., for strongly convex and non-convex optimization. Furthermore, the paper presented two algorithms ADOM+VR and GT-PAGE, resp., for strongly convex and non-convex optimization while comparing its performance with the state-of-the-art methods both analytically (see Tables 1 & 2) and numerically. Notably, GT-PAGE is optimal by achieving the lower complexity bounds while ADOM+VR is optimal in terms of communication iterations. Some open problems have also been highlighted. The numerical examples for the LibSVM dataset show the superior performance of the algorithm in terms of communication and computational complexities. Interestingly, the optimal algorithm GT-PAGE achieve presents better yet not strongly superior performance in comparison to the state-of-the-art methods.

### Strengths
- The paper studies an important problem.
- The paper is well-written.
- Notation, assumptions, and results are presented clearly.
- The established lower bounds on the complexities and presenting optimal algorithms achieving these bounds are solid contributions.
- Numerical examples further strengthen the paper's claims.

### Weaknesses
 - The paper is fairly technical. To smoothen the paper's technical content and to improve the paper's accessibility, more qualitative discussions can be included.
- The introduction directly jumps to the optimization problem formulation. More motivating examples for the problem formulation would improve the paper.
- In the introduction, Tables 1 and 2 present the complexities in terms of parameters n, L, \mu, and some others. However, it is not clear what these parameters, e.g., L and \mu, refer to.
- Numerical examples do not provide error bars.

### Questions
- Can the authors clarify whether there is no need to represent error bars across independent experiments to mitigate the impact of stochasticity in the numerical examples?

### Soundness
3

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
This manuscript addresses a decentralized stochastic optimization problem with a finite sample set at each node over time-varying networks. The authors propose two algorithms tailored for strongly convex and non-convex objective functions, respectively, and provide a lower bound analysis to discuss the optimality of the proposed algorithms.

### Strengths
- This work provides rich theoretical analytical results for different objective function assumptions. By comparing with the proposed lower bound, it is shown that the proposed algorithm is optimal in their scenario;
- The lower bound in this paper takes into account the smoothness coefficient of each node, which is more refined.

### Weaknesses
While this work presents a set of results for distributed stochastic optimization problems, I found the paper difficult to follow, with unclear motivation and insufficient discussion on the necessity of this study. My specific concerns are as follows:

- On the significance of this work: The paper addresses time-varying topologies in distributed networks, but it is unclear why these topologies pose unique challenges for distributed algorithms. In my view, as long as Assumption 2.5 holds (i.e., the topology is connected at each iteration) and multi-round communication acceleration is employed, a time-varying topology does not seem substantially more challenging than that of fixed topology. Thus, this work appears to be tackling a corner case, especially considering that similar problems have been widely studied, e.g., Kovalev et al., 2021a, Luo and Ye, 2022, Huang and Yuan, 2022, Li and Lin, 2021. The authors need to further clarify the novelty and contribution of this work against these exisitng works.
- On the Assumptions on Smoothness: The assumptions regarding smoothness are somewhat confusing. The authors consider three types of smoothness but do not compare their differences or clarify which assumptions are strongest. Additionally, Assumption 2.1 requires that each sample’s objective function is smooth. It would be helpful to discuss whether this holds in typical machine learning tasks and if it is verifiable in practice. Furthermore, the relationship between the smoothness constants $L$, $\overline{L}$, and $\hat{L}$ is not clearly explained, making it difficult to understand the implications of each assumption.
- Regrading the proof of Theorem 3.2, compared to (Kovalev et al., 2021a), it seems to differ in only one constrained VR gradient estimation error (c.f. Lemma B.1), while the other proofs are almost identical to Kovalev et al., 2021a, differing only in some parameter choices. This makes the technical contribution of this paper vague. The core innovation in handling the time-varying topology, specifically how the gradient tracking and error feedback mechanisms are adapted, is not sufficiently highlighted, making it seem like a minor extension of existing work.
- On Readability and Clarity: The paper’s readability could be significantly improved. In the algorithm design section, the authors rely heavily on prior literature to explain their algorithmic approach, offering limited unique insights. This reliance diminishes the perceived novelty of the work. Additionally, the paper contains many symbols that are either used before being defined or left undefined altogether (e.g., $\lambda^{+}_{\text{min}}$), making it challenging to follow.

### Questions
- Why the two proposed algorithms require different function smoothness assumptions (c.f. Assumption 2.1, 2.2 and 2.3)?
- The LibSVM dataset used for the experiments in this work seems not adequate; the reviewer would like to know if the algorithm could be applied to more complex datasets such as cifar-10/100 to further validate the effect of the algorithm.
- How is the time-varying topology being implemented in the experiments?
- Why the reference Metelev et al. (2024) is not discussed in the main text? In fact, the time-varying topological sequences used in this work for obtaining lower bound adopt their strategy.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies stochastic decentralized optimization problems of strongly-convex and non-convex settings over static and time-varying networks. For the strongly-convex setting, the ADOM+VR algorithm is proposed and the convergence property is established; For the non-convex setting, the GT-PAGE algorithm is proposed and the convergence property is established. The authors also study the lower bounds of both strongly-convex and non-convex decentralized optimization problems theoretically. The efficacy of the proposed algorithms is validated in simulations.

### Strengths
The topic of the work is well aligned with ICLR community and it is significant to extend the lower bound analysis for decentralized optimization problems. The work also contains great amount of theoretical work.

### Weaknesses
1. The organization of the manuscript is not clear and different pieces (section 3.2, 3.3, 4.1) are isolated from each other. Since they are presented in this manuscript, it is assumed they have some internal relationship. For example, is the optimal non-convex algorithm, GT-PAGE, also optimal in the strongly-convex setting? Why is the strongly-convex algorithm based on ADOM+ algorithm while the non-convex algorithm is based on PAGE algorithm?

2. It is concerned that the Assumption 2.5 is too strong, i.e., assuming the existence of $\chi \geq 1$ (also why $\geq 1$ rather than $ > 1$?).  This work studies time-varying networks and the matrices $W(k)$ change at every time step $k$. How is it guaranteed that such $\chi$ exists? Are there any other requirements for the network connectivity or matrix construction to guarantee the existence of $\chi$?

### Questions
1. The organization clarity (please see weakness-1). In order to better elaborate the contributions in this work, it is suggested that the authors re-write all bullet points in the contribution paragraph. For the ADOM+VR algorithm, please state the type of optimization problem/network setting and why it is optimal (is it applied to a different optimization problem or the convergence speed is faster than others); For the GT-PAGE algorithm, please also state the type of optimization problem and why it is optimal. It is not strong enough to only mention the elements of different algorithms in the contribution.

2. The achievability of Assumption 2.5 (please see weakness-2).

3. In experiments, are those plots presenting training set performance or testing set performance? It is expected both training and testing performance are shown. Moreover, it would be good to show classification accuracy on test set.

### Soundness
3

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
This paper studies decentralized finite-sum optimization over time-varying networks for smooth objectives. 

In the strongly-convex setting, the ADOM+VR algorithm consists in mixing the ADOM+ (accelerated decentralized optimization for time-varying graphs) and Katyusha (Accelerated variance-reduced single-machine) algorithms. Similarly, the lower bound mixes the ones from ADOM+ and ADFS. 

In the non-convex setting, gradient tracking (a standard way to obtain "exact" decentralized algorithms) is combined with the PAGE VR algorithm. Similarly, the lower bound mixes that of Yuan et al (2022) and ADOM+. 

In both cases, combining existing optimal approaches yields (almost) matching upper and lower complexity bounds. Toy experiments are given to illustrate the practical performances.

### Strengths
- the overall approach is clear and natural
- (almost) matching upper and lower bounds 
- results for both strongly convex and non-convex settings

### Weaknesses
 - Contributions are incremental: mostly combining accelerated variance-reduced estimators with accelerated decentralized algorithms over time-varying graphs (or gradient tracking for the non-convex setting) 
- The setting (finite-sum decentralized optimization over time-varying graphs) is rather niche
- The algorithms are quite rigid, with long communication stages (through $W(k)$) and long computation stages (through mini-batching), which is effective but not very elegant, and unlikely to extend well to, e.g., asynchronous settings. Approaches like DADAO (Nabli and Oyallon, 2023) are likely to lead to better solutions, as well as maybe close the gap between lower and upper bounds in the strongly-convex setting.
- The non-convex algorithm has a pretty bad dependence on the graph constants ($\chi^3$), and is only saved by multi-consensus steps (which again, would likely break in asynchronous settings for instance).

### Questions
- It is said in Corollary 3.3 that the number of communications per iteration is of order $\chi$, but in Algorithm 1 there is only one communication per iteration (matrix $W(k)$ is used). I understand that we should use Algorithm 1 with the multi-consensus matrix $W(k, \kappa)$ instead, is that true? This should be clarified.

### Soundness
3

### Presentation
3

### Contribution
2
