# SpaceGNN: Multi-Space Graph Neural Network for Node Anomaly Detection with Extremely Limited Labels

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Node Anomaly Detection (NAD) has gained significant attention in the deep learning community due to its diverse applications in real-world scenarios. 
Existing NAD methods primarily embed graphs within a single Euclidean space, while overlooking the potential of non-Euclidean spaces. 
Besides, to address the prevalent issue of limited supervision in real NAD tasks, previous methods tend to leverage synthetic data to collect auxiliary information, which is not an effective solution as shown in our experiments.
To overcome these challenges, we introduce a novel SpaceGNN model designed for NAD tasks with extremely limited labels. 
Specifically, we provide deeper insights into a task-relevant framework by empirically analyzing the benefits of different spaces for node representations, based on which, we design a Learnable Space Projection function that effectively encodes nodes into suitable spaces.
Besides, we introduce the concept of weighted homogeneity, which we empirically and theoretically validate as an effective coefficient during information propagation. This concept inspires the design of the Distance Aware Propagation module. 
Furthermore, we propose the Multiple Space Ensemble module, which extracts comprehensive information for NAD under conditions of extremely limited supervision. Our findings indicate that this module is more beneficial than data augmentation techniques for NAD. Extensive experiments conducted on 9 real datasets confirm the superiority of SpaceGNN, which outperforms the best rival by an average of 8.55% in AUC and 4.31% in F1 scores.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to address two problems of existing methods in node anomaly detection, Euclidean space only and limited supervision. The authors propose SpaceGNN, consisting of Learnable Space Projection, Distance Aware Propagation, and Multiple Space Ensemble. Both theoretical analysis and experimental results demonstrate the effectiveness of the proposed methods.

### Strengths
- The paper proposes to adopt ensemble of multiple spaces with different curvature in the task of node anomaly detection, which is novel and effective.
- The paper offers empirical and theoretical analysis to illustrate the soundness of the proposed method. 
- The paper provides experimental results to prove the effectiveness of the proposed method.

### Weaknesses
 - The paper has no details on what $\kappa$ is like after learning.
- The Multiple Space Ensemble may increase the computational complexity. There is neither theoretical analysis nor efficiency experiments to show how much additional cost is compared to a single model.
- The authors have not released code for reproducibility.
- Although the paper is understandable, there are several minor presentation issues that reduce readability:
  - The captions of figures are usually at the bottom of the figure instead of on the top in ICLR format.
  - The sections in the Appendix are not necessarily subsections in a single Section A.
  - The abbreviation of Multiple Space Ensemble (MSE) may be confusing to the audience and can be misinterpreted as another commonly used term Mean Squared Error.
  - Line 281: avoid in-place operation to $H^l$
  - Line 313: $s_{ij}$ is not clear defined
- Evaluation metrics: existing **supervised** benchmark GADBench adopts AUC, AUPRC, and Rec@K. It is not convincing to have a different metric.
- Dataset split: the semi-supervised setting in GADBench has 20 positive labels (anomalous nodes) and 80 negative labels (normal nodes) for both the training set and the validation set in each dataset, which is not so different from 50/50 in authors' setting. The public split should be used.

### Questions
- GADBench adopts AUC, AUPRC, and Rec@K as metrics for comprehensive evaluation. Is there any particular reason you use AUC and F1 instead?
- GADBench also provides a semisupervised setting with limited labels. Instead of using a random split, it will be more convincing and reproducible to run experiments on the public split provided by GADBench.
- Line 292 claims $\kappa$ is learnable, but line 405 seems to restrict $\kappa$ either positive or negative.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies the node classification problem by ensembling embeddings from multiple spaces.

### Strengths
S1. This paper includes theoretical analyses to show the rationale of the proposed method.

S2. This paper includes many datasets and comprehensive baseline methods.

### Weaknesses
W1. I think this paper has two important focuses: (1) the anomaly detection task and (2) extremely limited samples. However, after reading the whole methodology section, my personal impression is that the proposed method is designed for a regular binary classification task. I suggest the authors emphasize more on which designs are specialized for few-shot samples and what makes this proposed method specialized for an anomaly detection problem, compared to a regular binary classification task.

W2. This paper includes 4 theorems in total, but I found that theorems 3 and 4 are very general theorems, regarding the general ensemble methods for cross-entopy losses, which is irrelevant to the node anomaly detection task. Also, to be frank, I think they are a bit trivial because they are very straightforward and might not be appropriate to be termed as "theorems" (maybe propositions).

W3. Another concern of this paper is its writing. I tried to understand the whole model architecture through the equations in Section 4 but found some notations that were missing or had not been introduced appropriately. Also, it looks like most critical equations are not numbered. I suggest numbering them so they can be quoted when two equations are closely working. I will name a few:

W3.1 I found the distance is defined in line 236, but it looks like it is not being used in Eqs between lines 281 and 286.

W3.2 Eq. 405 defines the ensemble of models, which is the sum of several functions, but it is unclear how this "addition" operation works for several functions. Do you mean the output of every function from line 286 is added together?

### Questions
Please check the weaknesses I mentioned.

### Soundness
3

### Presentation
2

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
This paper studies the problem of Node Anomaly Detection when the training data is as small as 50. The authors design a Learnable Space Projection function that effectively encodes nodes into suitable spaces, and a Multiple Space Ensemble module to extracts comprehensive information for NAD under conditions of extremely limited supervision. The most surprising result is that it is more beneficial than data augmentation techniques.

### Strengths
1. The method requires very limited training samples, which is a promising property in anomaly detection where anomaly training data is limited.

2. The paper is well-organized, with each section (subsection) clearly stating the intuition along with a solid derivation. 

3. Baselines and datasets are sufficient. SpaceGNN consistently outperforms 8 baselines on 9 datasets, which demonstrates the effectiveness of the paper.

### Weaknesses
1. SpaceGNN has demonstrated its superior performance under low-resource conditions. How about the performance when more training data are available? This experiment may make SpaceGNN a more general and practical algorithm.

### Questions
How about the performance when more training data are available?

### Soundness
3

### Presentation
3

### Contribution
3
