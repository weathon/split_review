### Summary

This paper proposes a novel method for dataset condensation, which aims to preserve the architecture/hyperparameter rankings of different architectures/hyperparameters. The proposed method is evaluated on image and graph datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is novel and interesting. The idea of preserving the architecture/hyperparameter rankings of different architectures/hyperparameters is novel and interesting.
- The proposed method is evaluated on image and graph datasets.

### Weaknesses

#### Some Related Works

[1] Dataset Condensation with Hypergradient Matching
[2] Towards dataset condensation with the fisher information matrix

#### comment

 - The proposed method is only evaluated on image and graph datasets. It would be better to evaluate the proposed method on other types of datasets, such as audio and text datasets.
- The proposed method is compared with only a few baselines. It would be better to compare the proposed method with more baselines, such as [1, 2].
- The proposed method is compared with baselines on the Spearman's rank correlation of architecture/hyperparameter rankings. It would be better to also compare the proposed method with baselines on the test performance of the best architecture/hyperparameter selected by the baselines and the proposed method.
- The proposed method is compared with baselines on the Spearman's rank correlation of architecture/hyperparameter rankings. It would be better to also compare the proposed method with baselines on the test performance of the best architecture/hyperparameter selected by the baselines and the proposed method.

### Suggestions

The evaluation of the proposed method should be broadened to include a more diverse set of data modalities. While image and graph datasets are important, the absence of evaluations on audio and text datasets limits the generalizability of the findings. Specifically, the method's performance on sequential data, such as audio, and the unstructured text data is crucial to understand its applicability in real-world scenarios. For audio, the evaluation should consider tasks like speech recognition or music generation, while for text, it should include tasks like sentiment analysis or text classification. This would provide a more comprehensive understanding of the method's strengths and weaknesses across different data types. Furthermore, the evaluation should include a wider range of baselines, including more recent and state-of-the-art dataset condensation techniques. This would allow for a more rigorous comparison and a better understanding of the proposed method's relative performance. 

In addition to the Spearman's rank correlation, the evaluation should also focus on the practical impact of the proposed method. The primary goal of dataset condensation is to accelerate hyperparameter optimization, and therefore, the test performance of the best architecture/hyperparameter selected by each method is a critical metric. The current evaluation focuses on the correlation of rankings, which is useful but not sufficient to demonstrate the method's effectiveness in real-world scenarios. The test performance should be reported for the best architecture/hyperparameter selected by each method, including the proposed method and the baselines. This would provide a more direct measure of the method's ability to identify the optimal architecture/hyperparameter. Furthermore, the evaluation should also consider the computational cost of each method, including the time required for dataset condensation and hyperparameter optimization. This would provide a more complete picture of the method's practical utility.

Finally, the evaluation should include a more detailed analysis of the method's performance under different conditions. For example, the method's performance should be evaluated with different dataset sizes and different numbers of architectures/hyperparameters. This would provide a better understanding of the method's scalability and robustness. The analysis should also include a discussion of the method's limitations and potential areas for improvement. This would provide a more balanced and nuanced view of the method's performance and its potential for future research. The current evaluation lacks a detailed analysis of the method's performance under different conditions, which limits the understanding of its practical applicability.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
