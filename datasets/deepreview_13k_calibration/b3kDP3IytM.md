# KITAB: Evaluating LLMs on Constraint Satisfaction for Information Retrieval

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
We study the ability of state-of-the art models to answer \emph{constraint satisfaction} queries for information retrieval (e.g., ``a list of \texttt{ice cream} shops in \texttt{San Diego}''). In the past, such queries were considered to be tasks that could only be solved via web-search or knowledge bases. More recently, large language models (LLMs) have demonstrated initial emergent abilities in this task. However, many current retrieval benchmarks are either saturated or do not measure constraint satisfaction. Motivated by rising concerns around factual incorrectness and hallucinations of LLMs, we present \dataset, a new dataset for measuring constraint satisfaction abilities of language models. \dataset\ consists of book-related data across more than 600 authors and 13,000 queries, and also offers an associated dynamic data collection and constraint verification approach for acquiring similar test data for other authors. Our extended experiments on GPT4 and GPT3.5 characterize and decouple common failure modes across dimensions such as \emph{information popularity}, \emph{constraint types}, and \emph{context availability}. Results show that in the absence of context, models exhibit severe limitations as measured by irrelevant information, factual errors, and incompleteness, many of which exacerbate as information popularity decreases. While context availability mitigates irrelevant information, it is not helpful for satisfying constraints, identifying fundamental barriers to constraint satisfaction. We open source our contributions to foster further research on improving constraint satisfaction abilities of future models.~\footnote{\url{https://huggingface.co/datasets/microsoft/kitab}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a dataset KITAB for testing on how LLMs can satisfy constraints in IR. A set of books are collected. Constraints can be set on authors, titles, dates, etc. and can be combined. The evaluation of the results by GPT-3.5 and GPT-4 are evaluated in terms of irrelevance, completeness, etc. Three test conditions are set using different prompts: no-context, self-context and context, providing (or not) the list of books written by an author.
The paper examines how GPT-3.5 and GPT-4 perform on different queries. A wide range of experimental results are reported.

### Strengths
The problem examined - constraint satisfaction - is not a widely studied problem. To some extent, this investigation extends the traditional IR to a special type of IR.
The data collection and experimental setting are well described.
The results may reveal that GPT models are not able to process this type of queries very well, and in particular, those with some constraints.
The authors will release the dataset.

### Weaknesses
The targeted problem is very special. The authors consider it as an IR problem. It resemble more database querying problem. Indeed, once the book references are transformed into structured database, the problem may be much simpler. Howere, as I understand, the intent of the author is not to examine how GPT models can handle such a search problem, but try to use this to test the ability of LLMs to handle queries containing constraints. While I appreciate this effort, I still question on the appropriateness of thFor e task. Instead of expression general constraints in a language, the constraints examined are very specific, and sometimes special. For example, constraints asking a title to end with a letter `v', or titles to be of 4 words, seem very particular. It is expected that a general LLM may not perform the task well because they have not been trained for the task. The main concern about the work is whether the types of constraints used can really test the ability of LLMs to satisfy constraints, or if the tests are on LLMs ability to understand the constraints and to execute filterings of books accordingly in this very special case. Even if LLMs are able to do the job well, would one be able to draw interesting conclusions? The experiments shown in the paper may not allow to draw general conclusions on LLM's ability to satisfy constraints.
Given the very special characteristics of the dataset, I question about the value of the KITAB dataset for the purpose of examining LLM's capability of constraint satisfaction in search.
While the ground truth is determined correctly, there may be some problem in the measure of irrelevance and completeness, as some fuzzy matches are allows. As the authors admit, there may be some overestimation of the performance. So the experimental results are only indicative, with some possible rate of errors.

### Questions
For the estimation of irrelevance or partial satisfaction, one case of match is when one is a string subset of another: For each ki, we check if there exists a book in the ground truth set of books by that author which is either a string subset match for ki (in both directions),... Do you also apply a threshold on the percentage of the substring, or a substring of any length is accepted?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes KITAB, a dataset for evaluating how large language models perform on information retrieval tasks with constraint satisfaction. The author(s) describe the dataset constructions and settings in detail. Evaluated on the proposed dataset, observations from different perspectives indicate that KITAB is still a challenging task for LLMs.

### Strengths
1. Timely study of LLMs on constraint satisfaction for information retrieval.
2. The overall paper is well-written and easy to follow.
3. Detailed descriptions of the data construction are provided.
4. The author(s) also promise to release the dataset, as well as code to the community.
5. The author(s) comprehensively analyzed the results to draw several interesting observations.

### Weaknesses
1. Concerns of the submission being out-of-scope. The paper undoubtedly stands out as a great resource that makes contributions through its new dataset and the accompanying empirical studies. It certainly serves as a valuable asset for the research community. However, I'm concerned about its suitability as a full paper for ICLR, given the conference's typical focus.

2. The author(s) have indeed conducted a thorough consideration of multiple facets in constructing the dataset, such as the number of constraints, the variety of constraints, and unsatisfiability. Nevertheless, the scope of the proposed dataset is fundamentally narrow, being confined to the domain of books. This domain-specific focus could limit its applicability to a broader range of IR research. It could be better if data from a variety of domains can be included.

3. The evaluations presented are primarily focused on the LLM services provided by OpenAI. While these are undoubtedly among the leading services in the field, the inclusion of open-source LLMs, such as LLaMA 2 chat, in the evaluation process could provide a more comprehensive view of the landscape.

### Questions
Please refer to "Weaknesses".

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new dataset, KITAB that evaluates how well LLMs  perform in answering constraint satisfaction queries for information retrieval.

### Strengths
Overall I think this new dataset is a well posed and timely work.

* The dataset seems well constructed and reasonable
* Incorporating constraint satisfaction for LLMs appears to be somewhat understudied, and this dataset will fit nicely into the existing LLM evaluation framework
* The choice of model evaluation on the data (ChatGPTs) is reasonable
* The differing frames for the data (with context, without, etc) makes sense
* The dataset construction is well documented, with design choices explicitly described
* The metrics and evaluations are well constructed

### Weaknesses
The dataset is somewhat limited, being about books, years and authors. I would prefer if the dataset included a wider portfolio of constraint tasks, perhaps around geography or movies.

It would also be nice if at least one opensource LLM was used in evaluation (i.e. LLAMA or LLAMA 2).

Some of the constraints seem a little artificial: authors born in a specific year. Some of the constraint questions are out of scope of the design of current LLM's tokenization, "Book title starts with the letter v". These constraints don't accurately reflect user interaction with a LLM, I feel.

### Questions
Can you enumerate all the constraints? It's not clear from the text what exactly the single and double constraints general architecture is.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops a dataset and associated dataset construction framework for the evaluation of LLMs on _constraint satisfaction information retrieval_ tasks (eg, "celebrities who died in 2022"). This problem is interesting because many it covers many important and useful factual query tasks, but LLMs have significant accuracy difficulties. The authors experiment against existing LLMs (GPT-3.5 and GPT-4) while varying key dimensions of the task, and conduct performance and error analyses on the results.

### Strengths
A crisp task definition and associated evaluation dataset can be a high-leverage research contribution that enables and accelerates other work, so this is a worthwhile goal. It's also quite promising that the task seems to be intuitively straightforward yet is still challenging for state-of-the-art proprietary models like GPT-4.

The citations and engagement with IR research going back to 1989, 1999, 2009, etc is good to see and contextualizes the work well. 

The exploration of problem setting parameters (task settings, author popularity, selectivity) is systematic and illuminating. The research questions are clearly defined and answered. The explanations of the dataset development and scoring are clear and thorough. The "extensible" nature of the methodology for dataset construction is useful to "future proof" the work.

Some of the detailed error analysis was intriguing and suggestive of mechanisms behind the failure modes which is very exciting for future work:
* ends-with vs starts-with constraints
* "sharp phase transition" for failure rate vs author popularity
* fabrication for "list all books by author"

### Weaknesses
For the open datasets (Open Library and WikiData), is there some precautions taken to "snapshot" these to a specific point in time for reproducibility purposes? Also, the procedures uses a few proprietary tools to develop the dataset: Azure Cognitive Services NER and Language API, Geonames in the dataset preparation. If the framework code release is open-sourced, future developers could substitute open or more reproducible components in these places, but this means that it would be difficult to create a new version of the dataset "out of the box". Likewise for GPT-3.5 and -4: are all the queries and responses captured somehow for reproducibility of the experiments and analysis? Some of these reproducibility concerns potentially undercut the usefulness and extensibility of the framework.

For controlled experimentation purposes it is useful to focus on a single domain such as book  authorship. However, it seems like there is some risk that the findings or behaviors may not transfer to other constrained IR tasks. How easy or difficult would it be to adapt the framework to generate similar dataset-task pairings in other domains as mentioned in the paper (movies, restaurants, etc)? 

Can fine-tuned LLMs do well on KITAB? The results and dataset would be more compelling with another FINE-TUNED setting, even if it had to be done with an OSS model.

### Questions
What does KITAB stand for? I couldn't find a definition. 

Table 3: why are some numbers red?

### Soundness
2 fair

### Presentation
3 good

### Contribution
4 excellent
