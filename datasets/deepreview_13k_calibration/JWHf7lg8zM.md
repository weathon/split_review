# MultiContrievers: Analysis of Dense Retrieval Representations

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Dense retrievers compress source documents into (possibly lossy) vector representations, yet there is little analysis of what information is lost versus preserved, and how it affects downstream tasks. % like question answering and summarisation.
We conduct the first analysis of the information captured by dense retrievers compared to the language models they are based on (e.g., BERT versus Contriever).
We use 25 MultiBert checkpoints as randomized initialisations to train \textbf{MultiContrievers}, a set of 25 contriever models.
We test whether specific pieces of information---such as gender and occupation---can be extracted from contriever vectors of wikipedia-like documents. We measure this \textit{extractability} via information theoretic probing. We then examine the relationship of extractability to performance and gender bias, as well as the sensitivity of these results to many random initialisations and data shuffles.  
We find that (1) contriever models have significantly increased extractability, but extractability usually correlates poorly with benchmark performance 
2) gender bias is present, but is \textit{not} caused by the contriever representations 
3) there is high sensitivity to both random initialisation and to data shuffle, suggesting that future retrieval research should test across a wider spread of both.\looseness-1
\footnote{We release our 25 MultiContrievers (including intermediate checkpoints), all code, and all results, to facilitate further analysis

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes a suite of Contriever retrieval models, each initialized from a different pre-trained BERT model. The primary aim of the paper seems to be examining the extent to which contriver representations capture aspects such as gender and occupation (referred to as topic in the paper) of the subject of a document and to what extent this information correlates with retrieval benchmark performance. The paper presents results showing: 1) contriever models see a large variation in performance based on random seed 2) while gender and topic are more extractable from contriver representations than BERT, the ratio of the two is more extractable from BERT. 3) Extractability of gender and topic dont correlate with performance on the retrieval benchmarks.

### Strengths
- The paper presents an analysis of retrieval model representations that has not been done before.
- The results presented may be useful for future model development work for retrieval tasks.

### Weaknesses
 - Motivation and framing: Examining the extractability of gender and occupation and attempting to correlate this with benchmark performance seems undermotivated and distracting - it's unclear why one would expect these two pieces of information to be crucially important for performance on the datasets. (on the other hand, the analysis with gendered queries seems reasonable)
- Experimental details: The experimental section seems less than ideal in rigor, the writing in the paper is a bit scattered, and the figures are quite poorly labeled for a paper that is largely result-driven.



### Questions
- I would highly encourage referring to "topic" in the paper as "occupation" - this is much clearer and seems much more true to the data used for analysis (even the original paper seems to refer to this as occupation: https://arxiv.org/abs/1901.09451). The current presentation also makes it seem like the papers scope is much larger than it actually is. Else, please rationalize the scope and the framing of the analysis in greater detail.
- Several claims in the paper ("This highlights the gap between ... a limitation of the benchmark", "lack of correlation between extractability and performance points to a mismatch between the self-supervised contrastive training objective ...") seem to imply that there is a problem with the BEIR benchmark tasks or the training objective for contriver because while the training improves extractability of gender and occupation it does not correlate with the benchmark performance. This is not a reasonable inference - an alternative is that the two attributes examined are insufficient for explaining the underlying signals captured by the benchmark tasks and for studying the influence of training. For example training may be improving the extractability of several other attributes not examined in this paper which may better explain benchmark performance. Please soften these claims and discuss the limitations of the attributes examined in this paper (which would of course not be a slight on this work).
- Table 1 and Figure 1: Thank you for this analysis, this is interesting. While I understand that the analysis is somewhat tangential to the point of the paper, I would recommend some changes to strengthen this analysis: 1) It seems a bit misleading to report the max-min difference for various seeds as a measure of variance based on the seed. Please also report the standard deviation in performance across seeds - this is more common for reporting this kind of variance: https://arxiv.org/abs/2302.07778. 2) Please report similar statistics for other metrics like Recall@100. It may be the case that the large gaps in performance are a result of the metric choice (eg exponential gain in computation of NDCG) and the presence of unjudged documents in retrieval datasets. Deeper rank metrics will alleviate the latter issue. It would also be illustrative to understand the Recall since dense retrieval systems are usually used for a high recall first stage retrieval. 3) A few of the datasets used in the BEIR benchmark are quite small (~50 queries). Please consider computing statistical significances for the max-min differences. The differences are unlikely to be significant for all the datasets. 4) It is unclear why the seeds influence performance so much - please consider discussing this in greater detail - do the representations change massively due to random seeds? Do the score distributions for positive vs negative change across seeds? (similar to: https://proceedings.mlr.press/v162/menon22a.html) etc.
- Please add a main number/caption for all figures and label the axis of plots aptly - they are missing in many places.
- It's unclear what the procedure for measuring extractability of the gender:topic ratio is - please clarify this better.
- Please consider citing: https://dl.acm.org/doi/10.1145/3234944.3234959

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an information theoretic analysis on the dense retrieval representation, obtained using the contrastive loss, by providing the extractability metric. Focusing on two types of information – topic and gender, the paper observes 1) the contrastive learning increases the extractability of both topic and gender, 2) but the extractability is poorly correlated with the IR benchmark performance, and 3) the allocational gender bias is observed, but the bias is not reduced after removing the relevant gender information (using the null space projection). Overall, this work presents a series of interesting observation on information bias entailed from the dense retrieval representation.

### Strengths
- The proposed probing analysis based on the extractability for exploring the dense retrieval representation is quite interesting and novel. 
- The reported analysis on topic and gender is also valuable and useful; The extractability does not necessarily entail the retrieval performance, and the bias such as gender bias is not originated from the representation itself, etc.

