### Summary

This paper presents a new dataset and model for 3D language understanding. The dataset is a combination of existing datasets, and the model is a modification of LLaVA-1.5. The authors show that the dataset and model can be trained from scratch, and the model can be adapted to 3D tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The dataset is a valuable contribution to the community, and the model is a good baseline for future work. The authors have shown that the dataset and model can be trained from scratch, and the model can be adapted to 3D tasks.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the dataset's characteristics, such as the distribution of object categories, the density of 3D annotations, or the diversity of viewpoints. This lack of analysis makes it difficult to assess the true value and potential biases of the dataset. The model architecture is a simple combination of existing components, and the paper does not provide a clear justification for the specific choices made in the architecture, such as the selection of DINOv2 over other potential visual encoders, or the specific arrangement of fine-tuning stages. The lack of ablation studies makes it difficult to understand the contribution of each component. The experiments are not comprehensive enough to demonstrate the effectiveness of the proposed method. The paper only compares against a limited number of baselines, and the results are not consistently superior across all benchmarks. The paper also lacks a detailed error analysis, which would be helpful in understanding the limitations of the proposed method.

### Suggestions

The authors should provide a more detailed analysis of the proposed dataset, including the distribution of object categories, the density of 3D annotations, and the diversity of viewpoints. This analysis should also include a comparison with existing datasets to highlight the unique characteristics of the new dataset. For example, the authors could analyze the overlap in object categories and annotation density with existing datasets, and discuss how the unified format addresses the limitations of individual datasets. Furthermore, the authors should investigate the impact of different viewpoints on the performance of the model, and discuss how the dataset was constructed to ensure sufficient coverage of viewpoints. This would provide a more comprehensive understanding of the dataset's strengths and weaknesses.

To address the concerns about the model architecture, the authors should conduct ablation studies to justify the specific choices made. This should include a comparison of different visual encoders, such as DINOv2, CLIP-ViT, and ViT-L/14, and an analysis of their impact on the model's performance. The authors should also investigate the effect of different fine-tuning stages, and provide a rationale for the chosen arrangement. For example, the authors could compare the performance of the model with and without the visual chain-of-thought prompting, and analyze the contribution of each stage to the overall performance. The ablation studies should be presented in a clear and concise manner, with detailed explanations of the results and their implications. This would help to understand the contribution of each component and to identify potential areas for improvement.

Finally, the authors should expand the experimental evaluation to include a wider range of baselines and benchmarks. This should include comparisons with state-of-the-art methods for 3D reasoning, and an analysis of the model's performance on different types of queries. The authors should also conduct a detailed error analysis to identify the limitations of the proposed method and to understand the types of errors that the model is prone to make. This analysis should include examples of failure cases and should provide insights into the underlying causes of these failures. The authors should also discuss the limitations of the current evaluation and suggest future directions for research.

### Questions

See weaknesses.

### Rating

6

### Confidence

3

**********
