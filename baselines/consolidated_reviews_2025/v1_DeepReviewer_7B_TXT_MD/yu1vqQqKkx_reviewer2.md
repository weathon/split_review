### Summary

This paper proposes a novel method, LICO, for molecular optimization, which leverages pretrained large language models (LLMs) to perform black-box optimization (BBO). LICO extends the capabilities of LLMs by adding embedding and prediction layers for molecules and their scores. It is trained on a combination of intrinsic and synthetic functions, enabling it to generalize to unseen molecular properties. The authors demonstrate that LICO achieves state-of-the-art performance on the Practical Molecular Optimization (PMO) benchmark, outperforming existing methods in terms of sample efficiency and accuracy.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to leveraging LLMs for molecular optimization, which is a challenging and important problem in drug discovery and materials science. By adapting LLMs to a non-language domain, the authors open up new possibilities for applying these powerful models to scientific tasks.

2. The semi-synthetic training strategy is a creative way to enable LLMs to generalize to unseen molecular properties. By training on a combination of intrinsic and synthetic functions, the model learns to extract relevant features from molecular data, which is crucial for effective optimization.

3. The paper is well-written and organized, making it easy to follow the methodology and results. The authors provide a clear explanation of the LICO framework, including the embedding and prediction layers, and the semi-synthetic training process.

4. The empirical evaluation is thorough and convincing. The authors compare LICO against several state-of-the-art methods on the PMO benchmark, demonstrating its superior performance in terms of sample efficiency and accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of LICO on the PMO benchmark, it is unclear how well the method generalizes to other molecular optimization tasks or datasets. Further experiments on diverse molecular optimization tasks would strengthen the claims of generalizability.

2. The reliance on LLMs for molecular optimization introduces potential limitations, such as the computational cost of inference and the need for large amounts of training data. The authors could discuss these limitations in more detail and explore potential solutions to mitigate them.

3. The paper could benefit from a more detailed comparison with other LLM-based methods for molecular optimization, highlighting the specific advantages and disadvantages of LICO compared to these approaches.

### Suggestions

The authors should consider expanding their evaluation to include a wider range of molecular optimization tasks, such as those involving different types of molecules or optimization objectives. For example, testing on tasks that involve optimizing properties related to drug-like molecules or materials with specific structural properties would provide a more comprehensive assessment of the method's generalizability. Furthermore, it would be beneficial to explore the performance of LICO on datasets with varying sizes and complexities, to understand its scalability and robustness. This would help to identify potential limitations of the approach and guide future research directions. The current evaluation, while thorough on the PMO benchmark, could be strengthened by demonstrating its effectiveness on a broader set of problems.

To address the computational cost concerns, the authors should investigate techniques to reduce the inference time of LICO. This could involve exploring model compression techniques, such as pruning or quantization, or using more efficient LLM architectures. Additionally, the authors should discuss the memory requirements of the method, especially when dealing with large molecules or datasets. A detailed analysis of the computational resources needed for training and inference would provide a more complete picture of the practical applicability of LICO. Furthermore, the authors should explore the trade-offs between model size, performance, and computational cost, to provide guidance on how to choose the appropriate model for different applications.

Finally, a more detailed comparison with other LLM-based methods for molecular optimization is needed. The authors should not only compare the performance of LICO with these methods but also discuss the specific advantages and disadvantages of each approach. For example, how does LICO compare to methods that use LLMs for property prediction in terms of optimization performance? What are the specific types of problems where LICO excels or struggles compared to other LLM-based optimization methods? A more in-depth analysis of these aspects would provide a more nuanced understanding of the contribution of LICO and its place in the field.

### Questions

1. How does LICO compare to other LLM-based methods for molecular optimization, such as those that use LLMs for property prediction?

2. What are the computational costs associated with training and inference using LICO, and how do they compare to other methods?

3. How does the performance of LICO vary with different sizes of training data, and what is the minimum amount of data required to achieve good performance?

### Rating

6

### Confidence

3

**********
