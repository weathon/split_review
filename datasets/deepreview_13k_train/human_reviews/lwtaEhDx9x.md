# Elephants Never Forget: Testing Language Models for Memorization of Tabular Data

- Decision: Reject
- Scores: 5, 8, 3, 3

## Abstract
While many have shown how Large Language Models (LLMs) can be applied to a diverse set of tasks, the critical issues of data contamination and memorization are often glossed over. In this work, we address this concern for tabular data. Starting with simple qualitative tests for whether an LLM knows the names and values of features, we introduce a variety of different techniques to assess the degrees of contamination, including statistical tests for conditional distribution modeling and four tests that identify memorization. Our investigation reveals that LLMs are pre-trained on many popular tabular datasets. This exposure can lead to invalid performance evaluation on downstream tasks because the LLMs have, in effect, been fit to the test set. Interestingly, we also identify a regime where the language model reproduces important statistics of the data, but fails to reproduce the dataset verbatim. On these datasets, although seen during training, good performance on downstream tasks might not be due to overfitting. Our findings underscore the need for ensuring data integrity in machine learning tasks with LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper specifically targets the issue of contamination in training sets when evaluating LLMs on tasks with tabular data.
Compared to previous work on LLMs for tabular data, the authors propose methods to test the LLM for memorization (in addition to the dimensions "knowledge" and "learning").
These novel tests help to better analyze and understand the performance on downstream tasks, such as deciding if the data has been seen in training or not.

### Strengths
* LLMs are pervasive currently, and it's important to understand and control their behavior. The authors emphasize the importance of verifying data contamination before applying LLM.
* Their setup based on tabular data is an elegant way to test “knowledge”, “learning”, and “memorization” of an LLM.
* Moreover, they assume only blackbox API access, without assuming access to the probability distributioin over tokens or the ability to re-train the model.
* Release of an open-source tool that can perform various tests for memorization.

### Weaknesses
My main point of criticism is that the paper feels a bit like a collection of remarkable examples and the analysis largely confirms known concerns/behavior of LLMs. The experiments, while interesting, don't seem to offer a fundamentally new understanding of LLM capabilities or limitations, but rather re-iterate existing knowledge about memorization and statistical reproduction. The paper lacks a deeper theoretical analysis of why certain datasets are memorized and others are not, or what specific characteristics of the data lead to statistical reproduction without verbatim memorization. 

"we also identify a regime where the language model reproduces important statistics of the data, but fails to reproduce the dataset verbatim": It's not clear to me what this statement means. Specifically, what constitutes 'important statistics' and how is this regime different from cases where the LLM simply fails to generate meaningful output? The distinction between reproducing statistics and verbatim memorization needs to be more clearly defined and justified with concrete examples beyond the California Housing dataset.

Just echoing the authors: "A limitation of our work is that we do not have access to the training data of GPT-3.5 and GPT4." I.e., the interpretation of results often remains speculative. This limitation significantly impacts the strength of the conclusions, as the authors can only speculate about the source of the memorization and statistical reproduction. The analysis would greatly benefit from a more rigorous approach to identifying and characterizing the training data used by the LLMs.

Figure 3: Why are some results with gpt-3.5 and some with gpt-4? The choice of which model is used for which dataset is not clearly justified and makes it difficult to compare results across models. 

Typo: "two publicly available dataset that are highly memorized"

Typo: "UCI repository athttps://"

### Questions
1. "​​An important result of our investigation is to identify a regime where the LLM has seen the data during training and is able to perform complex tasks with the data": Don't LLMs behave as expected on some data and not on other? How does this work help to control the behavior of LLMs?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
LLMs are increasingly being applied to various types of data, including tabular data. Since, at the moment, the most advanced LLMs are essentially black-boxes w/ restricted APIs with little details available about their training data, it is hard to tell a priori whether the tabular data was leaked into the training and whether the models have memorized it.
This paper proposes four tests that probe an LLM for the training data contamination and estimate the degree of the contamination (“knowledge”, “learning”, “memorization”).

