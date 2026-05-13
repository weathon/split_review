# Dissecting Arbitrary-scale Super-resolution Capability from Pre-trained Diffusion Generative Models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Diffusion-based Generative Models (DGMs) have achieved unparalleled performance in synthesizing high-quality visual content, opening up the opportunity to improve image super-resolution (SR) tasks. Recent solutions for these tasks often train architecture-specific DGMs from scratch, or require iterative fine-tuning and distillation on pre-trained DGMs, both of which take considerable time and hardware investments. More seriously, since the DGMs are established with a discrete pre-defined upsampling scale, they cannot well match the emerging requirements of arbitrary-scale super-resolution (ASSR), where a unified model adapts to arbitrary upsampling scales, instead of preparing a series of distinct models for each case. These limitations beg an intriguing question: \textit{can we identify the ASSR capability of existing pre-trained DGMs without the need for distillation or fine-tuning?} In this paper, we take a step towards resolving this matter by proposing Diff-SR, a first ASSR attempt based solely on pre-trained DGMs, without additional training efforts. It is motivated by an exciting finding that a simple methodology, which first injects a specific amount of noise into the low-resolution images before invoking a DGM's backward diffusion process, outperforms current leading solutions. The key insight is determining a suitable amount of noise to inject, \ie small amounts lead to poor low-level fidelity, while over-large amounts degrade the high-level signature. Through a finely-grained theoretical analysis, we propose the \textit{Perceptual Recoverable Field} (PRF), a metric that achieves the optimal trade-off between these two factors. Extensive experiments verify the effectiveness, flexibility, and adaptability of Diff-SR, demonstrating superior performance to state-of-the-art solutions under diverse ASSR environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides an interesting way to use the pretrained diffusion model as tool to achieve arbitrary scale super-resolution. The idea of using a pretrained diffusion model to achieve such a task is novel to my knowledge. But the writing of the paper can take some work. The claimed theoretical contribution is not very convincing.

### Strengths
- The task of using pretrained diffusion model for arbitrary scale super resolution is very interesting. 
- the core of the method is very simple : similar to SDEdit, where the low resolution image will be first upsampled and send forward through the diffusion pass before getting denoised. The diffusion model will try to add back the detail. If the noise is chosen properly, then the diffusion model can add detail without losing the structure.

### Weaknesses
 - The writing of the paper can take some more work. There are many places that has the risk of overclaiming. For example, I don’t believe the methodology of this paper is “Pioneering” as it’s very similar to SDEdit and many other diffusion model techniques that add noise to the images before denoising it. I’m not very convinced of the mathematical “guarantee” as the foundation of the analysis seems to be built on equation (3), which is an inequality that can have slacks in between. Since I haven’t checked all the maths in detail I will defer to other reviewer. Some of the observations are already made by prior works (e.g. the message from Figure 1 and Figure 2(b) resembles the message in Figure 2 of the latent diffusion paper). I am not convinced that these observations are first discovered by this paper, so properly citing prior works could be appreciated.
- While it’s a good idea to leverage the pretrained diffusion model for downstream tasks, I believe the most powerful diffusion models are trained with text-conditioning and classfier-free guidance. I probably miss the proper discussion of how the method proposed by this method works with the state-of-the-art diffusion models of that kind.

### Questions
- “recovering LR images by generating visual details” do you mean recovering high-resolution images from LR images?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Diff-SR, a novel approach using pre-trained diffusion generative models (DGMs) for arbitrary-scale image super-resolution (ASSR) tasks. The key idea behind Diff-SR is to inject a specific amount of noise into the low-resolution (LR) image before feeding it into the DGM's backward diffusion process. By controlling the noise injection level, Diff-SR can adapt a single DGM to handle diverse ASSR tasks without requiring fine-tuning or distillation. Through theoretical analysis, the authors introduce the concept of Perceptual Recoverable Field (PRF) to determine the optimal noise level for different scales. Experiments on standard datasets demonstrate Diff-SR's effectiveness over competing methods.

### Strengths
- Interesting idea of utilizing noise injection to activate ASSR capacity in pre-trained DGMs, avoiding costly retraining or distillation.
- Great analysis of the impact of noise injection, leading to the valuable concept of PRF for quantifying model capacity.
- Superior performance over baselines on various metrics and datasets, especially for high upsampling rates.
- Qualitative results exhibit excellent recovery of textures and details.
- Great ablation studies validate key designs like adapting noise levels and DGM architectures.

### Weaknesses
 - In my understanding, the claimed arbitrary-scale image super-resolution refers to the process that resizes the arbitrary LR input to 256*256  before restoring it. This claim may not be considered a novel approach. Many existing super-resolution methods can adopt a similar process, and this approach resembles the way blind restoration methods work.
