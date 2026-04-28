# No Factor Left Behind: Towards arbitrary amount of factors in the medical cohort analysis

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Driven by the goal of data-driven analysis on the large-scale cohort, a large language model(LLM) has solidified itself as a critical focus of artificial intelligence medical research today. However, such efforts have coalesced around a small group of evidence, leaving behind the vast majority of factors collected in the cohort investigation. What does it take to break the more than 70 factors while ensuring responsible, high-quality prediction, all while keeping medical considerations in mind? In No Factor Left Behind, we first took on this challenge by numerical interpretable evidence contextualizing the need for Premature rupture of membranes (PROM) risk assessment through exploratory interviews with domain experts. Then, we created datasets and models aimed at narrowing the performance gap between low and high-frequency factors. More specifically, we developed a model based on factor-value pairs trained on data obtained with robust and effective data mining techniques tailored for low-frequency factors. We propose multiple architectural and training improvements to counteract overfitting while training on 70 factors. Critically, we interpreted the risk of PROM over 7000 cohort participants' directions using numerical interpretable evidence with precise values of factors combined with human evaluation covering all factors in the dataset to assess medical safety. Our model achieves a performance of 79\% accuracy (78 factors) and 96\% accuracy(40 factors) with risk assessment at the screening level, laying the novel insight for realizing a general medical cohort analysis method in the era of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study aims to enhance predictive modeling for medical risk assessment using large language models (LLMs) by addressing the challenge of integrating a broad range of low- and high-frequency factors. Through expert interviews and specialized data mining, the team developed a model capable of accurate PROM risk assessment across 70 factors, achieving 79% accuracy on 78 factors and 96% accuracy on 40 factors.

### Strengths
+ The study overall plan (while fairly unclear) seems fairly reasonable and timely. 
+ The study aims to use an LLM-based pipeline for a novel application (i.e., identifying the factors to include in medical cohorts), in a customized and expanded way.
+ The study adopts a few solid theoretical frameworks, such as the one from epidemiology. 
+ The study includes a user (human) study, although its design and findings are a bit unclear.

### Weaknesses
 + Despite the excitement, the primary concern about this submission is about its presentation and soundness. In the submitted format, the overall rationale and design seems quite convoluted and unclear. The whole paper's flow is weak. Numerous formatting and typos can be seen in the document. For instance, the whole paragraph related to Equation 4 seems to be duplicated. Or the text refers to the left and right side of Fig 1, but it seems that the authors were referring to the top and bottom parts. It is very hard to understand Section 3.2 (a key section for the Method) and its connection to 3.3 is unclear. Unfortunately, this issue makes evaluation of the core concepts and contributions very challenging.

### Questions
+ How function v in Eq 4 (or 5) is implemented in practice? That seems to have a key role in the process. 
+ How the expert-augmented part is implemented? Are they sourced from the human participants? What would this mean for a general application of this tool?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The text does not flow well and I feel like sometimes sentences do not logically follow each other. The text is poorly formatted and a lot of details are missing. I have to say that the language is formatted in such a way that I am probably missing the the point of the paper. It feels like large parts have been written/corrected by an LLM. This is the case in the entire text.

### Strengths
- Used existing biomedical models in experiments.
- Collected a new dataset to use in the experiments (details are missing about this dataset, though).

### Weaknesses
 The text does not flow well and I feel like sometimes sentences do not logically follow each other. The text is poorly formatted and a lot of details are missing. I have to say that the language is formatted in such a way that I am probably missing the the point of the paper. It feels like large parts have been written/corrected by an LLM. This is the case in the entire text.

### soundness:
 2

### presentation:
 1

### contribution:
 2

### strengths:
 - Used existing biomedical models in experiments.
- Collected a new dataset to use in the experiments (details are missing about this dataset, though).

### weaknesses:
 - line 275: why is this seperate line here?
- 402: spelling error: superviesd
- Figure 2: the text overlaps with the bars. Also predication is meant to be prediction?
- line 486: is supposed to be a section heading?
- Line 522: multiple links/garbled (?) text
- No contextualization/related work of PROM which is only fully mentioned in the abstract. This should be part of the related work section and then again in the discussion section.
- Line 151: why cite the SHAP paper?
- The PROM use case is not explained well, and it is not clear how this would contribute to the wider ICLR community. There needs to be a generalization of the knowledge.

