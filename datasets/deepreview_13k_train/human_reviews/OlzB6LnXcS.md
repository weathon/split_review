# One Step Diffusion via Shortcut Models

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
\begin{hyphenrules}{nohyphenation}
Diffusion models and flow-matching models have enabled generating diverse and realistic images by learning to transfer noise to data.
However, sampling from these models involves iterative denoising over many neural network passes, making generation slow and expensive.
Previous approaches for speeding up sampling require complex training regimes, such as multiple training phases, multiple networks, or fragile scheduling.
We introduce shortcut models, a family of generative models that use a single network and training phase to produce high-quality samples in a single or multiple sampling steps.
Shortcut models condition the network not only on the current noise level but also on the desired step size, allowing the model to skip ahead in the generation process.
Across a wide range of sampling step budgets, shortcut models consistently produce higher quality samples than previous approaches, such as consistency models and reflow.
Compared to distillation, shortcut models reduce complexity to a single network and training phase and additionally allow varying step budgets at inference time.
\end{hyphenrules}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces shortcut models, a modification to the diffusion approach to be conditioned on noise level and step size. The approach is able to train end-to-end flexible models that simultaneously allow many-steps and one-step sampling.

### Strengths
- The paper is well written and easy to follow

- The proposed idea is novel and promising, this work pioneers a new family of diffusion/flow based generative models.

- The method is experimentally evaluated in a controlled setting, an extensive comparison with alternative methods is present.

- An open source codebase to replicate all the experiments and pretrained models will be release to falicitate further research

### Weaknesses
 - The performance of 1 step generated samples still lags behind multi-step methods; 1-step generated images presents some artifacts so the usability of the proposed solution in a pratical setting is limited to generate proxy images with 1 step and resample them with multiple steps

- end-to-end training to reach a few sample diffusion model is an interesting solution as it removes the burden of performing two separate training phases and leads to a flexible model. However the best results in 1 step regime are obtained by Progressive Distillation, thus demonstrating that the best option for a one step model is to distill it in a separate training phase. 

- It may be possible that learning few step models in a joint way introduces instabilities to the learning process especially when using much more complex data distribution than ImageNet or CelebA dataset. There are no guarantees on how the proposed approach would scale to large data regime training.


### Questions
- Comparing the various approach using the same compute budget could not be the best way as different methods may require different compute budget to converge to their optimal performance, did you take this consideration into account? It would be helpful to detail how the compute budget for each method has been fixed, and if you expect different convergence rates for each method. Moreover a plot of performance versus compute would be a nice addition if it's feasible.

- How does this method relates in any way to the ICLM 24 paper " Optimizing DDPM Sampling with Shortcut Fine-Tuning", I think the paper should be discussed as very relevant to the proposed method. 

- It would be nice to introduce a comparison on additional compute required by post training distillation methods compared to the proposed solution which just increase the required compute by 16% over a standard diffusion training. A table highlighting the total compute overdue required by each method should be added.

- The method presents a lot of hyperparameters to be tuned for training, as the selection of M (total number of sampling steps) and k, have you ablated how varying this affect the final results? do you have estimated the impact of choosing a bigger/smaller k? Can you show any ablation study varying some of these parameters, and provide generale guidelines for their selection to pratictioners?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes shortcut modes, an end-to-end training method that could produce high-quality images in either single or multiple sampling steps. The shortcut models take an additional input of the desired step size, compared to diffusion or consistency models.

### Strengths
* The paper is well written in the context of reducing sampling steps of diffusion models.
* The proposed method is novel and clearly presented.
* The experiments are comprehensive and convincing.

### Weaknesses
 * Lacks explicit comparison of training compute against other methods.
* The issue with CFG could hinder future practical use.

### Questions
* Why the CFG scale must be specified before training?
* Why use 128 as the number of steps? What about something as large as 1024? How would this design choice affect the quality? 
* Why not consider a two-stage distillation training, so that a pretrained diffusion model could be converted to a shortcut model?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes denoising generative model called shortcut model. These models are trained end-to-end and can generate samples in both single-step and few-step setting. The core idea is to condition the model on step size in addition to time step, which is typically done in conventional diffusion models. The hypothesis is that the additional conditioning on step size allows shortcut models to account for the future curvature. The model is trained via a loss objective that combines the optimal-transport flow matching loss with a self-consistency loss. The self-consistency loss is enforced by ensuring that the prediction of model at a given skip size matches the target obtained by two sequential smaller skips (for the same skip distance) with the shortcut model. The high computational cost as well as variance during training is dealt with by computing self-consistency loss on a small subset of samples in the batch. The proposed method has been tested on CelebAHQ-256 and ImageNet-256, and has good single-step image generation quality.

### Strengths
1. _Simplicity_: The proposed method is simple, easy to understand and simplifies some challenges previously encountered in other methods to obtain one-step or few-step models. For eg. It gets rid of two-stage training required for diffusion distillation as well as complex training scheduling required for consistency models. The loss objective is intuitive and builds upon flow matching loss and introduces an additional self-consistency condition. 
2. _Writing_: The paper is well-written. The core method has been explained well. The paper talks about challenges that can be encountered while training shortcut models and ways to address these challenges. 
3. _Computational efficiency_: The method seems computationally efficient as with an additional (marginal) cost of training diffusion models, shortcut models can be trained to generate samples in single-step as well as few steps. Further, even on larger datasets such as ImageNet-256 and CelebAHQ-256, these models can be trained in 1-2 days (though the exact number of TPUv3 nodes is unclear).  
4. _Applications_: The authors demonstrate advantages of this method on both image-generation as well as on robotic control tasks showing ways to generate an iterative sequence of actions in a single denoising step per action.

### Weaknesses
Note: The template of this paper seems to be different and doesn’t have line numbers present in the standard template for papers under review. 

