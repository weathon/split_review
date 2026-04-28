# MisAttributionLLM: Integrating Error Attribution Capability into LLM Evaluation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
With the widespread application of Large Language Models (LLMs) in various tasks, evaluating the performance of LLMs becomes an essential research topic. However, existing judge models lack the specific capability required for error attribution (i.e., identify the types of  error made in responses). In this work, we first establish a comprehensive Misattribution Framework with 9 primary and 19 secondary  categories, which are intended to facilitate in-depth analysis and enhance the performance of LLMs. Based on this framework, we present  AttriData, a dataset specifically designed for error attribution, encompassing misattributions, along with the corresponding scores and feedback. We also propose MisAttributionLLM, a fine-tuned model on AttriData, which is the first open-source, general-purpose judge model  with error attribution capability which provides valuable insights into the model’s weaknesses and enables targeted improvements. Experimental results show that MisAttributionLLM achieves the highest Pearson correlation with human evaluators among 8 open-source  and closed-source LLMs. Furthermore, MisAttributionLLM also obtains the highest accuracy and micro-F1 in the performance of error attribution. Extensive experiments and analyses are conducted to confirm the effectiveness and robustness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors first propose a taxonomy of LLM errors with 9 primary and 19 secondary categories, then annotate a collection of LLM error responses with these categories and use GPT-4 to further write feedback. Finally, the authors fine-tune a 7B model on the annotated dataset and achieve a higher attribute capability than other baselines without finetuning.

### Strengths
1. The idea of implementing large-scale error attribution is relatively novel.

2. The dataset is relatively large with manually annotated data points.

### Weaknesses
1. The research question and motivation is a bit unclear to me. In the introduction, although the authors write ''This oversight tends to result in a misjudgment of the LLM’s performance and is likely to hinder the identification of critical opportunities for improvement.'', it is still unclear what is the importance and significance of the research question. What will happen if we only detect the errors without identifying 19 categories?

2. The biggest concern is the dataset creation. Although the authors collect a wide range of datasets, the rule-based classification that classifies all tasks of the LLMs into 7 categories is not comprehensive enough. For instance, what about the code completion task? For math, there are many types of questions, such as math word problems, GSM8k, etc. It is unclear how the authors collect the datasets and how to cover all tasks with these categories. Even if the dataset is perfect, the categorization is also subjective without good reasoning and classification methods. This makes it a bit difficult to judge the following results of the proposed work.

3. Some experiments are unreasonable. First, naturally, the performance of fine-tuned models is better than zero-shot settings. Can you try to compare it with the few-shot setting of GPT-4 to get the result? Also, do you feed the instructions of each type to GPT-4? Otherwise, it is unfair for other models to compare with.  Furthermore, the accuracy of Misattribution Detection is close to 100, I am wondering if the setting and categories are too simple for LLMs. Finally, multi-classification has not been introduced before, making it difficult to understand the results.

4. The GPT-4 based feedback is doubtful. There is no human annotation to ensure the quality of the feedback. At least some sample and annotated work is needed. Besides, do you train the model on feedback? If so, is the model better than GPT-4 generated feedback?

### Questions
See the weakness.

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
4

### Summary
This paper proposes a framework which consists of 9 primary and 19 secondary categories to facilitate the evaluation of LLMs. Using this framework, it then introduces a dataset for incorporating error attribution capability into LLM evaluation. Finally, it fine-tunes Qwen2-7B with the proposed dataset to obtain MisAttributionLLM for fine-grained evaluation. MisAttributionLLM  shows a strong correlation with human evaluators.

### Strengths
1. By fine-tuning on the proposed AttriData, the authors are able to reach better performance than baselines on most of the metrics, which demonstrate the utility of AttriData. I like the fact that the authors fine-tune an LLM based on the proposed dataset.

2. Based on Section 3, the dataset construction process seems to be rigorous, so dataset quality is not my concern.

### Weaknesses
1. The impact of this paper is limited. As stated in the limitation section, the paper’s primary focus is on a Chinese-language dataset, which restricts the generalizability of the findings. Each language presents unique linguistic features. For example, even when all the error types of your framework exist in English, these error types might appear as different forms than the examples you see in Chinese. Thus, your findings might vary in a different language.

2. This seems to be an incremental work with low novelty. It is not clear to me the difference between the dataset of "Evaluating llms at detecting errors in llm responses" and your dataset.

3. Although the authors claim a comprehensive Misattribution Framework, this framework still appears coarse. I do not see concrete examples of each error type and some of the error types (e.g., hallucination) might need to be further expanded. Please see my question below.

