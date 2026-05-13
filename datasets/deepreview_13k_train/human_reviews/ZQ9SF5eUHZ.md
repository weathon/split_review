# Learn from the Past: Dynamic Data Pruning with Historically Weighted Bernoulli Sampling

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Dynamic data pruning, which also known as data importance sampling, has been proposed to improve training efficiency. For the case of sampling with replacement, the optimal sampling distribution to minimize the variance is to sample proportional to the gradient norm, which can be approximated by the gradient norm of the logits from an extra forward pass. However, this could result in repeated samples, which can be an undesirable property. Noticing that most dynamic data pruning methods that avoids repeated samples can be seen as weighted Bernoulli sampling, in this work we study the optimal distribution to reduce its variance. Furthermore, to avoid an extra forward pass, we study the use of historic statistics. We propose the use of exponential moving average and probability smoothing to improve the performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a weighted Bernoulli sampling method, called Omission, for dynamic data pruning, which can minimize the variance of the gradient estimate without the problem of repeatedly selected samples in sampling with replacement. Aside from this theoretical motivation, the method Omission is also made more practically robuste and implementable through techniques of score smoothing, score normalisation, and estimation of the sample gradient squared norm from historical statistics. The provided experimental results on tasks of image classification and LLM instruction finetuning attest to the competitive performance of Omission. An ablation study was carried out to investigate the importance of the practical techniques used in the implementation of Omission.

### Strengths
* The proposition of a dynamic data pruning method that yields an unbiased gradient estimate of minimal variance while avoiding the selection of repeated samples is a valuable theoretical contribution.

* In addition to the solide theoretical foundation, several practical techniques are employed for a more efficient and robust implementation of the proposed weighted Bernoulli sampling scheme.

* An extensive empirical study is provided, where the proposed algorithm is observed to perform competitively against a range of related algorithms.

### Weaknesses
 * Considering that the empirical results are reported over only four trials, the observed performance gains of Omission, which are not always significantly large with respected to the error bars, may be induced by the randomness of trials.


### Questions
* Would the empirical performance gains of Omission remain stable when the number of trials is increased?

* Why is the performance of full training not provided for the experiments reported in Table 4? And what is the pruning ratio used in these  experiments?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies dynamic data pruning, also known as data importance sampling, which has been proposed to improve the efficiency of training large machine learning models. In Section 2, Background, the reason for dynamic sampling is well explained by establishing the inequality (2). The main point of this paper is to propose a new way to choose p_i as in Theorem 1 (similarly in Theorem 2) so that a smaller upper bound in inequality (2) can be achieved. The rest of the paper details how to implement the formula in Theorem 1 and 2.

### Strengths
Overall, a well written paper. It's easy to follow the main idea.

### Weaknesses
Section 3.2.1 EXPONENTIAL MOVING AVERAGE OF GRADIENT NORM SQUARED is not clearly written. This reviewer has difficulty to see the value of this subsubsection. It should be better motivated. 

In theorem 1 and 2, the determination of p_i requires ||g_i||, for all i=1,\ldots, n (or B), which may not be realistic. It seems that this will be the limitation of the proposed approach. The authors tend to address it in the paper. However, there doesn't seem to be a convincing solution. If one can't compute ||g_i|| for all observations (samples), then the proposed method doesn't seem sensible. Nevertheless, I am unsure how we should consider this in our evaluation...

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on improving dynamic data pruning or data importance sampling,
with the goal of enhancing the training efficiency of large machine learning
models by skipping less critical samples during training. The authors adopt
Bernoulli sampling to avoid repeated samples and derive the optimal distribution
to minimize variance. They propose a method called Omission for implementation.
Numerical experiments were conducted on image classification tasks (CIFAR-10,
CIFAR-100, ImageNet-100) and large language model (LLM) fine-tuning tasks.

### Strengths
Numerical experiments were conducted on image classification tasks and large language model fine-tuning.

### Weaknesses
The paper lacks novelty and originality. The optimal sampling distribution has
already been derived more rigorously and investigated more deeply in previous
works for various settings. Some relevant earlier references are listed below,
and there have been additional developments since then:

- Ting, D., Brochu, E. Optimal subsampling with influence functions. *Advances in Neural Information Processing Systems*, 2018; 31. 
- Wang, H., Zou, J. A comparative study on sampling with replacement vs Poisson sampling in optimal subsampling. In *International Conference on Artificial Intelligence and Statistics*, 2021 Mar 18 (pp. 289-297). PMLR.

The statement "in practice we can keep sampling until a fixed batch size is
reached" is scientifically incorrect. Doing so changes the distribution of the
selected samples, rendering all theoretical results invalid.

Notations are poorly defined, leading to many confusing statements. For example,
what are the relationships among $n$, $B$, and $b$? How does the batch variance
relate to the empirical loss? Additionally, from the second sentence of Section
3.2, it appears that you are only focusing on the logit loss, which could easily
confuse readers who are not already experts in the field. Clearer explanations
and definitions are needed to make the content more accessible.

### Questions
1. Do you mean an argument in an existing software package when you say "drop_last=True"?  
2. What is the meaning of the numbers in the tables?  
3. Why discuss Table 1 and Table 5 first, before the other tables? Why not move Table 5 to be Table 2?  
4. What is the "Prune Ratio"?  
5. The lines in the figures are not distinguishable in grayscale.

### Soundness
2

### Presentation
3

### Contribution
2
