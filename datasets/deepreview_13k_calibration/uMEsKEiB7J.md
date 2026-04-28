# NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
The rapid advancement of Large Language Models (LLMs) has introduced a new frontier in natural language processing, particularly in understanding and processing long-context information. However, the evaluation of these models' long-context abilities remains a challenge due to the limitations of current benchmarks. To address this gap, we introduce NovelQA, a benchmark specifically designed to test the capabilities of LLMs with extended texts. Constructed from English novels, NovelQA offers a unique blend of complexity, length, and narrative coherence, making it an ideal tool for assessing deep textual understanding in LLMs. This paper presents the design and construction of NovelQA, highlighting its manual annotation, and diverse question types. Our evaluation of Long-context LLMs on NovelQA reveals significant insights into the models' performance, particularly emphasizing the challenges they face with multi-hop reasoning, detail-oriented questions, and extremely long input with an average length more than 200,000 tokens. The results underscore the necessity for further advancements in LLMs to improve their long-context comprehension and computational literary studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new benchmark called NovelQA, which is designed to evaluate the performance of LLMs on extremely long and complex texts. NovelQA uses English novels as contexts and annotates questions across three levels of complexity and seven aspects by literature experts. The proposed benchmark surpasses existing ones in length, includes evidence alongside questions, and emphasizes detailed comprehension. This paper also presents experimental results from a suite of LLMs on this benchmark and analyses their performance across different aspects.

### Strengths
1. The paper is generally well-written and clear.
2. The proposed NovelQA benchmark features the longest context to date
3. The experiments are generally well-designed

### Weaknesses
1. The benchmark only focuses on novels, which is somewhat limited. It is essential to include other forms of long-context in order to provide a more comprehensive evaluation of LLMs' long-context understanding capabilities.
2. The templates mainly focus on information extraction types of tasks. It would be beneficial to design more complex questions, e.g. ones 
that require reasoning

### Questions
1. How was the evidence annotated?
2. It was mentioned in the paper that LLMs "usually fail to tackle information spanning over multiple chapters." How does the proposed benchmark assess this aspect?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new dataset on long-context understanding. It uses novel as the long context and evaluate the model with questions from different complexity and aspect categories. Those questions and answers are annotated by human annotators, with a high inter-annotator agreement on answers. The answers are also with distractions for multi-choice setting generated from GPT-4. They evaluate open-source and commercial LLMs on the constructed dataset, revealing some findings such as performance degradation after 100K tokens, difficulty with questions on meaning, relation, span and times and low performance on evidences recall.

### Strengths
1. This paper presents a new dataset on long-context understanding. It has some unique features that are not covered by previous work, such as the long averaged context length, and human annotation efforts. It has the potential to be used in later work.

2. The benchmarking results include some interesting findings, such as performance degradation after 100K tokens and low performance on evidence recall. Those findings may enlighten future research in this area,

3. This paper is well-organized and easy to follow, with comprehensive appendix on the details of the data.

### Weaknesses
1. One major concern of this work is that this paper only focuses on using novels as the genre for long-context understanding. It would be better if the author could cover other long-context genres, such as other nonfiction books, to evaluate the long-context understanding comprehensively.

2. Another concern I have is about the analysis of the performance based on the position of corresponding evidence. Because the annotation on the annotation does not include whether the evidence is unique in the long context, there may be some cases where the annotated evidence can also be found in another snippet of the context. And it may ultimately impact the analysis or the conclusion of the analysis based on the evidence position.

3. As we can see in Table 1, most of the questions are either single-hop or details, which is generally based on a short text snippet of the long context. It would be also beneficial to include more discussion on the multi-hop questions, for example, the performance with regard to the relative distances of the pieces of evidence for a multi-hop question, as these questions are more difficult to be produced by LLMs.

### Questions
1. How are the question types and evidence annotated?

2. What does the distribution of the evidence positions look like?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
NovelQA is a new benchmark designed for evaluating large language models (LLMs) on complex, extended narratives with average context windows exceeding 200,000 tokens. This is relevant as the most advanced long-context LLMs can process over 250,000 tokens. NovelQA provides a combination of complexity, length, and narrative coherence, using a diverse selection of English novels from various eras, genres, and formats. Professional expert annotators carry out the annotation process, and all of them hold or are pursuing degrees in English Literature. The dataset includes multi-hop, single-hop, and detail questions, which assess the model's abilities to retrieve and integrate scattered information, summarize information, and accurately identify specific and subtle details. Both closed APIs and open models have been evaluated using this benchmark, and a comprehensive analysis is proposed based on the results.

### Strengths
— Annotators performed a huge amount of work. The questions, golden answers, and evidence of NovelQA are crafted through the efforts of experts. The context is extensive, making it challenging to create such a set.

— An informative, descriptive Appendix with details, annotation agreements, and error analysis.

— The contribution is clear and high

### Weaknesses
— No ethical consideration and Limitations sections. The Limitation section is highly recommended, as mentioning the restrictions is important.

— There are efficiency problems with the benchmark running for the long-context models. 

— To add in the limitations: data leakage. `To prevent against data leakage, we will not release golden answers for the test set, minimizing the risk of overfitting.`
The novels are not created from scratch. Many of them, particularly public domain works, are already included in the training datasets of models like GPT-4. This represents an indirect issue of data leakage. It is also crucial to discuss the problems related to data contamination and leakage.

