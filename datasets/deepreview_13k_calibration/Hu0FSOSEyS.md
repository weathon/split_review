# Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
\vspace{-2ex}
Generative models transform random noise into images; their inversion aims to transform images back to structured noise for recovery and editing.
This paper addresses two key tasks: (i) \textit{inversion} and (ii) \textit{editing} of a real image using stochastic equivalents of rectified flow models (such as Flux).
Although Diffusion Models (DMs) have recently dominated the field of generative modeling for images, their inversion presents faithfulness and editability challenges due to nonlinearities in drift and diffusion.
Existing state-of-the-art DM inversion approaches rely on training of additional parameters or test-time optimization of latent variables; both are expensive in practice.
Rectified Flows (RFs) offer a promising alternative to diffusion models, yet their inversion has been underexplored. 
We propose RF inversion using dynamic optimal control derived via a linear quadratic regulator. 
We prove that the resulting vector field is equivalent to a rectified stochastic differential equation. 
Additionally, we extend our framework to design a stochastic sampler for Flux.
Our inversion method allows for state-of-the-art performance in zero-shot inversion and editing, outperforming prior works 
in stroke-to-image synthesis and semantic image editing, with large-scale human evaluations confirming user preference.
\vspace{-2ex}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper propose RF inversion using dynamic optimal control derived via a linear quadratic regulator. We prove that the resulting vector field is equivalent to a rectified stochastic differential equation.

### Strengths
This paper propose RF inversion using dynamic optimal control derived via a linear quadratic regulator. We prove that the resulting vector field is equivalent to a rectified stochastic differential equation.

### Weaknesses
1. The paper lacks a clear pipeline diagram, algorithm, or pseudocode, making it challenging to understand the methodology. The reviewer suggests adding an algorithm or pipeline diagram to improve clarity and readability.

2. The paper does not include a comprehensive comparison on established benchmarks for text-guided image editing. The sole focus on face editing in SFHQ for the “wearing glasses” task is insufficient to demonstrate the method's effectiveness. The authors are encouraged to refer to recent surveys or the latest papers in the field and to identify one or two well-recognized benchmarks for text-controlled image editing for a more complete evaluation. It would be beneficial to include comparisons with state-of-the-art image editing methods from 2024, rather than relying on older methods.

3. The proposed method involves a large number of hyperparameters, which is a potential drawback. The authors should perform a complete sensitivity analysis on all hyperparameters, as most training-free methods are known to be highly sensitive to hyperparameter choices, with different settings leading to vastly different editing results. The reviewer suggests specifying the hyperparameter values used for each case to provide better transparency.

### Questions
1. *In Equation (8), since the value of \( y_1 \) is unknown, how is the conditional term in Equation (8) calculated when \( y_1 \) is needed?*

2. *Similarly, in Equation (15), the calculation relies on \( y_0 \). This implies that the target \( y_0 \) is fully known, which raises fairness concerns. Reconstructing a value that is already available seems unfair and could be viewed as “cheating,” making a 100% reconstruction accuracy almost inevitable. Many training-free methods do not require access to \( y_0 \) during sampling. The authors should explain why they have chosen to compare reconstructions in this potentially biased manner.*

### Soundness
3

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
This paper tackles the problem of image inversion and editing with Rectified Flow models such as Flux. In particular, the authors are interested in the case where the input image is corrupted, and where faithful inversion and reconstruction is not necessarily ideal. To this end, the authors introduce an optimal control-inspired guidance scale, which interpolates between the unconditional flow trajectory and one given by an optimal controller. This effectively controls the tradeoff between faithfulness and editability during inversion. Additionally, the paper derives the stochastic differential equation associated with the ODE of flow matching, providing additional insights. They demonstrate the effectiveness of their method on two tasks: stroke-to-image synthesis and image editing.

### Strengths
- The problem that the authors are solving is significant, as the literature is progressively moving towards RF models.
- The proposed solution is sound and the results show the effectiveness of the method. In particular, the key contribution of conditioning the reverse process on the input image $\mathbf{y}_0$ is new and interesting.
- The derivation of the SDE associated with the RF ODE (Eq. 10) provides theoretical  value regarding RF models.
- Overall, the writing quality of the paper is very good. The explanations are clear, the equations rigorous.

