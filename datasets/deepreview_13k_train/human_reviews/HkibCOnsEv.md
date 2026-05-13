# Structured Inverse-Free Natural Gradient: Memory-Efficient & Numerically-Stable KFAC for Large Neural Nets

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Second-order methods for deep learning---such as KFAC---can be useful for neural network training.
However, they are often memory-inefficient and numerically unstable for low-precision training since their preconditioning Kronecker factors are dense, and require high-precision matrix inversion or decomposition.
Thus, such methods are not widely used for training large neural networks such as transformer-based models.
We address these two issues by (i) formulating an inverse-free update of KFAC and (ii) imposing structures in each of the Kronecker factors, resulting in a method we term structured inverse-free natural gradient descent (SINGD).
On large transformer- and convolution-based models, we show that, in contrast to KFAC, SINGD is memory efficient and numerically robust.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method called Structured Inverse-Free Natural Gradient Descent (SINGD) to address the memory inefficiency and numerical instability issues of second-order methods like KFAC for training large neural networks. SINGD combines an inverse-free update and imposes sparse structures of each Kronecker factor. Experimental results on transformer-based and convolution-based models demonstrate that SINGD outperforms KFAC in terms of memory efficiency and numerical robustness.

### Strengths
This paper is well-written and organized.  This work presents SINGD method to improving the efficiency and stability of second-order optimization methods for deep learning.  Under certain conditions, they make a connection between the INGD method and the KFAC method. Furthermore, they extend the original INGD and develop memory-efficient SINGD method by imposing special structures in the Kronecker factors.

### Weaknesses
This article provides a very detailed and specific introduction to KFAC and INGD method. However, it seems not highlight the contribution of this article itself. Some details on sparse kronecker factors are put in the appendix or skipped. Some derivation process and proofs of the algorithm could be included in the main text rather than in the appendix, which would make the algorithm more naturally presented.


More detailed comparisons with other state-of-the-art optimization methods such as Shampoo[1] and NGPlus[2] would strengthen the case for the superiority of SINGD. In Fig. 6, it is better to show the changes of the test error with respect to the training time. Besides, it is important to report the peak memory for these four neural networks.

### Questions
From my experience, for experiment VGG16 on CIFAR100 dataset, the KFAC method should be tuned carefully. I want to ask if the search space of hyperparamters of KFAC method is large enough?

The difference between this paper and the INGD paper should be stated clearly and properly. As shown in Figure 4, the difference is that the use of projection $\hat{\Pi}_K$ and the structures $\hat{\mathcal{L}}$ in SINGD. Could you please give a specific example to show how to compute the projection and how to use the strcuture?

Why the NGD update for BLR can be simplified as the equations in the end of Page 4? Please add some explanation.

Does $O(\beta_1^2)$ small enough in Theorem 1?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors describe a novel variant of INGD, sparsifying updates in the INGD step. Structured Kronecker factors are also used to obtain a matrix-free variant of KFAC. These approaches allow for low-precision training and memory savings over their respective matrix based variants which suffer from numerical issues due to the numerical instabilities of solving lin. systems in low precision. The approach is well-written but could use some more experimental results to demonstrate the effectiveness of the method.

### Strengths
- well-written theory exposure that draws a bridge between INGD and KFAC
- The method is well-motivated and and well-explained.

### Weaknesses
 - While Figure 1 provides memory footprints, these could be better-described and contextualised. Also timings would have been a welcome addition.
- It would have been great to have some more details on the hierarchical approach. Even with the SM, I could not understand it well.

### Questions
- How do overall training times compare to the non-matrix free variants and to SGD-based approaches such as ADAM?
- From the figures alone, it seems that these methods do no outperform ADAM in terms of convergence to a certain test-loss. What would be the advantage of using this method over ADAM?
- how exactly does the hierarchical approach work?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors aim to address the memory inefficiency and the numerical instability issue of KFAC. For the theory part, they close the gap between INGD and KFAC. For the experiment part, they show that the inverse-free methods have better numerical stability than KFAC. Furthermore, they show that by imposing structures on the Kronecker factors, they can achieve competitive performance while being more memory efficient.

