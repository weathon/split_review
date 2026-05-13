# One Step Diffusion-based Super-Resolution with Time-Aware Distillation

- Decision: Reject
- Scores: 5, 6, 5, 5, 6

## Abstract
Diffusion-based image super-resolution (SR) methods have shown promise in reconstructing high-resolution images with fine details from low-resolution counterparts. However, these approaches typically require tens or even hundreds of iterative samplings, resulting in significant latency. Recently, techniques have been devised to enhance the sampling efficiency of diffusion-based SR models via knowledge distillation. Nonetheless, when aligning the knowledge of student and teacher models, these solutions either solely rely on pixel-level loss constraints or neglect the fact that diffusion models prioritize varying levels of information at different time steps. To accomplish effective and efficient image super-resolution, we propose a time-aware diffusion distillation method, named TAD-SR. Specifically, we introduce a novel score distillation strategy to align the data distribution between the outputs of the student and teacher models after minor noise perturbation. This distillation strategy enables the student network to concentrate more on the high-frequency details. Furthermore, to mitigate performance limitations stemming from distillation, we integrate a latent adversarial loss and devise a time-aware discriminator that leverages diffusion priors to effectively distinguish between real images and generated images. Extensive experiments conducted on synthetic and real-world datasets demonstrate that the proposed method achieves comparable or even superior performance compared to both previous state-of-the-art (SOTA) methods and the teacher model in just one sampling step.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a method to distill a super-resolution diffusion model into one step, by combining 3 losses: direct regression loss, GAN loss, and a modified score distillation loss. The main contribution is the score distillation part.

### Strengths
1. The paper targets at an important problem of distillation of SR diffusion models. While diffusion distillation is a popular research area, it is interesting to see some insight particularly designed for SR models

2. The paper introduces a novel technique to reduce the bias of the score estimate of generated samples in SDS, which particularly fits in the insights from SR.

3. Empirical results shows promising improvements.

### Weaknesses
1. The biggest concern is insufficient baselines. The method compare against a large number of non-diffusion based methods or diffusion based iterative methods, but it lacks comparisons against the most closely related methods: other diffusion distillation algorithms. This method distill a pre-trained SR diffusion model into one step with some specific design for SR, but there are many distillation methods designed for general diffusion models, such as consistency model and the family of distribution matching distillation. The authors should run controlled experiment with the same teacher model with different algorithms to emphasize the relative advantage. For example, personally I found CM works well in distilling SR model into one step, and DMD and its variant can distilled the more complicated T2I model into one step. Their relative performance on SR diffusion is what we really care.

2. It seems like the method requires teacher model to generate clean samples, which can be computationally expensive, even if you pre-compute the data off-line. 

3. The background of SDS and how to reduce the bias is unclear to readers without prior knowledge.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a time-aware diffusion distillation method named TAD-SR, which enables the student model to focus on high-frequency image details at smaller time steps and eliminates inherent biases in score distillation sampling. The authors also design a time-aware discriminator that fully leverages the teacher model’s knowledge by injecting time information to differentiate between real and synthetic data. Experimental results demonstrate the effectiveness and efficiency of the proposed method.

### Strengths
* The paper is well-written.
* Experimental results demonstrate that the proposed method achieves state-of-the-art performance with high efficiency.

### Weaknesses
* The evaluation is not comprehensive. Some image fidelity metrics are lacking, such as PSNR and SSIM on ImageNet-Test, where the competing methods ResShift and SinSR all reported.

* The improvement over the previous single-step distillation method SinSR is minor. Considering that LPIPS—a crucial metric for perceptual quality—is very important, the increase from 0.221 to 0.227 represents a big drop in quality and is not slight.

* The ablation study examines only the presence or absence of the discriminator, neglecting other important aspects—for example, the number of scales used in the discriminator.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This  paper proposes a time-aware diffusion distillation method, TAD-SR, to achieve one-step SR inference with competitive performance. It applies a score distillation strategy make efforts to eliminate the inherent bias SDS focus more on high-frequency image details when sampling at small time steps. A time-aware discriminator is also designed to differentiate between real and synthetic data.

### Strengths
1.	This paper proposes a time-aware distillation method that accelerates diffusion-based SR models into a single inference step.
2.	The writing of this paper is good.

### Weaknesses
See the questions.

### Questions
1.	Since this is a distillation method, please compare more diffusion-based distillation SR methods, like OSEDiff [1], quantitatively and qualitatively. (Why are the comparison with diffusion-based distillation SR methods missing in some tables and figures?)

2.	Since you claim that TAD-SR can achieve better reconstruction of high-frequency information, please present the spectrum images of the LR input, GT, baseline methods’ reconstruction, and TAD-SR’s reconstruction. Examine the differences in the high-frequency patterns around the periphery of the spectrum images.

3.	Please compare the inference time of TAD-SR and baseline methods.

4.	In Fig. 10 and Fig. 12, TAD-SR’s results appear to contain many fragmented particles, which make the images look sharper at first glance; however, this is actually due to the addition of pseudo-textures or unnatural details. Could you explain the cause of this? For instance, could it be due to the adversarial loss?

5.	Following the concern raised in my 4th question, could you please provide more qualitative  comparisons that contain fine details or small textures?

[1] Rongyuan Wu, et al. One-Step Effective Diffusion Network for Real-World Image Super-Resolution. 


