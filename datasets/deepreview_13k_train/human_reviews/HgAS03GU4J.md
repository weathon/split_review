# Inference-time Alignment of LLMs at the Token Level

- Decision: Reject
- Scores: 6, 5, 6, 8, 5

## Abstract
Large language models (LLMs) require alignment—such as instruction-tuning or reinforcement learning from human feedback—to effectively and safely follow user instructions. This process necessitates training aligned versions for every model size in each model family, resulting in significant computational overhead. In this work, we propose nudging, a simple, plug-and-play, and training-free algorithm that aligns any base model at inference time using a small aligned model. Nudging is motivated by recent findings that alignment primarily alters the model’s behavior on a small subset of stylistic tokens, such as "Sure" or "Thank". We find that base models are significantly more uncertain when generating these tokens. Leveraging this observation, nudging employs a small aligned model to generate nudging tokens to steer the large base model's output toward desired directions when the base model's uncertainty is high. We evaluate the effectiveness of nudging across 3 model families and 13 tasks, covering reasoning, general knowledge, instruction following, and safety benchmarks. Without any additional training, nudging a large base model with a 7× - 14× smaller aligned model achieves zero-shot performance comparable to, and sometimes surpassing, that of large aligned models. For example, nudging OLMo-7b with OLMo-1b-instruct—affecting less than 9% of tokens—achieves a 10% absolute improvement on GSM8K over OLMo-7b-instruct. Unlike prior inference-time tuning methods, nudging enables off-the-shelf collaboration between model families. For instance, nudging Gemma-2-27b with Llama-2-7b-chat outperforms Llama-2-70b-chat on various tasks. Overall, this work introduces a simple yet powerful approach to token-level model collaboration, offering a modular solution to LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes NUDGING, an innovative approach for aligning base models at inference time without any additional training. NUDGING is a training-free method that leverages a smaller, pre-aligned nudging model to guide the base model’s output on uncertain tokens, making it an efficient alternative to traditional alignment methods. This approach not only maintains strong alignment but also significantly reduces the computational costs associated with training large models for alignment, thereby improving their practical applicability across diverse tasks.

### Strengths
1. This paper presents an innovative method, NUDGING, which introduces a novel, training-free approach for aligning base models at inference time. Unlike traditional alignment methods that require fine-tuning across each base model,  NUDGING leverages a small aligned model to "nudge" a larger, unaligned base model by intervening selectively when the base model displays uncertainty. The proposed method does not require any additional training.
2. This paper conducts comprehensive evaluations across multiple model families and a diverse range of tasks, demonstrating that NUDGING achieves comparable or even superior zero-shot performance relative to fully aligned large models, all without additional training. 
3. This paper is clear and well-organized, effectively guiding readers through the motivation, design, and implementation of NUDGING.

### Weaknesses
1. Although the authors conduct comprehensive experiments across different model families, I am curious about the effect on llama3. We know that the performance of llama3-instruct is great, so how does NUDGING compare with it? Specifically, it would be beneficial to see a direct comparison of NUDGING applied to Llama 3 base models against the performance of the Llama 3 instruct-tuned models, particularly on tasks where instruction-tuned models excel, such as complex reasoning and multi-turn dialogues. This comparison would help clarify the practical benefits of NUDGING when a strong instruction-tuned model is already available.

2. The authors use a fixed uncertainty threshold γ to trigger intervention based on the uncertainty of the underlying model. Although an ablation study was done to demonstrate the choice of threshold, is it possible to have an adaptive threshold? This is just a question and does not affect my judgment on this paper contribution. It would be interesting to explore methods for dynamically adjusting this threshold based on the context of the input or the specific task, potentially using metrics like the entropy of the base model's output distribution. Such an adaptive approach could lead to more efficient interventions, reducing unnecessary nudging when the base model is already confident.

