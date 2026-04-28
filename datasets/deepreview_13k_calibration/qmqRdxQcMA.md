# Enhancing Cost Efficiency in Active Learning with Candidate Set Query

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
This paper introduces a cost-efficient active learning (AL) framework for classification, featuring a novel query design called candidate set query. Unlike traditional AL queries requiring the oracle to examine all possible classes, our method narrows down the set of candidate classes likely to include the ground-truth class, significantly reducing the search space and labeling cost. Moreover, we leverage conformal prediction to dynamically generate small yet reliable candidate sets, adapting to model enhancement over successive AL rounds. To this end, we introduce an acquisition function designed to prioritize data points that offer high information gain at lower cost. Empirical evaluations on CIFAR-10, CIFAR-100, and ImageNet64x64 demonstrate the effectiveness and scalability of our framework. Notably, it reduces labeling cost by 42% on ImageNet64x64.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an active-learning framework called Candidate Set Query (CSQ) to reduce the size of possible classes during annotation process, minimizing the search space and lowering the labeling cost at the same time. Furthermore, the authors leverage conformal prediction to produce accurate candidate sets, and introduce an acquisition function that exploits data points with high information gain.

### Strengths
1. This paper introduces a novel approach called Candidate Set Query (CSQ), which effectively reduces labeling costs by narrowing down the candidate classes presented to annotators, thereby minimizing annotation time.
2. The proposed method leverages conformal prediction to dynamically produce accurate candidate labels based on a cost-efficient data acquisition function. This function prioritizes samples with high information gain, leading to greater efficiency and reduced labeling costs.
3. The framework demonstrates strong performance across multiple image recognition datasets, consistently outperforming baseline methods by a significant margin.
4. The authors provide comprehensive ablation studies to thoroughly validate the effectiveness of all components.

### Weaknesses
 1. The rationale behind the cost-efficient acquisition function in Eq. (8) needs to be further explained. Additional motivation and explanation for this function are recommended. Specifically, the interplay between the information gain term and the cost term is not entirely clear. The current explanation lacks a detailed breakdown of how these two components are balanced, and how the hyperparameter 'd' influences this balance. It would be beneficial to provide a more thorough explanation of how the cost is calculated, and why this specific formulation is chosen.
2. As shown in Fig. 9a, the performance is sensitive to the hyperparameter d. Providing guidelines for setting this parameter to an appropriate range on different datasets would be beneficial. The current analysis does not offer sufficient insight into how the optimal value of 'd' might vary across different datasets, or how to determine a suitable range for this parameter. A more detailed discussion on the impact of 'd' on the trade-off between exploration and exploitation would be valuable.
3. In realistic scenarios, the samples with high uncertainty waiting to be annotated can be divided into two groups based on their probability distributions on categories, high confidence on several specific classes or low confidence on almost all classes. The proposed framework might only be suitable for the former case. As for the latter one, an intuitive solution is to sift out all candidate labels with low prediction probabilities, such as less than 0.1 * 1/C where C is the number of categories. So it’s suggested to conduct more experiments to evaluate the performance of this approach under this scenario. The paper does not adequately address how the method performs when faced with samples exhibiting very low confidence across all classes, and it is unclear whether the conformal prediction approach is robust in such cases.
4. A smaller candidate label set means model have higher certainty for samples, which seems to be against the motivation of selecting the most uncertain samples in active learning. Despite the proposed method minimizing the labeling cost by narrowing down the label space, the information gain is limited. It’s suggested to plot the graph of how performance varies with the number of queried samples. It is not clear if the proposed method truly maximizes the information gain, or if it merely reduces the cost of labeling at the expense of learning from more informative samples. A more detailed analysis of the trade-off between labeling cost and information gain is needed.
5. There is a minor formatting issue in Fig. 5c, where certain data points from the top-1 prediction fall outside the scale range of the graph.
6. Line 274 contains a typo: “calcuclate” should be corrected to “calculate.”

### Questions
Please refer to the above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a cost-efficient active learning strategy using conformal predictions. Instead of letting the annotator choose from all possible labels, a candidate set of fewer labels is given. The paper uses a log order expected cost function and shows the improved efficiency in terms of actual labeling cost.

