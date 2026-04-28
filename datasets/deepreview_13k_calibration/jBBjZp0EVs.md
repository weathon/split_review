# Exchange of Perspective Prompting Enhances Reasoning in Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Large language models (LLMs) have made significant advancements in addressing diverse natural language processing (NLP) tasks. However, their performance is often limited by inherent comprehension of problems. To address this limitation, we propose Exchange-of-Perspective (EoP), a novel framework designed to exchange perspectives across different definitions of problem, so that it can break the fixed mindset from any particular formulation of the question. We conducted extensive and comprehensive experiments on 8 benchmarks. The results show that EoP can significantly improve performance. For instance, compared to the non-commutative baseline PHP, with GPT-3.5-Turbo and EoP, we observe a 3.6% improvement on AQuA (60.6% → 64.2%), while GPT-4-powered EoP demonstrates a 7.7% overall accuracy enhancement on Math (53.9% → 61.6%) and a 3.5% improvement on OlympiadBench Maths (43.5% → 47.0%) when using Qwen-2.5-72b.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a prompting framework Exchange of Perspective (EoP) for improving LLMs performances. The key idea is to rephrase the questions in different ways, so that LLMs can incorporate different understandings and perspectives of the same question. To be specific, this framework first formulates the original question to be an augmented question, and then asks LLMs to generate answers for both the original question and the augmented question. Then, it will refine the answer to the original question by incorporating the answer to the augmented question, and vice versa. This exchange of perspectives across two branches can be repeated for several iterations, until some criterion has been satisfied, e.g., when the two branches reach consensus, or one of the branches converge to a stable answer.

### Strengths
- The motivation of exploiting different definitions of the same question is insightful. This focus on the question on the input side, rather than the reasoning process on the generation side, opens up a new direction for improving LLM performance, which can be impactful.

- This framework further exchanges reasoning processes across two questions, so that it can break the fixed mindset from any particular formulation of the question, leading to more robust and accurate answers. This idea is also novel to me.

- This prompting framework is simple and straightforward to apply to any LLMs. It can also be coupled with any advanced prompting methods, such as CoT+EoP.

- The experiments demonstrate improvements across seven datasets for math and arithmetic reasoning, compared with several strong baselines. The analysis provides some interesting discussion such as the ablation study of the effectiveness of exchanging perspectives and comparisons between different question redefinition methods.

- The paper is well written and easy to follow.

### Weaknesses
 - This work is a bit incremental compared to PHP. The all use previous answers to refine the answer in multiple iterations, and the difference is that EoP uses prior answers from the other branch as hints.

- Due to the iterative and two-branch nature of this method, this will significantly increase the cost.

- The improvements of this method for arithmetic reasoning in Table 1 and Table 2 look marginal compared with the previous state-of-the-art methods.

- The choice of datasets is narrow because it focuses mostly on math and arithmetic reasoning.

- Only GPT family models (GPT-3.5-turbo and GPT-4) have been tested.

### Questions
- Does your method work for other types of reasoning tasks, such as logical reasoning, or BBH dataset?

- Does your method work for other models other than GPT?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Exchange of Perspective Prompting (EoP), a novel framework designed to improve the reasoning abilities of LLMs in complex reasoning tasks. Unlike traditional methods such as CoT and PHP, EoP reformulates a question into an augmented version, allowing the model to address the query from diverse perspectives. By iteratively swapping responses between the original and augmented questions, EoP creates a feedback loop that cross-checks answers from various angles until the termination condition is met. Results show that EoP outperforms existing baselines on reasoning tasks, highlighting the importance of external perspectives in enhancing the reasoning capabilities of LLMs.

### Strengths
The main strength of the paper is its introduction of EoP as a novel framework to improve reasoning in LLMs. This paper focuses on reformulating questions externally, allowing cross-checking of answers through feedback loops from alternate perspectives, rather than relying on internal logic as seen in methods such as CoT. This design shows that creating augmented branches and proceeding with EoP can improve reasoning accuracy and surpass existing baselines in reasoning datasets. By integrating feedback from varied question interpretations, EoP demonstrates high performance in handling complex reasoning problems, which is crucial for applications where reliable multi-step reasoning is essential. Lastly, rather than using a fixed number of iterations, EoP includes termination conditions, allowing the model to stop once stability is reached, demonstrating flexibility as the model stabilises in its performance.

### Weaknesses
The EoP framework relies on an iterative feedback loop until a termination condition is met, which results in a significant increase in computational cost compared to CoT prompting. The paper does not appear to discuss computational time or cost in detail, such as the time per instance or the number of GPUs required, given that only GPT models are used. Solely using GPT may not be sufficient to showcase how EoP outperforms other existing baselines. For instance, it is unclear how open-source models like llama, Qwen2, among others, would perform under the EoP framework. Would these smaller models be more prone to generating inaccurate information or hallucinations during the iterative feedback process? Testing EoP with a wider variety of models would strengthen the validity of its results, and I would consider raising the score if more models were tested. Additionally, while EoP demonstrates accuracy improvements in complex reasoning tasks, its applicability to a broader range of reasoning tasks, such as GPQA and other challenging datasets, remains unexplored. It is also unclear if the method is limited to mathematical reasoning or if it extends to other domains within the Olympiad benchmark. 

