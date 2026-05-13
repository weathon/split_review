# Calibrated Dataset Condensation for Faster Hyperparameter Search

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Dataset condensation can be used to reduce 
the computational cost of training multiple models on a large dataset by condensing the training dataset into a small synthetic set. 
State-of-the-art approaches rely on matching model gradients between the real and synthetic data.
However, there is no theoretical guarantee on the generalizability of the condensed data: data condensation often generalizes poorly \emph{across hyperparameters/architectures} in practice.
In this paper, we consider a different condensation objective specifically geared toward \emph{hyperparameter search}. 
We aim to generate a synthetic validation dataset so that the validation-performance rankings of models, with different hyperparameters, on the condensed and original datasets are comparable.
We propose a novel \emph{hyperparameter-calibrated dataset condensation} (\ouralgo) algorithm, which obtains the synthetic validation dataset by matching the \emph{hyperparameter gradients} computed via implicit differentiation and efficient inverse Hessian approximation.
Experiments demonstrate that the proposed framework effectively maintains the validation-performance rankings of models and speeds up hyperparameter/architecture search for tasks on both images and graphs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel method for optimizing a synthetic validation set to align the model performance rankings between the condensed and original datasets. To achieve this, the authors introduce a hypergradient alignment objective function and devise an algorithm that employs implicit differentiation and inverse Hessian approximation. Through a comprehensive series of experiments conducted on datasets in both image and graph domains, the authors effectively demonstrate how their optimized synthetic dataset enhances the results of architecture and hyperparameter search when using the condensed dataset.

### Strengths
- The paper introduces a novel approach to condensing datasets for architecture and hyperparameter search.
- This paper effectively tackles the important challenges within the field of dataset condensation research.
- The primary motivation behind the main objective is compelling.
- The proposed method shows strong performance in architecture and hyperparameter search across various datasets.

### Weaknesses
- Some technical sections of the paper are hard to understand. 
  - On page 5, Definition 2: Is "cos" representing cosine-similarity? If so, why should the term between two hypergradients be zero?
  - In section 5.2 on page 6, how can discrete factors like model depth or kernel size be expanded continuously?
- The process of condensing synthetic validation appears intricate and time-intensive. However, the paper lacks a comprehensive analysis of this procedure.
  - Could you provide information on the time required to optimize the dataset using the HCDC algorithm in experiments, including Table 3?
- Figure 4 doesn't offer a fair comparison of the architecture search. To achieve this, the graph should be revised to include the optimization time for the HCDC algorithm.

typo
- p.2: $\mathcal{T}$ with $\mathcal{T}^{\text{train}}$ -> $\mathcal{T}^{\text{train}}$ with $\mathcal{T}$
- p.6: , We employ -> , we employ
- p.6: ).Specifically -> ). Specifically

### Questions
See the weakness section above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel hyperparameter-calibrated dataset condensation (HCDC) algorithm, to solve the problem of existing dataset distillation methods being difficult to migrate to models other than predefined ones. The validation set is condensed through hyperparameter gradient matching. The proposed method retains the ranking information on different hyperparameters and accelerates the search for hyperparameter and architecture.

### Strengths
1. The hyperparameter gradient matching proposed in the paper is relatively novel and provides new ideas for improving the generalization performance of dataset distillation methods;
2. The paper provides a solid theoretical analysis and a clear explanation of the research issues;
3. The proposed method achieves good results on image datasets and graph datasets.

### Weaknesses
1. The paper does not explain some concepts mentioned for the first time, such as "supernet";
2. Lack of some ablation experiments, such as the performance of searching directly by compressing the test set using the dataset distillation method;
3. As a dataset distillation method, there is a lack of comparison with other dataset distillation methods in terms of compression rate and generalization performance.

