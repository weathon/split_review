# ProFI-Painter: Text-Guided Prompt-Faithful Image Inpainting with Diffusion Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent progress in text-guided image inpainting, based on the unprecedented success of text-to-image diffusion models, has led to exceptionally realistic and visually plausible results.
However, there is still significant potential for improvement in current text-to-image inpainting models, particularly in better aligning the inpainted area with user prompts.
Therefore, we introduce $\textit{ProFI-Painter}$, a $\textbf{training-free}$ approach that $\textbf{accurately follows prompts}$.
To this end, we design the $\textit{Prompt-Aware Introverted Attention (PAIntA)}$ layer enhancing self-attention scores by prompt information resulting in better text aligned generations.
To further improve the prompt coherence we introduce the $\textit{Reweighting Attention Score Guidance (RASG)}$ mechanism seamlessly integrating a post-hoc sampling strategy into the general form of DDIM to prevent out-of-distribution latent shifts.
Our experiments demonstrate that ProFI-Painter surpasses existing state-of-the-art approaches quantitatively and qualitatively across multiple metrics and a user study. 
Code will be made public.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduced Prompt-Aware Introverted Attention (PAIntA) block without any training or fine-tuning requirements, enhancing the self-attention scores according to the given textual condition aiming to decrease the impact of non-prompt-relevant information. They also proposed Reweighting Attention Score Guidance (RASG), a post-hoc mechanism seamlessly integrating the gradient component in the general form of DDIM process. This allows to simultaneously guide the sampling towards more prompt-aligned latents and keep them in their trained domain.

### Strengths
* The writing is clear to understand with detailed formulations and figures.

* The results are superior when compared to other methods.

* The phenomena of Appendix B are very interesting, revealing that the original model maintains a similar visual pattern from other parts of images and the PAIntA would increase the probability to respond to the prompts.

### Weaknesses
Some questions below

* Would this method be easily adapted to some modern models, for example, SDXL, SD3, or even FLUX?

* The successful rate of one case with sufficient sampling of different seeds is not clear.

* The experiments are conducted in cases with few instances, so if there are multiple instances (>5), what is the performance?

* Could the method deal with the inpainting tasks with multiple masks in one inference?

### Questions
Please see weaknesses.

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
4

### Summary
This paper introduces a training-free approach to enhancing prompt-guided image inpainting with diffusion models. It proposes two key components: Prompt-Aware Introverted Attention (PAIntA) and Reweighting Attention Score Guidance (RASG), which improve alignment with text prompts. PAIntA adjusts self-attention layers to prioritize text-related regions, while RASG refines cross-attention scores for better prompt consistency. A specialized super-resolution technique ensures high-quality image scaling. Quantitative and qualitative results on MSCOCO confirm the method’s superiority.

### Strengths
The discussion about prompt neglect is promising. 

The proposed solution achieves strong results on evaluation metrics.

### Weaknesses
Some discussion and analysis should be included, see the question part.

The inference time cost should be reported and compared.

How to derive Claim 1? How to define high-quality images?

Will the proposed method work on transformer-based models like SD3 and FLUX?

In Table 2, the bolded aesthetic score is not the best one.

### Questions
The inference time cost should be reported and compared.

How to derive Claim 1? How to define high-quality images?

Will the proposed method work on transformer-based models like SD3 and FLUX?

In Table 2, the bolded aesthetic score is not the best one.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Paper addresses the problem of prompt neglect in text-guided image inpainting. Existing solutions (smartbrush, imagen editor) are argued to have reduced generation quality. The proposed method is training-free. The paper proposes to techniques, Prompt-aware Introverted Attention layer, and Reweighting Attention Score guidance for accurate prompt following and high image quality.

### Strengths
- the hypothesis that the problems of existing methods is based because of the self-attention, and that this problem can be addressed there, is interesting and convincing (even though it is not well explained).
- the qualitative results clearly show the superiority of the proposed method. Also the quantitative results are ok, but they do not seem to indicate the large improvement seen in the qualitative results.

### Weaknesses
-	 the self-attention map analysis (in Appendix B) is important for the motivation of the paper and should be moved to main paper. This would help to provide a motivation in section 3.3. before just stating it in math, helping the reader understand the proposed method.

-	 the explanation of the main idea behind section 3.3 is not well presented. The main idea is the introduction of c_j in the self attention, but what this represent is not well explained in words. 

-	 does the 'introverted' nature make it hard to use information from outside of the impainted region. For example if you ask for an object with a whole behind which the background should continue ? Or a bike in front of a fence, etc. 

-	 section 3.4 should also start out by stating the problem it addresses and how it is planning to address this. I found the presentation not good of this section, and very hard to understand. 

-	 in the user study the results of DreamShaper are better than SmartBrush, but in figure 5 the results of DreamShaper are very bad not following the prompt at all, and SmartBrush is much better. Any explanation, this makes me doubt the correctness/usefullness of the user study.

MINOR points: 

Think would be better to directly put equation of c_j also in (5), and then explain. Try to first explain the main idea, then the details (SOT, EOT, clipping etc). Now the main idea is hard to distill. 

More usage of \citep might make reading easier (e.g. line 96).

Too many forward references in introduction (to future tables and figures and appendices).

References for relevant information to appendix are out of place in the introduction. The main information should be in the main paper; the introduction introduces the most relevant information of the paper.

line 248. Maybe better to keep professional factual style (instead of diary-style 'we did this' 'than that'), so better 'a thorough analysis of Stable Inpainting led to the conclusion...'

### Questions
Overall I found the visual results appealing. The quantitative improvement less so (maybe a new metric should be developed to better show the superiority of the method ?). I found the presentation of the crucial section 3.3-3.4 of bad quality and they need to be improved much. 

- see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the diffusion based image inpainting task. The proposed method is training-free, which modifies the self attention block and use post training alignment/guidance. The experimental results prove the effectiveness of the proposed method.

### Strengths
- The method is intuitively clear and reasonable. The self attention may contain irrelevant information regarding area to be inpainted. The modification to self attention block makes sense. The visualization of attention map proves the efficiency of the method.
- Although a bit heuristic, the training-free nature makes the method easily extensible to other pretrained inpainting diffusion models.
- The proposed RASG is cleverly simple yet effective, which transforms the post training alignment to the form of non-deterministic DDIM. It seems to efficiently avoid noisy latent deviating too far from the original trajectory.

### Weaknesses
 - Lack of experiments on running time. What is the additional time cost associated with the proposed method?
- Lack of ablation study on hyperparameters. How sensitive is the model to different hyperparameters? Espscially $\eta$.

### Questions
Please check the weakness.

(Minor comment) In line 183, it should be VQGAN or VAE within SD, where usually VAE is chosen.

### Soundness
3

### Presentation
3

### Contribution
3
