# Revisiting the Scaling Effects of LLMs on Medical Reasoning Capabilities

- Decision: Reject
- Scores: 3, 6, 5, 3, 3

## Abstract
Recently, LLMs such as the Llama and Qwen families have rapidly improved by significantly scaling their training corpora, with smaller models trained on larger datasets now approaching or surpassing the performance of previous-generation larger models on public benchmarks.  In this paper, we revisit the scaling effects of LLMs, using the medical field as a case study, by carefully analyzing how training corpus size and parameter size affect model performance on problems of varying difficulty. To this end, we present MedResEval, a new benchmark built upon the MedQA dataset. It is designed to demand more complex reasoning and decision-making and more accurately reflect real-world medical scenarios. Leveraging MedResEval, we investigate the scaling effects of training corpus and model size in LLMs through a comprehensive analysis of several prominent LLM families on medical reasoning tasks of varying complexity.
The results reveal that while smaller models like Llama 3 (8B) approach the performance of older, larger models like Llama 2 (70B) on simple tasks like MedQA, they consistently underperform on complex tasks requiring advanced reasoning. Furthermore, we develop a difficulty-dependent scaling-law formula to characterize how LLMs' performance varies with training data size at a fixed model parameter size. The quantitative study reveals that reasoning error reduction rates are 1.3 times greater for large LLMs ($\approx$ 70B) compared to small LLMs ($\leq$10B) on simple tasks, and 2 times greater on complex reasoning tasks. Our study highlights that while both data and parameter scales enhance LLM performance, greater emphasis must be placed on parameter scales, particularly for complex reasoning tasks. Only LLMs with sufficiently large parameters can effectively tackle the complexities of real-world medical scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces MedResEval, an evaluation framework designed to examine the impact of model parameters and dataset size on the performance of large language models (LLMs) across four specified tasks. The framework defines a formula based on neural scaling law that models the relationship between performance, parameter count, and dataset size, closely aligning with empirical findings. However, there are concerns about the clinical rigor of the MedResEval framework, as it generates a "complex" dataset with certain definitions that may not fully align with established clinical insights.

### Strengths
The paper presents an in-depth evaluation of the proposed MedResEval framework, specifically testing the effects of $N$ (number of parameters) and $D$ (dataset size) — the critical elements of the scaling law. The study defines a formula that effectively models the relationship between performance, parameter count, and dataset size, aligning well with empirical results.

### Weaknesses
Although MedResEval introduces a new evaluation framework with results that adhere to a defined scaling rule, concerns persist about its clinical relevance, and some claims regarding its clinical rigor appear overstated.

1. The task definitions in Section 3.2 somewhat overstate the clinical relevance and how each task contributes to the complexity of clinical questions.
- Available Clues: If the answer provided within the paragraphs (as in Figure 8) includes an obviously correct or easily dismissible wrong answer, this could reduce the complexity of the original MCQ. In many challenging MCQs, the difficulty lies in choosing between two or three closely related options. The example in Figure 8 suggests that the LLM only needs to determine if the single integrated answer choice is correct, which may simplify the question. The simplification arises because the LLM is not required to perform a comparative analysis across multiple plausible options, but rather a binary assessment of a single provided answer against the question context. This approach does not fully capture the nuanced decision-making required in complex clinical scenarios.
- Decision Space: Including an easily dismissible wrong answer does not necessarily increase the complexity of the question. Maintaining question complexity would require distractors that present a closer challenge, as straightforward wrong options may not sufficiently elevate the complexity of decision space. The current design fails to adequately simulate the challenge of selecting from a set of highly plausible, yet subtly different, options that clinicians often face. This limitation undermines the framework's ability to assess the model's capacity for nuanced clinical reasoning.
- Reasoning Steps: Verifying whether a randomly provided answer is correct could simplify the task, as the model only needs to evaluate a single option rather than considering multiple potential answers, thus reducing the overall complexity. This approach bypasses the iterative reasoning process often required in clinical practice, where multiple hypotheses are considered and evaluated before arriving at a conclusion. The task, as currently designed, does not adequately assess the model's ability to navigate complex, multi-step reasoning scenarios.

2. The evaluations lack confidence intervals, which weakens the robustness and reliability of the claims presented in this paper.

