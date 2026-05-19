# SVDQuant: Absorbing Outliers by Low-Rank Component for 4-Bit Diffusion Models

- Decision: Accept
- Scores: 8, 8, 8, 6, 8, 6

## Abstract
\looseness=-1
    Diffusion models have been proven highly effective at generating high-quality images. However, as these models grow larger, they require significantly more memory and suffer from higher latency, posing substantial challenges for deployment. In this work, we aim to accelerate diffusion models by quantizing their weights and activations to 4 bits. At such an aggressive level, both weights and activations are highly sensitive, where conventional post-training quantization methods for large language models like smoothing become insufficient. To overcome this limitation, we propose \textit{\method}, a new 4-bit quantization paradigm. Different from smoothing which redistributes outliers between weights and activations, our approach \textit{absorbs} these outliers using a low-rank branch. We first consolidate the outliers by shifting them from activations to weights, then employ a high-precision low-rank branch to take in the weight outliers with Singular Value Decomposition (SVD). This process eases the quantization on both sides. However, \naively running the low-rank branch independently incurs significant overhead due to extra data movement of activations, negating the quantization speedup. To address this, we co-design an inference engine \textit{\engine} that fuses the kernels of the low-rank branch into those of the low-bit branch to cut off redundant memory access. It can also seamlessly support off-the-shelf low-rank adapters (LoRAs) without the need for re-quantization. Extensive experiments on SDXL, PixArt-$\Sigma$, and FLUX.1 validate the effectiveness of \method in preserving image quality. We reduce the memory usage for the 12B FLUX.1 models by 3.5×, achieving 3.0× speedup over the 4-bit weight-only quantized baseline on the 16GB laptop 4090 GPU, paving the way for more interactive applications on PCs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents SVDQuant quantizes weights and activations to 4 bits to accelerate inference of large-scale diffusion models. Through a low-rank decomposition branch, the authors introduce SVDQuant, a method for mitigating the impact of outliers on quantization.
They absorb outliers on weights/activations. To do so, they first migrate the outliers from activation to weight. Then they apply SVD to the updated weight, decomposing it into a low-rank branch and a residual.  Additionally, they incorporate an inference engine, LoRunner, which combines low-rank and low-bit kernels to maximize computation speed and minimize memory overhead. As demonstrated in empirical results for different large diffusion models, SVDQuant offers significant memory savings and performance improvements without affecting image quality significantly. This demonstrates that it is a promising approach for deploying diffusion models on consumer-grade hardware.

### Strengths
1-SVDQuant’s strategy to manage outliers using low-rank decomposition offers an improvement over standard smoothing techniques.

2-LoRunner effectively reduces memory access overhead and enhances performance, particularly for GPU inference, addressing practical deployment constraints.

3-Pushing boundaries for low-bit quantization of both weight and activation

### Weaknesses
1-The level of contribution is not great. Using outliers and low rank for quantizations is a very well-known technique. The authors need to have a section in related work and highlight the difference/novelty between the technique and all related work. Otherwise, the novelty seems incremental.

2- The paper lacks a theoretical analysis of why the low-rank decomposition approach can consistently outperform other outlier-handling techniques beyond empirical observations.

3- Code is not provided.

### Questions
1- Using outliers and low rank for quantizations is a very well-known technique. The authors need to have a section in related work and highlight the difference/novelty between the technique and all related work. Otherwise, the novelty seems incremental.
Maybe you can provide a table for all related work including the mentioned one here and show all similarities and differences with the proposed technique. 

[A] QNCD: Quantization Noise Correction for Diffusion Models

[B] Q-DiT: Accurate Post-Training Quantization for Diffusion Transformers


2- The choice of rank (e.g., rank 32) appears somewhat arbitrary, without adequate theoretical or empirical justification for why this setting was chosen over others.  Can the author put more comments about it? Maybe more ablation studies and more detailed experiments about it will give more insight to the reviewer. 

3- If a neural network exhibits skewed distributions that may not align well with the low-rank assumption used here (e.g., nongaussian behavior), how does it work? Please discuss the robustness of the method to different weight distributions.

4-With the advent of mixed-precision computation, some architectures might benefit from a mix of 4-, 8-, and. How would LoRunner perform in such configurations, and could it be adapted to handle this flexibility?

