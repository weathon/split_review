# RA-TTA: Retrieval-Augmented Test-Time Adaptation for Vision-Language Models

- Decision: Accept
- Scores: 6, 5, 5, 6

## Abstract
Vision-language models (VLMs) are known to be susceptible to distribution shifts between pre-training data and test data, and test-time adaptation (TTA) methods for VLMs have been proposed to mitigate the detrimental impact of the distribution shifts. However, the existing methods solely rely on the internal knowledge encoded within the parameters, which are constrained to pre-training data. To complement the limitation of the internal knowledge, we propose **retrieval-augmented-TTA (RA-TTA)** for adapting VLMs to test distribution using **external** knowledge obtained from a web-scale image database. Fully exploiting the bi-modality of VLMs, fine-grained **text descriptions** are used both for retrieving proper external images and refining VLMs' predictions with the retrieved external images. As a result, the pivotal features of test images are more precisely recognized through the text descriptions. 
Extensive evaluations on 17 datasets validate that RA-TTA outperforms the state-of-the-art methods by 2.49-8.45\% on average.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the success of RAG into VLM for test-time adaptation, achieving performance improvements. Extensive experiments demonstrate the effectiveness of the method.

### Strengths
1. This paper is well-written, and the framework is clear and easy to follow. Additionally, the provided code enhances reproducibility.
2. Introducing RAG into VLM for test-time adaptation is a reasonable and meaningful idea.
3. The experiments in this paper are thorough, with detailed descriptions. The method surpasses others on multiple datasets.

### Weaknesses
1. More training-free methods should be discussed and compared. In VLM-based transfer learning, training-free adapters [1] have significantly improved with a small number of image samples, as in CaF [2] with fine-grained descriptions based on classes. The proposed method is more complex, so I am curious about its performance advantage compared to these easy but efficient methods.

2. This method involves generating descriptors for each test sample with a GPT-based generator, then self-filtering with the image itself, retrieving similar samples, and finally drawing conclusions. This is a relatively lengthy pipeline. How does its efficiency compare to other methods? Additionally, GPT usage is not free, though open-source models could be a workaround. Could this pipeline be simplified, perhaps by using improved prompts to avoid generating imaginary content or by creating visual descriptors to replace the image-to-description selection?

3. Could more visualization results be provided, showing the generated descriptors -> filtered irrelevant descriptors -> refined inference results, similar to the presentation in Figures 3 and 4 of DVDet [3]?

References:

[1] Tip-Adapter: Training-free CLIP-Adapter for Better Vision-Language Modeling
[2] Visual Classification via Description from Large Language Models
[3] LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-Grained Descriptors

### Questions
Please see the weakness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a novel retrieval-augmented test-time adaptation (RA-TTA) for improving VLM generalization on downstream datasets at test time. RA-TTA exploits additional visual information through retrieval of web-scale images to regularize VLM predictions at test time. Extensive experiments over various datasets show the effectiveness of the proposed method.

### Strengths
The introduction retrieval augmentation into TTA problem is an innovative approach. Also, the proposed description-based retrieval technique aligns well with the multi-modal capabilities of VLMs.

The paper presents extensive experimental evaluations over 17 diverse datasets. The authors also conduct detailed ablation studies and sensitivity analyses.

The paper is well-organized and easy to follow.

### Weaknesses
The paper lacks some necessary discussions and analyses.

(1) In the proposed method, different databases are sampled from large-scale datasets for each downstream dataset respectively. This may introduce additional computational requirements when adapting to different datasets. Will directly retrieving from the large-scale datasets like LAION2B help mitigate this issue? In addition, the computation overhead or inference time compared with TPT should be provided for examining the efficiency of the proposed method.

(2) The retrieval process highly depends on the LLMs for generating detailed text descriptions. The authors are suggested to discuss how different LLMs might affect description quality and, consequently, the final adaptation performance.

(3) How do the authors ensure that the retrieved images contain the expected features to augment the test image? For example, in the examples provided in the introduction, if the test image depicts the front and side of a vehicle, the retrieved images should ideally contain related information, such as headlights.

Some recent and related studies are missing from the section Related work. The author should consider discussing the difference with these works [a,b,c,d].
[a] Efficient Test-Time Adaptation of Vision-Language Models
[b] Dual memory networks: A versatile adaptation approach for vision-language models
[c] SwapPrompt: Test-Time Prompt Adaptation for Vision-Language Models
[d] Historical Test-time Prompt Tuning for Vision Foundation Models

