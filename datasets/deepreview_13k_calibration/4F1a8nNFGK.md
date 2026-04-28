# Context is Key: A Benchmark for Forecasting with Essential Textual Information

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
\vspace{-0.2cm}
Forecasting is a critical task in decision making across various domains. While numerical data provides a foundation, it often lacks crucial context necessary for accurate predictions. Human forecasters frequently rely on additional information, such as background knowledge or constraints, which can be efficiently communicated through natural language. However, the ability of existing forecasting models to effectively integrate this textual information remains an open question. 
To address this, we introduce ``Context is Key'' (CiK), a time series forecasting benchmark that pairs numerical data with diverse types of carefully crafted textual context, requiring models to integrate both modalities. 
We evaluate a range of approaches, including statistical models, time series foundation models, and LLM-based forecasters, and propose a simple yet effective LLM prompting method that outperforms all other tested methods on our benchmark. 
Our experiments highlight the importance of incorporating contextual information, demonstrate surprising performance when using LLM-based forecasting models, and also reveal some of their critical shortcomings. 
By presenting this benchmark, we aim to advance multimodal forecasting, promoting models that are both accurate and accessible to decision-makers with varied technical expertise.
The benchmark can be visualized at \url{https://servicenow.io/context-is-key-forecasting/v0/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new benchmark, CiK, to evaluate how well forecasting models can use essential textual context alongside numerical data to improve prediction accuracy. The benchmark includes 71 tasks across various fields, where models need to integrate natural language information—like historical trends or future events—with time series data for accurate forecasts. To assess performance, the authors develop the Region of Interest CRPS (RCRPS) metric, which emphasizes context-sensitive parts of the forecast and accounts for constraints stated in the text. Through experiments, they show that a simple prompting method for large language models (LLMs) outperforms traditional forecasting methods, underscoring the importance of context for improved predictions.

### Strengths
1. Good writing and easy to follow
2. CiK uniquely requires essential textual context for forecasting, marking a new direction in multimodal prediction.
3. The benchmark is robust, with real-world tasks and a novel, context-focused RCRPS metric.

### Weaknesses
1. Missing Information on Context Annotations: 
The paper relies on carefully crafted textual contexts but omits crucial details about the annotation process, such as the guidelines provided to annotators, the number and qualifications of annotators, methods used to resolve disagreements, and quantitative measures of inter-annotator agreement (IAA). This lack of information raises questions about the consistency and reliability of the annotations. Including examples or a sample of the annotation guidelines, a description of annotator expertise, and the process for calculating IAA would strengthen the benchmark’s credibility and demonstrate rigorous annotation practices.

2. Limited Benchmark Novelty:  
While the CiK benchmark combines existing time-series datasets with manually created textual contexts, its contribution to multimodal benchmarks is limited in novelty. The approach resembles prior work that integrates time-series data with textual sources like news or social media.[1,2] To clarify its uniqueness, the authors could provide comparisons to specific existing work and clearly articulate the novel contributions or improvements over these prior works. Additionally, the manual creation of contexts raises concerns about scalability; introducing semi-automated methods or leveraging AI to generate contexts could make the benchmark more practical for real-world applications and future expansions.

3. Ambiguous Task Type Annotations: 
The paper lacks clarity in task categorization, with no explicit definitions provided for each model capability category. For instance, “instruction following” is inconsistently applied, leaving tasks like “Public Safety” uncategorized, despite requiring instruction interpretation. It would be helpful if the authors included definitions for each capability category, specified criteria for categorizing tasks, and offered examples illustrating why certain tasks fall into each category. This additional information would clarify the task taxonomy and improve the interpretability of the benchmark structure.

4. Unexplained Results Discrepancies:  
Certain performance discrepancies raise concerns about the validity of the benchmark’s metrics. For example, LLMP Mixtral-8x7B shows lower CRPS performance with context compared to without in Figures 4 and 5, yet it still appears to outperform traditional quantitative models when using context. This inconsistency suggests that CRPS may not fully capture the forecast quality in multimodal contexts. The authors could benefit from including a discussion on why CRPS was chosen, exploring alternative or complementary metrics, or providing a deeper analysis of the observed discrepancies to enhance the reliability of the reported results.

5. Limited Model Variety:  
The benchmark’s experimental setup primarily includes larger models like Llama-3 series, limiting the variety across model sizes and architectures, as well as smaller models like Mistral, Qwen, and Falcon. A more diverse set of models, including smaller or less resource-intensive models, could offer broader insights and improve the benchmark’s generalizability. Explaining any practical or strategic reasons for the current model selection would provide additional context. Exploration of smaller models or discussing plans for future testing would also enhance the paper’s impact.

### Questions
1. How the textual contexts were annotated, including any guidelines, annotator expertise, and inter-annotator agreement (IAA) metrics?

2. Do the authors envision methods to automate or partially automate this process, such as using existing NLP techniques to generate context?

3. Could the authors provide explicit definitions for each capability and clarify the criteria used to categorize tasks?

4. Could the authors clarify whether this discrepancy suggests limitations of the CRPS metric or other factors in the benchmark design?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the integration of contextual textual data with numerical time series to improve time series forecasting. It introduces the CiK benchmark, consisting of 71 diverse forecasting tasks across multiple domains. Unlike existing benchmarks, CiK requires models to process both numerical data and associated textual context, reflecting real-world complexities such as seasonal trends or future constraints (e.g., maintenance periods). The authors also propose a novel metric, the Region of Interest Continuous Ranked Probability Score (RCRPS), which weights context-sensitive time windows and penalizes constraint violations.

### Strengths
The paper provides rigorous evaluation, testing various model types and prompting techniques. The introduction of the RCRPS metric enhances assessment accuracy by factoring in context relevance and constraint adherence. The combination of text and time series has always been something that researchers in the field want to try, and this benchmark provides a good research foundation. The writing structure of the paper is very clear

### Weaknesses
From the experimental results, we can see that text provides a good auxiliary role, but this method should be limited to models with LLM as the backbone.

### Questions
1. Are all the time series is univariate? 
2. In this benchmark construction, have you tried very refined text rather than information at a specific time step or overall? How did it perform?
3. Regarding retrieval, if I use the time series segment corresponding to a specific text as the retrieval "text", will the performance be better? Because this is more direct.

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
The paper addresses a pertinent issue: the scarcity of benchmarks for context-enhanced forecasting. Although many recent studies focus on predicting future values using textual cues, there is limited data available for training and evaluating such models. This paper introduces a manually curated benchmark specifically for text-aided time-series forecasting, featuring numerical time series data paired with contextual text. The benchmark is extensive in its selection of domains and tasks, providing a comprehensive resource. It is also thoroughly evaluated across a wide range of forecasting models. Furthermore, the paper introduces a novel metric for forecast evaluation.

### Strengths
This work is original and highly relevant to the current trend of LLM-based forecasting. The benchmark is well-designed, offering broad coverage across various domains and tasks, with results for multiple forecasters included to showcase its capabilities. The analysis and results are clearly presented, with examples and figures that effectively illustrate key benchmark characteristics and greatly enhance comprehension. Additionally, the paper introduces an intriguing new metric for evaluating forecast quality within relevant regions, which adds depth to the evaluation framework.

### Weaknesses
While this work is both novel and relevant, it lacks analytical rigor in its benchmark evaluation. The reader is supposed to assume that all provided textual information contributes meaningfully to the forecasts, with minimal evidence beyond the overall performance improvements seen for the entire dataset. Evaluating the relevance of the textual context—perhaps through methods such as LLM-based or human assessments—would strengthen the claim that these textual data are correct and relevant descriptions for the time series. Additionally, some covariate information appears to include future events, which a causal forecaster would not typically access (e.g., “Speed From Load” in Appendix B.2). This raises concerns about causal consistency, as there is no mechanism for systematically separating different types of contextual data other than through manual or LLM editing. Such limitations could present challenges for users who want to avoid incorporating future or irrelevant covariate information in their experiments.

The paper also lacks clarity regarding the historical context length and forecasting horizon—key details that should be specified. Furthermore, the reliability of the benchmark results hinges on the sample size, yet no information about the number of samples for the datasets is provided.

Perhaps the most notable contribution of the paper is its manual curation of the dataset. However, this process remains underexplained. Details such as the curation methodology, sources of textual data, and the criteria used for selecting relevant data are absent, which limits the transparency of this work.  A more comprehensive discussion of these aspects would significantly enhance the credibility and utility of the dataset for future research.

### Questions
Questions:
1) Does the covariate information always imply the availability of the future values of the covariates, or are there examples with covariate information provided only for the history time series?
2) While I believe it would be handled in a discussion of the manual curation process, I wanted to know if the entire manual curation for so many datasets was done by the authors who would be credited for the paper or if any form of crowdsourcing was utilized for the manual tasks. Were the annotators paid fairly for their efforts if any crowdsourcing was utilized? Was any LLM used during the manual curation process?

