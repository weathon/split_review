# Causal Effect Estimation with Mixed Latent Confounders and Post-treatment Variables

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Causal inference from observational data has attracted considerable attention among researchers. One main obstacle to drawing valid causal conclusions is handling of confounders. As the direct measurement of confounders may not always be feasible, recent methods seek to address the confounding bias via proxy variables, i.e., variables postulated to be causally related to unobserved confounders. However, the selected proxies may scramble both latent confounders and latent post-treatment variables in practice, where existing methods risk biasing the estimation by unintentionally controlling for variables affected by the treatment. In this paper, we systematically investigate the bias of latent post-treatment variables, i.e., latent post-treatment bias, in causal effect estimation. We first derive the bias of existing covariate adjustment-based methods when selected proxies scramble both latent confounders and latent post-treatment variables, which we demonstrate can be arbitrarily bad. We then propose a novel Confounder-identifiable VAE (CiVAE) to address the bias. CiVAE is built upon a mild assumption that the prior of latent variables that generate the proxy belongs to a general exponential family with at least one invertible sufficient statistic in the factorized part. Based on this assumption, we show that latent confounders and latent post-treatment variables can be individually identified up to simple bijective transformations. We then prove that with individual identification, the intractable disentanglement problem of latent confounders and post-treatment variables can be transformed to a tractable conditional independence test problem. Finally, we prove that the true causal effects can be unbiasedly estimated with transformed confounders inferred by CiVAE. Experiments on both simulated and real-world datasets demonstrate that CiVAE is significantly more robust to latent post-treatment bias than existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the estimation of treatment effects under the presence of latent confounders and latent post-treatment variables. This is a challenging scenario where conventional methods may yield biased estimates of treatment effects. To correct the bias, this paper proposes a novel method, namely Confounder-identifiable VAE (CiVAE), to estimate treatment effects. The paper provides some theoretical guarantees for the method. Moreover, the paper demonstrates that the proposed method performs well in empirical applications.

### Strengths
- The problem is well-motivated.
- The method seems to work well in empirical applications.
- Figures 1 and 2 are very helpful for understanding the problem setup.

### Weaknesses
 - The real-world dataset used in the empirical study does not seem to be publicly available.
- The paper uses many notations without definition. For example, the definitions of $K_Z$ in footnote 3, $p(X\mid C)$, and the matrix of $p(C, X)$ are missing. It is unclear how $K_Z$ relates to the dimensions of the latent spaces for confounders and post-treatment variables. The lack of a clear definition for $p(X\mid C)$ makes it difficult to understand the conditional independence assumptions. Furthermore, the representation of $p(C, X)$ as a matrix is not standard, and the dimensions of this matrix are unclear, especially given that $C$ and $X$ are likely high-dimensional.
- Section 4 is a bit challenging to follow -- notations are heavy, and the exposition is a bit detail-oriented. Providing some high-level intuitions in this section could be helpful. The theoretical arguments rely on several assumptions that are not clearly stated or justified. For example, the identifiability conditions for the latent variables are not explicitly discussed, and it is unclear how these conditions relate to the practical implementation of the method. The proofs are also quite dense and lack sufficient explanation of the key steps.
- I am not sure why there is always a clear separation between latent confounders and post-treatment variables. It is possible that the value of latent confounders (e.g., health indicators) can be changed by the treatment, and thus, these latent confounders also seem to be post-treatment variables. The paper does not adequately address the scenario where the treatment may influence the latent confounders, which would violate the assumption of strict separation.

### Questions
See Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript proposes CiVAE method to address the risk of conditioning on post-treatment (latent) variables in estimating causal effects, by disentangling the latent unobserved confounders from the latent post-treatment variables. The identification result of CiVAE and identification of latent confounders are shown. The authors also show the empirical results by a simulated data and a real data.

### Strengths
- The authors study a important issue of latent post-treatment bias.
- Pratical algorithm and sound theoretical results are provided under certain conditions. 
- Empirical performance is strong comparing with existing ones.

### Weaknesses
 - Assumption 1 requires $f$ to be injective, which is much stronger than common conditions in the literature, even the dimension of the observation space is larger than dim(C) + dim(M). In many cases, there might be a  latent confounder or post-treatment variable not correlated with $X$. It is suggested to check if the proposed method sensitive to the injective condition.