In the experimental study, the paper focuses on ChatGPT 3.5 & 4 and 10 tabular datasets, which have a high chance of being in the training data obtained by crawling the Internet (Iris, Kaggle Titanic, …). 

First, the authors show that both LLMs have memorized basic meta-data from the datasets. Next, the LLMs are probed for an ability to reproduce a dataset example, conditioned on a part of its features. As an example, on the Adult Income dataset, the LLMs completed EduNum feature significantly better than a marginal distribution baseline. Further, the authors propose “zero-knowledge” prompting technique where the model is prompted to sample samples from a dataset (unconditionally or conditionally), provided samples from other datasets. Using that approach, the authors show that the models often can reproduce the distribution of the data in some datasets (approximately). Finally, the models are probed to reproduce parts of the datasets verbatim; for some datasets that happens extremely often.

Additionally, S5 provides a comparative analysis of the LLMs performing few-shot classification tasks on a subset of datasets, in comparison to standard ML baselines. It turns out that the LLMs have marked drop in performance on some datasets that are likely absent in training (Pneumonia & Spaceship Titanic); at the same time very high performance on datasets that are likely to be memorized (Kaggle Titanic).

### Strengths
* I believe this work (a) raises an important overlooked question, (b) addresses it, (c) by proposing an original technique. I particularly like the zero-shot prompting technique that allows sampling from a dataset w/o leaking information in the prompt.
* The paper disentangles a few levels of training data contamination and comprehensively tests for those.
* The paper showcases the potential impact of the contamination on the downstream comparisons, hence proving a strong motivation to the work. 
* The text and the story are clear.
* The code is made public.

### Weaknesses
 * The paper only studies ChatGPT-3.5 and 4. Those are very likely to be strongly correlated in terms of the data used, which harms the representativeness of the study.
* As there is no ground-truth knowledge on whether a particular dataset was seen at training, it is impossible to strictly verify the findings. Including an LM trained on a known dataset would allow us to verify the used methods.
* Another related issue: the work is mostly relevant when we consider closed-data models w/ a black-box API access. This scenario reflects a dominant situation at the moment, but it is not given that this will not/should not change.

Minor:
* Table 1 is mentioned on page 3, yet only appears on page 6. Is there a way to bring it closer?
* Would it make sense to consider swapping sections 5 and 6? I feel the S6 is more connected to the S3-4 than S5.

### Questions
I wonder if authors would be willing to address the first two points in ‘weaknesses’.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a discussion on data contamination and memorization in large language models concerning tabular data. The authors propose multiple methods to examine whether an LLM has memorized specific tabular datasets during training. The paper also proposes methods to examine knowledge, learning, and memorization separately and discuss the distinction between them. Finally, the paper analyzes the influence of learning and memorization on the performance of downstream tasks, and advocates checking memorization as a crucial step in evaluating LLM on tasks with tabular data.

### Strengths
The paper presents several novel methods to evaluate memorization of tabular data in LLMs, and evaluation results on a series of datasets correlate well with the publication time and availability of the data, confirming the effectiveness of the proposed methods in identifying memorization. The different evaluation methods also complement each other, elucidating the different aspects of memorization of tabular data.

The paper is overall well-written and very easy to read, the visualizations present the main findings nicely.

The contamination and memorization of training data by LLMs is a critical issue. The findings provoke essential discussions on the evaluation of LLMs on tabular data, which is likely to become more relevant given the rising usage of LLMs in diverse tasks. 

The introduced tools and code potentially provide easy and accessible ways to evaluate memorization of tabular data, reusable in future research.

### Weaknesses
Some important details in the experiment design may be missing or incomplete: 

