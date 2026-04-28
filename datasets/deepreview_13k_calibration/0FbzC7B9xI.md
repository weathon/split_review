# Truncation Is All You Need: Improved Sampling Of Diffusion Models For Physics-Based Simulations

- Decision: Accept
- Avg Score: 6.60
- Scores: 6, 8, 8, 5, 6

## Abstract
State-of-the-art Denoising Diffusion Probabilistic Models (DDPMs) rely on an expensive sampling process with a large Number of Function Evaluations (NFEs) to provide high-fidelity predictions. This computational bottleneck renders diffusion models less appealing as surrogates for the spatio-temporal prediction of physics-based problems with long rollout horizons. We propose Truncated Sampling Models, enabling single-step and few-step sampling with elevated fidelity by simple truncation of the diffusion process, reducing the gap between DDPMs and deterministic single-step approaches. We also introduce a novel approach, Iterative Refinement, to sample pre-trained DDPMs by reformulating the generative process as a refinement process with few sampling steps. Both proposed methods enable significant improvements in accuracy compared to DDPMs, DDIMs, and EDMs with NFEs $\leq$ 10 on a diverse set of experiments, including incompressible and compressible turbulent flow and airfoil flow uncertainty simulations. Our proposed methods provide stable predictions for long rollout horizons in time-dependent problems and are able to learn all modes of the data distribution in steady-state problems with high uncertainty.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a truncation approach and an iterative refinement process in the sampling procedure of the Denoising Diffusion Probabilistic Model (DDPM) that enable to reduce the number of function evaluations without decreasing the accuracy. The first method proposes to stop the sampling process at an earlier time point and to estimate the denoised sample using Tweedie's formula. The second method uses the forward diffusion for a given shorter noise schedule and the denoised sample is approximated using Tweedie's formula. The authors show the efficiency of the approach on the simulations of airflow field.

