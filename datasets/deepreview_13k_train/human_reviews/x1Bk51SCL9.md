# Face-Human-Bench: A Comprehensive Benchmark of Face and Human Understanding for Multi-modal Assistants

- Decision: Reject
- Scores: 8, 3, 6, 6

## Abstract
Faces and humans are crucial elements in social interaction and are widely included in everyday photos and videos. Therefore, a deep understanding of faces and humans will enable multi-modal assistants to achieve improved response quality and broadened application scope. Currently, the multi-modal assistant community lacks a comprehensive and scientific evaluation of face and human understanding abilities. In this paper, we first propose a hierarchical ability taxonomy that includes three levels of abilities. Then, based on this taxonomy, we collect images and annotations from publicly available datasets in the face and human community and build a semi-automatic data pipeline to produce problems for the new benchmark. Finally, the obtained Face-Human-Bench comprises a development set with 900 problems and a test set with 1800 problems, supporting both English and Chinese. We conduct evaluations over 25 mainstream multi-modal large language models (MLLMs) with our Face-Human-Bench, focusing on the correlation between abilities, the impact of the relative position of targets on performance, and the impact of Chain of Thought (CoT) prompting on performance. Moreover, inspired by multi-modal agents, we also explore which abilities of MLLMs need to be supplemented by specialist models. The data and evaluation code of the Face-Human-Bench will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes Face-Human-Bench, a hierarchical benchmarking framework aimed at evaluating the ability of multi-modal large language models (MLLMs) to understand and interpret faces and human figures. The framework categorizes tasks across multiple levels of comprehension, from facial attributes and actions to complex reasoning like social relationships and spatial relationships. It comprises 900 development set problems and 1,800 test problems, supporting both English and Chinese. By leveraging a semi-automatic data pipeline, the authors collect and annotate images from multiple datasets to form this comprehensive benchmark. Evaluations on 25 MLLMs reveal insights on model performance relative to the task type, the relative positioning of target objects, and the effectiveness of Chain-of-Thought (CoT) prompting. Results suggest areas where specialist models surpass MLLMs, emphasizing the benchmark’s role as a holistic tool to gauge MLLM performance on face and human understanding.

### Strengths
- **Comprehensive Benchmarking Framework**: The face-human bench spans many abilities, providing a holistic evaluation of multimodal assistants’ capabilities in the face and human understanding.
- **New Metrics and Evaluation Protocols**: The paper introduces RPSS to measure sensitivity to the relative position of targets and percentile recall to assess retrieval in large galleries. These metrics provide nuanced insights, aiding model development.
- **Multi-Language Support**: The benchmark ensures broader applicability across language barriers by supporting both English and Chinese.
- **Empirical Findings on MLLM Performance**: The evaluation of 25 MLLMs is thorough, providing insights into model performance across diverse tasks and the potential utility of Chain-of-Thought prompting.

### Weaknesses
 - **Limited Discussion on Dataset Biases**: Although the benchmark includes diverse tasks, the paper could expand on potential biases in the benchmark datasets, especially considering the variability in demographic representations in face and human recognition tasks. The relatively low representation of certain groups, such as Indian individuals in the Face Understanding tasks and African individuals in Human Understanding, might still contribute to underperformance for these groups. Further analysis of how this impacts specific task results within the benchmark would strengthen the conclusions. The racial performance disparity observed in the RFW-derived experiments, with a significant gap between Caucasians and other groups, could merit further discussion on potential mitigations, such as rebalancing the dataset or weighting performance metrics to emphasize fairness. It would be helpful to explicitly link these diversity statistics to performance breakdowns within the benchmark, beyond RFW, to provide a clearer picture of how the diversity in Face-Human-Bench affects model evaluations across tasks. Consideration, whether in an actual experiment or as part of the analysis, should consider the BFW dataset, which offers a simple experiment of facial verification using balanced data.
