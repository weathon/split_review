# Cohesion: Coherence-Based Diffusion for Long-Range Dynamics Forecasting

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3

## Abstract
We recast existing works on probabilistic dynamics forecasting through a unified framework connecting turbulence and diffusion principles: Cohesion. Specifically, we relate the coherent part of nonlinear dynamics as a conditioning prior in a denoising process, which can be efficiently estimated using reduced-order models. This fast generation of long prior sequences allows us to reframe forecasting as trajectory planning, a common task in RL. This reformulation is beneficial because we can perform a single conditional denoising pass for an entire sequence, rather than autoregressively over long lead time, gaining orders-of-magnitude speedups with little performance loss. Nonetheless, Cohesion supports flexibility through temporal composition that allows iterations to be performed over smaller subsequences, with autoregressive being a special case. To ensure temporal consistency within and between subsequences, we incorporate a model-free, small receptive window via temporal convolution that leverages large NFEs during denoising. Finally, we perform our guidance in a classifier-free manner to handle a broad range of conditioning scenarios for zero-shot forecasts. Our experiments demonstrate that Cohesion outperforms state-of-the-art probabilistic emulators for chaotic systems over long lead time, including in Kolmogorov Flow and Shallow Water Equation. Its low spectral divergence highlights Cohesion's ability to resolve multi-scale physical structures, even in partially-observed cases, and are thus essential for long-range, high-fidelity, physically-realistic emulation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Cohesion, a coherence-based diffusion model for long-range dynamics forecasting, aimed at addressing challenges in autoregressive probabilistic forecasting.

### Strengths
- The integration of turbulence and diffusion principles with ROM-based conditioning is novel and provides a new approach for multi-scale and chaotic systems.
- This paper uses quantitative (RMSE, MAE, MS-SSIM) and physics-based metrics (spectral divergence), provide strong empirical support.

### Weaknesses
 - Lack of interpretability. How to prove the role of coherent flow after decomposition and how it promotes long-term stability prediction? Lack of theoretical explanation.

- Please explain what the zero-shot forecasts without classifier and multi-scale physical structure mentioned in the paper are. There exists confusion in the statements.

- Please explain why SFNO is used as the baseline. SFNO is mainly used to predict atmospheric dynamics. Intuitively, the datasets used in this paper are not suitable for spherical geometry operators. Please give an explanation.

- The baseline only uses SFNO. Why not compare other neural operator models, such as CNO[1], UNO[2], LSM[3], etc.

- The model is based on Diffusion. Why not compare diffusion-based models, such as PreDiff[4] and DYffusion[5].

- The time complexity comparison analysis of the model should be increased.

### Questions
Please address the questions in the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Cohesion, a framework for probabilistic dynamics forecasting in chaotic systems like fluid dynamics. By reframing forecasting as a trajectory-planning task, the framework makes use of reduced-order models (ROM) to make denoising processes more efficient. This approach is much faster because it applies a single denoising pass to the whole forecast sequence, rather than using multiple autoregressive steps. Cohesion also includes a way of guiding the process without using classifiers, which makes it suitable for zero-shot forecasting. Tests on the Kolmogorov Flow and Shallow Water Equation show that Cohesion works better than other methods for capturing multi-scale physical structures and reducing spectral divergence, which is important for modeling chaotic systems accurately.

### Strengths
The framework is innovative in its approach to combining turbulence theory, conditional generative model, and reinforcement learning principles for forecasting. By applying diffusion models with coherence-based conditioning, the paper contributes a novel perspective on long-range forecasting. The idea of Turbulence-diffusion framework and the induced Zero-shot conditional sampling is interesting and inspiring.  Cohesion presents a promising solution for long-range dynamics forecasting, especially in chaotic and partially observed environments. Experiments are exhaustive.

### Weaknesses
 **Over-claims:**

**Reinforcement Learning:** After reading the methodologies, I didn't see RL play any role in this work. The only related part is borrowing the idea from Diffuser (Janneretal. 2022), to do the (sub) trajectory generation rather than autoregressive generation for efficiency. Such point and even claiming to achieve stable long rollouts with RL are invalid to me, given that Diffuser is a purely a generative method but to solve RL problems only. The critical components like **value function and reward function** never appear.


