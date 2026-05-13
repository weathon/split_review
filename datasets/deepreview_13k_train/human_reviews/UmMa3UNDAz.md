# EfficientDM: Efficient Quantization-Aware Fine-Tuning of Low-Bit Diffusion Models

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Diffusion models have demonstrated remarkable capabilities in image synthesis and related generative tasks.
Nevertheless, their practicality for low-latency real-world applications is constrained by substantial computational costs and latency issues.
Quantization is a dominant way to compress and accelerate diffusion models, where post-training quantization (PTQ) and quantization-aware training (QAT) are two main approaches, each bearing its own properties.
While PTQ exhibits efficiency in terms of both time and data usage, it may lead to diminished performance in low bit-width settings. On the other hand, QAT can help alleviate performance degradation but comes with substantial demands on computational and data resources.
To 
capitalize on 
the advantages while avoiding their respective drawbacks,
we introduce a data-free, quantization-aware and parameter-efficient fine-tuning framework for low-bit diffusion models, dubbed EfficientDM, to achieve QAT-level performance with PTQ-like efficiency.
Specifically, we propose a quantization-aware variant of the low-rank adapter (QALoRA) that can be merged with model weights and jointly quantized to low bit-width.
The fine-tuning process distills the denoising capabilities of the full-precision model into its quantized counterpart, eliminating the requirement for training data.
To further enhance performance, we introduce scale-aware LoRA optimization to address ineffective learning of QALoRA due to variations in weight quantization scales across different layers.
We also employ temporal learned step-size quantization to handle notable variations in activation distributions across denoising steps.
Extensive experimental results demonstrate that our method significantly outperforms previous 
PTQ-based
diffusion models while maintaining similar 
time and data efficiency.
Specifically, there is only a marginal $0.05$ sFID increase when quantizing both weights and activations of LDM-4 to 4-bit on ImageNet $256\times256$.
Compared to QAT-based methods, our EfficientDM also boasts a $16.2\times$ faster 
quantization
speed with comparable generation quality, rendering it a compelling choice for practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a quantization-aware variant of low rank adapter and a data-free training scheme  for fine-tuning quantized diffusion models. It introduces scale-aware techniques to optimize the weight quantization parameters. For activation quantization, this paper employs a separate activation quantization step-size parameter for each denoising time step. With tuning the low rank weight parameter adapters, this method can achieve  image generation performance comparable to QAT based methods with much lower fine-tuning cost. It firstly achieves FID score as low as 6.17 on conditional image generation on ImageNet 256x256 dataset with 4bit-weight, 4bit-activation diffusion model.

### Strengths
* This paper is the first to achieve very good image generation performance with W4A4 diffusion models and W2A8 diffusion models.

* This paper introduces **low rank adapter** and **distillation loss** to fine-tune quantized diffusion models and achieve good results with relatively low cost than QAT methods.

### Weaknesses
 * The experimental results listed in this paper are confusing and do not align well. The effectiveness is not very well proved. Specifically, the FID score of the W4A4 model (6.17) in Table 2 is significantly lower than the FP model (11.28), which is counterintuitive for a quantized model. This discrepancy raises concerns about the reliability of the reported results and the overall effectiveness of the proposed quantization method. Furthermore, the FID score of the W8A8 model (11.38) being comparable to the FP model is also unexpected, given that quantization usually leads to some performance degradation. The paper does not provide a sufficient explanation for these inconsistencies.

* This paper proposes **TLSQ**, which is quite similar to TDQ in [1]. TDQ is applicable to diffusion models with both continuous time and arbitrary discrete time steps . The paper should clarify the number of time steps used in TLSQ and discuss the settings. The lack of clarity regarding the specific number of time steps used in TLSQ and how it relates to the overall denoising process makes it difficult to assess the novelty and practical applicability of the proposed method. It is crucial to understand whether the method is optimized for a specific number of steps or if it can generalize to different sampling schedules.


