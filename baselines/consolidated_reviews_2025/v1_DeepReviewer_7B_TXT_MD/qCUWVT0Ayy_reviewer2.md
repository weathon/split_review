### Summary

This paper proposes a code-based approach to layout generation. The proposed method, LayoutNUWA, consists of three stages: (1) code initialization, which converts the input into masked HTML code; (2) code completion, which uses LLMs to complete the masked HTML code; (3) code rendering, which renders the completed HTML code into the final layout. The authors evaluate LayoutNUWA on three datasets and show that it outperforms existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors conduct extensive experiments to evaluate the proposed method and show that it outperforms existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is relatively simple and may not be novel enough.
- The authors only evaluate the proposed method on three datasets. It would be better to evaluate it on more datasets.
- The authors only compare the proposed method with some baseline methods. It would be better to compare it with more recent and advanced methods.

### Suggestions

The paper's core idea of using a code-based approach for layout generation is interesting, but the novelty is somewhat limited given the existing body of work in this area. While the authors frame their approach as a code generation task, the underlying mechanisms appear to be largely incremental. Specifically, the code initialization stage, which converts input into masked HTML, and the code completion stage, which uses LLMs, are not fundamentally different from existing methods that use similar techniques for layout generation. The code rendering stage, while necessary, is also a standard process. To strengthen the contribution, the authors could explore more sophisticated code manipulation techniques or introduce a novel loss function that is specifically tailored to the code-based layout generation task. Furthermore, a more detailed analysis of the limitations of existing methods and how the proposed approach addresses these limitations would be beneficial.

Expanding the evaluation to a wider range of datasets is crucial for demonstrating the robustness and generalizability of the proposed method. The current evaluation on only three datasets raises concerns about potential overfitting to the specific characteristics of these datasets. The authors should consider including datasets with varying complexities, styles, and domain-specific layouts. For example, evaluating on datasets with more intricate layouts, such as those found in complex UI designs or architectural floor plans, would provide a more comprehensive assessment of the method's capabilities. Additionally, it would be beneficial to evaluate the method on datasets with different types of input, such as natural language descriptions or image-based inputs, to assess its versatility. This would provide a more thorough understanding of the method's strengths and weaknesses.

Finally, the comparison with baseline methods needs to be more comprehensive. While the authors compare their method with some existing approaches, it is important to include more recent and state-of-the-art methods in the comparison. This would provide a more accurate assessment of the proposed method's performance relative to the current state of the art. The authors should also consider including a more detailed analysis of the performance differences between the proposed method and the baseline methods, including a discussion of the strengths and weaknesses of each method. This would provide a more nuanced understanding of the proposed method's contributions and limitations. Furthermore, it would be beneficial to include ablation studies to analyze the impact of different components of the proposed method on its overall performance.

### Questions

- Could the authors provide more details about the datasets used in the experiments? Specifically, what are the characteristics of the datasets, and how do they differ from each other?
- Could the authors provide more details about the baseline methods used in the experiments? Specifically, what are the differences between the baseline methods and the proposed method?
- Could the authors provide more details about the evaluation metrics used in the experiments? Specifically, what do the metrics measure, and how do they relate to the task of layout generation?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