**Zero-shot:** While zero-shot forecasting is addressed conceptually, further clarification on how this aspect was validated experimentally is lacking.



**Writing:**

- Abstract: some sentences are naively extracted from the introduction but unclear after compression. "Nonetheless,Cohesionsupports...", unclear what's the advantage the authors refer to. Specifically, why iterations over subsequences are not allowed in the previous works. And direct abbreviation "NFEs".
- Section 2: The demonstration of $u_K$ and the relationship between $u_K$ and $u$ should be exposed clearer. E.g. change the title of "Coherent flow as conditioning prior" to "Conditional Diffusion Modeling", then put the demonstration of $u_K$ here first, and then introduce the coherent flow is the conditioning prior.

### Questions
1. **On Model Flexibility**: ROM is a type of method with limited expressiveness e.g. Koopman Operator, a linear approximation model. Would Cohesion be adaptable to domains where coherent flow cannot be efficiently approximated by ROM? 
2. **Baselines:** SFNO seems the only baseline. How about others like Markov Neural Operator (MNO)?
3. **Long-Term Stability**: The results are over long rollouts, how long is it and how hard is it to predict that?
4. **Ablation Study** has been lacking, such as W window size.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a diffusion-based approach for forecasting with dynamical systems that is able to generate the entire sequence in one conditional denoising pass. This is achieved by leveraging reconstruction guidance, where the conditioning information is a sequence of priors (one for each state of the final trajectory), generated by iteratively applying a (lightweight) reduced-order method (ROM) to the initial condition. The score network operates over subsequences, and temporal coherency is assured by applying temporal convolution with a small receptive window. The experiments are performed on two chaotic systems (Kolmogorov flow and Shallow Water), and the performance of the model as a probabilistic emulator is tested in terms of pixel-based metrics (RMSE, MAE), structure-based metrics (MS-SSIM), and physics-based metrics.

### Strengths
1. **Relevant topic.** The problem addressed in this paper (probabilistic emulation for PDEs) is an active area of research with important downstream applications, such as weather and climate modelling.
2. **Non-autoregressive approach.** The possibility of using a non-autoregressive sampling strategy from the diffusion model without compromising too much on accuracy is nice, and something of significance for the field of forecasting.
3. **Flexibie guidance with ROMs.** The use of reconstruction guidance is a very useful technique when the observation process changes over time, offering more flexibility as opposed to classifier-based approaches. Although the technique is not a contribution of this work, the paper is the first (as far as I am aware) to utilise as conditioning information a sequence of autoregressively-produced priors through a compute-efficient ROM. The experiment in which the authors condition on partially-observed fields of the ROM output highlights the flexibility of this technique and is relevant to real-life settings with partially-observed data.
5. **Wide range of metrics used for the experiments.**

### Weaknesses
1. **Unclear contributions/Lack of clear citations.** This approach shares striking similarities with the approach from Rozet et al. [1], but fails to properly reflect this throughout the main text. There should be a much more clear distinction between the contributions of this paper and what is taken from other works.
- The overall training and sampling from the score-based model relies heavily on the approach proposed by Rozet et al. [1], but this is not made clear in the paper. They also train the model on subsequences of length $W$ (justifying this approach from a Markov order perspective), and stitch these subsequences together at sampling time to generate arbitrary length trajectories in one go.
- The reconstruction guidance mechanism is exactly the same as the one proposed in Rozet et al. [1]. This is mentioned in the paper (L215), but it can be interpreted as if the authors propose a way to improve the numerical stability of the method, as opposed to using results from previous work.
- The similarity between the proposed framework and Rozet et al. [1] is reflected in the algorithms presented.
   - Algorithm 1 is the same as Algorithm 3 in Rozet et al. [1]
   - Algorithm 2 is the same as Algorithm 4 in Rozet et al. [1]
   - Algorithm 3 is the same as Algorithm 1 in Rozet et al. [1]
   - Algorithm 4 is the same as Algorithm 2 in Rozet et al. [1]. However, in the paper this is posed as a novel temporal convolution technique, rather than something already employed in Rozet et al. [1].

  I acknowledge that this paper adapts Rozet et al. [1]’s approach, making it suitable to other tasks (forecasting), as opposed to data assimilation. This is achieved by conditioning on those prior states, generated autoregressively through a ROM. This is a nice approach and equips Rozet’s method with the ability to perform forecasting, a task where their approach fails based on the observations from Shysheya et al. [2]. However, I do not think this is how the paper portrays the technique, and it is debatable whether this is enough of a contribution overall when considering the results (see below). At the very least, a clear paragraph on contributions should be included.
