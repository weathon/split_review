### Summary

This paper proposes a transformer-based model for tabular data. The authors propose a method to embed different types of columns (numerical, categorical, and binary) into a common embedding space, and a column-type-aware positional encoding to enhance the model's understanding of numerical values. The authors conduct experiments on 76 OpenML classification datasets and show that TDTransformer significantly outperforms existing methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct experiments on 76 OpenML datasets, which is a large number of datasets.
3. The authors compare TDTransformer with 13 baselines, including XGBoost, CatBoost, and SwitchTab.
4. The authors conduct extensive ablation studies to analyze the impact of different components of TDTransformer.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the paper is limited. The authors propose three different embedding processes for numerical, categorical, and binary columns, and a column-type-aware positional encoding. However, these techniques are not new and have been widely used in other areas of machine learning. The paper does not provide a strong justification for why these specific techniques are particularly well-suited for tabular data, beyond the fact that they are commonly used. The lack of a novel core mechanism or a significant departure from existing practices makes the contribution seem incremental rather than transformative.
2. The authors do not provide a theoretical analysis of the proposed method. While empirical results are valuable, a theoretical understanding of why the proposed method works, and under what conditions it is expected to perform well, is crucial for establishing the robustness and generalizability of the approach. The absence of such analysis limits the paper's ability to provide deep insights into the method's behavior.
3. The authors do not compare the proposed method with some recent transformer-based methods, such as TabLLM and TableLLama. The lack of comparison with state-of-the-art transformer-based methods makes it difficult to assess the relative performance of the proposed method and its potential for further improvement. The absence of these comparisons leaves a gap in the evaluation of the method's competitiveness.

### Suggestions

The paper would benefit from a more detailed explanation of the specific challenges posed by heterogeneous tabular data that are not addressed by existing techniques. While the authors mention the heterogeneity, they do not delve into the nuances of how different types of columns interact and how their embedding strategies specifically address these interactions. For instance, a discussion on how the proposed embedding methods handle the varying scales and distributions of numerical and categorical features, and how the column-type-aware positional encoding mitigates positional bias, would be beneficial. Furthermore, the authors should provide a more in-depth analysis of the limitations of existing methods when dealing with heterogeneous tabular data, and how their approach overcomes these limitations. This would strengthen the motivation for the proposed method and highlight its unique contributions.

To address the lack of theoretical analysis, the authors could consider providing some insights into the convergence properties of the proposed method or the generalization bounds. While a full theoretical treatment might be beyond the scope of the paper, a discussion on the theoretical underpinnings of the method would add significant value. For example, the authors could discuss the conditions under which the proposed embedding strategies are guaranteed to converge to a good solution, or how the proposed positional encoding affects the model's ability to generalize to unseen data. This would provide a more solid foundation for the empirical results and increase the paper's impact. Additionally, the authors should consider including a discussion on the computational complexity of the proposed method, especially in comparison to existing methods. This would help readers understand the practical implications of using the proposed method in real-world scenarios.

Finally, the paper should include a more comprehensive comparison with recent transformer-based methods for tabular data, such as TabLLM and TableLLama. This comparison should not only focus on performance metrics but also on other aspects such as computational efficiency, robustness, and ease of implementation. The authors should also discuss the potential advantages and disadvantages of their method compared to these existing approaches. This would provide a more complete picture of the state-of-the-art and help readers understand the relative strengths and weaknesses of the proposed method. Furthermore, the authors should consider including a discussion on the potential for future research directions, such as exploring different embedding strategies or positional encodings, and how these could further improve the performance of the proposed method.

### Questions

See Weaknesses.

### Rating

5

### Confidence

4

**********
