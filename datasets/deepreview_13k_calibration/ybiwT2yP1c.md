# BIRB: A Generalization Benchmark for Information Retrieval in Bioacoustics

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The ability for a machine learning model to cope with differences in training and deployment conditions---e.g. in the presence of distribution shift or the generalization to new classes altogether---is crucial for real-world use cases. However, most empirical work in this area has focused on the image domain with artificial benchmarks constructed to measure individual aspects of generalization. We present \Birb\footnote{\url{www.audubon.org/news/when-bird-birb-extremely-important-guide}}: a generalization Benchmark for Information Retrieval in Bioacoustics, a complex benchmark centered on the retrieval of bird vocalizations from passively-recorded datasets given focal recordings from a large citizen science corpus available for training. We propose a baseline system for this collection of tasks using representation learning and a nearest-centroid search. Our thorough empirical evaluation and analysis surfaces open research directions, suggesting that \Birb fills the need for a more realistic and complex benchmark to drive progress on robustness to distribution shifts and generalization of ML models.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a benchmark to measure the generalization capabilities of bird vocalization detection models.
The benchmark is composed of existing datasets in the field, one large-scale upstream (i.e. training) dataset and 7 small-scale downstream (evaluation) datasets, which overall evaluate generalization against several challenges, such as domain shift, label shift, limited data and class imbalance.
Models are trained on the upstream dataset and used as "embedding models" (i.e. feature extractors) to solve retrieval tasks using a few labeled instances on the downstream datasets.
7 recent baseline models are evaluated on this benchmark, including linear models trained on handcrafted features and deep embedding models with EfficientNet, Conformer and Transformer architectures.
Results show that domain-shift is one of the most challenging generalization factor.

### Strengths
- The benchmark is a nice real-world application on measuring generalization in the field of bioacoustics, which could be interesting for practitioners.
- Evaluation protocol is simple to follow/apply, i.e. models are used as feature extractors and the task is simple retrieval.
- A decent number of baselines already evaluated in this setting.

### Weaknesses
## Concerns on the evaluation protocol
- The evaluation benchmark retrieves relevant samples from a downstream dataset given a query, and it allows reusing class embeddings for queries learned during training. I'm not sure to get this point. If the label of a query is known, then what is the point of retrieving samples from a dataset? We already know the answer. The use of class embeddings from training time as queries is particularly concerning, as it conflates the evaluation of the model's generalization ability with its memorization of training data. This approach doesn't adequately test the model's capacity to generalize to unseen data distributions, which is a primary goal of the benchmark.
- Regardless, it would be nice to report results where none of the class embeddings from training time is used when evaluating the models. Because, one of the generalization aspects posed by the datasets is domain-shift, and it is not clear how to measure domain-shift when query embeddings come from training dataset (rather then being embedded at test time using downstream dataset images).

## Comments on datasets
- I wonder if there is a universal class taxonomy which encapsulates all the classes in all the datasets. For instance, in standard vision datasets (like ImageNet, MS-COCO), classes come from different ontologies/granularities and matching those classes is far from being trivial. To measure "label shift", it is essential to know which classes have been seen during training vs at test time (i.e. seen and unseen classes).
- Also, when measuring label shift, what is the semantic relation (due to their granularity) between seen and unseen bird classes? The semantic relationship between classes, such as whether they are closely related species or from different families, can significantly impact the difficulty of transfer learning. This should be considered when analyzing label shift.
- Is it possible to evaluate domain-shift while fixing label-shift? For instance, seen and unseen classes being equal, whereas recordings being focal vs passive.

## Comments on the paper overall
- Given that this is a benchmark paper, and that not everybody is super familiar with the domain (bioacoustics), I would expect a more direct and clear explanation of the task being solved, the types of input given to the network, etc. In that sense the paper is not easy to understand.

### Questions
I would like the authors to address the weaknesses I listed above.
My main concerns are related to soundness of the evaluation protocol.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces BIRB, a benchmark for bioacoustics, addressing challenges in machine learning generalization. BIRB focuses on a retrieval task where models are trained on an upstream dataset and tested on retrieving vocalizations from a different corpus. It assesses out-of-distribution generalization, few-shot learning, and robustness to class imbalances. The benchmark provides a baseline system using a nearest-neighbor search for efficient evaluation. BIRB has practical implications for bioacoustics research and large-scale data processing, offering a real-world and complex evaluation platform for machine learning models in bioacoustics.

