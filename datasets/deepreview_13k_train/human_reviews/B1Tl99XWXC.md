# Efficient Transfer Learning in Diffusion Models via Adversarial Noise

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Diffusion Probabilistic Models (DPMs) have demonstrated substantial promise in image generation tasks but heavily rely on the availability of large amounts of training data. Previous works, like GANs, have tackled the limited data problem by transferring pre-trained models learned with sufficient data. However, those methods are hard to be utilized in DPMs since the distinct differences between DPM-based and GAN-based methods, showing in the unique iterative denoising process integral and the need for many timesteps with no-targeted noise in DPMs. In this paper, we propose a novel DPMs-based transfer learning method, TAN, to address the limited data problem. It includes two strategies: similarity-guided training, which boosts transfer with a classifier, and adversarial noise selection which adaptive chooses targeted noise based on the input image. Extensive experiments in the context of few-shot image generation tasks demonstrate that our method is not only efficient but also excels in terms of image quality and diversity when compared to existing GAN-based and DDPM-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Diffusion Probabilistic Model (DPM)-based transfer learning method, i.e., to address the limited data problem. Specifically, similarity-guided strategy is designed to enhance the few-shot transfer learning and an adversarial noise selection method is proposed to address the underfitting problem during a limited number of iterations. Both qualitative and quantitative results demonstrate the effectiveness of the proposed method.

### Strengths
The paper is well-written with clear description.

It analyzes the limitations of DPM-based transfer learning and presents reasonable solutions.

### Weaknesses
How does the pre-trained DPMs come and if the proposed method can be applied on other pre-trained DPMs for transfer learning?

If the authors could provide visualizations on the selected noise for deeper analysis on its effect?

The step number used to perform the projected gradient descent (PGD) in Eq.(7)?

### Questions
Please refer to the Weaknesses for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Generative models can leverage large-scale datasets to learn and produce diverse high-quality outputs. To overcome the limitations of this approach, methods for transfer learning from models trained on extensive datasets have been studied. However, diffusion-based generative models, unlike directly step-wise generative models like GANs, generate samples through the diffusion of noises over a large number of steps, making it challenging to apply conventional transfer learning methods. Therefore, in this paper, a method called TAN, which utilizes adversarial noises to effectively transfer learning to diffusion models. 

Generating high-quality and diverse results with generative models comes with the challenge of obtaining a large amount of training data and stabilizing the training process. In this regard, transfer learning and few-shot learning research are important, yet relatively less explored. Previous studies attempted transfer learning by matching the results of intermediate steps of DDPM, but they led to distorted transfer and overfitting issues. the proposed approach, incorporating similarity-guided training and adversarial noise selection techniques, yielded well-transferred results.

### Strengths
This paper proposes simple yet effective methods, namely similarity-guided training and adversarial noise, for transfer learning with diffusion models. 

The proposed methods yielded high-quality results and were demonstrated through various experiments. 

The paper presents equations 4 and 5, which induce the Kullback-Leibler divergence between the source and target models during the reverse process of the diffusion model. 

This divergence is defined as similarity and utilized to control transfer learning.

The proposed similarity-guided approach by the authors not only induces overall transfer for the target domain but also considers the characteristics of the diffusion generative model. 

By utilizing adversarial noise selection, the method allows the noise to fit more accurately, resulting in high-quality output and addressing the issues faced by previous methods. 

The paper presents a cohesive and easily understandable writing flow, effectively conveying the underlying arguments and the rationale of the study.

### Weaknesses
I think it would be better if there is deeper analysis regarding the similarity or adversarial noise in the proposed method. It would be even better if there were various experiments and analyses to examine the semantic effects of the redefined reverse step compared to the vanilla model. I am curious about the author's insights beyond mathematically deriving the KL divergence between the source and target domains, exploring different aspects.

### Questions
1. I am curious if this method can be applied not only to transfer learning or few-shot learning but also to fields such as domain adaptation or domain control.

2. I wonder if the adversarial noise in this method can assist in achieving higher-quality results in the training of general DDPMs.

3. I'm curious if this method has been experimented with in domains other than 2D images.

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
The paper presents an innovative approach to transfer learning in diffusion models with sparse target data. To tackle the limited data problem, the authors propose TAN, a new diffusion-based method including two strategies: similarity-guided training, which aims to enhance transfer with a classifier, and adversarial noise selection to improves the efficiency of training process. The authors conducted extensive experiments in the context of few-shot image generation tasks and demonstrated that their method is not only efficient but also excels in terms of image quality and diversity when compared to existing GAN-based and DPM-based methods.

