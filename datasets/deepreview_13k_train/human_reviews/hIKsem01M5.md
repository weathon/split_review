# Automated Black-box Prompt Engineering for Personalized Text-to-Image Generation

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Prompt engineering is an effective but labor-intensive way to control text-to-image (T2I) generative models. Its time-intensive nature and complexity have spurred the development of algorithms for automated prompt generation. However, these methods often struggle with transferability across T2I models, require white-box access to the underlying model, or produce non-intuitive prompts. In this work, we introduce \textsc{\modelname}, an algorithm that automatically produces human-interpretable and transferable prompts that can effectively generate desired concepts given only black-box access to T2I models. Inspired by large language model (LLM) jailbreaking, \modelname{} leverages the in-context learning ability of LLMs to iteratively refine the candidate prompt distribution built upon the reference images. Our experiments demonstrate the versatility and effectiveness of \modelname{} in generating accurate prompts for objects, styles, and images across multiple T2I models, including Stable Diffusion, DALL-E, and Midjourney.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a training-free iterative algorithm based on in-context learning of Multimodal LLMs (MLLM) to refine prompts for text-to-image (T2I) generation that would increase alignment of the generated images with a given set of reference images. The algorithm, PRISM, makes use of a MLLM to first zero-shot guess a caption for the reference images, then it uses the caption to generate a new image, which is evaluated in terms of visual similarity to one of the reference images using another multimodal model (in practice, the same model is used). Then the new prompt and its generation are included in the metaprompt of the MLLM for proposing a new caption based on in-context learning. This pipeline is executed for multiple iterations and with different bootstrapped captions in parallel. Eventually, the prompt generating the most similar image to the entire reference set is selected. The experiments test PRISM for personalized image generation/editing, and image inversions. A comparison with other baselines from these tasks show on-par or better performance when testing with different T2I models.

### Strengths
1. The paper is well written. The structure makes it clear and easy to follow.
2. The experiments are comprehensive and well executed
3. Higher interpretability and transferability compared to other personalization / invertion methods

### Weaknesses
1. The idea is not novel. There exists similar attempts, .e.g., Manas et al 2024,  Liu et al 2024, Yang et al 2023. Manas et al propose a very similar iterative algorithm based on in-context learning. The only (small) difference lies in the tasks, which here is personalization / inversion, while in Manas et al is improving prompt-image consistency in general (with no reference images).  Yang et al work is similar as it relies in on GPT4V, which is used to evaluate and propose new candidates prompt based on an initial idea of the user (kinda personalization). Finally, Yang et al, explore in a very similar the use of GPT-4V for text to image generation and prompt invertion (see Section 6 of the paper). Moreover, despite less related, i.e., do not need to be compared, there exists a few work that proposed prompt improvement based on LLM fine-tuning, e.g., Prompist (Hao et al 2024). I think these works might be worth a mention in the related work section even tho clearly using a different approach.  
2. The improvements w.r.t. GP4V is marginal. Table 3 shows quantitatively that PRISM only improves 0.02 of ClipScore on images, while having higher (worse) negative log likelihood.

### Questions
Please comment on the mentioned weaknesses.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents the PRISM algorithm for producing prompts that can generate desired concepts given an input of images and (optionally) an original prompt. PRISM iteratively generates images with a text-to-image model, assesses the images with a vision-language model, and generates new prompts with a large-language model. The method is applied to two kinds of prompting situations - personalized text-to-image generation and prompt inversion from a given set of images. The work includes comparisons across existing methods, with both quantitative and qualitative analyses. The work also includes ablations over alternative vision-language models (GPT-4V) and the number of iterations used.

### Strengths
* The PRISM method is presented with clarity, is intuitive, and straightforward to implement.
* The experimentation applies PRISM to two useful usecases - text-to-image personalization and image inversion - demonstrating its utility.
* The authors apply PRISM to three different families of models and several generations of models, demonstrating extensibility across model classes 
* The analysis includes good coverage over other methodologies, and the PRISM method shows strong performance compared to prior works, highlighting its efficacy.
* The paper includes useful qualitative discussions about patterns of the generated prompts and subsequent images, including highlighting strengths of the method such as maintaining structural consistencies or small visual details in images.
* The method usefully recommend alternatives to CLIP in the selection of the judge model, noting its weakness in the context of promp generation.

### Weaknesses
1. The work would be strengthened with greater discussions about possible weaknesses of VLMs as judge models and how these concerns may be mitigated. For example, VLMs have known issues with compositionality and counting [1,2]. 
2. While the ablation focusing on budget provides useful insights, it would be useful to contextualize how the improvement in metrics translate to visually perceptible improvements to better contextualize the extent to which the iterations are required for human-perceived improvements. 
3. Section 3.1 and 3.4 usefully highlights that the visual similarity criteria may relate to different kinds of image qualities, such as a focus on the main objects in the image, style of the image, or general similarity. However, the Experimental Section 4.2 does not have much discussion about how these different similarity criteria are captured by the PRISM methodology and how it affects the visual representation of the newly generated images using the PRISM-generated prompts.
4. [minor] The maintenance of the whole prompt distribution in the prompt generation process (mentioned in Section 3.2) has been studied in other works [3]. It would be useful to contextualize among this prior work.

### Questions
[Questions numbered according to each Weakness above]
1. How might known issues with VLMs affect the efficacy of PRISM (e.g. compositionality and counting), and what are possible mitigations?
2. How do quantitative improvements across iterations and associated budget correspond to visual improvements in images? 
3. How well are different kinds of visual similarity, and their potential mutual exclusivity, captured by PRISM in Experimentation? Is it possible to prioritize certain kinds of criteria via the meta-prompt for the judge or generator within the method? Are there potential gaps in achieving some kinds of visual similarity?

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
4

