# Bayesian Neural Controlled Differential Equations for Treatment Effect Estimation

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Treatment effect estimation in continuous time is crucial for personalized medicine. However, existing methods for this task are limited to point estimates of the potential outcomes, whereas uncertainty estimates have been ignored. Needless to say, uncertainty quantification is crucial for reliable decision-making in medical applications. To fill this gap, we propose a novel \emph{\methodlong}~(\method) for treatment effect estimation in continuous time. In our \method, the time dimension is modeled through a coupled system of neural controlled differential equations and neural stochastic differential equations, where the neural stochastic differential equations allow for tractable variational Bayesian inference. Thereby, for an assigned sequence of treatments, our \method provides meaningful posterior predictive distributions of the potential outcomes. To the best of our knowledge, ours is the first tailored neural method to provide uncertainty estimates of treatment effects in continuous time. As such, our method is of direct practical value for promoting reliable decision-making in medicine.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to estimate the treatment effect and quantify the uncertainty over continuous time. To achieve this goal, a VAE-based Bayesian method was proposed to learn ODE (resp. SDE) over latent variables (resp. encoder parameters), as well as the posterior distribution of potential outcomes. An evidence lower bound was derived for optimization. Experiments on semi-synthetic data were conducted.

### Strengths
The treatment effect over continuous time is a very important and interesting topic since it can model the instantaneous effect that is beyond the scope of traditional causal modeling such as Granger causality. Besides, this paper conducted a thorough experimental analysis regarding the uncertainty quantification. The paper is well-written and easy to understand.

### Weaknesses
This paper fails to discuss the motivation for learning latent representations, which was commonly used for unstructured data. However, the experimental setting in this paper is still structured data. In this regard, why do not directly model the ODE over (treatment, covariates, and outcome)? Moreover, the introduction of latent variable $Z$ may violate the unconfoundness assumption. Specifically, the implicit causal assumption behind latent representation is $Z_t$ affects $(A_t, X_t, Y_t)$ and $Z_t 	o Z_{t'} (t' > t)$ which also effects $(A_{t'}, X_{t'}, Y_{t'})$. In this regard, an unblocked path will open from $Y_t$ and $Y_{t'}$. Besides, since $Y_t \perp A_t | X_t$, we should implement backdoor adjustment for $X_t$, which is necessary to eliminate the confounding bias. However, I fail to see such an adjustment in the paper.

### Questions
Please see the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces BNCDE which combines neural controlled differential equations with neural stochastic differential equations to model the time dimension. It leverages the Bayesian paradigm to account for both model and outcome uncertainty, allowing for uncertainty-aware treatment effect estimation in continuous time.

### Strengths
The paper focuses on the crucial task of estimating treatment effects over time in the context of personalized medicine. 

The incorporation of uncertainty quantification is a critical aspect of the proposed methodology. It allows for probabilistic estimates of treatment effects, which is essential for making informed decisions in medical contexts.

The problem setting appears to be innovative and unique.

### Weaknesses
1/ It appears that the timestamps follow a point process. Is there a method to verify if the intensity satisfies the Overlap assumption: 0 < λ(t | H_t^i) < 1? I understand that intensities in point processes can exceed 1. I believe that the number of events would be less frequent with the constraint λ(t | H_t^i) < 1. Could you please provide some insights on this?

2/ Understand that the variance of the variational posterior is often smaller than that of the true posterior. Could this potentially lead to overconfidence in uncertainty predictions?

3/ Experimental results are only on one synthetic data. Is there any real-life data or semi-synthetic data that is applicable to this model?

4/ Page 7: "we the maximize ELBO"

### Questions
Please see section Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an estimation of the treatment effects with uncertainty in continuous time by exploiting Bayesian neural controlled differential equations. The proposed method (BNCDE) is based on an encoder-decoder architecture and allows for estimating posterior predictive distributions of the potential outcomes. In the proposed method the time dimension is modeled through a coupled system of neural-controlled differential equations and neural stochastic differential equations.

### Strengths
-	The paper is clearly written and identifies the gap in the literature with clear motivation (estimating treatment effects in continuos time with uncertainty quantification). The paper is self-contained and easy to follow.
 
-	The implementation details are well documented in both the paper/appendix and the provided code.

### Weaknesses
-	Considering medical applications in mind, it is important to mention: 1) possible downsides of the proposed approach; and 2) which assumptions need to be satisfied for the method to be robust.

