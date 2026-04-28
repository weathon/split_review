# On the loss of context-awareness in general instruction finetuning

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Pretrained Large Language Models (LLMs) require post-training methods such as supervised fine-tuning (SFT) on instruction-response pairs to enable instruction following. 
However, this process can potentially harm existing capabilities learned during pretraining. 
In this paper, we investigate the loss of context awareness after SFT, defined as the capability to extract and understand information from the user-provided context and respond accordingly. 
We are the first to identify and show that the loss of context-awareness appears on instruction-finetuned LLMs when the chat template is applied to the input prompts. 
We identify the performance decline is partially caused by the bias embedded into the chat template to focus less on the the user-provided context.
Based on these observations, we propose two methods to mitigate the loss of context awareness in instruct models: post hoc attention steering on user prompts and conditional instruction fine-tuning with a context-dependency indicator.
Empirical experiments on 4 context-dependent downstream tasks and 3 pretrained LLMs of different sizes show that our methods can effectively mitigate the loss of context awareness without compromising the general ability of instruction following. 
Our findings also strongly advocate the necessity to benchmark context awareness after instruction fine-tuning carefully.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper claims the loss of context-awareness on instruction-tuned LLMs when the chat template is applied to the input prompts. It further proposes two methods to mitigate the loss of context awareness in instruct models: post-hoc attention steering and instruction tuning with special token. Though studying an interesting topic, the paper still has multiple drawbacks.

### Strengths
It is interesting to study the loss of context-awareness for instruction-tuned LLMs with chat templates.

### Weaknesses
1. I am not convinced about the phenomenon of loss of context awareness for instruction-tuned LLMs with chat templates. Fig. 3 shows attention weight allocation in which a part of the attention is allocated to chat template tokens. However, these format tokens serve to indicate dialogue roles or separate dialogue turns. It is not straightforward to claim the allocation of attention weights to chat template tokens would cause the loss of context awareness. The attention shifts observed in Fig. 3 are relatively small, typically within 10%, and it's unclear if such minor shifts significantly impact performance. Furthermore, the paper does not provide a clear definition of 'context awareness' making it difficult to evaluate the claim.

2. It is not well motivated that the proposed two methods would serve to mitigate the claimed loss of context awareness. I suspect the post-hoc attention steering would be beneficial since the model is further optimized through instruction finetuning. Furthermore, it is unclear why prepending a special token as the indicator to user instruction for instruction tuning would mitigate loss of context awareness. The paper lacks a theoretical justification for why these methods should be effective, and the connection between the proposed methods and the claimed loss of context awareness is weak.

3. In Table 2, the best performance with alpha=1.0 for multiple scenarios, and the minor difference between alpha=1.0 and alpha=0.9 seem to indicate the post-hoc performance is ineffective to mitigate the claimed loss of context awareness. The fact that alpha=1.0 often performs best suggests that the attention steering is not beneficial and may even be detrimental, further weakening the claim of context-awareness loss.

4. In Table 3, the improvements with indicator for popular public benchmarks like SQuAD, QuAC, DROP, and MT-Bench seem very small. These results strengthens my concerns on the effectiveness of prepending the special token for mitigating the loss of context awareness. The performance gains on standard benchmarks are marginal, suggesting that the proposed methods do not significantly address the claimed issue. The paper does not provide a clear explanation for why the improvements are so small on these benchmarks.

### Questions
None.

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
3

### Summary
This paper examines how supervised fine-tuning (SFT) for instruction-following can reduce context awareness in large language models (LLMs). The authors identify a bias from the chat template as a key factor, which shifts focus away from user-provided context. They propose two methods—post-hoc attention steering and conditional instruction fine-tuning with a context-dependency indicator—to counteract this loss. Experiments show these methods effectively restore context awareness without impacting instruction-following ability. The study highlights the importance of benchmarking context awareness post fine-tuning.

### Strengths
1. The paper tackles an important topic in LLMs, examining the impact of applying chat templates to inputs during fine-tuning.

2. The paper proposes  both training-free and fine-tuning method to address this issue, evaluated on a range of LLMs and datasets.

### Weaknesses
1. The concept of "loss of context-awareness" remains somewhat unclear. Based on the description, it appears related to the contextual reasoning capabilities of LLMs. Section 3.1 illustrates this phenomenon using a chat template in Llama. Does this issue persist across different models and templates? There is a brief discussion in lines 197-199, but no further details are provided. Specifically, the paper does not provide a clear, quantifiable definition of context-awareness, making it difficult to assess the extent of the problem and the effectiveness of the proposed solutions. The examples provided are limited, and it's unclear how the observed behavior generalizes beyond the specific scenarios presented. A more rigorous definition, perhaps tied to specific metrics or benchmarks, would significantly strengthen the paper.

2. Typo in line 144: “[Optional User template] and [Optional User template] are user and assistant role indicators used.” The second “Optional” should be “Assistant.”

3. Error bars are not reported in the experimental results, such as in Table 2 and Table 3. This absence makes it difficult to assess the statistical significance of the results and the reliability of the conclusions. Without error bars, it is impossible to determine whether the observed differences between methods are due to actual improvements or simply random variation.

