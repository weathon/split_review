# LongCite: Enabling LLMs to Generate Fine-grained Citations in Long-context QA

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Though current long-context large language models (LLMs) have demonstrated impressive capacities in answering user questions based on extensive text, the lack of citations in their responses makes user verification difficult, leading to concerns about their trustworthiness due to their potential hallucinations. In this work, we aim to enable long-context LLMs to generate responses with fine-grained sentence-level citations, improving their faithfulness and verifiability. We first introduce LongBench-Cite, an automated benchmark for assessing current LLMs' performance in Long-Context Question Answering with Citations (LQAC), revealing considerable room for improvement. To this end, we propose CoF (Coarse to Fine), a novel pipeline that utilizes off-the-shelf LLMs to automatically generate long-context QA instances with precise sentence-level citations, and leverage this pipeline to construct LongCite-45k, a large-scale SFT dataset for LQAC. Finally, we train LongCite-8B and LongCite-9B using the LongCite-45k dataset, successfully enabling their generation of accurate responses and fine-grained sentence-level citations in a single output. The evaluation results on LongBench-Cite show that our trained models achieve state-of-the-art citation quality, surpassing advanced proprietary models including GPT-4o. 
We also discover that SFT with citation information effectively reduces hallucinations and enables a more uniform utilization of context.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces LongBench-Cite, a Long-Context QA benchmark that requires models to add citations in their responses. Different from other similar works, this work evaluates citations at the sentence level, rather than at the chunk level. That is, models in this task are supposed to cite specific sentences in context that support their responses rather than documents or large chunks of text. The authors also construct LongCite-45k, which is a supervised fine-tuning dataset for the task studied, and use this dataset to train two models. Their 8B and 9B parameter, fine-tuned models outperforms GPT-4o. The results of their experimentation show that existing models are not proficient in sentence level citation. Moreover, requiring sentence level citations degrades model performance. Finally, fine-tuning improves model capability in QA and sentence level citations a reasonable amount.

### Strengths
**Interesting Task.** Studying fine-grained citations (at the sentence-level) is interesting. Efforts in developing models with the capability to provide fine-grained citations is useful. In particular, this could help with evaluation of the veracity of model outputs

**Results.** The results show that the fine-tuned models generally outperform proprietary models in long-context QA with citations, which is a nice result. Furthermore, results seem to imply that proprietary models may have been adequate at chunk-level citations but struggle more with sentence level citation. Finally, the "correctness ratio" measurement, which compares how models perform with and without having to cite, is interesting and clearly shows shows that making the models output citations alongside correct answers seems to degrade model performance on QA. 

**Complete Work.** The paper presents a relatively complete exploration of an idea: a new variant of QA with citations is proposed; an evaluation metric for the task is proposed; existing models are evaluated on the task; a dataset is constructed for fine-tuning, and used to train new models for the task; those models perform well; analysis is presented.

**Human evaluation** It’s great to have human evaluation. I liked the analysis of LongCite-9B vs LongSFT-9B; I think it could be fleshed out more. The manual evaluation of citation recall/precision strengthens the paper, although I think the correlation is not entirely convincing since--if I understand correctly--it only includes 3 data points (GLM-4, LongCite-8B and -9B). The presentation could perhaps be strengthened; it took me some time to correctly interpret the correlation from the table. The Cohen’s Kappa result is more convincing, although I wasn’t sure how it was computed (questions below).

### Weaknesses
 **Clarity and Missing Details.**  The writing is a bit hard to follow at times, for example in the description of the construction of the dataset. Another area that was hard to follow were the pipeline details. Specifically, what retrieval method is used to retrieve chunks in the chunk-level citation generation (I know it's Zhipu, but could more details be provided)? How were the hyperparameters chosen (l, k, & n)? In pipeline validation, how are the evaluations carried out (done manually? Or automatically)? It's unclear how the values for *l*, *k*, and *n* were determined, and what impact these choices have on the overall performance. The paper would benefit from a more detailed explanation of the retrieval process, including the specific embedding model used and the similarity metric. Furthermore, the validation process lacks clarity; it's not specified whether the pipeline validation is performed manually or automatically, and what criteria are used to assess the pipeline's performance.

**Over-reliance on LLM Evaluation.** Either GPT-4o or GLM-4  is used for: 1) evaluating correctness of QA answers, 2) evaluating correctness of citation (precision and recall), 3) filtering out starting, transition, summary and reasoning sentences, 4) all steps of the CoF pipeline for dataset construction. Your human evaluation showing correlation between GPT-4o evaluations and human evaluations is critical to dispelling some concern over possible systemic errors from GPT-4o corrupting your results, but the concern isn’t totally alleviated. For example, it seems like one way to get a high score is to emit many sentences that GPT-4o would deem “starting, transition, summary or reasoning” since these need no citations according to the evaluation scheme. I think a discussion of this reliance and where things could go wrong should be included in a limitation section, or additional measurements and/or human evaluations should be conducted to address potential issues. The reliance on LLMs for evaluation introduces a potential bias, as these models might favor responses that align with their own training data or biases. The paper should include a more thorough discussion of the potential limitations of this approach, and explore alternative evaluation methods or additional human evaluations to validate the results.

