# FinTruthQA: A Benchmark Dataset for Evaluating the Quality of Financial Information Disclosure

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Accurate and transparent financial information disclosure is crucial in the fields of accounting and finance, ensuring market efficiency and investor confidence. Among many information disclosure platforms, the Chinese stock exchanges' investor interactive platform provides a novel and interactive way for listed firms to disclose information of interest to investors through an online question-and-answer (Q\&A) format. However, it is common for listed firms to respond to questions with limited or no substantive information, and automatically evaluating the quality of financial information disclosure on large amounts of Q\&A pairs is challenging. This paper builds a benchmark FinTruthQA, that can evaluate advanced natural language processing (NLP) techniques for the automatic quality assessment of information disclosure in financial Q\&A data. FinTruthQA comprises 6,000 real-world financial Q\&A entries and each Q\&A was manually annotated based on four key evaluation criteria: \textit{question identification}, \textit{question relevance}, \textit{answer readability}, and \textit{answer relevance}. We benchmarked various NLP techniques on FinTruthQA, including statistical machine learning models, pre-trained language model and their fine-tuned versions, as well as large language models (LLMs).  Experiments showed that existing NLP models have strong predictive ability for \textit{question identification} and \textit{question relevance} tasks, but are suboptimal for \textit{answer readability} and \textit{answer relevance} tasks. By establishing this benchmark, we provide a robust foundation for the automatic evaluation of information disclosure, significantly enhancing the transparency and quality of financial reporting. FinTruthQA can be used by auditors, regulators, and financial analysts for real-time monitoring and data-driven decision-making, as well as by researchers for advanced studies in accounting and finance, ultimately fostering greater trust and efficiency in the financial markets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a dataset designed to assess the quality of responses on Chinese stock exchange investor platforms, specifically the Shanghai and Shenzhen exchanges. The FinTruthQA dataset includes 6,000 Q&A entries, each manually annotated across four evaluation criteria: question identification, question relevance, answer readability, and answer relevance. The authors benchmark various NLP models, including machine learning methods, pre-trained language models, and large language models, demonstrating that while models perform well on question-related tasks, challenges persist in evaluating answer readability and relevance.

### Strengths
1. Novel Benchmark Dataset: The paper introduces FinTruthQA, a unique and practical dataset for evaluating the quality of financial information disclosure in Q&A format on investor platforms. This dataset fills a gap in financial NLP, providing a structured way to evaluate both question and answer quality, which is valuable for real-world applications in finance.

2. Comprehensive Model Evaluation: The authors benchmark a range of NLP techniques, from traditional ML-based models to pre-trained language models (PLMs) and LLMs, demonstrating the utility and limitations of each in assessing Q&A quality.

### Weaknesses
1. Limited Evaluation Settings: The evaluation framework is somewhat restrictive, as only ML-based and PLM-based models are assessed across most tasks, while LLMs are evaluated solely on the answer relevance task in a zero-shot setting. A comprehensive comparison across all tasks is necessary to fully understand the strengths and limitations of ML-based models, PLMs, and LLMs. Moreover, applying only zero-shot results for LLMs on answer relevance is inconsistent with the supervised fine-tuning used for ML and PLM models, which could skew the comparative assessment. The lack of a consistent evaluation protocol makes it difficult to draw definitive conclusions about the relative performance of these different model classes. Specifically, the paper does not explore how fine-tuned LLMs would perform on the question identification, question relevance, and answer readability tasks, which are crucial for a complete understanding of their capabilities.

2. Copyright and Data Usage Concerns: The paper lacks clarity regarding copyright compliance for the data sources. It is unclear if legal permissions have been obtained to use and openly release the Q&A entries from stock exchange platforms for research purposes. Explicit details on copyright considerations are essential to ensure the ethical and legal viability of this dataset for the broader research community. The absence of clear statements about the terms of use for the data raises concerns about the dataset's suitability for open research and potential legal issues.

3. Exclusion of Financial LLMs: While the paper evaluates a range of models, it does not include financial domain-specific LLMs, which are highly relevant for the specialized nature of this task. Incorporating financial LLMs would provide valuable insights into the performance gains from domain-specific pre-training and would create a more representative assessment of available model options. The exclusion of these models limits the practical applicability of the benchmark, as it fails to consider models specifically designed for the financial domain, which are likely to perform better than general-purpose models.

4. Class Imbalance in Dataset: The dataset suffers from significant class imbalance, such as in tasks like question identification, where the majority of samples are labeled as positive. This imbalance could lead to models that are biased towards the majority class and perform poorly on minority classes, which are often the most important for real-world applications. The paper does not adequately address the potential impact of this imbalance on model performance or explore techniques to mitigate it.

### Questions
See weakness

### Soundness
2

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
4

### Summary
The authors discuss the relationship between the quality of disclosure in financial Q&A data and the ability of investors to make informed decisions. In this paper, the author created a new benchmark dataset (FinTruthQA) containing 6,000 manually annotated financial Q&A pairs from Chinese stock platforms. The author benchmarked various approaches including ML-based models, pre-trained language models, and large language models.

### Strengths
1. This paper targets a real-world problem in financial markets about how to improve transparency and quality of financial reporting. 

