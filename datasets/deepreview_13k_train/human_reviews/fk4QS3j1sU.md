# PoTable: Programming Standardly on Table-based Reasoning Like a Human Analyst

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Table-based reasoning has garnered substantial research interest, particularly in its integration with Large Language Model (LLM) which has revolutionized the general reasoning paradigm. 
    Numerous LLM-based studies introduce symbolic tools (\textit{e.g.}, databases, Python) as assistants to extend human-like abilities in structured table understanding and complex arithmetic computations. 
    However, these studies can be improved better in \textit{simulating human cognitive behavior} when using symbolic tools, as they still suffer from limitations of non-standard logical splits and constrained operation pools. 
    In this study, we propose \textsc{PoTable} as a novel table-based reasoning method that simulates a human tabular analyst, which integrates a Python interpreter as the \textit{real-time} executor accompanied by an LLM-based operation planner and code generator. 
    Specifically, \textsc{PoTable} follows a human-like logical stage split and extends the operation pool into an open-world space without any constraints. 
    Through planning and executing in each distinct stage, \textsc{PoTable} standardly completes the entire reasoning process and produces superior reasoning results along with highly accurate, steply commented and completely executable programs. 
    Accordingly, the effectiveness and explainability of \textsc{PoTable} are fully demonstrated. 
    Extensive experiments over three evaluation datasets from two public benchmarks on two backbones show the outstanding performance of our approach. 
    In particular, GPT-based \textsc{PoTable} achieves over 4\% higher absolute accuracy than runner-ups on all evaluation datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces POTABLE, a table-based reasoning method that simulates human analyst behavior through a staged analytical approach. The method combines a Python interpreter for execution with an LLM-based operation planner and code generator. The method mimics human-like logical stage split (initialization, row selection, data cleaning, reasoning, and answering) and open-world operation space. The authors demonstrate POTABLE's effectiveness through experiments on WikiTQ and TabFact datasets, showing performance improvements.

### Strengths
1. The paper provides a systematic refinement of existing table-based agents. By breaking down the process into well-defined stages and implementing careful error handling, POTABLE addresses common failure modes of general-purpose agents. The empirical results demonstrate that these refinements lead to meaningful performance improvements, showing the value of structured approaches to agent design.

2. The authors test their method across different datasets (WikiTQ and TabFact), model backbones (GPT and LLAMA), and conduct detailed ablation studies. The performance improvement over baselines (>4% on multiple datasets) suggests that the structured approach does offer tangible benefits over more generic agent implementations.

### Weaknesses
1. The idea of using LLMs with pandas for table reasoning has already been previously explored in various works. For instance, LangChain has implemented pandas agents [1] at least a year ago, and at least 2 paper [2][3] (and I think there are more as this is a paper one year ago) has discussed the relationship between agent-based and direct reasoning approaches for tabular understanding. Under this situation, the main contribution will be in providing a more refined (and maybe fixed) workflow for table reasoning, which might have diminishing returns with more capable models. 
2. The paper lacks a crucial analysis of token efficiency and alternative approaches. A key consideration for any agent-based system is whether the increased token consumption from multiple LLM calls is justified by the performance gains. For instance, an alternative approach using self-consistency with multiple single-pass attempts might achieve similar accuracy while being more token-efficient. Without this comparison, it's difficult to determine if the improved accuracy (>4%) justifies what could be a significant increase in token usage. The paper should have included a detailed analysis comparing token consumption with simpler approaches and demonstrating why their multi-stage workflow is more effective than alternative methods like self-consistency.
3. There are several fundamental limitations in current (especially programming-based) table agents. Specifically, these agents (including POTABLE) struggle with three key scenarios: (1) multi-table reasoning that requires joining or comparing information across tables, (2) hybrid reasoning that combines tabular data with textual context, and (3) handling irregular table structures with multiple headers or nested hierarchies. While these challenges may be outside the paper's intended scope, they represent critical real-world use cases that limit the practical applicability of such methods.

### Questions
- See weakness and:
- How do you envision POTABLE could be extended to handle multi-table scenarios or hybrid reasoning with both tabular and textual data or irregular table structures ?  
- As LLM capabilities continue to advance, would you agree or maybe disagree that the benefits of structured workflows might need to be reconsidered? (One could argue that giving more autonomy to stronger models - perhaps with fewer constraints on their reasoning process - might actually lead to better performance, but i would be interested in your thoughts on this trade-off between structure and autonomy.)

### Soundness
2

### Presentation
3

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
This work proposes a pure prompt-based method to solve reasoning that involves table, namely PoTable. The author proposes to split the process explicitly into several stages: initialization, row selection, data type cleaning, reasoning and final answering. These stages include prompting API LLMs for planning, and for using pandas package to manipulate the table. The experiments show the proposed method performs better on certain types of table reasoning tasks.

### Strengths
See below

### Weaknesses
## Novelty

PoTable is a pure prompt-based method with hardwired reasoning stages designed specifically for solving a certain type of table reasoning tasks. On top of API LLMs, PoTable is also equipped with tool usage and self-correction, but both of these techniques are widely studied in prior work on various types of reasoning. The highlighted human-like reasoning stage design lacks justification and is somewhat overfitted to a certain type of table reasoning, leading to poor generalization over other types of questions. That said, this work lacks novelty.


