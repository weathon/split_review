# IMPLICIT VARIATIONAL REJECTION SAMPLING

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Traditional approaches to variational inference rely on parametric families of variational distributions,
with the choice of family playing a critical role in determining the accuracy of the resulting posterior approximation.
Simple mean-field families often lead to poor approximations, while rich families of distributions like normalizing
flows can be difficult to optimize and usually do not incorporate the known structure of the target distribution
due to their black-box nature.
To expand the space of flexible variational families, 
we revisit Variational Rejection Sampling (VRS) \citep{grover2018variational}, which combines a parametric
proposal distribution with rejection sampling to define a rich non-parametric family of distributions that
explicitly utilizes the known target distribution.
By introducing a low-variance reparameterized gradient estimator for the parameters of the proposal distribution,
we make VRS an attractive inference strategy for models with continuous latent variables. 
We argue theoretically and demonstrate empirically that the resulting method---Reparameterized Variational 
Rejection Sampling (RVRS)---offers an attractive trade-off between computational cost and inference fidelity.
In experiments we show that our method performs well in practice and that it is
well-suited for black-box inference, especially for models with local latent variables. % in probabilistic programming frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel approach that leverages neural networks to construct implicit proposal distributions, incorporating rejection sampling for improved efficiency. 
Additionally, it employs a discriminator network to estimate the density ratio between the implicit proposal and target distributions. Building on this, the paper proposes a refined Implicit Resampling Evidence Lower Bound (IR-ELBO) to enhance accuracy. 
The proposed method is evaluated against existing variational inference (VI) techniques through a series of experiments, demonstrating its effectiveness.

### Strengths
1. The paper is well-written, providing a clear presentation of the background, related work, major challenges, and the strategies employed to address each challenge.
2. The use of rejection sampling to enhance the accuracy of implicit variational inference is straightforward yet effective.
3. By improving the accuracy of implicit variational inference, the paper enables the construction of a tighter Evidence Lower Bound (ELBO).

### Weaknesses
1. Variational inference is typically employed to avoid direct sampling from complex target distributions, thus enhancing sampling efficiency. 
However, the algorithm proposed in this paper requires an additional discriminator network to estimate the acceptance probability and density ratio. 
Additionally, there is a manually tuned parameter, $M$, which must be selected via cross-validation. 
In high-dimensional or large-scale settings, this approach could become computationally intensive due to the overhead of training the discriminator network and optimizing the hyperparameter $M$. Specifically, the discriminator network introduces a computational bottleneck, as it needs to be trained to convergence for each target distribution, and the computational cost scales with the dimensionality of the data and the complexity of the target distribution. Furthermore, the cross-validation process for selecting $M$ adds another layer of computational overhead, making the method less practical for very large datasets or high-dimensional problems where each evaluation during cross-validation can be expensive.

2. Variational inference is generally favored over sampling methods like MCMC for high-dimensional posterior distributions due to its efficiency. 
However, rejection sampling faces significant challenges in high-dimensional settings because of the curse of dimensionality. I am therefore skeptical about this algorithm's performance and scalability in high-dimensional scenarios. The curse of dimensionality implies that the volume of the proposal distribution will be much larger than the volume of the target distribution, leading to extremely low acceptance rates and making the method computationally infeasible. While the authors use a neural network to parameterize the proposal distribution, it remains unclear how well this mitigates the exponential decrease in acceptance probability as the dimensionality increases. The paper lacks a theoretical analysis or empirical evidence demonstrating that the proposed method can maintain reasonable acceptance rates in high-dimensional spaces.

### Questions
1. Rejection sampling may face challenges in high-dimensional settings. 
Could you discuss whether your method maintains robustness under these conditions and support this claim with experiments conducted in high-dimensional scenarios?
2. Additionally, could you compare the computational efficiency of your method with other approaches when applied to large-scale datasets or high-dimensional cases?

### Soundness
3

