# Are LLMs Prescient? A Continuous Evaluation using Daily News as the Oracle

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 8, 3

## Abstract
Many existing evaluation benchmarks for Large Language Models (LLMs) quickly become outdated due to the emergence of new models and training data. These benchmarks also fall short in assessing how LLM performance changes over time, as they consist of static questions without a temporal dimension. To address these limitations, we propose using future event prediction as a continuous evaluation method to assess LLMs' temporal generalization and forecasting abilities. Our benchmark, \ourdataset{}, automatically generates question-answer (QA) pairs from daily news, challenging LLMs to predict ``future'' event outcomes. Our findings reveal that as pre-training data becomes outdated, LLM performance degrades over time. While Retrieval Augmented Generation (RAG) has the potential to enhance prediction accuracy, the performance degradation pattern persists, highlighting the need for continuous model updates.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Daily Oracle, a continuous evaluation benchmark for assessing LLMs' ability to predict future events using daily news. The authors automatically generate True/False and Multiple Choice question-answer pairs from daily news articles and evaluate various LLMs' temporal generalization capabilities, both with and without RAG. The experiments reveal performance degradation over time, particularly pronounced around models' knowledge cutoff dates.

### Strengths
1. Continuous evaluation: The daily updated benchmark effectively addresses data contamination concerns in LLM evaluation, providing a timely assessment mechanism.
2. Comprehensive experiments: The work presents thorough analyses of both open-source and closed-source models, clearly demonstrating the effect of knowledge cutoff dates on forecasting performance through moving average visualizations. The study reveals some valuable findings about model performance dropping after the cutoff date and how RAG of more recent data doesn't always help forecasting.

### Weaknesses
1. Limited technical novelty: The benchmark question format, construction prompt, and main steps are similar to TempLongBench.


- I suggest the authors provide a comparison table that clearly outlines the key differences between their pipeline and previous work like TempLongBench. 

- Additionally, consider including a flowchart or diagram of the dataset construction process with annotations explaining the rationale for each step.

- Also, the authors could add their prompts in the appendix for a better understanding.

---

2. Insufficient dataset quality evaluation: Though the construction pipeline has an LLM-based scoring and filtering step, there lacks an assessment of the final generated data quality.

I suggest the authors:
- Provide a breakdown of how many questions passed each principle in their quality control process
- Show or plot the distribution of the final data's score in each of the designed principle dimensions
- Conduct a human evaluation on a randomly sampled subset (e.g., 100 questions) of data, assessing both the news and QA data quality on specific metrics (e.g., Evidence, Reasonable, Plausible in TempLongBench)
- Also, conduct human forecasting performance on the sampled subset as a reference. Include inter-annotator agreement scores to demonstrate the reliability of their assessments.

---

3. Incomplete analysis of RAG results: The authors observe that RAG does not uniformly enhance performance for Llama3, with some RAG cutoffs performing worse than the closed-book setting, and conclude that outdated information may negatively impact performance.

I suggest the authors conduct a more detailed inspection of the RAG process:
- What articles does the model retrieve? Are they relevant to the question? 
- As the retriever is a simple BM25 model, does this process consider the temporal distance between the retrieved article and the target date? Will this influence the forecasting results? Will there be most of the cases that even if different RAG cutoffs are set, the model still retrieves the same and very old articles due to the BM25 limitation, such that the experiment condition of different RAG cutoffs becomes meaningless?

To make this analysis more concrete, the authors may consider:
- Compute and report the average relevance score of retrieved articles to the questions.
- Plot a histogram of the temporal distribution of retrieved articles for different RAG cutoffs.
- Analyze the correlation between article recency and model performance.
- Provide a specific case study of a few example questions, showing the full chain of retrieved articles and how they influenced the model's prediction.

### Questions
Will the code base become public? Will the database be maintained and updated in a daily manner and be available publicly?

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
This paper focuses on evaluating large language models (LLMs) in a way that remains relevant over time, as traditional benchmarks fail to capture the dynamic, ever-evolving nature of real-world information. To tackle this issue, the paper proposes using daily news articles to continuously assess LLMs' forecasting abilities. By generating QA pairs from news in various categories (such as business, politics, and arts), the authors create an evaluation benchmark named Daily Oracle. This benchmark is designed to evaluate LLMs’ ability to predict near-future events and test their temporal generalization.

### Strengths
The problem of degradation of performance over time is relevant and this resource along with the framework can be of large interests for the community.

### Weaknesses
The work presents a known problem and dive deep into potential impacts. While the paper has its merits, I don't think it is at a maturity level to be published yet (see my questions below).

