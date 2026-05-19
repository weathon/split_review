### Summary

The paper introduces R-EDL, a novel approach to Evidential Deep Learning (EDL) that relaxes two non-essential settings in the traditional EDL framework. The authors identify that the prior weight parameter, which governs the balance between leveraging the proportion and magnitude of evidence, is often overlooked and rigidly set to the number of classes in existing EDL methods. They propose treating this parameter as an adjustable hyperparameter, allowing for a more flexible and accurate uncertainty estimation. Additionally, the paper highlights that the variance-minimized regularization term in traditional EDL encourages the Dirichlet PDF to approach a Dirac delta function, exacerbating overconfidence. To address this, R-EDL deprecates this regularization term and directly optimizes the expectation of the Dirichlet PDF. Through extensive experiments on various benchmarks, including confidence estimation and out-of-distribution detection, the authors demonstrate the effectiveness of R-EDL in alleviating overconfidence and providing more accurate uncertainty estimation compared to traditional EDL and other state-of-the-art methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a comprehensive analysis of the significance of the prior weight parameter in the subjective logic framework, highlighting its role in balancing the trade-off between leveraging the proportion and magnitude of evidence. This analysis offers valuable insights into the inner workings of EDL and its potential limitations.

2. The authors propose a novel approach, R-EDL, that relaxes the rigid setting of the prior weight parameter and deprecates the variance-minimized regularization term in traditional EDL. This relaxation allows for a more flexible and accurate uncertainty estimation, addressing the overconfidence issue often observed in EDL.

3. The paper presents extensive experiments on multiple benchmarks for uncertainty estimation tasks, including confidence estimation and out-of-distribution detection. The results demonstrate the effectiveness of R-EDL in various scenarios, including classical, few-shot, noisy, and video-modality settings. The comprehensive experimental evaluation strengthens the credibility of the proposed method.

4. The authors provide a rigorous mathematical exposition of subjective logic and a detailed introduction to EDL, ensuring a solid theoretical foundation for their proposed method. The clear and well-structured presentation enhances the readability and understanding of the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the computational complexity of R-EDL compared to traditional EDL and other uncertainty estimation methods. Providing insights into the computational overhead introduced by the proposed relaxations would help readers assess the practical applicability of R-EDL in resource-constrained environments.

2. While the paper demonstrates the effectiveness of R-EDL on various benchmarks, it would be valuable to explore its performance on more complex and real-world datasets. Evaluating R-EDL on datasets with higher dimensionality, noise, or imbalanced classes could further validate its robustness and generalizability.

3. The paper primarily focuses on image classification tasks. It would be interesting to investigate the applicability of R-EDL to other domains, such as natural language processing or time-series analysis. Exploring the performance of R-EDL in these diverse domains would broaden its impact and demonstrate its versatility.

### Suggestions

The paper would be strengthened by a more thorough analysis of the computational demands of R-EDL. While the authors propose a novel approach to evidential deep learning, the practical implications of their method, particularly in terms of computational cost, need further clarification. A detailed breakdown of the time and memory requirements for both training and inference, compared to standard EDL and other uncertainty estimation techniques, would be highly beneficial. This should include a discussion of how the adjustable hyperparameter for the prior weight impacts computational overhead. For instance, does optimizing this hyperparameter require significant additional computation, and how does this scale with the size of the dataset and the complexity of the model? Furthermore, it would be useful to explore the potential for approximations or optimizations that could mitigate any increased computational burden, making R-EDL more practical for real-world applications with limited resources. This analysis should also consider the impact of different hardware configurations on the performance of R-EDL.

Expanding the experimental evaluation to include more challenging datasets is crucial for establishing the robustness and generalizability of R-EDL. The current evaluation, while comprehensive within the image classification domain, does not fully address the potential limitations of the method in more complex scenarios. Specifically, the paper should include experiments on datasets with higher dimensionality, such as those found in medical imaging or remote sensing, where the feature space is significantly larger and more complex. Additionally, the performance of R-EDL should be evaluated on datasets with varying levels of noise and class imbalance, which are common in real-world applications. This would provide a more comprehensive understanding of the method's strengths and weaknesses and its ability to handle the complexities of real-world data. Furthermore, it would be beneficial to explore the sensitivity of R-EDL to different hyperparameter settings, particularly the prior weight, in these more challenging scenarios.

Finally, the paper should broaden its scope by investigating the applicability of R-EDL to other domains beyond image classification. The current focus on image data limits the potential impact of the proposed method. Exploring the performance of R-EDL in domains such as natural language processing or time-series analysis would demonstrate its versatility and potential for wider adoption. For example, in natural language processing, R-EDL could be used for tasks such as sentiment analysis or text classification, where uncertainty estimation is crucial. Similarly, in time-series analysis, R-EDL could be applied to tasks such as anomaly detection or forecasting, where accurate uncertainty quantification is essential. This would not only broaden the impact of the paper but also provide valuable insights into the generalizability of the proposed method across different types of data and tasks.

### Questions

1. Could the authors provide more insights into the computational complexity of R-EDL compared to traditional EDL and other uncertainty estimation methods? This would help readers assess the practical applicability of R-EDL in resource-constrained environments.

2. How does R-EDL perform on more complex and real-world datasets with higher dimensionality, noise, or imbalanced classes? Evaluating R-EDL on such datasets would further validate its robustness and generalizability.

3. Have the authors considered applying R-EDL to other domains beyond image classification, such as natural language processing or time-series analysis? Exploring the performance of R-EDL in these diverse domains would broaden its impact and demonstrate its versatility.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
