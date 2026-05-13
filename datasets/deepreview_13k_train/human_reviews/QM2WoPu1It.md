# HelloBench: Evaluating Long Text Generation Capabilities of Large Language Models

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities in various tasks (e.g., long-context understanding), and many benchmarks have been proposed. However, we observe that long text generation capabilities are not well investigated. Therefore, we introduce the \underline{H}i\underline{e}rarchica\underline{l} \underline{Lo}ng Text Generation \underline{Bench}mark (\textbf{HelloBench}), a comprehensive, in-the-wild, and open-ended benchmark to evaluate LLMs' performance in generating long text. Based on Bloom's Taxonomy, HelloBench categorizes long text generation tasks into five subtasks: open-ended QA, summarization, chat, text completion, and heuristic text generation. Besides, we propose \underline{H}i\underline{e}rarchica\underline{l} \underline{Lo}ng Text \underline{Eval}uation (\textbf{HelloEval}), a human-aligned evaluation method that significantly reduces the time and effort required for human evaluation while maintaining a high correlation with human evaluation. 
We have conducted extensive experiments across around 30 mainstream LLMs and observed that the current LLMs lack long text generation capabilities. 
Specifically, first, regardless of whether the instructions include explicit or implicit length constraints, we observe that most LLMs cannot generate text that is longer than 4000 words. 
Second, we observe that while some LLMs can generate longer text, many issues exist (e.g., severe repetition and quality degradation).
Third, to demonstrate the effectiveness of HelloEval, we compare HelloEval with traditional metrics (e.g., ROUGE, BLEU, etc.) and LLM-as-a-Judge methods,
which show that HelloEval has the highest correlation with human evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents HelloBench, a comprehensive benchmark designed to assess the long text generation capabilities of large language models (LLMs). Additionally, the authors introduce HelloEval, an automatic evaluation method that leverages LLMs-as-a-Judge to efficiently evaluate checklist results associated with each long text generation task. Through extensive experimentation across approximately 30 mainstream LLMs, the work reveals significant limitations in the long text generation capabilities of these models, including an inability to generate text exceeding 4000 words.

### Strengths
HelloBench encompasses a diverse array of long text generation tasks, such as open-ended QA and summarization, thereby offering a holistic evaluation framework for assessing LLMs' long text generation capabilities. The proposed HelloEval methodology reduces the time and labor associated with human evaluation, while maintaining a strong correlation with human judgments. The authors conducted experiments across 30 mainstream LLMs, providing valuable insights into the current limitations of long text generation.

### Weaknesses
1) Omission of Prior Work: The paper fails to adequately acknowledge and compare its methodology with ProxyQA [1], a pioneering framework specifically designed for evaluating long-form text generation capabilities of LLMs. Both methodologies assess generated content indirectly through evaluators to ensure adherence to specific standards. However, ProxyQA employs a query-specific checklist known as proxy questions, while HelloBench uses a more general checklist, which can not adaptively provide query- and semantic-aware checklists. The motivations and insights of both approaches appear to align closely.

2) To provide valuable context, it would be beneficial to include a comparison with ProxyQA in Table 1. Additionally, an analysis of the correlation between the results of ProxyQA and those of the proposed HelloBench would significantly strengthen this paper. If this analysis demonstrates that HelloBench aligns well with ProxyQA while offering more challenging and representative tasks, it would enhance the credibility of the work. 

3) It appears that all the key components of HelloBench or HelloEval, such as the six levels of Bloom's Taxonomy, the concept of LLM-as-a-Judge, the checklist-based evaluation method, and the dataset collection approach, have already been proposed in existing works. Furthermore, the ProxyQA work has already investigated the long-text generation benchmark and evaluation method, which overlaps with the focus of this study. The novelty and contribution of the work are quite limited.

### Questions
Lack of Robustness Analysis: Beyond examining the correlation between Hellobench and human evaluation, it would be beneficial to conduct win rate analysis or similar experiments (CI test). This would help determine if the proposed method consistently produces reliable and firm judgments, as even top-performing LLMs or human evaluators can generate inconsistent evaluation results.

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
4

### Summary
This paper develops a new LLM evaluation benchmark, namely HelloBench, focusing on evaluating LLM’s long text generation capability, filling the missing piece in the current LLM evaluation landscape. HelloBench covers 5 tasks in 38 subcategories, totaling 647 examples, constructed by manual selection from the web and some existing benchmarks. It focuses on open-ended tasks and targets at generation over 1000 words. To evaluate LLMs, the authors further propose HelloEval, a checklist-based LLM-as-a-Judge method that shows positive correlation with human evaluation. Experiments on popular open-source and proprietary LLMs reveal their insufficiency in long text generation.

