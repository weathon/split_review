# InstantIR: Blind Image Restoration with Instant Generative Reference

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Handling test-time unknown degradation is the major challenge in Blind Image Restoration (BIR), necessitating high model generalization. An effective strategy is to incorporate prior knowledge, either from human input or generative model. In this paper, we introduce Instant-reference Image Restoration (\methodname), a novel diffusion-based BIR method which dynamically adjusts generation condition during inference. We first extract a compact representation of the input via a pre-trained vision encoder. At each generation step, this representation is used to decode current diffusion latent and instantiate it in the generative prior. The degraded image is then encoded with this reference, providing robust generation condition. We observe the variance of generative references fluctuate with degradation intensity, which we further leverage as an indicator for developing a sampling algorithm adaptive to input quality. Extensive experiments demonstrate \methodname achieves state-of-the-art performance and offering outstanding visual quality. Through modulating generative references with textual description, \methodname can restore extreme degradation and additionally feature creative restoration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A good baseline for blind image restoration. Although the performance is not good, the editing ability is good in some real-world applications.

### Strengths
Good theoretical analysis and well written manuscript. Some experimental results are used to prove the effectiveness of design.

### Weaknesses
The performance on blind image restoration is not so good as other methods. The pipeline is simple and not novel.

The details of Instant Restoration Previewer is not well written. The authors only know that the previewer is a diffusion model. The same things happened on aggregator and DCP. In other word, Fig. 2 need to be redrawn in a detailed way.

Do the authors train DINOv2 for DCP from scratch? Also how to distill the diffusion model fro Previewer from a pre-trained DINOv2? It is confusing as it is said in Sec. 4.1.

As a workflow of blind image restoration, it contains deblur, SR, denoise and dejpeg. What is the differences between all-in-one and it? Can it also be evaluated on the all-in-one setting, such as Perceive-IR, PromptIR or ProRes?

The performance of the proposed method is not superior than other compared methods. The authors should press more on the essential keys of this paper.

The ability of editing LQ images seems to be derived from DiNOv2. The authors should provide more examples of editing scenario and discuss it in details.

### Questions
1. The details of Instant Restoration Previewer is not well written. The authors only know that the previewer is a diffusion model. The same things happened on aggregator and DCP. In other word, Fig. 2 need to be redrawn in a detailed way.
2. Do the authors train DINOv2 for DCP from scratch? Also how to distill the diffusion model fro Previewer from a pre-trained DINOv2? It is confusing as it is said in Sec. 4.1.
3. As a workflow of blind image restoration, it contains deblur, SR, denoise and dejpeg. What is the differences between all-in-one and it? Can it also be evaluated on the all-in-one setting, such as Perceive-IR, PromptIR or ProRes?
4. The performance of the proposed method is not superior than other compared methods. The authors should press more on the essential keys of this paper. 
5. The ability of editing LQ images seems to be derived from DiNOv2. The authors should provide more examples of editing scenario and discuss it in details.

Scores can be raised upon replies.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a novel approach to Blind Image Restoration (BIR) called Instant-reference Image Restoration (INSTANTIR), which addresses the challenge of model generalization under unknown degradation conditions. The authors propose a diffusion-based method that dynamically adjusts the generation conditions during inference by utilizing prior knowledge extracted from a pre-trained vision encoder.  Overall, the paper contributes a significant advancement in the field of image restoration by effectively integrating generative models with adaptive sampling strategies, demonstrating robust results across various degradation levels.

### Strengths
1. The design of the proposed method seems to be reasonable. In fact, different images should be enhanced with different generation ability, previous works do not address this issue. Meanwhile, this work introduces a solution for this important issue, which is important.
2.  The flexibility of the proposed method is verified, which may contribute to the usage of the diffusion model for image restoration.
3.  The paper summarizes the advantages of INSTANTIR and points out possible future research directions, including improving the interaction between generated priors and conditions, which is important in this topic.

### Weaknesses
1. The figure seems to be naive, I need to read the method carefully to get the key idea of the proposed method. Can authors provide a more detailed figure for both Sec.3.2 and Sec.3.3 to make it more clear?
2. In Sec.3.3, the authors claim "By employing a text-guided Previewer, we can generate diverse restoration variations with compound semantics from both modalities. However, these variation samples can conflict with the original input, making them ineligible as generative references." However, the authors do not provide visual analysis or references to support this opinion.
3. It seems the quality of the reference produced by the Previewer seems to be important for the final restoration effect, can authors provide deep analysis for the effect of the reference quality beyond simply visual results?
4. Since there are two diffusion models in the architecture, the computation cost and efficacy of the proposed method should be discussed.

### Questions
Please see the above Weaknesses.

### Soundness
3

### Presentation
2

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
The paper INSTANT-IR addresses the challenge of handling unknown test-time degradation in Blind Image Restoration (BIR) using diffusion model 

