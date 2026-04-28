# HELMET: How to Evaluate Long-context Models Effectively and Thoroughly

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
There have been 
   many benchmarks for evaluating long-context language models (LCLMs), but developers often rely on synthetic tasks like needle-in-a-haystack (NIAH) or arbitrary subsets of tasks.
It remains unclear whether they translate to the diverse downstream applications of LCLMs, and the inconsistency further complicates model comparison. 
    We investigate the underlying reasons behind current practices    
    and find that existing benchmarks often provide noisy signals due to low coverage of applications, insufficient lengths, unreliable metrics, and incompatibility with base models. 
    In this work, we present \oursfull, a comprehensive benchmark encompassing seven diverse, application-centric categories. 
    We also address many issues in previous benchmarks by adding
    controllable lengths up to 128k tokens,
    model-based evaluation for reliable metrics,
    and few-shot prompting for robustly evaluating base models. 
    Consequently, we demonstrate that \ours{} offers more reliable and consistent rankings of frontier LCLMs. 
    Through a comprehensive study of 51 LCLMs, we find that
    (1)~synthetic  tasks like NIAH are not good predictors of downstream  performance;
    (2)~the diverse categories in \ours{} exhibit distinct trends and low correlation with each other; and
    (3)~while most LCLMs achieve perfect NIAH scores,  
    open-source models significantly lag behind closed ones when the task requires
    full-context reasoning or following complex instructions---the gap widens with increased lengths.
    Finally, we recommend using our  RAG tasks for fast model development, as they are easy to run and more predictive of other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper constructs a comprehensive benchmark to test LLMs' long context abilities. It covers various types of tasks such as RAG, ICL, LongQA, Retrieval, Re-rank and so on.  The used prompts and evaluation metrics and carefully designed to ensure both IFT models and base models can give predictions. This benchmark also evaluates most commonly recognized LLMs and accordingly provides insights about LLMs' long context performance.

### Strengths
1: The benchmark is comprehensive. It covers most real-world long context use cases.

2: The investigation of performance correlation among all task types are insightful. It provides a new perspective to understand LLMs' long context ability.

3: The improvement to prompting strategy and evaluation method effectively stabilizes the evaluation results.

### Weaknesses
1: The so called "expected" ranking of LLMs is a bit subjective. 

2: Lack of some deep analysis to interesting results, such as why the json-kv task has higher correlation with re-rank than RAG or LongQA

3: The RoPE scaling settings are not suitable for 128k/64k testing. With ABF, usually, the scaling factor should be at least 2x the target extension ratio. With 8k context, Llama3 should use at least a scaling factor of 32 for 128k testing.

### Questions
1: Figure 2 is missing? 

2: What is the value for 'depth' in Figure 11? From top to the bottom, is the key information located at the beginning of the context to the tail of the context? 

3: Gemma series have a unique attention head dimension of 256 rather than 128. It might have interesting impact on the long context things. It would be better to have results with Gemma series as the tested models.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new benchmark called HELMET, which is designed to comprehensively evaluate the performance of long-context language models (LCLMs). Current LCLM evaluations largely rely on synthetic tasks, like Needle-in-a-Haystack (NIAH), or arbitrary subsets of some datasets. However, these methods present issues such as high noise, insufficient coverage of downstream applications, inadequate dataset lengths, and unreliable metrics. HELMET aims to address these shortcomings by expanding task diversity across seven application-centric categories (including long-document QA, citation-based generation, etc.), supporting controllable input lengths up to 128k tokens, and implementing model-based evaluations for more reliable results. Through testing 51 LCLMs, this study finds that synthetic tasks are poor predictors of downstream performance, open-source models fall behind closed-source models on complex long-context tasks, and there is low correlation among task categories, highlighting the need for multi-dimensional LCLM evaluation .

### Strengths
1.	**Diverse Task Design**: HELMET includes seven categories of tasks, enhancing the representativeness of LCLMs in real applications.

2.	**Support for Ultra-Long Inputs**: This benchmark accommodates input lengths over 128k tokens, making it suitable for evaluating the long-context capabilities of frontier models.

3.	**Reliable Model-Based Evaluation**: HELMET’s evaluation metrics reflect human judgment better than traditional n-gram matching, offering more reliable model ranking.

4.	**Compatibility with Base Models**: The benchmark allows evaluations of base models that haven’t undergone instruction fine-tuning, broadening LCLM applicability.

### Weaknesses
1.	**High Complexity**: With multiple tasks and model comparisons involved, HELMET’s setup and evaluation process is intricate and demands considerable effort from researchers. The sheer number of tasks, each with its own data preprocessing, input formatting, and evaluation scripts, creates a significant barrier to entry for researchers wanting to use the benchmark. This complexity extends beyond just the initial setup; it also impacts the debugging and analysis phases, as pinpointing issues across so many different tasks can be challenging. Furthermore, the need to manage and track results across seven different categories adds to the logistical overhead.

2.	**Low Correlation Among Some Tasks**: The low correlation between different tasks may make it challenging to assess a model’s overall long-context handling ability if it performs exceptionally in only certain tasks. This lack of correlation raises questions about the benchmark's ability to provide a unified view of long-context capabilities. For instance, a model might excel at long-document question answering but perform poorly on citation-based generation, making it difficult to draw general conclusions about its overall long-context proficiency. The lack of a clear, overarching metric that synthesizes performance across all tasks makes it hard to determine which models are truly superior.

