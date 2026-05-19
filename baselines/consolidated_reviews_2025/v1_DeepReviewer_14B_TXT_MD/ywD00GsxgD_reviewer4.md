### Summary

The paper presents a method for generating synthetic tumors in healthy livers and using them as validation data to improve the generalization performance of the model. The paper also proposes a continual learning framework that continuously trains AI models on a stream of out-domain data with synthetic tumors. The experiments show that the proposed method improves the model's performance on both in-domain and out-domain test sets, especially for detecting tiny liver tumors.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel approach to using synthetic data as validation data to improve the generalization performance of the model.
2. The paper proposes a continual learning framework that continuously trains AI models on a stream of out-domain data with synthetic tumors.
3. The experiments show that the proposed method improves the model's performance on both in-domain and out-domain test sets, especially for detecting tiny liver tumors.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the potential limitations of the proposed method, such as the risk of overfitting to the synthetic data or the need for careful tuning of the hyperparameters.
2. The paper does not compare the proposed method with other state-of-the-art methods for tumor detection in CT volumes.

### Suggestions

The paper should include a more thorough discussion of the potential for overfitting to the synthetic data. While the authors mention the use of a large number of synthetic tumors, they should also explore techniques to mitigate the risk of the model learning to recognize specific patterns in the synthetic data that do not generalize to real tumors. For example, they could investigate the use of data augmentation techniques on the real training data to increase its diversity and reduce the gap between real and synthetic data distributions. Furthermore, the authors should analyze the sensitivity of the model's performance to the number of synthetic tumors used for validation and the diversity of these tumors. A detailed analysis of the impact of different synthetic tumor characteristics (e.g., size, shape, texture) on model performance would also be beneficial. This would help to understand the limitations of the proposed method and provide guidance for its practical application.

Additionally, the paper needs to provide a more comprehensive comparison with existing state-of-the-art methods for tumor detection in CT volumes. The authors should not only compare their method with a baseline that uses real data for training and validation, but also with other methods that utilize synthetic data or data augmentation techniques. This comparison should include a detailed analysis of the performance of different methods on both in-domain and out-domain test sets, as well as an analysis of the computational cost and complexity of each method. The authors should also discuss the advantages and disadvantages of their method compared to other approaches, and provide a clear justification for the use of their method in specific scenarios. This would help to establish the novelty and significance of the proposed method and provide a more complete understanding of its performance.

Finally, the paper should include a more detailed description of the hyperparameter tuning process. The authors should specify the range of hyperparameters explored, the optimization algorithm used, and the criteria used to select the optimal hyperparameters. They should also analyze the sensitivity of the model's performance to different hyperparameter settings. This would help to ensure the reproducibility of the results and provide guidance for the practical application of the proposed method. Furthermore, the authors should discuss the computational resources required for training and validation, and provide an estimate of the time and cost associated with the proposed method.

### Questions

1. How does the proposed method compare with other state-of-the-art methods for tumor detection in CT volumes?
2. What are the potential limitations of the proposed method, and how can they be addressed?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