### Presentation
3

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
In this submission a lower bound IR-ELBO is derived by considering a family of implicit variational distributions obtained via rejection sampling. The method is tested on Bayesian NN learning, toy examples and applied to VAEs, tested on MNIST where it compared favorably against the considered baselines.

### Strengths
The paper is well-written and there are some recent works on variational rejection sampling, thus the submission should be relevant to the ML community. The method is evaluated in quite varied experimental settings which is good (although the VAE results on MNIST are not close to the SOTA [5]; to be clear, this was not a claim made by the authors). Furthermore, the algorithmic descriptions are useful for understanding the proposed methods and I also appreciate the transparency of the limitation provided in Sec. 6.

### Weaknesses
To start with, I want to be clear that I am not an expert on implicit variational inference, which may be reflected in some of my concerns below.

I was expecting to see a distinction between the proposed method and the rejection sampling approach in [1] and the one in [2].

In [1] they also learn an acceptance function which "can be interpreted as estimating a (rescaled) density ratio between the aggregate posterior and the proposal". I think the principle is different between this submission and [1] since [1] reformulates the prior to be a resampled distribution, but this should be made clear in the submission.

In [2] their Equation (2) is identical to your Eq. (13), which you state is different to "traditional implicit variational inference approaches". Could you please expand on how your formulation of $r_{\theta, \phi}$ is different from the one in [2]? Furthermore, Eq. (14) is the same lower bound as the one used in Eq. (4) in [2] and in Eq. (5) in [3] which should be stated---as it reads now, Eq. (14) appears to be a contribution of the submission.

Regarding the IR-ELBO, I am a bit confused about the exact formulation of the IR-ELBO: below Eq. (16) it states "Substituting the lower bound for log $Z_{\theta, \phi}(x)$ from Equation (16) into Equation (15) yields the final loss function, which we call the IR-ELBO" which to me implies that Eq. (16) is not IR-ELBO, but a term in the IR-ELBO, while in row 4 in Algorithm 2 it says that the IR-ELBO is Eq. (16)?


### Questions
Do I understand it correctly that the IR-ELBO is a looser bound on the marginal log-likelihood than the one in Eq. (14)? To me it seems a bit counter intuitive as the implicit distribution setting "allows for more flexible posterior approximations". Do you have an intuition to why the bound is looser (if this is indeed the case)?

Is Eq. (4) really correct? Typically $f_\phi(x)$ denotes the amortized mapping from data to variational parameters, $\phi$ (is it the same here?). Here I read Eq. (4) as the function (the neural net which outputs $z$ after taking also the standard normal sample) is sampled from the variational distribution. Maybe this is correct, but the formulation looks a bit awkward.

Could IWRS be used for mixtures of variational distributions? I.e., would it make sense to have mixtures of resampled distributions to leverage the strong results from [4, 5]?

Would it be possible to apply the importance weighted ELBO [6] to Eq. (16) to make it tighter?

[4] https://proceedings.mlr.press/v202/kviman23a.html

[5] https://arxiv.org/pdf/2406.07083

[6] https://arxiv.org/abs/1509.00519

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes "Implicit Variational Rejection Sampling" (IVRS), an approach combining implicit variational inference with rejection sampling to approximate complex posterior distributions more accurately. An implicit variational approximation is learned using prior-contrastive adversarial variational inference (density ration estimation $T(z,x)=p(z)/q(z|x)$). IVRS refines the posterior approximation using rejection sampling using an accept-reject routine with an acceptance probability function of form  $a(z,x)=\sigma(T(z,x) + p(x|z) -M)$. The authors derive a new, tighter, lower-bound evidence called IR-ELBO (which is analogous to R-ELBO for explicit models). The method is tested on a set of toy examples, Bayesian Neural Network (BNN) benchmarks, and a Variational Autoencoder (VAE) on MNIST. The authors claim that IVRS outperforms traditional VI in terms of accuracy and efficiency.

