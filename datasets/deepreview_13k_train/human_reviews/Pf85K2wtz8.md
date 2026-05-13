# Deep MMD Gradient Flow without adversarial training

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
We propose a gradient flow procedure for generative modeling by transporting particles from an initial source distribution to a target distribution, where the gradient field on the particles is given by a noise-adaptive \final{Wasserstein Gradient of the} Maximum Mean Discrepancy (MMD). 
The noise-adaptive MMD is trained on data distributions corrupted by increasing levels of noise, obtained via a forward diffusion process, as commonly used in denoising diffusion probabilistic models. %~\citep{ho2020denoising}.
The result is a generalization of  MMD Gradient Flow, which we call
Diffusion-MMD-Gradient Flow or $\DMMD$.
The divergence training procedure is related to discriminator training in Generative Adversarial Networks (GAN), but does not require adversarial training.
We obtain competitive empirical performance in unconditional image generation on CIFAR10, MNIST, CELEB-A (64 x64) and LSUN Church (64 x 64). Furthermore, we demonstrate the validity of the approach when MMD is replaced by a lower bound on the KL divergence.

\iffalse
We propose a novel approach for generative modeling based on noise adaptive version of Maximum Mean Discrepancy (MMD)~\citep{gretton12a} Gradient Flow~\citep{arbel2019maximum}. At the basis of the method is a noise-conditional MMD discriminator trained to distinguish clean from noisy data for a given level of noise. The noisy data is produced from the forward diffusion process commonly used in denoising diffusion probabilistic models~\citep{ho2020denoising}. The proposed procedure mimics Generative Adversarial Networks (GAN) training but does not require adversarial training. At inference time, the trained noise conditional discriminator is used in a noise-adaptive variant of MMD Gradient Flow. We refer to the training and inference procedures as Diffusion-MMD-gradient flow or \DMMD. We demonstrate competitive empirical performance of the method in unconditional image generation on CIFAR10 dataset. Moreover, we provide theoretical justifications behind the use of this noise-adaptive procedure in the MMD Gradient flow.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel approach, "Diffusion Maximum Mean Discrepancy Gradient Flow" (DMMD), to improve generative modeling by combining Maximum Mean Discrepancy (MMD) with a noise-adaptive gradient flow mechanism. Unlike GANs, DMMD eliminates adversarial training by utilizing a noise-conditional MMD discriminator. DMMD introduces a particle transport technique, adapting MMD as the divergence metric to transport particles from a source distribution to a target distribution.

### Strengths
1. The paper is clearly written and well-organized, tackling a genuine problem and effectively presenting its contributions and findings.

2. The paper establishes a solid mathematical foundation, rigorously linking each section to prior research.

3. The results presented are sufficient to validate the theoretical findings and showcase the effectiveness of the proposed approach.

### Weaknesses
1. While the paper shows promising results, it is still outperformed by standard diffusion models, especially in terms of FID scores. Further work might be necessary to reach SOTA performance on larger datasets like ImageNet.

2. Related to the previous point, the experimental results are primarily limited to smaller datasets (CIFAR10, MNIST, CELEB-A, and LSUN Church), which may not reflect the potential scalability of DMMD to more complex, high-resolution datasets.

3. Although the method avoids adversarial training, the noise-adaptive MMD flow still introduce complexity, which may limit reproducibility.

### Questions
1. As mentioned above, what challenges do you consider in scaling DMMD to larger datasets like ImageNet?
2. What factors limit DMMD's FID performance relative to state-of-the-art diffusion models?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper integrates MMD GAN with the diffusion forward process, introducing a novel generative model framework called DMMD. Through the design of a noise-adaptive MMD gradient flow, this framework aims to reduce the challenges of adversarial training and address the singularity issues found in score-based methods.

### Strengths
S1 - The paper provides a well-formulated background and problem statement, with a theoretically motivated and well-grounded DMMD framework.

S2 - The idea of using an adversarial training-free discriminator based on the diffusion forward process could offer valuable insights to the community.

### Weaknesses
W1 - The framework's absolute performance is a concern, as DMMD shows a significant performance gap compared to DDPM and more modern methods on the selected image generation benchmarks.

W2 - Its broader application potential is limited, with empirical evaluation restricted to small datasets like MNIST and CIFAR.

W3 - The sampling method appears restrictive, requiring reference features from the ground truth dataset to formulate the witness function. This reliance on ground truth features during the sampling process raises questions about the practical applicability of the method in scenarios where such features are not readily available or computationally feasible to obtain.

### Questions
Q1 - The need for dataset features during sampling seems counterintuitive. Do the authors have any insights into potential solutions for addressing this limitation?

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
The article proposes a gradient flow procedure for generative modeling by transporting particles from an initial source distribution to a target distribution, where the gradient field on the particles is given by a noise-adaptive Maximum Mean Discrepancy (MMD) divergence. The noise adaptive MMD is trained on a data distribution corrupted by forward diffusion process. The divergence training procedure is related to discriminator training in Generative Adversarial Networks (GAN), but does not require adversarial training. The article demonstrates competitive empirical performance of the method in unconditional image generation on CIFAR10 dataset.

