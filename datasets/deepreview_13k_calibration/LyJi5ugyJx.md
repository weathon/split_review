# Simplifying, Stabilizing and Scaling Continuous-time Consistency Models

- Decision: Accept
- Avg Score: 9.20
- Scores: 10, 10, 8, 10, 8

## Abstract
Consistency models (CMs) are a powerful class of diffusion-based generative models optimized for fast sampling. Most existing CMs are trained using discretized timesteps, which introduce additional hyperparameters and are prone to discretization errors. While continuous-time formulations can mitigate these issues, their success has been limited by training instability. To address this, we propose a simplified theoretical framework that unifies previous parameterizations of diffusion models and CMs, identifying the root causes of instability. Based on this analysis, we introduce key improvements in diffusion process parameterization, network architecture, and training objectives. These changes enable us to train continuous-time CMs at an unprecedented scale, reaching 1.5B parameters on ImageNet 512×512. Our proposed training algorithm, using only two sampling steps, achieves FID scores of 2.06 on CIFAR-10, 1.48 on ImageNet 64×64, and 1.88 on ImageNet 512×512, narrowing the gap in FID scores with the best existing diffusion models to within 10\%.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper investigates a fundamental topic in consistency models (CMs), specifically the challenges of discretization errors and the resulting training stability issue. Consistency Models can be trained in discrete or continuous time, either from scratch using a dataset or distilled from pretrained teacher scores. CMs' theoretical foundation elucidates the importance of controlling the discretization error and eventually achieving consistency in continuous time. While continuous-time CMs eliminate the discretization errors present in their discrete-time counterparts, they suffer from training instability, a problem that is not yet well understood in the research community.

This work conducts a comprehensive study into continuous-time CMs, covering forward process parameterization, network architecture, and training techniques. The authors first develop a simplified diffusion process formulation called TrigFlow, which unifies EDM and Flow Matching for the first time. Building upon this foundation, they analyze the gradient flow of continuous-time CMs, identify the root cause of training instability, and mitigate this issue through modifications to time embeddings and adaptive group normalization. Additional training techniques, such as adaptive weighting functions and annealing, further contribute to improved training stability and scalability.

The resulting method, sCT/sCD, allows continuous-time CMs to be trained at an unprecedented scale, scaling up to 1.5B parameters on ImageNet 512x512. These results significantly narrow the performance gap between CMs and state-of-the-art diffusion models to less than 10% in FID, while matching or even surpassing adversarial methods and discrete/continuous autoregressive models in both performance and efficiency.

### Strengths
This is a very strong paper in analysis, practical techniques, writing, and experiment results. 

- Novelty. This paper's novelty is evident in several aspects.
    - First, it studies an important but less studied problem: consistency models in continuous time, together with the training stability and discretization error of consistency models. 
    - The proposed TrigFlow, as a novel unification of EDM and Flow Matching, substantially simplifies the analysis presented later and the practical techniques.
    - The gradient analysis of continuous-time objective reveals the root cause of instability. To the best of my knowledge, this is the first paper to establish the gradient analysis for CMs.
    - Model architecture modifications are original since existing works are mostly inherited from Diffusion Models' design and focus on the training techniques and formulations, leaving the architectural design underexplored.

- Soundness. Its technical claims are well backed up by both theoretical analysis and empirical results. I particularly appreciate the in-depth investigation into the training dynamics and gradient analysis of continuous-time CMs.

- Presentation. The logical flow of this paper is well structured and smooth. The problem statement is clearly defined, and the explanation of why discretization errors matter for CMs and the motivation toward continuous-time formulation is crystal clear. The gradient analysis into continuous-time CMs is thoughtfully motivated and carefully organized. Even the appendix is well-written, offering useful insights into the proposed techniques.

- Experiments. Proposed techniques allow for training continuous-time Consistency Models (sCMs) at an unprecedented scale. Experiment results are impressive, matching/outperforming adversarial approaches, score distillation, and recent autoregressive models.
    - Gradient variances have been carefully controlled via adaptive weighting and normalization techniques.
    - Comprehensively studying the scaling behaviors of sCMs under continuous-time training. 
    - Comparisons with improved score distillation baseline using many methods developed in this work confirm the mode coverage of CMs.
    - Additionally, the paper discusses efficient and stable implementation strategies for continuous-time CMs.

