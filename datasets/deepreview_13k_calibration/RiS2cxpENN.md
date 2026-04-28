# Diffusion Models as Cartoonists! The Curious Case of High Density Regions

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
We investigate what kind of images lie in the high-density regions of diffusion models. We introduce a theoretical mode-tracking process capable of pinpointing the exact mode of the denoising distribution, and we propose a practical high-probability sampler that consistently generates images of higher likelihood than usual samplers. Our empirical findings reveal the existence of significantly higher likelihood samples that typical samplers do not produce, often manifesting as cartoon-like drawings or blurry images depending on the noise level. Curiously, these patterns emerge in datasets devoid of such examples. We also present a novel approach to track sample likelihoods in diffusion SDEs, which remarkably incurs no additional computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces new augmented SDE for likelihood estimation in SDE sampling of diffusion models. Moreover, a novel theoretical mode-tracking approach is proposed in order to locate the exact mode of the generative distribution and introduce a high-probability sampler capable of generating samples with higher likelihood than all the other samples, under theoretically proved guarantees. 
Finally, the main findings of the proposes analysis lies in the discovery of Cartoon-like images that lies in high-likelihood regions, even if the model has never been trained with images of the same style.

### Strengths
- The paper is well written and it develops new theoretical insights, especially the augmented SDE for tracking likelihood evolution are innovative and pratical since they don't introduce any additional computational cost.

- The proposed high-probability sampler is a nice tool to generate high-likelihood samples that are not discoverable by traditional sampling techniques

- The paper analize the diffusion probability landscape finding analyzing the different images in high-likelihood regions, experimentally demonstrating that the proposed theoretical tools can be used to perform analyisis of this landscape.

### Weaknesses
 - The proposed mode-tracking approach has a very high computational cost and this is not clearly discussed. The discussion on how this mode-tracking approach scale and its computational limitations should be discussed and quantified. Specifically, the paper lacks a detailed analysis of the computational complexity of the mode-tracking ODE, making it difficult to assess its practical applicability. The authors should provide a breakdown of the operations involved and how the cost scales with the dimensionality of the data and the number of steps required for convergence.

- The high-likelihood samples discovered by the proposed analysis does not seem to have a real practical advantage, being cartoon drawings or blurry images. It is not discussed how these insight can be leveraged to improve sample generation strategies or how these high-density samples can be practically useful. The paper should explore potential applications or modifications to the sampling process that could benefit from these findings, rather than simply presenting them as an interesting observation. The lack of a clear practical application diminishes the impact of the theoretical analysis.

- The limitations of the work are not discussed at all, a limitations section covering all the main potential limitations should be added. This should include a discussion of the assumptions made in the theoretical analysis and how they might affect the results, as well as the limitations of the experimental setup and the generalizability of the findings. A thorough discussion of limitations is crucial for a balanced assessment of the work.

- The work does not report any implementation details, code and implementation are not submitted in the supplementary materials. It would be important to openly release the contribution upon acceptance to ensure reproducibility and improve transparency. The absence of implementation details makes it difficult to reproduce the results and verify the claims made in the paper. The authors should provide sufficient information to allow other researchers to replicate their experiments.

- The analysis of high-density regions is done on small and simple diffusion models trained on restricted datasets with limited variability. Moreover the selected models and study is done on uncoditional sampling without any guidance from text. In my opinion it would be valuable to explore real-world and more complex diffusion models (such as SD, Flux etc), especially focusing on the impact of text. The current analysis is limited by the use of simple models and datasets, which may not reflect the behavior of more complex models used in practice. The authors should investigate the applicability of their findings to more realistic scenarios, including conditional generation with text guidance.

- The related work does not take into consideration a very relevant paper "Null-text Guidance in Diffusion Models is
Secretly a Cartoon-style Creator", Zhao et al which is not discussed. In particular it would be relevant to highlight some connection and insights with this previous related work.

### Questions
- The related work does not take into consideration a very relevant paper "Null-text Guidance in Diffusion Models is
Secretly a Cartoon-style Creator", Zhao et al which is not discussed. In particular it would be relevant to highlight some connection and insights with this previous related work. 

- See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the high-density regions of diffusion models, discovering that samples in these regions often appear as unrealistic cartoon-like or blurry images, despite the absence of such images in the training data. The authors propose a novel framework based on augmented stochastic differential equations (SDEs) to estimate the likelihoods of generated samples. This approach enables efficient, high-likelihood sampling without additional computational cost. The authors also introduce a high-probability sampling method that consistently yields higher-likelihood images than traditional sampling techniques, while their empirical analysis shows that images with less detail (e.g., blurred images) tend to achieve higher likelihood scores. The paper contributes to a better understanding of the diffusion model probability landscape and the relationship between likelihood and image quality.

### Strengths
The paper introduces a novel framework for estimating likelihoods within diffusion models using augmented stochastic differential equations (SDEs) and high-probability samplers. This is an important advancement because it allows the exploration of high-likelihood regions without increasing computational costs. By deriving density estimates through augmented SDEs, the authors provide a theoretically efficient approach to analyzing model outputs across noise levels, setting a foundation for future studies in likelihood-based generative modeling. The findings reveal that high-likelihood samples often resemble cartoonish or blurry images—even though such images are not present in the training data.

