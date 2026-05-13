# $InterLCM$: Low-Quality Images as Intermediate States of Latent Consistency Models for Effective Blind Face Restoration

- Decision: Accept
- Scores: 6, 3, 6, 5, 6

## Abstract
Diffusion priors have been used for blind face restoration (BFR) by fine-tuning diffusion models (DMs) on restoration datasets to recover low-quality images. However, the naive application of DMs presents several key limitations. 
(i) The diffusion prior has inferior semantic consistency (e.g., ID, structure and color.),  increasing the difficulty of optimizing the BFR model;
(ii) reliance on hundreds of denoising iterations, preventing the effective cooperation with perceptual losses, which is crucial for faithful restoration.
Observing that the latent consistency model (LCM) learns consistency noise-to-data mappings on the ODE-trajectory and therefore shows more semantic consistency in the subject identity, structural information and color preservation, 
we propose $\textit{InterLCM}$ to leverage the LCM for its superior semantic consistency and efficiency to counter the above issues. 
Treating low-quality images as the intermediate state of LCM, $\textit{InterLCM}$ achieves a balance between fidelity and quality by starting from earlier LCM steps. 
LCM also allows the integration of perceptual loss during training, leading to improved restoration quality, particularly in real-world scenarios.
To mitigate structural and semantic uncertainties, $\textit{InterLCM}$ incorporates a Visual Module to extract visual features and a Spatial Encoder to capture spatial details, enhancing the fidelity of restored images.
Extensive experiments demonstrate that $\textit{InterLCM}$ outperforms existing approaches in both synthetic and real-world datasets while also achieving faster inference speed. Code and models will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose using the LQ image as an intermediate state in the LCM. Because of how LCM works, they can apply image-based loss during training. The method uses the diffusion model’s prior by adding noise to the LQ image. This drags the LQ image to the domain of generative capability.  And then they guide diffusion model to restore the LQ image with constraint of semantic related info.

### Strengths
(+) The proposed method is carefully designed and based on an interesting observation about LCM.

(+) The paper is well-written and easy to follow. The figures are well-designed and professionally presented, clearly illustrating the main takeaway.

(+) The experiments are thorough and solid, with especially useful discussions in the appendix.

(+) The performance is solid, outperforming baselines in terms of visual quality on real-world images across many cases.

(+) Thanks to the advantages of LCM, the inference speed is excellent, which could benefit the related community.

### Weaknesses
(-) What does the author mean by "back to the low-quality image initialization" in line 100? Does Figure 3 show all the trainable components? It seems the authors are suggesting that some latents are also trainable.

(-) Table 2 should be reorganized. The current version is squeezed and difficult to read.

(-) It seems the whole pipeline has a strong capability to preserve identity. I am curious about how the method performs when the face in the LQ image has additional textures, like tattoos or festival-style face paint. How would the proposed method handle these cases?

(-) Does the author's method design draw significant inspiration from general image restoration approaches built on diffusion models? I ask this because using a ControlNet-like design to extract useful information from low-quality images is not a new concept. Meanwhile, it seems that the main performance improvement comes from the spatial encoder, which is the ControlNet as semantic info encoder, as demonstrated in Tables 1 and 2. Additionally, the second main source of performance appears to be the LPIPS loss. It seems that one could solely rely on the spatial encoder to achieve good results. Could I understand that the performance improvements on your task could be easily obtained by simply using a ControlNet to extract LQ's semantic info? If this is not the case, please provide a justification.

### Questions
All my concerns are listed in the weakness part. The main concern is about the key source of performance, which requires the author’s justification for the method design. I will consider raising my score if the author provides a thorough explanation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new method for blind face image restoration, consisting of three main components: 1) applying a latent consistency model (LCM) for fast sampling; 2) starting from a low-resolution (LR) image instead of standard Gaussian noise during inference; and 3) incorporating semantic information from the LR image. The authors compare their method against numerous baselines and achieve better quantitative performance over most metrics.

### Strengths
1) The comparison against various baselines is comprehensive and well-organized.
2) Figure 2 and Figure 3 clearly illustrate the key concepts of the method.
3) The qualitative results demonstrate a significant improvement over several baselines.

### Weaknesses
1) The paper overlooks important literature [1], which discusses accelerating diffusion models for inverse problems, including image restoration, by beginning with a better initialization rather than standard Gaussian noise. This prior work shares a similar concept of initiating the diffusion process from LR images in this study.
2) One motivation for employing LCM appears to be the acceleration of the diffusion prior. However, the manuscript simply states that “diffusion-prior based approaches still suffer from time-consuming inferences” (line 161) without discussing the extensive literature on accelerating diffusion models, such as techniques involving distillation (beyond the consistency model) and diffusion bridges [2].
3) The abstract is difficult to follow. I recommend revising it to make it shorter and more focused, allowing readers to easily grasp the key ideas of the paper.
4) While the quantitative metrics indicate improvements, the visual results do not convincingly demonstrate superior performance. For instance, compared to the ground truth, the proposed method generates features that differ significantly (e.g., hair in Figure 6), similar to other baselines. From a perceptual quality standpoint, it is challenging to determine whether the proposed method is indeed better. In Figure 6, the proposed method oversharpens the image compared to the reference. This concern is further supported by only marginal improvements in perceptual metrics over the baseline methods, such as CodeFormer (with a worse FID score than some baselines and a marginal improvement of 0.004 in LPIPS and 1.03 in MUSIQ).
5) Some statements in the manuscript appear overly assertive without adequate support from references or experimental evidence. For example, the abstract claims that “the latent consistency model shows more semantic consistency in the subject identity,” and line 163 states that “the commonly used perceptual loss in image restoration tasks cannot be well integrated into their framework.”
6) The contributions of this paper seem somewhat incremental. The use of LR as a prior has been investigated in [1], and LCM for fast diffusion prior is a well-established technique. From this perspective, the main contribution appears to be the incorporation of semantic information from LR images, which raises questions about whether it meets the standards for ICLR.