Although the presentation and evaluation of the paper were quite comprehensive, this limitation is viewed to be critical and hard to fix at this point of submission. Because this limitation would reduce the impact and contribution of the paper to medical applications, I am inclined to reject the paper in its current form. However, if there could be any improvements that could be made in the short term that address this concern, would be open to revisiting this decision.

### Questions
Does $K$ in Equation 2 refer to the number of tasks considered in MedResEval (specifically, the 4 tasks)? It would be helpful if this were clearly indicated in the manuscript.

### Soundness
2

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
3

### Summary
The paper proposed a new benchmark for LLMs' medical reasoning capabilities, MedResEval, built on the MedQA dataset. MedResEval is designed to evaluate the scaling effects of LLMs on medical reasoning capabilities from training corpus sizes and parameter sizes (or model size). From various evaluation experiments and in-depth results analysis, the paper concluded that both training data size and parameter scales would enhance LLM performances on medical reasoning, and parameter scales lead to a more pronounced performance improvement than scaling training data size for complex reasoning tasks.

### Strengths
- Originality: the paper proposed a novel benchmark to evaluate the utility of LLMs on medical reasoning by expanding the existing popular MedQA dataset with more complex question representations, larger decision space and multi-step tasks. 
- Quality: the paper is solid in technical soundness with meaningful experiment design and proposed evaluation metrics that fit the hypotheses to test the scaling factors of different LLMs. Most conclusions are based on quantitive performance comparison. 
- Clarity: the paper is well-structured with good illustration of diagrams, plots and tables. 
- Significance: the benchmark proposed by the paper is a meaningful expansion of the existing popular MedQA dataset. Also, the same approach could also be applied to other medical benchmark datasets like MedMCQA, PubMedQA, etc. Also, the scaling factor of LLMs is an interesting and important question on practical utility of LLMs in medical domain. The paper offers a good insight or framework on carefully examination of the marginal gain/loss of increasing training data or parameters.

### Weaknesses
 - Lack of limitations and future work in Conclusion part.
- The bar plots somehow are a little bit hard to illustrate the performance changes by various Ns & Ds. Scatter plots like Figure 6 (with dot sizes indicating N or D) might work better. 
- It might be better to indicate both x-axis and y-axis are in log-scale in Figure 6 caption. 
- Overall, the performance differences lack significant analysis since only average performance is reported (e.g. Figure 5). Pls add confidence intervals if they are available.

### Questions
- Will the new benchmark be published, including the diagnosis case study?
- In page 5 "Expanding Decision Space": how to make sure that the randomly generated answers are wrong? Assuming correct answers might be also generated. 
- Does the proposed benchmark support multi-answer questions? (2 or more answers are correct)
- It seems the "reasoning steps" only add an additional intermediate task but still towards the same end task. Taking more steps to achieve the same correct answer seems to be a disadvantage instead of advantage. Should this be rephrased as additional task?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a new benchmark dataset, MedResEval, built over the MedQA dataset, by varying 3 dimensions of difficulty. The authors also propose a difficulty dependent scaling law and results for the same with general purpose LLMs. They tackle the question of whether smaller LLMs can do as well as larger LLMs if given sufficiently large datasets, even when difficulty level of the data changes. The authors seek to identify boundaries to the application of smaller LLMs under specific constraints like data difficulty.

### Strengths
•	Significance: The authors have taken on a relevant problem, especially given the growing landscape of LLMs in the medical context. The authors propose a relevant benchmark that can aid further research in this area.

•	Quality: The authors have performed a quantitative and qualitative assessment of their dataset. The authors have conducted evaluations with 12-18 open source models from 2 model families.

•	Clarity: The writing is quite clear. The authors have provided good examples to illustrate the modifications added.

•	Originality: The novelty is in the proposed dataset and modification to the scaling law in the event of changing difficulty, although the findings themselves are not completely surprising.

### Weaknesses
•	The authors have not shared the proposed dataset yet, which is a key contribution.