## Quality
Several methodological concerns undermine the paper's quality:

Hardwired reasoning stages:
- The authors claim that the 5-stage split represents "standard logic" (L85, L90), but there no direct evidence is provided to justify why these particular stages should be considered standard.
- Scalability issue: How flexible is this setup? Though it is claimed to be standard, can this approach handle general tabular reasoning scenarios? How does it perform with complex queries requiring merging tables? What about multi-step reasoning problems?  

Pipeline design choices not well-motivated or -justified:
- Why only use few-shot examples at the final stage?


## Clarity

This paper is generally easy to follow.


## Significance

As mentioned above, this work targets a specific type of table reasoning tasks that involve single-step, single-table reasoning. While being able to beat the baseline methods, the performance gain is moderate. More importantly, the introduced 5-stage reasoning significantly limits its application to other types of reasoning, further limits its impact on the field. That said, the significance is minor.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method, PoTable, to solving table-based reasoning tasks with two contributions: (i) logically standard reasoning and (ii) unrestricted operation tools.

### Strengths
1. The proposed method appears to be effective on the three datasets experimented. 

2. The analysis of PoTable performance on varied task difficulty and table size is interesting. It would be further informative if the result breakdown on baseline methods are also provided, so it tells more clearly on which category the proposed PoTable method provides the most increases.

### Weaknesses
1. Unclear unique contribution of the proposed method: particularly, it is unclear to me where two main component highlighted are unique contributions of this paper.

(i) non-standard logical splits: (first of all, this term is somewhat vague so suggest changing it.) This paper proposed “standard” stages including (initialization, row selection, data type cleaning, reasoning, and final answering), where previous works such as Chain-of-Table (https://arxiv.org/abs/2401.04398) and Datar (https://arxiv.org/abs/2301.13808) have proposed similar decompositions, yet it is unclear why the split proposed in this paper is “more standard” than existing ones. Adding some clarifications on this could be helpful.

(ii) constrained operation pools: many table-related works do not have a restricted operation pool, for example, they can use arbitrary Python programs (ReAcTable: https://arxiv.org/abs/2310.00815, Chameleon: https://arxiv.org/abs/2304.09842) or even allowing model self-designed new operations (TroVE: https://arxiv.org/abs/2401.12869) 

Overall, both dimensions claimed as novel in this work seem to be already explored by existing works. It would be helpful to highlight the differences of this work further to clarify the novelty aspect.
Further, it is not entirely clear to me why (i) and (ii) leads to human-like analysis, and what “human-like analysis” is defined/characterized in this work.

### Questions
1. How did you decide on the five steps as proposed in the PoTable method? And why do you believe that is the most "standard" split of the task? Can this split be generally applied to all table-reasoning tasks?

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
The study introduces PoTable, a novel method for table-based reasoning that effectively simulates human cognitive behavior by integrating a Python interpreter with a Large Language Model (LLM). This approach addresses limitations in previous methods by employing a human-like logical stage split and expanding the operation pool into an open-world space. PoTable uses an LLM-based operation planner and code generator to produce highly accurate, step-by-step commented, and fully executable programs. The method demonstrates strong effectiveness and explainability, achieving over 4% higher accuracy than competitors across multiple datasets.

### Strengths
- Tabular analysis is crucial for both research and practical applications, highlighting the relevance of this study.
- The proposed method, POTABLE, achieves state-of-the-art performance on selected evaluation datasets, outperforming existing approaches.

### Weaknesses
 1. I don't think Initialization and Final Answering are important enough to be count as stages.
2. The claim that your analysis stage split is human-like is too arbitrary. How do you know that human do tabular analysis in this way? Have you ever done any research about this? if so, please cite them in the paper.
3.  The evaluation datasets are not extensive enough. Evaluation on just two datasets cannot really support your concusion. For evaluation datasets, why did you choose to use both validation and test sets of WiKiTQ? is there any inherent difference between these two sets? The evaluation results in Table 1 actually show almost similar results for both sets.
4. The results analysis in the seconde paragraph in Sec 3.2 could be further improved. I think it is important to discuss the phenomenon that the difference between GPT and LLAMA is quite different across approaches, i.e., for WiKiTQ, GPT > LLAMA for Binder, Dater, GPT < LLAMA for Chain-of-Table, GPT = LLAMA for TabSQLify and PoTable. The same for TabFact.
5. In Figure 3, it is suggested to discuss why "removing data type cleaning (w/o Dty. Cle.)" gets the lowest scores. It would be weird if you ignore this result because it is so obvious in the figure.
6. I found that the max tokens of the backbone models used in the study is 2048 (Appendix A). Thus i am particular interested in that, if you put the full table in the prompt, how do handle the table with large content exceeding 2048 tokens?  Also, the code_base would also increase as the analysis stage goes ahead. 
7. In figure 11, the prompt contains several suggested operations when generating the reasoning plan. Would this be contradicted with the claim that the PoTable "extends the operation pool into an open-world space without any constraints." If not, please provide some examples to prove.

### Questions
See questions in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
