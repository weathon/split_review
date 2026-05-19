### Summary

This paper introduces Instructive Decoding (ID), a method to improve the instruction-following ability of instruction-tuned language models. By contrasting the original instruction with noisy instructions, the model is able to generate responses that better align with the given instructions. Experiments on unseen task generalization demonstrate that ID consistently outperforms baseline models across various setups.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.
2. The experimental results are good and the analysis is comprehensive.

### Weaknesses

#### Some Related Works

[1] Contrastive Decoding
[2] Contrastive Input Decoding for Language Model Alignment

#### comment

1. The novelty of this paper is somewhat limited. The idea of using noisy instructions as negative examples for contrastive decoding is straightforward and has been explored in previous work. For example, the "opposite" instruction is similar to the negative prompts in contrastive decoding [1,2]. It's like using the "opposite" of instructions as a negative prompt to filter out tokens that diverge from the instructions.
2. The proposed method is similar to using a larger k in top-p top-k decoding. The "opposite" instruction can be seen as introducing a "k" that encompasses almost the entire vocabulary, and the contrastive decoding filters out tokens that are inconsistent with the instructions. Therefore, it's like using a larger k and then filtering out tokens according to the instructions, which is intuitively better.
3. The motivation for using noisy instructions is not clear. It would be better to provide a more detailed explanation of why noisy instructions are used and how they help improve the model's performance. For example, why do the proposed noisy instructions work? How do they help the model better understand the original instructions? Are there any other types of noisy instructions that could be explored?

### Suggestions

The paper should more clearly articulate the specific mechanisms by which noisy instructions lead to improved instruction following. While the idea of contrasting against negative examples is not new, the application to instruction tuning could be novel if the specific types of noise and their impact are well-justified. The authors should provide a more detailed analysis of how each type of noisy instruction (e.g., truncated-shuffled, opposite) affects the model's attention or internal representations. For instance, does the truncated-shuffled instruction force the model to rely more on the initial parts of the instruction, thereby improving its ability to capture the core intent? Similarly, how does the 'opposite' instruction help the model better understand the nuances of the original instruction? A deeper dive into the model's internal behavior would strengthen the paper's claims and provide a more solid foundation for the proposed method. Furthermore, the authors should explore the relationship between the degree of noise and the performance gain. Is there an optimal level of noise that maximizes the effectiveness of the method? This could be explored by varying the amount of truncation, the degree of shuffling, or the strength of the 'opposite' prompt. Such an analysis would provide a more nuanced understanding of the method's behavior and potentially lead to further improvements.

To further enhance the paper, the authors should consider comparing their method against more established baselines in instruction tuning. While the paper demonstrates improvements over a basic baseline, it would be more convincing to compare against methods that explicitly aim to improve instruction following, such as those that use reinforcement learning or adversarial training. This would help to contextualize the performance of the proposed method and highlight its unique advantages. Additionally, the authors should investigate the computational cost of their method compared to other approaches. While the method appears to be simple, the additional forward pass required for the noisy instruction might introduce a significant overhead, especially for large models. A thorough analysis of the computational cost would be essential for assessing the practicality of the method. Furthermore, the authors should explore the robustness of the method to different types of instructions and tasks. Does the method perform equally well across different domains and instruction styles? Are there any specific types of instructions or tasks where the method struggles? Addressing these questions would provide a more comprehensive understanding of the method's limitations and potential for real-world applications.

Finally, the paper would benefit from a more detailed discussion of the limitations of the proposed method. While the experimental results are promising, it is important to acknowledge the potential shortcomings and areas for future research. For example, the authors could discuss the potential sensitivity of the method to the choice of noisy instructions and the need for careful tuning of the noise parameters. They could also explore the potential for the method to be gamed by adversarial examples. Addressing these limitations would provide a more balanced and realistic assessment of the method's capabilities. In addition, the authors should consider exploring alternative methods for generating noisy instructions. While the current methods are simple and effective, there might be other more sophisticated techniques that could lead to further improvements. For example, they could explore using generative models to create more diverse and challenging noisy instructions. This could potentially lead to a more robust and generalizable method for improving instruction following.

### Questions

Please see Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
