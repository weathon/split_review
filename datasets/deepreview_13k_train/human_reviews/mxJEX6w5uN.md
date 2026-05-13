# Scaff-PD: Communication Efficient Fair and Robust Federated Learning

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
\noindent
We present {\algname}, a fast and communication-efficient algorithm for distributionally robust federated learning. Our approach improves fairness by optimizing a family of distributionally robust objectives tailored to heterogeneous clients. We leverage the special structure of these objectives, and design an accelerated primal dual (APD) algorithm which uses bias corrected local steps (as in {\sc Scaffold}) to achieve significant gains in communication efficiency and convergence speed. We evaluate {\algname} on several benchmark datasets and demonstrate its effectiveness in improving fairness and robustness while maintaining competitive accuracy. Our results suggest that {\algname} is a promising approach for federated learning in resource-constrained and heterogeneous settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors presented a new algorithm for federated learning in heterogeneous setup. The main idea of their approach is based on three things: distributionally robust objective problem (the appropriate reformulation of the problem), application of Prima-Dual Hybrid Gradient Method (PDHG) and Scaffold algorithm to make the method with local updates. The authors provide both convergence guarantee for strongly convex-concave and strongly convex-strongly concave cases. The experimental results show the effectiveness of the method.

### Strengths
1. The new method solves the DRO problem in saddle-point reformulation.
2. The combination of two technique tackle the issue related to data heterogeneity. 
3. SCAFF-DP achieves better rates than previous methods and the experiments support this.

