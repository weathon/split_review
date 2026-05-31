## Human Reviewer 1

### Summary
The authors propose ESS-Flow, a method to guide sampling from probability flow generative models without gradient-based guidance. Their method samples with MCMC along ellipsoids in the source space (Gaussian prior), and takes a step based on the potential /target property evaluated in the data space. They motivate their method with the limitations of gradient-based guidance and evaluate their guidance on protein and material design tasks.

### Strengths
- Guidance without gradients is a nice benefit of the proposed method
- The method is motivated well theoretically and with prior work
- The experiments suggest that ESS-Flow is able to effectively guide samples compared to gradient-based approaches

### Weaknesses
- Does guidance for certain properties improve the estimation of other properties/observables not used in guidance?
- Given that one of the benefits of the proposed method is not relying on gradients, it would strengthen the paper to show guidance for discrete target properties.
- The discussion of challenges about challenges with gradient-based guidance (Fig. 2) is interesting, and I think further discussion / experiments along these lines would further strengthen the paper. I wonder if there is a way to show something similar with more realistic data by artificially creating 2 disconnected modes (i.e. removing data in a transition region or something like that).
- "Limits ESS-Flow’s effectiveness when the prior does not well inform the target distribution": while I understand that things like image inpainting might be challenging for the method, have the authors evaluated ESS-Flow on other image guidance tasks?
- There are newer and more accurate models compared to something like CHGNet that might give more accurate metrics (MACE, eSEN, UMA, etc.)

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposed a plug-and-play controllable generation method for flow-based generative models, which is based on sampling the controlled prior distribution through elliptical sliced sampling (ESS), and then run the ODE to convert the prior samples to samples from the tilted target distribution. The method avoids the need to compute the Jacobian of the flow map $T _ \theta$, and does not require the tilt to be differentiable. The authors further proposed to use a coarse discretization of the flow ODE as a proposal for the transition kernel and reweight the samples with the evaluation of the tilt on the final samples to reduce the computational cost.

### Strengths
Unlike most existing controllable generation methods such as CFG and DPS that involve the computation of an extra term in the SDE (often requires approximation), the proposed method just treat the flow ODE as a black-box and only modifies the prior distribution, and instead of doing gradient-based optimization, it directly samples from the controlled prior distribution. This makes the method simple and concise, and I personally appreciate this idea.

The paper also provided comparisons of the proposed method with existing controllable generation methods based on optimization. I'm not familiar in the domain of material design and protein structure prediction, but the experimental results look nice.

