# MIRAI: Evaluating LLM Agents for International Event Forecasting

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
\label{sec:abstract}

Recent advancements in Large Language Models (LLMs) have empowered LLM agents to autonomously collect world information, over which to conduct reasoning to solve complex problems. Given this capability, increasing interests have been put into employing LLM agents for predicting international events, which can influence decision-making and shape policy development on an international scale.
Despite such a growing interest, there is a lack of a rigorous benchmark of LLM agents' forecasting capability and reliability. 
To address this gap, we introduce \dataset, a novel benchmark designed to systematically evaluate LLM agents as temporal forecasters in the context of international events. 
Our benchmark features an agentic environment with tools for accessing an extensive database of historical, structured events and textual news articles. 
We refine the GDELT\footnote{GDELT: \href{https://www.gdeltproject.org/}{https://www.gdeltproject.org/}} event database with careful cleaning and parsing to curate a series of relational prediction tasks with varying forecasting horizons, assessing LLM agents' abilities from short-term to long-term forecasting.
We further implement APIs to enable LLM agents to utilize different tools via a code-based interface.
In summary, \dataset comprehensively evaluates the agents' capabilities in three dimensions: 1) autonomously source and integrate critical information from large global databases; 2) write codes using domain-specific APIs and libraries for tool-use; and 3) jointly reason over historical knowledge from diverse formats and time to accurately predict future events. 
Through comprehensive benchmarking, we aim to establish a reliable framework for assessing the capabilities of LLM agents in forecasting international events, thereby contributing to the development of more accurate and trustworthy models for international relation analysis.\footnote{Our dataset is available on \href{https://drive.google.research.google.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents MIRAI, a benchmark designed to assess the performance of LLM agents in predicting international event relations. It emphasizes APIs to enable LLM agents to utilize different tools, a refined GDELT event database, and a dynamic data construction pipeline to ensure contamination-free test sets, aiming to provide a reliable standard for assessing the capabilities of LLM agents in forecasting international events.

### Strengths
•	Clarity and Structure: The paper is clearly written and easy to follow, which facilitates understanding and replicability.
•	Contamination-Free Test Sets: The focus on providing contamination-free test sets is a significant strength, ensuring unbiased performance evaluation. Regular updates to the test sets also add to its robustness and relevance over time, when newer models should be evaluated.
•	Insightful Visuals: Figure 2 offers a valuable overview of the distribution of relation types within the dataset.
•	Detailed Analysis: The authors provide an in-depth result analysis across diverse categories, such as action order and accuracy across different relation types

### Weaknesses
1.	Absence of Baseline Comparisons: As a benchmark paper, a comparison with simple (heuristic) baselines is critical to contextualize the agents performance in the MIRAI benchmark. The lack of such comparisons with simple baselines is a notable drawback, reducing the ability to assess the evaluated agents true effectiveness.  See suggestion 3).
2.	Focus Solely on Relation Prediction: The exclusive focus on relation forecasting seems narrow. Incorporating link prediction tasks (i.e., predicting specific subjects and objects for given queries) would align it better with existing TKG forecasting approaches and provide a more comprehensive benchmark. See question 1)
3.	Doubts in Experimental Setting when comparing to "traditional" models: 
o	The "traditional" models that you compare to are a bit old, which may not reflect current advancements in temporal knowledge graph forecasting. Inclusion of more recent models, such as TiRGN (Time-Guided Recurrent Graph Network with Local-Global Historical Patterns for Temporal Knowledge Graph Reasoning), would enhance the relevance of comparisons. 
o	I have some doubts about the evaluation on these models, see question 5. For example, why finetune it only until 2023-06, even though some agents have more recent cutoff-dates. 

1.	Integrate Human Performance in Main Paper: Including the presented human forecasting performance in the main paper (currently in Appendix G.4) would strengthen the benchmark's validation, given the strong performance of human evaluators on most metrics.  I strongly suggest to include the human study in main paper.
2.	Condense the Appendix: I suggest to potentially not include the full API specification and implementation, and README of the github repo, but instead a link to the github repo containing these. This could streamline the paper, allowing readers to focus on MIRAI's core contributions.
3.	Include a simple Baseline for Comparison: To provide a more meaningful comparison, I strongly suggest to include a simple/ heuristic baseline to compare the agents to. For example, a baseline that predicts the same relations as previously occurred, e.g. a modification from [1] to relation prediction. 
4.	References: AutoGPT Documentation: this should at least contain a date and a link.

### Questions
1.	Focus on Relation Forecasting: Why did the authors choose to focus solely on relation forecasting rather than including link prediction (predicting subjects and objects), which is more standard in TKG forecasting, and KG completion evaluation?
2.	Metric Selection: What motivated the choice of the current metrics, and why were more commonly reported metrics, like MRR and Hits@k, excluded?
3.	Dataset Update Commitment: The authors commit to updating the dataset split monthly. How long is this commitment expected to last, and will it be sustained indefinitely?
4.	Higher Thresholds for Test Data: What is the rationale behind applying higher thresholds to the test data (100 daily mentions, 5 news articles) than to the training data? 
5.	Clarification on the "traditional models" experiments: Section 3.2 3): 
o	What do you mean with "fine-tuned" in this case? Did you train the models on the provided GDELT event data? 
o	Assuming that with "fine-tune" you mean train: Why call it fine-tuned? 
o	Why do you fine-tune it only until 2023-6? considering that the query date is 2024-02, this is a very large gap. It seems also unfair, considering that e.g. for Llama-3.1-8B-Instruct the cutoff date is 2023-12. 
o	Do you apply RE-GCN in single-step or multi-step prediction mode, i.e. for predicting t, do you feed ground truth up until t-1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new LLM benchmark for short- and longterm forcasting international events, which is essentialy trying to predict relations between international parties. The general and fine-grained relations stem from an ontology, namely CAMEO. The authors define a think, act, oberserve loop, where the agent processes the query at hand and can give an answer right away, otherwise can act to get more information via coding and eventually observes the executed code. The benchmark equips agents to act by either single functions for data retrieval or code blocks for writing more complex code.

The results show that the task is challenging for LLMs by evaluating a set of baseline LLMs, where GPT-4o mini ends up performing the best. Next to the baseline LLMs, the authors also show the performance of fine-tuned methods from other benchmarks, underlining the benchmark is challenging. In addition, the authors run additional experiments and analyses, including observed generated code errors, boosting smaller architectures or investigating chosen action orders.

### Strengths
- Novel relation prediction task formulation (wrt other benchmarks) 
- Sensibe LLM system design, enabling the to query for information or to write own code, and defining an agent-based behavioural loop
- Sufficiently broad evaluation, including diverse analyses and also including baselines from other competing benchmarks
- Empirical results are promising

### Weaknesses
 - Unclear if, beyond the integrated fine-tuned approaches from other works, the results for LLMs are superior if compared to other task formulations such as QA. Since LLMs have been used there as well, the question remains open if other types of system components or prompts significantly worked better in the past

### Questions
- Did you also try a fine-tuned the baseline LLMs (given their are open-source)?
- Which competitor in the related work overview would be strongest compared to your approach?
- From the related work it becomes quite clear what the conceptual differences to prior LLM QA works are, but how much better does the new agent design actually work compared to more straightforward prior approaches?

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
This paper introduces MIRAI, a benchmark to test LLMs for events forecasting. The article provides a detailed description of the process for generating predictions from LLMs which are based on recently extracted news and geopolitical events. This is based on a strategy called ReAct that includes the three steps of thinking, acting, and observing. An ontology called CAMEO is used for the geopolitical events analysis. Extensive experiments have been performed to compare MIRAI to other approaches and strategies. Different Large Language Models have been used to evaluate their performance.

### Strengths
- The paper is well-written.
- Extensive experiments have been provided. These include comparing MIRAI process against other strategies and temporal reasoning 
  benchmarks and comparing base LLMs and smaller Language Models using MIRAI.
- The results of these experiments seem promising.

### Weaknesses
 - Only one concrete example is provided and discussed in the paper. More examples would facilitate a better understanding of the results.  For instance, examples that showcase different types of forecasting scenarios or that highlight the strengths of MIRAI could have been included.
- The work should have been also compared with RAG-based (Retrieval-Augmented generation) approaches. It is unclear how MIRAI's approach differs from RAG-based methods.
- Typos  line 088: ".. is able to better utilizes and benefits... " ->  ".. is able to better utilize and benefit... "

### Questions
How LLMs would perform if the news were used as a direct source instead of following the ReAct strategy?

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
4

### Summary
This paper introduces MIRAI, a practical benchmark designed to predict future interactions between two countries. It constructs a dataset based on news articles and existing information extraction and representation tools, and then exposes an API that allows an LLM agent to interact with the different data sources. The authors' extensive experiments provide valuable insights into how LLMs perform on this task.

### Strengths
S1. The paper provides the code and data. Besides, it comes with an extensive description of the data and code, ensuring reproducibility and reuse.

S2. The authors ran a lot of experiments testing different scenarios and configurations. They obtained very insightful and broad results about the task.

S3. The paper is well illustrated, with many examples showcasing the performance of the systems. It is also well-written and easy to follow.

### Weaknesses
W1. The paper heavily relies on the appendix (the paper is 73 pages long!). As a reviewer, I am not supposed to read it, but in many cases, I had to. For example, the previous work is mostly in the appendix (two small paragraphs are in the main paper) and the human evaluation is in the appendix. 

W2. The technical contribution of the paper could be clearer. The dataset construction pipeline is standard and relies on many existing tools with additional cleaning. The baselines are also coming from previous works.

W3. The scope of the task is very narrow: Predicting the future interaction between two countries.

Others/Typos

O1. Some figures are hard to read, especially in black and white (2, 4, 5, 7, 8)

O2. Human evaluation of the dataset is done in the appendix. Is it enough to only evaluate 51 events? Besides, 82% seems quite low to me.

O3. The authors include the confidence intervals but do not discuss them. In many cases, there are overlaps between the baseline, making the conclusions unclear.

O4. Adding the human evaluation in Table 2 is only one line, and it would be insightful.

O5. Having the RAG baseline would be very insightful in knowing if one needs the API interface.

T6. Line 420, problem citation (et al, 2024)

O7. Figure 8.b: In general, red is used to show incorrect things. Here, it is counter-intuitive.

### Questions
Q1. Are the news articles freely available? Are there copyright issues?

Q2. Line 260: Is balancing this way fair? Some months are naturally more active than others, and some relationships are more frequent than others.

Q3. How does the number of parameters in the LLM impact the performance? In Table 2, GPT-3.5-turbo has more parameters than the other baselines but is competitive with GPT-4o-mini, which the oldness of GPT-3.5 can explain.

Q4. For the Direct IO baseline, isn't a main issue outputting the output following the standard of the answer? Do you provide the possible relationships in any way?

### Soundness
3

### Presentation
3

### Contribution
3
