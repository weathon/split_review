# Change Point Detection via Variational Time-Varying Hidden Markov Model

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
The task of modeling time series data that exhibit sudden regime shifts has been an enduring focus of research due to its inherent complexity. Among the various strategies to tackle this issue, the Hidden Markov Model (HMM) has been extensively investigated, which captures the regime changes by modeling the transition between latent states. Despite its popularity, the HMM-based methodology carries certain limitations, including specific distribution assumptions and its computational intensity for inference and learning, particularly when the number of change points is unidentified. In this work, we propose a novel approach that models the location of change points and introduce the $\textbf{TV-HMM}$, a variant of the Hidden Markov Model incorporating the time-varying location transition matrix. Based on the novel modeling scheme, we propose an associated variational EM algorithm that simultaneously detects the locations and the number of change points, together with inferring the posterior distributions of regime parameters. In contrast to previous approaches, the proposed method exhibits robustness against the misspecification of change point numbers and can be augmented with stochastic approximation techniques to effectively mitigate the computational burden. Furthermore, we establish the statistical consistency of the change point location estimation under the Gaussian likelihood assumption. We also generalize the parametric likelihood function using the Maximum Mean Discrepancy (MMD) and propose the semi-parametric $\textbf{TV-HMM}$ that is free of distribution assumptions. A series of experiments validate the theoretical convergence rate and demonstrate our estimation accuracy in terms of Rand index and MSE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses modeling time series data with sudden regime shifts, noting the limitations of the widely-used Hidden Markov Model (HMM). Introducing the TV-HMM, a variation with a time-varying location transition matrix, the authors offer a novel variational EM algorithm that pinpoints change point locations and quantities. This method remains robust against misidentification of change point numbers and has optimized computational efficiency. Statistical consistency under the Gaussian likelihood is assured, and a semi-parametric TV-HMM, free from distribution constraints, is also proposed.

### Strengths
1. The proposed variational EM algorithm is designed to be resilient against misidentification of change point numbers, and through the integration of stochastic approximation techniques, the paper addresses the computational intensity traditionally associated with HMMs.

2. The paper not only ensures the statistical consistency of change point location estimation under the Gaussian likelihood but also broadens its application by introducing a semi-parametric TV-HMM, which operates without stringent distribution assumptions, enhancing its adaptability to diverse data sets.

### Weaknesses
1. While the paper does propose a semi-parametric model free from stringent distribution assumptions, a significant portion of the study, including the assurance of statistical consistency, is still based on the Gaussian likelihood assumption, which may not always be applicable in real-world scenarios. This reliance on the Gaussian assumption limits the practical applicability of the theoretical results, especially when dealing with non-Gaussian time series data, where the performance of the proposed method may degrade significantly. The paper does not provide a thorough analysis of the robustness of the method to deviations from this assumption. 

2. No improvement with respect to competitors. The simulation studies presented do not demonstrate a clear advantage of the proposed TV-HMM over existing methods. The lack of a substantial performance improvement raises questions about the practical significance of the proposed approach. Furthermore, the paper does not explore scenarios where the proposed method might offer a clear advantage, such as in situations with specific types of regime shifts or noise characteristics.

### Questions
1. A clear discussion about the assumptions would be helpful. 

2. Is assumption 2 strong with respect to literature? 

3. The simulation study does not show an improvement. I think it would be helpful to see a more substantial improvement.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the change point detection problem with a time-varying hidden Markov model. The authors develop a variational inference algorithm for parameter estimation as well as a semi-parametric extension using the Maximum Mean Discrepancy (MMD).

### Strengths
1. The model formulation is natural for the change point detection problem.
2. The authors generalize the log-likelihood based estimation with MMD to achieve improved robustness against model misspecification and outliers.
3. Theoretical guarantees are provided for the consistency of parameter estimation.

### Weaknesses
1. Placing the ARD prior on the elements of the transition matrix \Pi does not seem to be correct. How does this guarantee that the elements are nonnegative and add up to one? Typically, a Dirichlet prior is used which also induces sparsity. How does the proposed method perform compared to a Dirichlet prior?
2. Similarly the number of change points is determined by examining the posterior of the transition matrix. This also suffers from the issue above.
3. Is the left-to-right Markov chain assumption necessary? There could be identical regimes and the HMM can switch to a previously observed regime. 
4. The authors adopted a SGD-type update for the posterior, e.g., line 8 of Algorithm 1. The update does not respect the sum to one constraint for the transition matrix.

