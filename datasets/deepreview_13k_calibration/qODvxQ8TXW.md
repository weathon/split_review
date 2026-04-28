# Masks, Signs, And Learning Rate Rewinding

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Learning Rate Rewinding (LRR) has been established as a strong variant of Iterative Magnitude Pruning (IMP) to find lottery tickets in deep overparameterized neural networks. While both iterative pruning schemes couple structure and parameter learning, understanding how LRR excels in both aspects can bring us closer to the design of more flexible deep learning algorithms that can optimize diverse sets of sparse architectures. To this end, we conduct experiments that disentangle the effect of mask learning and parameter optimization and how both benefit from overparameterization. The ability of LRR to flip parameter signs early and stay robust to sign perturbations seems to make it not only more effective in mask identification but also in optimizing  diverse sets of masks, including random ones. In support of this hypothesis, we prove in a simplified single hidden neuron setting that LRR succeeds in more cases than IMP, as it can escape initially problematic sign configurations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study compares two key techniques in deep neural networks: Learning Rate Rewinding (LRR) and Iterative Magnitude Pruning (IMP). A clear and detailed analysis of both methods highlights the benefits of LRR, particularly its early parameter sign switching and better optimization of various network structures.
Through practical testing on different models and datasets, the authors present LRR's advantages, emphasizing it as a more versatile method for neural network optimization. This research serves as practical groundwork for further exploration of improvements to sparse training algorithms.
Interestingly, the authors examine the impact of sign perturbations. The experimental evidence in the paper shows that at lower sparsity levels, the impact of sign perturbations is small, but it has a significant effect on performance in the complex CIFAR100 dataset. This evidence further aligns with the authors' point - LRR is not only better at identifying masks but also optimizes various mask scenarios.

### Strengths
This paper presents two new advantages of Learning Rate Rewinding (LRR) and validates their existence, offering fresh insights not covered in previous LRR research. This work is an essential foundation for understanding and improving network pruning algorithms, particularly the LRR method. One notable contribution is the discovery of parameter sign switching, a key characteristic of LRR. This not only reveals a unique facet of LRR but also offers new perspectives for understanding and designing more effective algorithms.
The article presents enough experiments as evidence. Firstly, it uses a single hidden neuron model for learning tasks, showing that LRR has more success cases than IMP because LRR can avoid problematic initial sign configurations.
The paper further validates LRR's advantage over IMP through a series of representative tasks and networks. Experimental results show that LRR performs well in standard benchmark tests such as CIFAR10, CIFAR100, and Tiny ImageNet, regardless of its combination with ResNet18 or ResNet50. These results strongly support the superiority of LRR over IMP in deep neural network training.

### Weaknesses
This paper impressively combines clear presentation with strong experimental results, and I have yet to identify any significant shortcomings. But I have some questions about hyperparameters :
1. Considering that hyperparameter tuning is generally a problem-specific task, do you believe this sensitivity might hinder the practical application of LRR? Could you provide some advice or guidelines for hyperparameter selection or tuning when using LRR and discuss how the learning rate schedule influences the performance of this algorithm?
2. Your paper also indicates that LRR can benefit from the overparametrization of neural networks. Can you elaborate on how this overparametrization impacts the functionality of LRR? Is it possible to have too much overparametrization, which could negatively impact the performance of LRR?

### Questions
See above weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the effectiveness of learning rate rewinding (LRR) both from a theoretical and practical perspective, with a specific focus on the concept of weight sign flipping. In the context of a single-layer neural network, the authors offer theoretical evidence that LRR can reliably rectify initially problematic weight sign patterns by inheriting the sign information from a well-trained overparameterized model. When applied to more complex neural networks, empirical findings validate that the observed changes in weight sign configurations align with the theoretical insights. Furthermore, the authors dissect the impact of LRR into two distinct components: sparse network optimization and the performance of the generated mask. Through rigorous experiments, they provide empirical support for LRR's exceptional performance in both of these aspects.

