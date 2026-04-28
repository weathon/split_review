# Structured Diffusion Models with Mixture of Gaussians as Prior Distribution

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
We propose a class of structured diffusion models, in which the prior distribution is chosen as a mixture of Gaussians, rather than a standard Gaussian distribution. The specific mixed Gaussian distribution, as prior, can be chosen to incorporate certain structured information of the data. We develop a simple-to-implement training procedure that smoothly accommodates the use of mixed Gaussian as prior. Theory is provided to quantify the benefits of our proposed models, compared to the classical diffusion models. Numerical experiments with synthetic, image and operational data are conducted to show comparative advantages of our model. Our method is shown to be robust to mis-specifications and in particular suits situations where training resources are limited or faster training in real time is desired.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a class of structured diffusion models that utilize a mixture of Gaussian distributions as the prior, rather than the conventional standard Gaussian distribution. It also proposes a straightforward training procedure that effectively integrates this mixed Gaussian prior. Through numerical experiments with the EMNIST and CIFAR10 datasets, the authors demonstrate that the proposed mixDDPM and mixSGM achieve better generation performance than DDPM and SGM at the same sampling steps.

### Strengths
1. The structure of the paper is well organized and effectively facilitates the presentation of its content.
2. It is both intuitive and reasonable to consider employing a mixed Gaussian prior in diffusion models, which, as opposed to a single Gaussian distribution, allows for a more accurate representation of the real data distribution. The resulting performance improvements align well with this intuition.

### Weaknesses
1. The paper lacks a thorough discussion of the impact of varying K values on model performance, particularly whether mixDDPM merely degrades to DDPM when K=1 or if it has a more efficient training procedure compared to DDPM. Additionally, it fails to address whether an excessively large K introduces unnecessary computational overhead or whether the choice of K selection algorithms affects the results. Specifically, the paper does not analyze how the choice of K impacts the convergence rate of the model or the quality of the generated samples, and whether there are diminishing returns as K increases. Furthermore, the paper does not provide any guidelines on how to select K for different datasets or tasks.
2. While the experimental results demonstrate that mixDDPM achieves better generation performance than DDPM with the same number of steps, the paper does not address whether the combination of multiple Gaussian distributions incurs greater storage and computational overhead during model training and whether there is a trade-off involved. The paper should provide a detailed analysis of the memory footprint and computational cost of mixDDPM compared to DDPM, including the time complexity of the training and sampling processes. It should also discuss whether the increased complexity of the model leads to overfitting or other issues.
3. The paper may need to include additional experiments. It would be important to investigate whether mixDDPM and mixSGM remain applicable to more complex data structures, such as high-resolution image generation scenarios. The current experiments are limited to relatively simple datasets, and it is unclear whether the proposed method can scale to more challenging tasks. The paper should also investigate the robustness of the proposed method to different hyperparameter settings and noise levels.
4. The manuscript contains several typos, such as in Section 4.2, where the first sentence reads, "Suppose a given data x0is assigned," missing a space between "x0" and "is."

### Questions
See the weaknesses part above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies a class of structured diffusion models, mixDDPM and mixSGM, using a Gaussian Mixture Model (GMM) as the base distribution (prior distribution) instead of Gaussian, in order to utilize more structure information of the dataset.

### Strengths
Instead of using Gaussian prior as most work does, the authors make use of the potential clustering information from the training set with GMM priors. This improves the efficiency for the cluster-finished problems. The authors also discuss practical implementations, such as using a data-driven clustering method to select the centers of the GMM. The experiments on datasets like MNIST show some improvements training steps. The authors also give simple computational algorithms.

### Weaknesses
0. Innovation. Please notice the paper: Guo et al (2023, NeurIP 2023) and Zach et al (2023, SSVM). The ideas seem quite similar. Moreover, there are a lot of work using non-Gaussian priors, or actually more general priors.
1. Although the authors mention 'not all scenarios where diffusion models are used enjoy access to extensive training re-sources', the scale of the experiments are far too small. Have you tried scaling up?
2. What if the number of clusters are quite large? Solving large clusters problem can be another new issues. If having numerous number of clusters, the prior can be ill-posed. It can be close to nonparametric case and the computation is quite expensive. This method already restricts the dim of the problem. It seems that the number of clusters also needs restricted.
3. Theoretically, from Gaussian to GMM, people just need one step, using one more layer like in the hierarchical models.
4. CIFAR-10 and NIST datasets are a little bit small. And in the experiment, only original DDPM and SGM compared. FIDs are far higher than SOTA, maybe indicating the lack of training.

### Questions
Please see the weaknesses.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Diffusion models have become prominent generative models for tasks like image and audio synthesis, but they demand high computational resources due to their multistep noise-corruption and denoising processes. This intensive training can pose challenges, especially for users with limited resources, like small enterprises or real-time applications, where accelerated training is essential. To address these constraints, the authors propose enhancing classical diffusion models by adjusting the prior distribution. Instead of the standard Gaussian prior, they suggest using a Gaussian Mixture Model (GMM) as the prior, which can leverage any inherent structure in the data. This approach aims to improve training efficiency and maintain model performance even with fewer resources. Key contributions of this work include:

