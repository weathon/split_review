# Harnessing Orthogonality to Train Low-Rank Neural Networks

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
This study explores the learning dynamics of neural networks by analyzing the singular value decomposition (SVD) of their weights throughout training. 
Our investigation reveals that an orthogonal basis within each multidimensional weight's SVD representation stabilizes during training.
Building upon this, we introduce Orthogonality-Informed Adaptive Low-Rank (OIALR) training, a novel training method exploiting the intrinsic orthogonality of neural networks.
OIALR seamlessly integrates into existing training workflows with minimal accuracy loss, as demonstrated by benchmarking on various datasets and well-established network architectures. 
With appropriate hyperparameter tuning, OIALR can surpass conventional training setups, including those of state-of-the-art models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces an innovative training approach known as "Orthogonality-Informed Adaptive Low-Rank Neural Network Training." The method is rooted in the hypothesis that the orthogonal bases of the low-rank decomposition of neural network weights become more stable during training. By following standard tuning procedures, this proposed method outperforms conventional training setups. Additionally, the paper demonstrates the effectiveness of the tuned low-rank training procedure by applying it to enhance the performance of a state-of-the-art transformer model designed for time series prediction.

### Strengths
This paper showcases a commendable strength in its comprehensive and rigorous experimental methodology. The research rigorously evaluates various neural network architectures across diverse datasets, thus ensuring the generalizability and robustness of the proposed approaches. Notably, the experiments extend to the training of the OneFormer on the challenging CityScapes dataset, mini-ViT on CIFAR-10, and Autoformer on ETTm2, demonstrating the versatility and adaptability of the methods across distinct application domains and scenarios. This meticulous experimentation contributes significantly to the paper's credibility and the trustworthiness of its findings.

### Weaknesses
The progress towards achieving a state-of-the-art (SOTA) model is somewhat constrained. While the incremental improvements made in this work are commendable, a more extensive exploration of novel approaches or the inclusion of additional techniques may be necessary to achieve a substantial leap in performance that rivals the current SOTA models in the field.

### Questions
Why does the training time not exhibit a significant reduction even as the number of trainable parameters decreases substantially, from 100% to just 9.97%?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a low-rank neural network update method (OIALR) via SVD decomposition.  Experiments on various network architectures and learning tasks show that the proposed OIALR achieves a slight accuracy loss with fewer parameters.

### Strengths
1. The paper is well-written and well-organized. 

2. The authors provide experimental evaluations on various tasks and different network architectures.

### Weaknesses
1.  $	extbf{Marginal Contribution}$.

The orthogonal neural networks and low-rank neural networks are widely studied in the literature.  The technical contribution of this paper is marginal.  Low-rank neural networks and low-rank fine-tuning via SVD decomposition are not new.  The proposed Algorithm 2 seems to be an incremental variation compared with previous works. The core idea of using SVD for low-rank approximation and subsequent fine-tuning is not novel, and the paper does not adequately highlight any significant departure from existing methods. Specifically, the incremental update of the low-rank factors via SVD, as presented in Algorithm 2, appears to be a straightforward application of well-established techniques, lacking a clear demonstration of unique innovation.

2.  $	extbf{No discussion about the difference between the proposed algorithm and previous works}$

In this paper, the authors fail to provide a detailed discussion about the difference between the proposed algorithm and previous low-rank methods.  It is unclear what is the advantages and disadvantages of the proposed method compared with previous low-rank neural network methods. The paper lacks a rigorous analysis of how the proposed method differs from existing low-rank approaches, such as those based on matrix factorization or tensor decomposition. A thorough comparison should include a discussion of computational complexity, convergence properties, and the sensitivity to hyperparameter choices, which are not addressed in the current manuscript.


3.  $	extbf{No comparison with related baselines}$

In this paper, there is no empirical comparison with related low-rank methods to support the advantage of the proposed method.  It is unconvincing to distinguish the proposed method from related low-rank methods without experimental compassion. The experimental evaluation is incomplete without a direct comparison to established low-rank methods. The paper should include a comparative analysis against methods like low-rank matrix factorization, tensor decomposition, or other relevant techniques, to demonstrate the proposed method's effectiveness and potential advantages.

### Questions
Q1. Could the authors discuss the differences and advantages/disadvantages of the proposed method compared with related low-rank methods?

