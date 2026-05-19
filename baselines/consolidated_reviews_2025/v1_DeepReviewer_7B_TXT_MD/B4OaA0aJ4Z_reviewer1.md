### Summary

This paper presents a benchmark for time series foundation models, evaluating various foundation models across different datasets and settings. The authors analyze the performance of these models under zero-shot, few-shot, and full-shot learning scenarios and investigate aspects such as channel independence vs. dependence, model efficiency, and data characteristics. They compare foundation models with traditional time series models and provide insights into the strengths and weaknesses of current foundation models, highlighting directions for future model design.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The authors conduct a comprehensive comparison of various foundation models and traditional time series models, offering a valuable reference for the community.
2. The paper analyzes different aspects of foundation models, such as data characteristics, model efficiency, and performance under different settings, providing a detailed understanding of these models.
3. The paper is well-organized and clearly written, making it easy to follow and understand.

### Weaknesses

#### Some Related Works

[1] Timesnet: Temporal 2d-variation modeling for general time series analysis
[2] Timesmamba: A time series state space model
[3] Times-gpt: A generalized pre-trained model for general time series forecasting

#### comment

1. The paper claims to be the first benchmark for foundation models in time series forecasting, but this is inaccurate. There are already several benchmarks available, such as the one published in NeurIPS 2023 [1]. Additionally, the authors do not compare the performance of foundation models with more recent state-of-the-art time series models, such as TimesNet [2], TimesMamba [3], and Times-GPT [4]. These models have demonstrated strong performance in time series forecasting and should be included in the comparison to provide a more comprehensive evaluation.
2. The paper lacks a detailed description of the experimental setup, including specific hyperparameters and training procedures for each model. This lack of detail makes it difficult to reproduce the results and assess the validity of the findings. For example, the specific optimization algorithms, learning rates, and batch sizes used for each model are not clearly stated.
3. The paper does not provide a thorough analysis of the results, particularly regarding the performance differences between foundation models and traditional models. A more in-depth discussion of these differences, including potential reasons for the observed performance, is needed. For example, the paper should discuss why certain foundation models perform better than others in specific settings.

### Suggestions

The authors should significantly expand the related work section to include a more comprehensive overview of existing benchmarks and time series models. Specifically, they should discuss the methodologies and findings of other time series benchmarks, such as the one published in NeurIPS 2023 [1], and clearly articulate how their work differs and contributes to the field. Furthermore, the authors should include a more thorough comparison with recent state-of-the-art time series models, such as TimesNet [2], TimesMamba [3], and Times-GPT [4]. This comparison should not only include performance metrics but also a discussion of the architectural differences and computational complexities of these models. This would provide a more robust evaluation of the foundation models and highlight their strengths and weaknesses relative to the current state of the art.

To address the lack of detail in the experimental setup, the authors should provide a comprehensive description of the hyperparameters and training procedures used for each model. This should include specific details such as the optimization algorithms, learning rates, batch sizes, and any data preprocessing steps. The authors should also specify the hardware and software environment used for the experiments. This level of detail is crucial for ensuring the reproducibility of the results and allowing other researchers to build upon their work. Furthermore, the authors should consider including ablation studies to analyze the impact of different hyperparameters on the performance of the foundation models. This would provide a deeper understanding of the models' behavior and help identify the optimal settings for each model.

Finally, the authors should provide a more in-depth analysis of the results, focusing on the performance differences between foundation models and traditional models. This analysis should include a discussion of the potential reasons for these differences, such as the inductive biases of the models, their ability to generalize to unseen data, and their computational efficiency. The authors should also discuss the limitations of their study and suggest directions for future research. For example, they could explore the performance of foundation models on more diverse datasets or investigate the impact of different training strategies on their performance. This would provide a more complete and nuanced understanding of the capabilities and limitations of foundation models for time series forecasting.

### Questions

See Weaknesses

### Rating

5

### Confidence

4

**********
