# Test-time Adaptation for Image Compression with Distribution Regularization

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Current test- or compression-time adaptation image compression (TTA-IC) approaches, which leverage both latent and decoder refinements as a two-step adaptation scheme, have potentially enhanced the rate-distortion (R-D) performance of learned image compression models on cross-domain compression tasks, \textit{e.g.,} from natural to screen content images.  However, compared with the emergence of various decoder refinement variants, the latent refinement, as an inseparable ingredient, is barely
 tailored to cross-domain scenarios. To this end, we aim to develop an advanced latent refinement method by extending the effective hybrid latent refinement (HLR) method, which is designed for \textit{in-domain} inference improvement but shows noticeable degradation of the rate cost in \textit{cross-domain} tasks. Specifically, we first provide theoretical analyses, in a cue of marginalization approximation from in- to cross-domain scenarios,  to uncover that the vanilla HLR suffers from an underlying mismatch between refined Gaussian conditional and hyperprior distributions, leading to deteriorated joint probability approximation of marginal distribution with increased rate consumption. To remedy this issue, we introduce a simple Bayesian approximation-endowed \textit{distribution regularization} to encourage learning a better joint probability approximation in a plug-and-play manner. Extensive experiments on six in- and cross-domain datasets demonstrate that our proposed method not only improves the R-D performance compared with other latent refinement counterparts, but also can be flexibly integrated into existing TTA-IC methods with incremental benefits.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a latent refinement techqniue in test-time adaptation methods for image compression.
Especially, the paper focuses on methods that use a hyper-prior model, where the image is encoded into a latent variable $y$ and a hyper-latent variable $z$ in a hierarchical way.
The paper analyzes the issue of recent latent refinement methods not generalizing well in cross-domain settings, arguing the cause to a mismatch between the hyper-prior $p(z)$ and the gaussian conditional $p(y|z)$ used in refinement methods.
Based on this conjecture, the paper proposes a distribution regularization term that uses dropout variational inference, claiming it can improve probability approximation. 
Experimental results show that the proposed method continuously improves latent refinement and demonstrates effectiveness even when integrated into state-of-the-art methods that jointly utilize latent and decoder refinement.

### Strengths
1. The proposed method can be applied without altering any model parameters, making optimization easy and immune to catastrophic forgetting.
2. The paper tries providing detailed discussions on the proposed method, both in a principled and empirical way.
3. The experimental results consistently demonstrate the effectiveness of the proposed method in cross-domain image compression across different settings: (1) with only latent refinement, (2) integrated with state-of-the-art TTA-IC methods, which further include decoder adaptation, and (3) on medical images.

### Weaknesses
Most importantly, as i understand, the theoretical analysis and subsequent derivation of the proposed method, which are claimed as major contribution in this paper, contain many unclear and misleading aspects. 
1. (L173, 193) The definition of "optimal probability representation" is not clearly defined, throughout the paper. It's unclear what specific properties this representation should possess, and how it relates to the practical implementation of the method. This lack of clarity makes it difficult to assess the validity of the theoretical claims.
2. The entropy function, i.e., $H(X)=-\mathbb{E}_{x\sim p(x)}[\log p(x)]$, is interpreted in the form of log probability, and it seems that the expectation term is not considered in the analysis and derivation. This omission raises concerns about the rigor of the mathematical arguments, as the expectation is a crucial part of the entropy definition, and its absence could lead to incorrect conclusions.
3. In the Proposition 1, assuming an optimal joint probability approximation of the true marginal distribution $p(y^*)=\int p(y,z)dz$, the proposition simply interprets $H(Y,Z) - H(Y^*) = H(Z|Y) + H(Y) - H(Y^*) = H(Z|Y)$ when $H(Y) = H(Y^*)$. However, the assumption $p(y^*)=\int p(y,z)dz$ may not induce equations (7,8), which can be misleading. The jump from the marginalization assumption to the specific decomposition of the joint entropy is not well-justified, and the conditions under which equations (7) and (8) hold are not sufficiently clear.
4. In the proof of Proposition 2, the authors argue that the entropy bottleneck $p(z_t)$ and the posterior $p(y_t|z_t)$ are learned from the source dataset (L212, source image correlated) and may not work effectively. While this makes sense, it is not a theoretical analysis, in my point of view. This argument is more of an empirical observation than a rigorous theoretical derivation. It lacks a formal connection to the mathematical framework established earlier in the paper.
5. For Corollary 1, it is unclear whether $z^*$ and $y^*$ in equation 13 correspond to in-domain or cross-domain cases. In the cross-domain case with $y^*_t$ and $z_t^*$ as in Proposition 2, equation 13 is as follows: $\triangle H = H(Y, Z) - H(Y^*_t) > H(Z^*|Y^*)$, which holds according to equations (11, 12) only if $H(Y^*_t)=H(Y^*)$ and $H(Z^*_t|Y^*_t)=H(Z^*|Y^*)$. However, there is no guarantee for the condition. The application of equations (11) and (12) to the cross-domain case is not clearly explained, and the conditions under which the inequality in equation (13) holds are not rigorously established.
6. Importantly, in Section 3.3, the paper proposes distribution regularization using equation 13, interpreting the first three terms in equation 17 as corresponding to $H(Y|Z), H(Z), H(Z^*|Y^*)$ (the three terms at the front) in equation 13. However, it is unclear how $H(Z^*|Y^*)=\mathbb{E}_{y^*,z^*\sim p(y^*,z^*)}[p(z^*|y^*)]$ leads to $-\log p(z^m_t|y^m_t)$ in the optimization objective. Note that $H(Z^*|Y^*)$ includes expectation from $p(y^*,z^*)$. The connection between the theoretical term $H(Z^*|Y^*)$ and its practical approximation in the optimization objective is not well-justified. The expectation over $p(y^*, z^*)$ is not directly addressed in the optimization objective, raising concerns about the validity of this approximation.

