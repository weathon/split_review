# An Examination on the Effectiveness of Divide-and-Conquer Prompting in Large Language Models

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Foundation models, such as Large language Models (LLMs),  have attracted significant amount of interest due to their large number of applications. However, when handling tasks involving repetitive sub-tasks and/or deceptive contents, such as arithmetic calculation and article-level fake news detection, simple instructional prompts suffer from inaccurate responses. Existing works show that more complicated prompting strategies, such as Chain-of-Thoughts and Least-to-Most, can unlock LLM's powerful capacity in diverse areas. Recent researches reveal that simple divide-and-conquer prompting strategy, i.e. simply dividing the input sequence to multiple sub-inputs, can also substantially improve LLM's performance in some specific tasks such as misinformation detection. 
In this paper, we aim at examining the utility of divide-and-conquer prompting strategy and answer on which kind of tasks this strategy gets advantages. Specifically, we provide a theoretic analysis to  divide-and-conquer prompting strategy and help us identify the specific tasks where DaC prompting can bring performance boost with theoretic guarantee.
We then present two cases (\textbf{large integer arithmetic and fact verification}) where experimental results aligns with our theoretic analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the effectiveness of Divide-and-Conquer (DaC) Prompting. The author first provides a theoretical framework that can analyze how the divide-and-conquer strategy expands the expressive power of a fixed-depth log-precision Transformer. In this context, the author presents some conditions under which DaC has advantages compared to other prompting strategies. The author empirically validates this theory on tasks such as Large Integer Multiplication, Hallucination Detection, and Article-level Fact Verification, which require very long reasoning paths or contain deceptive contents.

### Strengths
The authors conducted a theoretical analysis of the Divide-and-Conquer prompting method, which is helpful for understanding the reasoning capabilities of large language models (LLMs) and is timely.

Providing the conditions under which DaC brings a performance boost has practical application value.

### Weaknesses
In the task decomposition stage of Algorithm 1 and Algorithm 2, hallucinations or intermediate errors also seem to occur. Based on the current version of the paper, it is not clear whether the errors in CoT stem from the subtask solutions rather than the subtask decomposition. I suggest conducting further statistical analysis on the types of errors in CoT and DaC.

Considering that the applicability of DaC may not be as broad as CoT and that the reasoning process may require more tokens, the potential impact of this paper might not be as significant as Feng et al. 2023. Therefore, this work appears to be somewhat incremental. Specifically, the paper does not adequately address scenarios where the decomposition itself might introduce errors or inefficiencies, which could limit the method's practical utility in complex real-world tasks. Furthermore, the paper needs to more rigorously analyze the trade-offs between the potentially increased token usage of DaC and its performance gains, especially when compared to more established methods like CoT. The lack of a detailed analysis of these trade-offs makes it difficult to assess the true value of DaC in resource-constrained environments.

### Questions
How do the token usage and inference time of DaC compare to those of CoT?

### Soundness
3

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
This paper tries to analyze the utility of the divide-and-conquer prompting strategy and answer the questions on which kind of tasks this strategy has advantages. The paper provides a theoretical analysis of the divide-and-conquer prompting strategy to identify the specific tasks where DaC prompting can bring a performance boost with a theoretic guarantee. The paper claims to present two cases where experimental results align with our theoretical analysis.

### Strengths
1. The paper mainly focuses on the theoretical view of a prompting strategy and tries to find experimental results that align with the theoretical results, which should be encouraged.

### Weaknesses
1. The presentation of the paper should be improved. For example, for the method, which is the main difference between ToT and DaC, from the description of the paper, it looks like DaC prompts LLMs to perform subtask decomposition first and then solve each subtask, while ToT does not distinguish between subtasks and general intermediate reasoning steps, just perform a tree-based reasoning process. Then, from Figure 2, DaC seems to solve tasks with homogeneous decomposition, is there any situation in which the depth of each subtask is not the same?
2. The proof part is also a little bit confusing for me. For example, theorem 4.1 seems trivial to me as all IO prompts can be seen as special cases of DaC prompts, which means IO prompts are a subset of DaC prompts, then the set of problems IO prompts can solve is also a subset of problems DaC prompts can solve, so there must be S(IO) in S(DaC).

### Questions
Please refer to the weaknesses part.

### Soundness
3

