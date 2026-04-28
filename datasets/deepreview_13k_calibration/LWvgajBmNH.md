# MORE: A MIXTURE OF LOW-RANK EXPERTS FOR ADAPTIVE MULTI-TASK LEARNING

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
With the rapid development of Large Language Models (LLMs), Parameter-Efficient Fine-Tuning (PEFT) methods have gained significant attention, which aims to achieve efficient fine-tuning of LLMs with fewer parameters. As a representative PEFT method, Low-Rank Adaptation (LoRA) introduces low-rank matrices to approximate the incremental tuning parameters and achieves impressive performance over multiple scenarios. After that, plenty of improvements have been proposed for further improvement. However, these methods either focus on single-task scenarios or separately train multiple LoRA modules for multi-task scenarios, limiting the efficiency and effectiveness of LoRA in multi-task scenarios. To better adapt to multi-task fine-tuning, in this paper, we propose a novel Mixture of Low-Rank Experts (MoRE) for multi-task PEFT. Specifically, instead of using an individual LoRA for each task, we align different ranks of LoRA module with different tasks, which we named low-rank experts. Moreover, we design a novel adaptive rank selector to select the appropriate expert for each task. By jointly training low-rank experts, MoRE can enhance the adaptability and efficiency of LoRA in multi-task scenarios. Finally, we conduct extensive experiments over multiple multi-task benchmarks along with different LLMs to verify model performance. Experimental results demonstrate that compared to traditional LoRA and its variants, MoRE significantly improves the performance of LLMs in multi-task scenarios and incurs no additional inference cost. We also release the model and code to facilitate the community.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a MoE LoRA-based method, MoRE, for parameter-efficient fine-tuning in multi-task scenarios. The authors introduce a shared low-rank matrix with different rank cut-offs, which serve as distinct experts. Additionally, they present an adaptive gating mechanism that selects the appropriate rank value for each task, enabling efficient specialization across diverse tasks.

### Strengths
1. The idea is interesting. Rather than allocating dedicated experts through separate low-rank adapters, this work reuses a single low-rank matrix, employing a gating function to select portions of it as distinct experts. This approach effectively models diverse tasks in multi-task training.

2. The experimental results are promising. The proposed method consistently outperforms baselines across most datasets, with particularly strong performance in the LLAMA setting.

### Weaknesses
1. The contribution over existing mixture-of-LoRA methods (such as MixLoRA and MOELoRA) appears limited. This work can be interpreted as a specific case within existing frameworks, where each expert has a rank of 1, and a condition is enforced such that, when selecting expert k, all preceding experts (1 to k-1) are also selected. While the authors claim parameter efficiency, the core mechanism of selecting cumulative ranks still resembles a constrained form of existing MoE methods, and the novelty in terms of architecture is not substantial.

2. While the proposed method reuses the adapter matrix and claims that this reduces the number of parameters, making it independent of the number of experts, several concerns arise:
    - With this design, the first few rows or columns of the adapter matrix are reused by multiple tasks, which may be effective for tasks with some correlation, such as those in GLUE. However, this could be problematic when the feature-label mappings differ significantly across tasks. The method's ability to handle heterogeneous tasks with minimal shared information remains questionable, as the shared low-rank matrix might become a bottleneck.
    - The number of experts is constrained by the maximum rank of the LoRA matrix, which may lead to issues when the number of tasks is large. This constraint limits the scalability of the approach when dealing with a large number of diverse tasks, as the method cannot allocate a unique expert for each task beyond the maximum rank.

### Questions
Q1: How does the proposed method handle scenarios where the number of tasks significantly exceeds the maximum rank of the shared low-rank matrix?

Q2: If tasks are highly distinct with no shared information, does the design fail to accommodate such diversity effectively?

Q3: Why is the selection enforced as 1:k rather than allowing an arbitrary subset of ranks from 1 to \( r_{\text{max}} \), which might seem more intuitive?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors aim to address the problem of Applying LoRA to multi-taslk scenarios. The authors propose a MoRE approach for multi-task PEFT, aligning different ranks of LoRA modules with different tasks using a Gate function and designing an adaptive rank selector to select the appropriate rank for each task. The empirical findings show that the proposed MoRE method can outperform existing multi-task LoRA methods.

### Strengths
(1)The topic of multi-task PEFT is important.

(2)Even though there are many typos appear in the current version, the paper is easy to follow.

(3) To use a gate function to define the selection of appropriate ranks for different tasks is interesting. 