2. **Weak baseline for the empirical analysis.** Although the paper mentions that the SFNO approach [Bonev et al. [4]] is the state-of-the-art, I believe there are other probabilistic forecasting approaches that achieve stronger performance.
- Two works I have in mind are Lippe et al. [5] and Shysheya et al. [2], with the former being considered state-of-the-art. However, the main metric these works consider for forecasting is high correlation time, rather than the metrics used in this work. But based on the trajectories, they seem to maintain correlation with the ground truth for longer than Cohesion. It would be interesting to compute the high correlation time and compare it with some of these works, especially since the Kolmogorov dataset looks similar to the one in Shysheya et al. [2].
- As in Lippe et al. [5], I believe that another relevant (deterministic) baseline would be an MSE-trained UNet. In their experiments, it tends to achieve better results than FNO-based approaches.
3. **Lack of error bars in the results.** The performance plots lack error bars. Thus, it is hard to determine how significant the difference between methods is. This is especially the case between Cohesion (R=1) vs. Cohesion (R=T) (i.e. autoregressive vs. in one go), where having error bars is important to figure out whether the hit in performance by generating the entire trajectory in one go is significant.
4. **Copying from other papers without citing.** There are certain paragraphs/sections in the appendix which are directly taken from other works without specifying so. For example Appendix B.2. Structure-based metrics is the same as Appendix F.1.4. Multi-scale Structural Similarity Index Measure (MS-SSIM) in Nathaniel et al. [6], Appendix B.3 is very similar to Appendix F.2 in Nathaniel et al. [6]. It is ok to use the same definitions as in other works (in the end, the definitions of the metrics are what they are), but if the writing is so similar, I think you should at least cite the relevant work. 
   
   Could you please review these sections and either rephrase them, or make it clear that they are heavily based on Nathaniel et al. [6]?

**Minor**

5. **Typos.** The paper contains several typos, I won’t include them all but examples are L091-spatiotempral, L125 - deterministic priors, L235 - should be $\nabla_{\mathbf{u}_k}$ , etc.
6. **Small labels in figures.** See for example y label in Figures 5, 7, legend in Figure 8.
7. **Unclear figures.** I appreciate the attempt to create a visual representation of the framework in Figure 1, but I find the figure confusing, without mentioning the colour coding of the bubbles, why there are two trajectories in b), etc.
8. **Lack of x label in Figure 5**. I believe that is the timestep $T$, but that should be labelled.
9. **Ablation hyperparameter choices.** In appendix C.1 you detail how you chose the dropout rate $p$ and perturbation factor $f$ for the baselines. However, those correspond to the lowest values you experimented with and it’s unclear whether going even lower would give better results or not. You’d like to obtain a convex function of your hyperparameters (i.e. worse performance for lower and higher values of the hyperparameter).

### Questions
1. Could you please highlight the differences between this approach and Rozet et al. [1]? Is there anything that wasn’t captured in **W1**?
2. Could you also compute the high correlation time in the Kolmogorov (and SWE) experiment to compare with other results reported in the literature (i.e. Lippe et al. [5], Shysheya et al. [2])
3. While in the SWE experiment I understand the usefulness of the spherical embeddings used in SFNO, it is not clear to me why they would help in Kolmogorov, but I might have missed some relevant experimental setup detail that justifies it.
4. Could you provide error bars for your results?
5. If you provide comparisons to Lippe et al. [5] on the Kolmogorov flow experiment, could you also provide computational speed comparisons?
6. In L205 you assume a Gaussian observation process (as it is usually done). Would you be able to extend the framework to a non-Gaussian likelihood too?

