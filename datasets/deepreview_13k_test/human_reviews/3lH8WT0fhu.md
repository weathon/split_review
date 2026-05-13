# ConMix: Contrastive Mixup at Representation Level for Long-tailed Deep Clustering

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Deep clustering has made remarkable progress in recent years. However, most existing deep clustering methods assume that distributions of different clusters are balanced or roughly balanced, which are not consistent with the common long-tailed distributions in reality. In nature, the datasets often follow long-tailed distributions, leading to biased models being trained with significant performance drop. Despite the widespread proposal of many long-tailed learning approaches with supervision information, research on long-tailed deep clustering remains almost uncharted. Unaware of the data distribution and sample labels, long-tailed deep clustering is highly challenging. To tackle this problem, we propose a novel contrastive mixup method for long-tailed deep clustering, named ConMix. The proposed method makes innovations to mixup representations in contrastive learning to enhance deep clustering in long-tailed scenarios. Neural networks trained with ConMix can learn more discriminative representations, thus achieve better long-tailed deep clustering performance. We theoretically prove that ConMix works through re-balancing loss for classes with different long-tailed degree. We evaluate our method on widely used benchmark datasets with different imbalance ratios, suggesting it outperforms many state-of-the-art deep clustering approaches. The code has been submitted to the supplementary file.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method called ConMix for dealing with the long-tailed problem of deep clustering. A major challenge in long-tailed deep clustering is how to deal with class imbalance in a dataset without label information. ConMix solves this problem through an innovative approach to mixed representations in contrastive learning to enhance deep clustering performance in the case of long-tailed distributions.

### Strengths
1.	The author has conducted comprehensive experiments, compared with multiple clustering algorithms, and prove the effectiveness of ConMix under long-tailed distribution.
2.	Reasonable theoretical analysis is given to verify that ConMix can implicitly achieve the loss-balance.
3.	Contributions of different elements in ConMix are studied through extensive experiments.

### Weaknesses
The representation synthesis part is supposed to be represented more intuitively, which may be a little confusing at first reading.

### Questions
1. The result of pairwise ConMix shown in Table3 on CIFAR-10 is better than the result of ConMix with M=500 presented in Figure 2.Is this reasonable? In my understanding, the former is equivalent to ConMix with a larger M on CIFAR-10.
2. Have you conducted additional experiments on balanced models of other methods as ConMix-B to support the opinion about robustness?
Question3. Are there other clustering methods being studied besides k-means?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel method, ConMix, aimed at addressing the challenges of long-tailed distributions in deep clustering. The authors argue that existing deep clustering approaches typically assume balanced class distributions, which is not the case in many real-world datasets. ConMix leverages a contrastive mixup strategy to enhance representation learning, theoretically proving its effectiveness in rebalancing class losses without the need for label information. The method is evaluated on benchmark datasets, demonstrating superior performance over existing state-of-the-art approaches.

### Strengths
The introduction of ConMix as a contrastive mixup method specifically designed for long-tailed deep clustering is a notable contribution to the field. The approach is innovative, extending mixup techniques into the realm of unsupervised learning.

The authors provide a theoretical foundation for their method, demonstrating how it can implicitly balance losses across head and tail classes. This theoretical insight is valuable and adds depth to the paper.

The evaluations on various benchmark datasets and the assertion of outperforming existing methods lend credibility to the proposed approach. The performance metrics presented seem robust.

### Weaknesses
Diversity of Datasets: The experiments are limited to a few benchmark datasets, lacking validation of the method’s effectiveness on more complex and diverse datasets. It is recommended to conduct experiments on larger image classification datasets such as ImageNet to thoroughly evaluate the model’s generalization ability and practicality.

Interpretability of the Method: Although theoretical proofs are provided, the interpretability of how ConMix specifically affects the model learning process remains insufficient. Consider adding comparative experiments to illustrate the specific impacts of ConMix under varying conditions (e.g., different long-tail ratios) to enhance the depth of the paper.

Details of Experimental Setup: The experimental section lacks detailed descriptions of hyperparameter choices and training specifics, which could affect the reproducibility of results. It is suggested to include these details in the methodology section to assist other researchers in understanding and replicating the experiments.

### Questions
Conduct additional experiments on large and complex datasets like ImageNet to validate the effectiveness and generalization capability of ConMix.

Enhance the discussion on method interpretability by providing more empirical analysis regarding its impacts.

Provide detailed descriptions of the experimental setup and hyperparameter selections to improve transparency and reproducibility of the research.

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
3

### Summary
The paper proposes to leverage mixup to improve deep clustering approaches for imbalanced datasets. In particular, a multi-sample mixup is incorporated into the SimCLR loss. Instead of just contrasting two augmentations of the same sample, a random subset of samples are selected and the mean representations of their two augmentations are contrasted. A theoretical analysis is performed that shows, under a certain set of simplifications, that this procedure increases the loss of the underrepresented classes. Further, empirical evaluation demonstrate that the scheme can outperform alternative approaches in the imbalanced setting.

### Strengths
Limited work has been done on considering imbalance in deep clustering, with most approaches adopting a balanced assumption, and approaches addressing this shortcomings are thus of significance to the community.

While mixup on a representations has previously been integrated into contrastive learning (also mixing multiple samples), there is a certain novelty of leveraging this in the clustering setting to address class imbalance, which is further supported by the theoretical analysis.

The proposed approach is simple and appears to be effective in the settings considered in this work.

### Weaknesses
While the author’s main focus is on the imbalanced setting, it would be beneficial to also include comparisons in a balanced setting to be able to judge the overall ability of the method.

The overall clarity of Section 3.3. can be improved. How are the “stochastically assigned tags” selected? Does each sample have a certain probability of being included (independent of each other)? If that is the case, what is the probability set to? Also, in line 215, the notation of the cardinality of the set is not aligned with Eq. 3.

The comparison to pairwise ConMix (standard manifold mixup) in Table 3 is not clear. It appears that the pairwise mixup obtains equivalent results to ConMix w/o SDCLR warmup and it is unclear if pairwise ConMix leverages SDCLR warmup here. Also, is this pairwise ConMix directly leveraging the mean representation of the pair or do the authors create a convex combination with weights sampled from a beta distribution? 

As deep clustering methods tend to be a bit less stable than supervised models, some measures of variability/statistical significance would be beneficial in Table 3.

### Questions
Could the authors elaborate on the statement in Line 220: “…. Equivalent to implicitly sampling different weights from the beta distribution”. Do the authors refer to the mixing coefficient in the original mixup formulation? While the reviewer understands that the cardinality of the set U_m follows a beta distribution, the final mixup representation will be the mean representations of these samples, which is different from the mixing coefficients. 

Further, could the authors comment on the performance of the proposed approach in the balanced setting and on the results in Table 3 with regards to the pairwise mixup and the variability of the results?

### Soundness
2

### Presentation
2

### Contribution
2
