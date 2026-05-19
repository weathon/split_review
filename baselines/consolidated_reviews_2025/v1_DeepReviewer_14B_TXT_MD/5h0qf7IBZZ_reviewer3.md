### Summary

This paper proposes a knowledge distillation method for large language models (LLMs). The authors argue that the standard knowledge distillation objectives are sub-optimal for LLMs that perform tasks in a generative manner. To alleviate this problem, they propose to minimize reverse KLD, which causes the student to seek the major modes of the teacher, and assign low probabilities to the teacher’s void regions. They derive the gradient of the objective with Policy Gradient. To further stabilize and accelerate training, they propose single-step decomposition to reduce variance, teacher-mixed sampling to alleviate reward hacking, and length normalization to eliminate the length bias. They apply their method to various generative language models with sizes ranging from 120M to 13B in the instruction-following setting that covers a large range of NLP tasks. They use 5 datasets with Rouge-L and human judgment for evaluation. Experiments show that MiniLLM consistently outperforms standard KD baselines on all the datasets and scales up well from 120M to 13B models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The motivation is clear and the proposed method is sound.
3. The experiments are extensive and the results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the standard KD objectives are sub-optimal for LLMs that perform tasks in a generative manner. However, the authors do not provide a detailed analysis of the limitations of standard KD objectives in this context. Specifically, it's unclear how the forward KL divergence, typically used in standard KD, fails to capture the nuances of generative tasks performed by LLMs. A more in-depth discussion of the mismatch between the training objective and the generative nature of LLMs would be beneficial.
2. The authors propose to minimize reverse KLD, which causes the student to seek the major modes of the teacher, and assign low probabilities to the teacher’s void regions. However, the authors do not provide a detailed analysis of the potential drawbacks of this approach. For instance, while focusing on the major modes might improve performance on common tasks, it could lead to a loss of diversity in the student model's output, potentially hindering its ability to generalize to less frequent but still valid outputs. This trade-off between mode-seeking and diversity needs further exploration.
3. The authors propose single-step decomposition to reduce variance, teacher-mixed sampling to alleviate reward hacking, and length normalization to eliminate the length bias. However, the authors do not provide a detailed analysis of the effectiveness of these strategies. For example, how does the single-step decomposition specifically reduce variance compared to other variance reduction techniques? What is the optimal mixing ratio for teacher samples, and how does this ratio affect the student's learning process? A more rigorous analysis of these techniques is needed.
4. The authors use 5 datasets with Rouge-L and human judgment for evaluation. However, the authors do not provide a detailed analysis of the limitations of these evaluation metrics. For example, Rouge-L primarily measures n-gram overlap and may not capture the semantic quality or coherence of the generated text. Similarly, human judgment can be subjective and may not be consistent across different evaluators. The authors should discuss the potential biases and limitations of these metrics and consider incorporating additional metrics that capture different aspects of text quality.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the limitations of standard knowledge distillation (KD) objectives when applied to generative tasks performed by large language models (LLMs). Specifically, they should elaborate on why the forward KL divergence, which is commonly used in standard KD, is not well-suited for capturing the complexities of generative tasks. This could involve a discussion of how the forward KL divergence might lead to a mismatch between the training objective and the desired output distribution of the student model. For example, the authors could analyze how the forward KL divergence might encourage the student model to overfit to the teacher's training data, rather than learning to generate diverse and high-quality text. Furthermore, the authors should provide a more rigorous justification for using reverse KL divergence, including a discussion of its potential drawbacks. While the mode-seeking behavior of reverse KL divergence might be beneficial in some cases, it could also lead to a loss of diversity in the student model's output. The authors should explore this trade-off and discuss how they mitigate the potential negative effects of mode-seeking. This could involve analyzing the impact of reverse KL divergence on the student model's ability to generate diverse and creative text, and comparing it to the performance of standard KD methods in this regard.

In addition, the authors should provide a more detailed analysis of the effectiveness of the proposed optimization strategies. For example, they should explain how single-step decomposition specifically reduces variance compared to other variance reduction techniques, such as importance sampling or control variates. They should also provide a more thorough analysis of the teacher-mixed sampling strategy, including a discussion of how the optimal mixing ratio is determined and how it affects the student's learning process. Furthermore, the authors should provide a more detailed explanation of how length normalization eliminates length bias, and how this bias affects the performance of the student model. This could involve analyzing the impact of different length normalization techniques on the student model's ability to generate text of varying lengths. The authors should also consider including ablation studies to demonstrate the effectiveness of each of these strategies individually and in combination.

Finally, the authors should provide a more detailed analysis of the limitations of the evaluation metrics used in the paper. While Rouge-L and human judgment are commonly used in text generation tasks, they have limitations that should be acknowledged. For example, Rouge-L primarily measures n-gram overlap and may not capture the semantic quality or coherence of the generated text. Similarly, human judgment can be subjective and may not be consistent across different evaluators. The authors should discuss these limitations and consider incorporating additional metrics that capture different aspects of text quality, such as semantic similarity, coherence, and diversity. They could also consider using metrics that are specifically designed for evaluating generative models, such as BLEU or METEOR. Furthermore, the authors should provide a more detailed analysis of the human evaluation process, including the instructions given to the evaluators and the measures taken to ensure consistency and reliability.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
