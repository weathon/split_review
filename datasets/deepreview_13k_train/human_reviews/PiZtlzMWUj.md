# SoftCVI: Contrastive variational inference with self-generated soft labels

- Decision: Accept
- Scores: 6, 5, 10, 8

## Abstract
\noindent
Estimating a distribution given access to its unnormalized density is pivotal in Bayesian inference, where the posterior is generally known only up to an unknown normalizing constant. Variational inference and Markov chain Monte Carlo methods are the predominant tools for this task; however, both are often challenging to apply reliably, particularly when the posterior has complex geometry. Here, we introduce \gls{softcvi}, which allows a family of variational objectives to be derived through a contrastive estimation framework. The approach parameterizes a classifier in terms of a variational distribution, reframing the inference task as a contrastive estimation problem aiming to identify a single true posterior sample among a set of samples. Despite this framing, we do not require positive or negative samples, but rather learn by sampling the variational distribution and computing ground truth soft classification labels from the unnormalized posterior itself. The objectives have zero variance gradient when the variational approximation is exact, without the need for specialized gradient estimators. We empirically investigate the performance on a variety of Bayesian inference tasks, using both simple (e.g. normal) and expressive (normalizing flow) variational distributions. We find that \gls{softcvi} can be used to form objectives which are stable to train and mass-covering, frequently outperforming inference with other variational approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose an approach that reformulates the inference problem as a classification task using contrastive learning and the generation of soft labels. 

These soft labels, derived from an unnormalized target distribution, are employed in a cross-entropy loss to fit the variational distribution. The authors demonstrate the efficacy of their methodology through a series of experiments on Bayesian inference.

### Strengths
The paper presents an elegant method for fitting the variational distribution by training the model to solve a classification problem. 

I identify two key benefits of the proposed approach:

1. There is no need for samples from either the negative or the target distribution.
2. The densities of the target and negative distributions need only be known up to a normalizing constant.

Overall, the paper is well-written and easy to follow.

### Weaknesses
I note the following weaknesses in the paper:

### Major:

1. Deep Learning examples:

The experimental evaluation feels modest and misses an opportunity to show the benefits of the proposed methodology in deep learning scenarios. The authors focus solely on "classical" examples of Bayesian inference. I think it would be very illustrative to consider deep learning applications.

For example, in the related work section, the authors mention papers on Variational Auto-Encoders (VAE). It would be interesting to see how the proposed methodology performs in this context.

I see several ways your approach could be applied:

- End-to-End VAE training: Instead of optimizing the standard ELBO (or alternatives like IWAE [1]), incorporate the SoftCVI training procedure and evaluate the negative log-likelihood.
- Fitting variational distribution for pretrained VAE: For an already pretrained VAE (decoder) with a complex, multimodal posterior, apply your training procedure to fit a variational distribution to this posterior. Then demonstrate that the variational distribution fitted with SoftCVI covers more modes and provides more diverse samples (see e.g. [2]).

I appreciate the example with the SLCP task. Similarly, an example with a "circular" posterior in [3] could be considered for demonstration.

2. Training curves with different $K$:

Since $K$ is a hyperparameter we can choose as we wish, it's important to understand how it influences the results. In Figures 1 and 6, two different choices of $K$ are considered, but there is no discussion on which is better. It would be beneficial to see not only the final evaluations but also the training curves for different $K$ values. Given that $K$ can range widely (from 2 to infinity), practical guidance on selecting $K$ would be valuable.

Additionally, training curves are interesting in the context of comparison with SNIS-fKL, as the variance of estimation will be greater there, and it is interesting to see it.

### Minor:

1. Motivation in Section 2.1:

Initially, I found the beginning of Section 2.1 a bit confusing. It mentions a scenario with $K−1$ negative samples and only 1 positive, which doesn't seem to match the scenario in the paper. As I understand it, we have samples only from the proposal distribution and assign probabilities to them as if they come from the true distribution to generate soft labels. We don't assume that only one sample comes from the true distribution. If my understanding is incorrect, please clarify. Otherwise, consider rephrasing this section for clarity.


2. Typo:

Line 329: "in contrast **to to**".