### Soundness
2

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
4

### Summary
This paper presents Cohesion, a Coherence-Based Diffusion Model for Long-Range Dynamics Forecasting. The model leverages the concept of Reynolds Averaged Navier-Stokes (RANS) as conditioning priors to address two key issues in diffusion-based autoregressive models: (1) instability in long-term predictions, and (2) the computational inefficiency of generating priors. The authors utilise a Koopman-based reduced order model to efficiently generate these priors, thereby speeding up the forecasting process. Standard fluid dynamics principles and diffusion models are adapted to support this framework. Furthermore, cohesion acts as a refinement mechanism that aggregates temporal sequences from the model’s output, improving performance. The proposed approach is evaluated on two benchmark fluid systems. While the work is well-motivated and promising, there are critical issues with the presentation and formulation (detailed below).

### Strengths
The targeted problems are both interesting and critical for applying diffusion models to autoregressive forecasting. The main ideas and design choices presented in this paper are well-motivated and promising.

### Weaknesses
### Presentation 
1.	The authors claim that trajectory planning, a concept central to reinforcement learning (RL), is crucial to Cohesion. However, they do not adequately explain the operational or conceptual connections. Although they mention reframing forecasting as trajectory planning, no clear relationship to RL principles—beyond standard autoregressive or multi-step predictions—is evident. Without a specific RL objective formulation or a direct link to decision-making scenarios, the reference to RL seems forced and mislead readers.

2.	The paper's use of terminology is potentially confusing and could be considered an abuse of terms. Specifically, the names "Cohesion" and "coherent" are too similar, which creates ambiguity about their distinct roles. From personal understanding, the cohesion refers to the whole framework whereas “coherent” describes a predictable component of the dynamical system. While, as the figures 1,2,3 and experiment sections, the "cohesion " seems refer to the temporal-aggregation component. In addition, given the two words have specific meanings in the scientific community, the author should be careful and avoid potential confusions and abusing of terminology. 

3. Koopman Operator Introduction (Lines 253-256): The introduction of the Koopman operator is vague and contains some mathematical issues: (1) the text does not discuss that practical implementations use a finite-dimensional approximation. (2) The domain and mapping of the encoder and decoder are not clearly defined. (3) No clear definition for $\mathcal{G}$ and $\mathcal{G}_E(\mathcal{X})$. 

4. The numerical results are discussed too briefly, with only three lines dedicated to each experiment (Lines 378-380, 432-434). More in-depth discussion and analysis are needed to properly interpret the findings.

5. There is only one baseline methods. Additional baselines, particularly diffusion-based models, should be included for a more comprehensive comparison.

## Others
1.	The paper uses incorrect citation formatting. Citations should be enclosed in parentheses, e.g., "(xxx et al., year)," when they are not acting as the subject or object within sentences.
2.	Figures 5, 7, 8, and 9 lack axis descriptions 
3.	Several acronyms, such as Number of Function Evaluations (NFE), are introduced without definition at first mention. All abbreviations should be defined before initial use to ensure clarity.

### Questions
1. The Spherical Fourier Neural Operator (SFNO) is used as the only baseline despite being designed for spherical domains, whereas both demonstrated cases in the paper use standard square domains. This choice makes SFNO an unsuitable and potentially misleading baseline. It is unclear why the authors included this baseline, as it does not align with the problem setting. 

2. The use of Reynolds decomposition is indeed a central aspect of the paper, and this core idea is not clearly stated. While RANS typically deals with time-averaged components, the authors extend it to a time-dependent setting without discussion on this extension and theoretical foundation. It remains unclear how the authors achieved this extension and ensured its validity.

3. The authors claim improved inference efficiency through incorporating Koopman-based ROM; however, no comparison with other baselines is provided to support this claim.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes Cohesion, a model that combines a deterministic latent autoregressive component and a diffusion model for probabilistic dynamics forecasting. The high-level intuition of the model is as follows: first the current state is encoded to a compressed latent space. Then, one or more steps of a deterministic autoregressive model are applied, after which the predictions in the latent space are decoded back to the data space to get the initial prediction(s). In terms of the Reynold decomposition, the paper interprets this initial prediction as the coherent component of the flow. To resolve the fluctuating component, a diffusion model, which is conditioned on the predicted coherent component, is used to ‘stochastically refine’ the states. Cohesion is evaluated against the Spherical Fourier Neural Operator (SFNO) on Kolmogorov flow and Shallow Water Equation benchmarks, in terms of point wise-metrics like MSE, as well as structure-based and physics-based metrics.