### Strengths
The paper reads very well and provides some good contributions to the development of diffusion models. 

   - Although the presented approach is based on some known results (Tweetie's formula, ancestral sampling), the proposed solution seems very efficient in practice and leads to lower computational costs. Both idea's exploit the denoising Tweedie's formula in forward and backward sampling.

   - Including the truncation in the training is smart trick that eases the training. 

   - The numerical experiments show that the presented approaches achieve better performances than traditional DDPM sampling and reduce the computational costs.

- The approach seem to be very efficient in physic based simulation of flow field. I think this is a very good contribution in this specific domain.

### Weaknesses
Although the approach seems efficient in the presented numerical experiments, there is a number of points that need to be clarified. 

- Tweedie's formula is well known. It seems that this has been already used in some previous works such of [Delbracio et Milanfar, 2024]. In  their work, the authors provide some intermediate reconstructions through this formula. They show that by adding some stochastic steps 
they can get better performances than state-of-the-art. I know the model is not the same but it would have been interesting to highlight the links with this work because they seem very closely related. May the authors comment on that point?

- The results show that TS outperforms traditional DDPM by using s=1. This means that on this specific problem, there is no need to sample intermediate diffusion steps. I wonder whether this aspect is problem specific or this happens for a wider range of problems. Is this result expected? 

- This would have been interesting to see how this method perform against traditional DDPM sampling on image reconstruction. Indeed, DDPMs usually perform well on such problems.

- The training data are deterministic sequences of flow field data. It would have been interesting to observe how the model performs on noisy dataset. 

- Overall, I like the idea of truncation and iterative refinement, but since there is no major theoretical contribution in this work, I would have liked to see more numerical results. The claim "Truncation is all you need" would have been justified if the authors had included numerical results on different applications. So far, the paper makes very good contribution in this specific domain, and proposes an interesting approach to reduce computational costs.

### Questions
- Does s=1 mean that the model is trained as a single variational autoencoder? Or is this truncation only used for sampling? (paragraph about the training is not clear to me)

- naive question for my understanding: At the beginning of Section 5.1, the authors say that they consider time series of flow field from j= 1 to T. It is not clear how the time series are handled here. Could the authors clarify this point?

- How do the authors handle the high fluctuations areas of the domain? It seems that some region of the domain have a highly turbulence flow field (low pressure vortex) and this would require a more flexible model in this specific area. 

- Did the authors try to change the value of the initial input $x_{init}$? 

I look forward to reading the answers of the authors and I can change my score depending on their answers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This article first analyzes DDPM and finds that after an appropriate truncation (stop diffusion), the model has high fidelity and high-efficiency sampling performance. On this basis, an iterative refinement method is introduced to further improve accuracy and long-term stability.

### Strengths
Advantages:

1. As we all know, if we consider an infinite boundary heat equation (diffusion process), or consider long-term diffusion, then the usefulness of a long part of the noise addition/noise reduction behavior is not that great. The article fully considers and utilizes the diffusion behavior in a finite time (truncation), thus achieving a balance between accuracy and running time, which is a very good point.

2. Truncated sampling reduces the uncertainty of the sample to a certain extent, or increases the accuracy of the sample response distribution.

3. Based on the content of the appendix(in particular, part D), the experimental effect is very significant. In other words, iterative refinement even makes up for the truncated sampling to a certain extent (the useful information and samples that are truncated).

### Weaknesses
Disadvantages:

1. I want to know whether there is a mathematical inference for the truncation sampling standard, or whether it is completely based on experience, that is, truncation and retention (importance) interpretability.

2. The purpose of refinement iteration and truncation sampling is to improve efficiency while ensuring a certain degree of accuracy. I think this requires a game. How to achieve such a balance? Is there a more rigorous mathematical explanation?

3. I think experiments can increase the breadth. One is to compare with a more general SDE instead of just with DDPM (and Kohl's 2024 work). In addition, for experiments, do you consider more general PDE solutions?

### Questions
The experimental results are very good, and I hope to add more theoretical analysis.  I will be happy to improve my score in subsequent discussions.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the application of diffusion models to physics simulations. Over the past years, neural networks have emerged as surrogate modeling approach for physics simulations, with a key use-case being computationally efficient inference. However, for this purpose, diffusion models have the drawback of requiring many function evaluations due to their iterative ancestral sampling procedure. To this end, the authors propose two contributions: (1) truncation of the last steps of the reverse diffusion process, and (2) iterative refinement, which considers a much shorter noise schedule at inference time. Both methods reduce the number of function evaluations and thereby increase sampling speeds. Moreover, the empirical results demonstrate that accuracy is generally maintained and sometimes even improved compared to standard expensive sampling procedures.

### Strengths
**S1:** The experimental setup is rigorous, comparing methods in both pointwise metrics and relevant physics-based metrics to provide complementary perspectives on their performance for three relevant datasets. Moreover, many additional results and baselines can be found in the appendix, making an extensive empirical evaluation overall.

**S2:** Two methodological contributions are evaluated: truncation of the last steps of the reverse diffusion process, and iterative refinement, which optimizes the inference sampling schedule such that less denoising steps are required. Both contributions are aimed at reducing the number of function evaluations to improve computational complexity of diffusion models for physics simulations. This is a relevant research direction, since reducing computational complexity of computational procedures is one of the primary use-cases of neural simulation models, for which diffusion is emerging as a promising modeling approach. 

**S3:** The paper is well-written, and the explanations of the proposed algorithms are intuitive and easy to follow and understand. The clear structure of the text helps the reader to efficiently navigate the paper.

### Weaknesses
 **W1:** While reading the text, I found it difficult to distill what the key differences between iterative refinement and PDE refiner are (Lippe et al., 2023). Does it have to do with the greedy optimization method of the refinement schedule (to my knowledge PDE refiner uses a fixed schedule), or details in the formulation of the diffusion process (a nonzero vs zero drift term in IR and PDE refiner respectively), or something else? Since both IR and PDE refiner are quite similar, it would be good if the ‘method novelty’ paragraph explicitly contrasts the two approaches and highlights their differences. Additionally, if the greedy optimization of $\gamma$ is a core novelty relative to PDE refiner, then it would be beneficial to explain this more elaborately in the main text rather than the appendix, since it would be a key aspect of one of the contributions in this case.

**W2:** One of the goals of the paper is to show that the proposed methods close the gap between the diffusion models and deterministic baselines. However, most of the results in the main text (both tables and plots) focus only on diffusion models. It would be relatively straightforward to also show the results of one or two deterministic methods that are considered by the authors in part of the plots and tables, for example in Figure 2 and Table 2. This would help the reader to get a better understanding of the tradeoffs of existing diffusion-based approaches, deterministic approaches, and the proposed methods without taking additional space in the paper.

**W3:** The conditioning on the autoregressive step size (j in Sec. 2 of the paper) is already introduced in Gupta et al (2022), and as such cannot be claimed as a contribution of the paper (currently point 1 of the contributions listed in the introduction). Since this is not a core point in the rest of the paper, it seems that this can straightforwardly be removed from the list of contributions in the introduction without affecting the rest of the work and the core contributions significantly.

### Questions
**Q1:** Given that PDE-refiner is conceptually relatively similar to iterative refinement, I am surprised to see a quite large performance difference between the two methods in Appendix D.1. Can the authors explain the reasons behind this large performance gap?

**Q2:** The truncation of the last steps of the reverse diffusion process seems to be equivalent to a modification of the noising schedule: we can choose the noise schedule $\beta_t$ such that the first step in the forward diffusion process has already a quite low signal-to-noise ratio (in line with the level corresponding to the last step before truncation in the reverse process), and afterwards noise is added gradually as per usual, while reducing the total amount of steps in the forward process in line with the skip percentage. Can the authors provide their thoughts on this perspective and whether or not they agree? If they agree, can they comment on why the noise schedule that is equivalent to the truncated process is a good choice for this problem setting relative to other problem settings, and in this way place their contribution in the broader context of noise schedules?

**Q3:** Please comment on W1-W3.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Truncated Sampling Models (TSMs) and Iterative Refinement (IR) to improve the efficiency and fidelity of Denoising Diffusion Probabilistic Models (DDPMs) for fluid simulations by enabling reduced steps sampling through truncation of the diffusion process. These methods significantly reduce inference time and improve stability over long rollout horizons for turbulent flow and airfoil simulations.

### Strengths
- Interesting topics – Generative diffusion models as surrogate model for fluid simulations.
- Clear motivation – Reduce computation costs in the generative process using a novel reverse sampling approach.

### Weaknesses
 - The paper lacks clarification of superiority of the proposed methods over other surrogate models, such as neural operators which are currently the most widely used ML-based surrogate models in fluid dynamics for speed and accuracy. Given that a primary contribution of this paper is reducing time costs, a more thorough comparison with advanced neural operators – either highlighting the proposed method’s improved accuracy at similar time costs or its time efficiency at comparable accuracy – would strengthen the argument. However, there are few comparisons with neural operators in the experiments in main text; although Unet is included, more advanced neural operators should be included. Additionally, the proposed method does not appear to clearly outperform Unet.
- The title may mislead some readers, as “physics-based simulations” implies a broad range of applications, while the paper is mostly on fluid dynamics. To improve clarity, I recommend replacing “physics-based simulations” to “Fluid Dynamics Simulations”. Alternatively, the authors could clarify whether they intend to generalize their approach to other physics-based simulations beyond fluid dynamics or provide examples of how the method could be applicable to other physics domains.

### Questions
- Could you theoretically or intuitively clarify the effectiveness of the pre-trained diffusion model in the IR sampling procedure at noise level $t = \gamma $? The distribution $x_{init}$ at noise level $t = \gamma $ appears to differ from the distribution $x_0$ at the same level $t = \gamma $. Additionally, in Equation 6, is it ensured that the error between the final output and the $x_0$ remains sufficiently small, such that $E[‖x _0^N - x_0 ‖_2 ]<\epsilon $?

- Could you also clarify (experimental support would be helpful) line 288 (2), which states that IR sampling does not require data consistency to $\hat{x}_0$? I mean why the proposed method does not require the data-consistency? Enforcing data consistency to $\hat{x}_0$ could be plugged in after line 7 in Algorithm 2 to improve accuracy in a single iteration, without compromising the number of iterations needed. Also, related to the above question, data consistency could help reduce the error towards zero, such as [1] and [2]. 

[1] A physics-informed diffusion model for high-fidelity flow field reconstruction, 2023.

[2] Diffusionpde: Generative pde-solving under partial observation, 2024.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the high computational requirements of existing diffusion-based techniques for modelling dynamical systems. They propose two sampling techniques that lead to good sample quality with only a few NFEs. The first one requires modifications to the training process and is performed by truncating the diffusion process close to the clean data. The second one is compatible with pre-trained DDPMs and proposes an iterative refinement based on Tweedie’s formula. The paper provides extensive experimental evidence on three datasets: incompressible and compressible turbulent flow (2D) and airfoil flow simulation (3D).

### Strengths
1. **Relevant topic.** Lately, there has been increasing interest in modelling dynamical systems with diffusion models due to their probabilistic nature. However, many works (Kohl et al. [1], Shysheya et al. [2], Lippe et al. [3]) acknowledge that diffusion models tend to be computationally costly, and techniques that reduce this cost would be greatly beneficial. This is exactly the problem this paper aims to address.
2. **Clear distinction from other works.** The paper clearly delineates its contributions from the already existing work, and how the proposed sampling techniques differ from other approaches.
3. **Good experimental evidence.** The paper provides good empirical evidence, with experiments on three diverse datasets, and using a wide range of metrics.
4. **Well-structured, clear writing.** Overall, I found the structure and writing clear.

[1] Kohl, G., Chen, L., & Thuerey, N. (2023). Benchmarking Autoregressive Conditional Diffusion Models for Turbulent Flow Simulation.

[2] Shysheya, A., Diaconu, C., Bergamin, F., Perdikaris, P., Hern'andez-Lobato, J.M., Turner, R.E., & Mathieu, E. (2024). On conditional diffusion models for PDE simulations.

[3] Lippe, P., Veeling, B.S., Perdikaris, P., Turner, R.E., & Brandstetter, J. (2023). PDE-Refiner: Achieving Accurate Long Rollouts with Neural PDE Solvers. ArXiv, abs/2308.05732.

### Weaknesses
1. **Unclear how the method generalises to other settings.** I acknowledge that the aim of the paper is to study the efficacy of the proposed sampling methods in the context of dynamical systems. As the authors mention, the fact that they lead to good results is probably due to:
- The characteristics of the data distribution—states with fairly coarse resolutions, where the high frequency information has been lost during downsampling.
- The task considered—predicting next step (forecasting) distribution, which is predominantly unimodal.
  
  I’d be curious to know whether the sampling methods remain applicable 
  - for other tasks that might require modelling multimodal distributions: e.g. some sort of inverse problem (reconstruct field based on sparse, partial observations, compatible with multiple solutions), which is also a task of interest in dynamical system modelling, 
  - or for other datasets: potentially still PDEs but not as coarsened and with more complicated nonlinear behaviour, or images. 

  One could argue that Air_multi requires sampling from a more complicated distribution, and there the improvements are not as pronounced as in other settings. Perhaps you could include a brief discussion on this, or a preliminary experiment on a more complex PDE dataset, such as Kuramoto-Sivashinsky (see **Q1**)?
2. **Counter-intuitive comparison to DDPM.** Maybe this is not necessarily a weakness, but I find it counter-intuitive that these sampling methods outperform DDPM, given that DDPM (or at least the continuous-time frame formulation) has stronger theoretical foundations (Similarly to how DDIM is posed as a framework where you can trade off computation for sample quality, not gain in both). I would have expected the same accuracy with significantly fewer NFEs to be possible, but not both. Is it possible that the DDPM model could be further tuned to achieve similar performance and maybe the DDPM baselines are not optimal? Maybe this is where a comparison with EDM would have been beneficial, as it provides a more principled approach of setting up diffusion models.
3. **Lack of theoretical guarantees.** While the methods seem effective in practice, the paper does not provide any theoretical guarantees. I realise this might be hard to derive, but this makes the applicability of the methods more ad-hoc. This also reflects in the empirical investigation, where there is no clear recipe for what works best and how one should choose the hyperparameters optimally.
Also when making statements such as “However, we assert that
our methods will consistently improve over ancestral sampling, as demonstrated in our experiments.” - This was only shown in three experiments, and the paper does not contain guarantees that this would always hold, so I would avoid over-generalising.
4. **Lack of analysis of the stability of longer rollouts.** The paper provides several metrics to analyse the performance of the sampling methods, but none provides intuition/results about how the metrics evolve in time for the transient datasets (Tra and Fturb) (e.g. per-time-step MSE or per-time-step correlation). In particular, I’d be interested to compare the performance of the benchmarks to your methods on rollouts longer than what the model has been trained on. (This could, for instance, be tested on Tra_long from Kohl et al. [1]).
  
    I think that one potential weakness of these sampling schemes is that they lose more of the high frequency information than the traditional sampling schemes. Maybe this doesn’t affect the short rollouts significantly but it might negatively impact the accuracy of longer term rollouts (see Lippe et al. [3]). It would also be good to check that if extended significantly beyond the training range, the proposed sampling methods still generate physically plausible states, and outperform the baselines.
5. **Lack of a comparison to EDM.** While I agree that a comparison to, for example, distillation techniques is outside the scope of the paper, I think EDM is relevant as a baseline. The fact that it is “designed to handle more complex stochastic data with multimodal distribution” does not mean it is not relevant for cases that do not exhibit much stochasticity. And it shouldn’t incur a different computational cost at training time. I think a comparison to EDM would be very useful to the community to figure out what the fastest and most accurate way to set up diffusion models for dynamical systems is. If the methods proposed here outperform EDM, this makes the paper stronger. If they don’t, I think this would also be a valuable result, potentially implying that EDM is a robust technique (regardless of data distribution) that should be used as a “first thing to try” as opposed to spending time and resources on hyperparameter tuning of more ad-hoc techniques.
   Maybe the authors could include a comparison to EDM on one or two experiments?
6. **Unclear experimental setup.** I found it hard to figure out some experimental details in certain places. I am aware these details exist in other papers (Kohl et al. [1]), but for ease of interpreting the results, it would help to include some more details, potentially as a brief table in the appendix which summarises the most important dataset characteristics. For example: 
   - Tra - What is the Mach number range of the training trajectories? Is it also Ma $\in [0.53, 0.63] \cup [0.69, 0.90]$ as in Kohl et al.?
   - Tra - How many trajectories are there per Mach number?
   - Fturb - I am slightly confused about the number of states within each trajectory for this dataset. You mention that each simulation contains 51 temporal states, but do you just consider 30 out of these for the test results? And what do you mean by “AR sampling is employed for $R = 30$ timesteps … for two sequences per $Re$?”
   - Fturb - you are feeding in the $Re$ number as conditioning information to the model as in Kohl et al., right?

**Minor**

7. **Comparison to DDIM (L306)** - You say that “IR should supersede the deterministic DDIM sampling regarding accuracy and NFEs” due to its stochastic nature. While I agree that stochastic sampling is beneficial because it can correct previous errors in sampling, Karras et al. [4] mention that, in practice, the situation is more complex because approximating the extra Langevin term introduces error in itself (see Section 4 Stochastic sampling). Thus, I would not say there is any guarantee that IR would supersede DDIM in all scenarios.
8. **Lack of discussion on $j$.** I find it interesting that the optimum $j$ value varied so much between methods, as shown in Tables 6 and 7, but you do not include any discussion about this. Do you have any insight about why this might be the case?
9. **Small typos**, such as L291 “to be evaluated”, L776 “presnted”, L772 “where” missing at the beginning of the line, L819 “allow” rather than “allows”, L840 “are not needed” etc.

### Questions
1. **Regarding W1** - I’d be curious to see how the methods perform on dynamical systems with more complicated nonlinear dynamics, for example the Kuramoto-Sivashinsky equation used in PDE-Refiner (Lippe et al. [3]). That is a fourth-order non-linear equation where correctly capturing the high frequencies seems to be more important than in other settings, so it would be interesting to see how you compare there with benchmarks such as PDE-Refiner [3] (which can also be interpreted as a refinement of an MSE-trained one-step prediction). 
2. **Regarding W2** - Do you have any intuition why these methods outperform DDPM and whether the DDPM baseline could be improved?
3. **Regarding W4** - Could you provide some experiments that test the long rollout performance of these sampling methods vs. traditional ones? Including frequency spectra of generated states would also help.
4. **Regarding Minor 2** - It seems that in general the optimum $j$ for these methods is between [2, 4], but have you noticed any significant patterns? Were there differences between interpolation and extrapolation tasks?
5. **Eq (5).** I am not sure I understand this equation. I will omit the $\theta$ in the $p_{\theta}$ subscript because the equations do not render correctly. If $p^T(x_T, \mathbf{x}_0, j) = \mathbf{x}(j \cdot \delta t)$, then wouldn’t $\mathbf{x}(2j \cdot \delta t) = p^T(x_T, \mathbf{x}(j \cdot \delta t), j) = p^T(x_T, p^T(x_T, \mathbf{x}_0, j), j)$ (i.e., we still start from white noise $x_T$, but we now condition on the output of the previous step)? In my mind $\mathbf{x}(\tau_f) = p^T(x_T, p^T(...p^T(x_T, \mathbf{x}_0, j)...), j)$, but maybe I didn’t interpret the equation correctly.
6. When comparing the results in Table 5 vs. Tables 6 and 7 - Shouldn’t the metrics corresponding to, for example, Fturb TSM T80 s =0.75 ($j=2$) from Table 5 ($3.63 \pm 1.95$) be the same as in TSM T80, s=0.75 with optimal $j=2$ ($3.43 \pm 3.03$) Table 7? What’s the difference between these settings?

**----Update after rebuttal-----**

The majority of my concerns have been addressed and I believe the paper offers a useful empirical investigation into how to speed up sampling with diffusion models for physics-based simulations. As such, I increased my score to 6.

### Soundness
2

### Presentation
3

### Contribution
2
