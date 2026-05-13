# Understanding Diffusion-based Representation Learning via Low-Dimensional Modeling

- Decision: Reject
- Scores: 5, 1, 8, 3

## Abstract
This work addresses the critical question of why and when diffusion models, despite their generative design, are capable of learning high-quality representations in a self-supervised manner. We hypothesize that diffusion models excel in representation learning due to their ability to learn the low-dimensional distributions of image datasets via optimizing a noise-controlled denoising objective. Our empirical results support this hypothesis, indicating that variations in the representation learning performance of diffusion models across noise levels are closely linked to the quality of the corresponding posterior estimation. Grounded on this observation, we offer theoretical insights into the unimodal representation dynamics of diffusion models as noise scales vary, demonstrating how they effectively learn meaningful representations through the denoising process. We also highlight the impact of the inherent parameter-sharing mechanism in diffusion models, which accounts for their advantages over traditional denoising auto-encoders in representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a low-rank decomposition theory of diffusion representation learning, which supports the empirical result that using a medium denoise level t achieve best classification performance.

### Strengths
1. Theorem 1 provides direct connection from the noise level sigma_t to the empirical results. 

2. The paper is well-written and easy to read.

### Weaknesses
1. The results are not rigorous.  theorem 1 is obtained by many approximations: 1)  $x_\theta(x_t, t)$ defined in proposition1 is replaced with $x_\theta(x_0, t)$ with some informal arguments. The gap between these two terms cannot be easily ignored. Specifically, the denoising process is a Markov chain, and the approximation ignores the accumulated error from previous steps. It's not clear how this approximation affects the final result. 2) eq 9 replaces eq 6 for simplicity. It should be put in theorem instead. The connection between the two equations is not clearly established, and the simplification may not hold in all cases. The authors should provide a more rigorous justification for this replacement, or at least state it as an assumption.

2. The empirical results. Since authors do not provide new empirical method, I am wondering why no larger experiments are conducted, e.g., ImageNet with some pretrained diffusion models. Evidence on Cifar are not strong enough to support all arguments in this paper. The current experiments are limited to relatively small datasets and simple architectures. The claims about the general applicability of the theory would be much stronger with experiments on more complex datasets and models.

3. The K-space. Do you use K=number_of_classes? Is it too strong assumption? Human classify objects into different classes, but it would be overly strong to assume that K classes subspaces are independent? The assumption of independent subspaces is a strong simplification. Real-world data often exhibits complex dependencies between classes, and this assumption may not hold in practice. The authors should discuss the limitations of this assumption and its potential impact on the results.

### Questions
as above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper makes an attempt to explain *representation quality* in a diffusion model using a simple model of Gaussian data over low dimensional subspaces. They observe a uni-modal trend in *representation quality* as a function of noise level, which indicates that the best representation of the clean input image can be obtained at a certain noise level. It seems that the representation quality is empirically measured by classification accuracy over test data using the internal representation at the bottleneck of a UNet. 

To explain this observation, they 1) assume image data lies on a union of manifolds, where each manifold corresponds to a class. 2) They approximate manifolds with linear sub-spaces. 3) They assume each subspace of a class contains features that are relevant for high quality representation ($U_k$) and anything that is not relevant is noise and lies on orthogonal complement ($U^T_k$). Moreover, the assumption is that data is Gaussian distributed over the image subspaces. 4) They define Class Signal to Noise Ratio to measure the goodness of representation using denoised images (i.e. posterior mean estimate) and the class sub-spaces. 5) They show both of their measures for quality of representation (i.e. classification test accuracy from bottleneck and CSNR) have a uni-modal trend as a function of noise level. 6) Due to the theoretical analysis, for the low rank Gaussian model, the highest representation quality is a function of the ratio of added Gaussian noise level and the *noise* level of portion of image that lies in ($U_k^T$).

### Strengths
1. Important and interesting topic: The question of representation learning through diffusion models is interesting and worthwhile for more investigation. 
2. This paper could potentially be interesting with major improvement in writing and clarity. Overall, the paper needs more refinement to be ready for publishing.

### Weaknesses
1. The paper is very poorly written. It's hard to follow the logic and it's not clear what are the contributions. It's also not clear what parts are borrowed from other works and what parts are novel. For example, a good portion of the assumptions, modeling, and toy experiment setup are borrowed from [1] which is not obvious from the text.
2. The key concept are not explained clearly. For example, what do you mean by "representation quality"? It's been referred to throughout the text and figures without any definition. How do you connect your two measures of quality to each other? Overall, many of the key concept in the text are never defined! How can one assess the results without knowing what the experiments are trying to measure?!
3. The linearity assumption (approximating each class nonlinear manifold with a subspace) is obviously too simplistic for real data. As a result the theoretical result, expressed in theorem 1 does not extend beyond the simple low rank Gaussian model.
4. Even within the union of low-rank Gaussian model, a major drawback is the arbitrary split of $U_k $ and $U_k^T$. How does one decide what it relevant to representation and what is *noise* or irrelevant perturbations? To answer this question and correctly decide where the image subspace is, one needs to solve the representation learning problem first. To decide what is relevant information to representation, one needs to define the task the representation will be used for. Features that are noise with respect to one task are relevant information w.r.t another task. For example: for a coarse level classification task more information is irrelevant hence $U_k$ is lower rank. That means the mode in your uni-modal plots will be at higher noise levels. For a more granular classification task, more information about details are needed, so the mode will be at lower noise levels. Thus, the whole notion of "representation quality"as a function of noise level  is not well-defined.
5. The authors are using two separate notions of representation: the ave-pooling responses in the bottleneck layer, and the strength of projections of posterior mean onto the class subspace (CSNR). Merely showing that both of these are uni-modal as a function of noise level doesn't prove anything! Specially given that the maximums happen at different noise levels!


