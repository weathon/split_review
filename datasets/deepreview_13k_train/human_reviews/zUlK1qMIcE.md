# Active partitioning: inverting the paradigm of active learning

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
\label{sec_Abstract}

Datasets often incorporate various functional patterns related to different aspects or regimes, which are typically not equally present throughout the dataset. We propose a novel, general-purpose partitioning algorithm that utilizes competition between models to detect and separate these functional patterns. This competition is induced by multiple models iteratively submitting their predictions for the dataset, with the best prediction for each data point being rewarded with training on that data point. This reward mechanism amplifies each model’s strengths and encourages specialization in different patterns. The specializations can then be translated into a partitioning scheme. The amplification of each model’s strengths inverts the active learning paradigm: while active learning typically focuses the training of models on their weaknesses to minimize the number of required training data points, our concept reinforces the strengths of each model, thus specializing them. We validate our concept -- called active partitioning -- with various datasets with clearly distinct functional patterns, such as mechanical stress and strain data in a porous structure. The active partitioning algorithm produces valuable insights into the datasets’ structure, which can serve various further applications. As a demonstration of one exemplary usage, we set up modular models consisting of multiple expert models, each learning a single partition, and compare their performance on more than twenty popular regression problems with single models learning all partitions simultaneously. Our results show significant improvements, with up to 54\% loss reduction, confirming our partitioning algorithm’s utility.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose to partition the dataset by using predictions from multiple models.

During training, each sub-model is allowed to submit their predictions for all points in the datasets. The datapoints are then assigned to the sub-model with the best performance, and the sub-model is trained only these datapoints. As training proceeds, the hope is that the process induces specialization in the models, which is then translated into a partitioning. There is some connection to active learning, where datapoints are chosen for which the model is most uncertain about; whereas here, the datapoints are assigned to the model with best performance.

Experimental results are reported on 6 datasets, 3 of which are unidimensional datasets.

### Strengths
* The claims of the paper are easy to understand (though I dont quite believe them, see below)
* The experimental results one of the datasets was interesting to read

### Weaknesses
TLDR; I dont think the contributions of the paper meet the conference bar.

* There are lots of existing work on MOEs, this paper feels like re-inventing them from scratch. There is minimal mention to existing literature, no comparisons.

* The experimental results are quite unconvincing. The scale of the datasets are just too small. Why not have larger capacity models which can learn more. The scale of the datasets + model sizes (the latter I suspect is also small), makes me question if partitioning the dataset is needed at all.

* Even if we assume that partitioning is required, why not compare with simpler baselines like run clustering algorithm first, and then train independent models on the clusters?

### Questions
Please see weakness above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses a new learning paradigm called active partitioning, aiming to improve model performance by leveraging competition among models. The key idea is to separate and detect distinct functional patterns within datasets by rewarding models that provide the best predictions for specific data points with additional training on those points. This encourages each model to specialize in certain patterns, allowing the datasets to be divided into specialized partitions. Unlike traditional active learning, which focuses on training models based on their weaknesses to minimize training data, active partitioning emphasizes strengthening models' specialties. The approach is tested on datasets with distinct patterns (e.g., stress and strain data), showing how models can learn different partitions. The results demonstrate improved performance, with a 54% reduction in loss compared to single models handling the entire dataset, validating the effectiveness of active partitioning.

### Strengths
1. Interesting new paradigm. Even though it's similar to the ideas of mixture of experts which are well-studies in current LLMs era, the idea of applying multiple experts and partitioning datasets are interesting in active learning literatures.
2. The number of datasets in experiments section is impressive, including 2 two-dimensional datasets and 22 datasets from UCI Machine Learning Repository.

### Weaknesses
1. Lack of related works: The author mentions mixture of experts algorithm in Section 2.2. There is a rich body of related works regarding applications of mixtures of experts on LLMs [1, 2, 3]. The paper fails to adequately discuss the nuances of existing mixture of experts approaches, particularly in the context of large language models, where routing mechanisms and expert specialization are actively researched. The current discussion lacks depth in differentiating the proposed method from existing techniques, especially those employing gating networks or other dynamic routing strategies.

