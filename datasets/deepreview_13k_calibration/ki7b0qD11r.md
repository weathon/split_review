# BenTo: Benchmark Reduction with In-Context Transferability

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Evaluating large language models (LLMs) is costly: it requires the generation and examination of LLM outputs on a large-scale benchmark of various tasks. 
  This paper investigates how to efficiently reduce the tasks used to benchmark LLMs without affecting the evaluation quality. 
  Our study reveals that task transferability and relevance provide critical information to identify the most representative subset of tasks via optimizing a facility location function.
  We propose a practically efficient metric for estimating the transferability between two tasks via in-context learning (ICL). 
  By analyzing the pairwise transferability, we can reduce tasks in a modern LLM benchmark (e.g., MMLU or FLAN) to 5\% while inducing only a $<4$\% difference to the evaluation on the original benchmark. 
  Compared to prior works, our method is training-free, gradient-free, and highly efficient requiring ICL only. \looseness-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of evaluating large language models (LLMs) efficiently by proposing a method to reduce the size of LLM benchmarks without compromising the quality of evaluation. Traditional benchmarking approaches are costly and resource-intensive due to the large number of tasks included to cover various LLM capabilities. The authors introduce In-Context Transferability (ICT) as a training-free method to estimate task transferability by leveraging in-context learning, allowing them to assess which tasks are likely to improve performance on others. Using ICT, they propose Benchmark Task Reduction (BENTO), which formulates the task selection as a facility location problem to select a representative subset of tasks. Experiments show that BENTO can reduce benchmark tasks by up to 95% while maintaining consistent evaluation results, offering a cost-effective solution for LLM benchmarking.

### Strengths
1.By reducing the benchmark to just 5% of its original size without sacrificing evaluation quality, BENTO significantly lowers the computational and financial burden of LLM evaluation.

2.The paper’s novel use of in-context learning for transferability estimation provides a scalable, training-free solution for task reduction, making it more practical than traditional methods that rely on finetuning.

3.The ICT and BENTO methods can be applied to various LLM research and evaluation scenarios, potentially benefiting a wide range of applications beyond just benchmarking.

### Weaknesses
1.The reliance on in-context learning may limit the generalizability of the approach, as it assumes that in-context performance accurately reflects task transferability, which may not hold true across all tasks or models, especially for weak LLMs. More experiments for weak LLMs should be added. Specifically, the method's reliance on the quality of in-context examples is a concern. If the in-context examples are not representative or are poorly constructed, the estimated transferability could be skewed, leading to a suboptimal task selection. This is particularly concerning for tasks that require complex reasoning or domain-specific knowledge, where the in-context examples may not fully capture the task's nuances.

2.Although the paper demonstrates consistency with reduced benchmarks on certain datasets, additional testing across more diverse tasks and benchmarks could strengthen the validity of the results. Reducing a benchmark to a small subset of tasks may overlook nuanced skills or specific task requirements that LLMs need to perform well in specialized applications, potentially leading to incomplete evaluations in some cases. For instance, if the reduced benchmark primarily focuses on tasks requiring language understanding, it might not adequately assess skills related to code generation or mathematical reasoning, which are crucial for certain LLM applications. The paper should also consider the potential for bias in the task selection process, where the selected tasks might inadvertently favor certain types of models or skills, leading to an incomplete evaluation.

3.It is necessary to analyze if the reduced benchmark would cause the hurt of robustness for benchmark leakage issue or overfitting to few dimensions. The reduced benchmark, by its nature, exposes the model to a smaller set of tasks, which could potentially lead to overfitting on these specific tasks. This is particularly concerning if the reduced benchmark is used repeatedly for model development and evaluation, as the model might start to memorize the solutions for these specific tasks rather than learning generalizable skills. Additionally, the paper should address the potential for benchmark leakage, where the model might have been trained on data that is similar to the reduced benchmark, leading to inflated performance scores that do not reflect true generalization capabilities.

### Questions
Please refer to weaknesses

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
The paper presents a novel approach for improving the efficiency of benchmark evaluation in machine learning. The authors propose a method for reducing the number of tasks needed for comprehensive benchmarking by leveraging in-context transferability. This involves identifying and selecting a subset of tasks that can effectively represent a broader set of benchmarks while minimizing redundancy.
(1)	Analyzing the transferability between tasks from the perspective of in-context learning
(2)	The experiments on MMLU and FLAN show that the method proposed by the author can approximate the full performance with 5% of the data.

### Strengths
-	Analyzing task transferability from the perspective of ICL presents a novel approach.
-	The method does not require fine-tuning using existing evaluation data; it only needs to conduct ICL transferability tests on some models, which enhances the scalability of the approach.
-	The experimental results demonstrate greater effectiveness compared to selection methods such as random sampling or BM25.

### Weaknesses
-	The method raises concerns about its computational efficiency, particularly regarding the actual sizes of the in-context learning (ICL) test samples. For the ICL transfer tests from task i to task j, what are the sizes of the test samples n_j? Given that the transfer tests from i to j involve N^2 tests (where N is the total number of tasks), the total number of test samples conducted amounts to N^2 \times n_j \times M. Taking MMLU as an example, with N=57, if n_j \times M is only 50 (considering M=10 in appendix B), the total number of tests already reaches 160k, which extremely exceeds the complete MMLU dataset of 12k. This raises a significant concern: if the process of determining the reduced benchmark set requires conducting ICL tests on a scale that surpasses the size of the full dataset, then the practicality of the proposed method for reducing benchmark evaluation is questionable. Extensive ICL testing suggests that the model has been evaluated on a full dataset, which contradicts the authors' motivation for efficiently reducing the test set size.

