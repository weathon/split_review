### Summary

This paper proposes a new knowledge distillation (KD) approach for white-box LLMs. The authors replace the forward KL divergence objective with reverse KL, which is more suitable for generative language models, to prevent the student model from overestimating the low-probability regions of the teacher distribution. They also derive an effective optimization approach to learn this objective. The student models are named MINILLM. Extensive experiments in the instruction-following setting show that MINILLM generates more precise responses with higher overall quality, lower exposure bias, better calibration, and higher long-text generation performance than the baselines. The method is scalable for different model families with 120M to 13B parameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a novel KD approach that distills LLMs into smaller language models using reverse KL divergence, which is more suitable for generative language models.
2. The authors derive an effective optimization approach to learn the reverse KL objective, which is a significant contribution to the field of KD.
3. The authors conduct extensive experiments in the instruction-following setting and show that MINILLM generates more precise responses with higher overall quality, lower exposure bias, better calibration, and higher long-text generation performance than the baselines.
4. The method is scalable for different model families with 120M to 13B parameters, which is a significant advantage over existing KD methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate their method on instruction-following tasks. It is unclear how well the method would perform on other tasks such as summarization, translation, or question answering. The lack of evaluation on these diverse tasks limits the generalizability of the findings. For example, summarization often requires capturing the essence of long documents, which might expose weaknesses in the distilled model's ability to handle long-range dependencies. Similarly, translation tasks would test the model's ability to handle cross-lingual semantics, which is not directly assessed by instruction-following tasks.
2. The authors do not compare their method to other KD methods for LLMs, such as Mini-1.3B. It is unclear how their method compares to existing approaches. The absence of a direct comparison with other state-of-the-art KD techniques makes it difficult to assess the relative advantage of the proposed method. Specifically, it is not clear if the gains observed are due to the reverse KL divergence objective or other factors in the training procedure. A comparison with methods like Mini-1.3B, which also focus on distilling large language models, would provide a more comprehensive understanding of the method's performance.

### Suggestions

To strengthen the paper, the authors should evaluate their method on a broader range of tasks beyond instruction-following. Specifically, including summarization tasks, such as those found in the CNN/DailyMail dataset, would provide insights into the model's ability to handle long-form text and extract key information. Similarly, incorporating translation tasks, such as those in the WMT dataset, would assess the model's cross-lingual capabilities. Furthermore, question answering tasks, like SQuAD, would evaluate the model's ability to understand and reason about factual information. These additional evaluations would provide a more comprehensive understanding of the method's strengths and weaknesses across different task types and help to establish the generalizability of the proposed approach. The authors should also analyze the performance of the distilled model on these tasks in relation to the teacher model, providing a clear picture of the knowledge transfer process.

In addition to expanding the evaluation tasks, the authors should include a direct comparison with other state-of-the-art knowledge distillation methods for large language models. Specifically, a comparison with Mini-1.3B would be highly beneficial. This comparison should not only focus on overall performance metrics but also delve into the specific strengths and weaknesses of each method. For example, it would be useful to analyze the computational cost, the training time, and the memory requirements of each method. Furthermore, the authors should investigate the impact of different hyperparameters on the performance of both their method and the baseline methods. This would provide a more nuanced understanding of the trade-offs between different approaches and help to identify the most effective strategies for knowledge distillation of large language models. The authors should also consider ablating different components of their method to understand the contribution of each component to the overall performance.

Finally, the authors should provide a more detailed analysis of the training process, including the convergence behavior of the reverse KL divergence objective. It would be beneficial to visualize the training curves and analyze the stability of the training process. Furthermore, the authors should investigate the sensitivity of the method to different hyperparameters, such as the learning rate, the batch size, and the number of training epochs. This analysis would provide a better understanding of the robustness of the method and help to identify the optimal training settings. The authors should also discuss the limitations of their method and suggest potential directions for future research. This would help to position the work within the broader context of knowledge distillation and provide a roadmap for future advancements in the field.

### Questions

1. How does the proposed method perform on other tasks such as summarization, translation, or question answering?
2. How does the proposed method compare to other KD methods for LLMs, such as Mini-1.3B?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
