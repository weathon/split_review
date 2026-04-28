# Understanding and Mitigating Gender Bias in LLMs via Interpretable Model Editing

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 3, 8

## Abstract
Large language models (LLMs) have achieved great success in various tasks. While LLMs can learn powerful capabilities from large datasets, they also inherit the gender bias present in that data. Existing studies usually propose methods to reduce bias by data cleaning and model retraining/fine-tuning. Although these methods have shown some success, the cost of designing data and retraining/fine-tuning an LLM increases significantly as the model size grows larger. Furthermore, a lack of understanding of the mechanisms behind gender bias prevents researchers from effectively tailoring solutions to address it. In this paper, we utilize mechanistic interpretability methods to construct the neuron circuits for gender bias cases and locate the important neurons storing gender bias. Then we propose the Interpretable Model Editing (Interpret-ME) method to reduce gender bias without designing huge datasets or fine-tuning. Compared to fine-tuning methods, our approach shows competitive results in reducing gender bias across experiments with 8 LLMs. At the same time, our method does not affect the performance in other tasks. Overall, our analysis is useful for understanding the mechanism of gender bias and our method paves a potential way for reducing bias.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores gender bias in large language models (LLMs) and highlights challenges with current methods, like data cleaning and fine-tuning, which become costly as models get larger. The authors use interpretability tools to identify specific neurons linked to gender bias and introduce a new method, Interpretable Model Editing (Interpret-ME), to reduce this bias without needing extensive retraining.

### Strengths
1. The method does not rely on a large amount of data, making it more practical and cost-effective compared to approaches that require extensive datasets for bias mitigation.

2. Since the method does not require fine-tuning the entire model, it saves substantial computational resources and time, especially for large language models.

3. The method has minimal impact on performance across common datasets, ensuring that the model’s general abilities remain intact while reducing gender bias.

### Weaknesses
1. Some notations can be more clear. For example, B and d in section 3.1.

2. The method does not compare changes in entropy difference on WinoG/CPairs with fine-tuning. Without this comparison, it is unclear if Interpret-ME is as effective as or better than fine-tuning in terms of reducing bias on these datasets.

3. It remains unclear whether different gender-biased sentences activate the same neurons or if varying sentences affect the method's results. This uncertainty suggests that the method might not generalize well to a broad range of gender-biased language, potentially impacting its consistency and reliability across diverse examples.

### Questions
1. Will different types of gender-biased sentences activate distinct important neurons? The selected sentences focus on professions. If sentences featuring other gender-stereotyped topics, such as personality traits or colors, are used, would we observe similar results?

2. What happens if the sentence is changed to "This woman is ==> a nurse"?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Existing approaches usually use model re-training or model fine-tuning methods to alleviate gender bias. They usually require curating a data set for debiasing purposes. And such re-training and fine-tuning might hurt model’s performance on other tasks. 
Towards this end, the paper proposes Interpretable Model Editing (Interpret-ME), a method to reduce gender bias without designing huge datasets or fine-tuning. Compared to fine-tuning methods, the proposed approach shows competitive results in reducing gender bias across experiments with 8 LLMs.

### Strengths
1. good presentation

2. proper adaptation of existing methods to application problems

3. thorough experiments on various models

### Weaknesses
My only concern is that from the experiments, it seems that in order for Interpret-ME to not hurt models’ performance on other tasks, it requires very delicate hyper-parameter search. Therefore I’m not convinced that compared to fine-tuning approaches, the proposed approach is more beneficial from the perspective of maintaining LLM’s existing capability. More experiment designs and results along this line would be very helpful.

### Questions
Please see weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces an approach to mitigate gender bias using a neuron-level framework called Interpret-ME. Unlike resource-intensive finetuning methods, this proposed approach edits key neurons to reduce bias while maintaining model performance. The authors demonstrate the effectiveness of their proposed approach on eight LLMs using various metrics such as StereoSet, WinoGender, and CrowS-Pairs, achieving competitive results.

### Strengths
- The study addresses a crucial issue in machine learning: mitigating gender bias in LLMs through an efficient method that avoids resource-heavy fine-tuning or data collection. 
- It is validated across a range of large and common models, enhancing practical significance. 
- The method also maintains overall model performance while offering valuable neuron-level interpretability insights into bias mechanisms.

### Weaknesses
The paper requires substantial revisions to meet the standards of a prestigious venue like ICLR. The main issues are:

- The writing is difficult to follow due to unclear explanations and a confusing structure. Key sections, such as the background and methodology, require multiple readings to understand. For example, the background section introduces numerous variables and equations without sufficient context or motivation, making it challenging for readers to relate them to the main methodology. While it extensively reiterates standard multi-head attention formulas with many variables, it fails to explain their relevance to this work. Conversely, the authors omit essential background on the key concept of the unembedding space, which is central to understanding the proposed methodology.

- Figures and tables are presented without adequate spacing, blending into the text and making it difficult to differentiate between the main content and captions (e.g., page 5).

- The method relies heavily on existing interpretability frameworks, leading to limited innovation and making the contributions feel incremental.

- The idea of addressing bias in LLMs by identifying and editing specific neurons is not new, and similar approaches have been explored before. The authors do not adequately acknowledge this and fail to distinguish their work from related studies like those by Chintam et al. (2023) and Lutz et al. (2024). For example, Chintam et al. (2023) used methods like automated circuit discovery to identifying causal relations between LM components and gender bias, following by performing a finetuning strategy to mitigate bias in those components.

- The study's use of bias-evaluation datasets, such as CrowS-Pairs and StereoSet, which have been criticized for noise and reliability issues (Blodgett et al., 2021), raises concerns about the robustness of the evaluation.


### Questions
Q1. Could you provide a clearer explanation of how the hypotheses in Section 3.3 were derived from the previous analyses?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper mitigates the gender bias issue of large language models by editing model parameters instead of data cleaning and fine-tuning. The paper argues that some neurons in LLM exhibits significant bias and thus results in the bias of LLM. Therefore, the authors firstly adopt interpretability methods to identify such neurons and then propose Interpret-ME to reduce it. The experimental results demonstrate the effectiveness of Interpret-ME across 8 LLMs without degrading their performance.

### Strengths
1. It is important to studying the neuron circults of the generated response to make LLMs more interpretable and align with human values. The motivation is convincing.
2. The methodology of implementing the idea is sensible.
3. The experimental results show the effectiveness of the methods.

### Weaknesses
1. My major concern is that the models studied by the authors may be outdated. With the continuous development of LLMs, more and more drawbacks of them vanished. It’s unclear whether recent LLMs suffer from such an issue and whether the proposed method could generalize to recent LLMs. Specifically, the paper does not address if the observed bias is an artifact of older model architectures or training data, or if it persists in more recent models with larger parameter counts and more diverse training sets. Without this, it's difficult to assess the practical relevance of the proposed method. I suggest more experiments to clarify this point. Otherwise, the contribution of this work will be vague or limited. 
2. It seems that the activated neurons vary across different prompts, and gender bias is often implicitly represented by models. The paper's reliance on a women-and-man (or specific-prompt) setting raises concerns about the generalizability of the findings. It's unclear if the selected prompts are representative enough to draw broad conclusions about gender bias. The paper needs to investigate whether the identified neurons remain consistent across a wider range of prompts and contexts, and if the model editing approach can effectively address bias in more complex real-world scenarios.

### Questions
1. Do recent LLMs suffer from gender bias issues (e.g., o1, GPT-4o, GPT-4, GPT-3.5-turbo, LLaMa 3.1, LLaMa 3.2)?
2. With the recent development of LLMs, their “intelligence” keeps growing due to the boost of data volume and quality. Various kinds of bias are less likely to be present in the training data. Could you give some examples of the bias categories represented by recently proposed LLMs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Interpretable Model Editing (Interpret-ME) method, which effectively reduces gender bias in LLMs by identifying key neurons without requiring large datasets or fine-tuning, achieving competitive results while preserving performance in other tasks.

### Strengths
1.	This paper analyzes the neurons in LLMs responsible for storing gender bias, contributing to a deeper understanding of how gender bias exists within these models.
2.	By identifying key neurons associated with gender bias, the paper demonstrates that editing these neurons can achieve better debiasing results with minimal impact on overall model performance.
3.	The paper also explores the importance of different neurons and points out that "FFN query neurons" have the most significant influence on gender bias.

### Weaknesses
The located neurons may not be sufficiently representative. Since only five sentences per gender are used to locate neurons, these sentences may not adequately capture real-world gender stereotypes. Moreover, there is no experiment in the paper that demonstrates whether using more or fewer sentences would affect the performance of the Interpret-ME method.

### Questions
Why is Table 5 not a comparison between the Interpret-ME method, fine-tuning methods, and the original model? Why does Table 5 not include a comparison between the Interpret-ME method, fine-tuning methods, and the original model? I would like to know whether Interpret-ME causes less performance drop compared to fine-tuning methods.

### Soundness
3

### Presentation
4

### Contribution
3
