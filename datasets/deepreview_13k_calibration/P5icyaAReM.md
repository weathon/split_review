# Stochastic Approximation to Contrastive Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Contrastive learning is a powerful paradigm that has been crucial for self-supervised representation learning. While there is evidence for its effectiveness, these methods typically rely on arbitrary definitions of positive and negative pairs. Most existing contrastive learning methods require large batch sizes during training due to their rigid control over the tradeoff between the two contrastive terms. Consequences are that, substantial computational resources are wasted on negative pairs that provide minimal learning signals. To address this issue, this work present a novel method. We reformulate contrastive learning as a matrix approximation problem using I-divergence, a non-normalized form of Kullback-Leibler divergence. Our proposed objective function is decomposable across instance pairs, enabling the development of efficient stochastic approximation algorithms from neighbor embeddings which perform well with fewer negative samples. Additionally, we generalize the scaling factor beyond normalization, allowing it to adaptively emphasize positive pairs that carry more learning signals, thereby reducing the computational waste associated with negative pairs. Experimental results on visual representation learning benchmark datasets such as CIFAR and ImageNet demonstrate major improvements over other contrastive learning methods, particularly when using small batches and with only one negative pair.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an approach to reformulate contrastive learning, used in many self-supervised learning methods such as SimCLR, in terms of matrix approximations. This reformation enables stochastic approximations of contrastive learning to enable good performance with smaller batch sizes. The authors validate the idea with experiments on CIFAR and ImageNet by measuring linear evaluation classification accuracy as well as embedding projections. The authors compare the method against standard self-supervised training method such as SimCLR as well as stochastic approximation methods such as SogCLR that also aim to reduce the need for large batch sizes in self-supervised training.

### Strengths
The authors study the important problem of revisting contrastive learning's reliance on large batch sizes. The authors present an interesting reformulation of contrastive learning by taking inspiration from stochastic cluster embeddings. This point of view is an interesting perspective on standard contrastive learning 
Experimentally, the authors train SACLR on CIFAR and ImageNet using standard setup and compare against a reasonable set of baselines. I appreciate the author's notes on which libraries were used for the method implementations, aiding reproducibility (although I do hope the authors also release code for the proposed method).

