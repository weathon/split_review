# Evaluating word representation for hypernymy relation: with focus on Arabic

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Hypernymy relation is one of the fundamental relations for many natural language processing and information extraction tasks. A key component of the performance of any hypernymy-related task is word representation. Traditional word embeddings capture word similarity but fall short of representing more complex lexical-semantic relationships between terms, such as hypernymy. To overcome this, recent studies have proposed hypernymy-specific representations. In this study, we conduct an evaluation of several types of word representations to determine the most effective approach for modeling hypernymy relationships in Arabic. We use an Arabic training corpus and several datasets to assess traditional embedding, hypernymy-specific embedding, and contextual embedding across several hypernymy-related tasks, including hypernymy detection. The results indicate that different embeddings have different effects on the performance. Moreover, the performance is affected by the selected datasets. This highlights that there is a need for further research to develop more robust word representation and benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Authors try to evaluate different algorithms, which create hypernymy relation representations in Arabic. They select AraBERT corpus as a base for training all embedding models and train several models on this data. As a baseline for contextual embeddings, BERT is used, while for classic embeddings GloVe is used. For hypernymy-specific embedding LEAR, GLEN, Princare and Poincare Glove is used. After that, a simple feedforward models are trained for all embeddings for three tasks: hypernymy detection, hypernymy directionality detection and semantic relation classification. Results show, that Poincare GloVe performs best on hypernomy detection and hypernomy directionality detection tasks. In semantic relation classification tasks Poincare GloVe performs worse. Overall, there is no best representation for all tasks.

### Strengths
1. The goal of the paper is easy to understand, as it provides valuable insight into which representations are best for hypernym-based tasks (none are best overall)

2. Experiment design makes sense and is mostly without issues. There is a minor issue stemming from the limited resources available to the authors of the paper, but I will touch upon them in the weaknesses part of the review.

### Weaknesses
1. Authors are very constrained in resources, having to resort to halving the size of the training dataset for some of the algorithms. This raises questions to the validity of the collected information, since Poincare GloVe, the best algorithm in Hypernymy Directionality and Hypernymy Detection tasks, has seen only half as many data samples, which can possibly make the results non-representative. However, due to the simplicity of the Poincare GloVe, most likely it won’t impact the results as much, thus, making this just a minor issue.

2. The quality of the text's presentation is poor; it contains numerous typos and improperly formatted tables. Table 7 has incorrectly formatted items in header, Table 8 has incorrectly formatted dataset names, in table 7 the highest F1 score for ASRD dataset is incorrectly attributed to 100D Poincare GloVe, which has the score of 0.88 instead of Poincare Embedding, which have the score of 0.89. On the line 070 BERT has no citation available, on the line 220 the sentence starts from lowercase, on the line 291 the word Assess is incorrectly capitalized, line 480 is cut in half, etc. Both Introduction and Related Work sections are hard to read, since they are written in a big wall of text instead of separate paragraphs on groups of algorithms. Some of the citation years are in brackets (lines 065-068), some are not (line 079).

### Questions
Please, correct the formatting of the paper, it is very hard to read in current condition.

### Soundness
3

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
3

### Summary
This paper focuses on evaluating and improving word vector representations specialized for hypernym relations in Arabic. Your research captures the gaps in hypernym aspects of performance by conducting multiple sets of experiments on different datasets, and this aspect of the research is important for the NLP task.

### Strengths
1. **Relevance**: Focusing on hypernym in Arabic is timely and relevant, and it addresses a less explored area of NLP.
2. **Experiments**: The paper presents a comprehensive experimental evaluation of multiple word representation techniques, demonstrating a solid methodological framework.
3. **New findings**: The findings presented in the paper provide new insights into how Arabic word embeddings can be enhanced to better detect hypernym.

### Weaknesses
1. **Literature Review**: Although the paper discusses related work, a more comprehensive literature review would have positioned the paper's contribution more effectively. I suggest the authors report precision and recall specifically for elements that have both spatial and logical relationships, compared to those with only one type of relationship.
2. **Clarity**: Some sections may lack clarity, particularly in explaining the significance of the research methodology and findings. 
3. **Results Interpretation**: The results section may need to discuss the significance of the findings in more depth, especially in the context of existing models.

### Questions
1. How do the results of your study compare to existing models in other languages, especially in terms of applicability to Arabic?
3. What are the advantages of your study over previous studies? Is a new methodology or a new dataset proposed?
### Additional feedback
- Consider revising the introduction to better outline the motivation for the study and its significance in the broader context of NLP research.
- It may be helpful to include more hypernym examples in Arabic throughout the paper to illustrate your points.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenge of modeling hypernymy relations specifically focusing on Arabic. The authors evaluate various word representation methods to determine the most effective for Arabic hypernymy tasks. They compare traditional embeddings, hypernymy-specific embeddings, and contextual embeddings using an Arabic corpus and multiple datasets to assess their impact on tasks such as hypernymy detection.

### Strengths
1. Word representations for hypernymy are essential for a variety of tasks in NLP and information extraction.

2. By concentrating on the Arabic language, the paper contributes to a less explored area, providing insights for non-English NLP research.

3. The research conducts an evaluation of multiple types of embeddings, including traditional, hypernymy-specific and contextual embeddings.

### Weaknesses
1. The paper primarily focuses on evaluating existing word representations rather than introducing a novel approach or method for hypernymy modeling. The novelty is very limited.

2. The written quality of this paper is poor. The authors should carefully revise this paper for better presentations. For example, the citation format is incorrect.

3. The paper seems to provide an evaluation of performance effects without a deep analysis of why certain embeddings perform better or worse in specific contexts or tasks.

4. The impact of this work in the ICLR community is limited. Maybe an NLP workshop on the Arabic language is more suitable.

### Questions
There are no specific questions here. But I suggest that the authors might consider proposing a novel method or modification in word representation tailored to hypernymy in Arabic instead of solely focusing on evaluation. In addition, this work may be better suited for a specialized venue, such as an NLP workshop focused on the Arabic language. This could provide a more appropriate audience that appreciates the linguistic specificity.

### Soundness
2

### Presentation
2

### Contribution
2
