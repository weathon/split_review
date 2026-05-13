# ClinicalBench: Can LLMs Beat Traditional ML Models in Clinical Prediction?

- Decision: Reject
- Scores: 3, 3, 8, 8

## Abstract
Large Language Models (LLMs) hold great promise to revolutionize current clinical systems for their superior capacities on medical text processing tasks and medical licensing exams. Meanwhile, traditional ML models such as SVM and XGBoost have still been mainly adopted in clinical prediction tasks. An emerging question is \textit{Can LLMs beat traditional ML models in clinical prediction?} Thus, we build a new benchmark {\cb} to comprehensively study the clinical predictive modeling capacities of both general-purpose and medical LLMs, and compare them with traditional ML models. {\cb} embraces three common clinical prediction tasks, two databases, 14 general-purpose LLMs, 8 medical LLMs, and
11 traditional ML models. Through extensive empirical investigation, we discover that \textbf{both general-purpose and medical LLMs, even with different model scales, diverse prompting or fine-tuning strategies, still cannot beat traditional ML models in clinical prediction yet}, shedding light on their potential deficiency in clinical reasoning and decision-making. We call for caution when practitioners adopt LLMs in clinical applications. {\cb} can be utilized to bridge the gap between LLMs' development for healthcare and real-world clinical practice.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents ClinicalBench, comparing traditional ML models with LLMs on clinical prediction tasks. While the experimental setup is thorough, I have significant concerns about the scientific value and broader impact of this work given the dramatic performance gap demonstrated between LLMs and traditional ML models.

The results show that even state-of-the-art LLMs perform substantially worse than basic ML models like XGBoost and SVMs across all tasks. For example, traditional ML models achieve Macro F1 scores of 65-70% on Length-of-Stay prediction while LLMs struggle to exceed 30%. Similar large gaps exist for mortality and readmission prediction. Even with extensive prompt engineering and fine-tuning, LLMs fail to approach traditional ML performance.

Given these results, it's unclear what meaningful insights this work provides beyond demonstrating that LLMs are currently inappropriate for clinical prediction tasks. The paper essentially confirms what one might expect - that specialized ML models trained directly on structured clinical data outperform general language models on specific prediction tasks. While the thorough empirical validation may have some value, the magnitude of the performance gap suggests this comparison may be unnecessary.

### Strengths
Thorough experiments

### Weaknesses
The results show that even state-of-the-art LLMs perform substantially worse than basic ML models like XGBoost and SVMs across all tasks. For example, traditional ML models achieve Macro F1 scores of 65-70% on Length-of-Stay prediction while LLMs struggle to exceed 30%. Similar large gaps exist for mortality and readmission prediction. Even with extensive prompt engineering and fine-tuning, LLMs fail to approach traditional ML performance.

Given these results, it's unclear what meaningful insights this work provides beyond demonstrating that LLMs are currently inappropriate for clinical prediction tasks. The paper essentially confirms what one might expect - that specialized ML models trained directly on structured clinical data outperform general language models on specific prediction tasks. While the thorough empirical validation may have some value, the magnitude of the performance gap suggests this comparison may be unnecessary.

### Questions
None

### Soundness
3

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
The paper explores the capabilities of large language models (both general-purpose and medical-oriented models) in clinical prediction tasks (including length-of-stay, mortality, and readmission), comparing them with conventional machine learning-based models. The paper reveals that LLMs still cannot outperform traditional ML models in various settings (parameter size, different LLMs, prompting/finetuning strategies, etc.). The dataset employed in this research consists of code-based data extracted from MIMIC-III and MIMIC-IV. To better understand the code semantics, the authors convert codes to text.

### Strengths
The paper is well-presented and organized with clear motivation and writing flow. The paper addresses a key problem in the era of LLMs, where plenty of researchers are exploring the boundary capability of LLMs.

