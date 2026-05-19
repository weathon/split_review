### Summary

This paper introduces a novel meta-rewarding mechanism for improving the judgment capabilities of large language models (LLMs) without human supervision. The approach involves a three-role iterative training scheme where the model acts as an actor to generate responses, a judge to evaluate those responses, and a meta-judge to assess the quality of its own judgments. The meta-judge generates preference pairs for training the judge, which in turn provides higher-quality feedback for training the actor. The method also incorporates a length-control mechanism to prevent response length explosion. Experiments on benchmarks like AlpacaEval 2 and Arena-Hard demonstrate significant improvements in both instruction following and judging accuracy.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a novel meta-rewarding mechanism that improves the model's judgment capabilities without human supervision.
2. The method demonstrates significant improvements on multiple benchmarks, outperforming baselines like Self-Rewarding and SPPO.
3. The paper provides a detailed description of the iterative training process and the roles of the actor, judge, and meta-judge.
4. The length-control mechanism effectively mitigates the issue of response length explosion.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough analysis of the computational resources required for training. This makes it difficult to assess the practical feasibility of the method, especially for researchers with limited access to computational resources. The paper should include details on the number of GPUs used, the training time per iteration, and the overall training cost in terms of GPU hours.
2. The evaluation is limited to a single model, Llama-3-8B-Instruct. While the results are promising, it is unclear how well the method would generalize to other models with different architectures or sizes. The paper should include experiments on a range of models, including smaller models and models with different architectural designs, to demonstrate the robustness of the proposed method.
3. The paper does not provide a detailed analysis of the potential biases that might be introduced by the meta-judge. Since the meta-judge is also an LLM, it may have its own biases that could affect the training process. The paper should investigate the types of biases that the meta-judge might exhibit and how these biases could impact the performance of the actor and judge.

### Suggestions

To address the lack of computational resource analysis, the authors should include a detailed breakdown of the resources required for each stage of the training process. This should include the number of GPUs used, the training time per iteration, the total training time, and the overall cost in terms of GPU hours. Furthermore, the authors should provide an analysis of the memory requirements and the energy consumption of the method. This information is crucial for researchers who want to reproduce the results or apply the method in resource-constrained environments. It would also be beneficial to compare the computational cost of the proposed method with other existing methods, such as Self-Rewarding and SPPO, to provide a clear understanding of the trade-offs involved.

To improve the generalizability of the method, the authors should conduct experiments on a wider range of models, including smaller models and models with different architectures. This would help to demonstrate the robustness of the proposed method and its applicability to different scenarios. The authors should also analyze the performance of the method on different types of tasks and datasets to assess its versatility. It would be beneficial to include a discussion of the limitations of the method and the types of models or tasks where it may not be effective. This would provide a more complete understanding of the strengths and weaknesses of the proposed approach.

To address the potential biases introduced by the meta-judge, the authors should conduct a thorough analysis of the meta-judge's behavior. This should include an investigation of the types of biases that the meta-judge might exhibit and how these biases could impact the performance of the actor and judge. The authors should also explore methods for mitigating these biases, such as using a more diverse set of training data or incorporating techniques for bias detection and correction. Furthermore, the authors should provide a discussion of the ethical implications of using a meta-judge and the potential risks associated with biased judgments. This would help to ensure that the method is used responsibly and ethically.

### Questions

1. Can the authors provide more details on the computational resources required for training, such as the number of GPUs used and the training time per iteration?
2. Have the authors considered applying the method to other models besides Llama-3-8B-Instruct? If so, what were the results?
3. What are the potential biases that could arise from the meta-judge, and how can they be mitigated?

### Rating

6

### Confidence

4

**********
