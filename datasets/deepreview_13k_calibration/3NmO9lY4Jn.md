# Don't Play Favorites: Minority Guidance for Diffusion Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
We explore the problem of generating minority samples using diffusion models. The minority samples are instances that lie on low-density regions of a data manifold. Generating a sufficient number of such minority instances is important, since they often contain some unique attributes of the data. However, the conventional generation process of the diffusion models mostly yields majority samples (that lie on high-density regions of the manifold) due to their high likelihoods, making themselves ineffective and time-consuming for the minority generating task. In this work, we present a novel framework that can make the generation process of the diffusion models focus on the minority samples. We first highlight that Tweedie's denoising formula yields favorable results for majority samples. The observation motivates us to introduce a metric that describes the uniqueness of a given sample. To address the inherent preference of the diffusion models w.r.t. the majority samples, we further develop \emph{minority guidance}, a sampling technique that can guide the generation process toward regions with desired likelihood levels. Experiments on benchmark real datasets demonstrate that our minority guidance can greatly improve the capability of generating high-quality minority samples over existing generative samplers. We showcase that the performance benefit of our framework persists even in demanding real-world scenarios such as medical imaging, further underscoring the practical significance of our work.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper claims that the distribution that diffusion learns tends to lead to the underrepresentation of certain parts of latent space. They tried to show and provide guidance to produce the underrepresented classes.
They used CelebA 64×64, ImageNet 64x64, LSUN Bedrooms 256x256, and a proprietary Brain MR dataset to show the effectiveness of their approach.

### Strengths
The introduction of metrics and the guidance to improve minority representation is interesting. The text is easy to follow and read, and the qualitative and quantitative results are intuitive. I enjoyed reading through the paper, despite some  questions raised through the arguments.

### Weaknesses
The paper interchangeably uses the general term of diffusion models and assumes that the Tweedy formula is a general form of any diffusion model.

The author cited the paper, Sehwag, V., Hazirbas, C., Gordo, A., Ozgenel, F. and Canton, C., 2022. Generating high fidelity data from low-density regions using diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 11492-11501).
as a motivation "The principle guarantees their generated samples to respect the (clean) data distribution, which naturally makes the sampler become majority-oriented, i.e., producing higher likelihood samples more frequently than lower likelihood ones (Sehwag et al., 2022)," but in the cited paper, they claimed that uniform sampling is the problem, and changing the sampling process could introduce novel, or as authors phrased samples from "long-tail" part of the distribution:
"We observe that uniform sampling from diffusion models predominantly samples from high-density regions of the data manifold. Therefore, we modify the sampling process to guide it towards low-density regions while simultaneously maintaining the fidelity of synthetic data."

The authors mentioned this baseline but only used it in one of the datasets, even though this work at least claimed that they tackled the problem of long-tailed distribution generation. In addition, in that dataset, the results are in 64x64, whereas Sehwag et al. mentioned that they produced 256x256 images after upscaling from 64x64.

This paper seems also doing similar approach, but has not been investgated.
Qin, Y., Zheng, H., Yao, J., Zhou, M. and Zhang, Y., 2023. Class-Balancing Diffusion Models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 18434-18443).

### Questions
In Fig. 2, how the labels of small, moderate, and high minority scores are assigned in real data?
In Proposition 1, could you please clarify what you mean by "Assume that a given noise-conditioned score network sθ(xt, t) have enough capacity?" and how does it affect the proposed method?
Why did not you evaluate CIFAR-LT which is seemingly designed for such a task? (Cao, K., Wei, C., Gaidon, A., Arechiga, N. and Ma, T., 2019. Learning imbalanced datasets with label-distribution-aware margin loss. Advances in neural information processing systems, 3)

### Soundness
2 fair

### Presentation
3 good

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
This work tackles the problem of minority data generation using diffusion models. First, they propose a metric that defines the uniqueness of a sample. Then, they propose a classifier guidance approach based on the proposed metric to generate minority samples. The proposed metric and guidance are based on Tweedie's formula for denoising. The method is evaluated on 4 datasets for the minority generation task.

### Strengths
1. The theoretical background is well explained and supports the claims.

2. The paper is well-written and easy to follow.

3. The idea of using Tweedie's denoising method for minority sample generation seems to be novel to the best of my knowledge.

### Weaknesses
1. Evaluation: The baselines are limited to a few outdated works (StyleGAN 2020, DDPM 2020). The only recent baseline is by Sehwag 2022 on ImageNet which outperforms the proposed method in two out of four metrics. All methods in Tab. 1 are evaluated for the minority generation task, which despite being old, outperform the proposed method in some metrics. More recent methods, such as LDM [a], which is not even cited, can generate minority samples to some extent. The evaluation lacks a thorough comparison with state-of-the-art methods, particularly those employing diffusion models. The performance of the proposed method should be benchmarked against more recent and relevant techniques to properly assess its contribution. The evaluation also does not explore the sensitivity of the method to hyperparameter choices, which could significantly impact its performance.

2. Literature Review: The literature review is limited. There are many related methods that are not cited, contrasted against, or compared to:

[a] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." CVPR 2022.