### Questions
1. In line 57, the authors mention proposing **a family of variational objectives**. Could you clarify this point? It seems that there is only one objective—the cross-entropy between true soft labels and the predicted categorical distribution. Is there indeed a family of objectives, or is it a single objective?

2. [questions from Weaknesses] How does the choice of $K$ influence the training curves and final results? Is there an optimal value for $K$? What criteria should be used to select $K$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers a variational inference approach that builds upon classifying ‘noisy’ samples from a learned proposal distribution as negative samples, similar to a noise contrastive estimation approach, and where ‘ground truth soft labels’ depend on a self-normalised importance sampling estimate for the log ratio of the target density relative to the proposal density. In contrast to a classical ELBO minimizing the reverse KL to the target, the suggested approach appears to better approximate the forward KL to the target. Numerical experiments on benchmark Bayesian inference problems illustrate that suggested approach yields te better coverage probabilities and yields to approximations with less bias for the posterior mean estimate.

### Strengths
The paper addresses the classic and important question of Bayesian inference, particularly for the challenging setting where the approximate posterior should be close to the target with respect to the forward KL to yield well calibrated inferences. The approach avoids previous objectives that yield mass-covering behaviour, but are more challenging to optimise, particular in high dimensions. The suggested objective is now as far as I am aware. It is also very interesting that the suggested approach can be used to construct a previously constructed objective (SNIS-fKL), but with a gradient estimator that has zero variance in the idealised setting when the approximate posterior coincides with the true posterior. Experiments do indeed show that the suggested method improves the coverage and leads to approximate posterior that are closer to the target in terms of the forward KL.

### Weaknesses
The empirical verification seems a bit limited. In particular, the only baseline (beyond a standard ELBO) is the SNIS-fKL objective. However, as the paper shows, they have the same expected gradients. It is thus not clear how well the suggested approach compares to other (approximate) Bayesian methods that have different averaged gradients, e.g. [1-3].

Also as the suggested approach has a higher computation complexity requiring sampling and density-evaluations of K particles, evaluations with a simple IWAE approach instead of the ELBO baseline appears appropriate.

The authors consider (in Section 2.1) that they have access to samples from the true posterior. However, is having access to samples from the true posterior not the aim of the method? In (4), is $y$ equal to $\hat{y}$ as in Algorithm 1 when one does not have true posterior samples?

It is not clear why eq. (4) is the right objective to optimise when one does not have access to the true labels $y$. Does optimizing it correspond to some proper scoring rule or divergence [4] that are minimized for this objective?

Can you clarify why the optimal classifier recovers the true posterior and that the true posterior is equal to the approximate variational distribution as per eq. (6)? The ‘optimal classifier parameterized as in eq. (3)’ depends (apparently?) on the number of samples $K$ from the proposal and on the proposal distribution. Do all the arguments on page 3 from line 141 not depend on these choices? I understand that the classifier is optimal with respect to a cross-entropy loss if it recovers the Bayesian posterior [4]. But is this optimality even realisable in the suggested form (3)?

The experiments target posteriors that are not that high-dimensional (<=200). Does the method scale to high-dimensional problems? Does it overcome scalability issues commonly faced when optimizing the forward KL or for importance sampling?

### Questions
It would be helpful if the paper is a bit clearer what kind of reference posteriors are used. Are they from MCMC algorithms that can be assumed to closely approximate the true posterior? What about the SBI posteriors?

Re line 127, can you elaborate what is the exact parameterisation of the classifier in terms of the ratio of two distributions. Are the parameters (infinite-dimensional) probability densities?

Can you clarify why you compare against simulation-based reference models (SBI)? How is the proposed approach applicable without having access to the likelihood function?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper proposes a new way to approximate the posterior distribution over parameters for a parametric model $p(x;\theta)$. 

The approach:
* defines 2 multinomial distributions:
   *  $y(\\{\theta_k\\})$ over the index $k$ of $K$ parameter samples $\theta_k$ as a function of the model $p(x,\theta)$ and noise distribution; 
   * $\hat{y}(\\{\theta_k\\})$ as a function of the parameterised approximate posterior $q_\phi(\theta)$ and the noise distribution;
