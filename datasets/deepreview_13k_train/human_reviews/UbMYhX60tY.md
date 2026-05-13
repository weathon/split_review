# RestoreGrad: Signal Restoration Using Conditional Denoising Diffusion Models with Jointly Learned Prior

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Denoising diffusion probabilistic models (DDPMs) estimate the data distribution by sequentially denoising samples drawn from a prior distribution, which is typically assumed to be the standard Gaussian for simplicity. Owing to their capabilities of generating high-fidelity samples, DDPMs can be utilized for signal restoration tasks in recovering a clean signal from its degraded observation(s), by conditioning the model on the degraded signal. The degraded signals are themselves contaminated versions of the clean signals; due to this correlation, they may encompass certain useful information about the target clean data distribution. However, naively adopting the standard Gaussian as the prior distribution in turn discards such information. In this paper, we propose to improve conditional DDPMs for signal restoration applications by leveraging a more informative prior that is jointly learned with the diffusion model. The proposed framework, called RestoreGrad, exploits the correlation between the degraded and clean signals to construct a better prior for restoration tasks. In contrast to existing DDPMs that just settle on using pre-defined or handcrafted priors, RestoreGrad learns the prior jointly with the diffusion model. To this end, we first derive a new objective function from a modified evidence lower bound (ELBO) of the data log-likelihood, to incorporate the prior learning process into conditional DDPMs. Then, we suggest a corresponding joint learning paradigm for optimizing the new ELBO. Notably, RestoreGrad requires minimum modifications to the diffusion model itself; thus, it can be flexibly implemented on top of various conditional DDPM-based signal restoration models. On speech and image restoration tasks, we show that RestoreGrad demonstrates faster convergence (5-10 times fewer training steps) to achieve on par or better perceptual quality of restored signals over existing DDPM baselines, along with improved robustness to using fewer sampling steps in inference time (2-2.5 times fewer steps), advocating the advantages of leveraging jointly learned prior for efficiency improvements in the diffusion process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes RestoreGrad, a framework that enhances signal restoration tasks using conditional denoising diffusion probabilistic models (DDPMs) with a jointly learned prior. The authors introduce a data-dependent prior distribution to improve the efficiency of DDPMs for recovering clean signals from degraded versions. RestoreGrad’s framework incorporates two additional networks, Prior Net and Posterior Net, to capture more relevant information for the reverse diffusion process.

### Strengths
1. Adaptive Prior Distribution: RestoreGrad learns a data-dependent prior rather than relying on a fixed Gaussian, potentially improving efficiency by tailoring the prior to the degraded signal. 

2. Joint Training with Minimal Modifications: The proposed approach requires only the addition of Prior and Posterior networks and a modified loss function, making it compatible with various DDPM architectures without significant changes. 

3. Efficiency in Training and Inference: RestoreGrad exhibits faster convergence and robustness to fewer sampling steps during inference, making it computationally efficient compared to baseline DDPMs.

### Weaknesses
1.  Lack of Novelty in Methodology: The method heavily builds on existing techniques, including the use of conditional DDPMs, adaptive priors (as seen in PriorGrad), and standard VAE and DDPM loss formulations. The Prior and Posterior networks adapt concepts from encoder-decoder architectures, similar to those in VAEs, rather than presenting new model designs.

2. Learned Prior Concept is not novel: The idea of using an adaptive, learned prior is inspired by existing models, like PriorGrad [1]. PriorGrad introduced the concept of data-dependent priors by using the degraded signal to inform the prior distribution, so RestoreGrad's approach of a learned prior based on the degraded input builds directly on this idea rather than introducing a fundamentally new approach 
3. Limited Novelty in Loss Function Design: The modified ELBO loss primarily integrates known VAE and DDPM loss terms without introducing novel loss structures or constraints tailored to signal restoration. 

4. No New Restoration-Specific Techniques: The Prior and Posterior networks are based on standard architectures (e.g., ResNet), and there is no exploration of restoration-specific methods, such as task-specific losses or architectures, that might further enhance the model's performance in different restoration tasks. 

