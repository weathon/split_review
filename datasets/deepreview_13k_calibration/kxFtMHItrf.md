# Reti-Diff: Illumination Degradation Image Restoration with Retinex-based Latent Diffusion Model

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Illumination degradation image restoration (IDIR) techniques aim to improve the visibility of degraded images and mitigate the adverse effects of deteriorated illumination. Among these algorithms, diffusion model (DM)-based methods have shown promising performance but are often burdened by heavy computational demands and pixel misalignment issues when predicting the image-level distribution. To tackle these problems, we propose to leverage DM within a compact latent space to generate concise guidance priors and introduce a novel solution called Reti-Diff for the IDIR task. Reti-Diff comprises two key components: the Retinex-based latent DM (RLDM) and the Retinex-guided transformer (RGformer). To ensure detailed reconstruction and illumination correction, RLDM is empowered to acquire Retinex knowledge and extract reflectance and illumination priors. These priors are subsequently utilized by RGformer to guide the decomposition of image features into their respective reflectance and illumination components. Following this, RGformer further enhances and consolidates the decomposed features, resulting in the production of refined images with consistent content and robustness to handle complex degradation scenarios. Extensive experiments show that Reti-Diff outperforms existing methods on three IDIR tasks, as well as downstream applications. The code will be released.
  \keywords{Illumination degradation image restoration \and Latent diffusion model \and Retinex theory}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes to use diffusion models in conjunction with a transformer model to perform image restoration of poorly lit images. The proposed method is evaluated in 4 different settings and shown the merits.

### Strengths
+ The paper looks at an important problem of illumination restoration in images which is quite relevant for downstream tasks.

### Weaknesses
 - The use of intrinsic image decomposition through Retinex is a dated idea. There are several better methods available that have neither been explored nor used. https://www.elenagarces.es/projects/SurveyIntrinsicImages/ 

- The work lacks novelty as it uses diffusion to decompose the image and a transformer to reconstruct it. The method has hardly any contribution. 

- Though the evaluation of the method is done for several conditions, the process is not built correctly with any conviction, which is a downer. 

- The method uses a couple of downstream applications to demonstrate the merits: detection and segmentation. The tasks are very easy to generalize, given the power of deep networks without illumination enhancement. The work could not convince the reader about the merit of this approach.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces Reti-Diff, a novel latent diffusion model-based framework tailored for Illumination Degradation Image Restoration (IDIR). It leverages Retinex theory to improve image quality by using two primary components: the Retinex-based Latent Diffusion Model (RLDM) and the Retinex-guided Transformer (RGformer).

### Strengths
1. The paper combined the Retinex model and data-driven methods since the first effort of RetinexNet. 
2. Experiments are sufficient.
3. Code is a plus.

### Weaknesses
1. For the low-light enhancement task, I want to see more results on LIME, NPE, MEF, DICM and VV. Since these datasets do not have ground truth, then is more fair to justify the effectiveness. Any visual results?

2. Missing citations of real-world low-light enhancement methods,
[1] Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression
[2] Enhancing Visibility in Nighttime Haze Images Using Guided APSF and Gradient Adaptive Convolution

3. LDM is slow in inference.
The paper lacks a discussion on the computational complexity and runtime efficiency of the proposed model.

### Questions
1. How does the proposed method handle edge cases such as extreme noise or heavy color distortions, which may not follow typical low-light degradation patterns?

2. Is there a recommended strategy for tuning the noise variance parameters in the latent diffusion process for optimal performance across varied image qualities?

3. How does Reti-Diff perform in scenarios with extreme lighting conditions, such as overexposed or underexposed images, which may challenge the reliability of Retinex-based priors?

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
This paper introduces the Retinex-based LDM solution, Reti-Diff, for illumination degradation image restoration (IDIR) tasks, aiming to generate visual fidelity results while decreasing computational burdens. In specific, Reti-Diff proposes RLDM to acquire Retinex priors and then leverage RGformer to guide the image restoration process with the extracted priors, resulting in the production of refined images with consistent content and robustness to handle complex degradation scenarios. Extensive experiments demonstrate that Reti-Diff outperforms existing methods on three IDIR tasks, as well as downstream applications.

