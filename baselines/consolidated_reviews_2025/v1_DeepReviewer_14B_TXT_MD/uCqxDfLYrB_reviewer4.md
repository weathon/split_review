### Summary

This paper investigates the scaling laws of time series foundation models (TSFMs) across in-distribution (ID) and out-of-distribution (OOD) data, focusing on encoder-only and decoder-only Transformer architectures. The authors explore how model parameters, compute budgets, and dataset sizes impact performance, revealing that encoder-only Transformers generally exhibit better scalability than decoder-only variants. Additionally, they find that while advanced architectures like Moirai and Chronos improve ID performance, they do not enhance OOD generalization. The paper provides practical guidelines for designing scalable TSFMs based on these findings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical gap in understanding the scaling behavior of TSFMs, particularly in OOD scenarios, which is essential for real-world applications.
2. The study includes a comprehensive analysis of encoder-only and decoder-only Transformers, as well as comparisons with state-of-the-art models like Moirai and Chronos, providing valuable insights into the impact of architectural choices on scalability.
3. The authors provide practical design principles based on their findings, which can guide future research and development in TSFMs.

### Weaknesses

#### Some Related Works


#### comment

1. The study focuses exclusively on univariate time series forecasting, which may limit the generalizability of the findings to multivariate time series. The analysis does not explore how the observed scaling laws might change when dealing with multiple correlated time series, which is a common scenario in real-world applications. The interactions between different time series could introduce complexities not captured by univariate analysis, potentially leading to different scaling behaviors.
2. The paper does not explore the impact of different context window lengths and forecast horizons on the scaling behavior of TSFMs. The choice of context window and forecast horizon can significantly affect model performance, and it is unclear how these factors interact with the observed scaling laws. For instance, longer context windows might reveal different scaling patterns compared to shorter ones, and the optimal window length could vary depending on the specific time series characteristics.

### Suggestions

To address the limitations of focusing solely on univariate time series, future work should investigate the scaling behavior of TSFMs in multivariate settings. This would involve analyzing how the number of input time series affects the scaling laws for both encoder-only and decoder-only architectures. Specifically, it would be beneficial to explore how the dimensionality of the input data interacts with model size, compute budget, and dataset size. For example, does the optimal model size scale differently with the number of input time series? Does the compute budget required to achieve a certain level of performance increase linearly or non-linearly with the number of input series? Furthermore, it would be valuable to examine the impact of different correlation structures between the input time series on the observed scaling laws. This could involve generating synthetic datasets with varying degrees of correlation and analyzing how the scaling behavior changes. Such an analysis would provide a more comprehensive understanding of the applicability of the proposed scaling laws to real-world scenarios.

Additionally, the study should investigate the impact of context window length and forecast horizon on the scaling behavior of TSFMs. This could involve conducting experiments with different context window lengths and forecast horizons and analyzing how the scaling exponents change. For example, does the scaling behavior become more or less pronounced with longer context windows? Does the optimal model size or compute budget vary with the forecast horizon? It would also be beneficial to explore the interaction between context window length, forecast horizon, and model architecture. For instance, do encoder-only and decoder-only architectures exhibit different sensitivities to these factors? Understanding these interactions is crucial for designing TSFMs that can effectively handle time series with varying characteristics. The analysis should also consider the computational cost associated with different context window lengths and forecast horizons, as this could impact the practical applicability of the proposed scaling laws.

Finally, the paper should provide more detailed guidelines on how to apply the observed scaling laws in practice. This could involve providing specific recommendations on how to choose the optimal model size, compute budget, and dataset size for a given task and resource constraint. For example, the authors could provide a set of rules of thumb or a decision tree that practitioners can use to guide their model design. This would make the findings of the paper more accessible and useful to the broader research community. Furthermore, it would be beneficial to explore the limitations of the proposed scaling laws and identify scenarios where they might not hold. This would help practitioners understand the boundaries of applicability of the proposed guidelines and avoid potential pitfalls.

### Questions

1. How do the scaling laws observed in this study generalize to multivariate time series data?
2. What is the theoretical basis for the observed scaling laws, and can a formal framework be developed to explain them?
3. How do different context window lengths and forecast horizons affect the scaling behavior of TSFMs?
4. Are there any critical thresholds or transitions in scaling behavior as model size, compute budget, or dataset size increases?
5. How do the findings of this study compare to scaling laws observed in other domains, such as natural language processing or computer vision?

### Rating

8

### Confidence

3

**********
