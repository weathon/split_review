# Can Models Help us Create Better Models? Evaluating LLMs as Data Scientists

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
We present a benchmark for large language models 
designed to tackle one of the most knowledge-intensive tasks in data science: writing
\textit{feature engineering} code, which requires domain knowledge in addition to a deep understanding of the underlying problem and data structure.
The model is provided with a dataset description in a prompt and asked to generate code transforming it. The evaluation score is derived from the improvement achieved by an XGBoost model fit on the modified
dataset compared to the original data. By an extensive evaluation of state-of-the-art models and comparison to well-established benchmarks, we demonstrate that the \bench{} of our proposal can cheaply and efficiently assess the broad capabilities of LLMs, in contrast to the existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an LLM benchmark that prompts the LLM writing feature engineering code for ML tasks and then run XGBoost with the obtained features to get a score.

### Strengths
This paper is overall clear and easy to understand.

### Weaknesses
It might be okay for the proposed benchmark to evaluate a specific coding aspect of LLMs, but I think this paper overclaims its generalbility to a large extent. Specifically, it claims it addresses limitations of existing benchmarks like MMLU and HumanEval, and reflects all fundamental aspects of intelligence. However, I feel the benchmark has significant limitations compared with what the paper claims.
* Narrow application scope: "Wrting feature engineering code" is just a single, specific use of LLMs. Also, it is not a highly frequent use of LLM users.
* Limited applicable LLMs: The proposed metric requires the LLM has both natural language and coding abilities, but this is not a must-have feature for a "strong LLM".
* This evaluation would prefer coding LLMs over really intelligent models. For example, in Table 1 of the paper, codestral-22B is even better than llama-3-405B under the proposed metric.
* I also have concerns on the flexibility of the metric and how challenge it is -- usually, the feature engineering of ML has just a handful of strategies, such as BPE tokenization for text data, one-hot for discrete labels, normalization for float number labels, etc.

### Questions
* Could you share any examples regarding the wrong decisions of mistral-7b for its low score?
* Is there any LLM-produced data processing strategies beyond what human engineers often use?

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
This paper introduces FeatEng, a new benchmark for testing large language models (LLMs) in feature engineering. The idea is pretty cool—they've set up a way for models to generate code that transforms data, making it more suitable for machine learning tasks. The key metric is whether the transformation improves the performance of an XGBoost model trained on the modified data compared to the original data. The authors emphasize that FeatEng aims to fix gaps in existing benchmarks by focusing on real-world tasks, like practical usefulness, integrating knowledge, handling complex skills, and being resistant to "gaming" the system. They ran various models through FeatEng and analyzed the results to see how well the benchmark captures what different models can and can’t do in this context.

### Strengths
+ Focusing on feature engineering is a fresh approach for LLMs, as this task demands both technical skill and domain knowledge. It’s a step away from standard code generation and into real-world data science workflows. Nice angle!

+ The benchmark is well-defined with solid metrics. Using an outcome-based metric (i.e., the performance improvement of a downstream model) is smart—it’s a straightforward way to check if the code is actually making things better. Also, the dataset selection is thorough, covering a variety of domains and types, which keeps it well-rounded.

+ The paper does a great job explaining the ideas behind each of their evaluation criteria. They walk readers through their motivations and outline the benchmark design clearly. It’s easy to follow and understand the reasoning behind why they chose each aspect of evaluation.

### Weaknesses
 - Even with diverse datasets, there's a possibility that models could end up overfitting to specific dataset types or common data science tasks, which could skew the results. If a model is already trained on similar data, it might appear more capable than it really is.

- The benchmark’s main evaluation metric depends entirely on XGBoost’s performance. While XGBoost is popular, it’s not the only ML model, and different feature engineering efforts might have varied effects on different types of models. A mix of evaluation algorithms could give a more rounded view.

- Running this benchmark might be resource-heavy, especially on larger datasets or complex transformations. It seems realistic but could be a bottleneck if someone wants to use FeatEng on many models at scale.

- Although they mention that a human baseline would be helpful, they don’t provide one here. Without it, it’s harder to tell how well these models are doing in comparison to actual human experts. Even a rough human baseline would make the results more relatable.

### Questions
+ How are you making sure that models aren’t just memorizing common feature engineering techniques? Any thought on including completely new datasets down the line to keep models on their toes?

+ What made you pick XGBoost as the benchmark’s only evaluation model? Wouldn’t including other models (like neural networks) give a broader view of the impact of the feature engineering?

+ Can you give more detail on how improvement is scored across different dataset types (like binary classification, multi-class, regression)? This would help make sure everything’s consistently fair.

### Soundness
3

