# Correcting Flows with Marginal Matching

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Flow matching models, ODE-based generative models, generate samples by gradually morphing a simple source distribution into a target distribution. 
In practice, these models still fall short of perfectly replicating the target distribution, mainly due to imperfections of the learned mapping. Previous work mainly focus on alleviating discretization error, which rises from sampling a continuous trajectory with a finite number of steps. In this work we focus on prediction error, an error that is inherent in the model. 
Our main contribution is identifying a trajectory that complies with the imperfect flow model and leads exactly to the target distribution. Based on this finding, we propose Marginal Matching&mdash;a simple inference-time correction scheme to steer the generated samples in the direction of the data.
This scheme proves to reduce a bound on the distance between the data and the learned distribution, motivating two different implementations for the correction function. We show that our proposed method improves sample quality on CIFAR-10 and ImageNet-64,  with minimal overhead in computation time, or non at all when applying approximated correction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes using corrector steps during the sampling of flow models. Two correction models are proposed: a score model, and a classifier model. If I understand correctly, in practice, the score model is trained with a constant noise instead of being time-dependent. The classifier model should act similarly to a discriminator, but empirical performances seem to favor the score model.

### Strengths
- Discusses using additional inference-time compute which could be interesting.

### Weaknesses
 - The concrete connection between theoretical derivation and proposed algorithm is unclear to me.
- There is also missing information regarding the method.
- How does Algorithm 1 relate to the idea of the backward marginal?

- Why does Algorithm 1 add noise in line 4? Doesn't this add bias to the sampling when no correction is used?

- How do you choose beta and alpha?

- The proposal for the score model is to a time-dependent score. But in practice, only a constant noise is used. Why is that?

- If you used a time-dependent score and set beta = sqrt(2 * alpha), does your method recover Langevin dynamics as the corrector step?

- What is "Backward Marginals Interpolation"? How is this different from the standard "Score" correction model?

- Why can't this be used with diffusion model sampling (by just replacing line 6)? Intuitively, the choice of corrector steps should be independent to the predictor (ODE/SDE) steps.

### Questions
- How does Algorithm 1 relate to the idea of the backward marginal?

- Why does Algorithm 1 add noise in line 4? Doesn't this add bias to the sampling when no correction is used?

- How do you choose beta and alpha?

- The proposal for the score model is to a time-dependent score. But in practice, only a constant noise is used. Why is that?

- If you used a time-dependent score and set beta = sqrt(2 * alpha), does your method recover Langevin dynamics as the corrector step?

- What is "Backward Marginals Interpolation"? How is this different from the standard "Score" correction model?

- Why can't this be used with diffusion model sampling (by just replacing line 6)? Intuitively, the choice of corrector steps should be independent to the predictor (ODE/SDE) steps.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the refinement of the flow-based/diffusion models with marginal matching, which delves into the gap between the forward and reverse process to mitigate the *prediction error* of the model, which is the gap between the optimal flow $u*$ and the estimated $v_\theta$. The principle behind the marginal matching is that since the model cannot be learned perfectly and the forward and backward marginal (path) must have some gap, there should be some corrector to move from the forward to the (correponding) backward marginal.
To implement the marginal matching, the paper piloted two models: score-based and robust classifier. Score-based marginal matching assumed the forward marginals to be the noisy version of the backward marginal, and the robust classifier first constructs the classifier discriminates the forward-marginal particle to the backward-marginal particle (using both data) and get the gradient to move from the forward to the backward marginal trajectory. 
With this corrector model with marginal matching, the generation quality from the image datasets are improved with a few steps.

### Strengths
* The idea of marginal matching correction is sound, and can be ubiquitously applied to other generative model approaches.
* The convergence property from the marginal matching is concretely headlined with Wasserstein distance bound. 
* Moreover, the interpolation part which says that using the data and approximate source rather than the full trajectory for training resolves some of my interests, which is the multi-marginal matching from the partial trajectory rather than the full trajectory.

### Weaknesses
 * My main concern is that the idea of the marginal matching correction is not directly used in the score model, as the forward marginal is not directly connected to the backward marginal but is considered as the noisy version of the backward marginal. If so, (as I mentioned in the question) the corrector part is the external-model version of the existing work. As this paper implies that the score version of the corrector works better than the robust classifier version, it would be better if this issue is resolved.

 * For my understanding, the corrector model $h_\psi$ constructed by the score model is the same or similar to the predictor-corrector proposed in [Song et al, 2021]? If it is so, the score model part of the marginal matching is the flow-based equivalent of the existing work with more theoretical background with Wasserstein distance bound and external corrector model.
* The result in Table 1 will be more concrete if the RK4 solver includes NFE=24, 28, and 32 (as a single step uses 4 NFE). I'm curious that the paper mentioned that the NFE of a single RK4 step is 2
* How is the corrector step $\alpha$ chosen? This seems that the choice of $\alpha$ heavily affects the performance of the corrector. Are the hyperparameters in Table 10-12 hand-crafted?