Given the potential impact of this paper, I strongly recommend acceptance with conference highlights. It was a great pleasure to read through the manuscript!

### Weaknesses
I did not find any apparent weaknesses in the analysis or experiments (including both ablation studies and performance evaluation). There are research questions worth further investigation, as discussed below.

### Questions
1. I appreciate the scaling study from ImageNet 64x64 to 512x512, where the former operates directly in the image space, while the latter relies on additional image compression models. The difference between sCT and sCD at the 512x512 resolution is intriguing, as even increasing model size and batch size cannot easily close the gap, while at the 64x64 resolution, scaling is sufficient to compensate for the variance induced by Monte Carlo estimation.
    - Data complexity at 512x512 and the lack of effective mode decomposition definitely contribute to this discrepancy. However, I am curious about the authors' thoughts on the extent to which the increased variance could be caused by the pretrained image encoder/decoder. In other words, could data modes become *more dispersed* in the latent space, making it harder for sCT to learn effectively? Would it be better to train CMs directly in the image space (with some special architecture design and weighting schemes) or to find a latent space that is more suitable for CMs? In some sense, modern autoregressive models focus on tokenizer design for visual generation. Could latent space compression for CMs require properties distinct from those used in DMs? While this is more hypothetical, I would be happy to hear more thoughts.

2. If I understand correctly, there are three weighting functions applied, namely learnable adaptive weighting, tangent normalization (per-sample basis weighting), a prior weighting $w(t) = \frac{1}{\sigma_d \tan(t)} = \frac{1}{\sigma_t}$. To what extent does this prior weighting contribute to variance reduction? Is it helpful to stabilize the learnable adaptive weighting layer? I assume the time embeddings of learnable adaptive weighting could be either positional embedding or Fourier embedding since it is not directly involved in $\frac{\mathrm{d} \boldsymbol{f}}{\mathrm{d}t}$.

As an additional comment, could the authors consider conducting distillation experiments using the data-free formulation in [1]? I am curious how continuous-time CMs would scale and how stable they would be without using an extra dataset. No hurry to complete these experiments during the limited rebuttal period!

[1] Consistency Models Made Easy

### Minor

1. In Line 213 and in Line 227, both diffusion models and consistency models are denoted as $f_\theta(\mathbf{x}_t, t)$ but with different equations.

2. The Adaptive Double Normalization is less explained. Is it the same as local response normalization applied to the modulation layer?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors propose improvements to the consistency models generative paradigm and named their new method sCM. Specifically they -vastly- improve the FID for consistency models with the introduction of several new ideas to both stabilize and simplify continuous consistency models. 

My understanding is the main claim of simplification for sCM comes from the simplification of EDM (Kerras et al.) normalizing design, resulting in $c_{in}=c_{skip}=1$ which in turns simplifies the continuous expression of consistency models. Another simplification is the combination of both EDM and Flow Matching concepts into their method which they call TrigFlow. Yet another simplification, not claimed as such by authors, is the use of vanilla L2 loss compared to Huber/LPIPS use in previous iterations of consistency models. This last simplification has the additional benefit to be more probabilistically grounded.

There are 3 main proposed ideas to stabilize the training of consistency models:
1. Identity-time transformation as a replacement to the log-transformation from EDM
2. Fourier embedding of the time dimension are replaced by positional embeddings
3. AdaGN is modified to also normalize the conditioning inputs for scale and bias.
More ideas are also proposed in the training objective to stabilize training, namely: tangent normalization and tangent warmup. It is my understanding that the adaptative weighing is the same as in EDM.

The paper also provides ample ablations to demonstrate the effects and the reasoning motivating these 3 proposed improvements.

### Strengths
The paper is very well grounded mathematically and experimentally. The analysis is based on understanding the causes of training instabilities by decomposing the loss, validating each component experimentally and proposing changes to solve the root causes.
The mathematics while greatly simplified are still pretty complex and the paper shines in its clarity to make the logical reasoning easy to follow.
The experimental results are also outstanding resulting in very significant gains, essentially taking consistency models within 10% of the SOTA for diffusion models.

