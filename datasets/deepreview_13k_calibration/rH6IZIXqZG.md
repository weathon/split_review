# Diffusion Preference Alignment via Relative Text-Image Contrast

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Aligning Large Language Models (LLMs) to human preferences has become a prominent area of research within language modeling. However, the application of preference learning to image generation in Text-to-Image (T2I) models remains relatively unexplored. One approach, Diffusion-DPO, initially experimented with pairwise preference learning in diffusion models for individual text prompts. We propose Diff-contrast, a novel method designed to align diffusion-based T2I models with human preferences. This method utilizes both prompt-image pairs with identical prompts and those that are semantically related across different modalities. Additionally, we introduced a new evaluation task, style alignment, to address the issues of high cost, low reproducibility, and poor interpretability associated with current evaluations of human preference alignment. Our results show that Diff-contrast surpasses existing techniques, e.g. Diffusion-DPO, in tuning Stable Diffusion versions 1.5 and XL-1.0 across both automated evaluations of human preference and style alignment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose a new diffusion alignment method based on RPO. They also provide a newly selected subset of the Pick-a-Pic V2 dataset for style transfer. They conduct experiments in comparison with baselines including Diffusion-DPO and observe higher win rates.

### Strengths
This paper aims to tackle an important and interesting problem, text-to-image diffusion alignment. Qualitatively, the proposed method seems to deliver good results for the tasks experimented in this paper.

### Weaknesses
My main concern about this paper lies in its novelty.
1. The first major contribution of this paper is a simple adaptation of RPO to diffusion models. While it seems to provide decent performance, the technical novelty is not very significant.
2. The second major contribution is the so-called “new” task “style alignment”. This task is identical to the well-established task style transfer. In fact in the definition the authors provide, they describe it as “Style alignment aims to fine-tune T2I models to generate images that align with the offline data to achieve style transfer on T2I models” (Line 320-321). Just rebranding it as “alignment” does not make it an actual novel task.

Besides novelty, I also have the following concerns regarding the evaluations conducted in this paper:

3. Style transfer task has a well-established evaluation metric, i.e. gram matrix distance. While FID can also tell part of the story, adding the standard metric can be better.

4. In the human preference evaluation, the authors only provide the win rate as their comparison results (they claim that they have provided the average scores in Line 378, however, I personally could not find it). Win rate cannot provide the information of the improvement margin gained by the proposed method. In other words, it is possible that the proposed method wins 70% of the time but still has a lower average score when all the winning cases are won by small margin and all the losing cases are lost by large margin. I think providing the raw scores is essential for this comparison.

Finally, I would like to make some suggestions about the general writing of this paper:

5. This paper is also structured in a way that mixes prior work with their contributions. I would suggest a clearer cut between the literature and the new contribution by including proper related works and background sections in the main paper if the authors ever consider restructuring the paper.

### Questions
It would be great if the authors can address the weakness mentioned above.
In addition, I am wondering if the authors can provide additional information about how they define the multimodal embedding function $f$.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors introduce the Diff-contrast model combining the diffusion model with the RPO strategy. A novel loss function and style alignment dataset are proposed. In the style alignment task, experiments prove the advantage of the proposed Diff-contrast compared with SDXL model, SFT-SDXL and DPO-SDXL.

### Strengths
This paper continues the previous research on human preference in the Text-to-Image area, and constructs a new loss function by introducing a relative strategy from LLM area. At the same time, in order to successfully construct the loss, a corresponding reference dataset is constructed, and the effectiveness of the method is verified by comparative experiments.

### Weaknesses
1. Similar to the Diffusion-DPO approach, this article is more like a simple change of strategy. There is no obvious innovation.
2. Personal preference is achieved in T2I primarily through textual descriptions. This paper argues that the task of reconstruction is mainly through the consistency of the generated samples and reference datasets. However, the real massive data samples have been trained and integrated into the pre-trained model during the training phase.

### Questions
1.  More comparisons with LoRA methods need to be verified. Since the style change of images in the T2I task can be achieved by way of LoRa training.
2. Images in the Figure 1 need to compare with the other generation of similar style images.
3. It is necessary to compare this strategy with other T2I models, like Flux 1.0 and SD3, to show its superiority. Rather than just comparing it to the base model.
4. The generated results in each figure should be displayed with quantitative evaluation indicators to demonstrate their superiority.

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
This paper aims to align diffusion models with human preferences by optimizing relative preferences. Previous work uses a reward model to optimize the diffusion model but might suffer from high computational cost and fail to accurately capture human preferences. This paper proposes Diff-contrast loss along with contrastive weighting to enable the diffusion models to learn to align the preference effectively from contrasting images generated from different prompts. Moreover, this paper contributed a task named Style Alignment along with a dataset to aid in the evaluation of preference alignment methods without human annotators. The experiment results indicated its effectiveness with performance compared to other baselines.

### Strengths
1. The paper is well-structured overall and easy to follow with good clarity in writing.
2. This paper presents a new method to utilize the information in the prompt pairs for preference alignments for diffusion models and the originality is sufficient.
3. The significance of this paper is good with the aim of helping diffusion models generate images that align better with human preference in terms of image details or overall expression.
4. The qualitative comparison of the proposed method and other baselines shows the effectiveness of this method with better image quality.

### Weaknesses
1. The paper contributed a dataset of three styles for the evaluation of style alignment, however, the generated results are evaluated with FID scores that might not fully capture the information of the styles. The FID score, while useful for evaluating the overall quality of generated images, may not be sensitive enough to capture subtle stylistic nuances. It primarily measures the statistical similarity between two sets of images, and might not reflect the specific characteristics of style transfer, such as texture, brush strokes, or color palettes.
2. There are several minor writing suggestions:

- Page 2 line 77 "Diffusion-DPO (Wallace et al., 2024) and incorporates Direct Preference Optimization (DPO) (Rafailov et al., 2023) into"

- The notation of the formulas needs to be further clarified or rearranged. Such as moving the definition of preference data $(y^w, y^l, x)$ or the notation of $w, l$ before the equations (1) and (2) to explain what $w, l$ are in the equations; $\omega_{i, j}$ in equation (2) refers to the contrastive weight but was not indicated until section 2.1.

- The bond fonts in Table 1 are not clear in meaning.

- A brief discussion on the metrics in 4.1 would be helpful.
3. See the questions below.

### Questions
1. The styles (Van Goph, Sketch, and Winter) do not seem to be parallel. How are the styles for the style alignment task selected? Is there any specific concern when the dataset for style alignment is constructed?
2. The images in the datasets are generated with image editing models, and how do you guarantee the generated images fit human preference in terms of styles? If not, how do the authors make sure the style alignment task is helpful for the evaluation of preference alignment?
3. For the two-stage fine-tuning experiments for style alignment, is there any specific reason to use SFT along with SFT/DPO/Contrast instead of using the same methods twice?
4. In abstract lines 50-51, the authors mentioned that "both prompt-image pairs with identical prompts and those with semantically related content across various modalities", what does the prompt-image pairs with semantically related content mean? Does it refer to the contrastive weight in section 2.1?

### Soundness
3

### Presentation
2

### Contribution
3
