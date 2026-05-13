# LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Current long context large language models (LLMs) can process inputs up to 100,000 tokens, yet struggle to generate outputs exceeding even a modest length of 2,000 words.
Through controlled experiments, we find that the model's effective generation length is inherently bounded by the sample it has seen during supervised fine-tuning (SFT).
In other words, their output limitation is due to the scarcity of long-output examples in existing SFT datasets.
To address this, we introduce AgentWrite, an agent-based pipeline that decomposes ultra-long generation tasks into subtasks, enabling off-the-shelf LLMs to generate coherent outputs exceeding 20,000 words. 
Leveraging AgentWrite, we construct LongWriter-6k, a dataset containing 6,000 SFT data with output lengths ranging from 2k to 32k words. 
By incorporating this dataset into model training, we successfully scale the output length of existing models to over 10,000 words while maintaining output quality.
We also develop LongBench-Write, a comprehensive benchmark for evaluating ultra-long generation capabilities. Our 9B parameter model, further improved through DPO, achieves state-of-the-art performance on this benchmark, surpassing even much larger proprietary models.
In general, our work demonstrates that existing long context LLM already possesses the potential for a larger output window--all you need is data with extended output during model alignment to unlock this capability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of long-form generation for large language models (LLMs). The authors find correlation between the output length limitation of current LLMs and the scarcity of long-output examples in existing supervised fine-tuning datasets. As a remedy, they generate long-output texts by decomposing ultra-long generation (over 10k words)  tasks into subtasks and prompt LLMs for each subtask, and then fine-tune LLMs with the long output. Preference tuning with DPO is also applied. They measure the required output length and the quality of long-form generation judged by GPT-4 as the main metrics. As a result they can enable a 9B/8B parameter model to generate very long sequences over 10k words.

Essentially, the paper focuses on data augmentation for fine-tuning LLMs to a specific problem, which is long-form generation to tens of thousands of words. The idea is straightforward to mix in training examples of ultra-long sequences from 2k to 32k words so that the model generation does not stop after around 2k words.

### Strengths
- The focus of the paper is very clear. The paper presents very logical steps around the core idea of enabling LLMs to generate very long sequences. This makes the paper easy to understand (although I feel there might be too many closely related but different names such as LongWrite-Ruler, LongBench-Write, etc. that are a bit confusing).

- The empirical results of demonstrating current LLMs’ cap at around 2k output words provide interesting insights. And connecting it back to the training data distribution is very reasonable leading to the data augmentation used in the paper.

- The data generation pipeline, AgentWrite, is useful for generating long sequences based on instructions. The experimental results are promising, showcasing mixing in long-output sequences can enable the model to generate longer outputs.

### Weaknesses
 - The novelty of the paper is somewhat limited. I like the idea of enabling the model to generate ultra-long sequences, but essentially it boils down to adjusting the training data length distribution to be better correlated with the testing scenario. Model behaviors are following what models are being trained on, so data augmentation or adjusting training data distribution is always a basic solution.

- The evaluation of ultra-long generation quality is less satisfactory, as it mainly relies on GPT-4. No variance of the LLM-based evaluation is provided, making it a bit hard to gauge the performance differences. From Table 3, it seems the generation quality under this metric is not improved with LongWriter, and the main improvement is on the model becoming able to generate longer sequences, which is not surprising since that was mixed in the training data (e.g. having training examples with end-of-generation token after 10k words instead of 2k).

- Following the above point on long-form generation quality evaluation, there is not enough details provided for the human evaluation in Figure 9 either. Long-form generation is very hard to evaluate, even for humans for texts over 10k words. How can we guarantee that the GPT-4 and human evaluations are trustworthy?

- There are certain baselines lacking for comprehensively comparing long-form generation, compromising the experimental claims. For example, direct comparisons with AgentWrite + other models, which can be a strong baseline with good quality indicated from results in Table 3. Also, for the NLL loss comparison, no baseline models were compared with.

- Efficiency is another concern, which was also mentioned in the conclusion. The paper could discuss more efficiency details such as computational cost, although this might be an orthogonal direction.

### Questions
1. Line 194: “we collect 120 varied user writing prompts”: how did you collect? 

2. Line 254: “we see that AgentWrite does not compromise the quality of the output while expanding its length”: the scores do drop when the length is expanding in Table 2 right?

