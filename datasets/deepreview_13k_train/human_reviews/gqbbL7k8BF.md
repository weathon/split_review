# A Conditional Independence Test in the Presence of Discretization

- Decision: Accept
- Scores: 6, 8, 5, 6, 3

## Abstract
Testing conditional independence (CI) has many important applications, such as Bayesian network learning and causal discovery. Although several approaches have been developed for learning CI structures for observed variables, those existing methods generally fail to work when the variables of interest can not be directly observed and only discretized values of those variables are available. For example, if $X_1$, $\tilde{X}_2$ and $X_3$ are the observed variables, where $\tilde{X}_2$ is a discretization of the latent variable $X_2$, applying the existing methods to the observations of $X_1$, $\tilde{X}_2$ and $X_3$ would lead to a false conclusion about the underlying CI of variables $X_1$, $X_2$ and $X_3$.
Motivated by this, we propose a CI test specifically designed to accommodate the presence of discretization. To achieve this, a bridge equation and nodewise regression are used to recover the precision coefficients reflecting the conditional dependence of the latent continuous variables under the nonparanormal model. An appropriate test statistic has been proposed, and its asymptotic distribution under the null hypothesis of CI has been derived.
Theoretical analysis, along with empirical validation on various datasets, rigorously demonstrates the effectiveness of our testing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors examine the problem of developing conditional independence (CI) tests when a subset of variables is discretized. This discretization introduces bias into existing CI test methods. They apply the concept of bridge equations to accommodate discretized random variables. Additionally, they demonstrate that the asymptotic distribution of their test under the null hypothesis (conditional independence) is normal and finally evaluate their test empirically.

### Strengths
The problem studied is highly relevant and significant across various fields. 
The theoretical findings and asymptotic analysis provide valuable insights, and the empirical results are promising.

### Weaknesses
The method is developed under the assumption of Gaussianity, which is quite limiting. While the authors argue that this assumption is not restrictive, the reliance on correlation measures (covariance and precision matrices) is a significant concern. These measures are only sufficient to characterize dependency and independence structures in the specific case of multivariate normal distributions. This means that the theoretical guarantees of the proposed method are only valid under this restrictive assumption, and the method's behavior in non-Gaussian settings is not theoretically justified. The empirical evaluation, while showing some promise, does not fully address the limitations imposed by this assumption, as it does not provide a comprehensive analysis of the method's performance across a wide range of non-Gaussian distributions with varying degrees of non-Gaussianity. 

Additionally, Equation (5) lacks precision, as a Taylor expansion includes a residual term. Specifically, the last term should be $f'(\theta_*)$  for a $\theta_*$ between $\theta_0$ and $\hat{\theta}$ rather than $f'(\theta_0)$. This omission could impact the accuracy of the asymptotic analysis.

The empirical results are limited for showing the generality of the developed method for non-gaussian settings. The experiments should include a more diverse set of non-Gaussian distributions and explore the sensitivity of the method to deviations from the Gaussian assumption.

### Questions
Please see the above comments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the challenge of testing conditional independence (CI) with a focus on accommodating discretized data, a crucial aspect for various applications. The authors introduce bridge equations to estimate covariance and establish asymptotic normality, facilitating an unconditional independence test. For the conditional independence test, they employ nodewise regression to recover precision coefficients. The effectiveness of the proposed method is substantiated through rigorous theoretical analysis and empirical validation.

### Strengths
This paper is well-written and easy to follow. The proposed CI test effectively corrects and infers the true CI relationships among latent continuous variables, recognizing that discretized variables may show different conditional independence compared to their continuous counterparts.

### Weaknesses
The authors primarily discretized variables into binary categories, which could potentially lead to some efficiency loss. Specifically, the use of only binary discretization might discard valuable information present in the original continuous variables, leading to a less powerful test. This is particularly concerning when the underlying continuous variables have a complex structure that is not well-represented by a simple binary split. The choice of discretization threshold can also significantly impact the results, and the paper does not provide a clear justification for the specific thresholds used. Furthermore, the reliance on a single bridge equation for covariance estimation, while computationally simple, may not fully capture the nuances of the relationship between the discretized and continuous variables, potentially leading to biased estimates.

### Questions
1. In Theorem 2.1, the authors emphasize the importance of establishing correct CI relationships among the latent continuous variables of interest. However, if we can only observe $\tilde X_2$, why is it necessary to infer the original conditional relationships? Could the authors provide practical examples to clarify this necessity?

2. In line 192, multiple definitions for $\tilde h_j$ are possible, such as substituting $E\tilde X_j$ with other quantities. Considering that $\tilde h_j$ impacts the asymptotic variance of the estimated covariance as noted in Theorem 3.5, is there an optimal choice for $\tilde h_j$?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses a specific challenge in confidence independence (CI) testing when variables of interest are discretized. In practice, accurately measuring continuous variables is often difficult due to data collection limitations, resulting in a common reliance on discretized values for these variables. To tackle this, the authors propose a unified bridge equation to estimate the covariance between two random variables by binarizing them. They then employ nodewise regression to recover precision coefficients that capture the conditional dependence among latent continuous variables. An appropriate test statistic is proposed, and its asymptotic distribution under the null hypothesis is derived.