### Weaknesses
While the structure of the paper is clear, some parts seem to lack purpose. For example, the introduction of the LQR problem and the optimal controller in the method seems superficial, as the resulting path is simply a linear path between the input image $\mathbf{y}_0$ and a sampled noise $\mathbf{y}_1$ (which is similar to SDEdit). Similarly, while the derived SDE in Eq. 10 has theoretical value, it is not used in practice as suggested by the Algorithms 1 & 2 in appendix C. Finally, the joint effect of the controller guidance parameters $\gamma$ and $\eta$ is not clearly exposed in the paper (see questions).

Regarding the inversion process (Section 3.2 & 3.3):

- I was confused by the implication of Proposition 3.1. Is it correct to understand that, out of the box, RF models are better than DM models for inversion? i.e., one can get almost perfect reconstruction in RF models by simply solving the ODE backward and then forward? This seems to be the case according to Table 5. If this is really the case, the problem to solve is actually more about editability than faithfulness. I would suggest the authors make it more explicit in the main paper by contrasting/comparing with DM models, where DDIM inversion is known to be sensitive to discretization errors.
- Proposition 3.2 states that the solution to the LQR problem is simply a linear path between the input image $\mathbf{y}_0$ and a randomly sampled (fixed) noise $\mathbf{y}_1$. This seems exactly like what SDEdit proposes. I was wondering if the optimal control perspective is different in any way? What additional insight or value does introducing the LQR problem bring compared to the straightforward linear interpolation explanation of SDEdit?
- The main result of the first part is shown in Eq. 8, where the authors introduce the *controller guidance* $\gamma$. Conceptually, is Eq. 8 essentially a linear interpolation between SDEdit (linear path solution to the LQR problem) and DDIM inversion (following the ODE backwards)? If so, wouldn’t it be more efficient to solve the ODE backward (normal inversion) and interpolate the result with a Gaussian noise at time $t=1$?

Regarding the SDE formulation (Section 3.4):

- Eq. 10 is the SDE formulation of Eq. 8. However, the stochastic part only relates to the unconditional ODE (from RF model), not the linear path conditioned on $\mathbf{y}_1$. Have the authors considered also making the linear path ODE stochastic? Intuitively, I assume that it would remove the need to fix the noise sample, as the SDE would converge to the entire Gaussian distribution.
- Around l.235, the authors mention that SDEs are more robust to initial conditions, which motivates the SDE formulation in Section 3.4. However, looking at Algorithms 1 & 2 in the appendix C, it seems that this SDE formulation is never used in practice (they only appear in C.3 for the numerical simulations). Why?

Regarding the Algorithm & Results (Section 4 & 5):

- What values of $\gamma$ and $\eta$ are used in Figure 2.?
- In Fig. 5, what models are used for SDEdit, DDIM inversion, NTI?
- The authors point out in the appendix that they use a fix value $\gamma=0.5$ through out the experiments. I wonder how does $\gamma$ affect the final result for a given $\eta$? It would be also interesting to have a two-axis grid comparison with varying $\gamma$ and $\eta$ to better understand the interplay between these two guidance parameters.

Miscelleanous:

- The caption in Fig. 10 says “The number below each figure denotes the starting time scaled by 28”, which is not true, since the number is the controller guidance value in this Figure.
- Typo at l.192: “we need to process**s**”.

### Questions
Regarding the inversion process (Section 3.2 & 3.3):

- I was confused by the implication of Proposition 3.1. Is it correct to understand that, out of the box, RF models are better than DM models for inversion? i.e., one can get almost perfect reconstruction in RF models by simply solving the ODE backward and then forward? This seems to be the case according to Table 5. If this is really the case, the problem to solve is actually more about editability than faithfulness. I would suggest the authors make it more explicit in the main paper by contrasting/comparing with DM models, where DDIM inversion is known to be sensitive to discretization errors.
- Proposition 3.2 states that the solution to the LQR problem is simply a linear path between the input image $\mathbf{y}_0$ and a randomly sampled (fixed) noise $\mathbf{y}_1$. This seems exactly like what SDEdit proposes. I was wondering if the optimal control perspective is different in any way? What additional insight or value does introducing the LQR problem bring compared to the straightforward linear interpolation explanation of SDEdit?
- The main result of the first part is shown in Eq. 8, where the authors introduce the *controller guidance* $\gamma$. Conceptually, is Eq. 8 essentially a linear interpolation between SDEdit (linear path solution to the LQR problem) and DDIM inversion (following the ODE backwards)? If so, wouldn’t it be more efficient to solve the ODE backward (normal inversion) and interpolate the result with a Gaussian noise at time $t=1$?

