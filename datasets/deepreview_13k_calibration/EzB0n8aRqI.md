# Towards Better Understanding Open-set Noise in Learning with Noisy Labels

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
To reduce reliance on labeled data, learning with noisy labels (LNL) has garnered increasing attention. However, most existing works primarily assume that noisy datasets are dominated by closed-set noise, where the true labels of noisy samples come from another known category, thereby overlooking the widespread presence of open-set noise—where the true labels may not belong to any known category.
In this paper, we refine the LNL problem by explicitly accounting for the presence of open-set noise. We theoretically analyze and compare the impacts of open-set and closed-set noise, as well as the differences between various open-set noise modes. Additionally, we examine a common open-set noise detection mechanism based on prediction entropy. To empirically validate our theoretical insights, we construct two open-set noisy datasets—CIFAR100-O and ImageNet-O—and introduce a novel open-set test set for the widely used real-world noisy dataset, WebVision. Our findings indicate that open-set noise exhibits distinct qualitative and quantitative characteristics, underscoring the need for further exploration into how models can be fairly and comprehensively evaluated under such conditions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of open-set noise in learning with noisy labels (LNL), a problem where the true labels of noisy samples may not belong to any known category. The authors refine the LNL problem by accounting for open-set noise and theoretically analyze its impact compared to closed-set noise. They construct two open-set noisy datasets and introduce a novel open-set test set for the WebVision dataset to empirically validate their findings. The results indicate that open-set noise has distinct characteristics and a lesser negative impact on model performance compared to closed-set noise, highlighting the need for further exploration into model evaluation under such conditions. The paper also examines an entropy-based open-set noise detection mechanism and proposes additional out-of-distribution detection tasks for model evaluation.

### Strengths
- The paper studies a detailed examination of open-set noise in the context of learning with noisy labels, an area that has been largely overlooked in previous research.

- It offers a robust theoretical framework to analyze the effects of open-set noise and supports these findings with empirical evidence through the creation and testing on synthetic datasets.

- The paper provides a careful look at different modes of open-set noise, comparing 'easy' and 'hard' open-set noise scenarios, which is crucial for understanding how various types of noise affect model performance.

- It introduces the use of out-of-distribution (OOD) detection as a complementary evaluation metric to traditional accuracy measures, enhancing the assessment of model performance in the presence of open-set noise.

- The paper underscores the significance of open-set noise in real-world datasets and demonstrates the practical impact of its findings on existing learning methods, highlighting the need for more research in this area.

### Weaknesses
 - The paper examines a few existing learning with noisy labels (LNL) methods on the synthetic datasets, outlined in Appendix E.1. However, it does not explore a wide range of existing methods such as robust losses in LNL, which could limit the comprehensiveness of the comparison and the conclusions drawn about the state-of-the-art in handling open-set noise. Specifically, the evaluation lacks a thorough investigation into how methods designed to handle closed-set noise perform under open-set conditions. For example, techniques like MixUp or other data augmentation strategies tailored for noisy labels could provide additional insights.

- For Section 3.3.2, Authors exclude the effect of closed-set noise (Cx = 0) and only focus on open-set noise which could limits the findings in real-world scenarios. For example, It is not clear how different open-set noise with same close-set label noise. The analysis would benefit from a more comprehensive exploration of the interplay between closed-set and open-set noise, including scenarios where both types of noise are present at varying ratios. This is crucial because real-world datasets rarely exhibit only one type of noise in isolation.

- Experiments on the main paper are not thorough enough. I suggest add more LNL methods and discusses how different methods behave and align with the theorems in the main paper. The empirical validation could be strengthened by including a more diverse set of LNL methods, particularly those that explicitly address label noise through techniques like re-weighting, meta-learning, or gradient manipulation. A more extensive experimental section would provide a more robust assessment of the theoretical claims.

### Questions
- For Figure 2 (c) (d), Authors state in the paper that "the presence of open-set noise degrades OOD detection performance, whereas, conversely, the presence of closed-set noise could even improve OOD detection performance.". However, from my observation, the closed-set noise does not improve detection performance from the Figure. 

- In Section 3.3.2, Is it possible to assume the same pattern and noise ratio of close-set noise and then study how different open-set noise compare to each other?

- For Figure 2, is it drawn when model converges for each case?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper analyzes the learning with noisy labels problem by explicitly accounting for the presence of open-set noise. However, only theoretical analysis and dataset construction are not sufficient to be published in ICLR.

### Strengths
This paper analyzes the learning with noisy labels problem by explicitly accounting for the presence of open-set noise.

### Weaknesses
Only theoretical analysis and dataset construction are not sufficient to be published in ICLR. The theoretical analysis, while potentially sound, lacks sufficient connection to practical applications and does not provide clear, actionable insights for practitioners. The paper introduces a new benchmark dataset, but the novelty and utility of this dataset are not sufficiently justified. It's unclear how this dataset addresses gaps in existing benchmarks or enables new research directions that are not already possible with current datasets. The paper does not demonstrate the practical value of the theoretical findings or the proposed dataset through comprehensive experimental validation.

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
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors theoretically analyze and compare the impacts of open-set and closed-set noise, as well as the differences between various open-set noise modes. Additionally, they examine a common open-set noise detection mechanism based on
prediction entropy. Moreover, to validate their insights, they construct two open-set noisy datasets and a open-set test-set for evaluation.

### Strengths
1.The paper is easy to follow and the conclusions are easy to understand.

2.The mathematical analysis is adequate and there are experimental results to support these insights.

3.The experimental figures are clear and adequate on the constructed dataset.

### Weaknesses
1.The way of constructing benchmark is quite similar to existing benchmarks in LNL. Thus it may be not suitable to list it as a contribution.

2.Though the author introduces a hard open-set noise (seems like a combination of feature-dependent noise and open-set noise), but it seems that the author does not design a method to tackle such kind of noise.

3.Some of the conclusions may be naive and simple.  For example, " it may be effective only for ‘easy’ open-set noise.". Because entropy-based methods generally fail to detect close-set feature-dependent noise as well.


There are some minor issues that will not affect the rating:
1." the concept of complete noise transition matrix" should be " the concept of a complete noise transition matrix".

2. "namely fitted case and overfitted case" should be "namely the fitted case and overfitted case".

3.It would be better if the contributions are more compact. There are six contributions now.

### Questions
What does this sentence mean: obtaining a model that perfectly fits the data distribution is often challenging; here, we consider training a single-layer linear classifier upon a frozen pretrained encoder. I think a single-layer linear classifier may even be worse to fit the data distribution.

### Soundness
3

### Presentation
3

### Contribution
2