(1) Developing “mixed diffusion models” that use a GMM prior, detailing both forward and reverse processes, and introducing variants like Mixed Denoising Diffusion Probabilistic Models (mixDDPM) and Mixed Score-based Generative Models (mixSGM).
   
(2) Introducing a new metric, “Reverse Effort,” to measure efficiency by quantifying the reduction in effort needed during the reverse denoising process.

(3) Demonstrating the model’s efficiency through experiments on synthetic and real datasets, highlighting its effectiveness under limited training resources.

### Strengths
1. Perhaps the introduction of a “Reverse Effort” metric provides a fresh perspective on quantifying the model's efficiency and aligns closely with practical concerns around computational cost in generative modeling.

2. The paper is written with clarity and conciseness, making complex concepts accessible. The structure follows a logical progression, starting with motivation, theoretical developments, and concluding with empirical validation.

### Weaknesses
1. The choice of a Gaussian Mixture Model (GMM) as the prior is intriguing, but the paper does not fully analyze why a GMM is particularly well-suited for diffusion models over other structured priors (e.g., Student’s t-distribution, other hierarchical models). Specifically, the paper lacks a discussion on the limitations of GMMs, such as their potential to oversimplify complex data distributions or the challenges in determining the optimal number of mixture components. A more thorough analysis should include a comparison of GMMs with other potential priors, considering factors like computational cost, flexibility in modeling different data types, and the ability to capture long-range dependencies.

2. While the “Reverse Effort” metric is an interesting addition, its practical interpretation and relevance could be better explained. The paper might improve by providing additional intuition behind this metric, perhaps through visualizations or step-by-step examples demonstrating how “Reverse Effort” correlates with sample quality. For instance, it would be beneficial to see how changes in the reverse effort correspond to observable differences in the generated samples, and whether this metric is sensitive to different aspects of the data distribution. The paper should also discuss the limitations of this metric and whether it is applicable to different types of data and diffusion models.

3. This reviewer has certain concerns over the model structure based on the mixture of Gaussian prior. As both diffusion forward and reserve processes are designed based on the cluster label information of the data which is pre-determined according to the initial centroids, thus the entire process is roughly equivalent to couple of individual diffusion process (although all the noise models share the same networks and trained individually).  Originally I would expect that the mixture of Gaussian structure can be propagated on the chain. But it is not.  This entirely downgrades the paper's innovation level. The lack of interaction between the different Gaussian components during the diffusion process is a significant drawback, as it prevents the model from learning a truly unified representation of the data. The model essentially performs independent diffusion processes within each cluster, failing to leverage the potential benefits of a mixture model structure.

### Questions
1. It seems the process depends on the initialization of the centroids c_j.   Could the author(s) explore more on this initialization.  What is its impact on the final generalized distribution.

2. Several experiments have been conducted on several basic datasets such as EMNIST and Cifar10.  They are quite classic.  Can more modern dataset be used for testing, for example, LSUN (Large-scale Scene UNderstanding Challenge)?

3. Why in Algorithm 2, the cluster index j is gone missing in noise model \epsilon_{\theta}?

4. Perhaps ReEff defined in (14) and (15) are OT-distance?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a variant on diffusion models where the initial  noise (x_T)  has a Gaussian Mixture Model (GMM) distribution rather than a Gaussian distribution. The algorithm is equivalent to first clustering the datapoints, and then training a diffusion model separately for each cluster. The paper proves that by first clustering the points, the amount of work that the diffusion model has to do is lower. Experiments show that for a small number of iterations, the results of the proposed method have better FID than using a Gaussian prior.

### Strengths
The basic idea is simple and appealing: if the data distribution is composed of different clusters, it makes a lot of sense to model each cluster separately. This intuition is nicely formalized in proposition 1.

### Weaknesses
The algorithm is described quite poorly. At first reading, it looks very complicated but in fact the proposed method is just to first cluster the data and then run diffusion models separately on each cluster.

The requirement of first clustering the data is a weakness because finding a good clustering is in itself a difficult problem. I can imagine settings where getting a poor clustering will end up hurting the final performance.

In terms of significance, the paper mainly argues for lower effort (the average distance between the initial noise vector and the final generated sample). But it is not clear why in practice we would care about effort. The paper argues that this also leads to better visual results when we consider a limited number of training steps but I did not see any theoretical support for the improvement in visual quality. The numerical experiments also show better FID scores with a fixed number of training steps but the results seem inferior to previously published DDPM results on the same datasets.

### Questions
Is there a theoretical connection between effort and sample quality?

How do the samples that you generate with DDPM compare to published results?

### Soundness
3

### Presentation
2

### Contribution
2