### questions:
 - I don't understand the "husband education level" example for a biomedical LLM. Why would this be relevant to the task(s) that you are trying to solve? Again, the lack of related work and the explanation of the application could help here.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 2

### code_of_conduct:
 Yes

### Questions
- I don't understand the "husband education level" example for a biomedical LLM. Why would this be relevant to the task(s) that you are trying to solve? Again, the lack of related work and the explanation of the application could help here.

### Soundness
2

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
3

### Summary
This paper states an approach for improving medical cohort analysis using LLMs, especially by incorporating low-frequency factors that are usually not considered in traditional methods. They propose a method for developing prompts via both manual and automatic techniques, using methods such as MLM and cohort-specific prompts to improve risk prediction in medical data. The study explores the use of models such as LLama3.1 and MedAlpaca, among others, and evaluates their performance on different factor sets, showing better accuracy, especially in the prediction of PROM. Key contributions include the introduction of a factor-based interaction map to represent the relationships between individual factors and architectural improvements designed to reduce overfitting. The results show that the proposed method outperforms traditional supervised baselines, which provides a better tool for medical cohort analysis while addressing challenges in the LLM-based models.

### Strengths
Originality: This paper introduces an approach by focusing on low-frequency factors in medical cohort analysis, which are often ignored. Using manual and automatic prompt generation with LLMs like LLama3.1 and MedAlpaca is relatively creative, as is the factor-based interaction map. 
Quality: The paper provides partial technical depth, with some explanations of the prompt generation techniques and factor-based interaction map. 
Clarity: The paper is primarily clear, particularly in describing the prompt generation and the interaction map. 
Significance: By incorporating low-frequency factors, the paper has the potential to significantly improve risk prediction in healthcare, such as in the prediction of premature rupture of membranes. 
Overall comment on strengths: This paper makes a good contribution, especially in applying LLMs to low-frequency factors in healthcare.

### Weaknesses
The paper doesn’t compare the mentioned method with traditional machine learning models, which would highlight the specific advantages of the proposed approach. The computational cost and feasibility of automatic prompt generation aren’t discussed, leaving doubts about its practicality in clinical settings. The experiments are based on only one dataset, restricting the generalizability of the findings. Also, overfitting is a risk with the factor-based interaction map, but this paper lacks a discussion on a few mitigation strategies, such as regularization techniques. Some terms throughout the paper are not clear and need further clarification for non-expert readers. The explanations for evaluation metrics are too narrow and centered around accuracy without reporting other critical metrics such as AUC. Some ethical concerns and potential biases in the data are mentioned but not completely addressed and discussed.

-The abstract section mentions 79% accuracy with 78 factors and 96% with 40 factors but doesn't give a context on how these results compare to benchmarks or their clinical significance. The term "numerical interpretable evidence" is unclear.
-In the introduction section, the paper states that traditional studies overlook most of the factors but doesn't elaborate on why adding so many factors is necessary or even how this can lead to better outcomes.
-The factor-based interaction map does not explain why it was chosen and how it improves performance. There is also no discussion on scalability, overfitting, or managing complexity as more factors are added.
-The automatic prompt generation method's scalability is mentioned, but computational costs and feasibility for clinical use are missing. There's no mention of time or resources required, making it hard to assess practical viability.
-The results rely on outdated models like LLama3.1 and MedAlpaca without clear justification. The reported accuracy metrics lack context and comparison to modern benchmarks, making it difficult to interpret their significance.
-There are no error bars or confidence intervals, making the reliability of the results hard to assess. These are essential to determine how robust the findings are in medical contexts where consistency is critical.
-The ethical concerns around using cohort-specific medical data are barely discussed despite the sensitivity of such data. More focus is needed on privacy risks and potential biases in using large language models on this data.
-The conclusion overstates the method's applicability, claiming it provides a universal solution despite showing only incremental improvements. The method's broader relevance to other conditions or datasets isn't convincingly demonstrated.
-Choosing 78 factors is not clearly mentioned. There's no explanation for why these factors were selected or how they were deemed necessary, making it so difficult to assess the significance of this approach.
-The manual prompt engineering process is impractical for large-scale settings or dynamic settings. Its lack of generalizability across conditions or datasets is a significant limitation, and the adaptability of these prompts in new domains isn't discussed.
-The automatic prompt generation pipeline lacks discussion on potential errors or biases, especially in medical applications where accuracy is crucial. The risks of generating irrelevant content aren't addressed.
-The interaction map may not scale well as more factors are added. As complexity increases, overfitting becomes a risk, but the paper doesn't discuss how to manage this or mitigate it such as regularization techniques. This subject cannot be ignored.
-Bias and fairness issues in the data aren't addressed. Without steps to ensure fairness, the model may propagate existing biases in the training data, leading to unequal outcomes for different patient groups.
-The cohort-specific prompts could be overfitted to the dataset and fail to generalize to new cohorts. There's no discussion on how adaptable these prompts are across different settings.
-The computational cost of fine-tuning large models isn't considered. Training these models is resource-heavy, and the paper doesn't quantify the time or hardware needed, limiting its practicality in clinical environments.
-The baseline comparison is only with LLMs, but a comparison to simpler machine learning models would be useful. Traditional models are often preferred in healthcare for their interpretability, and their inclusion would provide a clearer picture of the method's advantages.
-The dataset is from a specific cohort, but the findings' generalizability to other datasets is not discussed. Testing on diverse datasets would strengthen the paper's claims.