### Weaknesses
1. The first thing is related to the paragraph about choosing $\psi$ and $\Lambda$. From the convergence analysis, $\Lambda$ is a bounded set. However, there is no discussion about the specific constraints or structure of this set in the main part, which is crucial for understanding the practical implications of the method. The authors should clarify how the choice of $\Lambda$ affects the performance and robustness of the algorithm, especially in heterogeneous settings.
2. In the main part there is no expression for local stepsize. The absence of a clear definition for the local stepsize $\eta_{\ell}$ makes it difficult to reproduce the results and understand the practical implementation of the algorithm. The authors should provide an explicit formula for $\eta_{\ell}$ in the main part of the paper, detailing how it relates to the global learning rate and the number of local steps.
3. The formulation of Theorem 5.5 is not full. There is no word about the smoothness of function $f$. The smoothness assumption is critical for the convergence analysis, and its omission makes the theorem incomplete. The authors should explicitly state the smoothness conditions required for the function $f$ in the theorem statement.
4. It is good that the authors compare Proxskip and SCAFF-PD theoretically, however, there are a lot of new algorithms of 5th generation of local methods (see some of them here in the literature review https://arxiv.org/pdf/2302.09832.pdf). Better to say some words about them and compare. Another interesting thing is related to ProxSkip for variational inequalities (see https://openreview.net/forum?id=ct_s9E1saB1). There is no comparison between SCAFF-PD and this algorithm. The lack of comparison with other state-of-the-art methods, particularly those designed for variational inequalities, limits the understanding of the relative advantages and disadvantages of the proposed method. A more comprehensive comparison is needed to position the contribution of this work within the broader landscape of federated learning algorithms.
5. In the experiments, there is no comparison between the performances of SCAFF-PD and ProxSkip. The absence of experimental comparison with ProxSkip, which is theoretically compared, makes it difficult to validate the practical performance of SCAFF-PD against a relevant baseline.

### Questions
1. Could you explain whether your proposed method has a speed up related to number of clients and number of local steps, which is observed for SCAFFOLD? 
2. Please, add explanation for derivation of eq. (B.59) from eq.(B.57)

typos:
1.  In (A.1) one of $z$ in the last term have to be $x$.
2. in the first sentence of proof of Lemma A.4, probably, there is no need $4$ in denominator. 
3. In the next sentence after eq. (B.17) in the formula for $\tau_r$, there is an extra bracket.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce SCAFF-PD, which enhances fairness by optimizing distributionally robust objectives customized for diverse clients. They then employ an accelerated primal-dual (APD) algorithm with bias-corrected local steps, similar to SCAFFOLD, to improve communication efficiency and convergence speed.

### Strengths
1. This paper is easy to follow.
2. Building upon the foundation of SCAFFOLD, a new algorithm is developed for addressing distributionally robust federated objectives, and its convergence rate is rigorously derived.

### Weaknesses
1. The algorithm design and theoretical analysis rely on SCAFFOLD, encompassing the hypothesis and proof framework. This extensive reliance on prior work may potentially diminish the originality and contribution of the proposed method in this paper.
2. A notable issue arises in the algorithm design, as it necessitates two times of communications with nodes at each round, transmitting distinct content. This introduces a huge communication overhead. Additionally, contradictory to the federated context where nodes may join or leave the network at any time, the proposed algorithm must consistently maintain a stable participation at every round. This operational requirement may pose challenges to the practical applicability of the proposed algorithm.
3. The comparative analysis is limited by the inclusion of a small number of old methods.

### Questions
Please clarify the reason to claim that the proposed method is communication-efficient, while the algorithm introduces additional communication overhead.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a communication efficient fair and robust federated learning algorithm. The communication efficiency is achieved by performing multiple updates at local agents before the central server performing the aggregation with a gradient extrapolation step that achieves the similar effect as Nesterov's acceleration. Fairness of the DRO problem is achieved by incorporating a set of weights to different agents that are subject to a constrained set and can be regularized through the design of the regularization function. Experiments on synthetic and real datasets to prove the communication efficiency and model performance are provided. Theoretical analysis in terms of convergence is also conducted.

### Strengths
The problem that is studied is of interest to the federated learning community. The developed algorithm also seems to be able to achieve the desired objective in terms of the experimental performance.

### Weaknesses
The technical proof part is not rigorous enough. More details will be provided below. There are a couple of typos and unclear definitions, will also be provided below.

Major comments:
1. What is $\bar{\tau}$ in Condition 5.1 and how do you set $\gamma_0$?
2. Lemma B.2 is wrong and the proof is also wrong, which leads to the soundness of Theorem B.6 and Theorem 5.1. Specifically, 
to prove 
\begin{equation}
t_r(\frac{1}{\tau_r}+ \mu_{\boldsymbol{x}}) \geq \frac{t_{r+1}}{\tau_{r+1}},
 \end{equation}
we should not start from rewritting this equation, which already assumes that this inequality is correct. The procedure I did is shown below:
\begin{equation}
t_r(\frac{1}{\tau_r}+ \mu_{\boldsymbol{x}}) =\frac{t_r}{\tau_r} (1+ \mu_{\boldsymbol{x}}{\tau_r}) = \frac{t_r}{\tau_r} \frac{\gamma_{r+1}}{\gamma_r}  = \frac{\sigma_r}{\sigma_0\tau_r} \frac{\gamma_{r+1}}{\gamma_r}  = \frac{\sigma_r}{\sigma_0\tau_r} \frac{\sigma_{r+1}/\tau_{r+1}}{\sigma_r/\tau_r}   = \frac{\sigma_{r+1}/\tau_{r+1}}{\sigma_0} =  \frac{t_{r+1}}{\tau_{r+1}}.
 \end{equation}
That means there is no greater than or equal to relationship, the two sides always equal to each other. Meanwhile, $\frac{t_r}{\sigma_r} = \frac{t_{r+1}}{\sigma_{r+1}}$.

3. From the assumptions and the definition of all symbols, I recognized that $\tau_r = J\eta_l\eta_g$, which indicates that $\tau_{r+1} = J\eta_l\eta_g$, too, if I did not miss anything. That means, for equation B.38, with $\frac{t_r}{t_r+1} = \theta_r$, we must have $V_{r+1}\leq \theta_{r+1}Z_{r+1}$, which however, is based on the condition that $\theta_{r+1}>1$. However, $\theta_{r+1} = \frac{\sigma_r}{\sigma_{r+1}} = \frac{\gamma_r\tau_r}{\gamma_{r+1}\tau_{r+1}} = \frac{\tau_r}{(1+ \mu_{\boldsymbol{x}}\tau_r)\tau_{r+1}} = \frac{1}{1+ \mu_{\boldsymbol{x}}{\tau_r}}<1$, which contradicts the assumption, which leads to me doubt about the soundness of the theorems. Please correct me if I am wrong.

4. The experiments on synthetic and real datasets seem contradict each other. For example, Figure 2 shows that larger $\rho$ leads to higher convergence rate while Figure 3 as well as in the analysis says “Meanwhile, the experimental results suggest that smaller $\rho$ leads to faster convergence w.r.t. worst-20% accuracy for our algorithm.” Which one is correct and why larger/smaller $\rho$ leads to faster convergence?

I am willing to discuss and change my rating if my comments can be addressed. 

Minor comments:
1. Page 4, the line before equation (3.2), "iFor" ==> "For".
2. Page 5, "The extrapolation step used in Eq. (4.1) is to Nesterov’s acceleration (Nesterov, 2003)" ==> "The
extrapolation step used in Eq. (4.1) is $\textbf{similar}$ to Nesterov’s acceleration (Nesterov, 2003)".
3. Page 6, "We first introduce how to $\textbf{choice}$ the parameters for SCAFF-PD $\textbf{in when is}$ convex and {fi}i2[N]
are strongly convex in Condition 5.1.", some words seem missing.
4. First paragraph in Section 6, “After conducting thorough evaluations, we have observed that our proposed accelerated $\textbf{algorithms achieve}$ fast convergence rates and strong empirical performance on real-world datasets.” “After conducting thorough evaluations, we have observed that our proposed accelerated $\textbf{algorithm achieves}$ fast convergence rates and strong empirical performance on real-world datasets.”
5. Section 6.1, “we generate $y_i^i$ as $y^i_i = <\boldsymbol{a}_i^j, \hat{\boldsymbol{x}}+\delta_i^{\boldsymbol{x}}>$ “ ==>“we generate $y_i^i$ as $y^i_i = <\boldsymbol{a}_i^j, \hat{\boldsymbol{x}}>+\delta_i^{\boldsymbol{x}}$.
6. Page 8, “$\textbf{beside}$ the average classification accuracy across clients, we also evaluate the worst-20% accuracy1 for comparing fairness and robustness of different federated learning algorithms.” == > “$\textbf{besides}$ the average classification accuracy across clients, we also evaluate the worst-20% accuracy1 for comparing fairness and robustness of different federated learning algorithms.”
7. In table 3 in Appendix C.4, the leftmost column should be CIFAR-10 instead of CIFAR-100.

### Questions
1. In equation (3.1), what is the range of each $\lambda_i$? Is there any constraints on all $\lambda_i$'s, for example, does $\sum_i \lambda_i =1$?
2. What is the definition of $\Delta$ in equation (3.3)?
3. What is the definition of $D(\boldsymbol{\lambda}, \boldsymbol{\lambda}^r)$ in equation (4.2)?
4. Corollary 5.2, what is the definition of $\epsilon$?
5. What is the definition of $L_{xx}$ in equation (5.3)?
6. In the Introduction part, you use $T$ to indicates the convergence while in the theorems presented, you use $R$. Shouldn’t those be consistent?
7. For figure 2, how is the local update iteration $J$ chosen?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studied a distributionally robust federated learning problem, where the problem tries to improve the fairness among clients by optimizing a class of distributionally robust objective functions plus a regularizer that aims to keep the weights $\lambda$ not far from the average weights. The resulting problem now becomes a min-max problem, where the max is take over weights within a prior constraint set $\Gamma$ and the min is taken over the model parameters $x$ to minimize the weighted loss across all clients. The regularizer is chosen to be the penalty from Levy et al., 2020. The authors propose an accelerated primal-duel federated method using some tools from the variance-reduction idea in SCAFFOLD as well as an extrapolation step for acceleration. In theory, the authors characterize the convergence rate for the proposed method for the strongly-convex-concave and strongly-convex-strongly-concave geometry, which matches with centralized version under certain conditions. Experiments are provided to demonstrate the effectiveness of the method.

### Strengths
1.	The work is well written. Distributionally robust objectives in FL are important to achieve certain-level fairness by optimizing the worst-case distribution over clients rather than their simple average. The formulated problem is easy to following and well structured. 

2.	The proposed algorithms incorporate several ideas in the primal-duel designs and the theory shows some improvements.

### Weaknesses
1.	The formulation seems not to be quite new given existing studies. Although the authors show that their formulation is a generalization of existing ones, directly applying the distributionally robust objective (i.e., client weights optimized over a set of candidate distribution) is not new. The $\Phi$ regularizer seems not to add too much new things into the formulation as well. In sum, although the formulation is general, the idea and individual components are not new. 

2.	The algorithms do not incorporate many new stuffs. For example, the SCAFFORD bias correction, the extrapolated step for min-max acceleration have been well studied. The proposed algorithm seems to apply to the general federated min-max problem. However, since the DRO-FL problem has its special structure, i.e., $\lambda$ is linear in the first part of the total objective and the regularizer may still have some benign and dedicated structure in terms of $\lambda$. It may be more interesting to explore such architecture to get better results rather than in the worst-case setting of federated minmax case. In sum, the developed algorithms are not existing enough. 

3.	Theory is not strong. The analysis is only conducted for strongly-convex-(strongly)-concave settings, while most practical examples work under the nonconvex setting. In addition, there are quite a few works on general federated nonconvex-concave/PL/strong-concave setting (see https://arxiv.org/abs/2302.04249 and related works therein). It would be great to discuss why only strongly-convex-(strongly)-concave settings are studied here. Again, the analysis is mainly developed for general case without taking the DRO min-max structure into account. 

4.	Experiments can be made more convincing. The improvements in Table 1 are not that significant. In some cases, the worst-20% results are improved with too much loss in average accuracy. For example, for $\alpha=0.1$, worst-20% increases from 29.5 to 29.78, but the average accuracy drops from 46.11 to 41.23.

### Questions
Overall, I think this is a very important problem but the algorithms, analysis and experiments are not novel and convincing enough. Thus, I give a weak reject but open to increase given the feedback and others’ comments. My questions can be found in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