4. Certain error categories, such as those involving multi-turn dialogue and instruction following, may be underrepresented in the proposed dataset, which limits the usability of AttriData. As discussed in line 463, insufficient training data for these two aspects might be a problem for fine-tuning LLMs.

### Questions
1. Would you please clarify line 123? For the paper "Evaluating llms at detecting errors in llm responses", you mentioned that "the types of error they identify are limited". So what is difference of error types between your framework/dataset and theirs? Is this difference really important? I think their dataset uses English so a wider range of audience can be benefited.

2. Since you only work on Chinese-language dataset, I suggest to restrict your findings to Chinese and mention this important information at the very beginning of your paper (e.g., title, abstract, and/or introduction) to make your writing clear. I suggest not to claim something that you have not done.

3. Hallucination is just one error type in your framework. What if the content generated by the model is inconsistent with real-world facts but is still consistent with the user’s input? I suggest to dive deeper in some types such as hallucination error. There are two papers I have read before about taxonomy of hallucination that might help: "FaMeSumm: Investigating and Improving Faithfulness of Medical Summarization" and "Understanding Factuality in Abstractive Summarization with FRANK: A Benchmark for Factuality Metrics".

4. What are the "realistic evaluation scenarios" mentioned in line 211 and 212?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is about improving LLM-as-a-Judge models. The authors curated a large (22K) dataset of LLM-generated outputs in Chinese (or mostly Chinese). They asked 48 human annotators to provide a general score (0-3) and detect misattributions (19 error types predefined by the authors). Then, they fine-tuned 7b LLM on this dataset and conducted experiments with 7 LLM baselines to (1) measure the correlation between the LLM and human general score and (2) measure misattribution detection. The authors show their fine-tuned LLM performs better on the test set of their dataset than other baselines.

### Strengths
* This dataset presents a large collection of human-annotated response quality scores, including misattribution annotations. It is an impressive and timely contribution that will undoubtedly be valuable to other researchers. The labor invested in creating this dataset is unparalleled compared to other preference-based open-source datasets.
* The experiments include numerous (7) baselines.

### Weaknesses
 **Presentation and Missing Details:** The presentation of this paper is lacking, with numerous crucial details missing that are necessary for a proper evaluation. For example (and this is a recurring issue throughout the paper):
* What exactly are the 22K outputs evaluated by the annotators? How were these outputs generated?
* Where did the prompts of those examples originate from? Which models were used?
* What are the dataset statistics? Are all examples in Chinese? If so, what is the language distribution, and why is it only mentioned in the limitations section? This is vital information that both reviewers and readers need in order to properly interpret the results.
* What does a training example look like? How is it used for fine-tuning (this should be illustrated with an example in the appendix)?
* What exactly are the Misattribution Detection and Multi-Classification tasks?
* How are the final LLM answers extracted? What prompts were used for scoring? Are they different from those used for other models?

These are just some key aspects missing from the paper. Please refer to all the suggestions I provided to help improve the overall presentation.

**Irrelevant Misattributions and Their Statistics:** The authors do not provide any statistics on the misattributions, such as the proportion of each type or the correlations between them. I believe that some of these misattributions, like typos or duplications, may not be relevant to current LLMs. Additionally, it's unclear whether the more interesting misattributions, such as hallucinations, process errors, or issues related to long-term memory, were correctly annotated. How can I be certain that the annotators are qualified for this task? The general knowledge of current LLMs often surpasses that of the average human or crowd worker, and it’s unclear how non-expert annotators can reliably identify all hallucinations. This issue should either be clarified in the rebuttal or discussed as a limitation in the paper.

**Related Work**: All the introduction and related work citations are from 2023-2024. It gives the impression that the authors did not conduct an extensive literature review before or during their research. There is a comprehensive body of literature on error analysis in generation models that could have potentially led to a better misattribution framework (e.g., in SumEval, there are coherence and fluency dimensions that are not fully covered by the current framework). I believe the authors could have drawn inspiration from a decade of NLG research.

**Comparison with Other (OOD) Datasets:** The only notable finding from this study is yet another reinforcement of the well-known fact that fine-tuned models perform better in-domain than general LLMs (i.e., if the training and test data are the same, a fine-tuned model will outperform even a larger, more general LLM). This is a well-established result. I would like to compare MisAttributionLLM and other LLMs on different datasets, especially since dozens of preference datasets are available. Furthermore, the ablation study suggests that fine-tuning the model with misattributions does not lead to significant improvement (at best, a 0.01 improvement, which could be due to chance or because the authors likely paid more attention and ran more experiments with the full version).

