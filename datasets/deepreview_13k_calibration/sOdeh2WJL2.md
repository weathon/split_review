# Unified Multi-Task Learning & Model Fusion for Efficient Language Model Guardrailing

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 1, 8, 3

## Abstract
The trend towards large language models (LLMs) for guardrailing against undesired behaviors is increasing and has shown promise for censoring user inputs. However, high inference speed, memory consumption, hosting expenses and generative non-structured outputs can make their use prohibitive. 

In this work, we show that task-specific data generation can lead to fine-tuned classifiers that significantly outperform current state of the art (SoTA) while being orders of magnitude smaller. Secondly, we show that using a single model, \texttt{MultiTaskGuard}, that is pretrained on a large synthetically generated dataset with unique task instructions further improves generalization. Thirdly, our most performant models, \texttt{UniGuard}, are found using our proposed search-based model merging approach that finds an optimal set of parameters to combine single-policy models and multi-policy guardrail models

On 7 public datasets and 4 new guardrail benchmarks we created, our efficient guardrail classifiers improve over the best performing SoTA publicly available LLMs and 3$^{\text{rd}}$ party guardrail APIs in detecting unsafe and safe behaviors by an average \textbf{29.92} (\text{Aegis-LlamaGuard}) and \textbf{21.62} (\texttt{gpt-4o}) F1 respectively. Lastly, our guardrail synthetic data generation process leads to models that outperform training on real data using our custom defined policies that describe the guardrailing task.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces three models: TaskGuard, MultiTaskGuard, and UniGuard. TaskGuard is trained on synthetic data tailored to specific tasks, MultiTaskGuard is trained on multi-task synthetic data for broader applicability, and UniGuard combines TaskGuard and MultiTaskGuard through model merging techniques. These models achieve state-of-the-art performance across 11 datasets, offering enhanced accuracy and efficiency.

### Strengths
1. The proposed models achieve superior accuracy and efficiency compared to existing approaches.

2. The evaluation, conducted on 11 datasets, provides a comprehensive assessment.

### Weaknesses
1. Key hyperparameters, such as lambda, k, and n, are not specified, making it difficult to reproduce the results or understand the sensitivity of the models to these parameters.

2. An ablation study examining the impact of different components in the multi-task training loss (line 173) is missing. Specifically, it is unclear how much each component contributes to the overall performance, and whether some components are more important than others.

3. Data statistics are unclear, specifically for the training, validation, and test sets. The paper lacks details on the number of safe and unsafe samples, the policy definitions used for their generation, and the configurations used to determine if samples are borderline, in-domain, or out-of-domain. It is also unclear if syntactic augmentation was used to test guardrailing robustness to noise.

4. The proposed MMS method results in only a modest performance improvement, raising questions about its practical utility given the added complexity.

### Questions
Q1. How many policies are used to train TaskGuard? Is a separate version of TaskGuard, MultiTaskGuard, and UniGuard trained for each dataset? Could you provide examples of the policies used?

Q2. How many training stages are there for MultiTaskGuard, TaskGuard, and UniGuard?

Q3. During inference, what is the input format for TaskGuard, MultiTaskGuard, and UniGuard?

Q4. What are the ablation results for multi-task training loss?

Q5. What is the over-refusal rate of the proposed model on xstest?

Q6. How does the model merging cost of the proposed method compare to the baseline?

Q7. For the public benchmark, was training data utilized in the data synthesis process?

Q8. What backbone model is used in Table 3?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper proposes a unified framework for guardrailing large language models (LLMs) to ensure safety and efficiency when filtering out unsafe or malicious content. The main contributions include the development of a synthetic data generation pipeline, a multi-task learning approach called MultiTaskGuard, and a model merging search strategy to optimize guardrailing models.

### Strengths
- the paper addresses an important problem.

