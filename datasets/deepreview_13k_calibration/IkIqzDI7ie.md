# M$^4$LE: A Multi-Ability Multi-Range Long Context Evaluation Benchmark for Large Language Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Managing long sequences has become an important and necessary feature for large language models (LLMs). However, it is still an open question of how to comprehensively and systematically evaluate the long-sequence capability of LLMs. One of the reasons is that conventional and widely-used benchmarks mainly consist of short sequences.  In this paper, we propose $\textbf{M$^4$LE}$, a $\textbf{M}$ulti-ability, $\textbf{M}$ulti-range, $\textbf{M}$ulti-task, $\textbf{M}$ulti-domain benchmark for $\textbf{L}$ong-context $\textbf{E}$valuation.
$\textbf{M$^4$LE}$ is based on a diverse NLP task pool comprising
36 NLP datasets, 12 task types and 12 domains.
To alleviate the scarcity of tasks with naturally long sequences and incorporate multiple-ability assessment, we propose an automatic approach  (but with negligible human annotations) to convert short-sequence tasks into a unified long-sequence scenario where LLMs have to identify single or multiple relevant spans in long contexts based on explicit or semantic hints.
Specifically, the scenario includes five different types of abilities: (1) explicit single-span; (2) semantic single-span; (3) explicit multiple-span; (4) semantic multiple-span; and (5) global context understanding.
The resulting samples in $\textbf{M$^4$LE}$ are evenly distributed from 1k to 8k input length.
We conducted a systematic evaluation on 11 well-established LLMs, especially those optimized for long-sequence inputs. Our results reveal that: 1) Current LLMs struggle to understand long context, particularly when tasks require multiple-span attention. 2) Semantic retrieval task is more difficult for competent LLMs. 3) Models fine-tuned on longer text with position interpolation have comparable performance to those using Neural Tangent Kernel (NTK) aware scaling methods without fine-tuning.
We make our benchmark publicly available to encourage future research in this challenging area.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces M4LE, an evaluation benchmark designed to assess the long-sequence understanding capabilities of large language models (LLMs). Recognising the limitation of current benchmarks, which primarily focus on short sequences, the authors propose a multi-ability, multi-range, multi-task, multi-domain evaluation strategy. M4LE is based on a diverse NLP task pool consisting of 36 NLP datasets, 12 task types, and 12 domains. The authors propose an automatic approach to convert short-sequence tasks into long-sequence scenarios.

### Strengths
M4LE provides a comprehensive evaluation of LLMs' long-context understanding capabilities across different abilities and length ranges. This is a significant advancement over existing benchmarks which primarily target short sequences.

The authors have collected a diverse set of tasks from a variety of domains which makes the benchmark more robust and comprehensive.

### Weaknesses
1. The construction of the dataset is detached from realistic scenarios. This is because the dataset is mainly composed of short texts synthesized into longer documents, which is not typically how users interact with long-context language models. They are unlikely to use such synthesized long documents as inputs. Moreover, this dataset is evidently more beneficial to models trained on these synthesized short texts, therefore introducing a potential bias.

2. The experimental results can not convince me.  The authors claim that when we scale up the input context from 1k tokens to 8k tokens, the results continuously decrease which is interesting. However, when the answer does not appear at the beginning of the document, gpt3.5-16k usually outperforms gpt3.5-4k.
I think the potential reasons are as follows:
(1) Unfair metrics. This paper mainly uses n-gram matching metrics like ROUGE and F-1 which may not correlate with human evaluation results.
(2) Position bias in the dataset construction. Most answers are at the beginning of the document, additional input is noise.
(3) The current long context models indeed cannot handle many input tokens but how is the Llama2-4k?

3. The authors simply left the main results in the appendix without analysis. For example, I find that in many tasks even a 6B model can outperform gpt3.5 by a remarkable margin. More analysis can make us better understand current long context models.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces M4LE, a comprehensive benchmark for evaluating the long-sequence capability of large language models (LLMs). M4LE comprises a diverse set of 36 NLP datasets, covering 12 task types and 12 domains, to address the scarcity of tasks with naturally long sequences. The benchmark incorporates five different types of abilities, including explicit and semantic single-span, explicit and semantic multiple-span, and global context understanding. This work conducts massive experiments to evaluate existing large language models with the proposed M4LE. The study also explores the impact of factors such as language differences and the positioning of relevant information on long-context understanding capabilities.

### Strengths
1. M4LE offers a multi-dimension assessment by including tasks that cover different abilities, ranges, tasks and domains. This makes it feasible to evaluate a wide variety of skills for long context LMs.

2. M4LE explores factors such as language differences and the positioning of relevant information, showing their impact on the models' long-context understanding capabilities. This analysis contributes to a deeper understanding of the challenges and potential improvements in handling long context inputs.

