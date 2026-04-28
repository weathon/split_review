# LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 6, 8, 5

## Abstract
Following the impressive development of LLMs, vision-language alignment in LLMs is actively being researched to enable multimodal reasoning and visual input/output. This direction of research is particularly relevant to medical imaging because accurate medical image analysis and generation consist of reasoning based on a combination of visual features and prior knowledge. Many recent works have focused on training adapter networks that serve as an information bridge between image processing (encoding or generating) networks and LLMs; but presumably, in order to achieve maximum reasoning potential of LLMs on visual information as well as language, image and text features should be allowed to interact more freely. This is especially important in the medical domain because understanding and generating medical images such as chest X-rays (CXR) require not only accurate visual and language-based reasoning but also a more intimate mapping between the two modalities. Thus, taking inspiration from previous work on the transformer and VQ-GAN combination for bidirectional image and text generation, we build upon this approach and develop a method for instruction-tuning an LLM pre-trained only on text to gain vision-language capabilities for medical images. Specifically, we leverage a pretrained LLM’s existing question-answering and instruction-following abilities to teach it to understand visual inputs by instructing it to answer questions about image inputs and, symmetrically, output both text and image responses appropriate to a given query by tuning the LLM with diverse tasks that encompass image-based text-generation and text-based image-generation. We show that our model, LLM-CXR, trained in this approach shows better image-text alignment in both CXR understanding and generation tasks while being smaller in size compared to previously developed models that perform a narrower range of tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates the issue of multi-modal data alignment in large language models, using medical images and reports. 

In terms of contributions, the authors propose a bidirectional reasoning generation mechanism that encodes images into tokens, allowing large language models to process and generate both text and images. In model training, a two-stage fine-tuning method is utilized, which not only captures the latent feature distribution of images but also imposes constraints on the model's representation of high-quality samples. 

Overall, this paper offers new perspectives on the processing of multi-modal data in large language models, demonstrating their value in the field of medical image processing.

### Strengths
1. The author demonstrates the potential of large language models in radiological diagnostics, offering greater flexibility than previous methods in generating diagnostic reports or creating images.

2. Inspired by VQ-GAN, the author ingeniously encodes images into tokens and integrates these image tokens into the large language model (LLM) for fine-tuning, achieving alignment of language and image features in the feature space.

3. The author defines four tasks in this paper, particularly emphasizing the use of the CHATGPT API for Visual Question Answering (VQA), which further strengthens the association between images and text in the feature space. This part of the design is very interesting.

4. During training, the dataset is cleansed, with initial learning of image latent features using low-quality data; the LLM is fine-tuned using the cleansed data.

### Weaknesses
1. The experiments in this paper were conducted using only one dataset. As the author mentioned, the quality of the dataset used was limited, necessitating adjustments in the training strategy.

2. The paper lacks visualization of the alignment of images and text in the feature space. Particularly when using VQA for data augmentation, the questions posed by GPT contain rich prior information, focusing the text more on the key lesion areas in the images. I believe that appropriate visualization is necessary to demonstrate the effectiveness of incorporating VQA.

### Questions
1. This paper demonstrates the potential application of LLMs in the medical field, but the content of the study extends beyond generating diagnostic reports from radiological images. I hope the author could further clarify in the introduction whether there are specific application scenarios for this research.

2. In '2.1 CLINICAL INFORMATION-PRESERVING CXR TOKENIZATION', the author mentions '...causes loss of clinically important information such as characteristics of microscopic lesions...'. However, in this study, generating image tokens is key to aligning images with text during LLM fine-tuning. Is the mere use of L2 reconstruction loss sufficient to effectively reduce the loss of clinical information? Could there be an enhancement of features in the design of the module network structure? I think this is a very important challenge in this paper, and I hope the difference in experimental results before and after the introduction of L2 reconstruction loss can be explained.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript introduces an instruction-tuning technique geared towards amplifying the image comprehension and generative capabilities of a text-exclusive LLM for CXR imagery interpretation and generation. The outcomes indicate a top-tier performance in both image-text understanding and generative capacities, surpassing earlier models in the field.

### Strengths
The method of instruction-finetuning effectively elevates the LLM's capability to intricately map vision-image modalities. Consequently, it markedly excels in tasks like CXR-to-Report generation, CXR-VQA, and Report-to-CXR generation, outshining the open-sourced versions of models such as XrayGPT and UniXGen.