(4) The experiments are convinced

### Weaknesses
(1) The author should double-check their writings. For example: in Line 161, The target is to learn a shared model F with parameters θ to satisfy the requirements of different （？） simultaneously. And in Line 243 “One step further, during the backward pass, the arg max in Eq.(3) is non-differentiable” obviously, argmax appears in eq(4).

(2) The authors claim that a smaller learning rate will benefit the training of MoRE, it would be better to test different learning rate in the extensive experiments to support this claim.

(3) It would be better to test other LLMs, like Mistral-7B, to demonstrate the proposed method can be used in different architectures.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the MoRA, a mixture of expert LoRA methods to leverage the MoE framework in parameter-efficient tuning settings. This paper is well-written and shows some gains on the performance. However, this paper lacks novelty compared with other related works and the method is only tested on GLUE benchmarks. Also, similar as other MoE LoRA methods, the lora experts cannot merge with the LLM during inference. Thus, this method will increase the memory usage during inference and cannot leverage inference optimization of the Transformer model.

### Strengths
This paper is well-written, and the statement is clear. This method improves previous LoRA MOE methods and provides some gains. The experiments show promising improvements compared to the baselines reported.

### Weaknesses
1. This paper only evaluates on GLUE benchmarks, where most of the datasets mainly focus on natural language processing instead of commonsense and complicated reasoning. The reasoning and knowledge capabilities of the LLMs are still under explored in this paper.

2. MoE-based LoRA uses more parameters than standard LoRA methods and this LoRA matrix cannot be merged into the original LLMs during inference. Therefore, during inference, the model requires more memory to perform inference and could not leverage inference optimization on Transformer model. 

3. This approach has no novelty compared to other MoE lora methods.

### Questions
1. Whether does this method perform well on other popular reasoning or knowledge benchmarks such as MMLU, code or math?
2. How does this method perform inference?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an approach to enhance the effectiveness of LoRA in multi-task Parameter Efficient Fine-Tuning scenarios. Traditional LoRA methods, which often employ a separate module for each task or focus solely on single-task applications, fall short in multi-task environments due to limited efficiency. MoRE addresses this by integrating multiple low-rank experts, each aligned with different tasks, within a single framework. More incorporates the adaptive rank selector, which dynamically chooses the most suitable expert for each specific task. This integrated approach allows for the simultaneous training of multiple low-rank experts.

### Strengths
1. The MoRE method introduces an approach by integrating multiple low-rank experts into a single, adaptive framework. This design, combined with an adaptive rank selector, provides a flexible and efficient solution for multi-task learning.

2. MoRE improves the overall performance of LLMs in multi-task settings by allowing multiple tasks to be addressed concurrently without the need for separate modules for each task.

### Weaknesses
1. One key advantage of LoRA is its ability to merge into the original model, which reduces inference costs. However, the use of a selector with varied ranks in this paper seems to compromise this advantage. Clarifying how this approach can be effectively merged back, if possible, or discussing strategies to mitigate the increased inference complexity would provide valuable insights and address a critical concern.

2. Testing the proposed method on more advanced models, such as Gemma2, would be beneficial to demonstrate its robustness and relevance.

3. The current experiments only test LoRA with a fixed rank of 8, which limits understanding of the proposed method’s performance under different rank configurations. Testing with a range of ranks would give a more comprehensive view of how varying rank values impact the approach's effectiveness and the trade-offs between parameter efficiency and task performance.

4. The method of setting the maximum rank for the selector is not clearly explained. It remains unclear whether the maximum rank is manually defined or set automatically. Providing a detailed explanation of this parameter choice and how it adapts to different tasks, if applicable, would enhance the method’s transparency and usability.

5. The performance improvement demonstrated by the proposed method appears marginal and does not achieve the best results across several tasks, including SST-2, MRPC, and ARC. Conducting statistical significance tests would help substantiate whether the reported improvements are meaningful and support the claims that the improvement is significant.

6. The relationship between the selected ranks, the specific tasks, and the reason are not well explored. A detailed analysis of how the selector determines ranks for each task and which type of tasks consistently require higher or lower ranks would provide valuable insights.

7. The current evaluation does not explore the effect of handling different numbers of tasks in a multi-task learning setting. Testing the model’s performance with varying numbers of concurrent tasks would provide valuable insights into its scalability and robustness.

### Questions
Please refer to the Weakness.

### Soundness
2

### Presentation
2

### Contribution
2
