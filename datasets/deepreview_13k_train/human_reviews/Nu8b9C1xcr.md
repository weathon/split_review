# CardBench: A Benchmark for Learned Cardinality  Estimation in Relational Databases

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Cardinality estimation is crucial for enabling high query performance in relational databases. Recently learned cardinality estimation models have been proposed to improve accuracy
  but there is no systematic benchmark or datasets which allows researchers to evaluate the progress made by new learned approaches and even systematically develop new learned approaches.
  In this paper, we are releasing a benchmark, containing thousands of queries over 20 distinct real-world databases
  for learned cardinality estimation. In contrast to other initial benchmarks, our benchmark is much more diverse and  can be used for training and testing learned models systematically. 
  Using this benchmark, we explored   whether learned cardinality estimation can be transferred to an unseen dataset in a zero-shot manner. We trained GNN-based and
  transformer-based models to study the problem in three setups: 1-) instance-based, 2-) zero-shot, and 3-) fine-tuned.
  
  Our results show that while we get promising results for zero-shot cardinality estimation on simple single table queries; as soon as we add joins, the accuracy drops. 
  However, we show that with fine-tuning, we can still utilize pre-trained models for cardinality estimation, significantly reducing training overheads compared to instance specific models.
  We are open sourcing our scripts to collect statistics, generate queries and training datasets to foster more extensive research, also from the ML community on the important problem of cardinality estimation and in particular improve on recent directions such as pre-trained cardinality estimation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a benchmarking framework aimed at cardinality estimation within relational databases, using advanced learning methods like GNNs and Transformers.

### Strengths
The paper details a systematic data preparation process, including SQL query generation, dataset statistics calculation, and annotated query graph creation, which offers a replicable approach for dataset-agnostic testing.

The paper’s emphasis on creating a model that can generalize to unseen datasets is a unique and relevant shift in the CE field, considering the increasing need for adaptable models in dynamic data environments.

### Weaknesses
1. The authors said that they have collected data from 20 datasets with diverse sources compared with existing benchmarks. But I can't see this comparsion to conclude that how novel this part is. It deserves detailed discussion.

2. Although it includes single-table and multi-table queries, it lacks support for deeply nested and highly complex SQL queries, which are common in real-world database applications. This limitation in query complexity could lead to suboptimal model performance in practical scenarios.

3. Only q-error is used as the main evaluation metric, which may not fully capture model performance. Additional dimensions, such as runtime and resource consumption, could provide a more comprehensive assessment.

### Questions
see weakness above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces CardBench, a benchmark for evaluating learned cardinality estimation models in relational databases. Cardinality estimation is vital for query optimization, but existing models lack a comprehensive benchmark for systematic evaluation. CardBench provides this with extensive queries across 20 real-world databases. The study evaluates GNN and transformer-based models in instance-based, zero-shot, and fine-tuned setups, highlighting challenges in zero-shot accuracy with complex queries but demonstrating the potential of fine-tuning pre-trained models. By releasing scripts and data, the authors encourage further research, showing that pre-trained models can achieve high accuracy with reduced training overhead.

### Strengths
S1: Cardinality estimation is critical for the database community.

S2: This paper proposes several datasets, which will be useful for academic and industry communities.

S3: Zero-shot cardinality estimation seems to be useful.

### Weaknesses
W1: The details of the datasets are unclear. Specifically, the paper lacks a thorough description of the data generation process, including the distributions of cardinalities, the complexity of join patterns, and the presence of any skew in the data. Without this information, it is difficult to assess the generalizability of the benchmark.

W2: The baselines are too weak and lack state-of-the-art and representative cardinality estimation baselines. The paper primarily focuses on GNN and transformer-based models, but it does not compare against other established techniques such as sampling-based methods, histograms, or other learned models that have shown strong performance in cardinality estimation. This makes it hard to evaluate the proposed models' relative performance.

