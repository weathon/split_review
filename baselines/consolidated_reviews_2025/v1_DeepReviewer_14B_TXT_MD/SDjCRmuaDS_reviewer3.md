### Summary

The paper proposes an autoregressive model for molecular generation that uses molecular fragments as building blocks. The model grows molecules in a semi-order-agnostic manner, allowing for flexible and chemically valid molecule generation. The model is trained on a dataset of organic compounds and evaluated on its ability to generate molecules with desired properties.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper introduces a novel approach to molecular generation by using fragments as building blocks and growing molecules in a semi-order-agnostic manner.
- The model is trained on a dataset of organic compounds and evaluated on its ability to generate molecules with desired properties, demonstrating its potential for practical applications.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a thorough comparison with existing molecular generation models, which makes it difficult to assess the relative performance and advantages of the proposed approach. Specifically, the absence of comparisons against established methods like RNN-based sequence models or graph-based generative models makes it hard to gauge the novelty and effectiveness of the fragment-based approach. The evaluation should include metrics that are standard in the field, such as validity, uniqueness, and novelty of generated molecules, in addition to the property-based metrics.
- The evaluation of the model is limited to a specific dataset and set of properties, which may not generalize to other types of molecules or materials. The dataset used seems to be relatively small and focused on a specific class of organic compounds, raising concerns about the model's ability to handle more diverse chemical spaces. The paper should include an analysis of the model's performance on a more diverse set of molecules and properties, or at least discuss the limitations of the current evaluation.
- The paper does not provide a detailed analysis of the model's limitations or potential failure cases, which would be valuable for understanding its practical applicability. For example, it is unclear how the model handles complex ring systems or molecules with unusual functional groups. A discussion of the types of molecules that the model struggles to generate would be beneficial.
- The paper does not provide a detailed analysis of the model's limitations or potential failure cases, which would be valuable for understanding its practical applicability. For example, it is unclear how the model handles complex ring systems or molecules with unusual functional groups. A discussion of the types of molecules that the model struggles to generate would be beneficial.

### Suggestions

To address the lack of comparative analysis, the authors should benchmark their model against several established molecular generation methods. This should include both sequence-based models (e.g., RNNs or Transformers operating on SMILES strings) and graph-based models (e.g., graph neural networks generating molecular graphs). The comparison should not only focus on the target properties but also on standard metrics for generative models, such as the validity, uniqueness, and novelty of the generated molecules. Furthermore, the authors should provide a detailed analysis of the computational cost of their approach compared to these baselines. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method. The authors should also consider using a standardized benchmark dataset, such as the ZINC database, to facilitate comparison with other methods.

To improve the evaluation, the authors should expand their analysis to include a more diverse set of molecules and properties. This could involve using datasets with a wider range of chemical structures and functional groups, as well as evaluating the model's performance on different types of target properties. The authors should also investigate the model's ability to generate molecules with specific structural features, such as particular ring systems or functional groups. This could be done by analyzing the distribution of these features in the generated molecules and comparing it to the distribution in the training data. Furthermore, the authors should provide a more detailed analysis of the model's performance on molecules with varying sizes and complexities. This would help to identify any limitations of the model and provide insights into its scalability.

Finally, the authors should provide a more detailed analysis of the model's limitations and potential failure cases. This should include a discussion of the types of molecules that the model struggles to generate, as well as the reasons for these failures. For example, the authors could analyze the model's performance on molecules with complex ring systems, unusual functional groups, or specific structural motifs. This analysis should also include a discussion of the limitations of the fragment-based approach and how these limitations might be addressed in future work. The authors should also consider providing visualizations of the generated molecules, highlighting both successful and unsuccessful cases, to provide a more intuitive understanding of the model's behavior.

### Questions

- How does the model perform on molecules with complex ring systems or unusual functional groups?
- Can the model be extended to generate molecules with specific structural features or properties that are not well represented in the training data?
- How does the model handle the trade-off between generating novel molecules and generating molecules with desired properties?

### Rating

3

### Confidence

3

**********
