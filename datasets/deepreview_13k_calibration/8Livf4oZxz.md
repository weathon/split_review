# Video Instruction Tuning with Synthetic Data

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
The development of video large multimodal models (LMMs) has been hindered by the difficulty of curating large amounts of high-quality raw data from the web. To address this, we consider an alternative approach, creating a high-quality synthetic dataset specifically for video instruction-following, namely~\DataName{}. This dataset includes key tasks such as detailed captioning, open-ended question-answering (QA), and multiple-choice QA. By training on this proposed dataset, in combination with existing visual instruction tuning data, we introduce \ModelName{}, a new video LMM. Our experiments demonstrate that \ModelName{} achieves strong performance across various video benchmarks, highlighting the effectiveness of our dataset. We plan to release the dataset, its generation pipeline, and the model checkpoints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a synthetic dataset LLaVA-Video-178K, which consists of 178510 videos with detailed annotations, open-ended questions and multiple-choice questions. To build the dataset, the authors select the most dynamic videos from 10 major video data sources, and use a recurrent caption generation pipeline to generate video captions. The authors define 16 question types and generate question-answer pairs using GPT-4o. Based on LLaVA-Video-178K, the authors fine-tuned LLaVA-OneVision on the combination of LLaVA-Video-178K and other four public datasets to obtain the model called LLaVA-Video. Experiments show that the model trained with LLaVA-Video-178K will have a performance gain on a wide range of video benchmarks.

### Strengths
1. The paper proposes a caption generation pipeline, which recurrently generates and refines the captions of video in three temporal levels.
2. To filter out the static videos that can be summarized by a single video frame, the authors construct the dataset using dynamic videos which are selected by detecting the number of scenes in the videos. 
3. The paper proposes 16 different question types on the video, which are more comprehensive compared to existing benchmarks.

### Weaknesses
1. The level-1 and level-2 description are generated on fixed time intervals (10s and 30s), which are not event-specific or scene-specific. 
2. Most of the videos in the dataset are 180 seconds long, which may hinder the dataset's effectiveness in the field of long video understanding. 
3. Several typos and errors exist in the paper. It seems that the paper is not carefully proofread and checked. For example:
line 184 & 186: condtion->condition
line 400: should be [M/(4*p^2)] for the fast frames
line 415: considegreen->considered as

### Questions
1. In Table 3, what is the training data settings for +LLaVA-Video-178K, +Three Q&A datasets, and +LLaVA-OV (images)? From line 481 to line 485, it seems that LLaVA-Video-178K, three Q&A datasets and LLaVA-OV(images) are incrementally added for training. If so, what is the performance gain if LLaVA-Video-178K is the last dataset added for training? If datasets are trained separately in three settings, then why the performance of LLaVA-Video-178K is lower than LLaVA-OV (images)?
2. In Table 4, are there any insights on the out-of-domain performance loss of LLaVA-Video-178K compared to LLaVA-Hound on EgoSchema?
3. Figure 4 illustrates an interesting video. I am wondering whether the generated questions are only about the “facts” in the video such as “How many steps does “normal people” climb?”. I think people are more curious about whether the model understand the humor in the video. Whether the captions of the video can generate such questions?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the challenge of developing large multimodal models (LMMs) for video understanding, which has been limited by the scarcity of high-quality training data. To overcome this, the authors introduce LLaVA-Video-178K, a synthetic dataset designed for video instruction-following tasks such as detailed captioning, open-ended question-answering (QA), and multiple-choice QA. By training on this dataset alongside existing visual instruction tuning data, they develop LLaVA-Video, a new video LMM. Experiments demonstrate that LLaVA-Video performs strongly across various video benchmarks, underscoring the effectiveness of the synthetic dataset.

### Strengths
- The recurrent, multi-level annotation strategy for generating detailed captions and question-answer pairs is effective.
- The authors have conducted extensive experiments across multiple video benchmarks, demonstrating the effectiveness of the proposed LLaVA-Video models. The use of diverse datasets and thorough ablation studies supports the robustness of the results.
- The paper is well-structured, clearly explaining the problem, methodology, and experimental design.
- The significance of this work lies in its potential to advance video-language understanding models by providing a high-quality, open-source synthetic dataset. LLaVA-Video-178K has broad applicability in tasks such as video captioning and question-answering.

### Weaknesses
- The primary concern lies in the heavy reliance on GPT-4o for video captioning and question-answer (QA) pair generation. This approach essentially distills GPT-4o’s video capabilities into a structured format, raising questions about the originality of the contribution. Moreover, This has been done in previous work: ShareGPT4Video: improving Video Understanding and Generation with Better Captions, NeurIPS 2024 D&B Track. This work is an incremental improvement over prior work by scaling the data from 40K QA pairs to about 1.3M QA pairs. 
- The hierarchical captioning strategy employed in the paper is not new. The concept of recursive or hierarchical video captioning has been previously explored, for instance, in Video ReCap: Recursive Captioning of Hour-Long Videos (CVPR 2024). The failure to cite and differentiate from this work undermines the perceived novelty.
- The inclusion of multi-choice QA pairs appears to be tailored primarily for fitting into existing evaluation benchmarks rather than reflecting practical, real-world video understanding scenarios. This raises concerns about the broader utility of these QA pairs. 
- The model’s strong performance is largely due to fine-tuning from a powerful base model, LLaVA-OneVision. While the experimental results are compelling, the paper’s core contributions are somewhat overshadowed by the reliance on this pre-trained foundation.

