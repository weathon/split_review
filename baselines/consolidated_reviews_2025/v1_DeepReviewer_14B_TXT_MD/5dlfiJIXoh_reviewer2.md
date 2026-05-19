### Summary

This paper introduces a video-language pre-training framework that leverages fine-grained structures in video and language to learn region-object correspondences and temporal-aware features. The framework, named S-ViLM, incorporates two novel designs: inter-clip spatial grounding and intra-clip temporal grouping. These designs promote learning region-object alignment and temporal-aware features simultaneously. The paper demonstrates that S-ViLM outperforms existing methods on four downstream tasks, including text-video retrieval, video question answering, video action recognition, and temporal action localization. The superior performance of S-ViLM validates the effectiveness of the proposed framework and its potential for various video-language understanding tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper introduces a novel video-language pre-training framework called S-ViLM, which focuses on learning fine-grained structures in video and language. The framework incorporates two novel designs: inter-clip spatial grounding and intra-clip temporal grouping, which promote learning region-object alignment and temporal-aware features simultaneously.

2. The paper demonstrates the effectiveness of S-ViLM on four downstream tasks, including text-video retrieval, video question answering, video action recognition, and temporal action localization. The results show that S-ViLM outperforms existing methods on these tasks, validating the effectiveness of the proposed framework.

3. The paper is well-written and easy to understand. The authors provide clear explanations of the proposed framework and its components, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed framework. It would be helpful to understand the computational requirements of S-ViLM, including the number of parameters, training time, and inference time, to assess its practicality for real-world applications.

2. The paper does not discuss the limitations of the proposed framework in detail. It would be beneficial to understand the potential challenges and limitations of S-ViLM, such as its sensitivity to hyperparameter settings or its performance on specific types of videos or languages.

3. The paper does not provide a comparison of the proposed framework with other state-of-the-art methods on a wider range of datasets. It would be helpful to evaluate the performance of S-ViLM on more diverse datasets to assess its generalizability and robustness.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the S-ViLM framework. Specifically, providing a breakdown of the number of parameters for each component (e.g., video encoder, text encoder, and the grouping blocks) would be valuable. Furthermore, reporting the training time per epoch, along with the inference time for a single video or text input, would allow for a better understanding of the framework's efficiency. This analysis should also include a comparison of the computational cost with other similar video-language pre-training models. For example, a table summarizing the parameter count, training time, and inference time for S-ViLM and other relevant models would be highly informative. This would help to contextualize the computational overhead introduced by the novel intra-clip temporal grouping and inter-clip spatial grounding mechanisms.

To address the lack of discussion on limitations, the authors should explore the sensitivity of S-ViLM to different hyperparameter settings. For instance, how does the performance vary with changes in the number of grouping blocks, the dimensionality of the group tokens, or the learning rate? A sensitivity analysis would provide valuable insights into the robustness of the framework. Additionally, the authors should investigate the performance of S-ViLM on specific types of videos, such as those with fast motion, occlusions, or complex backgrounds, and on different languages, especially low-resource languages. This would help to identify potential weaknesses and areas for improvement. A discussion of the potential failure cases and the reasons behind them would also be beneficial.

Finally, the paper should include a more comprehensive evaluation of S-ViLM on a wider range of datasets. While the current evaluation covers four downstream tasks, it would be beneficial to include more diverse datasets, especially those that are more challenging or that have different characteristics. For example, evaluating on datasets with longer videos or videos with more complex temporal dynamics would provide a more thorough assessment of the framework's capabilities. Furthermore, comparing the performance of S-ViLM with other state-of-the-art methods on these additional datasets would help to establish its generalizability and robustness. This would also help to identify any potential biases in the current evaluation and provide a more complete picture of the framework's strengths and weaknesses.

### Questions

1. Can you provide more details on the computational cost of the proposed framework, including the number of parameters, training time, and inference time?

2. What are the potential limitations of the proposed framework, and how do you plan to address them in future work?

3. Have you considered evaluating the performance of the proposed framework on a wider range of datasets, and if so, what are the results?

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
