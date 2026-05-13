# LogoRA: Local-Global Representation Alignment for Robust Time Series Classification

- Decision: Reject
- Scores: 3, 6, 5, 5, 6

## Abstract
Unsupervised domain adaptation (UDA) of time series aims to teach models to identify consistent patterns across various temporal scenarios, disregarding domain-specific differences, which can maintain their predictive accuracy and effectively adapt to new domains. However, existing UDA methods struggle to adequately extract and align both global and local features in time series data. To address this issue, we propose the \textbf{Lo}cal-\textbf{G}l\textbf{o}bal \textbf{R}epresentation \textbf{A}lignment framework (\abbr), which employs a two-branch encoder—comprising a multi-scale convolutional branch and a patching transformer branch. The encoder enables the extraction of both local and global representations from time series. A fusion module is then introduced to integrate these representations, enhancing domain-invariant feature alignment from multi-scale perspectives. To achieve effective alignment, \abbr employs strategies like invariant feature learning on the source domain, utilizing triplet loss for fine alignment and dynamic time warping-based feature alignment. Additionally, it reduces source-target domain gaps through adversarial training and per-class prototype alignment. Our evaluations on four time-series datasets demonstrate that \abbr outperforms strong baselines by up to $12.52\%$, showcasing its superiority in time series UDA tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the problem of unsupervised domain adaptation on time series data in classification, which is to help ML models to adapt the other scenarios. The authors proposes LogoRA to extract both local and global representations. The result indicates a improvement of 12% on four datasets.

### Strengths
1.The authors design a new metric learning method based on DTW, which can overcome the severe time-shift patterns that exist in time series data and learn more robust features from the source domain.

2.The proposed method extract both global and local features different domains and  outperforms baselines by up to 12.52%

### Weaknesses
1. The technical details seem to be a bit lack of innovation. The author can improve the paper by further explain how global and local information work together to improve the quality of the classification.

2. Only four datasets are employed, it may be not sufficient enough to support the claim of the advantage of the proposed method.

3. Since the ablation experiment was only conducted on the best performing HHAR dataset, we believe that the results of the ablation experiment do not fully support the author's work

### Questions
1. The effectiveness of the algorithm proposed by the author compared to the baseline method varies significantly across four datasets, with an improvement of+12.52% on the HHAR dataset, but only+0.51% on the HAR dataset. Can the author explain the reason for this difference?

2. The author suggests that using both global and local information simultaneously can help improve algorithm quality. Can we use intuitive examples to explain this process?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a universal framework for unsupervised (actually semi-supervised) sequence modeling that captures both local patterns and global patterns. Instead of using simple concatenation, it proposes to used cross attention, which has been shown promising in recent studies. Many regularization losses have been included to enforce alignment.

### Strengths
Overall, this paper is well-polished and experiments are extensive. More specifically, 
1: The ablation study is very comprehensive. The table 2 and 3 provides very convincing evidence for each component and why they should be part of the framework. 
2: The choice of loss functions is convincing. I can see that authors have put many thoughts on it. Table 2 is a strong support for each loss function. 
3: Authors have included many baselines in the study, including models from recent papers.

### Weaknesses
1: I am interested in the implementation, as reproducibility is a key metric in ML publications nowadays. I wish authors can provide a code repo (hopefully using notebook so I can see the results without re-running everything). If authors can show the reproducibility durign rebuttal, I would like to increase my rating. 
2: The cross-attention is only validated by qualitative visualizations but not in ablation study. Although the heatmap looks good to me, it is interesting to know how much gain does cross attention bring vs. other fusion methods (e.g., addition or concatenation). 
3: As the authors have ackowledged in the last paragraph, this framework does not work well in other public datasets, so this paper most likely only includes those successful datasets. I would invite the authors to append their explorations on other datasets in the appendix or code repo, so others (like me) can learn from it and investigate further.

### Questions
Usually time series data are coupled with static data (tabular, images or texts), for example, MIMIC dataset. How to expand the current framework to deal with multi-modal data? You can share your thoughts as limitation/future work. If you have tried, you could share your exploration in the appendix too (even if it failed).

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the LogoRA which does time series classification according to the fusion feature, in which the fusion features are obtained by the fusion module that integrates the local and global representations extracted by CNN encoder and transformer encoder, respectively. LogoRA then uses different representations for invariant feature learning, and adversarial approaches to narrow the gap between domains.

