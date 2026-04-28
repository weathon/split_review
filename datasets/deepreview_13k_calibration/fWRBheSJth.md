# GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
The effectiveness of large language models (LLMs) is closely tied to the design of prompts, making prompt optimization essential for enhancing their performance across a wide range of tasks. Although recent advancements have focused on automating prompt engineering, many existing approaches rely exclusively on textual feedback, refining prompts based solely on inference errors identified by large, computationally expensive LLMs. Unfortunately, smaller models struggle to generate high-quality feedback, resulting in complete dependence on large LLM judgment. Moreover, these methods fail to leverage more direct and finer-grained information, such as gradients, due to operating purely in text space. To this end, we introduce, we introduce *GReaTer*, a novel prompt optimization technique that directly incorporates *gradient information over task-specific reasoning*. By utilizing task loss gradients, *GReaTer* enables self-optimization of prompts for smaller, lightweight language models (LM) without the need for costly closed-source LLMs, while maintaining reasonable prompt structures. This allows high-performance prompt optimization without dependence on massive LLMs, closing the gap between smaller models and the sophisticated reasoning often needed for prompt refinement. Extensive evaluations across diverse tasks demonstrate that \ours consistently outperforms previous methods, even those reliant on powerful LLMs. Additionally, *GReaTer*-optimized prompts frequently exhibit better transferability and, in some cases, boost task performance to levels comparable to or surpassing those achieved by larger language models, highlighting the effectiveness of *"gradient over reasoning"*-based prompt optimization. Full source code of *GReaTer* will be available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents GREATER, a novel prompt optimization technique that enables smaller language models to self-optimize their prompts without relying on larger, costly language models.

### Strengths
* This paper addresses a significant limitation in current prompt optimization methods
* This paper involves gradient information to prompt optimization
* This paper shows practical utility for improving smaller language model performance
* Figure 1 clearly demonstrates the difference between GREATER and previous methods

### Weaknesses
 * The case studies section could benefit from more detailed analysis of why certain prompts work better
* Could benefit from more theoretical analysis of why gradients over reasoning work better
* Line 462 explicitly mentions large language models (LLMs) which have already been defined in the introduction section. There seems like a typo in line 1186 as well, "Use these logical reasoning process steps and explain Step. step. Here is correct answer.","step" appears multiple times.
* Could include more diverse task types beyond reasoning tasks

### Questions
* How does the method scale with increasing model size? Have you considered using GREATER on larger open-source models like Llama-3.1-70B?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a prompt optimization technique that leverages gradient information over task-specific reasoning to enhance the performance of smaller language models (LLMs). GREATER enables self-optimization of prompts without relying on large, computationally expensive LLMs, which is a significant departure from existing methods that depend on textual feedback from large models.

### Strengths
1. GREATER presents an approach to prompt optimization by incorporating gradient information directly into the process, which is a departure from traditional text-based feedback methods. This innovation could reduce the computational costs associated with prompt engineering.

2. The paper is well-structured, with a clear problem statement and a detailed explanation of the GREATER method.

### Weaknesses
1. While GREATER shows promising results, it is not clear how well these findings generalize to other types of tasks beyond reasoning tasks. The method's reliance on task-specific loss gradients for optimization raises concerns about its applicability to tasks lacking clear objective evaluation criteria, such as text generation or summarization. The paper should address how GREATER could be adapted for tasks where the loss function is not as straightforward to define.

2. Although GREATER aims to reduce reliance on large LLMs, the paper does not discuss the computational resources required for the gradient-based optimization process itself. The computational cost of calculating gradients, especially with respect to the prompt, needs to be analyzed in detail. This includes the number of forward and backward passes required, the memory footprint of the optimization process, and how these scale with the size of the language model and the length of the input sequences. A comparison with the computational costs of traditional text-based prompt optimization methods is necessary to fully assess the practical benefits of GREATER.

3. The paper could benefit from a more detailed comparison with other gradient-based methods, especially those that also aim to optimize prompts without relying on large LLMs. The current evaluation lacks a thorough comparison with methods like AutoPrompt and PEZ, which also use gradient-based techniques for prompt optimization. A more comprehensive comparison should include a discussion of the differences in their optimization strategies, their performance on various tasks, and the characteristics of the prompts they generate.

### Questions
1. Can the authors comment on the potential of GREATER to be applied to tasks outside of reasoning, such as generation or summarization tasks?

2. How do the computational costs of GREATER compare to traditional text-based prompt optimization methods, especially when considering the training and inference phases?

3. The paper mentions the impact of different initialization prompts. Could the authors elaborate on how sensitive GREATER is to the choice of initialization and whether there are best practices for initializing prompts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a novel prompt optimization method that leverages some small language models to generate reasoning/explanation for problem solutions and utilizes the gradients on probable token candidates from the loss of answer tokens over reasoning tokens to refine the prompt optimization process. Experiments over 2 models and several benchmarks demonstrate that this method is effective.

### Strengths
- The idea of applying gradients over reasoning tokens to refine the selection of prompt tokens is novel.
- The proposed method has shown empirical success.

### Weaknesses
 - Presentation is unclear:
    - Slight notation abuse: the output space of $f_{\text{LLM}}$ is not well-defined. Does it output texts or token probabilities? They are different in Eq. 2&3.
    - It is not clear for the main results presented in Sec. 5.2 which model is used for prompt evaluation and which model is used for optimizing the prompt (e.g., in Table 2).
    - The complete algorithm 1 in Appx. B.1 should be moved to the main text for better understanding, as the presentation of the designed method is not very easy to follow.

- Sec. 5.6 does not show much insight which I think should be omitted from the main text.
- How to justify “simply considering fLLM(y|x ⊙ p) would give us the wrong objective to optimize, which in turn will give incorrect gradient information” in lin 237-238? The idea of taking gradients over reasoning paths is not well-explained. Intuitively, I expect the distribution of fLLM(y|x ⊙ p) to be more skewed than fLLM(y|x ⊙ p ⊙ r) as we can view $r$ as more computation to search for the right answer $y$.
- What does the gradient direction $\frac{\partial \mathcal{L}}{\partial \epsilon_i}$ physically mean? Why is there a negative sign and why is the token with the highest negative gradient value selected instead of the one with the largest gradient norm?
- Recent literature [1, 2, 3] related to applying the gradient concept in prompt optimization should be at least discussed.

### Questions
- what if there is no intersection in Eq.4? And how to guarantee semantic coherence among different token positions?
- Can you explain why the performance gain from gradient over reasoning is much smaller on Gemma model compared with LLaMA model?
- How about the performance on 1.5B or 3B model? 9B model is actually not very small in practice.

### Soundness
3

### Presentation
2

### Contribution
3
