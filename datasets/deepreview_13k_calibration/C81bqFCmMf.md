# COMET: Benchmark for Comprehensive Biological Multi-omics Evaluation Tasks and Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
As key elements within the central dogma, DNA, RNA, and proteins play crucial roles in maintaining life by guaranteeing accurate genetic expression and implementation. Although research on these molecules has profoundly impacted fields like medicine, agriculture, and industry, the diversity of machine learning approaches—from traditional statistical methods to deep learning models and large language models—poses challenges for researchers in choosing the most suitable models for specific tasks, especially for cross-omics and multi-omics tasks due to the lack of comprehensive benchmarks. To address this, we introduce the first comprehensive multi-omics benchmark COMET (Benchmark for Biological **CO**mprehensive **M**ulti-omics **E**valuation **T**asks and Language Models), designed to evaluate models across single-omics, cross-omics, and multi-omics tasks. First, we curate and develop a diverse collection of downstream tasks and datasets covering key structural and functional aspects in DNA, RNA, and proteins, including tasks that span multiple omics levels. Then, we evaluate existing foundational language models for DNA, RNA, and proteins, as well as the newly proposed multi-omics method, offering valuable insights into their performance in integrating and analyzing data from different biological modalities. This benchmark aims to define critical issues in multi-omics research and guide future directions, ultimately promoting advancements in understanding biological processes through integrated and different omics data analysis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents the performance of eight foundation models of varying design on 17 tasks of varying underlying biological attributes. The authors adapted and trained the models for the

### Strengths
The authors grouped various tasks from multiple sources and did exceptional work in clearly detailing the underlying biological importance of the task. They choose multi-omics data. The task not only describes different biological aspects but also varying computational types, as some are classification and some are regression tasks. The training data process was clearly detailed.
They displayed the performance of cross-omics tasks by combining models, a crucial aspect and direction for future research.

### Weaknesses
The manuscript does not sufficiently explain the primary criteria for selecting models or tasks. For instance, the authors did not include models like HyenaDNA; it is unclear if this was due to lack of availability, popularity, or suitability. Furthermore, the rationale behind choosing specific tasks, such as those related to gene expression, is underdeveloped. Additional databases like PanglaoDB could have been considered to broaden the task scope. In addition, the task generation.The authors' decision to group cell types also introduces a layer of specificity that might limit the generalizability of conclusions across model families or architectures. If I'm not mistaken the tasks are not shared and if not require some summary statistics to support the conclusions.

Model performance is evaluated based on fine-tuning, but it is unclear whether the observed results are due to the model architecture or the fine-tuning process itself. This could be addressed by performing multiple training runs and reporting the mean and variance to provide a more reliable performance measure. Also, only a single metric is shared, which again limits the ability to generalize.
The term frozen in Table Three is not fully explained. I assume it refers to the use of the model released weights if so for DNABERT the performance of the frozen is better than the non-frozen?. The difference in performance between the frozen and unfrozen should be discussed in the results.

In summary, three main limitations affect this study: (1) the absence of clear criteria for model and task selection, (2) a lack of performance confidence intervals, and (3) insufficient detail in task creation. These weaknesses limit the generalizability of the findings, and hinder reproducibility and application in other contexts. Even the conclusion that “language models outperform naïve supervised models” is hard to ascertain for the

### Questions
1.	Detail the criteria for choosing models?
2.	Detail the criteria for creation of the specific tasks (why this DB why not another)?
3.	Elaborate on the performance add confidence intervals and other metrics?
4.	What does the term frozen mean?
5.	Expand on the task creation process or supply the tasks or the summary statistics.

### Soundness
4

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
4

### Summary
This paper presents the comprehensive multi-omics benchmark COMET (Benchmark for Biological Comprehensive Multi-omics Evaluation Tasks and Language Models), created to assess models across single-omics, cross-omics, and multi-omics tasks. The goal of this benchmark is to identify key challenges in multi-omics research and to guide future efforts, ultimately fostering advancements in understanding biological processes through the integrated analysis of diverse omics data.

