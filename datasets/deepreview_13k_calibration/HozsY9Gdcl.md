# Leveraging Set Assumption for Membership Inference in Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Membership Inference (MI) refers to the task of determining whether or not a document is included in the training data of a given model. MI provides an effective post-training alternative for analyzing training datasets when the access to them is restricted, including studying the impact of data choices on downstream performance, detecting copyrighted content in the training sets, and checking for evaluation set contamination. However, black-boxed Language Models (LMs) only providing the loss for the document may not provide a reliable signal for determining memberships. In this work, we leverage the insight that documents sharing certain attributes (e.g., time of creation) are all expected to be in a training set or none of them is, and develop methods that aggregate membership predictions over these documents. We apply our set assumption on five different domains (e.g., Wikipedia, Arxiv), and find that our method enhances prior MI methods by 0.14 in AUROC on average. We further analyze the impact of different language model sizes, training data deduplication, and methods of aggregating membership predictions over sets and find that our method is more effective on undeduplicated and larger models with more documents available in each set and longer sequence sampled for each document, and show our method’s robustness against noises in the set assumption under practical settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to leverage set assumption for solving the Membership Inference (MI) problem.  That is, considering the whole set is included in the model training to determine whether or not a document is included in the training data of a given language model.  This could be useful for analyzing training datasets when the access to them is restricted, including studying the impact of data choices on downstream performance, detecting copyrighted content in the training sets, and checking for evaluation set contamination. The work relies on the insight that documents sharing certain attributes (e.g., time of creation) are all expected to be in a training set or none of them is and develop methods that aggregate membership predictions over these documents. They apply this set assumption on five different domains (e.g., Wikipedia, arXiv), and find that the method enhances prior MI methods by 0.14 in AUROC on average. It also shows that the method is robust against noises in the set assumption under practical settings.

### Strengths
1.	Overall, the paper is relatively clearly written.  

2.	The paper relies on one major assumption, set assumption; and also assumes that such metadata related to this assumption are also available; and based on this assumption, experiments were conducted with some good results.

3.	Two relatively sizeable data sets, Wikipedia and arXiv, are used in the experiments

### Weaknesses
1.	The insight of using set assumption, that is, the insight that documents sharing certain attributes (e.g., time of creation) are all expected to be in a training set, or none of them is.  However, this assumption needs to be discussed.  This is because even the training set includes the whole set, the preprocessing of training data could remove some documents due to its content largely duplicates or overlaps with that of some other documents (by deduplication), credibility assessment (by removing noisy or low credibility documents), etc.  It is hard to assume that the whole set or none in the set will be included in the training data.  Also, even when the sets as a whole are included in the training, the contents of some documents in different sets could overlap substantially with some other documents in some existing sets (e.g., evolving news).  I feel the membership identity relying on such an assumption could still be questionable in practice.

2.	The datasets used in experiments are pretty small, except two datasets, and such datasets Wikipedia and arXiv, are relatively clean and non-redundant datasets, which may contain less redundant and noise documents.  However, they may not be the typical cases in the real large datasets, which may need lots of data cleaning, deduplication and preprocessing before feeding into LLM training in the real case.

3.	At the end of the paper, the author mentions that “Our work makes an assumption that the metadata about the dataset of interest (D) is available, enabling the identification of sets that satisfy the set assumption. We highlight that this may not always be the case in practical MI scenarios, and leave relaxing this assumption for future work.”   Actually, this could be the real case where the testing of the datasets satisfying such an assumption a difficulty tasks for real life applications.

### Questions
The points outlined in the “weakness” are the major questions that the reviewer would like to raise and be clarified in the rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the Membership Inference (MI) task, which detect whether a document is included in training data. The author proposes a new method called SET-MI that leverage the set assumption: either all documents in the set are present in the training dataset or none of them are.  To evaluate this new method thoroughly, the author constructs five benchmarks covering a variety of domains. Results show that Set-MI significantly enhances four Individual-MI methods with an improvement of 0.14 in AUROC. Further experiments demonstrate the robustness of this method against noise.

### Strengths
- The idea is novel, simple and effective.
- This new method is orthogonal to previous MI methods and obtain a performance enhancement on almost all benchmark settings.
- Further analytical experiments show the robustness of SET-MI to some extent.

### Weaknesses
 - The author constructs five benchmarks and uses the corresponding set assumption to obtain the main result. However, in the practical scenario, one cannot know in advance which set assumption to use.