### Weaknesses
 - The probing analysis such as the correlation b/w the extractability and the retrieval is explored well. But, it is unclear how to applying the current probing analysis to obtain better retrieval or application tasks. How the retrieval method is modified such that the extractability is helpful to improve the performance? 
- The current experiment is restricted to only two types of information – topic and gender. An extension to other types of bias is desirable. 
- The extractability is considered as the only metric for this probing method, but other metrics need to be discussed and considered for extracting target types of information.

### Questions
- How the probing model is designed? 
- It seems that the retrieval performance is reported for all queries. What is retrieval performance when using the topic/gender-related queries are examined? 
- What is the motivation that the "contrastive learning" to obtain the dense representation can further enhance the extractability?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors initialize Contrievers from the MultiBERTs and evaluate on BEIR. The goal of the work is to measure how sensitive Contriever is to random initialization. There is variance on the BEIR data, but there is something not clear about whether the correct reference numbers are used, and more importantly, it remains unclear if data shuffling is more important than random initialization and BEIR may not be fully representative of supervised retrieval. In contrast, the results pertaining to gender and topic bias show low variance, but perhaps should factor in findings from previous works associated with gender bias and retrieval.

### Strengths
1. It will be interesting for the community to see detailed analysis pertaining to random initialization of dense retrievers. Although, it is not clear that BEIR is the correct evaluation set here, since it does not involve supervision---it could be the models show low variance when trained on supervised retrieval.

2. There is extensive experiments and analysis on BEIR and also on gender/topic bias. Although sometimes the plots are hard to read, and there are multiple concerns about the data and model choice.

3. The models and intermediate checkpoints will be released. Although it could be helpful to include at least one model that has the same weight initialization, but different data shuffling.

### Weaknesses
1. The evaluation tasks are designed for a specific subset of retrieval that is notoriously hard. Perhaps evaluation on fully supervised retrieval would be more informative.

2. It is interesting to study variance in retrieval, but Contriever is not especially competitive compared to more recent dense retrievers.

3. I am not sure the reference numbers for contriever are correct. I checked the contriever paper and saw ndcg@10 is 75.8 instead of 68 for Fever, and is 67.7 instead of 65 for scifact. More generally, the claim that some Contriever random seeds outperform some "supervised" models remains confusing since those models are not supervised directly on BEIR and are often outperformed by unsupervised models like BM25. Although more modern models will likely outperform both Contriever and BM25, such as GTR. Contriever paper, https://openreview.net/pdf?id=jKN1pXi7b0

4. The plots are very hard to read with blurry and small text.

5. Perhaps this is the first paper to apply probing to dense retrievers, but there are many papers that analyze gender bias of neural retrieval. These should probably be addressed. See Rekabasz and Schedl: Do Neural Ranking Models Intensify Gender Bias?

### Questions
Q1: After a quick search, it appears there are datasets specifically designed to measure gender bias for information retrieval. Did you consider using these datasets? How would they compare to your approach?

Q2: Is gender / topic bias only a concern for dense retrieval? What about sparse retrieval?

Q3: It does seem strange how Contriever seems to converge always to the same accuracy. Could this be due to some peculiar property of the Contriever training? Is it worth training not only on a different shuffle of the data, but perhaps removing some of the data too?

Q4: There should probably be additional clarification for "exceed the difference in per- formance from adding supervision (over unsupervised learning only)", since models evaluated on BEIR on never trained directly on BEIR. I assume the supervision is from some other retrieval data such as MSMarco.

Q5: Have you considered causes for variance in some of these datasets? For example, TREC COVID is very small (only 50 queries). HotpotQA is much larger but has one of the stranger evaluation protocols for BEIR, since the original HotpotQA relevance would typically require documents to be retrieved together and BEIR abandoned this.

Q6: Did you consider that data shuffling for Contriever training may play a bigger role than the MultiBERT seed?

Q7: "The corpus could have lower quality or less informative articles about female entities, queries about women could be structurally harder in some way." It could be helpful to clarify this with some examples.

Q8: Why did you choose contriever instead of modern alternatives? I realize that MultiBERTs allow for diversified checkpoints, but it may greatly limit our understanding when applied to retrieval. Are none of the modern retrievers compatible with BERT? Is there some option to provide multiple checkpoints for a modern retriever, perhaps through data shuffling or re-initializing some layers? Or perhaps a different retrieval approach focused on re-ranking the output of BM25 (this is only a rough idea, and I am not confident it is sufficient)?

Presentation Notes

* Figure 1 is hard to read. Perhaps remove background grid and make the reference line more prominent? Why are some plots missing the reference---should indicate if outlier is better or worse? Also the axis is so small... It could be better to include a subset here and put the rest in the appendix.

* typo: there is a large range of benchmark performance across seeds [with for] identical contrastive losses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper empirically explores what information is encoded by the embeddings of dense retrievers. It leverages probing techniques to measure the degree of information that is encoded by the embeddings. It assesses the correlation between extractability of information in these embeddings and performance across 14 retrieval datasets spanning various retrieval tasks.

### Strengths
The exploration of embeddings' underlying information is a commendable effort. The motivation of the research is acknowledged.

### Weaknesses
 - The encoded information of embeddings are influenced by many factors, e.g. the training data, the training algorithm. To understand the behavior of embeddings, it is necessary to take all these factors into account. Unfortunately, the paper fails to take into account any of these factors, which significantly diminishes the research significance of its conclusion. 

- The paper is not quite readable. The quality of presentation is far from that of a professional research paper.

### Questions
Please check the posted weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
