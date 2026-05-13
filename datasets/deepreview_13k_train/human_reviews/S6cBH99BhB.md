# Enhancing Multilingual Reasoning in LLMs: Insights from Cross-Linguistic Correlations and Optimal Data Proportions

- Decision: Accept
- Scores: 5, 8, 5, 8

## Abstract
Large language models (LLMs) typically rely on fine-tuning to enhance their reasoning capabilities across various languages. However, limited research has been conducted on the optimal balance of language proportions within multilingual reasoning datasets. To fill this gap, we performed a systematic study to examine how different proportions of language data in multilingual reasoning datasets influence fine-tuning performance. Our study revealed a clear relationship between language proportions in datasets and the fine-tuning performance of LLMs. By fine-tuning multiple LLMs using the appropriate language distributions and data volumes identified in our study, we achieved state-of-the-art performance in both multilingual mathematical reasoning and solving mathematical problems using Python code. Furthermore, our approach significantly reduced data volume requirements and translation costs compared to existing methods, providing a valuable reference for future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates how varying language proportions in multilingual reasoning datasets impact the fine-tuning performance of large language models (LLMs). The authors aim to demonstrate that carefully balancing language data can enhance LLM performance, achieving state-of-the-art results in multilingual mathematical reasoning and problem-solving while reducing data and translation costs.

### Strengths
There is significant interest in optimizing the pre-training or fine-tuning mixtures for multilingual LLMs, and this work aims to provide valuable insights into this area.

### Weaknesses
W0: The overall writing of the paper lacks coherence, making it difficult to follow the experimental phases. The fragmented presentation of the experiment phases obscures essential aspects of the study, such as training characteristics, the mixture used for fine-tuning, the evaluation tasks, metrics, and analysis. Additionally, several figures, such as Figure 3, lack complete captions, contributing to the confusion. There is also repetition in section headers (e.g., "Phase 2" in Lines 269 and 320), which affects readability and structure.

There are a lot of points and claims that lock in motivation and support:
- W1: Why is language alignment only studied within the context of mathematical reasoning? The rationale for limiting the focus to this particular setting is unclear.
- W2: What criteria were used to select the 10 or 25 languages? How are "high resource" languages defined in this context? Is the selection based on a specific pretraining dataset, and is there a reference for this?
- W3: The grouping of languages appears arbitrary. What was the basis for forming these specific language groups?
- W4: In Line 189, why did the authors choose only high-resource languages for language alignment when, as stated in Line 35, the problem primarily impacts low-resource languages? This choice seems to contradict the motivation expressed in the introduction.
- W5: In Line 45, the paper claims, "The key is to efficiently leverage a small amount of low-resource language data to broadly enhance the multilingual reasoning capabilities of LLMs." Is there any literature or existing research that supports this assertion?

W6: It appears that the evaluation was conducted solely on the MGSM benchmark. This raises concerns about overfitting the optimal mixture to this specific benchmark. How can the proposed method for creating an "optimal mixture" be generalized to other benchmarks?

### Questions
Q1: Many references are missing from the claims presented in section 1/ introduction

Q2: Figure 2: Is this data format known for the literature about its performance? Where is the reference?

Q3: Line 076: The motivation for the language extension from 10 to 25 is not clearly explained. What does it mean that the authors extended the language coverage to 25 languages?

Q4: It might be better to provide the full language names in the tables instead of the language codes since, depending on the implementation and the taxonomy used, the codes might be different. 

Q5: Please provide captions on all the figures.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper shows a way to enhance multilingual reasoning in LLMs by optimizing the proportion of language data in multilingual reasoning datasets. It addresses challenges in fine-tuning LLMs for low-resource languages, which often lack sufficient training data, by investigating the impact of language proportions on model performance. The paper shows optimal language ratios and volume of data for fine-tuning. The paper also present 'HighMath-350k' and 'HighCode-350k' datasets for multilingual mathematical reasoning and Python-based problem-solving.

### Strengths
The paper shows a unique way to improve multilingual reasoning in LLMs by optimizing the dataset language proportions and that is highly relevant for AI applications. This work contributes a systematic approach to identifying optimal language data ratios. Also, the paper shows extensive methodology and use of Gaussian Process Regression for language group optimization. The outcome/resultant datasets from this work (HighMath-350k and HighCode-350k) are specifically for multilingual reasoning tasks and that will be helpful for future research in this field.

### Weaknesses
There are 25 languages in the phase3 of this study. But in phase 1 and 2, they used a smaller subset. How does this difference may affect the generalizability of findings to low-resource languages is not covered. Also, the datasets generated in this study are based on Non-English to English translation task. However, the study does not cover how to safeguard against translation inaccuracies in low-resource languages. The paper does not discuss the potential impact of varying translation quality across different language pairs on the final results. Specifically, the study does not address whether the performance gains observed are consistent across all languages or if some languages benefit more than others due to better translation quality. Furthermore, the paper lacks a discussion on the computational cost associated with the Gaussian Process Regression used for language group optimization, which is crucial for reproducibility and practical application of the method.

