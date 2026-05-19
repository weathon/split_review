### Summary

This paper proposes a data selection method for pre-fine-tuning LLMs. The method is based on optimal transport theory and aims to select data that is most similar to the target data. The authors provide theoretical justification for the proposed method and conduct experiments to show that it outperforms existing data selection methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and the experimental setup.
2. The proposed method is theoretically sound and well-motivated. The authors provide a clear explanation of the optimal transport theory and how it can be applied to data selection.
3. The proposed method is computationally efficient and can be applied to large-scale datasets. The authors provide empirical results to show that the method is efficient and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only applicable to the case where the target data is available during the pre-fine-tuning stage. However, in practice, the target data is often not available and the pre-fine-tuning data is also used for evaluation. In this case, the proposed method cannot be applied.
2. The proposed method requires the computation of the gradient of the optimal transport plan, which can be computationally expensive for large-scale datasets. Although the authors claim that their method is efficient, they do not provide any empirical results to support this claim. It would be better to provide the running time of the proposed method and compare it with other methods.
3. The authors only evaluate their method on BERT-base. It would be better to evaluate their method on larger LLMs, such as LLaMA-2, to demonstrate its scalability.

### Suggestions

The paper's reliance on target data availability during pre-fine-tuning is a significant limitation. While the authors frame this as a pre-training scenario, the practical utility is questionable when the target data is also used for evaluation. The method's applicability is restricted to scenarios where the pre-fine-tuning data is representative of the evaluation data, which is not always the case in real-world applications. A more robust approach would be to explore methods that can operate without explicit target data, perhaps by leveraging techniques like unsupervised domain adaptation or by incorporating a proxy for the target distribution. Furthermore, the paper should clearly define the scope of its applicability and acknowledge the limitations when target data is not available. The authors should also consider the implications of their method in scenarios where the pre-fine-tuning data is not representative of the target data, and how this might affect the performance of the proposed method.

The computational cost of calculating the gradient of the optimal transport plan is a major concern. While the authors claim efficiency, the lack of empirical evidence makes it difficult to assess the practical implications. The paper should provide a detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for different dataset sizes. It would be beneficial to compare the running time of the proposed method with other data selection methods, such as random selection or simple heuristics, to demonstrate its efficiency. Furthermore, the authors should discuss the scalability of their method to larger datasets and models, and provide insights into how the computational cost scales with the size of the data and model. The authors should also consider the practical implications of the computational cost for real-world applications, and provide guidance on how to optimize the method for different scenarios.

Finally, the evaluation of the proposed method is limited to BERT-base. While BERT-base is a widely used model, it is not representative of the current state-of-the-art in large language models. The authors should evaluate their method on larger models, such as LLaMA-2, to demonstrate its scalability and effectiveness. The evaluation should also include a comparison with other data selection methods on these larger models. Furthermore, the authors should analyze the performance of their method on different types of tasks and datasets, to assess its generalizability. The evaluation should also consider the impact of different hyperparameters on the performance of the proposed method, and provide guidelines for selecting the optimal hyperparameters for different tasks and datasets.

### Questions

Please see the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
