### Summary

This paper introduces a benchmark for evaluating UDA techniques for time series classification, focusing on deep learning methods. It provides seven new benchmark datasets covering various domain shifts and temporal dynamics, facilitating standardized assessments of UDA methods. The paper also offers insights into the strengths and limitations of the evaluated approaches, serving as a valuable resource for researchers and practitioners.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper provides a detailed review of current state-of-the-art UDA algorithms for time series data.
2. This paper introduces seven new benchmark datasets for UDA time series data.
3. This paper evaluates the UDA time series data using different hyper-parameter selection methods.

### Weaknesses

#### Some Related Works

[1] Deep unsupervised domain adaptation for time series classification
[2] Deep unsupervised domain adaptation for time series: A review

#### comment

1. The contribution of this paper is quite limited. This paper seems like a simple A/B/C comparison, rather than a technical paper.
2. This paper claims to be the first benchmark of UDA for time series data. However, Adatime (Ragab et al., 2023) and the review (Ragab et al., 2023) have already provided benchmarks for UDA time series data.
3. This paper lacks a detailed description of the datasets introduced. For example, the specific domains included in the Ford dataset and the domain shift between the source and target domains are not clearly explained.
4. This paper does not provide ablation studies for the proposed InceptionDANN, InceptionCDAN, InceptionMix, and InceptionRain models.
5. The experimental results in this paper show that the proposed InceptionDANN, InceptionCDAN, InceptionMix, and InceptionRain do not outperform the existing methods. Additionally, the paper does not offer sufficient analysis regarding this issue.
6. The paper does not adequately address the limitations of the existing UDA methods, such as the large number of hyperparameters and the lack of a clear explanation of how the proposed benchmark overcomes these limitations.
7. The paper does not provide a clear explanation of the practical implications of the proposed benchmark and how it can be used by practitioners in the field.

### Suggestions

The paper needs to more clearly articulate its novel contributions beyond simply applying existing UDA methods to new datasets. While the introduction of new datasets is valuable, the paper should provide a more in-depth analysis of the specific challenges these datasets pose for UDA, such as the nature of the domain shifts and the complexity of the temporal dynamics. For example, a detailed analysis of the feature distributions across different domains within each dataset could highlight the specific difficulties in achieving effective domain adaptation. Furthermore, the paper should justify the selection of the specific UDA methods evaluated, explaining why these methods were chosen over other existing approaches and how they relate to the specific challenges posed by the new datasets. A more rigorous analysis of the performance of the proposed Inception-based methods is needed, including ablation studies to understand the contribution of different components and a discussion of why they do not outperform existing methods. This analysis should go beyond simple performance comparisons and delve into the underlying reasons for the observed results, such as the suitability of the method's architecture for the specific characteristics of the datasets.

To enhance the practical impact of the benchmark, the paper should provide clear guidelines on how practitioners can use the benchmark to evaluate new UDA methods. This should include a discussion of the evaluation metrics, the hyperparameter tuning process, and the computational resources required. The paper should also address the limitations of the proposed benchmark, such as the number of datasets included and the types of domain shifts considered. A discussion of the potential biases in the datasets and the limitations of the evaluation metrics would also be beneficial. The paper should also provide a more detailed explanation of the hyperparameter tuning methods used, including a discussion of the advantages and disadvantages of each method and a comparison of their performance across different datasets. This should include a discussion of the sensitivity of the UDA methods to different hyperparameter settings and the potential for overfitting to the source domain.

Finally, the paper should provide a more thorough discussion of the limitations of existing UDA methods and how the proposed benchmark addresses these limitations. This should include a discussion of the challenges in tuning UDA methods, the lack of a unified evaluation framework, and the limited understanding of the interplay between the degree of shift and the performance of UDA methods. The paper should also discuss the potential for future research in this area, such as the development of new UDA methods that are more robust to different types of domain shifts and the creation of more comprehensive benchmarks that cover a wider range of datasets and evaluation metrics. The paper should also provide a more detailed explanation of the practical implications of the proposed benchmark and how it can be used by practitioners in the field, including specific examples of how the benchmark can be used to evaluate the performance of UDA methods in real-world applications.

### Questions

1. In Section 4, the paper mentions ensuring temporal causality for the splits. However, it does not provide detailed explanations or justifications for this. Could you provide more details about this?
2. In Section 5.1, the paper mentions that the results differ from the original papers due to three reasons. However, it does not provide a detailed explanation of these reasons. Could you provide more details about these reasons?
3. In Section 5.2, the paper compares different hyper-parameter selection methods. However, it does not provide a clear explanation of which method is the best. Could you provide more details about this?
4. In Section 5.3, the paper states that the backbones do not have a significant impact on the performance. However, it does not provide a detailed explanation of this. Could you provide more details about this?
5. The paper does not provide a detailed description of the existing UDA methods, making it difficult to understand the specific innovations of the proposed methods. Could you provide more details about the existing UDA methods?
6. The paper does not provide a detailed description of the proposed InceptionDANN, InceptionCDAN, InceptionMix, and InceptionRain. Could you provide more details about these methods?
7. The paper does not provide a detailed explanation of the experimental results. For example, the paper does not explain why the proposed InceptionDANN, InceptionCDAN, InceptionMix, and InceptionRain do not outperform the existing methods.
8. The paper does not provide a detailed discussion of the limitations of the proposed benchmark. For example, the paper does not discuss the potential biases in the datasets or the limitations of the evaluation metrics.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