•	The main issue is that the evaluation is limited to general purpose LLMs. Since the context is the medical domain, it would be more impactful to examine the effect on the scaling law and the effect of varying difficulty levels on medical LLMs like MedPALM[1], Meditron[2] etc. Specifically, the absence of evaluations on models explicitly designed for medical tasks raises concerns about the generalizability of the findings within the medical field. The paper's conclusions might not hold for models with specialized medical pre-training or fine-tuning, which could exhibit different scaling behaviors.

•	The authors have only evaluated on MedResEval, which is derived from MedQA. Other medical datasets like MedMCQA[3] or PubMedQA[4] can also be considered. It would also be good to give an intuition of how these can be modified to increase the difficulty levels. The lack of evaluation on diverse medical datasets limits the scope of the study and raises questions about the robustness of the proposed difficulty scaling approach. It is unclear if the observed scaling laws are specific to the MedQA-derived dataset or if they generalize to other medical question-answering scenarios.


### Questions
•	The intuition behind Eq 3 and how it relates to Eq 1 can be elaborated on, to aid readers.

•	In Eq 3, is the difficulty dependent aspect only coming from the separation into $i$ tasks? If not, please elaborate.

•	In line 179, it would be good to highlight why the 3 aspects mentioned were the way to increasing difficulty. If possible, please add citations supporting each dimension.

•	The authors have validated the diagnosis simulation task with clinicians. Can a similar evaluation be done for the other 3 tasks and dimensions, to ensure that the questions generated are non-trivial (for example adding relevant options while expanding the decision space)?

•	A complete evaluation should include medical LLMs as well.

•	The authors have not included limitations of the work.

•	In Appendix B, where the 5-shot setting is described, please add in details of the difficulty level of the examples used in 5-shot learning.

•	Minor Comment: A few typos are present in the current draft (eg: sematic instead of semantic in Figure 5)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the impact of training corpus size and model parameter size on the performance of large language models (LLMs) in the medical domain. The authors introduce a new benchmark, MedResEval, which is designed to demand more complex reasoning and decision-making, reflecting real-world medical scenarios more accurately. Through comprehensive analysis, the paper reveals that while smaller models can approach the performance of larger models on simple tasks, they underperform on complex tasks requiring advanced reasoning. The authors also develop a difficulty-dependent scaling-law formula to characterize the performance of LLMs with varying training data sizes at a fixed model parameter size. The study emphasizes the importance of model parameter scales, particularly for complex reasoning tasks, and suggests that sufficiently large parameters are essential for effectively addressing real-world medical scenarios.

### Strengths
1. The paper provides a novel analysis of the scaling effects of LLMs within the medical domain, an area critical for the application of advanced reasoning capabilities. The creation of MedResEval, a benchmark requiring complex reasoning, is a contribution as it allows for more accurate assessment of LLMs in medical scenarios.
2. The paper is well-structured, with a clear problem formulation and methodology. The experiments are thorough, involving multiple LLM families and a range of model sizes and training data amounts. The analysis include both qualitative and quantitative assessments.
3. The paper is also well-written and easy to follow. The introduction of the problem, related work, methodology, experiments, and results are clearly presented. The use of figures and tables to summarize the study's process and findings is effective.
4. The study's findings are significant as they provide insights into the limitations of current LLMs in handling complex reasoning tasks, which is crucial for their deployment in high-stakes domains like healthcare. The proposed scaling-law formula offers a predictive tool for future model development.

### Weaknesses
1. Generalizability: While the paper focuses on the medical domain, it's unclear how these findings generalize to other domains requiring complex reasoning. Further discussion on the broader implications of these results would be beneficial. When extended to other domains, the conclusions may change. The study's focus on medical reasoning, while important, limits the immediate applicability of the scaling laws to other fields such as legal or financial analysis, where the nature of complex reasoning may differ significantly. The paper needs to address whether the observed trends in medical reasoning are consistent with those in other domains, or if domain-specific characteristics influence the scaling behavior of LLMs.
2. Data Diversity: The paper primarily uses one benchmark (MedQA) as the basis for MedResEval. It would be valuable to see how the models perform on other medical datasets to ensure the results are not dataset-specific. At the same time, the so-called "more complex" tasks are not expanded enough, and more complex medical scenario problems should be designed. The reliance on a single benchmark, even with modifications, raises concerns about the robustness of the findings. The study should include evaluations on other medical datasets, such as those focusing on clinical notes or medical imaging reports, to validate that the observed scaling effects are not specific to the MedQA format. Furthermore, the complexity introduced in MedResEval, while a step forward, may not fully capture the nuances of real-world medical reasoning, and more diverse and challenging scenarios should be considered.
3. Model Diversity: The study focuses on a limited number of LLM families. Including a more diverse set of models, including those with different architectures, could provide a more comprehensive understanding of the scaling effects. The analysis should consider models with different architectural designs, such as encoder-decoder models or models with different attention mechanisms, to determine if the observed scaling laws are consistent across different model families. The current study's conclusions may be limited by the specific characteristics of the chosen model families, and a broader analysis is needed to ensure the generalizability of the findings.