### Strengths
1. The authors give a theoretical connection between an existing inverse-free method (INGD) and KFAC.

2. The authors provide a plausible reason for the better empirical performance of INGD compared to KFAC and IKFAC.

### Weaknesses
1. It feels like the contribution is mostly theoretical. The novelty of the inverse-free part is undermined by INGD. The discussion and analysis on the structured part also seems not to be very in-depth.
2. The empirical evaluation is a bit weak. The visualization makes it hard to see how the proposed methods compared to Adam near the end. Also, I think the evaluation will be more reasonable under settings where KFAC outperforms Adam. Such examples can be found in some previous work like [1].
3. The application of the block diagonal structure seems to be straightforward and existing. So it feels important that the proposed structure should be shown to solidly outperform block diagonal or some other simpler structure to have contribution on this part, but the discussion and the evaluation does not seem to be in-depth. The hierarchical structure seems to be interesting and outperforms the block diagonal structure, but the exact setting for the experiment is a bit unclear. For clarity, it is better to show how model weights with more than two dimensions are merged into two dimensions and the resulting dimensionality. Also, papers like [1] seem to suggest that for CNN, it is plausible for one Kronecker factor to be small and dense, while the other to be large but diagonal. This kind of structure is interesting to be considered/compared with, and it also suggests that setting the sparsity parameter to be the same for both Kronecker factors might not be the best for comparison.

### Questions
The following is a list where a response from the authors could make my opinion of the paper more positive.

1. I feel like evaluations on settings where KFAC outperforms Adam can convince me more on the effectiveness of the proposed method.
2. More thorough discussion and comparison to show that the hierarchical structure performs better than the other simpler ones can also provide more contribution on the empirical part.
3. It is also possible for authors to justify if the theoretical contribution is enough to cover up the weakness on the empirical evaluation part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper combines the strengths of two algorithms and leverages the advantages of each to improve upon their respective limitations. Specifically, the following results and contributions are observed:

- The proposal of an inverse-free KFAC update scheme: 

 Inspired by the inverse-free natural gradient descent
(INGD) algorithm, the authors introduce an inverse-free approach to the KFAC algorithm. This modification allows the KFAC algorithm to be utilized in low-precision training scenarios, eliminating the need for computationally expensive matrix inverses.
The authors propose an inverse-free KFAC update scheme, inspired by the inverse-free Kronecker-factored natural gradient descent
(INGD) algorithm. This scheme enables the KFAC algorithm to be used without requiring matrix inverses, making it suitable for low-precision training. 

- Imposition of a Kronecker-factored structure on INGD: 
The authors impose a Kronecker-factored structure on the INGD algorithm and propose structured inverse-free natural gradient descent (SINGD). This structural modification allows for the utilization of sparse structures, effectively reducing memory costs. By leveraging the sparsity of specific components within the algorithm, the authors aim to optimize memory utilization while maintaining computational efficiency.

### Strengths
Overall, this paper is well-motivated and provides a clear and detailed description of the KFAC and INGD methods. It successfully bridges the gap between these two methods by addressing their respective limitations. Specifically, the paper achieves two key objectives:
1. Making KFAC inverse-free for low-precision training: The authors propose an inverse-free KFAC update scheme, which eliminates the need for computationally expensive matrix inverses. This modification enables the KFAC algorithm to be effectively used in low-precision training scenarios, where precision is reduced to reduce memory and computational requirements.

2. Reducing memory cost in INGD: By imposing a Kronecker-factored structure on the INGD algorithm, the authors achieve a lower memory cost. This structural modification leverages sparse structures, optimizing memory utilization while maintaining computational efficiency.

### Weaknesses
This paper presents an incremental improvement by combining the strengths of existing algorithms and addressing their limitations. However, it fails to demonstrate completely new elements that offer significant advantages over previous approaches. Furthermore, upon reviewing the original INGD algorithm, it appears that the authors of the original work already discussed the sparse structures by considering sparse group structures in K and C. Consequently, the imposition of a Kronecker-factored structure on the INGD algorithm may be considered trivial, and not a substantial contribution compared to the original INGD algorithm. As a result, the overall strength of this work may not be sufficient for it to be accepted as a significant advancement in the field.

### Questions
See the weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