### Summary
This paper proposes a prompting technique for text-to-image generation, termed PRISM, utilizing a Large Multimodal Model (LMM). PRISM iteratively generates image captions, evaluates the generated images, and refines the images based on the evaluation scores. By providing scores to the LMM in a manner similar to the chain-of-thought approach, PRISM guides the LMM to improve captions for enhanced image generation quality.

### Strengths
1. Unlike previous techniques that generate only a bag of words, PRISM generates fully human-readable prompts for image generation.

2. PRISM has a straightforward implementation, as it does not require model training.

3. The paper is written in a clear and accessible manner.

### Weaknesses
1. In Line 187 and Line 9 of the algorithm, you state that$\text{P}_{\theta_F}$ is updated; however, the method for updating the distribution is not specified in the method section. In the Appendix, it appears that this process simply involves prompting the score generated by the discriminator. How, then, can this be interpreted as updating the distribution? This could lead to misunderstandings, as “updating the distribution” generally implies updating the model parameters. The authors should clarify that they are not updating model parameters but rather using in-context learning to influence the sampling distribution of the Large Multimodal Model (LMM) through iterative prompting. The current description is misleading and needs to be more precise about the mechanism of influence.

2. In Figures 3,4, and 5, the length of the prompts used in the comparison techniques varies, so it is necessary to clearly indicate the settings for each comparison group. However, varying the prompt length in this way seems to make the experiment somewhat unfair. The authors should provide a more detailed explanation of how prompt lengths were chosen for each baseline and justify why these lengths are appropriate for a fair comparison. It is essential to ensure that the baseline methods are evaluated under conditions that are as close to their optimal settings as possible.

3. There is no ablation study for the LMM model. The authors should conduct experiments with other LMMs (e.g., BLIP-2, LLaVA) to assess the generalization capability. The choice of LMM can significantly impact the performance of the proposed method, and it is important to demonstrate that the approach is not overly reliant on a specific model. An ablation study with different LMM architectures would provide a more robust evaluation of the method's generalizability.

4. There is no ablation study on prompt length. The authors should investigate how the performance of their method varies with different prompt lengths. This is crucial for understanding the sensitivity of the approach to prompt length and for identifying the optimal prompt length for different tasks. Such an analysis would also help in comparing the method with other approaches that might have different prompt length requirements.

5. Iteratively prompting a large model is computationally expensive, as noted in the Appendix. The authors should discuss the computational cost in more detail, including the time and resources required for each iteration. A more thorough analysis of the computational burden is needed to assess the practical applicability of the method.

### Questions
see weaknesses

+)
Have you explored other tasks in the PEZ paper, such as style transfer, prompt distillation, or multi-concept generation (prompt concatenation)? Since this task requires a much shorter prompt than the maximum text length allowed by CLIP (for concatenate the different prompts), if PRISM struggles with generating shorter prompts, it may not perform well in those tasks either.

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
3

### Summary
The paper introduces PRISM, an automated hard prompt generation algorithm designed for text-to-image (T2I) generation. PRISM minimizes the needs for human intervention, avoiding laborious trial-and-error prompt creation processes. PRISM integrates T2I generator, Judge, and Prompt Engineer models, where the latter two are existing black-box Vision-Language models. Generated prompts are intended to be human-interpretable and transferable across various T2I models. Experimental results show that PRISM achieves lower NLL and higher image similarity scores compared to previous methods such as TI or PEZ.

### Strengths
* PRISM is compatible with any black-box T2I models, Judge, and Prompt engineer models. This model-agnostic design and hard prompt generation seem to be a good combination. In addition, PRISM does not require any training.
* The paper demonstrates PRISM’s effectiveness using a variety of experiments. Quantitative evaluations include NLL, CLIP-I, and DINO scores. Qualitative demonstrations present various applications including personalized T2I, direct image inversion, and easy prompt editing.
* The paper thoroughly discusses the background and related works.

### Weaknesses
 * Although the automated process would reduce human effort, PRISM’s iterative process may require huge computational resources and time (as discussed by authors in the limitation section). On the other hand, there is no efficiency (latency, resource usage) comparison between PRISM vs. pervious approaches. For example, CLIP-Interrogator may not achieve the best performance; but given the same resources, does PRISM show better results than CLIP-Interrogator?
* N seems to be more critical than K. For example, in Table 5, using (N, K) = (30, 1) shows a much lower NLL than (6, 5) while maintaining a similar CLIP-I score. This implies that the quality of the initial prompt/candidate may be a key factor in the final performance, making the role of iterative refinement less important. To better illustrate this, it would be useful to show (1) the distribution of initial “scores” across N, and (2) the “score” improvements for all candidates through multiple iterations. These “scores” may be represented by the Judge score, or CLIP-I score, directly reflecting the image quality.
* Is there a mechanism that strictly guarantees the candidates’ score (provided by the Judge) keep increasing? Or does the model itself implicitly increase the score? I am asking this question because I am not sure whether the “scoring” process is necessary, and whether the “score” actually increases through iteration.
* Does the concept of “stream” equal to the beam search candidates? There are not many details about generating diverse streams N.

### Questions
* Is there a mechanism that strictly guarantees the candidates’ score (provided by the Judge) keep increasing? Or does the model itself implicitly increase the score? I am asking this question because I am not sure whether the “scoring” process is necessary, and whether the “score” actually increases through iteration.
* Does the concept of “stream” equal to the beam search candidates? There are not many details about generating diverse streams N.

### Soundness
2

### Presentation
3

### Contribution
2
