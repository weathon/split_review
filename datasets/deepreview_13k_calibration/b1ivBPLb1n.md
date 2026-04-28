# BigDocs: An Open and Permissively-Licensed Dataset for Training Multimodal Models on Document and Code Tasks

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Multimodal AI has the potential to significantly enhance document-understanding tasks, such as processing receipts, understanding workflows, extracting data from documents, and summarizing reports. Code generation tasks that require long-structured outputs can also be enhanced by multimodality. Despite this, their use in commercial applications is often limited due to limited access to training data and restrictive licensing, which hinders open access. To address these limitations, we introduce \bigdocscpt{}, a high-quality, open-access dataset comprising 7.5 million multimodal documents across 30 tasks. We use an efficient data curation process to ensure our data is high-quality and license-permissive. Our process emphasizes accountability, responsibility, and transparency through filtering rules, traceable metadata, and careful content analysis. Additionally, we introduce \bigdocsft{}, a benchmark suite with 10 novel tasks where we create datasets that reflect real-world use cases involving reasoning over Graphical User Interfaces (GUI) and code generation from images. Our experiments show that training with \bigdocsft{} improves average performance up to 25.8\% over closed-source GPT-4o in document reasoning and structured output tasks such as Screenshot2HTML or Image2Latex generation. Finally, human evaluations showed a preference for outputs from models trained on \bigdocs{} over GPT-4o. This suggests that \bigdocs\ can help both academics and the open-source community utilize and improve AI tools to enhance multimodal capabilities and document reasoning. The project is hosted at \url{https://bigdocs.io}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces BigDocs-7.5M, a large-scale, license-permissive dataset for training multimodal models on document and code-related tasks. Along with a comprehensive suite of tools and data analysis, the authors present BigDocs-Bench, featuring 10 downstream tasks that assess a model’s ability to generate long-format code outputs from images. These tasks serve as practical benchmarks for real-world applications. In paper the experiments show that models trained on BigDocs outperform those trained on existing datasets. All the artifacts in this paper is open source and permissive.

### Strengths
1. All the stuff in the paper is under permissive license, which is a big plus for an artifact and benchmark focused research paper.
2. The dataset curation process and filtering make sense for better data quality
3. Bonus point on keeping multimodal in mind when creating a document-understanding dataset.
4. Data contamination analysis is nice to have when the dataset proposes training set.

### Weaknesses
1. Many aspects of the data curation process, including the effect of OCR, VQA format and text-image alignment, etc. are sort of still unanswered in the experiment section, making readers wonder, why and if these curation processes are needed, or are they actually contributing to better performance resulted in the final model.
2. As a aggregation benchmark with a lot of different downstream tasks, how are the aggregated score on this BigDocs-Bench correlates with other existing benchmarks also presented in the paper? A comparison of what new aspects this new Benchmark is adding to existing research landscape is crucial to justify.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces BigDocs-7.5M, a large-scale, open-access dataset (CC-BY-4.0) designed to enhance multimodal model training on document and code-related tasks. Addressing limitations in existing datasets such as restrictive licensing and data access, BigDocs-7.5M provides a rich collection of 7.5 million multimodal documents suitable for a variety of tasks including document reasoning, structured output generation, and graphical interface interpretation. The authors alrso release the BigDocs-Bench to evaluate LLMs ability to analyze code and docs over 10 categories of tasks.

### Strengths
1. Comprehensive and Novel Dataset: The introduction of BigDocs-7.5M offers a permissively licensed, open-source dataset that includes a wide variety of document types and structured outputs

2.  Improvement in Model Performance: The paper convincingly demonstrates that models trained on BigDocs-7.5M outperform those trained on existing closed-source datasets, particularly in multimodal document understanding and code generation tasks​ with Phi-3.5 Finetuned at ~50% vis-a-vis gpt-4o ~25%. 

3. Thorough evaluation suite: The introduction of BigDocs-Bench for benchmarking model performance across 10 novel tasks is a valuable contribution, providing detailed insights into the models' capabilities.

### Weaknesses
1.With regards to human-evaluation in section 5.3 of the paper, could the authors shed more light on the evaluators' qualifications, selection process, and any potential conflicts of interest? 

2. While I do appreciate the value of BigDocs-Bench, and the evaluation on a collection of open-source and closed-source models, I would encourage the authors to consider including a correlation analysis between BigDocs-Bench and specific benchmarks like human-eval and RULER. This would provide a clearer picture of how BigDocs-Bench relates to existing evaluation metrics in the field.



### Questions
While I appreciate the authors pro-actively acknowledging that the limited context length of the models trained (8192 tokens) might impact the performance of the models, can the authors provide some insights on the artifacts of this decision. For example, we can see both the 7b and the phi-3.5 models saturating around 50%. Do the authors suppose this might be an artifact of the context length? On the same lines, or perhaps, is there another reason for the plateau? Or is it merely the dataset getting harder beyond half the samples?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new large-scale and license-permissive dataset BigDocs for continual pertaining on multimodal document and code tasks. Based on this dataset, the paper also introduces BigDocs-Bench containing the training set, validation set and test set to evaluate tasks like code generation and reasoning from documents.

### Strengths
+ The paper introduces a new large-scale dataset for pertaining and fine-tuning, and a corresponding benchmark, with permissive license, which is the first one in the target domain. This is a concrete contribution to the research community and industry in the subarea.
+ The paper presents comprehensive experiments with leading open and closed models on both general and proposed benchmarks. The results are promising. Also, human evaluations provide further evidence on the effectiveness of training on BigDocs.

### Weaknesses
 + The results on the proposed BigDocs-Bench are a bit strange. The performances of the same model on different tasks are not stable, e.g., Claude-3.5-sonnet behaves very bad on Chart2MD and gets a high score on GUI2Sum. Further, small models can gets higher scores than a much larger model, e.g., Qwen2-VL-2B gets a higher avg. score(20.00) than Claude-3.5-Sonnet(18.31) and GeminiPro-1.5(19.23). This could indicate the benchmark is too specific for a general model not trained with BigDocs.
+ In human evaluation, gpt-4 gets a higher win rate than Phi3.5-BigDocs, while in BigDocs-Bench it's the opposite, which again indicates the benchmark may not differentiate a stronger model.

### Questions
+ 'BigDocs will be open-sourced (upon acceptance)'. If you want to open-source this dataset, what's the point of waiting upon acceptance?
+ Personally, I think it's not necessary to keep a *hidden test set* for the benchmark.

### Soundness
4

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
3

### Summary
This paper introduces BigDocs, an open-source large-scale multimodal dataset for document understanding and code generation tasks. The main contributions include:

1. BigDocs-7.5M: A high-quality dataset containing 7.5 million image-text pairs across 30 tasks
2. BigDocs-Bench: 10 new benchmark tasks focusing on structured output generation
3. BigDocs Toolkit: A set of tools for data processing and preparation
4. Experimental validation: Demonstrated effectiveness through comparisons with models like GPT-4

### Strengths
1. Addresses a significant issue: licensing restrictions and accessibility problems in existing document understanding datasets

2. Quality assurance:
        Rigorous data filtering process
        Traceable metadata

3. Comprehensive task coverage: from basic document information extraction to complex structured output generation

4. Open-source commitment: supports responsible AI development

### Weaknesses
1. Insufficient validation of benchmark quality and reliability

    a). While Section 4.2 mentions manual human verification for BigDocs-Bench, the paper lacks crucial details about the verification methodology and evaluation criteria. For example, the number of human verifiers involved, their qualifications, the specific criteria they used for evaluation, or how inter-rater reliability was ensured.

    b). Given the large volume of synthetic data in the benchmark, the paper fails to address the practical challenges of comprehensive human verification. The sampling strategy and quality assurance process for human verification are not described, raising questions about the robustness of the validation process

2. Limited scope of base model experiments

    a). The experimental validation is confined to models ranging from 2B to 7B parameters. The absence of experiments with larger-scale base models (>7B parameters) limits the understanding of the dataset's effectiveness across different model scales

3. Insufficient qualitative analysis of model performance

    a). The paper lacks detailed error analysis and concrete examples in the Qualitative Results section.

    b). Section 5.3 would benefit from including error distribution patterns across different models and tasks. The absence of systematic error analysis makes it challenging for readers to:

        i. Understand the specific improvements BigDocs-7.5M brings to different document processing tasks

        ii. Identify potential limitations or biases in the dataset

        iii. Comprehend the typical failure modes of models trained on this dataset

### Questions
In addition to the three points mentioned in the weaknesses section, I am concerned about the performance reported in Table 3. The unusually low performance of advanced models like GPT-4o and Claude-3.5-sonnet raises questions about the experiment's setup. Did you use one-shot prompting in your experiments? If zero-shot prompting was used, this might create an unfair comparison with models that haven't been fine-tuned on these specific benchmarks. Could you clarify the prompting strategy and consider providing results with one-shot or few-shot prompting for a more equitable comparison?

### Soundness
3

### Presentation
3

### Contribution
3
