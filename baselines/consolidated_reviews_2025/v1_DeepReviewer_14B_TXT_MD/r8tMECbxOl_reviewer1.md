### Summary

The paper introduces the TDTransformer, a novel framework designed to enhance transformer-based models for tabular data. The paper addresses key challenges such as the heterogeneous nature of tabular data and the difficulty in interpreting numerical values. The proposed approach includes distinct embedding processes for different column types, alignment layers for mapping these embeddings to a common space, and piece-wise linear encoding for numerical values.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper tackles the underperformance of transformer-based models in tabular data, which is an important area in machine learning. 

The paper evaluates the proposed method on a large number of real-world datasets, which strengthens the validity of the findings.

### Weaknesses

#### Some Related Works


#### comment

The proposed method is complex, combining multiple components (distinct embedding processes, alignment layers, piece-wise linear encoding). This complexity could make the model difficult to implement and tune in practice. 

The experimental results are not very significant, in addition, some important benchmarks such as TabPFN and T2G-Former are missing.

### Suggestions

The paper introduces a novel framework, TDTransformer, for tabular data, but several aspects warrant further consideration. The complexity of the proposed model, with its multiple components, raises concerns about its practical applicability. While the authors argue that each component addresses a specific challenge, the combined effect of these components on computational cost and hyperparameter tuning needs further investigation. For instance, the distinct embedding processes for different column types, alignment layers, and piece-wise linear encoding all introduce additional parameters and computational steps. A detailed analysis of the computational overhead and a sensitivity analysis of the hyperparameters would be beneficial to assess the practical feasibility of the proposed method. Furthermore, the paper should provide more clarity on how these components interact and whether there are any dependencies or constraints in their application. It would be useful to see a breakdown of the computational cost associated with each component, and how this cost scales with the size and complexity of the datasets.

Additionally, the experimental results, while evaluated on a large number of datasets, do not demonstrate substantial improvements over existing methods. The lack of comparison with important benchmarks such as TabPFN and T2G-Former is a significant oversight. These models have shown strong performance in tabular data processing, and their exclusion makes it difficult to assess the true novelty and effectiveness of the proposed approach. The paper should include a comprehensive comparison with these benchmarks, using the same experimental settings, to provide a more robust evaluation of the TDTransformer. This comparison should not only focus on average performance but also analyze the performance on individual datasets to identify the specific scenarios where the proposed method excels or falls short. A more detailed analysis of the results, including statistical significance tests, would also be beneficial to determine the reliability of the observed improvements.

Finally, the paper should address the limitations of the proposed method more explicitly. While the authors mention the challenges of tabular data, they do not discuss the potential limitations of their approach in handling specific types of datasets or tasks. For example, how does the model perform on datasets with a large number of categorical features or datasets with complex interactions between features? A discussion of these limitations would provide a more balanced view of the proposed method and guide future research in this area. Furthermore, the paper should explore the potential for simplifying the model architecture without compromising its performance. This could involve investigating alternative embedding techniques or exploring the possibility of combining some of the components. A more thorough analysis of the model's limitations and potential for simplification would enhance the overall contribution of the paper.

### Questions

See above

### Rating

3

### Confidence

5

**********