[b] Huang, Gaofeng, and Amir Hossein Jafari. "Enhanced balancing GAN: Minority-class image generation." Neural computing and applications 35.7 (2023): 5145-5154.

[c] Samuel, Dvir, et al. "Generating Images Of Rare Concepts Using Pretrained Diffusion Models. arXiv 2023.

### Questions
1. The method is evaluated quantitatively for the minority image generation task. Doesn't it lead to loss of performance for generating long-tail data?

2. Were the minority samples only chosen based on the minority score? Did the authors perform any verification on whether they are all actually minorities? There are some samples shown for different minority scores, but I was wondering if there was a more systematic verification process or not.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work the authors proposed a guidance to diffusion models so it is encouraged to generate the minority data. In doing so, the author opposed the use of the distance between original data and the denoised version of the same data by a diffusion model as a minority score, inspired by Tweedie’s denosing formulae. Data with larger such score is used to train a auxiliary classifier, which is used to guide the generation with commonly used classifier-guidance approach. Substantial theoretical and empirical results are shown to demonstrate the superiority, especially quantitative, of the proposed method.

### Strengths
Overall, this paper is okay to read. It is a neat combination of straightforward ideas that produces good results: identifying uniqueness with distance between clean and denoised data, marking the data points that are showing minority data, and training a classifier of minority data to guide the generation. 

Particularly, the problem of generating samples belonging to the minority part of the data domain is an interesting one with potential applications. Components in the proposed work are existing ideas (Tweedie’s formula inspired deonsing, training auxiliary classifier to guide the inference process), but the quantitative quality are consistent and should give readers some insights. Furthermore I’d like to praise the authors for detailed explanation of the method, theories behind and extra examples in appendix.

However there are some issues (see weaknesses and questions below) in the manuscript. Overall my assessment of this manuscript is borderline, but if my concerns are addressed I’m happy to adjust accordingly.

### Weaknesses
Overall the technical contributions are somewhat limited, as ideas are from existing works. This may not be a issue on its own as long as the work presents an interesting approach in the whole, but a few missing details hurts, as follows:

It is unclear how the minority classifier guidance plays with other classifier guidance or classifier-free guidance. From an application perspective, it’s important that users can control the generation through guidance, and a mere generation of minority data, while still being useful for say data augmentation, may limit its value for the end-user if the user cannot control the generation effectively. However, now only in Appendix E some examples are shown for conditional generation and details/quantitative evaluates are omitted. This makes it hard to assess the broader impact of this work.

Also, it would be better to discuss the rationale behind minority score — the exact motivation of having a minority data generation remains not elaborated.

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

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
This article primarily aims to address the issue of diffusion models' inability to generate data samples in low-density regions of the data manifold. Initially, they illustrate that Tweedie's denoising formula tends to generate the majority of samples, which lie in high-density regions of the manifold. Building upon this, they devise the minority score to quantify the uniqueness of the features of a given data instance. Drawing inspiration from classifier guidance, they incorporate minority guidance into the diffusion model to generate samples in low-density regions.

### Strengths
1. The paper is easy to read and generally well-written.
2. The paper evaluates the proposed method on benchmark real datasets and demonstrates the effectiveness of their approach in demanding real-world scenarios, such as medical imaging.

### Weaknesses
1. Given the scarcity of real samples in low-density regions, the paper does not adequately address the potential for overfitting when generating samples in these regions. While the minority score aims to quantify uniqueness, it remains unclear how the model differentiates between truly novel features and artifacts arising from fitting to a limited number of real samples. A more rigorous analysis of the authenticity and diversity of generated samples in low-density regions is needed. This could involve examining the distribution of generated samples relative to the few available real samples in these regions, or exploring metrics beyond nearest neighbor distances to assess sample diversity.
2. The experimental details provided are insufficient for full reproducibility and understanding of the method's application. The paper should specify the exact size of the subset of real data used for validation in each experiment. Furthermore, clarity is needed on the selection of minority score levels for data generation. Providing the range or distribution of minority scores used in each experiment would allow for a better understanding of how this parameter influences the results.
3. In Fig. 1(a), the specific perturbation timestep used to generate the noise samples in the middle is not explicitly stated. Clarifying whether it is 0.9T or T is important, as the choice of 't' significantly impacts the interpretation of Section 3.1. Additionally, the authors should provide a more detailed justification for why the reconstructed image is indeed a valid reconstruction. Showing specific images of $x_t$, $x_0$, and $\hat x_0$ for different values of 't', or providing a more rigorous theoretical analysis of the reconstruction process based on the chosen perturbation timestep, would strengthen the argument.
4. In the experimental section, the proposed method does not achieve satisfactory results in terms of both precision and recall, particularly on the LSUN-Bedrooms dataset. While the paper focuses on generating samples in low-density regions, a more thorough discussion of these results is necessary. The authors should provide a more detailed analysis of the trade-offs between precision and recall in the context of minority sample generation and discuss potential reasons for the observed performance.
5. The nomenclature in the paper could be more standardized. For instance, in Section 4.2, the representation of $\tilde l$ appears to have an error. Consistent and accurate notation throughout the paper is crucial for clarity and understanding.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
