### Summary

This paper studies the problem of selecting data from large-scale open data to pre-fine-tune LLMs for specific downstream tasks. The authors propose a new method, Gradient of Optimal Transport for Data Selection (GOT-D), which is theoretically grounded and can be efficiently solved using existing OT solvers. The authors demonstrate the effectiveness of GOT-D through extensive experiments on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation and a comprehensive review of related work. The proposed method is well-explained and the experimental results are thoroughly discussed.

2. The authors provide a solid theoretical foundation for the proposed method, which is a significant strength. The authors also conduct extensive experiments to demonstrate the effectiveness of GOT-D.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their method is efficient, but they do not provide any empirical results to support this claim. It would be better to include the running time of GOT-D and compare it with other methods.

2. The authors only evaluate their method on BERT-base. It would be better to evaluate their method on larger LLMs, such as LLaMA-2, to demonstrate its scalability.

### Suggestions

The paper would benefit from a more thorough analysis of the computational efficiency of the proposed GOT-D method. While the authors claim efficiency, they do not provide any concrete evidence to support this claim. Specifically, it is crucial to report the actual running time of GOT-D and compare it with other data selection methods. This comparison should be done under similar experimental settings, including the same hardware and software configurations. Furthermore, the authors should provide a breakdown of the computational cost of each step in the GOT-D algorithm, such as the computation of the gradient of the optimal transport plan and the selection of the data points. This would help to identify the bottlenecks of the algorithm and provide insights into potential areas for optimization. Without such empirical evidence, the claim of efficiency remains unsubstantiated and weakens the overall impact of the paper.

To further strengthen the paper, the authors should evaluate their method on larger language models. While BERT-base is a widely used model, it is not representative of the current state-of-the-art in large language models. The authors should demonstrate the effectiveness of GOT-D on larger models, such as LLaMA-2, to show that their method is scalable and applicable to more complex models. This evaluation should include a comparison with other data selection methods on these larger models. It is important to show that the proposed method can handle the increased computational cost and data volume associated with larger models. Furthermore, the authors should analyze the performance of GOT-D on different layers of the larger models to understand how the method behaves with different model architectures. This analysis would provide a more comprehensive understanding of the method's applicability and limitations.

Finally, the authors should also consider evaluating their method on a wider range of tasks and datasets. While the current evaluation covers several tasks, it would be beneficial to include more diverse tasks, such as text summarization, machine translation, and question answering. This would demonstrate the generalizability of the proposed method and its applicability to different domains. Furthermore, the authors should consider evaluating their method on datasets with varying sizes and complexities. This would help to understand the performance of the method under different conditions and provide insights into its robustness. The authors should also analyze the sensitivity of the method to different hyperparameters and provide guidelines for selecting the optimal hyperparameters for different tasks and datasets.

### Questions

Please see the weaknesses above.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