### Weaknesses
1. The limitations of the method are not very clear to me besides the fact that it's still 10% worse than SOTA for diffusion.
2. The section on positional embeddings (line 269 and on) lacks details to be fully understandable without having to read another paper. Maybe beefing up that section would make the paper more self-contained.
3. I found all figure very useful with the exception of Figure (3) which I felt did not add much value.

I also noticed a typo (definitely not affecting my score), just leaving it there for authors to fix their manuscript:
- Line 362: "cause instability" => "causes instability"

### Questions
These are mostly from the weakness section:
1. Are there more limitations other than the 10% worse than diffusion SOTA?
2. Is the method really fully stable?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a unified perspective on diffusion-based and flow-based generative models and introduces a comprehensive set of techniques aimed at improving the training stability and overall performance of continuous-time consistency models for large-scale image generation. The techniques include: 1) enhancing time transformation and embeddings, 2) replacing the AdaGN layer with Adaptive Double Normalization, 3) normalizing the tangent function and applying tangent warm-up, 4) implementing an adaptive weighting function in the training objective, and 5) optimizing forward-mode differentiation. These techniques mitigate the numerical instability issues in continuous-time consistency models and enable the model to achieve highly competitive performance in class-conditioned image generation.

### Strengths
S1 - The paper provides a comprehensive analysis and set of solutions addressing the numerical instability issues in continuous-time consistency models, significantly improving performance and enabling the model to achieve competitive results on selected benchmarks.

S2 - Many of the enhancements are supported by detailed theoretical justification and experimental results.

S3 - The unified perspective on previous diffusion and flow-matching parameterizations is thorough, complete, and well-grounded, offering novel insights that could benefit the community.

S4 - The paper is well-structured and easy to follow.

### Weaknesses
W1 - Several design choices appear arbitrary and lack supporting evidence. 

For example, in Section 4.1, the authors discuss the preference for Adaptive Double Normalization over AdaGN, but there is no experimental evidence supporting this choice. It would be more insightful to add a Figure similar to Figure 5 show experimental comparison between Adaptive Double Norm and AdaGN. Specifically, a comparison of training stability (e.g., loss curves) and sample quality (e.g., FID scores) across different training iterations would be beneficial. This would provide a clearer understanding of the practical advantages of Adaptive Double Normalization over AdaGN, beyond the claim of divergence.

Similarly, in Section 4.2, the authors propose training with linear warm-up w.r.t the model's time derivative, yet no evidence is provided to demonstrate this choice’s effectiveness. Again, including an ablation study or comparative analysis showing the impact of the linear warm-up on training stability or performance metrics would provide more concrete evidence for the effectiveness of this specific choice. For instance, comparing the training dynamics (e.g., gradient magnitudes, loss fluctuations) with and without the linear warm-up could offer valuable insights.

Furthermore, Figure 5(b) suggests that incorporating adaptive weighting in a two-step setting may lead to worse performance, while in the one-step setting, it only yields marginal improvement. Have the authors considered alternative designs for the two step case? It is unclear if the adaptive weighting function is optimized for the two-step setting, or if the same function is used for both one-step and two-step sampling.

W2 - In Sections 4.1 and 5.2, the paper discusses the training compute of sCM. However, including a comparison of compute efficiency with other models (e.g., ECT [1]) would be more insightful, maybe a table or figure comparing the compute efficiency (e.g., FLOPs or training time) of sCM against ECT and other relevant baselines for a given performance level. A detailed comparison should include not only training time but also inference time and memory usage, providing a more comprehensive view of the computational trade-offs. Additionally, given that the model is trained on a large-scale dataset (ImageNet 512) under latent setting, it would be beneficial to include discussions related to text-to-image generation. It is unclear how the proposed techniques would generalize to text-to-image models, which often involve more complex architectures and training procedures.

### Questions
Q1 - In Section 4.1, the authors emphasize the importance of time transformation in mitigating numerical instability. Have the authors considered other potential candidates for time transformation?

Q2 - In Figure 6(a) and Section 5.2, the authors mention that sCT is less effective at higher resolutions. Do the authors have any insights into why this might be?

