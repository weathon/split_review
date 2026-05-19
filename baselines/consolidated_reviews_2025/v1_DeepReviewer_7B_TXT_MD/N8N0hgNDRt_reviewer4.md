### Summary

This paper proposes a method to improve the mathematical reasoning ability of LLMs. The method is based on the idea that a mathematical question can be solved by a forward reasoning process or a backward reasoning process. The authors propose to augment the training dataset with the generated questions and reasoning paths by the forward and backward reasoning process. The experiments show that the proposed method can improve the mathematical reasoning ability of LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of using forward and backward reasoning to improve the mathematical reasoning ability of LLMs is interesting and novel.
- The experiments show that the proposed method can improve the mathematical reasoning ability of LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is quite similar to the work of Wu et al. (2022). The authors should discuss the differences between the two works in the paper.
- The experiments are not sufficient to fully evaluate the effectiveness of the proposed method. The authors should conduct more experiments to evaluate the effectiveness of the proposed method.

### Suggestions

The paper introduces an interesting approach to improve mathematical reasoning in LLMs by leveraging both forward and backward reasoning. However, the current evaluation lacks the depth needed to fully assess the method's capabilities. Specifically, the paper should include a more comprehensive analysis of the model's performance across different types of mathematical problems. For instance, it would be beneficial to see results on problems that require multi-step reasoning, problems with multiple possible solution paths, and problems that involve more complex mathematical concepts. Furthermore, the evaluation should not only focus on accuracy but also consider the model's ability to generate correct reasoning steps and explanations. This could be achieved by using metrics that evaluate the quality of the generated reasoning paths, such as the length of the path, the correctness of each step, and the overall coherence of the reasoning process. The current evaluation is limited to a few datasets, and expanding the evaluation to include more diverse and challenging datasets would provide a more robust assessment of the proposed method.

To strengthen the paper, the authors should also explore the impact of different parameters and hyperparameters on the performance of the proposed method. For example, the number of forward and backward reasoning steps, the size of the generated dataset, and the choice of the base LLM should be investigated. A sensitivity analysis of these parameters would provide valuable insights into the robustness and generalizability of the method. Additionally, the authors should consider comparing their method with other state-of-the-art approaches for improving mathematical reasoning in LLMs. This would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages compared to existing techniques. The comparison should not only focus on overall accuracy but also consider other aspects such as the computational cost and the interpretability of the results. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors could discuss the challenges of applying the method to more complex mathematical problems, the limitations of the current evaluation metrics, and the potential for improving the method's efficiency and effectiveness. This would help to guide future research in this area and provide a more complete picture of the proposed method's capabilities and limitations. The discussion should also address the potential for bias in the generated dataset and how this bias might affect the model's performance. Addressing these limitations would significantly enhance the paper's contribution and impact.

### Questions

Please see the weaknesses section.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
