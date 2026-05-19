### Summary

This paper introduces a large-scale video-centric dataset for multimodal learning and generation. The dataset contains over 7 million videos and 234 million video clips with detailed descriptions. The authors also propose a video-text representation learning model based on ViT-L, which demonstrates leading zero-shot action recognition and competitive video retrieval performance. The dataset and model have broad applications in various fields, including autonomous driving, intelligent surveillance, and human-computer interaction.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a large-scale video-centric dataset, InternVid, which is a significant contribution to the field of multimodal learning and generation. The dataset contains over 7 million videos and 234 million video clips with detailed descriptions, making it one of the largest and most comprehensive video datasets available.
- The authors propose a video-text representation learning model, ViCLIP, which demonstrates leading zero-shot action recognition and competitive video retrieval performance. The model is trained on InternVid via contrastive learning and incorporates video masking to accelerate learning without compromising effectiveness.
- The dataset and model have broad applications in various fields, including autonomous driving, intelligent surveillance, and human-computer interaction. The dataset can be used to learn video-text representations for multimodal understanding and generation, while the model can be used for tasks such as action recognition, video retrieval, and video-text matching.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the limitations of the dataset and model in detail. It would be helpful to have a more thorough discussion of the potential biases, weaknesses, and areas for improvement.
- The paper could provide more details on the data collection and annotation process, including the sources of the videos, the criteria for selecting videos, and the methods used to generate captions and other annotations. This information is important for understanding the quality and reliability of the dataset.
- The paper could provide more details on the training and evaluation of the ViCLIP model, including the hyperparameters used, the training data, and the evaluation metrics. This information is important for understanding the performance and limitations of the model.

### Suggestions

The paper should include a more detailed discussion of the potential biases present in the dataset. For instance, the geographical distribution of the videos, the types of activities represented, and the language used in the captions could all introduce biases that affect the performance of models trained on this data. A thorough analysis of these biases, including quantitative measures where possible, would be beneficial. Furthermore, the paper should discuss how these biases might impact downstream tasks and what steps could be taken to mitigate them. For example, if the dataset over-represents certain types of actions, the model might perform poorly on under-represented actions. The authors should also consider the ethical implications of these biases, especially when the dataset is used in sensitive applications like surveillance or autonomous driving. A clear plan for addressing these limitations in future work would significantly strengthen the paper.

To improve the reproducibility and transparency of the work, the authors should provide a more detailed description of the data collection and annotation process. This should include specific information about the sources of the videos, such as the websites or databases from which they were obtained. The criteria used for selecting videos should also be clearly defined, including any filtering or preprocessing steps applied to the data. Furthermore, the methods used to generate captions and other annotations should be described in detail, including the specific models or algorithms used and any post-processing steps applied to the generated text. The authors should also provide examples of the generated captions and discuss the quality and accuracy of these annotations. This level of detail is crucial for other researchers to understand the dataset and to potentially replicate the data collection process.

Finally, the paper should include a more comprehensive description of the training and evaluation of the ViCLIP model. This should include a detailed list of the hyperparameters used during training, such as the learning rate, batch size, and optimizer settings. The specific training data used, including any data augmentation or preprocessing techniques, should also be clearly defined. The evaluation metrics used to assess the performance of the model should be described in detail, including the specific formulas and any variations used. The authors should also provide a more detailed analysis of the model's performance on different subsets of the data, such as different action categories or video lengths. This would help to identify the strengths and weaknesses of the model and to guide future research.

### Questions

- Can you provide more details on the data collection and annotation process, including the sources of the videos, the criteria for selecting videos, and the methods used to generate captions and other annotations?
- How does the performance of the ViCLIP model compare to other state-of-the-art models on various tasks, such as action recognition, video retrieval, and video-text matching?
- What are the limitations of the dataset and model, and how do you plan to address them in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