Q3 - In Figure 6(b), it appears that the performance of sCD-XL under the two-step sCD setting is better than that of sCD-XXL, which contradicts the results reported in Table 2. Could the authors clarify the specific settings used in Figure 6(b)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper tackles the problem of  instability in continuous consistency models and presents many contributions. 

The first novelty is the simplification of model parametrization in the EDM/CM frameworks. It is shown that rescaling the mean ($\alpha_t$ ) and noise ($\sigma_t$) schedule of conditional probability flows with the norm $||(\alpha_t, \sigma_t)||$, produces a second conditional flow, such that the EDM model parametrization and loss in the first are identical to those in the second. Furthermore, the ODE sampling procedure remains unchanged. However, the connection between the new flow schedule parameters and the  EDM scaling parameters is greatly simplified after normalization, facilitating further theoretical analysis, while maintaining the benefits of the EDM model definition (unit variance of input, target and minimizing the scaling of the output). The formulation with $\alpha_t=cos(t)$ and  $\sigma_t=sin(t)$ is named *TrigFlow*.

Then the training objective is studied and probed for causes of instability. Several factors are detected such as: an inappropriate $c_{noise}(t)$ which is fixed by being set to $t$; inappropriate Fourier scales in the time positional embeddings which are then reduced; the usage  'AdaGN layer', which is then replaced with 'Adaptive Double Normalization'; highly varying target norm alleviated by target normalization; inappropriate weighting mitigated by adaptive weighting and unstable terms solved by slowly introducing such terms into the loss with respect to the number of parameter updates. 

In addition, methods for scaling such models to large sizes and datasets are proposed, namely JVP Rearrangement and JVP of Flash Attention.

Finally, the proposed models are compared against the state of the art methods, and results show that continuous consistency models are excellent generators, that only require 1 or 2 sampling steps to generate new quality data from learned distributions with continuous support.

### Strengths
The contributions of this paper are novel, clear, significant and positioned correctly.

Trigflow simplifies the theoretical analysis of flows by showing that  the mean ($\alpha_t$ ) and noise ($\sigma_t$) schedule in the definition of conditional flows can be normalized while preserving the model/loss formulation and the integrator-generated paths, while simplifying the connection between the scaling parameters of the model and those of the conditional flow. **(novelty, significance)**

Several components of continuous consistency models are studied and probed for potential causes of instability. They include: an inappropriate $c_{noise}(t)$ which is fixed by being set to $t$; inappropriate Fourier scales in the time positional embeddings which are then reduced; the usage  'AdaGN layer', which is then replaced with 'Adaptive Double Normalization'; highly varying target norm alleviated by target normalization; inappropriate weighting mitigated by adaptive weighting and unstable terms solved by slowly introducing such terms into the loss with respect to the number of parameter updates.  **(novelty, significance)**

Strategies for scaling such models to large sizes and datasets are proposed, namely JVP Rearrangement and JVP of Flash Attention. **(quality, significance)**

The proposed method shows competitiveness with the state of the art models, while only using 1 or 2 steps for generation, and outperforms all other tested methods that use 1 to 2 generation steps **(significance, quality)**

### Weaknesses
While the contributions of the paper are numerous, the paper could be strengthened even further by:

1) Comparing the proposed model with more recent flow models such as [1] and [2] and adding the results for rectified flows with 2 generation steps.

2) Placing the number of parameters and the number of parameter updates (or training time on identical hardware) for each model in Table 1 is very important as using an equal umber of parameters/compute is essential for ensuring a fair comparison.

Some smaller issues and suggestions:

a) The paper would be improved if an intuitive explanation is given for the loss in Equation 2. Also it could save readers some time if it is mentioned that the loss is derived in Song et al 2023, *Remark 10*.

b) The paper would be enriched by adding some generated images with one step.

c) Shouldn't $c_{skip}$ and $c_{out}$ be $\sigma_t$ and  $ \alpha_t \sigma_d$, that is for $\sigma_t=t$ and  $\alpha_t=1$: $c_{skip}=t$  and $c_{out}=\sigma_d$ in line 201/202?

