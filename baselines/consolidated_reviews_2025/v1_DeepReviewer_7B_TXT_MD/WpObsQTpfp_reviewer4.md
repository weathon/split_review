### Summary

This paper proposes a method to improve the quality of web-crawled image-text pairs by using LLaMA-3 to re-caption the DataComp-1B dataset. The re-captioned dataset, called Recap-DataComp-1B, is then used to train a new vision-language model, called Recap-CLIP. The paper provides a detailed analysis of the dataset, including the impact of different mixing ratios between original and re-captioned data on model performance. The proposed method is shown to improve the performance of the model on image-text retrieval tasks and text-to-image generation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method of using LLaMA-3 to re-caption the DataComp-1B dataset is simple and effective.
3. The authors provide a detailed analysis of the dataset, including the impact of different mixing ratios between original and re-captioned data on model performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other captioning models, such as BLIP-2 and InstructBLIP. Including these models would help to better understand the performance of the proposed dataset when used with different captioning architectures.
2. The paper does not provide a detailed analysis of the types of errors present in the generated captions. A detailed error analysis would help to understand the limitations of the proposed dataset and identify areas for improvement.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing captioning models. Specifically, the authors should evaluate the performance of models trained on the proposed dataset using different captioning architectures, such as BLIP-2 and InstructBLIP. This would provide a more comprehensive understanding of the dataset's strengths and weaknesses, and help to identify potential biases or limitations of the proposed approach. For example, it would be valuable to see how the performance of these models varies when trained on the proposed dataset versus the original DataComp-1B dataset. This analysis should include not only overall performance metrics, but also a breakdown of performance across different types of captions and image-text pairs. Furthermore, the authors should investigate the impact of different training strategies, such as varying the amount of training data or using different optimization algorithms, to determine the optimal settings for each model.

In addition to comparing with other captioning models, the paper should include a detailed analysis of the types of errors present in the generated captions. This analysis should go beyond simple quantitative metrics and delve into the qualitative aspects of the captions. For example, the authors could categorize the errors into different types, such as object hallucinations, attribute errors, and relationship errors. They could then analyze the frequency of each type of error and identify any patterns or trends. This would help to understand the limitations of the proposed dataset and identify areas for improvement. For instance, if the dataset is found to be prone to object hallucinations, the authors could explore techniques to mitigate this issue, such as using a more robust captioning model or incorporating additional constraints into the training process. Furthermore, the authors should investigate the impact of different training strategies, such as varying the amount of training data or using different optimization algorithms, to determine the optimal settings for each model.

Finally, the paper should explore the impact of different mixing ratios between original and re-captioned data on model performance. While the authors provide a detailed analysis of this aspect, they could further investigate the optimal mixing ratio for different types of models and tasks. For example, they could explore whether a higher mixing ratio is more effective for image-text retrieval tasks, while a lower mixing ratio is more effective for text-to-image generation tasks. This analysis should also consider the computational cost of training with different mixing ratios, and provide practical guidance for researchers who want to use the proposed dataset. Furthermore, the authors should investigate the impact of different training strategies, such as varying the amount of training data or using different optimization algorithms, to determine the optimal settings for each model.

### Questions

1. Could you provide a comparison of the proposed dataset with other datasets, such as ShareGPT4V and ShareLLava, to highlight its unique contributions?
2. Could you include a comparison with other captioning models, such as BLIP-2 and InstructBLIP, to demonstrate the dataset's effectiveness with different architectures?
3. Could you provide a detailed analysis of the types of errors present in the generated captions to better understand the dataset's limitations?

### Rating

6

### Confidence

4

**********