### Questions
- How is the transition matrix posterior updated with the ARD prior? Specifically, why line 8. of Algorithm 1 ensures that the updated estimates are in a simplex?
- How does the proposed method perform compared to using Dirichlet priors on \Pi?
Minor:
\tau is used to denote change points (Sec 2) and also the step size in Algorithm 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a change point detection approach based on a time-varying Hidden Markov Model. The paper introduces a Hidden Markov Model with a time-varying location transition matrix and a corresponding inference method for this model based on variational expectation maximization (EM). The aim of the proposed method is the ability to deal with an undefined number of change points and, therefore, robustness against a mis specified number of change points. Furthermore, stochastic approximation allows to ease computation burden. Finally, the proposed approach operates within the common piece-wise i.i.d. setting and does not necessarily assume Gaussian likelihood.

### Strengths
The benefits of the approach are in its flexibility, in particular, the ability to learn the number of change points and flexibility in terms of likelihood specification.

### Weaknesses
Overall, the paper still needs improvement in clarity and more convincing experimental setup, which clearly shows in which situations the proposed approach would be preferred over existing methods and how it compares to other approaches in terms of computational speed.

Detailed comments:
- At times, writing is not always clear. For example, it is unclear what is the role of section 4 in the paper as there is no experimental evaluation of this extension. There are quite a few typos.

- With the current details, I would struggle to implement the method and reproduce the results of the paper. I would suggest writing an additional section with implementation details, which ensures reproducibility.

- The experimental setup is limited. In particular, the simulation study includes equally spaced change points, which is quite simplistic.

- There is no computational comparison between the methods, and therefore, it is unclear how much one has to sacrifice in terms of speed to gain a little extra performance.

- There are somewhat marginal differences in the performance between the proposed approach and other methods (both when the proposed approach underperforms and overperforms). From the current evaluation, it is unclear in what scenarios it would be beneficial to use the proposed method.

- Table 1 lacks standard deviations over the 100 runs.

- Some references do not include journal information or arxiv identifier.

- Figures are sometimes missing labels and captions of the figures/tables are not self-contained.

### Questions
Detailed comments:
-	At times, writing is not always clear. For example, it is unclear what is the role of section 4 in the paper as there is no experimental evaluation of this extension. There are quite a few typos. 

-	With the current details, I would struggle to implement the method and reproduce the results of the paper. I would suggest writing an additional section with implementation details, which ensures reproducibility. 

-	The experimental setup is limited. In particular, the simulation study includes equally spaced change points, which is quite simplistic. 

-	There is no computational comparison between the methods, and therefore, it is unclear how much one has to sacrifice in terms of speed to gain a little extra performance. 

-	There are somewhat marginal differences in the performance between the proposed approach and other methods (both when the proposed approach underperforms and overperforms). From the current evaluation, it is unclear in what scenarios it would be beneficial to use the proposed method. 

-	Table 1 lacks standard deviations over the 100 runs. 

-	Some references do not include journal information or arxiv identifier. 

- Figures are sometimes missing labels and captions of the figures/tables are not self-contained.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of change point detection in the offline setting. While a large span of previous methods rely on Hidden Markov Models, the authors introduce TV-HMM, a variant of the Hidden Markov Model incorporating the time-varying location transition matrix. An EM-based algorithm is proposed for inference with theoretical guarantees. The TV-HMM model is shown to lead to more robust results compared to standard HMMs and is better suited when the number of change points is not known.

An extension of the TV-HMM model to a semi-parametric setting is proposed, getting rid of the usual restrictive distribution assumptions.

### Strengths
- The authors propose a different viewpoint on the change point detection problem. As far as I know, their approach is new and allows to obtain more robust results compared to standard methods when the number of change points is not known.

- The authors compare their approach with other benchmark methods and show the good performance and the robustness of their method.

- The authors propose an interesting extension of their model to bypass the restrictive parametric assumption on the distribution of the observations.

### Weaknesses
 - The current version contains a few typographical errors and some notational issues, which make it somewhat challenging to read.

- It seems that the results and details of the simulations corresponding to Section 4 (the semi-paramteric model) are not given in the paper. (In particular, I would have been curious to know how the author select the mapping $\phi$ in their simulations.)

- A more detailed comparison with other methods (particularly in terms of computer complexity) would have been useful.

- There is a typo in the use of the notation $M_{K+1}$. For example, in the first bullet point of Assumption A3, it should be $t_i\in \{1,\dots, M_{k+1}-1\}$. (Let me point out that $M_k$ for $k\neq K+1$ have not been defined and I think that they should not be used anyway). The same holds for the second bullet point of assumption A3, Theorem 1, Figure 1 and Section C of the Appendix.

