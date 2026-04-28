# Learning Representations of Intermittent Temporal Latent Process

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 8, 6, 5

## Abstract
Identifying time-delayed latent causal process is crucial for understanding temporal dynamics and enabling downstream reasoning. While recent methods have made progress in identifying latent time-delayed causal processes, they cannot address the dynamics in which the influence of some latent factors on both the subsequent latent states and the observed data can become inactive or irrelevant at different time steps. Therefore, we introduce intermittent temporal latent processes, where: (1) any subset of latent factors may be missing during nonlinear data generation at any time step, and (2) the active latent factors at each step are unknown. This framework encompasses both nonstationary and stationary transitions, accommodating changing or consistent active factors over time. 
Our work shows that under certain assumptions, the latent causal variables are block-wise identifiable. With further conditional independence assumption, each latent variable can even be recovered up to component-wise transformations. 
Using this identification theory, we propose an unsupervised approach, InterLatent, to reliably uncover the representations of the intermittent temporal latent process. The experimental findings on both synthetic and real-world datasets verify our theoretical claims.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposes a method for identifying latent causal variables for observed time sequences, motivated by sparsity of the causal connections. The identifiability of the latent variables is shown. Unlike most previous work, the considered setting allows the support of the mixing function to change over time.

### Strengths
The considered setting is interesting and well-motivated.

### Weaknesses
1. What $\mathcal{Z}$ refers to in condition (ii) of Theorem 1? Specifically, is $\mathcal{Z}$ a fixed subset of the support of $\mathbf{z}_{t}$ or the estimate? Additionally, where exactly is condition (ii) used in the proof? Finally, why isn’t the support sparsity assumption included explicitly in the statement of Theorem 1?

2. There should be more in-depth discussion on condition (iii) and the support sparsity assumption in Theorem 1, as these are critical for the identifiability results. Currently, it is unclear how strong these assumptions are. Including simple examples where condition (iii) holds naturally could be helpful. 

3. The presentation of Section 4.1 and 4.2 needs to be improved. The relationships between the components in Section 4.1, the loss function, and the illustration in Figure 2 are currently difficult to follow. The rationale behind the loss design is not clearly explained.

### Questions
See weaknesses 1 and 2

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
This paper introduces InterLatent, a framework for learning latent variables with an intermitent generative process. Intermitence is defined as some variables being "switched off" from at both transition and generation processes. The authors include theoretical analysis which demonstrates identifiability of the latent variables up to permutation and non-linear scaling, and provide some interesting applications to realistic domains where the missingness assumption is useful.

### Strengths
- The idea of "switching off" variables from the generative process at certain time steps is very interesting.
- The theoretical analysis establishes identifiability up to permutation and nonlinear scaling.
- The paper introduces the idea very clearly and states its importance in contrast to other very recent works.
- The proposed estimation method outperforms recent approaches and demonstrates applicability on realistic domains.

### Weaknesses
 
**Summary:**

This paper presents an interesting exploration of both applications and theoretical results. However, I have identified potential technical limitations in terms of formulation, theoretical rigor, and estimation methods. My comments below are organised into **Problem statement**, **Theory**, **Estimation**. They refer to section 2, 3, and 4 in the main paper. I would be glad to reassess my score if the authors address the issues outlined here.

**Problem setting:**
- Line 90: It is unclear if $f_n$ is truly invertible, given the setup described. If the noise variable's dimensionality matches the output variable’s, and at least one parent is from $z_n$, then the input dimensionality may exceed the output’s, making invertibility challenging. Could the authors clarify this statement or adjust the formulation to account for dimensionality constraints?
- Line 98: Does the transition function $f^u$ have any equivalence to the previous $f_n$?
- Line 99: “This implies that when $z^u_t$ is missing, it does not influence $z_{t-1}$ , $z_{t+1}$, or $x_t$”. How is it possible that $z^u_t$ would have any effect on $z_{t-1}$ in the first place, considering time moves forward? I believe the authors mean $z_{t-1}$ does not affect $z^u_t$ when the latter is missing, could this be clarified?
- Line 101, Equations (2) and (3): The definitions of $s$ are not complementary. Note that NOT (a AND b) = (NOT a) OR (NOT b). In your Eqs. you have AND in both cases. Given missingness in Eq. (3) is what you want, the authors might want to reformulate Eq. (2). 
- **Definition of Missingness:** The paper could benefit from a more formal presentation of how missingness affects the injectivity of the mixing function. Since the dimensionality of input variables varies based on the cardinality of $s_t$​, explicitly defining the generative process after establishing missingness might clarify the setup.


