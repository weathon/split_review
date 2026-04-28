# PREDICTING 3D STRUCTURE BY LATENT POSTERIOR SAMPLING

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
The remarkable achievements of both generative models of 2D images and neural field representations for 3D scenes present a compelling opportunity to integrate the strengths of both approaches.
In this work, we propose a methodology that combines a NeRF-based representation of 3D scenes with probabilistic modeling and reasoning using diffusion models.
We view 3D reconstruction as a perception problem with inherent uncertainty that can thereby benefit from probabilistic inference methods.  
The core idea is to represent the 3D scene as a stochastic latent variable for which we can learn a prior and use it to perform posterior inference given a set of observations. 
We formulate posterior sampling using the score-based inference method of diffusion models in conjunction with a likelihood term computed from a reconstruction model that includes volumetric rendering. 
We train the model using a two-stage process: first we train the reconstruction model while auto-decoding the latent representations for a dataset of 3D scenes, and then we train the prior over the latents using a diffusion model.
By using the model to generate samples from the posterior we demonstrate that various 3D reconstruction tasks can be performed, differing by the type of observation used as inputs. 
We showcase reconstruction from single-view, multi-view, noisy images, sparse pixels, and sparse depth data. 
These observations vary in the amount of information they provide for the scene and we show that our method can model the varying levels of inherent uncertainty associated with each task.
Our experiments illustrate that this approach yields a comprehensive method capable of accurately predicting 3D structure from diverse types of observations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to combine diffusion prior and conditional gradient from reconstruction model to achieve posterior sampling. The authors choose to use latent code to representation each scenes and learn an mapping from latent code to tri-plane representations by minimizing the image loss after rendering. They try to prove the effectiveness of their method by showing reconstruction quality.

### Strengths
1. They propose to use latents to represent various objects in a dataset, and train diffusion on latents, which is reasonable and efficient to approximate the distribution of the dataset.
2. They provide the possibility of generating 3D uncertainty maps after training a "generative prior".
3. They provide the results of extensive experiments like noisy observed images, sparse observed images reconstruction, and they get relatively better results.

### Weaknesses
1. The method lacks more novelty, which has been proposed really similarly in previous works.
2. The tasks are relatively easy and the results are few and not impressive.

3. Diffusion models are very likely to memorize rather than generalize when the data scale is relatively small, which has been studied and proved by many works. So can the authors explain, whether the results of your posterior sampling are generalizable or not, as the data amount is small? Also, the test dataset size is too small to provide more solid proofs and insights.
4. Basically, given 100 images about a scene, we can directly get a NeRF. Can the author explain what is the need for optimizing a latent? Or can the author prove that the NeRF generated directly is worse that the results of your method?
5. Also, we can train the diffusion model directly by CFG(classifier-free-guidance), which also play the role of posterior sampling. What is the advantage of using RM gradient, which is also similar with conditional score in CFG?

### Questions
1. Diffusion models are very likely to memorize rather than generalize when the data scale is relatively small, which has been studied and proved by many works. So can the authors explain, whether the results of your posterior sampling are generalizable or not, as the data amount is small? Also, the test dataset size is too small to provide more solid proofs and insights.
2. Basically, given 100 images about a scene, we can directly get a NeRF. Can the author explain what is the need for optimizing a latent? Or can the author prove that the NeRF generated directly is worse that the results of your method?
3. Also, we can train the diffusion model directly by CFG(classifier-free-guidance), which also play the role of posterior sampling. What is the advantage of using RM gradient, which is also similar with conditional score in CFG?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an approach to 3D scene reconstruction by combining neural radiance fields (NeRF) with probabilistic diffusion models. The method uses a two-stage training process: first, it trains a reconstruction model that compresses 3D scenes into compact latent representations using a tri-plane structure, and second, it trains a diffusion model as a prior over these latent representations. During inference, the method performs posterior sampling using the trained diffusion model guided by reconstruction error, allowing it to generate multiple plausible 3D reconstructions that are consistent with the input observations. The authors demonstrate that their method achieves competitive results with existing approaches while showcasing the model's additional capability of inference on a wide variety of tasks with different levels of uncertainty.

### Strengths
1. The authors have provided a well-rounded algorithm that combines CNF with compressed latent, Diffusion prior training for the distribution of latent, and a strategy that combines the prior and the rendering algorithm for sampling from the posterior given the observations. The algorithm is mostly sound and supported by theoretical basis from the Langevin sampling process, and empirical evidence also illustrates its competitiveness with similar methods.
2. The ability to perform inference on 3d reconstruction tasks using widely different observations appears to be novel and is quite interesting. Empirical evidence also shows that the influence of the prior is in proportion to the uncertainty of the 3d structure given the observations. The flexibility and effectiveness of such a posterior sampling strategy are valuable and can be expanded upon.
3. The two training steps and the sampling strategy are well-explained in the methods section, with clear graphic illustrations and experiment results to support the incentive for the algorithm. The paper is overall easy to understand.

