# Spectral Compressive Imaging via Unmixing-driven Subspace Diffusion Refinement

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Spectral Compressive Imaging (SCI) reconstruction is inherently ill-posed, offering multiple plausible solutions from a single observation. Traditional deterministic methods typically struggle to effectively recover high-frequency details. Although diffusion models offer promising solutions to this challenge, their application is constrained by the limited training data and high computational demands associated with multispectral images (MSIs), complicating direct training. To address these issues, we propose a novel Predict-and-unmixing-driven-Subspace-Refine framework (PSR-SCI). This framework begins with a cost-effective predictor that produces an initial, rough estimate of the MSI. Subsequently, we introduce a unmixing-driven reversible spectral embedding module that decomposes the MSI into subspace images and spectral coefficients. This decomposition facilitates the adaptation of pre-trained RGB diffusion models and focuses refinement processes on high-frequency details, thereby enabling efficient diffusion generation with minimal MSI data. Additionally, we design a high-dimensional guidance mechanism with imaging consistency to enhance the model's efficacy. The refined subspace image is then reconstructed back into an MSI using the reversible embedding, yielding the final MSI with full spectral resolution. Experimental results on the standard KAIST and zero-shot datasets NTIRE, ICVL, and Harvard show that PSR-SCI enhances visual quality and delivers PSNR and SSIM metrics comparable to existing diffusion, transformer, and deep unfolding techniques. This framework provides a robust alternative to traditional deterministic SCI reconstruction methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a novel framework named PSR-SCI aimed at enhancing CASSI reconstruction. The framework consists of a initial predictor(MST or DAUHST), a unmixing-driven reversible spectral embedding module to decomposes the MSI into subspace images and spectral coefficients, and a pre-trained RGB latent diffusion models (SD-2.1) refinement processes. Furthermore, the authors implement a high-dimensional guidance mechanism that ensures imaging consistency. Experiments on the KAIST, NTIRE, ICVL, and Harvard dataset demonstrate that PSR-SCI enhances visual quality and achieves PSNR and SSIM metrics.

---
After rebuttal: I read the authors response and have raised my score.

### Strengths
1. The proposed method has higher performance than previous diffusion-based methods on CASSI reconstruction.
2. The method costs less time in both training and inference time than previous diffusion-based methods.

### Weaknesses
1. The novelty of this approach is limited, as spectral decomposition and refinement using pre-trained RGB diffusion models have previously been introduced in the spectral image restoration field [1]. The specific implementation of spectral decomposition and the refinement process, while demonstrating performance gains, does not introduce a fundamentally new concept beyond existing work in the field.
2. The method relies heavily on the initial prediction network. Although the authors claim robustness for the proposed framework, it may not perform well on unseen optical setups (such as different masks, noise, and number of channels). The framework depends on initial reconstruction results from a pre-trained CASSI reconstruction network. If the pre-trained network does not perform adequately on a new system with different optical settings (a common issue in CASSI reconstruction) the framework’s effectiveness diminishes. For example, PSR-SCI-T (initial predictor: MST) and PSR-SCI-D (initial predictor: DAUHST) demonstrate this, with weaker predictors leading to inferior reconstruction results. The performance delta between different initial predictors suggests a potential lack of true robustness.
3. The experiments presented are insufficient. The proposed method should be evaluated with recent state-of-the-art predictors, such as [2], DPU-9stg, and SSR-L. Additionally, comparisons with similar 'refinement' frameworks, such as [3], would further validate its performance. The absence of these comparisons makes it difficult to assess the true contribution of the proposed method against the current state-of-the-art.

### Questions
1. Why are the SSIM metrics omitted in Table 2?
2. The number of abundance maps A in spectral unmixing should correspond to the number of endmembers. Why is an up-sampled 3-channel feature map used instead? Is this solely for compatibility with the RGB pre-trained model? The URSe module seems more like a data dimension reduction or latent space encoding operation, with little relevance to spectral unmixing

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a new two-stage method, namely a predict-and-subspace refine (PSR-SCI) framework, using the diffusion model for snapshot compressive imaging reconstruction. In the first stage, an inexpensive predictor generates a rough MSI approximation. Then in the second stage, a spectral unmixing-driven subspace learning module is employed to reduce the dimensionality. Eventually, a diffusion model is fine-tuned to enhance the high-frequency details. There are three technical contributions:

(i) Given the complexities of spectral unmixing models, a reversible decomposition network is introduced to implement spectral subspace learning while maintaining high reversibility.

(ii) The diffusion generation is facilitated by low- and high-frequency decomposition.