-	The method is only compared against other neural methods. I understand those are the most natural competitors, but this ignores a large body of literature. Are there other methods which could deal with the same setup? Or not at all?



### Questions
-	The conclusion states: “(4) Our BNCDE is further fairly robust against noise”. It would be nice to be more explicit about what “fairly” means.

-	Please discuss possible failure modes of the method. Considering that the aim is to apply it in the medical domain, this would be relevant for anyone trying to use it. 

-	In the abstract, it states: “However, existing methods for this task are limited to point estimates of the potential outcomes, whereas uncertainty estimates have been ignored.”. I believe this is an incorrect assumption. There are methods which take uncertainty into account. Are you specifically referring here to neural methods?

-	The confounding problem is not discussed in the proposed approach. As far as I understand, the baseline method is able to deal with confounders through a balancing term in the loss. Is it possible to address the problem of confounders within this framework?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a Bayesian Controlled Neural Differential Equations (BNCDE) framework aimed at estimating treatment effects in time-series data within a continuous time. The approach involves employing a Bayesian Neural Network to model the drift function of the CDE, with the posterior distribution of the neural network weights defined by the solution of a stochastic differential equation.
The authors outline a training regimen for the framework by optimizating the Evidence Lower Bound (ELBO) in an end-to-end manner. 
On the empirical side, the author includes experiments conducted on synthetic tumor growth data, with a focus on evaluating the uncertainty estimation quality of the proposed model. The results from these experiments are compared to non-Bayesian counterparts, highlighting the performance differences between the two approaches.

### Strengths
This paper proposes a treatment effect estimation framework for time series in continuous time, demonstrating a better uncertainty estimation compared to the non-Bayesian counterpart with MC dropout. I briefly checked the derivation, which seems to be correct. The presentation of method is clear in most places but there are still some ambiguities that requires further clarification.

### Weaknesses
There are two aspects that warrant further discussion, particularly in terms of its novelty and scalability. With respect to novelty, it appears that the main formulations of Stochastic Differential Equations (SDE) and Controlled Differential Equations (CDE) are derived from prior works, and the variational inference methods employed are consistent with those utilized in existing latent SDE literature [1]. This gives an impression that the current work may be an amalgamation of these previous methodologies, adapted to extend the CDE framework. Furthermore, there are noticeable similarities between this work and [2]. Despite the authors’ footnote indicating a substantial divergence from [2], there is a potential for their framework to be adaptable for time series treatment and to incorporate CDE elements. A more comprehensive discussion of the distinctions between the current work and [2] could enhance the clarity on this matter.

In terms of scalability, the neural network weights are modeled through an SDE with a neural network drift function. This configuration implies that the input dimensionality of the SDE drift scales with the dimensionality of the weights, which could potentially escalate to millions. This raises pertinent questions regarding the computational cost and the stability of the training process under such high-dimensional circumstances. An exploration of these aspects would contribute to a more thorough understanding of the framework’s practical applicability and limitations.

### Questions
1. In section 3.3, the author briefly talked about the 3 assumptions required for identifiability. To make it even more clear, the author can consider adding explicit reference or discussions regarding why those 3 assumptions can lead to identifiability. 

2. Since the potential outcome is modelled through the latent embeddings, does this affect the identifiability?

3. The prediction also estimate the outcome uncertainty. But typically, this can potential lead to the a naive model with large uncertainty. I wonder the quantification quality for the aleatoric uncertainty.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
