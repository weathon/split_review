# Task Facet Learning: A Structured Approach to Prompt Optimization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Given a task in the form of a basic description and its training examples, prompt optimization is the problem of synthesizing the given information into a text prompt for a large language model (LLM). Humans solve this problem by also considering the different facets that define a task (e.g., counter-examples, explanations, analogies) and including them in the prompt. However, it is unclear whether existing algorithmic approaches, based on iteratively editing a given prompt or automatically selecting  a few in-context examples,  can cover the multiple facets required to solve a complex task.  In this work, we view prompt optimization as that of learning multiple facets of a task from a set of training examples. We identify and exploit structure in the prompt optimization problem --- first, we find that prompts can be broken down into loosely coupled semantic sections that have a relatively independent effect on the prompt's performance; second, we cluster the input space and use clustered batches so that the optimization procedure can learn the different facets of a task across batches.  The resulting algorithm, \shortname{}, consists of a generative model to generate initial candidates for each prompt section; and a feedback mechanism that aggregates suggested edits from multiple mini-batches into a conceptual description for the section. Empirical evaluation on multiple datasets and a real-world task shows that prompts generated using \shortname{} obtain higher accuracy than human-tuned prompts and those from state-of-the-art methods. In particular, our algorithm can generate long, complex prompts that existing methods are unable to generate. Code for \shortname{} will be available at \url{https://aka.ms/uniprompt}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a prompt optimization method $U_{NI}P_{ROMPT}$ to generate complex prompts for covering multiple facets of a task and improving overall accuracy. Its effectiveness is demonstrated through relevant experiments.

### Strengths
The strategy for creating mini-batches to generate edits and then aggregating them at the batch level to yield the final edit in a feedback mechanism is interesting. 

Experimental results achieves SOTA.

### Weaknesses
1.The paper contains some detailed issues, e.g., $U_{ni}P_{rompt}$ mentioned in  line 100-101; an extra space before "So" mentioned in line 197-198. 

2. The experiments should be re-organized and polished carefully before submission, especially in Section 4.1,  4.2 and 4.5. 

3. Some qualitative experiments are supported be added to validate the differences in report accuracies under various mini-batch sizes.

### Questions
The impact of mini-batch size. 

The impact of aggregation.

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
The paper introduces UNIPROMPT, a method that uses task facet learning to enhance prompt optimization by breaking down prompts into distinct semantic sections, targeting diverse facets such as counter-examples and explanations.

### Strengths
- UNIPROMPT clusters examples to capture task-specific facets effectively, with a two-tier feedback mechanism ensuring that prompt modifications are generalizable and not overly specific to individual examples.
- The authors provides strong empirical results, with UNIPROMPT outperforming state-of-the-art methods on multiple datasets, notably achieving significant improvements on hate speech classification.
- By focusing on automatic prompt generation without relying heavily on human-engineered prompts, this approach may reduce the manual overhead of prompt tuning.
- Extensive ablations validate the contribution of each component (clustering, feedback structure) to performance.

### Weaknesses
 - All experiments are conducted on powerful proprietary LLMs, I wonder whether the proposed method remains effective for opensource LLMs such as LLaMA or Qwen.
- It seems that the proposed method underperforms DSPy on MedQA, while surpassing it on other benchmarks, what might be the reason?
- How to determine the number of clusters when constructing the minibatches? How does this affect the method's effectiveness?

### Questions
See weaknesses.

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
This paper introduced a method for prompt optimization called UNIPROMPT. The prompt optimizaiton is deemed as the task of learning multiple facets of a task. UNIPROMPT exploit the structure in the prompt optimization and use a clustering approach to group examples with similar task facets. Experimental results on multiple datasets demonstrate that prompts generated using UNIPROMPT achieve higher accuracy than human-tuned prompts and state-of-the-art methods.

### Strengths
(1) The paper introduces a new method for prompt optimization and consider multiple facets of a task and leveraging the structure in the prompt.
(2) The proposed clustering approach and two-tier feedback mechanism provide a systematic way to generate prompt edits that capture generalizable concepts.
(3) The experimental results on several datasets shows that UNIPROMPT outperforms human-tuned prompts and SOTA methods.

### Weaknesses
(1) I am skeptical about the current importance of prompt optimization. Prompt optimization is more of a need in an era when large models are not powerful (for example last year). Nowadays, the instruction model follows human instructions very well, and many of them are 0-shot, see llama-3.1 model card. I would like to hear the author's opinion on this.

(2) For the results in table 1, it is recommended to add an average column to make the presentation clearer.

(3) I found that on the ARC task, compared with the llama prompt, the optimized prompt led to a decrease in performance. Is there any explanation?

### Questions
N/A

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
This paper presents an improvement to current prompt optimization approach. It does so by clustering the input space and enabling the optimization algorithm to learn multiple facets of a task from a set of batched clusters. The paper discusses the empirical observation that inspires the improvement and conducts experiments to demonstrate its efficacy. Results suggest that the framework achieve better results than existent approach.

### Strengths
1. The paper is well-structured and the story is well-told. It starts with essential observations that motivate the improvements so that the approach bears heuristic justification. 

2. Experiments are comprehensive, including several baselines, and benchmarks of different types. Experiment results also provide strong support to the thesis of the paper.

### Weaknesses
My concern on the improvement is its generalization ability. The experiments cover hate speech detection, math, QA but there are many other task types not covered in this dataset. For example, OPRO and [Li et al 2024](https://arxiv.org/abs/2409.15199) ran experiments on BBH which contains a much more diverse task portfolio than presented in the paper. Since the proposed improvement centers around clustering the training examples, whether the samples can be cluster into meaningful subspace has a direct impact on optimization performance. But we don't see sufficient evidence to demonstrate the approach works on a divers task portfolio. 

Besides, the prompt optimization is very sensitive to the initial prompt and iterations (also discussed in Sec 2.1), but the reported metrics don't take the performance variation into consideration. I have concern on the robustness of the results.

### Questions
1. If I understand correctly, the wrongfully predicted training samples are clustered only once at onset, how does the algorithm handle the wrong samples after the optimization starts? Does it use them to generate feedback?

2. Did you try using other model families? How does the performance look like when the expert model is not as powerful as GPTs? 

3. The clustering is conducted through LLM, but this could be an issue when the number of examples increases. Did you try other clustering approach? which might make it feasible to dynamically cluster the examples along the iterations.

### Soundness
3

### Presentation
3

### Contribution
2
