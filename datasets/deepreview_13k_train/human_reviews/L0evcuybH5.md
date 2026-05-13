# Projection Head is Secretly an Information Bottleneck

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
Recently, contrastive learning has risen to be a promising paradigm for extracting meaningful data representations. Among various special designs, adding a projection head on top of the encoder during training and removing it for downstream tasks has proven to significantly enhance the performance of contrastive learning. However, despite its empirical success, the underlying mechanism of the projection head remains under-explored. In this paper, we develop an in-depth theoretical understanding of the projection head from the information-theoretic perspective. By establishing the theoretical guarantees on the downstream performance of the features before the projector, we reveal that an effective projector should act as an information bottleneck, filtering out the information irrelevant to the contrastive objective. Based on theoretical insights, we introduce modifications to projectors with training and structural regularizations. Empirically, our methods exhibit consistent improvement in the downstream performance across various real-world datasets, including CIFAR-10, CIFAR-100, and ImageNet-100. We believe our theoretical understanding on the role of the projection head will inspire more principled and advanced designs in this field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the design choices of the projection head in contrastive learning, and shows that the projection head should serve as a proper information bottleneck that keeps only "useful" information related to the class label or the contrastive objective.

For the problem setup, consider the information flow of $Y \rightarrow X \rightarrow Z_1 \rightarrow Z_2 \rightarrow R$, where $Y$ is the semantic info (e.g. class label), $X$ is the observable/input, $Z_1$ is the pre-projection head features, $Z_2$ is the projection head output, and $R$ is the contrastive label.
The paper argues that we should focus on $I(Y; Z_1)$ (rather than $I(Y; Z_2)$), since the projection head is discarded in downstream training.

The main results are as follows:
- It provides **upper and lower bound on the downstream performance** for the pre-projection head features.
  - Lower bound: $I(Y;Z_1) \geq I(Z_1; R) - I(Z_1; Z_2) + \text{const}$, where $\text{const} = I(R;Y)$ is not affected by the learned features.
  - Upper bound: $I(Y; Z_1) \leq I(Y; Z_2) - I(Z_1; Z_2) + H(Z_1)$.
- We want to adjust the terms on the right hand side so that the bounds are tighter, which leads to **two modifications**: 1) adding a mutual-information-based regularization term in the training objective, and 2) modifying the projector architecture.
  - The **mutual information regularizer** $I(Z_1; Z_2)$: estimated using the matrix mutual information (Renyi entropy) as the surrogate. The matrices are $\hat{Z}_1\hat{Z}_1^\top, \hat{Z}_2\hat{Z}_2^\top$, where $\hat{Z}_1, \hat{Z}_2$ denote the normalized feature matrix before and after the projection head.
    - Result: The accuracy improvements are slightly higher for Barlow Twins than for SimCLR.
  - 2 types of **structural regularization**, both meant to bottleneck the information allowed by the projection head.
    - Discretized projector: the output is discretized into $L$ integer values.
    - Sparse projector: using the top-k activation function, which keeps the $k$ largest hidden representation. 
        - The experiments use $k=0.001d$ or $k=0.2d$, where $d$ is the projector's latent dimension.

### Strengths
- The proposed changes are motivated by the terms in the mutual information-based lower and upper bounds.
- The proposed changes lead to an 0.26 to 3.99 increase in the accuracy of SimCLR and Barlow Twins on CIFAR-10, CIFAR-10, and ImageNet-100.

### Weaknesses
Since the theoretical results of the paper are not strong enough to serve as a major contribution, the empirical results should be strong.

However, the relation between the derived bounds and the empirical results are not strong: the correlation is computed based on a small number of points (please see the question below), and there is no correlational result on Barlow Twins.

### Questions
- Fig 2: the curves are only shown up to 100 epochs, at which point the validation accuracy hasn't saturated. What happens to epoch 100-200 (Sec 4 mentions that the models are trained for 200 epochs on CIFAR-100)?
- Do you observe the same trends on other datasets (i.e. CIFAR-10 and ImageNet-100, which are partially shown in Fig 3) and from Barlow Twins?
- Fig 3: are these results varying across training hyperparameters (e.g. learning rate, weight decay, augmentation strengths, temperature of the contrastive objective)?
- For the accuracy: since the paper is based on mutual information, the downstream experiments should also consider nonlinear evaluation, i.e. making the downstream classifier sufficiently powerful to make sure the performance is actually bottlenecked by the "information" in the representation rather than by the classifier.
- Does combining several of the 3 proposed changes lead to further improvements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- The paper proposes that contrastive methods using separate representation layers (for downstream tasks) and projection heads (for computing the contrastive loss) are actually taking advantage of an Information Bottleneck between the representation layer and the projection head.
- The authors derive lower and upper bounds on I(Y;Z_1) (the Mutual Information between the downstream target, Y, and the representation Z_1) that show an I(Z_1;Z_2) term being minimized (where Z_2 is the projection layer’s representation).
- The authors show a correlation between their bounds and the validation set accuracy to attempt to justify their theoretical claims.
- The authors then use an estimator of I(Z_1;Z_2) as a regularizer in the contrastive loss and show empirically that using that regularizer improves performance on the downstream classification task for three image classification problems.
- The authors then compare with two previously-studied “structural” regularizers that (they argue) also minimize I(Z_1;Z_2) and show that those regularizers also improve performance on these classification tasks.

