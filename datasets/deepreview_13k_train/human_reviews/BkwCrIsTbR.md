# Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models (LLMs) struggle with long-context reasoning, not only due to the quadratic scaling of computational complexity with sequence length but also because of the scarcity and expense of annotating long-context data. There has been barely any open-source work that systematically ablates long-context data, nor is there any openly available instruction tuning dataset with contexts surpassing 100K tokens. To bridge this gap, we introduce a novel post-training synthetic data generation strategy designed to efficiently extend the context window of LLMs while preserving their general task performance. Our approach scalably extends to arbitrarily long context lengths, unconstrained by the length of available real-world data, which effectively addresses the scarcity of raw long-context data. 
Through a step-by-step rotary position embedding (RoPE) scaling training strategy, we demonstrate that our model, with a context length of up to 1M tokens, performs well on the RULER benchmark and InfiniteBench and maintains robust performance on general language tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel post training synthetic data generation strategy for long context.  The approach works by splitting a long context document into smaller documents and generating question-answer pairs from separate smaller documents as well as combinations of the documents.  The generated data is used in combination with a step-by-step rotary position embedding scaling strategy to scale the model context.  The proposed approach is tested in several benchmarks for longer context and overall results appear higher for the proposed finetuning.

### Strengths
- The paper makes contributions to improving long context reasoning of LLMs. The exploration of algorithms and fine-tuning strategies for increasing the context length is an important problem for language models and finetuning on synthetic data appears to be a promising direction for this work
- The proposed method appears simple to implement and should be reproducible as many of the proposed prompts are provided in the appendix, and the training strategy is similar given the generated data.

### Weaknesses
 - A main concern with the proposed work is that for many of the results (e.g. Table 1, 5) the improvements appear to primarily come from a single task Retrieve.KV.  Improvements on the other datasets are smaller.  While this leads to an overall increase, it's important to understand the importance of this subtask rather than simply the reported overall average increase. 
- The scale of the datasets in experiments is rather small and there are no uncertainty estimates provided.  This is important particularly as for some of the tasks, there is only 100-200 samples, where a few correct answers can increase.  I would encourage the authors where possible to increase the amount of evaluation data.
- The authors only test a larger model for generating the synthetic data.  The method would further be justified by including comparisons for models of the same size that are used to generate the data as it is unclear the dependency on model size.  Further the experiments are only done for the Llama-8B model, but experiments on other models even smaller would be beneficial to see whether smaller or larger models benefit more from increasing context length.
- there is some confusing wording in the paper that the authors should clarify particularly around Section 3.2 Authors could do a better job clarifying what are $N_1$, $N_2$ and $N_3$.

### Questions
- What is the Retrieve.KV task and are there hypotheses about why this task in particular has large improvements?
- What are $N_1$, $N_2$ and $N_3$? Can the authors include some ablations if needed on these values?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel post-training method for generating synthetic data designed to efficiently extend the context window of LLMs, all while preserving their task performance. This approach leverages a summarizer to reduce the context length, enabling a hierarchical pipeline for data generation.

### Strengths
- The paper addresses an important need for long context instruction data.
- The proposed methods allows for diverse instruction tasks
- Finetuning on this data retrains performance on medium context lengths (~10k)

### Weaknesses
 - The impact of the summarizer’s quality on the data generation pipeline is unclear. The paper uses Qwen-72b, but further discussion and experimentation are needed to understand how different summarizer models could influence the method’s effectiveness. For example, different model sizes and a different model family like Llama-2 or Llama-3. Specifically, the paper should investigate how the summarization quality affects the diversity and coherence of the generated instruction-following data, as poor summarization could lead to a loss of critical information or the introduction of inconsistencies.
- RULER evaluations at extended context lengths (like 1M): It would be insightful to include evaluations with context lengths of 1M tokens (or 500k), as most evaluations in the paper are currently under 200k. This would help clarify whether the proposed method maintains performance at significantly larger context lengths. The current evaluations do not sufficiently demonstrate the method's scalability to the extreme context lengths that are increasingly relevant in real-world applications. It is crucial to verify that the performance gains observed at shorter context lengths are not diminished when the context window is significantly expanded.
- Can the author provide performance in small contexts like MMLU or hellaswag after FT'ing? This would show that the model retains performance on shorter contexts while improving long-context capabilities. It is important to ensure that the fine-tuning process does not degrade the model's performance on standard benchmarks, which would indicate a trade-off between long-context and short-context abilities. The paper needs to demonstrate that the model's general knowledge and reasoning capabilities are preserved.

