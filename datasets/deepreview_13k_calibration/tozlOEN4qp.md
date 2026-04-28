# Heavy-Tailed Diffusion Models

- Decision: Accept
- Avg Score: 6.17
- Scores: 6, 6, 6, 8, 3, 8

## Abstract
Diffusion models achieve state-of-the-art generation quality across many applications, but their ability to capture rare or extreme events in heavy-tailed distributions remains unclear. In this work, we show that traditional diffusion and flow-matching models with standard Gaussian priors fail to capture heavy-tailed behavior. We address this by repurposing the diffusion framework for heavy-tail estimation using multivariate Student-t distributions. We develop a tailored perturbation kernel and derive the denoising posterior based on the conditional Student-t distribution for the backward process. Inspired by $\gamma$-divergence for heavy-tailed distributions, we derive a training objective for heavy-tailed denoisers. The resulting framework introduces controllable tail generation using only a single scalar hyperparameter, making it easily tunable for diverse real-world distributions. As specific instantiations of our framework, we introduce \emph{t-EDM} and \emph{t-Flow}, extensions of existing diffusion and flow models that employ a Student-t prior. Remarkably, our approach is readily compatible with standard Gaussian diffusion models and requires only minimal code changes. Empirically, we show that our \emph{t-EDM} and \emph{t-Flow} outperform standard diffusion models in heavy-tail estimation on high-resolution weather datasets in which generating rare and extreme events is crucial.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors provide a framework, termed t-EDM, for diffusion models where the added noise is heavy-tailed, following a Student-t distribution. They build upon the EDM introduced by Karras et al 2022. Interestingly, starting with the EDM framework, replacing the Gaussian noise by the Student-t distribution and changing the KL divergence in the objective function to $\gamma-$Power Divergence for a specific $\gamma$ leads to same loss function as that of the EDM, except that the noisy state is now drawn from a Student-t distribution. This is of practical interest since their framework can be obtained by only performing minimal changes to previous implementations of EDM. It is of theoretical interest that since the Student-t distribution with $\nu$ degrees of freedom converges to a Gaussian distribution as $\nu$ goes to infinity, t-EDM is a generalization of the EDM. The authors provide experiments on weather prediction showing that t-EDM outperforms EDM for both unconditional and conditional generation for certain metrics.

### Strengths
The t-EDM provides a straightforward and mathematically justified extension for diffusion models to heavy-tailed data. This is to be compared, for instance, to Yoon et al (2023) who also provide a framework for heavy-tailed diffusion models (using Levy processes), but whose implementation requires heavier mathematics and to make the model work in practice they make theoretically unjustified changes to the model. 

The authors do a good job presenting the concepts as natural extensions of what was already known in the field. 

The experiments make the case for t-EDM being useful for weather modeling, an application that requires capturing tails and extreme events. Although the present reviewer is not knowledgable in this application, it is clear that having an extension of EDM to heavy-tails is an important contribution to scientists working on weather forecasting and several other natural science applications. It is especially useful that this implementation requires only minimal changes over previous EDM implementation, so it is quick to implement for practitioners.

One advantage of the t-EDM is that it has a free parameter $\nu$ that can be tuned to model different datasets (see results in Table 4), providing a flexible framework useful for practitioners. 

Yoon, E. B., Park, K., Kim, S., & Lim, S. (2023). Score-based Generative Models with Lévy Processes. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, & S. Levine (Eds.), Advances in Neural Information Processing Systems (Vol. 36, pp. 40694–40707). Curran Associates, Inc.

### Weaknesses
The experiments for unconditional generation in Table 2 show that the EDM (using preconditioning) outperforms the t-EDM for the KR and SR metric in the VIL channel with test data. This hinders the claim the authors make that standard diffusion models, even with preconditioning, fail to capture the heavy-tailed distributions (line 043) and that t-EDM outperforms standard diffusion models. Qualitatively, the plots in Figure 3 do show that t-EDM outperforms EDM with preconditioning in capturing the heavy-tailed behavior. However, I believe a justification of why the KR and SR metrics do not reflect this should be included. As addressed in Appendix F.2, this metrics rely on flattening the data. This may be one reason, but the metric KS also relies on flattening the data but does show that t-EDM outperforms EDM. In any case, I believe a more throrough justification or explanation is needed here.

