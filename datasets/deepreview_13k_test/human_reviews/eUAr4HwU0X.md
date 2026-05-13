# L-Eval: Instituting Standardized Evaluation for Long Context Language Models

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Recently, there has been growing interest in extending the context length of large language models (LLMs), aiming to effectively process long inputs of one turn or conversations with more extensive histories. While proprietary models such as GPT-4 and Claude can largely preserve the reasoning ability in an extended context, open-source models are still progressing through the early stages of development. 
To bridge this gap, we propose L-Eval to institute a more standardized evaluation for long context language models (LCLMs) addressing two key aspects: dataset construction and evaluation metrics. On the one hand, we build a new evaluation suite containing 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs encompassing diverse question styles, domains, and input length (3k$\sim$200k tokens). On the other hand, we investigate the effectiveness in evalution metrics for LCLMs. Results show that popular n-gram matching metrics generally can not correlate well with human judgment, and thus we strongly advocate for length-instruction-enhanced (LIE) evaluation and employing LLM judges.  We conducted a comprehensive study of 4 popular commercial LLMs and 12 open-source counterparts using the L-Eval benchmark. Our empirical findings offer useful insights into the study of LCLMs and lay the groundwork for the development of more principled evaluation of these models

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is focusing on the evaluation of long-context language models and proposes a new evaluation benchmark for the evaluation of long text generation that consists of 20 closed (reasoning and understanding) and open-ended (summarization) sub-tasks, 508 documents, 2000 human annotations for query-response pairs. The authors investigate the performance of existing evaluation metrics on this benchmark and find that n-gram matching metrics present poor correlation with human judgements, leading them to recommend the use of LLM-based evaluation metrics.

### Strengths
The paper is making an important contribution to the community which is in need of benchmarks for evaluating long-term text generation models. The authors present comprehensive statistics about the benchmark which includes both new and existing datasets. For the existing datasets, the authors put effort into cleaning and correcting misleading previous annotations. On the proposed benchmark, the authors evaluate the performance of existing reference-based evaluation metrics on both open-ended and close-ended tasks.

### Weaknesses
Abstract: “GPT-4 and Claude can largely preserve the reasoning ability in an extended context” - this statement is misleading, there is a significant body of work showing how the reasoning abilities of these models is limited particularly for long contexts / multi-hop reasoning tasks.

The paper  does not provide a clear and convincing argumentation on why the specific datasets they select are included in this benchmark. To what extent this was an informed decision made by the authors is unclear. In addition, there is no clear highlight of differences between the currently proposed benchmark and existing long sequence benchmarks in the literature (which the authors describe in Section 2.2). Why is L-eval superior to existing benchmarks is not clarified in this paper. As this paper has the potential to impact the research community, it should be motivated why researchers would use this benchmark instead of other existing long-context benchmarks. 

It would be good to include length statistics for both inputs and references across the tasks in the benchmark, and maybe correlate this with the difficulty of solving a particular task. The paper only limits to briefly mentioning “The length of reference in L-Eval also varies significantly across tasks.” 

The authors conduct evaluation of reference-based metrics on their proposed benchmark, and conclude that n-gram based metrics are inferior to LLM-based metrics for long-text generation. Furthermore, the main takeaway from the evaluation analysis is that authors recommend the use LLM-based metrics, however these come with problems that are not discussed in this paper. The blunt recommendation of LLM-based metrics without a thorough discussion of their biases and failure cases is a strong limitation of this paper. 

“LLM evaluators have been reported to favor more detailed and lengthy answers”  - the authors do not discuss how the length statistics across the tasks in this benchmark have an impact on these evaluation biases. For the length-instruction based evaluation, accounting for the length of the reference answer may introduce additional biases: “We need a 50-word summary, where 50 is the number of words in the reference answer”.

Moreover, they claim that “Human evaluation This is the most accurate evaluation for open-ended tasks.” - While I agree with this statement, human evaluation is not flawless either. This paper does not present details of how the manual annotation was conducted, which does have an impact on the results reported and the conclusions of this paper.

### Questions
Contradictory information: In Introduction you mention “L-Eval has 20 sub-tasks, 4 sub-tasks are annotated from scratch (§3.1), 4 sub-tasks are re-annotated from the public datasets (§3.2), and the remaining 12 sub-tasks are manually cleaned from previous long sequence datasets.”, while in Section 3.2 you claim “We re-annotate 5 publicly available datasets in L-Eval.” How many publicly available datasets are you annotating?

Section 3.1. - Data Annotation from Scratch: for the 4 datasets presented, are these manually or automatically annotated? There is no information provided in this section. 

“The average input length in L-Eval ranges from 4k to 60k”. Do you measure the length in tokens? If yes, this should be specified.

How is your benchmark different from from existing long sequences benchmarks?

Have you considered the behaviour of referenceless metrics on your benchmark?

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
This paper proposes L-Eval, a new benchmark for evaluating long context language models (LCLMs). 

The authors start by arguing that existing benchmarks have limitations in dataset construction and evaluation metrics for properly assessing LCLMs' capabilities. To address this, the authors construct L-Eval, which contains 20 diverse sub-tasks with over 500 long documents and 2000 human-labeled question-answer pairs. The tasks cover various domains, question styles, and input lengths up to 200k tokens and, importantly, contains both *closed-ended* (with exact evaluation) and *open-ended* tasks . To construct the benchmark, the authors annotate 4 datatsets from scratch, re-annotate 5 others, and aggregate other 12 datasets/tasks from previous literature, resulting in a total of 21 tasks.