### Strengths
1. **Well written**: The paper is overall well written and structured, with clear explanations of the proposed method and its theoretical underpinnings. The paper is grounded in solid theoretical foundations, combining implicit variational inference with rejection sampling.
2. **Experiments BNN** : The proposed method is evaluated on various datasets, and the method is compared to other methods (for implicit VI), demonstrating its effectiveness in approximating complex posterior distributions for BNN (Table 2). The reported results of 81.78 nats on MNIST seem good to me (but not state-of-the-art).

### Weaknesses
1. **Novelty**: The idea of using rejection sampling to refine variational distributions was already introduced by Grover et al. 2018 for explicit models (as the authors acknowledge); the extension to implicit models is new to my knowledge (although very related).

2. **Toy evaluation (5.1)**:  The performance for toy data is not very convincing (at least as visualized in Fig. 1). This might also be due to the non-optimal visualization/KDE artifacts (what is the color gradient on the contours? Shouldn't the approximations be perfect in these simple cases, especially using rejection sampling?). Can you provide a more interpretable metric, such as two-sample tests or actual statistical distances (C2ST,  Wasserstein distance...) to the target? (in Table 1, in addition to NLL) 

3. **VAE evaluation (5.3)**: To my understanding Table 3, contains metrics from literature (which might have different hyper parameterizations/training routines)? Furthermore, it "compares" against methods that are almost ten years old, with the most recent one from 2018. Picking out some examples from more recent work [1,2] that achieve even better nats on MNIST (79.09, or 76.93 with data augmentation). This should be discussed in more detail (any reason why this is not included?). Furthermore, only MNIST is evaluated, which is rather simple; the paper would benefit from more datasets (e.g., CIFAR or ImageNet, which also have clearer leaderboards on bits/dim). Overall I hence think that the current manuscript does not provide enough evidence to support the authors claim that the "method outperforms traditional variational inference techniques in terms of both accuracy and efficiency."

### Questions
- Can the authors address my major concerns raised in the weakness section?
- I would expect the rejection rate to be rather high initially (i.e. depending on the initializations of q, choice of M and T). For particularly bad initializations, the rejection sampling could just get stuck in the while loop. Do the authors truncate the rejection sampling algorithms after a maximum number of iterations to avoid this problem?
- The paper would benefit from a more elaborate evaluation to support the claim by the authors that the "method outperforms traditional variational inference techniques in terms of both accuracy and efficiency". This can be done by comparing against more recent baselines and/or more complex datasets (with clear performance results).

Overall, I tend to reject the paper in its current form. The paper is well written, and the methodology is sound, but the novelty is limited. In addition, the experimental evaluation is not very convincing or rather limited (the toy data and the VAE evaluation).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to combine implicit variational inference with rejection sampling to improve inference quality. To overcome the limitation that the implicit variational distribution cannot be evaluated, they train a discriminator to learn the density ratio. The authors apply their method to multiple toy examples and benchmarks.

### Strengths
(1) Presentation

The paper is well-presented and clearly written.

(2) Empirical evaluation

The paper demonstrates the utility of the method on multiple low-dimensional toy datasets which provide a nice intuition for the method and clearly demonstrate that it improves inference quality. In addition, the authors also provide comprehensive evaluation on two large scale examples (BNNs and VAEs).

### Weaknesses
 (1) Overstatement of contribution

The authors point out that (page 3 middle) one of the contributions of their method is to apply rejection sampling also when the posterior is unnormalized. I don’t think this should be phrased as a contribution as it is a standard textbook application of rejection sampling. Please de-emphasize this point.

(2) Lack of clearer limitations

While the authors provide a limitations section, this section is quite minimal. I think the authors should comment on the following points that are currently not addressed explicitly (or only in other parts of the paper): (A) The need to train an additional neural network, (B) The increased compute requirement to set M with cross validation.

(3) Lack of explanations on how to set M

The authors state that they set M with cross validation, but later claim that it requires empirical hand-tuning. Which one is it?

### Questions
I would appreciate a discussion of the behavior of the algorithm if M is not set correctly—will the proposed method just perform sub-optimally or will it fail catastrophically (and potentially even worsen performance of plain VI)?

### Soundness
4

### Presentation
3

### Contribution
2