### Strengths
1. This paper proposes RLDM to extract Retinex priors, and RGformer to integrate the priors, ensuring robustness and generalization in complex illumination degradation scenarios.
2. This paper is well organized.
3. Experiments on four IDIR tasks verify the superiority, efficiency, and generalizability of the method and demonstrate that Retinex priors can serve as a plug-and-play strategy to improve the quality of existing methods.

### Weaknesses
1. More related works are expected to be discussed, for example, low-light image enhancement via clip-fourier guided wavelet diffusion[1]. 
2. Why do the authors choose to use a cross-attention mechanism to model the Retinex theory?
3. The authors are encouraged to highlight the motivation for extracting Retinex priors and explain why using a diffusion model to extract the priors. 
4. Additionally, in the experiment, the authors are expected to verify if the Retinex priors perform better than the sole RGB prior and if the diffusion model can serve as a better predictor than the common network structure.
5. In Phase 2, the authors first train the RLDM before conducting joint training with RGFormer. In the ablation study, the authors provide results without the joint training stage, but they do not compare the results of removing the independent RLDM training stage. Would it yield better results if RLDM, RPE, and RGFormer were trained directly together?
6. Some typo errors are expected to be fixed, for example, ZR and ZL in Line 90 in the Supp.

### Questions
Can the authors analyze the reason for the failure cases? Will this be because of the failure of one of the Retinex priors or because of the failure of RGformer to integrate the priors?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focuses on designing a latent diffusion model that utilizes the Retinex priors to address the issue of illumination degradation. To be detailed, the authors developed a module for estimating the Retinex priors from the low-quality and high-quality images and a Transformer backbone for the image enhancement. These components work in synergy to restore images. The authors provide extensive experiments to demonstrate the effectiveness and advancement of their method.

### Strengths
1. The coupling of latent diffusion model with the Retinex priors and Transformer is intriguing. And exploring the robustness of network with the Retinex theory in illumination degradation scenarios is meaningful.
2. The proposed method, compared to existing diffusion models in image enhancement, demonstrates relatively high computational efficiency and lower resource consumption while maintaining strong performance.
3. The experimental validation in the paper is thorough, particularly regarding downstream tasks and evaluations across multiple datasets.
4. The paper is well-organized, clearly written, and easy to understand.

### Weaknesses
1. The paper utilizes diffusion models to get the latent Retinex priors, but further analysis is needed to explore the relationship between diffusion models and the designed latent Retinex priors. (insights)
2. The mechanisms by which the Retinex priors operate need to be clarified. Ensuring the consistency of the Retinex theory in the latent space is a question worthy of investigation. Further deepening the results-oriented experimental conclusions in the mechanistic level would improve the quality of study.
3. The design of the method results in a significant reliance on the modeling of Retinex theory. However, there seems to be little discussion on the reliability of Retinex decomposition.

### Questions
1. What’s the motivation of using the latent diffusion model to generate the Retinex priors? What are its advantages? Would it be more efficient and reliable to use a single Transformer or CNN network for it?
2. DiffIR [1] achieves image restoration using a similar prior. What would be the difference if the entire image enhancement process were simply treated as the prior, compared to using the Retinex-based model as the priors? Demonstrating the necessity of the latent Retinex priors would be more valuable.
3. About the Retinex priors, how does it perform in terms of prior feature errors when exchanging features between the ground truth and low-light images? In addition to the qualitative and quantitative evaluations of the enhancement results, it would be beneficial to conduct an assessment at the prior level as well.
4. It is recommended to perform a convergence analysis of using the latent Retinex priors. For example, showcasing the changes in loss or evaluation metrics on the training and validation sets would be beneficial.
5. Given the introduction of the Retinex priors, does the proposed method heavily depend on the reliability of Retinex decomposition? Since this is an ill-posed problem, it would be helpful to provide an explanation or at least a few qualitative results of the Retinex decomposition to support this claim.
6. How does the method perform in extreme conditions, specifically when the Retinex decomposition fails? (Extremely bright light and strong shadows) 

Although there are some concerns, they do not detract from the fact that this is a relatively well-researched paper. I am inclined to provide a positive opinion in this stage.

[1] Xia, Bin, et al. "Diffir: Efficient diffusion model for image restoration." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Soundness
3

### Presentation
4

### Contribution
3
