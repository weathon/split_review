# $\textbf{PLUM}$: Improving Code LMs Using On-Policy Preference Learning Powered by Automatic Test Cases

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 8, 6

## Abstract
Preference learning provides a promising solution to address the limitations of supervised fine-tuning (SFT) for code language models, where the model is not explicitly trained to differentiate between correct and incorrect code.
Recent findings demonstrate that on-policy data is the key to successful preference learning, where the preference data is collected using the same policy LM being trained.
Inspired by this, we propose PLUM,
an on-policy $\textbf{P}$reference $\textbf{L}$earning framework A$\textbf{u}$gmented with test cases for code L$\textbf{M}$s.
The framework operates in three key stages: (1) automatic generation of test cases from natural language instructions, (2) creation of a preference data by evaluating candidate code solutions sampled from the policy, which can then be used to (3) train the policy LM. PLUM levitates the need to train reward models, allowing for large scale on-policy and online preference data collation. 

PLUM is evaluated on both standard benchmarks (HumanEval, MBPP) and more challenging ones (LiveCodeBench), delivering substantial improvements over original SFT'ed models and other execution-feedback-driven approaches. We show PLUM benefits are consistent across various widely-used code LMs even they have been well-trained with SFT. For example, PLUM increases pass rates by up to 4.8% on average on standard benchmarks and 11.8% on LiveCodeBench, demonstrating its effectiveness and generalizability. We also demonstrate the benefits of on-policy and online preference learning

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the application of preference optimization on code language models. To obtain the preference data over pre-defined prompts, the paper follows previous work and uses GPT-4 to automatically generate unit tests (filtered with consistency checks) which are subsequently used to determine whether on-policy code solutions are functionally correct (i.e. preferred) or not (i.e. dis-preferred). 

The experiments focus on applying the DPO and KTO methods over these derived data and comparing against SFT and RL (limited to Reflexion) training across multiple models and datasets. The results show consistent improvement of preference optimization over the baselines.

### Strengths
- The experiments demonstrate that the proposed PLUM methodology leads to consistent improvement over baselines across many models and datasets.
- The experiments are robust, covering many models and benchmarks.

### Weaknesses
 - The novelty of the proposed work seems limited to the application of preference optimization over code. The on-policy data are obtained following previous work and the benefits of on-policy vs. off-policy training and test-cased filtered data vs. execution filtered data has already been demonstrated in previous work as well (i.e. Le et al. 2022, Gorinski et al. 2023, Liu et al. 2023).
- The motivation of the paper is somewhat unclear. Preference optimization is generally used to align LLM output to human values, e.g. reduce harmful and toxic expressions. In terms of code solutions that are strictly correct or incorrect (based on functional execution over unit tests), RL or contrastive learning over online signal seem more appropriate, and already explored in previous work. The paper should directly compare against those methods (e.g. CodeRL, DeepSeek-Coder-V2, etc.) instead of Reflexion.
- The presentation of the paper could be improved, with the tables being ordered consistently with how the corresponding experiments are introduced. Corresponding tables and figures should also be moved closer to where they are first referenced.
- Preference optimization over code has been explored in previous work (Miao et al. 2024, Zhang et al. 2024, Gee et al. 2024). While this work can be considered concurrent, the paper would benefit from discussing it.
- The methodology seems to require a more powerful model (than the one being trained) to generate the unit tests. Have the authors explored using the policy itself to generate the unit tests?
- Performing SFT over OSS-Instruct, Evol-Instruct-Code and ShareGPT may not necessarily translate to improvements in MBPP and HumanEval datasets. SFT may be forcing models to adapt to out-of-domain prompts resulting in lower performance (and an unfair baseline). The benefits observed in PLUM could be due to these datasets being filtered through on-policy consistency. 
- Many tables are underexplained and potentially misleading (the best results are not always bolded, as in Table 2, 5 and 7). Please clearly indicate which baseline is used for each experiment. Figure 2 is particularly unclear, and (if this reviewer's interpretation is correct) in many cases PLUM introduces no benefit and in some execution based signal outperforms PLUM. Please confirm.

### Questions
- Preference optimization over code has been explored in previous work (Miao et al. 2024, Zhang et al. 2024, Gee et al. 2024). While this work can be considered concurrent, the paper would benefit from discussing it.
- The methodology seems to require a more powerful model (than the one being trained) to generate the unit tests. Have the authors explored using the policy itself to generate the unit tests?
- Performing SFT over OSS-Instruct, Evol-Instruct-Code and ShareGPT may not necessarily translate to improvements in MBPP and HumanEval datasets. SFT may be forcing models to adapt to out-of-domain prompts resulting in lower performance (and an unfair baseline). The benefits observed in PLUM could be due to these datasets being filtered through on-policy consistency. 
- Many tables are underexplained and potentially misleading (the best results are not always bolded, as in Table 2, 5 and 7). Please clearly indicate which baseline is used for each experiment. Figure 2 is particularly unclear, and (if this reviewer's interpretation is correct) in many cases PLUM introduces no benefit and in some execution based signal outperforms PLUM. Please confirm.

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
The paper presents an on-policy preference learning framework augmented with test cases for code language models called PLUM. It enhances the code generation capabilities of language models by leveraging preference learning driven by automatically generated test cases. The preference data is curated by evaluating candidate code solutions sampled from the policy based on the test cases.  PLUM is evaluated on several code generation tasks, including HumanEval, MBPP and LiveCodeBench, and shows improvements over SFT’ed models and other execution-feedback-driven methods.

### Strengths
- The proposed method uses on-policy preference learning, which aligns with the distribution of the base model itself, reducing the risk of distribution shift.

- The authors conduct comprehensive experiments with several models and compare their performance on multiple benchmarks.

- PLUM does not require extra training for the reward models, which simplifies its implementation.

### Weaknesses
 - This paper focuses on Python language only, during training and evaluation. It would be better if the authors could discuss how the methods could be applied to multilingual settings. Since different programming languages have different executing requirements, I assume it’s not very straightforward to apply the proposed framework directly to other languages. 

- The preference learning relies on executing the test cases, which need to be generated by GPT-4, which is not scalable to generate large volumes of data, limiting the preference data size. Exploring other open-source LLMs might be more helpful in understanding the robustness of the proposed method, i.e. whether it heavily relies on the power of GPT-4. 


- The model sizes used in the experiments are not clearly explained. There are several model families that have different sizes of instruct-model, such as DeepSeek-Coder-6.7B-Instruct and DeepSeek-Coder-33B-Instruct. Without such information, it is harder to understand the proposed method’s impacts on different model sizes.

### Questions
When checking the consistency between the generated reference solution and the test cases, in line 179,  how to check whether the test cases accurately reflect the solution?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The current research piece introduced a new approach for improving code generation skills on existing Code LLMs. To this end, a two step process is introduced i) given a set of coding problems, generate, via prompting, test cases for them, and validate their correctness with the reference solution ii) with the resulting dataset, prompt the LLM to generate new solutions, check them with the generated test cases, and updated the model via iterative preference optimization.
The idea is applied to several standard Code LLM models using DPO and KTO as preference optimization technique and compared with other, non PO approaches including prompting and alternative fine-tunning techniques.

