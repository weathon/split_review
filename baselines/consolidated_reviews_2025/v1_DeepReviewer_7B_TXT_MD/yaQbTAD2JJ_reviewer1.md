### Summary

This paper proposes a new dataset and a new model architecture for 3D reasoning. The dataset is built by merging multiple existing datasets into a unified format. The model architecture is based on LLaVA-1.5, with a new visual encoder DINOv2 and additional finetuning stages. The model is evaluated on 3D grounding and question answering benchmarks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well written and easy to follow.
2. The idea of merging multiple datasets into a unified format is interesting and useful.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed dataset is a simple combination of existing datasets. The paper does not provide a detailed analysis of the dataset's characteristics, such as the distribution of object categories, the density of 3D annotations, or the diversity of viewpoints. This lack of analysis makes it difficult to assess the true value and potential biases of the dataset.
2. The model architecture is a simple combination of existing components. The paper does not provide a clear justification for the specific choices made in the architecture, such as the selection of DINOv2 over other potential visual encoders, or the specific arrangement of fine-tuning stages. The lack of ablation studies makes it difficult to understand the contribution of each component.
3. The experiments are not comprehensive enough to demonstrate the effectiveness of the proposed method. The paper only compares against a limited number of baselines, and the results are not consistently superior across all benchmarks. The paper also lacks a detailed error analysis, which would be helpful in understanding the limitations of the proposed method.

### Suggestions

The authors should provide a more detailed analysis of the proposed dataset, including the distribution of object categories, the density of 3D annotations, and the diversity of viewpoints. This analysis should also include a comparison with existing datasets to highlight the unique characteristics of the new dataset. Furthermore, the authors should conduct ablation studies to justify the specific choices made in the model architecture, such as the selection of DINOv2 and the arrangement of fine-tuning stages. These studies should systematically evaluate the impact of each component on the overall performance of the model. For example, the authors could compare the performance of the model with different visual encoders or different fine-tuning strategies. This would help to understand the contribution of each component and to identify potential areas for improvement.

To strengthen the experimental evaluation, the authors should compare against a wider range of baselines, including state-of-the-art methods for 3D reasoning. The comparison should not only focus on overall performance but also on specific aspects, such as the model's ability to handle different types of queries or to generalize to unseen data. The authors should also conduct a detailed error analysis to identify the limitations of the proposed method and to understand the types of errors that the model is prone to make. This analysis should include examples of failure cases and should provide insights into the underlying causes of these failures. This would help to guide future research and to develop more robust and reliable models.

Finally, the authors should consider releasing the dataset and the code to the public. This would allow other researchers to reproduce the results and to build upon the work presented in the paper. The availability of the code and the dataset would also facilitate further research in the area of 3D reasoning. The authors should also provide clear instructions on how to use the dataset and the code, and they should ensure that the data is properly documented. This would make the work more accessible and would contribute to the advancement of the field.

### Questions

1. What is the motivation for merging multiple datasets into a unified format? What are the advantages of the unified format compared to the original datasets?
2. What is the motivation for using DINOv2 as the visual encoder? What are the advantages of DINOv2 compared to other potential visual encoders?
3. What is the motivation for the specific arrangement of fine-tuning stages? What are the advantages of this arrangement compared to other possible arrangements?
4. What is the motivation for using LLaVA-1.5 as the base model? What are the advantages of LLaVA-1.5 compared to other potential base models?

### Rating

3

### Confidence

4

**********