5. Missing Computational Time Comparison: The paper lacks a clear and detailed computational time comparison with baseline models, which is critical for understanding the added cost of the Prior and Posterior Nets. Including this comparison in training and inference steps, along with performance metrics, would provide a clearer assessment of RestoreGrad's computational demands. 

6. Missing FID details in Tables 3, 4, and 7 - While the paper reports PSNR and SSIM metrics for assessing image quality, it omits the FID (Fréchet Inception Distance) metric, a widely used measure for evaluating the realism and distributional similarity of generated images. Including FID would give a more comprehensive understanding of RestoreGrad's performance in terms of perceptual quality. 

7. No Discussion on Trade-offs: The method introduces additional computational layers and complexity, yet there's little discussion on the trade-offs between quality improvement and increased model size or computation. 

### Questions
How the authors address the above weakness will be important for re-evaluating the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on signal restoration tasks and explores diffusion models with learned prior distributions capturing information about corrupted signal $y$. The pipeline the authors propose resembles VAE with the decoder represented by a conditional diffusion model and two encoders. Thus, at inference information about corrupted signal is used not only as conditioning to the network estimating diffusion noise, but also parameterizes the diffusion prior. Three networks are trained jointly, and the posterior encoder (skipped at inference) takes as input both clean signal $x_0$ and its corrputed verison $y$ and helps the prior encoder learn data-dependent task-specific prior. The novel loss function providing upper bound on negative log-likelihood for such combined VAE-diffusion model is proposed. Experiments on speech enhancement and image restoration tasks show the benefits of the proposed approach compared to conditional diffusion models with data-independent priors or the ones based on heuristics when applicable.

### Strengths
1. The authors introduced a novel model design combining ideas from VAE and diffusion modeling: the proposed model consists of two encoders parameterising prior distribution and a conditional diffusion based decoder.
2. A novel ELBO-like loss was proposed allowing for stable training of the mentioned model. The learned priors look quite reasonable. Thus, this approach can become a good alternative to hand-crafted diffusion priors in signal restoration tasks.
3. The experiments clearly demonstrate that diffusion models can benefit from the priors learned in the way the authors propose. The number of training steps necessary to achieve the same performance level decreases compared to data-independent or hand-crafted priors. Moreover, RestoreGrad achieves better performance at convergence.
4. The presentation quality is good (except for one point, see below); the text is clear and the paper is easy to follow.

Overall, I think that this is a good paper from the point of view of originality and clarity.

### Weaknesses
I can point out three main weaknesses.

1. As I far as I understand, the role of the posterior net is to better capture the correlation between $x_0$ and $y$ and to pass this knowledge to the prior net whose only input is the corrupted signal $y$ which is achieved by prior matching terms in Formula (9). But what happens if we get rid of this posterior encoder? It is possible to think of the following design: both at training and inference we have the same scheme, the prior net $\psi$ is conditioned only on $y$ and parameterizes diffusion prior, and the conditional diffusion $\theta$ restores a signal from this prior. This model wouldn't differ from the one the authors propose at inference. As for training loss, we obviously would not have prior matching terms anymore, and  $\Sigma_{post}$ would be replaced with $\Sigma_{prior}$ in the latent regularization and denoising matching terms. Such a design looks more simple (only one encoder instead of two) and also allows for learnable prior. I think that it could be a good baseline in the experimental section and it could help to support the idea that the posterior encoder is helpful since it is trained on both $y$ and $x_0$.

2. Non-diffusion baselines in the experimental section seem to be a bit outdated. E.g., in speech enhancement best methods have started to achieve > 3.0 PESQ on a common SE benchmark (Valentini dataset) since the year 2022 [1] outperforming CDiffuSE and RestoreGrad, and you just mention quite old methods with PESQ < 2.5. Although I don't have experience with image deblurring, I also suspect that the baselines you choose for this task are far from SOTA because the papers you refer to were published no later than in 2020.

3. What is $\sigma_t$ in Formula (9)? On the one hand, in the text of the paper $\sigma_t$ is mentioned in the context of common diffusion models (e.g. lines 153 or 189) and it suggests that the reverse process $p_{\theta}$ has fixed (unlearnable) covariance matrix $\Sigma_{\theta}=\sigma^2_t I$. In your setting it must mean something different, since the Algorithm 2 in the Appendix suggests that at each reverse diffusion step the noise you add has covariance matrix $\sigma^2_t\Sigma_{prior}$. Anyway, you should define the reverse process $p_{\theta}$ in your setting more clear, like in lines 188-190, especially since you use $\sigma_t$ that seems to have something to do with it in Proposition 1.

