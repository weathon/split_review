# WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Recent advancements in large language models~(LLMs) have driven a revolutionary paradigm shift in process automation from Robotic Process Automation to Agentic Process Automation by automating the workflow orchestration procedure based on LLMs. 
However, existing LLMs (even the advanced OpenAI GPT-4o) are confined to achieving satisfactory capability in workflow orchestration. 
To address this limitation, we present \WholeTitle, a data-centric framework elaborately designed to enhance the capability of LLMs in workflow orchestration.
It first constructs a large-scale fine-tuning dataset \BenchTitle with \TotalNum samples, covering \APINum APIs from \APPNum applications across \CategoryNum categories.
Specifically, the construction process can be divided into three phases:
(1) Data Collection: we collect real-world workflow data from Apple Shortcuts and RoutineHub, transcribing them into Python-style code.
We further equip them with generated hierarchical thought via ChatGPT.
(2) Query Expansion: we prompt ChatGPT to generate more task queries to enrich the diversity and complexity of workflows.
(3) Workflow Generation: we leverage an annotator model trained on collected data to generate workflows for synthesized queries. Finally, we merge the synthetic samples that pass quality confirmation with the collected samples to obtain the \BenchTitle.
Based on \BenchTitle, we fine-tune Llama-3.1-8B to obtain \ModelName.
Our experiments show that \ModelName demonstrates a strong capacity to orchestrate complex workflows, while also achieving notable generalization performance on previously unseen APIs. Additionally, \BenchTitle exhibits robust zero-shot generalization capabilities on an out-of-distribution task planning dataset, T-Eval.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper argues that state-of-the-art models like GPT-4o face challenges in effectively handling complex workflows. To address this, the paper introduces WorkflowLLM, a data-centric framework designed to enhance the workflow orchestration capabilities of LLMs. Central to this framework is WorkflowBench, a large-scale fine-tuning dataset comprising 106,763 workflows, 1,503 APIs, and 83 applications across 28 categories. WorkflowBench is constructed through a three-phase pipeline: data collection from sources like RoutineHub, query expansion using ChatGPT to create diverse and complex workflows, and workflow generation leveraging a trained annotator model for high-quality workflow synthesis. The dataset is enriched with Python-style code, comments, and hierarchical thought structures to improve LLM learning.

Based on WorkflowBench, the paper fine-tunes Llama-3.1-8B, resulting in WorkflowLlama, which demonstrates superior performance compared to existing models, including GPT-4o, on workflow orchestration tasks. WorkflowLlama achieves notable success in generalization to unseen APIs and tasks, evaluated using metrics such as CodeBLEU and Pass Rate. Additionally, WorkflowBench exhibits robust zero-shot generalization on the T-Eval benchmark, achieving an F1 plan score of 77.5%.

### Strengths
S1)The observation and problems are interesting and relevant to the conference

S2) The dataset might have potential uses

S3)The experiments involve many systems

### Weaknesses
W1) The scientific or technical contributions are limited as the key contributions of paper are around data curation effort. And the significance of data size and quality  is not clear (see Q2).

W2) Section 3 mentions many steps to generate the needed data for its workflow using ChatGPT but the Quality control protocol is not very clear. Even the author provides some examples and algorithms in appendix, the details are very descriptive . Also section4.2  mentions using  human evaluator to re-label the sampled data,It’d be better to provide more details towards the quality control protocol for this human-driven process as well.

W3) Many technical details are not very clear (see questions)

W4) Code is provided in supplemental material but there is no document how to reproduce the experiment results ( also see Q3)

### Questions
Q1)The “pass rate” is an important metric to evaluate the performance in section 4.3. Could you elaborate more on how it is calculated? What are the reasons to choose it? And how is related to training/fine-tuning phases?

Q2)Could you  contextualize the size and the quality of the generated dataset   in terms of  how significant it is in comparison with SOTA or related works? Are they general enough for RPA for just for applications around Apple Shortcuts and RoutineHub?

Q3) The papers also mention about fine-tuning Worfflow Lalama and annotator in a very short paragraph in section. Could you elaborate more about setup, why such training parameters are chosen?

### Soundness
2

### Presentation
1

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
This paper proposes a framework that leverages LLMs to automate workflow orchestration. It extends the real world dataset by creating synthetic data through LLMs, to train the model. It conducts experiment study to compare the proposed framework with several proprietary and open source models, using CodeBLEU and Pass Rate as the metrics.

### Strengths
The paper is well-written and easy to follow. Examples are given to illustrate the important steps. 

The extended dataset improves the diversity and complexity of the samples in the training data, allowing the models to adapt to the situations that are closer to real-world applications. 

The experimental results show that the proposed framework outperformed the existing models by a large margin.

