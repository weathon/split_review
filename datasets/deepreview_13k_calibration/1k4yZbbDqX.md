# InstaFlow: One Step is Enough for High-Quality Diffusion-Based Text-to-Image Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Diffusion models have
revolutionized text-to-image generation with its exceptional quality and creativity. However, its multi-step sampling process is known to be slow, often requiring tens of inference steps to obtain satisfactory results. 
Previous attempts to improve its sampling speed and reduce computational costs through distillation have been unsuccessful in achieving a functional one-step model.
In this paper, we explore a recent method called Rectified Flow~\citep{liu2022flow, liu2022rectified}, which, thus far,
has only been applied to small datasets. 
The core of Rectified Flow lies in its \emph{reflow} procedure, which straightens the trajectories of probability flows, refines the coupling between noises and images, and facilitates the distillation process with student models. 
We propose a novel text-conditioned pipeline to turn Stable Diffusion (SD) into an ultra-fast one-step model, in which we find reflow plays a critical role in improving the assignment between noises and images.
Leveraging our new pipeline, we create, to the best of our knowledge, the first one-step diffusion-based text-to-image generator 
with SD-level image quality, achieving
an FID (Fréchet Inception Distance) of $23.3$ on MS COCO 2017-5k, surpassing the previous state-of-the-art technique, progressive distillation~\citep{meng2022distillation}, by a significant margin ($37.2$ $\rightarrow$ $23.3$ in FID). 
By utilizing an expanded network with 1.7B parameters, we further improve the FID to $22.4$. 
We call our one-step models \emph{InstaFlow}.
On MS COCO 2014-30k, InstaFlow yields an FID of $13.1$ in just $0.09$ second, the best in $\leq 0.1$ second regime, outperforming the recent StyleGAN-T~\citep{sauer2023stylegan} ($13.9$ in $0.1$ second).
Notably, the training of InstaFlow only costs 199 A100 GPU days.

\begin{figure}[!h]
    \vspace{-5pt}
    \centering
    \includegraphics[width=0.95\textwidth]{figs/n_step.png}
    \caption{
    InstaFlow is a high-quality one-step text-to-image model derived from Stable Diffusion~\citep{rombach2021highresolution}.
    Within $0.1$ second, it generates images with similar FID as StyleGAN-T~\citep{sauer2023stylegan} on MS COCO 2014. The whole fine-tuning process to yield InstaFlow is pure supervised learning and costs only 199 A100 GPU days. 
    }
    \label{fig:enter-label}
    \vspace{-35pt}
\end{figure}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper successfully demonstrates the use of RECTIFIED FLOW to linearize the model's sampling trajectory, followed by distillation to enhance the sampling speed of the ODE model. It proposes a method for distilling Text-Conditioned flow models, showcasing a variety of ablation studies and results across multiple settings.

### Strengths
The results of this paper are truly captivating. It manages to generate images of impressive quality with just one or two steps. The quality showcased in the figures is highly satisfying. In addition, the paper provides a detailed account of various experiments and the corresponding performance metrics, which adds greatly to its value.

### Weaknesses
While the paper demonstrates impressive results, it appears to be a straightforward application of RECTIFIED FLOW. I was unable to discern any clear novelty in the algorithms or methods presented. If I'm wrong please kindly let me know the difference.

The model that claims to operate in 1 step actually resembles a configuration of two UNets linked together, and thus feels closer to a 2-step process. Additionally, when the refined model from SDXL is not applied, the results show a noticeable degradation in high-frequency details.

### Questions
Given that RECTIFIED FLOW is trained based on its own trajectory, are there any issues that arise from this approach?

Methods like DDIM inversion also seem like they could be applicable in a flow-based context. I am curious about the results in cases where a small number of steps, close to 2, are used.

### Soundness
4 excellent

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends a recently introduced framework of rectified flows to the distillation of the coupling learned by the pretrained diffusion model, e.g. Stable Diffusion (SD). 
While the recent work [1] reported the results of experiments on unconditioned generation (on CIFAR-10, LSUN, AFHQ, MetFace and CelebA-HQ datasets) as well as on img2img translation, the current submission focuses on text-conditional generation.
The paper reconfirms that a "rectified" ODE produces an easier target for 1-step distillation. 

The main contribution is the InstaFlow model which essentially is a multi-step pipeline which takes a pretrained SD model as an input and outputs a 1-step generative model. 
In addition, a novel type of architecture called Stacked U-Net is presented.
As the conducted evaluation shows, InstaFlow outperforms recent baselines such as Progressive Distillation of SD and StyleGAN-T in terms of FID and CLIP score.

[1] Liu et al. Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow. In ICLR, 2023.