**Theory:**
-  **Figure 2 and Injectivity under Missingness:** Figure 2 introduces a mixing process affected by missingness, yet it is unclear how this interacts with the injectivity of the mixing function $g$. Specifically, if $g$ is injective at $t=1$ with $|s_t| = 2$, how would this property hold at $t=2$ with $|s_t| = 3$? Such cases seem to challenge the theoretical claims unless clarified.
- **Dimensionality of $d_t$:** If $d_t$ is fixed the above argument is not problematic. However, Figure 2 suggests that $d_t$ can vary, making the injectivity claim potentially problematic. Could the authors specify this constraint in the theoretical statements if $d_t$ is indeed fixed?
- **Possible Extension to Time-Dependent $d_t$:** One way I can think of incorporating a time-dependent $d_t$ is to intoduce a mixture distribution for $x_t$, where each mixture component allows different values of $d_t$. You could incorporate results from identifiability in mixture models for sequences, such as switching dynamical systems, by conditioning the mixture component at each time step. However, implementing this change would likely require substantial modifications to the theoretical framework.
- **Validity of Assumptions:** It would be helpful if the authors could provide empirical or theoretical justifications for the assumptions (i-iii) in Theorem 1, specifically how they ensure consistency with the InterLatent model.


**Estimation:**
- **Estimating $s_t$:** The inference process feels incomplete due to the absence of information on how to estimate $s_t$​, which is central to the framework’s operation. This aspect isn’t fully explained in the main text, and more details on how $s_t$​ is computed or estimated would greatly clarify the estimation procedure.
- **Framework Adjustments in Figure 2:** Given that missingness affects the data generation process by altering the mixing function, it would be useful to understand how this variation is incorporated into the learning method. Could the authors expand on this?
- **Clarifying the Role of Sparsity Regularization (Eq. 10):** If the authors intend for sparsity regularization to automatically account for missingness, this point could benefit from a clear explanation. Without an explicit estimate of $s_t$, it’s challenging to understand the approach used for computing Eqs. (8) and (9). Some added details could help readers follow the inference method more easily.

### Questions
Below are some miscellaneous comments:
- line 59 typo: “... has yet to fully addressed these challenges.
- Consider using \citet instead of \citep in some cases. Examples:
  - line 59: “(Wiedemer et al., 2024) relies on … “
  - line 60: “(Lachapelle et al., 2023; Fumero et al., 2023; Xu et al., 2024) are restricted to linear … “
- Line 64: Would it be possible to briefly define block-wise identifiability? Similarly for component-wise identifiability.
- Lines 144-150: Can you define the domain for $h$ in both cases?
- Line 186: I believe you refer to pdf instead of cdf in both cases.
- Eq (7). With LeakyReLU(MLP(x)) you can get negative covariances. Is this expected?
- Line 263: Typo in $\hat{z}_t | x_t$

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new class of discrete-time stochastic process with a series of latent variables that are allowed to (i) vary over time, (ii) be uninformative to either the observed data and/or the subsequent latent values, and (iii) be identifiable for those that are informative. Along with defining this class of processes, the paper also proposed a variational inference method for learning and modeling them, which is able to adequately represent this latent and observed sequential values.

### Strengths
I found the general proposed process to be simple yet powerful in practice. The authors were able to derive useful theoretical findings with minimal assumptions made on the underlying process, and the proposed model itself appears to be straightforward in design. I believe that this work is of interest in general to the graphical modeling community, with advances towards interpretable latent dynamics.