3. NUDGING’s design requires multiple back-and-forth interactions between the base and nudging models, which adds latency to the inference process, especially for tasks requiring quick response times. Wondering if the author has a way to avoid this? The iterative nature of the nudging process, with its repeated queries and responses between the base and nudging models, introduces a significant overhead. This latency could be a major bottleneck in real-time applications, and it would be beneficial to see a more detailed analysis of this overhead and potential mitigation strategies, such as parallel processing or more efficient communication protocols between the models.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
The authors propose a method called Nudging, which aims to align large language models (LLMs) during inference without any additional training. Instead of retraining large models for alignment, they use a smaller, aligned model to guide the base model by injecting "nudging tokens" whenever the base model is uncertain about what to generate next. The authors also evaluate Nudging across three model families—Llama-2, Gemma-2, and OLMo—on a set of 13 tasks, including reasoning, general knowledge, instruction following, and safety benchmarks.

### Strengths
- The idea of leveraging a small aligned model to steer a larger base model in real-time is  an area that worth studying (e.g., speculative decoding). This paper starts from another perspective and uses the effect of the small model steer model when the model confidence is relatively low. Although some might say the method is very simple, I think it is novel.

- The authors tested Nudging across three different model families (Llama-2, Gemma-2, and OLMo) and 13 diverse tasks. In many cases, Nudging's performance matched or even surpassed that of fully aligned large models, which is good given that no additional training was involved.

- The authors perform analysis in nudging's performances and behaviors both in Section 2 & 4 & 5, which is informative. However, the authors fail to analyze the scenarios that nudging won't work well.

### Weaknesses
 - Nudging relies on the base model’s uncertainty estimates to decide when to intervene. If the base models themselfe are strong, the effectiveness will decrease (e.g., the results of Gemma 2). Specifically, the method's reliance on uncertainty as a trigger for intervention means that for highly confident and capable base models, the nudging mechanism may not activate frequently enough to provide a substantial benefit. This is particularly concerning as base models continue to improve in performance and confidence, potentially diminishing the applicability of this method.

- I don't quite understand the specific practical scenarios for using nudging. In what situations do we need to use nudging, considering that most practical models are already well-aligned, and we will continue to get increasingly powerful base and aligned models? If I'm not mistaken, the improvement nudging offers for well-aligned models shouldn't be very significant. The paper does not clearly articulate the niche applications where nudging would be preferred over direct use of a well-aligned model, especially given the overhead of maintaining and querying a separate nudging model. The lack of a clear use case makes it difficult to assess the practical value of this approach.

- The benchmarks selected in the paper are not very challenging these days, and it is kind of weird that the Gemma 2 model performs poorly on the CF task. How will the nudging method perform if we use more challenging benchmarks? The choice of benchmarks, while standard, does not fully capture the complexities of real-world tasks. The poor performance of Gemma 2 on the CF task raises concerns about the robustness of the method across different model architectures and tasks. The paper would benefit from an evaluation on more complex and nuanced benchmarks to better understand the limitations and generalizability of nudging.

### Questions
- Does this method conflict with other methods that enhance performance during the inference stage, such as Chain of Thought and Speculative Decoding?

- The paper focuses primarily on standard benchmarks with shorter completions. It would be interesting to see how well Nudging scales to tasks like essay writing, story generation, or extended dialogue, where maintaining alignment over longer contexts becomes more challenging.

### Soundness
3

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
The paper presents a method to align a large base LLM at inference time with the help of a small aligned LLM. Based on the observation that base LLMs are uncertain when generating alignment-related tokens, the authors propose injecting token(s) generated by a small aligned LLM when top-1 token probability assigned by the large base LLM is less than some threshold. The effectiveness of this method is demonstrated on 3 model families and several diverse tasks, across which “nudging” is shown to be comparable to, or sometimes better than, a large aligned LLM.

### Strengths
- This paper proposes a simple and intuitive approach for inference-time alignment significantly reducing the computation burden required to align a family of base LLMs.

- The authors provide strong and clear motivation for their approach in section 2, demonstrating experimentally where and when to inject nudging tokens.

- Extensive evaluation and analysis on standard and alignment-related benchmarks are easy to follow and demonstrate the effectiveness of the proposed approach. Additional experimentation, particularly the section on scaling, provide great insight.

