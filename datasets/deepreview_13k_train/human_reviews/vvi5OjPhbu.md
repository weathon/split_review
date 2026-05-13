# Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
With the explosive growth of video content, video captions have emerged as a crucial tool for video comprehension, significantly enhancing the ability to understand and retrieve information from videos. However, most publicly available dense video captioning datasets are in English, resulting in a scarcity of large-scale and high-quality Chinese dense video captioning datasets. To address this gap within the Chinese community and to promote the advancement of Chinese multi-modal models, we develop the first, large-scale, and high-quality Chinese dense video captioning dataset, named Youku Dense Caption. This dataset is sourced from Youku, a prominent Chinese video-sharing website. Youku Dense Caption includes 31,466 complete short videos annotated by 311,921 Chinese captions. To the best of our knowledge, it is currently the largest publicly available dataset for fine-grained Chinese video descriptions. Additionally, we establish several benchmarks for Chinese video-language tasks based on the Youku Dense Caption, including retrieval, grounding, and generation tasks. Extensive experiments and evaluations are conducted on existing state-of-the-art multi-modal models, demonstrating the dataset's utility and the potential for further research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Youku Dense Caption, a large-scale Chinese dense video captioning dataset. Dataset addresses the scarcity of high-quality Chinese video captioning resources, containing 31,466 short videos with 311,921 Chinese captions. A strategies is proposed to improve benchmark quality by filtering out redundant or low-quality annotations. The authors establish several benchmarks for Chinese video-language tasks and conduct extensive experiments demonstrating the dataset's utility and potential for research. They also discuss challenges related to the linguistic and cultural differences between Chinese and English video data.

### Strengths
1. A Chinese video captioning dataset is proposed to fill the research gap in the Chinese community for video captioning data.
2. A embedding-based similarity and a Non-Maximum Suppression method is used to set up a Chinese PRVR benchmark that effectively reduces annotation redundancy.
3. The work reduces redundancy in video captioning and grounding by filtering out videos with high self-BLEU scores and minimal scene changes,  which is measured through color histogram correlation, ensuring a diverse and representative dataset.

### Weaknesses
1. The statement in the section “Chinese Characteristics” seems unclear. The English translation of the so-called “fine-grained Chinese captions” could also serve as fine-grained English captions in an English-language context. For me, only the localized data part is valuable, as it highlights a major difference between Chinese and English video captions. Adding more data and statistics to support this distinction would strengthen the paper.
2. In the experiment, when translated back to Chinese. It's kind of blur that which attributes of Chinese dataset lead to the poor performance, the analysis failed to state clearly about the language differences between Chinese and English.
3. In ablation study, mixing of different datasets only strike a balance between different tasks but failed to achieve idealized performance across different tasks. And the best performance comes from larger data scale rather than data distribution and video-caption pair. 
4. Overall, the dataset serve as a valuable data source for Chinese community in video caption domain, but the value and key attributes of the dataset remain unclear and is not fully proved by the experiment.

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Youku Dense Caption, the largest publicly available dataset for Chinese dense video captioning, comprising 31,466 videos annotated with 311,921 captions. Collected from the Youku video platform, this dataset addresses the lack of high-quality Chinese video captioning datasets and promotes advancements in Chinese multi-modal research. It provides benchmarks for key tasks such as retrieval, grounding, and generation, and extensive experiments demonstrate its effectiveness on state-of-the-art multi-modal models. The dataset’s scale and quality make it a valuable resource for future research in video-language understanding.

### Strengths
Youku Dense Caption contains 31,466 short videos annotated with 311,921 captions, making it the largest dataset for fine-grained Chinese video descriptions.It addresses the scarcity of high-quality Chinese dense video captioning datasets, promoting advancements in Chinese multi-modal models and video-language research.The dataset establishes benchmarks for key video-language tasks such as retrieval, grounding, and generation, with extensive experiments demonstrating the utility of the dataset on state-of-the-art multi-modal models.

### Weaknesses
1. Lack of Caption Diversity and Detail: In Figure 1, the captions for different segments of Video ID 1070344446 show high similarity with little distinction, lacking sufficient variability. Additionally, the descriptions are relatively simple and do not provide background information about the visual content.
2. Potential Hallucination in Captions: In the D. Implementation Details of Baselines section, the authors mention that they convert videos to 320p resolution and remove the audio component. However, in Figure 1, the second frame of Video ID 1192027222 shows the caption: “The old lady boasts that young women who work hard at chopping can do it.” It is difficult to determine solely from the visual content that the old lady is boasting, raising concerns about the potential for hallucinated captions, especially for those tied to audio-related information.

