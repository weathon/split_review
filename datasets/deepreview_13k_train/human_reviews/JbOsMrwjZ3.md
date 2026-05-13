# BioCoder: A Benchmark for Bioinformatics Code Generation with Contextual Pragmatic Knowledge

- Decision: Reject
- Scores: 8, 6, 6, 5

## Abstract
Pre-trained language models like ChatGPT have significantly improved code generation. As these models scale up, there is an increasing need for the output to handle more intricate tasks and to be appropriately specialized to particular domains. Bioinformatics provides an important domain. In this field generating functional programs poses additional notable challenges due to the amount of specialized domain knowledge, the need for complicated data operations, and intricate functional dependencies between the operations. Here, we present BioCoder, a benchmark developed to evaluate existing pre-trained models in generating bioinformatics code. In relation to function-code generation, BioCoder covers potential package dependencies, class declarations, and global variables. It incorporates 1026 functions and 1243 methods in Python and Java from GitHub and 253 examples from the Rosalind Project. BioCoder incorporates a fuzz-testing framework for evaluation, and we have applied it to evaluate many models including InCoder, CodeGen, CodeGen2, SantaCoder, StarCoder, StarCoder+, InstructCodeT5+, GPT-3.5, and GPT-4. The results highlight two key aspects of successful models: 1) that they contain specific domain knowledge of bioinformatics (beyond just coding knowledge); 2) that they accommodate a long prompt with full context (i.e. functional dependencies).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have introduced a benchmark named BioCoder for code generation in bioinformatics. BioCoder covers codes in Python and Java, featuring examples from the Rosalind project. The benchmark creation process is detailed, encompassing preprocessing, evaluation metrics, and baselines. Additionally, several state-of-the-art models are evaluated on the benchmark, and their performance is reported highlighting the superiority of black-box models over open LLMs for code.

### Strengths
* The proposed benchmark is an essential collaboration in the field of Bioinformatics.
  * The processes for dataset creation, preprocessing, and other steps are very well described, including examples and explanations.
  * The authors test most of the state-of-the-art models for code generation on the proposed benchmark, reviewing each and also fine-tuning one of them.
  * Every prompt is exemplified in the Appendix with a code snippet.
  * Another interesting comparison is the one between BioCoder and CoderEval.
  * Every model is analyzed and discussed (very large Appendix).

### Weaknesses
* Explanations of the prompt configurations, shown in Table 4, should come in the Table description or somewhere in the main text, not only in the Appendix. Specifically, the differences between Zero-shot, Zero-shot-COT, Few-shot, and Few-shot-COT need to be clarified for readers unfamiliar with these prompting techniques. Providing a concise definition of each in the main text would significantly improve the paper's accessibility.
* It Would be interesting to have a human evaluation or experiment considering the descriptions as a way to bring more validation to the GPT3.5 creation. While the automated evaluation using GPT-3.5 is a good starting point, a human evaluation would provide a more nuanced understanding of the quality and accuracy of the generated code descriptions. This is particularly important for assessing the clarity and unambiguity of the descriptions from a human perspective, which might differ from the model's assessment.

### Questions
-

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a large-scale benchmark, BioCoder, which is devoted to assessing the capability of LLMs regarding code generation, specifically in the field of bioinformatics. The authors collect 1026 functions and 1243 methods in two programming languages (Python and Java) from GitHub and 253 examples from the Rosalind project to form a relatively intricate dataset to evaluate the LLMs' code generation abilities from various aspects. The authors conduct multiple steps to ensure the validity and unbiasedness of the constructed benchmark. In particular, 10 different LLMs (including the fine-tuned one) are evaluated on BioCoder, and the experiments reveal what factors can potentially affect the performance of LLMs while tackling challenging code generation tasks.

### Strengths
1. Timely and vital problem.
2. A valuable large-scale benchmark for code generation, including specialized domain knowledge.
3. Comprehensive evaluation with multiple LLMs.
4. The presentation is in a good manner, and the paper is easy to follow.

### Weaknesses
I appreciate that this paper has provided a valuable benchmark to the communities, as the new benchmark can potentially help researchers and practitioners in this direction. However, there are several concerns regarding the methodology and evaluation of this paper, which I will elaborate on below:


