# Causal Inference with Conditional Front-Door Adjustment and Identifiable Variational Autoencoder

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
An essential and challenging problem in causal inference is causal effect estimation from observational data. The problem becomes more difficult with the presence of unobserved confounding variables. The front-door adjustment is a practical approach for dealing with unobserved confounding variables. However, the restriction for the standard front-door adjustment is difficult to satisfy in practice. In this paper, we relax some of the restrictions by proposing the concept of conditional front-door (CFD) adjustment and develop the theorem that guarantees the causal effect identifiability of CFD adjustment. Furthermore, as it is often impossible for a CFD variable to be given in practice, it is desirable to learn it from data. By leveraging the ability of deep generative models, we propose CFDiVAE to learn the representation of the CFD adjustment variable directly from data with the identifiable Variational AutoEncoder and formally prove the model identifiability. Extensive experiments on synthetic datasets validate the effectiveness of CFDiVAE and its superiority over existing methods. The experiments also show that the performance of CFDiVAE is less sensitive to the causal strength of unobserved confounding variables. We further apply CFDiVAE to a real-world dataset to demonstrate its potential application.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method of Average Treatment Effect estimation and representation learning through the Conditional Front-Door Criterion (CFD) combined with a variational autoencoder model (CFDiVAE).

The authors start with the standard front-door criterion scenario and relax it by allowing backdoor paths between the treatment and the mediator as well as between the mediator and the outcome. The second relaxation is allowing unmeasured confounding variables between treatment and outcome. A background on the front- and back-door criteria is given after which the authors proceed to state the first contribution of the paper, the Conditional Front-Door adjustment (CFD). The CFD is the same formula as the standard front-door adjustment but with additional conditioning on W (the backdoor paths between the treatment and the mediator). Subsequently, the second contribution of the paper, the CFDiVAE model, is described. It follows existing generative VAE work (such as (Louizos et al.)) and adjusts it to the assumed generative model of CFD. CFDiVAE learns a representation of the mediator, given observed back-door paths (confounding variables) between the treatment and the mediator, and allowing for potential unobserved confounding variables. A thorough analysis of model indentifiability is provided. The paper concludes with a series of experiments. First, estimation bias of ATE is compared to competing causal-VAE methods. CFDiVAE beats the other methods for large enough dataset sizes. Secondly, a short assessment of CFDiVAE on a real dataset is performed.

### Strengths
The paper tackles the important problem of causal inference with observational data. It is well-written and easy to follow. The methods the paper builds on (front-door criterion) are useful in many areas, from model interpretability to algorithmic fairness. The first contribution (CFD) is a correct relaxation of the front-door criterion, while the second one (CFDiVAE), while building on existing VAE methods, is well analyzed. . The experiments show that, assuming a linear generative model with a mediator, CFDiVAE estimates ATE better than methods that do not model a mediator directly.

### Weaknesses
The main weakness of the paper is its limited novelty.

The main contribution, the Conditional Front-Door Adjustment is a straightforward extension of the front-door criterion (where everything is conditioned on the backdoor path W between the treatment and the mediator; W is assumed to be observed). It, in fact, boils down to plugging in the front door criterion into the backdoor criterion.

One could argue that any concrete DAG which allows for the relaxation of the front door criterion with the do calculus (as mentioned in Pearl, Causality, 2009, page 83, Figure 3.1) can form a basis for a similar model.

The second contribution, the CFDiVAE generative model, builds heavily on similar models present in literature. The generative and inference part follow standard VAE procedures adjusted to the assumed underlying SEM.

While the specific combination of CFD with a generative VAE-based model is novel, it also does seem incremental.

### Questions
Would considering relaxations of the front door criterion as mentioned in Pearl, Causality, 2009, page 83, Figure 3.1, result in any major changes to the model (I assume the inference model might have to be adjusted)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method to relax some of the restrictions by introducing the concept of conditional front-door (CFD) adjustment and developing the theorem that guarantees the causal effect identifiability of CFD adjustment. The authors further propose CFDiVAE to learn the representation of the CFD adjustment variable directly from data with the identifiable Variational AutoEncoder. They apply CFDiVAE to a real-world dataset to demonstrate its potential application.

### Strengths
1. The writing of the paper is good.  The method potentially has broad applications.
2. The authors provide theoretical analyses for the proposed approach.  The reviewer did not check the details due to the review time limit, but it looks sound.

### Weaknesses
1. Additional results on real-world datasets and analysis could strengthen the paper.

2. The section references in the supplemental file are confusing.  E.g., the title of section C.4 refers to ‘Section 4.5’ in the main text. However, section 4.5 in the main text does not exist. This causes trouble for the readers.

### Questions
The authors could apply the method to additional real-world datasets, conduct a comparison with existing methods, and provide the analysis to strengthen the paper.  The author also needs to address the errors in the section reference.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Post rebuttal update** The final version is much better than the original submission. I **raise the score to 6, conditional on** that the following point is fixed in the (possible) camera-ready version. *I believe one main concern of reviewer BvSP is also related to this.*

