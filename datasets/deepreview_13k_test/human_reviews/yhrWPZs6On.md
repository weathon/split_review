# HYBRID GRANULARITY DISTRIBUTION ESTIMATION FOR FEW-SHOT LEARNING: STATISTICS TRANSFER FROM CATEGORIES AND INSTANCES

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Distribution estimation (DE) is one of the effective strategies for few-shot learning (FSL). 
It involves sampling additional training data for novel categories by estimating their distributions employing transferred statistics  (*i*.*e*., mean and variance) from similar base categories.
This strategy enhances data diversity for novel categories and leads to effective performance improvement.
However, we argue that relying solely on coarse-grained estimation at category-level fails to generate representative samples due to the discrepancy between the base categories and the novel categories.
To pursue representativeness while maintaining the diversity of the generated samples, we propose **H**ybrid **G**ranularity **D**istribution **E**stimation (HGDE), which estimates distributions at both coarse-grained category and fine-grained instance levels. 
In HGDE, apart from coarse-grained category statistics, we incorporate external fine-grained instance statistics derived from nearest base samples to provide a representative description of novel categories. Then we fuse the statistics from different granularity through a linear interpolation to finally characterize the novel categories. Empirical studies conducted on four FSL benchmarks demonstrate the effectiveness of HGDE in improving the recognition accuracy of novel categories. 
Furthermore, HGDE can be applied to enhance the classification performance in other FSL methods. The code is available at:
[https://anonymous.4open.science/r/HGDE-2026}](https://anonymous.4open.science/r/HGDE-2026)

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed Hybrid Granularity Distribution Estimation (HGDE), which estimates distributions at both coarse-grained category and fine-grained instance levels. Apart from coarse-grained category statistics, the proposed method incorporates external fine-grained instance statistics derived from nearest base samples to provide a representative description of novel categories. Then the proposed method fuses the statistics from different granularity through a linear interpolation to finally characterize the distribution of novel categories.

### Strengths
1. The illustrations are clearly presented, colorful, and easy to understand.

2. This paper is well-written and easy to read.

### Weaknesses
1. Motivation is not described clearly and insightfully. Why utilize fine-grained instances to estimate distributions?

2. Utilizing HGDE to estimate distributions is simple, and increases the amount of computation but the gains are limited compared with counterparts. Also, the category estimation has been explored in the community, and this degrades the contribution and novelty of this paper.

3. In section 3.2.2, the top k most similar base samples are selected based on cosine distance, if the selected samples belong to the same class as the support prototypes, is it still reasonable for learning of the distribution, or even counterproductive?

4. What are the pre-trained datasets of the chosen feature-extracting networks? Also, the increased time consumption for similarity calculation is not shown. It seems the proposed method does not need training, thus the title of Sec. 3.3 should be amended accordingly.

### Questions
See Weakness.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper argues that previous Distribution estimation (DE) focus on category-level, which is coarse to align the gap between the base categories and the novel categories samples. To fill this gap, this work proposes Hybrid Granularity Distribution Estimation
(HGDE) by leveraging instance-wised information during training, which can lead to more representative description of novel categories. The statistics from different granularity are fused via a linear interpolation. Empirical studies conducted on four FSL benchmarks demonstrate the effectiveness of HGDE

### Strengths
- The motivation is clear and novel to me. 
- The writing is good and easy to follow.
- The ablation studies are enough and easy to follow.

### Weaknesses
- A primary concern arises from the basic hypothesis, that classes with close distant tend to have a similar distribution in the feature space. In my opinion, this is affected by at least two factors, including the optimization of backbone in the pretraining stage and data distribution itself. In the experiments, I appreciate the authors choose to use figures to demonstrate the fidelity of generated features. However, I think it would be better to include some metric-based results on the whole dataset to measure the fidelity of generated features of the proposed method. I think the author needs to design some baselines to show that the proposed method is reasonable, e.g., distribution estimation based all samples in the datasets or random-selected samples.

- The performance gain on recent work SMKT is not significant, why? Also, why the variance of your method is so big?

- What are the extra computation and parameter costs of HGDE over DE?

- Does this method can be applied into recent visual prompt methods?

- I notice that the proposed method has a larger variance compared to the meta-baseline. It would be better to include some clarification.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an approach to few-shot learning (FSL) called Hybrid Granularity Distribution Estimation (HGDE), which aims to improve the diversity and representativeness of training data for novel categories. While distribution estimation (DE) has proven effective in FSL by leveraging transferred statistics from similar base categories, it is limited by its coarse-grained estimation at the category level, which may lead to non-representative samples. HGDE addresses this issue by estimating distributions at both category and fine-grained instance levels. It incorporates fine-grained instance statistics from nearest base samples to provide a more representative description of novel categories, ultimately fusing statistics from different granularity levels using linear interpolation. Empirical studies on four FSL benchmarks demonstrate that HGDE significantly enhances the recognition accuracy of novel categories and has the potential to improve classification performance in other FSL methods.

### Strengths
1.	One significant advantage of HGDE is its integration of statistics from both coarse-grained category-level and fine-grained instance-level data. This approach ensures that the generated additional samples for novel categories are not only diverse but also representative. This is crucial in FSL, where data availability for novel categories is limited.
2.	The introduction of refinement techniques, such as weighted sum and eigendecomposition, enhances the accuracy of distribution statistics. This refinement process contributes to a more precise estimation of the mean and covariance statistics, which can lead to better model performance. 
3.	The paper highlights that HGDE can be applied to various FSL methods, indicating its flexibility and compatibility with existing FSL approaches.

### Weaknesses
1.	The proposed method appears to be more complex than some existing FSL approaches. The incorporation of various statistics and refinement techniques may require additional computational resources and might not be suitable for all FSL scenarios, especially those with strict resource constraints.
2.	Apart from the caption below Figure 2, the paper does not provide any additional detailed description for Figure 2.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