### Questions
1. Vocabulary Statistics and Comparison: Can the authors provide vocabulary statistics and a comparison with other datasets? The captions appear to contain a high degree of repetition.
2. Threshold for Average Self-BLEU: Why was the threshold for Average Self-BLEU set to 0.15?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper details a novel Chinese language based dense video caption dataset.

### Strengths
+ This work collected a new Chinese based dense video captioning dataset (named Youku Dense Caption). The dataset has several benchmarks for Chinese video-language tasks, including retrieval, grounding, and generation tasks. 
+ This allow developer and researcher to train multmodal foundation model with a fair benchmark. 
+ This submission has validate the impact of large scale dataset on existing multimodal model. Providing empirical evidence of the advantage of rich data in the context of Chinese language.

### Weaknesses
- The proposed dataset's video are evenly sampled from the Youku-mPLUG dataset based on dedicated (sub)categories. So the assumption is that the licensing should not be an issues. To properly handle the copyright concerns, please details the licensing terms for the Youku-mPLUG dataset, and discuss the coverage of usage right, redistribution policies, and any restriction.

- This paper should provide addition details related to the annotation progress. Please provide detilas on: 
1. The total number of human annotators involved.
2. The qualifications or expertise of the annotators (e.g., native Chinese speakers, etc.) and how are them recruited. 
3. The cost and time spent on annotation per video. 
4. The total number of annotations per annotator and the overall duration. 
5. Any quality control measures sued during the annotation process.

### Questions
- Has the author consider to release the English caption of the proposed dataset? In my opinion, this will broaden the impact of this dataset and benefit more downstream tasks. Please confirm if this is a a planned future work, as well as to discuss the plan for creating high-quality English translation of the captions. Further analysis on the English translation with open-source tool in Fig 1, it is clear that it requires professional proofreading or checked by someone (crowdsourcing?) who are fluent in both Chinese and English language.

- This paper should provide addition details related to the annotation progress. Please provide detilas on: 
1. The total number of human annotators involved.
2. The qualifications or expertise of the annotators (e.g., native Chinese speakers, etc.) and how are them recruited. 
3. The cost and time spent on annotation per video. 
4. The total number of annotations per annotator and the overall duration. 
5. Any quality control measures sued during the annotation process.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Youku Dense Caption dataset, which is the largest publicly available Chinese dense video captioning dataset for now. The dataset is annotated by human to guarantee the quality of the dataset.
Building upon the proposed dataset, the paper also establishes benchmarks for video-language tasks.
The experiments demonstrate that existing state-of-the-art multi-modal models can benefit from this dataset.

### Strengths
- The paper focuses on the topic of Chinese dense video captioning dataset, which is an interesting and under-explored research area.

### Weaknesses
 - Doubtful value of the proposed dataset
    - First, while the proposed dataset is claimed to be a dense video captioning dataset, the collection pipeline is similar to regular video captioning datasets, like HD-VILA-100M or Panda-70M, where a long video is first segmented into multiple clips and each clip is annotated with a caption. Could the authors provide more differences between the dataset collection pipelines of your dataset and a regular video-text dataset? The core issue is that the annotation process, as described, does not inherently create a 'dense' captioning dataset. Datasets like ActivityNet Captions include explicit temporal relationships between events, such as "A person does X, then Y, then Z", which is absent in the provided description of the Youku Dense Caption dataset. The segmentation of long videos into clips and annotating each clip is a common practice in video captioning, not a defining characteristic of dense captioning.
    - Second, it is unconvincing to state that "Chinese and English have significant linguistic differences, so a Chinese dataset is needed". I appreciate the authors show the errors of translation in line 211 and Section 3.2.2. However, I use ChatGPT to translate the provided samples and it can produce correct results in most of the cases. Take the leftmost sample in Figure 3 as example, I got this: "A group of motorcyclists is resting by the roadside, chatting." from ChatGPT, which is totally correct.

- Lack of necessary experiments: to evaluate the value of the proposed dataset, the authors need to train a model on different datasets and show that the one trained on the proposed dataset is more robust than the others. Such experiment should be conducted on different tasks, such as dense video generation, partially relevant video retrieval. However, none of this experiment is presented.

- It has been shown that long and detailed prompts are beneficial to various tasks, such as video generation. However, the caption annotations are short and less detailed, limiting the value of the dataset.

- For the scene change detection algorithm mentioned in lines 345~364, TransNet-v2 should be more robust than the adopted pixel-based algorithm.

### Questions
- How is a long video segmented into multiple clips? What is the splitting criteria?

- Could you show more data samples in Youku Dense Caption dataset? It is helpful for checking the diversity, visual quality, and annotation quality  of the proposed dataset?

### Soundness
2

### Presentation
2

### Contribution
3
