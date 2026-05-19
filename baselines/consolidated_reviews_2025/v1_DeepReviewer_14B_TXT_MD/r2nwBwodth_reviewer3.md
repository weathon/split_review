### Summary

The paper presents a novel self-supervised learning (SSL) algorithm for time-series data, named Prediction of Functionals from Masked Latents (PFML). The key innovation is predicting statistical functionals of masked input signals based on unmasked embeddings, which helps avoid representation collapse. The method is validated across three different real-life classification tasks: infant posture and movement classification, emotion recognition from speech, and sleep stage classification from EEG data. PFML outperforms a similar SSL method and is competitive with state-of-the-art SSL methods, without suffering from representation collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel SSL algorithm, PFML, which effectively addresses the issue of representation collapse, a common problem in SSL methods. This is a significant contribution to the field of time-series data analysis.
2. The experimental results demonstrate that PFML is superior to a conceptually similar pre-existing SSL method and competitive against the current state-of-the-art SSL method. The method's effectiveness is validated across three different real-life classification tasks, showcasing its versatility and robustness.
3. The paper is well-structured and clearly written, making it easy to follow the methodology and understand the results. The authors provide a comprehensive analysis of their method, including comparisons with other SSL methods and discussions on the implications of their findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed comparison with other SSL methods, particularly those that are not conceptually similar to PFML. This would provide a more comprehensive understanding of PFML's strengths and weaknesses relative to the broader landscape of SSL techniques.
2. While the paper demonstrates PFML's effectiveness on three specific datasets, it would be valuable to see how the method performs on a wider range of time-series data and classification tasks. This would help establish the generalizability of PFML and its applicability to different domains.
3. The paper does not extensively discuss the computational complexity and resource requirements of PFML. Providing this information would be crucial for practitioners who are considering implementing the method in real-world applications.

### Suggestions

To strengthen the paper, a more thorough comparison with diverse self-supervised learning (SSL) methods is needed. The current comparison primarily focuses on methods conceptually similar to PFML, such as masked autoencoders. A more comprehensive analysis should include methods that employ different pre-training objectives, such as contrastive learning approaches (e.g., SimCLR, MoCo) or predictive coding methods (e.g., PredCLIP). This would involve not only reporting performance metrics but also analyzing the learned representations, for example, by visualizing the embedding spaces or evaluating the transferability of the learned features to other tasks. Furthermore, it would be beneficial to discuss the specific advantages and disadvantages of PFML compared to these alternative approaches, highlighting the scenarios where PFML is expected to excel or underperform. This would provide a more nuanced understanding of PFML's position within the broader landscape of SSL techniques and help readers make informed decisions about its applicability.

To further establish the generalizability of PFML, the authors should evaluate its performance on a wider range of time-series datasets and classification tasks. The current evaluation is limited to three specific datasets, which may not fully represent the diversity of time-series data encountered in real-world applications. Including datasets with different characteristics, such as varying sampling rates, signal-to-noise ratios, and underlying phenomena, would provide a more robust assessment of PFML's capabilities. For example, evaluating PFML on datasets from domains like finance, weather forecasting, or industrial monitoring would demonstrate its versatility and applicability to different domains. Additionally, exploring a broader range of classification tasks, such as anomaly detection or time-series forecasting, would further showcase the potential of PFML beyond the current classification tasks. This would provide a more comprehensive understanding of the method's strengths and limitations across different problem settings.

Finally, the paper should provide a more detailed analysis of the computational complexity and resource requirements of PFML. This should include not only the number of parameters but also the training time, memory usage, and inference time. This information is crucial for practitioners who are considering implementing the method in real-world applications, especially those with limited computational resources. The authors should also discuss the scalability of PFML to larger datasets and longer time series. Furthermore, it would be beneficial to compare the computational cost of PFML with other SSL methods, providing a clear understanding of the trade-offs between performance and computational resources. This would allow readers to make informed decisions about the practical feasibility of using PFML in their specific applications.

### Questions

1. How does PFML compare to other SSL methods that are not conceptually similar, in terms of both performance and computational complexity?
2. Can the authors provide more insights into the choice of statistical functionals used in PFML and how these choices impact the performance of the method?
3. Are there any plans to extend the evaluation of PFML to other types of time-series data or classification tasks? If so, what are the expected challenges and how does PFML plan to address them?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