2. The annotation process is comprehensive in that the annotation team takes multiple rounds and quality control, comprehensive evaluation using multiple metrics, and documentation of the data collection and processing steps. 

3. This paper evaluated multiple types of models (ML, PLM, LLM), including domain-specific models, and continued pre-training models. The author also showed a detailed error analysis and performance comparisons. 

4. The experiment results demonstrated that domain-specific models, FinBERT with continued pre-training, perform better on complex tasks. This insight is useful to the domain.

### Weaknesses
1. The FinTruthQA dataset is exclusively from Chinese markets. In addition, the proposed dataset focuses only on the Q&A format, excluding other types of financial disclosure (like, long reports, and analytic reports).

2. In question relevance, the label is imbalanced (99.51% positive), and limited number of samples for some categories. This may affect the validity and generalizability of the benchmark results.

3. Limited overall technical contribution to financial Q&A or general domain Q&A.

4. Experiment detail is not comprehensive, such as no details such as temperature were reported.

### Questions
See in Weaknesses.

In addition, the authors still use traditional metrics when evaluating. I'm not sure if this is entirely appropriate for evaluation in the financial sector.

### Soundness
3

### Presentation
4

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
The paper introduces a dataset designed to assess the quality of financial information disclosure using natural language processing (NLP) techniques. This dataset, FinTruthQA, consists of 6,000 annotated Q&A entries from Chinese stock exchanges, focusing on four evaluation criteria: question identification, question relevance, answer readability, and answer relevance. The authors benchmarked various language models, finding that while models perform well in identifying and categorizing questions, they struggle with answer readability and relevance.

### Strengths
1. Dataset: The paper introduces a  dataset, FinTruthQA, specifically tailored for assessing financial information disclosure quality, covering critical criteria such as question relevance and answer readability. 

2. Real-world Applicability: The dataset and methods are designed with practical applications in mind, aiding auditors, analysts, and regulators in real-time monitoring and enhancing transparency in financial disclosures.

### Weaknesses
 1. Title Discrepancy: The title of the paper suggests a focus on the truthfulness of the responses within the dataset. However, the actual content primarily addresses other aspects such as readability and relevance. A title that more accurately reflects the paper's content could improve its alignment with the reader's expectations. 

 2. Baseline Methodologies for Readability: The paper could be strengthened by including more established baselines for evaluating readability, such as the Gunning fog index. For a comprehensive view on this, the authors might consider reviewing literature from targeted workshops like the TSAR workshop on readability (https://tsar-workshop.github.io/). 

 3. Label Distribution and Utility: The current label selection, particularly for answer readability, seems suboptimal. Labels 2 and 3 are underrepresented, appearing in less than 3% of the QA pairs. This distribution is problematic, as evidenced by the classification challenges shown in Figure 4, where Label 4 is frequently misclassified as Label 1, but rarely as Labels 2 or 3. Refining these categories could enhance the model's learning and classification accuracy. 

 4. Definition of Readability: The paper's definition of readability focuses on ease of understanding and quality of writing. However, readability could be more effectively assessed by considering additional components such as structure, clarity, style, and grammar. A more detailed framework for readability would likely improve the assessment’s depth and utility.

### Questions
None

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
The paper introduces FinTruthQA, a new benchmark dataset developed to evaluate the quality of financial information disclosures on interactive platforms for investors in Chinese stock exchanges (Shanghai Stock Exchange and Shenzhen Stock Exchange). The dataset comprises 6,000 real-world Q&A entries and assesses disclosure quality across four key criteria: question identification, question relevance, answer readability, and answer relevance. The authors benchmark various machine learning (ML) and pre-trained language models (PLMs) and examine their effectiveness on these tasks.

### Strengths
The authors address the crucial challenge of evaluating the quality of financial disclosures on platforms where companies communicate with investors. The interactive nature of these disclosures and their unstructured format make this a valuable problem.

By focusing on investor-platform Q&A interactions, the paper explores a unique and under-researched form of financial communication that differs from more structured formats like reports or calls.

The experiments cover a wide range of ML and PLM-based models, and the paper offers insights into their performance, especially emphasizing the limitations of current models in answer readability and relevance tasks. This provides a strong foundation for future improvements.

### Weaknesses
Although the dataset focuses on investor Q&A in the Chinese stock exchange context, the lack of testing across different regulatory and cultural contexts limits its generalizability. Without broader applicability, the impact of FinTruthQA as a global benchmark remains restricted.

The reliance on human annotation for subjective criteria (e.g., answer readability and relevance) introduces potential biases. While the authors conducted quality control, it is unclear how consistently these subjective labels would hold across diverse annotator groups or application settings.

Although the paper provides an overview of performance results, it lacks an in-depth analysis of errors made by models. Understanding specific failure cases would offer valuable insights into the dataset’s complexity and guide future model improvements.

Many releted papers are not refered, such as 
The FinBen: An Holistic Financial Benchmark for Large Language Models
FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models
Large Language Models as Financial Data Annotators: A Study on Effectiveness and Efficiency
FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making
Open-FinLLMs: Open Multimodal Large Language Models for Financial Applications

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
2
