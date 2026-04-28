# Revealing Hidden Causal Variables and Latent Factors from Multiple Distributions

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
In many problems, the measured variables (e.g., image pixels) are just mathematical functions of the hidden causal variables (e.g., the underlying concepts or objects). For the purpose of making prediction in changing environments or making proper changes to the system, it is helpful to recover the hidden causal variables $Z_i$, their causal relations represented by graph $\mathcal{G}_Z$, and how their causal influences change, which can be explained by suitable latent factors $\theta_i$ governing changes in the causal mechanisms. This paper is concerned with the problem of estimating the underlying hidden causal variables and the latent factors from multiple distributions (arising from heterogeneous data or nonstationary time series) in nonparametric settings. We first show that under the sparsity constraint on the recovered graph over the latent variables and suitable sufficient change conditions on the causal influences, the recovered latent variables and their relations are related to the underlying causal model in a specific, nontrivial way.  Moreover, we show that orthogonally, under the modular change condition on the causal modules (without the sparsity constraint on the graph), the underlying latent factors $\theta_i$ can be recovered up to component-wise invertible transformations. Putting them together, one is able to recover the hidden variables, their causal relations, and the corresponding latent factors up to minor indeterminacies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper works on the problem of recovering the hidden causal structure of latent variables given observational data from different environments. Authors show, that under a sparsity constraint of an underlying Markov network and a sufficient number of changes across environments, the Markov network can be recovered up to the simple indeterminacies. Furthermore, under additional mild assumptions, the recovered Markov network coincides with the moralized causal DAG. Additionally, latent factors can be recovered too, under similar assumptions. The authors provide two different implementations following the theory and do several synthetic experiments.

### Strengths
The problem of identifying a latent structure is highly relevant in causal inference research. To tackle it, the authors made some interesting theoretical work by applying the proof technique from Lin (1997) based on second-order derivatives of the log-density. Also, I found the connection between Markov networks and causal DAGs interesting.  Additionally, I appreciate the attempts to make the proposed approach as general as possible.

### Weaknesses
I identified several important flaws, which need to be addressed by the authors. Those include connections to previous works, lack of rigour and questionable correctness of the statements, realisticness of the assumptions, and experimental evidence/evaluation issues. 
  
**Connections to previous works**. It seems like the identification technique with second-order derivatives of the log-density from  Lin (1997) is a standard technique for identifying structural causal models (SCMs), e.g., used in [1, 2]. Also, I don’t understand the connections between existing identifiable SCMs, like additive noise models and post-non-linear models, and the statements of Theorems 1 and 3, as those SCMs must be special cases of the proposed Theorems. 