### Strengths
The paper presents a well-established theoretical foundation and methodology. The authors begin with a straightforward theorem to illustrate the impact of discretization, emphasizing the potential need for correction in CI testing. The theoretical framework is clearly articulated and thorough.

### Weaknesses
The paper needs improvement in writing. There are several instances where the notations are unclear, inconsistent, and occasionally used imprecisely (see Questions for more details).

Major questions:
1. The authors empirically verify the Type I and Type II errors of the test. I’m curious if the asymptotic Type I error and power of the test could also be theoretically verified as well. I'm assuming the asymptotic power or Type I error will depend on $\mathbf{Λ}$ as well.
2. Have the authors considered providing a quantitative rate theory to support the test’s validity for smaller datasets? Additionally, are there any debiasing corrections that could be applied for small dataset sizes?
3. [Optional] The authors present a comprehensive framework based on the assumption that the random vector follows a multivariate normal distribution. I wonder if they have any thoughts on extending this framework to accommodate non-normal variables.

Minor questions:
1. Line 34: undefined notation $X_{j_1}$. More explanation on what ${j_1}$ means or may consider using $X_{1}$ and $X_{2}$ here.  
2. Line 89-90: same issue as in 1.
3. Line 122: inconsistent notations $\mathrel{\text{{$\perp\mkern-10mu\perp$}}}$ versus $\bot$ defined at Line 36. The former notation is more commonly referred as conditional independence in literature.
4. Line 126: what does DCT stand for? Should introduce the abbreviation beforehand.
5. Line 754: minor typo, should be $X_1\mathrel{\text{{$\perp\mkern-10mu\perp$}}}X_3 | X_2$
6. Line 137: undefined subscript $\sigma_{j_1, j_2}$. Consider using different subscripts for $\sigma_{j_1, j_2}$ and $\omega_{k,l}$ to distinguish them.
7. Line 362: remove ) after $vec(B^i_{-j})^T$.
8. Line 369: as much as I love the theory, I do find the mathematical notations concerning. I don't really see people using $vec$ to denote the rows of a matrix.

### Questions
Major questions:
1. The authors empirically verify the Type I and Type II errors of the test. I’m curious if the asymptotic Type I error and power of the test could also be theoretically verified as well. I'm assuming the asymptotic power or Type I error will depend on $\mathbf{Λ}$ as well.
2. Have the authors considered providing a quantitative rate theory to support the test’s validity for smaller datasets? Additionally, are there any debiasing corrections that could be applied for small dataset sizes?
3. [Optional] The authors present a comprehensive framework based on the assumption that the random vector follows a multivariate normal distribution. I wonder if they have any thoughts on extending this framework to accommodate non-normal variables.

Minor questions:
1. Line 34: undefined notation $X_{j_1}$. More explanation on what ${j_1}$ means or may consider using $X_{1}$ and $X_{2}$ here.  
2. Line 89-90: same issue as in 1.
3. Line 122: inconsistent notations $\mathrel{\text{{$\perp\mkern-10mu\perp$}}}$ versus $\bot$ defined at Line 36. The former notation is more commonly referred as conditional independence in literature.
4. Line 126: what does DCT stand for? Should introduce the abbreviation beforehand.
5. Line 754: minor typo, should be $X_1\mathrel{\text{{$\perp\mkern-10mu\perp$}}}X_3 | X_2$
6. Line 137: undefined subscript $\sigma_{j_1, j_2}$. Consider using different subscripts for $\sigma_{j_1, j_2}$ and $\omega_{k,l}$ to distinguish them.
7. Line 362: remove ) after $vec(B^i_{-j})^T$.
8. Line 369: as much as I love the theory, I do find the mathematical notations concerning. I don't really see people using $vec$ to denote the rows of a matrix.

### Soundness
3

### Presentation
2

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
In this paper, a CI test has been designed specifically for handling the presence of discretization. An appropriate test statistic for the CI of latent continuous variables, based solely on discretized observations, has been derived. The key is to build connections between the discretized observations and the parameters needed for testing the CI of the latent continuous variables. To achieve this, first, the bridge equations have been developed to estimate the covariance of the underlying continuous variables with discretized observations. Then, a node-wise regression has been applied to derive appropriate test statistics for CI relationships from the estimated covariance. By assuming that the continuous variables follow a Gaussian distribution, it has been derived the asymptotic distributions of the test statistics under the null hypothesis of CI.

### Strengths
1- Improving CI test accuracy is an essential and practical problem, particularly for structure learning in Bayesian networks and causal discovery.

2- The proposed method is novel, and the solution provided is relatively simple and efficient.

### Weaknesses
1- In (1), the discretization model (function) is unclear. How many discretization levels are used in this formulation? In addition, While the main idea is well presented, the authors have not clearly conveyed the details of the proposed method.

2- Providing a step-by-step explanation of CDT in a numerical example would enhance understanding of the proposed method.

3- The proposed method has improved the accuracy of the CI tests. However, another significant challenge with CI tests is the computational burden, particularly when there are many conditioning variables and a large sample size. Including a complexity analysis or a runtime comparison with existing methods in the numerical results would help demonstrate the impact of the proposed method.

