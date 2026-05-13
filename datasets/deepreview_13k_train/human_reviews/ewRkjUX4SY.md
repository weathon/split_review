# Conversational Few-Shot Prompting: Rethinking Few-Shot Prompting for Chat Language Model

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
In-context learning, also referred to as few-shot learning, enables language models to adapt to tasks using a limited number of examples embedded in the prompt. Traditional approaches typically present all examples in a single prompt, which works well for pre-trained base models. However, the application of this method to instruction-tuned chat models, such as ChatGPT, remains underexplored.
In this paper, we introduce a novel conversational few-shot prompting technique, which structures few-shot examples as multi-turn conversation between the user and the assistant, rather than a single input prompt. This conversational framing better aligns with the interactive nature of chat models, enhancing their instruction-following abilities and generalization across tasks.
Through experiments on various benchmarks, we demonstrate that this approach significantly improves performance, particularly in low-shot scenarios, compared to traditional few-shot prompting. Our results suggest that this method provides a more flexible and robust way to leverage few-shot examples in instruction-tuned chat models, improving task performance without the need for additional fine-tuning, reducing prompt sensitivity, and offering potential for diverse applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel conversational few-shot prompting technique for instruction-tuned chat language models. The proposed approach structures the few-shot examples as a multi-turn dialogue between the user and the assistant, in contrast to the traditional single-prompt format. The authors demonstrate through extensive experiments that this conversational framing significantly improves performance, particularly in low-shot scenarios, across various benchmarks and model families. The results suggest that this method provides a more flexible and robust way to leverage few-shot examples in chat models, enhancing their instruction-following abilities and generalization without the need for additional fine-tuning.

### Strengths
(1) The authors propose a conversational few-shot prompting technique that aligns more naturally with the interactive nature of chat models, allowing them to better leverage their inherent conversational capabilities.
(2) The experimental evaluation is comprehensive, covering a diverse set of benchmarks, model families, and shot settings, providing strong empirical evidence for the effectiveness of the proposed approach.
(3) The paper is well-structured, with a clear problem definition, thorough background on few-shot prompting, and a detailed description of the new conversational method, making it easy for readers to follow and understand the contributions.

### Weaknesses
1. The approach relies on prompt engineering without a clear explanation of why the multi-turn structure improves overall performance or enhances instruction-following capabilities. Why would putting few-shot exemplars in the chat be beneficial? Is there any potential mechanism behind the scenes?
2. The paper offers limited insight into error cases or scenarios where the method may perform poorly, which would provide a clearer understanding of its robustness across different applications.

### Questions
(1) Could you please provide the specific prompting templates used in your experiments, including the format of the few-shot examples and the instructions given to the models?
(2) Can you elaborate on the potential reasons why the conversational framing leads to superior performance, particularly in low-shot scenarios? What are the key characteristics or capabilities of the chat models that enable them to benefit from this approach?
(3) Would it be possible to conduct additional experiments comparing the proposed method with other few-shot prompting techniques, such as prompt tuning or prompted fine-tuning? This could help to better understand the relative merits and limitations of the conversational approach.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the gap in applying in-context learning (or few-shot learning) to instruction-tuned chat models, like ChatGPT, which has been underexplored. It introduces a "conversational few-shot prompting" approach that presents few-shot examples as multi-turn interactions between the user and assistant, rather than a single prompt. This conversational format aligns with the interactive nature of chat models, enhancing their ability to follow instructions and generalize across tasks. Experimental results show that this method improves performance, especially in low-shot scenarios, offering a flexible and robust way to use few-shot examples without additional fine-tuning. This approach reduces prompt sensitivity and opens up potential for diverse applications.

### Strengths
- This paper presents a new few-shot prompting method optimized for chat-based, instruction-tuned large language models (LLMs).
- The authors conduct extensive experiments with popular open-source LLMs, including the LLaMA series and Qwen series, across various benchmarks, varying the number of few-shot examples.

### Weaknesses
- In my opinion, this technique lacks technical novelty, as it primarily focuses on a prompting method. However, the paper provides extensive experiments demonstrating the effectiveness of the proposed "conversational few-shot prompting method," making it an acceptable approach.
- Regarding the proposed method, the conversational few-shot prompting method appears to address problems by presenting contextually similar topics in a dialogue format. Could you clarify the difference between few-shot prompting in a chat-based model (as shown in the bottom right of Figure 1) and "conversational few-shot prompting"?
- I do not fully understand the motivation for this paper. Specifically, could the authors elaborate on why they believe few-shot prompting is beneficial for instruction-tuned chat models, given that these models are not specifically optimized for this approach?
- In Table 1, a detailed analysis would be beneficial to explain why the performance decreases with larger models as the number of few-shot examples increases. For instance, perhaps larger models exhibit a higher tendency to refuse generating responses. Additionally, in the BoolQ dataset, there is no performance difference in the LLaMA 70B model regardless of the few-shot count, suggesting that the proposed few-shot prompting method may not be effective in this case. This aspect requires further explanation.
- In Table 2, on the MMLU dataset, the LLaMA-3.2-1B model achieves a score of 0, even with varying numbers of few-shot examples. Could you present one or two generated examples? (This part does not impact the overall score).

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes Conversational Few-Shot Prompting for chat models, transforming few-shot examples into multi-turn dialogues to align with conversational model dynamics. Conversational Few-Shot Prompting improves instruction-following and generalization, outperforming traditional few-shot prompts in low-shot scenarios across benchmarks without additional fine-tuning, enhancing task performance and reducing prompt sensitivity.

### Strengths
1. Revises few-shot prompting by structuring examples as multi-turn dialogues, aligning better with conversational models.
2. Demonstrates enhanced performance across multiple tasks in various few-shot configurations and ability to follow complex instructions.

### Weaknesses
1. The approach relies on prompt engineering without a clear explanation of why the multi-turn structure improves overall performance or enhances instruction-following capabilities. Why would putting few-shot exemplars in the chat be beneficial? Is there any potential mechanism behind the scenes?
2. The paper offers limited insight into error cases or scenarios where the method may perform poorly, which would provide a clearer understanding of its robustness across different applications.

### Questions
1. In instruction-following tasks, where are the instructions placed within the prompt in the conversational format? Could the authors provide an example comparing how instructions are incorporated in this approach versus traditional instruction-following formats?
2. Are there specific tasks or model architectures where this approach might be less effective? Have the authors considered edge cases where the conversational context may not provide improvements or could even hinder performance?
3. How does this approach perform relative to other prompting techniques (such as CoT+few shot vs conv-fewshot without CoT), particularly in complex reasoning scenarios?
4. What types of errors are most frequent with this method, particularly across different task types or complexity levels? Are there specific failure cases that occur more often in certain scenarios (e.g., instruction-following vs. complex reasoning tasks)? Could a detailed error analysis, possibly by task type or difficulty level, reveal areas for potential improvement or further refinement?
5. What are the decoding parameters for the baseline prompts and the conversational prompts? Any randomness is included during the decoding steps? How many runs are conducted for evaluating each task?

### Soundness
1

### Presentation
2

### Contribution
2