3. In Table 3, it seems the quality score judged by GPT-4 does drop compared to other models such as GPT-4o and GLM-4-9B-chat. The main increase of scores for LongWriter come from respecting the required output length. This makes the argument of both length and quality a bit compromised. If users want to generate long output of good quality, it seems AgentWrite is already good or even better.

4. In the paragraph lines 398-409, for NLL comparison, could you compare with other models to see how they score the long generations to make this metric more justifiable? 

5. In the ablation study in section 4.3.2, it mentions in lines 476-480 that “taching the model to first output its reasoning process before generating the writing content does not significantly improve task performance…” As I understand this claim is made solely with the GPT-4 evaluation, could there be a problem with the evaluation metric? In fact, I am wondering if the authors have more comments on how to evaluate ultra-long-form generations reliably.


6. Typo: Line 189: “(Introduced in Sec)”

7. Table 4: the green and red colors are not very friendly for accessibility reasons.

### Soundness
2

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
4

### Summary
The paper addresses a very crucial gap in LLM research of overcoming limitations regarding long form output token limits. The paper investigates the root cause for this limitation in a systematic manner and also comes up with a clever solution to augment LLM solutions to 2k+ token limits. An elaborate evaluation and scoring strategy - that takes into account both the number of tokens generated and the quality of those tokens - has been described, along with DPO alignment and intuitive ablation studies.

### Strengths
1. The paper presents a systematic approach towards investigating the reason behind limitations around long generations in LLMs. 
2. The proposed agentic pipeline is pretty intuitive and seems to solve the issue very effectively.
3. Extensive validation checks and comparison of SOTA models against the finetuned models has been provided.
4. Good work with seeing the lift provided by DPO alignment and further ablation studies to strengthen the hypothesis.

### Weaknesses
1. Need for Human Eval to assess AgentWrite quality - While the paper proposes AgentWrite for generating long-form content, the validation of output quality is primarily based on automatic metrics using GPT-4o as a judge. More rigorous human evaluation would strengthen the quality assessment.
2. Dependency on proprietary models - The AgentWrite pipeline relies on GPT-4o for generating training data, which makes the approach dependent on proprietary models and potentially difficult to reproduce. Analysis and comparison with an open-sourced version of AgentWrite would be helpful to understand how scalable and adaptable the pipeline is.
3. Need for Plan validation in Step 1 : The "Plan" phase of the pipeline comes up with the various subtasks needed for the instruction. There needs to be a validation step to assess the quality and relevance of the subtasks being generated in the first place. The "quality metric" defined later would not take this into account.
4. More elaboration needed on the controlled experiment on Section 2 : this subsection mentions using GLM-4-9b as the base model and then its further finetuned with a subset of GLM-4’s chat SFT data. Has the model not been fine-tuned on this data already? Wouldn't it just overfit on the specific data subset again and that might be the reason why the model performed better when you add longer output length instances in the sft data (due to iterative finetuning on the same instances)? This would nullify the hypothesis that the model’s output limit is due to insufficient output length in the SFT data.

### Questions
1. How did you determine the optimal paragraph length range (200-1000 words) for AgentWrite? Were other ranges tested?
2. Is there a theoretical upper limit to how much the output length can be scaled using your approach?
3. Could you elaborate more on what motivated the choice of using token-level loss averaging instead of sequence-level averaging during training?
4. Does the quality of generation degrade differently for different types of content (e.g., technical vs creative writing)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the limitation of current long context large language models (LLMs) in generating lengthy outputs despite their capacity to process extensive inputs. The authors identify the primary constraint as the scarcity of long-output examples in supervised fine-tuning (SFT) datasets. To overcome this, they introduce AgentWrite, an agent-based pipeline that decomposes ultra-long generation tasks into subtasks, enabling LLMs to produce coherent long outputs. They construct the LongWriter-6k dataset, containing 6,000 SFT data points with output lengths from 2k to 32k words, and incorporate it into model training, successfully scaling output length to over 10,000 words while maintaining quality. Additionally, they develop LongBench-Write, a benchmark for evaluating ultra-long generation capabilities, demonstrating their 9B parameter model's state-of-the-art performance.

### Strengths
1. The paper is written clearly, making it easy to understand.
2. This paper focuses on the very practical issue of model output length limitations and provides a systematic research approach.