### Weaknesses
1. The paper's premise relies on the fine-tuning of LLM across multiple instruction tuning tasks. This approach isn't particularly novel, as numerous large-scale medical models adopt a similar strategy but with a broader functional range. Both the innovation in method and the paper's applicative contribution seem to be lacking.
2. The LLM-CXR, when compared with the open-sourced versions of XrayGPT and UniXGen, appears to be unfair. It's noted that these models aren't trained on a consistent instruction tuning dataset. It's recommended that a uniform dataset is utilized for training before making such comparisons. Furthermore, there's an evident absence of comparison with existing LLM+instruction tuning models, such as Med-PaLM and Med-PaLM 2.
3. The paper's comparative methods across various understanding and generative tasks aren't comprehensive. For instance, in the realm of report generation, several contemporary methodologies exist, such as "Dynamic Graph Enhanced Contrastive Learning for Chest X-ray Report Generation, CVPR 2023."
4. The evaluation metrics used for report generation seem lacking in depth. For instance, within the paper (table 1), only the AUROC scores across six categories are reported, while prior research typically reports the average Precision/Recall/F1-score across all 14 categories.
5. The paper's writing style isn't fluid and contains multiple errors, hindering smooth reading and comprehension. For instance, repetitive phrases like "… generate these VQAs as shown as shown in …" and grammatical mistakes like "During the fine-tuning process …" detract from the paper's clarity.

### Questions
Methodology Concerns:
1. How does the instruction-finetuning method differentiate itself from existing large-scale medical models that employ a similar strategy?

Comparative Analysis:
1. Is the comparison between LLM-CXR and the open-sourced versions of XrayGPT and UniXGen made on a consistent dataset?
2. Why hasn't the paper compared its methodology with existing LLM+instruction tuning models, such as Med-PaLM and Med-PaLM 2?
3. Are there reasons for not exploring contemporary methodologies in report generation, like "Dynamic Graph Enhanced Contrastive Learning for Chest X-ray Report Generation, CVPR 2023"?

Evaluation Metrics:
Why were the AUROC scores for report generation only presented for six categories instead of the standard 14 categories?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into enhancing Large Language Models (LLMs) with vision-language capabilities, specifically targeting medical imaging like chest X-rays (CXR). Recognizing that current "adapter network" methods might limit the deep integration of visual and language features, the authors propose a novel "instruction-finetuning" method. Drawing from vision-language pretraining (VLP) techniques, they tokenize images using VQ-GAN, facilitating the generation of combined text and image sequences. Rather than building a new model, they finetune a pretrained LLM with diverse CXR-related instructions. This approach allows the LLM to understand and generate visual data without structural modifications. Their finetuned LLM showcases proficiency in tasks such as translating CXRs to reports and vice versa, and performing CXR-specific visual question answering. The model not only outperforms specialized models in these tasks but also demonstrates the potential of seamlessly integrating visual and language abilities in LLMs for medical applications.

### Strengths
Strengths:
1. **Novel Approach**: The paper introduces a novel "instruction-finetuning" method, which is a significant departure from the prevalent "adapter network" techniques. This innovative approach allows for a more intimate integration of visual and language features in LLMs.

2. **Leveraging Existing LLMs**: Instead of starting from scratch, the authors smartly utilize the inherent instruction-following abilities of pretrained LLMs. This approach is efficient and maximizes the potential of existing models.

3. **Broad Application**: The finetuned LLM exhibits versatility in handling a range of tasks, from converting CXRs to reports, generating CXRs from textual reports, to CXR-specific visual question answering. This breadth of application showcases the model's potential in real-world medical scenarios.

4. **Outperformance**: The paper demonstrates that their model surpasses other specialized models in various tasks. This comparative analysis underscores the efficacy of their approach.

5. **Seamless Integration**: By using VQ-GAN for image tokenization, the authors ensure a smooth integration of image and text token spaces without necessitating structural changes to the base LLM. This seamless integration is crucial for practical implementations.

### Weaknesses
Areas for improvement:

1. **Potential for Catastrophic Forgetting**: As with any endeavor to expand a pretrained model's capabilities, there's the inherent risk of the model losing or diminishing its foundational skills—known as catastrophic forgetting. While the paper's intent is to preserve and build upon the LLM's language capabilities, it doesn't extensively address measures taken to prevent this potential degradation. Specifically, the paper lacks discussion on techniques such as regularization, replay buffers, or parameter isolation that could mitigate this issue during the instruction finetuning process. The absence of empirical analysis demonstrating the preservation of original language skills is a notable gap.

2. **Adapter Network Dismissal**: The paper critiques the prevalent "adapter network" approach but doesn't provide a comprehensive empirical comparison. A deeper, side-by-side evaluation highlighting performance, adaptability, and computational efficiency would offer a clearer picture of why their "instruction-finetuning" method is superior or preferable. The paper should include a quantitative comparison of training time, parameter efficiency, and performance on downstream tasks between the proposed method and adapter-based approaches. Without this, the claim of superiority remains unsubstantiated.

