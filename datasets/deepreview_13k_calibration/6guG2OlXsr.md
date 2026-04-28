# MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Large Language Models (LLMs) have displayed massive improvements in reason- ing and decision-making skills and can hold natural conversations with users. Recently, many tool-use benchmark datasets have been proposed. However, existing datasets have the following limitations: (1). Insufficient evaluation scenarios (e.g., only cover limited tool-use scenes). (2). Extensive evaluation costs (e.g., GPT API costs). To address these limitations, in this work, we propose a multi-granularity tool-use benchmark for large language models called MTU-Bench. For the "multi-granularity" property, our MTU-Bench covers five tool usage scenes (i.e., single-turn and single-tool, single-turn and multiple-tool, multiple-turn and single-tool, multiple-turn and multiple-tool, and out-of-distribution tasks). Besides, all evaluation metrics of our MTU-Bench are based on the prediction results and the ground truth without using any GPT or human evaluation metrics. Moreover, our MTU-Bench is collected by transforming existing high-quality datasets to simulate real-world tool usage scenarios, and we also propose an instruction dataset called MTU-Instruct data to enhance the tool-use abilities of existing LLMs. Comprehensive experimental results demonstrate the effectiveness of our MTU-Bench.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a multi-granularity tool-use benchmark for large language models, called MTU-Bench.

The main contribution of this paper can be summarized as,

-  a novel automated data synthesis pipeline is designed to generate high-quality, fine-grained tool-use datasets from pre-existing task-oriented dialogue datasets.

- introduce MTU-Instruct and MTU-Eval.

Comprehensive experimental results demonstrate the effectiveness of the proposed MTU-Bench.

### Strengths
The strengths of this paper are summarized as follows,

- The proposed MTU-BENCH cover more tool-use scenes than previous datasets.

- The evaluation cost of MTU-BENCH is cheaper.

- The authors will open-source all relevant code and data, supporting further research in this field by the community.

### Weaknesses
 The questions, concerns and weaknesses of this paper are summarized as follows,

- In Section 2.1.1, during the Data Collection phase, the authors should provide a more detailed and comprehensive list of the specific criteria and standards used for dataset selection. It is unclear how the authors ensured the selected datasets were appropriate for fine-grained tool use, especially given the potential for variations in dialogue structure and intent representation across different datasets.

- There appear to be situations where multiple classification criteria, such as 'Information missing,' 'Information exists,' 'Information confirmed,' 'Aimless chatting,' and 'Specific API call,' could apply simultaneously. How should these cases be handled? The current description lacks clarity on how these potentially overlapping categories are disambiguated and assigned during the annotation process. This ambiguity could lead to inconsistencies in the dataset.

- Any visualization results with specific examples can be shown for Tool Clustering in Section 2.1.1? The lack of visual examples makes it difficult to assess the effectiveness of the clustering approach and understand how similar tools are grouped. Without concrete examples, it's hard to evaluate the quality of the tool clustering.

- Is data quality truly assured? Since the data is synthesized by GPT-4 and also validated by GPT-4, can the reliability of the synthetic data be guaranteed? There is a potential for confirmation bias when using the same model for both data generation and validation. This raises concerns about the robustness of the dataset.

- The overall presentation of Section 2.1.1 is not very strong, and many details are not clearly explained (such as quality filters and adjustments). The authors should refine this section thoroughly. The current description lacks sufficient detail regarding the specific quality filters and adjustments applied to the synthesized data, making it difficult to assess the rigor of the data cleaning process.

- The content in Section 2.1.2 does not fully align with what is presented in the introduction. The authors should add a reasonable comparison with previous datasets at an appropriate place in the paper. The connection between the claims in the introduction and the specific metrics presented in Section 2.1.2 is not clear. A more explicit comparison with existing datasets is needed to contextualize the contribution.

- Could the authors provide some experimental results that train other open-sourced LLM on MTU-BENCH?

### Questions
I have included the main questions in weaknesses box and the authors can response according to the comments there.

### Soundness
2

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
4