>The exponential family prior eq11 is too general to be useful. Examine the identifiability in eq25 again, the sufficient statistics S are involved. Only in some cases like Gaussians, we can get around this problem. See [1] and reference therein.

For further improvement, my concern about the outcome regression on the Adult dataset was that here the proxies also affect the outcome. That was why I am asking “is the process in Sec 5 still applicable” for the Adult dataset?

**End update** 

The paper considers an extension of the front-door adjustment (FDA), called conditional front-door (CFD) adjustment, where there is a (conditional) variable that affects the adjustment variable in the FDA. An identifiable VAE is employed to recover the adjustment variable from the proxy. Directly based on previous results, the identifiability and adjustment equation of CFD is proved, and the identifiability of the proposed VAE is also proved. Experiments show favorable results.

### Strengths
The front-door adjustment (FDA) is an important and understudied approach in the ML community.

Considering a conditional variable in front-door is a meaningful extension.

Using iVAE to recover the FDA variable is novel and interesting.

### Weaknesses
*It is very hard to recover the adjustment variable from the proxy (if the proxy noise is not very small)*

The proxy setting is challenging in itself, and the only rigorous identification result under this setting I know is (Miao et al 2018), which depends on two types of proxies and has several assumptions about the proxies.  ref Miao, Wang, Zhi Geng, and Eric J. Tchetgen Tchetgen. "Identifying causal effects with proxy variables of an unmeasured confounder." Biometrika 105.4 (2018): 987-993.

In fact, the current theory is only meaningful under small proxy noise that is \epsilon in eq10.  If we examine the identifiability of iVAE closely, we see, as in eq25 in the current paper, only $f^{-1}(X)$ is identified (up to deterministic transformation) but not the latent variable. And, $f^{-1}(X)=f^{-1}(f(Z)+\epsilon) \neq Z$ if $\epsilon \neq 0$. See the Questions for more related points.

However, if $\epsilon = 0$, then X and Z are related by an injective function, and it is not very meaningful to say X is a proxy of Z, because the whole point of proxy setting is that there is *unmeasured* information of Z not captured in X.

I do not require to fix this weakness in the rebuttal, but it should be discussed and made explicit in the revised version.

*Separated, limited, and unclear outcome estimation*

The connection between the front-door setting and the proposed VAE is weakened, because the outcome is not modeled by the VAE, and the outcome estimation is done in a standalone step, as in Sec 5. Importantly, how does the 2-step process here implement the adjustment eq3? How exactly the ATE is computed? Moreover, the adjustment and outcome variables follow linear models; this might not be an inherent limitation in the approach, but this limitation in the current work should be mentioned in the Conclusion. Finally, for such an important component of the approach, citing a web article makes me nervous, please find and cite an original reference (a research paper).

*Experiments are not sufficient or clear.*

The major problem is that there are no comparisons to methods designed for the front-door setting. And this renders the good result in Fig 4 not very meaningful. I cannot see why we need to exclude FINDFDSET and LISTFDSETS because they require a known DAG; when you build the synthetic dataset, the DAG is known anyway? And I doubt there are no other methods for the FDA. If you really cannot fix this weakness, it is necessary to mention this in the Conclusion.

Another important issue is that, as in Table 1, the proposed method requires a huge amount of data to perform well. In previous work, the methods usually train on sample size < 1k, but the proposed method is worse than other methods when sample size < 1k. This should be examined seriously and would be a major weakness of the approach if this is a general observation. 

The experiment on Adult is very confusing to me. First, the “proxy” X also affects Y as shown in the Appendix, can we still say this is a “proxy”? In particular, is the process in Sec 5 still applicable? Second, a reader cannot understand the discussion of direct and indirect causal effects without looking into the Appendix. You need to mention X (eg., marital status) also affects Y and is the “mediator” here. Third, it seems to me that “significant indirect discrimination … through the indirect paths via marital status” and “significant discrimination against sex through the stereotype” are contradictory but not consistent?

### Questions
The exponential family prior eq11 is too general to be useful. Examine the identifiability in eq25 again, the sufficient statistics S are involved. Only in some cases like Gaussians, we can get around this problem. See [1] and reference therein.

As is observed in [1], setting the representation dim(Z) to dim(X) is better than dim(Z)=1, and sometimes even better than using the true dim of the adjustment variable. It is better to add experiments in this regard.

*An important reference is missing*. Intact-VAE [1] is also based on iVAE and it is more related to the proposed VAE than any other compared methods, although it considers a different causal setting. In fact, many points mentioned in this review are discussed in [1], e.g., the noise level, the form of the identifiability, and the representation dim. And it is good to add experimental comparison.

[1] Wu, Pengzhou Abel, and Kenji Fukumizu. "beta-Intact-VAE: Identifying and Estimating Causal Effects under Limited Overlap." International Conference on Learning Representations (2022).

I believe only the link W → Z is necessary but not W→T and W→Y. In fact, the Adult dataset does not have W→T.