### Questions
* For my understanding, the corrector model $h_\psi$ constructed by the score model is the same or similar to the predictor-corrector proposed in [Song et al, 2021]? If it is so, the score model part of the marginal matching is the flow-based equivalent of the existing work with more theoretical background with Wasserstein distance bound and external corrector model.
* The result in Table 1 will be more concrete if the RK4 solver includes NFE=24, 28, and 32 (as a single step uses 4 NFE). I'm curious that the paper mentioned that the NFE of a single RK4 step is 2
* How is the corrector step $\alpha$ chosen? This seems that the choice of $\alpha$ heavily affects the performance of the corrector. Are the hyperparameters in Table 10-12 hand-crafted?

```
[Song et al., 2021] Score-Based Generative Modeling through Stochastic Differential Equations, ICLR 2021
```

---

I recommend borderline acceptance in the current stage of review: this can be varied in the discussion period, and additional question can be added.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method to correct the path trajectories of continuous normalizing flow models trained with flow-matching. Instead of focusing on improving ODE solvers for potentially poorly fitted models, as much of the existing literature does, this work aims to train networks that directly guide the sample trajectory by correcting the model-fit failures at each step with a (residual) network $h_\theta$.

As the authors note, although the general idea has been previously explored for continuous normalizing flows [A], this paper differentiates itself by focusing on frameworks that train normalizing flows using conditional flow matching.

I have two main concerns:

1. **Theoretical Presentation**: Some theoretical sections are presented poorly and the notation could be improved. Portions of the theory seem inconsequential and do not tie back to the story (Separation of A and B in Theorem 3.3), and could be safely removed, moved to the appendix, or generally improved for easier readability. Above that, I do have some concerns about the assumptions for one of the theorems.

2. **Lack of Evidence in Large NFE Settings**: The paper initially distinguishes between improving flow matching models by $(i)$ improving model fit and $(ii)$ refining the ODE solver. However, the authors do not provide evidence that their method is beneficial in settings with a large NFE. Specifically, if the generative performance is poor due to model-fit issues, merely increasing NFEs should not significantly help; however, the results show that increasing NFE without any correction is still getting the same performance as doing correction but with lower NFE. Therefore, to convincingly advocate for their method, experiments in large NFE settings are essential.

The second concern is crucial for connecting the results back to the paper's motivation and introduction. Indeed, the paper even has a line (L142) mentioning that "while a larger $N$ reduces discretization error, it also leads to a greater accumulation of prediction error", so why do we not have comparisons in precisely these large NFE settings?  

My interpretation based on the experimental results is that adding the guidance $h$ seems to be more similar to distillation methods that allow the model to take larger steps, as opposed to inherently fixing model-fit errors. I also have some more detailed points and a suggested ablation which I will present in the "questions" section.

All in all, the paper does seem to introduce a nice method at its core, but without sufficient experimental evidence and improvements in writing, it is not ready for acceptance!

### Strengths
1. The paper aims to address the problems associated with image generation in possibly the most performant variant of generative models. Any improvements to flow matching approaches are therefore highly useful!

2. The background, introduction, and discussion of related work are thorough and clear.

3. The main idea is clearly presented with a nice figure that helps understanding.

4. The theoretical contribution appears sound, though not all of them directly factor into the methodology.

5. I appreciate the amount of detail and extra context that is included in the Appendix for the ablations and comparisons.

### Weaknesses
1. I find that separating Theorem 3.3 into parts A and B is tangential to the story and overly confusing. In reality, we do not have full control over our correction network and its Lipschitz constant. Therefore, we can never determine the best scheduling. This section seems like its being theoretical for its own sake! It might be clearer to simply present Lemma A.2 of the appendix in its most general form:
$$W_2(p^b_t, p^f_t) \le W_2(p^b_{t_0}, p^f_{t_0}) \cdot e^{L(t-t_0)}$$
and say that improving the Wasserstein distance on the RHS for $t_0$ can effectively bound the Wasserstein distance on the LHS, especially for $t$ that is sufficiently close to $t_0$. I don't think A, B, and examples 3.4 and 3.5 are particularly insightful when it is not directly factored into the decisions made in the experiments. The results in A and B can still be included, but in the appendix.

2. The parallel sampling section seems slightly oversold! To my understanding, while both forward passes can be done in parallel, it cannot be done in one batch because the forward call is on different methods. Could you please provide a time comparison between parallel and serial sampling on one experiment with the hardware that you have?
 
3. The statement of Lemma 3.6 seems to spill over to the rest of the main text and I generally do not agree with the base assumption that $p_t^f = p^b_{t, \sigma}$ which is the main driver for Lemma 3.6. Please let me know if I am misunderstanding this!