### Strengths
- The writing is generally clear and easy to follow.
- The paper gives an Information Theoretic explanation for why the projection head is important in many contrastive loss settings.
- The paper proposes a method to directly minimize the claimed quantity of interest, I(Z_1;Z_2) and shows that using that minimizer can improve accuracy on the downstream classification task.
- The paper provides an explanation for the effectiveness of aggressive bottlenecking between the representation layer and the projection head.

### Weaknesses
 - Line 154: The simplest relationship of interest is that I(Y;Z_1) >= I(Y;Z_2), by the data processing inequality, so maximizing I(Y;Z_2) also maximizes I(Y;Z_1), which you acknowledge as the quantity of interest. Since by assumption we don’t have access to Y, we are limited to maximizing I(X;Z_2), which is what many SSL objectives do (including InfoNCE); again by the data processing inequality, I(X;Z_1) >= I(X;Z_2). But in the limit when I(X;Z_2) approaches H(X), I(Y;Z_2) must be maximized. While my view is that correct compression is important for learning good representations, this kind of information maximization argument is common in SSL (since you don't know what the downstream task is, why would you want to throw out any information in the representation?), so I think it is important to be careful how you justify your approach.
- Thm 3.2, line 209: You appear to be using I(Y;Z_1|Z_2) = H(Z_1|Z_2) - H(Z_1|Y,Z_2) and then assuming that H(Z_1|Y,Z_2) >= 0, but that is not guaranteed unless Z_1 is discrete, which it probably isn’t. So it seems to me that the bound is broken, or at least that your proof of the bound may be incorrect. Have I misunderstood your justification for the inequality in line 209?
- Figure 2a: The lower bound estimate is non-monotonic with a noticeable (but small) peak at 80 epochs, even though validation accuracy increases monotonically through epoch 100. This indicates that you should probably run more experiments to get more robust statistical results, or that your analysis is not perfectly accurate. Or perhaps some other explanation, but it doesn’t appear to be addressed in the paper, as you claim (line 264) that the lower bound “continuously increase[s]”.
- More generally, the “Tendency during training” paragraph is weak, as there are many quantities that can generally increase during training while accuracy is increasing, without real explanatory power, such as weight magnitudes.
- The two “structural” regularizers were already known to improve downstream task performance, so it is not clear to me that the empirical results are adding much to the presentation, although they do show that (in the settings you consider) the explicit minimization of I(Z_1;Z_2) is less effective than just using a strong architectural bottleneck.
- It might be helpful in Figure 1 to show how Z_1 is used in downstream tasks – i.e., add an edge Z_1 \to \hat{Y} or something like that.
- Line 152: “pipline” => “pipeline”.

### Questions
- Line 250: why do you set \alpha=2? Wouldn’t \alpha=1 correspond to the Shannon Mutual Information? Is there some benefit to distorting the Shannon Information in this setting?
- Given that the “structural” regularizers are more effective than the direct minimization of (an estimate of) I(Z_1;Z_2), my sense is that this paper needs to do more work to demonstrate that the “structural” regularizers improve performance for the stated reason (that they minimize I(Z_1;Z_2)). I don’t contest that they *are* reducing I(Z_1;Z_2), but I would like to know that there isn’t some alternative hypothesis that better explains the improvement in performance. Alternatively, perhaps it’s worth considering a variational approach to minimizing I(Z_1;Z_2), such that you can properly bound I(Z_1;Z_2) – perhaps the relatively poor performance of your objective-based approach is due to using an estimate of I(Z_1;Z_2) rather than a proper bound? All that being said, I think the underlying hypothesis is plausible, so I welcome your pushback on my concerns about the paper. I’m open to good arguments to increase my rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper analyzes the performance of encoder features (before projection head) in contrastive learning. Using an information-theoretic perspective, it derives bounds on the mutual information of the encoder features with the labels. Based on these bounds, it concludes that a good projection head removes unnecessary information from encoder features. It then proposes training and structural modifications to this end, and validate the effectiveness empirically on a few datasets.

### Strengths
The paper provides a novel analysis of pre-projection features in contrastive learning based on mutual information. The proposed modifications to contrastive learning are well motivated by the theory, and the experiments help validate the theory. 

The paper is overall pretty easy to follow.

### Weaknesses
See questions.

### Questions
I wonder if/how the analysis can be applied to supervised learning, e.g. could features from before the last layer in supervised learning also be improved in a similar fashion?

What is the impact/motivation for the choice of $\alpha$ in the matrix based mutual information?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to understand the role of the projection head in contrastive learning from an information-theoretic perspective. Treating the mutual information between the supervised label Y (potentially in downstream tasks) and the learned representations Z1 (before the projection head) as the metric for downstream task accuracy, this paper presents both the lower and upper bounds based on mutual information between features at different layers and proposes that the term I(Z1;Z2) as the information gap plays an important role. To boost the performance of downstream tasks, this paper proposes two types of modified loss functions to regularize the term I(Z1;Z2).

### Strengths
1. It is novel to view the projection head as information bottle neck, which provides one way to regularize the infoNCE loss to directly boost the downstream performance
2. Different types of regularization are proposed in this paper, which enables the cross-comparison and validates the consistent improvement over the canonical infoNCE loss.

### Weaknesses
1. The performance of downstream task (e.g. classification accuracy) is related to mutual information implicitly. Thus, using mutual information between Y and Z1 as the target to justify the claim seems insufficient to me. It would be very helpful to provide concrete toy examples to relate the downstream accuracy and the mutual information in an explicit way. In this sense, the information gap I(Z1;Z2) seems to be a reasonable motivation for the regularized loss, but is not strong enough as a theoretical explanation to fully understand the role of the projection head.
2. The message conveyed in experiments is not clear enough. 
	- For example, in Figure 2 and 3, instead of the comparison between lower bound VS downstream accuracy, as the claim of this paper is the role of I(Z1;Z2), it would be more insightful to plot downstream accuracy VS I(Z1;Z2).
	- In addition, in Figure 4, it would be more helpful to compare the proposed methods in terms of the downstream accuracy with more datasets to see if the ranks of all methods remain consistent.



### Questions
1. [Theorem 3.1 and 3.2] Regarding the lower and upper bounds for the mutual information I(Y,Z1) as the proxy of the downstream accuracy, there are three terms in each bound, in which, the effect of I(Z1;R) (or I(Y;Z2)) and I(Z1;Z2) are mixed. Also, as  is shown in Figure 2, both the upper and lower bounds are not tight, it is not sufficiently convincing to claim that the role of the projection head is only revealed via I(Z1;Z2). I was wondering if we could design experiments (e.g. fixing the encoder) such that other terms in the bounds are fixed to study the role of I(Z1;Z2).
2. [Calculations of mutual information] Suppose there exist perfect features Z1 such that Z1 = Y almost surely. This corner case with infinity mutual information should be taken care of.
3. [Figure 3] It seems that points in the right-top corner are more close to a horizontal line. Is it because the upper and lower bounds are not tight enough?
4. In addition, there are several related papers investigating the role of the projection head:
	- Saunshi, Nikunj, Jordan Ash, Surbhi Goel, Dipendra Misra, Cyril Zhang, Sanjeev Arora, Sham Kakade, and Akshay Krishnamurthy. "Understanding contrastive learning requires incorporating inductive biases." In International Conference on Machine Learning, pp. 19250-19286. PMLR, 2022.
	- Gui, Yu, Cong Ma, and Yiqiao Zhong. "Unraveling Projection Heads in Contrastive Learning: Insights from Expansion and Shrinkage." arXiv preprint arXiv:2306.03335 (2023).
	- Wen, Zixin, and Yuanzhi Li. "The mechanism of prediction head in non-contrastive self-supervised learning." Advances in Neural Information Processing Systems 35 (2022): 24794-24809.
	- Xue, Yihao, Eric Gan, Jiayi Ni, Siddharth Joshi, and Baharan Mirzasoleiman. "Investigating the Benefits of Projection Head for Representation Learning." arXiv preprint arXiv:2403.11391 (2024).

I am open to raising my score if the more explicit connection between the mutual information I(Y;Z1) and the downstream accuracy can be presented in some concrete settings, and if fine-grained analysis can be provided to study the tightness of the lower and upper bounds.

### Soundness
2

### Presentation
3

### Contribution
2