### Questions
* Please address the weakness above.
* The writing is a bit difficult to understand, especially in the discussion parts of both the methodology and experiment sections

### Soundness
2

### Presentation
2

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
The authors propose a new latent refinement method to enhance the rate-distortion (R-D) performance for test-time adaptation image compression. They theoretically analyze that existing methods require higher rate consumption to estimate the marginal probability of the latent variables in cross-domain scenarios. To address this, the authors incorporate a new distribution regularization term into the R-D objective, promoting a better approximation of the latent representation. Experimental results across six cross-domain datasets demonstrate the effectiveness of the proposed approach, showing its superiority over existing methods. Please see my detailed comments below.

### Strengths
1. The authors offer a theoretical analysis highlighting limitations of existing methods, which informs their introduction of a distribution regularization technique. This technique effectively adapts the compression model to test data with domain shifts.
2. They provide detailed analysis results on the entropy curves of different probabilities about different methods. The results in Figure 4 demonstrate that the proposed method can lead to a good convergence of rate consumption and better R-D performance.
3. Experimental results demonstrate that the proposed method can be easily integrated with existing methods to enhance R-D performance across cross-domain image datasets.

### Weaknesses
1. The test datasets used in the experiments contain a limited number of images, which may affect the robustness of the results. To strengthen the findings, please consider providing additional results on larger-scale datasets. Specifically, the current datasets do not sufficiently represent the diversity of real-world image content, making it difficult to assess the generalization capability of the proposed method across different image characteristics, such as varying levels of detail, texture, and lighting conditions.
2. It would be helpful to include a preliminary section explaining the image compression process before the theoretical analysis of existing methods. This section could clarify the steps involved in obtaining the latent variable y and hyper-latent variable z (side information), enhancing readers' understanding of the compression model and the subsequent theoretical analysis. A detailed explanation of the encoding and decoding processes, including the role of the entropy model, would be beneficial for readers unfamiliar with learned image compression techniques.
3. In addition to the adaptation cost of different methods, it is better to provide the compression cost of the proposed methods, which would offer a more comprehensive view of its performance. This should include the computational overhead of both encoding and decoding, as well as the memory footprint of the model, to provide a complete picture of the practical implications of the proposed approach.
4. The authors do not provide a limitation analysis of the proposed methods. For instance, the long adaptation time may limit the proposed methods to be used in real-time applications. Furthermore, a discussion on the sensitivity of the method to different hyperparameter settings and the potential for performance degradation in certain scenarios would be valuable.
5. More discussion on recent test-time adaptation works would be beneficial to place this study in context. Relevant works to consider include, but are not limited to, [A-E].
6. In Table 3, the results indicate that increasing the number of dropout layers can negatively impact image compression performance. Please add further discussion on how to effectively approximate the distribution regularization to avoid such performance degradation. It is important to understand the trade-offs between the number of dropout layers and the accuracy of the approximated distribution, and how this affects the overall compression performance. A more detailed analysis of the impact of different dropout configurations is needed.