— The biases of the annotators also need to be mentioned in the Limitation section.

— Truncation is also a limitation as nobody checked whether the truncated part influences the result.

— The creation of templates based on the most difficult cases for GPT-4 and Claude2.1 is understandable but may cause biases.

— Syntactic choices for the multiple choices:
`We use GPT-4 to generate three distracting options for each question and its golden answer and randomly permute the four answers`
Authors further evaluate API models on the same sets: it will be with a high probability of a strong bias for GPT4 to answer the questions.
Thus, the authors can not claim that the GPT performs better than others.

### Questions
— Somehow the Table 7 and Figure 5 are above the Appendix section, and needs to be formatted.

— No Table number in Line 1120

— Consider using VLLM models to reduce running costs and time.

— Better to write `multichoice` or `multi-choice` consistently during the paper

— Add Human Baseline in Table 2

— Write in bold the best scores in Tables, better readability

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new benchmark to assess LLMs on reading and understanding very long inputs (200k in average). Concretely, the task is Question Answering (QA) in two forms, multiple-choice and generative, over novels. The dataset is constructed based on public and copyrighted novels from the Project Gutenberg (purchasing ones when necessary) and manually crafted questions, gold answers (distractors generated automatically but manually inspected), and evidence. Human annotators are Language and Literature students. The benchmark contains questions of different complexity (multi-hop, single-hop, and details) and about different aspects (e.g., relationships or narrative settings -- 8 categories in total). Five large-context LLMs are evaluated on the benchmark (3 commercial and 2 open source). Results reveal that LLMs struggle to read, find and process the content in the long context necessary to formulate the answer; this happens even with commercial LLMs (GPT-4) with open-source LLMs exhibiting worse performance. 

The paper is easy to follow and with illustrative examples. It includes performance analysis per question type and by content position.

### Strengths
The proposed benchmark is a valuable resource for the evaluation of LLMs performance on reading and reasoning to answer questions over long texts.

### Weaknesses
While the evaluation of LLMs shows that these struggle to understand, attend, and recall all the content from the long context necessary to answer questions (main focus of the paper), I wonder whether an initial extractive step would be a strong baseline in this setup. For instance, a common practice in summarisation of long inputs, is an initial extractive step (e.g., by tf-idf) that is applied before carrying out the actual task with the selected text. Maybe adding such a baseline would contribute to highlight the robustness of the proposed QA benchmark (i.e., how difficult is it to solve the task in this way). Also, some of the questions (e.g., counting) could be a LLM reasoning weakness rather than a long context processing issue.

### Questions
The authors could incorporate experiments with the new Llama 3.1 family.

### Soundness
3

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
4

### Summary
This paper introduces NovelQA, a benchmark designed to evaluate LLMs on long-context question-answering tasks. NovelQA addresses limitations in existing benchmarks by focusing on texts exceeding 200,000 tokens, derived from a diverse selection of English novels. NovelQA incorporates human-annotated questions that require detailed comprehension of lengthy narratives. The dataset evaluates multiple aspects of comprehension, including multi-hop reasoning, detail retrieval, and narrative coherence, revealing significant gaps in LLMs' ability to manage large, complex contexts.

### Strengths
NovelQA benchmark addresses an important challenge in long-context LLMs by introducing a dataset that emphasises extended context comprehension within complex narratives, representing a significant advancement over standard benchmarks. The dataset is carefully constructed with expert annotations, which are detailed in the paper, ensuring that question complexity aligns appropriately with model capabilities. The paper provides comprehensive documentation on question types and evaluation metrics, establishing a strong foundation for interpretability and contributing to a reliable benchmark. Last but not least, NovelQA evaluates narrative comprehension, multi-step reasoning, and retrieval-based tasks in LLMs, marking a substantial contribution to long-context evaluation.

### Weaknesses
Though the transparency of the annotation process is addressed, it could be strengthened. Although the authors state that questions are created by expert annotators with backgrounds in English Literature, the paper lacks clarity regarding annotator instructions, experience levels, and quality control measures above basic inter-annotator agreement scores — this could be demonstrated more clearly. Secondly, evaluation methods are insufficiently justified and may introduce bias due to the use of automated scoring. For instance, gpt-4 is used as an evaluator, with limited details on its evaluation process, which is particularly concerning given that the benchmark aims to capture complex reasoning across extended narratives.  eg. gpt-4 as an evaluator may score higher for gpt-4's answer. This could lead to bias in the results. While two human evaluators are mentioned, the paper does not provide information on their backgrounds or expertise. Other than these issues, the paper is well-written!

### Questions
1. I’m curious about the performance of other open-source models, such as mistral, llama, and so on, or perhaps smaller closed-source models like GPT-4o-mini. Could you provide additional insights into how these models perform compared to the primary models evaluated in the paper?

2. Regarding the use of gpt-4 as an evaluator, as noted above, this may introduce potential bias. Could you clarify how gpt-4 , or an alternative model, acted as an evaluator in the paper?

3. Are the questions and sample sentences in the dataset accessible online for user verification in the future, or are they restricted and not publicly available for sourcing and comparison?

### Soundness
4

### Presentation
3

### Contribution
3