### Weaknesses
 - the paper is hard to follow: (1) it's rare the say a model is a "1GB" classifier; (2) using unnecessary abbreviations (e..g., synthetic data generation => SDG) can be misleading; (2) inconsistently using unnecessary math symbols can be even more misleading (e.g.,  $P_{\text{name}}$ denotes the name attribute of the polices, but $P_{i}$ refers to the i-th police); and (3) incorrectly using of escape characters (e.g., in line 169 "\n").

- related work is not cited in a proper way. For example, in lines 258-265, the paper provides the links to previous work but does not cite them.

- There is no appendix in the paper, but some details are said to be provided in the appendix. 

- the proposed methods, including synthetic data generation and model merging, are not introduced clearly.

- it is not clear how are the baseline models such as gpt-4 adopted for the experiments. For example, how does the prompt look like? Are few-shot examples included? Moreover, there is no specific version of the GPT models, making it impossible to make reliable comparisons between different models. 

- none of the tables are captioned in a reasonable way

### Questions
- where is the appendix?
- will you public the new test set?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper the authors propose a new method, using multi-armed bandit to merge guardrailing across multiple policies. Essentially, the trained model is able to handle multiple guardrail tasks (policies). It can better generalize to new policies, and requires less fine tuning data and fine tuning parameters.
The benchmarking results over other guardrailing models show superior performance.

The new model, MultiTaskGuard, is a multi class detector/classifier, it is not clear from the paper what information it outputs per class (for example per class confidence level) if at all, or it merges and considers the multi-policies as one new policy.

### Strengths
New technically sound approach for merging multiple guardrails across multiple policies into one model.

### Weaknesses
Doesnt explain how multi class classification is being handled and what output is being provided and what is the performance per different policy in the fused MultiTaskGuard model.

### Questions
It is not clear from the paper if the MultiTaskGuard provides confidence levels for the multi class classification, for each considered policy?

### Soundness
3

### Presentation
3

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
The paper introduces a method called TaskGuard for language model guardrailing that uses synthetic data to finetune a small model like RoBERTa and achieves SOTA performances. They use a single model that is pretrained on a large multitask synthetically generated dataset, called MultiTaskGuard, to further improve the generalization. Furthermore, they propose UniGuard, a search-based model merging approach that finds an optimal set of parameters to combine TaskGuard models and MultiTaskGuard models. Experimental results show that when equipped with the proposed method, small models like Roberta even outperform LlamaGuard and GPT-4o on 7 public datasets and 4 internal datasets.

### Strengths
1.	The method could achieve SOTA guardrailing performance against large language models like GPT-4o and LlamaGuard. 

2.	Based on only a sub 1GB classifier and synthetic data, the method could perform very well without the high demand for resources and computation.

### Weaknesses
1. In section 3.1, the authors introduce the process of synthetic data generation formally. However, the generation details are not provided in this section. For example, what is the meta prompt of LLM used for data generation? What is the template that prompts LLM to self-reflect on its own label judgments? Is there any example that shows the synthetic data? This kind of information is essential for future reproduction.

2. It is not clear whether MultiTaskGuard and TaskGuard share the same task format and input schema. If not, it is somewhat strange that UniGuard combines its best-performing models tuned towards different input schemas. If so, more ablation studies should be conducted to test the performance where only MultiTaskGuard models are merged or only TaskGuard models are merged.

3. Table 1 shows the outstanding performance of the proposed methods. From the table and the experimental settings, I can infer that the API guard models and open guard LLM-based guard models are tested in zero-shot. In contrast, TaskGuard and MultiTaskGuard are trained on real data or synthetic data tailored to specific benchmarks. In this way, the comparison setting may be unfair. I am curious about how a large language model, e.g., Llama2-7B, would perform when tuned on the training data.

4. The extensibility of MultiTaskGuard and UniGuard is unclear. When more policies come in, the trained model may fail to guard new cases. How to incrementally add new policies without influencing the original performance needs to be further discussed.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
3
