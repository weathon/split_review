# EndoAssistant: A Large-scale Vision-Language Dataset for Endoscopic Surgery Understanding from Open-Source Videos

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
Endoscopic interventions offer a minimally invasive approach, minimizing patient discomfort and facilitating expedited recovery. Proficient training of junior surgeons necessitates the ability to analyze and interpret endoscopic scenes through questioning and answering. Consequently, the development of a robust foundation model for endoscopic visual language understanding holds immense value for medical training and surgical education. However, existing endoscopy vision-language datasets are limited in scale and diversity, consisting of only 50 videos sourced from a few clinical sites, thus posing a significant hurdle to the advancement of generalized and robust artificial intelligence models for endoscopic surgical applications. To address this challenge, we present a large-scale, meticulously curated image-text dataset of surgical endoscopic scenes from expert surgeons, designed to propel a vision-language assistant in medical scene understanding. Encompassing 590 open-source videos spanning more than 91 hours, our curated dataset includes 65,844 unique images, 30,002 unique captions, and 157,589 image-caption/question-answering pairs. This dataset aims to assist the development of automated systems to support medical professionals by mitigating repetitive tasks. We present a comprehensive endoscopic surgery assisting pipeline, (1) a first-ever image-caption dataset specifically for endoscopic scenes; (2) an image-question-answer dataset that offers greater size and diversity compared to existing collections; (3) rigorous evaluation demonstrating its efficacy in downstream surgical endoscopic scene comprehension tasks like classification, retrieval and visual question answering.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents the first large-scale, meticulously curated image-text dataset of surgical endoscopic scenes and demonstrates its effectiveness in downstream surgical endoscopic scene comprehension tasks.

### Strengths
1.	The curated dataset is a valuable resource for developing automated systems (e.g., LLMs, VLMs) to assist medical professionals in surgical endoscopic scenes.
2.	The paper employs a well-designed data processing pipeline, including rigorous data cleaning and optimization procedures, to generate high-quality image-text pairs from a large collection of endoscopic surgical videos.
3.	The CLIP model pretrained in EndoAssistant demonstrates superiority over mainstream vision-language pretraining frameworks through a broad range of empirical experiments.
4.	The paper is very clear and easy to follow.

### Weaknesses
1.	The proposed Visual Question Answering (VQA) models should be evaluated on internal datasets, such as parts of EndoAssistant, to better assess the endoscopic knowledge learned by the models. Evaluating solely on external datasets can only provide a limited view of the model's capabilities.
2.	The data, model, and training details should be openly released.
3.	The construction of Question-Answer Pairs raises concerns, as some pairs appear to be divergent questions unrelated to the images. The inclusion of such data may not effectively improve performance on specific downstream tasks that require cross-modal reasoning between image and text.
4.	The proposed Visual Question Answering (VQA) models, while built upon a large multimodal foundation model, are evaluated in a manner that does not fully utilize the multi-turn conversational capabilities typically associated with VLM models. This approach limits the assessment of the model's potential for complex, interactive question-answering scenarios.
5.	All symbols used in the tables should be clearly defined, such as shading and underlining.

### Questions
1.	How are the Question-Answer Pairs constructed? Looking at the Question-Answer Pairs in Fig. 2, some pairs appear to be divergent questions unrelated to the images. Will such data (Question-Answer Pairs) improve performance on specific downstream tasks?
2.	The proposed Visual Question Answering (VQA) models seem more akin to a VLM model than a traditional VQA model. Could you clarify this distinction?
3.	All symbols used in the tables should be clearly defined, such as shading and underlining.

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
The paper introduces EndoAssistant, a large-scale, expert-annotated vision-language dataset for endoscopic surgery, designed to enhance AI-driven medical training and surgical decision support systems.

### Strengths
1. The creation of a large-scale dataset with 65,844 unique images and over 157,589 image-caption pairs holds great potential to facilitate robust model training.

2. Incorporating both image-caption and image-question-answer pairs in the dataset supports diverse applications, from simple classification to complex question-answering.

3. The detailed data curation pipeline involving keyframe extraction, captioning, and alignment is methodologically sound for ensuring quality data preparation.

4. The involvement of domain experts throughout the data curation process helps ensure high factual correctness and relevancy.

### Weaknesses
1. The sampling method ignores temporal dynamics in endoscopic videos, potentially limiting the model's ability to perform cross-frame reasoning and handle dynamic scenes effectively. Specifically, the keyframe extraction process, while reducing redundancy, discards the temporal relationships between frames, which are crucial for understanding motion and changes in the surgical field. This could hinder the model's ability to predict surgical phases or anticipate tool movements that rely on understanding temporal context.