### Weaknesses
The paper mainly relies on prompting LLMs to generate the results of the key steps, such as data generation, commenting actions, and plan generating. It seems that there is a large space of prompt engineering to improve the performance but left to be undone. 

The proposed framework bypasses the API selection when handling the OOD setting by directly serving the required APIs as the input. This greatly simplifies the problem of automating workflow orchestration. 

The paper relies heavily on LLMs for the entire process, including generating the dataset, training the model, and evaluating the models (only less than 82% accuracy in a small sample with 330 instances in total). This weakens the technical contribution and the reliability of the experiment results.

### Questions
Are the prompts used in the framework that drive the LLMs usage automatically generated?  If yes, how to ensure the quality of the prompts? If not, how to scale up?

For each step from data generation to model evaluation, how to optimize the prompts?

The description on quality confirmation is a bit vague. The example given about the issues is not clear. How are such issues detected? How to prompt ChatGPT to refine A’ and P’, and how to ensure the quality of the refinement? How to perform the rule-based filtering, e.g., how to automatically detect if parameter constraints are violated or not?

For OOD settings, how are the other models evaluated? Do they also be given the same input like the one for Workflow Llamma, i.e., providing the list of required APIs? 

Given synthetic data takes the large portion of the final benchmark (91k out of 11k) but the quality is unsure, it would be interesting to also see how Workflow Llama performs on the real-word dataset, i.e., without the synthetic data, compared to other models? 

The proposed framework outperforms all the other models by an extremely large margin in the first four columns in Table 2 (such as 9.4% vs 0.5). This seems to be suspicious and needs further examination and explanation. 

In Table 2, both CodeBLEU and Pass Rate are used, one examines the similarity of code and one examines if the code is executable. It would be interesting to combine both of them, such as setting a threshold on the CodeBLEU score when checking the Pass Rate to compare models, since Pass Rate itself doesn’t necessarily indicate the success of the workflow orchestration.

### Soundness
2

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
3

### Summary
The paper presents a detailed explanation of the construction and evaluation of the WorkflowBench dataset, which contains many examples of workflow descriptions. The dataset is later used to fine-tune the open-source LLM Llama-3.1-8B.
The dataset creation follows a well-established and potentially reproducible approach. It starts with data gathering, expands to increase data diversity, and generates a final workflow dataset, enhancing real collected data with synthetic data.
The fine-tuning intends to overcome the limitations of existing LLMs in workflow orchestration and provide a consistent improvement in process automation by proposing an agentic approach.
The fine-tuned LLM called WorkflowLllama is detailed, and its capabilities are evaluated, showing a solid capacity to orchestrate complex workflows. Its performance was compared with commercial and open-source LLMs using the test set of Workflowbench.

### Strengths
The paper is well-presented and well-written overall. The authors identified a clear pain point in achieving an agentic LLM approach for process automation: lacking LLMs capable of correctly describing complex workflows. Although partially addressed by other works, as pointed out by the authors in the related work section (section 2), their approach is innovative in dealing with fairly more complex workflows than previous solutions.

Their approach to overcoming this limitation is sound and clever. They provide a fine-tuned LLM specialized to handle this kind of task.
To do so, they craft a well-defined dataset, and it is possible to highlight the process of dataset creation as one of the paper's main contributions, as crucial as the constructed dataset and the fine-tuned model.
After the data collection, the query expansion phase is especially interesting because it uses another LLM (e.g., ChatGPT) to help overcome the lack of diversity and complexity of the gathered initial data with syntactic data. The same applies to the clever use of ChatGPT in the evaluation phase.
Compared with other LLMs solving the same kind of problem, the presented results show the potential use of the author's solution to deal with the initial established problem, i.e., the automation of complex tasks.
WorkflowLlama outperforms other LLMs when the workflow demands generalization to unseen instructions and unknown APIs.

I also highlight the good approach to evaluating the effectiveness of the LLM-based evaluator (section 4.2), which strengthens the paper's arguments.

### Weaknesses
- The background on automation's relevance (lines 36-38) might be condensed, as automation's importance is widely recognized.
- In section 3.1, the author can better explain the $\mathcal{D}$. The other elements were presented before, but  $\mathcal{D}$ is directly introduced on line 248 without prior explanation.
- Lines 245-247 read (my emphasis):  "This bottom-up [...], efectively **ensuring content realiability** and **minimizing the risk of hallucination**". These are pretty strong assumptions without solid evidence, especially if generalized to every LLM. Do the authors know published papers that confirm them (since this paper is not about reducing hallucinations)? If not, the phrase can be removed or rephrased to be more humble.
- The paper lacks a clearer section on threats to validity. The authors provided some in Appendix E, but they should be incorporated into the main text.
- The paper also lacks a more evident running example/use case. Although the authors provide a small case study in section 4.7 and some examples in Appendix D, a consistent running example, incorporated throughout sections, could clarify the model's applications and emphasize practical use cases.

