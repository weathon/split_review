# Machine Unlearning for Contrastive Learning under Auditing

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Machine unlearning offers effective solutions for revoking the influence of specific training data on pre-trained model parameters. While existing approaches address unlearning for classification and generative models, they overlook an important category of machine learning models: contrastive learning (CL) methods.
This paper addresses this gap by introducing the Machine Unlearning for Contrastive Learning (MUC) framework and adapting existing methods. We identify limitations in current approaches, noting that several methods perform inadequately as unlearners and that existing auditing tools insufficiently validate unlearning effects in contrastive learning. To address these issues, we propose Alignment Calibration (AC), a novel method that explicitly considers contrastive learning properties and optimizes towards new auditing metrics for easy verification of unlearning. Through empirical comparisons with baseline methods on SimCLR, MoCo, and CLIP, we demonstrate that AC: (1) achieves state-of-the-art performance, approximating exact unlearning (retraining); (2) enables data owners to clearly visualize unlearning effects through black-box auditing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a new method of machine unlearning for contrastive learning

### Strengths
The reported numerical results show that the proposed method outperforms other method

### Weaknesses
1. More intuition/insights about the proposed method would be helpful. For example, I don't get why AM and AGM are good metrics. Shall we consider loss evaluated on both positive and negative pairs?
2. Any insight why it is beneficial to maintain the term for negative pairs?
3. I also don't understand the formula $UA \approx TA < RA$
4. The experiments are only performed on CIFAR-10, CIFAR-100, and MS-COCO datasets. This seems inadequate. 
5. How the tuning parameters for other unlearning methods are tuned should be described

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Machine Unlearning for Contrastive Learning (MUC), a framework designed to remove specific data influences from contrastive learning models efficiently. The authors show the shortcomings in the existing unlearning methods when applied to models trained with contrastive learning like SimCLR, MoCo, and CLIP. Then they propose a novel approach called Alignment Calibration (AC) to address these shortcomings. This method optimizes the unlearning process by new retraining procedure minimizing loss on retained data and maximizing an unlearning criterion on the data to be unlearned.  This also gives data owners  tools to visually audit unlearning. Experiments show that AC outperforms existing unlearning methods, providing near-exact unlearning while maintaining model utility.

### Strengths
- This paper tackles an important problem—how to unlearn data from self-supervised models, especially for contrastive learning. This is important as contrastive models trained on internet-sourced data are growing and powering multiple applications.

- Provides a systematic study on adapting existing unlearning methods to contrastive models, revealing their inadequacy in unlearning with contrastive models. Then the authors provide a solution called Alignment Calibration along with auditing tools/metrics suited for contrastive models.

- The authors conduct extensive experiments with AC and baselines across multiple contrastive learning models, showing that it performs well in removing unwanted data influence while retaining the model’s core functionality. The results are backed by multiple metrics and support the claim that AC offers improved unlearning over baselines

### Weaknesses
 - The loss $\mathcal{L}_{retain}$ in equation 3, is computed on the retained data. As this data could be huge, computing and minimizing this loss could take a lot of time. Often, the unlearning could be even for a single data point but invoked by multiple users, in such cases a simple editing technique that can remove specific data points without expensive training would be preferable. 

- I do not find the metrics and other tools to measure unlearning convincing. A user would want a guarantee that their data point(s) have been removed and a model provider would like to provide such a guarantee. How can these metrics be translated into such guarantees, if at all? In Figure 3, the matrices look nearly the same, the point of “visual auditing” is not clear to me. 

- The evaluation setup also does not seem realistic. Randomly removing x% of points from CIFAR-10, and CIFAR-100 seems artificial and far from the realistic settings of unlearning where some specific data points need to be removed (even those that might have a huge influence on the performance). Given that very good performance can be achieved on these datasets even with very few samples (see results in zero-shot/few-shot classification or semi-supervised learning), I am not convinced by the effectiveness of the proposed method in unlearning while retaining high performance. Relatedly, you can see research on data pruning strategies, the setup of dropping x% points randomly is at best a simple data pruning strategy. 


Typo:
line 138, "retaining dataset"

### Questions
See weaknesses above. Also,

1. Aren't there any systematic benchmarks to evaluate unlearning? Where the data to be removed is selected depending on various criteria reflecting the real-world scenarios. 

2. Is there any theoretical research on giving a guarantee/certificate that the requested data points have been removed? Can such results be adopted to contrastive models?

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
2

### Summary
This paper tackles the problem of machine unlearning in self-supervised pre-training (for contrastive approaches).
The authors identify two challenges, namely that adapting methods from either supervised or unsupervised machine unlearning might not be sufficient and the need for black-box auditing methods that could allow data owners to verify the removal of their data without access to the model.

The authors propose a novel unlearning method targeted specifically at unlearning data from pre-trained models trained through contrastive learning. This method is tested against proposed baselines adapted from the machine unlearning literature on three different pre-trained models across 2 datasets.

A black-box auditing tool in the form of alignment matrices that a data-owner can compute from the embeddings for the unlearning data is also proposed.

### Strengths
The paper tackles an interesting problem that seems relevant (although I am not an expert in machine unlearning).
The authors do a good job presenting and motivating the two distinct challenges they identify with contrastive unlearning.

The selection of baselines in the experimental setup also seems reasonable to me.

### Weaknesses
 **1. Motivation of the proposed black-box metrics**