3. **VQ-GAN Limitations**: Using VQ-GAN for image tokenization introduces its own set of challenges. VQ-GANs, while powerful, can sometimes produce artifacts or representations that aren't entirely faithful to the original image. The paper doesn't discuss how it mitigates or addresses these potential shortcomings, leaving room for questioning the quality or accuracy of the generated content. For example, the paper should detail the specific VQ-GAN architecture used, the training process, and the impact of quantization errors on the final results. Furthermore, an analysis of the fidelity of reconstructed images compared to the original CXRs is needed.

4. **Lack of Diverse Evaluation**: The paper's evaluation, though rigorous, might benefit from a more diverse set of metrics. For instance, qualitative evaluations or user studies involving medical professionals could provide insights into the model's practical utility. Comparisons with human diagnostic capabilities might also offer a benchmark for the model's proficiency. The current evaluation focuses on quantitative metrics, but a qualitative assessment of the generated reports and images by medical experts is crucial to determine the clinical relevance and accuracy of the model.

5. **RoentGen AUC and FID numbers**: The authors need to address the discrepancy between the AUC and FID numbers provided in their paper and those in the RoentGen paper. It should be clarified whether these numbers were reproduced by the authors or cited from the RoentGen study, and if there are differences, the paper should explain the reasons behind these.

6. **Minor edits**:

a. Grammar throughout the text requires attention for better readability, as exemplified by the construction of the second sentence in section 2.2.

b. The term "txv-all-1024" utilized in the text should be clearly defined. It is presumed to refer to the 1024-dimensional outputs from a densenet-121 model trained on chest X-ray classification, but this assumption needs confirmation in the paper for clarity.

### Questions
If the authors address the areas of improvement, I can reconsider my assessment.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work developed an instruction-finetuning method to integrate visual information into out-of-the-box LLMs, which can be used for bidirectional multi-modal CXR tasks, such as CXR report generation, VQA, and report-to-CXR generation.

### Strengths
- The image is tokenized by VQ-GAN, ensuring that clinical information is preserved. It is an efficient use of existing resources and knowledge by expanding pre-trained LLM's embedding space to include image tokens.
- The bidirectional instruction fine-tuning maintains the integrity of the LLM's structure and objectives while expanding its capabilities, which have many applications in the field.

### Weaknesses
The interpretability and scalability are not discussed.

### Questions
- How scalable is the tokenization and fine-tuning process for larger medical images (e.g., 3D CT/MR scans)?
- How interpretable are the model's decisions, especially given the clinical context where explanations for predictions are crucial?
- The comparison with other related methods is missed. https://github.com/chaoyi-wu/RadFM

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed an image-text alignment framework for chest X-ray images and report pairs based on LLM models. In addition to the existing vision adapter, the authors reconstruct the adapted vision representation back to the images.  Furthermore, VQA pairs (as image-instruction-answer) are generated using GPT3.5 from the associated reports as a form of data augmentation for the image report pairs.  The reconstruction module is pre-trained as a VQGAN and then frozen when tuning the VQA instructions. The MIMIC-CXR dataset is employed here for the experiments. Superior results of the proposed model are reported in comparison to previous LLM models in report generation and VQA. However, the presented work suffers from several critical flaws that are detailed below.

### Strengths
+ Tackling the image-text alignment problem in medical imaging, which is not well-researched yet
+ The manuscript is overall easy-to-follow

### Weaknesses
 - The authors claim the proposed bidirectional LLM is different from previous ones, as illustrated in Figure 1. However, I found the difference between them (a) and (c) is really minor. The encoder and decoder parts in the VQGAN are indeed equivalent to the vision adapter and image generative model, as listed in (a). Therefore, it is a bit overclaimed that it is novel to introduce bidirectional reconstruction tasks(both image-to-text and text-to-image) in the pre-training.
- The motivation for training an image-text aligned model is not clearly introduced and justified. First, it will be helpful to discuss how this model could be applied to the downstream clinical tasks. Then, the designed experiments only demonstrate the performance of the proposed method on these instruction tuning tasks, i.e., report generation based on images and VQA. It is hard to appreciate the benefit of adopting such a pre-trained and then SFTed model in practical use without demonstrating downstream applications. There are many chest X-ray benchmarks, and datasets are commonly used for the evaluation of pre-trained models, e.g., disease classifications and localizations. 
- The metrics utilized in the experiments for most tasks are not the commonly used ones, e.g., AUCROC/F1 and Jaccard similarity index for report generation, FID alone for image generation, and accuracy alone for VQA. 
- In the results of report generation, only LLM-based methods are compared. How about a dozen of those SOTA  methods in chest X-ray reporting? IU X-ray is another dataset commonly used for the evaluation of report generation performance. It will be helpful to report results on that as well, mainly when used as a cross-domain evaluation dataset.  
- I am not sure why the upsampling is performed for the image data as described in section 3.1 since the X-ray images are much larger than this resolution. How this upsampling process will affect the results?
- In section 2.2, the authors mentioned that the image tokens are parts of expanded embedding tables. I wonder how big K_img should be?

### Questions
see weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
