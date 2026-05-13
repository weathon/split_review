# Does Instruction Tuning Reduce Diversity? A Case Study Using Code Generation

- Decision: Reject
- Scores: 3, 5, 6, 1

## Abstract
Large Language Models (LLMs) should ideally generate diverse content for open-ended prompts (e.g., variety in cooking recipes). Anecdotal evidence has suggested that preference-tuned language models struggle to generate diverse content, which would have important implications for how we align models. However, research on this question has been limited by the difficulty of measuring diversity, which naively would require costly human evaluation. We propose to leverage code as a means to study semantic diversity, since code has executable semantics. To this end, we create an open-ended program synthesis task, enabling us to cheaply evaluate the diversity of hundreds of thousands of generations. Using our methodology, we find that while instruction-tuning reduces syntactic and lexical diversity, it can actually increase semantic diversity. We also study the effect of model size and prompting technique on diversity. Finally, we find that neural diversity metrics correlate poorly with our semantic diversity metrics, highlighting the need for more rigorous methodologies for evaluating diversity.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the impact of instruction tuning (via supervised finetuning (SFT) or preference-tuning (PT)) on output diversity, using code as a medium for semantic diversity through test case execution. Despite limitations in experimental scope (e.g., limited problem set, comparison using different baselines for SFT and PT), the study presents three notable findings: (1) optimal temperature values for achieving semantic diversity in code, (2) both SFT and PT increase semantic diversity, and (3) PT achieves greater semantic diversity than SFT.

### Strengths
- Figure 1’s temperature plot reveals potential improvement over CodeT's [1] default T=0.8, suggesting that T=0.9 or T=1.0 may yield higher diversity. This deserves further elaboration.

[1] Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, & Weizhu Chen (2023). CodeT: Code Generation with Generated Tests. In The Eleventh International Conference on Learning Representations.

### Weaknesses
 - The experimental results are limited to 21 competitive programming problems, raising concerns about generalizability.
- The comparison between CodeLLama (based on LLama2) and LLama3(.1) for SFT vs. PT may be problematic, as the use of distinct model versions could affect the observed diversity differences. A controlled experiment using LLama3(.1)-based SFT would improve reliability.
- Instruction-tuned LLM diversity could be influenced by the training set’s diversity. It would be beneficial to include a controlled comparison of LLMs without instruction tuning and LLMs with tuning that vary in training set or trajectory diversity.
- The finding that execution-based diversity differs from lexical/syntactic diversity is unsurprising. Prior work (e.g., APPS [2]) has documented similar discrepancies between lexical-based (BLEU) and execution-based metrics. Additionally, Section 4.2 reiterates results seen in counterfactual code augmentation research [3,4]. Further, the statement on lines 327-338 about the difficulty of semantic differentiation in code contrasts with the use of code to study semantic diversity.
- CodeBERTScore is outdated. More current options include UniXCoder [5] or CodeExecutor [6]. Another approach could leverage LLM-based evaluation, such as in CHASE-SQL [7], which employs a fine-tuned LLM as a code-pair verifier.
- The vagueness in problem descriptions makes it difficult to evaluate functional correctness and limits scalability, as the problems need manual abstraction and the evaluation relies on model-based alternatives or human effort. The lack of constraints on expected outputs, where random word sequences cannot be considered valid answers, further complicates the evaluation process.

### Questions
- Could you elaborate more regarding the best semantic diversity in Figure 1?
- Could the number of problems be increased to enhance generalizability?
- Could SFT and PT be compared on identical base models, for instance, by adding an SFT baseline trained on LLama3.1-base?
- Could a controlled comparison be added for LLMs with and without instruction tuning, varying training set or trajectory diversity?
- Could CodeExecutor be adopted for neural diversity evaluation?
- Could an LLM-based neural diversity metric, such as in CHASE-SQL, be added?

### Soundness
3

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
3

### Summary
This work explores the impact of instruction tuning on the ability of Large Language Models (LLMs) to create diverse outputs. For their empirical analysis, they focused on code generation tasks, which allow for automatic verification of correctness via code execution. To measure code diversity, they introduced a holistic evaluation that encompasses semantic, lexical, syntactic, and neural diversity. The key contribution of this study is a methodology for evaluating LLMs' capacity to generate diverse code outputs. Additionally, they investigated the relationship between model size and diversity metrics.

