# Mean Field Theory in Deep Metric Learning

- Decision: Accept
- Avg Score: 5.40
- Scores: 5, 3, 8, 6, 5

## Abstract
In this paper, we explore the application of mean field theory,
  a technique from statistical physics, to deep metric learning
  and address the high training complexity
  commonly associated with conventional metric learning loss functions.
  By adapting mean field theory for deep metric learning,
  we develop an approach to design classification-based loss functions from pair-based ones,
  which can be considered complementary to the proxy-based approach.
  Applying the mean field theory to two pair-based loss functions,
  we derive two new loss functions,
  \mbox{MeanFieldContrastive} and \mbox{MeanFieldClassWiseMultiSimilarity} losses,
  with reduced training complexity.
  We extensively evaluate these derived loss functions on three image-retrieval datasets
  and demonstrate that our loss functions outperform baseline methods in two out of the three datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes new DML losses that are inspired from the Mean-Field Theory (MFT), which is a concept from statistical physics. Specifically, the authors follow the constructive loss and the multi-class loss to implement two MFT losses. Their extensive experiments demonstrate the efficiency of the new losses on popular DML benchmarks.

### Strengths
The idea of introducing unique losses based on the theory of statistical physics looks interesting and novel. No prior research has taken on this particular task.

The proposed method is evaluated on several popular DML benchmarks. The authors evaluate their method on advanced MLRC metrics, making their results convincible.

### Weaknesses
My major concern is that the proposed theory does not seems to be solid when it is applied on DML task. There is not enough theoretical clue that the mean-field theory (MFT) would directly benefit the DML task compared with the proxy-based losses. The authors should provide more analysis to explain the intrinsic connection between the interaction between the magnetic spin and the similarity (distance) between the data points in DML task.

The relation and comparison between the proposed loss and proxy-based loss is still not clear. The intuition behind the MFT looks similar to the proxy-based loss, where they both compare a sample with an anchor instead of all class members. Thus, a systematic compare between it and other close related losses should be provided.

It seems the computation complexity to get the mean field in Eq.5 is higher than compared with the proxies. Thus, a comparison of performance and running time may be essential to be discussed. To further clarify its arithmetic progress and complexity, it is also suggested to list the pseudo-code of the loss.

Experimental results show that the improvement in some datasets is not significant (as illustrated in table 2, figure 2). But this is not a big issue for me.

### Questions
Is there any assumption or internal connection between the point distances and the spin configuration?

Please respond to the above weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the mean field theory into metric learning  by designing two loss functions to train deep neural networks. The model's performance is evaluated on various benchmarks, including CUB, Cars, and SOP. While the paper is generally easy to follow, it lacks a sufficient level of novelty and performance improvement.

### Strengths
This paper explores the mean field theory into metric learning  by designing two loss functions to train deep neural networks. The model's performance is evaluated on various benchmarks, including CUB, Cars, and SOP, by comparing several other methods. The paper is generally easy to follow.

### Weaknesses
The major concern is that the paper lacks a sufficient level of novelty and performance improvement.

First, they mainly explore mean filed theory into metric learning. Such metric is close to central loss [R1].
[R1]. Wen, Yandong, et al. "A discriminative feature learning approach for deep face recognition." Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part VII 14. Springer International Publishing, 2016.

Second, the performance is not significant. In table I, compared with ArcFace and ProxyAnch, it is hard to justify the significant improvement. It is essential to do t-test.

### Questions
The clarification of model novelty.
The performance improvement.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript proposes two new metric learning algorithms inspired by mean-field analysis from physics. In pair-based algorithms, the loss function pushes pairs of the same class to be closer and pairs of different classes to be apart, and need to be calculated over many training pairs; in contrast, for the proposed mean-field approach, the loss pushes each sample to be close to the class mean and away from other classes' mean, and further pushing class means away from each other. The underlying technical derivation is quite general, through taking a derivating of an energy function. Thus, the same method can be applied to other cases, such as proposing a loss function using class means in a minibatch setting.

### Strengths
* Regardless of any inspiration taken from physics, replacing pair-based methods with mean-based methods seems a scalable approach, well grounded in statistics.
 * The proposed class of methods is possibly prudent in the sense that they can be used to derive loss functions, taking into account mean-class information for other problems.
 * The simulations performed seem great, and the authors explain the optimisation carried out on both their method and other methods used for comparison. The results suggest the proposed class of methods achieve very competitive results. 
 * The writing is clear, almost tutorial-like, and easy to follow.