5-What are the challenges to extending the method below 4-bit? For example 2w2a or 4w2a or 2w4a?

6-I am interested to see a breakdown of LoRunner’s impact on speed and memory, perhaps by comparing SVDQuant with and without LoRunner.

7- Minor typos:
"Quantizes both the weights and activations" – quantizes both weights and activations.
“on NVIDIA RTX-4090 laptop" – "on an NVIDIA RTX-4090 laptop."

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
3

### Summary
This paper proposes a 4-bit PTQ method for diffusion models that absorbs the outliers between weights and activations using a low-rank branch. To augment this method, the paper also presents an efficient inference engine to avoid the redundant memory access of the activations. Experimental results on latest diffusion models validate the superior accuracy and memory efficiency of the proposed method.

### Strengths
The paper is well-written and clear. Though the idea is generally intuitive, the observation of the low-rank outliers and the fusion from the low-rank branch to low-bit branch makes this work a strong submission. Experiments are conducted on the latest diffusion models, and the results are generally strong.

### Weaknesses
1. Can the authors include some results on sub 4-bit quantization with the proposed method? It would be good to know the limitations of the method.

2. The authors should include more comparisons in their experimental results. While they compared with MixDQ and ViDiT-Q, some prominent works have been left out, such as Q-Diffusion [1] and QUEST [2].

[1] https://arxiv.org/pdf/2302.04304

[2] https://arxiv.org/pdf/2402.03666v1

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a post-training quantization method for diffusion models called SVDQuant that successfully quantizes both weights and activations to 4 bits without sacrificing visual quality. By integrating the low-rank branch kernels into the low-bit branch, SVDQuant minimizes overhead, significantly accelerating model inference. Tested on the 12B parameter FLUX.1-schnell model, it reduces memory usage by 3.6 times compared to the BF16 model and achieves a 3.6 times speedup over the NF4 W4A16 baseline on a laptop equipped with an RTX-4090 GPU.

### Strengths
1. The paper introduces a full-precision low-rank adapter and Singular Value Decomposition (SVD) to effectively compensate for quantization errors.
2. The authors have implemented a novel kernel that efficiently fuses low-rank and low-bit branches, minimizing computational overhead.
3. The extensive experiments conducted on state-of-the-art diffusion models, such as FLUX, provide strong evidence of the method's effectiveness and robustness.

### Weaknesses
1. Adding a W8A8 baseline to the latency comparison would provide valuable insights and a clearer performance reference.
2. Since the authors use group quantization for weights and activations in the 4-bit setting, it would be beneficial to include methods that also use group quantization, such as Atom [1], as baselines.

References: 
[1] Zhao et al. "Atom: Low-bit Quantization for Efficient and Accurate LLM Serving" in MLSys'24

### Questions
1. Could you explain the calculation method for the smoothing factor in more detail?
2. In the ablation study, what is meant by "SVD-only" and "naive quantization"? Does "SVD-only" indicate that no quantization is applied? And what is the setting for naive quantization?

### Soundness
4

### Presentation
4

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
This work accelerate diffusion models by low-bit quantization and low-rank decomposition. The motivation of this work is the outlier quantization error in activations for recent PTQ methods. The authors propose a multi-branch architecture with both low-bit and low-rank operations. To speed up the inference, a kernel fusion implementation is also proposed for the two branches. In experiments, the DiT and UNet diffusion models are evaluated in 4/8-bit conditions.

### Strengths
- It is an interesting topic to combine the low-bit quantization and low-rank decomposition, previous work including Loft-Q (ICLR 24), et al.

- This work proposes a kernel fusion implementation to speed up on-device inference.

- The method is reasoning and the writing is easy to follow.

### Weaknesses
- I don't think splitting low-rank and low-bit branches is a good idea to overcome quantization errors. Different from the QLLM (ICLR 24) et al.,  the computation of the two branches can not merge after training, leading to 5~10% overheads in the paper (line 314).

- Experiments parts are not very solid: the baseline quantization methods are kind-of weak. Recent works including SpinQuant [1], AffineQuant [2], et al. achieve much higher performance than the baseline NF4 in the paper and also without the additional branch.

[1] SpinQuant: LLM quantization with learned rotations
[2] AffineQuant: Affine Transformation Quantization for Large Language Models