### Weaknesses
While a lot of time was spent on the general class of processes, I feel like the modeling (section 4) was a bit rushed and could benefit from more explanations and commentary on the design decisions made. For instance, why was a variational approach chosen over a sampling-based one? It is clear some inference procedure is needed to account for $z$ values being latent, but not much discussion is given to justify the choices made here. Additionally, the sparsity regularization is thrown in as part of the loss without much discussion around it. I am assuming that this is to encourage latent values to be "missing" when possible but that is just speculation.

### Questions
I would personally rebrand describing when the Jacobian results in a 0 as the corresponding latent value being "missing" to rather be described as "uninformative" or something similar. The reason being is the latent values are always missing / never observed. Should $p(x|z_1,z_2)=p(x|z_1)$, then that is a matter of independence rather than missingness. I am curious on your thoughts to this, or if I missed something concerning this.

### Soundness
4

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
The authors propose a setting where observations are produced by a set of latent factors. These latent factors, however, may or may not be active from period to period. The authors suggest that under certain conditions these latent factors can be identified. Their theory informs a very specific architecture, and they demonstrate that the method works on synthetic data and on a real-world video dataset.

### Strengths
I like and understand the setup - it is indeed reminiscent of many real-world problems. I also like how tightly the theory and the architecture are connected. Finally, I find the synthetic experiments persuasive - they do show that the proposed method indeed works.

### Weaknesses
I have 2 main concerns: (1) there is no attempt to show that this method scales to high dimensions, and (2) real-world dataset experiments are woefully insufficient.

### Questions
I don't have specific questions - the paper is written clearly. But scalability needs be addressed. And demonstrating that the method works only on one dataset is completely unacceptable. The LEAP paper (one of the benchmarks), for example, has 3 datasets. The setup lends itself well to the time series modality. The authors themselves mention applicability to finance - they should consider pointing this machinery at that type of data. Medicine, or other setting with sensors could work well too.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a meaningful study on learning latent variables and their identifiability theory in intermittent temporal latent processes. The author establishes a set of novel identifiability results for intermittent latent temporal processes, extending the identifiability theory to scenarios where latent factors may be missing or inactive at different time steps.  However, despite the proposed identifiable theory being relatively sophisticated, the theory and the proposed network structure are relatively isolated and do not adapt well to the identifiable assumption.

### Strengths
1. The author presents a promising research scenario, namely intermittent temporal latent processes.

2. The author proposes a complex identifiable theory, in which both non-stationary and non-stationary transition processes are applicable, 

3. the author suggests that under certain assumptions, latent variables can be identified in blocks. By further assuming conditional independence, each latent variable can even be restored to a component by component transformation.

### Weaknesses
1. In this paper, the author considers latent variables as causal variables. Is the "causality" referred to Granger causality? If not, what is the difference between Granger causality and latent variables

This is more like a blind source separation task. How does it relate to mainstream structural causal models or latent outcome models? Or what is the connection with traditional Granger causality?

2. The relationship between the proposed theory and the established model is not closely related, making it difficult to see the relationship between the network design and the assumptions given by the theorem. 

3. The same type of variational autoencoder introduced, such as "a transition prior module based on normalizing flows," has been used in many papers[LEAP, TDRL, etc ], and it has been found that there is no significant difference or improvement in network design compared to other methods. Does this mean that all baseline variational autoencoders have the identification capability proposed in this paper?

4. During the experiment, it was also difficult to directly identify where the synthesized dataset met the identifiable assumption conditions proposed in the article.

### Questions
1. This article presents a promising theory, but network design is no different from most papers(eg, LEAP, TDRL, etc ), and it is also unclear which modules are designed to meet specific identifiable conditions, which appears very disjointed and the results in a mismatch between theory and methodology.

2. What are the limitations of this article, and does it mean that any variational autoencoder model is applicable to any data in any situation?

3. The author should further clarify where the given synthetic data method satisfies the assumption of identification, and should provide a detailed description of how it is combined with the proposed theory in the process of network design, rather than simply listing the network structure

4. The author should clarify whether the causal variable belongs to the Granger causality category or other categories.

### Soundness
3

### Presentation
3

### Contribution
2