### Questions
1. How do you plan to do quality control for translations in languages where direct verification might be challenging?
I am asking this question because some low-resource languages may not generate accurate translations in English or vice-versa. It would be interesting to know the author's view on this.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a systematic study on the impact of language data proportions in multilingual reasoning datasets on the fine-tuning performance of LLMs. The authors claim to have identified optimal language distributions and data volumes for fine-tuning, leading to state-of-the-art performance in multilingual mathematical reasoning and solving mathematical problems using Python code. The study also aims to reduce data volume requirements and translation costs compared to existing methods.

### Strengths
The paper addresses a significant gap in the literature regarding the optimal balance of language proportions in multilingual reasoning datasets for LLMs.

The research is methodologically sound, with a clear three-phase approach and over 600 groups of experiments providing a robust basis for the findings.

### Weaknesses
The paper outlines a three-phase methodology to minimize the search space to a manageable size. A crucial step involves categorizing languages based on their alignment with English. It raises questions about the general applicability of the findings. If a LLM is trained primarily based on non-English datasets, does it still work?

As stated in the abstract, the paper asserts that it achieves state-of-the-art performance in both multilingual mathematical reasoning and in solving mathematical problems using Python code. However, the experimental section lacks empirical comparisons with existing benchmarks that utilize Python code. Specifically, while the authors mention comparisons in Figure 10, the lack of explicit baseline details in the figure caption makes it difficult to assess the true significance of the results.

Lastly, the presentation requires further enhancement. The font size of the figures is too small, and it would be beneficial to include descriptions for figures, such as Figure 3 and Figure 7.

### Questions
In line 252, Figure 3 depicts the variations in translation performance. Which LLM do the results in the figure pertain to? Is the correlation consistent across different LLMs?

In lines 256 to 259, Figure 4 assesses the model's performance on the MGSM dataset after fine-tuning with various non-English to English translation pairs. However, does the author take into account that fine-tuning with WMT datasets might lead to a decline in mathematical reasoning performance?

In lines 368 to 370, when extending 10 languages to 25 languages, how to get the ratio of en:de:ru:fr:others = 24:8:8:8:12?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
LLM gains reasoning ability across multiple languages after finetuning. The typical approach is to use the same amount of data entries in each language during finetuning. This paper points out that it is more efficient and effective when the proportion of each language is different. Thru a 3-phase systematic approach, authors found the optimal balance in terms of the proportions and achieved the SOTA performance in math reasoning and python code reasoning. It effectively reduces the data volume and translation cost needed during finetuning for multilingual reasoning.

### Strengths
The paper is well written and nicely presented with comprehensive tables and figures.

The topic discussed is original and significant, especially during the finetuning stage; that is equal amount of data entries in different languages may not result in the optimal performance. 

Authors made it clear that via experiments; by strategically distributing the amount of data across multiple languages, the multilingual reasoning ability can be acquired at much cost.

The experiment covers 25 languages and most performant open source LLMs.

Authors created two multilingual datasets, namely HighMath-350k and HighCode-350k.

The idea, "given a fixed amount of data volume, how to achieve the optimal performance by including the right amount of data for each aspect", can be borrowed at different stages of the training process, which will lower the cost of training as well as the GPU hours needed.

### Weaknesses
There are some minor grammar issues, such as no space after a comma or a period. For example, line 221 "selection,in ..." and line 231 "system.In ..."

Another minor layout issue is that the last two figures split the conclusion onto two pages.

Figure 3 and figure 7 might need some description briefly explaining the purpose for improved readability.

Figure 3 depicts three scores (COMET, BLEURT, BLEU), but there is no elaboration in the context about them.

It is unclear why the authors only adopted finetuning from non-English to English translation pairs and omitted bi-directional pairs in phase 1. This limits the exploration of potential benefits from English to non-English transfer.

Finetuning configuration is not properly documented, making it difficult to reproduce the results or understand the specific training setup.

The translation of dataset is solely based on the model DeepSeek-Chat-v2-236B. Even though authors adopted some methodology to ensure the quality of translation, like preserving formulas and using Arabic numerals, the validation of the translated content can be improved. For example, a subset sampled from the translation can be further validated by native speakers for coherency and consistency. The lack of human validation introduces a potential bias in the dataset.

### Questions
1. what was the reason that English to Non-English translation is not explored?

2. (line 208) what are the two examples used in the prompt? 

3. (line 215) what's the percentage of discarded data entries? 

4. does the pattern / ratio found in this paper single-purposely apply to math reasoning dataset? could it generalize to other multilingual tasks? or should researchers and developers follow the 3 phases and look for a new ratio?

5. (table 1) why is only llama3 investigated in phase 3?

6. (figure 3) the reasoning performance dropped after finetuning (like Swahili), and the dropped amount is close to the improvements. how should we understand this phenomenon?   

7. can you explain the reason why model llama2 was not shown in Table1 but used in phase 3 in the experiment?

### Soundness
3

### Presentation
3

### Contribution
3
