### Summary

This paper proposes a cascade framework to save the cost of using LLMs while not sacrificing task performance. The proposed framework uses a weaker LLM to solve easy questions and a stronger LLM to solve hard questions. The authors propose two methods to detect whether the weaker LLM can solve the question correctly. Experiments on six reasoning datasets show that the proposed framework can achieve comparable performance to using solely the stronger LLM but require only 40% of its cost.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed framework is simple and effective. The experimental results show that the proposed framework can achieve comparable performance to using solely the stronger LLM while requiring only 40% of its cost.

### Weaknesses

#### Some Related Works

[1] Self-Consistency Improves Chain of Thought Reasoning in Language Models
[2] Self-Refine: Iterative Refinement with Self-Feedback
[3] Self-Ask: Enhancing Large Language Models with Active Learning for Mathematical Reasoning
[4] Self-Alignment for LLMs: Aligning Models with Noisy Self-Feedback
[5] Self-Refine: Enhancing Reasoning Capabilities of LLMs through Self-Refinement
[6] Self-Refine: A Study on Self-Refinement for Large Language Models

#### comment

1. The proposed framework is similar to the self-consistency framework [1]. The main difference is that the proposed framework uses a weaker LLM to solve easy questions and a stronger LLM to solve hard questions, while the self-consistency framework uses the same LLM to solve all questions. The authors should compare the proposed framework with the self-consistency framework and analyze the advantages and disadvantages of the proposed framework compared to the self-consistency framework.
2. The proposed framework is also similar to the self-refine framework [2-6]. The main difference is that the proposed framework uses a weaker LLM to solve easy questions and a stronger LLM to solve hard questions, while the self-refine framework uses the same LLM to solve all questions. The authors should compare the proposed framework with the self-refine framework and analyze the advantages and disadvantages of the proposed framework compared to the self-refine framework.
3. The authors should compare the proposed framework with other methods that use different LLMs to solve questions, such as the ensemble method [7] and the multi-model method [8].
4. The authors should evaluate the performance of the proposed framework on more datasets, such as the GSM8K dataset [9] and the MATH dataset [10].
5. The authors should evaluate the performance of the proposed framework on more LLMs, such as the LLaMA-2-7B model [11] and the Mistral-7B model [12].

### Suggestions

The paper introduces a cascade framework that leverages a weaker LLM for easier questions and a stronger LLM for more difficult ones, aiming to reduce computational costs while maintaining performance. While the idea is promising, the paper would benefit from a more thorough comparison with existing methods, particularly those that also employ a form of model selection or routing. The current comparison with self-consistency is insufficient; a more detailed analysis of the differences in how the two approaches handle uncertainty and question difficulty is needed. For example, the paper should explore how the proposed framework's performance varies with the relative capabilities of the weaker and stronger LLMs. Does the framework still perform well when the difference in capabilities between the two models is small? Furthermore, the paper should investigate the impact of the sampling strategy used by the weaker LLM. How does the number of samples and the diversity of those samples affect the accuracy of the consistency check? A more detailed analysis of these factors would strengthen the paper's claims.

In addition to the comparisons with self-consistency and self-refine, the paper should also consider comparing against other methods that use different LLMs for different tasks. The current discussion of ensemble methods is too brief and does not fully address the nuances of combining multiple models. The paper should explore how the proposed framework compares to methods that use a weighted average of predictions from multiple models, or methods that use a more sophisticated routing mechanism. Furthermore, the paper should investigate the computational overhead of the proposed framework. While the paper claims that the framework is cost-effective, it does not provide a detailed analysis of the computational resources required to run the weaker and stronger LLMs. A more thorough analysis of the trade-off between cost and performance would be beneficial. The paper should also explore the sensitivity of the framework to the choice of the weaker and stronger LLMs. Does the framework perform well with a wide range of LLMs, or is it highly dependent on the specific models used?

Finally, the paper should provide a more detailed analysis of the types of questions that are correctly classified as easy or hard by the proposed framework. Are there specific characteristics of these questions that make them easier or harder to solve? A more detailed analysis of the error cases would help to identify the limitations of the framework and suggest directions for future research. The paper should also explore the robustness of the framework to adversarial examples. Are there specific types of questions that are particularly difficult for the framework to classify? Addressing these points would significantly strengthen the paper and provide a more comprehensive understanding of the proposed framework.

### Questions

See Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