### Questions
- Could you elaborate on how your approach to using GPT-4o for generating video captions and QA pairs differs from prior work, such as ShareGPT4Video?
- Additionally, would you consider exploring or providing insights on how non-GPT-based annotations might influence the model’s performance or diversity in understanding?
- Your hierarchical captioning approach is similar to what has been previously proposed, such as in Video ReCap: Recursive Captioning of Hour-Long Videos (CVPR 2024). How does your method differ conceptually or practically from this prior work? Please clarify if I may have overlooked novel aspects in your captioning pipeline.
- EgoSchema contains the videos from Ego4D, so the training set or even test set (not sure) can be observed in your training data mixture.

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
3

### Summary
This paper introduces LLaVA-Video-178K, a video instruction-following dataset automatically annotated using GPT-4o. This dataset features dynamic untrimmed videos with dense frame sampling for annotation. The authors also present the LLaVA-Video model, which incorporates an optimized slow-fast video representation for multi-modal video understanding. They finetune LLaVA-Video on this new dataset, demonstrating that it complements existing datasets to improve video understanding performance further.

### Strengths
1. The proposed dataset has potential benefits for the video understanding community. The authors demonstrate through finetuning experiments that it complements existing datasets effectively.
2. The paper is well written and organized. The authors provide high-quality figures that illustrate various attributes of the proposed dataset from multiple perspectives.

### Weaknesses
1. Lack of Technical Novelty and Depth: The dataset lacks a clear motivation, making it unclear why it improves performance. While prior datasets have already demonstrated the feasibility of synthetic data, this dataset appears to simply expand upon them without significant innovation. Although the authors claim that dynamic scenes improve performance, there is no direct experimental evidence supporting this claim. There is no statistical comparison of dynamic scenes in the new and existing datasets, nor is there an ablation study on this claim.
2. Limited Insights in Video Representation: The proposed video representation method offers limited insights and seems more like an engineering trick than a conceptual advancement.
3. In Summary: While the dataset provides practical value, the scientific insights are relatively limited. I suggest the authors conduct further analyses to highlight the unique contributions of this dataset.

### Questions
It appears there may be an error in the formula. line 400 & 871: ( T - t / s) * (M / 4p^2)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces LLaVA-Video-178K, a synthetic dataset for video instruction tuning, designed to address the challenge of curating large amounts of diverse and dynamic video data. The dataset contains 178,510 videos with detailed annotations, open-ended questions, and multiple-choice questions, created using a combination of GPT-4o and human efforts. The paper also presents LLaVA-Video, a new video large multimodal model (LMM) developed by training on LLaVA-Video-178K and existing visual instruction tuning data. LLaVA-Video outperforms previous models on various video benchmarks, demonstrating the effectiveness of the dataset. The authors plan to release the dataset, its generation pipeline, and model checkpoints to support the development of general-purpose visual assistants. The paper's contributions include the creation of a comprehensive video instruction-tuning dataset, the development of an advanced video LMM, and the commitment to open-source the resources to the public.

### Strengths
- **Originality:** Introduces LLaVA-Video-178K, a synthetic dataset for video instruction tuning. And LLaVA-Video, a new video LMM leveraging the synthetic dataset.

- **Quality:** Offers a comprehensive dataset with detailed captions and diverse QA tasks, enhancing model training and evaluation, and develops a video representation technique that optimizes frame and token usage, improving model performance.

- **Clarity:** Articulates the significance of the dataset and model advancements in an understandable manner.

- **Significance:** Contributes to advancing video instruction tuning with synthetic data.

### Weaknesses
- **Dataset Pipeline**: The description of the pipeline is unclear, both in terms of intuitive understanding from the diagrams and the verbal explanation. Moreover, it appears that there is not much difference from previous methods of automatically constructing datasets.

- **Model Architecture**: The design approach of the model seems to have poor generalizability and robustness, and it cannot adaptively handle videos of diverse scenarios and lengths.

### Questions
**Dataset Pipeline**:
- While this three-level approach is commendable, the description at Level-1 for time \(t\) heavily relies on the previous time \(t-1\), without leveraging longer-term dependencies, and the same applies to Level-2 and Level-3. This not only prevents it from capturing sufficiently long-range temporal information across the video but also makes the aggregated information less meaningful.
- The videos are all shorter than 3 minutes, and most scenes and content are singular without much dynamic transition information. Where is the significance of hierarchization, and what help can it provide for data quality?
- What is the motivation behind designing this architecture, and what evidence is there to prove that it generates higher-quality data? What is the essential difference between these QA datasets and previous ones, and can they provide more additional information and annotations?
- Are the 16 forced categories appropriate, what are the specific implementation details? If it was a manual review and summary, how many were reviewed, and are they representative? Or were they derived from the existing 40+ datasets' annotations for GPT-4o to summarize? Additionally, if QAs are generated for each video across the 16 categories, how are the unsuitable or low-quality QAs filtered out?

**Model Architecture**:
- The parameter \( s \) plays a crucial role in understanding the video; arbitrarily setting it obviously has no effect. How can events be dynamically recognized and videos segmented, employing differentiated sampling schemes at appropriate times? Are there potentially more suitable design schemes, along with experimental evidence and analysis?

**Ablation Study**:
- Why don't the experimental results in Table 3 present the individual results of LLaVA-Hound combined with the other three datasets, as well as the results of LLaVA-OV alone, and finally include the results of LLaVA-Video-178K? This makes it difficult to demonstrate that the significant improvement after adding LLaVA-Video-178K is not due to the disadvantages of LLaVA-Hound. Additionally, it cannot verify whether adding LLaVA-Video-178K after incorporating all datasets can still bring additional knowledge that is not present in the existing datasets to enhance performance sufficiently.

### Soundness
2

### Presentation
1

### Contribution
1