### Strengths
1. The research focuses on a relevant matter, as there are few established evaluation frameworks in place to assess the capabilities of large language models (LLMs) in terms of diversity.

2. The study is not only theoretical but also includes several empirical demonstrations, providing tangible evidence.

### Weaknesses
1. The dataset construction could benefit from more detailed explanations.
2. The overall presentation of the study requires improvement to enhance clarity.
3. The study's findings regarding the research question, "Does instruction tuning reduce diversity?", are not conclusive. 
4. The contribution appears insufficient for a comprehensive paper, but it could form the basis of a shorter piece, such as a research agenda exploring this topic further.

### Questions
### Comments and suggestions on Soundness
The authors utilized 21 handcrafted abstractions derived from CodeNet, along with corresponding test cases sourced from AlphacaCode, as the foundation for the dataset. Unfortunately, further specifics are inadequately detailed in the appendix, making it challenging to evaluate the integrity of the data collection procedure.

### Comments and suggestions about Presentation
1. The overall paper outline needs improvements. For example, as the study requires of multiple concepts and terminology to set the background (e.g., approaches to measure LLMs diversity, types of LLMs, instruction-tuning types, NLP techniques), I suggest including a stronger Background/Related Work section in the main paper. As a second example, I suggest creating a flow chart figure that clearly paints the big picture followed to create the dataset. 
2. Grammar and Narrative. The paper needs general proofreading to improve quality. These are a few typos that I took note of: ‘the the’ (line 389), ‘We’ (line 296).

### Questions
1. Why are you presenting this work as a case study?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a novel strategy for studying semantic diversity by focusing on code generation, illustrating some interesting properties of the output diversity for LLM open-ended generation.

### Strengths
1. The semantic diversity and other diversity measurement is crucial for openended tasks to evaluate the generation of models in terms of creativity, randomness, etc. 
2. The metric devised by the authors makes for measuring model output diversities. 
3. The most interesting part is the insights coming from the experiment results, offering fresh arguments for openended code generation diversity.

### Weaknesses
The major concerns are the meaningfulness of studying diversity and the generalizability of conclusions to general-domain openended generations.

1. Why is it meaningful to study diversity for LLM open-ended generation? From my perspective, it may contribute to more effective solution searching if we scale up the inference computation (like o1). But this is not discussed in this work, so whether only studying the diversity is  meaningful remains uncertain.
2. Code generation is a special case in open-ended generation: it usually has a "correct" output. As the semantic diversity is measured by considering the model output, then why it matters when it generates diverse outputs while only one of them is correct? Isn't it true that we only care about whether it covers the correct output?
3. Whether the conclusions obtained generalizable to the general-domain openended generation? I think it's hard to evaluate, and at the same time, the answer might be no.

### Questions
Can you elaborate more on the benefit of higher response diversity other than some applications like creative writing?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors conduct a case study on how instruction tuning affects the diversity of generated programs. Through the study, the authors find that instruction tuning reduces the lexical and syntactic diversity of generations but increases the semantic diversity of generations.

### Strengths
There are several strengths of the paper:
- The overall structure is clear and easy to follow.
- The authors conduct experiments on several Llama models.
- The authors evaluate the diversity from multiple dimensions.

### Weaknesses
The contributions and the setups are very limited, specifically:
- There is no evaluation of correctness metrics. Representative benchmarks like HumanEval [1] and BigCodeBench [2] should be included.
- Neural diversity like CodeBERTScore is not very appropriate here. Prior works like ICE-Score [3] show that CodeBERTScore is very weak compared to the evaluators based on LLMs as Judges. For example, the authors should consider using ICE-Score instead of CodeBERTScore.
- The conclusion that "Program semantics may be harder to model than natural language." is a bit wrong, as BERTScore itself is not robust [4-6]. There is no reason why CodeBERTScore should accurately reflect the program's correctness.
- The open models included in the evaluation are not diverse. The authors should use other Code LLMs, such as StarCoder2 [7] and CodeQwen [8].
- The training setups are not documented, and the results could be questionable.
- The experiments are Python-only. The authors should conduct evaluations on more programming languages.
- There is no related work on Code LLMs, code generation, and coding benchmarks.

### Questions
- What's the column N in the tables?
- There is a lack of motivation to conduct investigations on code generation over text generation. The authors should provide sufficient explanations.

### Soundness
2

### Presentation
2

### Contribution
1
