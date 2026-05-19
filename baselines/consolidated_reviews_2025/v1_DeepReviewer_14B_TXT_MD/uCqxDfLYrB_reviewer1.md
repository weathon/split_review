### Summary

This paper investigates the scaling laws of Time Series Foundation Models (TSFMs) by examining their performance on both in-distribution (ID) and out-of-distribution (OOD) data. The authors focus on encoder-only and decoder-only Transformer architectures, evaluating how model parameters, compute resources, and dataset size impact performance. They find that while TSFMs exhibit power-law scaling in both ID and OOD settings, certain architectural choices that improve ID performance may hinder OOD scalability. The study provides guidelines for designing scalable TSFMs, emphasizing the importance of large datasets and computational resources for enhancing OOD generalization.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The investigation of scaling laws across ID and OOD data distributions is a valuable perspective.

### Weaknesses

#### Some Related Works

[1] Towards a General and Scalable Graph Foundation Model: A Survey
[2] Unified Training of Universal Time Series Forecasting Transformers
[3] Lag-Llama: A Lag-based Foundation Model for Time Series
[4] Timer: A Time Series Forecasting Foundation Model
[5] A Survey of Time Series Foundation Models
[6] Chronos: Learning the Language of Time Series

#### comment

1. The studied problem lacks novelty. Several existing works have already investigated the scaling laws of TSFMs [1, 2, 3, 4, 5, 6]. Although this paper focuses on ID and OOD scaling laws, the prior works above also include OOD experiments.
2. The findings in this paper mainly reflect the properties of the specific base model architecture, encoder-only and decoder-only Transformer. These results are not general enough for TSFMs, especially considering many recent TSFM works employ decoupled architectures, such as the encoder-decoder structure.
3. The architectural modifications introduced in this paper are not novel and have been widely adopted by previous works, such as Moirai [2] and Chronos [6].
4. The case studies of Moirai and Chronos are not novel either.
5. The practical implications of the design principles are limited. The authors suggest that increasing model size improves TSFM performance, a well-known fact in the community. Additionally, the authors do not provide evidence of the performance of the proposed design principles on other base model architectures.

### Suggestions

The paper's exploration of scaling laws for time series foundation models (TSFMs) across in-distribution (ID) and out-of-distribution (OOD) data is a valuable endeavor, but it needs to be contextualized more thoroughly within the existing literature. While the authors focus on power-law scaling, they should also acknowledge and discuss the finite-capacity scaling behavior observed in other recent works. Specifically, the paper should delve into the conditions under which different scaling behaviors emerge, such as the influence of model architecture, dataset characteristics, and optimization techniques. For instance, some studies have shown that larger models and certain architectural choices can lead to a finite-capacity regime, where performance improves linearly with scale rather than following a power law. The authors should investigate whether their findings are consistent across different model sizes and architectural variations, and discuss the implications of these different scaling regimes for practical applications. Furthermore, the paper should provide a more detailed analysis of the specific OOD datasets used in the experiments, including their characteristics and how they differ from the training data. This would help to better understand the generalization capabilities of the proposed TSFMs.

To strengthen the paper's contribution, the authors should move beyond simply observing scaling laws and focus on identifying the underlying mechanisms that drive these laws in the context of time series data. For example, they could investigate how different architectural choices, such as the use of attention mechanisms or recurrent layers, affect the scaling behavior of TSFMs. They could also explore the impact of different training techniques, such as data augmentation or regularization, on the generalization performance of these models. A deeper understanding of these mechanisms would allow for the development of more principled design guidelines for TSFMs, rather than simply relying on empirical observations. Additionally, the authors should consider the practical implications of their findings for real-world applications. For example, they could investigate the trade-offs between model size, computational cost, and performance on different OOD datasets. This would help to guide practitioners in selecting the most appropriate TSFM for their specific needs.

Finally, the paper should provide a more comprehensive evaluation of the proposed design principles. The authors should demonstrate the effectiveness of their principles on a wider range of base model architectures, including decoupled encoder-decoder structures, which are increasingly common in recent TSFM works. They should also provide more concrete examples of how their design principles can be applied in practice, including specific recommendations for model size, training data, and optimization techniques. Furthermore, the authors should consider the limitations of their study and discuss potential avenues for future research. For example, they could investigate the impact of different types of OOD data on the generalization performance of TSFMs, or explore the use of more advanced evaluation metrics that capture different aspects of forecasting accuracy. By addressing these points, the authors can significantly enhance the novelty, significance, and practical impact of their work.

### Questions

Please refer to the Weaknesses.

### Rating

3

### Confidence

4

**********