### Strengths
1.	This paper is well written, easy to follow and conducts a lot of experiments  with comprehensive analysis, demonstrating the effectiveness of the proposed approach.
2.	The design of the similarity-guided training and adversarial noise is intuitive and reasonable.

### Weaknesses
1.	The graphical representation of the results doesn't clearly demonstrate a significant improvement compared to other existing methods.
2.	Regarding the approach to adversarial noise selection for Eq. 7 and Eq. 8, could you provide further clarification on the choice of minimizing the maximum Gaussian noise at step t? Additionally, since optimizing for maximum noise can be particularly challenging, could you delve deeper into how the multi-step variant of PGD with gradient ascent ensures the performance of this methodology? Expanding on these aspects would significantly enhance the comprehensibility and value of this paper.
3.	The paper lacks an in-depth exploration of the implications for time and GPU memory conservation when utilizing the supplementary adaptor module and the process of adversarial noise selection. To enhance the overall quality of the paper, I suggest providing a more comprehensive elucidation, along with relevant graphical representations, regarding the efficient training procedures involving these components.

### Questions
My main concerns and questions lie in the weaknesses. The author should discuss them in detail.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, authors propose a novel DPMs-based transfer learning method, TAN, to address the limited data problem. It includes two strategies: similarity-guided training, which boosts transfer with a classifier, and adversarial noise selection which adaptive chooses targeted noise based on the input image. As illustrated in the paper, authors think they haved achieved SOTA results compared with prior works.

### Strengths
1.The paper introduces a binary classifier to guide the training and an adversarial way to generate noises, this idea is interesting.
2.The exploration of overfitting in Fig.1 is helpful for the few-shot learning of generative models.

### Weaknesses
1.The quantitative results reported for different methods have large overlap when factoring in the std values, in general, the boldfacing of average values when ignoring the stds is not the best practice. The reported standard deviations are substantial, indicating a high degree of variability in the results. This makes it difficult to ascertain if the differences in average values are statistically significant. The authors should provide a more rigorous statistical analysis, such as p-values or confidence intervals, to support their claims of improvement. The current presentation of results is misleading, as the bolding of average values suggests a clear advantage that is not supported by the overlapping standard deviations.
2. I have read several related works and find almost all of them show use samples transferred from FFHQ as qualititative results. I found that the results of this paper on FFHQ are only shown in Supp. I cannot figure out the improvement of this method compared with DDPM-PA on those results. Actually, I think DDPM-PA shows better results. The lack of qualitative results on the FFHQ dataset in the main paper makes it difficult to assess the method's performance on a standard benchmark. The qualitative results in the supplementary material are not sufficient to demonstrate a clear improvement over DDPM-PA, and in some cases, the results appear to be inferior. The authors should include a more thorough qualitative comparison in the main paper, with a focus on the FFHQ dataset, to better illustrate the strengths of their method.
3. Results in this paper should be compared with more modern text-to-image methods based on diffusion models, including textual inversion, dreambooth, domainstudio. If this method is only applied to traditional methods, it's not convincing enough. The paper's focus on traditional methods limits its relevance in the context of recent advancements in text-to-image generation. The authors should compare their method with more recent techniques, such as textual inversion, dreambooth, and domainstudio, to demonstrate its competitiveness in the current landscape. The absence of such comparisons makes it difficult to evaluate the practical significance of the proposed approach.
4. In LSUN Church --> Landscape drawings, it seems that DDPM-PA carries out a style transfer process, this work fails to get samples of church actually. Therefore, I wonder if this comparison is fair. For FFHQ --> babies and sunglasses, this work and DDPM-PA share the same target. However, I think DDPM-PA performs better. The comparison between the proposed method and DDPM-PA on the LSUN Church to Landscape drawings task is questionable. The fact that DDPM-PA appears to perform style transfer rather than few-shot image generation raises concerns about the fairness of the comparison. The authors should clarify the specific goals of the transfer learning task and ensure that all methods are evaluated on the same criteria. Furthermore, the qualitative results for FFHQ to babies and sunglasses suggest that DDPM-PA performs better, which contradicts the authors' claims.

### Questions
My main concern is about the performance and applicable scenarios. See the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
