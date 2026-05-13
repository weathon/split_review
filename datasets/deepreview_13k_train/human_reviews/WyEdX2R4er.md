# Visual Data-Type Understanding does not emerge from scaling Vision-Language Models

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Recent advances in the development of vision-language models (VLMs) are yielding remarkable success in recognizing visual semantic content, including impressive instances of compositional image understanding. Here, we introduce the novel task of \textit{Visual Data-Type Identification}, a basic perceptual skill with implications for data curation (e.g., noisy data-removal from large datasets, domain-specific retrieval) and autonomous vision (e.g., distinguishing changing weather conditions from camera lens staining). We develop two datasets consisting of animal images altered across a diverse set of 27 visual \textit{data-types}, spanning four broad categories. An extensive zero-shot evaluation of 39 VLMs, ranging from 100M to 80B parameters, shows a nuanced performance landscape. While VLMs are reasonably good at identifying certain stylistic \textit{data-types}, such as cartoons and sketches, they struggle with simpler \textit{data-types} arising from basic manipulations like image rotations or additive noise. 
Our findings reveal that (i) model scaling alone yields marginal gains for contrastively-trained models like CLIP, and (ii) there is a pronounced drop in performance for the largest auto-regressively trained VLMs like OpenFlamingo. 
This finding points to a blind spot in current frontier VLMs: they excel in recognizing semantic content but fail to acquire an understanding of visual \textit{data-types} through scaling. By analyzing the pre-training distributions of these models and incorporating \textit{data-type} information into the captions during fine-tuning, we achieve a significant enhancement in performance. By exploring this previously uncharted task, we aim to set the stage for further advancing VLMs to equip them with visual data-type understanding. %

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduced a new task: visual data-type identification for vision foundation models. This task builds on earlier literature on robustness and domain adaptation of ImageNet models, but tailored for vision foundation models. This task has practical importance for data curation and data cleaning. The authors have conducted extensive experiments (detailed in the "Strengths" section below) and found that scaling model size results in minimal gain, and training with data-type information is a promising direction.

### Strengths
- Interesting taskification of data-type identification. I agree with the usefulness for downstream applications such as data curation and data cleaning.
- Introduced TypeIdent dataset spanning 27 data types across 4 categories (geometric, pixel, semantic, and style)
- Extensive experiments ranging from initial evaluation using 13 model families, error analysis using embeddings and looking into CLIP's pre-training dataset, in-context learning, and fine-tuning with newly created dataset TeDaTy, which incorporates data-type information into image-text pairs.
- Interesting findings such as: scaling model size results in minimal gain, in-context learning (using 7B models) doesn't improve the performance of data-type identification much.

### Weaknesses
 -  The size of the model (i.e. 7B) used for in-context learning experiments might be too small to test the capability of in-context learning. In-context learning with larger models might work so I think it would be better if the authors could clarify this point.

### Questions
- For Section 4.1, when assessing the accuracy of LMMs, aren't there more than one correct answer for data type description? For example, "pencil sketch" could be "pencil drawing", "black and white drawing" etc and "Origami style" could be "low-poly style" etc. How did you deal with these?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research introduces the novel task of Visual Data-Type Identification, which involves identifying the visual data-type of images and holds practical value in data curation and autonomous vision systems. Two datasets were created, featuring animal images modified to represent 27 different visual data-types, and 39 VLMs were extensively evaluated. While VLMs perform well with certain stylistic data-types like cartoons and sketches, they face challenges with simpler data-types. Importantly, the study emphasizes that merely scaling up models is insufficient for improving performance, especially for the largest auto-regressively trained VLMs. By incorporating data-type information and pre-training analysis, the study achieved notable performance enhancements, setting the stage for advancing VLMs with visual data-type understanding.

### Strengths
1) The paper is clearly written and easy to follow.
2) The method introduces a novel task of Visual Data-Type Identification. This task involves recognizing the visual data-type of an image, such as whether an image has been altered, and how it has been changed. This concept is relatively unexplored in the field of vision-language models.
3) The researchers created two datasets containing animal images altered to represent 27 different visual data-types, spanning a wide range of categories. This diversity in the datasets allows for a more comprehensive evaluation of VLMs' performance. They conduct an extensive evaluation of 39 VLMs, covering a wide range of model sizes, from small to extremely large. This comprehensive evaluation provides insights into how different VLMs perform in the context of Visual Data-Type Identification.
4) The study identifies a limitation in existing VLMs. While these models excel at recognizing semantic content, they struggle to understand visual data-types, even when scaled up. This finding highlights the need for a more systematic approach to data-type understanding.
5) The method demonstrates a way to significantly enhance VLM performance by incorporating data-type information and pre-training analysis. This innovative approach improves the models' capability to understand visual data-types.