### Presentation
2

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
The paper examines the utility of divide-and-conquer prompting strategy, and summarizes two conditions under which DaC leads to performance gains when tasks satisfy both of these conditions. Meanwhile, the paper lists three applicable tasks and three inapplicable tasks, and conduct experiments on two tasks: large integer arithmetic and fact verification to make validation.

### Strengths
1. The paper theoretically proves the DaC and proposes two conditions that DaC needs to satisfy to bring performance improvement.
2. The paper select two tasks (large integer arithmetic and fact verification) for experiments to make validation on theoretic analysis.

### Weaknesses
1. The concept in condition 2 is too general, what does it mean to be subject to hallucinations or intermediate errors, and I think most tasks suffer from this problem, can this definition be more specific?

2. In the applicable and inapplicable tasks, I think the granularity of the 6 tasks is completely different, and the paper proposes to conduct experiments on two tasks large integer arithmetic and fact verification. Integer Multiplication and Integer Addition belong to large integer arithmetic. However, the remaining four tasks are not proposed at the same granularity, and the reasons for the selection of the six tasks should be described in detail in this paper. In addition to the three tasks that are applicable, what other tasks are applicable?

3. In this paper, how is the answer extraction of the LLMs to make experimental statistics. Can the 100% on some metrics in Table 3 be analyzed in detail?

4. DaC generally performs better in Integer Addition as the model capacity increases (GPT-3.5->GPT-4). At the same time, on the HaluEval dataset, baselines have a large difference in the performance of the two LLMs, while the DaC method has the similar performance as GPT3.5 in GPT-4. It is necessary to further explore the influence of the model parameters on DaC.

### Questions
1. The writing and presentation of the paper need further improvement.
There are some missing symbols and wrong words in line 33, line 197, line 343, line 436, and etc.
2. The publications of the references need to be corrected such as Zhou et al., 2022.

### Soundness
2

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
4

### Summary
The paper presents a theoretical and empirical analysis of the divide-and-conquer (DaC) prompting strategy in the context of large language models (LLMs). The authors argue that DaC can improve the performance of LLMs on specific tasks, particularly those involving repetitive sub-tasks or deceptive contents. The paper provides a theoretical framework to identify tasks where DaC prompting can be advantageous and supports these claims with experimental results from two case studies: large integer arithmetic and fact verification.

### Strengths
1. The theoretical claims are backed by empirical evidence from two distinct case studies, providing a comprehensive view of DaC's utility in both arithmetic and natural language processing tasks.
2. The study addresses a significant challenge in the application of LLMs, where tasks requiring long solution paths or dealing with complex and deceptive content are concerned. The findings have practical implications for prompt engineering in LLMs.

### Weaknesses
1. While the paper makes a strong case for DaC in specific tasks, it does not explore its applicability in a broader range of tasks or domains, which might limit the generalizability of the findings. For example, the authors only explore arithmetic and fact verification, but do not investigate tasks that require more complex reasoning or planning, such as code generation or multi-hop question answering. This narrow focus makes it difficult to ascertain whether the observed benefits of DaC are specific to the chosen tasks or if they can be generalized to other areas of LLM application.
2. At present, it is difficult to claim that the idea of the divide-and-conquer prompting strategy is novel, as there are many prompting strategies for LLM in-context learning. Besides, the paper doesn't compare with recent studies, such as Graph of Thoughts, and Program of Thoughts. The lack of comparison with these methods, which also aim to improve reasoning capabilities of LLMs, makes it difficult to assess the relative advantages and disadvantages of DaC. The paper should clarify how DaC differs from these approaches and under what conditions it might be preferred.
3. The theoretical analysis, while comprehensive, may be challenging for readers without a strong background in computational complexity theory, potentially reducing the accessibility of the paper. For instance, the paper uses concepts such as 'expressive power' and 'parallel sub-tasks' without providing sufficient intuitive explanations for readers who are not familiar with these concepts. This could make it difficult for a broader audience to understand the core arguments of the paper.

### Questions
1. How does DaC prompting compare with the latest prompting techniques or methods in terms of performance and computational efficiency?
2. Could the authors provide further insights into the robustness of DaC prompting and discuss potential sources of error or failure in the context of their case studies?

### Soundness
2

### Presentation
1

### Contribution
2