- **Generalizability to Other Tasks**: The applicability of Face-Human-Bench to tasks beyond face and human recognition remains unclear. Expanding on how these benchmarks might generalize to other domains would add depth. Detailed, reusable guidelines for data collection, problem formulation, and standardization would make this methodology more accessible to researchers aiming to replicate or extend the benchmark framework. If the work extends to other capabilities, addressing potential biases (e.g., geographic distribution of flora/fauna or cultural biases in mathematical reasoning datasets) should be a central concern. This aligns with the identified issues in demographic diversity and fairness for the Face-Human-Bench.
- **Impact of CoT Prompting is Limited for Open-Source Models**: While Chain-of-Thought prompting improves closed-source models, the performance gain is minimal for open-source counterparts, indicating limitations in the broader applicability of CoT. It may be helpful to explore how curated pretraining datasets emphasizing CoT reasoning could enhance these models' abilities. Additionally, providing insights into any experiments (e.g., fine-tuning on CoT-style tasks) would demonstrate the feasibility of mitigating this limitation. While lower parameter counts are identified as a limitation, it would be useful to contextualize this issue with examples. For instance, how do parameter counts correlate with CoT performance across open-source and proprietary models? This could help readers gauge whether scaling up model sizes is a plausible solution or whether architectural innovations might be required. Consider exploring alternatives to CoT prompting, such as retrieval-augmented generation or task-specific fine-tuning, which might bypass some current constraints on open-source models.

### Questions
1. Dataset Composition and Diversity: Could you provide more details on the demographic diversity of the benchmark datasets, particularly for face recognition tasks?
2. Transferability Across Domains: Do you envision Face-Human-Bench or its methodologies applying to multi-modal tasks outside of face and human recognition?
3. Insights on CoT Prompting Performance: Do you hypothesize that the limited effectiveness of CoT prompting on open-source models is due to training data limitations, model architecture, or another factor?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper gathers together many face and human related visual perception tasks (e.g. age and emotion recognition, crowd counting, person re-id) in the proposed Face-Human-Bench and evaluates several VLLMs (25 in total) on them.

### Strengths
The evaluation task pursued in this paper has some value especially for researchers working on face and human analysis. The problem is that most tasks evaluated are purely vision tasks for which many strong baselines exist. It's not surprising that specialists models outperform the VLLMs on these tasks. But arguably the authors have put a considerable amount of effort to organise the benchmark and evaluate the models. Finally, the experiment of section 3.4 is interesting.

### Weaknesses
Overall, unfortunately, the are a few issues with the paper which limit the impact of the proposed work: 
- It's not clear whether the proposed benchmark adds something to our understanding of VLLMs. 
- It's not clear why one would use a VLLM to accomplish the tasks mentioned in the paper which are visual perception tasks with very specific use cases. Since the proposed tasks are very different from the ones that the VLLMs were trained on it is perhaps not even meaningful to evaluate the models on these tasks (even the ranking of the models does not reveal some interesting information/conclusion about the VLLMs)
- In terms of novelty, the authors perform standard steps to reformulate the tasks in a manner which is understandable by the VLLM. 
- Another issue is that the paper reveals very few not expected results. For example it is not surprising that sophisticated pipelines for face analysis (that perform detection, alignment and recognition) trained on datasets developed for these tasks would perform a lot better than the evaluated VLLMs  on the corresponding tasks. Nor it is surprising that models with more parameters perform better.

### Questions
See weaknesses above.

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
4

### Summary
This paper presents a benchmark specifically designed to evaluate the facial and human understanding abilities of multimodal assistants, named Face-Human-Bench. Based on a hierarchical ability taxonomy divided into three levels, Face-Human-Bench covers 18 relevant tasks. Using the proposed Face-Human-Bench, this paper conducts a comprehensive evaluation of mainstream Multimodal Large Language Models (MLLMs) and explores the correlations between abilities, the impact of target relative positioning on MLLM performance, and the effects of Chain-of-Thought (CoT) prompting on MLLM performance.

