### Summary

This paper proposes a transformer-based framework for tabular data learning. The framework uses different embedding processes for different column types, and introduces a piece-wise linear encoding for numerical values. The proposed method is evaluated on 76 real-world tabular classification datasets and shows improved performance over existing methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper proposes a column-type aware position encoding method, which is a novel contribution.
3. The paper conducts extensive experiments on a large number of datasets and shows improved performance over existing methods.

### Weaknesses

#### Some Related Works

[1] TabTransformer: Tabular Data Modeling Using Contextual Embeddings, AAAI 2022
[2] TabLLM: Few-shot Classification of Tabular Data with Large Language Models, NeurIPS 2023
[3] TabR: Retrieval-Augmented Language Models for Tabular Data Analysis, ACL 2024

#### comment

1. The proposed method is not very novel. The idea of using transformer architecture for tabular data learning has been explored in previous work [1]. The paper does not introduce any new transformer architecture or learning objective, but rather focuses on designing column-type specific embedding layers. The core architecture remains a standard transformer, and the modifications are primarily confined to the input embedding stage. The paper could benefit from a more detailed explanation of how these embedding modifications differ fundamentally from existing approaches that also use column-specific embeddings.
2. The paper only considers classification tasks. It would be interesting to see how the proposed method performs on other tabular data tasks such as regression and structured prediction. The lack of evaluation on regression tasks is a significant limitation, as it leaves open the question of whether the proposed method can effectively handle continuous target variables. Furthermore, structured prediction tasks, such as time series forecasting or anomaly detection, could reveal additional strengths or weaknesses of the approach.
3. The paper does not compare the proposed method with other recent tabular data learning methods such as [2, 3]. The absence of comparisons with these methods makes it difficult to assess the relative performance of the proposed approach. Specifically, the paper should include comparisons with methods that also leverage large language models or retrieval mechanisms for tabular data, as these represent the current state-of-the-art in the field.

### Suggestions

The paper should provide a more detailed explanation of the proposed column-type specific embedding layers, highlighting the differences from existing methods that also use column-specific embeddings. For example, the authors could elaborate on the specific design choices for each column type, such as the piece-wise linear encoding for numerical values, and how these choices contribute to improved performance. A more thorough analysis of the impact of these design choices on the learned representations would also be beneficial. Furthermore, the paper should include ablation studies to demonstrate the contribution of each component of the proposed method, such as the column-type aware position encoding and the piece-wise linear encoding. This would help to isolate the impact of each modification and provide a more comprehensive understanding of the method's effectiveness.

The paper should extend the evaluation to include regression tasks and structured prediction tasks. For regression tasks, the authors should report metrics such as Mean Squared Error (MSE) and Root Mean Squared Error (RMSE). For structured prediction tasks, the authors should consider tasks such as time series forecasting or anomaly detection, and report appropriate metrics for these tasks. This would provide a more comprehensive evaluation of the proposed method's capabilities and limitations. The authors should also discuss the challenges and adaptations required to apply the proposed method to these different task types. This would provide valuable insights into the method's generalizability and robustness.

The paper should include comparisons with recent tabular data learning methods, such as those that leverage large language models or retrieval mechanisms. Specifically, the authors should compare their method with TabLLM [2] and TabR [3], as these methods represent the current state-of-the-art in the field. The comparisons should be conducted on the same datasets and using the same evaluation metrics, to ensure a fair and accurate assessment of the relative performance of the proposed method. The authors should also discuss the differences in the underlying assumptions and design choices of these methods, and how these differences contribute to their relative performance. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method in the context of the current state-of-the-art.

### Questions

1. How does the proposed method compare with other recent tabular data learning methods such as [2, 3]?
2. How does the proposed method perform on regression tasks and structured prediction tasks?
3. Can the proposed method handle tables with a large number of columns or high cardinality categorical features?

### Rating

5

### Confidence

4

**********