2. Lack of theoretical justifications. Most of partitioning experiments have theoretical guarantees and more theoretical understandings would be helpful in understanding this algorithm. The paper lacks a theoretical framework to analyze the convergence properties of the proposed active partitioning method. Specifically, there is no discussion on whether the partitioning process is guaranteed to converge to a stable solution, or how the choice of reward function impacts the final partitioning. A rigorous analysis of the algorithm's behavior under different conditions is needed to establish its reliability.

3. Datasets are too simple and small scale. Code is not open-sourced. Datasets selected are mainly from UCI Machine Learning Repository where most of them are low-dimensional and small scale in terms of datasets size. Since there are no theoretical justifications, experiments should not be limited to regression tasks. The experimental evaluation is limited by the use of relatively small and low-dimensional datasets from the UCI Machine Learning Repository. The lack of experiments on larger, more complex datasets, such as those found in computer vision or natural language processing, makes it difficult to assess the scalability and generalizability of the proposed method. The absence of open-sourced code also hinders reproducibility and further investigation by the research community.

4. Ablation study of network architectures. The tasks should be not limited to regressions settings and more experiments regarding various network architectures should be discussed. The authors claim active partitioning paradigm is better than active learning but many active learning algorithms have experiments showcasing there optimality across multiple networks architectures. For instance [4] performs experiments across network architectures including networks similar to LeNet and ResNet-18. The evaluation lacks a thorough ablation study on the impact of different network architectures on the performance of active partitioning. The paper should explore how the method performs with various network architectures, including convolutional neural networks and transformers, to demonstrate its robustness and applicability across different model families. The current experiments are limited to regression settings, and the paper would benefit from exploring classification tasks to further validate the method's generality.

### Questions
No

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
4

### Summary
The paper introduces an algorithm that leverages competition between models to partition datasets based on distinct functional patterns. Unlike traditional active learning, which focuses on minimizing data for weak areas, this approach amplifies the strengths of models, promoting specialization. The modular models, consisting of multiple expert models each focused on learning a specific partition, demonstrate significant improvements over a single model.

### Strengths
1. The writing in this paper is easy to understand, and the use of flowcharts and other visuals makes it easier to grasp the core methods and concepts.

2. The authors provide pseudocode and detailed parameter settings in the paper, and the code is included in the supplementary materials, ensuring the reproducibility of the work.

### Weaknesses
1. The number of dataset partitioning baselines compared is insufficient. In the related work section, the authors discuss other dataset partitioning methods, while the authors did not compare active partitioning with any of these methods. The authors may supplement the baselines or explain why there is no comparison between them.

2. The modular model tends to underperform compared to a single model when the split dataset using active partitioning exhibits one coherent pattern or when multiple patterns have significant overlap. A related work [1] that first attempts to solve a problem with a single network and handles the unsolved portion(s) of the input domain recursively seems to be superior to the proposed method.

3. The authors claim that the novelty of this work lies in “the development of a flexible partitioning method through the competition of entire models,” but what advantages does this approach offer compared to previous dataset partitioning methods? The motivation behind the proposed method needs further elaboration and clarification.

4. The authors may provide a more detailed introduction to active learning and elaborate on how the proposed method invests in the paradigm of active learning.

5. The paper is lack of detail in the dataset partitioning phase. The authors mention that competing models might exhibit differences, such as using ‘wider neural networks or smaller learning rates’ for different patterns, but they do not provide concrete details on how model diversity is implemented during this stage. It would be beneficial to elaborate on how these variations are chosen and how they impact the effectiveness of the partitioning process.

6. The authors sometimes mix in-text and parenthetical citations throughout the related work section, such as "Wu et al.adapted ... (Wu et al., 2004)."

### Questions
1. I would like to know how much time the active partitioning and training of modular model will cost compared to training a single model.

2. I wonder whether the competing models used for active partitioning can be directly used to combine a modular model.

### Soundness
2

### Presentation
2

### Contribution
2
