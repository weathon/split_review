### Summary

This paper proposes a new example-based explanation method, HD-Explain, which leverages the Kernelized Stein Discrepancy (KSD) to identify training samples that provide the best predictive support to a test point. The authors demonstrate the effectiveness of HD-Explain through comprehensive quantitative and qualitative evaluations, showing its superior performance in terms of fidelity, consistency, and computation efficiency compared to existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel approach to example-based explanation by leveraging Kernelized Stein Discrepancy (KSD), which is a unique perspective in the field of model explainability.
- The paper is well-written and easy to follow.
- The authors provide a comprehensive evaluation of HD-Explain, including both quantitative and qualitative analyses, which strengthens the validity of their claims.
- The proposed method shows superior performance in terms of fidelity, consistency, and computation efficiency compared to existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of HD-Explain, which could be a concern for large-scale datasets.
- The paper could benefit from a more in-depth discussion of the limitations of HD-Explain and potential areas for future research.

### Suggestions

The paper should include a more thorough analysis of the computational cost associated with HD-Explain. While the authors mention that the method is efficient, a detailed breakdown of the time complexity for each step, including the computation of the KSD and the selection of training samples, would be beneficial. This analysis should consider the impact of dataset size and dimensionality on the runtime. Furthermore, it would be helpful to compare the computational cost of HD-Explain with that of other example-based explanation methods, providing a clear understanding of the trade-offs involved. For instance, the authors could analyze the time complexity of computing the KSD as a function of the number of training samples and the dimensionality of the input space. This would allow readers to better assess the scalability of the proposed method for different types of datasets. The authors should also discuss the practical implications of the computational cost, such as the feasibility of using HD-Explain for very large datasets or real-time applications.

In addition to the computational analysis, the paper should provide a more detailed discussion of the limitations of HD-Explain. While the authors demonstrate the effectiveness of their method, it is important to acknowledge the potential scenarios where the method might not perform optimally. For example, the authors could discuss the sensitivity of HD-Explain to the choice of kernel parameters in the KSD. A more detailed analysis of the impact of different kernel choices on the quality of the explanations would be valuable. Furthermore, the authors should discuss the potential limitations of relying on a single explanation method. It is possible that HD-Explain might not capture all the relevant aspects of the model's decision-making process, and that other explanation methods might provide complementary insights. The authors could also discuss the potential for combining HD-Explain with other explanation techniques to obtain a more comprehensive understanding of the model's behavior. A more thorough discussion of the limitations would provide a more balanced view of the proposed method and guide future research in this area.

Finally, the paper should include a more detailed discussion of potential future research directions. While the authors mention that future work could explore the use of HD-Explain for different types of models and tasks, they could also elaborate on specific research questions that are particularly relevant to the proposed method. For example, the authors could discuss the potential for using HD-Explain to improve the interpretability of complex models, such as deep neural networks. They could also explore the use of HD-Explain for tasks such as model debugging and fairness analysis. Furthermore, the authors could discuss the potential for extending HD-Explain to handle more complex data types, such as images and text. A more detailed discussion of future research directions would help to guide the development of new and improved explanation methods.

### Questions

- How does HD-Explain perform on datasets with high dimensionality or complex structures?
- What are the potential challenges of applying HD-Explain to real-world datasets, and how can these challenges be addressed?
- How does the choice of kernel parameters in the KSD affect the quality of the explanations provided by HD-Explain?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
