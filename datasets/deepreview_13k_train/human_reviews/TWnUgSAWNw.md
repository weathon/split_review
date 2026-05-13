# Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent advancements in multimodal models highlight the value of rewritten captions for improving performance, yet key challenges remain. For example, while synthetic captions often provide superior quality and image-text alignment, it is not clear whether they can fully replace AltTexts: the role of synthetic captions and their interaction with original web-crawled AltTexts in pre-training is still not well understood. Moreover, different multimodal foundation models may have unique preferences for specific caption formats, but efforts to identify the optimal captions for each model remain limited. In this work, we propose a novel, controllable, and scalable captioning pipeline designed to generate diverse caption formats tailored to various multimodal models. By examining Short Synthetic Captions (SSC) towards Dense Synthetic Captions (DSC+) as case studies, we systematically explore their effects and interactions with AltTexts across models such as CLIP, multimodal LLMs, and diffusion models. Our findings reveal that a hybrid approach that keeps both synthetic captions and AltTexts can outperform the use of synthetic captions alone, improving both alignment and performance, with each model demonstrating preferences for particular caption formats. This comprehensive analysis provides valuable insights into optimizing captioning strategies, thereby advancing the pre-training of multimodal foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies the roles of (1) short description caption (2) dense caption, and (3) AltText in training multi-modal models.

### Strengths
- The paper is well-motivated and grounded in a thorough analysis of various captioned datasets used for training multimodal models. This analysis offers valuable insights that effectively inform the proposed solution.
- The paper makes an important conclusion that AltText is valuable in training MLLMs, providing guidelines for future research.
- The experimental studies are comprehensive, encompassing three different multimodal models: CLIP-style models, ViT-LLM models, and diffusion models.

### Weaknesses
 - While the performance of models trained on different data ratios is presented, there is no guidance on how to determine the optimal ratio.
- There is no discussion regarding the release of the trained captioning models or the datasets, which could limit the impact of this work.

### Questions
The human-annotated Stage-1-1M and Stage-2-HA datasets are valuable, and could be easily hosted on HuggingFace. Will these datasets be made available for future research?

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
The paper studies the impact of using synthetic captions in foundational vision-language models such as contrastive models, multimodal LLMs and diffusion models. The paper presents hierarchies of synthetic captions, SSC, DSC and DSC+ based on the density and length of captions and studies them across 3 broad categories of VL models. It presents results on a combination of baseline AltText and synthetic captions to understand ratios and setups that affect model performance.

### Strengths
1. The paper studies an important problem : understanding the impact of synthetic captions (a rapidly emerging paradigm) in conjunction with the baseline AltText captions.
2. For the models studied, such as CLIP, MM1 and SD3, the authors perform comprehensive evaluations on a wide-range of tasks. For CLIP, the authors study performance on retrieval and classification, for MM1, the authors study VQA and hallucination benchmarks and for diffusion the authors study object-centric and image fidelity metrics.

### Weaknesses
1. My biggest concern is that the findings are not generalizable enough.
(i) For example, findings on CLIP will not be applicable to SigLIP [1], MM1 results will not translate to Qwen-VL [2], and findings on SD3 cannot be applied on the PixArt [3] family of models. Since the paper seeks to present insights into the impact of synthetic captions, the authors should perform, for each family of models, experiments on other models which vary widely in their architecture, loss functions etc. Specifically, the architectural differences between CLIP and SigLIP, such as the use of a different normalization scheme and training objective, could lead to different behaviors with synthetic captions. Similarly, the decoder architecture in diffusion models like SD3 and PixArt differ significantly, potentially impacting how they leverage synthetic captions. The paper's conclusions are thus limited by the narrow selection of models.
(ii) The synthetic captions adopted in this work is a function on top of human generated captions. Will all of the results still be valid if a different sampling of the human annotators is performed? The reliance on a single set of human annotations introduces a potential bias, as different annotators may emphasize different aspects of an image, leading to variations in the generated synthetic captions and potentially affecting the observed trends.