### Questions
Would it be possible to up scale a single document? Although multiple document concatenation was considered to scale to larger context lengths, the proposed methods do up-scaling to a single document that might be 1M. For example, for a document that might only be 128k, increasing the total context to 256k. This would make the entire data synthetic pipeline a more holistic data synthetic pipeline for all long context documents/instructions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to generate a high-quality, long-context instruction-tuning dataset that significantly surpasses the context length of typical raw data. It incorporates a unique hierarchical ordering strategy to ensure logical coherence while preserving the diversity and complexity of the questions. The experimental results on RULER and InfiniteBench demonstrate that the proposed method significantly enhances the performance of llama3.1 in longer contexts.

### Strengths
1. The paper proposes a scalable long-context data generation strategy to significantly improve the long-context capacity of LLama3.1 and extend its context length to 1M.
2. Comprehensive ablation tests. Analyze the impact of data construction strategies from the perspectives of data complexity, diversity of questions, etc.

### Weaknesses
1. The paper uses the Qwen-2-72B model  to generate the QA pairs,  which may result in strong models having a distillation effect on small models. Can you provide experimental results using the Qwen2 7B or Llama3.1 8b as the generator model?
2. Lack of baseline models to validate data generalization . The paper only used llama 3.1 as a baseline. Can you provide more experimental results on models such as Qwen2 7B and deepSeek-V2-Lite?

### Questions
Reference to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Scaling Instruction-Tuned LLMs to Million-Token Contexts via Hierarchical Synthetic Data Generation" aims to address the challenges of scaling large language models (LLMs) to handle extended context lengths, particularly up to one million tokens, without compromising general task performance.

### Strengths
1. The authors propose a synthetic data generation pipeline for instruction tuning, which allows LLMs to effectively extend their context lengths without the need for vast, annotated long-context datasets.

2. Hierarchical Approach: The use of hierarchical splitting and question generation is a significant advancement. By logically structuring questions across multiple levels—hierarchical-aware, local-specific, and multi-hop—the authors ensure coherent instruction generation and improve the model's ability to reason over long contexts.

3. Comprehensive Evaluation: The authors extensively evaluate the proposed approach on multiple benchmarks such as RULER, InfiniteBench, and LongBench. The detailed ablation studies show the importance of different components in their data generation strategy, highlighting that hierarchical order and diverse question generation are critical to achieving better long-context performance.

### Weaknesses
1. **Lack of Strong Baseline Comparisons**: The paper lacks comparisons with suitable, strong baselines that have also achieved extensions to 1M tokens. For example, EasyContext (https://github.com/jzhang38/EasyContext) has similarly attempted to extend context lengths to 1M using long-text data. Especially since the comparisons are made against the original LLaMA-3.1-8B after additional fine-tuning on top of it.

2. **Decreasing Performance on LongBench**: The results on LongBench suggest that the model’s performance decreases as context length increases. This is in contrast to what one would expect after training on long-context data, raising questions about the effectiveness of the proposed methods in maintaining or improving performance across all types of tasks. An explanation should be provided as to why LongBench performance degrades with extended context length training.

3. **Limited Value of Ablation Study in Tables 3 and 4**: The results of the ablation studies in Tables 3 and 4 align closely with expectations, as instruction-tuning data types (e.g., Diverse Questions) are more closely aligned with the evaluation benchmark used (e.g., LongBench). Therefore, these tables have limited value in demonstrating broader insights. A deeper analysis of Table 5 would be more insightful, focusing on the types of questions and the effect of different question strategies during training.

### Questions
1. **Significance of Extending to 1M Context Length**: The authors should provide more justification for the significance of extending to a 1M context length. A 128K context is sufficient for most real-world long-context tasks, and demonstrating practical use cases that necessitate 1M tokens would help strengthen the motivation for this work.

2. **Figure Improvement**: Consider changing the layout of figures 2 to horizontal format for better readability and comparison.

3. **Loss Calculation During Training**: Clarify whether only the answer part of the generated question-answer pairs calculate to the loss during training or if both the question and answer are involved.

4. **Potential Explanation for Decreased LongBench Performance**: Consider discussing whether Section 3.2 of "How to Train Long-Context Language Models (Effectively)" could provide insights into why LongBench performance decreases as training progresses with long-context data, addressing the concerns raised in Weakness 2.

### Soundness
2

### Presentation
3

### Contribution
3
