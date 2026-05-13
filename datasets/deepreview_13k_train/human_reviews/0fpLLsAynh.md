# Sporadicity in Decentralized Federated Learning: Theory and Algorithm

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Decentralized Federated Learning methods are a family of techniques employed by devices in a distributed setup to (i) reach consensus over a common model which (ii) is optimal with respect to the global objective function. As this is carried out without the presence of any centralized server, prominent challenges of conventional Federated Learning become even more significant, namely heterogeneous data distributions among devices and their varying resource capabilities. In this work, we propose $\textit{Decentralized Sporadic Federated Learning}$ ($\texttt{DSpodFL}$), which introduces sporadicity to decentralized federated learning. $\texttt{DSpodFL}$ includes sporadic stochastic gradient calculations and model exchanges for aggregations. Our motivation is to achieve joint computation and communication savings without losing statistical performance. We prove that by using a constant step size, our method achieves a geometric convergence rate to a finite optimality gap. Through numerical evaluation, we demonstrate the resource savings achieved by $\texttt{DSpodFL}$ compared to the existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers computing and communication resource efficiency problems in decentralzied federated learning over undirected communication networks. To solve this problem, the authors propose the DSpodFL algorithm, which introduces sporadic local stochastic gradient descent (SGD) computations and model aggregations among nodes. Specifically, at each iteration, each node conducts local SGD with some probability and each communication link activates with some probability. Their analysis shows that the proposed DSpodFL achieves a geometric convergence rate to a neighborhood of the globally optimal solution for a constant SGD step size, in a strongly convex and smooth setting. They conduct some numerical experiments to demonstrate the superior performance of DSpodFL compared to the existing baselines.

### Strengths
1. Their proposed algorithm employing sporadic SGDs and sporadic aggregations, seems new to the reviewer.

2. They provide linear convergence results for their proposed DSpodFL and show that the final optimality gap (steady-state error) is dimishing with the step size.

3. The manuscript is well-organized and is easy to follow.

### Weaknesses
1. The dependence of linear convergence rate $\rho \left( \Phi \right)$ on problem-related parameters such as step size , number of devices, frequency of computations, frequency of communications and the connectivity of the communication graph is not discussed in their theoretical results, which is the main limitation in the convergence property of DSpodFL.

2. Moreover, there are no theoretical comparisons to the baselines: e.g., to [1].

3. Limited node scability: Only 10 nodes is considered in their numerical experiments. How does the proposed DspodFL scale with repect to the node number is not clear.

4. Some baselines are missing in experiments, such as AD-PSGD [2] and OSGP [3].

### Questions
Refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Paper proposes a Decentralized Sporadic Federated Learning (DSpoFL) algorithm which allows both sporadic (i) local gradient updates and (ii) model averaging. Using a constant step-size (when local gradient updates do occur), theoretical  results for DSpoFL are provided to detail the convergence rates of average model error and consensus error. These results require strong convexity assumptions as well as expected sporadicity variables for local gradient updates and communication. Empirical results are provided for simple datasets in convex and non-convex settings.

### Strengths
1. Nice theoretical analysis is provided in terms of convergence rates (for consensus and model errors) that are often left out in many FL papers.
2. Tackling heterogeneity in FL is one of the final frontiers that need to be addressed, and so this paper is looking to solve important issues.

### Weaknesses
1. The novelty of the idea behind DSpoFL is lacking to me. There is a lot of work in FL on sporadic communication as well as compression and asynchronous methods to speed up the actual communication process. Sporadic local updates is more interesting but just allowing local gradient updates to either happen or not happen (without specifying what is the optimal rate or schedule for this) does not seem to be a large improvement in the field. The paper does not sufficiently differentiate itself from existing asynchronous and sporadic communication techniques in federated learning. It needs to show how the specific method of sporadic local updates provides a significant advantage over existing methods, beyond simply introducing another form of sporadicity. The lack of a clear strategy for determining when local updates should occur further weakens the contribution.
2. Strong convexity assumption is ok, but not that realistic in ML today (where most training is non-convex). The theoretical analysis relies heavily on strong convexity, which limits the applicability of the results. While some empirical testing is done on non-convex problems, the lack of theoretical guarantees in this setting is a significant drawback. The paper needs to either relax the convexity assumptions in the theoretical analysis or provide a more thorough justification for why strong convexity is a reasonable assumption in this context.
3. Empirical testing was on only one smaller dataset, with no relevant baselines (FedAvg is a must to include), and not much improvement is showcased overall (especially when other asynchronous or compression methods can better reduce delay). The empirical evaluation is not sufficiently robust. The use of only one small dataset limits the generalizability of the results. The absence of FedAvg as a baseline, or a comparable decentralized variant, makes it difficult to assess the performance of DSpoFL against established methods. Furthermore, the lack of significant performance improvements, especially when compared to other communication-efficient algorithms, raises concerns about the practical utility of the proposed method.