- The authors define the FS score by analogy to the memorization score in data attribution. This still lacks motivation as to why the difference in alignment between positive pairs before and after unlearning should be a reasonable and complete measure of unlearning. The FS score, as presented, only considers changes in the alignment of positive pairs, neglecting the crucial aspect of how the unlearned data relates to other data points in the embedding space. A comprehensive unlearning metric should also consider the negative pairs and the overall distribution of the unlearned data.
- Furthermore, the proposed AGM is essentially a decomposed version of this FS score and similarly lacks motivation. The AGM, by focusing on individual components of the alignment matrix, might miss the holistic picture of how the unlearning process affects the overall embedding space. It is not clear how the decomposed components of the alignment matrix provide a complete picture of unlearning.
The authors should make an effort to show why a data owner should thrust this metric, for example, by showing that it correlates well with other established metrics of unlearning (even if they are white box). Simply showing that the alignment matrix changes with the unlearning process is not sufficient evidence for the data being unlearned. The authors need to demonstrate that changes in the alignment matrix directly correspond to a reduction in the model's reliance on the unlearned data, not just a change in the embedding structure.
- The latter seems particularly problematic since the proposed AC method is aimed directly at improving this proposed metric. It is however not clear in the text how this is accomplished (see question 2 below).

**2. Experimental Results**
- Standard errors are not reported for tables 1 through 3. The results from all methods seem too close and too metric dependent to really draw meaningful conclusions. The lack of standard errors makes it difficult to assess the statistical significance of the reported results. Without knowing the variability of the results, it's impossible to determine if the observed differences between methods are due to actual performance differences or just random fluctuations.

Furthermore, the aggregation of these metrics into an average gap seems problematic for multiple reasons:
- It's not clear to me how the RA, TA and UA metrics should be accounted for and aggregated into a meaningful overall measure. The authors take the absolute difference to the retrain baseline and average across the three metrics. Perhaps the gap between TA and UA would be a better measure of failure to unlearn. At the same time, higher is generally better for these metrics so penalizing a higher RA than the retrain baseline does not seem correct. The use of absolute differences for metrics where higher values are generally better is problematic. It penalizes methods that perform better than the retrain baseline, which is counterintuitive. A more appropriate approach would be to consider the signed difference and analyze the direction of the deviation from the retrain baseline.
- Similarly, the sign of the difference is not taken into account for the other metrics. For example, higher EMIA than the retrain baseline seem to be counted as a positive gap. This approach of using absolute differences for all metrics is problematic because it treats both positive and negative deviations from the retrain baseline as equally undesirable. For metrics like EMIA, where lower values indicate better unlearning, a higher value than the retrain baseline should be penalized more severely than a lower value. The current approach obscures the direction of the deviation and makes it difficult to interpret the results.

### Questions
1. Why should I thrust AGM as a valid measure of unlearning as a data owner?
2. $p_u^\times$ in the equation for $\mathcal{L}_\mathtt{unlearn}$ at the end of page 6 is never defined. What is the difference between the first two terms in that equation (other than the different sign) and how should this modification help improve AGM compared to Equation 4?
3. Why are standard errors not reported?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work fills the gap in the machine unlearning literature, specifically for contrastive learning pre-training, proposing a new unlearning method which is called the *Alignment Calibration* method. A new *white-box* auditing metric is also proposed for an easier auditing process for the users who request the unlearning.

### Strengths
Overall,
1. The paper is well-written and well-presented.
2. The setup is clean and clear. Figure 1 helps a lot.
3. The experiment is thoroughly done and well-organized.

### Weaknesses
The main weaknesses are the motivation of the design of Alignment Calibration:
1. The motivation of *positive alignment calibration*: in the paper, the motivation is to achieve a good **FS** score. However, as mentioned in Section 3.3, **FS** itself is not a reliable metric, which raises the question of why we care about **FS** at all. This novelty does not seem principle to me with this motivation. Furthermore, the paper does not adequately address the limitations of using FS as a guiding metric, especially given its known instability with small unlearning sets. The reliance on FS, even for white-box evaluation, needs more justification, particularly when the paper itself acknowledges its shortcomings.
2. The design of *Alignment Calibration* (Equation (5)) is quite heuristics. It seems natural, however, that some of the designs (including both negative and positive AC) directly optimize the proposed auditing metric (e.g., AGM), which seems a bit too ad-hoc and in the proposed method's favor. The direct optimization of the auditing metric by the unlearning method raises concerns about the generalizability of the approach. It is unclear if the method would perform well with other auditing metrics or if it is specifically tailored to the proposed one. This lack of generality is a significant weakness.

>I'm unfamiliar with the contrastive learning literature, and hence maybe some theoretical results support such a heuristic way of designing loss.

Additionally, 
3. The claim is a bit too broad. Specifically, the proposed new auditing tool is quite ad-hoc, and I do not find it visually intuitive. Moreover, if I understand it correctly, this essentially is a pair-wise version of **FS**, which as mentioned in Section 3.3, is unreliable. The paper needs to provide a more rigorous justification for the proposed auditing metric, especially given its similarity to the unreliable FS score. The lack of visual intuitiveness also makes it difficult for users to understand the unlearning effect, which undermines the purpose of the auditing tool.

### Questions
See Weaknesses. Additionally:
1. Are there any theoretical results in this field that support the design of Alignment Calibration?

Some minor suggestions in writing:
1. Use $\ell_1$ (`\ell_1`) instead of $l_1$.
2. Line 215, replace `\citep{}` with `\citet{}` for "in evaluating data attribution in ...".
3. Line 250, the word "shadow models" for MIA appears without explanation. It might cause some confusion for someone who is unfamiliar with MIA.
4. Line 251, it's unclear what the "lock" means in this context.
5. Line 255, Maybe something is wrong with the $\LaTeX{}$ environment? "[Exact unlearning...]" should not be intended I suppose.
6. Line 290, the unlearned model should be $\\hat{g}$.
7. Line 814, maybe a typo in "...pair of features, i.e.45 pairs..."?
8. Throughout the paper, the style of "i.e." changes between "i.e." and "*i.e.,*."

### Soundness
3

### Presentation
2

### Contribution
3
