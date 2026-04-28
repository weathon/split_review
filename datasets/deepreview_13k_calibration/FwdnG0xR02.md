# Balancing the Picture: Debiasing Vision-Language Datasets with Synthetic Contrast Sets

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
Vision-language models are growing in popularity and public visibility to generate, edit, and caption images at scale; but their outputs can perpetuate and amplify societal biases learned during pre-training on uncurated image-text pairs from the internet. Although debiasing methods have been proposed, we argue that these measurements of \textit{model bias} lack validity due to \textit{dataset bias}. We demonstrate there are spurious correlations in COCO Captions, the most commonly used dataset for evaluating bias, between background context and the gender of people in-situ. This is problematic because commonly-used bias metrics (such as Bias@K) rely on per-gender base rates. To address this issue, we propose a novel dataset debiasing pipeline to augment the COCO dataset with synthetic, gender-balanced contrast sets, where only the gender of the subject is edited and the background is fixed. However, existing image editing methods have limitations and sometimes produce low-quality images; so, we introduce a method to automatically filter the generated images based on their similarity to real images. Using our balanced synthetic contrast sets, we benchmark bias in multiple CLIP-based models, demonstrating how metrics are skewed by imbalance in the original COCO images. Our results indicate that the proposed approach improves the validity of the evaluation, ultimately contributing to more realistic understanding of bias in vision-language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, author target the problem of data debiasing, and propose a pipeline to augment the COCO to generate an synthetic, gender-balanced contrast sets, by editing the person in the image without shifting the background, to prevent spurious relationship between gender and background. By using the generated dataset, authors shows that the conventional metric for measuring model bias, are highly biased by the bias from dataset. Author appeal for attention on dataset debiasing to the community.

### Strengths
1. Author identify an vital problem in existing metric of measuring model debiasing, is less accurate due to being skewed by dataset bias. This provide new insight to the community and could be potential impactful.
2. Author also identify background bias as a vital source for gender bias by showing result from spurious correlations classifier. 
3. Author provide viable framework to generate balanced dataset without spurious relationship, and propose a dataset under this framework.
4. Most discussion of the paper is clear and easy to follow.

### Weaknesses
1. In this work, author only adopted COCO Captions dataset for tasking and gender as the debias attribute. It would be more convincing if author provide discussion and empirical result of how does insight draw from this work also applicable to other dataset and attribute. Specifically, the method relies on the ability to edit the person in the image while preserving the background. This might be challenging for datasets where objects are more tightly integrated with their surroundings, or where the attribute of interest is not easily isolated. For example, extending this to attributes like age or race might require more sophisticated image manipulation techniques, and the success of the approach might vary significantly across datasets with different characteristics.

2. In section 3 and 5, author shows that standard metric are biased by spurious relationship in dataset itself. However, there's no followup discussion on how to measure model bias over constructed balance, spurious-relationship free dataset. While the paper highlights the problem of dataset bias in evaluating model bias, it does not propose a concrete solution for measuring model bias on the debiased dataset. The paper shows that current metrics are flawed, but it does not offer an alternative way to evaluate model bias once the dataset is balanced and free of spurious correlations. This leaves a gap in the methodology, as it is unclear how to quantify the true model bias after the dataset has been debiased.

### Questions
The insight that spurious relationship between background pixel and foreground object seems to be generalizable beyond VLM and caption based dataset.  It would be helpful if authors can also provide some discussion on that. Also how does this insight be potential beneficial to other field like bias-free image generation?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel gender-debiased dataset named GENSYNTH. The dataset aims for gender balance and context independence, achieved through the use of image generation models guided by prompts, which allow for control over the gender expression of the generated images, ranging from masculine to feminine. The experimental results, as depicted in Table 3, demonstrate that the utilization of the GENSYNTH dataset effectively reduces gender bias.

### Strengths
+ Addressing this issue is crucial for the machine learning research community.
+ The methodology employed presents a plausible solution for mitigating gender bias.
+ Utilizing generative models as a strategy for reducing bias holds significant promise.

### Weaknesses
I recognize that this paper addresses a critical issue; however, I believe it is not yet suitable for publication due to numerous absent discussions.

