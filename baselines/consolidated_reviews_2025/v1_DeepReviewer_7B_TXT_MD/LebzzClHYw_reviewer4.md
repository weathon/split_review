### Summary

This paper proposes Instructive Decoding (ID), a novel method for enhancing the instruction-following capabilities of instruction-tuned language models. ID adjusts next-token predictions by contrasting them with those derived from a manipulated instruction, referred to as a noisy instruction. This approach aims to guide the model's output towards contextually relevant but deviating responses, thereby improving performance on unseen tasks. The authors evaluate ID across multiple datasets and model sizes, demonstrating its effectiveness and robustness, particularly with the opposing variant, which consistently yields the most significant performance gains.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and straightforward.
3. The authors conduct extensive experiments across various datasets and model sizes to demonstrate the effectiveness of ID.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The idea of adjusting logits based on a noisy instruction is not entirely new, and the paper does not provide a strong justification for why this particular approach is effective.
2. The experiments are limited to two datasets, UnNatInst and SupNatInst, and the results may not generalize to other datasets or tasks. The evaluation is also primarily focused on classification tasks, and it is unclear how the method would perform on other types of tasks, such as text generation or summarization.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It is unclear whether the performance gains justify the additional computational overhead.

### Suggestions

The paper would benefit from a more thorough investigation into the novelty of the proposed approach. While the idea of using noisy instructions for contrastive decoding is interesting, the paper needs to clearly articulate how this differs from existing methods that also leverage perturbed inputs. A more detailed comparison with related techniques, such as contrastive decoding with different types of noise or other methods that use adversarial examples, would help to establish the unique contribution of this work. The authors should also provide a more in-depth analysis of the specific types of noise used and why they are effective. For example, why does random word replacement work better than shuffling or truncating? A more rigorous analysis of the noise characteristics and their impact on the model's predictions would strengthen the paper's claims.

To address the limitations in the experimental evaluation, the authors should expand their experiments to include a wider range of datasets and tasks. The current evaluation is limited to two datasets, which raises concerns about the generalizability of the findings. It would be beneficial to include datasets from different domains and with different characteristics to assess the robustness of the proposed method. Furthermore, the evaluation should not be limited to classification tasks. The authors should also evaluate the method on text generation and summarization tasks to demonstrate its applicability to a broader range of NLP problems. This would provide a more comprehensive understanding of the method's strengths and weaknesses and its potential for real-world applications. The authors should also consider using a more diverse set of evaluation metrics to assess the performance of the method.

Finally, the paper needs to provide a more detailed analysis of the computational cost of the proposed method. While the authors claim that the method is lightweight, a more rigorous analysis is needed to quantify the computational overhead. The authors should provide a breakdown of the computational cost of each step of the method, including the noise generation and the contrastive decoding. It would also be helpful to compare the computational cost of the proposed method with other decoding methods. The authors should also discuss the practical implications of the computational cost and whether the performance gains justify the additional cost. A more thorough analysis of the computational aspects would provide a more complete picture of the proposed method and its practical applicability.

### Questions

1. How does the proposed method compare to other decoding methods that leverage noisy or perturbed inputs?
2. How does the performance of ID vary across different types of tasks?
3. What is the computational cost of the proposed method compared to other decoding methods?

### Rating

8

### Confidence

3

**********
