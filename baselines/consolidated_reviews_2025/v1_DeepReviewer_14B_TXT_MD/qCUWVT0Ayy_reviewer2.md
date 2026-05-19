### Summary

This paper proposes LayoutNUWA, the first model that treats layout generation as a code generation task to enhance semantic information and harnesses the hidden layout expertise of large language models (LLMs). It comprises three interconnected modules: 1) the Code Initialization (CI) module quantifies the numerical conditions and initializes them as HTML code with strategically placed masks; 2) the Code Completion (CC) module employs the formatting knowledge of LLMs to fill in the masked portions within the HTML code; 3) the Code Rendering (CR) module transforms the completed code into the final layout output, ensuring a highly interpretable and transparent layout generation procedure that directly maps code to a visualized layout. Experiments across a variety of conditional layout generation tasks on three datasets highlight the superiority of our method, in which LayoutNUWA can significantly outperform all the baselines and shows comparable results with the task-specific models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is interesting and novel. It is interesting to treat the layout generation as a code generation task. 
- The paper is well-written and easy to understand.
- The experimental results demonstrate the effectiveness of the proposed method. 
- The visualization results are interesting and further improve the human interpretability of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method seems to be only suitable for generating graphic layouts but not for indoor scene layouts. It is because the former can be easily represented by codes like HTML but the latter cannot. 
- The proposed method seems to be computationally expensive. It is because it needs to call LLMs to generate the layout.

### Suggestions

The paper's core idea of framing layout generation as a code generation task is novel and promising, but the current implementation appears to be limited in scope. The reliance on HTML-like code for representing layouts, while effective for graphic designs, raises concerns about its generalizability to more complex scenarios such as indoor scene layouts. The authors should explore alternative code representations that can capture the spatial relationships and object interactions inherent in indoor environments. For instance, a hierarchical code structure or a scene graph representation could be considered to encode the layout of a room with furniture and other objects. This would require a more sophisticated code generation process, potentially involving multiple LLMs or a single LLM with a more complex prompting strategy. Furthermore, the paper should discuss the limitations of the current approach in terms of the types of layouts it can handle and provide a clear roadmap for future research to address these limitations.

While the use of LLMs for code completion is a clever approach, the computational cost of this method needs to be addressed more thoroughly. The paper should provide a detailed analysis of the computational resources required for training and inference, including the number of GPUs, memory usage, and training time. A comparison with existing methods in terms of computational efficiency would be beneficial to understand the trade-offs between performance and resource consumption. Furthermore, the authors should investigate techniques to reduce the computational burden of using LLMs, such as model compression, knowledge distillation, or caching of intermediate results. The paper should also explore the possibility of using smaller, more efficient models for code completion, which could be fine-tuned for the specific task of layout generation. This would make the proposed method more practical and accessible for researchers and practitioners with limited computational resources.

Finally, the paper should include a more detailed discussion of the failure cases of the proposed method. While the visualization results are promising, it is important to understand the limitations of the approach and the types of layouts it struggles to generate. For example, the paper should analyze the cases where the generated layouts are not realistic or do not match the input conditions. This analysis should include a discussion of the potential causes of these failures, such as limitations of the LLM, errors in the code generation process, or ambiguities in the input conditions. The authors should also explore techniques to mitigate these failures, such as incorporating error detection and correction mechanisms into the code generation process or using a more robust LLM for code completion. A thorough analysis of the failure cases would provide valuable insights into the strengths and weaknesses of the proposed method and guide future research in this area.

### Questions

- What is the computational cost of the proposed method? 
- Does the proposed method have any failure cases? If yes, please show some failure cases and analyze the reasons.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