The method extracts a compact representation of the input image using a pre-trained vision encoder. During each diffusion step, this representation decodes the current diffusion latent state, embedding it into the generative prior. The degraded image is encoded with this reference, which creates a robust generation condition. By observing that the variance of generative references changes with degradation intensity, the authors develop a sampling algorithm that adapts to input quality.

Experiments show that INSTANT-IR achieves state-of-the-art performance, providing excellent visual quality. By adjusting generative references with textual descriptions, it can handle extreme degradation and even perform creative restoration.

### Strengths
It is not easy  to conclude what's the major strengths of this paper since most of the components are pretty straightforward compared with other paper. I will give authors a chance to answer what's the  Strengths from authors point of view.

### Weaknesses
Here are some of the points I am not clear by reading this paper.

1. Why DINO as the model to provide compact LQ image representation. From my understanding, DINO is a self-supervised learned representation that is very good for  semantic understanding. In a sense, the dino feature is highly compact and salient so that a lot of low-level cues are missing in the DINO feature. And Image Restoration is a pretty low-level task which need to pay more on the details rather than saliency.   That's why it doesn't make sense to me that DINO is a good choice here.

2. If the Generative Reference is generated from LQ image representation, it is not clear what extra information that could bring in. In addiiton, in Line 211-212, what high-level information is missing in LQ and it is super un-clear. 

3. For the case with prompt, how did author train it ? And what if the prompt and LR images are totally different like a women LR image but with a man as prompt etc. Please discuss more in this part and it is totally missing in this paper.

Overall, I didn't see any significant novelty in this paper since authors just use Dino feature and then decode it to be a reference image to guide the generation process.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new methodology for blind image restoration.
The main idea revolves around a new way to provide the degraded image as a condition to a pre-trained diffusion model (which is, to my knowledge, is typically done with a ControlNet).
Specifically, a pre-trained vision encoder first extracts a compact representation of the degraded image. This representation is combined with the diffusion state at each step, to form a preview of the generated image corresponding to that step (using a previewer). The previewed image is then used as the input condition for the diffusion model to produce the result in the next step.

### Strengths
1. The paper is overall clear and well written.
2. The proposed method is, to my knowledge, novel.
3. Connection to related work is good.
4. Experiments are thorough, including a convincing ablation study.

### Weaknesses
1. Compared to previous methods, the proposed method (InstantIR) seems to attain better perceptual quality, but this comes at the expense of worse distortion (e.g., PSNR, SSIM). Due to the perception-distortion tradeoff [1], this means that the proposed method cannot be claimed to be "SOTA", but just another point of the perception-distortion pareto frontier. Namely, to really be SOTA, a given algorithm needs to attain **better perceptual quality and better distortion simultaneously**, thus approaching the true perception-distortion tradeoff bound (dominating previous methods). Thus, it is not clear whether the proposed method is effective, because previous methods may also improve their perceptual quality at the expense of distortion (e.g., by tuning some hyper-parameters) and perhaps beat the proposed approach in terms of distortion at a given level of perceptual quality. Unfortunately, the authors do not discuss the perception-distortion tradeoff at all, which I believe is highly important given the fact that the proposed method's distortion is compromised in all data sets.
Note that the authors do briefly mention this limitation in the conclusion section (the compromised distortion compared to previous methods). But again, I believe that this should be thoroughly discussed, and it should be confirmed that the proposed approach is more effective than previous ones.

2. The conclusion/discussion section is quite short and limited. For example, a limitation I would specify is the design choice itself, which necessitates a degradation concept perceptor (e.g., DINO). What about other image modalities besides natural images (e.g., medical images, infra-red, compressed sensing), which DINO cannot handle? How can we then train InstantIR in such circumstances? Do we need to come up with a DINO-equivalent model to operate on images in other domains? My point is that InstantIR cannot be easily generalized/applied to other image modalities. I believe that this should be discussed, since many practitioners are working with other image modalities where blind image restoration is a crucial task.

3. While the proposed approach is novel, it is conceptually not that much different than previous methods (e.g., [2]). Specifically, the proposed method aims to generate samples from the posterior distribution (of natural images given a degraded image), which is an approach done in many previous works. Besides the empirical results, which, in my opinion, do not convince that the proposed approach is superior to previous ones (see point 1.), it is not clear why InstantIR offers any additional advantage over previous methods in terms of approximating the true sampler from the posterior.

4. The authors do not report NIQE scores for perceptual quality, which is standard in such works (e.g., [3]).

### Questions
1. Could you please explain why the proposed method is superior to previous ones, specifically referring to the perception-distortion tradeoff? (see weakness 1). Why is it appropriate to say that InstantIR is SOTA, given the perception-distortion tradeoff? What evidence in the paper convinces that the proposed approach is more effective than previous ones? For example, if previous methods were trained slightly differently (with different hyper-parameters), they may attain the same perceptual quality as InstantIR, but with better distortion (e.g., PSNR, SSIM).

2. How can we apply/train InstantIR in other image modalities besides natural images?

### Soundness
2

### Presentation
3

### Contribution
2
