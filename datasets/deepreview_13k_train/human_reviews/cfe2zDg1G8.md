# Scenario-Wise Rec: A Multi-Scenario Recommendation Benchmark

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Multi Scenario Recommendation (MSR) tasks, referring to building a unified model to enhance performance across all recommendation scenarios, have recently gained much attention. However, current research in MSR faces two significant challenges that hinder the field's development: the absence of uniform procedures for multi-scenario dataset processing, thus hindering fair comparisons, and most models being closed-sourced, which complicates comparisons with current SOTA models. Consequently, we introduce our benchmark, Scenario-Wise Rec, which comprises six public datasets and twelve benchmark models, along with a training and evaluation pipeline. We have also validated our benchmark using an industrial advertising dataset, further enhancing its real-world reliability. We aim for this benchmark to provide researchers with valuable insights from prior works, enabling the development of novel models based on our benchmark and thereby fostering a collaborative research ecosystem in MSR. Our source code is also available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper provides a much-needed benchmark for the emerging multi-scenario recommender systems (MSR) field. This benchmark contains a comprehensive framework (including training and evaluation pipelines) and inspects multiple public and industrial data sets. The detailed comparison of various MSR models provides valuable insights into their advantages and disadvantages. In addition, the source code is available to the public.

### Strengths
S1: The paper presents the first dedicated benchmark for multi-scenario recommendation tasks, which may become a valuable resource in the field. It offers a comprehensive pipeline that includes data processing, model training, and evaluation, setting a new standard for transparency and reproducibility in MSR research. 

S2: Including public and industrial datasets strengthens the benchmark's reliability and applicability, covering many real-world scenarios. The publicly available source code and detailed tutorials will greatly facilitate researchers in conducting experiments and building upon the benchmark.

S3: The paper provides a fair and detailed comparison of twelve state-of-the-art MSR models, which is valuable for researchers looking to understand the current landscape of MSR.

### Weaknesses
W1: Although the advantages and disadvantages of different baselines are provided, it can further enhance insights by solving the theoretical basis of the model and providing mitigation strategies for the "seesaw effect."

