# Industrial Benchmarking of LLMs: Assessing Hallucination in Traffic Incident Scenarios with a Novel Spatio-Temporal Dataset

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Large language models (LLMs) hold revolutionary potential to digitize and enhance the Health & Public Services (H&PS) industry. Despite their advanced linguistic abilities, concerns about accuracy, stability, and traceability still persist, especially in high-stakes areas such as transportation systems. Moreover, the predominance of English in LLM development raises questions about how they perform in non-English contexts.

This study introduces a novel cross-lingual benchmark dataset comprising nearly 99,869 real traffic incident records from Vienna (2013-2023) to assess the robustness of state-of-the-art LLMs (>9) in the spatio and temporal domain of traffic incident classification.  We then explored three hypotheses — sentence indexing, date-to-text conversion, and German-to-English translation — and incorporated Retrieval Augmented Generation (RAG) to further examine the models' ability to handle hallucinations in both spatial and temporal contexts.

Our experiments with GPT-4 and Llama models reveal significant performance disparities across these hypotheses in the spatio-temporal domain and also demonstrate how RAG can mitigate what types of hallucinations. These findings underscore the need for enhanced cross-lingual capabilities and improved explainability in LLMs.  We provide open access to our Health & Public Services (H&PS) traffic incident dataset, with the project demo and code available at [Website](https://sites.google.com/view/llmhallucination/home).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a traffic incidents spatio-temporal dataset about spatio-temporal QA instances in German. The data is processed based on publicly available dataset. Evaluation of multiple LLM families is performs on this proposed dataset. It also shows the ablation results of several prompting techniques, like whether includes bullet point index, human-readable data input format and English-only query.

### Strengths
* The proposed task and dataset is highly relevant to the real-world problem. The setting is different from synthetic datasets. It is very realistic and would be helpful if the dataset setting is sound.
* A rich ablation study and analysis of the evaluation result

### Weaknesses
* The evaluating test set is limited. A small number of test cases are used, it's hard to say whether the produced evaluation result can be generalized.
* The setting is not well explained, leaving concerns about the soundness of the proposed setup
	* What is the exact input provided to the model (besides the question prompt)? The questions are heavily depend on whether related incidents are provided and how they are provided. We don't have sufficient details in the current version of paper.
	* How is the metric mAP calculated
	* For the RAG baseline, what is the size and pool used for retrieval?
* Using generation output under different temperatures to represent model generalizability and robustness is a questionable setting
* Though the paper mentioned that the existing benchmarks do not support multilingualism well, this proposed dataset is also not broad in terms of language coverage since all descriptions are in German. It's not bad to only have one language, but a smaller-scale claim would be helpful.

### Questions
For the interpretation of the RAG performance (the paragraph before Section 6), why is the conclusion that it enhances the reasoning while it answers more questions incorrectly compared with plain GPT-4 in Table 3?

Please also refer to the question mentioned in the weaknesses section.

### Soundness
1

### Presentation
2

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
The paper studies the spatiotemporal reasoning capability of LLMs. It argues that existing LLM benchmarks still lack data and evaluation on spatial and temporal reasoning; there are not enough findings regarding this reasoning capability. The paper introduces a dataset and benchmark for handling spatiotemporal traffic incident questions. The dataset includes 99,869 traffic incident records from Vienna’s public transport system across 14 incident categories for the past 10 years. In addition, it also includes both German and English languages. 

They test three hypotheses related to sentence numbering, standardized date-to-text conversion, and translating German context data to English on 15 (or 14) questions on varying LLMs and temperatures. Additionally, they examine the application of Retrieval-Augmented Generation (RAG) to mitigate hallucinations. In summary, the results suggest that none of the LLMs can effectively answer spatial or temporal questions, even with RAG. In addition, the multiple-regression analysis shows that the hypothesis of translating to English significantly improves the performance and that temperatures have a non-linear relationship with the performance.

### Strengths
1. The paper provided a dataset that consisted of spatial and temporal information.
2. The paper confirmed the previous findings that LLMs have unsatisfactory performance in spatiotemporal reasoning when using standard prompt engineering techniques (including RAG).

### Weaknesses
1. While introducing a new dataset is a welcome contribution, the introduced data quality is not thoroughly validated. In Section 3, the paper discusses dataset creation (or simulation) with a minimum discussion on the "LLM-Enabled Tagging and Traffic Analysis" process in Figure 2. In addition, most existing benchmarks have questions and ground-truth answers (see a few examples in Table 8 in the appendix), and the introduced dataset only consists of records. The evaluation of LLMs using the proposed benchmark is then unclear. 
2. The paper conflates the definition of hallucination and equates it to low mAP (line 373). There could be multiple reasons why the answer is incorrect; not all will be plausible.
3. I found that many statements in the text lack support from the results. For example, 
    1. Table 3 shows the experiment results for 14 questions, but the text (line 339) suggests 15 (10 + 5).
    2. Table 3 shows RAG's rather poor performance, but the text (line 505) suggests that it reduces "off-topic" hallucinations. 
    3. Table 4 shows "ns" for Hypothesis 1 and Hypothesis 2, but the text (line 431) suggests that "... [the hypotheses] aids in maintaining robustness".
4. There are many papers that work in enhancing spatio-temporal reasoning capability of LLMs that the paper should acknowledge and discuss. For examples,
    1. Li, F., Hogg, D. C., & Cohn, A. G. (2024, March). Advancing spatial reasoning in large language models: An in-depth evaluation and enhancement using the stepgame benchmark. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 38, No. 17, pp. 18500-18507).
    2. Ouyang, X., & Srivastava, M. (2024). LLMSense: Harnessing LLMs for High-level Reasoning Over Spatiotemporal Sensor Traces. arXiv preprint arXiv:2403.19857.
    3. Wu, W., Mao, S., Zhang, Y., Xia, Y., Dong, L., Cui, L., & Wei, F. (2024). Mind’s eye of LLMs: Visualization-of-thought elicits spatial reasoning in large language models. arXiv preprint arXiv:2404.03622.
    4.

