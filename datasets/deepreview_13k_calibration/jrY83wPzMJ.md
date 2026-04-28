# Synchronous Scene Text Spotting and Translating

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Text image machine translation aims to translate the content of textual regions in images from a source language to a target language. Compared with traditional document, images captured in natural scenes have more diverse text and more complex layout, posing challenges in recognizing text content and predicting reading order within each text region. Current methods mainly adopt pipeline pattern, in which models for text spotting and translating are trained separately. In this pattern, translation performance is affected by propagation of mispredicted reading order and text recognition errors. In this paper, we propose a scene text image machine translation approach by implementation of synchronous text spotting and translating. A bridge and fusion module is introduced to make better use of multi-modal feature. Besides, we create datasets for both Chinese-to-English and English-to-Chinese image translation. Experimental results substantiate that our method achieves state-of-the-art translation performance in scene text field, proving the effectiveness of joint learning and multi-modal feature fusion.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this work, the authors propose a scene text image machine translation method, which can detect, recognize and translate text in natural scene images. They also create image datasets for both Chinese-to-English and English-to-Chinese image translation tasks.

### Strengths
The curated dataset STST800K can be beneficial to the community.

### Weaknesses
1. Considering the architecture and pipeline of the proposed model, the novelty of it is limited.
2. The details of casting existing baselines (such as ABCNetv2, SPTSv2 and UNITS) as text spotter and translator are very crucial, but they are absent in the paper.
3. The comparison in Tab. 5 is unfair. The proposed model is pre-trained with data from various sources (such as STST800K and WMT22) and fine-tuned on down-stream datasets, while the Qwen-VL model is not.

### Questions
Please address the questions and concerns in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method for synchronous scene text recognition and translation, which introduces a Bridge & Fusion module to integrate text and image modalities. Additionally, the paper collects multiple datasets to construct a scene text image machine translation (TIMT) dataset. The real data includes manually annotated test sets from ReCTS and HierText, while other datasets are annotated using the Qianwen API, followed by manual correction. The synthetic datasets are created based on existing tools. Experimental results demonstrate that the method in this paper outperforms existing text image translation models.

### Strengths
1.	A method is proposed that can perform text spotting and text image machine translation, achieving better performance than previous methods.
2.	A Chinese-to-English and English-to-Chinese TIMT dataset is constructed based on multiple existing datasets, which includes annotating real data and synthesizing data using existing tools. This dataset is beneficial to the development of the TIMT field.

### Weaknesses
1.	The related work section needs adjustment. This paper mainly focuses on TIMT, yet the authors provide very little introduction to this field in related work, instead offering a large amount of introduction on text spotting.
2.	The paper is somewhat difficult to read and does not provide some key experimental settings. For example, the setting of $\alpha$ in Equation 2 and the size of the Qwen-VL model are not specified. Additionally, all models labeled as 'ours' in the experimental results are bolded, yet they are not the best, which is quite confusing. This result does not align with what the paper claims as SOTA.
3.	The novelty is limited. The Bridge & Fusion module essentially extracts visual features based on the predicted text region's coordinates and then obtains multimodal features through cross-attention. This approach is very common in multimodal machine translation.
4.	The paper claims that its model is end-to-end, however, actually the model still requires autoregressively generating coordinates and recognition output first, and then combines them with the image to autoregressively generate the translation. Therefore, it is not fully end-to-end.
5.	The paper illustrates the issue of incorrect reading order in the pipeline method shown in Figure 1. However, the proposed method does not address this problem but merely provides such training data. Given this type of data, can the text spotting model in the pipeline also solve this issue?

### Questions
1.	What is the size of the Qwen-VL model being compared, and what are the differences in settings with AnyTrans [1]? It would be better if compared with AnyTrans.
2.	What is the specific setting of alpha in Equation 2? Is the model training sensitive to this parameter?
3.	Will the data and code be open source?