- Technical novelty is weak:
While the methodology is intriguing and the results are persuasive, the strategy appears somewhat simplistic, essentially constituting an application of generative models. The core idea of using generative models to modify gender attributes is not novel in itself, and the paper lacks a deep exploration of the specific challenges and innovations in adapting these models for the task of bias mitigation. The paper does not sufficiently detail how the chosen generative model is uniquely suited for this task compared to other available models, nor does it discuss the potential limitations of the chosen model in this specific context. A more thorough analysis of the model's architecture and its suitability for the task is needed.

- More detailed discussion should be conducted:
The instance depicted in Fig. 2 is gender-neutral. Nonetheless, in certain scenarios, other contexts might exhibit stronger gender biases, such as facial hair, attire, etc. Thus, merely manipulating images to appear more masculine or feminine does not consistently resolve the issue. The authors should explore and discuss the potential repercussions of generating new "noisy" or "misleading" examples. The paper needs to address how the method handles cases where gender expression is more complex or nuanced, and how it avoids creating unrealistic or stereotypical representations. The discussion should include an analysis of the types of artifacts that can arise from the generative process, such as unnatural textures or distortions, and how these artifacts might affect the evaluation of bias.

- More detailed discussion on bias freeness is needed:
The experimental results section predominantly presents numerical data, with a relatively modest improvement in performance compared to the baseline. The authors are encouraged to illustrate typical instances where gender bias mitigation is evident, as well as highlight persisting challenges, acknowledging that complete eradication of gender bias is unfeasible with the proposed method. The paper would benefit from a qualitative analysis of the generated images, showing examples where the method successfully reduces bias and examples where it fails. This would provide a more nuanced understanding of the method's strengths and limitations. The authors should also discuss the metrics used to evaluate bias and whether these metrics are sufficient to capture the complexities of gender bias.

- The potential introduction of new biases requires careful consideration:
The generative models are already acknowledged to be biased. The authors should thoroughly investigate potential risks associated with utilizing generative models for debiasing objectives. For example, in Fig. 3, adjustments are made to not only facial features but also skin color and clothing color, potentially leading to the inception of new biases. Furthermore, it is observed that the generative models seem to underrepresent Asian faces, potentially introducing additional biases. The paper needs to include a more detailed analysis of how the generative model's inherent biases might propagate into the generated dataset. A discussion of how the authors attempted to mitigate these biases, or at least acknowledge their presence, is essential. The paper should also explore the potential for the method to create new forms of bias, such as reinforcing stereotypes or creating unrealistic representations of certain groups.

### Questions
Please answer to my “weakness part.”

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to address and understand biases in vision-language datasets, specifically the bias between the background context and the gender of persons referenced or appearing in the data. Demonstrating their approach on the COCO Captions dataset with CLIP-based models, the authors propose a method for modifying the dataset with synthetically generated “contrast sets” where the gender of the subject is edited using InstructPix2Pix and the background fixed, such that the dataset can be balanced in gender.

### Strengths
* This work tackles the important problem of understanding and addressing dataset bias.
* The paper is relatively easy to understand.
* To the best of my knowledge, this appears to be a novel approach for editing an attribute (gender) in an image and observing how it impacts dataset bias.

### Weaknesses
 * Looking at qualitative examples of the GenSynth and GenSwap gender-edited images (Fig 1 in the appendix), the resulting images still have obvious artifacts, even after the various steps taken to verify quality and filter out low-quality images. From what I can tell, the authors have not really addressed how these artifacts may be a factor in their results.
* I would be interested to see a comparison with other image editing methods other than InstructPix2Pix that may produce higher quality contrast sets. How does varying the quality of the edited images affect the observed gender biases for the different models?
* The work only debiases for a single attribute (gender), and does not delve into what debiasing multiple attributes may look like. This limits the potential impact of this work (it’s not quite usable in practice, and the observations about bias in CLIP are also limited to gender only).
* The instructions for InstructPix2Pix only use gender editing, and does not control for other variables (e.g. skin tone, race).

### Questions
* The Wang et al. 2021a paper is referenced frequently; it would be useful to the reader to discuss in more depth how this work differs from the former.
* There is limited discussion of the CLIP models used; given how prominently they feature in the experiments, I would expect the authors to provide more background for the reader.
* In general, I found that the Appendix contained a lot of relevant information (e.g. qualitative examples) that I would have liked to see in the main paper.
* Section 3.2 “Extracting Image Gender Labels...”: The authors mention that the “images may be incorrectly labeled as undefined”. What percentage of the images were mislabeled?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