* Evaluation metric for knowledge, learning, and memorization is unclear. In Table 1, the evaluation results are categorized into three categories (✓,X, and ?), but the metric for the categorization is not given. It is probably a better idea to show the raw values (e.g., accuracy) than using categories to give the reader a direct comprehension of the degree of memorization on each dataset. Notations such as "✓" could be misleading as it may be confused as perfect memorization.

  The appendix gives raw accuracies for Row Completion Test, Feature Completion Test, and First Token Test, why raw accuracies for Feature Names, Feature Values, and Header Test are not provided as well?

* The differentiation between learning and memorization is not clear: the authors use feature distributions to examine learning, but memorization can also result in a high similarity of the generated data's feature distributions to the original data. Learning is defined as the model's ability to perform tasks in the current paper, but task performance is heavily affected by memorization and may fail to reflect true learning. Even with considerable discussion, the paper does not seem to arrive at a conclusion about how learning can be clearly assessed.

* Evalulation of memorization needs to take the nature of data fields into consideration. Some data fields in the tabular dataset are considerably harder to memorize verbatim or to predict exactly (such as measurement values) than other simpler fields (categorical values such as sex, occupation, nation). For numerical values, it may be more reasonable to measure the relative distance from the predicted value to the true value than using exact match (perhaps in a similar vein as the "first token test" in the paper but more principled).

  Under the current evaluation protocol, it is likely that datasets containing more easy fields are more likely to be judged as memorized. To compare the degree of memorization across datasets, it seems necessary to perform some kind of "normalization" before measuring memorization, for example, selecting a fixed number of categorical and numerical fields from each dataset. Results in Table 3 could suffer from this limitation as well.

* Evaluation of memorization needs to be evaluated separately for the training and test split. It may be possible that the training sets are memorized more than the test set due to more exposure on the internet. Memorizing the test set definitely compromises evaluation, but memorizing the training set may not always compromise evaluation.

* Connection between memorization and downstream performance is not reliably established. The main observation from Section 5 is that for datasets with a high degree of memorization, LLM performs better than decision tree and logistic regression, while for datasets with a low degree of memorization the reverse is true. Such observation alone may not be sufficient to conclude that memorization compromises evaluation, because there is no evidence that LLM cannot perform better than decision tree and logistic regression under no memorization. It would be much better to solicit new test sets for the tasks to use in evaluation, which can be used to show exactly how much performance gap is caused by memorization. In case finding new examples is difficult, perhaps one can modify the values of the fields known to be irrelevant to the label in existing examples, and that may break the reliance on memorization in LLMs.

Some main conclusions of the paper are compromised because of the above limitations:

* "We emphasize the importance of verifying data contamination before applying LLMs": the implication of data contamination is not reliably demonstrated in Section 5.

  Also, from the current discussion, it is not very clear how to interpret the test results on knowledge, learning, and memorization together. For example, if knowledge and learning show positive results and memorization show negative results, should we conclude that there is data contamination or not? And could the performance on downstream tasks be trusted in this situation?

  It can be argued that knowledge and learning will not directly compromise evaluation on downstream tasks, so there may not be as much need to evaluate them compared to memorization. I would suggest allocating more space in the paper for extended experiments and discussions on memorization, which is the ultimate reason why people are concerned about data contamination. 

* "... and propose practical methods to do so": the proposed method verifies memorization of data, but does not give a definite metric to judge when memorization is severe enough to compromise evaluation.

* "We offer a principled distinction between learning and memorization in LLMs": the distinction is not given clearly enough. One can tell whether there is memorization from the proposed test, but it is not clear how to tell whether learning exists (especially when memorization is present).

### Questions
What is the difference in the remembering behavior of LLM between tabular data and non-tabular data? The question may help strengthen the original contribution of the paper.