4. The experiments are conducted on a limited scope, specifically small-sized Llama models with Q-LoRA. It remains unclear whether the findings would generalize to a broader range of models. The use of only Q-LoRA for fine-tuning further limits the scope of the study. The paper should investigate whether the observed context-awareness issues and the effectiveness of the proposed solutions hold true for different fine-tuning methods and model architectures.

### Questions
1. The code has not been provided; how can readers reproduce the results?

2. Could you clarify the concept of "loss of context-awareness" with a more precise definition, illustrative examples, empirical findings, and evaluation metrics?

3. Given the limited time for rebuttal, would it be possible to expand your experiments to a broader scope to strengthen the robustness of the conclusions?

### Soundness
2

### Presentation
2

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
This work investigates that the context-awareness ability of instruction fine-tuning models decreases because the attention weight assigned to user prompts decreases when a chat template is added. Based on this observation, they propose an inference-time technique that manually intervening attention scores during response generation. In addition, they also propose a training-time technique that utilizes conditional indicators to further mitigate the loss of context awareness of pretrained language models when instruction-tuning.

### Strengths
1. The study on the context-awareness ability of instruction fine-tuned models will decrease is novel. and the observation that the attention weight assigned to user prompts decreases when a chat template is added is interesting and insightful.
2. The proposed  inference-time technique and training-time technique may contribute to the area of instruction fine-tuning.

### Weaknesses
The observation that the loss of context awareness after instruction tuning has only been experimented on small LLMs (e.g., llama 7B and 8B), and the models used in the experiment section are also small LLMs equal to or smaller than 8B. Therefore, I do not know whether the loss of context awareness after instruction tuning is a general phenomenon or only occurs on small LLMs, what about the 13B, 70B, and larger models? It is well known that bigger LLMs are more capable than smaller LLMs, whether this phenomenon holds or not is not known, so the study of bigger LLMs is very important for the contribution of this paper to be significant or not.

### Questions
Refer to the "Weaknesses".

The observation that the loss of context awareness after instruction tuning has only been experimented on small LLMs, what about the 13B, 70B, and other larger models? This is a limitation of this paper, so:

1. Specific experiments with larger models (e.g., 13B, 70B) that would help validate if the phenomenon generalizes.
2. Explicitly acknowledge this limitation in the paper. Discuss potential implications or hypotheses for how the findings may or may not generalize to larger models.
3. Propose a discussion on how the capabilities of larger language models might interact with or influence the observed loss of context awareness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of lower context awareness ability in instruction-tuned LLMs. The authors first conduct the needle-in-a-haystack (NIH) test on pre-trained and instruction-tuned LLMs to demonstrate the problem and then attribute this issue to the overemphasis on chatting templates by analyzing the distributions of attention activations. They further propose two strategies to enhance the ability to understand context during runtime or training time.

### Strengths
1. This paper conducts experiments on various LLMs from diverse model families.
2. Exploring the weaknesses of instruction-tuned LLMs is good.

### Weaknesses
1. The motivation of this work is unclear. As the goal of SFT is to achieve a _helpful_ chatbot, why do we have to care about their poorer context awareness? For example, in Table 3, we can find that a model with better context-awareness performance (i.e., NIH/SQuAD, QuAC, DROP) doesn't necessarily lead to a better instruction-following ability (i.e., MT-Bench). Also, in the NIH example of Figure 1, even though an instruction-tuned LLM cannot provide exactly the same suggestion from the user inputs at the first run, it doesn't necessarily mean that this instruction-tuned LLM lost its ability to retrieve knowledge from the context because it could be the instruction-tuned LLM fail to follow your first instruction that "answer question based on the given paragraph", or even could be the model feels that the target retrieved sentence is not helpful enough. A more comprehensive study on this phenomenon, at least, should provide diverse prompts that emphasize the idea of "answer questions based on the given paragraph" in different levels, and the instruction-tuned LLM _constantly_ fails to retrieve the target sentence.

2. The claim that poor context awareness can be attributed to the chat template is not supported. Firstly, attention weights may not faithfully express LLMs behaviors [1], especially in the cases where Transformers has skip-connect architecture. Secondly, even though I accept attention weight as a tool, the authors didn't set up a baseline to define when an attention weight is "high" and when it should be considered "low." Since we have formatted the user prompts with templates (meaning that the template is used), some attention weights have been allocated to the template part, which is reasonable. So, at least, we need to define a quantifier to measure the significant levels of attention weights. Specifically on Figure 3 (left), I feel the orange bar (User part) on Raw is almost equivalent high to that of Templated. Thirdly, the authors only cherry-pick one self-attention head from a model to conclude their findings, which is not reliable. Finally, instruction-tuned models pay some attention to the chat template, which is intuitive as they are trained on the data with the template; I cannot see any logical connection between the templates and the context awareness (I mean, I cannot prove/derive any connection between these two phenomenons, so they could be correlated, but may not be causally).

3. The authors didn't report the general instruction-following performance (i.e., MT-Bench) with the attention intervention strategies. So, we are unsure whether this strategy will hurt the generalizability of instruction-tuned models.

4. Some of the improvements shown in Table 3 are not significant. For example, QuAC of UltraChat on Llama-2 (0.154 --> 0.157), SQuAD of WizardLM on Llama-2 (0.8229 -> 0.8260) on Llama-3 (0.8765 -> 0.8792), and so on.

Overall, I am not satisfied with the proposed methods' motivations, main findings, and effectiveness of the proposed methods.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1
