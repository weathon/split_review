### Summary

This paper introduces Longitudinal Ensemble Integration (LEI), a framework for sequential classification using multimodal longitudinal data. The authors evaluate LEI's performance on early dementia detection using the TADPOLE dataset and compare it against existing approaches. LEI leverages intermediate base predictions from individual data modalities and identifies important features for dementia diagnosis.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in healthcare, i.e., sequential classification using multimodal longitudinal data. The proposed LEI framework has potential applications in various domains beyond healthcare.
2. The authors provide a comprehensive experimental evaluation of LEI on the TADPOLE dataset, comparing it against multiple baselines and configurations.

### Weaknesses

#### Some Related Works


#### comment

1. The technical contribution of the paper is limited. The proposed LEI framework is a straightforward combination of existing techniques - ensemble integration and LSTM. The novelty is not clearly established, as the paper does not adequately demonstrate how the specific combination of these techniques leads to a significant advancement over existing methods. The core idea of using base predictors with an LSTM is not inherently novel, and the paper lacks a deep exploration of the unique challenges addressed by this particular combination.
2. The paper lacks a thorough analysis of the proposed method. There is no ablation study to understand the contribution of different components of LEI, no discussion of the computational complexity, and no exploration of the sensitivity of the method to hyperparameter settings. The absence of these analyses makes it difficult to assess the robustness and practical applicability of the proposed framework. For example, it is unclear how the performance of LEI would change with different choices of base predictors or LSTM architectures, and how the method scales with increasing data size.
3. The experimental evaluation is limited to a single dataset (TADPOLE). While the authors mention ADNI, it's not clear if LEI was evaluated on other datasets. The lack of evaluation on diverse datasets raises concerns about the generalizability of the findings. The TADPOLE dataset, while valuable, may not fully represent the complexities of other multimodal longitudinal data, and the performance of LEI on other datasets remains an open question.

### Suggestions

The paper would significantly benefit from a more in-depth analysis of the proposed LEI framework. Specifically, a thorough ablation study is needed to understand the contribution of each component. This should include experiments where different base predictors are used, and the impact of varying the LSTM architecture is assessed. For example, the authors could compare the performance of LEI with different types of base predictors, such as decision trees, support vector machines, or simple neural networks, and analyze how the choice of base predictor affects the overall performance. Furthermore, the impact of the number of LSTM layers and the size of the hidden states should be investigated to understand the sensitivity of the method to these hyperparameters. This analysis would provide valuable insights into the design choices and help to identify the optimal configuration of LEI for different datasets and tasks.

Additionally, the paper should include a detailed discussion of the computational complexity of LEI. This should include an analysis of the time and memory requirements of the method, as well as a comparison with the computational cost of the baseline methods. The authors should also explore the scalability of LEI to larger datasets and longer time series. This analysis would help to assess the practical applicability of the method and identify potential bottlenecks. For example, the authors could provide a breakdown of the computational cost of each step in the LEI pipeline, such as the training of base predictors, the computation of intermediate predictions, and the training of the LSTM. This would allow readers to understand the computational trade-offs of using LEI and make informed decisions about its use.

Finally, the experimental evaluation should be expanded to include additional datasets. This would help to assess the generalizability of the findings and demonstrate the robustness of LEI. The authors should consider evaluating LEI on datasets with different characteristics, such as different modalities, sample sizes, and time resolutions. This would provide a more comprehensive assessment of the method's performance and help to identify its strengths and weaknesses. For example, the authors could evaluate LEI on datasets from other domains, such as finance or transportation, to demonstrate its applicability beyond healthcare. This would also help to establish the broader impact of the proposed framework and its potential for real-world applications.

### Questions

1. How does the proposed LEI framework compare with other state-of-the-art methods for sequential classification using multimodal longitudinal data?
2. What are the limitations of the proposed LEI framework, and how can they be addressed in future work?
3. How does the performance of LEI vary with different choices of base predictors and LSTM architectures?

### Rating

3

### Confidence

4

**********