### Questions
**Suggestions:**

Sort citations order by year (e.g.,  (Xie et al., 2023; Chang et al., 2024; Liu et al., 2024;) instead of (Chang et al., 2024; Liu et al., 2024; Xie et al., 2023)

033: I don't understand what "to guide the LLM in its continuous improvement" means.

036-038: Need rephrasing.

118: Judge LLMs that beside a score and output feedback, can identify misattributions however - it is given in natural language. The main difference is that the missattributions need to be extracted from the feedback, unlike what you propose -- but it is better to write it clearly.

120: Error attribution has been researched for decades in NLG, many papers break the evaluation into different dimensions.  Scoring low in the dimension can be thought of as an error. 
For example: 

https://arxiv.org/abs/2307.10928

https://arxiv.org/abs/2310.00752

https://aclanthology.org/2022.acl-long.531/

I would emphasize that several misattributions can occur at the same time.

257: Kappa is on a -1 to 1 scale and is not percentages.

266: Nothing is "illustrated"  in Figure (2).

267-270: The letter notations are not used, so I think you can omit it.

Caption of Figure 2: Please provide more details in the caption.

320: What is the fine-tuning data? what does it contain? How a does data instance look? Can you provide examples in the appendix? I can't understand what is contains... all the components from the inference? Only the misattributions? 

What about dataset statistics? The distribution of the misattribution? Correlation between misattribution? What are the correlations between each misattribution and the score?

Table 2: Remove "_" from column names.  What exactly does the "Human(GPT-4 assisted)" mean? Is it only because GPT-4 generates feedback, or do annotators use GPT-4 in their annotations? Please answer here and use the caption to elaborate, this is important (also for GPT-4(human assistant, I can't understand what it means...)

What are the prompts you use for the LLMs? Do you use few-shot? Any advanced LLM-as-a-Judge technique?

What is the language of the MisAttri dataset? How many English examples there are? How many Chinese? Any other languages? Can you provide statistics?

351: I guess every 2nd-year student knows what it F1 is; you can remove the five sentences explaining it to save space.

348: What is the difference between Misattribution Detection and Multi-Classification? Why do you write five sentences about the F1 score but not elaborate on the specific prediction tasks in your paper? I guess that for Misattribution Detection, the task of the LLM is to predict True or False for each error type (do you use all the 19 error types in the prompt? one by one? Do you ask the LLM to explain? Many missing information...). I guess you specify the error types in the prompt for the Multi-Classification and ask it to mention only relevant errors. Again, I can't evaluate the paper correctly if I can't understand what you did, the tasks, and how exactly you have implemented the experiments (I don't care about the hardware and number of epochs,... I am asking for much more basic information; how can I tell that you don't have flaws in the instruction of the prompt or how you evaluate and extract LLM answers?).


Figure 3: Notice that there is no left or right, but upper and lower model.

Figure 4: I do not like the "radar charts", I (personally) cannot read them - I suggest using barplots for each misattribution category (thus supporting comparison between models).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The author propose a framework, a dataset and a model to deal with the problem of misattribution consists of 9 primary and 19 secondary categories. The Misattribution Framework provide fine-grained labels for the misattribution problem (instead of a score). The AttriData dataset developed for incorporating error attribution capability into LLM evaluation. The author also train model with the AttriData dataset (named MisAttributionLLM), and the experiment shows that the MisAttributionLLM trully have the ability to judge error attribution.

### Strengths
1. Fine-grained error attribution is a important and interesting topic. 


2. MisAttributionLLM prove it can prediction error attribution in answer better then GPT-4

### Weaknesses
1. There is no judgment about whether GPT-4's feedback is reasonable or not in AttriData training set.

2. The instruction and question collection process is not clear. I can't figure out how the author collect them and if them may have copyright (or other) issues.

### Questions
1. What is the category design principle in the Misattribution Framework? Maybe different people have different opinions on the category design. (I admit that this question does not have a ground truth answer, and I won't lower the score because of this question, but I think it's interesting to discuss this question in the paper.)

2. Introduce Pearson, Spearman, and Kendall-Tau in appendix.

3. How many data have multiple error attribution in the AttriData dataset? It is also an important part of the statistics.

4. (minor) Change the example in Figure 2 to a multiple Misattribution QA example. Or it may mislead the reader to think that one question only has one error attribution.

### Soundness
2

### Presentation
3

### Contribution
3
