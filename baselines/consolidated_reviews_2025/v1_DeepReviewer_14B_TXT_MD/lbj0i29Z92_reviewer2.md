### Summary

The paper proposes a meta-rewarding step in the self-improving process of LLMs, where the model evaluates its own judgments to refine its judgment capabilities. This approach enhances both the model's judgment and instruction-following abilities, showing significant improvements on benchmarks like AlpacaEval 2 and Arena-Hard without human supervision.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel meta-rewarding mechanism that enhances the model's judgment capabilities, which is a significant advancement over existing self-rewarding methods.
2. The proposed method demonstrates substantial improvements on challenging benchmarks, indicating its effectiveness in real-world applications.
3. The approach is self-supervised, reducing the reliance on costly human-labeled data and making it more scalable.

### Weaknesses

#### Some Related Works


#### comment

1. The method's complexity, involving multiple roles (actor, judge, meta-judge), might make it challenging to implement and debug.
2. The paper does not extensively discuss the potential biases that might arise from the model evaluating its own judgments, which could lead to skewed or suboptimal learning outcomes.
3. The paper lacks a detailed analysis of the computational resources required for training, which is crucial for assessing the practicality of the approach.

### Suggestions

The paper introduces an interesting meta-rewarding mechanism, but several aspects require further clarification and analysis. First, the interaction between the actor, judge, and meta-judge roles needs to be more thoroughly explained. Specifically, how are the preferences generated for the judge and meta-judge training? Are these preferences based on simple win/loss outcomes, or are more nuanced scoring systems employed? The paper should detail the exact process of how the model's own judgments are used to create training data for the judge and meta-judge, including the specific loss functions and optimization techniques used. Furthermore, the paper should discuss the potential for instability or oscillations in the training process due to the interconnected nature of these roles. For example, if the meta-judge is not well-calibrated, it could lead to the judge being trained on noisy or biased data, which would then negatively impact the actor's performance. A more detailed analysis of the training dynamics and convergence properties is needed to ensure the robustness of the proposed method.

Second, the paper needs to address the potential biases that could arise from the model evaluating its own judgments. While the self-supervised nature of the approach is a strength, it also introduces the risk of the model reinforcing its own flawed reasoning patterns. The paper should explore the types of biases that might emerge, such as confirmation bias or overconfidence, and propose strategies to mitigate them. For instance, the paper could investigate the use of adversarial training techniques or the incorporation of external knowledge sources to provide a more objective evaluation of the model's judgments. Additionally, the paper should analyze the sensitivity of the method to the initial calibration of the judge and meta-judge. If the initial models are not well-calibrated, it could lead to a cascade of errors that are difficult to correct. A thorough analysis of the method's robustness to different initializations is crucial for its practical application.

Finally, the paper should provide a more detailed analysis of the computational resources required for training. This should include not only the total training time but also the memory requirements, the number of GPUs used, and the energy consumption. This information is essential for assessing the practicality of the approach and for comparing it to other methods. The paper should also discuss the scalability of the method to larger models and datasets. For example, how does the training time scale with the number of parameters in the model? Are there any bottlenecks in the training process that could limit the scalability of the method? A detailed analysis of the computational costs and scalability is crucial for the practical adoption of the proposed approach.

### Questions

1. How does the meta-rewarding step specifically address the issue of rapid saturation during iterative training?
2. Can the authors provide more details on the length-control mechanism and how it mitigates the issue of length explosion in model responses?
3. What are the potential biases that could arise from the model evaluating its own judgments, and how can they be mitigated?

### Rating

6

### Confidence

3

**********
