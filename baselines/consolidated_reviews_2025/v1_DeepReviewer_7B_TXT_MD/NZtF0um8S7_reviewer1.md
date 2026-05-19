### Summary

This paper studies in-context learning in seq2seq models, and proposes two approaches to improve the ICL ability of seq2seq models. The first approach is about prompt design, where the authors suggest aligning prompts with pretraining objectives and designing prompts that suit the task. The second approach is about the fusion of examples in the prompt. The authors evaluate their approaches on a variety of tasks, including NLU tasks from SuperGLUE and generation tasks from XSum and WebNLG. The results show that their approaches outperform baselines, including T5 and OPT.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. This paper studies in-context learning in seq2seq models, which has been relatively less explored compared to decoder-only models. The paper identifies two important aspects of ICL in seq2seq models: prompt design and example fusion. The proposed approaches are simple and effective, and the authors provide extensive experiments to validate their effectiveness.

2. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] T0: Massively Multitask Language Model for Zero-Shot In-Context Learning
[2] In-context Learning solves Smaller-Scale Sokoban
[3] In-Context Learning with Large Language Models for Time Series Forecasting
[4] In-Context Learning and Induction Heads
[5] What learning algorithm is in-context learning? Investigations with linear models

#### comment

1. The paper lacks a clear motivation for studying ICL in seq2seq models. While the authors mention that seq2seq models have been underexplored in this area, they do not provide a strong justification for why this is an important problem to tackle. Specifically, the paper does not articulate the unique challenges or opportunities that studying ICL in seq2seq models presents compared to decoder-only models. The connection between the observed performance gains and the broader goals of AI research is not clearly established.

2. The paper does not adequately discuss the relationship between ICL in seq2seq models and existing work on ICL in decoder-only models. The authors should clarify how their findings relate to the theoretical understanding of ICL in decoder-only models, such as the role of attention mechanisms and the emergence of in-context learning capabilities. The paper should also discuss whether the proposed methods are expected to generalize to decoder-only models, and if so, what modifications might be necessary.

3. The paper does not provide a detailed analysis of the computational cost of the proposed approaches. While the authors mention that their methods are efficient, they do not provide a quantitative comparison of the computational resources required by their methods versus standard fine-tuning approaches. This is important for assessing the practical applicability of the proposed methods, especially for large-scale models and datasets.

4. The paper does not explore the limitations of the proposed approaches. For example, the authors should discuss the types of tasks or datasets where their methods might not be effective, and the potential reasons for these limitations. A more thorough analysis of the failure cases would provide a more balanced view of the proposed methods.

5. The paper does not compare its methods to other approaches for improving ICL in seq2seq models, such as prompt engineering techniques or architectural modifications. A more comprehensive comparison would help to contextualize the contributions of the paper and highlight the advantages and disadvantages of the proposed methods.

### Suggestions

The paper would benefit from a more detailed discussion of the motivation behind studying ICL in seq2seq models. The authors should clearly articulate the unique challenges and opportunities that this area presents, and how their work contributes to the broader field of AI. For example, they could discuss whether the observed performance gains are due to the specific architecture of seq2seq models, or if they are a general property of ICL. Furthermore, the authors should explore the potential applications of their findings in real-world scenarios, and how these applications might differ from those of decoder-only models. A more compelling motivation would strengthen the paper's overall impact and relevance.

The paper should also include a more thorough discussion of the relationship between ICL in seq2seq models and existing work on ICL in decoder-only models. The authors should analyze the similarities and differences between the two, and discuss how their findings relate to the theoretical understanding of ICL in decoder-only models. For example, they could investigate whether the attention mechanisms in seq2seq models play a similar role to those in decoder-only models, and whether the proposed methods are expected to generalize to decoder-only models. A more detailed analysis of these aspects would provide a deeper understanding of the underlying mechanisms of ICL and help to contextualize the paper's contributions.

Finally, the paper should include a more comprehensive analysis of the computational cost of the proposed approaches. The authors should provide a quantitative comparison of the computational resources required by their methods versus standard fine-tuning approaches. This analysis should include the training time, memory usage, and inference time. The authors should also discuss the scalability of their methods to large-scale models and datasets. Furthermore, the paper should include a more detailed analysis of the limitations of the proposed approaches, and discuss the potential reasons for these limitations. A more thorough analysis of the failure cases would provide a more balanced view of the proposed methods.

### Questions

1. How does the proposed approach compare to other approaches for improving ICL in seq2seq models, such as prompt engineering techniques or architectural modifications?

2. What are the limitations of the proposed approaches? Are there specific tasks or datasets where the methods are less effective?

3. How does the computational cost of the proposed approaches compare to standard fine-tuning approaches?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