3. The paper was, in general, easy to follow. Its motivation is reasonable (but see the weakness).

### Weaknesses
1. My primary concern pertains to the strategy of constructing long sequences by simply converting short sequences into longer ones. It is clear that the model's performance deteriorates significantly as the length of the context increases, which raises doubts about the effectiveness and appropriateness of such data formation. The random selection of original short sequences appears to negatively impact the performance. Further investigation is needed to determine how to control the variance of data distributions/domains within a long sequence of text and assess the validity and reasonability of this data formation approach.

2. Additionally, I kindly request a performance comparison with recent state-of-the-art models, such as Llama2-4k.

### Questions
1. Please address the weaknesses above.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new Multi-ability, Multirange, Multi-task, Multi-domain benchmark called M^4LE for the long-sequence ability assessment of LLMs. The experiments on multiple popular LLMs reveal shortcomings in their ability to handle long-text inputs from various perspectives.

### Strengths
1. The collected data in this paper is extensive, encompassing 36 datasets from 12 tasks and domains, enabling the comprehensive evaluation of long-text generation by existing models across 5 different abilities. The considered task types and model capabilities are also highly diverse.

2. The evaluation experiments on several existing LLMs for both Chinese and English are substantial. They reveal from multiple angles the existing models' shortcomings in handling long-text inputs.

### Weaknesses
Additional statistical information of the proposed dataset could be provided, such as the distribution of sentence lengths and the proportion of samples in different languages. It would also be beneficial to understand the distribution of document lengths, not just sentence lengths, as this is a long-text benchmark. Furthermore, providing the average and standard deviation of token counts per document would give a more concrete understanding of the dataset's scale and complexity. The lack of this information makes it difficult to assess the true challenge posed by the benchmark.


### Questions
Do the authors have a data cleaning process? How is it done?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose M4LE, which is a multi-ability, multi-range, multi-task, multi-domain long-context evaluation benchmark for large language models. It evaluates the ability of LLMs to understand long sequences and perform tasks in different languages and context lengths. The benchmark includes five different abilities and five different context length ranges. The results show that current LLMs still struggle to understand long-context information, and the performance of different models varies in different context length ranges and languages. The benchmark also delves into the factors influencing long-context understanding capability, including the positioning of relevant information and the performance of LLMs under different languages.

### Strengths
1. The main contribution of the paper is a new long-context benchmark which covers a wide range of tasks. M4LE can better evaluate the long-context ability of LLMs across various scenarios.

2. The author evaluates 11 widely well-known LLMs on the M4LE benchmark, and find some interesting conclusions.

3. The authors do experiments with their benchmark to verify the lost-in-the-middle phenomenon in LLMs.

### Weaknesses
It is better to include some comparison between M4LE and other benchmarks in Table 2. It is also good to include the max. length number in it.

The observations from the evaluation in the paper are weak and uninformative, except that the existing LLMs struggle to process long inputs, and ChatGPT performs the strongest among all. These can be shown from other existing benchmarks as well.

The categorization and organization of different ranges of sentences lengths can also be done in other similar benchmarks.

The most interesting point introduced in the paper is to categorize inputs to 5 abilities, explicit single-span, semantic multi-span understanding. However, it is unfortunate that there is an unclear analysis with little informative points in the paper in terms of this point.

List a few unclear points.
1.	For example, M4LE spans different domains and tasks, while the evaluation does not consider these points, e.g. specific analysis on the different impacts of QA, translation.

2.	Besides, it shows the situations from 3 types of tasks are different. There can be more sophisticated explanations and experiments to furnish further ideas.

3.	In Figure 2, why most models perform worse on explicit multi-span understanding compared to both semantic multi-span and global context understanding?

4.	From the results in the paper, ChatGPT is the strongest ones in processing long-context inputs, which is much large in its size. However, only 13B models are evaluated in the paper. It is still unclear that whether larger models can perform much better, e.g. LLaMA2-70b.

5.. The paper seems to have no detailed report about how to construct the benchmark, for example, which instances I will consider to combine them together, or I will choose them randomly? how the number of instances N is decided? In that case, I will think that
the M4LE just simply combine the small datasets together to build long-context datasets, where most of them have no relevance between each other. It means that M4LE is a benchmark mainly tests the retrieval ability over long-context but less consider the comprehensive understanding over the global context.

6. In the experiments on different language, the authors claim that Vicuna and Long-chat exhibit a more pronounced performance drop in Chinese. However, in Figure 4, the drops of these models between these two languages have no obvious difference. For example, Vicuna-13B-1.5-16k declines greatly both in English and Chinese after 4k length.


Maybe I miss something. I am confused that M4LE is seemingly built from existing web sources, which LLMs are exposed to during training. How does it alleviate the data leakage problem, which also exists for other benchmarks?

### Questions
see my weakness part

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