### Strengths
1. The proposed Face-Human-Bench is a comprehensive evaluation benchmark that fully encompasses relevant tasks, making the assessment results more valuable and reliable.
2. The paper evaluates 25 existing mainstream MLLMs on Face-Human-Bench, with a substantial amount of experiments and rich content, intuitively demonstrating each MLLM's capabilities in facial and human understanding.
3. The paper is well-organized and clearly articulated, which improves readability and makes the findings accessible to a broad audience.

### Weaknesses
1. The paper mentions that Face-Human-Bench consists of a development set with 900 problems and a test set with 1800 problems, but it lacks a description of the roles of these two sets. In the subsequent experimental results, which set were the results based on?
2. There is a point of confusion regarding the calculation of the overall score: how are the weights for each sub-task determined?
3. The paper states that Face-Human-Bench supports evaluations in both English and Chinese. What insights does obtaining different results when evaluating in different languages provide? Do different models exhibit language preferences due to variations in training data?
4. The calculation method for correlation between abilities in Section 3.3 needs to be further detailed and clarified.
5. After using specialist models to assist MLLMs, did the performance of MLLMs improve on the corresponding tasks? By how much? It would be helpful to provide quantitative experimental analysis to illustrate this.
6. Minor error: In line 116, the classification of the models is reversed.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a study on how different Multimodal Large Language Models (MLLMs) perform on various tasks that relate to human and face understanding, and whether dedicated models can do better on those tasks than MLLMs. To this end, the authors collect in a semi-automatic way a large corpus of face and human data from existing datasets, through a manually defined curating process. The proposed Face-Human-Bench is divided following a hierarchical taxonomy of tasks from broad to fine grained tasks.

### Strengths
The paper presents a thorough evaluation of different models on a very well-defined, broad variety of tasks that relate human and face analysis, such as attribute classification, gender recognition, or activity recognition. The gathered corpus seems to have been curated in a neat manner and the authors are planning to make the corpus with their annotations open source. Different metrics such as accuracy and context-related performance are evaluated, shedding light on how far MLLMs are to bridge the gap w.r.t. dedicated models. 


The paper is overall well presented (although it requires some proof reading and some rephrasing here and there), and the supplementary material is accompanied with multiple visual examples and the dataset collection description. I believe the results and data are of interest to the community working on exploiting LLMs for human analysis.

### Weaknesses
 The main drawback of this paper is that it merely consists of a report. A thorough report, but that contains no technical contributions. The paper is an extensive, high-effort consistent evaluation of models, and this I believe is not enough for the paper to fit in the conference. 


Section 3.3 “Correlation Between Abilities” is rather loosely written. What does the “correlation between abilities” mean? What is the measure or score that is given to an “ability” for it to be correlated with other abilities? 


The RPSS as a score difference between a cropped image and the original one for attribute prediction is rather trivial and should not be counted as a contribution. That some models lose performance when prompted with local features is surprising. 


I believe that the paper should also include a small description of the actual MLLMs under evaluation (or at least of the most significant ones), as well as of the data they have been trained on. Would it be possible that some of the models outperform others just because their training data was closer to that expected for human analysis? Such analysis should be included in my opinion.

### Questions
In my honest opinion, I believe the paper is not fit for ICLR as its contributions seem to me far from the scope of the conference. By no means I disregard the authors’ work, as it is a complete study of how Multimodal LLMs perform on a broad set of tasks regarding human analysis. However, this is all I can take from the paper, a nice, well elaborated and through study with no technical contributions. ICLR is a conference that welcomes all kinds of technical contributions within ML and CV; however, such a study I believe fits better with the IEEE Trans. on Affective Computing than on ICLR. I don’t recall seeing in ICLR over the past years such kind of report. Of course I might be wrong, and I am willing to change my mind should the authors provide evidence of former ICLR papers that are of the same kind, as this would set for precedence; or should the AC believe the paper fits within the conference.

### Soundness
2

### Presentation
3

### Contribution
1