### Weaknesses
1. In the contributions section the authors mentioned "We show that considering the full posterior can lead to better reconstruction and provide additional insight such as 3D uncertainty maps." However, I do not see a clear description of how the 3D uncertainty maps are calculated given the overall pipeline. The method mentions using the variance of ten generated samples, but it is unclear what these samples represent in the 3D space (e.g., are they samples of the latent space, or rendered images, or something else?). A more detailed explanation of how these samples are generated and how their variance is computed to produce the uncertainty map is needed.
2. Although there is plenty of qualitative evidence to support the method, quantitative analysis is limited. It is also worth noting that the Table 2 results show the method does not provide the same accuracy compared to its peers. The paper could benefit from a more comprehensive summary of quantitative results, especially given the claim of improved reconstruction. The current quantitative analysis does not fully support the claim of superior performance, and it is unclear how the method compares to others in terms of standard metrics like PSNR, SSIM, or LPIPS for novel view synthesis, or Chamfer distance or IoU for 3D reconstruction.

### Questions
1. line 478-479 notes that "and an uncertainty map computed by the variance of ten generated samples". This is the only comment to how uncertainty can be calculated in the method. Given uncertainty is an important factor of the work, is it possible to give a clearer explanation on how uncertainty is retrieved? Does the uncertainty measure depend on the task or is it task agnostic?

2. Why are there only limited quantitative results? Have comparisons been done with other methods beyond 1/2 view reconstruction or latent reconstruction? (i.e. reconstruction with noisy/partial images, sparse points/depth)

3. In the last step of the posterior sampling, the gradient is used to update $z_{t-1}$ and is applied directly. Is a step size/ weight here that can be used here to control the influence of the observation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper combines a neural filed representation of 3D objects with a latent diffusion model for 3D novel view synthesis and completion from partial visible information.
In particular, it presents a method that learns prior distribution of 3D objects using a conditional neural field and a latent representation.
Then, a latent diffusion model is introduced to learn the prior over the proposed presentation.
Experiments are conducted on simple synthetic SRN cars and Objaverse-lvis chair, and demonstrate reasonable visual results on both novel view synthesis and completion,
outperforming the pixeNeRF baseline, which is a very old approach.

### Strengths
### S1 --- A good attempt at an interesting and valuable problem

- The task of novel view synthesis from single image is interesting, especially from partially visible inputs. This is very valuable given the heavy occlusion in the real applications, and has been attracting growing interest in the community.
- This paper makes a good initial attempt to tackle this problem in very simple synthetic cases (synthetic objects with single category, rendered with multiple views). The method is reasonable to combine the CNF and diffusion model.

### Weaknesses
### W1 --- Significance is not well demonstrated
- The proposed idea is only a very specific, minor change in SSDNeRF  --- basically using a slightly different conditional neural field (CNF) to replace the original NeRF in SSDNeRF, while the rendering is still the volume rendering. Fundamentally, I am not fully convinced that it is even crucial to use this claimed new representation. In theory, the SSDNeRF also used the tri-planes representation for xy, yz, and xz, and then do the rendering. The change to a conditional neural field, while technically different, does not seem to offer a significant advantage in terms of representation power or rendering quality, especially given that both methods rely on volume rendering.
- While the authors learn the latent representation for each object first, this small change is not so significant. The core of the method still relies on optimizing a latent representation for each instance, which is a common practice in similar works. The claimed novelty in using a diffusion model to learn a prior over these latents does not seem to translate to a significant improvement in reconstruction quality or view synthesis capabilities. The experiments do not clearly demonstrate that the diffusion prior is essential, or that it offers a clear advantage over directly optimizing the latent space.
- In general, I do not think the paper have demonstrated the significance of the proposed change clearly enough. The baseline SSDNeRF model seems to do quite well on these datasets already.  The experimental results do not demonstrate the significance of the proposed methods. Besides, the current interesting towards more on the open-world category. The paper would be stronger to try some more challenging datasets.
 
### W2 --- Confusion on method
- How many latent vectors for each dataset? If we need to define a latent vector for each instance, it will be very expensive to learn this prior distribution. It is unclear how the method scales to larger datasets with more object instances. The computational cost of learning a separate latent vector for each object, especially in the context of a diffusion model, needs to be addressed. The paper lacks a discussion of the computational complexity and scalability of the approach.
- How could we enforce each latent vector corresponding to one instance? If they are paired, how do we match the new instance to the latent space? In L318-L320, the author claimed "...test scenes are used to optimize the scene latents while freezing the model's weights". In this way, how many steps we need to do for the optimisation? And how expensive of this optimisation step? The paper does not provide sufficient detail on the optimization process at test time. The number of optimization steps, the learning rate, and the computational cost of this process are not clearly specified. This makes it difficult to assess the practical feasibility of the method.
- Generally, $z_{t-1}$ still has a large gap to the clean latent. How could this be used for the Reconstruction model for optimisation? The paper does not adequately explain how the noisy latent representation is effectively used for reconstruction. The iterative denoising process and its impact on the final reconstruction quality need to be clarified.