### Questions
1. Generalization to Other Domains: How do the authors envision their findings generalizing to other domains that require complex reasoning, such as legal or financial analysis?
2. Impact of Data Diversity: Are there any plans to validate the findings using other medical datasets to ensure the results are not specific to MedQA?
3. Model Architecture Variation: Would the inclusion of models with different architectures change the observed scaling effects, and is this something the authors have considered in their analysis?
4. Practical Implications: What are the practical implications of these findings for the deployment of LLMs in clinical settings? How might these insights inform the development of future LLMs for healthcare applications?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper identifies the lack of a robust dataset to benchmark the reasoning capabilities of Large Language Models (LLMs) in complex medical scenarios. To address this gap, the authors adapt the MedQA dataset, creating a new benchmark called MedResEval with three key improvements: limited clues, a broader decision space, and additional reasoning steps. The authors then benchmark multiple open-source LLMs on this dataset and propose scaling laws that relate performance to training data size.

### Strengths
- The paper addresses an important issue in evaluating LLM reasoning in the medical field.
- The experiments are conducted on a wide range of LLMs.

### Weaknesses
 - The novelty of the proposed dataset fall short when compare  to existing datasets: 
	- The authors argue that MCQs provide too many clues and a limited decision space. However, the modified dataset they propose still contains only MCQs, despite the existence of medical question-answering datasets without MCQs [1].
	- The authors propose benchmarking the multistep reasoning abilities of LLMs by artificially adding a reasoning step to the MedQA dataset. However, datasets specifically designed to assess this ability already exist [2,3], making the novelty of the authors' benchmark relatively limited in comparison.

- The benchmark proposed by the authors utilizes "Chain of Thought" prompting, with demonstrations generated by GPT-4. This approach makes the benchmark dependent on the performance of a third-party, closed-source model, and it diverges from realistic medical scenarios, as sensitive medical data cannot be processed by GPT-4 due to ethical concerns.


- The experimental details are incomplete, particularly the absence of the specific prompts used. This omission makes it challenging to have confidence in the results and to reproduce them, as the performance of each LLM can vary significantly depending on the prompt used.

- The paper lacks a contribution section, which makes it difficult to discern the specific claims and contributions being presented.

- The experiments lack reported margins of error, making it difficult to evaluate the significance of the presented results.

### Questions
- Is it possible that the dataset being enhanced is part of the training set for some of the LLMs used in this study? Given that MedQA was released in 2021 and the Llama-3 models’ training data has a cutoff in December 2023 for example, it seems likely that this dataset or its metadata could have been included in the training data. This issue is critical to consider for two reasons:
	- It may bias the proposed benchmark, as some models might have been trained on this dataset while others have not. Additionally, it risks transforming the benchmark into a test of memorization rather than reasoning ability.
	- It diverges from the real-world clinical conditions the authors aim to simulate,  particularly in comparison to other benchmarks that ensure they are not included in the training sets of LLMs [1,2].

- In Section 4, the authors propose adding an additional baseline to address the "simple generalization effect." Could the authors clarify what specific effects they are referring to here and explain how the added baseline mitigates these effects? Citing relevant literature to support this would be appreciated.

[1] (2018) emrQA: A Large Corpus for Question Answering on Electronic Medical Records 

[2] (2022) DrugEHRQA: A Question Answering Dataset on Structured and Unstructured Electronic Health Records For Medicine Related Queries

### Soundness
2

### Presentation
2

### Contribution
1