### Summary
This paper presents MTU-Bench, a benchmark designed to evaluate large language models (LLMs) in tool-use across diverse and complex dialogue settings, including single-turn, multi-turn, single-tool, and multi-tool tasks. MTU-Bench addresses limitations in existing benchmarks by incorporating automated, cost-effective metrics that do not require GPT-based evaluations. Key contributions include a large dataset of tool-use dialogues synthesized and validated with GPT-4, a detailed evaluation framework (MTU-Eval) with fine-grained metrics, and the introduction of MTU-LLaMA, a model fine-tuned for tool-use tasks that shows strong performance. This work provides a comprehensive benchmark that captures real-world complexities, supporting future advancements in tool-using LLMs.

### Strengths
MTU-Bench introduces a unique multi-granularity benchmark for tool-use in LLMs, covering single/multi-turn and single/multi-tool tasks, addressing limitations of prior benchmarks with a cost-effective, automated evaluation approach. It includes detailed metrics (e.g., tool and parameter selection accuracy, task process rate) that provide deep insights into model performance across diverse scenarios, adding rigor to the evaluation process.

### Weaknesses
1.The paper’s result analysis could be more comprehensive. While it presents performance comparisons across different models and scenarios, it lacks deeper exploration into the causes behind inconsistent model results, particularly in challenging multi-tool and multi-turn settings. A more granular investigation into factors such as specific error patterns, model architecture differences, or the influence of training data could provide actionable insights. This would help identify underlying reasons for performance variability and guide targeted improvements in model design and training strategies.

2.The paper does not indicate whether the experiments were conducted multiple times or if statistical confidence measures were applied to the results. Without multiple runs or confidence intervals, the stability and reliability of the reported results are uncertain, particularly in complex, multi-turn, multi-tool scenarios where model performance can vary significantly. This omission limits the ability to assess whether observed differences between models (e.g., GPT-4 vs. MTU-LLaMA) are statistically significant or simply due to random variation. Conducting multiple experimental runs and reporting average results with confidence intervals would strengthen the reliability of findings and clarify performance comparisons across different settings.

### Questions
1.You classified the types of model errors (such as operation errors, parameter errors, format errors), but did not delve into the specific reasons why the errors occurred or possible resolution strategies. Can the model's specific error patterns under different task complexity or tool combinations be further analyzed to help improve the model?

2.As a binary indicator, the success rate requires that the entire conversation is completely error-free to be successful, which may be too stringent for multi-round conversations. In practical applications, some small errors may not significantly affect the completion of the final task, especially in scenarios where users can tolerate partial mistakes. Such strict standards will cause the model to be marked as a failure due to small errors even at high performance, failing to reflect the overall effect of the model. Therefore, is it necessary to introduce a fault-tolerant mechanism for SR, such as allowing a small number of insignificant errors to exist?

3.SATS uses an exponential decay method to reduce the impact of early errors on subsequent rounds. While this decay mechanism captures the temporal location of errors, it may not be effective enough to cope with the impact of different types of errors. For example, some errors (such as parameter errors) may invalidate the entire conversation, while others (such as minor tool selection errors) have less impact on subsequent conversations. Is it possible to incorporate error type and severity into the decay function to get a more precise round success rate?

4.Current multi-round evaluation metrics do not differentiate between the type of error (e.g. tool selection error, parameter selection error, etc.) and severity. However, different error types have significantly different effects on dialogue. For example, parameter errors often have a greater impact than tool selection errors because parameter errors can lead to complete failure of the task. Therefore, should error type and severity be included in the assessment and given different weights, thereby improving the accuracy of the assessment?
5.In order to ensure the validity of the results in real applications, are there any plans to introduce a part of real human-labeled data and compare the performance difference of the model on real data and synthetic data?

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
This paper introduces MTU-Bench, a benchmark designed to evaluate large language models (LLMs) in terms of their ability to use tools across various scenarios. MTU-Bench addresses limitations in existing benchmarks by providing more comprehensive scenario coverage and reducing evaluation costs. It includes five distinct tool usage scenarios and relies on prediction results and ground truth for evaluation. The paper's key contributions include the MTU-Bench benchmark, the MTU-Instruct and MTU-Eval datasets, and the MTU-LLaMA model, which is fine-tuned to demonstrate strong tool-use capabilities. The experimental results highlight the benchmark's effectiveness in enhancing LLMs' tool-use skills.

