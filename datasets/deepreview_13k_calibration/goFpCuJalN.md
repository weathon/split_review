# ClimaQA: An Automated Evaluation Framework for Climate Foundation Models

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6

## Abstract
\begin{enumerate}
The use of foundation models in climate science has recently gained significant attention. However, a critical issue remains: the lack of a comprehensive evaluation framework capable of assessing the quality and scientific validity of model outputs. To address this issue, we develop \textit{ClimaGen} (Climate QA Generator), an automated algorithmic framework that generates question-answer pairs from graduate textbooks with climate scientists in the loop. As a result, we present \textit{ClimaQA-Gold}, an expert-annotated benchmark dataset alongside \textit{ClimaQA-Silver}, a large-scale, comprehensive synthetic QA dataset for climate science. Finally, we develop evaluation strategies and compare different Large Language Models (LLMs) on our benchmarks. Our results offer novel insights into various approaches used to enhance climate foundation models.

\end{enumerate}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce ClimaQA, a question-answering benchmark designed to evaluate climate foundation models in handling scientific inquiries. This paper develops ClimaGen, a framework for generating question-answer pairs with climate experts in the loop, resulting in two datasets: ClimaQA-Gold (expert-validated) and ClimaQA-Silver (synthetic). The benchmark assesses models across multiple task forms (MCQ, freeform, and cloze) to gauge factual accuracy and scientific reasoning. The paper presents an analysis of several LLMs on ClimaQA.

### Strengths
· Originality: ClimaQA stands out as a pioneering benchmark specifically tailored for climate science. The framework’s approach of combining domain expertise with synthetic QA generation represents an innovative solution to the lack of reliable climate QA datasets.

· Quality: The benchmark’s rigorous development process, including the expert validation of ClimaQA-Gold and systematic generation of ClimaQA-Silver, ensures high-quality question-answer pairs that reflect real-world scientific standards. The choice of using diverse question formats (MCQ, freeform, cloze) is well-aligned with testing scientific reasoning skills.

· Clarity: The paper is organized and highly readable, with clear descriptions of each dataset and evaluation metric. The figures illustrate the QA generation and annotation processes well, making the methodology transparent.

### Weaknesses
· Complexity of Generated Questions: While the QA generation pipeline is well-designed, some questions in ClimaQA-Silver may lack the complexity required to thoroughly test advanced climate models. Specifically, many of the synthetic questions appear to focus on single-hop reasoning and simple fact retrieval, rather than requiring multi-hop inference or the synthesis of information from multiple sources. Supplementing the dataset with more nuanced, multi-layered questions that necessitate complex reasoning and integration of diverse climate data could improve its utility.

· Dependence on Manual Annotation for ClimaQA-Gold: Although ClimaQA-Gold is an expertly annotated dataset, its reliance on manual validation limits scalability. The current approach, while ensuring high quality, is resource-intensive and may introduce inconsistencies due to subjective human judgment. Developing a semi-automated validation process that incorporates techniques like inter-annotator agreement metrics or implementing a peer review system with multiple experts could reduce bias and improve reproducibility, while also making the validation process more efficient.

### Questions
1. What is the potential for scaling the ClimaQA benchmark to other scientific domains? Could ClimaGen be adapted for other domains like environmental science or epidemiology, and what would be the main challenges?

2. Have you considered additional metrics for freeform QA evaluation? While factual accuracy is addressed, additional metrics like coherence and logical flow might further enhance the assessment of model responses on freeform tasks.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present ClimaQA, a benchmark for language models, assessing skills in the area of climate science. The research introduces an automated pipeline (ClimaGen) to generate question-answer pairs from graduate textbooks, resulting in two datasets: ClimaQA-Gold (expert-validated) and ClimaQA-Silver (synthetic). The article presents three types of tasks: multiple-choice, freeform, and cloze with varying levels of complexity to challenge models on factual recall, scientific reasoning, and scenario application. For evaluation, the research develops dedicated metrics for freeform and cloze tasks and employs a fine-tuned LLM for the synthetic annotation process using expert-annotated data. The study evaluates several state-of-the-art large language models on the created benchmark under different settings, such as default configurations, few-shot prompting, and retrieval-augmented generation.