### Weaknesses
# Presentation
* The introduction is quite lengthy and rehashes broadly well-known statements about the role of deep learning. I'd recommend the authors trim this lengthy introduction. 
* With this gained space, I recommend 1) the authors describe in more detail the similarities and differences to existing stochastic methods such as SogCLR that also tackle the same challenge of large batch sizes in contrastive learning. 2) the authors consider illustrating the method visually with a method figure. Right now the method as presented in Section 3 and Algorithm 1 requires parsing many variables, with nested summations that muddy the overall idea and intuition. A high-level intuitive figure to illustrate the method can help a great deal in this regard.
* The performance gains on ImageNet are marginal compared to SogCLR (and I'd be curious how they compare to iSogCLR as well). While this doesn't diminish the contribution in itself, I do recommend the authors downtone the claims made in the introduction and abstract accordingly. 

# Claims
* The authors claim our method is "more computationally efficient" (line 72), "signficant computaitonal resources are wasted on negative pairs that offer little learnign signal" (line 61), and again in the abstract (line 24). This claim is missing exactly what the efficiency is relative to—is it existing efficient methods such as SogCLR or standard SimCLR? This needs clarification and evidence. To support this claim the authors should provide evidence of the GPU training hours, flops, or amount of memory saved, which right now I could not find.

* The authors state SCE requires fixed input similarites and cannot generalize to data points outside the training set (lines 177-179), after which they suggest their method overcomes these limitations with three modification (using a deep neural network, using augmented view and row-ise vector approximation), however, no further discussion of how these three modification address the two limitations highlighted is provided. Can you the authors respond provide a detailed justification for this claim?

- The authors only provide classification accuracy figures using linear evaluation. I recommend the authors also include other evaluation common approaches such as finetuning, KNN-evaluation, and retrieval (see for example SogCLR) to provide a more complete picture of the methods' benefits.

### Questions
- Performance on ImageNet100, I'm curious why the authors suspect the matrix versus row method difference is much larger on ImageNet100 compared to ImageNet?
- I'm confused by what the comparison in Figure 1 shows. Is t-SNE panel illustrating standard SimCLR feature projections compared to SACLR? If so, maybe a better label is warranted?
- Which dataset is used in the ablations for figure 2? I'm also curious how the linear evaluation accuracy compares for SACLR-1 versus SACLR-all.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the contrastive learning paradigm, which is a typical and important representation learning method. Concretely, this paper focuses on its substantial computation resources and inspired by the Stochastic Cluster Embedding (SCE) method, authors reformulate contrastive learning as a matrix approximation problem, thus the objective function can be decomposable over instance pairs and generalize well for smaller batchsize. Extensive experiments are conducted on the CIFAR and ImageNet datasets to validate the effectiveness of the proposed loss.

### Strengths
+ The investigated problem is meaningful. 
+ The writing is good. The derivation of the mathematical formula is convincing. 
+ The experimental results are comprehensive.

### Weaknesses
Overall, this paper is readable and the proposed loss is convincing. But I still have some concerns as follows. 

- The logic behind the proposed loss over the robustness to the fewer negative samples is unclear. Since B refers to the batchsize, I do not see the analysis over various B in the formula or theorem. Specifically, it's not clear how the proposed method handles the increased variance in gradient estimation when the batch size, and thus the number of negative samples, is reduced. The paper should provide a more detailed explanation of how the proposed loss function mitigates the instability that typically arises with fewer negative samples, perhaps through a theoretical analysis or empirical study of gradient variance under varying batch sizes.

- The computational complexity should be analyzed or empirically investigated since it needs to calculate s in Eq.(6). The paper should provide a more detailed analysis of the computational cost associated with calculating 's' in Equation (6), especially in comparison to other contrastive learning methods. A breakdown of the operations involved and their time complexity would be beneficial. Furthermore, empirical evidence demonstrating the actual runtime overhead of calculating 's' would strengthen the analysis.

- The baseline methods are sort of weak. Since it focuses on the smaller batchsize, some other competing methods in terms of smaller batchsize should be included as well. For example, ReSSL (NeurIPS 2021) achieves 69.9% (Table 6) on ImageNet with ResNet50 which is much higher than that in this paper.

### Questions
Please refer to the Weaknesses.

### Soundness
4

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
3

### Summary
This paper addresses the problem of large batch sizes required for training networks under contrastive loss. The authors use ideas from Stochastic Cluster Embedding to represent the contrastive loss as a matrix approximation problem with approximation quality measures by I-divergence, an unnormalized form of KL divergence. To adapt the Stochastic Cluster Embedding setup to representation learning under contrastive loss, the authors represent the embedding using a neural network. The authors provide two algorithms: one with a row-wise scaling/normalization factor (similar to SimCLR under uniform normalization) and one with a single scaling/normalization factor over the whole matrix. In both cases, the authors treat the scaling factor as a constant during gradient computation, with the scaling factor updated after every iteration using a weighted sum of the values of the embedding matrix. The weighted formulation of the scaling factor allows the objective to emphasize the positive samples as training progresses.

The authors also apply the proposed methods on CIFAR and Imagenet datasets to demonstrate the superior performance of the proposed methods compared to other current SOTA Contrastive Learning methods.

### Strengths
The paper also addresses an important problem concerning the scalability of Contrastive Learning algorithms. The paper draws inspiration from the Stochastic Cluster Embedding paper to propose a novel formulation of the constrastive learning loss function.
The proposed weighting function $w$ to calculate the scaling factor $s$ during training provides a novel and interesting way to adaptively trade off the weight of signals from the positive and negative pairs during training.

### Weaknesses
While the theoretical motivation of the paper is quite interesting, it is not clear why the scaling quantity $s$ is considered to be a constant in the loss function. As seen later in the paper, $s$ is a function of $q^{uv}_{ij}$ and changes during training. The authors should clarify the implications of treating $s$ as a constant during gradient computation, especially given that $s$ is updated based on the embedding matrix values. The justification for this approximation needs to be more rigorous, as it could potentially lead to instability or suboptimal convergence. A more detailed analysis of the impact of this approximation on the loss landscape would be beneficial.

While the experiments on CIFAR and Imagenet show a slight performance improvement, the experiments do not include any variance bounds on the reported metrics. Without any confidence bounds, the proposed methods' relative performance boost is unclear. The lack of reported standard deviations makes it difficult to assess the statistical significance of the observed improvements. It is crucial to include these variance measures to ensure that the reported gains are not simply due to random fluctuations in the training process. Furthermore, the paper should include statistical tests to validate the significance of the performance differences.

Furthermore, the paper doesn't include any experimental data on the runtime or memory improvements the proposed method provides. It is unclear how much efficiency can be gained using $M=1$ instead of $M>1$ negative samples in a batch. It would be great to see the performance differences as well as runtime differences between the baselines and the proposed method under different values of $M$. The paper should provide a detailed analysis of the computational cost of the proposed method, including both runtime and memory usage, under different batch sizes and values of $M$. This analysis should be compared against the baselines to demonstrate the practical advantages of the proposed approach.

### Questions
Please refer to the Weakness Section for the questions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study proposes a method, SACLR, inspired by Stochastic Cluster Embedding (SCE), a similarity-based nonlinear dimensionality reduction (NLDR) technique. SACLR reformulates contrastive learning as a matrix approximation problem using I-divergence, an unnormalized form of Kullback-Leibler divergence.

### Strengths
This study proposes the SACLR method, which enhances existing contrastive learning approaches. Representations learned through SACLR are optimized to support effective clustering.

### Weaknesses
This study lacks novelty in its methodology. SACLR appears to be a straightforward application of SCE, incorporating a few modifications to SCE. However, the study does not sufficiently explain why these modifications are important or what roles they play within the model framework.

Theorem 1, the only theoretical result presented in this study, fails to justify why SACLR would be expected to outperform SimCLR. Since Theorem 1 does not highlight any specific advantages of SACLR over existing contrastive or non-contrastive methods, including SimCLR, the theoretical contribution appears limited in its significance.

From an experimental standpoint, there is also an inadequate comparison of SACLR’s performance across diverse benchmarks. Many studies have introduced methods that significantly improve upon SimCLR, yet these methods are omitted from the benchmark comparisons in this study.

Additionally, the study lacks a comprehensive ablation analysis. Although it claims that adjusting the scaling factor can reduce computational waste, there is neither a theoretical explanation for why this adjustment reduces computation nor a rigorous ablation study to support this claim. Similarly, while the study asserts that SACLR performs well with small batch sizes, it does not provide an extensive ablation analysis to substantiate this claim.

### Questions
In Figure 1, this study demonstrates that SACLR achieves effective clustering. However, does strong clustering necessarily indicate a good representation? Additionally, is there evidence that SACLR performs well on various downstream tasks beyond clustering?

### Soundness
2

### Presentation
2

### Contribution
1