In the beginning of the discussion section, the use of the term "representation learning" may be confusing to some people. Representation learning usually refers to the process of learning useful features from raw data (wikipedia), which does not include memorization by definition.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims at inspecting data contamination which happens when training a large language model. Specifically, they inspect whether some tabular datasets were used to train the language models. For this purpose, they propose several approaches to testing the language models.
- Testing for Knowledge and Learning:
    - Meta data: Testing whether the model can predict the name of the fields in the datasets.
    - Conditional completion: Testing whether the model can predict the value of a feature of a sample based on some other features.
    - Unconditional zero-knowledge samples: Testing whether the model produces the statistics of the features in a datasets.
- Testing for memorization:
    - Testing whether the model can generate rows based on the previous rows (either the first a few rows or a few rows starting from a random line) in the dataset csv file.
    - Testing whether the model can generate the correct value of a feature based on the value of the other features. Here the value is “unique”.
    - Testing whether the model can generate the first token of the next row.

Finally, they compare the language models’ performance on several datasets with some baseline models’ performance, and conclude that some models’ performance can be attributed to their memorization of the datasets during pretraining.

### Strengths
- They propose several methods to test whether the language models were trained with those datasets.
- The idea of comparing the distribution generated by the model and the distribution in the datasets (Sec 3.3) is novel and interesting.
- The claim that they show that some language models are pretrained with some tabular datasets is somewhat convincing and interesting.

### Weaknesses
Main concerns:

1. This work does not provide strong evidence supporting the validity of their proposed approaches. I think one main takeaway of this paper is that some models are pretrained with some datasets, so their performance is not indicative of. But this takeaway is based on the validity of their proposed approaches. I think the authors need to address this more. Specifically, the paper lacks a rigorous analysis of how well the proposed tests actually measure data contamination. For example, the metadata test relies on the model predicting column names, but it's unclear if this is a reliable indicator of pre-training on the specific tabular data. The conditional completion test, which predicts feature values based on other features, could be influenced by general knowledge rather than specific memorization of the dataset. A more thorough validation of these tests is needed, perhaps by testing on synthetic datasets with known levels of contamination or by comparing the results with other established methods for detecting data contamination.
2. I can’t understand the purpose of having these many different testing approaches, probably because the structure of this paper is hard to follow. The authors propose many approaches, some of them are interesting, but they do not provide a holistic interpretation of the results from these many approaches. It's unclear how the different tests relate to each other and what each test is specifically designed to capture. For example, how does the 'unconditional zero-knowledge samples' test differ from the 'conditional completion' test in terms of what it reveals about the model's training data? A clearer explanation of the motivation and interpretation of each test is required. The paper needs a more cohesive narrative that ties the results of the different tests together to provide a more comprehensive picture of data contamination.
3. The descriptions of the testing approaches are vague and not rigorous. Writing down the testing approaches with simple math equations could help. For example, in page 6, I can’t understand what it means by “we can perform a t-test between the similarity of model completions with actual vs. random rows.” The paper needs to define the similarity metric used in this t-test and explain how the random rows are generated. The description of the memorization tests, such as generating rows based on previous rows, lacks details on how the model is prompted and what specific metrics are used to evaluate the generated outputs. The lack of formal definitions makes it difficult to reproduce the experiments and to assess the validity of the claims.
4. Knowledge, learning, memorization should be defined more specifically. The paper uses these terms without providing clear definitions, leading to ambiguity in the interpretation of the results. For instance, what constitutes 'knowledge' in the context of this paper? Is it the ability to predict column names, or is it something more? Similarly, how is 'learning' distinguished from 'memorization'? The paper needs to provide precise definitions for these terms and to explain how the proposed tests measure each of them.
5. The authors (claims to) show data contamination exists in some datasets. However, I am not sure whether those datasets are commonly used to benchmark the language model. Thus I am not sure whether the findings are important (if they are valid). The paper needs to provide more context on the datasets used and their relevance to the language model benchmarking community. If the datasets are not commonly used, the significance of the findings is questionable. The authors should clarify whether the observed data contamination affects the performance of the language models on standard benchmarks.

### Questions
1. Figure 1: I suggest to use bar charts is more reasonable because your x-axis is not continuous.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
