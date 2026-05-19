### Summary

The paper introduces a novel approach called Meta-Rewarding for improving the alignment and instruction-following capabilities of large language models (LLMs) without relying on human-labeled data. The core idea is to enhance the model's ability to judge its own responses by introducing a meta-judge role, which evaluates the quality of the model's judgments. This approach aims to address the limitation of previous self-rewarding methods that primarily focus on improving response generation while neglecting the development of judgment skills. The Meta-Rewarding method involves three roles: an actor that generates responses, a judge that evaluates these responses, and a meta-judge that assesses the quality of the judgments made by the judge. The paper demonstrates that this unsupervised approach significantly improves the model's ability to judge and follow instructions, as evidenced by substantial win rate improvements on benchmarks like AlpacaEval 2 and Arena-Hard. The method also incorporates a length-control mechanism to mitigate the issue of response length explosion, ensuring that the model's outputs remain concise and relevant.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel and unsupervised approach to improve the alignment and instruction-following capabilities of LLMs, which is a significant advancement in the field. The idea of using a meta-judge to evaluate the quality of the model's own judgments is innovative and addresses a key limitation of previous self-rewarding methods.
2. The paper provides a clear and detailed explanation of the Meta-Rewarding method, including the roles of the actor, judge, and meta-judge, and the iterative training process. The figures and examples help to illustrate the concepts and make the paper easy to follow.
3. The paper demonstrates the effectiveness of the Meta-Rewarding method through extensive experiments on multiple benchmarks, including AlpacaEval 2 and Arena-Hard. The results show significant improvements in win rates and instruction-following capabilities, which are compelling evidence of the method's efficacy.
4. The paper also addresses the practical issue of response length explosion by introducing a length-control mechanism, which is an important consideration for real-world applications of LLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the Llama-3-8B-Instruct model, and it is unclear how well the Meta-Rewarding method generalizes to other models with different architectures or sizes. Further experiments on a wider range of models would strengthen the paper's claims.
2. The paper does not provide a detailed analysis of the computational resources required for training the Meta-Rewarding model, which is an important consideration for practical applications. Information on training time, hardware requirements, and energy consumption would be valuable for readers.
3. The paper could benefit from a more thorough discussion of the limitations of the Meta-Rewarding method. For example, how does the method perform on tasks that require complex reasoning or common sense? Are there any specific types of instructions or prompts that the method struggles with?

### Suggestions

The paper would be significantly strengthened by a more thorough investigation into the generalizability of the Meta-Rewarding method across different model architectures and sizes. While the results on Llama-3-8B-Instruct are promising, it is crucial to demonstrate that the approach is not overly tailored to this specific model. Experiments should include models with varying parameter counts, different pre-training objectives, and distinct architectural designs. For example, testing on models like the smaller Llama-2 variants, or larger models such as those in the GPT family, would provide a more comprehensive understanding of the method's robustness. Furthermore, the analysis should not only focus on overall performance metrics but also delve into the qualitative differences in how different models respond to the meta-rewarding process. This would help identify potential limitations and areas for improvement in the method's design. It would also be beneficial to explore how the meta-judge's performance scales with model size, and whether larger models consistently lead to better judgment capabilities.

In addition to model generalizability, the paper needs to provide a more detailed analysis of the computational resources required for training the Meta-Rewarding model. This should include not only the total training time but also the specific hardware requirements, such as the number and type of GPUs used, as well as the memory footprint of the training process. Information on the energy consumption of the training process would also be valuable for assessing the practical feasibility of the method. Furthermore, the paper should discuss the scalability of the method, including how the training time and resource requirements change as the model size and dataset size increase. This information is crucial for researchers and practitioners who want to apply the method in real-world scenarios. A comparison with the computational costs of other self-improvement methods would also be beneficial to contextualize the efficiency of the proposed approach.

Finally, the paper should include a more in-depth discussion of the limitations of the Meta-Rewarding method. This should go beyond the general limitations of LLMs and focus on the specific challenges and shortcomings of the proposed approach. For example, the paper should investigate how the method performs on tasks that require complex reasoning, common sense, or multi-step inference. Are there specific types of instructions or prompts that the method struggles with? The paper should also explore the potential for the meta-judge to develop biases or to overfit to the training data. A thorough analysis of these limitations would provide a more balanced and realistic assessment of the method's capabilities and would help guide future research in this area. This could include an analysis of failure cases and a discussion of potential mitigation strategies.

### Questions

1. How does the Meta-Rewarding method perform on tasks that require complex reasoning or common sense? Are there any specific types of instructions or prompts that the method struggles with?
2. What are the computational resources required for training the Meta-Rewarding model? How does the training time and resource usage scale with the size of the model and the dataset?
3. How does the Meta-Rewarding method compare to other self-improvement methods in terms of computational efficiency and effectiveness? Are there any trade-offs between the two?

### Rating

8

### Confidence

3

**********
