# Awakening Collective Wisdom: Elevating Super-Resolution Network Generalization through Cooperative Game Theory

- Decision: Reject
- Scores: 6, 6, 6, 8

## Abstract
Improving the generalization capability of image super-resolution algorithms is a fundamental challenge when deploying them in real-world scenarios. Prior methods often relied on the assumption that training on diverse data can improve generalization capabilities, leading to the development of complex degradation models that simulate real-world degradation.Unlike previous works, we present a novel training strategy grounded in cooperative game theory to improve the generalization capacity of existing image super-resolution algorithms. Within this framework, we conceptualize all neurons in the network as participants engaged in a cooperative relationship, where their collective responses determine the final prediction. As a solution, we propose to awaken suppressed neurons that hinder the generalization capability through our Erase-and-Awaken Training Strategy (EATS), thus fostering equitable contributions among all neurons and effectively improving generalization performance. EATS offers several compelling benefits.1) Seamless integration with existing architecture: It integrates with existing networks to enhance their generalization capability for unseen scenarios. 2) Theoretically feasible strategy: We theoretically prove the effectiveness of our strategy in enhancing the Shapely value (reflecting each participant's contributions to prediction). 3) Consistent performance improvements: Comprehensive experiments on various challenging datasets consistently demonstrate performance improvements when employing our strategy. The code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The following paper proposes Erase-and-Awaken Training Strategy (EATS), a cooperative game theory-inspired novel training strategy that improves the generalization capability for Single Image Super-Resolution (SISR) algorithms in dealing with real-world scenarios. Unlike previous data-driven methods, EATS presents itself as an optimization-based method, where it encourage all neurons within an existing SISR framework to actively collaborate in solving the generalization problem by randomly perturbing response of inhibited neurons and maximize their contributions to prediction. EATS consists of two steps: (1) **Erasing step**, where it randomly samples a disruptor filter $n_l^{dis}$ and applies it towards a randomly selected erased filter $n_l^{ear}$ in the network's $l^{th}$ layer and assess performance before-and-after the erasure ($f_{\theta}$ and $f_{\theta'}$), and (2) **Awakening step**, where an awakening regularization term $\mathcal{L}\_{awa}$ is employed to close the gap between predicted high-resolution image and the low-resolution image from the disrupted network $f_{\theta'}$. Besides providing theoretical proof to show the effectiveness of EATS in improving the Shapley value of the network, experiments on multi-degradation settings within various unseen datasets have demonstrated that plugging EATS into SISR algorithms such as SRResNet and RRDBNet results in quantitatively and qualitatively better images than baselines.

### Strengths
- The proposed method is original, simple, and applicable to existing methods.
- The paper is well-written for the most part.
- Incorporating EATS with existing baseline methods SRResNet [1] and RRDBNet [2] outperforms the baselines on various tasks and baseline + Dropout for the most part.

### Weaknesses
Aside from the limitations pointed out in Section 5 of the paper, I have several concerns regarding the paper:

- The experiments could have used more recent SISR models instead of SRResNet and RRDBNet, which have been more than 5 years old. One possible way to alleviate this issue is to replicate Table 1 and Table 2 results in the paper using more recent attention-based architectures like HAN [3], SAN [4], or SwinIR [5] to demonstrate the effectiveness of EATS, if possible. Specifically, the current experiments do not sufficiently demonstrate the generalizability of EATS across diverse architectures, particularly those employing attention mechanisms, which have become prevalent in recent SISR research. The absence of results on these models leaves a gap in understanding the true scope of EATS's applicability.
- Minor typos exist in the text. For instance, 'Shapely' should be 'Shapley' in the abstract and the Solution subpoint on the 2nd page. In addition to that, 'Managa109' should be 'Manga109' [6] on Table 2 on the 9th page.

### Questions
To my understanding, since the model uses two networks: original network $f_{\theta}$ and disrupted network $f_{\theta'}$, does that mean that the whole framework involves more parameters (approximately doubles) to that of the baselines? If yes, can authors address the # of parameters involved in employing said method with EATS?

[1] Ledig, Christian, et al. "Photo-realistic single image super-resolution using a generative adversarial network." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017. https://arxiv.org/abs/1609.04802

[2] Wang, Xintao, et al. "ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks." Proceedings of the European conference on computer vision (ECCV) workshops. 2018. https://arxiv.org/abs/1809.00219

[3] Niu, Ben, et al. "Single image super-resolution via a holistic attention network." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XII 16. Springer International Publishing, 2020. https://arxiv.org/abs/2008.08767

[4] Dai, Tao, et al. "Second-order attention network for single image super-resolution." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019. https://ieeexplore.ieee.org/document/8954252

[5] Liang, Jingyun, et al. "SwinIR: Image Restoration Using Swin Transformer." Proceedings of the IEEE/CVF international conference on computer vision. 2021. https://arxiv.org/abs/2108.10257

[6] Matsui, Yusuke, et al. "Sketch-based manga retrieval using manga109 dataset." Multimedia Tools and Applications 76 (2017): 21811-21838. https://arxiv.org/abs/1510.04389

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces the cooperative game theory improve the generalization of super-resolution algorithms. It proposes an erase-and-awaken training strategy, which prompts all neurons in networks to achieve equitable contributions to predictions by an awakening regularization term. This paper conducts efficient analyses of feature responses to demonstrate the effectiveness of the proposed EATS.

### Strengths
1. This paper improve the generalization capability of image super-resolution algorithms from a novel perspective of the cooperative game theory. It views all neurons within the network as the active participants in a cooperative game. 

2. The authors propose an Erase-and-Awaken Training Strategy (EATS) to awaken the inhibited neurons that hinder the generalization performance. EATS promotes equitable contributions from all neurons to the predictions, thus improving the generalization capability of networks on the unseen scenarios. 

3. The authors provide the theoretical proof to validate the effectiveness of EATS in improving the Shapely value, which signifies the contribution of each participant to predictions. In addition, authors present efficient analyses about feature responses, providing substantial evidence to support the claims made in this paper.


=========================== Update

I have read the author feedback and the reviews from other reviewers. I keep my rating as 6--accept

### Weaknesses
1. The implementation of EATS involves an awakening regularization term, which emphasizes the contribution of the erased filter by constraining predictions of the disrupted network approximates the baseline image. However, the random sampling of layers and filters in each training iteration has raised concerns about the convergence of the awakening regularization term. Specifically, the paper does not detail how the magnitude of the regularization loss is balanced with the primary super-resolution loss. Without a clear explanation of how these two losses are dynamically balanced, it is difficult to assess the stability and effectiveness of the training process. The authors should provide more details on the loss balancing strategy and its impact on overall convergence.

2. The proposed EATS requires an additional forward propagation step during each training iteration. While the paper acknowledges this, it lacks a detailed analysis of the computational overhead. The increased training time should be quantified not only in terms of total time but also in terms of the additional FLOPs (floating-point operations) incurred. Furthermore, the paper should discuss the scalability of EATS with respect to larger network architectures and datasets. It is crucial to understand how the extra computation scales and whether it introduces bottlenecks in the training process.

### Questions
Figure 1 in the manuscript presents the channel responses of the shallow layer, 2nd block, in SRResNet and SRResNet-EATS. However, it would be valuable for reviewers to also observe if similar phenomena occur in deep layers, where channel responses are awakened and equitable. Visualizations of channel responses from shallow to deep layers would provide a more comprehensive understanding of the awakening effect across various network depths.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an erase-and-awaken training strategy to improve the generalization capacity of existing super-resolution algorithms. The strategy treats the neurons within networks as cooperative players and awakens the inhibited filters that hamper the generalization performance via an awakening regularization term. The quantitative and qualitative results show the effectiveness of the proposed strategy.

### Strengths
1. This paper introduces a novel perspective by conceptualizing the neurons in the network as players within a cooperative game. The authors propose an Erase-and-Awaken Training Strategy (EATS), which fosters equitable contributions from all neurons to predictions for improving model’s generalization capacity. 

2. The authors establish a theoretical connection between the proposed strategy and the Shapely value in cooperative game theory. This theoretical foundation highlights the efficacy of EATS in promoting equitable contributions from all neurons. 

3. The paper conducts extensive experiments and analyses, demonstrating the effectiveness of EATS. These experiments not only validate the theoretical claims but also show the practical effect of the proposed strategy.

### Weaknesses
 1. The authors are encouraged to provide the computational costs introduced by the proposed training strategy. This addition would help reviewers to assess the practical implications and feasibility of the proposed approach.

 2. The ablation studies about the impact of varying layer ratios involved in EATS make me confused. I'm uncertain about how the authors divided the involved layers. Was it through random sampling, division from shallow to deep layers, or perhaps another approach? If the division was from shallow to deep, please explain why more deep layers involved results in better performance.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to awaken the suppressed filters that hinder the generalization performance for improving the generalization ability of super-resolution algorithms. To this end, the authors propose an erase-and-awaken training strategy grounded on the cooperative game theory to equitable contributions among all neurons for predictions.

### Strengths
1. The authors propose a novel perspective of utilizing the cooperative game theory to improve the generalization of super-resolution algorithms.
2. The proposed erase-and-awaken training strategy is general and feasible to existing SR approaches due to its simple but effective implementation through a regularization term.
3. The authors present theoretical evidence for the effectiveness of EATS in prompting equitable contributions from all neurons.
4. Through diverse analyses, including feature visualization, channel salience maps, and channel correlations, this paper effectively demonstrates the effectiveness of the proposed strategy. The comprehensive experiments and analyses support the paper’s claims and facilitate understanding of the method.

### Weaknesses
 1. In Figure 1, the authors claim the proposed strategy alleviates the co-adaption phenomenon and achieve consistent channel response distribution. Can the dropout operation achieve the similar effect as the proposed strategy?
 2. The authors have performed the ablation studies about the ratio of layers involved in EATS, indicating that the increased involvement of layers leads to better generalization. How does the number of filters involved in each training iteration affect the generalization performance?

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