(iii) A high-dimensional guidance strategy is introduced for fine-tuning subspace diffusion, enhancing the effectiveness of guidance within the subspace.

### Strengths
(i) The novelty is good and interesting. The big idea of partitioning the reconstruction into two stages is cool. It seems like the latent space diffusion models. The first stage of prediction and decomposition is like the embedding process of VAE and this process is highly reversible. Besides, using the frequency domain decomposition (low- and high-frequency) to facilitate the generation process is also very fancy. It matches the nature of spectra. It is very exciting to have this work in the community of SCI reconstruction.

(ii) The performance is solid. As compared in Table 1, Figures 6, 8, and 9. The proposed method PSR-SCI not only outperforms the state-of-the-art end-to-end methods by large margins but also achieves better visual results. Compared to the SOTA diffusion-based method DiffSCI, the proposed PSR-SCI is 2.86 dB higher! It is great progress of the diffusion-based method in SCI. This work even contains the results of Pseudo-RGB on the RGB-to-HSI reconstruction task. 

(iii) The presentation is well-dressed. The figure of the pipeline looks clear. I can easily see the workflow of the proposed framework. The table of quantitative comparisons is also neat. The style of this table is from the series work of MST, MST++, CST, DAUHST, etc. I like it very much. The writing also looks good and easy to follow.

(iv) Code and the reconstruction results have been submitted,

### Weaknesses
 (i) Some modifications and explanations should be added. For example, why do you want to use an inexpensive predictor to produce an initial HSI instead of directly reconstructing the HSI results from the noisy measurements? The current explanation lacks a detailed justification for this design choice. It is not clear why the low-frequency information cannot be extracted directly from the measurements. Besides, since the process looks like the Stablediffusion - latent space diffusion. So I think it is better to discuss your work with it to highlight the differences and your contributions. The connection to latent diffusion models needs to be made explicit, detailing how this work differs in terms of architecture, training, and application to SCI reconstruction.

(ii) The experiments are insufficient now. The ablation study only has a visual study (Figure 10). This is far from satisfactory. A more comprehensive ablation study is needed to demonstrate the effectiveness of each technical contribution. The current visual study does not provide quantitative evidence to support the claims about the individual contributions of the reversible decomposition network, the low- and high-frequency decomposition, and the high-dimensional guidance strategy. The lack of quantitative ablation makes it difficult to assess the true impact of each component.

(iii) The computational cost and memory usage of different methods are not reported in Table 1. I cannot judge the efficiency of the proposed method and compare it with other algorithms. It is essential to include metrics such as the number of parameters, floating-point operations per second (FLOPS), and inference time to provide a complete picture of the method's efficiency. Without these metrics, it is difficult to assess the practical viability of the proposed approach.

### Questions
Some parts may need more explanation. For example,

In Algorithm1 (Line 270 - 287), the return value $\mathcal{A}_{diff}^h$ is fed into the VAE decoder to obtain the final reconstructed hyperspectral images. However, for the latent space diffusion, the VAE is trained to decode normal RGB images. Can it directly work on hyperspectral images? Or did you fine-tune it or something like that?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The proposed Predict-and-Unmixing-driven Subspace-Refine framework (PSR-SCI) addresses the challenges in Spectral Compressive Imaging (SCI) reconstruction, particularly the difficulty of recovering high-frequency details from ill-posed inverse problems. By leveraging a cost-effective prediction module, unmixing-driven reversible spectral embedding, and pre-trained RGB diffusion models, PSR-SCI demonstrates superior visual quality and competitive performance compared to state-of-the-art diffusion, transformer, and deep unfolding approaches, providing an alternative to traditional deterministic methods.

### Strengths
The problem this work aims to solve is crucial. Recovering high-frequency details from ill-posed inverse problems is always challenging for both traditional optimization-based methods and end-to-end deterministic networks. Leveraging the powerful generative capabilities of models pre-trained on large RGB datasets and making them transferable to spectral imaging is a promising approach to address this challenge.

In addition, I like the idea of using reversible spectral unmixing to bridge spectral image and RGB image. 

The novelty is enough, to address the high-frequency reconstruction challenge in spectral compressive imaging, this paper solved several problems and makes 4 key contributions: (1) the introduction of a spectral unmixing-driven predict-and-subspace refine strategy, offering improved perceptual quality and efficiency; (2) the inclusion of a reversible decomposition module, tackling the ill-posed nature of spectral unmixing; (3) focusing diffusion generation on high-frequency components, reducing training data requirements and accelerating fine-tuning; and (4) employing high-dimensional guidance with SCI imaging consistency to enhance robustness.