Also, I feel there's something wrong with the values of $\gamma_t$ in Proposition 1. In practice you set them all to $1$, so it is not a big issue, but still I'll mention my concerns. On the one hand, in lines 250-251 and 824-825 it is defined as $\beta_t^2/2\sigma_t^2\alpha_t(1-\bar{\alpha_t})$ for $t>1$. On the other hand, in the proof of Proposition 1 we have lines 858-859 implying a different expression $\gamma_{t}=\beta_t/2\alpha_t(1-\bar{\alpha}_{t-1})$.

### Questions
1. I have a question regarding the proof in lines 858-860: we see that the expectation of KL divergence between two Gaussians $q(x_{t-1}|x_t,x_0)$ and $p_\theta(x_{t-1}|x_t,y)$ contains only MSE term $\Vert\epsilon-\epsilon_{\theta}\Vert_{\Sigma^{-1}}^2$ and does not contain the log-determinant terms implying that it is KL divergence between two Gaussians with the same covariance matrices $\Sigma_A$ and $\Sigma_B$ (and $\log\frac{\Sigma_A}{\Sigma_B}$ cancels out).  In the assumptions in Proposition 1 you explicitly define how the forward diffusion paths look like. It's easy to see that for such forward diffusions the covariance of $q(x_{t-1}|x_t,x_0)$ is $\tilde{\beta}_{t}\Sigma$. So, is it true that reverse process has this covariance matrix?

2. One of latent regularization terms is multiplied by $\alpha_T$ which should be very little since the mean of the prior should be very close to zero. So, this term should have very little impact in theory. Why do you still use it at training? Does it have any impact on the training in practice?

3. Is the training process sensitive to the choice of loss weights $\lambda$ and $\eta$?

Also, I'd like to make a couple of additional remarks here. These are just the remarks to consider, not questions:

4. Typo in line 043: "DDPMs typically consistS..."

5. It's interesting to see what happens with your model if we consider continuous-time diffusion formalism as in [2]. Continuous-time diffusions also allow for likelihood estimation (but in a different way, without ELBO-like derivation). In my understanding, in this case prior matching terms in the total loss (9) would remain unchanged, denoising matching terms would look similar, but I'm not sure about Latent Regularization terms. Would they still be there in the loss function? If they would, what whould the exact expression look like, and how would these changes affect model training/final performance?

[2] Score-Based Generative Modeling through Stochastic Differential Equations, Song et al.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to improve the approach of using diffusion models conditioned on degraded data to solve restoration tasks in the audio and image domains. This method is inspired by PriorGrad, which uses a data-dependent adaptive prior, and attempts to extend this approach. Specifically, it simultaneously trains a Prior Net that estimates the parameters of the data-dependent prior. During training, it also simultaneously trains a Posterior Net that estimates the parameters of the data-dependent prior using the true data x_0 as input, along with the main score function. While PriorGrad handcrafts the prior, this method learns it simultaneously. The model is trained with a modified ELBO as the objective function, and experiments show that the proposed method converges 5 to 10 times faster in training compared to the baseline and achieves good performance with 2 to 2.5 times fewer steps.

### Strengths
- The experiments in Section 5 demonstrate that RestoreGrad shows notable improvements over baseline models in both speech and image restoration tasks. This method contributes significantly to the field as it has a certain level of generalizability, meaning it can be applied to many techniques with similar frameworks.
- The number of parameters in the Prior Net and Posterior Net is only about 2% of the main diffusion model's total parameters. This means that the additional computational/memory cost is kept to a minimum.
- This method includes hyperparameters \eta and \lambda that balance the weights in the loss function. However, the performance of the model doesn't seem to be very sensitive to the values of these parameters. This is a significant advantage for practitioners who will use this method in real-world applications.