* $\hat{y}$ is trained to match $y$ under cross entropy loss;
* at optimality $q_\phi(\theta)$ matches the true posterior $p(\theta|x)$ (subject to the choice of the parametric family $q_\phi$).

Results compare the proposed method to typical amortised variational inference (maximising the ELBO) and a more similar method, showing improved outcomes on those datasets.

### Strengths
* The proposed method makes sense and appears straight-forward to implement. 
* The method appears general to problems with a parametric model where $p(x,\theta)$ can be computed.
* Comparison to SNIS is revealing and clear.

### Weaknesses
Overall I like the paper, find it to be of high quality and soundness and the proposed method is a clever trick that converts a difficult problem into a simpler classification-type task. Areas in which the paper could improve (from good to excellent) are: 

**Clarity**: as someone familiar with this field but not immersed in it, the paper could be clearer to read. As specific examples:
* [033, 078] From the outset, the paper refers to *latent variables*, which often refer to variables that are one-to-one with data samples, whereas the term *parameters* typically relates to global variables of the model, i.e. common across all samples. (Of course parameters are often treated as unobserved, hence latent, variables). I appreciate that this may be subjective, but I find it to be fairly universal and a useful distinction, so this phrase put the wrong starting point in my mind. I was wondering throughout when "parameters of the model" get updated and only when I reached the experiments did it become clear that it is about parameters and it made more sense. I would suggest referring to "parameters" (treated as latent variables).
* The preamble to Eq 2 is not directly relevant and could be more clear: labels y are constructed analytically and the approximate posterior is trained by learning to predict them. The backstory of predicting k* doesn't seem so relevant (as it is in NCE, say) so this bit threw me off until I realised that.
* [202-213] This part stands out as less precise relative to preceding arguments. The method trains one ratio of ratios to match another ratio of ratios using cross entropy loss. Reference to "classification being too easy" and "punishing" seems out of place and unclear. The issue seems to be the relative range of values in the softmax function (+/- numerical instability?), which is mentioned but blended with loose wording. This part could be improved, particularly as computing these ratios/choosing the negative sampling distribution is the crux and potential pitfall of ratio estimation.
* [161] Ensuring $\pi$ covers the true posterior - I can't see how this is "guaranteed", unless pi is diffuse, which sounds problematic for ratios.
* Experiments: to compute a posterior, you need a prior, but the priors don't seem clearly specified.
* Fig 1: how are some log probability values positive?
* GARCH experiment: The descriptions of $\alpha_1$ and $\beta_1$ are rather vague.

**Analysis/Experiments**: For such a widely applicable method, the experiments to showcase its efficacy/analyse performance etc seem thin. 
* Understanding how well it works in higher dimensions is of interest, where potentially finding a negative distribution close to the true posterior could be less straightforward.
* Understanding how the methods compare as number of data points increases is of interest to know when the method is most applicable.
* Understanding how the methods compare when the posterior is mis-specified is of interest to understand robustness (mode seeking may be preferable to distribution covering?).

Minor
* [134] it would aid clarity to explicitly say optimisation is "with respect to $\phi$"
* [134] it would be much clearer to state labels y "(from Eq 2)".
* [370] "a different observation" of what?
* [421-424] the paper does well to be relatively self-contained, this part could be made more clear to the less familiar reader.

### Questions
* 50k "optimisation steps": this sounds a lot, any explanation for this? What is the definition of step?
* K=8: Any ablation of the effect of K on accuracy vs wall-clock time? i.e. trade off in slower steps vs number of steps
     * Fig 6 (K=2) is hard to compare to Fig 1 (K=8) due to their separation and the SNIS result dominates the scale, squashing up the rest.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes SoftCVI, a variational inference method based on contrastive learning that uses soft labels, i.e., binary classification probabilities. SoftCVI reframes fitting a variational distribution as finding a classifier to identify actual posterior samples among a set of samples. The paper claims that:
  1. SoftCVI works without having access to samples from the posterior.
  2. SoftCVI forms objectives that are mass-covering.
  3. SoftCVI yields better posterior approximation than baselines with simple and flexible variational distributions.

