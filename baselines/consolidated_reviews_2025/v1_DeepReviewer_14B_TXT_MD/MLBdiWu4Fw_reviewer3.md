### Summary

This paper introduces InternVid, a large-scale video-centric multimodal dataset for learning video-text representations for multimodal understanding and generation. The dataset contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. The authors also propose a video-text representation learning model based on ViT-L, which demonstrates leading zero-shot action recognition and competitive video retrieval performance. The dataset and model have broad applications in various fields, including autonomous driving, intelligent surveillance, and human-computer interaction.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The InternVid dataset is a large-scale video-centric multimodal dataset that contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. The dataset is collected from various sources, including YouTube, and covers a wide range of topics, including actions, objects, scenes, and events. The dataset is designed to be used for multimodal understanding and generation tasks, such as video-text representation learning, video captioning, and video question answering.
2. The authors propose a video-text representation learning model based on ViT-L, which demonstrates leading zero-shot action recognition and competitive video retrieval performance. The model is trained on InternVid via contrastive learning and incorporates video masking to accelerate learning without compromising effectiveness.
3. The dataset and model have broad applications in various fields, including autonomous driving, intelligent surveillance, and human-computer interaction. The dataset can be used to learn video-text representations for multimodal understanding and generation, while the model can be used for tasks such as action recognition, video retrieval, and video-text matching.

### Weaknesses

#### Some Related Works


#### comment

1. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos.
2. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos.
3. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos.
4. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos.

### Suggestions

The authors should consider expanding the dataset to include a wider range of video lengths, particularly longer videos that are more representative of real-world scenarios. This could involve incorporating videos from other sources beyond YouTube, such as video archives, educational platforms, or user-generated content from other platforms. Furthermore, the authors could explore methods for artificially extending shorter videos, such as concatenating multiple clips or using video repetition techniques, to create a more balanced dataset with respect to video duration. This would help to address the limitations of the current dataset and improve the generalizability of models trained on it. Additionally, the authors should investigate the impact of video length on the performance of their proposed model and provide a more detailed analysis of how the model performs on videos of varying lengths.

To further enhance the dataset's utility, the authors should consider incorporating more diverse content beyond the current focus on actions, objects, scenes, and events. This could include videos with more complex narratives, abstract content, or videos that require a deeper understanding of context and temporal relationships. The current dataset, while large, may not fully capture the complexity and diversity of real-world video content. By incorporating a wider range of video types, the dataset could become more valuable for training models that are robust and generalizable to a broader range of applications. The authors should also explore methods for automatically categorizing and tagging videos with more fine-grained labels, which would facilitate more targeted training and evaluation of models.

Finally, the authors should investigate the potential biases present in the dataset due to its reliance on YouTube. The content available on YouTube may not be representative of all types of video content, and there may be biases related to popularity, demographics, or other factors. The authors should analyze the dataset for potential biases and develop strategies for mitigating them. This could involve using techniques such as re-weighting or data augmentation to ensure that the dataset is more balanced and representative. Furthermore, the authors should provide a detailed analysis of the dataset's limitations and potential biases in the paper, which would help other researchers to use the dataset responsibly and effectively.

### Questions

1. How does the performance of the ViCLIP model compare to other state-of-the-art models on various tasks, such as action recognition, video retrieval, and video-text matching?
2. What are the limitations of the dataset and model, and how do you plan to address them in future work?
3. Can you provide more details on the data collection and annotation process, including the sources of the videos, the criteria for selecting videos, and the methods used to generate captions and other annotations?

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
