### Summary

This paper proposes Swin4TS algorithm. It incorporates the window-based attention and hierarchical representation techniques from the Swin Transformer and applies them to the long-term forecasting of time series data. The window-based attention enables the algorithm to achieve linear computational complexity, while the hierarchical architecture allows the representation on various scales. Furthermore, Swin4TS can flexibly adapt to channel-dependence and channel-independence strategies, in which the former can simultaneously capture correlations in both the channel and time dimensions, and the latter shows high training efficiency for large datasets. Swin4TS outperforms the latest baselines and achieves state-of-the-art performance on 8 benchmark datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The authors propose the Swin4TS algorithm for LTSF, motivated by the similarity of data structure between time series and image patches. Swin4TS has linear computational complexity and allows representation across multiple scales. Besides, it is designed to be compatible to either channeldependence and channel-independence strategies, which consider the multivariate correlation or not, respectively.

The authors evaluate Swin4TS on 32 prediction tasks across 8 benchmark datasets and achieve performance surpassing the latest baseline methods (both Transformer-based and non-Transformer-based) on almost all tasks.

The authors successfully apply techniques from ViT to LTSF, indicating the feasibility of modeling time series modality using architectures from image modality. This allows advancements at the forefront of ViTs to facilitate research in time series analysis.

### Weaknesses

#### Some Related Works


#### comment

The authors only provide the inference time and memory usage for one baseline model (PatchTST). A more comprehensive comparison with other baselines would be helpful for a thorough evaluation.

The authors do not discuss the limitations of the proposed method in detail. For example, the effectiveness of Swin4TS/CD may depend on the quality and quantity of the training data, as well as the complexity of the underlying time series patterns.

### Suggestions

The paper would benefit from a more thorough analysis of the computational efficiency of the proposed Swin4TS algorithm. While the authors mention linear computational complexity, a more detailed comparison of inference time and memory usage against a wider range of baseline models is needed. Specifically, the current comparison only includes PatchTST, which is insufficient to fully assess the practical advantages of Swin4TS. Including models such as Informer, Autoformer, and other state-of-the-art time series forecasting methods would provide a more comprehensive understanding of the computational trade-offs. Furthermore, it would be beneficial to analyze the scaling behavior of Swin4TS with respect to input sequence length and the number of channels, as this would provide insights into its applicability to different problem settings. This analysis should also include a breakdown of the computational cost associated with different components of the model, such as the window-based attention mechanism and the hierarchical representation, to better understand the sources of computational efficiency.

In addition to computational efficiency, a more detailed discussion of the limitations of Swin4TS is necessary. The authors should explore the sensitivity of the model to the quality and quantity of training data. For instance, how does the performance of Swin4TS degrade when trained on noisy or limited data? Furthermore, the authors should investigate the model's ability to capture complex time series patterns, such as non-stationarity and seasonality. It would be valuable to analyze the performance of Swin4TS on datasets with varying degrees of complexity and to identify the types of time series patterns that the model struggles to capture. This analysis should also consider the impact of different hyperparameter settings on the model's performance and robustness. A more thorough discussion of these limitations would provide a more balanced view of the proposed method and guide future research directions.

Finally, the paper should include a more detailed analysis of the channel-dependent (CD) and channel-independent (CI) strategies. While the authors mention that CD can capture correlations in both channel and time dimensions, and CI shows high training efficiency, a more in-depth analysis of the trade-offs between these two strategies is needed. For example, under what conditions does the CD strategy significantly outperform the CI strategy, and vice versa? How does the performance of each strategy vary with the number of channels and the complexity of the time series data? A more detailed analysis of these trade-offs would provide valuable insights into the practical applicability of each strategy and help users choose the most appropriate strategy for their specific problem. Furthermore, the authors should investigate the impact of different window sizes and patch lengths on the performance of both CD and CI strategies, as this could provide further insights into the optimal configuration of the model.

### Questions

1. The authors only provide the inference time and memory usage for one baseline model (PatchTST). A more comprehensive comparison with other baselines would be helpful for a thorough evaluation.
2. The authors do not discuss the limitations of the proposed method in detail. For example, the effectiveness of Swin4TS/CD may depend on the quality and quantity of the training data, as well as the complexity of the underlying time series patterns.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
