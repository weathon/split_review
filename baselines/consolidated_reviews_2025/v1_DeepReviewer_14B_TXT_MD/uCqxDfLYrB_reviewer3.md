### Summary

The paper investigates scaling laws for time series foundation models (TSFMs), focusing on both in-distribution (ID) and out-of-distribution (OOD) performance. The authors explore how model parameters, computational resources, and dataset size affect TSFM performance across encoder-only and decoder-only Transformer architectures. They find that while scaling improves both ID and OOD performance, certain architectural choices (like those in Moirai and Chronos) enhance ID performance but limit OOD scalability. The study provides guidelines for designing scalable TSFMs, emphasizing the importance of large datasets and computational resources for robust generalization.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a comprehensive analysis of scaling laws for TSFMs, covering model parameters, computational resources, and dataset size, which is crucial for advancing the field.
2. The empirical findings are robust and well-supported by extensive experiments across multiple datasets and model architectures.
3. The authors offer practical design principles for TSFMs, which can guide future research and development in time series forecasting.

### Weaknesses

#### Some Related Works


#### comment

1. The study primarily focuses on encoder-only and decoder-only Transformers, which might limit the generalizability of the findings to other TSFM architectures. Specifically, the conclusions drawn about the trade-offs between ID and OOD performance might not hold for architectures that incorporate convolutional layers, recurrent layers, or attention mechanisms in different configurations. The lack of exploration into hybrid architectures or those with more complex attention mechanisms leaves a gap in understanding the broader landscape of TSFM scaling.
2. While the paper provides valuable insights, it could benefit from a more detailed discussion on the practical implications of the findings for real-world applications. For instance, the paper does not delve into the computational costs associated with scaling up models, nor does it discuss the trade-offs between model size, training time, and performance gains in practical scenarios. This makes it difficult for practitioners to directly apply the findings to resource-constrained environments.

### Suggestions

To enhance the generalizability of the findings, future work should investigate a wider range of TSFM architectures beyond the encoder-only and decoder-only Transformers. This should include exploring models that incorporate convolutional layers, recurrent layers (such as LSTMs or GRUs), and different attention mechanisms (like sparse or linear attention). Furthermore, hybrid architectures that combine these elements should be considered. For example, a model that uses convolutional layers for initial feature extraction followed by a Transformer encoder could be evaluated. Such an approach would provide a more comprehensive understanding of how different architectural choices impact scaling behavior and generalization capabilities. The study should also explore the impact of different pre-training strategies on the scaling laws, as this could significantly affect the observed performance trends. By including a more diverse set of architectures, the study can provide more robust and widely applicable guidelines for designing scalable TSFMs.

In addition to expanding the architectural scope, the paper should include a more detailed discussion of the practical implications of the findings. This should involve a thorough analysis of the computational costs associated with scaling up models, including the memory requirements, training time, and inference latency. The authors should also discuss the trade-offs between model size, training time, and performance gains, providing practical guidance for practitioners working in resource-constrained environments. For example, the paper could include a section that discusses how to choose the optimal model size and training parameters based on available resources and desired performance levels. This could involve providing benchmarks for different model sizes and computational budgets, allowing practitioners to make informed decisions about model selection and training strategies. Furthermore, the paper should discuss the impact of different hardware configurations on training and inference times, providing practical guidance for deploying TSFMs in real-world applications.

Finally, the paper should explore the impact of different data characteristics on the observed scaling laws. For example, the study could investigate how the length of the time series, the presence of noise, and the complexity of the underlying patterns affect the scaling behavior of TSFMs. This could involve conducting experiments on datasets with varying characteristics and analyzing how the scaling exponents change. Such an analysis would provide a more nuanced understanding of the factors that influence the performance of TSFMs and would allow for the development of more robust and adaptable models. The paper should also discuss the limitations of the current study and suggest directions for future research, such as exploring the use of more advanced optimization techniques or investigating the impact of different regularization methods on the scaling laws.

### Questions

1. How do the findings of this study compare to scaling laws observed in other domains, such as natural language processing or computer vision?
2. Are there any critical thresholds or transitions in scaling behavior as model size, compute budget, or dataset size increases?
3. How do the scaling laws differ when applied to multivariate time series data?

### Rating

6

### Confidence

4

**********
