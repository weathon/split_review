# Solving Video Inverse Problems Using Image Diffusion Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Recently, diffusion model-based inverse problem solvers (DIS) have emerged as state-of-the-art approaches for addressing inverse problems, including image super-resolution, deblurring, inpainting, etc. 
However, their application to video inverse problems arising from spatio-temporal degradation remains largely unexplored due to the challenges in training video diffusion models.
To address this issue, here we introduce an innovative video inverse solver that leverages only image diffusion models.
Specifically, by
drawing inspiration from the success of the recent decomposed diffusion sampler (DDS), 
our method treats the time dimension of a video as the batch dimension of image diffusion models and solves spatio-temporal optimization problems within denoised spatio-temporal batches derived from each image diffusion model.
Moreover, we introduce a batch-consistent diffusion sampling strategy that encourages consistency across batches by synchronizing the stochastic noise components in image diffusion models. 
Our approach synergistically combines batch-consistent sampling with simultaneous optimization of denoised spatio-temporal batches at each reverse diffusion step, resulting in a novel and efficient diffusion sampling strategy for video inverse problems.
Experimental results demonstrate that our method effectively addresses various spatio-temporal degradations in video inverse problems, achieving state-of-the-art reconstructions.
Project page: \small \textsf{\url{https://svi-diffusion.io}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a video inverse problem solver using pre-trained image diffusion models. Specifically, the method treats the time dimension of a video as the batch dimension of image diffusion modles and solves spatial-temporal optimization problems. Additionally, a batch-consistent sampling strategy is developed to ensure temporal consistency. Experimental results demonstrate the model’s effectiveness in handling various spatio-temporal degradations with significant speed improvements over existing methods.

### Strengths
1. This paper offers an innovative approach to video inverse problems by leveraging pre-trained image diffusion models for video tasks, eliminating the need for computationally intensive video diffusion model training.
2. The method is computationally efficient, with VRAM savings that make it feasible for deployment in lower-resource environments.

### Weaknesses
1. The paper lacks comparison with recent state-of-the-art video processing methods beyond diffusion-based approaches, which would provide a more comprehensive benchmark. Specifically, the absence of comparisons against non-diffusion based methods limits the assessment of the proposed method's relative performance. For example, comparisons with established optical flow based methods or recurrent neural network based video restoration techniques would be beneficial.
2. The evaluation is limited to the DAVIS dataset, potentially restricting insights into the model’s performance on a broader range of video types and characteristics, such as high-frame-rate and highly dynamic videos. The DAVIS dataset, while useful for benchmarking, may not fully represent the diversity of real-world video content. Testing on datasets with varying frame rates, motion complexities, and scene types is crucial to validate the robustness of the proposed method.
3. The degradations used in the experiments are synthesized through point spread functions (PSF), which may not fully capture real-world scenarios. Further testing on established video restoration datasets, such as GoPro for deblurring and other widely-used datasets for denoising and decompression, would help more thoroughly assess the model’s performance across diverse degradation types. The use of synthetic PSFs may not accurately reflect the complex and often spatially varying degradations encountered in real-world videos. Evaluating the method on datasets with real-world degradations would provide a more realistic assessment of its practical applicability.

### Questions
1. How does the model perform on high frame rate video datasets? Could it be adapted to conduct video frame interpolation task?

### Soundness
3

### Presentation
3

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
This paper introduces a method to solve video inverse problems using image diffusion models instead of complex video models. By treating video frames as image batches, the authors achieve temporal consistency across frames through a batch-consistent sampling strategy. They also apply a multi-step optimization to improve accuracy, allowing for efficient and coherent video reconstruction without needing specialized video model training.

### Strengths
1. The paper utilizes image diffusion models to reduce the need for extensive video model training, leading to faster processing times.

2. The paper proposes a batch-consistent sampling strategy that ensures coherent frame generation, enhancing the visual quality of reconstructed videos.

3. The paper conducts experiments on various video inverse problems, such as deblurring and super-resolution, with improved reconstruction accuracy.

### Weaknesses
1. The ablation experiments in this paper could be more comprehensive. For instance, it remains unclear whether the choice of different image pre-trained models affects the final results and whether the proposed algorithm yields consistent conclusions across various pre-trained models. Specifically, the paper does not explore how the performance varies when using different diffusion model architectures (e.g., DDPM, DDIM, or LDM) or different pre-training datasets. This is crucial because the generalization capability of the method is directly tied to the robustness of the underlying image diffusion model.

2. The paper lacks testing on more complex real-world datasets, such as videos with low bitrate compression or older films. The current experiments are limited to relatively clean datasets, which do not fully represent the challenges encountered in practical scenarios. This includes handling artifacts from compression, noise from older recordings, or complex motion patterns that may not be well-represented in the training data. The absence of these evaluations limits the practical applicability of the proposed method.

3. The image quality in the manuscript is low, please provide a high-quality version.

### Questions
Can the authors provide specific examples of failure cases where your proposed method does not perform as expected? 
Additionally, it is well-known that metric evaluations, even subjective ones, may not accurately reflect people's actual viewing experiences. Can the authors provide a user study to further compare the different methods?

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
4

### Summary
This paper tackles video inverse problems by leveraging pretrained image diffusion models. The authors introduce a batch-consistent sampling scheme that maintains temporal consistency while introducing temporal diversity from the conditioning steps. Experimental results demonstrate the effectiveness of this approach in preserving quality across frames.

### Strengths
1. The presentation is clear and intuitive, with well-defined formulations and symbols.
2. The proposed method is efficient and effective for video inverse problems. Experimental settings are clearly explained, and the results validate the effectiveness of the sampling strategy in improving temporal coherence.
3. The ablation study is comprehensive and provides a clear understanding of the role of each component.

### Weaknesses
Incremental Novelty: The main contribution of this paper lies in addressing the batch consistency problem by applying a 2D pretrained diffusion model. The paper highly dependent on established techniques for inverse problems, including Tweedie denoising and multi-step conjugate gradient (CG) for frame-dependent perturbation. While the results are impressive, the technical contribution appears relatively incremental.

### Questions
Why is the sampling approach different between the proposed method and other methods (e.g., 20 steps for DDIM vs. 1000 steps for NFE)? Would baseline methods with 20-step DDIM show a notable performance drop?

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
4

### Summary
The authors introduce a method to restore videos by using an pretrained image-based diffusion model.
The videos are degraded by spatio-temporal blurring, downsampling and missing data, and as far as I understand the degradation model A(X) is assumed known. The focus of the paper is on the prior on X obtained via a pre-trained diffusion model. However, in the case of videos one would need a corresponding pre-trained video diffusion model. Such models are today available, albeit very challenging to train due to the required large model, data dimensionality and compute resources. The authors suggest to use a pre-trained image diffusion model, which is much easier to train, and propose a method to adapt it to videos. The essential idea is to use the same noise used during the diffusion steps across all frames so that their denoising is more consistent. The authors show that this simple change combined with the gradients to match the data term (specifically, the conjugate gradients -- which are inspired by prior work) is sufficient to obtain temporally consistent restored videos.

### Strengths
The presentation is clear and self-contained. The proposed method is original as far as I know in the context of video restoration. The main originality is in the use of the same additional noise across all the frames at each step of the inverse diffusion process. This change combined with the data term constraint (and the use of conjugate gradients from prior work) seems to be sufficient to restore videos and yield sota performance on different video restoration tasks.

### Weaknesses
This method has been demonstrated for the case where the degradation operator is given, ie, we are
working in the non-blind video restoration case.  If I misunderstood this point, please clarify this in the rebuttal.
I am assuming that A(X) is fully known and used to compute the conjugate gradients.
My main critique is that in practice it is very difficult to have access to such operator in the case of real videos. One could argue that having these operators is at the same level of complexity of solving the restoration task. Typically, one argues that focusing on the prior term by working in the non-blind case of the restoration task is still quite useful. However, this holds only if one can show that the prior could be 
used effectively also in the blind case. My main concern is that this may not hold in the proposed method.

The proposed novelty is that one should use the same additional noise samples for all the restored video frames. I wonder if this would work also in the blind case, ie, when also one needs to simultaneously recover the degradation operator. Basically, if the proposed method would only work in the non-blind case, then I would say that this is not a very significant contribution. If instead we could know that the method would also hold in the blind case, then it would be more significant (ie, the implicit temporal constraint through the same-noise sampling would be strong enough to work in the general case).

Intuitively, my concern is that the noise sampling choice implicitly guides the frame restorations to be very similar to each other, but does not provide any hint on how the temporal dynamics should be. In fact, an image diffusion model cannot impose this type of constraint. The component that imposes some temporal constraint seems to be just the degradation operator. So if this operator is unknown/to be estimated, I wonder how well all the rest would work.

In the literature there is quite a bit of past work on dealing with unknown degradation operators (the so-called _blind_ case). These methods differ from the one proposed here, as they typically use a dataset to train a model in a supervised fashion to map a blurry/degraded video to a sharp one. The advantage is that they learn to generalise to new degradation operators at test time. It would be important to understand how this approach compares to such methods and to highlight their pros and cons.
I think it would be more important to have such comparisons than to compare to even older ADMM methods.
If needed I can provide a few references on such recent blind video restoration methods, but it is straightforward to look them up.

### Questions
Based on the weaknesses above I have the following questions:
1) Is your method based on complete knowledge of the degradation operator?
2) If yes to 1) could you provide insights on how well your proposed video prior would work in the blind restoration case?
3) If your proposed video prior has other applications other than in the more practical blind restoration case, could you present these applications/motivations?
4) Could you clarify how your method would compare to prior blind video restoration work and why it is a better framework?

### Soundness
3

### Presentation
3

### Contribution
2
