# Evaluating the Instruction-following Abilities of Language Models using Knowledge Tasks

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
In this work, we focus our attention on developing a benchmark for instruction-following where it is easy to verify both task performance as well as instruction-following capabilities. We adapt existing knowledge benchmarks and augment them with instructions that are a) conditional on correctly answering the knowledge task or b) use the space of candidate options in multiple-choice knowledge-answering tasks. This allows us to study model characteristics, such as their change in performance on the knowledge tasks in the presence of answer-modifying instructions and distractor instructions. In contrast to existing benchmarks for instruction following, we not only measure instruction-following capabilities but also use LLM-free methods to study task performance. We study a series of openly available large language models of varying parameter sizes (1B-405B) and closed source models namely GPT-4o-mini, GPT-4o. We find that even large-scale instruction-tuned LLMs fail to follow simple instructions in zero-shot settings. We release our dataset, the benchmark, code, and results for future work.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to evaluate the instruction-following abilities of LLMs using Knowledge Tasks. It adopts several popular benchmarks and add rules on top of them to evaluate instruction following capability and content correctness at the same. It includes details of how to design these instructions and evaluation results of popular models including GPT-4, etc.

### Strengths
* This paper proposes a benchmark that both evaluate instruction following capability and content verification, which does not draw too much attention in the community before.
* This paper includes details regarding how to design the instructions and benchmarks, and run a lots of experiments to benchmark  different models in various scales.

### Weaknesses
 * This paper ignores one key related work [1]. [1] instructs the model to verbalize the task label with words aligning with model priors to different extents, adopting verbalizers from highly aligned (e.g., outputting “positive” for positive sentiment), to minimally aligned (e.g., outputting “negative” for positive sentiment). During evaluations, [1] uses task labels after manipulations, which in fact evaluates both the instruction following capability and conduct content verification. In theory, this technique can be used for any classification task. However, such a related work was not discussed at all in this paper, indicating that Table 1 in this paper does not provide a comprehensive reviews to the community.


* Although authors run lots of experiments, it is hard to draw insights from their plots. For example, it is more interesting to plot model performance in the same family (e.g. LLaMA 3.1 in different sizes) to see how scaling can help solve this task instead of plotting them according to model size. 


* In addition, it will also good to know what is the reference result, which is the result of original benchmark without any modifications. From existing results, it is hard to know how following instructions will impact models' content' correctness.


* The paper tiles has "using Knowledge Tasks" to evaluate model capabilities but I would only count MMLUPro as knowledge task and all others are reasoning related ones. In this case, the title of this paper should be further clarified.


* I do knot see too much value of Lite Benchmark version, which only consists of 150 samples. It introduces large variances when used for evaluating models. The authors should only consider have only one version for both simplicity and clarity, e.g. using the full benchmark or half size of the full version benchmark as the final benchmark.

### Questions
See the weakness.

### Soundness
2

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
This paper presents a benchmark for evaluating the instruction-following abilities of LLMs on knowledge tasks with automated error classification. The authors augment existing dataset knowledge datasets (e.g., MMLU-Pro, MathQA) with manually-crafted instructions to test the instruction following abilities of LLMs. Extensive evaluation across various LLMs demonstrate failures in instruction-following, even among frontier LLMs.

### Strengths
- The authors provide extensive evaluations of various models ranging in size on their proposed instruction-following benchmark. 

- By augmenting existing knowledge datasets with manually constructed instructions, the authors can automatically classify errors as either knowledge errors or instruction-following errors.

### Weaknesses
 - As a whole, the main paper includes a lot of implementation details, which is not necessarily a bad thing, but in this case takes up valuable space that would be better used to provide additional discussion and analysis of the experimental results, which are largely underdeveloped. For instance, sections 4.1 and 4.2 could be briefly summarized in the main paper with the bulk of the details moved to the appendix.

- The automatic error classification is rather underdeveloped in the main paper and lacks sufficient analysis. For instance, only a few results in the main paper (Figure 1 and Table 4) include IC and KTS scores, and even then the subsequent discussion focuses primarily on variants of exact match. A lot of relevant analysis (e.g., on which instruction categories do models make the most instruction-following errors on average?) is hard to follow, in part because the layout of figure 2 makes it hard to compare across instruction categories. 