- In the practical scenario, different set assumptions may result in a completely different score for the same document. It's difficult to judge which one is correct. This situation does not appear in the baseline methods.
- The author uses five self-constructed benchmarks. However, there exist some benchmarks to evaluate membership inference attack (MIA) methods, such as WIKIMIA [1]. The experiments could be more solid if the evaluation on WIKIMIA is included.

### Questions
- Is it possible to conduct a small experiment on documents with multiple critiera? For example, for documents with meta data that across different date, language and license, use different set assumptions and observe the performance enhancement of SET-MI.
- If using different set assumptions and obtain a completely different score, how to determine which result is correct?
- There exist benchmarks for membership inference, such as WIKIMIA. Why do you not use the WIKIMIA benchmark as your part of the experiment?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new method for membership inference (MI), Set-MI, to determine if specific documents were part of a language model's training data. Building on traditional MI techniques, Set-MI leverages the set assumption that certain groups of documents, which share the same attributes such as creation date or license type, tend to either all be included or all excluded from training datasets. By aggregating membership scores across these document sets, Set-MI provides a stronger and more reliable signal than analyzing documents individually, particularly in black-box settings where only limited information, like loss scores, is available. This method can improve traditional individual MI performance.

To evaluate Set-MI, the paper constructs five diverse benchmarks across different domains, including Wikipedia, Arxiv, languages, licensing, and instruction-based datasets. These benchmarks assess the method’s effectiveness in practical scenarios where the set assumption holds, such as documents grouped by creation date or license type. Results demonstrate that Set-MI consistently outperforms traditional MI techniques and performs especially well with larger models, duplicated datasets, and longer document sequences. Additionally, they empirically confirm Set-MI’s robustness even in noisy settings where some sets may partially violate the set assumption.

### Strengths
1. This paper introduces Set-MI, a new approach to membership inference (MI) that leverages set assumptions and aggregates membership scores across document groups, enhancing the effectiveness of individual MI. This method is particularly valuable in black-box settings where only limited information is available.

2. This paper conducts extensive experiments to validate Set-MI, testing it across five diverse benchmarks—covering domains such as Wikipedia, Arxiv, languages, licensing, and instruction-based datasets. These experiments demonstrate Set-MI’s consistent performance improvements over individual MI methods, particularly in larger models, duplicated datasets, and with longer document sequences. The paper also evaluates Set-MI’s robustness in noisy settings, showing its potential practicality in real-world scenarios.

3. This paper is well-structured and some key concepts, such as the set assumption, are effectively clarified through examples.

4. Set-MI improves membership inference, especially for black-box models, which could be useful for downstream tasks like privacy auditing.

### Weaknesses
1. I appreciate the authors' efforts in their experiments. However, the novelty of the method appears limited, as Set-MI seems to simply adjust traditional membership inference by aggregating and averaging individual membership scores across document groups, which is more like an incremental improvement.

2. This method heavily relies on a strong set assumption—that data sharing a specific attribute are either entirely present or entirely absent in the training dataset. This assumption, grounded mainly in practical experience, limits the method's theoretical foundation. Additionally, selecting an appropriate attribute for set division requires prior knowledge, which can be challenging and subjective. That means in practical applications, set divisions will likely contain considerable noise, and the authors’ experiments indicate that Set-MI’s performance declines significantly in noisy settings. This suggests substantial limitations in the method’s effectiveness and generalizability in real-world scenarios its generalizability.

3. The experiment details are not clearly written. For example, It is not clear to me how authors utilize the membership scores to identify whether data is in the training data. The specific decision criteria or thresholds for interpreting these scores are not clearly explained, which could limit the method's reproducibility.

### Questions
1. It seems that the membership score is based on the model's output for each data point. However, I question the assumption that high output scores reliably indicate that the data is part of the training set. Couldn’t models also produce high scores for data that closely resembles the training distribution, even if that data was not seen during training? For example, if a test point shares common patterns or phrases frequently encountered in training, the model might still assign it a high score, despite it being new data. Is there any evidence to support this assumption?

2. Although the authors explored the effect of segment length for membership inference, I am curious about the ratio of selected tokens to the total tokens in each original document. Selecting a larger or smaller proportion of tokens may capture different levels of unique document features, potentially impacting inference performance. Examining whether this ratio affects membership inference accuracy could provide further insights for optimizing the approach.

2. More details of experiment settings would improve the clarity of this paper.

### Soundness
3

### Presentation
3

### Contribution
2