### Strengths
Comprehensive Evaluation: The paper provides a thorough evaluation of both open-source and proprietary models using the newly proposed benchmark, covering a wide range of scenarios.

Detailed Experimental Setup: The experiments are well-designed and extensive, allowing for a clear comparison of LLMs' tool-use capabilities.

Improved Scenario Coverage: By incorporating multiple scenarios, including multi-turn and multi-tool settings, the benchmark offers a more nuanced evaluation of LLMs, which is a step forward from existing benchmarks.

Clarity and Structure: The paper is well-structured, making it easy to follow the methodology and understand the results.

### Weaknesses
Limited Novelty: While the benchmark offers more scenarios and finer-grained evaluations, it lacks a significant innovation or breakthrough that fundamentally advances the field. The paper needs to clearly articulate how these additions lead to new insights or directions in tool-use capabilities for LLMs.

Lack of Real-World Impact: The paper does not provide concrete examples or case studies demonstrating how the new benchmark can lead to improvements in real-world applications. For example, the introduction of the COCO dataset in the object detection field highlighted specific challenges that state-of-the-art methods at the time struggled with, such as detecting small objects, handling occlusions, and recognizing a wider variety of categories. This enabled researchers to evaluate and improve their models effectively. In contrast, MTU-Bench does not clearly show how it highlights current limitations of LLM tool-use or how it can similarly drive innovation in practical applications.

The paper notes that existing benchmarks lack sufficient evaluation scenarios. Your proposed benchmark seems to merely add a few extra scenarios—how does this impact tool usage? Are there fundamental differences between the new scenarios and the previous ones? Without strong experimental evidence, it may appear that you are simply expanding the dataset. If your goal is to build a comprehensive evaluation suite, it seems to lack a thorough analysis and discussion of its completeness.

Your paper claims that previous datasets were not based on real-world data, yet the dataset you present is constructed using GPT-4 and existing datasets, rather than data collected from actual application users. How do these data fundamentally differ from previous datasets in accurately reflecting real-world scenarios?

Although your dataset is more detailed and extensive than previous ones, it remains unclear which specific challenges it addresses. Could combining existing evaluation datasets achieve similar results? What unique value does your benchmark provide that makes it indispensable for evaluating tool usage?

### Questions
The paper notes that existing benchmarks lack sufficient evaluation scenarios. Your proposed benchmark seems to merely add a few extra scenarios—how does this impact tool usage? Are there fundamental differences between the new scenarios and the previous ones? Without strong experimental evidence, it may appear that you are simply expanding the dataset. If your goal is to build a comprehensive evaluation suite, it seems to lack a thorough analysis and discussion of its completeness.

Your paper claims that previous datasets were not based on real-world data, yet the dataset you present is constructed using GPT-4 and existing datasets, rather than data collected from actual application users. How do these data fundamentally differ from previous datasets in accurately reflecting real-world scenarios?

Although your dataset is more detailed and extensive than previous ones, it remains unclear which specific challenges it addresses. Could combining existing evaluation datasets achieve similar results? What unique value does your benchmark provide that makes it indispensable for evaluating tool usage?

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
5

### Summary
This paper proposes MTU-Bench, a benchmark dataset for evaluating the ability of a large language model(LLM) to invoke tools in multiple scenarios. MTU-Bench provides a more granular and detailed approach compared to previous studies in this domain by considering two key dimensions: (1) the number of tools that can be invoked within a conversation and (2) the number of rounds of tool call involved in multi-turn dialogues. Moreover, the construction pipeline for the MTU-Bench dataset is novel and carefully designed. It begins by collecting tasks from traditional conversation datasets, and these datasets are then transformed through a synthesis process into tool-oriented conversations, simulating realistic tool usage. This innovative approach serves as a scalable paradigm for expanding both the variety of tools and the diversity of conversations available for research. In addition, the paper proposes MTU-Eval, an automated evaluation framework that does not require an external LLM, which reduces the cost of evaluation to a large extent. Finally, the MTU-Instruct dataset is introduced for fine-tuning the tool-usage capabilities of the model, demonstrating the excellent performance of the fine-tuned model in a variety of complex tasks.