### Weaknesses
I believe there's room for improvement in the experimental aspect.
1. Is it possible to directly leverage AgentWrite to generate long responses with the target model, e.g., Llama-3.1-8B? Can it meet our requirements for output length and quality? Can the output be used to train the model? I think only having results from GPT4-o is not sufficient to demonstrate the effectiveness of AgentWrite. The core issue is whether AgentWrite is truly model-agnostic and can be effectively applied to other models besides GPT-4o, especially open-source models with varying architectures and capabilities. The paper should include a more thorough evaluation of AgentWrite's performance across different model families, not just a single closed-source model.
2. As shown in Table 3, the performance of LongWriter-9B (w/ and w/o DPO) and LongWriter-8B is worse than the original model in the [0, 500) subset, and the performance of LongWriter-9B is also worse in the [500, 2k) subset. Given that only "over 1%" of user prompts require such lengthy outputs, is it worth sacrificing performance on shorter texts? Furthermore, to me, LONGWRITER seems to be essentially about adjusting the model's generation behaviors with longer data plus using GPT4-o for knowledge distillation. The improvement in long-text generation quality through knowledge distillation seems trivial, and changing the model's generation behaviors in this way does not seem to be a good way to enhance the model's fundamental capabilities, as demonstrated by the declined performance on shorter outputs. The concern is that the method might be overfitting to long-text generation, potentially at the expense of overall model performance on more common shorter text generation tasks. This raises questions about the generalizability of the approach and its practical utility for real-world applications where diverse text lengths are expected.

Missing reference: Line 189, "Sec"

### Questions
1. If we directly set min_new_tokens = max_new_tokens = target length during generation, how would the quality of output from various models be affected?
2. I have doubts about LongWrite-Ruler: the current prompts provided are too vague. If we provide more detailed prompts, will the model generate longer outputs (also with higher quality)? For now, it feels like an assessment of the model's capability to follow instructions in generating outputs of a certain length. Also, as shown in Table 2, even after training the model with longer texts, the model's output still largely fails to meet the required length, which seems to confirm that the model lacks this instruction-following ability, rather than being incapable of generating the required output.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The SOTA LLMs can support the input lenght up to million tokens. However, their output length is limited to a few thousand, which greatly constrains their application in many areas. This work first investigates the reason of such limitation and found that the main reason is because the SFT training sample lenghts are limited. To address this issue, this work introduces an agentic pipleine, AgentWrite, that can generate long output responses by decomposing long generation tasks into subtasks. By using the data generated by this pipeline to train SFT LLMs, the trained LLMs are able to generate responses over 10,000 words while maintaining output quality.
The main contributaions of this work include the following:
1. Analyze and identify the primary reason limiting the output lenght of LLMs.
2. It proposes an agentic framework to construct SFT samples with long output lengths. It also contributes the LongWriter-6k dataset.
3. The empirical results show that the proposed approach is able to scale the current LLMs output lenght to up to 10,000 words.

### Strengths
1. This work studies an interesting question of LLM output length limitation, compared to othere works that focus on input lenght. It investigates and finds the reason why output lenght is limited for current LLMs. Specifically, the output lenght is mainly limited by the output length of the SFT training samples.
2. Besides finding the reason of model response lenght limitation, this work also proposes the AgentWrite approach for generating long response SFT data. LLMs trained with this dataset is able to scale its output lenght. The empirical results also show its efficacy.
3. The experiments involves 4 proprietary and 5 open-source models, which makes the conclusions/results of the experiments more convincing.

### Weaknesses
 1. This work studies an interesting question of LLM output length limitation, compared to othere works that focus on input lenght. It investigates and finds the reason why output lenght is limited for current LLMs. Specifically, the output lenght is mainly limited by the output length of the SFT training samples.
2. Besides finding the reason of model response lenght limitation, this work also proposes the AgentWrite approach for generating long response SFT data. LLMs trained with this dataset is able to scale its output lenght. The empirical results also show its efficacy.
3. The experiments involves 4 proprietary and 5 open-source models, which makes the conclusions/results of the experiments more convincing.

### weaknesses:
 1. This work including experiments focsuses on only one task, i.e., writing. However, it's not clear how generalizable this approach is to other areas such as coding, which usualy has long output length, especially for large coding projects. Conducting experiments on more tasks can make the proposed approach more compelling.
2. The related work section doesn't mention if there's any exsiting work on this topic. If yes, they should be used as baseline. If no, it should be mentioned explicitly.

### Questions
Please see the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