d) In Equation (20) Appendix, shouldn't it be $\hat{D}$ for $D_{\theta}(x_t)=\hat{D}_{\theta}(\hat{x}_t(x_t))$?

e) The paragraph from line 924 to 938 (appendix) needs additional elaboration regarding the implications of having $||(\alpha_t, \sigma_t)||=1$ with respect to the invariance of the geometric set connecting $x_0$ and $z$.


Typos:

i) In line 126, a 2 is squared instead of the norm.

ii) in line 122, $z_t$ does not depend on time.

### Questions
How do the proposed models compare with [1} and [2]? Even tests on a small dataset using small models of equal size would be informative.. I completely understand however  if such comparisons cannot be made due to the short length of the discussion period. 

Shouldn't $c_{skip}$ and $c_{out}$ be $\sigma_t$ and  $ \alpha_t \sigma_d$, that is for $\sigma_t=t$ and  $\alpha_t=1$: $c_{skip}=t$  and $c_{out}=\sigma_d$ in line 201/202?

Based on the experiments performed, are there any indications that the continuous consistency models will still face instability issues for even larger scales, in particular as compared to diffusion/flow models? This question mostly relates to this part in the paper: "Additionally,
we observe that consistency training is more effective at smaller scales but suffers from increased
variance at larger scales, while consistency distillation shows consistent performance across both
small and large scales."

[1]  Tong et al. 2024. Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport

[2]  Kornilov et al 2024. Optimal Flow Matching: Learning Straight Trajectories in Just One Step

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposed a set of improved training techniques to stabilize the training of continuous-time consistency models, including new consistency function formulations, new network architectures and new training objectives. With these new training techniques, the proposed method called sCMs outperformed all previous consistency models in terms of one-step and two-step FIDs.

### Strengths
- This paper is very well-written and easy to read. 
- This work proposed a new diffusion formulation, called TrigFlow, that unifies EDM and Flowing Matching, and also simplifies the analysis of continuous-time consistency models. 
- It provided a thorough analysis of the training stability of continuous-time consistency models, from the perspective of network architecture, training objective and diffusion process parameterization.
- Experiments on CIFAR-10, ImageNet-64 and ImageNet-512 demonstrate the effectiveness of the proposed method and the scalability of continuous-time consistency models.

### Weaknesses
 - Although I really like the improvements of continuous-time consistency models, which could fundamentally eliminate the discretization error in discrete-time consistency models, it comes with more time and memory costs related to JVP computation in the loss function. To this end, this work introduces JVP of Flash Attention to reduce the costs, which is great. Still, there may be a considerable gap between the continuous-time and discrete-time consistency models. I wonder if the paper can provide a more detailed comparison between sCMs and the previous discrete-time consistency models - ECMs, in terms of the training convergence and memory cost. 
- There is no explanation for the phenomenon that sCT performs better than sCD on CIFAR-10 and ImageNet-64, but sCTs performs worse on ImageNet-512. Any intuition of why sCT suffers from increased variance at larger scales? 
- There are no ablation study results on “Adaptive Double Normalization” except for claiming it “removes its instability in CM training”.
- In Figure 5b, it looks like “w/o adaptive weighting” achieves better two-step FIDs than “w/ adaptive weighting” and very similar one-step FIDs to “w/ adaptive weighting”. Why do we need adaptive weighting?
- In Figure 5c, do discrete-time CMs have a constant number of time steps $N$ or a timestep schedule up to the maximum number of steps $N$? If it is the former one, it seems to be a bit unfair to discrete-time CMs because the scheduling of time steps is very important to them. Does it make more sense to compare with the best-performing discrete-time CMs?
- In Figure 7, does the paper apply TTUR proposed by DMD2 (Yin et al. 2024a)? From the DMD2 paper, TTUR improves the performance of VSD. Thus, a comparison with VSD + TTUR is more convincing.
- In Figure 7, sCDs condition the consistency network on the guidance scale $s$. I wonder if VSD also condition the generator on the guidance scale, for a consistent evaluation setting? 
- A minor issue: In line 266, should it be $c_{\text{noise}}(t) = \frac{1}{4} \log(\sigma_d \tan t) $?

### Questions
See the weaknesses in the above.

### Soundness
3

### Presentation
3

### Contribution
3
