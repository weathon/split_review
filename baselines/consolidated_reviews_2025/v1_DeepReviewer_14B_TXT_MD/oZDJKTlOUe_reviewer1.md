### Summary

This paper proposes a simple yet powerful algorithm, LVLM Hallucination Revisor (LURE), to post-hoc rectify object hallucination in LVLMs by reconstructing less hallucinatory descriptions. LURE is grounded in a rigorous statistical analysis of the key factors underlying object hallucination, including co-occurrence, uncertainty, and object position. The authors find that LURE can also be seamlessly integrated with any LVLMs. They evaluate LURE on six open-source LVLMs and found it outperforms the previous best approach in both general object hallucination evaluation metrics, GPT, and human evaluations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors propose a simple yet effective method to mitigate the hallucination of LVLM.
3. The authors conduct a comprehensive experimental analysis to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. In the theoretical explanation, the authors analyze the reasons for hallucination generation from the information theory perspective. However, the solutions proposed in the method are not closely related to the analysis, such as co-occurrence and uncertainty.
2. The authors should include more implementation details of the proposed method, such as the structure and hyperparameters of the hallucination revisor.
3. The authors should include more ablation studies to validate the effectiveness of the components, such as the [IDK] and the three key factors.
4. The authors should include more experiments to demonstrate the generalization of the proposed method, such as different training and inference LVLMs.

### Suggestions

The paper's theoretical analysis, while interesting, lacks a clear connection to the proposed method. The authors should elaborate on how the information theory perspective directly informs the design choices of LURE. For instance, if the analysis suggests that hallucinations arise from specific information bottlenecks, the method should explicitly address these bottlenecks. The current approach of using co-occurrence and uncertainty as heuristics feels somewhat disconnected from the theoretical framework. A more rigorous justification is needed to bridge this gap, perhaps by demonstrating how these heuristics are derived from or aligned with the information-theoretic analysis. Furthermore, the authors should explore alternative methods that are more directly rooted in information theory, such as those that explicitly minimize the mutual information between the input and the hallucinated output.

To improve the reproducibility and understanding of the method, the authors should provide a detailed description of the hallucination revisor's architecture. This includes specifying the type of neural network used (e.g., Transformer, LSTM), the number of layers, the hidden dimension, and the activation functions. Furthermore, the authors should provide details on the training hyperparameters, such as the learning rate, batch size, optimizer, and the number of training epochs. The loss function used for training the revisor should also be clearly stated. Without these details, it is difficult to assess the complexity and effectiveness of the revisor. The authors should also discuss the computational cost of training and inference with the revisor, which is important for practical applications. Including a sensitivity analysis of the hyperparameters would also be beneficial to understand the robustness of the method.

Finally, the ablation studies should be expanded to provide a more granular understanding of the method's components. For example, the authors should investigate the impact of different thresholds for co-occurrence, uncertainty, and object position. It would also be beneficial to analyze the effect of each factor individually and in combination to determine their relative importance. The role of the [IDK] token should be further explored, including how its placement affects the revisor's performance. The authors should also consider the impact of different strategies for selecting which objects to mask. Furthermore, the generalization of the method should be tested on a wider range of LVLMs, including those with different architectures and training datasets. This would provide a more comprehensive evaluation of the method's robustness and applicability.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
