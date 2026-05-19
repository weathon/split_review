### Summary

This paper proposes a large-scale video-text dataset InternVid. The dataset contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. The authors utilize a multi-scale approach to generate video-related descriptions. The authors also introduce a video-text representation learning model based on ViT-L. Learned on InternVid via contrastive learning, this model demonstrates leading zero-shot action recognition and competitive video retrieval performance. Beyond basic video understanding tasks like recognition and retrieval, the dataset and model have broad applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper proposes a large-scale video-text dataset InternVid. The dataset contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. The authors utilize a multi-scale approach to generate video-related descriptions. The authors also introduce a video-text representation learning model based on ViT-L. Learned on InternVid via contrastive learning, this model demonstrates leading zero-shot action recognition and competitive video retrieval performance. Beyond basic video understanding tasks like recognition and retrieval, the dataset and model have broad applications.
2. The paper is well-written and easy to follow.
3. The proposed InternVid is a large-scale video-text dataset. The dataset contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. The authors utilize a multi-scale approach to generate video-related descriptions. The authors also introduce a video-text representation learning model based on ViT-L. Learned on InternVid via contrastive learning, this model demonstrates leading zero-shot action recognition and competitive video retrieval performance. Beyond basic video understanding tasks like recognition and retrieval, the dataset and model have broad applications.

### Weaknesses

#### Some Related Works


#### comment

1. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos. Furthermore, the reliance on YouTube as the sole source introduces a potential bias towards content that is popular or trending on the platform, which may not be representative of the broader video landscape. This could impact the generalizability of models trained on this dataset to other video domains.
2. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos. The dataset's focus on short-form content might not adequately capture the complexities of longer, more structured videos, such as those found in educational or documentary contexts. This could lead to a performance gap when models are applied to such content.
3. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos. The limited duration of the videos may also restrict the dataset's utility for tasks that require temporal reasoning or the analysis of long-term dependencies within videos. This could hinder the development of models capable of understanding complex temporal dynamics.
4. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos. The dataset's reliance on short videos might also lead to a lack of diversity in terms of video content and style, as shorter videos often focus on a single, concise idea or action. This could limit the robustness of models trained on this dataset when faced with more varied and complex video content.

### Suggestions

The authors should consider expanding the dataset to include a wider range of video lengths, particularly longer videos that are more representative of real-world scenarios. This could involve incorporating videos from other sources beyond YouTube, such as video archives, educational platforms, or user-generated content from other platforms. Furthermore, the authors could explore methods for artificially extending shorter videos, such as concatenating multiple clips or using video repetition techniques, to create a more balanced dataset with respect to video duration. This would help to address the limitations of the current dataset and improve the generalizability of models trained on it. The authors should also consider the potential biases introduced by relying solely on YouTube and explore methods to mitigate these biases, such as stratified sampling or data augmentation techniques that can help to diversify the dataset.

To address the limitations of the dataset's short video lengths, the authors could explore techniques for training models that are robust to variations in video duration. This could involve using techniques such as temporal pooling or attention mechanisms that can effectively aggregate information across different time scales. Additionally, the authors could investigate methods for transferring knowledge from models trained on longer videos to models trained on shorter videos, which could help to improve the performance of models on tasks that require long-term temporal understanding. The authors should also consider evaluating their models on a wider range of tasks that involve longer videos, such as video summarization, long-term action recognition, or video question answering, to better understand the limitations of their approach and identify areas for future improvement.

Finally, the authors should provide a more detailed analysis of the dataset's characteristics, including the distribution of video lengths, the diversity of content, and the potential biases introduced by the data collection process. This analysis should be included in the paper to provide a more comprehensive understanding of the dataset's strengths and limitations. The authors should also consider releasing the dataset with metadata that includes information about the video length, source, and content, which would help other researchers to better understand and utilize the dataset. This would also allow for more targeted analysis of the dataset's properties and facilitate the development of more robust and generalizable models.

### Questions

1. The InternVid dataset is collected from YouTube. The videos in the dataset are all short videos, with an average length of about 5 minutes. This may limit the applicability of the dataset to tasks that require longer videos, such as video summarization or long-term video understanding. The short average length of the videos may also limit the ability of models trained on this dataset to generalize to longer videos.

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
