# GIST: Generating Image-Specific Text for Fine-grained Object Representations

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Recent vision-language models outperform vision-only models on many image classification tasks. However, because of the absence of paired text/image descriptions, it remains difficult to fine-tune these models for fine-grained image classification. In this work, we propose a method, GIST, for generating \textit{image-specific} \textit{fine-grained} text descriptions from image-only datasets, and show that these text descriptions can be used to improve classification. Key parts of our method include 1. prompting a pretrained large language model with \textit{domain-specific} prompts to generate diverse fine-grained text descriptions for each class and 2. using a pretrained vision-language model to match each image to label-preserving text descriptions that capture relevant visual features in the image. We demonstrate the utility of GIST by fine-tuning vision-language models on the image-and-generated-text pairs to learn an aligned vision-language representation space for improved classification. We evaluate our learned representation space in full-shot and few-shot scenarios across four diverse fine-grained classification datasets, each from a different domain. Our method achieves an average improvement of $4.1\%$ in accuracy over CLIP linear probes and an average of $1.1\%$ improvement in accuracy over the previous state-of-the-art image-text classification method on the full-shot datasets. Our method achieves similar improvements across few-shot regimes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method for generating and matching fine-grained descriptions for images, which is named GIST. The proposed method GIST adopts a large language model to generate fine-grained texts with carefully designed prompts and then uses pre-trained CLIP to match the images with generated texts.
Based on the generated image-text pairs, this paper adopts a pre-trained CLIP and trains a classifier for downstream tasks. The experiments are conducted in both full-shot and few-shot settings. The experimental results show that the proposed GIST outperforms previous approaches and the baseline CLIP.

### Strengths
1. This paper presents a new method named GIST for fine-grained classification.
2. The proposed method adopts a large language model to generate domain-specific class descriptions and matches the texts and images with a pre-trained vision-language model.
3. This paper trains a CLIP classifier with the generated and matched descriptions.
4. The proposed GIST achieves good results on several benchmarks with full/few-shot settings.

### Weaknesses
1. I'm concerned about the technical contribution of this paper. Using a large language model to generate/augment text for CLIP training has been explored in several works [1,2]. 
2. This paper lacks the ablations about matching texts and images. It's unclear whether the matching based on a pre-trained CLIP will impact the downstream tasks. In addition, I'm concerned about how many captions are matched to one image and whether more captions will help.
3. This paper lacks studies on the impact of fine-tuning CLIP and whether more data (images) will further improve.

### Questions
1. What are text inputs for the proposed GIST, the standard text prompts with labels or the text descriptions?
2. I'm concerned about the performance of fine-tuning CLIP with both short text descriptions and the original texts, and how about fine-tuning the CLIP with longer texts while fine-tuning classifiers with shorter descriptions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a method of generating image-specific text by prompting LLM for fine-grained object representations. In particular, the authors provide a three-step workflow, i.e., 1) prompting GPT-3 with domain-specific prompts to generate detailed  candidate text descriptions; 2) using CLIP to match each training each to the candidate text set; 3) summarizing the matched text via LLM to construct image-text pairs for fine-tuning CLIP image encoder. In addition, the learned representation is useful for fine-grained image classification. Besides, the authors provide a new fine-grained image classification dataset, Fitzpatrick40. Experimental results proved the effectiveness of the proposed method.

### Strengths
(1) The motivation of prompting LLM for fine-grained classification is well presented.

(2) The explanations and illustrations of the three-step workflow is well-formulated and mostly clear.

### Weaknesses
(1) The motivation of prompting LLM for visual classification is not that novel to the community and the authors listed (Maniparambil et al., 2023) as an example.

(2) The contribution is limited since the core idea is the same as typical data labeling workflow that uses LLM. More specifically, during prompting LLM, the user-provided prompt is not coming for free, it is also a kind of human knowledge or preference prior. There is no discussion on this difficulty of prompt preparation as compared to typical easy prompt such as “a photo of class name”. Thus, the workflow of generating image-text pairs has no difference from data labeling workflow that uses LLM.

(3) In the experiments, Table 1, the proposed workflow which uses GPT-3, CLIP and intricate prompts, does not get significant improvement over FLYP which uses CLIP and a typical easy prompt, though the comparison setting is unfair.

(4) The most conflicting method (Maniparambil et al., 2023) is not compared in the experiments.

### Questions
No.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to enhance VL model ability for few-shot classification. Using the names of interested classes, LLM generates diverse and descriptive explanations of each class. The CLIP model matches each image in the dataset with the generated explanations, resulting in an image-synthetic caption dataset. Using the dataset, the CLIP model can discriminate the fine-grained information better. The proposed method achieves better results than comparable methods.

### Strengths
+ The proposed method is simple, straightforward, and sound. 

+ The paper is clearly written and easy to understand.

+ The proposed method achieves better results than comparable methods.

### Weaknesses
 - The proposed method requires domain (dataset) specific designs such as prompts for LLM. However, in a few-shot setting, it is hard to determine the designs because of the scarcity of validation and test sets. This makes the proposed method less general to real-world few-shot tasks.

- The paper lacks of comparison with other fine-tuning techniques such as prompt tuning approaches. Please analyze and compare with other families of VL finetuning.

- If I understood correctly, the proposed method requires full images for the target domain. In a real-world setting, it may be hard to obtain such images, especially for medical images. 

- Why is a summary is required? We can see the performance improvement by doing this, but I found no proper explanations for why.

- Manual cleaning mentioned in Section 5 seems not fancy. In a specific field, manual cleaning requires an expensive effort of experts such as the medical field. In addition, instead of manually cleaning, we can make labels for more images under the same effort, which is likely to produce much more improvements than manual cleaning.

### Questions
- Instead of the process of generating captions using LLM and matching with CLIP, how if the trained vision-llm models (e.g., BLIP-2, Flamingo) are used to generate captions?

- The generated explanations are exclusively matched to images? Or the same captions can be matched to multiple images? If so, please statistics how frequently each explanation is matched to the images.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