Also see questions regarding preconditioning for EDM vs t-EDM. If these questions are successfully addressed I will raise my score.

Smaller comments: 
* in line 198 there is a typo, the equal is in the subscript and it should not.

### Questions
Questions
* Since the preconditioning for EDM helps a good amount for unconditional generation (see Table 2), is not there some preconditioning for EDM in a similar spirit to the unconditional case that could help for the conditional generation case?
* As mentioned in strengths the t-EDM has a free parameter $\nu$ that can be tuned to predict more accurately the heavy-tail behavior for different datasets. However, the INC preconditioning for the EDM could be given a parameter by reparameterizing into a normal with variance $\sigma^2$ instead of a standard normal. (More precisely, this means that in step 4 in Baseline 2 in Appendix C.1.2. we would replace 'standard Normal distribution' to centered normal distribution with variance $\sigma^2.$) This change in variance is qualitatively different from a change in decay (which is what happens when we vary $\nu$) so this approach may not be theoretically justified, but it may work in practice. The PCP preconditioning already has parameters. Is there any claim for INC/PCP that can be made about whether tuning this parameters helps or not in capturing different type of heavy-tail distributions?

In summary, I am wondering if the performance of EDM can be increased only by preconditioning to reach that of t-EDM or if t-EDM does provide a significant difference not achievable by preconditioning.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper adds to the line of work investigating training diffusion models using heavy-tailed noise. Specifically the paper investigates the setting where the increments of noise added in a discrete diffusion model are drawn from a student T distribution.

New methods are developed for training the diffusion model based on power divergences.

### Strengths
- The paper introduces a new way of training a score based model with heavy tailed noise, based on the student t distribution, and shows clear benefits in training.
- The experimental results are reasonably convincing.

### Weaknesses
 - The paper fails to discuss previous work, for example "Heavy-tailed denoising score matching" covering the subject matter.
- The paper lacks experiments on synthetic data which is generated as heavy tailed. While not needed, I believe it would help make the case that this method definitively helps with modeling heavy tails by demonstrating it on definitively heavy tailed data.



### Questions
- Can the authors comment on the draw backs of using student t noise discussed in "Heavy-tailed denoising score matching" and why this makes sense in the context proposed?
- proposition 2 to me is not well defined. The construction of the stochastic process with student t increments. Can the authors discuss how such a process is constructed in more detail?
- In the proof of proposition 2 the authors derive the last term converging to Brownian motion, not a student process, can they please comment on this discrepancy.
- It seems unintuitive to define a diffusion model via its finite increments, only to show it converges to a continuous time diffusion and later make use of this perspective. Can the authors comment on why the did not simply define the noising process as a student-t diffusion in the first place and later discretise this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Diffusion models are widely used, but there has been little work studying how well they capture extreme events in the tail of distributions. This is especially important in environmental prediction where extreme events are often the ones that we care most about. This paper shows that standard approaches can fail to capture the extremes accurately. It develops a new form of diffusion by leveraging the multivariate Student-t distribution to form new noising and denoising processes in discrete and continuous time. It develops a method to fit these new processes using a power-divergence which avoids the intractability of the ELBO.  It then applies the new methods to modelling a pair of variables from HRRR, NOAA’s high-resolution local area system for the continental US. This product has recently been a focus of AI diffusion emulators e.g. in NVIDIA’s StormCast.

### Strengths
I really liked the problem the paper was looking into — better characterisation of extremes in diffusion and flow based generative models — especially in the context of environmental forecasting.  I think that this is an important practical problem. I also liked the use of a simple example to analyse how well diffusion models capture tail behaviour. (In fact I would have liked to have seen more investigation to toy examples of this sort to pin down the failure models of diffusion more generally.) 

 I thought the writing was very clear and struck a good balance between communicating technical content and the high level idea. 

The technical contribution is interesting. I liked the fact that the authors provide both the discrete-time version and the continuous-time version of the new approach. The use of the power-divergence for producing a more tractable training objective was creative. 

HRRR was a sensible domain to test the new method on. A range of sensible metrics that are used by practitioners e.g. CRPS for the forecasting experiments. I liked the simple modifications to EDM using the inverse CDF transform and per-channel preconditioning.