### Strengths
## Reason for score
- The presentation is lucid.
- The derivations look good,  aside from a couple of technicalities (see questions).
- Using soft labels in contrastive learning for Bayesian inference is exciting and novel.
- The connection to SNIS-fKL is clear, and viewing the gradient of eq. 7 as a control variate is insightful and supported by evidence.
- Experimenting with normal and normalizing flow variational distribution demonstrates SoftCVI's flexibility, and the results support that SoftCVI is more mass-covering than ELBO and SNIS-fKL.

### Weaknesses
 - It is unclear whether the variational distribution is a biased estimator of the posterior. Please see the questions.

 - It is unclear what is meant by a stable objective (line 064). Is numerical stability, stable convergence or something else? What evidence is there for the type of stability claimed?

 - Why does the equation after eq.4 hold (line 146)? It seems like there is a population limit ($\lim_{K \rightarrow \infty}$) missing. Is this the case? Otherwise, please explain why this is not necessary.

 - The article establishes that $\alpha=0$ leads to leakage and that $\alpha=0.75$ is an good choice for the experiments. How do you suggest deciding $\alpha$? Could you provide theoretical justification or guidelines for choosing in practice $\alpha$? And, is there a threshold under which $\alpha$ will lead to leakage, or is this only the case for $\alpha=0$?

 - Could you explain the second equality in the derivation leading to eq. 26? For example, by a step-by-step derivation.

 - The claim that the parametric variational distribution can recover the posterior exactly under only a support constraint (lines 143-144) seems odd. Is there a condition that the posterior is contained within the parametric variational family missing? If so, please add this and any other assumption to the paragraph. If not, explain the flaw in the following case: Let the posterior $p(\theta|\mathcal{D})$ be multi-modal (for example, a mixture posterior) and the variational distribution parameterized by $\phi$ be unimodal, e.g., Gaussian, both supported on the real line. By construction, we would have that $\forall \phi.p(\theta|\mathcal{D}) \not = q_\phi(\theta)$ contradicting the claim in lines 143-144 that there $\exists \phi. p(\theta|\mathcal{D}) = q_\phi(\theta)$ namely the $\phi$ that parameterizes the optimal classifier from eq. 3.

### Questions
1. Given the connection between SNIS-fKL and SoftCVI and that MC estimation of the SNIS-fKL objective is a biased estimation of the forward KL, does SoftCVI give a biased estimation of the posterior when $p^-(\theta)=\pi(\theta)=q_w(\theta)$? Could you clarify whether SoftCVI with $p^-(\theta)=q(\theta)^\alpha$ gives a biased estimation of the posterior?
2. What is claimed when stating that SoftCVI enables a stable objective (line 064)? Is numerical stability, stable convergence or something else? What evidence is there for the type of stability claimed?
3. Why does the equation after eq.4 hold (line 146)? It seems like there is a population limit ($\lim_{K \rightarrow \infty}$) missing. Is this the case? Otherwise, please explain why this is not necessary.
4. The article establishes that $\alpha=0$ leads to leakage and that $\alpha=0.75$ is an good choice for the experiments. How do you suggest deciding $\alpha$? Could you provide theoretical justification or guidelines for choosing in practice $\alpha$? And, is there a threshold under which $\alpha$ will lead to leakage, or is this only the case for $\alpha=0$?
5. Could you explain the second equality in the derivation leading to eq. 26? For example, by a step-by-step derivation.
6. The claim that the parametric variational distribution can recover the posterior exactly under only a support constraint (lines 143-144) seems odd. Is there a condition that the posterior is contained within the parametric variational family missing? If so, please add this and any other assumption to the paragraph. If not, explain the flaw in the following case: Let the posterior $p(\theta|\mathcal{D})$ be multi-modal (for example, a mixture posterior) and the variational distribution parameterized by $\phi$ be unimodal, e.g., Gaussian, both supported on the real line. By construction, we would have that $\forall \phi.p(\theta|\mathcal{D}) \not = q_\phi(\theta)$ contradicting the claim in lines 143-144 that there $\exists \phi. p(\theta|\mathcal{D}) = q_\phi(\theta)$ namely the $\phi$ that parameterizes the optimal classifier from eq. 3.

### Soundness
3

### Presentation
4

### Contribution
3