### Questions
1. In Table 3, the results indicate that increasing the number of dropout layers can negatively impact image compression performance. Please add further discussion on how to effectively approximate the distribution regularization to avoid such performance degradation.

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
5

### Summary
Current Test-Time Adaptation Image Compression (TTA-IC) methods improve rate-distortion (R-D) performance on cross-domain tasks by refining both latent variables and decoders in a two-step process. However, latent refinement has not been specifically optimized for cross-domain scenarios. The authors conduct theoretical analyses to identify a mismatch between refined Gaussian conditionals and hyperprior distributions in the vanilla Hybrid Latent Refinement (HLR), leading to poorer joint probability approximations and higher rate consumption. To address this issue, they introduce a Bayesian approximation-based distribution regularization technique that enhances joint probability modeling in a plug-and-play manner. Extensive experiments across six in-domain and cross-domain datasets demonstrate that the proposed method outperforms existing latent refinement approaches in R-D performance.

### Strengths
1. The paper effectively identifies the limitations of existing Hybrid Latent Refinement (HLR) methods in cross-domain image compression, particularly highlighting the mismatch between refined Gaussian conditionals and hyperprior distributions.

2. It provides a thorough theoretical analysis using marginalization approximation, establishing a solid foundation for the proposed improvements.

3. The introduction of a Bayesian approximation-based distribution regularization technique successfully addresses the identified mismatch, enhancing joint probability approximation. 

4. The method shows improvements in rate-distortion (R-D) performance compared to other latent refinement approaches, validating its effectiveness.

### Weaknesses
1. The paper does not include a comparison of GPU memory usage and GFLOPs, which are crucial metrics for evaluating the complexity of various methods. Including these metrics would illustrate the trade-off between performance gains and computational complexity more clearly. It would be beneficial to present memory usage across different datasets, especially since DVI is introduced during optimization, making it reasonable to assess the additional complexity incurred.

2. In [1], the posterior distribution of $\hat{z}$ is assumed to be a uniform distribution. It is unclear whether directly inferring $\hat{z}$ through a hyper analysis transform in out-of-distribution (OOD) scenarios is the better choice? Because this approach not only avoids incurring a larger $\Delta H$ but also naturally matches its posterior distribution during pre-training. 

3. The paper introduces a regularization term based on HLR in TTA-IC. While this contribution is valuable, its impact on the community appears moderate.

### Questions
Will the authors make their code public to assist the community upon acceptance?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article investigates test-time adaption image compression method on cross-domain compression tasks from the perspective of latent refinement, by extending hybrid latent refinement and introducing a simple Bayesian approximation-endowed distribution regularization. The authors provide theoretical analysis and experimental results to demonstrate the performance of this method. My detailed comments are as follows.

### Strengths
1.	The authors propose their method from the perspective of latent refinement, which hasn’t been fully investigated. Compared with HLR, the method proposed by the author greatly improves the performance cross-domain compression tasks.
2.	The authors provide sufficient theoretical analysis on the method proposed in the article.

### Weaknesses
1. The experimental results of this plug-and-play method are relatively weak, which cannot illustrate the generalization ability of this method on other TTA-IC approaches. It would be better to apply this method to more baseline approaches.
2. It would be better to report the image compression results on top of popular image reconstruction benchmarks, such as Set5, Set14, BSD100, Urban100, etc.
3. This paper is hard to follow and the writing could be further improved. It would be better to explicitly highlight the key contributions of this paper.
4. The compared methods BLR and HLR are too old since both are published before 2021. It would be better to compare with more recent work, such as [A].

### Questions
The compared methods are too old. More popular image reconstruction/compression datasets should be considered for comparisons.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The author propose a novel test-time adaptation framework for image compression through directly refine the latent variables without altering any model parameters.

### Strengths
This research topic of this work seems a bit a minority (image compression + test-time adaptation) and contains a lot of background knowledge. After hard attempts, I think I still can't give an accurate evaluation. It is recommended that AC find another highly relevant reviewer in order to make a more comprehensive judgment.

### Weaknesses
This research topic of this work seems a bit a minority (image compression + test-time adaptation) and contains a lot of background knowledge. After hard attempts, I think I still can't give an accurate evaluation. It is recommended that AC find another highly relevant reviewer in order to make a more comprehensive judgment.

None

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2