**Lack of rigour & questionable correctness**. I found it hard to understand the claims of the Theorems, as some notation was not introduced properly or sufficiently. For example, how are $\tilde{Z}$, $h(\cdot)$, and $q(\cdot)$ defined? What is $m$ in Theorem 1, and which sparsity constraints Theorem 2 refers to? Are $\theta$ one-dimensional factors (parameters)? What is $u$ in Eq. 3?  This is problematic, as, e.g., I failed to understand the proof of Theorem 1. Some statements might be even wrong, given the current version of the paper. For example, I do not understand, how the dimensions of $X$ and $Z$ can be different and $g(\cdot)$ is an invertible transformation, and at the same time, the determinant of Jacobian is well-defined (App. A). In the case of the dimensions mismatch, an invertible transformation would be non-continuous (see Netto's theorem). On the other hand, if we assume a same-dimensional manifold embedded in higher-dimensional space, the change of variables formula used in App. A would be different, e.g., see [3].     

**Realisticness of the assumptions**. The major discussion is missing on whether the assumptions in Theorems 1 and 5 are realistic. For example, how could one assume the dimensionality of $Z$ only given $X$? Or even when assuming it, how can we verify, given the data from several environments, whether the number of environments is sufficient? I would love to see a real-world application or a case—study, where we could make those assumptions, or at least speculate about them.

**Experimental evidence/evaluation issues**. The provided experiments aim to support the claims of Theorem 3, and I did not find any regarding Theorem 5 for identifying latent factors. The provided experiments still contain very little implementation and evaluation details, and there is no source code available. For example, it is not clear, how the synthetic data is sampled, e.g., what are “noises” and “biases” in Sec. 5.3? Additionally, I don’t understand, how the provided synthetic datasets satisfy the assumptions of Theorem 3, e.g., what is the sufficient number of environments, what is the dimensionality of $X$, or how we ensure that the MLP is an invertible function.  On the other hand, the evaluation itself is ambiguous, as it is unclear, how the scatter plots in Figures 2 and 3 support the claim that “the hidden structure is recovered”.

### Questions
- Traditional SCMs, defined by Pearl [1], assume that latent variables by definition do not have parents. Why cannot we directly model an SCM for $X$ without assuming another latent SCM over $Z$ and a nonlinear mixing function? I would like to hear a discussion on this, as this modelling approach seems to be way simpler.
- Why is $Z_i$ a function of the $\hat{Z}_k$ or $\hat{Z}_l$, if $Z$ and $\hat{Z}$ are observed and modelled variables, respectively, and, thus, are variables of different SCMs? What is $\frac{dZ_i}{d \hat{Z}_k}$ in App. A?

References:
[1] Bareinboim, Elias, et al. "On Pearl’s hierarchy and the foundations of causal inference." Probabilistic and causal inference: the works of Judea Pearl. 2022. 507-556.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies identifiability questions for causal latent systems, in a situation where observations from multiple and diverse environments are available. The diversity here is a necessary condition for the method.  

It is shown that one can use a certain known characterisation of conditional independence using derivatives of the density to partially identify the dependence structure of the latent system, provided it is observed in a diverse enough number of environments.  


Experiments on small synthetic examples are performed to demostrate the general problem setup and identifiability in it.

### Strengths
The subject of identifiability in causal systems is important.  
I have not seen the characterisation of conditional independence via density derivatives used in recent literature, and believe it is of interest.

### Weaknesses
First, there are several critical issues with presentation. Second, the setup considered in the paper is quite restrictive. In addition, the main "sufficient changes" assumpion is not discussed. It is not discussed when we can expect it to hold, nor is it evaluated in any actual scenarios. This is the main issue.  Third, the experiments are performed on small toy examples, and use known architectures of causal discovery.  It is not clear what is their added value. 

In more detail:

**Presentation:**  
**(a)** the presentation is missleading as it positions the paper as "treating the case of multiple environments, which is not treated in the litarture". This makes the impression that the approach is a generalisation of a single environment case. However, it is not. The proposed methods can not be used for a single environment. In a way, the method exploits the differences in environments, and there must be many of them.   **(b)** Some critical definitions are not given in the main text. Specifically, "Modular Changes" of Theorem 5 is not defined, and "sparsity constraint" of Theorem 3.  **(c)** Literature: there is a significant amount of research on multiple environments via causality that is not mentioned in the paper. The NN architectures presented in Experiments are small modifications of known arhcitectures (normalising flows flows for causal discovery).  Proper references should be given. 



**Problem Setting and The Sufficient Changes Assumption**: 
The setting (1) is restrictive in two ways: First, the observations $X$ are a deterministic function, i.e not noisy observations. Second, and more importantly, the observation map $g$ is assumed to be _invertible_. For at least somewhat smooth maps this means dimension of $X$ and $Z$ must be the same, which is unrealistic. How important is invertability? 

The fundamental assumption of this paper, of Sufficient Changes, appears very strong. It requires independence for every point $z$. The number of environments must be at least as large as the number of variables (if same set of environments is good for all $z$). This condition must be discussed. When does it hold? Examples? I would suggest removing the Experiments section, and discussing this condition in detail. 



**Experiments**: 
In addition to what mentioned on the experiments above:
Regarding the following phrase in the end of Section 5: 
>However, when the noises are Gaussian, it becomes more challenging and we observe that some components are mixed, which further aligns with our theory (e.g., Theorem 3) and demonstrate the benefit of using suitable parameterization.

I do not see how this results aligns with the theory, and in particular with Theorem 3. Theorem 3 does not appear to have assumptions that distinguish between Gaussainity and non Gaussianity. Please exlain.

### Questions
Please see above.

### Soundness
1 poor

### Presentation
2 fair

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
This paper studies latent causal identification under multiple distributions where multiple distributions are modeled as mechanism change. The first part tries to latents under sparsity constraint using observational distribution only. The second part uses orthogonal changes to show that latent factors can be learned with multiple distributions.

### Strengths
The paper is well-written. It is quite easy to follow.

### Weaknesses
- Is the condition (sufficient change) of theorem 1 too strict? What are some practical use cases for this? Specifically, how many environments are typically needed, and what kinds of changes are sufficient to satisfy the conditions? It's not clear how this relates to real-world data where the number of environments might be limited or the changes may not be orthogonal.

- The experiment section is limited, only on simulated data and very limited graphs. The experiments do not explore the boundaries of the theoretical results, such as how the method performs with increasing graph complexity or when the assumptions are slightly violated. It would be beneficial to see experiments on more complex graphs and real-world datasets to validate the practical applicability of the method.

- The number of latents needs to be known in advance. This is a strong assumption that limits the practical use of the method. In real-world scenarios, the number of latent factors is often unknown and needs to be inferred from the data. The paper should discuss how to address this limitation, perhaps by incorporating model selection techniques or adaptive methods for determining the number of latent variables.

- I am a little confused about one of the main objectives of the paper: What does identifying potential shifts even mean? Even if I can learn $\theta$ up to component-wise invertible transformations? What does knowing $\theta$ tell me? It's unclear how this information can be used for downstream tasks or to gain a deeper understanding of the underlying causal mechanisms. And I don’t think theorem 5 is verified by experiments either. The paper needs to clarify the practical implications of identifying these shifts.

- By the way, Can you explain how the last line of the proof of theorem 5 leads to the conclusion? Also where in the proof do you need the modular change assumption? It's not immediately clear how the zero-product condition on the partial derivatives implies component-wise identifiability, and the exact role of the modular change assumption in the proof needs to be explicitly stated.

- the sparsity condition is not made explicit in theorem 2? Can you state it formally? What specific type of sparsity is assumed (e.g., edge sparsity, node sparsity), and how does this sparsity constraint affect the identifiability results? The paper should provide a formal definition of the sparsity condition used in the theorem.

- not sure how to interpret the results of theorem 1? it is not intuitive? If the main purpose of theorem 1 is to prove later theorem, maybe it should be a lemma? The result seems somewhat detached from the main goals of the paper and its connection to the subsequent theorems is not immediately obvious. The paper should clarify the role of this theorem and its implications.

- The proof of theorem 1 uses assumption 3 which is not assumed by theorem 1? This is a critical error that needs to be addressed. The proof should only rely on the assumptions stated in the theorem itself.

### Questions
- the sparsity condition is not made explicit in theorem 2? Can you state it formally?

- not sure how to interpret the results of theorem 1? it is not intuitive? If the main purpose of theorem 1 is to prove later theorem, maybe it should be a lemma?

-  The proof of theorem 1 uses assumption 3 which is not assumed by theorem 1?

- what's the relation between modular change and ICM? why do you use the "not related via equality constraint"? What if $\theta_i$ and $\theta_j$ are related by some inequalities? Does you result still hold? 

- How is your multi-distribution setting different from soft interventions?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, causal inference with hidden factors is investigated. The model studied in equation (1) is quite general, and the focus of the work is to understand when and how the causal structure can be estimated from observations. 

In the first set of results, the authors determine conditions under which the Markov graph underlying the conditional dependency structure of the variables can be uniquely identified from the distribution of observations (Thms 1 - 3). Furthermore, the latent factors which affect the hidden variables can also be identified (Thm 5). Finally, the authors assess their methods through simulations.

### Strengths
The authors study a very general model, and establish fundamental conditions for the identifiability of causal structures and latent factors. The fundamental contributions that are made for this model therefore have important and widespread applications. The paper is clearly written.

### Weaknesses
While the bulk of the paper establishes fundamental results for causal inference, this seems to have little impact on the design or guarantees of machine learning algorithms. Though there is a Simulations section in which the authors apply their theory, there seem to be many details and analysis missing. For instance, it is not clear to me how the data is generated, and the results shown in Figures 2 and 3 have little explanation. Hence it is quite challenging to understand what exactly the authors are trying to demonstrate, and how well their procedure performs.

The technical side seems reasonable. However, I didn't understand the significance of the linearly independent vectors (see, e.g., bullet point 2 of Thm 1). Please explain its importance.

### Questions
- On page 3, should it read $Z_j \to X_i$ if and only if $Zj \in PA(X_i)$?
- How should we imagine that $(\hat{g}, \hat{f}, p_{\hat{Z}})$ is learned to achieve Eq. (2)?
- Unclear how well structure is recovered, just from looking at Figure 2. What do these scatter plots represent? Same comment for Figure 3.
- In the text after Eqn (6), you state that $C^{(u)}$ and $S^{(u)}$ are a matrix and vector, respectively. Then in Eqn (7) you "divide" by $S^{(u)}$ in the right hand side. Could you elaborate on what this means

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