It should be made clearer in Contributions and Conclusion that it is the FDA, which is a well-established result, that deals with unobserved confounding in this approach, and the VAE learns the adjustment variable but does not do the adjustment using eq3. The CFD is a slight extension of the original FDA.

*Some unsupported/misleading statements*.

“it is often impossible for a CFD variable to be given in practice” This seems strong and needs a reference/discussion.

“there exist unobserved confounding variables and the standard front-door adjustment is no longer applicable” This reads as if FDA does not deal with unobserved confounding but the proposed VAE does.

”the latent variable (i.e., ZCFD) refers to the variable that is not measured, but its information is captured by its proxy” As mentioned, a proxy does not capture all the information of the latent variable, though it might capture *enough* information for the causal effect; this requires challenging analysis and specific assumptions as in Miao 2018.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
POST REBUTTAL UPDATE
Overall the paper has clearly improved during the rebuttal phase. The assumptions and limitations of the method are much better discussed and the changes in the experiments have improved them. That said, I fully concur with reviewer s6a3 that discussion on sufficient statistics with which the theory holds should still be included. I will update my score to 6.
POST REBUTTAL UPDATE END

The paper considers front-door adjustment for causal effect estimation. In particular, the setup involves the following variables: T (treatment), W (observed confounders), U (unobserved confounders), Y the outcome, Z (front-door adjustment variable), and X proxy variable for Z. The article makes two main contributions: 1) The article proposes a conditional front-door adjustment, which differs from the standard front-door adjustment by having an additional edge from the observed confounders W to the front-door adjustment variable Z. The paper shows how in this situation the standard front-door adjustment must be modified to estimate the causal effect (Theorem 3). The proof is based on the assumption that the front-door adjustment variable Z is observed. 2) The second contribution is a conditional VAE method for the situation where the front-door adjustment variable Z is not observed, to estimate it from the proxies X (conditionally on variables W and T).

### Strengths
1) The first contribution, the conditional front-door adjustment, seems intuitive, interesting, and useful. To the best of my knowledge this is novel (though I haven’t read all the papers about front-door adjustment). The conditional front-door adjustment is presented clearly and the proof seems mathematically correct.

2) The VAE approach seems a reasonable attempt to estimate the front-door adjustment variable from the proxies.

3) The empirical results demonstrate that the proposed approach clearly outperforms methods that do not do any front-door adjustment at all. Sensitivity analysis for assuming an incorrect number of latent variables (smaller than correct) was a nice bonus.

### Weaknesses
1) There seems to be a gap in the theoretical part. The model identifiability analysis in Section 4.3 shows that the front-door adjustment variable Z obtained with VAE is identifiable up to a transformation (more or less the result from Khemakhem, 2020). But Theorem 3 is based on the assumption that the front-door adjustment variable Z is observed. It is not clear if Theorem 3 is still applicable if it is used for a transformed Z.

2) The empirical comparison includes as baselines only methods that do not use the proxies of the front-door variable at all, and consequently each of those has poor performance. It would be better to think how the proxies would be used if the new method did not exist, for example by using the proxies directly for front-door adjustment? The existing front-door adjustment methods (by Jeong, Wienobst) were not included in the comparison because they assumed that the DAG is known. However, also the present method assumes that the causal graph is the one presented in Figure 2 and all simulations assume this correct structure (except for a possible mismatch in the latent dimension).

3) Some small inconsistencies in the notation, at least: Equation (4): LHS has T and W but RHS does not. Equation (6): formulas for the mean and variance have j on the LHS but not on the RHS.

4) In the real-world example, the ATE estimate is 0.176, which is very similar to the previous estimate 0.175 (from Appendix C.5), which seems to imply that the new method does not provide too much novel insight in this case (but of course it is a good demonstration that it is consistent with previous estimates). In general, it would be nice to see some example where the heavy VAE machinery is really needed, which might require more complex, e.g., higher-dimensional, proxies, to make a convincing case.

Overall, I liked the first contribution, the conditional front-door adjustment, but I found the conditional VAE a bit confusing, possibly breaking the theory, and whose usefulness was not demonstrated very convincingly. I’m not sure but that paper might have been stronger without the VAE aspect altogether. At the very least the possible gap in the theory should be addressed. If it is not possible to fix the gap, then the theory (regarding the identifiability of the VAE) could be moved to the supplement and replaced by more convincing empirical analysis, and the text could be updated accordingly.

### Questions
1) Could you comment on the weakness number 1, please?

2) Section 6.2. Can you clarify what you mean by ground-truth density function for the representation? With simulated data, don’t you know the representation variable exactly for each data point, which would allow you to compare the estimated and the ground-truth values directly (e.g. using a scatter plot)?

3) What is the dimension of the proxy variable in the simulated experiments?

4) Can you clarify if you used the linear method in Section 5 to estimate the causal effect? How is this compatible with the conditional VAE model that parametrizes the model for the front-door adjustment variable with a neural network?

5) What would happen if you assumed a larger than correct dimension of the latent variable?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