2. The findings are not necessary novel; for example, the fact that a mix of 50% synthetic+AltText captions for Diffusion models has been well reported in RECAP [4] and SPRIGHT [5]

### Questions
1. What is the reason of using synthetic captions as a LLM re-write on top of the human captions? I notice the results in Table A7-9, and only LLM-generated captions are not far away from the approach taken in the paper. In fact, I am confident if better MLLMs such as Llava-1.6 and CogVLM are used, this gap in performance would be closer.
2.  The captioner is MM1 and the MLLM used is MM1. Is there an impact if another captioner was used?
3. zero-shot results of DSC can be significantly improved with linear probing -- what sort of linear probing is performed? If linear probing helps and is independent of the type of captions used, then do the zero-shot findings still hold?
4. Some information on the demographics of the human captioners leveraged would be helpful.
5. The reason why DSC is restricted to 78 tokens is because CLIP has the same token limit. If CLIP was not used, would both DSC and DSC+ be needed?
6. Are there any findings if Stage-1-1M and Stage-2-HA are reversed?
7. The Average Number of Assertions (ANA) pipeline is very similar to https://arxiv.org/pdf/2311.01477; are there any major differences?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the interplay between alt text and synthetic captions as training data for training multimodal foundation models. It finds that overall, a mixture between alt text, short, and long synthetic captions is advantageous, with different preferences between models and tasks.

### Strengths
Overall the methodology appears sound and comprehensive. The array of tests provides insight into how to best combine caption data sources for multimodal training. I found particularly interesting the conclusions about the differing types of information provided by each – e.g. CLIP benefiting from the diversity of short alt texts while MLLMs may derive further benefit from longer, descriptive captions.

### Weaknesses
The synthetic captions are derived from a custom model (Section 3) and thus it is not clear to what extent the results would generalize to synthetic data produced by other models or those used in other works.

### Questions
Similarly to your AFC, have you tried rewriting or fusing alt texts to form short synthetic captions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the impact of synthetic captions on training CLIP, MLLM and a Diffusion Model. Specifically, it compares the effects of training with short versus dense captions and examines the outcomes of combining synthetic captions with original AltTexts. Additionally, the authors introduce two custom human-annotated datasets aimed at reducing hallucinations in the captioner—one tailored for short captions and the other for dense captions.

### Strengths
The paper addresses an interesting and important question by evaluating how captions with varying levels of visual detail impact the downstream performance of multimodal models. In addition, it approaches this evaluation more holistically than prior research by including a range of multimodal model types in the comparison.

Furthermore, the use of combined synthetic captions and original AltText represents an interesting direction that, to my knowledge, has not been extensively explored in previous studies.

### Weaknesses
While the paper addresses a relevant topic, several of the experiments appear similar to those in prior research, which limits the novelty of the findings. For example, as the authors note, Betker et al. [1] conducted a similar experiment evaluating the effects of long versus short synthetic captions on the downstream performance of diffusion models, reaching comparable conclusions. Similarly, Chen et al. [2] presented an experiment analogous to the MLLM analysis here, examining the impact of long versus short synthetic captions on downstream tasks. Although the models differ, the ideas and conclusions appear similar.

Additionally, while the authors justify training a custom captioner on a new dataset by claiming existing multimodal LLMs are prone to hallucinations, no experiments directly compare the effects of training with captions from, for example, LLaVA [3] or TinyLLaVA [4] (or newer and stronger models) versus the proposed captioner. Including such a comparison would enhance the reliability of the results. Moreover, the decision to create custom datasets is unclear, as similar datasets for short [3] and long captions [4] already exist. Further clarification on how the proposed captioning dataset differs from these existing resources would strengthen the paper.

### Questions
It seems like the following citations is missing? The paper explores the effect of synthetic versus AltText captions when training CLIP.

[1] Nguyen et al. Improving multimodal datasets with image captioning. 2023

### Soundness
3

### Presentation
3

### Contribution
2