### Strengths
1. Originality: MTU-Bench introduces a multi-granularity evaluation framework, considering the number of tools invoked and the number of turns required for interaction. This multi-granularity framework captures a variety of real-world interactions that are often overlooked in existing benchmarks. The construction of this benchmark employs a unique synthesis pipeline by transforming task-oriented dialogue datasets into tool-usage datasets.

2. Quality: The paper evaluates multiple LLMs (both open-source and closed-source) across a range of scenarios, including multi-tool, multi-turn, and out-of-distribution (OOD) tasks, ensuring robustness and completeness in the experimental validation.

3. Clarity: The paper follows a clear narrative, starting with motivation and problem formulation, followed by methodology, experiments, and detailed discussions on results, which makes it easy for readers to follow the flow of ideas.

4. Significance: The paradigm of transforming existing dialogue datasets into tool-use datasets opens new possibilities for exploring the tool-use ability of LLMs. The automated evaluation framework MTU-Eval significantly reduces the cost and complexity of benchmarking LLMs

### Weaknesses
1. Unable to cover complex tool-calling scenarios: The idea of the paper is to convert the dialogue into a function call dataset, which is an interesting and extendable idea. However, this also introduces a bottleneck that the dataset may not cover too much complex queries that request the agent to perform more than 5 steps to finish (the paper also states that only an average of 2 calls per turn in the dataset). While the dataset includes some multi-step interactions, the limitation on the average number of calls per turn suggests a potential lack of depth in complex, sequential tool usage scenarios. This could limit the ability of the benchmark to evaluate models on tasks requiring intricate planning and execution across multiple tools and turns.

2. Limitations of Virtual APIs: MTU-Bench generates all tools based on traditional conversation data, resulting in all APIs being fictitious. This approach may make LLM behave severely differently from when it calls real-world API, for example, if the model generates a wrong call in an executable env, it has the possibility to recover from its mistakes. (However, the reviewer does not expect this problem to be solved in this setting, but it would be good if the author could propose some nice practical thoughts to that)

3. Insufficiently Designed Evaluation Metrics: SATS and TPR overly emphasize the position of the first error, failing to adequately consider the LLM's ability to handle early mistakes. For example, if an LLM can disregard an early error and correctly execute subsequent tasks, it demonstrates robustness that the current metric does not capture. The metrics seem to penalize models heavily for initial errors, even if those errors are later corrected or do not prevent successful task completion. This could lead to an underestimation of a model's true capabilities in real-world scenarios where error recovery is crucial.

### Questions
1.How to calculate the Parameter Selection Accuracy in single-turn scenarios? Specifically, is it determined solely by whether the LLM's output matches the ground truth exactly? There are instances where the parameters provided by the LLM might convey the same meaning as the ground truth but differ in specific characters or formatting. Would a more nuanced approach to assessing parameter selection accuracy be beneficial? Do you use the same way of defining correctness in multi-turn scenarios?

2. Since the tools called in MTU-Bench are all synthetic and do not use the real-world API, do you have any experiments that show that the metrics used in the paper are consistent across models when applying datasets built from real-world API calls?

3. In tool creation, how do you make sure that the tools you create make sense? Besides, since the tools are merged in the latter stage, how can you guarantee that the tool provided can fit the request by the current turn? 

4. Most API doc are generated from GPT-4, which indicates that the distribution of API docs possibly falls into the distribution into the GPT4 capability distribution, how to overcome such bias?

5. Limited discussion of current tool-calling benchmarks
[1] T-Eval: Evaluating the Tool Utilization Capability of Large Language Models Step by Step, ACL 2024
[2] GTA: A Benchmark for General Tool Agents, NeurIPS 2024

6. Considering that this is a benchmark paper, the authors are highly suggested to provide the dataset data in the supple files, which allows the reviewer to have a glance at the quantity of the dataset in person, which is different from the dedicated demos selected in the supplementary. 

7. The author shows the performance gain on the MTU-Eval, however, it is actually an in-domain SFT. What is the performance gain on another tool benchmark?

### Soundness
2

### Presentation
3

### Contribution
3