### Weaknesses
My main concern is the paper's novelty and contribution. There are already many works that explore LLMs' capabilities on diverse tasks, including those in the medical field. The findings are straightforward and predictable: machine learning models trained on specific medical tasks naturally surpass LLMs' zero-shot performance, and in real-world clinical practice, the simplest models (e.g., logistic regression, LASSO) are still widely used for their simplicity and interpretability. With the development of more advanced LLMs, the findings may change, as they only reflect current guidelines and cannot predict the future practical use of LLMs. The employed LLMs are mainly small in size; larger models of 70B parameters and beyond should be explored. These larger language models have much better prompt-following capabilities, so CoT and ICL approaches may work, rather than simply concluding that "The effectiveness of typical prompting engineering techniques is generally limited." Additionally, no variance is reported in the benchmarking table, although LLMs' outputs can be sensitive to input prompts, temperature settings, and the sequence of input instructions.

### Questions
See weaknesses section above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ClinicalBench, a benchmark designed to evaluate the performance of 14 general-purpose LLMs, 8 medical LLMs, and 11 traditional ML models (e.g., XGBoost, Logistic Regression, RNN etc.) on three clinical classification tasks: Length-of-Stay Prediction (three-class classification), Mortality Prediction (binary classification), and Readmission Prediction (binary classification). On both the MIMIC-III and MIMIC-IV datasets, this paper shows that most LLMs currently still fall short in making accurate predictions for these real-world clinical tasks, underperforming by an obvious margin compared to traditional ML models.

### Strengths
1. This paper is clearly written and easy to follow, and the figures are informative.
2. This paper offers a head-to-head comparison between LLMs and traditional ML methods on three real-world clinical tasks, helping to clarify the current capabilities of LLMs in this domain. The three ways of enabling LLMs to make predictions utilized in this paper - direct prompting, engineered prompting (e.g. Chain-of-Thought, Self-Reflection, Role-Playing, In-Context Learning), and supervised fine-tuning using task-specific data - reflects the primary approaches for applying LLMs nowadays, making its insights broadly applicable and valuable for future research.
3. The evaluation is quite thorough, and the findings offer interesting insights for this domain.

### Weaknesses
1. While named as a benchmark, this paper did not introduce or curate new datasets, or introduce novel ways of processing or derive new clinical tasks from the MIMIC-III and MIMIC-IV datasets. The main contribution is in developing the framework of comparing LLMs with traditional ML methods on standard clinical tasks in MIMIC-III and MIMIC-IV. Thus I would argue that the contribution may be slightly less significant compared to benchmarks which both introduce new clinical tasks closer to real-world clinical reasoning / decision-making and also develops the LLM evaluation framework.
2. For Section 5 fine-tuning, the details about how the LLMs are fine-tuned are unclear in the main paper - is it by adding a classification head to the output of the transformer, or by next-token prediction on target outputs (from Appendix C it seems to be the latter)? I think adding this detail to Section 5 would help the readers understand how SFT was conducted and better understand the performance discrepancy compared to traditional ML methods.
3. For In-context Learning, it seems that 3 examples are provided to the LLMs per the prompt example in Appendix D. Are these examples chosen randomly or selected to be representative of the patient population? I think it might be helpful to also analyze how the number of in-context examples and how the diversity of the in-context examples (e.g. different disease type, different age groups etc.) impact the LLM performance, as sometimes LLMs can be quite sensitive to that.
4. The impact of parameter scaling is studied for direct prompting but not for engineered prompting, i.e., only 7B, 8B and 9B models are studied for engineered prompting but not 34B or 70B. I would assume that large models have better instruction following capabilities and thus may be better at reasoning or role play than smaller models, and would like to know your insights on this and why larger models are not used for engineered prompting.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper compares the performances of multiple LLM and traditional ML models on three clinical tasks (length of stay, mortality, readmission) on MIMIC III and IV. This paper contributes key conclusions on the underperformance of LLMs compared to traditional ML models. Furthermore, the authors demonstrate that specialised models do not always perform better and that advanced prompting strategies also do not help. Only fine-tuning strategies significantly improve the LLM performance on these tasks.

### Strengths
The paper explores the use of LLM in medical tasks clearly and thoroughly.

### Weaknesses
- The paper could discuss more in depth the different works that have aimed to use LLM for prediction and how the proposed paper differs.
- One limitation could be the reliance on MIMIC used to train some of these models. However, the current underperformance of LLMs only further emphasises the limitations of these strategies, which may benefit from data leakage.

### Questions
None

### Soundness
3

### Presentation
4

### Contribution
4