### Strengths
- The research addresses a lack of expert-annotated benchmarks in climate science and proposes a novel algorithmic framework to accelerate scientific benchmark creation through synthetic generation and expert validation.
- The synthetic scaling approach enables continuous updates to the benchmark, accommodating new findings in climate science research.
- The benchmark's incorporation of three distinct tasks (multiple-choice questions, freeform, and cloze) reduces potential biases arising from models' familiarity with specific question formats, unlike benchmarks limited to a single task type.
- The implementation of three well-defined complexity levels enables a comprehensive assessment of models’ knowledge and application capabilities, allowing precise identification of areas for improvement and a better understanding of current model performance.

### Weaknesses
 - Exclusive use of proprietary models (GPT3.5 for question generation and GPT4o-mini for freeform judgment) introduces potential bias favoring models from the same provider or those trained/fine-tuned on similar model outputs.
- The proposed metrics demonstrate an inconsistent correlation with expected language model performance. For instance, GPT3.5 exhibits superior or comparable performance against newer models, including those from the same family (GPT4o), on BLEU and BERTScore metrics as shown in Figure 5, highlighting potential metric reliability concerns in model evaluation.
- The research reports an 85% validity rate for generated multiple-choice questions in ClimaQA-Silver (Section 4.4), which may compromise the effectiveness of the evaluation. As several models on ClimaQA-Gold reach or exceed this performance level, the synthetic dataset may not provide reliable performance metrics. A comparative analysis similar to Table 3 for the synthetic dataset could illustrate this limitation.
- The study lacks quantitative comparisons with existing climate benchmarks, such as Climate Crisis or SciQAG-24D.
- The benchmark's reliance on textbook knowledge may introduce distribution bias in the evaluation process.
- The research provides a limited analysis of the expert validation process and common question generation errors, which could offer valuable insights into potential biases in the synthetic benchmark version.

### Questions
- Could you provide a quantitative comparison with established climate benchmarks, specifically Climate Crisis and SciQAG-24D?
- Would it be possible to present a comparative performance analysis, similar to Table 3, for the ClimaQA-Silver dataset to better understand potential quality differences between gold and silver datasets?
- Has the research considered implementing a mixture-of-experts approach for the freeform evaluation process instead of relying solely on GPT4o-mini?
- What were the selection criteria for the 18 textbooks, and how were they assessed for their relevance to recent advances in climate science?
- What methodology was used to ensure that the set of 5 textbooks provided a balanced coverage of climate science topics?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a benchmark that they have developed for evaluating LLMs on question-answer tasks specialized for the domain of climate science. They developed two datasets: ClimaQA-Gold containing 502 questions that have been annotated by climate science experts, and ClimaQA-Silver containing 3000 questions generated by their framework for LLM-powered generation of question-answered pairs based on a corpus of graduate-level textbooks. Their benchmark contains three types of questions: "free form" which expects the answers to be free-form text, "multiple choice" where the answer is given as an indicator to one of the proposed answer choices, and "cloze" which contains certain parts of text marked as "blank" and the task is to find the correct words to fill in the blanks. Questions come in three levels of difficulty: "base" which focuses on simple information retrieval, "reasoning" which requires the connection of multiple facts to form a conclusion, and "hypothetical scenario" which requires the application of knowledge to novel contexts. They conduct an empirical evaluation of several popular LLMs (including extensions such as RAG). The scores that the models achieve form a wide range which demonstrates the utility of the benchmark for evaluating LLMs on QA tasks for the specific domain of choice.

### Strengths
**(S1)** The proposed benchmark represents a significant step in creating a rigorous evaluation for QA models on climate-specific knowledge and reasoning tasks.

**(S2)** The authors provide both a human-curated corpus for final evaluation and an automatically augmented corpus for fine-tuning.

**(S3)** The fact that the benchmark is able to stratify models based on their performance on this task demonstrates that it is challenging, which will help it become a reference point for future models that are built specifically for the climate science domain.

### Weaknesses
 **(W1)** The domain that the authors focus on can be deemed as a very niche one. The authors could have tried to do a better job at providing concrete arguments in the introduction that underline the significance of this domain. Specifically, it would be good to explain why we need LLMs to be good at this specific domain. If they become better at this domain, which applications would this unlock?