- Similarly, the inclusion of new instruction classes (e.g., distractors, instructions that are conditional on the answer) is also rather surface-level. For instance, the conclusion drawn from section 4.3.3 on distractors is that they worsen model performance. More analysis is needed here (e.g., which models are the most susceptible to distractors, what kinds of distractors are most effective).

- The instructions categories are rather limited in comparison to existing work. Several of the instructions (e.g., alternate_case_correct_answer) play into known tokenization issues with LLMs [1]. Existing work such as IFEval include more practical instruction categories (e.g., length constraints, JSON formatting) [2]. 

- The writing quality needs to be improved. For instance, in the definition for “alternate_case_correct_answer”, “correction candidate answer” should be “correct candidate answer”. In section 3.5 line 268, the reader is referred to “Table 2 in the appendix” though table 2 is in the main paper. Likewise, some terminology is used inconsistently (e.g., print_correct_answer_text vs. print_correct_answer). This didn't affect readability too significantly so I did not factor this point into my decision assessment.

### Questions
- How can you measure correctness (in terms of knowledge) for instructions such as use_options_to_create_strings, where the output is seemingly independent of the correct answer?

- Could you verify that table 2 is correct? For instance, the definition of increment_incorrect_numeric_answers_by_one suggests that all answers should be indicated, not just the incorrect ones. Likewise, why is use_incorrect_options_to_create_string in the non-conditional operations on lists category when it seems to be inherently conditional on the correct answer?

- Related to figure 1, could you provide some insight into Qwen-2.5-1.5B’s performance? Why is the strict (PCA) score so similar between Qwen-2.5-1.5B and Qwen-2.5-3B, yet Qwen-2.5-1.5B’s strict (PCA label) score is significantly higher than Qwen-2.5-3B’s? Why are the knowledge and instruction-following error scores significantly higher for Qwen-2.5-1.5B than Qwen-2.5-3B even though the strict (PCA) scores are so similar?

- On average, what percent of errors can be automatically classified as either knowledge errors or instruction-following errors? Figure 1 leads me to believe that lots of errors escape categorization (e.g., Llama-3.2-1B achieves a strict (PCA) score of 2%, yet only 17% and 9% of instances can be classified as knowledge errors and instruction-following errors, respectively. Is this due to the high-precision nature of these metrics? If so, would supplementing with an LLM-based method for error categorization be better?

- Are certain categories of distractors (e.g., among the 5 instruction categories) more effective than others? Are some models (or family of models) more susceptible to certain categories of distractors than others?

[1] https://arxiv.org/abs/2410.19730

[2] https://arxiv.org/abs/2311.07911

I am willing to raise my score if my questions/concerns are adequately addressed.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to evaluate the instruction-following abilities of language models within knowledge-based tasks by developing a benchmark that integrates instruction adherence and task performance. This approach attempts to measure both knowledge task success and instruction-following compliance using various publicly available large language models.

### Strengths
The methodology uses a range of instruction types and tasks, aiming to comprehensively assess model capabilities in both knowledge retrieval and instruction adherence.

### Weaknesses
1. **Limited Innovation:**
   The proposed benchmark shares considerable overlap with existing methods, particularly with IFEval, making it difficult to distinguish any unique contributions. Given that previous work has established benchmarks and instructions in similar contexts, this work falls short in terms of innovation.

2. **Unclear Figures:**
   Several figures, such as Figure 1 and Figure 4, are difficult to interpret due to unclear resolution or layout. Additionally, the figures on pages 8 and 9 might be better suited for the appendix, as they do not contribute substantively to the main discussion.

3. **Insufficient Ablation Studies:**
   The paper includes limited ablation experiments, which leaves the proposed benchmark's robustness and effectiveness underexplored. A deeper exploration of instruction categories and configurations would provide a stronger foundation for the benchmark's utility.

4. **Lack of Practical Implications:**
   The results from this benchmark do not provide any novel insights or actionable guidance for the training and development of future models. In its current state, the benchmark primarily reiterates known limitations of LLMs in instruction-following without advancing understanding in a way that could influence future model training approaches or benchmarks.

### Questions
Why did the authors choose to assess instruction-following and knowledge in a combined format? For instance, if instruction-following is the main focus, why not evaluate using IFEval first and then separately test knowledge tasks (such as MMLU) for a clearer analysis? This work combines them, which others have worked to disentangle, potentially obscuring instruction-following performance and knowledge retrieval.

### Soundness
1

### Presentation
2

### Contribution
1