1. My biggest concern is the lack of justifications for the testing framework for Python and Java functions in BioCoder. The authors state, "... we employ a custom syntax to indicate the insertion points for custom randomly generated test cases." How are the test cases "randomly generated" and inserted into the context files? I did not find any detailed explanations in the main paper or in Appendix L and Y. In particular, Appendix L only briefly introduces the pipeline of the testing framework, how does such an approach deliver "a secure and efficient testing framework, promising robustness in the evaluation of generated code"? The authors need to clarify more about the generation of the test cases, including the specific algorithms used for random value generation, the range of these values, and how these are adapted to different data types and function signatures.

2. In addition to the previous point, for Rosalind functions, the authors mentioned, "...the output of this execution is compared with the cached golden code output." Why and how are the generated codes compared with the gold code outputs? I do not find any experiment results that illustrate the comparison outcomes. It is unclear if the comparison is a simple string match or if more sophisticated methods are used, especially given the potential for variations in output formatting or numerical precision.

3. Another concern is the implementation of correction mechanisms which rectify minor syntax and style errors. What kind of syntax and style errors can be considered "minor" with no impact on the functionality of the generated programs? As the authors take invalid syntax and runtime error as two major failure reasons in the following error distribution analysis, I recommend further justifying such correction mechanisms, which may affect the validity of the analysis results. The paper should detail the specific rules and heuristics used for these corrections, and how they are validated to ensure they do not introduce unintended changes in program behavior.

4. Table 4 summarizes the performance of the studied LLMs on BioCoder w.r.t 4 different types of prompt formats. However, the explanations of the different prompt versions are placed in Appendix I, which makes Table 4 hard to understand. Moreover, Appendix I only gives explanations with examples of the prompts in each version; nevertheless, I am looking for some high-level guidelines for the prompt design. Namely, how the five prompt versions are proposed? Are they from existing lectures or experimental experience? What are the characteristics of different prompt formats? The paper should provide a more systematic explanation of the prompt design choices, including the rationale behind each prompt type and how they are expected to affect the model's performance.

5. The discussion of the experiment results seems shallow to me. In section 5, the authors consider there is an inverse relationship between the length of the input prompts and the performance of the generated codes. However, from Table 4 and Appendix I, the Necessary only prompts have relatively shorter prompts but lower passing rates compared to uncommented and Summary at Top/Bottom in most of the studied LLMs. The author may elaborate more on the perspectives of prompt structures and contents instead of just the length of the prompts. The analysis should delve deeper into the interaction between prompt structure, content, and model performance, and consider factors beyond just prompt length, such as the presence of comments, the order of information, and the type of context provided.


Minor Comments

1. The "Summary At Bottom" results illustrated in Appendix U seem incomplete (no row for GPT-4). 

2. From section 3.4, "Our testing framework starts with a manual review of selected functions, leading to the creation of a context file and a golden code file for each problem (see Figure 3)". I do not find how Figure 3 is correlated with the testing framework, Figure 17 in Appendix R may be a better example.

### Questions
1. The details of the testing framework and the corresponding effectiveness should be discussed.

2. For Rosalind functions, why and how are the generated codes compared with the gold code outputs?

3. What are the guidelines while designing the 5 different prompt styles for the subject LLMs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the function-level code generation challenges within the field of bioinformatics and evaluate the effectiveness of current leading pre-trained  large models (including InCoder, CodeGen, CodeGen2, SantaCoder, StarCoder, StarCoder+, InstructCodeT5+, GPT-3.5, and GPT-4) in generating code in the realm of bioinformatics.  To accomplish this, the paper utilized web scraping techniques to extract data from 1743 bioinformatics-adjacent GitHub repositories on GitHub, constructing and presenting a benchmark dataset named BioCoder. This dataset offers a reliable evaluation standard for code generation tasks within the field of bioinformatics. The main contribution of this paper comprises code parsing tools, proposed dataset, docker environment and comprehensive evaluations.

### Strengths
The dataset, evaluation in this paper is particulary well-established. The implementation is very solid, and the presentation in this paper is easy to follow. It has the poteintial to become a standard evaluation benchmark for bioinformatic code generation.

### Weaknesses
The article includes an appendix that might be too long for the readers, and the content in the appendix is referred from the main body for multiple times. It is better to make the paper more self-contained if it is accepted to be published in conference proceedings. Moreover, the author should clearly point out the main technical contribution of this paper. I don't quite catch the challenges for benchmarking bioinformatics code generation compared to other domain specific languages. The paper does not sufficiently address how the BioCoder benchmark differentiates between a model's domain-specific knowledge and its general code generation capabilities. While the authors mention tasks like sequence alignment, phylogenetic analysis, and protein structure prediction, it remains unclear how the benchmark isolates and evaluates the understanding of domain-specific knowledge versus general programming proficiency. This distinction is crucial for assessing the true value of the benchmark in evaluating models for bioinformatics tasks.