### Strengths
The work is reasonable and clear. It uses established preference optimization techniques as DPO and KTO on for code synthesis improvement. It relies on automatic generation of test cases, guaranteeing their correctness by checking them with the reference solution.
Experimentation show a clear gain across the board in all the models included in the experiments (which are the most popular ones) to avoid the report of any spurious case.

### Weaknesses
1. The paper uses GPT-4-1106 as the generator model to obtain test cases. Without a more powerful model, can this method still have a significant improvement? Can you conduct an ablation study using less powerful models (e.g. GPT-3.5) for test case generation to analyze how model capability affects the overall performance gains？
2. There is no experimental verification for the enhancement capability of this method towards more powerful models, such as DeepSeek-Coder-V2-Instruct(21B AP / 236B TP). Can you add some experiments based on stronger models？
3. The pseudocode is inconsistent with the description in the paper. The paper talks about " Solutions passing all test cases are used as the chosen solutions, and those failing at least one the rejected solutions". But in pseudocode line 14, It seems like having just one case makes it a positive instance.

### Questions
Some suggestions

* Tables: 
Table 3 is shown after table 4. Tables numbers should follow their occurrence order. 
Also, table 2, seems too far from where is referenced (shown in page 5, referenced at the bottom of page 7.
Lines 350 - 364 encloses Table 3 despite it refers to Table 2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a preference learning framework (PLUM) for automatically building code preference data, which uses LLMs with natural language instructions to incorporate test cases and the model's on-policy candidate solutions into the training process. On commonly used evaluation benchmarks: HumanEval(+) and MBPP(+), PLUM further pushes performance of a wide range of instruction models on these coding benchmarks.

### Strengths
1. Without RM, this method accurately captures preferences related to accuracy with test cases and effectively improves the code capability of the model. 
2. This method exhibits good generalization capabilities, as it can integrate with other preference methods to further enhance the performance of various code instruction models.

### Weaknesses
1. The paper uses GPT-4-1106 as the generator model to obtain test cases. Without a more powerful model, can this method still have a significant improvement? Can you conduct an ablation study using less powerful models (e.g. GPT-3.5) for test case generation to analyze how model capability affects the overall performance gains？
2. There is no experimental verification for the enhancement capability of this method towards more powerful models, such as DeepSeek-Coder-V2-Instruct(21B AP / 236B TP). Can you add some experiments based on stronger models？

### Questions
1. The pseudocode is inconsistent with the description in the paper. The paper talks about " Solutions passing all test cases are used as the chosen solutions, and those failing at least one the rejected solutions". But in pseudocode line 14, It seems like having just one case makes it a positive instance.

### Soundness
3

### Presentation
2

### Contribution
3