Q2.  Could the authors provide a comprehensive experimental comparison with low-rank neural network baselines? 

Q3. What is the improvement of Algorithm 2 compared with a trivial baseline, i.e.,   low-rank approximation of a well-trained full-rank network?  

Q4.  What is the size of the trainable parameter $\Sigma$ in Algorithm 2? It seems that the size of the $\Sigma$ is the same as the size of $W=U \Sigma V^\top $.  If so, what is the difference and advantage of Algorithm 2 compared with a standard full-rank training of $W$? In addition, what are the advantages/disadvantages of Algorithm 2 compared with full-rank training of $W$ and low-rank approximation/fine-tuning at the last step?

Q5.  In the paper, the authors argue the "Stability" of the proposed method. What is the formal definition of the "Stability"? Why does the proposed method achieve "Stability"  compared with other low-rank methods?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the hypothesis that the orthogonal bases of the low-rank decomposition of neural network weights stabilize during training. The authors introduce Orthogonality-Informed Adaptive Low-Rank (OIALR) neural network training, which seamlessly integrates into existing training workflows with minimal accuracy loss. Experimental evidence is provided to support the hypothesis, and the effectiveness of the OIALR training approach is demonstrated through benchmarking on various datasets and network architectures.

### Strengths
1. The paper is easy to follow. 
2. The idea of orthogonal bases of the low-rank decomposition is reasonable.

### Weaknesses
1. The experimental results presented seem limited, with only two models tested and no comparisons to prior work. This makes it challenging to verify the effectiveness of the proposed method. It would be beneficial to include additional models and draw comparisons with previous works.
2. The algorithm initially trains the full-rank network during the initial epochs. As such, it might be more suitable for the term "full-rank to low-rank training" rather than strictly low-rank training. And what's the effect of removing the full-rank training phase?
3. How does this method compare in terms of advantages to existing pruning and quantization techniques? Or sparse training work[1]?

### Questions
Check the Weaknesses. 
More convincing experiments are needed.

### Soundness
2 fair

### Presentation
3 good

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
The paper starts by defining a notion called relative stability and illustrating the stability of network weights during training tends to plateau early on. Such observation motivates the authors to develop the method Orthogonality-Informed Adaptive Low-Rank (OIALR). This approach starts with an SVD of the weight matrices ($U \Sigma V^T$) and only updates $\Sigma$ at the majority time of training. This strategy significantly trims the number of training parameters. Empirical data further substantiates that the OIALR method either matches or marginally underperforms when compared with the baseline full-rank training, yet is less prune to overfitting.

### Strengths
1. The paper is overall well-written and clearly motivated.
2. The proposed method which only updates the $\Sigma$ matrix is quite interesting.
2. The reviewer personally appreciates the authors for reporting the untuned results.

### Weaknesses
A major contribution listed in the paper is reducing the number of trainable parameters during training hence allowing shorter training time and enabling fine-tuning and production on resource-constrained devices (as stated by the authors in the Conclusion section). Yet, this assertion seems not well substantiated by the experiments: (1) based on the experiments listed in the paper, OIALR shows nearly identical training time as the baseline and sometimes requires even longer time; (2) concerning memory allocation, the OIALR method, especially at step 7 in Algorithm 2, demand more memory than the baseline (factorizing a matrix to 3 matrices increase its memory cost) and throughout the training for a long time until $r$ is decreased to some small value. Hence the resource reduction is questionable; (3) if we instead consider the RAM consumption during training (given OIALR's reduced parameter count), there might indeed be potential savings. However, the paper lacks empirical validation in this context (e.g., a table to compare the RAM used between OIALR and the baseline). Given these observations, the reviewer finds it hard to evaluate the contribution of the paper as of the current version.

### Questions
1. In Figure 1, the stability measure exhibits an initial decline followed by a subsequent rise. What could account for this initial drop in the early stages?
2. In some of the experiments shown in the paper, the authors show the results for both tuned and untuned OIALR, but not in other experiments, which is a bit confusing to the reviewer. Is this due to time or resource constraints? 
3. To clarify, in Section 3, the authors wrote "To obtain a two dimensional (2D) representation of a weight tensor with more than two dimensions we maintain the original weight’s leading dimension and collapse those remaining", does this mean that for a tensor with dimension $a \times b \times c$, it will be transformed to a matrix with dimension $ a \times (bc) $?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