### Strengths
1. The paper introduces the BIRB benchmark, which is a novel and comprehensive benchmark designed for evaluating model generalization in the field of bioacoustics. The paper's originality lies in its approach to formulating retrieval tasks for bird vocalizations, capturing real-world complexities, and addressing generalization challenges specific to this domain. 
2. Moreover, this work's strength lies in its use of publicly available, high-quality bioacoustic datasets, such as Xeno-Canto and passively collected soundscape datasets. 
3. This paper's primary contribution is in the proposed benchmark, which opens up opportunities for researchers to explore and innovate in the field of bioacoustics. While the proposed method (baseline) is not the central focus, it provides a practical starting point for conducting retrieval tasks within the benchmark.

### Weaknesses
1. While the paper primarily focuses on introducing the benchmark, it could benefit from more innovative approaches or methodologies for retrieval tasks. I think it's important to inspire researchers with novel ideas for addressing the challenges in bioacoustics, beyond providing a baseline model.
2. The paper could be enhanced by a more extensive comparative analysis of different approaches or models for the tasks presented in the benchmark. Currently, it provides results for a set of baseline models but does not explore alternative methodologies.  
3. This work provides detailed results but could improve the interpretation of these results. For instance, it mentions that there's a significant difference in performance between deep models trained on XC upstream data and models pre-trained on AudioSet, but it doesn't delve into the reasons behind this discrepancy or suggest potential solutions.
4. The paper employs ROC-AUC as its primary evaluation metric. While this is common in information retrieval tasks, it would be beneficial to consider additional evaluation metrics that are specific to bioacoustics and relevant to the benchmark's objectives.

### Questions
1.  The paper mentions performance differences between models pre-trained on AudioSet and those trained on XC upstream data. Could the authors offer more insights into why this divergence occurs and what it might imply for domain adaptation in bioacoustics?
2. Are there any specific experiments, ablations, or investigations that the authors plan to conduct in the future with the benchmark, beyond the preliminary baseline models presented in this paper?
3. Are there specific implications for domain adaptation, representation learning, or transfer learning from the challenges in bioacoustics and the proposed benchmark?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is benchmarking a much more complicated evaluation scenario for modern machine learning algorithm. Specifically, it designs a information retrieval task based on bird vocalizations. Several existing public datasets are involved to create this benchmark. Accordingly, the author also provide several baselines for this benchmark. The machine learning generalization ability and robustness property are expected to be evaluated based on this real-world fashion benchmark.

### Strengths
1. The research topic is attractive to me. Considering a real practical scenario for current machine learning field is reasonable and necessary.

2. The collected datasets are sufficient and provided baselines cover some recent popular methods.

### Weaknesses
I mainly concern the presentation of this paper. Given the current machine learning field not familiar with the bird-based bioacustics, more background information should be included before introducing the benchmark. Similarly, the benchmark itself is also unclear. The task should be better to illustrate with a figure and the figure of baseline system is not informative. Some relevant information in supplementary may be moved into the main draft to elaborate the benchmark. In addition, for the experimental analysis, corresponding discussion and visualizations are necessary for a better description.

### Questions
Please refer to the weakness for my concerns and most of the paper format should be improved for a better illustration to readers. I recognize the research contribution of this paper but current draft is a bit unclear for a good publication. The author may want to significantly revise the paper draft to clarify this benchmark work.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a benchmark (BIRB) centered on the retrieval of bird vocalizations. It contains multiple passively-recorded datasets and a baseline system for these tasks are proposed. The benchmark aims for the direction of ML models' robustness and generalization ability.

### Strengths
1. The paper proposes a new series of datasets, covering various aspects of challenging ML problems, especially in the field of acoustic data shift.
2. A pipeline for performance evaluation is also proposed. The authors find that increasing the size of networks does not translate to improved generalization, which is an interesting phenomenon. 
3. Various models are tested and benchmarked on the datasets.

### Weaknesses
While the topic of this paper is intriguing, I have some concerns that lowers my score:
1. The paper claimed the finding of "increasing the size of networks does not translate to improved generalization". However, no reason for this phenomenon is given.
2. Many evaluation datasets are proposed. Does each of these datasets emphasize something (e.g. Label shift influence, long-tail distribution)? If not, they lack of research potential to be set as a part of benchmark dataset. A good example for constructing evaluation set would be ImageNet-C[1].
3. Throughout the paper, no example dataset sample is provided to give intuition of how the dataset is constructed.

### Questions
I also have the following questions:
1. Is it a reasonable practice to use existent public datasets to construct one's own dataset? Are the credits properly given?
2. What does BIRB stand for? Apologies in advance if I missed it in the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