-	The method heavily relies on the careful selection of the parameter k, representing the number of tasks to be selected for the reduced benchmark. In real scenarios without prior knowledge, determining the appropriate value for k is a significant challenge. The paper does not provide a clear methodology for selecting k, which could limit the method's usability in practical applications where such prior knowledge may not be available. The performance of the method is likely sensitive to the choice of k, and an inappropriate selection could lead to a reduced benchmark that does not accurately reflect the performance across the full set of tasks.

-	The approach is currently limited to task-level improvements and does not address example-level enhancements. This limitation may restrict the method's applicability across existing benchmarks, particularly in cases where there are a small number of categories but a large number of examples, such as MATH. Also, the subtasks of dataset FLAN used by the authors, such as ReCoRD and SQuADv2, where the number of examples exceeds 10k, does this indicate a lack of usability for the method? It is unclear how the proposed method would be applied to reduce the number of examples within each task, which is crucial for datasets with a large number of examples per task.

-	The authors only used 9 models for evaluation, raising concerns about whether the method would still perform consistently across more models. For example, LLaMA2-72B, Qwen2-7B, Qwen2-13B, etc. The transferability matrix derived from a limited set of models may not generalize well to other models with different architectures or training paradigms. This is particularly important as the field of machine learning is rapidly evolving, and new models with significantly different characteristics are constantly being developed.

### Questions
Q1: Will the difference in ICL capabilities of different models lead to bias in the evaluation?
The authors utilize two models (LLaMA 7 b and 13b). However, it is unclear whether their ICL performance is consistent across these models. Additionally, the methodology for integrating data from these models is not specified—do you simply average the results?

Q2: In the author's experimental setup for FLAN's 66 tasks, 100 questions were selected for each task to be considered as "whole benchmark"(Line 274-275). Does this simplification ensure the validity of the experimental results since FLAN contains 700k+ samples?

Q3: The NRMSE is used to compare the performance differences among methods. If the values were to be expressed in terms of absolute accuracy, what would the corresponding values for the other methods be? (Similar to the data presented in Table 1)

Typo: The letter "Q" in Appendix B experiment details has not been defined.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BENTO for reducing LLMs evaluation benchmarks by selecting representative tasks based on a new metric, In-Context Transferability (ICT), which estimates task similarity without additional training, reducing the computational cost.

### Strengths
1.  The BENTO method effectively reduces the number of benchmark tasks to approximately 5% of the original set with minimal impact (<4%) on evaluation accuracy, making LLM evaluation more cost-effective.
2. The proposed ICT metric enables efficient estimation of task similarity without requiring model training or fine-tuning, which lowers resource demands.
3. BENTO demonstrates reliable performance across various LLM benchmarks, indicating its potential applicability to diverse datasets and tasks.

### Weaknesses
1.  Currently, LLM benchmarks are highly vulnerable to contamination, which diminishes their reliability and credibility. The proposed BENTO method could exacerbate this issue, potentially causing LLMs to focus on a narrower range of tasks, thereby increasing the risk of contamination.
2. It would be valuable to see results on more advanced models, such as Gemini or GPT-4o, to assess the generalizability and scalability of the approach.
3. ICL results can be quite variable. It would be informative to evaluate ICL performance across different models and model sizes.
4. Since ICL requires additional sampling iterations, it would be helpful to provide the associated computation costs for reference.

### Questions
N.A

### Soundness
2

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
This paper introduces BENTO, a method designed to efficiently minimize the number of tasks in large language model (LLM) benchmarks while preserving evaluation quality. The core ideas include:
1. In-Context Transferability (ICT): A training-free approach to estimate transferability between task pairs in an LLM benchmark using in-context learning.
2. BENTO: This method formulates task selection as a facility location problem, utilizing task similarities derived from ICT. BENTO identifies the most representative subset of tasks to approximate the evaluation of the complete benchmark.
3. Experiments: Compared to the random selection baseline, BENTO achieves higher evaluation accuracy. It can reduce MMLU and FLAN benchmarks to  5% of the original task, enhancing the LLM evaluation efficiency.

### Strengths
1. The paper addresses an intriguing research question concerning the redundancy of data in benchmarks.
2. The use of in-context learning to estimate task transferability is effective.
3. The paper is well-written and easy to comprehend.

### Weaknesses
1. Potential Overfitting: Evaluating with a smaller sample size poses a risk of overfitting. It is challenging to ensure that the evaluation data in the benchmark is not used in supervised fine-tuning. Reducing the scale of evaluation data likely increases the chances of data contamination bias. The paper does not simulate or analyze this scenario. This is particularly concerning because the method relies on selecting a small subset of tasks, which could lead to the model being optimized for this specific subset rather than generalizing well to the broader task distribution. The paper needs to address how the selected tasks represent the overall benchmark and how the method mitigates the risk of overfitting to a small subset of tasks.
2. Greater Significance for SFT data: This method may be more beneficial for deduplicating training data than for selecting benchmark data. Training typically involves multiple iterations and back-propagation, which entail higher costs and thus require deduplication. The computational savings from reducing training data are likely much more significant than reducing evaluation data. The paper should explore the potential benefits of using this method for training data selection or deduplication.
3. Practicality of BENTO for Evaluation Data Reduction: I do not think using BENTO to remove evaluation data as a practical approach. Instead, I view BENTO as a metric for assessing benchmark quality rather than eliminating 95% of existing benchmark data. The paper does not adequately justify why reducing the evaluation data is a practical goal, especially given the potential for overfitting and the relatively low computational cost of evaluating on existing benchmarks.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