### Weaknesses
 - The topic of computational efficiency is not sufficiently addressed. For one, in table 2, it’s misleading to compare the number of calls to the large base models when each call with nudging generates significantly more tokens (16 vs 1 token) relative to the comparison methods. Moreover, no analysis is provided regarding the frequency at which tokens generated by the large aligned model in each call are discarded due to injecting the nudged token(s), but this analysis is crucial to understand the computational implications of this approach. The high ratio of discarded tokens, combined with the need to reprocess the full input for each API call, suggests that the method's efficiency over API is questionable without significant caching mechanisms. A more thorough analysis of the computational overhead, including the cost of discarding tokens and reprocessing the input, is needed.

- The results on standard benchmarks (section 4.2) suggest that nudging underperforms the large aligned model on most datasets. The slight increase in average performance of nudging seems primarily due to performance increases on a few toy tasks (e.g., coin flip, last letter concatenation). The performance gains on these tasks are not representative of overall performance improvements, and the method's effectiveness on more complex benchmarks is not well-established.

- Section 4.4 on the collaboration of models from different families is hard to follow and underdeveloped. For one, the results reported in table 6 don’t match those in table 3 (e.g., Gemma-2-27b scoring 16.5 vs 17.7 on MMLU). Moreover, it’s strange that Gemma-2-27b-it results and Gemma-2-27b nudged by Gemma-2-2b-it are not included in table 6, but it seems like nudging Gemma-2-27b with OLMo-7b-it and Llama-2-7b-chat can significantly underperform (e.g., Gemma-2-27b nudged by Gemma-2-2b-it scores 75.6 on GMS8K while nudging with OLMo-7b-it and Llama-2-7b-chat score only 41.0 and 65.0 respectively) despite Gemma-2-2b-it being a much smaller mode (2b vs 7b). The lack of clarity in this section, combined with the inconsistencies in results, makes it difficult to draw meaningful conclusions about the cross-family collaboration of models.

### Questions
- On average, of the 16 tokens generated in each call to the large base model, how many are discarded? Why is the generation length chosen as 16 for both the small aligned model and large base model? Can you comment on the effect of the generation length on computational efficiency? If you’re able to cache prefixes/intermediate generations at each step, why not use a generation length of 1 for the large base model and avoid discarding tokens? 

- Can you provide intuition for why certain tasks (e.g., coin flip, last letter concatenation) benefit so significantly by nudging relative to the other tasks?  Why do models from the OLMo family perform so poorly on last letter concatenation? 

- Are results in table 6 reported on smaller samples of GSM8K and MMLU than table 2? Can you provide some insight into why nudging Gemma-2-27b with OLMo-7b-it and Llama-2-7b-chat underperforms nudging Gemma-2-27b with Gemma-2-2b-it? Is Gemma-2-2b-it a strong model, or is some underlying distributional shift between model families to blame?

- In section 4.3, it’s said that “nudging Llama-2-70b-chat with Llama-2-7b-chat is rated slightly higher than even in helpfulness and engagement over Llama-2-7b-chat, even though over 85% of the tokens are from the base model”. What is the point of nudging one aligned model with another aligned model? What’s the takeaway from this experiment? Why is it interesting that Llama-2-70b-chat nudged by Llama-2-7b-chat is rated higher than Llama-2-7b-chat?

- Can you comment on the interoperability of nudging with non-greedy sampling techniques (e.g., temperature > 0) which are commonly the default for larger aligned models (e.g., GPT-4)?

- In line 6 of Algorithm 1, shouldn’t the operator be flipped i.e., $\text{top-1}(f_B(q, a, c_{<i}^B)) < \gamma$ instead of $\text{top-1}(f_B(q, a, c_{<i}^B)) > \gamma$?

I am willing to raise my score if my questions/concerns are adequately addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work introduces an algorithm, _nudging_, that allows for aligned generation with a large base unaligned model and a small aligned one, without any additional training. It works by inserting tokens from the small aligned model at positions where the base model is uncertain (probability for the top-1 token is below a predefined threshold), with the remaining tokens being generated by the base model.