### Questions
* In Table 2, the FID score of W4A4 model (6.17) is much lower than FP model (11.28) and W8A8 model (11.38) is comparable to FP model. Is there any possible explanation for that? And in the paper "High-Resolution Image Synthesis with Latent Diffusion Models", FID score of conditional generation on ImageNet 256x256 is 3.60, which is much lower than 11.28, why is there a gap? In the Appendix.A Table.A, the unconditional image generation on LSUN dataset, the FID score of W4A4 model is much worse than the FP model, how to explain the gap in these two set of experiments?

* Table 3 shows the ablation study results. Does the **QALoRA** use LSQ algorithm to fine-tune the low rank adapter parameters and quantization step-size parameters?  

* Are there any results on using LSQ method on quantized diffusion models on dataset other than Cifar10?

* In **Data-free fine-tuning for diffusion models** part, is $\mathbf{x}_t$ in Eq(7) sampled from Gaussion noise with an FP model?

* In **Variation of activation distribution across steps** part, it proposes to assign a separate step size parameter for activation quantization in each denoising time step, and the results shown in Table 2 are obtained from 20-step sampling. Is the total time steps fixed to 20 for the fine-tuning. Is the data-free fine-tuning in Eq(7) fixed for 20 steps?

* In Sec3.2 Eq(3), the quantization scheme has three parameters, $l, u, s$, are they all trainable? If so, is it optimized with LSQ [2] or LSQ+ [3] algorithm?


[1] High-Resolution Image Synthesis with Latent Diffusion Models.

[2] Learned step size quantization.

[3] LSQ+: Improving low-bit quantization through learnable offsets and better initialization.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a data-free fine-tuning framework tailored for low-bit diffusion models. The key approach involves freezing the pretrained diffusion model and fine-tuning a set of quantization-aware LoRA variants (QALoRA) by employing knowledge distillation to capture the denoising capabilities in the full-precision model. The paper also introduces two techniques, namely scale-aware optimization and learned step-size quantization, to address challenges related to ineffective learning of QALoRA and variations in activation distributions. Extensive experiments highlight that EfficientDM achieves performance levels comparable to QAT methods while preserving the data and time efficiency advantages of PTQ methods.

### Strengths
1.	Achieving QAT-level performance with PTQ-level efficiency is significant and promising for low-bit diffusion models.
2.	The idea of the QALoRA is novel. Compared to QLoRA, it avoids extra floating-point calculations during inference.
3.	The results are encouraging and demonstrate the strong performance of EfficientDM under various bit-widths.
4.	The paper is well-organized and easy to follow. The supplementary material provides additional experimental results and comprehensive visualization results, which enhance the overall credibility of the work.

### Weaknesses
1.	It would be beneficial to evaluate EfficientDM over recent text-to-image diffusion models, such as Stable Diffusion.
2.	Recent work TDQ [1] also introduces a quantization method that adjusts the quantization scale at various denoising steps. The differences should be discussed.
3.	Formulating the gradient of LoRA weights can help elucidate the reasons for ineffective learning of QALoRA.
4.	Figure 2: the notation for scale-aware optimization is inconsistent with Eq. (8), please fix it.

### Questions
See weaknesses

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a data-free and efficient Quantization-Aware Training (QAT) method for diffusion models. For efficient QAT, it introduces the Quantization-Aware Low-Rank Adapter (QALoRA), which combines LoRA and QAT. The paper extends the LSQ QAT method a little to the Temporal LSQ method, which learns different scale factors for different time steps to handle the activation distribution difference across steps. The experimental of image diffusion and latent diffusion models on CIFAR-10, LSUN, and ImageNet demonstrates that this method can significantly outperform previous PTQ methods when doing W4A4 and W2 quantization.

### Strengths
- Applying QAT to diffusion models to achieve better quantization performance is reasonable.
- The proposed QALoRA is data-free and efficient (cost about 10 GPU hours).
- The experimental results are promising.
- Actual speedup with CUTLASS is reported.