### Strengths
The article explores the integration of a diffusion process into models based on Maximum Mean Discrepancy (MMD) gradient flow, offering a theoretical foundation for both the discriminator and the sampling process used in MMD-GAN with this diffusion approach. Additionally, it employs a linear kernel for the scalable MMD-GAN to reduce computational complexity. The authors also conduct experiments using other forms of KL divergence, such as KALE divergence, to demonstrate its effectiveness.

### Weaknesses
1. I believe the contribution of this article is inadequate. Previous research has utilized the diffusion process in the discriminator, as noted in this work [1]. However, this article does not provide theoretical proof demonstrating that the MMD GAN can converge to more optimal points when using the diffusion process. Specifically, the paper lacks a convergence analysis that explicitly shows how the diffusion-based discriminator improves the optimization landscape of the MMD GAN, or how it avoids local minima compared to a standard MMD GAN. The authors should provide a rigorous analysis of the optimization dynamics, demonstrating the benefits of the proposed approach in terms of convergence rate and quality of the final solution.

2. Additionally, the effectiveness of MMD Gradient Flow has only been tested on low-resolution datasets, which does not provide sufficient evidence to confirm its overall efficacy. I recommend that the author conduct additional experiments using high-resolution datasets at a resolution of 256x256, specifically on the LSUN and CelebA datasets. These experiments should include evaluations based on the number of metric sampling steps (NFE) and diversity (FID). The current experiments on CIFAR10 do not adequately demonstrate the scalability of the method to more complex data distributions and higher dimensional spaces. The authors need to show that the method can handle the increased computational demands and maintain performance on high-resolution images.

### Questions
1. I recommend that the author conduct additional experiments using a variety of datasets to demonstrate the effectiveness of the DMMD. The results on CIFAR10 are not as impressive as those achieved by state-of-the-art generative models. I also suggest that the author include more comparative experiments with additional relevant works.

2. I am wondering if using vector Z in Eq.(15) to train a generator will result in better outcomes than using it as a sampling process.

3. I am curious about the time required to train the MMD Gradient Flow on the CIFAR-10 dataset. In my experience, training a diffusion-based discriminator takes significantly longer than training the original models. I find that incorporating a diffusion process in gradient flow-based models can reduce the number of accumulated gradient steps. I would like to know if the sampling steps of the DMMD model are influenced by the diffusion process.

4. I wonder how the sampling time changes with increasing data dimensions, such as in 256x256 high-dimensional datasets.

5. Can the MMD Gradient Flow be applied to other tasks such as Super-Resolution or Inpainting? These tasks also involve particle transportation from an initial source to a target distribution.

6. There are writing errors in the article, particularly in Table 4 and Algorithm 2.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a generative model based on the Wasserstein gradient flow of the Maximum Mean Discrepancy (MMD), called DMMD. Given the forward process in diffusion models, the proposed method learns a discriminator between clean data and noisy data. The Wasserstein gradient flow is represented via this discriminator. Therefore, DMMD generates samples by simulating particle trajectories through this flow. DMMD achieves superior performance compared to other discriminator flow and MMD flow baselines in image generation across various datasets.

### Strengths
- This paper is easy to follow.
- This paper suggests an efficient approximate sampling procedure for the linear kernel.
- DMMD is evaluated on various image datasets, such as CIFAR-10, MNIST, CelebA (64x64), and LSUN-Church (64x64).

### Weaknesses
 - My main concern is whether the trajectories of the probability distributions for the forward process $\{ p^{1}_{t} \}_{t \geq 0}$ in the diffusion model and the MMD gradient flow $\{ p^{2}_{t} \}_{t \geq 0}$ coincide. If these trajectories are different, DMMD learns the Wasserstein gradient flow for minimizing $MMD (p^{1}_{t}, p_{data})$. However, during the generation process, the particles follow $\{ p^{2}_{t} \}$ at $ t - \triangle t$. This gradient flow mismatch cannot guarantee that the particles correctly generate the target distribution. Could you clarify this concern?
- The generation process is computationally expensive. How many $N_{s}$ steps are required for each time $t$ during sample generation (Eq 9)?
- For a general kernel, the sampling from DMMD requires access to the training data (Eq 10). Only for linear kernel, this issue can be avoided by saving the average features for each time $t$ (Eq. 12).


### Questions
- In Table 1, do all the other baselines use the same backbone network?
- Could you provide the wall-clock time comparison to demonstrate the computational benefits of approximate sampling in Table 2?
- Is this method applicable to higher-dimensional datasets, such as CelebA-HQ (256x256)?
- Could you provide the potential advantages of this approach compared to other non-adversarial dynamic generative models, such as Flow Matching [1]?

[1] Lipman, Yaron, et al. "Flow matching for generative modeling." ICLR 2023.

### Soundness
2

### Presentation
3

### Contribution
2