The algorithm leads to improvements on downstream tasks when compared to results of the large base model without nudging, approaching results of the aligned version of the large model, and in some cases outperforming it.

The method allows for combination of models from different model families, which differentiates it from other training-free, inference-time alignment methods.

### Strengths
The work presents a novel approach for training-free inference-time alignment. The method shows strong empirical results, with performance improvements over the base model and sometimes exceeding the aligned version. It provides a clear and intuitive algorithm that is easy to understand and implement and enables cross-family model collaboration. The approach has significant potential impact, possibly offering an alternative to standard instruction tuning approaches.

### Weaknesses
I don't see any major issues with the paper, there are only a few minor ones related to presentation, mentioned in the the _Questions_ rubric (see the _suggestions_).

### Questions
Question:
- Line 224, "_This leads to better performance and facilitates better collaboration between model families with different tokenizers._" - What is the difference in performance?

Suggestions:
- Line 353: The difference should be expressed in percentage points (pp) rather than %.
- Figure 4: The lines are difficult to read without extreme zooming. Consider using solid lines and rescaling the plot for better readability.
- Line 499: Shouldn't "unturned small models" be "untuned small models"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
LLMs are instruction tuned to align them: to better follow user instructions, safety, improve reasoning, etc. In this paper, the authors propose a training free instruction fine tuning approach, where they modify the output sequence of a large base model (not aligned), using the output sequence of a small instruction tuned model, to align the big model. Specifically, whenever the distributions of the small and the big model do not match, they append the big model’s output with the nudging token i.e. the token as per the small aligned model. The empirical results and quite good and convincing, and the approach is definitely novel to the best of my knowledge. However, the paper misses a discussion on key limitations of the proposed approach and a proper discussion and providing intuition behind various sections critical to the functioning of the proposed approach.

### Strengths
- Quite an interesting idea and approach, with clean and convincing results. 
- Empirical results are done on both standard and safely alignment benchmarks.

### Weaknesses
 - Many task capabilities come with scale (emergence https://arxiv.org/abs/2206.07682). I fail to understand how the partial completion (generated by the bigger model) when fed to the smaller instruction tuned model would be comprehended in these cases. Can authors test their approach on some of these tasks, with emergence properties (i.e. performance is 0 below a param size, and jumps suddenly at a bigger scale)? 
- I fail to understand the argument in L191, i.e. the distribution at alignment related positions is the same in models of different sizes. Aligned models of different sizes, at same numerical position (say the 2nd position where the score is below threshold), might be producing totally different outputs (e.g., small model might be towards the end of solution, bigger model might just be at the start). I fail to understand that the steering tokens generated at these positions are the same or have the desired effect on the big model. 
- Lack of discussion on limitations of the approach: This approach inherently assumes that all the mis-alignment occurs at the token level, and does not add a discussion or a section of limitations. For example, the approach won’t work when the misalignment is due to lack of long  context dependencies or sub-sentence contradictions (which is fine t0 have). Would be great if authors can address the same.
- I am not sure about how much this approach will be used in practice. LLM instruction finetuning is not a very costly process (for folks who pretrained a model). If someone in practice really wants a reliable instruction tuned model, with specific capabilities, I doubt they will use this training free approach. For example, one cannot really “safety align” a model using this approach, as it will be quite easy to break, by attacking the small instruction tuned model to mimic distribution of big base model, etc.
- I would really encourage the authors to spend a page or so in their next version, on practical implications/usecases/discussion of their approach. How can this approach guide better instruction tuning or other insights the authors might have.
- Finally, the ICLR author guidelines require an ethics statement and a reproducibility statement. I would encourage the authors to follow the guidelines (I WILL NOT be considering this for my score though, just pointing it out).

### Questions
See the weakness section.
Overall, I would recommend the authors that in such papers, where you are proposing a “supposedly” counterintuitive algorithms, focusing on discussion/providing intuition into the results is crucial, and could really improve the work. 
I would be willing to increase the score, if authors clarify the intuition/address the questions I posed above (mainly related to why L191, task capabilities).

### Soundness
3

### Presentation
2

### Contribution
2
