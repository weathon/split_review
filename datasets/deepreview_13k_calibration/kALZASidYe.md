# Towards Enhanced Controllability of Diffusion Models

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
As Diffusion Models have shown remarkable capabilities in generating images, the controllability of Diffusion Models has received much attention. However, there is still room for improvement of controllability in some aspects, such as feature disentanglement of Diffusion Models for extended editability and composing multiple conditions naturally. In this paper, we present three methods that can be used in either training or sampling to enhance the controllability of Diffusion Models. Concisely, we train Diffusion Models conditioned on two latent codes, a spatial content mask, and a flattened style embedding. We rely on the inductive bias of the progressive denoising process of Diffusion Models to encode pose/layout information in the spatial structure mask and semantic/style information in the style code. We also propose two generic sampling techniques for improving controllability. First, we extend Composable Diffusion Models to allow for some dependence between conditional inputs, to improve the quality of generations while also providing control over the amount of guidance from each condition and their joint distribution. Second, we propose timestep-dependent weight scheduling for content and style latents to further improve the translations. We observe better controllability compared to existing methods and show that with our proposed methods, Diffusion Models can be used for effective image manipulation and image translation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an improved strategy for generating conditional samples in the setting where the conditions and their composition is semantically complex.

### Strengths
- The proposed method appears to improve empirically on CDM on several displayed generation examples -- namely, when there is unclear composition of two disparate (and more rarely composed) conditions, such as an octopus next to a pyramid, and a bear with a car.

- The authors evaluate the proposed method on a selection of benchmarks, and appear to obtain improved performance over existing baselines.

### Weaknesses
 - Poor formatting. Why are some equations not numbered in the main text? Some variables are never defined in the un-numbered equations. (See questions.)

- Unclear exposition. The concepts and notation in Sections 3.1 and 3.3 are difficult to reconcile. What is $\epsilon(x_t, t, c_1, c_2)$? Are $z_s$ and $z_c$ just the conditions $c_1$ and $c_2$, respectively? How is this a generalization of CDM?

- Limited novelty. It appears to me that the main contribution involves the addition of joint conditions, rather than simple independent conditions (CDM) in Eq. 3. This is overall a rather simple addition from CDM. Proposition 3.2 is not very interesting, as it appears to simply state that GCDM generalized CDM (which is known) and CDM generalized CFG (which is known).

- Lack of scalability. In the current formulation, it is not clear to me how the proposed method will scale well with increasing conditions. The number of joint conditions required in Eq. 3 seems to grow combinatorially with the number of conditions. For example, with 4 conditions, the model would need to compute $\epsilon(x_t, t, c_1, c_2)$, $\epsilon(x_t, t, c_1, c_3)$, $\epsilon(x_t, t, c_1, c_4)$, $\epsilon(x_t, t, c_2, c_3)$, $\epsilon(x_t, t, c_2, c_4)$, $\epsilon(x_t, t, c_3, c_4)$ and $\epsilon(x_t, t, c_1, c_2, c_3, c_4)$ in addition to the single condition terms. This quickly becomes intractable.

- Lack of ablation study. The authors propose several orthogonal improvements (e.g. timestep scheduling and an adaptive group normalization, a.k.a. AdaGN, layer). How much do these aspects contribute to the performance of the model?

- Significant increase in hyperparameters. It appears that at least 9 new hyperparameters are introduced in this conditioning method ($a$, $b$, $\alpha$, $\lambda$, $\beta_i$, $t_1$, $t_2$, $t_3$). It is not clear to me how to choose these hyperparameters, and to what extent the observed empirical improvements can be attributed to hand-tuning of these hyperparameters.

### Questions
What is $\epsilon_t$ in the un-numbered (first) equation in Section 3.1?

What is the intuition behind the basic form $(1 + t_1\phi(z_c))(1 + \zeta(z_s))((1 + t_2)h + t_3)$? Why is it basic?

