### Summary

The paper proposes a self-supervised learning (SSL) algorithm called Prediction of Functionals from Masked Latents (PFML) for time-series data. The goal is to predict statistical functionals of the input signal corresponding to masked embeddings, given a sequence of unmasked embeddings. The authors claim that PFML avoids representation collapse and is applicable to different time-series data domains. The effectiveness of PFML is demonstrated through real-life classification tasks across three different data modalities.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and intuitive. 
2. The motivation is clear and the paper is well written.
3. The authors identified the dimensional collapse issue which is common in SSL, and the proposed method PFML mitigate this issue.

### Weaknesses

#### Some Related Works


#### comment

1. The contribution of this paper is limited. The proposed method is a combination of MAE and wav2vec 2.0, and there is no surprise or new insight here. The idea of predicting statistical functionals is not novel either, as similar approaches have been explored in time series decomposition methods within the statistical literature. The core idea of masking and predicting has been extensively used in other methods, and the specific functionals used (mean, variance, skewness, kurtosis, etc.) are standard statistical measures, making the novelty of the approach questionable.
2. The paper claims that PFML alleviates the complexity of the pre-training task, but there is no experimental evidence to support this. The authors should provide results with a large model, such as a 3-layer transformer with an embedding size of 768. The current experiments do not sufficiently demonstrate that the method is inherently less complex, only that it achieves comparable performance with a smaller model. It is important to show that the method maintains its benefits when scaled to larger models.
3. The experiments are conducted on a small-scale dataset. It would be interesting to see the performance on a large-scale dataset, such as the experimental setup in Data2Vec. The current experiments do not provide sufficient evidence that the method generalizes well to larger and more complex datasets. The lack of large-scale experiments limits the impact of the paper.
4. The experimental results are not impressive. First, the performance gain compared with MAE is minimal. Second, compared to data2vec, the proposed method even has a performance drop in some tasks. The marginal improvements over MAE, combined with the performance drops compared to data2vec in some tasks, raise concerns about the practical utility of the proposed method. The paper needs to demonstrate more substantial and consistent improvements to justify its contribution.

### Suggestions

The paper needs to more clearly articulate the novelty of the proposed approach. While the combination of masking and predicting statistical functionals is simple, the authors need to demonstrate that this combination provides a unique advantage over existing methods. The authors should explicitly compare their approach to existing time series decomposition methods in the statistical literature, highlighting the differences and advantages of their method. It is important to show that the method is not just a rehash of existing ideas, but provides a new perspective or solution to the problem of self-supervised learning for time series data. The authors should also investigate and discuss the theoretical properties of the proposed method, such as its convergence and generalization bounds.

To address the concern about the complexity of the pre-training task, the authors should conduct experiments with larger models and provide a more rigorous analysis of the computational cost of their method. The authors should compare the training time and memory usage of their method with MAE and data2vec, using the same model size and dataset. This would provide a more objective measure of the complexity of the pre-training task. Furthermore, the authors should explore the impact of different hyperparameter settings on the performance of the proposed method, such as the masking ratio and the number of functionals used. This would provide a better understanding of the sensitivity of the method to different hyperparameter choices.

The authors should conduct experiments on larger-scale datasets to demonstrate the generalizability of their method. The authors should also investigate the performance of their method on a wider range of time series tasks, such as forecasting and anomaly detection. This would provide a more comprehensive evaluation of the method's capabilities. The authors should also consider using more challenging datasets with more complex temporal dependencies. The current experimental setup is not sufficient to demonstrate the effectiveness of the proposed method in real-world scenarios. Finally, the authors should provide a more detailed analysis of the results, including error analysis and visualization of the learned representations.

### Questions

Please refer to the weakness.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
