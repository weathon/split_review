# Noise-free Score Distillation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Score Distillation Sampling (SDS) has emerged as the de facto approach for text-to-content generation in non-image domains. In this paper, we reexamine the SDS process and introduce a straightforward interpretation that demystifies the necessity for large Classifier-Free Guidance (CFG) scales, rooted in the distillation of an undesired noise term. Building upon our interpretation, we propose a novel Noise-Free Score Distillation (NFSD) process, which requires minimal modifications to the original SDS framework.
Through this streamlined design, we achieve more effective distillation of pre-trained text-to-image diffusion models while using a nominal CFG scale. This strategic choice allows us to prevent the over-smoothing of results, ensuring that the generated data is both realistic and complies with the desired prompt.
To demonstrate the efficacy of NFSD, we provide qualitative examples that compare NFSD and SDS, as well as several other methods.

\vspace{-6pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study proposes a simple yet effective method, Noise-Free Score Distillation (NFSD), to improve the conventional score distillation using a minimal modification. This study decomposes the score with classifier-free guidance (CFG)  into three terms, the condition, the domain, and the denoising components. Then, they remove the prediction error on unconditional samples between the estimated scores and and injected noises, since the score prediction error on unconditional samples is noisy. The domain score is estimated by a text prompt for a text-to-image model. The experimental results show that extremely high scale of CFG in score distillation is unnecessary, and NFSD can improve fine-grained details of generated images or neural fields.

### Strengths
S1. The proposed method, NFSD, is simple yet effective. In addition, the qualitative results support and demonstrate the effectiveness of NFSD.

S2. The paper is well-organized and easy to understand.

S3. The analogical decomposition of scores into three terms is interesting and makes sense.

### Weaknesses
W1. Despite the interestingness of score decomposition, the proposed method stems from numerous assumptions based on empirical findings without a principal approach. The decomposition of the score into condition, domain, and denoising components, while intuitive, lacks a rigorous mathematical justification. The assumption that the domain score can be effectively estimated by negative text prompts is not theoretically grounded and could be sensitive to the choice of negative prompts.

W2. Thorough experiments to validate the effectiveness of NFSD are absent. Although the qualitative results show improved quality of text-to-NeRF than conventional SDS-based approaches, there is no ablation study and quantitative result. The lack of quantitative metrics makes it difficult to objectively assess the improvement achieved by NFSD, and the absence of ablation studies leaves open questions about the contribution of each component of the method.

W3. Some technical parts lack enough rationales. For example, estimating the domain score by negative text prompts lacks the rationales. The assumption that a negative prompt captures the 'out-of-distribution' domain is not well-justified. It is unclear why a text prompt for low-quality images would represent the domain of errors in score distillation, and this approach may not generalize well to different types of artifacts or errors.

### Questions
Q1. Although the authors discuss the low diversity of NFSD, I wonder the detailed reason why the reduced CFG scale cannot produce diverse visual contents. In addition, can the authors provide the samples with different seeds and the same text prompts to show the diversity of generated contents?

Q2. In Figure 3, what is the diffusion timestep? In addition, I think that the authors should show the results of 
$x_{\text{OOD}} + \delta_D + \delta_N^{\text{OOD}}$
, where $\delta_N^{\text{OOD}}$ is the denoising score of $x_\text{OOD}$, not $x_\text{ID}$. I also suggest clarifying the notation of $\delta_N$ and $\delta_D$ in Figure 3, since the two scores are from different samples. 

Q3. Why do the prediction errors in Figure 4 (the second row) show a less-noisy map at t=1000? I think that the results are unintuitive, since they indicate that the score prediction at t=1 is difficult, while the score prediction at t=1000 is conducted almost perfectly except for the central region. 

Q4. In Section 4, the authors claim that the magnitude of the noise to be removed is monotonically decreased in the backward process. I wonder how we can assume that the scale of the domain score is preserved? Is there any rationale that only $\delta_N$ decreases over the backward process, while $\delta_D$ preserves its scale?

Q5. How about the results of SDS, where its CFG adopts the same negative prompts as NFSD, described in Section 4?

Q6. The authors have discussed that ProlificDreamer’s LoRA adaptation has a similar role with NFSD to exclude the prediction error of the denoising term $\delta_N$. Then, can the LoRA of ProlificDreamer be replaced with NFSD, while variational particle optimization is used? It would be interesting to show the compatibility of NFSD with ProlificDreamer.

Q7. Since NFSD requires additional inference at each training iteration due to negative prompting, I think that comparing the results of NFSD with those of SDS in terms of the number of function evaluations (NFEs) of diffusion models. 

Q8. In Section 4, how can we assume that the score prediction on text conditions is also composed of $\delta_D + \delta_N + \delta_C$, where $\delta_D + \delta_N$ is equal to the unconditional prediction? I think that it is a technical flaw, since Eq.(3) just implies $\epsilon_\phi (z_t ; t) - \epsilon_\phi (z_t  ; y=p_\text{neg}, t) = \delta_{C=p_\text{neg}}$. That is, $\delta_C$ is defined with both conditional and unconditional scores, not solely on the conditional score term. 

Q9. How is the negative prompt to estimate the domain term defined? I wonder whether the negative prompt is universal regardless of the image renderer. In addition, it assumes that the domain score can be estimated by the text prompts. However, how can we say that the image is from out-of-distribution, when the image can be estimated by text prompts of text-to-image models?

Q10. Can be simply using $s \delta_C$ for the score distillation possible without $\delta_D$? That is, using $\delta_D$ is necessary?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper first revisits Score Distillation Sampling (SDS) and proposes to decompose the updates generated by SDS into three components: domain correction, noise estimation, and condition direction. Through this approach, the authors provide an explanation for why SDS accommodates a high Classifier-Free Guidance (CFG) coefficient and introduce Noise-Free Score Distillation (NFSD). NFSD re-estimates the unconditional score using the negative prompt trick. As a result, NFSD can employ a standard CFG weight to alleviate the over-smoothing/saturation problem and enhance the quality of text-guided image editing and 3D asset generation.

### Strengths
+ The paper is well structured and organized. The method introduced in this paper is intuitive and straightforward to implement. The motivations behind the approach are vividly conveyed through clear formulations and effective visualizations.

+ The decomposition of SDS is both novel and intriguing. It not only offers a compelling interpretation of the large CFG weight selection in DreamFusion but also offers valuable insights into DDS [1] and VSD [2].

+ The empirical results clearly demonstrate a significant enhancement in 3D generation through the simple modifications initiated by NFSD.

[1] Hertz et al., Delta Denoising Score, 2023

[2] Wang et al., ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation, 2023

### Weaknesses
 - While the explanation is intuitively presented, it remains somewhat challenging to discern the fundamental distinction from the negative prompt trick.

- In Sec. 5, the paper asserts that NFSD is notably more efficient than VSD, despite sharing a similar working mechanism. Although this claim appears obvious, I would recommend providing quantitative evidence to substantiate this advantage when compared to other baseline methods. It is conceivable that dropping the noise term could even speed up the convergence of ancestral sampling by using fewer optimization steps.

- Further ablation studies are needed to validate the assertions put forth in this paper. In comparison to SDS, two terms have been omitted according to Eqs. 5 and 7: the noise prediction $\delta_N$ and the noise ground truth $\epsilon$. However, it remains unclear which of these terms plays the most pivotal role in improving the final results.

### Questions
1. Furthermore, it is not evident how steering the update of SDS could alter the optimization objective. Providing a more rigorous and formal argument would deepen the contribution of this work.

2. The authors introduce Eq. 6 to estimate $\delta_D$. Can the authors offer a rationale or justification for this approximation? Additionally, including visualizations that align with Fig. 3 would enhance the clarity and understanding of this proposal.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper reexamined the Score Distillation Sampling and proposed Noise-Free Score Distillation. The details of the images generated using SDS are more blurred, due to the slightly different distribution between the images generated by the generator(x(\theta)) and the original image x. This paper found a decomposition to counteract this effect and the authors use this decomposition to explain why previous methods have improved SDS. Adequate experimental results also demonstrate the effectiveness of the methodology.

### Strengths
This paper proposed a decomposition method to solve the problem of ambiguous results caused by the different distribution of the images generated by the generator and the original images; and uses this decomposition method to explain why previous methods have improved SDS. The experimental results are intuitive.

### Weaknesses
I'm concerned about whether p_{neg} = “unrealistic, blurry, low quality, out of focus, ugly, low contrast, dull, dark, low-resolution, gloomy” is generalizable across situations and able to cancel out \delta_{N}. Would a better generator g(\theta) be able to achieve the same effect, or train a model to estimate the bias \delta_{N}?

### Questions
Please see the weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work tackles the blurry results from Score Distillation Sampling (SDS) for text-to-3D generation. The score is decomposed into the condition, domain, and noise residual terms; the proposed method is designed to reduce the effect of the undesired noise component, by heuristically estimating the domain term with a negative prompt.

### Strengths
- Text-guided 3D generation by leveraging pretrained text-to-image models is a hot, timely topic. The authors propose to improve the famous SDS-based framework with a small modification.
- The proposed decomposition can be also used to understand existing works (DDS and VSD), which seems like a valuable contribution.
- The paper is well-written; the terms and derivations are clearly presented.

### Weaknesses
 - Although a key value of this work seems to be the decomposition of the SDS loss, I have a few questions on designing the proposed ~NFSW~ NFSD method (<- apologize for this big typo at the initial review):
  - How did the authors separate the small and large timestep values based on t=200? Why not t=100, 300, or 400?
  - Is it valid to assume δ_{C=p_neg} ≈ −δ_{D}? Did the choice of the negative prompt affect the performance?
  - How about changing (6) into just using the second part of (6) for all the time steps (i.e., unconditional term - negative-prompt-induced term, for all the time steps)?
- I appreciate the effort for many visual results; however, the lack of any quantitative results concerns me a lot. Is it possible to include the comparison using CLIP R-Precision of Table 1 in the DreamFusion paper? Furthermore, leveraging the MS-COCO text-to-image benchmark with FID/IS/CLIP score metrics may be worth trying to justify the results of 2D image generation in Figure 7.

### Questions
Please refer to the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
