### Summary

The paper introduces PROVCREATOR, a graph synthesis framework designed to address the under-representation of programs in system provenance datasets. It generates synthetic provenance graphs that maintain structural and attribute fidelity, improving downstream model performance for program classification and malware detection.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a significant challenge in cybersecurity by proposing a synthetic data generation method for system provenance graphs, which are crucial for intrusion detection and program identification.
2. The paper provides a comprehensive evaluation of PROVCREATOR, demonstrating its effectiveness in generating synthetic graphs that are structurally and attribute-wise similar to real-world data.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's motivation is not clearly articulated. While the authors claim that real-world datasets suffer from class imbalance, the paper lacks a detailed analysis of the specific types of programs that are underrepresented. It is unclear what characteristics of these programs make them difficult to detect or classify, and how the proposed method addresses these specific challenges. For example, are these programs short-lived, highly dynamic, or do they exhibit unique interaction patterns that are not well represented in the training data? Without a clear understanding of these aspects, the significance of the proposed method is difficult to assess.
2. The evaluation of the proposed method is limited. The paper only compares PROVCREATOR with GDSS, which is not sufficient to demonstrate its superiority over existing methods. The authors should include comparisons with other state-of-the-art graph generation techniques, especially those that have been applied to similar domains. Furthermore, the evaluation should include a more comprehensive set of metrics that capture different aspects of graph quality, such as structural similarity, attribute fidelity, and the ability to preserve the underlying data distribution. The current evaluation lacks a thorough analysis of these different aspects.
3. The paper lacks a detailed discussion of the computational cost and scalability of the proposed method. It is important to understand how the method performs on large-scale datasets and whether it can be efficiently deployed in real-world applications. The authors should provide a detailed analysis of the time and memory requirements of the method, as well as its performance on datasets of varying sizes. This analysis should include a comparison with other graph generation techniques in terms of computational efficiency and scalability.

### Suggestions

To address the lack of clarity in the motivation, the authors should provide a more detailed analysis of the class imbalance problem in system provenance datasets. This analysis should include a breakdown of the different types of programs that are underrepresented, along with an explanation of the specific characteristics that make them difficult to detect or classify. For example, the authors could analyze the distribution of program execution times, the frequency of specific API calls, or the complexity of their interaction patterns. This analysis should be supported by concrete examples and visualizations to illustrate the challenges. Furthermore, the authors should clearly articulate how the proposed method addresses these specific challenges, demonstrating its ability to generate synthetic data that is representative of the underrepresented programs. This could involve showing that the generated graphs capture the unique interaction patterns or temporal dynamics of these programs.

To strengthen the evaluation, the authors should include comparisons with other state-of-the-art graph generation techniques, particularly those that have been applied to similar domains. This would provide a more comprehensive assessment of the proposed method's performance and its advantages over existing approaches. The evaluation should also include a more diverse set of metrics that capture different aspects of graph quality, such as structural similarity, attribute fidelity, and the ability to preserve the underlying data distribution. For example, the authors could use metrics such as graph edit distance, maximum mean discrepancy, or kernel-based similarity measures to assess the structural similarity between the generated and real graphs. They should also evaluate the fidelity of the generated attributes using metrics such as BLEU score or cosine similarity. Furthermore, the authors should provide a detailed analysis of the results, explaining why the proposed method performs better or worse than the baselines on different metrics.

Finally, the authors should provide a detailed analysis of the computational cost and scalability of the proposed method. This analysis should include a breakdown of the time and memory requirements of the method, as well as its performance on datasets of varying sizes. The authors should also compare the computational efficiency and scalability of their method with other graph generation techniques. This analysis should be supported by empirical results, demonstrating the method's ability to handle large-scale datasets. The authors should also discuss the limitations of their method in terms of computational cost and scalability, and suggest potential improvements for future work. This would provide a more complete picture of the method's practical applicability and its potential for real-world deployment.

### Questions

1. How does PROVCREATOR handle the generation of graphs with varying sizes and complexities, especially in scenarios with highly dynamic or rapidly changing programs?
2. What are the limitations of PROVCREATOR in terms of scalability and computational cost, especially when dealing with large-scale datasets?

### Rating

3

### Confidence

3

**********
