# Prompt as Knowledge Bank: Boost Vision-language model via Structural Representation for  zero-shot medical detection

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Zero-shot medical detection can further improve detection performance without relying on annotated medical images even upon the fine-tuned model, showing great clinical value. Recent studies leverage grounded vision-language models (GLIP) to achieve this by using detailed disease descriptions as prompts for the target disease name during the inference phase.  
However, these methods typically treat prompts as equivalent context to the target name, making it difficult to assign specific disease knowledge based on visual information, leading to a coarse alignment between images and target descriptions. In this paper, we propose StructuralGLIP, which introduces an auxiliary branch to encode prompts into a latent knowledge bank layer-by-layer, enabling more context-aware and fine-grained alignment. Specifically, in each layer, we select highly similar features from both the image representation and the knowledge bank, forming structural representations that capture nuanced relationships between image patches and target descriptions. These features are then fused across modalities to further enhance detection performance.
Extensive experiments demonstrate that StructuralGLIP achieves a +4.1\% AP improvement over prior state-of-the-art methods across seven zero-shot medical detection benchmarks, and consistently improves fine-tuned models by +3.2\% AP on endoscopy image datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this study, the authors introduce StructuralGLIP, a novel approach to zero-shot medical detection using vision-language models (VLMs). This method leverages structured representations within a dual-branch architecture that enables nuanced alignment between images and textual prompts, significantly enhancing the model's adaptability to new medical scenarios without needing annotated data. StructuralGLIP uses category-level prompts, maintained in a latent knowledge bank, and a mutual selection mechanism for precise cross-modal fusion, thus improving accuracy across diverse medical imaging datasets.

### Strengths
(1)	The paper introduces an effective structural representation by encoding prompts into a knowledge bank and utilizing a dual-branch structure. This approach enables adaptive and context-aware alignment, which is particularly advantageous for complex medical detection tasks.
(2)	StructuralGLIP outperforms traditional zero-shot models by effectively handling both instance-level and category-level prompts, achieving significant improvements across various benchmarks in endoscopy, microscopy, radiology, and more.
(3)	By allowing for zero-shot enhancement, the model can be fine-tuned and then further improved with category-level prompts, a feature well-suited for dynamic medical settings where data annotation is scarce.

### Weaknesses
(1)	The proposed dual-branch structure with a knowledge bank requires complex engineering and computational resources, potentially limiting its accessibility for practitioners in less resource-rich environments. Specifically, the implementation of the knowledge bank and the mutual selection mechanism introduces additional layers of abstraction and computational overhead, which may not be easily replicated or deployed in settings with limited infrastructure.
(2)	The paper may not adequately address the potential data imbalance present in the datasets used for evaluation. Some diseases or conditions may have significantly fewer examples, which could impact the model's performance and generalizability. The evaluation should include a detailed analysis of performance across different classes, particularly those with limited representation, to ensure that the reported improvements are not skewed by over-representation of certain conditions.
(3)	The model's inner workings, particularly regarding how it selects and utilizes prompts, may be difficult for practitioners to interpret, limiting trust in its decisions and making it harder to diagnose potential failures. The lack of transparency in the prompt selection process makes it challenging to understand why the model makes specific predictions, which is a significant concern in medical applications where interpretability is crucial.
(4)	Despite improvements in alignment, there may still be instances of misalignment between visual features and prompts, especially in cases of atypical presentations, which could lead to missed detections. The reliance on textual prompts might not fully capture the nuances of visual anomalies, especially when the visual presentation deviates significantly from the typical characteristics described in the prompts.

### Questions
(1)	To what extent can the findings be generalized to other medical imaging modalities or less common diseases? Are there plans to evaluate the model on broader datasets?
(2)	Besides Average Precision, what other metrics were considered for evaluating model performance? Are there plans to incorporate user feedback or clinical outcomes in future evaluations?
(3)	This paper focuses on zero-shot medical detection, whereas GLIP was initially developed for natural images. Can the proposed method also be applied effectively to natural image datasets?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduce a new zero-shot method for medical Vision-Language Models(VLMs) for detecting unknown targets. To address the prompt umatched with the variations in the medcial images, the authors propose a StructualGLIP desgin with a main and an auxiliary branch encoders for text input and introduce a mutual selcetion mechanism. 
The author explain that the auxiliary branch would work as a knowledge bank where the main branch can extract latent prompt tokens, while the tokens in the knowledge banked are filtered by the mutual selection process.
Overall, the motivation, method, and performance of this work is good enough, but I still need some explaination for some detail, please refer to the weakness and question section. I will consider adjust my rating based on the authors response.