### Strengths
This paper curated a collection of datasets and tasks covering structural and functional aspects in DNA, RNA, and proteins, including tasks that span multiple omics levels. This paper further evaluated a variety of FMs for respective Bio-modalities, offering insights into their performance, especially with respect to cross-modality applications.

### Weaknesses
The introduction to the various benchmark tasks is thorough. However, it would be advantageous to provide more detailed information about the AIML models being evaluated, particularly regarding their potential strengths and weaknesses for specific tasks. For example, the paper should specify the pre-training datasets, architectures, and any specific design choices that might influence performance on different omics modalities. Additionally, it is recommended to explain other aspects of model training and evaluation, such as the criteria for choosing between LoRA fine-tuning and full fine-tuning for each model, and the rationale behind selecting specific metrics for evaluating each model. For instance, why are certain tasks evaluated with Pearson correlation while others use Spearman correlation or R-squared? A more detailed justification for these choices is needed.

Results interpretation is rather brief and sometimes confusing.

•	What is the key takeaway from all the experiments when comparing Literature SOTA to Pre-trained FMs? Specifically, Literature SOTA outperformed in all protein-related tasks listed in Table 3—what insights can be drawn from this? Additionally, no RNA-based FMs achieved top performance in any RNA tasks—what insights can be provided here? Could it be related to how much data was used in pre-training the RNA-based FMs? The summary text in section 5.2 does not accurately reflect the data presented in Table 3, which is causing confusion.

•	For 5.3, CROSS-MOLECULAR BENCHMARK RESULTS, why the performance on EC is so much worse for CaLM after refinement, which is typically not the case if refinement is properly done? Also for EC task, using condon sequence gets noticeably worse results compared to its protein sequence counterpart. What is special about EC task compared to other tasks like Beta-Lac and Flu, which might contribute to this difference?

•	For 5.4 MULTI-MOLECULAR BENCHMARK RESULTS, In contrast to single-molecular tasks, for multi-molecular tasks, Literature SOTA still dominantly work better compared to multi-omics models or combination of two single-omics models. It would be important to elaborate the possible limitations in the current implementation of the multi-omics models that leads to this contrast and inferior performance.

The related work of paper can be strengthened and some of the claims can be formulated in the appropriate context of existing works. For example, the paper claims to be the first to establish a benchmark for "compiling tasks and data involving cross-molecules and multi-molecules" and "evaluate existing foundation models for DNA, RNA, and proteins, as well as multiomics approaches. We conduct experiments with fully-finetuned or frozen models." Recent works such as Prakash, Moskalev et al., 2024 (Bridging biomolecular modalities for knowledge transfer in bio-language models) and Boshar et al., 2024 (Are Genomic Language Models All You Need?) should be cited as laying the foundations for these ideas and uncovering the link to central dogma which the paper claims as their contribution.

Some of the conclusions have already been derived in prior works such as "CDS model demonstrates competitive performance on codon sequence data" has been reported already in CaLM (Outerial & Deane, 2024)

### Questions
Provided in Weakness section

### Soundness
2

### Presentation
2

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
This paper introduces a comprehensive multi-omics benchmark encompassing a diverse collection of 17 cross-omics downstream tasks and datasets. It evaluates a set of state-of-the-art (SOTA) foundational language models, providing detailed descriptions of both implementation and outcomes. The project represents a significant amount of work and offers valuable information for the research community. The paper is well-written and easy to follow. While the paper excels as a resource, it lacks methodological novelty and the findings are largely intuitive. Addressing these areas and providing more in-depth analysis and discussion would significantly enhance the paper's contribution to the field.

### Strengths
Comprehensive Benchmark: The introduction of a multi-omics benchmark covering 17 diverse tasks and datasets is a significant contribution. It provides a standardized framework for evaluating the performance of various models across different omics data types.
Detailed Implementation: The paper includes thorough descriptions of the implementation process, which enhances reproducibility and allows other researchers to build upon this work.
Valuable Resource: The benchmark and the accompanying evaluations serve as a valuable resource for the community, facilitating future research and development in the field of multi-omics.