### Questions
as shown in Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In vision-language models, existing test-time adaptation methods solely rely on the internal knowledge encoded within the parameters. To complement the limitation of the internal knowledge, this paper proposes retrieval-augment TTA for adapting VLMs to test distribution using external knowledge obtained from a web-scale image database. It uses fine-grained text descriptions for retrieving proper external images and refining VLM’s predictions with the retrieved external images. Extensive evaluations on 17 datasets validate that RA-TTA outperforms the state-of-the-art methods.

### Strengths
1. The paper is well-written and easy to follow. 
2. This work investigates test-time adaptation in visual language models. Due to the difficulty of updating pre-trained models frequently, TTA on visual language models is a highly researched topic.
3. The proposed method can achieve state-of-the-art results on 17 benchmarks, including standard transfer learning and distribution shift. And it conducts ablation study to validate the effectiveness of proposed modules.

### Weaknesses
1.	The biggest issue with the article is its lack of innovation. In fact, the proposed method is very similar to [1], which is not even cited in this paper. [1] firstly retrieves relevant samples from a web-scale database using seed prompts (T2I) or seed images (I2I), then build a K-shot cache by selecting the Top-K similar images per class based on CLIP embeddings, and the final predictions is an ensemble of original predictions and few-shot cache predictions. The basic idea and pipeline are very similar to [1].
2.	In Table2, the proposed method achieves inferior performance than TPT [2] and RLCF [3] in IN-V2 and IN-A. The authors should analyze the reasons behind this phenomenon. Does it indicate that the effectiveness of the method is related to the downstream datasets? 
3. The paper lacks clarity in describing certain operations. For instance, in the Equation 8, why is optimal transport used, and what is its purpose?


[1] Understanding Retrieval-Augmented Task Adaptation for Vision-Language Models, ICML 2024.

[2] Test-time Prompt Tuning for Zero-shot Generalization in Vision-Language Models, NeurIPS 2022.

[3] Test-time Adaptation with CLIP Reward for Zero-shot Generalization in Vision-Language Models. In ICLR 2022.

### Questions
1. The basic idea and pipeline are very similar to [1]. The differences and advantages should be claimed. 

2.  In Equation 8, why is optimal transport used, and what is its purpose?

3. Figure 3 is not very clear in presenting the proposed method, specifically in prototype-based retrieval part.

[1]  Understanding Retrieval-Augmented Task Adaptation for Vision-Language Models, ICML 2024.

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
4

### Summary
This work focuses on test-time adaptation (TTA) of vision-language models (VLMs) and proposes retrieval-augmented TTA (RA-TTA), aiming to improve the generalization ability of VLMs on downstream datasets. Specifically, RA-TTA incorporates external visual information by retrieving web-scale images with fine-grained text descriptions, which are then used to augment VLM predictions at test time. Unlike prior test-time adaptation methods that rely solely on the pre-trained model's internal knowledge, RA-TTA enhances test-time adaptation with retrieved images, consistently improving prediction accuracy across 17 datasets.

### Strengths
1. Introducing retrieval augmentation into test-time adaptation of VLMs is novel. Prior methods generally augment test images using simple augmentation strategies (e.g., crop, resize), while this work exploits the external knowledge form additional image data bases to augment each test image for better model predictions. Additionally, the proposed description-based retrieval could effectively leverages the bi-modality of VLMs, leading to more relevant retrieval results.
2. The experiments conducted in this work are extensive. The authors benchmark the proposed RA-TTA with the SOTA methods on 17 diverse datasets, and provide comprehensive analysis experiments, including ablation studies and parameter sensitivity analyses.

### Weaknesses
1. RA-TTA highly relies on Large Language Models (LLMs) to generate fine-grained text descriptions for image retrieval. Therefore, the authors should discuss how different LLMs might vary in their effectiveness at generating useful descriptions, and how this impacts retrieval relevance and quality.
2. The authors construct different data base for each downstream dataset by sampling form a large dataset such as LAION2B. The sampled database size may impact both computational cost and retrieval quality, for example, a larger sampled database size may bring better retrieval quality but may also increase latency and storage costs. Therefore, an analysis of how the sampled database size affects adaptation performance should be provided.
3. Ensuring semantic diversity in text descriptions for each class name is crucial in RA-TTA. How is this diversity ensured during the generation process?
4. Compared  with prior studies such as TPT, the proposed RA-TTA involves additional database construction process and retrieval process which may bring more computation cost and inference time. Therefore, the computational and storage overhead compared to TPT should be provided.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