**Missing Discussion of Sensitivity to Prompt.** Since the proprietary models are only prompted, and the task itself has a somewhat atypical format (e.g., with each sentence tagged with an index) it would be good to discuss whether any tuning of the prompts was conducted (especially for the proprietary models) and/or any observations related to the sensitivity of the models to the prompt. This would help alleviate concern that the proprietary may have performed better if only their prompts were tuned better. The paper should address the potential impact of prompt engineering on the performance of the proprietary models. It is essential to discuss whether different prompt formulations were explored and how the final prompt was selected. A sensitivity analysis of the models to variations in the prompt would also be valuable.

### Questions
- Construction of LongBench-Cite: Is LongBench-Cite just a concatenation of existing datasets? Is there any additional processing to create LongBench-Cite examples (and if so what is it)? If it is just a concatenation, then what is the advantage of combining it into one dataset vs. evaluating on them each separately? 
- Can you explain precisely what is being compared in the Cohen’s Kappa calculation? Is it correctness at the response level, or citation quality at the sentence level or something else?
- Can we just use CoF to do the LQAC task? What would be the disadvantage? 
- Not a question: When you list multiple Figures, often only one is hyperlinked in the text; all should be hyperlinked
- If you use GPT-4o for all of the evaluation steps, is it fair to compare GPT-4o (and have it evaluate itself)?
- Did you notice any “lost-in-the-middle” type phenomenon (https://arxiv.org/abs/2307.03172)?
- How much do you think the format of the citations you are asking for affects the sentence-level citations results of proprietary models? In other words, do you think there is a way to reformulate the task (prompt) such that those models would perform much better? Did you try many different prompts?
- Is it possible/necessary for your models to cite non-contiguous sentences, e.g., [1-2;5] ?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper first evaluates the performance of LLMs in generating sentence-level citations in long-context QA. Then, they distill GLM-4 to construct high-quality fine-grained citation data and fine-tune GLM-4-9B and Llama-3-8B to generate sentence-level citations. Experimental results show that simply SFT can improve citation quality and response correctness.

### Strengths
1. The structure of this paper is clear and easy to understand
2. The experimental design (choice of model, dataset, and evaluation criteria) is reasonable.
3. The author noticed that adding citations can harm response correctness, which was not mentioned in previous work
4. Both human evaluation and experiments demonstrate the effectiveness of the trained LongCite-8B and LongCite-9B

### Weaknesses
1. Lack of significant novelty: Firstly, the concepts of long-context LLM citation [1] and fine-grained citation [2][3] have already been discussed in previous works. This paper merely combines these two concepts, stitching them together into a single paper. More importantly, the authors even lack discussion and comparison of these important prior works. Secondly, the implementation approach for fine-grained citation heavily overlaps with [2][3], as both rely on distilling advanced LLMs to extract fine-grained spans. The main difference is that this paper extends the context length and distinguishes citation forms by splitting the context into sentences.
2. Unoriginal conclusions: Previous works on attributed text generation have already demonstrated that simply SFT can significantly enhance a model's attribution abilities [2][3][4]. I did not learn anything novel from the authors' conclusions, with the different prerequisite being a long-context.
3. Insufficient benchmarking: The paper only adopts the LAC-S strategy for benchmarking, which is insufficient. It is difficult to deduce whether the model’s poor sentence-level citation quality is more influenced by poor instruction-following or weak evidence-searching ability based on these evaluations.
4. Lack of baseline comparisons: The method in [2] achieves sentence-level citation through distilling Gemini, using different models for content selection and sentence planning. The authors lack a fair comparison with such method.
5. Evaluation of correctness: The authors’ evaluation of correctness includes both accuracy and comprehensiveness, which are actually different dimensions but equally important. These should be separately assessed instead of being unified under correctness. Otherwise, it becomes challenging to discern whether fluctuations in correctness are due to errors or insufficient coverage. The causes and consequences of these two are entirely different. I would prefer referring to correctness as response quality or overall quality.
6. High cost of constructing SFT data: The entire data construction process heavily relies on calling the proprietary model GLM-4, which is not only high-cost but also hard to reproduce.
7. Quality of the question and answer generated by self-instruct: This is crucial for the diversity and quality of CoF data, but the quality cannot be guaranteed. The authors lack specific analysis of the quality of the questions and answers generated in the first step. Will the generated questions focus too much on local information in the background, resulting in insufficient answers?
8. Control over granularity: LongCite-45k contains 128,000 tokens. Assuming an average sentence length of around 20-30 tokens, this would result in over 4,000 sentence indices, which is too fine-grained. I am concerned about its practicality in real-world usage.

### Questions
1. Typo: Line 82: "LongBench-Chat" should be corrected to "LongBench-Cite".
2. Typo: In Figure 4, lines 802-803, "Example Answer 2" should be corrected to "Example Answer 3".
3. Why are the standards for correctness evaluation inconsistent across different datasets in LongBench-Cite, and why are the scoring ranges different? For example, LongBench-Chat does not consider comprehensiveness, and its score range is 1-10, while GovReport’s score range is 1-5, and others are 1-3. Additionally, why does the evaluation of LongBench-Chat require a few-shot approach, while others are zero-shot?
4. How is the correctness score in Table 3 calculated? Is it the average score across the entire dataset? However, the correctness score range varies across different datasets. Was this unified into a percentage scale here? The authors did not clearly explain this.
5. Why is the performance of GLM-4-9B-chat on the GovReport dataset exceptionally weak in Table 2? Was there any specific analysis conducted?
6. Compared to chunk-level citation, are there any other statistics changes in sentence-level citations, such as the number of citations or the proportion of a statement citing multiple sources

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper primarily focuses on the task of Long-context QA with Citation, including the following key points:
1. adoption of sentence-level citation; 
2. proposal of an automated data construction method; 
3. improved model performance on the LQAC task after training.

### Strengths
1. The overall structure is complete, and the writing is well-organized.
2. A comprehensive body of work has been conducted for the LQAC task, including data construction and model training.

### Weaknesses
Indeed, as mentioned above, this paper presents a complete body of work around LQAC, with comprehensive content that is self-contained. However, the core issue with this paper lies in its low level of innovation:

1. The proposed LQAC task essentially combines aspects from *short-text QA*, *fine-grained citation*, and *long-context generation with citation*, making the innovation somewhat incremental.
2. I believe that in addition to discussing the general challenges of generation with citation, research on the LQAC task should emphasize the unique characteristics of **long-context scenarios**, such as *citation consistency across contexts*, *citation redundancy*, and *potential contradictions in citations*. This would better highlight the differences between this work and prior research.

### Questions
If the authors can clearly and explicitly explain the unique challenges addressed by this work in the long-context scenario, I would consider increasing the score.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper focuses on the Long-Context Question Answering with Citations (LQAC) task. To assess large language models (LLMs) in generating accurate answers with appropriate sentence-level citations, the authors introduce an automated benchmark called **LongBench-Cite**. They further develop a supervised fine-tuning dataset **LongCite-45k** using a **Coarse to Fine (CoF) pipeline**. Leveraging this SFT dataset, they train **two LLMs** that achieve state-of-the-art citation quality on their curated benchmark.

### Strengths
- The paper is well-structured, effectively integrating the benchmark, training data, and fine-tuned models for the LQAC task.

- The evaluation results on LongBenchCite demonstrate that the fine-tuned models achieve state-of-the-art citation quality, surpassing even advanced proprietary models, including GPT-4o.

### Weaknesses
 - **Lack of Motivation and Novelty**: In addition to the coarse granularity issue, the authors point out that the chunk-level citation may also result in incomplete sentences. This problem arises because the authors have rigidly divided the context into fixed-length chunks of 128 tokens. A potential solution could be splitting the text based on sentence terminators, such as periods or semicolons. Given that the authors assert that sentence-level citation is superior to chunk-level citation, what motivates the inclusion of chunk-level citation in the CoF pipeline? Additionally, since most methodologies (Evaluation Method / Dataset Construction / Model Training) in this paper are adapted from existing work [1], the novelty is unclear.

- **Obscure and Inconsistent Noun Naming.** There are several confusing noun pairs in the paper. The authors should read through their paper before submission. For instance:
    - *(LongBench-Chat, LongBench-Cite):* In the abstract (line 17), the authors state, "We first introduce LongBench-Cite, ...," whereas in the introduction (line 82), they refer to "We introduce LongBench-Chat, ...". This inconsistency is perplexing, and it is unclear if one of these is meant to reference a published work [1].
    - *(LongCite-9B, LongSFT-9B) and (LongCite-8B, LongSFT-8B):* The naming convention is confusing, making it hard for readers to discern whether these models are synonymous or represent distinct concepts.

### Questions
Could you explain why the chunk size must be fixed at 128 tokens instead of matching the sentence length?

### Soundness
2

### Presentation
2

### Contribution
2