W2: The focus of standard MSR is understandable, but it does not explore the benchmark testing of more scenario-related topics (e.g., multi-scenario multi-task) and additional information (e.g., user's interactive history sequence), limiting the scope of its practical procedures.

W3: The paper could benefit from a more detailed analysis of the models' computational efficiency, particularly how they scale with dataset size and complexity, which is crucial for practical deployment. In addition, moral considerations in the MSR system are also beneficial, especially data privacy and potential prejudice.

### Questions
Q1: Can the cause of different baselines on different data sets provide some additional insights? Are there any strategies that can be summarized for the seesaw effects?

Q2: Can the authors provide more detailed analyses or benchmarks on the computational efficiency and scalability of the MSR models, especially in resource-constrained environments? 

Q3: Can the moral considerations in the MSR system provide some corresponding insights?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presented benchmark results on 6 existing public datasets and one newly collected industrial dataset with 12 recommendations models. There is an emphasis on multi-scenario recommendation, where different datasets are treated as multi-scenario by using some features for differentiating scenarios, such as user age, ad position, context, item category, platform, and news genres. Results are reported for how the number of “scenarios” affect model performance.

### Strengths
comprehensive experiments are done with a wide range of algorithms and datasets, including a newly collected industrial dataset, with code provided and clear instructions.

### Weaknesses
The contribution and novelty is limited since the authors merely present existing public benchmark datasets with some features for differentiating “scenarios”, whereas some, if not all, of these features could very well be just normal features, and no justification is provided on why it’s a reasonable choice to make them “scenario” features, and it seems the results are not benchmarked with treating the dataset as “single-scenario” as is, and treat the “scenario-feature” as normal feature. How the "scenario" features are handled are also not clearly described. 

Many experiments are done, but limited insights are drawn from these experiments except some observations. Especially how the “scenarios” are modeled, and why certain models should be better than others. 

The introduction of the industrial dataset seems new, but the description seems quite plain, and it’s not convincing why this newly collected dataset is a good dataset for benchmarking.

### Questions
Why does it make sense to artificially make certain features differentiate scenarios? 

What is the “301” context feature?

What is “dense scenario” and “sparse scenario”?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new benchmark for Multi-Scenario Recommendation. To deal with the problems of lacking standard data process pipline and closed-source models in MSR research, this paper introduces Scenario-Wise Rec, which includes six public datasets and one industrial dataset, twelve benchmark models, and a standardized training and evaluation pipeline to achieve model comparisons.

The contributions are:
It is the first benchmark specifically designed for MSR, a standardized pipeline for data processing, training and evaluation.
Open-Source and Real-World Applicability: Scenario-Wise Rec is publicly available, and is validated by applying it to a complex industrial dataset.

### Strengths
This paper developed a standardized benchmark specifically for Multi-Scenario Recommendation tasks. This idea is good and needed in this area. This platform is particularly novel. It provides a comprehensive framework that includes multiple datasets, implementations, and a full evaluation pipeline, aiming to give comparisons across scenarios. The idea of the standard platform and benchmark is quite important. It provides a valuable tool to address the growing need for reliable, standardized MSR evaluations. 

The paper is also well-organized and clear in its presentation. It is easy to read and the idea is presented directly. The authors provide much context about the challenges in MSR and the motivation behind their benchmark. The diagrams and tables effectively illustrate the framework’s components and results, which help the researcher who may want to leverage the benchmark.

### Weaknesses
The idea of ​​the article is very good, providing a benchmark. However, because it is a benchmark, it must adapt to different needs and also take into account the multi-scenario interaction of MSR, which is a very difficult task. This paper has an ambiguous definition of multi-scenario. The datasets used are segmented but lack true cross-scenario relationships, which limits the ability to share knowledge between scenarios as MSR ideally should. The experiments focus on isolated scenario performance without evaluating transferability across scenarios.

Also, the use of only AUC and Logloss limits insights into cross-scenario performance consistency. What if other researchers's model have different targets and need different evaluation metrics?

Last, the pipeline may lack modularity, restricting researchers from customizing data processing, model structures, or metrics.

### Questions
1. The experimental setup appears focused on individual scenario performance. Could you consider expanding the experiments to include cross-scenario evaluations, such as training a model in one scenario and testing in another, to validate transferability? This would provide valuable insights into the models’ adaptability across scenarios.

2. Could you elaborate on how the current data segmentation aligns with a true multi-scenario framework? Specifically, how do you envision the potential for knowledge transfer between segmented scenarios in the current datasets, given that they do not share users or items across contexts?

### Soundness
2

### Presentation
3

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
This paper presents a benchmark that includes six existing datasets for multi-scenario ctr prediction. Besides, they implement twelve models in these datasets with established data and training pipelines. The datasets and codes are provided.

### Strengths
1. The datasets and codes are provided.
2. The topic is meaningful in that researchers can implement baseline comparison via the provided benchmark.
3. The experiments are comprehensive with 10 times running.

### Weaknesses
1. Some clarifications are confusing. The terminology requires revision, particularly the use of "recommendation," which does not accurately reflect the concept being discussed.
2. The comparative analysis presented in Table 1 does not sufficiently demonstrate novel contributions relative to existing work in the field.
3. The methodology section would benefit from additional detail, particularly regarding the model parameter selection process and optimization criteria.
4. The motivation and challenge are not convincing. Most of the works in the papers have been provided with runnable code responsity.

### Questions
1. Why do authors claim that this research is a cut-edge benchmark, while no related explanations are provided in the paper?
2. It seems that most of the baselines and evaluation metrics are designed for CTR prediction. So why use recommendation expressions in the paper?
3. What is the novel challenge for researchers to implement the multi-scenario models?
4. Can you provide statistical analysis for supporting the second challenge, that many MSR models are closed-sourced.

### Soundness
3

### Presentation
2

### Contribution
2