Minor issues:
- Line 52 mentions GPT-4, while the rest of the paper uses GPT-4o(-mini). Maybe it is only a typo, or the work mentioned indeed uses the GPT-4 model. Since they are different models, it can be good to double-check every reference to ensure it always talks about the correct model, maybe highlighting somewhere they are not the same.
- The size of Figure 2 can be increased to improve readability.
- Figures 3,5 and 6 could improve accessibility through higher contrast colors.
- Although well-written, the paper is sometimes repetitive (e.g., sections 1 and 3). Proofreading with this issue in mind may help the authors achieve a better final text.

### Questions
I am curious about the choice of ChatGPT to run both the query expansion phase of the dataset creation (section 3.2) and the experiments (sections 4.1 and 4.2). Altough I think it was a good idea, why rely on a proprietary model (the GPT-4o) with proprietary and non-disclosed prompt engineering behind it? Did the authors try to use directly the GPT-4o model? Did they try other models to run this phase? I assume that the "ease-of-use" of the ChatGPT is a fair point in favor of its use, but it should be evident in the paper.

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
This paper proposes a pipeline for constructing workflow (RPA) data to enhance LLMs' workflow orchestration capabilities. The core motivation stems from the observation that real-world workflows require more complex logic and longer sequences than what current LLMs can directly generate. The primary contribution is the construction of a dataset containing over 100K samples. The main limitations lie in the lack of certain technical details (such as specific ChatGPT versions used for annotation) and the lack of deeper investigation into model capability improvements.

### Strengths
1. Accurate and valuable problem identification. The paper identifies the limitations of existing work in handling real-world workflows: difficulty in processing long-sequence workflows with complex logical relationships like control flow. This observation directly addresses practical application pain points, making the motivation very solid.
2. Proposes a systematic data construction method. The paper designs a complete data synthesis process: from real data collection, workflow abstract representation, data synthesis to quality control, with detailed design considerations at each stage. The resulting large-scale dataset provides an important resource for this field.
3. Comprehensive experimental validation. The effectiveness of the method is strongly supported through multi-dimensional evaluation using CodeBLEU and Pass Rate, cross-domain testing with T-Eval, along with detailed case analysis and ablation studies.

### Weaknesses
1. Important technical details are missing. The paper mentions using ChatGPT for data annotation and optimization multiple times but doesn't specify the model version. For work with data construction as its core contribution, this seriously affects reproducibility and rigor. The lack of specific model versions, including the exact API calls and parameters used, makes it difficult to replicate the data generation process. Furthermore, the prompt engineering strategies used with ChatGPT are not detailed, which is crucial for understanding the quality and biases potentially introduced during the annotation process.
2. Lacks methodological innovation and mechanism analysis. Although data construction is an important contribution, the paper lacks in-depth analysis of how this data enhances model capabilities. Specifically, it doesn't investigate whether the improvements come from enhanced logical reasoning abilities or simply better format matching. Without such analysis, it's difficult to determine if the model has truly learned to reason about complex workflows or has merely memorized patterns from the training data. The paper should include an analysis of the types of errors made by the model before and after training on the synthesized data to understand the specific improvements.
3. Missing critical ablation experiments. The paper doesn't compare the performance difference between the Annotator Model and WorkflowLLM, despite both models using the same training method and data type. This results in questioning the necessity of the data synthesis strategy and weakens the core argument. Without a direct comparison, it's unclear if the improvements are due to the data synthesis process or simply the model architecture. A controlled ablation study is needed to isolate the impact of the synthetic data.
4. The paper mentions that the Annotator Model can generate workflows with over 70 actions, and theoretically WorkflowLLM should be capable of the same. Given the general limitations of LLMs in long sequence generation, including such long-sequence workflows in the appendix would further demonstrate the work's contribution. The absence of examples of long-sequence workflows makes it difficult to assess the practical utility of the proposed approach for complex real-world scenarios.
5. Given that the core contribution is data construction, whether the dataset will be open-sourced directly affects the practical value of the work. The authors should consider open-sourcing the dataset to promote development in this field.

### Questions
1. The performance of generic LLMs in workflow orchestration through agent-like approaches would serve as an interesting baseline for comparison. Through this comparison, we could better understand whether the core challenge lies in the model's reasoning capabilities or in its ability to maintain consistent output formats. This point won't affect the score; it's just for discussion.

### Soundness
2

### Presentation
2

### Contribution
1