The work relies on several automatic procedure to build the dataset that require clarification: 
- Did you evaluate the clustering approach? how is your clustering approach different from bert-topic? 
- What's the overlap rate between question and answer? 
- Degradation after cutoff is expected and RAG is commonly used to mitigate the problem. However, in this work the retrieval used to test RAG is quite weak. First, BM25 should be at least replaced with some hybrid or dense approach. Second, 5 top articles may not be enough (how did you choose 5?) and truncating the article at 512 can potentially cut off answers (it is unclear if the provided information contain the answer. In other words, how do we know if the problem is the retrieval or the model ability to handle such information?

### Questions
The work relies on several automatic procedure to build the dataset that require clarification: 
- Did you evaluate the clustering approach? how is your clustering approach different from bert-topic? 
- What's the overlap rate between question and answer? 
- Degradation after cutoff is expected and RAG is commonly used to mitigate the problem. However, in this work the retrieval used to test RAG is quite weak. First, BM25 should be at least replaced with some hybrid or dense approach. Second, 5 top articles may not be enough (how did you choose 5?) and truncating the article at 512 can potentially cut off answers (
it is unclear if the provided information contain the answer. In other words, how do we know if the problem is the retrieval or the model ability to handle such information?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a continuous evaluation benchmark for LLMs testing the ability to make predictions about real-word events and assess whether they show temporal generalisation and tests different LLMs using multiple eval configurations (closed-book setting, constrained open-book setting, etc).

### Strengths
The paper presents a very interesting idea as a benchmark for LLMs and describes in details the dataset construction and evaluation. I think this work would be very relevant as a benchmark for LLMs at ICLR.

### Weaknesses
While the paper is extremely interesting from a dataset construction point of view, I have found it a bit hard to follow through the experiment section, especially in terms of the task performed and each stage and the knowledge that the model had. This for me is true in particular for the "Constrained open book setting" sub-section, but in general all through the evaluation overview. I would suggest the authors to adopt a running example, referring to a specific model with a clear cutoff date and a question regarding a piece of news, in order to highlight how the model would perform differently in different situations.

It seems that the dataset is completely constructed automatically through the usage of LLMs - I was wondering if the authors have performed any manual check to assess the quality of the construction and if they could add details and evaluation metrics about that.

### Questions
It seems that the dataset is completely constructed automatically through the usage of LLMs - I was wondering if the authors have performed any manual check to assess the quality of the construction and if they could add details and evaluation metrics about that.

Are the authors planning to set-up a platform where users could test LLMs against the created dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
⁤This paper constructs a new benchmark to evaluate LLMs in real time by testing their ability to predict future events. ⁤⁤Traditional benchmarks quickly become outdated as LLMs and the world itself continuously evolve, limiting their ability to reflect current model performance. ⁤⁤To address this, the authors introduce Daily Oracle, a continuously updated dataset created from daily news articles. ⁤⁤Each day, they generate question-answer pairs about real-world events across domains like politics, science, and business, allowing for an assessment of whether LLMs can forecast future events based on prior knowledge. ⁤

⁤The findings show that LLMs experience a steady decline in performance over time as their training data becomes outdated, weakening their predictive abilities without regular updates. ⁤⁤Although techniques like RAG offer some enhancement by incorporating newer information, the models still struggle to maintain accuracy as the distance grows between training data and real-world events. ⁤⁤Overall, this paper presents Daily Oracle as a tool for ongoing evaluation of LLMs, focusing on their ability to generalize temporally through daily news-based question-answer pairs. ⁤

### Strengths
1. The writing in this paper is clear and easy to follow, with a well-organized structure. 
2. The authors' Daily Oracle benchmark covers more topics and more recent dates compared to previous benchmarks, and it provides continuous daily evaluation. 
3. In the experiments, the authors observe a notable performance drop across all LLMs in the closed-book setting after the knowledge cutoff date. They further analyze this degradation by testing with RAG and gold article settings, observing similar declines.

### Weaknesses
 **Major Issues:**
1. **Limited Innovations in Data Construction**: Although the benchmark is one of the main contributions, the data construction approach is highly similar to existing work. Specifically, the authors also rely on the Common Crawl News Dataset as the data source, and their QA construction process and question formats closely resemble TCELongBench. Aside from slight differences in the prompting steps, the main distinction appears to be the inclusion of True/False question types. This suggests limited technical contributions in data construction. This paper also lacks comparisons with TCELongBench in terms of both the approach and the quality of the generated QA pairs.
2. **No Human Verification**: The authors rely entirely on GPT-3.5 and GPT-4 to generate the benchmark’s QA pairs, yet the reliability of this approach is unverified. For instance, in the QA filtering step, GPT-3.5 scores based on seven principles, criteria that could be challenging even for humans to judge objectively. The authors should include a rationale for choosing these specific principles, explain why a score of 13 or above indicates a quality question, and provide inter-rater reliability among human evaluators. It would also be necessary to assess the correlation between GPT-3.5’s scores and human scores to gauge data quality accurately, even if only on a subset.
3. **No Cost Description or Comparison**: Since continuous daily evaluation is highlighted as a major benefit of this benchmark, it would be helpful to provide specific cost estimates for using Daily Oracle to periodically (daily, weekly, monthly) evaluate LLMs. Additionally, a cost comparison with other data construction methods, such as TCELongBench, is needed to assess the feasibility of this approach.

**Minor Issues:**
1. **Relatively Trivial Conclusion**: The conclusion that LLM performance declines significantly after the knowledge cutoff date is fairly predictable. Additional analyses and insights would be beneficial, such as examining a time span beyond the last four years to study how LLMs’ performance in memorization changes over decades. The rise and drop in Figure 5’s gold article setting post-knowledge cutoff could also be further analyzed (e.g., does it relate to inconsistencies in LLMs’ parametric knowledge). Such experiments would deepen community understanding of LLMs’ temporal generalization.
2. **No Estimate of Human Performance**: Adding an estimated score for average human or domain expert performance would help contextualize the accuracy scores achieved by the LLMs.

**Typos:**
- Lines 312, 321, 425, 453: Figure 7 → Figure 3.

### Questions
See the above Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
