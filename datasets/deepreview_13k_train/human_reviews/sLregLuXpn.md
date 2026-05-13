# On the Analysis of GAN-based Image-to-Image Translation with Gaussian Noise Injection

- Decision: Accept
- Scores: 3, 6, 6

## Abstract
Image-to-image (I2I) translation is vital in computer vision tasks like style transfer and domain adaptation. While recent advances in GAN have enabled high-quality sample generation, real-world challenges such as noise and distortion remain significant obstacles. Although Gaussian noise injection during training has been utilized, its theoretical underpinnings have been unclear. This work provides a robust theoretical framework elucidating the role of Gaussian noise injection in I2I translation models. We address critical questions on the influence of noise variance on distribution divergence, resilience to unseen noise types, and optimal noise intensity selection. Our contributions include connecting $f$-divergence and score matching, unveiling insights into the impact of Gaussian noise on aligning probability distributions, and demonstrating generalized robustness implications. We also explore choosing an optimal training noise level for consistent performance in noisy environments. Extensive experiments validate our theoretical findings, showing substantial improvements over various I2I baseline models in noisy settings. Our research rigorously grounds Gaussian noise injection for I2I translation, offering a sophisticated theoretical understanding beyond heuristic applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a robust theoretical framework for understanding the role of Gaussian noise injection in image-to-image (I2I) translation models. The key contributions of this work include:

(i) Analyzing the influence of noise variance on distribution divergence and resilience to unseen noise types.

(ii) Proposing a method to choose an optimal training noise level for consistent performance in noisy environments.

(iii) Connecting f-divergence and score matching to explain the impact of Gaussian noise on aligning probability distributions.

### Strengths
(i) The writing is clear and easy to follow. The presentation is well-dressed.

(ii) This paper conducts a detailed theoretical analysis in Section 3 to understand the role of Gaussian noise injection in I2I models from the perspective of alignment distribution.

(iii) To validate the conjecture proposed in this paper, the authors conduct sufficient experiments including three types of I2I models, i.e., cat to dog, photo to sketch, and human face super-resolution, covering five types of noise: Gaussian, Uniform, Color, Laplacian, and Salt & Pepper.

### Weaknesses
 (i) This paper has a fatal theoretical flaw, i.e., the authors think too simply and naively about real-world degradations. They set up additive Gaussian noise in the training phase and five synthetic degradations (Gaussian, Uniform, Color, Laplacian, and Salt & Pepper.) in the testing phase. However, the real-world degradations are much more complex and fundamentally different from these degradations. To be specific, as for the noise term, the real-camera raw noise produced by photon sensing comes from multiple sources (e.g., short noise, thermal, noise, dark current noise, etc.) [1, 2, 3] and is further affected by the in-camera signal processing pipeline to become spatio-chromatically correlated. The real-camera noise contains both signal-dependent and -independent terms. However, the authors only consider very naive and simple signal-independent noise types, which is far from their motivation because the degradation patterns they studied simply do not exist in real-world images. Similar to the face super-resolution problem, the blur kernel cannot be explicitly estimated.

[1] CycleISP: Real Image Restoration via Improved Data Synthesis. In CVPR 2020

[2] Variational denoising network: Toward blind noise modeling and removal. In CVPR 2019

[3] Dual adversarial network: Toward real-world noise removal and noise generation. In ECCV 2020

If you want to continue studying this topic, which I think is valuable too, I suggest you to conduct experiments in real degraded images. Here are some suggested datasets:

[4]  A high-quality denoising dataset for smartphone cameras. CVPR 2018

[5] Deep retinex decomposition for low-light enhancement. BMVC 2018

[6] Ntire 2020 challenge on real-world image super-resolution: Methods and results. In CVPRW 2020

(ii) This work does not have any technical contributions. Training with additive Gaussian noise has been studied in the image denoising I2I task for a long time. It is a very common setting. The robustness of noise has also been validated by many prior works. This paper does not propose any new method.

(iii) The idea of adding Gaussian noise and aligning distribution is highly similar to a prior work [7] that also studies real-camera degradations in I2I tasks. There is no discussion or comparison.

[7] Learning to Generate Realistic Noisy Images via Pixel-level Noise-aware Adversarial Training. In NeurIPS 2021.

(iv) Code and pre-trained models are not submitted. The reproducibility cannot be checked.

### Questions
(i) For the theoretical noise analysis part, if considering signal-independent and -dependent noise terms, what will happen to the analysis? How does it change?

(ii) To measure the domain discrepancy, why not using the metric PSNR Gap proposed by the prior work DANet [3]?

[3] Dual adversarial network: Toward real-world noise removal and noise generation. In ECCV 2020

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work provides a robust theoretical framework elucidating the role of Gaussian noise injection in I2I translation models. They address critical questions on the influence of noise variance on distribution divergence, resilience to unseen noise types, and optimal noise intensity selection.

### Strengths
- This paper thoroughly investigates the Gaussian noise in I2I area from both the theory and experiment. 
- Extensive experiments and analysis make the effects of the Gaussian noise more clear to us.

### Weaknesses
 - Analysis of the Gaussian noise has been widely investigated, the authors should give some comparison or analysis about them in related works.

### Questions
- How do you quantize the real and predictive distribution? Furthermore, how do you measure the diff between them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
## Summary
* This paper studies the problem of noise-resistent I2I generation. Particularly, it studies the noise injection approach both theoretically and practically. The paper shows that the joint f-divergence does not change too abruptly when the source is polluted by Gaussian noise. Further, the paper finds optimal noise level for training when the source is Gaussian, and verify their results on Gaussian source and real images.

### Strengths
## Strength
* The result of optimal training level in __Corollary 1__ is useful to practical training of noise resistent generative model, if it is not limited to Gaussian source. It provides theoretical justification to a  intuitative practice.
* The empirical result show that their approach improves the noise-robustness in various cases.

### Weaknesses
## Weakness
* The discussion after __Lemma 1__ only convers non-Gaussian noise, but the majority of experiment is about non-Gaussian source. The gap of source distribution should at least be explicitly discussed in the main text not appendix, if not well addressed. Currently the proof of __Corollary 1__ seems to rely on Eq. 6 of __Lemma 1__, which holds only when the source is Gaussian. If I understand correctly, in that case, it becomes unreasonable to derive the optimal noise level $0.08$ for actual image generation, which is obviously non-Gaussian. If the theory is not connected to the experiment, then this paper becomes a little bit unconvincing. As no new empirical approach is proposed and the empirical results alone is not enough for accepting this paper.

### Questions
## Questions
* Is it possible to extend current theory (__Lemma 1__, __Theorem 2__, __Corollary 1__) to non-Gaussian source with known $\mu,\Sigma$? As Gaussian is the max-entropy distribution with known 1st and 2nd moment, can similar results be obtained?
* Is it possible to extend current theory (__Lemma 1__, __Theorem 2__, __Corollary 1__) to mixture of Gaussian source? As we can approximate any distribution, including natural image distribution with GMM, it would be much better if we can extend the theory to GMM, even for finite mixture. In this way, the distance between the current theory and empirical results on natural image can be reduced.
* Current analysis on joint distribution looks quite general, can it be extended into any conditional GAN, beyond I2I?
* What about more real-life noise, e.g. JPEG compression?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