### Questions
1. How does the limit (sub-optimality gap) that is approached in Equation (9) compare to other classical works like FedAvg (when convex assumptions are used)? This is very important as much of the analysis showcases convergence to a first-order stationary point (FOSP) and not the true optimality gap.
    - If convexity isn't that strong (small $\mu$), then the suboptimality grows inversely $\mathcal{O}(\frac{2}{\mu})$ in Equation (9)
3. Can convergence be shown in the standard FOSP manner with the non-convexity (relaxing convexity assumptions)? 
4. There is no guidance for how to know or select the expected connectivity of links between devices as well as the expected sporadicity of local gradient updates. How should they be selected to optimize training and boost performance? Ablation studies are necessary for studying this phenomena.
5. DSpoFL does not seem to outperform Distributed Gradient Descent (DGD) in raw iteration testing. Comparison against FedAvg is a must since multiple local updates before communication also reduces communication costs and is shown to improve accuracy. DSpoFL should be compared with a range of similar communication-efficient algorithms (and should hopefully outperform them).

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study expands the decentralized SGD method to accommodate sporadic cases in which nodes might randomly omit certain gradient computations or communications during iterations. The primary contribution lies in introducing this method and providing a convergence analysis for the strongly-convex setting.

### Strengths
Modelling and analysis of DSGD with random communication and computation skipping.

### Weaknesses
The idea of this work is incremental, and the literature review seems to omit pivotal and relevant works that address similar issues. Notably:

Srivastava, Kunal, and Angelia Nedic. "Distributed asynchronous constrained stochastic optimization." IEEE journal of selected topics in signal processing 5.4 (2011): 772-790.

Zhao, Xiaochuan, and Ali H. Sayed. "Asynchronous adaptation and learning over networks—Part I: Modeling and stability analysis." IEEE Transactions on Signal Processing 63.4 (2014): 811-826.

Lian, Xiangru, et al. "Asynchronous decentralized parallel stochastic gradient descent." International Conference on Machine Learning. PMLR, 2018.

Wang, Chengcheng, et al. "Coordinate-descent diffusion learning by networked agents." IEEE Transactions on Signal Processing 66.2 (2017): 352-367.

Liu, Wei, Li Chen, and Weidong Wang. "General decentralized federated learning for communication-computation tradeoff." IEEE INFOCOM 2022-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS). IEEE, 2022.

The paper operates under the assumption of strong convexity. Furthermore, the present framework appears incremental and, due to the assumption of uncorrelated random variables, doesn't introduce significant challenges to the analysis. The study doesn't showcase any theoretical advantages achieved through sporadic updates.

The pseudo code for the method should be incorporated into the main text. Clear definitions of the notation are necessary, such as those referenced in equation (3)
There's a lack of clarity and order in presenting equations and notations; they come across as disorganized.
The paper only offers asymptotic rates, neglecting to provide transient rates, especially where the error approaches zero, requiring the stepsize to diminish accordingly.

### Questions
How does the problem parameters influence the convergence bound, and how does this compare to the standard DSGD case? To understand this, we require a bound on $\rho(\Phi)$ that's expressed in terms of the network graph and random probabilities.
Does your analysis highlight any theoretical benefits from using sporadic updates?
I recommend deriving results for the nonconvex scenario and clearly comparing the bounds of the proposed method with those from other studies.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