### Strengths
**S1:** The model is evaluated in terms of spectral divergence, a measure of divergence between the energy distribution at different frequencies. Indeed, for chaotic systems that can have strongly diverging trajectories for even slightly different initial conditions, point-wise metrics become meaningless for long simulation horizons, and the statistical properties of the system should be investigated.

**S2:** The interpretation of the deep Koopman operator as predicting the coherent part of the flow and of the diffusion model as refining the fluctuating component is intuitive and provides a physics-inspired motivation for Cohesion.

**S3:** The method supports different sampling strategies, dubbed trajectory planning and autoregressive. Autoregressive shows higher quality results, but requires more computational effort, whereas trajectory planning is more computationally efficient due to denoising the entire trajectory at once. As such, the sampling strategies provide an intuitive way to trade computational budget for accuracy.

### Weaknesses
 **W1:** I found the presentation of the paper at some parts counterintuitive and confusing. In particular, Section 3 (the method section) starts with a quite extensive explanation of score-based generative models and zero-shot super resolution, while this concerns background material introduced in other works. I think the paper would benefit from merging this part with the text around Eq. 3 in the background section. This would make it easier for the reader to distinguish already established methods/algorithms and the novel aspects introduced in this paper.

**W2:** The experimental evaluation has two weak aspects:

*   The method is compared against a single baseline only, the SFNO. There are other popular probabilistic methods that utilize a predictor-refinement approach, for example those that are cited in Section 2, e.g. Lippe et al. 2024; Srivastava et al. (2023); Yu et al. (2023); Mardani et al. (2024). It would greatly improve the paper to compare against a selection of those methods, and explain how the key conceptual differences in your approach relative to those works lead to different results. In addition, the work of Bergamin et al. [1] is relevant since it also considers two sampling modes that are highly similar to trajectory planning and autoregressive forecasting as described in the paper.
*   The SFNO is not a suitable model for the Kolmogorov flow experiment, since the geometry in this experiment is not spherical. Do you have a specific reason to not compare to the regular FNO instead here (in addition to other baselines that would be good to add)?

**W3:** After reading the paper, it remains unclear to me what the key novel insights are relative to prior papers. Diffusion-based refinement techniques have already been proposed, as cited in Section 2 of this work. In addition, the zero-shot conditioning on noisy or partial observations in the context of PDEs has already been established in [2]. As I currently understand, the novelty here lies primarily in the architectural choice of using the encoder-operator-decoder module to get the initial prediction. In itself, this seems a conceptually small change relative to earlier frameworks that show that similar predictor-refinement approaches work well. If using this architecture in the prediction-refinement setting could lead to a substantial performance increase or otherwise interesting results, these could be novel insights, but this is not investigated in the paper. I think it would help to get your point across if you contrast your work against the most similar related papers more explicitly, and highlight the differences between them.

### Questions
**Q1:** Did you investigate whether the predicted conditioning prior actually aligns with the coherent part of the flow? I.e., does it predict some kind of average (or perhaps localized/moving average) behavior of the dynamics in space and/or time?

**Q2:** It is unclear to me how the metrics are calculated over multiple samples from the probabilistic models. Did you simply average the metrics over those samples, or take a best-of-K like approach? What is the effect of the stochastic sampling on the calculation of those metrics using your approach?

**Q3:** Please add labels on the horizontal axes of Figures 5 and 7.

**Q4:** How should Figure 6 be interpreted? Is the spherical geometry here somehow projected on the 2D image? Is there a reason why the signal is only present at the top half of the image?

**Q5:** Can you also provide plots of the spectral divergence over time, of Cohesion, the baseline methods, and coherent-only?

**Q6:** Please comment on W2 and W3.

### Soundness
2

### Presentation
2

### Contribution
1