### Presentation
3

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
This paper proposes a new benchmark, *FeatEng*, to evaluate the ability of large language models (LLMs) to perform feature engineering for tabular data. The benchmark focuses on a code generation task where the model is given a description of a dataset and tasked with generating code to transform the data to improve the performance of a machine learning model. The authors argue that existing LLM benchmarks often fail to capture the practical usability, domain knowledge, and complex skill integration required for real-world data science applications. They further demonstrate that *FeatEng* aligns well with these criteria and offers a more effective and efficient way to assess the capabilities of LLMs in this area.

### Strengths
This is a well-written benchmark paper with clear motivation.
1. Clear classification of existing benchmarks regarding philosophical traditions of pragmatism, functionalism, computationalism, and scientific realism.
2. Well-organized dataset from diverse, high-quality Kaggle competitions.
3. An interesting finding of the high correlation between FeatEng and Chatbot Arena.
4. A good viewpoint LLMs can tackle feature engineering and improve upon current AutoML systems by leveraging their potential to integrate domain knowledge and reasoning to generate efficient and interpretable features.

### Weaknesses
This paper has many weaknesses regarding its experiment design.

1. The result interpretation is limited:
    - Table 1: Mean FeatEng scores (Improvement) compared to Chatbot Arena ELO. Would it be better if we made a line plot for the comparison?
    - It would be helpful if more AutoML baselines [1,2] could be compared. Also, the best human results from the Kaggle competition can be included.
    - The only takeaway I can draw from this paper is that FeatEng can be a cost-effective substitution for Chatbot Arena in a way that it assesses the genuine technical capabilities of LLMs.
    - Another comparison that comes to my mind is how LLM's number of parameters can affect the benchmark results on FeatEng. We can show what will happen when the number of parameters scales for the same group of LLM (i.e., Claude-3-Haiku, Claude-3-Sonnet, Claude-3-Opus), which will give more insights into how to develop parameter-efficient LLMs.

2. Examples of the single-pass evaluation pipeline do not look good to me
    - The pipeline, as described, involves a single pass where the LLM generates code based on the input. How can this single-pass evaluation compare itself with AutoML, an iterative algorithm?
    - Figure 3 is not clear. A flow chart can be helpful.

3. Earlier works, such as [3, 4, 5], have explored much potential in LLMs for machine learning and AutoML tasks with iterative revisions. A detailed comparison and literature review would be helpful.

### Questions
Typos:
1. Line 019: asses $\rightarrow$ assess
2. Line 563, 567: duplicated entries of the same citation

Questions:
Should we include citations for XGBoost[1]?

[1] Chen, T., & Guestrin, C. (2016, August). XGBoost: A scalable tree-boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785-794).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper constructs a benchmark called FeatEng, which focuses on evaluating LLMs through the lenses of Pragmatism, Functionalism, Computationalism, and Scientific Realism.

### Strengths
In general, the paper is easy to follow, with clear presentations in the figures and tables.

### Weaknesses
 **Summary: hard-to-justify claims, and lack of concrete experiments or showcase**
1. Limited literature works:
  - In Section 1.1, the authors mention many problems with existing benchmarks and explain why they do not fit the "four characteristics" that the authors abstract as essential for evaluating intelligent systems. However, in my view, many of the benchmarks mentioned are commonly used and well-recognized for testing base LLMs. They may be crucial for assessing specific capabilities of pre-trained base models.
  - In contrast, this paper seems more like it is evaluating a benchmark for post-trained LLMs, which makes such a comparison seem unfair from this perspective.
2. Moreover, the discussion in section 1.1 feels rather vague and lacks specific experimental evidence or concrete examples to support the claims about existing benchmarks. The authors should consider providing more detailed comparisons or results that highlight their benchmarks' advantages over others. At the same time, I wonder if the authors have considered that many concurrent works are also testing models in complex, knowledge-intensive scenarios, evaluating whether the models can perform well in real-world tasks that require extensive knowledge. I am not sure if feateng can compare against these benchmarks and highlight its advantages?
3. The paper (excluding the appendix) only presents one table to display the results. I do not think this is enough to fully demonstrate the characteristics of the dataset. Additionally, the so-called "strong correlation" to chatbot ELO scores does not seem clearly reflected in this table. I think such claim need quantitative values to demonstrate, rather than a vague statement. Without more specific experimental results or showcase examples, the claims remain unsubstantiated and less convincing.

### Questions
The textual description in Sec 3.1 still seems insufficiently structured and process-oriented. I wonder if the **100 work hours** mentioned by the authors included a clear workflow? This seems crucial for evaluating whether the data collection process is reasonable, and whether it aligns with the four criteria proposed by the authors.

For example:

- How did you collect the source dataset? Based on what principles can a Kaggle dataset be used for feateng?
- As Kaggle is a high-quality data science forum, I strongly believe that it has already been used in some LLM training corpora. Therefore, have you fully considered the possibility of data contamination?

### Soundness
2

### Presentation
3

### Contribution
2
