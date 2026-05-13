# The Emergence of Reproducibility and Consistency in Diffusion Models

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
Recently, diffusion models have emerged as powerful deep generative models, showcasing cutting-edge performance across various applications such as image generation, solving inverse problems, and text-to-image synthesis. These models generate new data (e.g., images) by transforming random noise inputs through a reverse diffusion process.
In this work, we uncover a distinct and prevalent phenomenon within diffusion models in contrast to most other generative models, which we refer to as ``consistent model reproducibility''. 
To elaborate, our extensive experiments have consistently shown that when starting with the same initial noise input and sampling with a deterministic solver, diffusion models tend to produce nearly identical output content. This consistency holds true regardless of the choices of model architectures and training procedures.
Additionally, our research has unveiled that this exceptional model reproducibility manifests in two distinct training regimes: (i) "memorization regime,'' characterized by a significantly overparameterized model which attains reproducibility mainly by memorizing the training data; (ii) "generalization regime,'' in which the model is trained on an extensive dataset, and its reproducibility emerges with the model's generalization capabilities. Our analysis provides theoretical justification for the model reproducibility in "memorization regime''.
Moreover, our research reveals that this valuable property generalizes to many variants of diffusion models, including conditional diffusion models, diffusion models for solving inverse problems, and fine-tuned diffusion models.
A deeper understanding of this phenomenon has the potential to yield more interpretable and controlable data generative processes based on diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors observe that different trained diffusion models map to almost identical output images when the deterministic ODE sampling starts from the same initial noise. They validate this experiment with different models and they measure that the behavior is consistent for models that are trained separately, with different architectures, different samplers, and even different perturbation kernels. The authors provide a theoretical justification for this phenomenon in a toy setting (with infinite model capacity and a target distribution of many diracs).

### Strengths
- The paper is easy to follow. 
- The authors conduct numerous experiments to verify their findings.
- Understanding the behavior of deterministic samplers is an interesting and timely research topic.

### Weaknesses
I believe the main finding of this paper is already known. The Probability Flow ODE depends on the functions $f$, $g$, and the score. For given functions $f$, $g$, the score function is unique! There is a unique score function because there is a unique likelihood function induced by corrupting the data distribution. All diffusion models are trained to estimate the exact same score function — even if they have different architectures and are trained separately — the target is always the same. Hence, if the diffusion models are trained perfectly, then it is actually expected that they will all map the same noise to the same output. The small deviations in the shown images in Figure 1, just indicate that there are some learning errors. The finding should stay the same even if we use different samplers, as long as the samplers arrive with guarantees that given enough steps and access to the score they will sample from the right distribution. The only surprising fact to me in this paper is the claim that models trained with different corruption processes will have this property. This doesn’t make much sense to me because for VE SDE and VP SDE for example, even the terminal distribution is different, so how do we even start from the same noise? What distribution does this noise follow?

### Questions
There is a chance that I am missing something fundamental about this paper. I would really like the authors to clarify, if possible, why their main finding is different compared to prior work.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper takes a deep dive into the identifiability of the diffusion model latent space induced by deterministic sampling procedures. In particular, it starts by showcasing the phenomenon that if initialized with the same noisy images and using a deterministic sampler, well-trained diffusion models with widely ranging architectures, training and sampling procedures all produce highly similar images on CIFAR-10. The paper analyses this further and uncovers two distinct regimes where this happens: The overparametrized, ‘memorization regime’, where only a small part of the CIFAR-10 data set is used, and the ‘generalization regime’, where the full CIFAR-10 data set is used. Importantly, there is a gap in between these extremes where the different models do not agree. The effect is measured quantitatively using metrics for comparing image pairs, confirming the result. The mapping from noise to images is visualized and shown again to be similar among different models, as well as smooth. A theoretical study in the ‘memorization’ regime is provided, and reproducibility is demonstrated in conditional generation, inverse problems and fine-tuned models as well.

