# Closed-Form Diffusion Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Score-based generative models (SGMs) sample from a target distribution by iteratively transforming noise using the score function of the perturbed target. For any finite training set, this score function can be evaluated in closed form, but the resulting SGM memorizes its training data and does not generate novel samples. In practice, one approximates the score by training a neural network via score-matching. The error in this approximation promotes generalization, but neural SGMs are costly to train and sample, and the effective regularization this error provides is not well-understood theoretically. In this work, we instead explicitly smooth the closed-form score to obtain an SGM that generates novel samples without training. We analyze our model and propose an efficient nearest-neighbor-based estimator of its score function. Using this estimator, our method
achieves sampling times competitive with neural SGMs while running on consumer-grade CPUs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new variant of diffusion models based on the fact that the score function can be equivalently written as the expectation over score functions of conditional distributions. This expectation can be written in closed-form as a weighted sum over all training points, thus the "closed-form" diffusion models. The paper then proposes to smooth the closed-form scores by integrating it over small noise perturbation of the inputs, akin to the denoising score matching approach. Due to the closed-form expression, sampling can be implemented without a parametric approximation to the score function. Because each evaluation of the score requires going through all training examples, a nearest-neighbor estimator is used to reduce the computation cost.

### Strengths
* The paper is clear and pleasant to read. 
* The experimental study is carefully designed and investigated most questions that I could think of about the closed-form model.
* It's interesting that the proposed method can fill in the gaps between the sparse training samples in the 3D point cloud experiment (although it's unclear to me why the method was able to do so--see below).

### Weaknesses
 * The proposed method is not well-positioned in literature. It's worth pointing out that the key idea of representing the marginal score as the expectation of scores of distributions conditioned on inputs is actually quite well-known. It has been used, for example, to develop the original denoising score matching objective [1]. It is also used in the literature as "score-interpolation" [2]. I just named a few but I would recommend the authors to do a thorough literature review as I believe this property is used in many more works. Specifically, the paper fails to acknowledge the extensive literature on kernel methods and their connection to score matching, where similar closed-form expressions for scores arise naturally. The use of Gaussian kernels, in particular, is a direct link that should be discussed. The paper also doesn't adequately address how the proposed method relates to other non-parametric approaches for density estimation.

* The definition of the notation \hat{c}_k (baycenters) is missing. 

* The exponential dependence of the sampling error on T is concerning. Although empirical evidence is provided to justify that this error bound is pessimistic, it also renders the bound unnecessary. Meanwhile, it's unclear if the conclusion that under sigma < 0.4, a large starting T is harmless will generalize to other datasets. The paper should provide a more rigorous analysis of the error behavior, especially regarding the interplay between T and sigma, and explain why the empirical observations deviate from the theoretical bound. Furthermore, the lack of a clear explanation of how the choice of T affects the sampling process is a significant weakness.

* The 3D point cloud experiment is interesting but I don't understand why the proposed method fills the gap there. Could the authors elaborate on this? It is unclear if the method is actually learning the underlying manifold or simply interpolating between the training points. The paper needs to provide more insight into the mechanism behind this behavior.

* The practical utility of the proposed closed-form models is also unclear. Given that the model can only sample from baycenters of data point tuples, is there a clear case where we would prefer such a model over a trained score model? The paper needs to clearly articulate the advantages of this approach, especially in comparison to existing methods. The limitations of sampling only barycenters should be discussed in more detail, and the paper should explore potential ways to overcome this limitation.

* This is minor, but the readability of section 3 can be greatly improved if not going to the notation convention used by rectified flow, as the proposed method can be described using the standard diffusion model formulation (where the time is reversed and stochastic transition is used). The current presentation makes it harder to understand the connection to standard diffusion models.

### Questions
Please see questions above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers the score-based generative models (SGMs) - precisely, their ability to generating novel data and prevent from the memorization the training data. The usual solution is approximating the score training a neural network via score-matching. Despite promoting the generalization, the neural SGMs are costly to train and sample. Instead, the authors propose to explicitly smooth the closed-form score to obtain an SGM that generates novel samples without training. In this work, they also formulate an efficient k-NN based estimator of their score function.

### Strengths
The paper has a few significant strengths overall, which I will outline below:
1. The proposed method is easy, but elegant. 
2. The significant advantage of the proposed method is the training and sampling times and the possibility to use the standard CPU.
3. The authors tested the method in different settings.
4. Overall, the flow of the manuscript is well-organized.