3. **High Resource Consumption**: Running the full suite of HELMET tasks is time-intensive. It would be beneficial to identify a few key subtasks that can maintain consistency with the results of full testing, allowing for time-saving evaluations. The computational demands of evaluating models on such long contexts, especially when considering the number of models and tasks involved, are substantial. This high resource consumption limits accessibility to researchers with limited computational resources and also hinders rapid experimentation and iteration.

### Questions
Please address the weaknesses in the previous section.

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
The paper presents HELMET, a benchmark for evaluating long-context language models (LCLMs) that try to address limitations in existing evaluations, which often rely on synthetic tasks lacking real-world applicability. HELMET includes 7 diverse, application-centric tasks and supports input lengths up to 128k tokens. Through evaluating 51 LCLMs, the authors demonstrate that synthetic tasks are poor predictors of downstream performance, different task categories exhibit distinct trends, and open-source models significantly lag behind closed-source models on complex tasks requiring reasoning over long contexts. They advocate for holistic evaluation across diverse tasks to gain a comprehensive understanding of LCLM capabilities.

### Strengths
* The paper attempts to provide a standardized, holistic benchmark for LCLMs, whose adoption can potentially improve consistency and reliability in model evaluation and comparison.
* The evaluation is extensive -- 51 LCLMs across multiple dimensions, tasks, input lengths, and model types (open-, closed-source)
* The paper provide some valuable findings and insights into the performance of LCLMs, e.g. the limitations of synthetic tasks as predictors of real-world performance and where the performance gaps are between open- and closed-source models. This can guide future research and model development.

### Weaknesses
 * The authors observe that on existing benchmarks like RULER and ∞BENCH, smaller models (e.g., Llama-8B) sometimes outperform larger ones (e.g., Gemini Pro, Llama-70B), and they conclude that these benchmarks are unreliable because they do not reflect human expectations that larger models should perform better. This reasoning may be premature and somewhat biased. It's possible that the larger models genuinely underperform on these benchmarks due to specific issues, such as overfitting, architectural limitations, or difficulties in handling certain tasks. The benchmarks might be accurately capturing these performance discrepancies. Dismissing unexpected results as benchmark unreliability without thoroughly investigating the underlying causes undermines the validity of the authors' argument. More analysis considering both the possibility of model issues and benchmark limitations would strengthen the conclusions.
* While the paper introduces model-based evaluation metrics using 4o to address the unreliability of traditional metrics like ROUGE, it provides limited details on how these metrics were validated against human judgments. Including more detailed results or analysis of human-model agreement would strengthen the validity of the evaluation methodology.
* Although the paper critiques existing benchmarks, it could offer more in-depth analysis demonstrating how HELMET improves over them in practice. Figure 1 seems to be the only place where a direct comparison is shown. Conducting more direct comparisons of model rankings or performance differences on HELMET and existing benchmarks and providing concrete evidence of HELMET's advantages would strengthen the paper's arguments.

### Questions
1. In your analysis, you conclude that existing benchmarks like RULER and ∞BENCH are unreliable because larger models sometimes perform worse than smaller ones, which contradicts human expectations. Could you elaborate on why you attribute these unexpected results to benchmark unreliability rather than potential issues with the larger models themselves? Did you investigate alternative explanations for the performance discrepancies?
2. Do you have any results from human evaluation that validates the model-based evaluation metrics? What were the human-model agreement rates? Were there any notable discrepancies between the human judgments and model-based evaluations?
3. Other than RAG, which types of tasks in HELMET are compatible with the base model without instruction following capabilities?

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
4

### Summary
The paper proposes HELMET, a benchmark designed to evaluate long-context language models across seven application-focused categories, addressing issues such as inadequate dataset length, noisy evaluation metrics, and inconsistencies in current benchmarks. Through empirical evaluation on 51 models, the authors argue that HELMET offers better differentiation among models compared to traditional synthetic tasks and demonstrates the inadequacy of simple benchmarks in predicting real-world performance.

### Strengths
- HELMET covers diverse tasks such as retrieval-augmented generation, passage re-ranking, and long-document QA, providing a comprehensive test bed for evaluating the full capabilities of long-context models.
- By introducing controllable length settings and using model-based metrics instead of n-gram matching, HELMET offers a better reflection of human judgments and real-world performance.
- The authors evaluate 51 models, providing valuable insights into how different architectures and model sizes handle long-context tasks.

### Weaknesses
 - While HELMET’s application-oriented tasks are extensive, they may not fully capture long-context models’ capabilities in highly specific domains like legal or medical texts, limiting its applicability in niche areas.
- The heavy reliance on closed models such as GPT-4 for comparison leaves open questions about the efficacy of HELMET in an entirely open-source setting, which may limit reproducibility for some researchers.

### Questions
- How well does HELMET handle variations in domain-specific tasks, such as medical or financial documents?
- Could open-source models trained on synthetic datasets achieve comparable results with additional tuning on HELMET's diverse tasks?

### Soundness
3

### Presentation
3

### Contribution
3