### Weaknesses
Methodological Novelty: While the paper is resource-rich, it lacks methodological innovation. The primary focus is on benchmarking existing models rather than introducing new techniques or approaches. This limits its contribution to the field, as it primarily validates existing methods without pushing the boundaries of current research. The absence of novel algorithms or architectures means that the paper does not offer new tools or strategies for addressing the challenges of multi-omics data integration and analysis.
Insightfulness of Findings: Many of the findings presented are intuitive and do not offer deep insights into the underlying mechanisms or potential improvements. For example, the observation that multi-omics models outperform single-omics models on multi-molecular tasks is not particularly surprising. The paper needs to delve deeper into why certain models perform better in specific scenarios and what biological insights can be derived from these performance differences. A more detailed analysis of model behavior, such as attention maps or feature importance, would be beneficial.

### Questions
Benchmark Scope: While the benchmark is comprehensive, it would be beneficial to discuss any limitations or potential biases in the selection of tasks and datasets. This would provide a more balanced perspective and guide future expansions of the benchmark.
Comparison with Existing Benchmarks: A comparison with existing multi-omics benchmarks, if any, would help contextualize the contributions of this work and highlight its unique aspects.
Future Directions: The paper could benefit from a discussion on potential future directions, such as the integration of additional omics data types, the development of new evaluation metrics, or the exploration of novel model architectures.
Practical Applications: Including examples of practical applications or case studies where the benchmark has been used to derive meaningful biological insights would demonstrate the real-world utility of the resource.

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
This paper proposed a new benchmarking pipeline for biological sequence models.

### Strengths
This paper is well-structured and covers most recent foundation models for biological sequence analysis, which will attract researchers in this field.

### Weaknesses
Although the pipeline and experiments are interesting, I do have some questions and I believe that the authors overclaim their dataset preparation and pipeline design. Here are my questions:

1. In Figure1, the authors mention that the benchmarking resources coming from different databases. However, if we zoom in each task, only one dataset is selected into benchmarking, which is really a biased selection. For similar benchmarking analysis [1,2], most of them will cover diverse datasets for each task. This is also different from a recent publication BEND [3], because the authors here intend to benchmark information like gene expression, which is less constant comparing with tasks like gene finding. Would the authors please justify that their choices are unbiased or consider including more datasets?

2. For Table 1, the metrics seem inconsistent. For example, why the authors sometimes select SCC, while other cases are based on PCC or R2? Should all of them be used for benchmarking a regression task? Also, what is the reason of not using PCC for all cases but using SCC for certain task? I cannot understand the reason.

3. In Table 2, the authors consider DNABERT2 [4]. However, I am confused about the max token length of DNABERT2. The current version of DNABERT2 can handle DNA sequence with different length, and the token length can be increased. Could the authors use the latest version for benchmarking to make a fair and useful comparison?

4. In Table 3, what is the meaning of percentage (%) for PCC, SCC or R2? These metrics can be negative, so what is the meaning of a negative percentage?

5. Could the authors ensure that their task-specific method (like Xpresso) is really the optimal solution? Why do the authors not choose Enformer [5] or Borzoi [6] for gene expression prediction? It will be much more helpful to list the sources of task-specific method and the reason to choose them (like based on benchmarking studies, they are top-performer?)

6. I am a bit confused from the conclusion of this benchmarking analysis. Would the authors please highlight their discovery in the abstract section and thus the readers can learn from your paper? I think most of the content of abstract and conclusion are presenting experiment design, but other key information, like some tasks need better methods, should be emphasized. 

7. Furthermore, I wonder if the authors can check if the validation dataset might be used in the pre-training stage of some foundation models. If so, will the benchmarking analysis for the frozen one fair?

### Questions
Please see my weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