### Strengths
1. This work is aiming for a vital issue in medical image understanding field, which is the generalization capability of foundation models with limit data access. The motivation of improving the existing work is clear and strong, which is the lack of object level prompt and fail to capture the various feature of images during prompt desgin.
2. This work present a novel but efficient method, called StructualGLIP, to increase the model's zero-shot/few-shot performance on various datasets. The desgin of StructualGLIP introduce the knowledge bank and mutual selection process to help prompt design process. This method address several shortcomings of current method and is novela and effective.
3. This method largely increased the zero-shot performance on different medical image datasets across different modalities.

### Weaknesses
1. Line 234, the sentence seems not finished. 
2. One of the major problem of the proposed method is not trainable as the Top-K selection operation is non-differentiable, while previous work is differentiable and thus finetuning would result in better performance. I would suggest include Reparameterization Trick for Gumbel-Softmax to improve your method. Though this work is good enough as a stand-alone method for zero-shot detection. But I see a potential to achieve better performance.

### Questions
1. How to evaluate the quality of the generated prompts by VQA method. As some previous work pointed out, the VLM without medical domain adaptation perform poorly on some medical datasets, especially for radiology datasets.
2. For Prompt as Knowledge Bank ablation study seciton, I would like to see an experiment on the whether adding noisy knowledge (for example, knowledge for another target) would sharply downgrade the StructureGLIP performance. This experiment would the the robustness of the mutual-selection process.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Prompt as Knowledge Bank, a method that encodes prompts into an adjustable knowledge bank, enhancing multimodal models’ accuracy in zero shot tasks by dynamically selecting prompts from prior knowledge. This approach achieves robust performance in high-precision fields like medical imaging, even with limited data.

### Strengths
1. By introducing a dynamic knowledge bank that selects the most relevant prompts, the model achieves more flexible and accurate vision-language alignment.
2. This method performs exceptionally well in unsupervised and few-shot scenarios, maintaining high detection accuracy even with limited labeled data.
3. The prompt generation module extracts information from prior knowledge of unseen classes, enhancing the model’s adaptability and making it suitable for tasks across various domains.

### Weaknesses
1. The introduction of the knowledge bank and prompt generation module increases computational costs, raising demands on hardware resources.
2. The model heavily relies on prompt quality, and low-quality prompts may negatively impact its performance.
3. The impact of the prompt’s LLM on performance is apparent; however, the paper does not analyze how the choice of LLM (e.g., LLaMA, Gemini) affects the results.
4. The complex prompt selection and knowledge bank structure reduce the transparency of the model's decision-making process, posing challenges for clinical applications.
5. There are formatting errors in the paper, such as an unexpected horizontal line near the number 15 in the table 5.

### Questions
1. How does the prompt generation module ensure the creation of valuable prompts for unseen classes without introducing distracting information?
2. How is the accuracy of instance-level contextual prompts generated from visual input for VQA ensured, as this seems crucial to the final experimental performance?
3. How does using alternative LLMs affect the experimental results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a zero-shot object detection model, StructrualGLIP, for medical image-based object detection tasks. The method uses a knowledge bank that stores encoded text prompts, which are later used to select and match relevant image features to form fine-grained structural representations to allow better alignment of image features with the prompt information, achieving accurate, context-aware detection.

### Strengths
1. the paper demonstrates a comprehensive evaluation of four medical image modalities.
2. the paper's representation and structure are mostly clear and easy to follow (although with some language and word choice issues, which will be discussed below).

### Weaknesses
1. The claimed novelty appears to be on the latent knowledge bank and its function to store encoded prompt tokens and later be used at each encoder layer as a vision token selector and vice versa. This is coined as a mutual selection process. The selected information is then merged into the original image and text encoder back at each layer. The entire process is different to a standard contextual prompt method (Fig. 1(a)) but it feels like a quite incremental difference which I don't see much novelty. Furthermore, the MHA, f, and RPN components in Eq. 8-10, which are part of the auxiliary branch, would require training or fine-tuning, otherwise they would not function out-of-the-box given the addition of features would shift the feature distribution. The paper does not specify what data is used for this training, nor if the GLIP model in S4/4-2 also received the same training, making the noise prompt argument questionable.
2. The word choice of "medical detection" bugs me, in medical science detection refers to "detecting diseases" whereas here this is object detection in medical images so this may cause confusion to certain readers.
3. Line 234 looks unfinished.
4. Eq. 6&7, perhaps the Top-P/Q^{max} function can be simplified by using argmax/argsort function?
5. L201/534: "... fine-grained alignment between target descriptions and medical images", L:256 "forming fine-grained structural representations", can the authors clarify what "fine-grained" refers to in those places?
6. L294: "...like BLIP Li et al. (2022a)", is the VQA model BLIP or not? Have you considered other VQA models and would the performance of other VQA models fluctuate your detection results? The performance of StructrualGLIP appears heavily dependent on the VQA model used, as demonstrated by the significant performance variation across different VQA models in Table S8-1/2. Additionally, AutoPrompter + Qwen2-VL-7B achieved 75.0 on CVC, which is higher than StructuralGLIP, suggesting the method's effectiveness is not consistent across all settings. Also, the choice of reporting AP instead of AP50 in Table S9 is unclear and should be justified.
7. L177: I don't entirely agree that zero-shot detection has a real-world clinical need as the clinicians I've encountered would not trust zero-shot settings, in the medical domain, accurate detection/segmentation/diagnosis is the the most important thing. The term "zero-shot enhancement" is also misleading, as it appears to be a novel term for fine-tuning, and the training settings are not clearly described. Specifically, it is unclear if the images and labels of the target dataset (e.g., CVC) were used for StructureGLIP's fine-tuning in the zero-shot enhancement setting. Furthermore, the paper does not address what components of StructureGLIP are trained and what data is used in the zero-shot detection setting.