[1] AnyTrans: Translate AnyText in the Image with Large Scale Models.

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
This paper proposes a synchronous text spotting and translating approach for Scene TIMT by jointly training the model with three sub-tasks, detecting text regions in the image, recognizing the source language text content, and translating it into the target language.
In order to solve the problem of mis-ordered text recognition and translation that occurs in existing pipelined methods, the paper introduces a “Bridging and Fusion (BAF)” module to more effectively utilize visual and textual features to achieve efficient scene text translation. The method is evaluated on the self-constructed STST800K dataset and compared with existing methods.

### Strengths
1) The paper proposes that the synchronized training approach can improve the sequential reading accuracy of translation compared to the traditional pipeline model. 
2) The proposed BAF module is creative and helpful in fusing visual and textual features.
3) The paper creates a large-scale dataset containing 800,000 samples of Chinese-English translations with real and synthetic data annotations, providing a new benchmark for scenario-based text translation tasks.

### Weaknesses
1) For text recognition and translation of complex scenes, especially fine-grained and layout complexity is not reflected in the paper. The paper lacks a rigorous definition of 'complex scenes,' making it difficult to assess the method's robustness in varied real-world scenarios. Specifically, the paper does not address challenges such as variations in font styles, sizes, and orientations, as well as the impact of occlusions and perspective distortions on both text detection and subsequent translation accuracy. Furthermore, the paper does not discuss how the model handles overlapping or closely spaced text instances, which are common in complex layouts.
2) The way of synchronized training is not clearly described. The paper provides a high-level overview of the training process but lacks specific details on how the three sub-tasks (detection, recognition, and translation) are jointly optimized. It is unclear what loss functions are used for each sub-task and how these losses are combined to achieve synchronous training. The model's training data is large, and the resources consumed are not mentioned. Large datasets lead to more resources consumed for training models. The paper should provide details on the computational resources required for training, including the number of GPUs, training time, and memory usage, to allow for reproducibility and to assess the practical feasibility of the proposed approach.

### Questions
1) How does the BAF module affect the reliability of the translated output in cases where errors occur in detection or recognition? Could more error analysis be provided to help understand the effects of the fusion of visual and textual features?
2) How about the recognition and translation performance of the model in more complex scenarios?
3) Can the model be applied to translations in languages other than Chinese and English?
4) Can there be a more detailed explanation of the construction of the dataset？

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a unified framework for scene text image spotting and translation. A BAF Module is proposed to connect and integrate visual and textual features. Additionally, the authors have created the Scene TIMT (Scene Text Image Multilingual Translation) datasets for both Chinese-to-English and English-to-Chinese translations. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper proposes a unified framework designed to enhance the performance of text image machine translation.
2. This paper introduces a new Scene TIMT (Scene Text Image Multilingual Translation) dataset for this field.

### Weaknesses
1. The proposed method involves a larger set of parameters compared to other methods.
2. When comparing with multimodal large models, the analysis lacks a comparison against the most recent large multimodal models, such as mplug-owl (CVPR 24), Monkey (CVPR 24), and InternVL (CVPR 24). It would be beneficial to have the performance results of the large multimodal models after they have been fine-tuned using the corresponding dataset. Furthermore, the comparison to AnyTrans is limited by the fact that it is trained on a different dataset, making a direct comparison difficult.
3. The authors claim that “In this pattern, translation performance is affected by propagation of mispredicted reading order and text recognition errors.” However, there is a lack of experiments or evidence to verify this claim. Specifically, the paper does not isolate the impact of reading order errors from other types of recognition errors, making it difficult to assess the claim's validity.
4. Lack of experiment to verify the effectiveness of proposed BAF Module using different text spotter and Translation module. It is unclear if the BAF module's performance is consistent across different text spotting and translation architectures, or if it is highly coupled to the specific modules used in the paper.
5. There is a lack of experimental validation to show how a unified framework improves different modules. Does it provide a greater improvement for end-to-end text spotting or for translation? The paper does not provide a breakdown of performance gains for each task, making it difficult to understand the specific benefits of the unified approach.

### Questions
Why is it necessary to unify end-to-end spotting and translation? The author did not emphasize the necessity of unification in the paper.

### Soundness
3

### Presentation
3

### Contribution
3