### Weaknesses
 - While one of the strength of this method lies in its generalizability, the speech-related experiments only use CDiffSE (proposed in 2022) as a baseline. This alone might not be sufficient to fully demonstrate the validity of the method. It seems necessary to address its applicability to other techniques as well. Specifically, the current baseline may not represent the state-of-the-art in speech enhancement, and thus the reported improvements might not be as significant when compared to more recent methods. A more comprehensive evaluation against multiple baselines, including those with different architectures or training strategies, is needed to solidify the claim of generalizability and effectiveness in the speech domain.
- In the field of SE, there are clear improvements compared to the baseline. However, looking at Table 3, it appears that the improvements in the image processing domain are not as significant. The improvements in image restoration, while present, do not appear as substantial as those in speech enhancement. This raises questions about the method's effectiveness across different data modalities. The relatively smaller gains in image processing could indicate that the proposed approach might be more suitable for certain types of data or tasks, and further investigation is needed to understand the underlying reasons for this discrepancy. It is also important to consider whether the baseline model for image restoration is already very strong, making further improvements inherently more difficult.

### Questions
1. In addition to PriorGrad, I understand that SpecGrad is also related to this paper and shares similar objectives, albeit for different tasks. Could you explain the relationship with SpecGrad and discuss the advantages of this method?
2. While this method seems applicable to various techniques, what are its limitations? For instance, does it require the amplitude information of the signal to be significant? If so, is it difficult to apply to latent diffusion model-based methods? This is briefly mentioned in the conclusion, but could you elaborate on this a bit more?
3. Can you provide more insights into the values output by the Prior Net (or the Posterior Net output)? How does the characteristics of the output signal sequence differ from PriorGrad or SpecGrad? I felt it was outputting the amplitude information of the signal to be estimated in the restoration task. If so, is it possible to replace this prior net module with the output of a fixed SE module?
4. Comparing the SE results with the IR results, the improvements in SE seem more pronounced. Can you discuss this difference? Is it possible to discuss this in light of the characteristics of each type of data? (For example, is it important that speech has a zero mean?)

### Soundness
2

### Presentation
2

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
The paper proposes RestoreGrad, a method that aims to enhance conditional restoration DDPM models. The main idea is to add to the training 2 auxiliary networks that will train jointly with the original DDPM model and allow the DDPM to use at inference non-gaussian prior that is dependent on the degraded input. RestoreGrad is tested on image restoration and speech enhancement and shows faster convergence at training as well as robustness to inference with fewer steps. The quality of the results is either on-par or better for the reported metrics.

### Strengths
-	RestoreGrad converges faster with the same performances relative to the baselines, and the auxiliary nets do not add many parameters (only 2%).
-	The experiments contain comparisons against many SotA algorithms.
-	The paper is clear and well written. 
-	The robustness to sampling using fewer timesteps is important and works well.

### Weaknesses
 -   **Novelty:** A core claim of novelty is the idea of using a learned, non-gaussian prior. However, this idea is not new. For example, PriorGrad already discussed in the past this exact same idea (however not achieving better performances). The authors mention this and previous non-learened non-gaussian priors as different conceptually or technically (L88). However, Grad-TTS also used a learned prior, and successfully. 
This limits the novelty contribution to only adaptation to the image domain.
-   **Evaluations:** 
  -   The paper lacks subjective evaluations via user studies.
  -   In L1057 the authors claim higher PSNR yields better perceptual image quality, which is known to not be the case as it is a distortion metric only (See e.g., Blau & Michaeli 2018 or Freirich et al.2021).
  -   The important LPIPS and FID metrics are only present in the appendix for a single task (RainDropDiff). The authors should move them to the main part of the manuscript and add these metrics for the rest of the domains and models (and specifically in the tables and not only as graphs).
  -   There are no links to qualitative samples for the speech enhancement task.
-   **Minor**: 
  -   In the abstract please clarify that you improve conditional DDPM for signal restoration (and not just general conditional models).
  -   L463 missing the device & train time (the latter is mentioned in later paragraph, but it's a bit unorganized).

### Questions
-	Will code be published on acceptance?
-	I would suggest maybe a more perceptual speech enhancement metric such as automatic speech recognition before and after the degradations, e.g. using whisper (see Benita et al. 2024).

### Soundness
2

### Presentation
3

### Contribution
2
