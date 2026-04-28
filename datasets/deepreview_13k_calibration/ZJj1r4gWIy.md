# Counterfactual Delayed Feedback Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Estimation of heterogeneous treatment effects has gathered much attention in recent years and has been widely adopted in medicine, economics, and marketing. Previous studies assumed that one of the potential outcomes of interest could be observed timely and accurately. However, a more practical scenario is that treatment takes time to produce causal effects on the outcomes. For example, drugs take time to produce medical utility for patients and users take time to purchase items after being recommended, and ignoring such delays in feedback can lead to biased estimates of heterogeneous treatment effects. To address the above problem, we study the impact of observation time on estimating heterogeneous treatment effects by further considering the potential response time that potential outcomes have. We theoretically prove the identifiability results and further propose a principled learning approach, known as CFR-DF (Counterfactual Regression with Delayed Feedback), to simultaneously learn potential response times and potential outcomes of interest. Results on both simulated and real-world datasets demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work studies causal inference in the potential outcomes framework in the super-population setting when outcomes are binary. The authors propose a model for (heterogeneous) treatment effect estimation when positive responses are observed only after some time delay; the causal estimands of interest are (a) effect of treatment on outcome (conditioned on covariate) and (b) for those individuals that would have a positive outcome regardless of treatment, effect of treatment on response time (conditioned on covariate). The work shows that both estimands are identifiable under some assumptions, proposes an EM-style algorithm for estimation, and evaluates the algorithm experimentally.

### Strengths
* The work proposes an interesting modeling problem for (heterogeneous) treatment effect estimation that seems to be reasonably-motivated by hypothetical real-world applications. The second estimand in particular is well-suited to the model. 
* Experimental evaluations compare against a variety of alternate methods and appear to be thorough.

### Weaknesses
* I had a lot of trouble understanding the model until the experimental section (see below). Additionally, I understand that delayed feedback (and the risk of 'false negatives') is a real issue in many settings where estimating treatment effect might be of interest. However, it's not obvious that *both* response time *and* observation time should be random variables; the latter seems like something that is typically fixed  and/or controlled, even in observational data. 
* It is surprising to me that only identifiability results are provided -- nothing about whether the proposed algorithm actually does the identification (e.g. unbiasedness, variance estimation/ convergence rates), which means that the strength of the method relies almost entirely on experimental results. In terms of presentation, it also would have been nice for identifiability to be formally defined.  
* The experimental setup is somewhat contrived and hard to follow -- it is not clear to me why treatment probabilities, response times and observation times should be simulated this way. 

Various presentation notes:
* Model and notation can generally be made clearer: that response times $D$ AND observation times $T$ are random variables; both taken to be in $\mathbb R$ rather than $\mathbb N$; that $D$, $Y$, and (apparently?) $T$ can depend arbitrarily on $X$. Note that lowercase $p$ will be used to denote density of $D$ and $\mathbb P$ used for (discrete) probabilities. The "given data point" discussed in on L262, i.e. the apparently-canonical data point format $(x_i, w_i, t_i, y_i^{t_i})$, should be introduced in section 2. 
* Minor, but probably good to note in preliminaries that super-population setting assumes (iid) samples from an underlying population with well-defined means etc. 
* L104, L121 sentence grammar
* Sentences at L138-L140 what conclusions? 
* L144 STUVA/SUTVA
* L377 what's $m_X$?

### Questions
* Is it important that HTE is the end-goal, rather than ATE (for either estimand)? Is the delayed feedback problem solved for ATE? 
* L406-407 / Fig 3: is this $\bar{T}$ the $\lambda$ parameter to the exponential distribution discussed on L399?
* L398 -- how does $b_D$ control heterogeneity?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper deals with a very practical scenario, where the response time is delayed. It incorporates the impact of observation time and the effect of the delays and subsequently in the likelihood estimation of the counterfactual observation. They simultaneously learn the response times and counterfactual response time. Finally, the paper shows experimental validation across several baselines.

### Strengths
I believe that there are two key strengths of the paper:

(1) Novel problem (not approach) with clear and important practical application.

(2) Neat formulation (with some caveats)

> Originality

The problem is quite new but the formulation is not quite technically challenging and hence did not require much creativity. I have some comments which I would elaborate in the weakness section.

> Soundness

The formulation is decent and sound.

### Weaknesses
(1) Notations and presentation are not clear: Note that this is not a minor suggestion but require a major revamping of the paper.
To give a few examples, $\tilde{Y}^T$ and $\tilde{Y}^t$ are used interchangeably (line 236--238). T is  random variable and t is an instantiation of the  random variable T; Equations barely have numbers; Second equation in line 229 is universally true: P(A,B) = P(A)P(B|A).
In figure (2), \tilde is used on top of D.