### Questions
1. How does the benchmarking for bioinformatics code generation differs from the benchmarking for other domain specific languages?
2. What is the key technical contribution for the BioCoder, that is strongly related to benchmarking bioinformatics code generation?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
## Summary
Authors construct a dataset for code generation targeting the bioinformatics domain.

They use a combination of automated fetching of code from GitHub combined with manual inspection of code, and creating test cases.

They ran existing popular LLM models on their dataset and reported how they perform.
This adds additional value to the paper, showcasing that all LLMs struggle on the task they created.

### Strengths
+ **Important problem**. I like the problem being tackled. There is a great challenge in enabling code generation for domain specific tasks.
+ **Combination of automated and manual inspection**. Manual inspection can ensure better quality.
+ Authors created a repository with code and thus are enabling **knowledge sharing**. I suppose they plan to open source it later as well.

### Weaknesses
 - **Paper writing**. Can be significantly improved. Flow of the paper is inconsistent, sometimes containing phrases which are not previously explained.
- **Inconsistent results and motivation**. The results shown in the evaluation don't testify much about the usefulness of the constructed dataset for the challenges authors initially propose tackling.

### Questions
## Other Comments
- Abstract. I would expect that in the second part of the abstract (after you motivated the problem of difficulty of correctly generating code for domain specific areas such as bioinformatics) you provide some evidence on why your dataset is either: (a) useful to help train models that achieve better performance for the given domain or (b) it provides a good measure to estimate whether an LLM is effective for the code generation in the field of bioinformatics (or specific subarea of bioinformatics coding domains).

- Abstract. Sentence "In relation to function-code generation ..." is unclear given the previous sentences. Reformulate.

- Abstract. Sentence "It incorporates 1026 functions and 1243 methods in Python and Java from GitHub". You probably need to add "respectively" after the word "Java".

- Introduction. I would like to see some discussion or evidence of why the dataset you constructed is an effective dataset for the field of bioinformatics. Some of the questions that are still left in my mind are:
    - What is the range of problems/areas bioinformatics code typically encompasses? 
    - What position/importance in the field of bioinformatics is occupied by the tasks you include in your dataset? I see some information in the appendix, but ultimately this is a crucial factor in the paper, so there needs to be a good evidence about it in the main paper.
    - Ultimately, what is the value that a bioinformatics programmer, who wants to use an LLM to help writing his/her code, will gain by evaluating LLMs on your dataset? Can he/she gain some level of confidence that LLM that works well on your dataset, will perform better on his/her problems?
    
- Introduction. You mention that you create "a new high-quality dataset". It may be a high-quality dataset, but it would be good to add some specific numbers or evidence on why it is so.

- It would be great if in Figure 2 (describing the overall process of constructing the dataset) you indicate which parts of the process are done manually, and which part is automated.

- Related Work. "We ensure each function demands a certain level of domain expertise in bioinformatics". Can you add briefly how? It can be as simple as "via manual inspection". But, later on you need to elaborate further how the manual inspection was performed to ensure that.

- "golden code file". While one can guess what the meaning of the golden code file is, it would be good to explain. This phrase is used only at a single place in the paper.

- "Summary Only prompts". When encountering this phrase in the paper for the first time, it's not obvious what this means. One can look at Figure 3 and infer, but it would be good to have a natural flow in the main body of the paper itself.
    - If your concern is space, I would rather remove results of certain prompt types from the main paper, and put them into the appendix. Then, for a single version of the prompt I would explain in detail in the main paper how it is constructed.
    - Also, Figure 3 is not elaborated inside of the paper.

- Table 4. "Results are in %". I would write something like: results are expressed in percentage.

- I would add line numbers for the review purposes so reviewers can easily refer to a given part of the paper in their comments.

- Table 1. Spell out the abbreviations somewhere for P.C., P.L., C.C., C.L.

- Table 6. I would suggest using percentage instead of raw numbers for showing distribution of test error types. You can also include information about total number of test cases vs number of failed cases. You could possibly restructure the table to remove repetitive "Failure Reason".

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
