### Summary

This paper investigates the scaling laws of time series foundation models (TSFMs) across different data distributions and model architectures. The authors conduct extensive experiments to explore the scaling behaviors of encoder-only and decoder-only Transformers on both in-distribution (ID) and out-of-distribution (OOD) data. The study provides insights into how model size, computational resources, and dataset size affect TSFM performance, offering practical design principles for developing scalable TSFMs.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow the methodology and results.
2. The experiments are thorough, covering a wide range of model sizes, compute budgets, and dataset sizes.
3. The study provides valuable insights into the scaling laws of TSFMs, which can guide future research and development in this area.

### Weaknesses

#### Some Related Works


#### comment

1. The study focuses exclusively on univariate time series forecasting, which may limit the generalizability of the findings to multivariate time series.
2. The paper does not explore the impact of different context window lengths and forecast horizons on the scaling behavior of TSFMs, which could be important factors in practical applications.
3. The analysis of scaling laws is primarily empirical, and the paper lacks a theoretical framework to explain the observed phenomena.
4. The comparison between encoder-only and decoder-only Transformers is somewhat limited, and the paper could benefit from a more in-depth analysis of the architectural differences and their implications for scalability.
5. The study does not investigate the transferability of the scaling laws to different time series domains or tasks, which could be a valuable direction for future research.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of context window length and forecast horizon on the observed scaling laws. Specifically, the authors should explore how varying these parameters affects the power law exponents and the overall performance of the models. For instance, do longer context windows lead to different scaling behaviors for encoder-only versus decoder-only architectures? It would be valuable to see experiments that systematically vary both context window and forecast horizon, perhaps using a grid search approach, to map out the parameter space and identify any critical thresholds or transitions in scaling behavior. This would provide a more complete picture of the factors influencing TSFM performance and enhance the practical applicability of the findings.

Furthermore, the paper should delve deeper into the architectural differences between encoder-only and decoder-only Transformers and their implications for scalability. While the paper notes that encoder-only models are more scalable, it does not provide a detailed analysis of why this is the case. A more in-depth investigation could explore the role of attention mechanisms, the impact of different normalization techniques, and the effect of varying the number of layers and attention heads in each architecture. For example, do encoder-only models benefit from more efficient information propagation due to their bidirectional attention, or are there other factors at play? A more detailed analysis of these architectural nuances would provide valuable insights into the design of scalable TSFMs.

Finally, the study should consider expanding its scope to include multivariate time series data. While the focus on univariate data is understandable for isolating scaling effects, many real-world applications involve multivariate time series. The authors should discuss the potential challenges and opportunities associated with extending their findings to multivariate settings. For example, how might the presence of cross-correlations between different time series channels affect the scaling laws? Would the observed power law exponents change, and if so, how? Addressing these questions would significantly enhance the generalizability and practical relevance of the study. Additionally, exploring the transferability of the scaling laws to different time series domains and tasks would be a valuable direction for future research, as it would provide insights into the robustness and adaptability of the proposed models.

### Questions

1. How do the scaling laws observed in this study generalize to multivariate time series data?
2. What is the theoretical basis for the observed scaling laws, and can a formal framework be developed to explain them?
3. How do different context window lengths and forecast horizons affect the scaling behavior of TSFMs?
4. Are there any critical thresholds or transitions in scaling behavior as model size, compute budget, or dataset size increases?
5. How do the findings of this study compare to scaling laws observed in other domains, such as natural language processing or computer vision?

### Rating

5

### Confidence

4

**********