### Weaknesses
I would have liked to have seen a bit more clarity on the formulation of the denoising process (the sub-optimalities here seem significantly more severe than in the Gaussian case, see questions below for more detail). The use of the power-divergence for training was creative, but connecting the parameters of the model to the divergence parameters also seemed sub-optimal as it does not allow the framework to learn the degree of freedom parameter in the student-t distribution. 

The experimentation was a little light in that only two variables were considered in the conditional and unconditional settings, there were no experiments that considered forecasting multiple variables at one time, or autoregressive rollouts.

Setting the degree of freedom parameter via a parameter sweep is a bit painful. It’s a shame that it can’t be learned directly, especially if it is going to be different for different dimensions of x  (locations / variables / pressure levels etc.).

### Questions
Figure 1 - I liked this! I thought it could be improved by adding axis labels including a description of what the colour map shows (log ground truth density?), calling the original density “ground truth” ("original hists” in the legend was slightly cryptic),  would add axis labels. 

I was a bit confused by the notation around the degree of freedom parameter v. Initially in figure 1 it is a vector, then in equation 2 it is a scalar, but then in the equations on line 155 we switch back to a vector with t_{2d}() being a composition of d independent 2-dimensional multivariate student-t distributions (although this isn’t explained). The issue around clarity here bleeds into the discussion of the divergences where then the divergence parameter \gamma would depend on the dimension. Balancing notational clarity and correctness is tricky here — perhaps say that "we’ll consider v to be constant across dimensions for the mathematical development, but the generalisation is simple" somewhere early on to clarify these issues?

There is a lack of clarity in my mind around the noising process and the approximations made when arriving at the denoising equation (equation 5). Wouldn’t the true denoising process be non-Markov? If you consider the student-t as a Gaussian scale mixture, I believe the latent scale parameter in your noising construction is effectively shared across all time-steps (a consequence of the equations on line 155). So, when generating x_t the whole history of previous x_{t+1:T} will inform us about the latent scale and so p(x_t | x_{t+1:T}) \ne  p(x_t | x_{t+1}). Have I misunderstood? Moreover, dropping the data dependent coefficient (v+d_1)/(v+d) is rather glossed over. In the Gaussian setting, dropping this can be somewhat justified by 1. it being an exact choice in the limit of small step sizes, and 2. at least it’s exact when the true distribution of x_0 is Gaussian. In the current case neither of these statements hold I believe. I felt that this should be discussed as the suboptimality of this choice in this case is likely far larger than in the usual case.  Finally, could you clarify how the continuous case fits in with this? I presume, both of the approximations mentioned above are made, and then we take the continuum limit?

Connecting the specific divergence used to a parameters in the model / denoising process (i.e. \gamma = 2/(v+d)) might be limiting e.g. the objective now can’t be used to learn the degree of freedom, the optimisation objective (8) cannot be used to compare between models that use different settings for v. Also, the correspondence to the traditional objective only then holds as q becomes Gaussian (ideally you’d like to recover the original ELBO without having to limit the model back to the DDPM). I’d have liked to have seen more discussion of this point. 

In table 1, it might be useful to add p(x_T) for the two cases (by the way do you mention somewhere that q(x_T) is a product of student-ts and that you set p(x_T) = q(x_T))?

Why not consider surface fields, arguably where modelling extremes have most impact? 

Have you considered a baseline that trains the EDM and then uses a base distribution for generation which is zero-mean unit-variance student-t, sweeping the degree of freedom parameter to find a suitable one? 

For the HRRR experiments, I presume that you are training off HRRR analysis (rather than, say forecasts) this should be mentioned (I didn’t see it in the main text or in the appendix). Also, is the time interval between inputs mentioned? Is it 1hr like in StormCast? 

The spatial fields shown in the appendix were useful. For the forecasts results shown in figure 8 and 9, it would be useful to show the persistence forecast.

For the unconditional sampling, it looks like on the test set t-EDM outperforms the baselines 1/3 of the time (and only on the KS metric). 

Is the KS metric to be more trusted? Why weren’t the other metrics applied to the forecasting case too? 

It would be interesting to see how t-Flow behaved during auto-regressive rollouts. I could imagine that the under-dispersion of EDM might actually help maintain stability in these cases, whereas heavier tails could lead to greater instability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel approach to adapting diffusion models for heavy-tail estimation by leveraging multivariate Student-t distributions. This method addresses the limitations of traditional Gaussian-based diffusion models in capturing rare or extreme events, which is particularly relevant for applications such as weather forecasting. The authors introduce extensions of existing diffusion and flow models, termed t-EDM and t-Flow, which utilize a Student-t prior to enable controllable tail generation through a single scalar hyperparameter. The framework is compatible with standard Gaussian diffusion models and requires minimal code changes. Empirical validation on high-resolution datasets, such as the HRRR weather dataset, demonstrates that the proposed t-EDM outperforms existing diffusion models in accurately modeling heavy-tailed distributions.

### Strengths
1. The use of multivariate Student-t distributions for diffusion models is innovative, allowing the model to better capture rare or extreme events with controllable tail behavior through a hyperparameter. It is a very brilliant idea. 
2. The overall presentation of this paper is very clear and understandable. 
3. As an extension of previous EDM and Rectified Flow, the authors established a new framework for Student-T distribution and flow, which is able to capture the rare events more effectively. 
4. The authors provide theoretical backing for their approach, linking it to robust statistical estimators and demonstrating its foundation in existing heavy-tailed distribution literature.
5. Choosing the weather dataset to verify the effectiveness is a great idea, and is novel.

### Weaknesses
I like this paper a lot and I believe there are no major weakness. The only thing is that, there are some duplicated references in the reference list.

### Questions
1.  Can the authors discuss potential applications in other domains where rare events or extreme values are important, such as finance, seismology, or network traffic analysis. This would help demonstrate the broader impact of the method beyond just weather forecasting.
2. Do you think it possible to extend your framework into other heavy-tailed distributions beyond the Student-t, such as the Cauchy or Lévy distributions, or even unifying all these classes of perturbation kernels? Are there any theoretical or practical challenges you foresee in such extensions?

### Soundness
4

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
4

### Summary
The paper proposes a novel generative model that, in a sense, mirrors traditional diffusion models (DM) by substituting Gaussian noise in the noising process with noise following a Student’s t-distribution.

More precisely, the authors introduce a sequence of joint conditional distributions $q_{t-\Delta t, t}(x_{t-\Delta t, t} \,|\, x_0)$ over $\mathbb{R}^{2d}$, which are Student distributions with mean $[\mu_{t - \Delta t} x_0, \mu_t x_0]$, covariance matrix $\Sigma_t$, and degrees of freedom parameter $\nu > 1$. Leveraging properties of conditional Student distributions, they demonstrate that the marginals of $q_{t-\Delta t, t}(x_{t-\Delta t, t} \,|\, x_0)$ are also Student-distributed, as are the conditional distributions. Given a family of transitions 
$p_{t-\Delta t \, |\, t}$, the authors fit this family by minimizing a modified DM loss, where the standard Kullback-Leibler divergence is replaced with a power divergence. They then incorporate their chosen conditionals $q_{t-\Delta t, t}(x_{t-\Delta t, t} \,|\, x_0)$. Finally, the developed methodology is benchmarked against standard EDM and several of its variations for generating dynamical variables in the High-Resolution Rapid Refresh dataset.

### Strengths
The approach appears interesting and addresses a relevant problem. Also, the methodology can be straightforwardly implemented using existing DM frameworks.

### Weaknesses
In my opinion, there are several key points the authors should address.

First, a major concern is the soundness of the proposed method. In particular, it is unclear to me that the sequence of conditional distributions $ q $ introduced by the authors genuinely defines a Markov noising process. The authors define $q_{t-\Delta t, t}(x_{t-\Delta t, t} \,|\, x_0)$ as a joint distribution, but it is not clear that this construction leads to a Markov chain $x_0 \rightarrow x_{\Delta t} \rightarrow x_{2\Delta t} \rightarrow ...$ where each transition only depends on the previous state. This is crucial for the validity of the diffusion process. As such, the loss function they employ does not appear to serve as a meaningful metric. More precisely, it remains uncertain why this loss function would serve as a good proxy for measuring discrepancies between the model marginal $p_0^{\theta}$ and the data distribution. The authors acknowledge that the loss function is not a proper ELBO and claim that the limiting diffusion model is a special case of their method, but further justification of the loss function is needed.

My second concern relates to the results and mathematical formalism of the paper. The mathematical treatment seems quite weak. For instance, the proof in the first section of the appendix contains several typos and appears incorrect in its current form. The reference to Ding (2016) would be sufficient, as it already includes the result. I also found Proposition 2 challenging to interpret, and the accompanying proof does not clarify matters. For example, it is unclear what $f$ and $g$ represent, whether they are any functions satisfying the proposition's conditions, and whether such functions exist. The lack of specific constraints on $f$ and $g$ makes the proposition difficult to assess. Similarly, the term $ dS_t \sim t_d(0, dt, \nu + d)$ lacks clarity. It is not clear how this stochastic differential is defined, and what its properties are. I am also unclear on the main conclusions to be drawn from Proposition 2.

My third concern is related to the experiments and the metrics used. First, there is a large gap in performance when using $\nu = 3$ versus $\nu = 5$, raising questions about the robustness and reliability of the method. This gap suggests that the chosen metrics (KR, KS, SR) might be sensitive only to the tails of the target distributions. Additional metrics such as precision, recall, and density coverage could provide a more balanced assessment. Moreover, the claims regarding t-EDM's performance appear somewhat overstated, given the tables and the likely margin of error. In my opinion, the experiments should include toy examples for a deeper comparison with existing diffusion models.

Finally, the authors should provide a comprehensive literature review on extensions of diffusion models, acknowledging previous relevant works. The current literature review is too limited.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method for adapting denoising diffusion models to sample from heavy tailed distributions. The core idea is to replace the Gaussian prior and transition distributions from standard DDPM with Student-t distributions. The authors show how to construct a heavy-tailed diffusion model by defining the relevant noising process in terms of the Student-t distribution, calculating the corresponding reverse noising process, showing how it can be appropriately parameterized in terms of a prediction of $x_0$, and deriving a training objective defined in terms of the $\gamma$-Power Divergence by analogy to the standard KL objective used to train diffusion models. They then demonstrate the empirical success of their method on distributions from the HRRR dataset, showing that it outperforms Gaussian-based diffusion models in most settings they study.

### Strengths
My overall feeling is that this is a very technically solid paper which takes a relatively simple core idea - exchanging the Gaussian distributions in diffusion models for Student-t distributions in order to have a heavy-tailed sampling distribution - and executes on it methodically and very well. The presentation and flow of the argument is clear throughout, and all the obvious questions (parameterization of the reverse process, tractable training objective, continuous-time sampling with SDEs and ODEs, empirical performance) are dealt with comprehensively in my opinion.

The problem of sampling from heavy-tailed distributions is one of significant interest to the field, and I'm not aware of other work providing such a nice and integrated framework for heavy-tailed diffusion modeling, so I consider the contribution of an appropriate size for the conference.

Particular highlights were the connection of the diffusion modeling loss to the $\gamma$-Power Divergence, showing that this choice of divergence makes the loss tractable and reduces to a denoising $L^2$ loss similar to that of DDPM, and the discussion in Section 5 on various theoretical intuitions and insights the authors have concerning their framework.

### Weaknesses
I do not think this paper has any major weaknesses. The addition I would be most keen to see is a more thorough discussion of the results in Tables 2 and 3 (empirical results in the unconditional setting). For example, it would appear from Table that in the test setting for VIL, their method actually underperforms compared to EDM (+PCP) and compared to EDM (+INC) in the other setting, and the authors do not discuss this in the text as far as I can tell. (Though, Figure 3 tells a somewhat different story, and I can't work out how to reconcile the two - see question below.) The authors also don't really discuss the results in Table 3 in the main body, and a short commend about what we should take from those results might be appropriate.

Secondly, I also feel that many of the derivations in the work are somewhat routine once one has the core idea of using Student-t distributions to parameterize the forward process, and the novelty of the work is therefore not outstanding. Nevertheless, the problem is of sufficient interest and the execution of the authors is sufficiently good that I believe this still clearly merits acceptance to the conference.

### Questions
- How do we tune the parameter $\nu$ in practice? It looks from Table 3 like the choice matters a lot, so it might be nice to say something about how one should choose a suitable value of $\nu$ or know that one has found a good value.
- How confident are you that the 1-dimensional summary statistics you are looking in Table 2 (and maybe Table 3 also) at appropriate? From looking at Figure 3, t-EDM seems clearly qualitatively superior to the other methods. The fact that this is not reflected in the summary statistics in Table 2 makes me suspect the summary statistics are not capturing the most relevant aspects of the distributions.

### Soundness
4

### Presentation
4

### Contribution
3
