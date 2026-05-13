# Unlocking Trilevel Learning with Level-Wise Zeroth Order Constraints: Distributed Algorithms and Provable Non-Asymptotic Convergence

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Trilevel learning (TLL) found diverse applications in numerous machine learning applications, ranging from robust hyperparameter optimization to domain adaptation. However, existing researches primarily focus on scenarios where TLL can be addressed with first order information available at each level, which is inadequate in many situations involving zeroth order constraints, such as when black-box models are employed. Moreover, in trilevel learning, data may be distributed across various nodes, necessitating strategies to address TLL problems without centralizing data on servers to uphold data privacy. To this end, an effective distributed trilevel zeroth order learning framework DTZO is proposed in this work to address the TLL problems with level-wise zeroth order constraints in a distributed manner. The proposed DTZO is versatile and can be adapted to a wide range of (grey-box) TLL problems with partial zeroth order constraints. In DTZO, the cascaded polynomial approximation can be constructed without relying on gradients or sub-gradients, leveraging a novel cut, i.e., zeroth order cut. Furthermore, we theoretically carry out the non-asymptotic convergence rate analysis for the proposed DTZO in achieving the $\epsilon$-stationary point. Extensive experiments have been conducted to demonstrate and validate the superior performance of the proposed DTZO, e.g., it approximately achieves up to a 40$\%$ improvement in performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose a distributed trilevel zeroth-order (DTZO) algorithm to address the trilevel optimization problem (TLL) when gradients or subgradients of level objectives (functions) are not available. They first reformulate the inner and outer layer constraints as feasible regions approximated by polynomials which are constructed using zeroth order cuts. These  zero order cuts, corresponding polynomial approximations and local variables are updated at each iteration of the algorithm. The method is implemented in the distributed manner. It is supported by a theoretical analysis of iteration and communication complexities, and experimental evaluation in the tasks related to large language models and robust hyperparameter optimization.

### Strengths
DTZO is the first algorithm designed to solve trilevel optimization (TLL) problems in distributed settings without requiring gradients or subgradients of level objectives (functions). The authors provide a theoretical analysis of the algorithm’s iteration and communication complexities. The method shows good performance in comparison to the chosen baselines​.

### Weaknesses
My major concern is related to the novelty of the DTZO algorithm as it combines the ideas from two previous papers. Indeed, the general structure of the algorithm seems to be borrowed from the recent paper (Jiao et al., 2024). The main difference is that the authors do not use gradients of functions, which are unavailable, but well-known approximations to them, following (S. Ghadimi and G. Lan, 2013). However, this modification does not seem very significant for me.


Moreover, I have concerns regarding the theoretical results. To prove the main of them, i.e., Theorem 1,2, the authors introduce $\mu$-smooth approximation of the final objective functional $F$. Then, similar to (Jiao et al., 2024), the authors conduct the convergence rate analysis using this approximation. However, there is no theoretical result showing how close the solutions of this $F_{\mu}$ approximation are to those of the objective functional $F$? Without such a result, the convergence rate for $F$ seems to be still an open question. I will appreciate it if the authors provide some comments on this topic.

My minor comments are related to the comparison with the baselines in the numerical experiments. The authors tested the approach in the tasks related to LLM and hyperparameters robust optimization and compare its performance with several baseline models, e.g., FEDZOO (Fang et al., 2022) and  FEDRZO$_{bl}$ (Qiu et al., 2023). Both of these algorithms provide the results for MSE or Loss vs iteration number and communication round, it would be great if the authors provide this kind of result too.

*Minor*: 
line 328: equation number (16) is missing

### Questions
- Can you comment on the connection between the solutions of $F$ and its $\mu$-smooth approximation $F_{\mu}$? Are they $\epsilon$-close to each other?
- I noticed that the zeroth-order gradient estimation method used here is based on (Ghadimi and Lan, 2013). Could you explain why you choose this method over the approach in (Liu et al., 2020), which utilizes mini-batch sampling to reduce variance?

**References.**
1. Jiao, Yang, et al. "Provably Convergent Federated Trilevel Learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 11. 2024.

2. Qiu, Yuyang, Uday Shanbhag, and Farzad Yousefian. "Zeroth-order methods for nondifferentiable, nonconvex, and hierarchical federated optimization." Advances in Neural Information Processing Systems 36 (2023).

3. Liu, Sijia, et al. "A primer on zeroth-order optimization in signal processing and machine learning: Principals, recent advances, and applications." IEEE Signal Processing Magazine 37.5 (2020): 43-54.

4. Ghadimi, Saeed, and Guanghui Lan. "Stochastic first-and zeroth-order methods for nonconvex stochastic programming." SIAM journal on optimization 23.4 (2013): 2341-2368.

5. W. Fang, Z. Yu, Y. Jiang, Y. Shi, C. N. Jones, and Y. Zhou. Communication-efficient stochastic zeroth-order optimization for federated learning. IEEE Transactions on Signal Processing, 70, 2022

