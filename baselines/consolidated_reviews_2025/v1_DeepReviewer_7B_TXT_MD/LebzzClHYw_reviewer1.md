### Summary

This paper proposes a new decoding method called Instructive Decoding (ID). The main idea is to adjust the logits for the next token prediction by contrasting them with those derived from a noisy instruction. This noisy instruction is created by injecting perturbations into the original instruction. The authors explore various types of perturbations, including truncation, shuffling, random word replacement, and opposing instructions. The proposed method does not require any additional parameter updates and can be applied to any instruction-tuned language model. The authors evaluate the performance of ID on two datasets, UnNatInst and SupNatInst, across various sizes of Tk-Instruct models. The results show that ID consistently outperforms the baseline model, with the opposing instruction variant yielding the most significant performance gains.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and straightforward.
- The authors conduct extensive experiments across various datasets and model sizes to demonstrate the effectiveness of ID.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed method is limited. The idea of adjusting logits based on a noisy instruction is not entirely new, and the paper does not provide a strong justification for why this particular approach is effective.
- The experiments are limited to two datasets, UnNatInst and SupNatInst, and the results may not generalize to other datasets or tasks. The evaluation is also primarily focused on classification tasks, and it is unclear how the method would perform on other types of tasks, such as text generation or summarization.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. It is unclear whether the performance gains justify the additional computational overhead.

### Suggestions

The paper should provide a more thorough justification for the specific design choices of the Instructive Decoding (ID) method. While the idea of contrasting logits with a noisy instruction is interesting, the paper needs to delve deeper into why this particular approach is effective and how it differs from existing methods that also leverage noisy or perturbed inputs. A more detailed analysis of the underlying mechanisms that lead to performance improvements would strengthen the paper's contribution. For example, the authors could explore the relationship between the type of noise used and the resulting performance gains, providing insights into which types of perturbations are most effective and why. Furthermore, a comparison with other methods that use similar techniques would help to contextualize the novelty of the proposed approach.

To address the limitations in the experimental evaluation, the authors should expand the scope of their experiments to include a wider range of datasets and tasks. This would help to demonstrate the generalizability of the proposed method and its applicability to different scenarios. Specifically, the authors should consider evaluating ID on datasets that involve text generation or summarization tasks, which are common in real-world applications. Additionally, the paper should include a more detailed analysis of the performance of ID on different types of tasks, highlighting any task-specific trends or limitations. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method. The authors should also consider including a comparison with other decoding methods that are specifically designed for instruction-tuned models, to better contextualize the performance of ID.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. While the authors claim that the method is lightweight, a more rigorous analysis is needed to quantify the computational overhead and to determine whether the performance gains justify the additional cost. This analysis should include a comparison with other decoding methods, and should consider the impact of different model sizes and instruction lengths on the computational cost. The authors should also discuss the practical implications of the computational cost, and whether the method is suitable for real-world applications with limited computational resources. A more thorough analysis of the computational aspects would provide a more complete picture of the proposed method and its practical applicability.

### Questions

- How does the proposed method compare to other decoding methods that leverage noisy or perturbed inputs?
- How does the performance of ID vary across different types of tasks?
- What is the computational cost of the proposed method compared to other decoding methods?

### Rating

5

### Confidence

3

**********