### Questions
1) Could the authors provide examples of the semantic information from HR and LR images of the same scene such that one could evaluate whether the semantic information from the LR image is sufficient as a prior for HR reconstruction?
2) How were the hyperparameters (2) chosen in this study?
3) Why was a four-step LCM considered instead of a different number of steps? This choice seems heuristic.
4) Figure 1 is unclear. It says that LCM maps directly to the real image space. Does it imply LCM learns a mapping from LR to HR images directly like [2], rather than progressively denoising as depicted in Figures 2 and 3?
5) What is the degradation process considered in the synthetic dataset? Is it a simple interpolation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to regard the low-quality image as the intermediate state of LCM models for blind face restoration, considering that the LCM enjoy superior semantic consistency compared to the naive diffusion models, in terms of the generative prior utilization. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper proposes an efficient method to utilize the generative prior for blind face restoration, that the LCM models enjoy more semantic consistency compared to the naive diffusion models, and the image-space optimization benefit more restoration-specific loss constrains.
2. The semantic consistency comparison between LCM and diffusion models are well illustrated, and the method design is straightforward without bells and whistles. The intermediate state validation and ablation experiments are reasonable and sufficient.
3. The presentation is well for readability.

### Weaknesses
1. Is there any comparison for x0-prediction-based diffusion model.
2. Why only face dataset, whether the proposed method could generalize to other natural image dataset, is there any discrepancy in adopting the LCM models as generative prior. If so, what modifications should we care to apply current method to other types of images, and the preliminary results on a non-face dataset would be nice if feasible.
3. Whether the proposed method can be integrated with LCM-LoRA for more fast inference? Is there any potential challenge, and the preliminary results would be recommended if feasible.

### Questions
1. The training efficiency is wondered, as the LCM backbone is freezed, how long could we get the model, and the training stability is concerned when various loss functions are added.
2. What's the difference between the spatial encoder and ControlNet, only incorporating the visual embedding?

### Soundness
3

### Presentation
4

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
The authors propose to use a latent consistency model to solve blind face restoration problems. Prior work on this research topic normally fine-tune a diffusion model on restoration datasets. To enhance the semantic consistency and incorporate the perceptual loss, authors further consider the low-quality image as the intermediate state of LCM models. The algorithm is tested on standard datasets and leads to improved performance over the considered baselines.

### Strengths
1. The paper is well-written, the experiments are systematic.
2. The authors manage to outperform the prior works on blind face restoration.

### Weaknesses
1. Regarding the contribution. Using pre-trained diffusion model as the image prior for blind face restoration is widely studied. The extension from conventional DDPM to LCM is quite straightforward. While the authors leverage the consistency properties of LCM, the core idea of using a pre-trained model for restoration remains similar to existing methods. The incremental benefit of using LCM over other diffusion models needs more rigorous justification, especially given the retraining process.
2. Considering the combination of different training objectives, it is better to provide further analysis on the choices of hyper-parameters, and discuss about the risk of human bias due to these manual parameters. The current hyperparameter selection seems arbitrary and lacks a systematic approach. For instance, the weighting between perceptual and adversarial loss is not thoroughly explored, and the impact of this choice on the final restoration quality is unclear. A more detailed analysis, such as a sensitivity study or a discussion of the trade-offs, would strengthen the paper.
3. I do not think the computation of perceptual loss is particularly challenging. Several existing works [1][2] on blind inverse problems have successfully integrated this term into a Bayesian framework. The authors claim that their approach uses x0 at the end of the inference steps, but this is a standard practice in diffusion models. The novelty of their approach in this regard is not clear, and the comparison with existing methods that also use perceptual loss within a diffusion framework is not sufficiently detailed.

### Questions
1. Overall, I consider retraining to be a disadvantage. However, if the model demonstrates strong performance on a range of low-quality face images in real-world scenarios, it adds value. Can the authors make the trained weights available for testing?
2. How does the proposed method extend to images beyond just faces? If the study focuses solely on face restoration and is not even effective with images that include hands, I find it lacks generalizability and robustness.

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
The latent consistency model (LCM) demonstrates improved semantic consistency in subject identity, structural information, and color preservation, making it a viable alternative to conventional diffusion model priors. In this study, the authors propose InterLCM, which utilizes the low-quality image as an intermediate state in LCM models to facilitate efficient blind face restoration. Extensive experiments showcase the superior performance of InterLCM compared to existing approaches .

### Strengths
1.	the authors propose a LCM-based face restoration, a simple but effective BFR framework, it effectively maintain better semantic consistency in face restorations.
2.	LCM-based method shows faster inference than stable diffusion model

### Weaknesses
1.it is nice to find some trials on the LCM model for blind face restoration. But there exists some questions 1). Why prefer the bfr task not for the general sr task.2). the usage of lcm is straightforward, and the theory analysis and support is absent. 
3).it is better to add more relevant works using the defined priors:

1). 3D Priors-Guided Diffusion for Blind Face Restoration
2). Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild
3). Face Restoration via Plug-and-Play 3D Facial Priors

### Questions
see in weakness

### Soundness
3

### Presentation
3

### Contribution
3