- One notable drawback of this approach is its relatively high computational cost, primarily because it heavily relies on the iterative sampling process of diffusion generative models (DGMs) without employing approximations or early stopping techniques.
- The ablation studies provided in the paper seem to be narrowly focused on variations in model architecture, rather than rigorously examining different aspects of the methodology itself. A more comprehensive set of ablation studies that investigate various parameters of the approach could provide a more in-depth evaluation of its strengths and weaknesses, as these Diffusion based models usually have obviously larger parameters than this one (500 vs 35).
- Recent diffusion based super-resolution methods are missing. It is better to give analyses with them. The related works are not enough.
- The quantitative results presented in Table 1 appear inconsistent with published results for the competing methods. For instance, the PSNR reported for SwinIR on the Set5 benchmark for the x2 task is 37.925, while the original paper reports 38.42. This discrepancy raises concerns about the comparability of the experimental setup.
- The paper does not discuss the similarity of the proposed approach with DifFace, which also adjusts fidelity and perception through the number of steps (noise variance). This omission is significant as both approaches share the core idea of injecting noise into the LR image (or using a CNN to predict an HR image first) and then manipulating the noise level to achieve a trade-off between fidelity and perception.

### Questions
- I note that the authors focus on image super-resolution tasks only. I wonder whether it can be used in real-world LR images, which usually contain different types of degradation, like noise, blur, and compression.
- Diff-SR contains 35.71 M parameters, which is obviously smaller than the competing diffusion based methods. In this task, do the model parameters have an obvious effect on the performance?
- The quantitative results in Table 1 seem to be not consistent with the results shown in the original papers. Do they adopt the same experiment settings?
- For LR images under the same downsampling scale, do they have the same parameters to balance the texture fidelity and semantic signature? If so, why? As the LR images which have the same downscale operation, may have different levels of blur. I think the trade-off parameters should also relate to the blur degree.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed Diff-SR for arbitrary-scale super-resolution (ASSR) using one pre-trained Diffusion model without any additional training efforts. To achieve arbitrary-scale super-resolution, this paper proposed to add a specific amount of noise to LR images before the Diffusion model backward diffusion process. Besides, a metric Perceptual Recoverable Field has been proposed for achieving the optimal trade-off between fidelity and realness. Overall, this paper is well-written and easy to understand.

### Strengths
1. This paper presented a new perspective that extends a pre-trained diffusion model into an arbitrary-scale super-resolution by adding a specific amount of noise to LR images before the diffusion model backward diffusion process. The idea is interesting.
2. This paper proposed a metric Perceptual Recoverable Field for achieving the optimal trade-off between fidelity and realness.

### Weaknesses
Please refer to the Questions.

### Questions
1. Since the proposed method is for arbitrary-scale super-resolution, it is important to provide the quantity results comparison of arbitrary-scale such as 1.6X, 2.7X, 3.5X, and 4.5X. Also, the visual comparison of different scales comparison of the proposed method on the same image is also important to evaluate this work.
2. It mentioned that the used pre-trained diffusion model is 256*256. How does this model achieve arbitrary-scale super-resolution? For example, the low-resolution image is sized 100*100, how can we achieve 3.5X super-resolution?
3. Please give a reference for the value of noise level in an interval of 0.1.
4. Can the proposed method extend in real-world arbitrary-scale super-resolution? 
5. Adding different noise levels when dealing with different scales, the higher noise means lower fidelity. When facing larger scale super-resolution, that means very low fidelity. Is there a big visual change between X2 and X4 results?
6. How does the proposed method maintain the trade-off between fidelity and realness? 
7. In Line 22 of Page 2, this paper mentions high-level signature of generated content. What does it mean? 
8. In Line 3 of Page 5, should the low-resolution image be high-resolution image? Otherwise, it is hard to understand this sentence.

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
In this paper, the authors introduce a new paradigm to achieve scale-arbitrary SR by exploiting pre-trained diffusion generative models without any additional training overhead. Specifically, a specific amount of noise is first injected into the low-resolution images and then the resultant images are fed to diffusion generative models to generate the SR results. The authors present theoretical analyses and propose a perceptual recoverable field to achieve the trade-off between the fidelity and the realness. Extensive experiments show that the proposed method produces state-of-the-art performance on several benchmark datasets.

### Strengths
+ This paper is well-motivated and well-written.
+ Endowing existing diffusion generative models with the capablity of scale-arbitrary SR without additional overhead is interesting.

### Weaknesses
 - As this paper aims to dissect arbitrary-scale SR capability, experiments should be conducted on arbitrary-scale SR tasks other than integer and symmetric scale factors (i.e., assymmetric SR).
- If I understand correctly, the proposed method is not only limited to arbitrary-scale SR tasks, but can be extended to arbitrary-degradation SR tasks. In my opinion, LR images with different scale factors are referred to as images with different degradation models such that different amounts of noise are required to recover the missing details. Consequently, I wonder more results on arbitrary-degradation SR.
- For fair comparison with previous perception-oriented methods, metrics like LPIPS should be included for evaluation.
- As diffusion generative models require several iterations to produce promising results and usually computationally expensive, inference time should also be reported such that the readers can be clearly aware of the cost of the proposed method.

### Questions
please see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
