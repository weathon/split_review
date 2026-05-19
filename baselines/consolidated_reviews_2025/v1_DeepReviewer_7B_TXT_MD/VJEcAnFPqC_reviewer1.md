### Summary

This paper proposes a new task of graph navigation to study the stepwise inference in LLMs. The authors show that the stepwise inference is helpful in some cases, while it is not helpful in some other cases. The authors also show that the length of the solution path is important and the model is more likely to output a shorter solution path. The authors also show that the model is more likely to output the solution that is consistent with the first example.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed task is interesting and the experimental design is reasonable.
2. The authors show that the stepwise inference is helpful in some cases, while it is not helpful in some other cases. The authors also show that the length of the solution path is important and the model is more likely to output a shorter solution path. The authors also show that the model is more likely to output the solution that is consistent with the first example.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed task is interesting and the experimental design is reasonable.
2. The authors show that the stepwise inference is helpful in some cases, while it is not helpful in some other cases. The authors also show that the length of the solution path is important and the model is more likely to output a shorter solution path. The authors also show that the model is more likely to output the solution that is consistent with the first example.

1. The authors only show the results of 2-layer transformers. It is not clear if the results are generalizable to other architectures. Specifically, the behavior of multi-layer transformers with varying hidden dimensions and attention mechanisms could significantly differ from a 2-layer model, potentially invalidating the observed trends. The lack of exploration into different architectural choices limits the scope of the conclusions.
2. The authors only show the results of one specific dataset. It is not clear if the results are generalizable to other datasets. The dataset used might have specific properties that are not representative of other graph structures or navigation tasks. For example, the density or connectivity of the graph could influence the model's performance and the observed phenomena might not hold for sparser or denser graphs. The limited generalizability of the dataset raises concerns about the robustness of the findings.
3. The authors only show the results of one specific LLM. It is not clear if the results are generalizable to other LLMs. The findings might be specific to the architecture or training data of the chosen LLM, and may not apply to other transformer-based models with different parameter sizes or pre-training objectives. This limits the broader applicability of the conclusions.
4. The authors do not show the results of other LLMs. It is not clear if the results are generalizable to other LLMs. The lack of comparison with other LLMs makes it difficult to assess the universality of the observed phenomena. Different LLMs might exhibit different behaviors and sensitivities to the proposed task, which could challenge the generalizability of the conclusions.
5. The authors do not show the results of other model sizes. It is not clear if the results are generalizable to other model sizes. The findings might be specific to the chosen model size, and may not apply to larger or smaller models. The lack of exploration into different model sizes limits the scope of the conclusions.
6. The authors do not show the results of other sampling temperatures. It is not clear if the results are generalizable to other sampling temperatures. The optimal sampling temperature can vary depending on the task and model, and the authors should explore a wider range of temperatures to ensure the robustness of their findings.

### Suggestions

The authors should conduct a more thorough investigation into the impact of different model architectures. Specifically, they should explore multi-layer transformers with varying hidden dimensions and attention mechanisms to determine if the observed trends are consistent across different architectures. This would involve systematically varying the number of layers, the size of the hidden layers, and the type of attention mechanism used. Furthermore, the authors should analyze the internal representations of these different models to understand how the architecture affects the model's ability to perform stepwise inference. This could involve techniques such as probing or representational similarity analysis to gain insights into the model's internal workings. Such an analysis would significantly strengthen the generalizability of the findings.

To address the concerns about dataset and LLM generalizability, the authors should evaluate their approach on a wider range of datasets with varying graph properties, such as density, connectivity, and size. This would involve generating synthetic datasets with different structural characteristics and analyzing how the model's performance varies across these datasets. Additionally, the authors should test their approach on multiple LLMs with different architectures, sizes, and pre-training objectives. This would involve using models with different numbers of parameters, different attention mechanisms, and different pre-training datasets. By comparing the results across these different models, the authors can gain a better understanding of the universality of their findings and identify any model-specific biases or limitations. This would also help to determine if the observed phenomena are specific to the chosen model or are more generalizable across different LLMs.

Finally, the authors should explore a wider range of sampling temperatures to determine the robustness of their findings. This would involve systematically varying the sampling temperature and analyzing how the model's performance changes. The authors should also investigate the relationship between the sampling temperature and the model's exploration-exploitation trade-off. This could involve techniques such as temperature scaling or adaptive sampling to optimize the model's performance. By exploring a wider range of sampling temperatures, the authors can gain a better understanding of the model's behavior and identify any limitations or biases that might be specific to certain temperature settings. This would also help to ensure that the conclusions are robust and not overly sensitive to the specific sampling temperature used.

### Questions

1. Why do you only consider 2-layer transformers?
2. Why do you only consider one dataset?
3. Why do you only consider one LLM?
4. Why do you only consider one sampling temperature?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
