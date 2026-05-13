# HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
We propose Hadamard High-Rank Adaptation (HiRA), a parameter-efficient fine-tuning (PEFT) method that enhances the adaptability of Large Language Models (LLMs). While Low-rank Adaptation (LoRA) is widely used to reduce resource demands, its low-rank updates may limit its expressiveness for new tasks. HiRA addresses this by using a Hadamard product to retain high-rank update parameters, improving the model capacity. Empirically, HiRA outperforms LoRA and its variants on several tasks, with extensive ablation studies validating its effectiveness. Our code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes Hadamard High-Rank Adaptation (HiRA), a parameter-efficient fine-tuning (PEFT) method for LLMs, to address limitations of Low-Rank Adaptation (LoRA) for complex tasks. The authors argue that while LoRA's expressiveness can be limited by its low-rank nature, which may restrict the model's ability to adapt to complex tasks. HiRA addresses this limitation by applying a Hadamard product between the low-rank update matrices and the frozen pretrained weights. The authors claim that this method effectively creates high-rank updates and enhance the expressiveness of the LLMs without significantly increasing the number of trainable parameters.

### Strengths
The paper introduces a creative way of using the Hadamard product to achieve high-rank adaptation within PEFT. This approach is an important contribution to address the common expressiveness limitation of LoRA-like PEFT methods. The authors show HiRA's consistent improvements over LoRA and other baselines which demonstrate that HiRA not only theoretically sounds but also practically effective. The ablation studies, such as singular value distribution analysis, show how HiRA's parameter dynamics behaves somewhat similarly to those of full fine-tuning and provide insights into the understanding of HiRA's expressiveness. Furthermore, the paper also compares HiRA not only to LoRA but also to another high-rank adaptation method called MoRA to justify the claim that its Hadamard product approach has unique advantages in achieving high-rank adaptability. Finally, HiRA seems to be lightweight and computationally efficient, which is attractive for practical applications.

### Weaknesses
First, my major concern is the connection between high rank, expressiveness and improved performance. Although the paper attempts to address this connection through ablation studies and performance improvements in experiments, it lacks a rigorous explanation that directly links high rank to expressiveness and explains why this is essential for improved performance in complex tasks. In other words, without showing how the observed rank impacts various task complexities, it's unclear if performance gains are solely due to the high rank, not other factors. For example, it's possible that the similarity in singular values of HiRA compared to FFT is due to an artifact of the data or tasks rather than an inherent property of high-rank adaptations.

Second, the paper lacks an in-depth analysis to show unique advantages of HiRA's high-rank nature. In particular, it's unclear if the improved performance of HiRA over MoRA is due solely to high-rank structure of Hadamard product, not other aspects of HiRA. Without detailed comparison of HiRA with other high-rank approaches such as MoRA, for example, showing distinctive singular value patterns of HiRA compared to those of MoRA, it's not easy to see unique benefits of HiRA's high-rank structure.

Finally, the paper provides limited insights into HiRA's generalization ability. In particular, while a high-rank structure might improve adaptability, it could also be potentially overfitting. The paper would benefit from evaluation of HiRA on, say, tasks requiring transfer learning.

### Questions
1. Is there a way to gain insights that using HiRA's Hadamard product is a better choice than other high-rank methods.
2. Can the authors justify that the singular value patterns of HiRA closely correlated to expressiveness properties that benefit tasks? Perhaps a detailed comparison of HiRA and MoRA in this context might help.
3. Are there attributes of HiRA other than high-rank strucutre that may contribute to its improved performance? Again, an in-depth comparison of HiRA and MoRA might help clarify this question.
4. Is HiRA prone to overfitting? Would evaluating HiRA on, say, transfer learning tasks help address this question?
5. Could you provide quantitative evidence of HiRA’s computational efficiency, such as memory usage, training time, and inference latency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the use of the Hadamard product in the new technique HiRA to parametrize _high-rank_ updates to the base model, based on LoRA, while using the same parameter count. Empirically HiRA outperforms LoRA on various tasks. The authors also provided analyses showing 1) the updates in HiRA are indeed high rank and 2) prominent singular values of HiRA trend more like full fine-tuning than LoRA. Finally the authors look into combining LoRA and HiRA as HiLoRA.

### Strengths
Clear presentation that empathizes the simple insight that the Hadamard product yields high-rank matrices. Extensive experiments. Convincing ablation studies.

### Weaknesses
More theoretical analysis would be useful. For example, more clarification on why Theorem 1 is important will help readers a lot. Specifically, it's not clear how the bound derived in Theorem 1 practically translates to the observed performance gains. The paper would benefit from a more detailed discussion on the conditions under which the Hadamard product leads to a high-rank update, and how this relates to the properties of the base model's weight matrix, $W_0$. The current analysis lacks a rigorous connection between the theoretical bound and the empirical results, leaving the reader to infer the practical implications of the theorem. Furthermore, the paper does not sufficiently explore the limitations of the proposed method, such as scenarios where the Hadamard product might not be effective or could lead to suboptimal updates.

### Questions
Did the authors consider alternative parametrization of the right operand of the Hadamard product? For example instead of W_0 maybe 'smooth' it with adjacent layers / other attention components within the same layer?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Hadamard High-Rank Adaptation (HiRA), a novel parameter-efficient fine-tuning (PEFT) method for Large Language Models (LLMs). HiRA aims to enhance the adaptability of LLMs by using a Hadamard product to retain high-rank update parameters, addressing the limitations of low-rank adaptation methods like LoRA. The authors demonstrate HiRA's effectiveness through extensive experiments and ablation studies, showing improved performance across various tasks compared to LoRA and its variants.

### Strengths
1. The paper introduces a new approach to PEFT by applying the Hadamard product to LLM adaptation, which is an original contribution to the field. Compared with LoRA, this method, HiRA, addresses a key limitation of LoRA by enabling high-rank updates, potentially improving the model's capacity to adapt to new tasks.

2. This method maintains a comparable number of trainable parameters to LoRA while enhancing performance, offering a cost-effective solution without additional inference overhead.

3. The paper offers a theoretical basis for the proposed method, and provides experimental results and ablation studies to demonstrate the effectiveness of the method.

### Weaknesses
The paper focuses primarily on comparison with LoRA and its variants. It would be beneficial to see comparisons with a broader range of PEFT methods. And it's unclear how well it generalizes across different model architectures or scales.

### Questions
1. How does HiRA perform on very large language models (e.g., models with hundreds of billions of parameters)? Are there any scaling challenges?

2. Have you explored the potential of combining HiRA with other PEFT techniques? Could this lead to even better performance?

### Soundness
4

### Presentation
3

### Contribution
3