### Weaknesses
 * The authors hide the actual derivation in the appendix, so they do not detail enough their technical approach. On the face of it, the modified loss function could have been suggested just through statistical intuition, not derived from an energy approximation (Hubbard-Stratonovich, saddle-point approx, etc.), so it is a pity the authors don't sketch their methodology in the main text.
 * It is hinted that the method can be more efficient (e.g. due to the lack of pair sampling or anchor points choice), but it is not reported if the training time is superior to the other methods or if the optimisation over `M`-s causes a substantial overhead (which may be justifiable with the improved results).

### Questions
* Is it always favourable to optimize the means `M` and the parameters `theta` together? Maybe alternating between optimisation steps would be superior in numerical terms.
 * The method seems similar to classic soft-clustering approaches, which were optimised by alternating between two optimisation steps, such as the EM algorithm. Can you make the connection more explicit?
 * Are the new methods faster or slower than other methods?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers mean field theory approximations of pair-based loss functions for metric learning. Inspired by techniques in statistical physics, pairwise calculations are approximated by comparing to a mean approximation, ie, turning a summation over $i$ and $j$ to only that of $i$. Using such an approach, two different mean field contrastive loss functions are proposed. Empirically, the proposed loss functions are evaluated and are shown to even out perform their non-mean field counterparts.

### Strengths
- The approximation technique for reducing pairwise summations to their mean field approximation intuitively makes sense. This concept is particularly well illustrated in Figure 1.
- The proposed approach seems promising. Surprisingly, the mean field approximations perform better than their non-mean field counterparts in many circumstances.

### Weaknesses
 - Part of the motivation for the approximation (not including its statistical physics analogy) was the reduction in runtime complexity pair-based loss function in metric learning. However, there is no runtime values reported in the paper.
- Some terms in the paper are not explained. (See questions below).

- The explanation for the performance increase due to the mean field approximation is not sufficiently detailed. While the authors suggest that the mean field approximation reduces noise, this explanation lacks depth. It is unclear how exactly the class means contribute to this noise reduction, and what specific properties of the mean field approximation lead to this effect. A more rigorous analysis of the loss landscape and how the mean field approximation alters it would be beneficial.

### Questions
- What are the runtimes of the mean field variants compared to their regular counterparts? Does the additional complexity of requiring optimization of mean fields $\mathbf{M}_c$ outweigh the reduction of computational complexity via the mean field approximation?
- One of the major interesting components of the paper is that mean field approximation performs better than its non-mean field counterparts. Is there a good hypothesis for why this may be the case? Have you found a good characterization of when one out performs the other? Additional insight here would be great since the paper claims in the empirical section that the mean field losses provide better "training complexity but also results in better embeddings".
- I am unsure exactly what the authors mean be "resummation" and "unstable terms". Clarification here would be great.
- Furthermore, what do that authors mean by "... the above discussion implies the mean field theory is independent of the concept of anchors ..."?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the mean field theory is introduced into the domain of deep metric learning. By incorporating foundational components such as the Contrastive loss and Class Wise Multi-Similarity loss, the authors construct the Mean Field Contrastive loss and Mean Field Class Wise Multi-Similarity loss. The proposed method is evaluated through extensive experiments on benchmark datasets, covering two benchmark protocols. The results demonstrate the effectiveness of the proposed approach.

### Strengths
1. The authors have integrated the mean field theory into the realm of deep metric learning. 

2. They have introduced two pair-based loss functions, namely the Mean Field Contrastive loss and the Mean Field Class Wise Multi-Similarity loss. 

3. The experiments and ablation studies conducted in the paper are comprehensive.

### Weaknesses
Deep metric learning involves a range of loss functions, and it is unclear whether the mean field theory can be applied to other loss functions commonly used in this context. It would be valuable for the authors to specify under what conditions and contexts the mean field theory is applicable and offer practical guidance for its implementation in other scenarios. Specifically, the paper lacks a discussion on the limitations of the mean field approximation itself. The mean field approximation often relies on assumptions of independence or weak correlations between data points, which may not hold true in complex, high-dimensional feature spaces typical of deep learning. The authors should address how these assumptions might affect the performance of their proposed method and provide insights into when the approximation is likely to be accurate or break down. Furthermore, the paper does not explore the computational cost associated with the mean field calculations, which could be a significant factor in practical applications, especially with large datasets.

### Questions
How can the mean field theory be extended to encompass other commonly used loss functions in deep metric learning?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