### Strengths
- This paper offers a clear rationale for the effectiveness of LRR by examining it through the perspective of weight sign flipping, which is a pioneering work in exploring sign flipping within the context of sparse neural networks. The authors provide theoretical evidence demonstrating that LRR gains an advantage from flexible mask sign configurations, in contrast to IMP, a finding substantiated by empirical experiments at a toy-level. This research has the potential to serve as a source of inspiration for the advancement of more efficient sparse training algorithms that can leverage the power of mask sign configurations.
- The paper presents carefully designed ablation studies investigating two distinctive roles of LRR in (i) sparse neural network optimization and (ii) discovering a good sparse mask.  
- The paper is effectively structured and exhibits clear and concise writing
- The paper covers a fair amount of relevant previous studies.

### Weaknesses
 - While the authors argue LRR finds a better mask than WR in Figure 3, I wonder if a longer training epochs within each IMP cycle would help WR to find a superior mask. In other words, are both WR and LRR fully converged? If that’s the case, does the mask configuration stay constant after convergence? Further, if the optimal mask can be attained only at the end of the training epochs, it could pose challenges in efforts to reduce the computational cost associated with IMP (both WR & LRR).
- Concerning the flexible LRR mask analysis (see Figure 4), there appear to be some questionable findings. For instance, the "LRR with IMP mask (blue)" does not appear to show significant improvement over WR (orange) except for the case of Cifar-10 with a moderate level of sparsity. Moreover, it is unclear regarding the implication of "LRR w/ BN rewind (yellow)" in Figure 4 in the context of "flexible LRR training."
- In Figures 3 and 6, there are only two sets of experimental results available for analysis, Cifar-10 and Cifar-100. The authors argue that Cifar-100 results may not fully meet expectations due to its higher complexity. However, it remains an open question whether the same trend would hold for different network architectures, such as VGG networks.

### Questions
- Is there any further results on ImageNet or any large-scale datasets?
- In Figure 3, is the presented LRR results with or without BN rewinding?

### Soundness
3 good

### Presentation
4 excellent

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
The paper explores LRR and IMP, the key methods for identifying lottery tickets in large neural networks, with the goal to understand the differences between mask learning and parameter optimization. The paper provides valuable theoretical results for one hidden neuron networks predicting the LRR's superior performance due to its ability to overcome initial parameter sign challenges. Experiments with ResNets on CIFAR10, CIFAR100 and Tiny ImageNet demonstrate LRR's superior performance due to its ability to adjust the parameter signs early in training.

### Strengths
* The paper addresses and important, timely and high-impact problem, which could help to drastically improve the efficiency and decrease the cost of sparse training. 
* Decoupling structure learning and parameter learning is interesting and the steps taken in the paper are meaningful.
* The theoretical results on one hidden neuron networks are interesting, strong, and well described. 
* The experimental results support the claims of the paper, although the performance differences between LRR and IMP are small.

### Weaknesses
 * Although the main ideas explored in the paper and the theoretical insights are strong, the empirical evaluation is limited to ResNet architectures. The empirical results are mainly reported for CIFAR10 and CIFAR100. Extending the findings to more architectures, such as Transformers or other CNN architectures, and other domains like natural language processing or object detection, would be helpful to understand the significance of the findings. Additionally, to reviewer's understanding, several figures do not fully support the claims made in the text (see questions below).
* Magnitude pruning is explored as the only strategy to train sparse networks. Can the findings regarding the superiority of LRR be generalized and extended to other pruning strategies, such as those based on gradient information or activation patterns? The paper should also explore the sensitivity of LRR to the specific pruning ratio used, as this could impact the observed performance gains.
* An exploration of the impact of the learning rate, and specifically different learning rate schedules, would also help to better understand the practical value of the proposed analysis. The paper should investigate whether the observed benefits of LRR are consistent across different learning rate regimes, or if specific learning rate schedules are required to realize these gains.

Minor: A missing reference [?] on p.3. "LRR is improves parameter optimization" on p.7.

### Questions
* The conclusions for CIFAR10 and CIFAR100 often diverge (Fig. 4: LRR with IMP mask vs IMP, Fig. 7), however the explanation for this divergence is not well understood. Although the authors list potential reasons, there is no experiment to support or reject the hypothesis. Evaluation on more datasets and more architectures should help to provide a stronger evidence for the claims and the relevance of the obtained theoretical findings.
* What is the meaning of the light blue line in Fig. 11?
* How does Fig. 12 support the claim made in the figure caption "LRR enables considerably more sign flips than IMP and thus improving mask identifcation and parameter optimization"?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