### Questions
-

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new Health & Public Services (H&PS) dataset called H&PS Traffic Incident Dataset, which contains approximately 100,000 traffic incident reports written in German over the past 10 years. The authors then tested the capabilities of the current state-of-the-art (SOTA) large language models (LLMs) on several tasks based on this dataset, with a focus on spatio-temporal question answering. Most of the LLMs tested performed poorly on the dataset, although the authors verified that certain techniques were effective in improving performance. These techniques included (1) numbering sentences sequentially in the description, (2) spelling out dates and times, (3) translating the description into English, and (4) using Retrieval Augmented Generation (RAG).

### Strengths
* The paper publishes and open-sources a dataset in a non-English language. The dataset covers real-world, socially important data, namely traffic incident reports.

### Weaknesses
* Unclear tasks and presentation: although the paper presents a new dataset and benchmark, the very definition of what tasks the paper is trying to solve with LLMs remain unclear. The abstract says "domain of traffic incident classification" and Section 3.1 mentions "tagging systems" but Section 5.2 mentions "identifying the top 10 most affected stations" and throughout the paper the task seems to be generic question-answering based on the examples. 
  * Related, but the paper is unclear how the test data used in the experiments is created
  * If the task is question-answering (for example, list of affected stations, as shown in Table 3) how do you evaluate the results? The paper mentions "we focus on the stability and accuracy (mAP)" but that's not how you usually evaluate question answering (also mAP is precision, not accuracy, and used for evaluating information retrieval in general). Figure 4 is also drawn using "score" which is not defined in the paper.
  * More importantly, many of the questions, such as "Find all incidents that begin between ... " (in Section 3.2) are simple information retrieval tasks that can be solved by simple SQL. Given that LLMs lack full access to the entire database (except in limited cases with RAG), the task appears ill-suited for LLMs.
* Trivial improvements: the paper proposes some research questions and techniques to improve the task proposed in the paper (Section 4). All of these seem trivial and some have shown to work in other domains already (e.g., translating into English), so they don't constitute the core technical contribution of the paper.
  * Slightly related, but I'm not sure why the experiments are overly focused on the temperature parameter. Can we simply choose the best parameter based on, e.g., the validation set and use it throughout? 
* Societal impact: Finally, even though the dataset is derived from the data that is socially important, there's no strong backing why the publish dataset and the tasks addressed in the paper is important socially.

### Questions
* Section 1. "across multiple languages" — I believe the dataset is monolingual (just German)?
* Section 2. "ChatGPT (Achiam et al., 2023) — the first author of the ChatGPT paper is "OpenAI"
* Section 2. "minority languages like German" — I wouldn't personally call German "a minority language" if that's the case almost all languages in the world, except English and maybe Mandarin, would be minority languages...
* Section 3.2. I'm not sure what the authors mean by "a Google Maps agent." Does Google Map have an agent? What does it do?
* Section 4 "Hypothesise" you meant "Hypotheses"?
* It'd be helpful to include some statistics about the evaluation data used for the experiments.
* Can you improve LLMs for this particular task by continued pretraining (or fine-tuning) on this dataset?

### Soundness
2

### Presentation
2

### Contribution
2