4- Does not the number of discretizing levels affect the accuracy (Type I and Type II error) of the DCT method? In Figure 2 the effect of the number of discretizing levels on Fisherz and Chi2 methods has been checked and shown but the impact of it on CDT has not been reported. Why? I think the number of discretizing levels affects the accuracy of the CDT.  

5- Using practical examples for the application of the CDT in causal discovery can help to indicate the effectiveness of the proposed method in practical and real problems. 

6- In proof of Theorem 2.1, in appendix A.1, “Var(X2| \tilde{X2}) will never be zero since  \tilde{X2} is the discretized version of X2 (information loss).” is intuitively correct but it is not a precise mathematical expression for proof. Is there any reference or more precise explanation for that?

7- According to Figures 5, 6, and 8, CDT outperforms other methods in F1 score and Precision but generally performs worse in Recall.

### Questions
1- In the numerical results for the causal discovery example, In Figure 3, with increasing the number of samples F1 score, and precision are reduced for Fisher_z and Chis-q. Usually, increasing the number of samples increases accuracy. What is your explanation? 

2-  The proposed CI test was developed and analytically proven for the Gaussian distribution. Although it has been applied to other distributions in the numerical results, can the proposed method be analytically extended to other continuous distributions or to handle nonlinear relationships?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses errors in existing CI tests caused by an implicit discretization of the original continuous variable during measurements. The authors propose DCT to deal with this issue and establish the necessary theoretical foundations under assumptions such as having a Gaussian distribution. The method is tested using simulations.

### Strengths
The studied problem is important. With respect to the presentation, the problem is well motivated, formulated, and explained, and the experimental result is also written clearly. Some good effort is put into the experiments.

### Weaknesses
1) The main drawback of this paper is the overall presentation. I was not able to grasp the main idea, preventing me from properly evaluating this work. The following provides some details:

a) The authors were careful and patient in explaining detailed notations up to line 190. However, after that, the pace and notational complexity suddenly got of hand. For example, in line 192, the notation 1{ } is not even defined, let alone the meaning of the equation (the sentence in line 194 does not help). It was as if this part of the paper was written by a different author. I had a hard time understanding the paper from this point.

b) Definition 3.1. What is “the estimated boundary”? It should be rigorously defined somewhere. If the intention of this definition is to define “the estimated boundary” then the language is not appropriate. It should be something like this: “the \emph{estimated boundary of variables $X_j$ is defined as ….”. Currently, it reads as the estimated boundary is already defined before. 

c) Definition 3.4. Isn’t this simply the formula for the sample covariance? that is Cov(X,Y) = 1/n \sum_{i=1}^n (X_iY_i) - \mu_X\mu_Y? If so, what’s the point of giving it a separate definition and name (bridge equation)?

d) Theorem 3.5. I am confused by what is the rigorous statement in this theorem? By “this statistic is approximated to follow a normal distribution”, do the authors mean that the statistic converges to a normal distribution as N grows? 

e) Theorem 3.9. Where is the \hat{\beta}_{jk} formally defined? I suppose the answer is not eq 13 as then it should have been out of the theorem. 

f) The Experiment Section is back on track and written clearly. It was unclear though why the addition of W at line 450 is good for assessing the power.

2) One of the main motivations of this work was its application in Bayesian network (BN) structure learning. Nevertheless, insufficient effort was put into it. As the authors stated, the experiments in Section 4.2 are only for [extremely] sparse DAGs. They do consider denser ones in C2, but that is an only minor improvement, as the number of edges increased from p-1 to at most p+6. True DAGs can be much denser. The authors should provide a fair comparison for this part (also not to move these important parts in the appendix). 

a) I suggest to test several established datasets in BN structure learning such as ASIA, CHILD, WATER, and ANDES. 

b) Similar to the other experiment section, here, non-Gaussian distributions should be tested for structure learning. 

c) Even if the results here are weak, DCT appears to be a promising method that is worthy of publication, provided a major rewriting. 

d) Note that without this structure learning application, this paper perhaps better suits a statistics journal.

### Questions
Minor comments: 

line 73) This is a very interesting idea to use a DAG to invest the discretization problem; however, the authors implicitly assume that the DAG is faithful. The fact that $X_1$ is not d-separated of $X_3$ given $\tilde X_2$in the DAG does not imply that the $X_1\not\perp X_3\mid \tilde X_2$ in the distribution. 
line 73) extra comma
line 89) 1). 2). 3). are not common. Consider 1) 2) 3)
line 100) So all discretized variables are Gaussian? This is a limitation.
[important] line 137) The notation seems to be redundantly complex. Why \sigma_{j_1,j_2} rather than just \sigma_{j,k}, or even simpler \sigma_{jk}?
line 159) better not to start a sentence with an equation.
line 264) Consider using ^\top for transpose.
- Was DCT ever defined? What does it stand for?
line 264) grammar “contain”
line 269) “null hypothesis”
line 270) Be more specific, what are “our settings” and “our framework”?

### Soundness
3

### Presentation
2

### Contribution
2
