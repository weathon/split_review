### Summary

This paper presents a novel approach to generating Scalable Vector Graphics (SVG) with a focus on improving the readability of the underlying code. The authors propose a set of metrics to evaluate SVG readability, including structural proximity, element simplicity, and redundancy quotient. They also introduce differentiable loss functions that guide the SVG generation model to produce more readable code without compromising visual accuracy. The paper demonstrates the effectiveness of their approach through experiments on synthetic datasets and font reconstruction tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a novel and important problem in the field of SVG generation, focusing on the readability of the generated code, which is often overlooked in favor of visual accuracy.
2. The authors propose a comprehensive set of metrics to evaluate SVG readability, providing a clear and quantifiable way to assess the quality of the generated code.
3. The introduction of differentiable loss functions that directly target code readability is a significant technical innovation, allowing for the optimization of readability within the SVG generation process.
4. The experimental results show that the proposed method can generate SVG code that is more readable without sacrificing visual accuracy, demonstrating the practical effectiveness of the approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the proposed method. It would be beneficial to understand how the additional readability-focused loss functions impact the training time and resource requirements, especially when scaling to more complex images or larger datasets. Specifically, the paper does not provide a breakdown of the time spent on calculating each loss component, making it difficult to assess the practical overhead of the proposed approach. Furthermore, the paper does not discuss the memory footprint of the additional loss functions, which could be a limiting factor for resource-constrained environments.
2. The evaluation is primarily conducted on synthetic datasets and font reconstruction tasks. It would be valuable to see how the method performs on more diverse and real-world datasets, such as complex natural images or icons with intricate details. The current evaluation does not adequately demonstrate the method's robustness to variations in image complexity and style. The paper should include a more thorough analysis of the method's performance on datasets with varying levels of detail and complexity.
3. The paper does not provide a detailed comparison with existing methods that also aim to improve the quality of generated SVGs, particularly in terms of code readability. A more comprehensive comparison would help to better understand the advantages and limitations of the proposed approach. The paper should include a quantitative comparison with state-of-the-art methods, using the proposed readability metrics, to demonstrate the superiority of the proposed approach. A qualitative comparison, showing examples of generated SVG code, would also be beneficial.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed readability-focused loss functions. This analysis should include a breakdown of the time spent on calculating each loss component, as well as the memory footprint of the additional loss functions. The authors should also investigate the scalability of the method by evaluating its performance on larger and more complex datasets. This would provide a more comprehensive understanding of the practical limitations of the proposed approach. Furthermore, the paper should explore the impact of different weighting schemes for the readability losses, providing a more detailed analysis of the trade-offs between visual accuracy and code readability. This would help to identify the optimal configuration for different applications.

To address the limitations of the current evaluation, the authors should include experiments on more diverse and real-world datasets. This should include datasets with complex natural images, icons with intricate details, and other types of vector graphics. The evaluation should also include a more thorough analysis of the method's performance on datasets with varying levels of detail and complexity. This would provide a more comprehensive understanding of the method's robustness and generalizability. The authors should also consider using a wider range of evaluation metrics, including metrics that capture the semantic meaning of the generated SVG code, to provide a more complete assessment of the method's performance.

The paper should include a more detailed comparison with existing methods that also aim to improve the quality of generated SVGs, particularly in terms of code readability. This comparison should include both quantitative and qualitative analyses. The authors should use the proposed readability metrics to quantitatively compare the performance of their method with state-of-the-art approaches. They should also provide qualitative comparisons, showing examples of generated SVG code, to highlight the advantages of their method. This would help to better understand the advantages and limitations of the proposed approach and to demonstrate its superiority over existing methods.

### Questions

1. How does the proposed method handle complex images with multiple overlapping objects or intricate details? Are there any limitations in terms of the types of images that can be effectively vectorized while maintaining code readability?
2. The paper mentions using GPT-3.5 to evaluate the readability of the generated SVG code. Can you provide more details on how this evaluation was conducted? What specific prompts were used, and how were the responses analyzed to determine the readability score?
3. How does the proposed method compare to existing approaches in terms of the trade-off between visual accuracy and code readability? Are there any scenarios where the proposed method might prioritize readability at the expense of visual fidelity, or vice versa?
4. Can the proposed readability metrics be applied to other types of vector graphics or programming languages? How generalizable is the concept of code readability as defined in this paper?

### Rating

6

### Confidence

3

**********
