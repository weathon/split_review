# Optimizing importance weighting in the presence of sub-population shifts

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
A distribution shift between the training and test data can severely harm performance of machine learning models. Importance weighting addresses this issue by assigning different weights to data points during training. We argue that existing heuristics for determining the weights are suboptimal, as they neglect the increase of the variance of the estimated model due to the finite sample size of the training data. We interpret the optimal weights in terms of a bias-variance trade-off,  and  propose a bi-level optimization procedure in which the weights and model parameters are optimized simultaneously. We apply this optimization to existing importance weighting techniques for last-layer retraining of deep neural networks in the presence of sub-population shifts and show empirically that optimizing weights significantly improves generalization performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses the challenge of distribution shifts between training and test data, specifically sub-population shifts. The authors propose a bi-level optimization framework to optimize importance weights while accounting for the finite sample size, thereby improving generalization. The method is validated on benchmark datasets from vision and NLP domains, demonstrating superior performance over traditional importance weighting methods.

### Strengths
1. The bi-level optimization of importance weights is novel, addressing the bias-variance trade-off more effectively than heuristic-based weighting.
2. The analysis using a linear regression model provides clear insights into the bias-variance tradeoff, making the proposed method more convincing.
3. The experiment section is comprehensive, covering multiple datasets.
4. The proposed method is useful in practice.

### Weaknesses
 1. The computational overhead of the proposed methods should be discussed. Since we only need to train on the last layer, I think the computational overhead is not large?
 2. The proposed method need to separate the training dataset into val dataset and remaining train dataset. What's the tradeoff here? What's the best way to split? If the training dataset is limited, will the proposed method work?

### Questions
see weakness section

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
2

### Summary
In this work, the authors develop a bi-level optimization algorithm for estimating importance weights (group weights) on top of existing deep learning algorithms, such as Group Weighted ERM and GDRO, to enhance generalization under sub-population shifts. They utilize a standard linear model to illustrate the necessity of this optimization in the presence of limited data and provide mathematical proofs to support their claims. Empirical demonstrations with deep networks using existing training strategies are presented, showing performance improvements on standard datasets.

### Strengths
The paper is well-written and systematically defines all terms and equations with attention to detail. It is mathematically well-supported and contains relevant experiments on standard benchmarks.

### Weaknesses
Refer to Questions

### Questions
* Can the authors clarify the overall outline of the training procedure? Did they follow the last-layer retraining protocol as described in Izamailov et al. (2022)? If so, additional details about this protocol would be beneficial.

* For the Group Weighted ERM procedure, it is mentioned that the likelihood ratio between the test and training distributions is required to initiate the proposed algorithm. However, in most cases, access to the test distribution is not available. How is this ratio computed for real-world datasets, such as Waterbirds? (I may have missed a key concept here.)

* Can the authors provide qualitative insights on how they believe the performance of their algorithms may vary with an increase in model scale, particularly for architectures like ViTs and SWIN?

* Can the authors include an example with large-scale datasets, such as ImageNet-1K, or a medical imaging benchmark (e.g., ISIC or MedMNIST) to enhance the impact of the proposed algorithms?

## Post-Rebuttal
I have increased my score and recommend acceptance

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies importance weighting of sub-population shifts. Conventional naive importance reweighting is $p_{te}(x,y)/ p_{tr}(x,y)$. This work argues that this conventional reweighting is sub-optimal under a limited training data size. Thus this work proposes to uses a learned importance reweighting coefficient. Empirical results show improved generalization performance across benchmarks like image and NLP datasets.

### Strengths
- The arguement that "the conventional importance weighting $p_{te}(x,y)/ p_{tr}(x,y)$ could be sub-optimal" is interesting. 

- This paper estimates model parameters and importance weights iteratively on train and iid-validation datasets. That is interesting, because it reduces the overfitting of training dataset. Different from conventional cross-validation and hyper-parameter search, this approach find the importance weights by optimization.

