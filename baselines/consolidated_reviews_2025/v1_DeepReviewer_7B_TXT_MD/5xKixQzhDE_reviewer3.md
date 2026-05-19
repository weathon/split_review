### Summary

This paper proposes a new dataset condensation method for hyperparameter search. The main idea is to match the hypergradient of the original dataset and the condensed dataset. This method is evaluated on both image and graph datasets and shows good performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. 
2. The paper is well-written and easy to follow. 
3. The proposed method is evaluated on both image and graph datasets and shows good performance.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on image and graph datasets. It would be better to evaluate the proposed method on other types of datasets, such as audio and text datasets.
2. The proposed method is compared with only a few baselines. It would be better to compare the proposed method with more baselines, such as [1, 2].
3. The proposed method is compared with baselines on the Spearman's rank correlation of architecture/hyperparameter rankings. It would be better to also compare the proposed method with baselines on the test performance of the best architecture/hyperparameter selected by the baselines and the proposed method.
4. The proposed method is compared with baselines on the Spearman's rank correlation of architecture/hyperparameter rankings. It would be better to also compare the proposed method with baselines on the test performance of the best architecture/hyperparameter selected by the baselines and the proposed method.

### Suggestions

The paper introduces an interesting approach to dataset condensation by focusing on matching hypergradients. However, the evaluation is limited in scope, focusing primarily on image and graph datasets. To strengthen the paper, it is crucial to evaluate the method on a wider variety of data modalities, such as audio and text. For audio, the method could be tested on tasks like speech recognition or music generation, while for text, it could be evaluated on tasks like sentiment analysis or text classification. This would provide a more comprehensive understanding of the method's generalizability and robustness across different data types. Furthermore, the current evaluation relies heavily on Spearman's rank correlation, which, while informative, does not directly assess the practical impact of the method. It is essential to also evaluate the test performance of the best architecture/hyperparameter selected by the proposed method and the baselines. This would provide a more direct measure of the method's ability to identify the optimal architecture/hyperparameter and its practical utility in hyperparameter search.

In addition to expanding the dataset types, the paper should also compare the proposed method with a broader range of baselines. The current comparison is limited, and it is important to include more state-of-the-art dataset condensation techniques. This would provide a more rigorous evaluation of the proposed method's performance and its relative advantages and disadvantages. Specifically, the paper should consider comparing against methods that also focus on preserving the performance of architectures/hyperparameters, as this is the core contribution of the proposed method. Furthermore, the paper should also consider including baselines that use different condensation strategies, such as those based on feature matching or gradient matching, to provide a more comprehensive comparison. This would help to better understand the strengths and weaknesses of the proposed method compared to existing approaches.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. While the paper mentions that the method is efficient, it does not provide a detailed analysis of the time and memory requirements. This is important for practical applications, as the computational cost can be a limiting factor for large-scale datasets. The paper should also discuss the scalability of the method and its performance on very large datasets. Furthermore, the paper should also discuss the sensitivity of the method to different hyperparameters and provide guidelines for selecting the optimal hyperparameters. This would make the method more practical and easier to use for other researchers. A more thorough analysis of these aspects would significantly improve the paper's overall quality and impact.

### Questions

1. In Table 1, why the performance of the proposed method is lower than the performance of the oracle?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
