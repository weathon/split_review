### Summary

The paper studies a stochastic variant of the deep neural network known as the stochastic neural network (StoNet). The authors show that the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models; establish that the sparse StoNet is consistent in network structure selection; and provides a recursive method to quantify the prediction uncertainty for the Stonet.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper introduces a stochastic neural network (StoNet) and demonstrates its equivalence to a standard deep neural network (DNN). Leveraging this equivalence, the authors establish the consistency of sparse structure selection in DNNs using the Lasso penalty. Additionally, they propose a post-StoNet procedure to quantify the prediction uncertainty of large-scale DNNs.

### Weaknesses

#### Some Related Works


#### comment

1. The introduction of StoNet seems to be unnecessary. The equivalence between DNN and StoNet, as presented in Lemma 1, appears to be the core of the paper, and the subsequent theoretical development is largely based on this result. However, the proof of Lemma 1 is not convincing. The authors state that "the continuous mapping theorem then yields (i)" without specifying the function to which the theorem is applied, the domain, and the codomain. Additionally, the strong law of large numbers is applied without verifying the identically distributed condition.

2. Theorem 1 is the consistency of StoNet. However, the proof of Theorem 1 heavily relies on Liang et al. (2018). It is unclear what the authors' contribution is in this context.

3. Theorem 2 presents a bound for the imputation error of ASGMCMC. However, the bound does not converge to 0 as $t \rightarrow \infty$. Therefore, it does not demonstrate the consistency of the ASGMCMC algorithm.

4. The proof of Corollary 1 is not convincing. The authors claim that "Our proof implies that under Assumptions A1-A6, such a consistent estimator can also be obtained by directly maximizing the penalized likelihood function of the complete data". It is not clear how the consistency of the MLE of complete data is related to the consistency of MLE of DNN (or penalized MLE of DNN).

5. The prediction error bounds presented in Section 4 are not valid. The estimation of $\mu(z,\theta^*)$ uses the estimator $\hat{\theta}$. However, the convergence rate of $\hat{\theta}$ is not taken into account in the bound. As a result, the prediction error bound converges to $-\infty$ as $n \rightarrow \infty$.

6. The paper lacks a comparison with dropout.

7. Theorem 3 is not presented as a formal theorem but rather as a figure caption in the numerical experiment section. The assumptions of Theorem 3 are not specified, and the result is only shown numerically without any proof.

Minor weaknesses:

1. The notations in Section 3.1 are very complicated. For example, $\gamma^{(t)}$ is defined in Equation (A3), but $\gamma^{(t)}_n$ appears in Equation (A4). The subscript $n$ is not explained. Additionally, $\theta^{(t)}_n$ is not defined, yet it is used in Equation (A4).

2. The paper uses the notation $\prec$ without explanation. The same symbol is used in Lemma 1, Theorem 1, and Lemma 3, but it is not clear what it means.

3. The paper states that "the consistency of the maximum likelihood estimator of StoNet can be shown by combining Theorem 1 and Lemma 3." However, Lemma 3 is the consistency of the MAP estimator, not the MLE.

4. The paper states that "it follows from Lemma 1 that a consistent estimator of $\theta$ can also be obtained by directly maximizing the penalized likelihood function of the DNN model." However, the penalized likelihood function of the DNN model is not defined. The noise variance $\sigma^2$ is missing in the likelihood function of DNN model.

5. The paper states that "By Lemma A2, the above procedure can also be applied to the StoNet trained by the adaptive stochastic gradient MCMC algorithm." However, Lemma A2 is the consistency of the ASGMCMC algorithm. It does not imply that the StoNet trained by ASGMCMC satisfies the assumptions of Section 4.

### Suggestions

The paper's core contribution hinges on the equivalence between DNNs and the proposed StoNet, yet the theoretical justification for this equivalence is not sufficiently rigorous. The application of the continuous mapping theorem in the proof of Lemma 1 lacks crucial details, specifically the function being mapped and the relevant spaces. Furthermore, the invocation of the strong law of large numbers fails to address the requirement for identically distributed random variables, which is not obviously satisfied in the context of the proof. These omissions undermine the validity of the equivalence result, which is the foundation for the subsequent theoretical development. The authors should provide a more detailed and rigorous proof, explicitly stating all assumptions and justifying the application of these theorems. Without a solid proof of Lemma 1, the rest of the theoretical results lose their significance.

Furthermore, the paper's claims regarding the consistency of the proposed StoNet and its connection to DNN structure selection require more clarification. While the authors reference Liang et al. (2018) for the consistency of the StoNet, they do not clearly articulate their novel contribution in this context. The consistency of the StoNet is a crucial step in establishing the consistency of DNN structure selection, and the authors need to explicitly state how their work builds upon existing results. Additionally, the proof of Corollary 1, which relates the consistency of the MLE of complete data to the consistency of the MLE of the DNN, is not convincing. The authors need to provide a more detailed explanation of how these two estimators are connected and how the consistency of one implies the consistency of the other. The current explanation is too vague and lacks the necessary technical details to support the claim.

Finally, the prediction error bounds presented in Section 4 are not valid due to the omission of the convergence rate of the estimator $\hat{\theta}$. The authors need to explicitly incorporate the convergence rate of $\hat{\theta}$ into the error bound to ensure that the bound converges to a non-negative value as $n \rightarrow \infty$. The current bound, which converges to $-\infty$, is not mathematically sound and undermines the validity of the theoretical results. The authors should also provide a more detailed explanation of how the prediction error is calculated and how the uncertainty is quantified. The current explanation is too brief and lacks the necessary technical details to support the claims. Additionally, the lack of comparison with dropout, a widely used technique for uncertainty quantification in deep learning, is a significant omission. The authors should include a comparison with dropout to demonstrate the advantages of their proposed method.

### Questions

1. Could you please provide a more detailed proof of Lemma 1, including the specific function for the continuous mapping theorem and a justification for the application of the strong law of large numbers?

2. What is your contribution to the proof of Theorem 1, given that it relies heavily on Liang et al. (2018)?

3. How does the bound in Theorem 2 demonstrate the consistency of the ASGMCMC algorithm as $t \rightarrow \infty$?

4. Could you please provide a more detailed proof of Corollary 1, explaining how the consistency of the MLE of complete data relates to the consistency of the MLE of the DNN model?

5. How does the prediction error bound in Section 4 account for the convergence rate of $\hat{\theta}$?

6. Could you please compare your method with dropout for uncertainty quantification?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