(I apologize for my previous review comments, which were not fully aligned with your article due to a heavy review workload. I am providing corrected feedback here, and if your response addresses these points well, I will consider adjusting the score.)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces TAD-SR, a time-aware diffusion distillation method designed to enhance the efficiency and performance of diffusion-based image super-resolution (SR) models. By aligning the student and teacher models with the proposed score distillation strategy and incorporating a time-aware discriminator to distinguish real and synthetic data across varying noise levels, TAD-SR achieves strong performance across several metrics.

### Strengths
1. The topic is interesting and meaningful.
2. Extensive experiments demonstrate that TAD-SR achieves results comparable to or exceeding multi-step diffusion models, espeically in some non-reference IQA metrics.

### Weaknesses
1. The organization of the paper needs improvement, as it is challenging to clearly understand the core idea. For instance, Fig. 2, which aims to illustrate the paper's motivation, has a caption that provides limited information.

2. The paper lacks essential metrics, such as PSNR and SSIM, to evaluate model fidelity. As shown in previous works, there is a trade-off between PSNR, SSIM, and CLIPIQA, MUSIQ. Reporting only LPIPS and non-reference IQA metrics is insufficient to demonstrate performance. Both the main results and ablation studies should include these metrics.

3. Although I understand that StableDiffusionXL also employs adversarial loss, it appears less elegant to me due to the inherent limitations of GANs.

4. In addition to the difficulty of assessing performance without PSNR and SSIM, the reported improvements seem marginal compared to existing methods.

### Questions
The motivation is not clear. If the proposed method wants to achieve one-step SR, why it is important for student model to learn how to deal with the intermediate steps?

Will increase the inference steps contribute to the improvement of the performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author proposes a time-aware diffusion distillation method, named TAD-SR, where a novel score distillation strategy is introduced to align the score functions between the outputs of the student and teacher models after minor noise perturbation. Such distillation strategy eliminates the inherent bias in score distillation sampling (SDS) and enables the student models to focus more on high-frequency image details by sampling at smaller time steps.  Furthermore, a time-aware discriminator is designed to mitigate performance limitations stemming from distillation, which distinguishes the diffused distributions of real and generated images under varying noise disturbance levels by injecting time information.

### Strengths
1. The proposed distillation strategy is simple and straightforward, which can eliminate the inherent bias in score distillation sampling (SDS) and enable the student models to focus more on high-frequency image details. 
2. The proposed time-aware discriminator can differentiate between real and synthetic data, contributing to the generation of high-quality images.
3. The presentation of this work is written well and is easy to read.

### Weaknesses
1. It is confusing which is the final output of the model when inference, z_0^{stu} or z ̂_0^{stu}? It is not clearly indicated in Figure 4. Please explicitly state in the text and figure.
2. The authors should clarify if the teacher model is used at all during inference, or if it is only used during training. If I understand correctly, only the student model samples one step, and then the teacher model is used later to sample multiple steps to get the final clean latent, so the model performance relies heavily on the performance of the teacher model, and is not exactly efficient.
3. What is the purpose of setting the weighting function (ω = 1/CS )? Please provide intuition for why this weighting function was chosen, and what effect it has on the training process or results. 
4. In order to eliminate the dependence of the proposed method on the teacher model of ResShift, the relevant ablation experiments should be conducted by replacing the different teacher models to validate the effectiveness of the proposed method.
5. The experiments lack comparisons with the most relevant distillation methods, including DMD, DEQ[1], DFOSD[2], etc. Among them, DMD, a new diffusion model, utilizes similar score distillation techniques to the proposed HSD. DEQ and DFOSD are both efficient and relevant diffusion models, which require one-step diffusion distillation or even no distillation.
6. In the experimental section, the authors compare many GAN and transformer-related methods. However, the proposed method is a diffusion model and should be compared with the most relevant diffusion models to validate its efficiency, especially accelerated diffusion models, including OSEDiff[3], DPM++[4], Unipc[5], etc. 
7. The authors claim that the method is designed to accomplish effective and efficient image super-resolution, but did not include a complexity comparison of the different methods (including parameters, sampling steps, running time, MACs, etc.), which is crucial for diffusion models. Please provide a Table to compare these computational complexity metrics with the key baselines.
8. Are there any limit conditions for using the method? The author should discuss and analyze the limitations of the proposed method. It is recommended to add a discussion of a discussion of potential limitations or where the proposed method might not perform as well.

References

[1] Geng Z, Pokle A, Kolter J Z. One-step diffusion distillation via deep equilibrium models[C]. Advances in Neural Information Processing Systems, 2024.

[2] Li J, Cao J, Zou Z, et al. Distillation-free one-dtep diffusion for real-world image super-resolution[J]. arxiv preprint arxiv:2410.04224, 2024.

[3] Wu R, Sun L, Ma Z, et al. One-step effective diffusion network for real-world image super-resolution[J]. arxiv preprint arxiv:2406.08177, 2024.

[4] Lu C, Zhou Y, Bao F, et al. Dpm-solver++: Fast solver for guided sampling of diffusion probabilistic models[J]. arxiv preprint arxiv:2211.01095, 2022.

[5] Zhao W, Bai L, Rao Y, et al. Unipc: A unified predictor-corrector framework for fast sampling of diffusion models[C]. Advances in Neural Information Processing Systems, 2024.

### Questions
See the Weakness part. 
The author should carefully describe the details of the method to enhance the readability and clarity of the paper. In addition, the comparison of the most relevant methods (including complexity comparison) should be added to clarify the innovation and effectiveness of the method, and the advancement of the method should be proved through relevant experiments.

I tend to improve the score if the author can solve my concerns.

### Soundness
2

### Presentation
3

### Contribution
2