### Strengths
The writing style of the paper is extremely clear.
It provides a very good introduction to the framework of rectified flows for a reader without deep knowledge of the topic, and overall the manuscript is quite self-contained. 
The conducted experiments provide a sufficient support for the motivation of the method. I find the evaluation thorough enough.
The results achieved in the paper are definitely interesting for the broad community of ML researchers and practitioners due to the achieved combination of required computational resources for the model training and inference and its performance.

### Weaknesses
1. First of all, this submission is more an extension of the previous work [1] rather than an independent work. The novelty of the presented ideas is definitely limited: all parts of the pipeline were actually introduced previously, and the submitted work applies the same pipeline to the coupling learned by SD model instead of independent coupling of noise and images. The proposed results are definitely valuable for applications. However, they look more like a technical exercise on top of the [1]. Overall, I find this work too incremental although helpful for practitioners.

2. While the idea of Stacked U-Net is interesting, the paper lacks the study if this type of architecture is actually better than increasing the depth (or the number of channels) of the conventional U-Net model. Specifically, the paper does not provide any ablation studies to justify the design choice of the Stacked U-Net. It is unclear whether the performance gains are due to the specific stacked structure or simply due to an increase in the overall number of parameters.

3. The paper provides the results for latent models only. Taking the empirical nature of this work into account, I suggest adding any of the open cascaded models to the comparison to see, e.g. DeepFloyd IF [2]. The absence of comparison with cascaded models limits the scope of the evaluation and makes it difficult to assess the true performance of the proposed method in the context of state-of-the-art text-to-image generation.

### Questions
1. Please, address the limitations discussed above.
1. The training pipeline described in the Appendix D, looks pretty complicated. 
    1. Why was it necessary to change the batch size (step 2), and why wasn't more common learning rate tuning applied instead? 
    1. What is the reasoning behind switching from L2 to LPIPS objective (step 4) instead of training with a combination of L2 and perceptual loss from the very beginning of the distillation phase? 
    1. How were switching points for steps 2 and 4 selected?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the InstaFlow, an application that applies the Rectified Flow to Stable Diffusion. The authors implement the rectified flow technique on Stable Diffusion and subsequently distill a one-step diffusion model from the rectified model. The rectified method makes the trajectories of Stable Diffusion straighter, thus making it much easier to distill the multi-step model to fewer or even one-step model.

### Strengths
The paper is well-written, and the experiments conducted are both sufficient and convincing. The InstaFlow achieves amazing performance (1-step inference with reasonable quality in approximately 0.09 seconds).

### Weaknesses
While this model demonstrates impressive performance, it does involve a trade-off between inference speed and generation quality. From the supplementary document of InstaFlow, we can still observe various artifacts, which may be inherited from the 2-Rectified Flow (e.g., many faces are already distorted in the rectified model). Specifically, the distortions are not limited to faces, but also include other fine-grained details such as textures and complex object boundaries, which appear blurred or fragmented. Furthermore, the one-step distillation process, while achieving remarkable speed, seems to amplify some of the existing artifacts present in the rectified flow model, suggesting that the distillation process may not be entirely robust to imperfections in the teacher model. Nevertheless, as the authors also mentioned, this model can be used for generating quick reviews, and then larger models can be employed for further generating high-quality images.

### Questions
I don't have further questions regarding the experiments since they're satisfactory to me.
However, given that this work involves practical applications, I encourage the authors to consider sharing the source code and pretrained models, as this would undoubtedly be of great benefit to the community.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to address the limitations of diffusion models in text-to-image (T2I) generation, particularly their slow multi-step sampling process. The authors propose a novel one-step generative model derived from Stable Diffusion (SD) using a method called Rectified Flow. The core of Rectified Flow is its reflow procedure, which improves the coupling between noises and images and facilitates the distillation process.

### Strengths
1. Well organized and clarified.
2. The contribution is great. Making the conditional diffusions work with one or very few steps will greatly boost the development of diffusion community. 
3. The comparison experiments are carefully and fairly set up, and I appreciate that.

### Weaknesses
I have several questions about this paper, and I hope the authors to clearly clarify them.

1. **Storage Overhead**: In my opinion, it seems that either the distillation process or the reflow process actually requires us to create a relatively large (noise, image) pair dataset in advance, which would cause the additional storage overhead.

2. **Intrinsic Difference between the so-called distillation and reflow process**: The distillation step aims to make the model predict the same as target computed by the ODE process of Stable Diffusion at the zero-timestep. While the reflow process seems to only change to make the distillation applied to all possible timesteps. 

3. **Noise Scheduler**: The noise scheduler of SD requires a normal diffusion noise scheduler. The reflow requires the "linear" (I call it "linear" just for convenience) scheduler. Wouldn't that cause trouble? Besides, the SD Unet requires time embedding, what time embedding do you use?

4. Why do you choose to predict "x1-x0" instead of "x1-xt"? Do you have any considerations about this?

### Questions
I tend to accept the paper, considering its theoretical and technical contributions. However, I have several questions about this paper and hope the authors answer them for me to make the final decision.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