- In Section 4, the use of the notation $\theta_k$ is confusing. Indeed, before section 4, we work in the full parametric case and $\theta_k=(u_k,\Lambda_k)$ (the parameter of the Gaussian distribution from which points are independently sampled from after the $k$-th change point). However, $\theta_k$ in Section 4 needs to be a vector in $\mathbb R^D$ (i.e. in the same space as the observations). Therefore, it might be good to use another notation or to stress at the beginning of Section 4 the properties of $\theta_k$.

- In Eq.(4), the parameters $\pi_{k,m,n}$ are still considered but the update from line 8 (Algo 1) is not presented anymore in Algo 2. I would be grateful if the authors could clarify this point.

- Below Algorithm 2, there should not be a final point: "Unlike Equation 2 in the parametric model, where $Q(\theta)$ must be derived using variational inference. Here, $Q(\theta)$ can be generally modeled using non-parametric density estimation...". Furthermore, using "must" suggests that no alternative can be considered. However, I would say that standard MCMC techniques could be used instead of variational inference. If the authors agree, I would suggest to reformulate the sentence. In the second sentence, it is also mention that $Q$ can be modeled using non parametric techniques, but the following sentence (and the presented algorithm) only deal with a parametric distribution (with parameter $\Phi$). It might be good to mention how the algorithm is changed when a non-parametric density estimation method is used.

- To be consistent with the notations introduced in sections 2 and 3, should $K$ in Algorithm 2 be replaced by $\tilde K$ (since $K$ is the true and unknown number of change points) ?

- In Section 4, "from MMD-based message passing of Equaton 4..." : it should be "Equation".

- The paper lacks a discussion on the practical implications of the proposed method. While the theoretical framework is well-developed, it would be beneficial to include a section discussing the applicability of the method to real-world datasets and the potential challenges that might arise. For example, how does the method perform with noisy or high-dimensional data?

### Questions
I thank the authors for this nice submission. Some of my questions are already listed in the previous sections. My others questions/comments (including some typos) are presented below. 

- I appreciate the discussion on computational complexity at the end of Section 2.2. Nevertheless, I would have been interested to see in the paper a more detailed discussion about the computational complexity of the algorithm (in terms of time and space) compared to others approaches.

- A closing parenthesis is missing at page 4 in the E-step equation. Same in the first line of Eq.(2). 

- In assumption A1, I think in the Gaussian distribution $S_k$ should be $\Lambda_k$ (to be consistent with the notations used in Eq.(1)).

- There is a typo in the use of the notation $M_{K+1}$. For example, in the first bullet point of Assumption A3, it should be $t_i\in \{1,\dots, M_{k+1}-1\}$. (Let me point out that $M_k$ for $k\neq K+1$ have not been defined and I think that they should not be used anyway). The same holds for the second bullet point of assumption A3, Theorem 1, Figure 1 and Section C of the Appendix.

- In Section 4, the use of the notation $\theta_k$ is confusing. Indeed, before section 4, we work in the full parametric case and $\theta_k=(u_k,\Lambda_k)$ (the parameter of the Gaussian distribution from which points are independently sampled from after the $k$-th change point). However, $\theta_k$ in Section 4 needs to be a vector in $\mathbb R^D$ (i.e. in the same space as the observations). Therefore, it might be good to use another notation or to stress at the beginning of Section 4 the properties of $\theta_k$.

- In Eq.(4), the parameters $\pi_{k,m,n}$ are still considered but the update from line 8 (Algo 1) is not presented anymore in Algo 2. I would be grateful if the authors could clarify this point.

- Below Algorithm 2, there should not be a final point: "Unlike Equation 2 in the parametric model, where $Q(\theta)$ must be derived using variational inference. Here, $Q(\theta)$ can be generally modeled using non-parametric density estimation...". Furthermore, using "must" suggests that no alternative can be considered. However, I would say that standard MCMC techniques could be used instead of variational inference. If the authors agree, I would suggest to reformulate the sentence. In the second sentence, it is also mention that $Q$ can be modeled using non parametric techniques, but the following sentence (and the presented algorithm) only deal with a parametric distribution (with parameter $\Phi$). It might be good to mention how the algorithm is changed when a non-parametric density estimation method is used. 

- To be consistent with the notations introduced in sections 2 and 3, should $K$ in Algorithm 2 be replaced by $\tilde K$ (since $K$ is the true and unknown number of change points) ?

- In Section 4, "from MMD-based message passing of Equaton 4..." : it should be "Equation".

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