### Weaknesses
In page 6, the authors identify that LMMs consistently underperform C-VLMs, despite using
LLMs as text models, compared to the smaller text encoders in C-VLMs. The authors propose two potential factors for this difference, namely, "weak alignment" and the "discriminative-generative gap." However, it is suggested that these factors appear to be more like observations rather than fully explored reasons. It is recommended that further investigations are necessary to gain a deeper understanding of these performance differences.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This papers explores the task of visual data type identification to better understand abilities of vision-language models (VLMs). Data-type identification here refers to cases like distinguishing between a natural image and a left-rotation / blurred version of the natural image. The authors construct two datasets containing 27 different datatypes (under 4 categories of geometric, pixel, style, semantic) with one dataset synthetic and the other natural. The synthetic uses generative models and image manipulations for creating all its images. The natural uses web-crawled images. Considering VLMs under contrastive (C-VLMs) and generative (LMMs) categories, they evaluate 39 different VLMs on the task of distinguishing each of these different datatypes. Their results indicate weak performance of both categories, with (the generally larger, newer) LMMs inferior to C-VLMs. Interesting analysis is presented including analysis of feature spaces and fine-tuning these models with data-type based supervision (which gives good results).

### Strengths
1. Valuable dataset contribution 
2. Interesting problem setup 
3. Useful framework for creating more data-type datasets 

4. Assuming correct, interesting and extensive analysis

The authors have performed extensive work evaluating a range of models and extracting multiple insights.

### Weaknesses
1. Method weak with respect to language (leading to possibly wrong analysis)

* A core component of experiments is language based classification (into one of 27 data-types). However, the authors simply use a short description for each data-type (as in appendix) on language side. This could simply mean that the model is not being prompted correctly (and the sensitivity of VLMs to prompting is well-known). If this is the case, the assertions of weaknesses (i.e. inability to distinguish data-types) is not generic. It is only for the selected set of prompts used in paper. 
* For simple verification, I took 10 random images, applied the patch&reshuffle operation, and passed both original and augmented to the online LLava API (https://llava.hliu.cc - this is one of the models evaluated in paper / API uses newer ckpt). While it did not generate the expected term "patch&reshuffle", it generated outputs for the augmented images different to original, consistently involving terms like "collage, mosaic, collage art style" (words somewhat synonymous to augmentation) which indicate some awareness of the model to this patch&reshuffle operation. The original images were not described with these keywords. However, according to Figure 4 in paper, the best LMM (LLava is one of those evaluated) has 0 informedness about patch&reshuffle. For this case, either the metric of informedness or the evaluation protocol does not well-represent the actual abilities of evaluated models like LLava.   


2. Missing LMM evaluation details

* "For a fair comparison, we evaluated LMMs by log-likelihood scoring" - please explain this in detail in the main text (or at least appendix) without directing reader to other papers (in fact the directed papers also re-direct to different papers) . This evaluation is crucial to understand all the reported analysis. Please explain it clearly.

### Questions
1. KNN + Linear Probing
* For C-VLMs, can the analysis in Figure-5 be done with KNN evaluation and linear probing? This will give a clear understanding of how linearly separable the visual features are for each datatype. If they are separable, the idea that it is a misalignment with text modality will be clear, and this could be an interesting contribution. If they are not, maybe even SVM on features could be done as a final test to verify their lack of separation. 
* While t-SNE embeddings are visually appealing, they can often be misleading in my personal experience. 

2. VLM pre-training datasets
* While the text based search is good, it maybe better to use semantic similarity metrics (maybe word vectors, scores like METEOR) to create a more comprehensive vocabulary for each data type (e.g. PATCH AND RESHUFFLE can have more words like collage, mosaic). This could retrieve more images similar to the setup. 

3. The reasoning for weakness
* Given how simple supervision helps a lot, the weaknesses could be attributed to a language-image mismatch in these models. Particularly, if the train set rarely contains these language terms. Can any simple experiments directly negate / verify this hypothesis?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
