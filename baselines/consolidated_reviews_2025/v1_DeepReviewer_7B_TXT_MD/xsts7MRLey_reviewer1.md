### Summary

This paper presents a benchmark for evaluating unsupervised domain adaptation (UDA) techniques for time series classification. The benchmark includes seven new benchmark datasets and a comprehensive evaluation of existing UDA methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. 
- The paper provides a comprehensive evaluation of existing UDA methods for time series classification.

### Weaknesses

#### Some Related Works


#### comment

 - The contribution of the paper is limited. The paper mainly focuses on the evaluation of existing methods. The contribution of the benchmark is not clear. 
- The datasets used in the paper are mainly from the UDA literature. It would be better to include more real-world datasets.
- The paper does not provide a clear guideline on how to select the most suitable UDA method for a given time series dataset.

### Suggestions

The paper would benefit from a more detailed discussion on the specific challenges posed by time series data that make it distinct from other data modalities when applying unsupervised domain adaptation (UDA). While the paper mentions the use of temporal information, it would be beneficial to elaborate on how this temporal aspect influences the selection and performance of UDA methods. For instance, the inherent sequential nature of time series data introduces dependencies between data points, which can significantly impact the effectiveness of domain adaptation techniques. The paper should discuss how methods designed for independent and identically distributed (i.i.d.) data might fail when applied to time series, and how the proposed benchmark addresses these specific challenges. Furthermore, the paper should provide a more in-depth analysis of the characteristics of the newly introduced datasets, highlighting the unique properties that make them suitable for evaluating UDA methods in the time series domain. This analysis should go beyond simply stating that the datasets are from the UDA literature and should focus on the specific domain shifts and complexities that are present in each dataset. For example, are the shifts due to changes in sensor characteristics, experimental conditions, or other factors? Understanding these nuances is crucial for the benchmark's value to the research community.

To enhance the practical utility of the benchmark, the paper should provide more concrete guidance on how to select the most appropriate UDA method for a given time series dataset. This could involve developing a set of rules or heuristics based on the characteristics of the datasets, such as the type of domain shift, the size of the source and target domains, and the complexity of the time series patterns. For example, the paper could analyze the performance of different UDA methods across various datasets and identify patterns that correlate specific dataset characteristics with the effectiveness of certain methods. This analysis could lead to the development of a decision tree or a set of guidelines that practitioners can use to select the most suitable method for their specific application. The paper should also discuss the limitations of the benchmark and identify areas for future research, such as the development of new UDA methods specifically tailored for time series data. This would help to position the benchmark within the broader context of UDA research and highlight its potential for guiding future advancements.

Finally, while the inclusion of real-world datasets is a positive step, the paper should provide a more detailed justification for the selection of these datasets. It is important to explain why these datasets are representative of real-world challenges and how they differ from the synthetic datasets commonly used in the UDA literature. The paper should also discuss the potential biases or limitations of these real-world datasets and how these might affect the evaluation of UDA methods. For example, are the domain shifts in these datasets similar to those encountered in practical applications? Are there any specific characteristics of these datasets that make them particularly challenging for UDA? Addressing these questions would strengthen the paper's claims about the practical relevance of the benchmark and its ability to evaluate UDA methods in real-world scenarios. Furthermore, the paper should consider including a wider range of real-world datasets to ensure that the benchmark is comprehensive and representative of the diverse challenges faced in time series analysis.

### Questions

- How to select the most suitable UDA method for a given time series dataset?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