**(W2)** There are certain small issues with the presentation: (1) the authors use the term "foundation models" but probably just want to say either "large language models" or "question-answering models". Foundation models are pre-trained on large corpora and used mainly for transfer learning across different tasks, but many of them are not LLMs. It would help to use a more specific term. (2) Formulas presented in section 3 use some symbols that were not explicitly defined (e.g. $p_s$, $p_r$). (3) The numbers in Figure 4 seem to keep going up (albeit at a reducing pace), and yet the authors conclude that a "context window of size 4 most effectively differentiates between correct and incorrect answers". From the figure, it is unclear to me why this context window is optimal.

**(W3)** This is a minor weakness, but the provided corpus is relatively modest, compared to other ones. I don't think this is too much of an issue given that it is probably large enough to sufficiently evaluate a QA model, and a small size makes it more manageable. That said, it would be good to provide some sense of how well the provided corpus covers the actual domain (e.g. by giving the readers a sense of the subdomains and the number of questions from each subdomain).

### Questions
**(Q1)** In section 5.2 you mention that there are 5 books used to derive the corpus of questions, and an additional 13 books that are used for the RAG model as a retrieval corpus. Do we know if all relevant information between these two sets of books overlaps? In other words, do we know if the information in the 13 books is sufficient to support all the questions that were produced by using the 5 books?

**(Q2)** In the introduction you mention "Creation of publicly releasable datasets". Could you please clarify what you mean by a "releasable" dataset?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a framework that significantly enhances the reliability and scientific rigor of AI models in climate science by generating domain-specific QA benchmarks. With ClimaQA-Gold, an expert-validated dataset, and ClimaQA-Silver, a large-scale synthetic set, the framework tests foundation models across different complexity levels, addressing factual accuracy, scientific reasoning, and hypothetical scenarios. By leveraging retrieval-augmented generation (RAG) and innovative metrics like Factual Accuracy and Phrase Similarity, ClimaGen facilitates more accurate model evaluation and fine-tuning. While advanced models like GPT-4 show promising results, they still face challenges in complex scientific questions, highlighting ClimaGen's role in driving further advancements in specialized climate AI. An expanded corpus and annotated dataset could enhance its robustness and adaptability to broader applications in scientific inquiry.

### Strengths
- The ClimaGen framework is tailored to climate science, which enhances the reliability of AI applications in this field by addressing unique requirements for factual rigor, domain-specific knowledge, and scientific reasoning.
- Combining an expert-validated gold-standard dataset with a large-scale synthetic dataset provides comprehensive resources for training and evaluating foundation models, supporting both high-quality benchmarking and scalability.
- The benchmark evaluates models across three question complexity levels (factual recall, reasoning, hypothetical scenarios) and multiple task types (MCQ, freeform, and cloze), which ensures a well-rounded assessment of model performance in scientific inquiry.
- Metrics like Factual Accuracy and Phrase Similarity for freeform and cloze tasks, respectively, offer a nuanced evaluation, considering both factual precision and contextual understanding.
- The use of RAG improves models' performance on reasoning questions, demonstrating a promising adaptation technique for enhancing model outputs.

### Weaknesses
 - The framework relies on a relatively small set of graduate-level climate textbooks, which may limit the diversity of contextual information and scientific perspectives in the generated questions. The selection of textbooks, while covering key areas, might not fully capture the nuances and debates within specific sub-disciplines of climate science, potentially leading to a narrow representation of the field's knowledge base.
- The expert-annotated dataset (ClimaQA-Gold) is relatively small, which may restrict the scalability and generalizability of automated annotations in other scientific disciplines. The limited size of the gold-standard dataset could hinder the development of robust, generalizable models, as the training data may not be sufficiently diverse to cover the full spectrum of scientific questions and reasoning patterns.
- Although improvements were noted, the models often struggle with reasoning-based questions, suggesting that further work is needed to refine reasoning capabilities in foundation models. This indicates a critical gap in the current capabilities of foundation models to perform complex scientific reasoning, which is essential for reliable climate science applications.
- The BLEU and BERTScore metrics show some bias towards the model used for question generation (GPT-3.5-turbo), which may affect the objectivity of the evaluation. The observed bias in these metrics raises concerns about the validity of the evaluation, as the metrics might be favoring models that are similar to the question generation model, rather than truly assessing their scientific accuracy and reasoning capabilities.