2. The image-text sampling process does not fully capitalize on multimodal associations, possibly lowering the model's performance in complex surgical scene understanding that requires integrated visual-text analysis. The current approach treats images and text as independent entities, only aligning them at a later stage. This fails to leverage the inherent semantic relationships between visual elements and their corresponding textual descriptions, such as the specific actions being performed or the tools being used, which could be better captured through a more integrated sampling approach.

3. The paper adopts a lower-performing method from Surgical-VQA (MICCAI 2023 paper) without demonstrating previous SOTA performance, casting doubts on the model's comparative effectiveness in the surgical domain. The choice of a baseline model that is not state-of-the-art makes it difficult to assess the true potential of the proposed dataset. A comparison with the best performing models on the Surgical-VQA benchmark would be necessary to establish the dataset's value.

4. The paper lacks a discussion on the downstream task (surgery-specific tasks such as phase or tool recognition) performance of models trained on the proposed dataset, which are essential for assessing practical applicability in the surgical domain. Without evaluating the dataset on relevant surgical tasks, it is unclear whether the dataset is truly useful for advancing surgical AI. The evaluation should include metrics specific to phase and tool recognition to demonstrate the dataset's utility.

5. The criteria for assessing the quality of text and images in the dataset are unclear, which may raise questions about the reliability of the dataset. The absence of specific metrics for image quality, such as sharpness, contrast, and noise levels, and for text quality, such as grammatical correctness and medical accuracy, makes it difficult to evaluate the overall quality of the dataset.

### Questions
1. Endoscopic surgery videos contain a large number of dynamic scenes, but the sampling process mainly processes static images or single-frame data, without fully considering the temporal information of the video. The sampling method that lacks temporal association will cause the model to be insufficient in dealing with cross-frame reasoning, thereby limiting the performance of the model in dynamic scenes. Discussion/experiments may be added for this problem.

2. The sampling process segments and processes images and texts. Although contrastive learning is used to project images and texts into a shared embedding space, the sampling process does not fully utilize the multimodal associations between images and texts. In particular, the semantic associations between images and corresponding surgical step descriptions and tool instructions are not strengthened during sampling. This weakened multimodal association may limit the performance of the model in understanding complex surgical scenes, especially in tasks that require the integration of visual and textual information (such as complex scene question answering or context understanding). A detailed analysis could be made.

3. Based on Surgical-VQA (MICCAI 2023, first release EndoVis-18-VQA & Cholec-VQA dataset), the accuracy of EndoVis-18-VQA & Cholec-VQA has reached 0.632 & 0.898, respectively. However, this submission selects the method with the lowest performance in Table 1 of Surgical-VQA. They have not proved their SOTA performance on benchmark VQA datasets in the surgical domain. BTW, after the first release, the specialized models have reached even higher performance.

4. Surgical data science researchers may focus on some surgery-specific tasks, e.g., phase/tool recognition. The zero/few-shot performance of a VLM trained on the proposed dataset may be expected. Besides, fine-tuning LLaVA on different datasets but evaluating on the same benchmark surgical datasets can further demonstrate the effectiveness of the proposed dataset.

5. What are the criteria for confirming the quality of text and images? Are there definite criteria for filtering low-quality images? What criteria do doctors use for text annotation?

### Soundness
3

### Presentation
3

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
The authors used a set of 590 endoscopic surgery videos to collect 157,589 image / caption pairs using a custom data curation pipeline. The image / caption pairs were further turned into open-ended and multiple choice question-answer pairs. 

The utility of the two datasets (image / caption pairs and QA pairs) was validated by training a CLIP model and a LLaVa model respectively, and evaluating them on downstream tasks (zero-shot classification / retrieval and linear probe for CLIP and VQA for LLaVa), demonstrating comparable or superior performance than several other biomedical CLIP models and VQA models.

### Strengths
The authors' proposed dataset appears 5 - 10 fold larger than previous endoscopic surgery video datasets in terms of metrics like hours of video content sourced from, question length and number of frames. 

The value of the dataset is validated across a range of different scenarios including zero-shot eval, representation learning (linear probe / few-shot learning) and VQA.

### Weaknesses
The quality of the dataset remains unclear to me - and would benefit from more clarification as well as investigation. While the dataset may be a valuable resource for computational researchers in the endoscopic surgical field, the paper otherwise does not appear to present novel ideas or evaluation. In fact, previous work published in CVPR 2024 have developed a much more sophisticated pipeline for curating instruction tuning data from Youtube videos in the field of pathology, involving more extensive quality control + mouse cursor location tracking: https://openaccess.thecvf.com/content/CVPR2024/papers/Seyfioglu_Quilt-LLaVA_Visual_Instruction_Tuning_by_Extracting_Localized_Narratives_from_Open-Source_CVPR_2024_paper.pdf.