4. I don't find the comparison between this method and Dai and Wipf [B] appropriate! [B] trains a VAE on VAE to fix problems associated with the dimensionality mismatch between the data manifold and the manifold induced by the (first) VAE. That is not a concern in flow-matching and diffusion models as these models are known not to suffer from the manifold mismatch difficulties as much.

5. Although FIDs are still being widely used for evaluation, there have been clear flaws associated with them and the simplistic Inception network [C]. Please use DinoV2 Frechet Distances for the comparisons from [C], in addition to the widely used FID metric.

6. Please also provide evaluations "matching" the same NFEs in the corresponding non-corrected models.

7. The paper does not sufficiently address the core motivation of correcting model-fit errors as opposed to discretization errors. The experiments do not convincingly demonstrate that the method is beneficial in settings with a large number of function evaluations (NFE). Specifically, the results show that increasing NFE without any correction is still getting the same performance as doing correction but with lower NFE. This suggests that the method might be more akin to a distillation technique that allows for larger steps rather than inherently fixing model-fit errors. The paper needs to provide more evidence that the method is beneficial in settings where model-fit is the primary limitation, and not just discretization error.

### Questions
1. Instead of correcting the marginals, what happens if you simply define a new network $\nu_\theta(t, x) := h_\theta(t, x) + v(t, x)$ and fine tune using the CFM loss? That seems like a more direct way to fix prediction error, so I'm curious if there is any gain from using the relatively more complicated algorithm you have suggested.


### References

[A] Chen Xu, Xiuyuan Cheng, and Yao Xie. Normalizing flow neural networks by jko scheme. Advances
in Neural Information Processing Systems, 36, 2024.

[B] Dai, Bin, and David Wipf. "Diagnosing and enhancing VAE models." arXiv preprint arXiv:1903.05789 (2019).

[C] Stein, George, et al. "Exposing flaws of generative model evaluation metrics and their unfair treatment of diffusion models." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
4

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a mitigation strategy for prediction errors in flow-based generative models. While previous research has often focused on minimizing discretization errors (by optimizing the mapping between Gaussian noise and the target data distribution), this work is the first to specifically target the prediction errors in flow-matching models.

The authors propose leveraging time reversibility in flow matching models. By implementing a corrective mechanism that modifies the generated sample trajectories during inference, the model can reduce errors between the generated and target distributions. This correction, applied intermittently with the ODE solver steps, is theoretically shown to minimize the Wasserstein distance between the generated and target distributions, under certain assumptions.

The paper presents two implementations of this correction mechanism: one that uses a score model and one that is based on a classifier. Empirical results show that this method improves generation quality on CIFAR-10 and ImageNet-64, achieving better FID scores with fewer sampling steps, especially in the former. The contributions of the paper include a novel time-reversal framework, theoretical analysis, and practical implementations to enhance flow-matching model performance.

### Strengths
- The paper presents an approach to improve flow models by enforcing that the forward and backward marginals need to match. This is a sensible thing to try.

### Weaknesses
The presentation of the paper can be improved. Some specific points that need to be changed:
- The statement of Theorem 3.3 is too long. It should be broken up.
- The explanation on the score model approach is confusing. It is not explained in detail in Section 3.2.1: the sentence “We assume that the forward marginals are there noisy versions…” is not clear. Section A.3.2, which is where the approach should be explained, contains an obscure statement that does not clarify how the training is performed. Then, Section A.10.3 does contain the training loss for the score model, but the reason to introduce $\sigma$ is still unclear.
- In App. A.5, what does percentage mean?

The experiments presented show some improvement with respect to the baseline models, but some questions arise: 
- The improvement relative to the baseline models is stronger for CIFAR-10 than it is for ImageNet64. Performance on ImageNet64 is much more indicative of performance on models that practitioners care about. In fact, Table 2 shows that the baseline OT-CFM with 16 NFE obtains FID 15.11, while OT-CFM with Score at 16 NFE (6 of those corresponding to the score model) obtains either 15.57 or 15.69 depending on the variant. Even if the score model is cheaper to evaluate, it is hard to make a case for using OT-CFM Score given that the obtained FID is higher. 
- It is also surprising that the FID with 16 NFE is higher than with 12 NFE, for both score variants. This goes against the intuition developed in the paper.
Experiments on larger scale text-to-image models would help clarify the usefulness of the suggested method.

### Questions
- Wouldn’t it make sense to fine-tune the FM vector field such that $\frac{1}{N}v_{\theta_{FT}}(t_n,x_{t_n}) = \frac{1}{N}v_{\theta}(t_n,x_{t_n}) + \alpha_n h_{\psi}(t_n, x_{t_n})$? That way, we don’t need to evaluate $h_{\psi}$ separately from the flow matching vector field, which means that we can arguably use the correction at every single time step without incurring additional compute costs. It seems that should work well in the cases where parallel sampling works well.

### Soundness
3

### Presentation
2

### Contribution
3