### Questions
Suggested Improvements:

- Increase the number and diversity of climate science sources, including a broader range of textbooks, research papers, and domain-specific databases. This would enhance the contextual diversity and robustness of the generated questions.
- Expand the expert-validated dataset to strengthen the framework's reliability and support automated annotations in additional scientific fields.
- Implement a tiered evaluation system that emphasizes model performance on reasoning and hypothetical questions separately, allowing for a deeper analysis of model strengths and weaknesses in scientific reasoning.
- Further experiment with retrieval-augmented generation using a wider array of sources or explore weighted retrieval to reduce distractors and improve information relevance.
- Introduce additional objective metrics to balance any biases introduced by BLEU or BERTScore, potentially incorporating domain-specific metrics tailored to scientific language accuracy and precision.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper designs an automated pipeline for constructing a ClimaQA benchmark, then presents two datasets, ClimaQA-Gold and ClimaQA-Silver, and finally conducts an experimental evaluation of existing LLMs on this benchmark.

### Strengths
- S1: This paper develops ClimaGen, an automated climate QA generator.
- S2: This paper proposes two datasets and three question-answering tasks.
- S3: Based on the ClimaQA benchmark, this paper presents some experiments to evaluate existing llms.

### Weaknesses
 - W1: One of the core innovations of the paper is the tool ClimaGen that automates the construction of ClimaQA, which involves the QA principle and prompt assembler. From line345 it appears to be a direct reference to other articles, which the authors do not describe in detail. However, this part directly affects the quality of the input prompt, which determines the quality of the generated QA pairs. The lack of detailed explanation regarding the prompt engineering and the specific QA principles used makes it difficult to assess the robustness and generalizability of the ClimaGen tool. The paper should provide a more thorough explanation of how these principles were derived and how they ensure the generation of high-quality, unbiased QA pairs.
- W2: This paper proposes a benchmark to assess the quality and scientific validity of the output of climate base models, but there is a lack of experimental validation that the QA pairs in the benchmark are scientifically meaningful, i.e., how to prove that the constructed dataset is able to help future research on climate foundation models, so that the output is of higher quality and scientific validity. The paper does not offer a clear methodology for validating the scientific rigor of the generated questions. It's crucial to demonstrate that the QA pairs accurately reflect the complexities and nuances of climate science, and that the benchmark can effectively differentiate between models with varying degrees of scientific understanding. Without this validation, the practical utility of the benchmark is questionable.
- W3: Lack of detailed information about the data source. The authors emphasize the data sources as 18 graduate-level textbooks, but give no detailed information about the data sources to prove it. The absence of specific textbook titles, editions, and even the selection criteria makes it difficult to verify the comprehensiveness and representativeness of the knowledge base used for QA pair generation. This lack of transparency undermines the reproducibility and reliability of the benchmark.
- W4: The experimental section lacks a case study. There is no visual comparison between the actual performance of the existing LLMs on these tasks and the difference between the groundtruth. The paper would benefit significantly from a detailed case study that visually compares the performance of different LLMs on specific QA pairs. This would provide a more intuitive understanding of the benchmark's ability to evaluate model performance and highlight the strengths and weaknesses of different models. Furthermore, it would demonstrate the practical relevance of the proposed evaluation metrics.
- W5: Writing flaws: lack of citations for some important ideas, such as in line32 and line35; inconsistency in font size of illustrations, such as Figure 6; lack of necessary explanations for the letters of the formulas, such as the equations about factual accuracy and phrase similarity.

### Questions
- Q1: Why only three tasks are designed and what is the motivation? Why not design judgment questions or are there any other possible tasks needed to assess the quality of scientific validity of model outputs?
- Q2: Both datasets of ClimaQA constructed in this paper are relatively small in size. What knowledge of climate is covered by these QA pairs? It shouldn't be very comprehensive, and I'm concerned that this only focuses on certain small branches of scientific knowledge. Is it possible to make some statistical analysis of the datasets to illustrate this?

### Soundness
2

### Presentation
2

### Contribution
2
