### Summary

This paper introduces InterVid, a large-scale video-text dataset for multimodal learning and generation. It consists of over 7 million YouTube videos with detailed captions and temporal descriptions, addressing the scarcity of high-quality video-language data. The authors propose a scalable approach to generate captions using a combination of models, including CLIP and BLIP2. They also introduce Video-CLIP, a video-language model trained on InterVid, which achieves state-of-the-art zero-shot action recognition and competitive fine-tuned results. The dataset and model demonstrate the benefits of scaling up video-language data for various applications, including video generation and dialogue systems.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The authors have curated a large-scale video-text dataset, which is a valuable contribution to the community. The dataset addresses the scarcity of high-quality video-language data and provides a resource for multimodal learning and generation tasks.
- The authors have proposed a scalable approach to generate captions using a combination of models, including CLIP and BLIP2. This approach is efficient and effective in generating detailed and diverse captions for the dataset.
- The authors have trained a video-language model, Video-CLIP, on the InterVid dataset, which achieves state-of-the-art zero-shot action recognition results and competitive fine-tuned results. The model demonstrates the benefits of scaling up video-language data for various applications.

### Weaknesses

#### comment

- The authors have not compared their approach with other state-of-the-art methods for video captioning and video-language modeling. It is essential to compare the proposed approach with other methods to demonstrate its effectiveness and novelty.
- The authors have not provided a detailed analysis of the dataset, including the distribution of video lengths, frame rates, and text descriptions. This information is crucial for understanding the characteristics of the dataset and its potential applications.
- The authors have not discussed the limitations of the dataset, such as the potential biases in the data collection process and the lack of diversity in the video content. Addressing these limitations is essential for ensuring the responsible use of the dataset.

### Questions

- How does the proposed approach compare with other state-of-the-art methods for video captioning and video-language modeling?
- What is the distribution of video lengths, frame rates, and text descriptions in the InterVid dataset?
- What are the limitations of the dataset, and how can they be addressed?

### Rating

3

### Confidence

4

**********