### Weaknesses
There exist some formulas and details that are not clear enough. Some additional ablation and analysis experiments are needed to make the overall method more convincing. Check the questions section.

- How to get $\bf{x}_t$ in equation (7) is not described properly. Do the authors sample $\bf{x}_T \sim \mathcal{N}$, and run several solver steps using the FP model to get $\bf{x}_t$, or otherwise? If it is the case, the equation (7) is not written properly.
- The proposed Temporal LSQ (TLSQ) method uses a different activation quantization scale for different time steps. Can the authors show the learned scales and analyze how the scale factors of certain layers change w.r.t. the time steps on different datasets? 
- Can the authors compare TLSQ with deciding the time-step-wise activation quantization scale using some calibration data or even run-time dynamic quantization? This can help illustrate the necessity of LSQ.
- The paper mentioned that "we interpolate the learned temporal quantization scales to deal with the gap of sampling steps between fine-tuning and inference". I found steps=100 experiments on CIFAR-10 and LSUN in Table 1 and Appendix A, I wonder if the authors experimented with using a different schedule with fewer steps? Does this scale-deciding technique work well in the fewer-step regime?
- Is QALoRA applied for all the weights, including the convolutions and the attention layers?
- For the good of future efficient diffusion, can the authors discuss more relevant limitations and raise questions worth future studying? The current discussion is not specific.

### Questions
- How to get $\bf{x}_t$ in equation (7) is not described properly. Do the authors sample $\bf{x}_T \sim \mathcal{N}$, and run several solver steps using the FP model to get $\bf{x}_t$, or otherwise? If it is the case, the equation (7) is not written properly.
- The proposed Temporal LSQ (TLSQ) method uses a different activation quantization scale for different time steps. Can the authors show the learned scales and analyze how the scale factors of certain layers change w.r.t. the time steps on different datasets? 
- Can the authors compare TLSQ with deciding the time-step-wise activation quantization scale using some calibration data or even run-time dynamic quantization? This can help illustrate the necessity of LSQ.
- The paper mentioned that "we interpolate the learned temporal quantization scales to deal with the gap of sampling steps between fine-tuning and inference". I found steps=100 experiments on CIFAR-10 and LSUN in Table 1 and Appendix A, I wonder if the authors experimented with using a different schedule with fewer steps? Does this scale-deciding technique work well in the fewer-step regime?
- Is QALoRA applied for all the weights, including the convolutions and the attention layers?
- For the good of future efficient diffusion, can the authors discuss more relevant limitations and raise questions worth future studying? The current discussion is not specific.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new quantization scheme for diffusion models. In particular, the paper notes that post-training quantization (PTQ) may be efficient but brings relatively low performance compared to quantization-aware training (QAT). Conversely, QAT brings higher performance but requires heavy computational resources. To combine the advantages of these two main quantization approaches, the paper introduces a quantization counterpart of low-rank adapter (LoRA). The paper also proposes to quantize the model in a data-free manner through distillation from the original full-precision model.

### Strengths
- The paper introduces a new quantization method that brings substantial efficiency improvement without incurring extra computational overhead and performance degradation.

- The paper demonstrates strong performance.

- The paper is clearly written.

### Weaknesses
 - Comparisons: What happens if other quantization models also employ LoRA and distillation, which are common techniques to use?

- Novelty concern: I think the paper presents a combination of existing works (scale-aware optimization from LSQ, common distillation technique, and LoRA). Can the authors clarify the difference in contribution from the combination of existing works? If there is a difference, how does the performance differ compared to the combination?

- The paper states that the proposed scale-aware quantization is inspired by LSQ, where quantization scales are optimized alongside other trainable parameters. It seems like the proposed scale-aware quantization is a simple extension of the one proposed in LSQ. I do not think simple extension of existing work to temporal domain is novel enough to be considered as one of main contributions.

### Questions
Please refer to the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