The paper also studies limitations of traditional n-gram matching metrics for open-ended generation tasks. Experiments show these metrics often fail to correlate with human judgments, particularly when models’ outputs different significantly in length from the reference answer. The authors propose techniques like length-instruction (asking for answer of similar lenght to the reference) and using LLM-based evaluation to improve correlation.

Comprehensive experiments are conducted on L-Eval with 16 closed-access and open-source LLMs, and include a human-evaluation for the open-ended tasks. 

Key findings include:

- Significant gaps remain between commercial and open-source LCLMs.
- While open-source LMs finetuned for long-context improve on closed-ended tasks, they struggle on open-ended tasks as input length increases, even compared to the non-long-context-finetuned counterparts.
- Scaled positional embeddings enhance retrieval but can hurt reasoning over long contexts.

### Strengths
- The problem tackled is very relevant: modelling long context is one of the most important open-problems in LM research, and one of the main difficulties has been lack of proper evaluation.
- The proposed benchmark is quite diverse, being composed of many domains and both closed-form and open-ended NLP tasks. It also seemed to have required a consirable amount of work given the amount of human-annotations involved.
- Very throughout analysis of the limitations of automatic metrics for open-ended tasks, including a potential easy fix (length instruction enhanced evaluation) to make them more reliable evaluators (albeit clearly human/model based eval still seems to be better).
- Throughout evaluation of current SotA models, both open-source and closed-access.

### Weaknesses
- My main criticism of the paper is due importance/relevance given to GPT-based evaluation. While I believe that this is probably better than lexical metrics, its unclear if it will lead to biased evaluations, particularly when evaluating GPT-based genarators. In my opinion, table 5 (human eval) is more important to include in the paper than Table 4, and should include results for human-eval of the GPT-4 model (so as to compare with the GPT-4 based eval).
- The paper has multiple typos and gramar errors. E.g.
    - “We inject come new”
    - “NTK-ware”
    - “directly exposure to LCLMs”
    - …
  I suggest the authors run the text by simple automatic grammar correction since I’m pretty sure it would catch most of these

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents L-Eval, a dataset for evaluating long context language models (LCLMs). The authors constructed an evaluation suite featuring 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs showcasing varied question styles and domains. Apart from this, the paper raises concern over the efficacy of prevalent ngram matching metrics as they often fail to sync with human judgment. Therefore, it favors employing length-instruction-enhanced (LIE) evaluation and using large language model (LLM) judges. A study of 4 widely-used commercial LLMs and 12 open-source models, evaluated with the introduced L-Eval benchmark, provides findings for future development of LCLMs evaluation methodologies.

### Strengths
1. The author clearly articulates the intended content, including methods and procedures for dataset construction, statistical features of the dataset, evaluation methods, and so on. 
2. The problem, namely the "Evaluation for Long Context Language Models" is important. The proposed dataset and conclusions regarding existing evaluation methods contribute to the advancement of long context LLMs.
3. A comprehensive evaluation has been carried out by the author on current commercial and open-source LLMs.

### Weaknesses
1. The key contribution of this paper is the dataset it provided, but the authors do not offer sufficient analysis on the data collection and construction methods. For instance, in section 3.1 detailing the construction of the Coursera dataset, the authors mention, "In order to increase the task's difficulty, we have set multiple correct options. To the best of our knowledge, this is the first multi-choice dataset with multiple correct answers, and it is more challenging than single-option questions." Could it be because without this increased difficulty, there wouldn't be any differentiation among various models?
2. The findings of the paper are rather intuitive and not enough insightful. For example, the authors mention in the penultimate paragraph of the Introduction, "There is still a significant gap between open-source LCLMs and commercial models, for both closed-ended tasks (Table 3) and open-ended tasks evaluated by LLMs and humans (Table 4, 5). However, this gap is not accurately reflected by n-gram metrics."

### Questions
1. Could you elaborate more precisely on the motivations and insights regarding the dataset construction methods, such as Coursera, CodeU, and LongFQA?
2. Could the authors provide further insights into the shortcomings of current open-sourced long-context models, and how the dataset provided in this paper could facilitate enhancements in these problems?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a carefully curated long context evaluation benchmark with both open and closed tasks. They also propose an LLM-judge evaluation method that correlates better with human judgment than traditional N-gram metrics that other benchmarks still use. Their analysis provides insights into the types of prompt settings, tasks, and evaluations that work well for this problem.

### Strengths
* Carefully curated and manually chosen questions that are unintuitive to models that do not read and understand the context (e.g. scifi that contradicts real world physics)
* Targets domains that are understudied, e.g. long context finance questions
* LIE shows interesting analysis → what details matter for prompting and evaluating long contexts like this.
* Continued finetuning analysis between open and closed tasks are insightful
* The effects of NTK positional embeddings on retrieval vs reasoning (their negative correlation) is very interesting

### Weaknesses
* Uses Claude-100k as the data filter. This detects unanswerable questions, but careful human review would be better, rather than steering scores towards closed LLMs.
* Length Instruction Enhanced (LIE) is arguably not a new or significant contribution, so the authors should be careful not to frame it as such. The analysis of it is what is interesting.

### Questions
* Did you test performance of models with the question but without the context? I.e. you make the argument that the questions are designed not to be easy just from using parametric knowledge – can we validate this?
* Confused about the 96 subset. Are there many evaluation questions in your benchmark ignored / not used?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
