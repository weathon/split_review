### Summary

This paper proposes a new approach to layout generation by framing it as a code generation task, leveraging the semantic understanding of large language models (LLMs). The authors introduce Code Instruct Tuning (CIT), a three-module process: Code Initialization (CI) for generating HTML code with masks, Code Completion (CC) for filling these masks using LLMs, and Code Rendering (CR) for converting the final HTML output into a visual layout. Experiments show that LayoutNUWA outperforms existing methods on multiple datasets, demonstrating its effectiveness in generating semantically rich layouts.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper introduces a novel approach to layout generation by framing it as a code generation task, which allows for better semantic understanding and generation of layouts.
- The proposed method, LayoutNUWA, achieves state-of-the-art performance on multiple datasets, demonstrating its effectiveness and potential impact in the field.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost associated with the proposed method, which is important for practical applications.
- The paper does not discuss the limitations of the proposed approach, such as potential biases in the training data or the generalizability of the model to unseen layouts.
- The paper does not explore the potential for error propagation in the Code Completion module, which could lead to inconsistencies in the generated layouts.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed method. Specifically, the authors should provide details on the training time, inference time, and memory usage for different dataset sizes and model configurations. This analysis should also compare the computational cost of LayoutNUWA with existing layout generation methods. Furthermore, the authors should investigate the scalability of the method by evaluating its performance on larger and more complex layout datasets. This would provide a more comprehensive understanding of the practical applicability of the proposed approach. It would also be beneficial to explore techniques for optimizing the computational efficiency of the method, such as model pruning or quantization, to make it more suitable for real-world applications.

The paper should also address the limitations of the proposed approach, particularly regarding potential biases in the training data and the generalizability of the model to unseen layouts. The authors should analyze the types of layouts that the model struggles with and discuss the potential reasons for these limitations. For example, the paper could investigate whether the model performs better on layouts with a specific structure or style. Additionally, the authors should explore techniques for improving the generalizability of the model, such as data augmentation or domain adaptation. It would also be beneficial to evaluate the model on a wider range of layout datasets, including those that are significantly different from the training data, to assess its robustness and adaptability. A more detailed discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

Finally, the paper should investigate the potential for error propagation in the Code Completion module. Since the generated HTML code is directly converted into a visual layout, any errors in the code could lead to inconsistencies or artifacts in the final layout. The authors should analyze the types of errors that are most likely to occur in the Code Completion module and their impact on the generated layouts. For example, they could investigate whether errors in the HTML structure or the attribute values propagate to the final layout. Furthermore, the authors should explore techniques for mitigating these errors, such as using a more robust code completion model or incorporating error checking mechanisms into the layout generation process. A thorough analysis of error propagation would provide valuable insights into the reliability and robustness of the proposed method.

### Questions

- How does the proposed method handle layouts with complex or unusual structures that are not well represented in the training data?
- What are the potential biases in the training data, and how might they affect the generated layouts?
- How does the model perform on different types of layouts, such as those with varying levels of complexity or different visual styles?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