### Questions
Please address Weaknesses #1,5,6.


------------------
04/12/2024:
I thank the authors' detailed responses. Since the reviewer's post deadline has passed so I am writing my final comments here. 

My conclusion is that I will retain my original score. I believe the paper should improve clarity as many new arguments and technical details surfaced during the discussion period which should have been included in the main manuscript. The novelty and settings should be explored in more depth.

My comments are:

1. Novelty. 

I agree with the authors' argument the image and language encoders do not need to be fine-tuned in your zero-shot detection setting. This I already mentioned in my last comment: "I can understand if the auxiliary branch's language encoder is untrained". My question was whether the modules in Eq. 8 to 10 need training or not? Especially the MHA module in Eq. 8, GLIP has the X-MHA module, did the author reuse the X-MHA weights for the MHA without retraining? The authors mentioned in L263 "we employ a multi-head attention (MHA) mechanism" which reads like it is a new module by the authors' own design. Given an MHA module (as far as I know) should have learnable weights but the authors claim the zero-shot detection setting is training-free, then I find the logic here is contradicted. Furthermore, the authors quoted L210 to demonstrate the training-free paradigm, but that is immediately after Eq.4 and the sentence only describes the encoders. This is an imprecise response to my question so I'm not making a judgment here, but this does make me think the paper should improve clarity. 

The above was not the main point of my original novelty concern, but a spin-off. My original point was that if the authors wanted to demonstrate the "preventing/addressing domain shifting" argument for the novelty, you should consider measuring the actual feature distribution difference between GLIP and StructureGLIP.  The authors revealed in the last comments that the domain referred to the features before RPN, and that is what I think you should demonstrate. To recap the authors' comments, the authors claimed the other methods would concatenate prompt so the feature to RPN becomes CLS token of [target_name, prompt] which causes the domain shift, whereas StructualGLIP did the prompts integration in early layers so StructuralGLIP only has CLS of [target_name] to the RPN, and that addresses the domain shift. Conceptually, maybe it is true but please provide empirical evidence. The final performance is a surrogate measure, which does not directly support your domain shift argument. Finally, StructrualGLIP also fuses additional information in the process, so the CLS token should exhibit some domain shift as you are trying to do domain adaptation, these two arguments also have contradictions to each other. 

Regarding the "addressing noise prompt" argument, I'd imagine the top-P/Q has a certain capability of limiting noise prompts as you only choose the top tokens, so even when you add more prompts, they won't be selected if the network was already trained to have higher attention for the target classes tokens, but that on the other hand, make it trivial argument rather than a novelty.

7. Zero-shot enhancement. After reading the authors' most recent comments, I strongly feel the setting should not be called zero-shot. When the target dataset's labelled data are already used to fine-tune your GLIP base model, then this is weakly supervised. In L175-176, the authors state "We propose a zero-shot enhancement setting. This involves fine-tuning the model on medical datasets first, and then using prompts to further improve performance on unseen medical images", initially I considered this as the model was trained on relevant datasets such as same/similar imaging modalities but different tasks or different datasets. However, if the target dataset itself was used for finetuning for training, then the "further improve performance on unseen medical images" does not hold.

Other comments:
The experiments I requested were for the understanding of how much performance gain was attributable to the design/novelty of StructrualGLIP, i.e., the introduction of the auxiliary branch. The zero-shot enhancement setting (i.e., fine-tuned GLIP) has boosted the performance by a larger margin than the StructualGLIP can bring to GLIP. Also, the choice of the VQA can sometimes affect the AP/AP50 by a noticeable margin (i.e., that 75 AP) but it appears not stable. Then, at least for me, the viability of zero-shot medical detection unfortunately remains questionable.

Once again I appreciate the authors' effort to address my comments but I'm sorry I will retain my original score based on my thoughts above. The authors are encouraged to delve into the details of the novelty and concepts as well as improve clarity of the manuscript.

### Soundness
2

### Presentation
3

### Contribution
2