How are the various new hyperparameters $a$, $b$, $\alpha$, $\lambda$, $\beta_i$, $t_1$, $t_2$, $t_3$ chosen? How robust are the results to perturbations in these hyperparameters?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Generative models have become increasingly popular in recent years, but there is still a need to improve their controllability. Diffusion models are a promising class of generative models, but existing methods for disentangling latent spaces in diffusion models do not effectively learn multiple controllable latent spaces. This paper proposes a novel framework for enhancing the controllability of diffusion models. The framework introduces a Content Encoder and a Style Encoder to better manage the structure and style aspects of an image during training. Additionally, it presents Generalized Composable Diffusion Models (GCDM) to allow for more natural compositions during inference when conditional inputs are not independent.  The paper also utilizes the inductive bias of diffusion models to improve results by applying a controllable timestep-dependent weight schedule to blend content and style codes during generation.

### Strengths
1. Enhanced Controllability: The proposed framework introduces a novel approach to enhance controllability in generative models, specifically Diffusion Models, by effectively learning two latent spaces—content and style. This level of control is crucial for a wide range of practical applications in image synthesis and beyond.

2. Disentanglement of Latent Spaces: The framework addresses a gap in existing research by effectively disentangling latent spaces. The introduction of separate Content and Style Encoders helps in managing the structural and stylistic aspects of an image more precisely.

### Weaknesses
1. Complexity of Implementation: The introduction of multiple encoders and the management of separate latent spaces could increase the complexity of the model's architecture, making it more challenging to implement and fine-tune.

2. Overlapping latent spaces: Are the latent spaces independent of each other?  How can this be verified?

3. Justification of success can be strengthened: Are there specific domains or types of images where the proposed method performs particularly well or poorly? What are the limitations in terms of content and style diversity?

4. The formulation of the style coder is based on human heuristic, instead of data driven.  How can you tell what styles can be controlled?

### Questions
1. Could the authors provide quantitative metrics to compare the performance of their proposed GCDM with existing models such as CDM and others?
2. Is there a possibility to extend the framework to more than two latent spaces, and if so, how would this affect the model's complexity and performance?
3. How does the proposed timestep-dependent weight schedule compare with existing methods in terms of computational efficiency and quality of generated images?
4. The formulation of the style coder is based on human heuristic, instead of data driven.  How can you tell what styles can be controlled?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to enhance the controllability of diffusion models by adding a content encoder and a style encoder in the diffusion models. Using the same design philosophy as Swapping Autoencoders, the content encoder learns a spatial layout mask while the style encoder outputs the flattened semantic codes. By doing so, the method enables deep image manipulation by mixing the style codes and the content codes. Furthermore, the paper proposes a timestep-dependent weighting schedule for content and style latents to get better results. Experiments are mostly done on FFHQ datasets as well as LSUN-Church and AFHQ.

### Strengths
1. The method is simple and easy to understand.
2. The controllability of diffusion models is an important problem and worth investigating.

### Weaknesses
1. The method adds two additional encoders and needs to be trained from scratch which makes it hard for larger text-to-image diffusion models which require a large amount of time training.
2. Swapping autoencoders is a strong baseline here and it does not seem the proposed model shows significant advantages over this previous method from Figure 4. For example, the results from SAE seem more plausible than the different results given by the proposed method.
3. From Figure 15 on the ablation of different weighting schedules, the difference seems little between the sigmoid and the linear ones.

### Questions
For the comparison with DiffAE+MagicMix, it seems that the image quality is really bad, does the author try different parameters over this? The paper states that the model takes $x_600$ as input but no other results are presented here.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work addresses the challenge of improving the controllability of Diffusion Models, which have shown significant capabilities in image generation. The authors introduce three methods to enhance the controllability of these models during both training and sampling phases. They train Diffusion Models conditioned on two latent codes: a spatial content mask and a flattened style embedding. The paper also introduces two sampling techniques to improve controllability and demonstrates that their methods allow for effective image manipulation and translation.

### Strengths
- The paper addresses a significant gap in the controllability of Diffusion Models, especially in feature disentanglement and composing multiple conditions.
- The method achieves a good performance on FFHQ, AFHQ, LSUN datasets.

### Weaknesses
 - So called style condition looks more like another object feature condition. The style image thus is quite close to the content image on the manifold. 
- All examples of content and style pairs are quite similar, i.e. both faces, cat and dog, cat and tiger. This undermines the effectiveness of this method on more general cases.

### Questions
- Can you explain how do you apply your method to SD text-to-image generation in detail? 
- Have you tried using another style image that is more different in style instead of just content? It seems more like a object feature transfer case in your experiments. Can you try an obviously different style image, such as a painting etc?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