(2) I did not find a clear mention about what are the observed data. Is the response time given in the data?  Line 263 mentions (x_i, w_i, t_i, y_i ^t), but it does not mention D. However the paper maximizes the likelihood of D=d as well. How practical is it obtain the response time in data? Does it come through a survey? In medical treatment, the response time would be noisy. How will one take into account of them?

(3) Experiments: Are the results winning in Table 2 and 4 statistically significant? There are quite a bit overlap between the mean $\pm$ STD across numbers. I am not sure there is enough investigation in the comparison in Table 2 and 4. It was not mentioned how a baseline is adapted to take into account delayed feedback or they have been not. How are the hyperparameters tuned? 

(4) Lack of novelty: The technical contribution is a bit limited and lacks creativity, although I believe the creativity was not needed for this problem since the derivation is straight forward.  

(5) I could not find any discussions on limitations in the paper.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Different from traditional HTE estimation, the paper addresses the challenge of estimating HTE when treatment effects are delayed. From my understanding, the setting can be described as the true outcome can be censored by the observation time window. The authors propose CFR-DF, a new method that simultaneously predicts potential outcomes and response times, using an EM algorithm to handle latent variables representing the eventual potential outcomes.

### Strengths
1. The problem, from my own perspective, is interesting, novel and practice relevant. The delayed feedback censored by the observation time window is actually a very common problem for online retailers. 
2. The paper is theoretically rigor, including formulations, proofs of identifiability for both eventual outcomes and response times in specific subgroups, which reinforces the robustness and applicability of the proposed method.
3. The computational evaluation is comprehensive.
4. The paper is well written and easy to follow. I like Figure 1 a lot, which presents the problem very well.

### Weaknesses
I enjoy reading the problem formulations and theories a lot. However, my main concern is about the technical contribution.
1. The identifiability results and analysis seem to be very standard, and I am not sure whether there is any novel part the authors want to highlight.
2. The idea of introducing a latent variable for the missing information and adopting the EM algorithm is very delicate, which I really enjoy. But, at the same time, it is also a bit standard and straightforward. Are there any additional technical challenges that the authors want to point out?
3. Generally, can I think the main contribution of the paper is on the formulation side?

### Questions
Please see the weakness above.

### Soundness
3

### Presentation
4

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
The paper provides a formalization of heterogeneous treatment effect estimation with delayed response. The authors show under what assumptions identifiability is satisfied in their setup. They present an EM-algorithm called CFR-DF for this task and compare their method against standard baslines for estimating HTEs in the causal ML literature.

### Strengths
Complete piece of work: the notation is consistent, the paper is well structured, and technical proofs are provided.

### Weaknesses
- **Unclear motivation:** In medical studies, a sufficiently large time window is typically considered for a treatment response to be observed. Hence, in all relevant datasets the eventual outcome is known. As the method is trained fully offline, I do not see why there is a need for a method that models the time of delayed treatment response (if the response time is not of direct interest). Instead, this is simply a pre-processing issue.
- **Delayed feedback as censoring problem:** There is plenty of literature on censoring. I wonder whether the proposed delayed feedback could alternatively be framed as such.
- **Binary outcome:** since the outcome is binary, I do not see the benefit of this work compared to survival analysis. The paper briefly mentions this literature stream (line 116) but I do not see why this is a completely different setting.
- **Straightforward method:** the proposed CFR-DF is, to a large extent, similar to existing works and therefore fairly straightforward.
- **Restrictive assumptions:** both Monotonicity and Prinicipal Ignorability are quite restrictive for identifiability. On a more positive note, the authors state that the assumptions are difficult to verify.
- **Short term proxy literature:** There is a stream of literature that covers long-term HTEs when short-term HTEs are available. Although this is a slightly different setting, it would be fair to acknowledge this literature stream.
- **Integral Probability Metric:** The function class of the IPM is not mentioned. Different function classes result in different IPMs. This is an important detail.
- **Baseline implementation:** There are no details on baseline implementation (in particular, hyperparameter tuning). Further, I wonder if the baselines are trained on the same data or if the authors removed all instances with Y=0 and D=infinity? Based on the my understanding, the authors did the former, which may introduce a systematic bias to due incorrect/noisy observations. A simple but important baseline would be drop the mentioned observations. This would increase the variance in the estimation but likely with little impact. Likewise, another baseline would be to _add D as another covariate to the data_ (it is unclear whether this happened). Further, were the baselines trained on the eventual outcomes or the outcome at the time of treatment? This makes a large difference.


Minor: 

The paper requires proof reading. There a quite a few typos + grammar errors.

### Questions
- Why is this not a censoring problem?
- What is the key difference to the survival analysis literature?
- Why is the estimation task not simply a pre-processing problem? (see weakness)
- Can you report details on baseline implementation?
- What is the exact IPM?

### Soundness
2

### Presentation
2

### Contribution
1
