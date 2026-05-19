### Summary

This paper proposes a data selection method for instruction tuning of LLMs. The authors focus on the learnability of whole batch data and the coverage of the data distribution. They conduct experiments on three datasets with two LLMs to demonstrate the effectiveness of their method.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The experiments are comprehensive. The authors conduct experiments on three datasets with two LLMs and use various evaluation metrics.
2. The method is efficient. The authors show that their method can achieve comparable performance while using less data.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation of this paper is not clear. The authors should explain why loss-based stratified sampling is important and why maximizing the relative distance between samples within a batch is important. The connection between these two aspects and the overall goal of improving instruction tuning needs to be more explicitly stated. It's unclear how these specific choices lead to better model performance compared to other data selection strategies.
2. The authors claim that they focus on the learnability of whole batch data, but they still select data based on loss. This seems contradictory. The authors should clarify this point. The notion of 'learnability' needs to be more precisely defined. If the method still relies on loss, it's not clear how it differs from existing loss-based selection methods. The authors need to explain how their approach to loss calculation and usage differs from standard practices and how this relates to their concept of 'learnability'.
3. The authors claim that they maximize the relative distance between samples within a batch to enhance diversity, but they only consider samples within various score ranges in a batch. This does not guarantee diversity. The authors should provide more evidence to support their claim. Simply selecting samples from different score ranges does not inherently ensure diversity in the feature space or semantic content of the data. The authors need to demonstrate that their method effectively captures a diverse range of data characteristics, not just variations in loss scores.
4. The authors claim that they utilize Hessian gradient optimization to guide the selection strategy for subsequent batches, but they do not provide any details about how they do this. The authors should provide more details about their method. The lack of detail makes it difficult to assess the validity and effectiveness of this component. The authors need to explain the specific mathematical formulation and implementation details of how the Hessian gradient information is used to guide data selection in subsequent batches.

### Suggestions

The paper would benefit from a more detailed explanation of the motivation behind the proposed method. The authors should clearly articulate why loss-based stratified sampling is crucial for instruction tuning and how maximizing the relative distance between samples within a batch contributes to improved model performance. Specifically, they should explain the theoretical underpinnings of their approach, detailing how these choices lead to better generalization and learning compared to other data selection strategies. For instance, they could discuss how their method addresses potential issues with data redundancy or bias that might arise from using a simple loss-based selection approach. Furthermore, the authors should provide a more rigorous definition of 'learnability' and explain how their method captures this concept beyond simply using loss as a selection criterion. This could involve discussing the relationship between loss, gradient magnitudes, and the potential for a sample to contribute to model improvement. A more thorough explanation of the theoretical basis for their approach would significantly strengthen the paper's contribution.

To address the concerns about diversity, the authors should provide a more detailed analysis of how their method ensures that selected samples are not only from different score ranges but also represent a diverse set of data characteristics. This could involve visualizing the feature space of the selected samples or using metrics that quantify the diversity of the selected data. For example, they could use techniques like t-SNE or UMAP to visualize the distribution of selected samples in a lower-dimensional space and demonstrate that their method selects samples that are spread across different regions. Additionally, they could use metrics like the average pairwise distance between samples in the feature space to quantify the diversity of the selected data. The authors should also provide a more detailed explanation of how they use Hessian gradient optimization to guide the selection strategy for subsequent batches. This should include the specific mathematical formulation of the Hessian gradient calculation and how this information is used to adjust the selection criteria. A clear and detailed explanation of this process is crucial for the reproducibility and understanding of the proposed method.

Finally, the authors should provide a more thorough comparison of their method with existing data selection techniques. This should include a discussion of the advantages and disadvantages of their approach compared to other methods, as well as a detailed analysis of the computational cost and scalability of their method. The authors should also provide more details about the experimental setup, including the specific hyperparameters used for each experiment and the rationale behind their choices. This would allow other researchers to reproduce their results and further validate their findings. The authors should also consider including ablation studies to demonstrate the impact of each component of their method on the overall performance. This would help to better understand the contribution of each aspect of their approach and identify potential areas for improvement.

### Questions

1. What is the definition of loss-based stratified sampling? The authors should provide a formal definition of this concept.
2. What is the definition of learnability? The authors should provide a formal definition of this concept.
3. How do the authors ensure diversity when they only consider samples within various score ranges in a batch?
4. How do the authors utilize Hessian gradient optimization to guide the selection strategy for subsequent batches?

### Rating

3

### Confidence

3

**********
