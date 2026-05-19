### Summary

This paper proposes a novel method for graphic layout generation, called LayoutNUWA, by converting layout generation task into the code generation task. LayoutNUWA consists of three interconnected modules: 1) the Code Initialization (CI) module, 2) the Code Completion (CC) module, and 3) the Code Rendering (CR) module. By leveraging the formatting knowledge of LLMs, LayoutNUWA enhances semantic information within layouts and achieves state-of-the-art performance on multiple datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The first model that treats the layout generation task as a code generation task.
- Treats layout generation as a code generation task to enhance semantic information and harnesses the hidden layout expertise of large language models.
- The proposed Code Instruct Tuning (CIT) approach, which consists of three interconnected modules.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method only generates the layout in code language, which seems not very practical in real world applications.
- The proposed method only generates the layout in code language, which seems not very practical in real world applications. The code generation approach may be not very suitable for layout generation task, as layout generation is more about visual perception and design, while code generation is more about logic and functionality.
- The proposed method seems not very novel, as it mainly applies the code generation approach to the layout generation task.
- The proposed method seems not very novel, as it mainly applies the code generation approach to the layout generation task. The code generation approach has been widely used in many fields, such as software engineering, web development, and data science.
- The proposed method seems to have limited scalability, as it requires large language models (LLMs) with strong formatting knowledge, which can be computationally expensive and difficult to train.

### Suggestions

The paper's core idea of framing layout generation as a code generation task is interesting, but the practical limitations need to be addressed more thoroughly. While the authors argue that code-based layouts are interpretable and customizable, the paper does not adequately explore the gap between generating code and actual user needs in real-world design scenarios. For example, most designers work with visual tools and expect to see immediate visual feedback, not raw code. The paper should include a discussion on how this code-generated layout can be integrated into existing design workflows, or how it can be made more accessible to non-technical users. Furthermore, the paper should explore alternative output formats, such as direct image generation or vector graphics, to enhance the practical applicability of the proposed method. The current approach seems to prioritize the use of LLMs over the practical needs of layout generation, which is a significant drawback.

To enhance the novelty of the proposed method, the authors should focus on the unique challenges of layout generation that are not typically encountered in other code generation tasks. For instance, layout generation requires a deep understanding of design principles, such as alignment, spacing, and visual hierarchy. The paper should demonstrate how the proposed method leverages these design principles to generate aesthetically pleasing and functional layouts. The current approach seems to treat layout generation as a generic code generation problem, without fully addressing the specific requirements of the layout domain. The paper should also explore how the proposed method can be extended to handle more complex layout scenarios, such as multi-page documents or responsive web designs. This would help to demonstrate the versatility and potential of the proposed method.

Finally, the paper needs to address the scalability concerns more directly. While the authors mention the use of DeepSpeed for training, they do not provide sufficient details on the computational resources required for training and inference. The paper should include a detailed analysis of the training time, memory usage, and inference speed of the proposed method. Furthermore, the paper should explore techniques for reducing the computational cost of the proposed method, such as model compression or knowledge distillation. The current approach relies heavily on large language models, which can be a barrier to adoption in resource-constrained environments. The paper should also discuss the limitations of the proposed method in terms of the size and complexity of the layouts that can be generated, and how these limitations can be addressed in future work.

### Questions

- How does the proposed method handle the scalability issue?
- How does the proposed method ensure the visual quality and aesthetic appeal of the generated layouts?
- How does the proposed method compare to other layout generation methods in terms of computational efficiency and resource requirements?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