### Strengths
* The benchmark, HelloBench, presents a timely effort on evaluating long text generation for LLM evaluation.
* The evaluation method, HelloEval, provides an automatic way to evaluate LLMs, saving time and effort.
* The experiments are conducted over many popular LLMs, making the findings more reliable and convincing.
* The findings offer insights on the insufficiency of existing LLMs on long text generation capability.

### Weaknesses
While HelloEval shows the highest and significant correlation with human evaluation, its overall spearman correlation is just 0.32. It’s not high enough to assume that improvements on HelloEval indicate real gains on long text generation.

### Questions
1. What’s the licence of HelloBench? This becomes more important for evaluation benchmarks.
2. Is the correlation analysis for HelloEval based on the annotations from the preparation stage? If so, there may be a risk of overfitting since HelloEval adopts checklist weights derived from this stage?
3. How many annotations did you use for correlation analysis? Is the number large enough to reach a significant conclusion? 0.32 is not a very high correlation value. Please include a plot for HelloEval score and human annotation score: I assume this plot looks more like a cloud rather than a line, so as to remind the others of the risk of HelloEval.
4. In lines 363-364, the authors compared the HelloEval scores between QA/text completion and summarization/chat. Is the scores of different tasks directly comparable?
5. Please provide a detailed section explaining what the HelloEval score means. For example, what does an increase of 1 in HelloEval indicate? What quality gains could be considered as significant? Can we compare scores across sub-tasks?
6. In line 1021, the authors state “By doing so, we guarantee that the data are not leaked for
the reason that they are all test samples and that their quality remains relatively high.” This is not true: test data may already leaked to LLMs.

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
The paper proposes HelloBench, a benchmark for long text generation inspired by Bloom's taxonomy of cognitive abilities. Furthermore, it proposes HelloEval, a technique to quantitatively evaluate the performance of LLMs initially assessed as checklists. The authors propose training a linear regression model to adjust weights of different checks obtained by human judges to the overall evaluation score, and then use these trained weights when working with an LLM judge.

The authors evaluate a range of recent LLMs on HelloBench, proprietary and open-source, large and small. The evaluation elicited various insights like most LLMs tend to generate output at around 1000 tokens (even those with max_tokens of 16384 or more), text generation quality decreases with response length (especially going outside the usual length of 1000 tokens)

They also conducted a correlation analysis of the HelloEval comparing it to a series of traditional automated text generation metrics and found much stronger Spearman correlation and much lower p-value that all the other methods.

### Strengths
* a new long text generation evaluation benchmark HelloBench is proposed which contains multiple tasks inspired by Bloom taxonomy of cognitive abilities
* an evaluation technique is presented for obtaining numerical scores from qualitative checklist-based assessments. It shows superior correlation to human judgements that a series of traditional metrics
* a comprehensive study of a wide range of LLMs is conducted on HelloBench eliciting insights of model's struggles to generate high-quality outputs at higher lengths.

### Weaknesses
 * the Bloom's taxonomy sounds inspiring but the mapping of different dimensions to text generation tasks looks superficial and containing overlaps. "...we have selected the most
 suitable task for each cognitive level" - this is not obvious to me, needs justification / proof

### Questions
N/A

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces HelloBench, a benchmark designed to evaluate the long text generation capabilities of LLMs. It categorizes long text generation tasks into open-ended QA, summarization, chat, text completion, and heuristic text generation based on Bloom’s Taxonomy and proposes HelloEval, a human-design evaluation method. The authors conduct experiments on approximately 30 LLMs, revealing limitations in their long text generation capabilities.

### Strengths
1. The proposed benchmark is well-categorized and well-grounded.

2. The metric HelloEval is quite innovative and wisely designed. It is also intuitive that using human judgments to induce metric parameters can lead to better human alignment.

3. The experiments are thorough and yield useful findings.

### Weaknesses
1. I am not satisfied with the benchmark. While the benchmark is well-categorized, it is not large-scale and does not have good coverage. Its contribution is also very incremental. For example, regarding open-ended questions, the authors only collected 200 samples from a single source Quora. I believe there are existing human-collected benchmarks that are very large-scale. ELI5 is such a representative.

2. To the best of my knowledge, Quora does not allow the crawling of its data. The benchmark may cause policy violations.

3. The analysis of the results lacks depth. While the paper mentions limitations in the models' capabilities, it does not explore the underlying reasons for these limitations or suggest potential improvements.

4. The paper claims that current LLMs struggle with long text generation, but it does not adequately discuss the implications of these findings for the development of future models.

### Questions
See weaknesses, plus, does Quora allow data crawling?

### Soundness
3

### Presentation
3

### Contribution
2