Regarding the SDE formulation (Section 3.4):

- Eq. 10 is the SDE formulation of Eq. 8. However, the stochastic part only relates to the unconditional ODE (from RF model), not the linear path conditioned on $\mathbf{y}_1$. Have the authors considered also making the linear path ODE stochastic? Intuitively, I assume that it would remove the need to fix the noise sample, as the SDE would converge to the entire Gaussian distribution.
- Around l.235, the authors mention that SDEs are more robust to initial conditions, which motivates the SDE formulation in Section 3.4. However, looking at Algorithms 1 & 2 in the appendix C, it seems that this SDE formulation is never used in practice (they only appear in C.3 for the numerical simulations). Why?

Regarding the Algorithm & Results (Section 4 & 5):

- What values of $\gamma$ and $\eta$ are used in Figure 2.?
- In Fig. 5, what models are used for SDEdit, DDIM inversion, NTI?
- The authors point out in the appendix that they use a fix value $\gamma=0.5$ through out the experiments. I wonder how does $\gamma$ affect the final result for a given $\eta$? It would be also interesting to have a two-axis grid comparison with varying $\gamma$ and $\eta$ to better understand the interplay between these two guidance parameters.

Miscellaneous:

- The caption in Fig. 10 says “The number below each figure denotes the starting time scaled by 28”, which is not true, since the number is the controller guidance value in this Figure.
- Typo at l.192: “we need to process**s**”.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an "inversion" method for flow-based models, like Flux. The method allows to edit either natural images (from the distribution on which the model was trained) or unnatural images (like paint strokes). The inversion process balances between a forward process that inverts the reverse flow ODE (like in DDIM inversion) and a process that drives the inversion towards some fixed, random noise vector, so that the inversion lands in a region of typical realizations of the prior Gaussian distribution. Editing is done by starting from the noise obtained during the inversion and performing a reverse process that balances between the standard vector field and a vector field that pushes towards the input image, all while injecting the target text prompt.
Experiments are presented on several datasets and editing tasks, including quantitative evaluations and a user study, comparing to several baseline methods.
An additional contribution of the paper is the introduction of an SDE variant for the proposed Controlled Rectified Flow process, which as a special case provides an SDE variant for the standard flow sampling process. This allows sampling using a stochastic process, which is less sensitive to the initial noise, rather than a deterministic process, which is a deterministic function of the initial noise.

### Strengths
- The proposed Controlled Rectified Flow formulation is mathematical elegant.
- The SDE variant of the method (and of regular flow as a special case) is quite nice, though it is not explored experimentally.
- The paper is well written and easy to follow.

### Weaknesses
 - The vast majority of the comparisons presented in the paper are against baselines implemented for different models (some of which are not even specified). Comparing between an editing method working with Flux and an editing method working with SD1.5, for instance, is meaningless. It does not reveal whether the differences in performance are due to the editing method or due to the fact that the underlying model is different (e.g. Flux is much stronger than SD1.5). The only exception is Fig. 7, which shows only two qualitative comparisons on Flux, but the baselines are very weak: SDEdit is known not to be consistent with the original image, and DDIM inversion is known to perform much better for editing when running the process only up to some intermediate t<1 (see e.g. Fig. 10 in [1]). I would expect to see at least the baseline of DDIM inversion for Flux going up to some midway point.
