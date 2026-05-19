### Summary

The paper proposes a systematic evaluation framework for tabular data synthesis algorithms. The authors propose new metrics for fidelity, privacy, and utility, and conduct extensive evaluations of eight synthesizers on twelve real-world datasets. The paper also introduces a unified tuning objective that can improve the quality of synthetic data for all methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important and timely problem of evaluating tabular data synthesis algorithms. The paper proposes a comprehensive and rigorous evaluation framework that covers three essential aspects: fidelity, privacy, and utility. The paper also proposes new metrics that address the limitations of existing metrics. For example, the Wasserstein distance can handle both numerical and categorical attributes, and the membership disclosure score can provide a worst-case privacy measurement. 
2. The paper conducts extensive experiments on a wide range of synthesizers and datasets, and presents the results in a clear and informative way. The paper also provides a unified tuning objective that can improve the performance of synthesizers. 
3. The paper makes a significant contribution to the field of data synthesis, by providing a systematic and robust evaluation framework that can help researchers and practitioners to compare and choose different synthesizers. The paper also reveals some interesting findings, such as the trade-off between fidelity and privacy, and the effectiveness of diffusion models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the limitations of the proposed framework and metrics. For example, how do they handle high-dimensional or skewed data? How do they account for the potential attacks or adversaries that might try to infer sensitive information from the synthetic data? How do they address the ethical or legal implications of data synthesis, such as data ownership, data governance, and data bias?
2. The paper does not provide any guidelines or recommendations for practitioners on how to use the framework or metrics in real-world scenarios. For example, how should they select the appropriate synthesizer for their specific data and task? How should they interpret the results of the evaluation? How should they deal with the trade-offs between different aspects, such as fidelity, privacy, and utility?

### Suggestions

The paper should delve deeper into the limitations of the proposed evaluation framework, particularly concerning high-dimensional and skewed data. For high-dimensional data, the authors should explore how the Wasserstein distance behaves, as its computational cost increases significantly with dimensionality. It would be beneficial to analyze the performance of the proposed metrics on datasets with varying dimensionality and provide insights into when the framework might become less effective. For skewed data, the authors should investigate how the proposed metrics, especially the fidelity metric based on Wasserstein distance, are affected by imbalanced distributions. It is possible that the metrics might be dominated by the majority class or attribute, leading to inaccurate evaluations. The authors could consider incorporating techniques such as re-sampling or weighted metrics to address this issue and provide a more robust evaluation framework. Furthermore, the paper should include a discussion on the sensitivity of the proposed metrics to different types of data transformations, such as normalization or encoding, as these transformations are commonly used in practice.

To address the lack of practical guidance, the paper should provide a more detailed discussion on how practitioners can use the proposed framework and metrics in real-world scenarios. This should include a step-by-step guide on how to select the appropriate synthesizer for a given dataset and task. The authors could consider providing a decision tree or a set of rules based on the characteristics of the data and the desired trade-offs between fidelity, privacy, and utility. For example, they could suggest using statistical methods when privacy is paramount, and deep generative models when fidelity is the priority. The paper should also provide a detailed explanation of how to interpret the results of the evaluation, including the meaning of the different metrics and their relative importance. The authors could provide examples of how to use the results to make informed decisions about the choice of synthesizer and the quality of the synthetic data. Furthermore, the paper should discuss how to deal with the trade-offs between different aspects, such as fidelity, privacy, and utility, and provide practical recommendations on how to balance these competing objectives.

Finally, the paper should include a more thorough discussion of the ethical and legal implications of data synthesis. This should include a discussion of data ownership, data governance, and data bias. The authors should consider the potential risks of using synthetic data, such as the possibility of perpetuating existing biases or creating new ones. They should also discuss the legal and regulatory frameworks that might apply to data synthesis and the use of synthetic data. The paper should provide practical recommendations on how to mitigate these risks and ensure that data synthesis is used in an ethical and responsible manner. This could include guidelines on data anonymization, data validation, and data auditing. The authors should also consider the potential impact of data synthesis on different stakeholders, including data subjects, data owners, and data users.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
