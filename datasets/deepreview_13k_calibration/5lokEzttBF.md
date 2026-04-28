# SCAR: Efficient Instruction-Tuning for Large Language Models via Style Consistency-Aware Response Ranking

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Recent studies have shown that maintaining a consistent response style by human experts and enhancing data quality in training sets can significantly improve the performance of fine-tuned Large Language Models (LLMs) while reducing the number of training examples needed. However, the precise definition of style and the relationship between style, data quality, and LLM performance remains unclear. This research identifies two key stylistic elements in responses: linguistic form and semantic surprisal. We find that, among training data of comparable quality, higher consistency in these response elements leads to better LLM performance. Inspired by this, we introduce Style Consistency-Aware Response Ranking (SCAR), which automatically prioritizes instruction-response pairs in the training set based on their response stylistic consistency. By selecting the most style-consistent examples, sometimes as few as 0.7\% of the full dataset, the fine-tuned LLMs can match or even surpass the performance of models trained on the entire dataset in coding and open-ended question-answering benchmarks. %Code and data are available at~\url{https://anonymous.4open.science/r/SCAR-0233/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a system called SCAR that can prioritize instruction-response pairs in a training dataset based on their style consistency. In addition, the paper also explores the relationship between response style, data quality, and LLM performance.

### Strengths
1. The paper proposes SCAR, which reduces the size of the training set while improving performance by optimizing data selection in the context of fine-tuning the existing LLM instructions. The core innovation of SCAR lies in its focus on language style consistency and defines two key style elements: language form and semantic surprisal. This systematic focus on style consistency and optimization method is an important contribution.

### Weaknesses
1. The motivation of this paper is unclear. Existing research has widely recognized the importance of ensuring diversity in instruction-tuning data. However, this paper seems to oppose this common understanding without strong justification. The experiments do not persuade me, as they are somewhat weak: both the dataset and the LLM size are limited. The results are unconvincing and, if not thoroughly validated, could potentially mislead the community.

2. Although the paper proposes "linguistic form" and "semantic surprisal" as key style elements, the definitions and measurement methods of these concepts are slightly vague in some sections, especially the concept of "semantic surprisal", which still needs further clarification and explanation.

3. Although the paper provides a lot of experimental data and results, the design and interpretation of some experiments are a bit complicated. For example, in the comparison of different data selection methods, some performance differences are not adequately explained. For some performance degradation cases (such as the performance of LLAMA2-13B), the paper does not explore the reasons behind it in detail.

### Questions
Refer to the above.

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
The authors analyze the impact of linguistic form and semantic surprisal on LLMs' SFT performance. They find that consistent data form leads to better outcomes. They propose a selection method, SCAR, to choose a small portion of SFT data, achieving strong performance on certain downstream tasks.

### Strengths
- Investigating the linguistic form and semantic surprisal of SFT data and their impact on fine-tuned performance is meaningful.
- The paper is well-written, easy to follow, and contains rich details.
- The authors conduct a large number of experiments to provide useful information.
- The authors open-source their code and data.

### Weaknesses
1. The position of the selection method is unclear. Is it proposed for training a general model (e.g., ChatGPT) or a specialized model (e.g., CodeLLaMA)?
   - If your method is proposed for training general models, you should verify its effectiveness using various downstream tasks (e.g., MMLU, GSM8k, HumanEval in TULU evaluation). Please report the performance on the above benchmarks directly using the checkpoints trained in Table 5. This will help determine whether the selection achieves overall improvement or just improvements in a few tasks.
   - If your method is proposed for training specialized models, you should compare it with more relevant baselines, such as directly using existing **high-quality** domain-specific data (rather than StackExchange), evol-instruct in specific domains, or instruction backtranslation in specific domains. If a user wants to train a specialized model, they do not need to select data from large-scale general data but can directly use high-quality domain-specific SFT data.

2. The method seems to select the response whose format is closest to an existing model (e.g., GPT 3.5), rather than detecting format-consistent instances in the dataset. This raises concerns that the method is not truly identifying inherent consistency within the dataset but rather imposing an external style bias.

3. The referenced response is unconvincing to me. Since the referenced prompt contains instructions, the model may correct the response even if asked to ignore them. It might be better not to provide the instruction. The inclusion of instructions introduces a confounding variable, making it difficult to isolate the impact of linguistic form versus instruction following.

### Questions
1. What is the output format of StackExchange? Does it contain only code or both text and code?
1. Regarding the code, is the linguistic metric meaningful? Since the standard deviation of TTR in code is larger than that in text, which may not be intuitive.
1. Why use max pooling when calculating v_p, which only preserves the information of one token?
1. What parameters need to be trained in your method?
1. Why is the selection ratio of code and text different (12.5% vs 10%)? Is this intentional?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes SCAR as a novel approach for instruction-following data selection. It is grounded in the observation that a model performs better when the response styles in its training data are more consistent. Thus, the author trains a reward model to capture response differences in linguistic form and surprisal-determining features. The required dataset consists of quadruples, i.e., an instruction, a human response, an LLM response, and a human-referenced LLM response. The model is trained to optimize the ranking loss and the representation learning loss simultaneously. Experiments on code and open-ended domains show consistent improvements in SCAR over several baselines.

### Strengths
The paper is rich in content and presents extensive analysis The investigation of the impact of styles on LLM fine-tuning effectively motivates the design of the ranking model, which is further validated through experiments on various datasets with ablation discussions.

### Weaknesses
 * There is a lack of a simple yet significant rule-based baseline. (See Q1)

* The model trained on general instruction-following data was only tested on AlpacaEval evaluated by LLMs. The data collected for training the ranking model also relies on responses generated by LLMs. This raises concerns that SCAR inadvertently leverages certain style features favored by the LLM judge. (See Q2)

* The font in some figures is difficult to read without zooming in, particularly in Figures 1 and 3. The organization of the experimental setup in Section 4 could be improved.

### Questions
Q1: The "longest" method discussed in prior work[1, 2] appears to be a strong rule-based baseline. How does its performance compare with SCAR?

[1] Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning
[2] Rethinking Data Selection for Supervised Fine-Tuning

Q2: The performance of SCAR on some objective benchmarks is expected, such as GSM8K, MMLU, BBH, etc.

Q3: Could you provide more details about how were the embeddings created for Figure 1(Left)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces SCAR (Style Consistency-Aware Response Ranking), a method to improve the efficiency of instruction tuning for Large Language Models (LLMs) by selecting data that maintains stylistic consistency in responses. The authors propose that consistent response style enhances fine-tuning performance, and define two key elements in response style: linguistic form (the structural presentation of responses) and semantic surprisal (the predictability of response content relative to the instruction). SCAR ranks instruction-response pairs by stylistic consistency, allowing LLMs to achieve comparable or even superior performance using only a very small portion of the original dataset in coding and open-ended question-answering benchmarks.

### Strengths
1. This paper proposes that Style Consistency is important for the efficiency of instruction tuning, which has not been well studied. Thus I think the novelty of this motivation is solid. 
2. The experiments conducted by this paper are comprehensive.

### Weaknesses
1. The paper is not well-written and very hard to follow and understand. I can not even find an overall description of the whole workflow. An illustrative main figure should be included. 
2. The definition of Semantic Surprisal in line 054 is not well-aligned with the real metric that is used in line 162. Your definition of Semantic Surprisal, “the choices of solutions, ideas, or approaches in a response that affects how predictably or unexpectedly it addresses the instruction” is largely beyond the capabilities of perplexities. 
3. Please let me know if I am wrong, when you calculate the PPL(y_c|x), you will first filter out all the functional words (y_p). So I think it is probable that this process will directly destroy the consistency and fluency of the original sentences, thus making the resulting ppl less meaningful. 
4. Similar to point 2, your definition of linguistic form is also not well-aligned with the real metric being used. I don’t think the utilization on TTR, MTLD, Flesch score, sentence length and punctuation frequency can support your definition as “elements that shape the presentation of a response, mostly independent of semantics, such as tone (formal or informal), transitional word choice, sentence structure, formatting (bullet points or heading lines), variable naming conventions”. 
5. The settings for this paper are slightly chaotic: In the paragraph in line 148, the LLMs being used are mainly llama2 families, but in the later parts of the paper, it seems that most experiments are conducted on llama3 families. Is this done on purpose? This inconsistency makes it hard to follow. 
6. The method is far too complicated and contains too many components, thus making it hard to get practical usage. For example, it needs LLMs to first generate an analysis on Helpfulness and Correctness, and it needs LLMs to re-generate some of the responses. It also needs to train a customized module for the ranking further. As mentioned in point 1, considering so many components utilized in the method, there is no illustrative figure, which is not reasonable to me.

### Questions
1. The colors in Table 1 are not aligned with the colors in other parts.
2. What is exactly presented in Figure 1? For left, are they the complete responses of the 3 categories or extracted functional words from responses of the 3 categories? Similarly, for right, are they the ppl over complete responses or ppl over y_c?  
3. Can you provide a more detailed illustration and analysis of how the takeaways are concluded? 
4. Please further illustrate the experimental results in Figure 2, especially in the Open-ended Domain. It looks like every metric is worse than the Full Data on Human dataset except for ppl, I think it contradicts with most of the previous findings. Can you explain it?

### Soundness
2

### Presentation
2

### Contribution
2