- The qualitative results are underwhelming, especially on LSUN Bedroom. Fig. 4 in the main text seems cherry picked, as in Figs. 13,15 in the appendix, none of the edited results look remotely similar to the input stroke image. It is not clear why this is not captured by the L2 metric in Table 1. The age and gender editing results are also quite weak. For instance, in Figs. 16,17, all edits look very far from the source. 
- The proposed inversion process pushes towards some noise y_1, which is arbitrarily fixed a-priori. This means that the parameter eta interpolates between some fixed generic image corresponding to this y_1, and the original image, as seen in Fig. 3. However, the effect that the choice of this y_1 has on the editing is not explored. It seems to me that when the noise vector y_1 encodes a completely different geometric structure than the image being edited, the edited result may significantly deviate from the original image. On the other hands, when y_1 happens to encode a similar structure, the edited result may be closer to the original image. The paper doesn't provide an ablation study illustrating the effect of y_1 and doesn't provide a clever method to choose it.

### Questions
I would be happy the hear the authors' thoughts on the weaknesses mention above.
In particular:
- What is the effect of y_1? How different are are results obtained with different y_1's? Is there a clever way to choose y_1?
- How does the method compare to DDIM inversion on Flux performed up to some midway timestep t? Namely, the inversion is up to some t*, and then the sampling starts from this t* using the text prompt describing the desired edit.
- How does the method work on other flow-based models, like SD3?
- Why does the L2 metric in Table 1 not capture the apparent discrepancies between the edited and original images in Figs. 13,15? As mentioned above, the edited images look almost completely unrelated to the original images.

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
Given a generative ODE that links pairs of noise and image, one can solve the forward/reverse ODEs to invert an image to noise or reconstruct noise into an image.

This paper modify the drift term of ODE to guide the process to terminate at high-likelihood noise/image. The guidance term is derived from LQR problem, which of solution is a minimum energy path to convert "any" image (noise) to given sample of random noise (image). This guidance is equal to conditional vector field that is computed analytically, without any optimization.

The authors propose a controlled forward/reverse ODE with drift term computed by linearly interpolating the conditional vector field and the original vector field. By adjusting the interpolation coefficient, the model achieves a trade-off between high-likelihood solutions and consistency to the original image.

Furthermore, the paper interprets the controlled ODE within the context of stochastic differential equations (SDEs), highlighting the robustness of SDEs to initial conditions and offering a deeper insight into the proposed method.

Experimental results validate the method's effectiveness in inversion-editing tasks, showing improved performance over existing techniques.

### Strengths
- Theoretical analysis provides valuable insights for the proposed method.
- The proposed framework of controlled ODE provides a design space for other applications, by adding regulation to the conditioned vector field.
- Experimental analysis is well established and demonstrating the effectiveness of the proposed method compared to baselines.

### Weaknesses
 - Missing comparison or discussion with fixed-point based inverse methods (ReNoise[1], AIDI[2]), which are applicable Euler solver. Their motivation is to reduce the error induced in inversion process with fixed point iterations and improve the editing performance.
- By design, controlled ODE will generate majority sample since it is guided toward mode. Thus, the proposed method may lose diversity even though we can control it via parameter $\gamma$. For example, edited faces always look at camera (Figure 5,6,7,10). But, this would be another open question.
- Proposed controlled forward ODE may break the OT path of Rectified Flow, as it compute conditioned vector field $u_t(Y_t|y_1)$ with fixed noise sample $y_1\sim \mathcal{N}(0, \mathrm{I})$.

### Questions
- Have authors tried to restore blurry or downsampled image using the controlled forward/reverse ODE? Although it may not reconstruct the true signal exactly, it seems possible to get much clearer image.
- Have authors tried non-rigid editing task? (e.g. dog -> jumping dog)
- Have authors tried local editing (e.g. red flower and blue car -> yellow flower and blue car) rather than global context editing (e.g. man -> woman, photo -> pixar)?
- Have authors reduced the NFE lower than 28? The reviewer just wonder if fast sampling is available even with controlled vector field, which may break the OT path established by reflow. Just for the reference, [1] used fixed point iteration to make more accurate inversion process and demonstrated that the method enables real-time editing using Flux.1 with 4NFEs. This does not mean that comparison with [1] is required.

**Reference**

[1] Lightning-Fast Image Inversion and Editing for Text-to-Image Diffusion Models, arxiv 2023

### Soundness
3

### Presentation
4

### Contribution
4