### W3 --- Experiment setting is too simple
- The current experiments are conducted on very simple synthetic data with one special category, which has almost been addressed in the past two years. The use of simple synthetic data limits the generalizability of the findings. The method's performance on more complex and diverse datasets needs to be evaluated to demonstrate its practical relevance.
- While the authors introduce a novel and interesting setting with partially visible information, the pixelNeRF is a too old baseline, which is not good enough to support the importance of the proposed method. The choice of baseline is not adequate to demonstrate the advantages of the proposed method. A comparison with more recent and state-of-the-art methods is necessary to establish the significance of the contribution.

### W4 --- Missing prior work
- First, the decoder-only GaussianCube has been used to represent open-world category and is combined with the 3D diffusion for 3D generation and conditional generation.
- VQ3D is also another latent representation for the in the wild 3D objects. 
- More feed-forward single-view 3D object reconstruction and novel view synthesis should be discussed, such as 3DIM.

### Questions
- What's the key difference between the proposed method to the existing SSDNeRF? A deeper discussion is necessary to highlight the main contribution of this manuscript.
- The proposed pipeline works only on one special category, which is very limited. For example, the similar GaussianCube also leans a decoder-only representation, but with the latest 3D Gaussian representation, and then use a 3D U-Net to deal with the generation and conditional generation. However, they verify the idea on various categories. Why this model can only work on a special category?
- The baseline model PixelNeRF is too old, which is hard to be considered as a baseline to demonstrate the effective of the proposed method. The latest 3DiM, zero-1-to-3, One-2345, Free3D, SV3D and others should be discussed and one of them can be used for the latest baseline.

### Soundness
2

### Presentation
2

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
The paper proposes a probabilistic 3D reconstruction model with diffusion prior. The core idea of this methodology consists of two parts: a two-stage training approach and a posterior inference pipeline. At the first training stage, it uses auto-decoding to train a conditional reconstruction model accompanying with its input latent space on a 3D dataset. Then it trains a diffusion model over the latent. During inference, the model iteratively denoises sampled noise into refined latent for reconstruction, where the reconstruction model provides posterior score at each step. The experiments demonstrate that the proposed framework can be applied on various reconstruction tasks, such as single-view, multi-view, noisy images, sparse pixels, and sparse depth, using some simple datasets. Overall, the paper shows a promising potential in using probabilistic 3D model for reconstruction and possible future development.

### Strengths
1. The paper is well-written and easy-to-understand. The background section provides clear preliminary knowledge on the theories used in this paper.
2. The model reasons the 3D structure well. When given less informative inputs, it synthesizes the overall geometry well and generates accurate uncertainty at unknown parts.
3. The model is time-efficient for 3D reconstruction without optimization at inference time.
4. The paper proposes a novel framework to incorporate posterior sampling and 2D diffusion models with 3D reconstruction model for non-deterministic optimization.

### Weaknesses
1.	The implementation details are not provided in the main paper, and they are also not complete enough in the appendix. Please provide more details so that the paper can be more reproducible. For example, there are some important hyperparameters for evaluation:
- Reconstruction model: rendering samples per ray.
- Hardware: GPU types, number of GPUs.
- Time costs: training hours.
2.	There are some missing works in Section 2. Specifically, many works have attempted to incorporate 2D diffusion priors with NeRF or other 3D reconstruction model, like 3D Gaussian Splatting recently, for single-view or sparse-view reconstruction. The paper only provides two outdated methods, i.e. DreamFusion and Zero-1-to-3, and claims that these models do not consider the uncertainty. However, there are also many works that utilize uncertainty measure during reconstruction to improve view consistency, e.g. [1-4]. Specifically, [4] also uses diffusion as priors, contains uncertainty measures, and targets sparse-view reconstruction, which is very similar to the claimed contribution. Although they haven’t released their code, the author(s) should also consider mentioning these works in the related work section.
3.	The motivation is not clear enough. The paper mentions that 3D reconstruction problem is usually approached with deterministic gradient based optimization methods, while 3D generation is typically addressed with probabilistic models, so the author(s) propose to utilize posterior sampling for probabilistic reconstruction. However, they do not mention the pros and cons of probabilistic methods. In specific, if current 3D reconstruction is good enough, why do we need non-deterministic approaches and how can we benefit from it?
4.	Insufficient comparison with baselines. Only Figure 7 and Table 2 show the comparison with previous works, where Figure 7 has only one example and one baseline, and Table 2 has two baselines. To help evaluation and prevent cherry pick, the author(s) may consider showing more examples from different views/subjects. Also, as mentioned, many 3D works with 2D diffusion can achieve single-view or two-view reconstruction, for example, SDS-based works, i.e. DreamFusion, DreamGaussian. Two baselines may lead to difficulties in evaluation.

### Questions
1.	The paper claims it as an efficient and accurate 3D reconstruction from observations, but did not provide comparison of time/computational/hardware complexity. Specifically, how would you compare this efficiency, and could you provide a quantitative comparison?
2.	See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
