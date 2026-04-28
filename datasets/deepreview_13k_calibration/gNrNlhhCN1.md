# FAACL: Federated Adaptive Asymmetric Clustered Learning

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Asymmetric clustering has remained an unexplored problem in Clustered Federated Learning (CFL), diverging from the traditional approach of forming independent, non-interacting clusters. Previous methodologies have been limited to either separating devices with different data quality into distinct clusters or merging all devices into a single cluster, both of which compromise either data utilization or model accuracy. We propose a new federated learning technique where some devices may contribute to the training of the models of other devices, but without enforcing reciprocity, leading to a form of asymmetric clustering.  This is beneficial in a variety of situations including scenarios where it is desirable for a device with high quality data to help train the model of a device with low quality data, but not vice-versa. This method not only enhances data utilization across the devices, but also maintains the integrity of high-quality data. Through a rigorous theoretical analysis and empirical evaluations, we demonstrate that our approach can efficiently find high quality (asymmetric) clusterings for numerous devices, achieving competitive performance metrics on existing CFL benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Authors discuss the clustered learning approach in Federated Learning and relax the following constraints:
1. Number of clusters being fixed (Adaptive)
2. Each device contributes to a single cluster (Adaptive) 
3. Model sharing is reciprocal in nature (Asymmetric)

### Strengths
S1: Introduced asymmetric clustering 
S2: Source code is shared for reproducibility.

### Weaknesses
W1: This comment is in relation to the Section 4.2 and 4.3 -> Some of the related works may need to be studied and probably be included as part of the comparison metrics. [1-2]

W2: How does this handle a newly added device in the Federated Learning? Do we check against all the clusters and find if it supports or not individually or against the clusters only? Does that a performance hit if the clusters are already prepared.  



### Questions
Q1 :  line 053 - “and all existing techniques assume that each device contributes to a single cluster.” - What does this line mean here? And how do address the same in your paper? 

Q2: Does it have the same privacy guarantees as other models proposed in the same vein such as [1] and others. 

Q3: How does the computational complexity compare to other algorithms? 

Q4: How far off is this clustering from ground truth? Additionally is there a comparison again Oracle? [2] 

Q5: Was there an ablation study performed without merging of clusters and just having asymmetric contribution? 

[1] Sattler, Felix, Klaus-Robert Müller, and Wojciech Samek. "Clustered federated learning: Model-agnostic distributed multitask optimization under privacy constraints." IEEE transactions on neural networks and learning systems 32.8 (2020): 3710-3722.

[2] Jothimurugesan, Ellango, et al. "Federated learning under distributed concept drift." International Conference on Artificial Intelligence and Statistics. PMLR, 2023.

### Soundness
2

### Presentation
3

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
This paper proposes a new federated learning technique where some devices may contribute to the training of the models of other devices, but without enforcing reciprocity, leading to a form of asymmetric clustering. This approach not only enhances data utilization across the devices, but also maintains the integrity of high-quality data.

### Strengths
1. The proposed approach tackles the underexplored issue of asymmetric clustering in Clustered Federated Learning, providing a fresh perspective.

2. The experimental results are comprehensive.

### Weaknesses
1. The paper presents a clustered federated learning method; however, it lacks an introduction to the implementation of federated learning (FL) and clustered federated learning (CFL). I recommend including details about the specific training processes and objectives of both FL and CFL in the BACKGROUND section to enhance clarity and context.

2. How can the proposed approach be effectively implemented in real-world scenarios? In practical federated learning settings, it seems challenging to determine whether cluster C2 supports cluster C1. Given that devices do not have visibility into each other's data during training, the primary method for assessing support appears to require multiple rounds of training and testing. This approach could lead to considerable resource inefficiencies.

3. The main operations of the method are presented in algorithmic form in the appendix (e.g., Algorithms 5 and 6). However, it may be more beneficial for readers to understand these concepts if they are described in text form within the main body of the paper.

4. In the experimental setup, there is no detailed information on how the data is divided or the rationale for this division. Different data partitioning methods can impact the final performance of federated learning.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a clustered federated learning method named FAACL, which aims to adaptively cluster devices and dispatch models for each device according to its cluster.

### Strengths
The author provides a theoretical analysis of its proposed cluster strategy.

### Weaknesses
This paper seems to be an incremental work of CFL. The contribution is limited.

This paper is poorly written. E.g., 1) the author should add a figure of framework and workflow. 2) The expression of lines 186-196 seems to detail the contributions and steps of the proposed method, rather than the components. I advise the author to reorganize the expressions.

The author attempts to utilize CFL-based strategy to address the problem of non-IID data. However, the author lacks comparison the proposed method with SOTA tradition federated learning optimization methods [1-4].

The proposed method cannot adapt to the secure aggregation method. The author should analyze the privacy of the proposed method.

The experiments are mainly based on MNIST and its variants. I would like to know how the method performs on more complex datasets, such as ImageNet. Please note that the experimental results show that the proposed method is not effective enough on the cifar10 dataset and is even inferior to the baseline.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
1

### Contribution
2