Suggestions for the authors:
1) Include a discussion on the manual curation process with information on the data sources and the selection of relevant context from them.
2) Include benchmark descriptions mentioning the sequence lengths, prediction horizon, and number of sequences present in each benchmark to build confidence in the robustness of the work.
3) Provide some ideas for separating different contextual information in the text.
4) Highlight the efforts taken to ensure that any contextual information paired with the time series is actually correct/relevant. Do a similar task to highlight the relevance of the said "region of interest."

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces "Context is Key" (CiK), a benchmark designed to evaluate the ability of forecasting models to integrate numerical data with essential textual context (time-invariants, history, covariates, future and causals...). Recognizing that accurate forecasting often requires more than just numerical inputs, the authors aim to bridge this gap by creating a collection of tasks that necessitate the use of both modalities. Some key contributions:
1. a relatively complete benchmark named cik
2. analysis of different models
3. propose direct prompt, which is a simple strategy to prompt LLM to do time-serise prediction

### Strengths
I would say this is a 'huge' work, congratulations!
The following are some points I agree:
1. the benchmark is relatively complete and has a potential to have impact, which include textual context (time-invariants, history, covariates, future and causals).This work may lead to complex or graph modelling with these information.
2. the proposed strategy to evaluate is simple but useful.
3. the paper contains some use case and discussion of existed models

### Weaknesses
1. lack of discussion of noise in texts. The texts are complete but the quality filter is not well designed. In general, we need more well-designed texts which is really useful
2. what is the importance of texts? are they hidden in time-series itself? For me, time-series is the sampling result of a complex system, and even you have already done a lot and try to give more complete one, but the system is hard to define. As a result, the time-series itself may contain more information than the texts.
3. besides model evaluation, the benchmark is hard to use as in real world, people may prefer to use simple model and may lack of texts.
4. The cooperation between texts and numbers is not well-designed. Generally, LLMs including GPT are not good at dealing with numbers, and they are not sensitive to the symbols in numbers.

### Questions
1. can you just open-source all the related-materials and I think it's better to let all people to judge if it has enough value and easy to use.
2. how do you choose the best-quality text and how would you access this quality?
3. Is there any better way to cooperate the numbers in prompt to evaluate the effect of the benchmark?
5. text brings more calculation, but the effect of the texts is not well discussed. How to balance and choose the most effective one?

### Soundness
3

### Presentation
3

### Contribution
2
