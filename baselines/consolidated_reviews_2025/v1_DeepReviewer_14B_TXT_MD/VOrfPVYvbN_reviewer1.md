### Summary

The paper proposes a method to determine the data domain of unknown black-box machine learning models by leveraging pre-trained generative models and language models. The contributions of the paper are summarized as follows:

1. A novel method is proposed to determine the data domain of unknown black-box machine learning models using pre-trained generative models and language models.

2. An objective function is formulated that captures both the relevance and generality of a potential candidate that represents the data domain. A heuristic search algorithm is presented to optimize this function.

3. The proposed method is empirically validated across different scenarios, including identifying the input data domain for classifiers with pre-established ground truth, utilizing datasets procured via the proposed method for subsequent investigations, and discerning the input data domain for models in real-world model repositories.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method demonstrates a promising approach to determine the data domain of unknown black-box machine learning models. The use of pre-trained generative models and language models enhances the efficiency and effectiveness of the method.

2. The paper presents a well-structured and organized approach to address the problem of identifying the data domain of unknown machine learning models. The heuristic search algorithm is designed to optimize the objective function, which captures both the relevance and generality of a potential candidate that represents the data domain.

### Weaknesses

#### Some Related Works


#### comment

1. The experimental setup is not clearly defined. The paper does not provide sufficient details about the datasets used, the evaluation metrics, and the baseline methods for comparison. This makes it difficult to reproduce the results and assess the effectiveness of the proposed method. Specifically, the paper lacks details on the size and composition of the datasets used for training and evaluation. Furthermore, the specific metrics used to evaluate the performance of the proposed method, such as precision, recall, or F1-score, are not clearly stated. The absence of a clear description of the baseline methods used for comparison makes it difficult to determine the relative advantages and disadvantages of the proposed method.

2. The paper does not provide a thorough analysis of the results. The discussion of the experimental results is limited, and the paper does not explore the potential reasons for the observed performance. Additionally, the paper does not address the limitations of the proposed method and potential directions for future research. For example, the paper does not discuss the sensitivity of the method to different hyperparameter settings or the impact of the choice of pre-trained models on the results. The paper also fails to explore the failure cases of the proposed method and the scenarios where it may not perform well.

### Suggestions

To address the lack of clarity in the experimental setup, the authors should provide a detailed description of the datasets used, including the size, composition, and source of the data. The authors should also clearly state the evaluation metrics used to assess the performance of the proposed method, and provide a justification for their choice. Furthermore, the authors should provide a comprehensive description of the baseline methods used for comparison, including the specific parameters and settings used for each method. This would allow for a more rigorous evaluation of the proposed method and facilitate reproducibility of the results. For example, if the method is applied to image classification, the authors should specify the number of images per class, the resolution of the images, and the preprocessing steps applied. If the method is applied to text classification, the authors should specify the length of the text samples, the vocabulary size, and the preprocessing steps applied. The authors should also specify the metrics used to evaluate the performance of the proposed method, such as accuracy, precision, recall, F1-score, or AUC, and provide a justification for their choice. The authors should also provide a detailed description of the baseline methods used for comparison, including the specific parameters and settings used for each method. This would allow for a more rigorous evaluation of the proposed method and facilitate reproducibility of the results.

To improve the analysis of the results, the authors should provide a more in-depth discussion of the experimental findings, including the potential reasons for the observed performance. The authors should also explore the sensitivity of the method to different hyperparameter settings and the impact of the choice of pre-trained models on the results. Furthermore, the authors should discuss the limitations of the proposed method and potential directions for future research. This could include exploring the use of different generative models or language models, or developing methods to improve the robustness of the proposed approach. The authors should also explore the failure cases of the proposed method and the scenarios where it may not perform well. For example, the authors could analyze the cases where the proposed method fails to identify the correct data domain, and discuss the potential reasons for these failures. The authors could also explore the impact of noise or adversarial examples on the performance of the proposed method. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method and guide future research in this area.

### Questions

1. Can you provide more details about the experimental setup, including the datasets used, the evaluation metrics, and the baseline methods for comparison?

2. Can you provide a more thorough analysis of the results, including a discussion of the potential reasons for the observed performance, the limitations of the proposed method, and potential directions for future research?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
