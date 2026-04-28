# Application of Metric Transformation in One-Step Retrosynthesis

- Decision: Reject
- Avg Score: 2.33
- Scores: 1, 1, 5

## Abstract
In this article, we investigate the impact of Deep Metric Learning and Transformer architecture on predicting the retrosynthesis of Simplified Molecular Input Line Entry System (SMILES) chemical compounds.

We demonstrate that combining the Attention mechanism with Proxy Anchor Loss is effective for classification tasks due to its strengths in capturing both local and global contexts and differentiating between various classes. 

Our approach, which requires no prior chemical knowledge, achieves promising results on the USPTO-FULL dataset, with accuracies of 53.4\%, 83.8\%, 90.6\%, and 97.5\% for top-1, top-5, top-10, and top-50 predictions, respectively.

We further validate the practical application of our approach by correctly predicting the retrosynthesis pathways for 63 out of 100 randomly selected compounds from the ChEMBL database and for 39 out of 60 compounds selected by Bayer's chemists and from PubChem.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The article explores using Deep Metric Learning and Transformer architecture for predicting chemical compound retrosynthesis in SMILES format. It shows that combining Attention mechanisms with Proxy Anchor Loss improves classification by capturing local and global contexts, achieving promising accuracy on the USPTO-FULL dataset without requiring prior chemical knowledge.

### Strengths
The use of Attention mechanisms and Proxy Anchor Loss enhances the performance of classification tasks by capturing both local and global contexts.

### Weaknesses
The retrosynthesis accuracy is relatively low compared to state-of-the-art models.
The model is restricted to template-based approaches, which hinders its applicability and scalability across a broader spectrum of chemical environments.

### Questions
Why are key methods like RetroExplainer excluded from the comparison？
How do your results compare to the state-of-the-art on the USPTO-50k dataset?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
Retrosynthesis is a central challenge in chemistry, crucial for effectively leveraging newly discovered and complex molecules. In this article, the authors present a framework that combines proxy anchor loss with a depth metric Transformer to improve retrosynthesis accuracy in template-based methods, framing the inverse synthesis problem as a classification task. Although the results demonstrate some improvement, the method lacks novelty and does not achieve optimal accuracy.

### Strengths
None

### Weaknesses
1. Retrosynthesis accuracy is low: Compared with state-of-the-art models such as LocalRetro, the retrosynthesis accuracy is low, performing poorly across multiple datasets.
2. Lacks comparative experiments: There is a lack of comparative experiments to demonstrate the improvement achieved by the applied method, making it difficult to see the advantages of this approach.
3. Limited diversity and practicality: The model is restricted to template-based methods and cannot be extended to a broader chemical space.
4. Inconsistent writing format: The manuscript's format presents issues,  such as the abstract, which lacks clear segmentation into distinct sections. This impacts the clarity and structured presentation of key information, making it challenging for readers to discern the main contributions and findings.

### Questions
1. The comparison lacks certain key methods, such as RetroExplainer and RetroKNN, and the reported results do not achieve state-of-the-art performance on the USPTO-50k dataset.

2. In Appendix A.2, only the limitations of the ring break model are discussed; however, its functional role in the model is not clearly explained.

3. Please clarify the distinction between the proxy anchor method employed and a clustering approach. Additionally, why is the same approach not applicable for segmenting larger subsets?

4. Section 3.1 assumes that the additional 11,567 data points are all failures for both our model and the baseline. Why are some of these not classified as correct predictions, at least in proportion?

5. Why was the inference speed of different models not benchmarked on the same device to ensure fair comparison?

6. While template coverage has improved, the results do not surpass those in previous studies. Could you provide an explanation for this outcome?

7. Are there corresponding ablation studies to validate the contribution of each component in the proposed framework? How do you explain the significant discrepancies between the results in Table 5 and those of the baseline model?

8. Minor formatting issues include a missing period at line 182, an extraneous period at line 278, and an extra space before the period on line 433.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the author addresses template imbalance in inverse synthesis by introducing a hierarchical classification approach. Besides, they use k-means clustering to split large template classes into subclasses and Implement proxy anchor loss for classification. Moreover, subclasses were mapped back to the original template categories.

### Strengths
The research effectively addresses a practical challenge in the field - the imbalance of template distributions in datasets. The approach demonstrates measurable improvements on the USPTO full dataset, offering a practical solution to reduce intra-class variance. The methodology shows progression in handling imbalanced data, with a clear focus on improving classification accuracy through hierarchical structuring.

### Weaknesses
Despite its contributions, the paper suffers from several limitations. The methodology presentation lacks clarity and precision, requiring interpretation to understand the core concepts. Specifically, the description of how k-means clustering is integrated with the hierarchical classification is not sufficiently detailed, making it difficult to reproduce the results. While improvements are shown, the achieved 50% accuracy falls behind the current state-of-the-art performance. The paper also omits comparisons with recent superior methods, raising questions about its relative contribution to the field. It is unclear how the method compares to other approaches that directly address class imbalance, such as re-sampling or cost-sensitive learning. Additionally, the overall writing style lacks precision and clarity, making it challenging to fully grasp the technical details without considerable effort.

### Questions
What is the computational overhead introduced by the k-means clustering step, and how was the optimal number of subclasses determined? 
Could the approach be enhanced by implementing more sophisticated clustering methods beyond k-means? 
How does this method perform when applied to datasets other than USPTO full?

### Soundness
2

### Presentation
2

### Contribution
2
