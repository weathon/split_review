### Summary

The paper introduces Recap-DataComp-1B, a large-scale dataset of one billion image-text pairs with enhanced textual descriptions generated using the LLaMA-3-powered LLaVA model. The authors aim to improve the quality of web-crawled image-text data, which is often noisy and misaligned, by recaptioning the DataComp-1B dataset. The enhanced dataset is shown to significantly improve the performance of vision-language models, including CLIP for zero-shot cross-modal retrieval and Diffusion Transformers for text-to-image generation. The paper provides comprehensive evaluations and analysis of the dataset's impact on model training and performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel large-scale dataset, Recap-DataComp-1B, which is generated using an advanced LLaMA-3-powered LLaVA model. This dataset addresses the issue of noisy and misaligned image-text pairs in existing web-crawled datasets.
2. The paper provides a thorough evaluation of the dataset's impact on various vision-language models, including CLIP and Diffusion Transformers. The results demonstrate significant improvements in zero-shot cross-modal retrieval and text-to-image generation tasks.
3. The paper is well-written and organized, with clear explanations of the methodology, experiments, and results. The figures and tables are informative and support the claims made in the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not sufficiently discuss the limitations and potential biases introduced by the recaptioning process. For example, the quality of the generated captions depends heavily on the performance of the LLaVA model, which may introduce or amplify existing biases in the dataset. Specifically, the paper lacks a detailed analysis of how the LLaVA model's biases might manifest in the generated captions, such as gender, racial, or cultural biases, and how these biases could affect downstream tasks. Furthermore, the paper does not explore the potential for the LLaVA model to generate captions that are overly generic or lack fine-grained details, which could limit the dataset's utility for certain applications.
2. The paper could benefit from a more thorough analysis of the impact of different text encoder sizes on model performance. While the authors explore different caption mix ratios, they do not provide a detailed analysis of how the text encoder size interacts with these ratios, which could be crucial for understanding the optimal configuration for training models with the new dataset. For instance, it is unclear whether a larger text encoder consistently benefits performance across all mix ratios, or if there is a specific encoder size that is optimal for a given ratio. The paper also does not discuss the computational cost associated with different text encoder sizes, which is an important consideration for practical applications.
3. The paper does not provide a detailed analysis of the computational cost associated with the recaptioning process and the training of models using the new dataset. This information is crucial for researchers who may want to use the dataset or replicate the study. The paper should include a breakdown of the computational resources required for each stage of the process, including the fine-tuning of the LLaVA model, the generation of captions, and the training of downstream models. This should include details on the type of hardware used (e.g., GPUs, CPUs), the training time, and the overall energy consumption.

### Suggestions

The paper would benefit from a more in-depth analysis of the potential biases introduced by the LLaVA-based recaptioning process. The authors should investigate specific types of biases, such as those related to gender, race, or cultural representation, and quantify their presence in the generated captions. This could involve using existing bias detection tools or developing new metrics tailored to the specific characteristics of the dataset. Furthermore, the authors should explore methods for mitigating these biases, such as by incorporating adversarial training or data augmentation techniques. A detailed analysis of the diversity of the generated captions is also needed, including metrics that capture the range of objects, attributes, and relationships described in the captions. This would help to assess whether the recaptioning process leads to a loss of fine-grained details or an over-reliance on generic descriptions. The authors should also consider the impact of these factors on downstream tasks, such as image retrieval or text-to-image generation, and provide recommendations for how to mitigate any negative effects.

To strengthen the analysis of text encoder sizes, the authors should conduct a more systematic exploration of how different encoder sizes interact with various caption mix ratios. This should include a detailed analysis of the performance of models trained with different combinations of encoder sizes and mix ratios, using a range of evaluation metrics. The authors should also investigate whether there is a specific encoder size that is optimal for a given mix ratio, and provide guidelines for selecting the appropriate encoder size based on the desired trade-off between performance and computational cost. Furthermore, the paper should include a discussion of the computational resources required for training models with different text encoder sizes, including the training time, memory usage, and energy consumption. This information is crucial for researchers who may want to use the dataset or replicate the study, and it would help them to make informed decisions about the practical feasibility of using different encoder sizes.

Finally, the paper should provide a more detailed breakdown of the computational cost associated with the recaptioning process and the training of models using the new dataset. This should include a detailed description of the hardware used, the training time, and the overall energy consumption. The authors should also provide an estimate of the cost of generating captions for the entire dataset, as well as the cost of training downstream models with different configurations. This information is crucial for researchers who may want to use the dataset or replicate the study, and it would help them to make informed decisions about the practical feasibility of using the dataset. The authors should also consider providing this information in a standardized format, such as a table or a figure, to make it easier for readers to understand and compare the computational requirements of different approaches.

### Questions

1. Can you provide more details on the limitations and potential biases introduced by the recaptioning process?
2. How does the size of the text encoder impact the performance of models trained on the new dataset, and what are the optimal configurations?
3. What is the computational cost associated with the recaptioning process and the training of models using the new dataset?

### Rating

6

### Confidence

4

**********