### Questions
1. Why does it make sense to replace $x_t$ with $x_0$ in $x_\theta(x_t, t)$?! What is $x_\theta(x_0, t)$ computing? This ad-hoc replacement creates an inconsistency between the noise level on the input image and the noise variance given to the network. Now it is not clear what the output of the function $x_\theta$ is after creating this inconsistency, and is not clear how to interpret empirical results that involve this (which seems to be all the empirical results). 
2. What does figure 1a convey? How did you measure *posterior accuracy* for CIFAR images? What is called posterior accuracy throughout the paper is equivalent to denoising performance. Indeed you can measure denoising performance, but how did you measure its accuracy for **real** images?! This is an unsolved problem, and it is not explained in the paper how the authors solved it. 
3. Figure b shows a result that has been around for a long time. That is denoising at higher noise levels results in the loss of details. It's not clear how this is part of their results, given that this has been known for more than 100 years and also has been rediscovered in deep learning era again and again. There should be at least some citations.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
I believe the authors try to study the structured emerged from training multi-scale score matching objective. Given different noise scale, for the model to achieve score matching (denosing), it musts learn feature at that scale. For example, for score matching on natural images, if the noise level is low, the model just need to learn low level (texture) features to denoise. But when the noise level is high, the model needs to learn high level (features) concept or also have to guess what's in the image. The author shows different scale of features learnt by multi-scale score matching can be used for semantic task like image classification, as well as for posterior estimation of mixture of Gaussian. The author author shows the performance of doing these task under different noise scale form an inverted u shape curve. Under strict assumption of mixture of Gaussian, the author provide analysis on the posterior estimation power given differer noise level. The author compare the learnt model's performance with the optimal one.

### Strengths
1. It relates multi-scale score matching to posterior estimation to representation learning.
2. It make (realistic?) assumption on the data so the connection in 1 can be studied and analyzed theoretically.
3. The theoretically analyze under simple data assumption is thorough.

### Weaknesses
1. I felt like the paper is missing lots of detail. I have to make many assumption outside the paper.
2. I wish I see a cleaner method. Despite these's extensive experiment and theoretical analysis under the strict "mixture of low-rank Gaussians" setting. I don't really see the key message. What I get is that different level of features learnt at different scale can be used for posterior estimation of mixture of Gaussian, as well as doing classification. How are these two related specifically? One statement is that they both has the inverted U shape curve. But is that it? I hope the author can make this more clear. 
3. Figure 4b tells us the learnt multi-scale score matching function (with neural network?) behave different from the optimal one on a simple dataset. I think this is really interesting result. But I also think the author should provide some insight on why is this the case, because it might reveal the nature of bias in neural network. For example, in [1], they find cnn based denoiser cannot learn optimal solution for simple toy example like global planer wave because it has spatial locality as bias.

### Questions
1. For image denosing case, I'm assuming the work is based on the idea of latent diffusion. So x_0 is the clean data embedded into the latent space using a VAE? Or it's the raw image? 
2. How is U_k calculated for cifar10? Is it calculated by doing PCA on all examples (in vae latent space) with class label k?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work evaluates the potential of representation learning with diffusion models. The authors evaluate the connection between the quality of posterior estimation and the quality of learned representations, extending this analysis to different scenarios.

### Strengths
- In Section 4.1, the authors present an interesting and insightful analysis of the effect of diffusion training with multiple levels of noise passed through the same model on the learned representations. It is intriguing to see that diffusion models have relatively steady representations across different denoising timesteps.

### Weaknesses
 - Several results presented in this work are not novel. For example, the evaluation presented in Figure 1 was already discussed in [1] and [2]. As noted by authors, the fact that representation learning dynamic captures a “fine-to-coarse” shift with the increased amount of noise was already noted in DAE works [3] and [4]
- I fail to see the significance of the contribution “Linking posterior estimation ability of diffusion models to representation learning”. Isn’t this observation a straightforward implication of the fact that samples at the late diffusion steps are, by definition, more noisy, which results in lower quality of the posterior estimation and higher entropy when analyzing predictions from the linear probe?
- The “representation learning” capability evaluation is very limited to the simple linear probing task. This significantly limits the significance of the presented results. Extending the analysis with other SSL tasks would strengthen the submission.
- Editorial: I’m lost in the presentation of this work as in Sec. 2.3 it is written that “since diffusion models tend to memorize the training data instead of learning underlying data distribution when the training dataset is small (Zhang et al., 2023), we focus on the case where sufficient training data is available throughout our analysis in Section 3”, yet there Figure 2 on the second page seems to be a reproduction of work by Zhang et al. The analysis related to Figure 2 is presented on the last page


### Questions
- As indicated in line 192, in a setup with clean images used being used for classification, the diffusion model is imputed with clear image and timestep t, “where t serves solely as an indicator of the noise level for diffusion model to adopt during feature extraction.” Isn’t this setup out of distribution for a model, as the diffusion model is never trained with a clear image or conditioned with a timestep equal to zero?
- Why limiting the evaluated features to only those encoded in the bottleneck layer of the UNet architecture? A lot of information relevant to classification (such as high-frequency features) might be passed through the residual connections.

### Soundness
3

### Presentation
2

### Contribution
1