6. Y. Qiu, U. Shanbhag, and F. Yousefian. Zeroth-order methods for nondifferentiable, nonconvex, and hierarchical federated optimization. Advances in Neural Information Processing Systems, 36, 2023.

### Soundness
2

### Presentation
3

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
This paper studies distributed trilevel optimization problem with zeroth-order constraints. It develops an algorithm based on the cutting plane method and provides its convergence rate. Moreover, the experiment validates its performance.

### Strengths
1. The trilevel optimization problem is interesting, which is less studied. 

2. This paper proposes a feasible approach to solve the trilevel optimization problem.

### Weaknesses
1. The proposed method is based on the cutting plane method. However, no background knowledge about cutting plane is provided. I suggest the author to provide some fundamental information about it. Otherwise, it is difficult for the reviewer to follow the proposed method. 

2. The proposed method converts a trilevel problem to an unconstrained problem. However, the solution landscape could be different. How does the approximated solution differ from the original solution? It's better to provide some theoretical analysis for this difference. 

3. For the cutting plane method, how to determine $a$, $b$, $c$, and $d$? How do they affect the convergence rate?

4. For the penalty coefficient $\lambda$, how does it affect the convergence? 

5. In the experiment, $a$, $b$, $c$, $d$, and $\lambda$ are not stated clearly. What values are used in experiments?

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes DTZO, a novel framework that utilizes zeroth order constraints to solve distributed trilevel learning problems. Unlike existing approaches that rely on first-order information for trilevel learning or previous single-level and bilevel zeroth-order methods, DTZO leverages zeroth-order optimization to address the unique challenges of trilevel structures. Experimental results demonstrate the superior performance of DTZO, establishing it as an effective alternative for trilevel learning problems.

### Strengths
1. DTZO provides a novel perspective for solving distributed trilevel learning problems by incorporating zeroth-order constraints, distinguishing it from traditional first-order-based trilevel learning approaches.
2. The paper provides a rigorous theoretical analysis of DTZO, specifically addressing its non-asymptotic convergence rate, which strengthens the framework’s validity and offers insights into its efficiency.

### Weaknesses
1. While the paper includes a theoretical analysis of DTZO’s non-asymptotic convergence rate, there are no experimental results to analyze this, such as a convergence analysis based on testing loss. Including such results would help validate the theoretical findings empirically.
2. In the experimental section, the paper employs black-box large language models (LLMs) to achieve DTZO. Although the introduction section mentions the importance of zeroth-order constraints when first-order information is unavailable in black-box LLMs, further elaboration on scenarios where first-order information is inaccessible would enhance readers’ understanding of the choice to use black-box LLMs in these experiments.
3. The paper lacks detailed hyperparameter analysis results in the main body, specifically on the effect of parameters like the iteration interval $\mathcal{T}$. Providing these insights would give readers a more comprehensive understanding of DTZO’s sensitivity to hyperparameter settings.

### Questions
1. While the paper presents a theoretical analysis of DTZO’s non-asymptotic convergence rate, could additional experimental results, such as a convergence analysis based on testing loss, be included to empirically validate these theoretical findings?
2. In the experimental section, black-box large language models (LLMs) are used to implement DTZO. Could the authors further elaborate on practical scenarios where first-order information is inaccessible, to clarify the rationale behind using black-box LLMs for these experiments?
3. Could the paper provide a more detailed analysis of hyperparameters in the main body, particularly regarding the impact of parameters like the iteration interval $\mathcal{T}$, to offer readers a better understanding of DTZO’s sensitivity to these settings?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studied the trilevel learning with level-wise zeroth-order constraints in the distributed setting, and proposed a distributed trilevel zeroth-order method. It provided the non-asymptotic convergence analysis of the proposed method. It also provided some experimental results on the proposed method.

### Strengths
This paper proposed a distributed trilevel zeroth-order method. It provided the non-asymptotic convergence analysis of the proposed method. It also provided some experimental results on the proposed method.

### Weaknesses
This paper is very poorly written. For example, the problem (1) in the paper, the authors do not distinguish between the optimal variables $x^*_1$, $x^*_2$ , $x^*_3$ and the variables $x_1$, $x_2$ , $x_3$. Under this case, the proposed algorithm and the provided convergence results are confusing. They may be wrong. 

From algorithm 1 of this paper, the proposed algorithm basically combines the existing algorithms with the existing zeroth-order gradient estimators. There do not exist any novelty in the proposed algorithm. Meanwhile, the convergence analysis mainly follows the exiting results.


Assumption 1 in the convergence analysis is very strict. Under this assumption, the contribution of the provided convergence analysis is very limited. Meanwhile, the convergence results can not provide any useful information to verify the specific properties of the proposed method. 

In the numerical experiments, many comparisons are missing. For example, many federated bilevel methods should be compared in the numerical experiments. Why the authors only provided two single-level federated methods.

### Questions
Please see the above weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