1. The proposed method for shortcut sampling is general and should work for any gaussian probability paths ($x_t = \alpha_t x_0 + \sigma_t \epsilon$) however this hasn’t been explored or described in the paper. The paper considers only one choice of optimal transport probability path ($x_t = (1-t) x_0 + t \epsilon$). However, nothing constraints the method to be restricted to this particular choice. (One motivation for this choice of parametrization could be that OT paths are said to have less curvature but in this case, these are conditional OT paths and are not exactly straight lines paths between $x_1$ and $x_0$.) It is worth exploring ablations on how shortcut models perform on other parametrization of gaussian probability paths/sampling paths. In addition, the text should also be updated to have a more general parametrization.
2. The paper should also include quantitative performance on more commonly used datasets such as ImageNet-64 and CIFAR-10. While reporting results on larger datasets such as CelebAHQ-256 and ImageNet-256 is impressive, reporting metrics on these smaller datasets is also important. Most of the prior papers report metrics on these datasets which makes it easier to compare the performance of shortcut models to a larger number of previously proposed methods/models which are not currently reported in the paper (Note: I understand that it is impossible to replicate all the previously proposed methods due to the vastness of literature in the space).
3. Minor: I personally feel that images such as in Figure 1 are misleading as the original flow-matching objective was not specifically meant for single step generation, and the performance is expected to deteriorate because these models don’t learn an ODE integrator. There are some advantages of the original flow-matching models as well over shortcut models. These models are continuous time models which can be evaluated at any time between [0, 1] whereas shortcut models are discrete time and can only be evaluated at specific discrete time steps.

### Questions
1. For the results of Progressive Distillation in Table 1, a reasonable 128-step model would be the obtained after taking the initial (say, T=1024) step model and then distilling it progressively until we get 128-step model. Was this model used to report metrics in the table or, did the authors use the final 1-step model to generate samples with 128 steps? 
2. Appendix B.1 - could the authors specify the amount of TPUv3 nodes needed to run these experiments in 1-2 days? 
3. For consistency training, is there a reason why the authors chose to deviate from the proposed discretization schedule by Song et al. (2023) during training? From my experience with these models, the choice of discretization schedule matters a lot, and deviations affect the performance. Further, does this paper implement consistency training (which includes perceptual loss)[1] or the follow up paper [2] which uses pseudo-Huber loss and proposes several improvements over their previous paper.
4. Could the authors include architectural details/positional encoding details of both of the conditioning (time/noise level and step size)?
5. Could the authors include some qualitative results of one-step generation of some other methods they have trained on in the appendix? FID score doesn’t always correlate with human perception of images. 
6. Minor: Related work: for consistency models, the line needs revision - “shortcut models are practically simpler, as many consistency model tricks - e.g. using a strict discretization schedule, using perceptual loss rather than L1 loss - can be bypassed entirely. ” In their latest paper, Improved Consistency Training [2], Song et al. already bypass the need of perceptual loss; they use only pseudo-Huber loss.
7. Minor: some typos: competetive -> competitive (Section 5, line 2), qualatative -> qualitative (Figure 4 caption)

[1] Song, Yang, et al. "Consistency models." arXiv preprint arXiv:2303.01469 (2023).
[2] Song, Yang, and Prafulla Dhariwal. "Improved techniques for training consistency models." arXiv preprint arXiv:2310.14189 (2023).

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
The paper introduces a shortcut design (self-consistency objective) in flow models for efficient and high-quality sampling. Unlike complex methods, this shortcut leverages existing networks and requires a single training phase.
The shortcut design involves incorporating an additional step size condition into the generative models, enabling them to learn the objective while considering the step size. This approach showcases improved performance in image and policy generation domains.

### Strengths
The paper introduces a shortcut design (self-consistency objective) in flow models to maintain consistency in intermediate sampling trajectories. This shortcut involves adding a self-consistency objective during training without significant additional burden. Empirically, it consistently outperforms other end-to-end methods in terms of generation quality.

### Weaknesses
Limited comparison with one-step generator GAN is provided. In Appendix Table 2, StyleGAN-X demonstrates the best performance (2.3). Does this suggest that GAN is currently the optimal choice for one-step sampling?

In Equation 5, Flow-Matching and Self-Consistency are intended to correspond to different units of time. Flow-Matching is represented by d=0, whereas Self-Consistency is associated with d > 0. Does it affect the training data samples or procedures?  

In Algorithm1, why stopgrad is applied in self-consistency target? Will it disable the gradient update?  

Table1 suggests two-phase training can give better results than all end-to-end methods in one step sampling: progressive distillation in 1-step:14.8 and 35.6 for Celeb and ImageNet. Does the two-phase method has higher performance ceiling than end-to-end? 

In Figure 7, does increasing the sampling steps lead to a higher success rate for Short-cut Policy, similar to the diffusion policy? In policy planning, the primary focus is on achieving multi-mode and high precision performance.

### Questions
* In Equation 5, Flow-Matching and Self-Consistency are intended to correspond to different units of time. Flow-Matching is represented by d=0, whereas Self-Consistency is associated with d > 0. Does it affect the training data samples or procedures?  

* In Algorithm1, why stopgrad is applied in self-consistency target? Will it disable the gradient update?  

* Table1 suggests two-phase training can give better results than all end-to-end methods in one step sampling: progressive distillation in 1-step:14.8 and 35.6 for Celeb and ImageNet. Does the two-phase method has higher performance ceiling than end-to-end? 

* In Figure 7, does increasing the sampling steps lead to a higher success rate for Short-cut Policy, similar to the diffusion policy? In policy planning, the primary focus is on achieving multi-mode and high precision performance.

### Soundness
4

### Presentation
3

### Contribution
3