Lastly, the paper does not investigate the potential for EoP-induced errors that might arise from question augmentation. LLMs do not always rephrase questions accurately; for instance, if the model rephrases questions inaccurately, it could compromise the faithfulness of the EoP process. No studies or manual annotations appear to have been conducted to assess how these rephrasing inaccuracies may impact final outputs, leaving the reliability of EoP in question for some reasoning tasks. Furthermore, if the rephrased outputs are incorrect, the paper does not discuss potential strategies to mitigate this issue.

### Questions
A few follow-up questions: I’m curious about how EoP would perform on questions involving high reasoning complexity, such as Olympiad-style questions. Given the need for complex reasoning in such questions, would EoP still be able to arrive at correct answers? Additionally, if the questions are relatively complex, how many reasoning iterations would be required in the EoP process? Secondly, what happens if smaller models, such as llama-3.1/3.2, Qwen2-72B, or perhaps other closed-source models, are used? Lastly regarding faithfulness in the EoP process, as mentioned in the weaknesses section, I wonder if there are conditions under which the model may rephrase questions inaccurately. If this occurs, how might it impact the final answer, and what precautions could be implemented to prevent error propagation within the iterative feedback loop?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new framework Exchange-of-Perspective (EoP) to incorporate external perspectives by swapping answers for the same question presented with different definitions. 

The paper conducts extensive experiments across various complex reasoning tasks to verify the effectiveness of EoP.

### Strengths
The strengths of this paper are listed as follows:
1. The paper is well organized in structure, which helps me better understand the research ideas of the authors.
2. The experiments are detailed, covering multiple tasks and multiple different datasets. EoP is compared with multiple baselines.

### Weaknesses
The weaknesses of this paper are listed as follows:
1. **Redundant Expressions.** I don't like the expressions in Section 2.1. I think the explanations of the method EoP is too redundant and complex. These cumbersome symbols and formulas do not help me better understand how EoP is implemented, but instead add to the burden of reading. I think it is better to simplify this section.
2. **Limited Novelty.** Actually, it is not surprising that the accuracy of the model's answers can be improved by rephrasing and rewriting the prompt words. Moreover, the rewriting techniques used in this paper is relatively trivial. Some existing work have proposed such algorithm for prompt engineering (https://arxiv.org/abs/2310.04451).

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors aim to enhance the reasoning ability of LLMs through self-improvement by modifying question descriptions to help LLMs better understand the problems. They introduce **PEC** and **QR** to diversify question descriptions and form the original branch and the augmented branch. They append the exchanged answers from the two branches to progress integrated answering. Comprehensive experiments are conducted on several arithmetic and math datasets, and the results demonstrate that the **EoP** method achieves the best performance. Also, the authors provide a detailed analysis of the effectiveness of **EoP**.

### Strengths
- The paper proposes a straightforward method to improve the reasoning capabilities of LLMs, showing notable improvement in the math datasets and a minor increase in arithmetic datasets.
- The authors provide a detailed analysis of EoP's effectiveness, including the prompt settings and iteration numbers.
- The paper is well-written and easy to follow.

### Weaknesses
 - The usage of **PEC** and **QR** may have limitations. While these techniques might appear effective for simpler tasks, it is unclear whether they hold for complex math questions like complex application questions or proof questions. It would be beneficial for the authors to provide human annotation or proof for these complex cases. Specifically, the rephrased questions consistently exhibit a lower pass rate compared to the original questions, suggesting that the LLMs may struggle to accurately rephrase complex questions, especially those with intricate logical flows, such as Olympiad-level problems. These questions often rely on many premises and a coherent logical structure, and it is unclear if LLMs can consistently represent such complexity correctly. A detailed case study and human annotation should be conducted to analyze this issue.
- Since EoP needs the original branch and the augmented branch to agree with each other, the time and cost should be reported as the efficiency and the effectiveness of the methods should be a trade-off. From my perspective, a single iteration in EoP requires double the inference time compared to PHP. Therefore, when considering the overall cost and time, EoP demands approximately four times the resources of PHP.
- Although the authors use multiple datasets from arithmetic and mathematics domains, the minor improvement in arithmetic datasets might be attributed to the inherent variability in LLM outputs. For math datasets, the performance of EoP lags in certain aspects, such as InterAlgebra and Precalculus, indicating that EoP may have limitations when applied to specific topics. It would also be interesting to see how EoP performs on more challenging benchmarks, such as **OlympiadBench (He et al., 2024)**. Furthermore, it is unclear why EoP underperforms in *InterAlgebra* and *Precalculus* tasks on the MATH dataset, especially when compared to previous state-of-the-art reasoning methods.
- The authors limit their experiments to OpenAI models, which may not be sufficient to demonstrate the general applicability of EoP. Testing on other models, such as Llama 3.1, would strengthen their claims. 
- EoP involves multiple iterations, unlike metrics like CoT which require a single step. This introduces an unfair comparison in terms of inference cost and time. Additionally, it would be interesting to compare EoP's performance with massive sampling approaches to see that under the same cost, can EoP make a huge difference.
- The implementation of the baselines mentioned remains vague. The prompt and some hyperparameters are missed like the temperature used.

### Questions
- In the paper, only the answers from the augmented branch and the original branch are exchanged. If we retain two original branches and conduct **EoP** as normal, would we achieve similar results? In other words, does changing the question description actually make a difference in terms of improving the answer quality? This requires further clarification.
- Can the authors elaborate on why EoP fails in certain areas of the MATH dataset?

### Soundness
2

### Presentation
3

### Contribution
2
