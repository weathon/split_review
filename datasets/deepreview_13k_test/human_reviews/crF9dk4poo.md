# Interpretable Deep Clustering

- Decision: Reject
- Scores: 8, 6, 5

## Abstract
Clustering is a fundamental learning task widely used as a first step in data analysis. For example, biologists use cluster assignments to analyze genome sequences, medical records, or images. Since downstream analysis is typically performed at the cluster level, practitioners seek reliable and interpretable clustering models. We propose a new deep-learning framework for tabular data that predicts interpretable cluster assignments at the instance and cluster levels. First, we present a self-supervised procedure to identify the subset of the most informative features from each data point. Then, we design a model that predicts cluster assignments and a gate matrix that provides cluster-level feature selection. Overall, our model provides cluster assignments with an indication of the driving feature for each sample and each cluster. We show that the proposed method can reliably predict cluster assignments in synthetic and tabular biological datasets. Furthermore, using previously proposed metrics, we verify that our model leads to interpretable results at a sample and cluster level.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors develop a novel deep clustering and feature selection method. The proposed model employs a two-stage approach. In the first stage, a Gating Network and an autoencoder are used for self-supervised learning of latent representations and sample-level informative features. In the second stage, a clustering head is trained to predict cluster assignments based on these latent embeddings. The model aims to provide both instance-level and cluster-level explanations by selecting a subset of features that are most informative for each cluster. The paper validates the model's performance through a series of experiments conducted on synthetic datasets, including well-known benchmarks like MNIST, FashionMNIST, and CIFAR10. The experiments show the model outperforms other clustering strategies while maintaining interpretability. The paper also includes ablation studies to understand the impact of various components of the model on its performance.

### Strengths
Comprehensive Experiments: the paper conducts a wide range of experiments across multiple datasets, including synthetic datasets, MNIST, FashionMNIST, and CIFAR10. A exploration of the time it takes to run the the method according to dataset size is also provided. 

Interpretability Focus: one of the key strengths of the paper is its focus on interpretability. The model aims to provide both instance-level and cluster-level explanations, which is crucial for understanding the model's decisions and could be particularly useful in sensitive applications.

Innovative Approach: the paper proposes a novel two-stage approach that combines self-supervised learning for feature selection and a clustering head for cluster assignment. This is an innovative way to tackle the problem and could inspire future research in this area.

Ablation Studies: the paper includes ablation studies to understand the impact of various components of the model, confirming that are components of the method are, indeed, relevant to its performance.

### Weaknesses
The paper addresses everything I would expect in a clustering paper, especially with the interpretability focus.
Perhaps the only weakness would be the lack of a deeper discussion on interpretability and its different perspectives in machine learning, but that does not decrease the quality of the paper.

### Questions
-

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an Interpretable Deep Clustering model that predicts an informative feature set for improved interoperability. Leveraging a self-supervised reconstruction task, the method employs stochastic gates to learn instance-level feature selection, which can be extended to the cluster-level form. The two-stage training process involves losses encompassing reconstruction errors and various constraint terms. Overall, the paper offers valuable insights and demonstrates its superiority in terms of performance and interoperability.

### Strengths
1. The paper is well-structured, featuring clear logic and technical explanations that allow readers to easily follow the authors' design. Additionally, the manuscript is well-written overall, demonstrating proficient English grammar and adhering to a formal writing style that aligns with academic standards for technical manuscripts.
2. The proposed method is technically sound and demonstrates impressive performance on both synthetic and real datasets.
3. The paper's approach to designing a clustering model with a focus on interoperability offers an intriguing perspective.

### Weaknesses
1. The paper's novelty appears to be somewhat incremental, as it combines existing unsupervised feature selection (stochastic gates) with deep clustering, lacking significant novel elements.
2. The main design of the model lacks a theoretical guarantee. For instance, the reasoning behind choosing an autoencoder (AE) over other self-supervised tasks, such as contrastive learning, requires clarification.
3. The method's generalizability to unseen data is not adequately explained. Eq. (6) suggests high computational complexity, necessitating a discussion on the complexity for better understanding.
4. The experiment comparison seems biased. While the proposed method employs strong feature transformation by DNN, competitors like k-means do not. Hence, a fair comparison with state-of-the-art deep clustering models is essential.
5. It would be beneficial to discuss the model's performance on a large-scale dataset to provide a comprehensive evaluation.
6. The subscripts in Eq. (6) should be carefully reviewed for accuracy.

### Questions
Please see the cons for details.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposed a new deep-learning framework for tabular data that predicts interpretable cluster assignments at the instance and cluster levels. They also  validated the performance in both synthetic and tabular biological datasets. However, this article overall did not meet the requirements of ICLR.

### Strengths
1. The paper is easy to follow
2. The experiments are comprehensive

### Weaknesses
1. The motivation is not clear, I don not understand what is interpretable clustering model and why we need  interpretable clustering model.
2. The overall method is just the combination of existing approaches, the novelty is limited
3. I don not agree with the authors the empirical diversity, faithfulness and uniqueness can represent  interpretability
4. The manuscript was not well prepared. It contains obvious typos, such as the citation "?" in third line of page six
5. The improvement in real-world dataset is not significant

### Questions
1. The motivation is not clear, I don not understand what is interpretable clustering model and why we need  interpretable clustering model.
2. The overall method is just the combination of existing approaches, the novelty is limited
3. I don not agree with the authors the empirical diversity, faithfulness and uniqueness can represent  interpretability
4. The manuscript was not well prepared. It contains obvious typos, such as the citation "?" in third line of page six
5. The improvement in real-world dataset is not significant

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