### Questions
-The abstract section mentions 79% accuracy with 78 factors and 96% with 40 factors but doesn't give a context on how these results compare to benchmarks or their clinical significance. The term "numerical interpretable evidence" is unclear.
-In the introduction section, the paper states that traditional studies overlook most of the factors but doesn't elaborate on why adding so many factors is necessary or even how this can lead to better outcomes. 
-The factor-based interaction map does not explain why it was chosen and how it improves performance. There is also no discussion on scalability, overfitting, or managing complexity as more factors are added.
-The automatic prompt generation method's scalability is mentioned, but computational costs and feasibility for clinical use are missing. There's no mention of time or resources required, making it hard to assess practical viability.
-The results rely on outdated models like LLama3.1 and MedAlpaca without clear justification. The reported accuracy metrics lack context and comparison to modern benchmarks, making it difficult to interpret their significance.
-There are no error bars or confidence intervals, making the reliability of the results hard to assess. These are essential to determine how robust the findings are in medical contexts where consistency is critical.
-The ethical concerns around using cohort-specific medical data are barely discussed despite the sensitivity of such data. More focus is needed on privacy risks and potential biases in using large language models on this data.
-The conclusion overstates the method's applicability, claiming it provides a universal solution despite showing only incremental improvements. The method's broader relevance to other conditions or datasets isn't convincingly demonstrated.
-Choosing 78 factors is not clearly mentioned. There's no explanation for why these factors were selected or how they were deemed necessary, making it so difficult to assess the significance of this approach.
-The manual prompt engineering process is impractical for large-scale settings or dynamic settings. Its lack of generalizability across conditions or datasets is a significant limitation, and the adaptability of these prompts in new domains isn't discussed.
-The automatic prompt generation pipeline lacks discussion on potential errors or biases, especially in medical applications where accuracy is crucial. The risks of generating irrelevant content aren't addressed.
-The interaction map may not scale well as more factors are added. As complexity increases, overfitting becomes a risk, but the paper doesn't discuss how to manage this or mitigate it such as regularization techniques. This subject cannot be ignored.
-Bias and fairness issues in the data aren't addressed. Without steps to ensure fairness, the model may propagate existing biases in the training data, leading to unequal outcomes for different patient groups.
-The cohort-specific prompts could be overfitted to the dataset and fail to generalize to new cohorts. There's no discussion on how adaptable these prompts are across different settings.
-The computational cost of fine-tuning large models isn't considered. Training these models is resource-heavy, and the paper doesn't quantify the time or hardware needed, limiting its practicality in clinical environments.
-The baseline comparison is only with LLMs, but a comparison to simpler machine learning models would be useful. Traditional models are often preferred in healthcare for their interpretability, and their inclusion would provide a clearer picture of the method's advantages.
-The dataset is from a specific cohort, but the findings' generalizability to other datasets is not discussed. Testing on diverse datasets would strengthen the paper's claims.

### Soundness
2

### Presentation
2

### Contribution
3