### Strengths
The structure of the article is well organized and the logic is clear.  
In UDA, local and global information of time series are used in combination.

### Weaknesses
In terms of writing, the first appearance of TCN in the sentence " Most existing approaches employ a TCN as the backbone…" on the first page should not be an abbreviation, otherwise we do not understand what it is. It should be described like RNNs, LSTM, and CNNs in the previous paragraph, with complete expressions followed by abbreviations.
The spelling of "evaluation" in the last sentence of the second page is incorrect.
Table 2 L_ cdan doesn't know what it refers to.
There are other writing errors like this.
The model structure is commonly used, and the idea of using adversarial training is also common. The innovation of aligning local features with global features is not enough to support the entire paper.

### Questions
How to determine the patch length P? Is it a hyperparameter of the associated dataset, trainable, self defined, or universal?
In feature invariant learning, is there an independent category for patch when selecting input p of the same class and input n of a different class, or is it equivalent to the category of the entire sequence? If so, what is the difference between using a patch subsequence and the entire sequence for DTW? Similarly, when calculating the Euclidean distance of a sequence, why choose to calculate on the fused features? Can DTW be calculated on fused features?
How to explain the significant decrease in the effectiveness of the 2->4 experiment compared to the second and fourth rows of the ablation experiment?
After adding global loss in the fifth row of the ablation experiment, the effect of the 7->1 experiment decreased by nearly half compared to the fourth row. How to explain this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper primarily introduces an effective model for unsupervised domain adaptation in time series classification tasks, which integrates both global and local features efficiently. This integration has led to a commendable performance in the realm of unsupervised domain adaptation.

### Strengths
1. Employing an attention mechanism to fuse global and local features is particularly intriguing. This approach offers a novel perspective on feature integration in the context of time series data.

2. The experimental results demonstrate the method's impressive performance.

### Weaknesses
1. The reason for using DTW to align the patch representations is not sufficient because the time-step shift occurs on the original sequence. Why not align the original sequence?

2. More limitations of the proposed method need to be discussed. For instance, in Table 2 of the ablation experiments, there is a noticeable performance degradation, particularly in the 4th and 5th rows compared to the 3rd row. This can be attributed to differences in performance across the first three scenarios. Can specific examples be used to illustrate this?

3. The training objective specified in Equation (5) involves five distinct loss functions, rendering it challenging to optimize the overall loss coherently during training. In essence, the presence of multiple training losses poses a challenge in comprehending the fundamental contributions of this paper, given the complexity associated with optimizing such a diverse set of loss functions.

4. The explanation for why the fusion of global and local features is effective is not clear. The interpretation of the heatmaps in Figure 6 is unclear as well. (1) How can different positions in the heatmaps be correlated with sequences? (2) Which weight activations in the heatmaps are meaningful? (3) How do different scales of heatmaps demonstrate their effectiveness?

### Questions
1. Why is the method of fusing global and local features of time series using an attention mechanism effective? 

2. What are the merits and drawbacks of the approach introduced in this paper, in comparison to existing methods, concerning both runtime efficiency and the convergence behaviour of the model?

3. Please answer other questions in the Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the Local-Global Representation Alignment framework LogoRA for unsupervised domain adaptation of time series data. The paper uses a two-branch encoder to extract local and global features, and uses triplet loss for fine alignment and dynamic time warping-based feature alignment. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
The paper is well-written and easy to understand.

The paper is theoretically sound.

The experimental results show the usefulness of the method.

### Weaknesses
The author should explain TCN when it appears for the first time.

The author claims that cross-attention in local-global fusion model is used to integrate local and global representations, which should be explained in detail. The cross-attention operation computes the similarity between query and key, and selects values based on the similarity score. It is confusing to compute the similarity of global and local feature, and use this score to select the local feature. What is the explanation behind it?

The paper only uses DTW for global features, how about the local features?

### Questions
See weaknesses above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