### Weaknesses
 - Experiments shows the good performance of the proposed method. However, Algorithm 1 (line 278 $p_0$ and line 282 $r$) requires the access of test dataset as parameter initialization. This could be problematic. I understand that some explicit reweighting methods, such as JTT, also contains some heuristic & data-dependent importance weights searching space. These heuristic hyperparameter searching space could also depends on test dataset.  However, group distributional robust optimization (GDRO) links to importance weighting in an implicit way [1], and doesn't contain any hints from test dataset. Thus, the comparison between the proposed method and GDRO is prolematic and potentionally unfair.

- minor typos: line 112 [L(y, fθ (x)] --> [L(y, fθ (x))]

### Questions
- How important are the $p_0$ and $r$ in Algorithm 1 line 278 and line 282? Currently these parameters depend on test dataset directly. And thus weaken the usefulness of the algorithm 1. Is it possible to set $p_0$ and $r$ by assuming a test dataset $p_{te}(g_i) = p_{te}(g_j) , \forall i,j $? If it is possible, how does it affect the experiments performances?  That is my main concern.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors present a bi-level optimization strategy to estimate optimal importance weights in the presence of distribution shifts. The authors use a linear regression model to demonstrate how the naïve but often used ratio of likelihoods is not necessarily an optimal choice for importance weights (figure 1.) The authors proceed to introduce their bi-level optimization strategy that estimates optimal weights given a validation set sampled from the training set.

The authors emphasize that the strategy can be used in conjunction with existing methods and write how they implement their strategy specific to each of five existing methods for fine-tuning models to manage distribution shift. The authors empirically test their claim using a benchmark of three datasets for each of the 5 modified methods and show how in almost all cases the performance on a held-out test dataset is improved using their bi-level optimization strategy.

### Strengths
To me the paper is a clear acceptance: it is well written, organized, to the point. You present an intriguing argument that the naïve choice of importance weights used in a variety of prior algorithms can be improved upon, present a practical answer of how to define and find these optimal weights, then show that this definition brings benefit over a controlled baseline. The topic clearly has potential for high impact as distribution shifts are pretty ubiquitous.

### Weaknesses
I think the paper could be improved with some additional discussion about the practical implementation of these strategies. For example, how much additional time is spent on your specific improvements compared to the naïve/heruristic weights? Roughly how does this time scale with the validation dataset fraction (1 – n’/n)? What additional hyperparameter tuning is done to find optimal weights (Appendix E.4)? Would a user need to repeat this hyperparameter tuning for their own model?

The impact of the paper could be heightened if the authors elected to demonstrate their technique improving upon a real-world challenge; for example, the authors identify in their introduction that importance weighting technique could be used to improve outcomes for algorithmic fairness.

I’ll focus specifically on the empirical experiments. I deem them overall sound, but I have a few questions to be sure. The authors describe fine-tuning a network 5 times to build a sample and perform their t-test. I wanted to confirm how that network was initialized (Appendix suggests you had the same base network that you then fine-tuned 5 different times?). It was then from this set of 5 fine-tuned networks that you then retrained the last layer using each algorithm’s original importance weight scheme and then compared to the paired performance when replacing with your optimal weights? What was controlled in this experiment in terms of random seeds? Were seeds controlling batch ordering varied between runs? Were seeds being varied between the pairs of optimal vs original weights?

The appendix describes some hyperparameters that had to be found for the optimal weight algorithm (E.4). Can the authors provide some additional detail about how these hyper parameters are found?

### Questions
I’ll focus specifically on the empirical experiments. I deem them overall sound, but I have a few questions to be sure. The authors describe fine-tuning a network 5 times to build a sample and perform their t-test. I wanted to confirm how that network was initialized (Appendix suggests you had the same base network that you then fine-tuned 5 different times?). It was then from this set of 5 fine-tuned networks that you then retrained the last layer using each algorithm’s original importance weight scheme and then compared to the paired performance when replacing with your optimal weights? What was controlled in this experiment in terms of random seeds? Were seeds controlling batch ordering varied between runs? Were seeds being varied between the pairs of optimal vs original weights?

The appendix describes some hyperparameters that had to be found for the optimal weight algorithm (E.4). Can the authors provide some additional detail about how these hyper parameters are found?

### Soundness
4

### Presentation
4

### Contribution
3