- The interactions among latent variables might come from other unobserved variables that confound $Z_i$ and $Z_j$, not belonging to three cases in section 4.5.

- How to determine the dimension of Z? How's the different selections of dim(Z) affect your ATE and identification of latent confounders with or without interactions?

- Please fix the typo in equation (8).

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the challenge of handling latent confounders and post-treatment variables. Recent research has attempted to solve this problem by using proxy variables. However, selected proxies may inadvertently combine both confounders and post-treatment variables, potentially introducing bias into estimates. To tackle this, the authors propose a novel method called the Confounder-identifiable Variational Autoencoder (CiVAE) to mitigate this bias.

### Strengths
1.I find the problem they studied intriguing, specifically how proxy attributes may cover both confounders and post-treatment variables. It is crucial to separate these biases throughout the causal effect estimation process.

2. The paper is well-written and theoretically sound, with proofs for all statements provided in the appendix.

3.The core idea is clearly explained and easy to follow. Including a code link improves reproducibility.

### Weaknesses
1. In Figure 2, there is a bi-directional path between M and Y. However, in the following example, M is treated as a strict mediator. Please ensure consistency in the directions of M. Or add more examples to show if the case T->M<-Y happened. In line 269, it states, "However, since both C and M form fork structures with the outcome Y (see Fig. 2-(c))." I am wondering why M forms fork structures.

2. Z is the true latent space (Z = [C, M]). According to the paper, there exists a bi-directional path between M and Y. Could you explain why only p(Z|Y,T) is considered? If T → M → Y, I agree with using p(Z|T); if T → M ← Y, I agree with p(Z|T,Y). I suggest considering different cases using different forms of p(·).

3. More interestingly, if Z also includes C, then is C identifiable? I am wondering if C is treated as a general case in CEVAE without considering identifiability. Even with iVAE, additional information may be missing to guide identifiability.

4. A related work may need to be included. [1] discusses the iVAE learning process of the front-door adjustment set, which is a very similar setting to this paper. I suggest adding a discussion of this in the related work section.

### Questions
See Above.

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
The paper introduces the Confounder-identifiable Variational Autoencoder (CiVAE) to estimate treatment effects in settings where the observed covariates are a function of latent confounders and latent post-treatment variables. The proposed method is designed to disentangle these latent components, and it is provably unbiased under some specific assumptions. Through experiments on both simulated and real-world datasets, the method demonstrates superior performance compared to existing baselines.

### Strengths
- The issue of post-treatment bias is understudied, making this paper a valuable contribution to the field.

- The paper is well-written, which makes it easy to understand the core ideas.

- The empirical validation shows that the method outperforms existing baselines.

### Weaknesses
 - **Main concern**. The method depends on strong and untestable assumptions for identifiability, e.g. the injective mapping described in Assumption 1. Such assumptions may be difficult to verify, even with domain knowledge, and fall short of the causal inference field's emphasis on interpretable and justifiable identification assumptions. Specifically, the requirement that the mapping from the combined latent confounders and post-treatment variables to the observed covariates is injective is a significant constraint. This implies that each unique combination of latent variables must map to a unique observed covariate vector, which is a very strong condition that may not hold in many real-world scenarios. The authors do not provide sufficient justification for why this assumption is reasonable or how to check it in practice.
- **Other concerns**. While post-treatment variables are recognized as an issue, I am skeptic regarding the significance of *latent* post-treatment variables as a problem. The example provided does not clarify why these latent variables pose a significant issue, and I'm uncertain about its practical relevance. It is unclear why the post-treatment variables cannot be directly observed or why they need to be latent. The authors need to provide more compelling examples where latent post-treatment variables are a critical concern for causal inference.
- **Other concerns**. The assumption of independence between latent confounders and latent post-treatment variables (see Fig. 1c) is quite strong and unlikely to hold in any realistic application. This independence assumption is a critical component of the proposed method's identifiability and it is unclear how the method would perform if this assumption is violated. The authors should provide a more detailed discussion of the implications of this assumption and how it might be relaxed in future work.

### Questions
- Could the author provide some examples in the causal inference literature that involve the use of post-treatment proxy variables?  
- Under what circumstances do you expect the injectivity assumption to hold, given that even some simple linear models may fail to satisfy this?
- Can the author share experimental results showing the impact of violating injectivity in Assumption 1?

### Soundness
2

### Presentation
3

### Contribution
2