### Weaknesses
The authors provided limited background information about the ESS algorithm, which I believe most of the readers in the ML community should not be familiar with. We know that there are lots of zeroth-order sampling methods for sampling from $\pi(z)\propto p(z) g(T _ \theta(z))$, such as rejection sampling, the MH algorithm, and proximal sampler (https://proceedings.mlr.press/v134/lee21a.html). What's the insight behind ESS, and why is the Gaussian prior important for it to work? (Also I'm not quite in favor of the use of the abbreviation ESS in this paper, since it is also used to refer to "effective sample size" in the literature of Monte Carlo methods, which may cause some misunderstanding. But it's fine if you keep it.)

For the experiments, I think it would be more convincing if the authors can also consider some image generation tasks, which are more familiar to most ML researchers, and can better demonstrate the effectiveness of the proposed method. Also, as the authors have introduced the multi-fidelity version of the proposed method through a coarse discretization of the flow ODE, it would be interesting to see some ablation studies on the choice of the discretization step size and its impact on the generation quality and computational cost.

I'm happy to raise the score if these issues can be addressed during rebuttal.

### Questions
1. What's the typical number of rejections needed in one iteration of ESS in order to get an accepted sample?

2. We know that diffusion model and flow matching allow one-step prediction of $\mathbb{E}[x _ 1|x _ t]$. For faster sampling, instead of still doing discretization of the flow ODE, do you think it is possible to replace the flow map $T _ \theta$ with a one or few step predictor in the proposed method? If a consistency model is available, we can even directly predict the final sample from the prior sample in one step, which may further reduce the computational cost.

3. The main text of the paper assumes the flow model is trained for Euclidean data, but in the experiments it turns out that the whole framework can also be applied to manifold data as long as we have a flow-based generative model, which I believe is an advantage of the proposed method, and should be highlighted more in the paper. I'm not quite familiar with the literature of manifold, but is there anything that we need to pay attention to when applying the proposed method to manifold data? For example, do we need to modify the ESS algorithm in any way?

4. In table 2 and 3, it would be better to highlight the best results in bold font for better readability.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces ESS-Flow, a training-free and gradient-free guidance method for flow-based generative models. The key idea is to do Monte Carlo inference directly in the source space, where the prior is Gaussian, by sampling from a distribution of the form $\pi(z) \propto g(T_\theta(z))p(z)$. This makes the method applicable to quantized/materials settings and to non-differentiable observation or reward functions. The authors further propose a multi-fidelity variant where the authors sample using a coarse ODE discretization and reweight using a fine discretization to reduce computation. Experiments on materials and protein structure prediction show that ESS-Flow achieves nearly SOTA results on all metrics for materials and comparable performance on protein generation metrics.

### Strengths
1. The paper is clearly written, with a coherent structure and well-motivated.

2. The proposed method is simple to implement and achieves strong results on the material generation task.

### Weaknesses
1. The paper lacks experiments on standard image-domain tasks (e.g. inpainting, deblurring), which are commonly used in related work such as D-Flow and PnP-Flow.


2. While the empirical contribution is solid, the theoretical contribution is relatively modest.

3. One of the main points of the contribution is having this apply to non-differentiable rewards/potentials yet there are no experiments demonstrating this capability.

### Questions
1. What are the quality metrics in Table 3 for the competing methods? It would be helpful to report the same set of metrics so we can compare ESS-Flow directly to the baselines.

2. How does multi-fidelity ESS compare to standard ESS on the metrics reported in Table 2 and Table 4.

3. What are the acceptance rates of the sampling?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
The authors introduce ESS-Flow, a gradient-free method for controlled generation in the setting of generative modelling with flow matching models. The authors perfoming Bayesian inference in source space using Elliptical Slice Sampling, which enables conditional generating without requiring gradients. The authors demonstrate their approach on various applications ranging from materials to proteins.

### Strengths
[S1] The gradient-free nature of this approach is appealing. There have been other works for source space sampling such as , but this still required gradients, wheras this approach here circumvents this via the Jacobian cancellation and the ESS approach.

[S2] One common with gradient-based optimisers in diffusion samplers are the multitude of often brittle hyperparameters like guidance scales or other schedulers; this approach here seems to be less reliant on these.

[S3] Good motivation of the different components introduced with formal justifications.

### Weaknesses
[W1] The authors demonstratet that they can avoid the Jacobian computation, but ESS-Flow still requires many evals (>1000 MCMC steps) of the transport map, hurting the efficiency of the approach

[W2] The authors openly describe the limitation of ESS-Flow in cases where the target is constrained on a lower-dim manifold, but claim that in scientific domains the target distribution is not overly collapsed. However, in many applications like in protein design the target distribution lies exactly on such a lower dim manifold with most of the target space being invalid sampels; some more explanation why the authors think that this is not the case in many scientific applciations would help here.

[W3] In many scientific applications, people have circumvented the non-differentiability of categorical sequences via soft relaxations similar to the atom relaxation the authors use for their comparisons. In approaches like BindCraft (Pacesa et al, 2025 Nature), this works remarkably well, so the authors should potentially try to tune that baseline to see if it as strong as it can be.

[W4] While some of the baselines in the protein structure prediction case of Figure 4 look unrealistic, ESS-Flow also seems to have biophysical implausibilities, and the ELBO of the model only partially captures these things. A more fundamental evaluation like counts of clashes could demonstrate how good the structures actually are; the RMSD values above 10 suggest that all baselines seem pretty far off.

### Questions
[Q1] The case studies all have quite low dimensionality, how does the approach scale to high dimensional problems?

[Q2] Given the authors say their method does not work well with priors that poorly inform the target distribution, can this statement be made more exact? ie is there a quantity that one can look at to see if the approach will work or not?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 5

### Summary
The paper introduces ESS-Flow, a training-free and gradient-free approach for controlled generation using pretrained diffusion or flow-based models. The method reframes inference in the Gaussian latent source space and applies elliptical slice sampling (ESS) instead of gradient-based updates, using a change of variables to apply updates in the data space. The main goal is to enable preference alignment when gradients are unavailable or unreliable, such as in cases involving quantized or simulator-based objectives.

### Strengths
- The paper introduces a new and practically useful application of elliptical slice sampling to flow- and diffusion-based generative models. While ESS itself is a known MCMC method, its use within the latent Gaussian space of pretrained flow-based models is novel and interesting.
- The algorithm is designed such that jacobian determinants of transport maps don’t need to be computed, enabling a scalable and efficient algorithm.


- The theory is sound, and the algorithm preserves theoretical guarantees from the original ESS method, making interpretability for downstream researchers easier.
Reported results compared to baselines show a non-negligible improvement in matching a new target energy function.


- Overall, the paper connects ideas from generative modeling, Bayesian inference, and MCMC in a coherent and insightful way. It is an interesting paper that I believe would bring a net positive to the research community, which would be strengthened by addressing the weaknesses below.

### Weaknesses
- While 0th-order methods can benefit greatly in settings with unreliable gradients, they can also face severe scaling issues in high-dimensional spaces. Having an experiment showing performance as problem dimension scales would help further inform future readers when they should use ESS-flow vs. a gradient-based method.


- While results on the provided experiments show that the 0th order methods are outperforming the gradient-based methods, none of the experimental settings to my understanding actually fall under the non-differentiable setting that the paper proposes to address. It would help to either (a) include a relevant experiment setting where gradient information is truly intractable to retrieve, or (b) demonstrate that in the reported settings, the gradient structure is highly unideal for gradient-based methods, e.g. high Lipschitz constant (also, for line 290, maybe better to call them gradient-based rather than optimization-based, since there are many 0th order optimization algorithms).
More statistical details on the experimental setup are needed, e.g. some std’s in table 2 are higher in magnitude than the mean.


- There are some missing baselines/ablations (e.g. adjoint matching [Domingo-Enrich et al.], non-ESS-based source space MCMC) that would help clarify whether the main benefit comes from being gradient-free or from the specific ESS mechanism.

### Questions
- How does ESS-Flow scale with increasing latent dimension? Does the acceptance rate or effective sample size drop significantly in higher dimensions?


- What is the runtime cost compared to the baselines?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3