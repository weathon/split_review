# Harmonious convergence for confidence estimation in depth estimation and completion

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Confidence estimation for monocular  depth estimation and completion  is important for their deployment  in real-world applications. Recent models for confidence estimation in these regression tasks   mainly   rely on the statistical characteristics of training and test data, while ignoring the information from the model training.  We propose a harmonious convergence estimation approach for  confidence estimation in the regression tasks, taking training consistency into consideration. Specifically, we propose an intra-batch convergence estimation algorithm with two sub-iterations to compute the training consistency for confidence estimation. A  harmonious convergence loss is newly designed to encourage the consistency between confidence measure and depth prediction. Our experimental results on the NYU2 and KITTI datasets show improvements ranging from 10.91\% to 43.90\% across different settings in monocular depth estimation, and from 27.91\% to 45.24\% in depth completion, measured by Pearson correlation coefficients, justifying the effectiveness of the  proposed method. We will release all the codes upon the publication of our paper.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes confidence estimation in monocular depth estimation and completion. The authors introduce a new method termed harmonious convergence estimation to integrate confidence estimation and for regression tasks taking training consistency.

- Introducing a harmonious convergence estimation and intra-batch convergence for monocular depth estimation and completion.
- Conducting diverse experiments across multiple datasets

### Strengths
S1. Clear Contribution with Confidence Estimation. The paper presents a contribution by incorporating confidence estimation for monocular depth estimation and completion.

S2. Diverse Experiments: The paper shows diverse experiments with two different datasets

S3. Writing and Presentation: The paper is well-written and easy to understand.

### Weaknesses
The paper lacks experimental results showing depth performance using commonly employed metrics in the depth estimation and completion research fields, such as δ (delta) or MAE.
This paper claims that the proposed confidence estimation method works well even in the more challenging task of regression compared to classification. 
Therefore, it is necessary to show more clearly that the performance of depth estimation or completion improves according to the confidence estimation even if this paper's main focus is related to confidence estimation.

### Questions
I would like to start by thanking the authors for their contribution to this field with their submission.

This relates to Weakness. Is there any reason that those metrics are skipped in the experimental results?

### Soundness
2

### Presentation
3

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
This paper addresses the confidence estimation for monocular depth estimation and completion. To this end, the authors propose a intra-batch convergence estimation algorithm and a harmonious convergence loss. The experiments are conducted on the NYU2 and KITTI datasets and the results show improvements ranging from 10.91% to 43.90% across different settings in monocular depth estimation, and from 27.91% to 45.24% in depth completion.

### Strengths
The paper is well-written and structured;

The experiments are thorough and conducted on multiple datasets;

The proposed method is effective according to the quantitative and qualitative results.

### Weaknesses
Could you provide a more detailed analysis of how intra-batch convergence estimation or harmonious convergence loss contribute to the performance gains compared to previous approaches?

In Fig. 1, D0 and D1 appear to be different, but C0 and C1 look exactly the same；Could you explain this apparent discrepancy and discuss its implications for the method's effectiveness? Additionally, could you provide a more detailed visualization or analysis of how C0 and C1 differ?

### Questions
Please see the weakness.

### Soundness
3

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
4

### Summary
This paper proposes a confidence estimation method in depth estimation and depth completion. The existing dense prediction confidence estimation methods may suffer high memory demands, so this paper proposes an "intra-batch convergence estimation algorithm" for consistency computation, and designs a "harmonious convergence loss function" that integrates training consistency
into confidence estimation for monocular depth estimation and completion tasks. Some experiments conducted on NYU and KITTI datasets prove the effectiveness of this method. 

However, this paper fails to adequately summarize existing methods, and the proposed solution also lacks theoretical support, and some related works are missing for comparison.

### Strengths
1. This paper proposes an "intra-batch convergence estimation algorithm" for consistency computation, and designs a "harmonious convergence loss function" that integrates training consistency into confidence estimation for monocular depth estimation and completion tasks. 
2. Some experiments conducted on NYU and KITTI datasets prove the effectiveness of this method.

### Weaknesses
1. This paper does not provide a good summary of the problems of existing methods. So, I can not figure out the motivation behind the entire design. As mentioned in Line 48 "One challenge is addressing spatial misalignment of training samples caused by random augmentations", but why I should overcome this point? In other words, I do not understand why we have to introduce "training consistency" into confidence estimation networks. I can not see any advantages of doing so over existing methods. The only explanation is in line 130 "Although significant progress has been achieved, these methods fail to take the information from training process into consideration." Through these words, I can not understand the author's motivation.
2. There are some missing related works for comparison (Bae G et al. 2022, Xiang M et al. 2024). But the most important is I need to know the Strengths between this paper and these existing determined confidence estimation methods.

3. The proposed solution in the papers lacks theoretical support. In my opinion, the inter-batch loss is just a constraint that ensures the gradient is sufficiently small during the optimization process of the network. This is a simple modification of (Li et al. 2023) without corresponding explanations. And the ablation experiment (Table 3) also shows that the $L_h$  is the most important part of the whole network, not $L_c$.

### Questions
See in the Weaknesses part.

### Soundness
2

### Presentation
1

### Contribution
2