### Strengths
+ The experiments are thorough and demonstrate the phenomenon clearly, and the phenomenon itself is quite striking.
+ The research is well-motivated
+ Although preliminary results on the phenomenon were reported in Song et al (2021), the paper uncovers new effects:
	- The generation is consistent across vastly different architectures, training and sampling procedures
	- The phenomenon occurs in two distinct phases, the ‘memorization’ and ‘generalization’ and regimes, with a clear transition in between where it doesn’t occur.
	- The model reproducibility holds across different types of conditional diffusion models and fine-tuned models as well
+ Potentially the paper opens up more avenues for theoretical work towards understanding diffusion models and how diffusion models generalize, in particular.

References:
Song et al., Score-Based Generative Modeling through Stochastic Differential Equations, 2021, ICLR

### Weaknesses
 - The present study is mainly on CIFAR-10, and it would be interesting to see how do the results transfer to larger data sets, like ImageNet. Especially when moving to the very large data sets used for text-conditional generation, it doesn't seem obvious that similar results would hold. It would be interesting to see how far can this be extended.


### Questions
- When studying the encoding from the noise hyperplane to the image manifold, would it be more appropriate to interpolate the noises using spherical linear interpolation instead of direct linear interpolation? From what I understand, the issue with linear interpolation is that because two randomly sampled high-dimensional noise vectors are, with a high probability, orthogonal to each other, the magnitude of a linearly interpolated vector decreases halfway by a factor of sqrt(2).

Overall, I think that the paper demonstrates and highlights the claimed effects very clearly, and that in addition to the new and more detailed characterization of the phenomenon make the paper worthy of publishing.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Diffusion models have demonstrated a strong ability to generate high-quality images. This paper presents a novel discovery referred to as "consistent model reproducibility": regardless of different training configurations, model architectures, and sampling strategies, diffusion models produce nearly identical output content given the same initial noise. The authors theoretically justify the above claim. Besides, they divide model reproducibility manifests in two regimes: memorization regime and generalization regime based on whether the model capacity matches the dataset size. This work provides insights for interpretable and controllable data generation based on diffusion models

### Strengths
- The authors both theoretically and empirically show that the same initial noise input results in nearly identical output regardless of the model architecture and training procedure, which is impressive.
- The study is thorough. It covers both unconditional and conditional diffusion models, and considers different sampling strategies, training configurations and model architectures.
- The writing is clear and easy to follow.

### Weaknesses
 - Lack of discussion about text-to-image diffusion models.
- [minor] "controlable" in the abstract should be controllable.
- Why are the reproducibility scores between transformer-based models and unet-based models low as shown in Figure 7(b)? According to Theorem 1, the reproducibility scores should be high. Could you please provide more explanation?
- Yet the explanation for the low scores between diffusion models with different architectures is not convincing. According to theorem 1, the score function also follows the pattern even given out-of-domain data.
- Also, I agree with Reviewer LTJ7 that Theorem 1 might be rather trivial. The model in Theorem 1 is too simple and too ideal: Theorem 1 only considers the optimal score function, which is impossible to obtain in practical training. The result in Eq.(2), which can be derived by computing the minimizer of a quadratic function, is trivial due to the simple modeling.

### Questions
Why are the reproducibility scores between transformer-based models and unet-based models low as shown in Figure 7(b)? According to Theorem 1, the reproducibility scores should be high. Could you please provide more explanation?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper found that diffusion models for image and text-to-image generation uniquely produce almost identical results when given the same starting conditions, regardless of their design or training. This happens in two ways: either by memorizing training data or by learning broadly from large datasets. This consistent output trait, present in various diffusion model types, could make these models more understandable and controllable.

### Strengths
It is quite interesting to investigate the memorization and generalization of diffusion models, which help us to understand current generative model better.

### Weaknesses
Although the author discovered an interesting phenomenon and used rich theories and experiments as supplementary explanations. But it seems that there is no further improvement in the training of the current diffusion model.

The experiments are conducted on small datasets (CIFAR)? It is not clear the performance on larger datasets.

### Questions
How does the ODE solver and the NFE influence the image? (Few NFE will brings corrupted image)

Have the authors investigated larger datasets, such as CoCo, ImageNet?

How can we get a better training strategy from the current conclusion?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