W3: The experiments lack detailed analysis of the proposed models regarding the zero-shot setting. While the paper mentions zero-shot performance, it does not provide an in-depth analysis of the factors affecting zero-shot accuracy, such as the complexity of queries, the presence of unseen join patterns, or the impact of different pre-training strategies. A more thorough investigation is needed to understand the limitations and potential of zero-shot cardinality estimation.

### Questions
D1: This paper proposes several synthetic cardinality estimation datasets. But what are the patterns and distributions in these datasets?

D2: Why are these datasets comprehensive and diverse? From a database view, are these proposed datasets complete? It is better to add more justifications.

D3: This paper proposes zero-shot estimation but only investigates limited GNNs. In cardinality estimation, whether sampling-based approaches or summary-based approaches, all work under a zero-shot setting. These approaches do not need any training instances. But this paper does not explore these approaches.

D4: Even for GNN-based baselines, they are too simple. 

D5: How about the training time and inference time compared with the time of the training-free methods? If the training-free methods are better than the proposed method, it is meaningless to propose a pre-trained model.

D6: This paper only explores the performance on cardinality estimation error. But how to prove it can achieve better performance on downstream applications? It is better to deploy this model on a real database system to see its improvements.

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
3

### Summary
This paper proposes the cardbench, a benchmark dataset for cardinality estimation in relational databases, which contains over 20 distinct real-world databases. This proposed dataset shows clear diverse and proposes several baseline models including the GNN and transformer modules to form a benchmark evaluation of this benchmark dataset.

### Strengths
+ A large-scale benchmark dataset for Cardinality Estimation
+ Good evaluations and benchmark analyses.
+ Clear organizations and easy to read.

### Weaknesses
 + My major concern is about the benchmark contributions to this research field. In the related work section, the authors talked about how existing benchmarks only contain one or two datasets which is insufficient for testing pretraining models. Thus my question is, how does this proposed benchmark test these pretrained models? It seems the authors only test typical GNN or Transformer architectures. 
This dataset seems not to be comprehensive as a benchmark in this research field.
+ Besides, gathering different datasets or re-organizing them also may help the aforementioned problems. Why is this proposed benchmark unique? I am concerned about the realistic usage and if this is a real problem for the community.
+ There are also several minor issues, including the presentations for the Sect. 3 and the table format for table 1. These presentations could be improved.

### Questions
Please refer to the weakness section and I am concerned about the realistic usage of this proposed benchmark or it is an ``made" problem.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents CardBench, a benchmark for evaluating learned cardinality estimation models in relational databases. CE is vital for optimizing query performance, yet traditional methods often lack accuracy. CardBench offers a diverse set of datasets and queries, featuring hundreds of thousands of queries across 20 real-world datasets, enabling systematic assessments of new CE approaches.
Experiments with GNN and transformer-based models were conducted under three setups: instance-based, zero-shot, and fine-tuning. While zero-shot estimation shows promise for simple queries, its accuracy declines with complex joins. However, fine-tuning pre-trained models can enhance performance significantly, reducing training costs.
The authors emphasize that CardBench will lower barriers for research in learned CE and encourage further exploration from the machine learning community.

### Strengths
- CardBench includes a broad range of datasets, 20 distinct real-world datasets, that provide a more comprehensive evaluation framework for learned cardinality estimation models compared to existing benchmarks.
- The benchmark facilitates systematic testing of various learned CE approaches, allowing researchers to assess model performance comprehensively. By open-sourcing the benchmark, query generator, and associated scripts, the authors foster collaboration and further research in the field, lowering barriers for other researchers to experiment with learned cardinality estimation.
- The paper is clearly written and organised.

### Weaknesses
 - There are several typos that need to be corrected in future revisions.
- It would be beneficial to include more detailed statistical experimental results. While boxplots effectively illustrate the distribution of results, providing exact values enables precise comparisons between data points.
- The descriptions of the GNN and Transformer models used in the experiments are lacking. More detailed explanations would help readers gain better insights into the methodologies.
- The paper should discuss how the performance of other state-of-the-art methods compares on CardBench, which would provide context and strengthen the findings.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