Moreover, this method shows nice results on the real SCI dataset, which is a hard case for existing methods.

### Weaknesses
In lines 296-365 of the main paper and Section A.3 of the appendix, most of the mathematical derivations are easy to follow. However, some detailed notations are unclear in the context, which reduces readability.

The motivation for designing the reversible unmixing module is not sufficiently clear. For example, why not use an SVD-based method? What advantages does the proposed unmixing module offer?

### Questions
(1) For the reversible unmixing module, although the experiments show that it is lightweight and efficient, I am curious how it compares with SVD, PCA, or band selection-based methods.

(2) It seems the hyperparameters, scale $s$and timestep $T$, shown in Fig. 12, are sensitive to the model's reconstruction accuracy. How do they influence the visual quality of the reconstructed image? The PSNR is not always a reliable metric for measuring image quality, especially for spectral images.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel framework called Predict-and-Unmixing-driven Subspace Refinement (PSR-SCI) for Spectral Compressive Imaging (SCI) reconstruction. SCI is an inherently ill-posed problem where traditional methods often struggle to recover high-frequency details. The proposed PSR-SCI framework starts with a cost-effective predictor that provides an initial estimate of the multispectral image (MSI). It then introduces an unmixing-driven reversible spectral embedding module to decompose the MSI into subspace images and spectral coefficients. This decomposition allows the adaptation of pre-trained RGB diffusion models, focusing refinement on high-frequency details efficiently, even with minimal MSI data. Additionally, the authors design a high-dimensional guidance mechanism with imaging consistency to enhance the model's effectiveness. The refined subspace image is reconstructed back into the MSI using the reversible embedding, yielding the final MSI with full spectral resolution. Experimental results on standard datasets like KAIST and zero-shot datasets such as NTIRE, ICVL, and Harvard demonstrate that PSR-SCI enhances visual quality and achieves PSNR and SSIM metrics comparable to some existing diffusion, transformer, and deep unfolding techniques.

### Strengths
1. The proposed high-dimensional guidance mechanism with imaging consistency is a noteworthy contribution that could enhance the model's performance.

2. The method is evaluated on both standard datasets and zero-shot datasets, showing competitive performance in PSNR and SSIM metrics compared to existing methods.

### Weaknesses
1. The motivation for using the unmixing-driven spectral embedding decomposition is not entirely clear. The paper does not sufficiently justify why this specific decomposition method is suitable for the SCI problem or how it leads to superior performance in terms of convergence speed, recovery accuracy, or error reduction. While the approach is innovative, its superiority over existing methods is not well-established.

2. The claim that there is limited training data available for MSIs compared to RGB images is questionable. Recent works have utilized large-scale MSI datasets to train diffusion models effectively (e.g., "HSIGene: A Foundation Model For Hyperspectral Image Generation," https://arxiv.org/abs/2409.12470, https://github.com/LiPang/HSIGene). This undermines the premise that data scarcity necessitates their approach.

3. The proposed method appears to have a high number of parameters and computational demands. It is unclear whether the performance gains are due to the novel method or simply the result of using a much larger model compared to others. Methods like DAUHST and MST use models with millions of parameters, whereas the proposed method uses billions. This raises concerns about the practicality and efficiency of the approach, especially considering the longer inference times.

4. Despite the innovative approach, the performance of PSR-SCI on the KAIST dataset is reported as 38.14dB PSNR, which is lower than some recent works that achieve PSNR values exceeding 39dB (e.g., PADUT [ICCV 2023], RDLUF-MixS2 [CVPR 2023], and "Latent Diffusion Prior Enhanced Deep Unfolding for Snapshot Spectral Compressive Imaging" [ECCV 2024]). This suggests that the proposed method may not offer a significant improvement over existing techniques.

### Questions
1. Could the authors elaborate on why the unmixing-driven spectral embedding decomposition is particularly suitable for SCI reconstruction? How does it contribute to faster convergence, higher recovery accuracy, or error reduction compared to other methods?

2. What is the total number of parameters in the proposed model, and how does it compare to other methods? Could the authors provide a detailed analysis of the computational complexity and inference times? How practical is the method for real-world applications given its computational demands?

3. Given that recent works have successfully trained diffusion models on large-scale MSI datasets, how do the authors address the claim of MSI data scarcity? Does this affect the necessity or uniqueness of the proposed approach?

4. To what extent does the high performance of PSR-SCI stem from the large number of parameters and depth of the model, as opposed to the proposed methodology itself? Have the authors conducted experiments to isolate these factors?

### Soundness
3

### Presentation
2

### Contribution
2
