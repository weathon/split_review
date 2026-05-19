### Summary

This paper introduces a novel self-supervised learning (SSL) algorithm for time-series data called Prediction of Functionals from Masked Latents (PFML). The key idea is to predict statistical functionals of the input signal corresponding to masked embeddings, given a sequence of unmasked embeddings. This approach aims to avoid representation collapse, a common issue in SSL methods where the model outputs a constant input-invariant feature representation. The authors demonstrate the effectiveness of PFML on three different real-life classification tasks across three different data modalities: infant posture and movement classification from multi-sensor inertial measurement unit data, emotion recognition from speech data, and sleep stage classification from EEG data. The results show that PFML is superior to a conceptually similar pre-existing SSL method and competitive against the current state-of-the-art SSL method, while also being conceptually simpler and without suffering from representation collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel SSL algorithm for time-series data that addresses the issue of representation collapse, which is a significant contribution to the field.
- The method is conceptually simpler than other SSL methods and does not require careful tuning of hyperparameters, making it more straightforward to apply to new time-series data domains.
- The experimental results demonstrate the effectiveness of PFML across three different real-life classification tasks and data modalities, showing that it is superior to a conceptually similar pre-existing SSL method and competitive against the current state-of-the-art SSL method.
- The paper is well-written and clearly explains the proposed method and its advantages.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of why PFML avoids representation collapse, which could be a valuable addition to the paper.
- The experimental results are limited to three classification tasks and data modalities. It would be beneficial to evaluate PFML on a wider range of tasks and data modalities to further demonstrate its effectiveness.
- The paper does not compare PFML to other SSL methods that are specifically designed for time-series data, which could provide a more comprehensive evaluation of its performance.

### Suggestions

The lack of theoretical justification for why PFML avoids representation collapse is a significant weakness. While the empirical results are promising, a deeper understanding of the underlying mechanisms would greatly strengthen the paper. Specifically, the authors should explore the properties of the learned latent space and how the prediction of statistical functionals influences the distribution of embeddings. For instance, analyzing the variance and covariance of the embeddings across different time steps and input samples could provide insights into the stability and diversity of the learned representations. Furthermore, it would be beneficial to investigate the relationship between the choice of statistical functionals and the resulting embedding space. A theoretical analysis, even if not fully rigorous, could provide a more solid foundation for the proposed method and guide future research in this area. This could involve exploring concepts from information theory or statistical learning to quantify the information preserved by the functional prediction task.

Expanding the experimental evaluation to include a broader range of time-series datasets and tasks is crucial for demonstrating the generalizability of PFML. The current evaluation is limited to three specific classification tasks, which may not fully capture the diversity of time-series data. It would be beneficial to include datasets with different characteristics, such as varying sampling rates, signal-to-noise ratios, and temporal dependencies. Furthermore, evaluating PFML on regression tasks, anomaly detection, or forecasting tasks would provide a more comprehensive assessment of its capabilities. For example, applying PFML to datasets from domains like finance, healthcare, or environmental monitoring could reveal its strengths and limitations in different contexts. Additionally, it would be valuable to compare PFML against other SSL methods that are specifically designed for time-series data, such as those based on contrastive learning or predictive coding. This would provide a more direct comparison and highlight the unique advantages of PFML.

Finally, the paper should include a more detailed analysis of the computational cost and efficiency of PFML. While the authors mention that PFML is conceptually simpler, they do not provide a quantitative comparison of the training time and memory requirements compared to other SSL methods. This information is crucial for practical applications, especially when dealing with large-scale time-series datasets. It would be beneficial to report the training time per epoch, the number of parameters, and the memory usage for different datasets and model configurations. Furthermore, the authors should discuss the scalability of PFML to longer time series and larger datasets. This could involve exploring techniques for efficient computation of statistical functionals or using distributed training strategies. A thorough analysis of the computational aspects would make the paper more practical and useful for researchers and practitioners.

### Questions

- Can you provide a theoretical analysis of why PFML avoids representation collapse?
- How does PFML perform on other types of time-series data and classification tasks?
- How does PFML compare to other SSL methods that are specifically designed for time-series data?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