### Weaknesses
1. Although the paper sheds light on high-density regions and likelihood estimation, it lacks a clear discussion on how these findings could practically inform the design or improvement of diffusion models in applied settings. Without recommendations on balancing high-likelihood sampling with image quality, it’s challenging to draw valuable insights from the findings, particularly for practitioners focused on real-world applications.

2. The paper describes the emergence of cartoon-like images in high-likelihood samples but provides limited exploration into why or how this phenomenon occurs. Specifically, the paper does not delve into the underlying mechanisms within the diffusion process that lead to this outcome, nor does it analyze the specific characteristics of these images (e.g., frequency components, color palettes) that might explain their high likelihood.

3. The experiments are primarily conducted on well-known datasets like CIFAR-10 and FFHQ-256. Expanding the study to other types of diffusion models or additional data domains would strengthen the generalizability of the findings. Additionally, clarifying any specific architectural limitations of the proposed high-probability sampler could benefit those aiming to extend the approach. For instance, it is unclear if the sampler is compatible with different noise schedules or if it requires specific network architectures to function effectively.

4. While the paper emphasizes the likelihood of generated samples, it does not address diversity within these high-likelihood outputs. The authors mention blurry and cartoon-like images, but they do not provide an assessment of diversity or how the high-likelihood sampling might affect the overall variance in generated outputs. It’s unclear if the method leads to mode collapse or reduces the richness of the model’s output space.

### Questions
1. Does the high-likelihood sampling technique impact the diversity of generated samples, potentially leading to mode collapse or other reductions in output variability? 

2. For applications that prioritize both high likelihood and visual quality, what adjustments to the high-probability sampler could mitigate the production of low-quality images?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors offer a theoretical framework for estimating the log probability of samples that follow SDE in diffusion models. They develop novel forward and reverse augmented dynamics that estimates log probability not only for the case where $\nabla \log p_{t}(x)$ is known precisely but for the case where the score function is known. Then, the authors provide novel upper and lower bounds on the bias of the proposed estimator and analyze them on the experimental data. Lastly, the authors apply their proposed theory to analyze the diffusion probability landscape. They propose a simple yet effective way to generate samples with the highest log probability and show that such samples are unrealistic and blurry.

### Strengths
* The authors develop a novel theory of augmented SDEs. They provided a clear and detailed derivation and coupled it with the bias estimation 
* Landscape analysis gives valuable insight into the structure of high-probability samples and provides a theoretical justification for the known fact that distorted images tend to have a higher likelihood 
* The paper is well-structured and easy to read

### Weaknesses
1. It isn't clear whether analysis from Section 5 can lead to the creation of better stochastic samplers or improve the quality of image generation. Overall practical implications of this work are quite poor 
2. There is no intuition behind observations from Figure 4. More precisely, what does it mean that the model optimized for sample quality yields a smaller difference between $p_{0}^{ODE}$ and $p_{0}^{SDE}$?
3. Experiments were conducted on rather small and outdated diffusion models. It would greatly improve the scope of the work if the experiments were performed on the frontier models

### Questions
1. Have the authors thought about how the proposed theory can be used to improve the quality of image generation?
2. Can we use the proposed estimation for the log probability to evaluate model quality the same way as [1] (Table 2)? Will there be any difference between SDE and ODE estimation? Which one is better to compare different models?

[1] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. arXiv preprint arXiv:2011.13456, 2020c.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a perspective on studying likelihoods for diffusion models. They introduce a stochastic way to keep track of the likelihood. They introduce a likelihood maximizing ODE that maximizes the likelihood of a path for any given starting condition. They attempt to argue that they can use this ODE to demonstrate that the high likelihood region of diffusion models results in cartoon like images.

### Strengths
- The paper is well written and the use of good figures and colors in equations really helps the presentation
- They present a stochastic way to keep track of the likelihood and a likelihood maximizing ODE

### Weaknesses
 - Up to section 4.2 everything was very reasonable and nicely introduced, however the use of the ODE in remark 1 for sampling is a big mistake. Real world data is multimodal, for instance CIFAR 10 has at least 10 modes. To use the assumption that the data is gaussian in order to use remark 1 results in incorrect results. Specifically this ODE doesn't sample from the correct target distribution, and therefore we observe those cartoon like images. 
- Additionally when comparing the likelihood of images sampled normally or from the HP-ODE the likelihoods were measured using different methods. In section 4.3 it is explained how they compute the likelihood of $p(y_0|x_t)$. Empirically they show that it results in higher likelihood than $p(x_0 |x_t)$, however since these likelihoods are being evaluated in different ways this comparison doesn't make sense. If done correctly the sample $y_0$ would be evaluated using the same way as $x_0$, so we would evaluate the likelihood of the **same distribution**
- The paper has a limited amount of quantitative evidence
- There is no explanation on the hyperparameters that were used during sampling

### Questions
Please see weaknesses

### Soundness
3

### Presentation
4

### Contribution
2