### Weaknesses
However, despite the strengths, the paper has a few major and minor weaknesses:
1. The method is compared only on a small resolution datasets - the largest resolution have the Butterflies dataset, which still is only 128x128 (and has small number of examples). I’m not sure if this model will be working well on a larger resolutions, e.g. at least 256x256 ImageNet. Maybe the comparable results to the DDPM is only a matter of not so large resolutions?
2. The authors compared their method only against the DDPM. Could you compare with different diffusion models, which might generalize better?
3. The presented results are not sufficient and unclear. They are unclear, because even in the Table 1, the proposed method is better on one dataset, whereas being worse on another. It would be helpful to include also other metrics than LPIPS (e.g., FID, SSIM).
4.  In the whole paper, the Figures and Tables are too small. It is very hard to see what is in the Table and if the proposed method is better than DDPM. The presented samples are also way too small - based on this presentation I just cannot compare the proposed model against DDPM.

### Questions
I would like to see especially the following experiments and improvements regarding specifically to the Weaknesses section:
1. Please if you could include comparison on datasets having higher resolutions, like ImageNet.
2. The comparison against others diffusion models (e.g., DDIM) is needed.
3. I would like to see results in other metrics also (like FID or SSIM).
4. Please if you be able to enlarge all the Figures and all the Tables.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers smoothed closed-form diffusion models. In particular, the authors study the properties of smoothed score function and propose a new sampling algorithm. Numerical experiments are organized to evaluate the performance of this new model.

### Strengths
1. The authors propose a new diffusion model with closed-form score function.
2. The paper studies analytic properties of smoothed diffusion models, including support of output distribution and the approximation error.
3. Comprehensive numerical experiments are organized. The smoothed diffusion model is compatible with neural network-based diffusion models such as DDPM.
4. The model is training-free. Sampling can be implemented even in CPUs.

### Weaknesses
1. If my understanding is correct, the motivation is to have a diffusion model with good generalization capacity. Although the smooth diffusion model performs as well as DDPM, it is still unclear how it is connected to the generalization of diffusion models. 
2. In terms of modeling, the only novelty seems to be an additional smooth term added to $k$. Could you point out your contribution more clearly?
3. The writing looks good but can still be improved.

### Questions
I have some minor questions:

1. Why do we have a closed-form score function as in Section 3? Could you give some references or provide derivations in the appendix?
2. Seemingly, you only provide a comparison to DDPM in terms of training time and LPIPS. Could you provide more comprehensive experiments compared to other benchmarks and additional metrics?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces closed-form diffusion models by smoothing the closed-form score function with finite training data. By explicitly introducing error through this smoothing process, the resulting diffusion models, referred to as $\\sigma$-CFDM, exhibit generalization capabilities. The paper also provides proof that $\\sigma$-CFDM's support contains the exact barycenters of $M$-tuples from the training points. To expedite the sampling process, the authors propose techniques such as initializing with unsmoothed CFDM samples at $T>0$ and utilizing an approximate nearest neighbor search method. Notably, experiments illustrate that $\\sigma$-CFDM can generate novel samples without the need for a training stage.

### Strengths
Originality: Although Equation (1,2) has been referenced in several existing works, the extension of this concept to closed-form diffusion models with generalization capabilities is an intriguing innovation. The deliberate introduction of error through a smoothing process not only distinguishes this work but also explicitly defines the inductive bias, a valuable contribution in the current deep learning-dominated era.

Quality: The work is well-motivated and logically compact. The presented propositions and the theorem are solid.

Clarity: The paper is generally well-written and easy to follow.

Significance: The paper offers a fresh perspective on the study of diffusion models. However, some concerns about its overall significance are detailed in the following section.

### Weaknesses
My primary concern about this paper revolves around the apparent simplicity of the generalization achieved by $\sigma$-CFDM. Indeed, the generalization abilities of generative models trained on finite datasets inherently arise from their deviation from a precise fit to the empirical distribution. Introducing explicit error to the empirical distribution, as presented in this paper, seem more elegant and interpretable compared to conventional deep learning methods. However, it's important to note that the proposed smoothing method essentially makes an assumption on the underlying data distribution (or the inductive biases). It posits that the barycenters of empirical data points also reside within the supports of the true data distribution. This assumption shares similarities with the mixing of training data points. An alternative approach would be to directly sample the mixup, rendering the diffusion process unnecessary. For instance, a generative model could be defined by initially sampling $M$ training data points and then returning their barycenter (with probabilities related to the variance) as the generated sample. Alternatively, one could employ a weighted average by further sampling weighting parameters from the $(M-1)$-simplex. It would be valuable to provide a comparative analysis with these alternative methods to offer a more comprehensive evaluation (e.g. FID score and visualization). As the authors mention in Section 6.4, for image data, the barycenters may not be well-registered, and an auto-encoder is adopted, such a comparison should also be conducted in the latent space for real image generation.

### Questions
- How does $M$ affect the behavior of $\\sigma$-CFDM?
- Can this method be extended to conditional generation?

Please also see my questions in the Weaknesses section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