### Questions
1. In image dataset distillation, is it possible for methods to be applicable to distillation models of different architectures? For example ConvNet, VGG, ResNet, etc.
2. What is the difference between distilling directly on the test set and then using it for hyperparameter search compared to using distilled samples on a randomly selected training set?
3. Do different sampling methods have an impact when sampling from pre-distilled samples?
4. What is the time cost of the method? Is it possible to extend from validation set compression to training set compression?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a different view of data condensation, which is more focused on "hyperparameter search" across multiple architectures. It extends the original data condensation problems into hyperparameter-calibrated data condensation, which has several challenges: nested optimization and continuous hyperparameter search space. The proposed solution works very well compared to prior SOTA methodologies, showing a much higher rank correlation in Table 2. Also, the paper has some examples of its general use cases on image and graph domains.

### Strengths
1. The proposed problem makes sense and is important - this is an initial work focusing on hyperparameter search space in data condensation.
2. The solution shows high-performance improvement in terms of the rank correlation on several domains (image and graph)
3. The paper has a good balance between theoretical analysis and empirical understanding.

### Weaknesses
1. For the image domain, the used datasets are too simple, which has 32x32 pixels and a smaller number of classes. Usually, the hyperparameter search benefit is much higher in large resolution and large class datasets. 

2. The current rank correlation metric is reasonable, but it would be extended to a more fine-granular level. For example, we can calculate the rank correlation for each class and aggregate them on average. This will show how the rank correlation matches with that obtained with the original dataset at the lower granularity.

### Questions
Refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a dataset condensation/distillation method specifically for the application of hyperparameter search. The authors first demonstrate the drawback of existing dataset condensation methods in this area and analyze the inefficiency of a naive solution that involves solving nested optimization. Then, through theoretical analysis, they propose a hyperparameter-calibrated dataset condensation method. The basic idea is to learn a synthetic validation dataset such that hypergradients on hyperparameters can be matched. They also apply effective approximation to further reduce the complexity so that the final algorithm is a first-order one. Experiments validate the effectiveness of the proposed method on both image and graph datasets.

### Strengths
* The research on a dataset condensation method specifically for hyperparameter search is meaningful. One important application of dataset condensation/distillation is to boost the training efficiency of neural network to facilitate researches like NAS. However, as demonstrated by the authors, existing methods fail to do so both theoretically and experimentally.
* The presentation is really good and coherent generally. The authors first demonstrate the drawbacks of existing methods and a naive solution before presenting the final solution, which indicates that the proposed method is well-motivated, reasonable, and interesting.

### Weaknesses
1. Limited evaluation. The experiments are only conducted on small-scale datasets like CIFAR, Cora, Citeseer, Ogbn-arxiv, and Reddit. To better demonstrate the scalability and robustness of the proposed method, experiments on larger datasets like ImageNet, at least subsets of ImageNet or TinyImageNet, are encouraged.
2. Limited Analysis. The authors only focus on the performance on several datasets. The analysis on the algorithm itself is insufficient. Specifically, how does the algorithm compare to the naive solution in Eq. 3 in terms of both performance and efficiency. The authors may consider using a toy dataset for this analysis. After all, the proposed method is an efficient approximation of directly using original datasets. Where the approximation comes from and how much it is are important in a scientific view.
3. I am curious about the details of the method to deal with discrete hyperparameters. The descriptions in Sec. 5.2 and Appendix H are confusing to me. An algorithmic flow is encouraged for better presentation. In addition, are other approaches like Gumbel Softmax applicable?
4. Eq. IFT is an efficient approximation of the hypergradients. It would be better to make this clear in the description. And "=" should not be used in Eq. IFT.
5. Minor: some confusing expersions:
   * "this limitation" in the second paragraph of Introduction: the contents in the previous paragraph is not actually a limitation. And this sentence is incoherent to the last sentence of the previous paragraph.
   * The last two lines in Page 5.
   * Page 6: "For generating $S^{train}$, We ...", "W" here should be lowercase.

### Questions
Please refer to Weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