### Questions
In the experiment part, this work almost evaluates on 4/8-bit quantization; what is the best trade-off between bit-width and performance for diffusion models? 

Also, adding more best practice of the diffusion model quantization will be fine.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an aggressive quantization method (4-bit) for both activations and weight in diffusion models. To mitigate quantization-induced quality losses, the author propose to  migrate outlayers from activations to weights and then to add low-rank branches at high accuracy 16b (as opposed to the traditional smoothing approach which is not sufficient at 4-bit quantization level especially for diffusion models): i.e. the network is modified also for inference by the presence of the branches A baseline implementation of the low-rank branches in inference is slow and negates the speed advantages of the quantized computations, The authors then propose a remedy to this shortcoming which merges the branches, to regain speed (while also retaining memory reduction advantages)

### Strengths
The paper presents clearly the flow of ideas: statements are clear and detailed proofs are moved to the appendix, hence they do not distract from the flow f the key messages.
The motivation for the work is clearly described as well as the gaps in the SoA, and the claims of novelty. 
The reader is led step by step to the final solution: this flow helps understanding the technical motivations of the various steps. 
Experiments are clear and the KPI used are well defined.

### Weaknesses
It is not clear ho lambda for the migration of outlayers from activations and weights si computed (it is per-channel - so the array can be quite big). This is in my view a bit of a problem, because lamda migh be impacted by the dataset used for calibration (if it is decided offline) or may be hard to determine efficiently online. 

Inference time results are missing because the authors have no access to modern gpus (Blackwell) with native 4b support. This is a minor weakness, but it must be noted that it's not fully clear if the merged kernels will benefit from the same speedup claimed for pure 4b kernels. 

the key ideas are not novel per se, but the combination is interesting - the key intuition being the merged low-rank and low-precision kernel to recover speed

### Questions
Please clarify how the diag lambda is determined
if possible provide an estimate of the speedup expected by the mixed kernel - possibly using mixed kernel ad higher precision and see how the speedup degrades from "pure" low precision kernel.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose SVDQuant to enable 4-bit quantization for diffusion models in terms of both weights and activations, with SVD approach utilized to enable quantization of residual (R=W-L1L2) rather than directly quantizing weight matrices. SVDQuant first use a smoothing technique proposed in previous work to transfer the outliers in activations to weights, then use SVD to enable 16-bit low-rank approximation of the weights and quantize the residual between the two weights, absorbing the weight outliers in the low rank branches L1 and L2.

### Strengths
1. I like the idea of translating the weight quantization into residual quantization to eliminate outliers in weights. 
2. The figures are well illustrated, and the math presentations are insightful. 
3. The model with a dinosaur head is hilarious.

### Weaknesses
1. There are a few strong statements in this work with insufficient reasoning. 
2. The method section mainly focuses on justifying the minimization of quantization error but lacking discussion of the computation flow. 
3. The residual quantization approach looks similar to the quantization of error matrix in LoRC.

### Questions
1. Some strong statements need to be properly supported by evidence:

- "Weight-only quantization *cannot* accelerate diffusion models" - For modern GPUs, maybe, but this lacks concrete evidence. Also, different hardware platforms have different bottlenecks. 

 - "Weights and activations *must* be quantized to the same bit width" - Can custom hardware support direct mixed precision operations?

 - "they primarily consider weight-only quantization..." For example, the authors have cited Q-diffusion and EfficientDM which quantize both activations and weights. This statement needs further justification. 

2. The authors mention that the "lower-precision side will be upcast during computation, negating potential performance boosts". However, as illustrated in Figure 6(b), the XL1L2 branch appears to retain 16-bit full precision before being combined with the quantized residual. This approach seems to be different from the authors' initial claim.

3. It would be very helpful if the authors could elaborate on the similarities and differences between their methods and LoRC (Yao et al.)
 
Minor:

- How is quantization level defined in Figure 3? And why can it take fractional numbers? I vaguely understand after smoothing, the peak of |X| drops from 10 to 2, but why the peak of |W| also drops? I thought smaller peaks means easier to quantize.

- QKV projection, presumably, is an LLM concept, and it may look abrupt in 4.3 without preliminary discussion.

### Soundness
3

### Presentation
2

### Contribution
2