For example, ASR is expected to be noisy and the transcript associated with a given key frame might have very limited context or be mismatched with the visual content displayed. Using GPT4 for retain only medically relevant information can help correct some incorrectly transcribed medical terms, but would not resolve the issues of limited context / mismatch with visual content. It is also not clear why out of 150k image / caption pairs, there are only 30,002 unique captions.

The created QA pairs similarly, might suffer from the same issues. I notice in the examples presented in Figure 2, are answers all very concise, and lack detailed explanation - which could arise due to both suboptimal prompting (e.g. only using zero-shot prompting instead of combining it with carefully, expert curated seed examples) and the concise nature of the source captions, and as a result limit their usefulness in training interactive AI assistants that can produce high quality responses in open-ended question answering (where a more detailed explanation or a specific response format is required).

Lastly, while the experiments are helpful for validating the usefulness of the dataset in the scenarios the authors investigated, crucial experimental details appear to be missing (i.e. hyperparemeters of training), which are needed to reproduce the results presented. Similarly, I cannot currently find a link to a github or hf repo that links to code and data used in the experiments in the study or the proposed dataset itself, and therefore can only draw conclusions about the quality of the data based on select examples / statistics presented in the paper.

### Questions
1. What is the average / std for the length of captions? 
2. How are the 120 image / caption pairs used in "Cross-modal retrieval" selected? Will this data be made available for future works to allow comparisons?
3. Can the authors offer any additional insights about the quality of the dataset? (perhaps having experts review a random subset and rate accuracy / descriptiveness, etc.)
4. What is the motivation for using both a CLIP model and a custom pretrained CNN classifier to classify endoscopic vs. irrelevant content?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces EndoAssistant, a large-scale vision-language dataset designed to enhance understanding of endoscopic surgery scenes. It addresses the limitations of existing datasets, which are small in scale and diversity, by providing a significantly larger collection of 590 videos, 65,844 unique images, 30,002 captions, and 157,589 image-caption/question-answer pairs. The dataset focuses on improving tasks like cross-modal retrieval, visual question answering (VQA), and image classification within the surgical context. The data curation process involves keyframe extraction, ASR transcription, hierarchical image classification, and rigorous text cleaning with clinical validation. EndoAssistant's vision-language data pipeline includes EndoCaption (image-caption pairs) and EndoQA (image-question-answer pairs), both of which are shown to improve baseline model performance across multiple benchmarks.

### Strengths
(1)EndoAssistant is the first large-scale, open-source vision-language dataset explicitly tailored for endoscopic surgery, surpassing previous datasets like Cholec80 in scale and semantic diversity. By integrating multiple existing models (CLIP, Whisper, GPT-4) into a surgeon-in-the-loop framework, this dataset provides a novel approach to generating diverse, medically relevant Q&A data from endoscopic videos.

(2)The paper clearly outlines each stage of the data pipeline, from video collection to model evaluation. The inclusion of figures detailing the dataset creation process and examples of the Q&A pairs and image captions adds clarity. Each stage is accompanied by performance metrics that demonstrate the impact of EndoAssistant on downstream tasks.

### Weaknesses
(1)Although EndoAssistant is curated for endoscopic tasks, some baseline models used (e.g., CLIP) are pre-trained on general vision-language datasets, which might limit their performance in highly specialized domains like medical imagery. Fine-tuning on similar medical datasets could make the evaluation more aligned with the dataset's intended use.

(2) How does EndoAssistant perform on surgical tasks beyond classification and VQA, such as surgical phase recognition or anomaly detection?

(3) While the dataset draws from multiple open sources, there is a limited analysis of potential biases within the data. Different hospitals, surgical types, anatomical regions, or patient demographics could introduce significant variability, impacting the generalizability of the model.

(4) The dataset relies on relatively straightforward image-text pairing and may not fully capture deeper semantic alignment between the visual and language modalities (e.g., multi-level semantic alignment or co-occurrence patterns). Surgical procedures often involve subtle contextual changes, and certain tools or anatomical structures may carry different meanings across procedural stages.

### Questions
It is recommended to include in the limitations a discussion on the challenging conditions often faced in endoscopic surgery, such as inconsistent lighting, obstructed views, interference from bodily fluids, as well as data biases arising from differences in hospitals, types of surgery, anatomical regions, or patient demographics.

### Soundness
3

### Presentation
4

### Contribution
3