### Strengths
1. The content of the paper is well presented.
2. The paper studies the cost of AL query in a more realistic way and proposes a solution for reducing the cost by candidate set query. 
3. The candidate set is formed by conformal prediction and the candidate labels are related to the expected information gain with cost considerations.

### Weaknesses
 The proposed method still depends on the conformal prediction and the calibration set to determine the confidence level. It is a realistic solution however not guaranteed to be theoretically sound. The convergence can not be obtained in a proper label complexity analysis. Similarly, the labeling cost assumption in Theorem 3.1 is only a rough approximation.

### Questions
1. Is random selection effective for the calibration set?
2. Is it possible that the candidate set obtained from eq(5) is empty?
3. Is there any guarantee that using the quantile from the previous round would work?

### Soundness
2

### Presentation
3

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
This paper introduces the Candidate Set Query (CSQ) framework which aims to improve the cost efficiency in active learning (AL) tasks. CSQ reduces the size of the set of candidate classes which reduces the search space, leveraging conformal prediction to dynamically adjust the optimal candidate set size across successive AL rounds. The paper also proposes an acquisition function that considers the ratio of information gain vs labeling cost to help prioritize samples to label. The author then benchmarked this framework across multiple datasets and empirically demonstrate the reduction in labeling costs.

### Strengths
1. The motivation for this paper is clear, and the paper proposes a novel framework of high significance 
2. The paper presents a solid theoretical framework that is thoroughly explained and mostly straightforward to follow
3. The framework is benchmarked across 3 well-known datasets, empirically demonstrating the effectiveness of the method 
4. Thorough ablations studies were conducted to highlight the significance of each component of the framework

### Weaknesses
 1. The benchmarks are conducted on very similar datasets (CIFAR-10, CIFAR-100, and ImageNet64x64 are all image classification datasets), and also only compares against a small number of baseline AL methods. It is unclear if the results will generalize well across different datasets and domains, and if more advanced underlying AL acquisition methods are used
2. The paper does not consider the implication of real-world datasets, such as those containing label noise, imbalance classes etc might impact the performance of CSQ. More experiments could help identify CSQ’s robustness when it comes to noisy annotations, as it could lead to inefficient training and candidate sets with lower quality
3. CSQ relies on several hyperparameters, however there is limited justification on how to properly optimize the hyperparameter $d$, making it difficult to apply the method in new datasets

### Questions
1. Have the authors considered any special handling of outlier or anomalous datapoints, which tend to have have high uncertainty, and could lead to inefficient construction of the candidate set, acquisition and labeling
2. Have the authors considered the risk of overfitting and drift of confidence scores across successive AL rounds and how CSQ could incorporate some steps to address it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors proposed a cost-efficient active learning (AL) framework for classification, featuring a novel query design called candidate set query (CSQ). CSQ narrows down the set of candidate classes likely to include the ground-truth class and leverages conformal prediction to dynamically generate small yet reliable candidate sets. Experiments on several datasets demonstrate the proposed CSQ is effective.

### Strengths
The proposed CSQ present the annotator with an image and a narrowed set of candidate classes that are likely to include the ground-truth class, which reduces labeling cost by minimizing the search space the annotator needs to explore. The various modules in the entire paradigm are relatively mature.

### Weaknesses
1. The explanation of "empirical quantile" in Section 3.2, titled "Candidate Set Construction from Conformal Prediction," is not very clear. Could the authors provide further clarification, specifically regarding the insights that Conformal Prediction offers for method design and its role in the proposed approach? It's unclear how the empirical quantile is specifically calculated and how it relates to the desired coverage of the candidate set. The connection between the calibration set and the generalization of the quantile to the actively sampled data needs more elaboration. The current description lacks the necessary detail to fully grasp the mechanism by which conformal prediction ensures the candidate set's reliability.

2. Is Table 1 in the experiments derived from the cost-efficient acquisition function?

3. Does the Active Learning (AL) approach include corresponding real-world datasets? Would it be possible to include more experimental results using real-world datasets?

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
