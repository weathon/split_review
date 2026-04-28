# Cross-domain Recommendation from Implicit Feedback

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 1, 3, 5

## Abstract
Existing cross-domain recommendation (CDR) algorithms aim to leverage explicit feedback from richer source domains to enhance recommendations in a target domain with limited records. However, practical scenarios often involve easily obtainable implicit feedback, such as user clicks, and purchase history, instead of explicit feedback. Thus, in this paper, we consider a more practical problem setting, called cross-domain recommendation from implicit feedback (CDRIF), where both source and target domains are based on implicit feedback. We initially observe that current CDR algorithms struggle to make recommendations when implicit feedback exists in both source and target domains. The primary issue with current CDR algorithms mainly lies in that implicit feedback can only approximately express user preferences in the dataset, inevitably introducing noisy information during the training of recommender systems. 
To this end, we propose a noise-aware reweighting framework (NARF) for CDRIF, which effectively alleviates the negative effects brought by the implicit feedback and improves recommendation performance. Extensive experiments conducted on both synthetic and large real-world datasets demonstrate that NARF, implemented by two representative CDR algorithms, significantly outperforms the baseline methods, which further underscores the significance of handling implicit feedback in CDR. The code is available in an anonymous Github repository: https://anonymous.4open.science/r/CDR-3E2A/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on tackling cross-domain recommendation problem under implicit feedback setup. To reduce the noisy signals from implicit feedback, the authors proposed a noise-aware re-weighting framework by leveraging dynamic sampling methods to optimize the embedding learning. Experimental results demonstrate the effectiveness.

### Strengths
1. The problem is well described and motivated.
2. The proposed solution is technically sound.
3. Experiments are well designed and the presented results demonstrate the improvement.

### Weaknesses
1. Technical contribution is limited. Both implicit feedback recommendation and cross-domain recommendation are well studied topics, and the proposed denoising framework is also stacked by well studied methods, e.g., negative sampling from learning to rank, AD/CTD. Moreover, the authors claim this is the first work on cross-domain recommendation with implicit feedback, however, it's not convincing. For example, "Cross-domain Recommendation Without Sharing User Relevant Data" and "User-specific Adaptive Fine-tuning for Cross-domain Recommendations" are both proposed to work on the implicit feedback data.
2. Baseline methods are not well selected. There are numbers of sampling related research in learning to rank and applied to implicit feedback recommendation methods, however, few are included in comparison or discussions, e.g., Learning Recommenders for Implicit Feedback with Importance Resampling, etc.
3. The presentation of this work needs improvement. In particular, the notations used in this paper are hard to follow and can be simplified. Moreover, the framework section is hard to follow. It's unclear why the calibration factor can act as a denoising factor. What's the difference between this proposed idea and other active learning ideas?

### Questions
1. What's the main technical contribution for this work if this is not the first one tackling cross-domain recommendation with implicit feedback?
2. Why the learnable calibration parameter can help denoising? What's the difference between this idea and the active learning idea?
3. What's the performance comparison with state-of-the-art negative sampling method in learning to rank?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the implicit feedback-based (e.g., click, purchase, count of behaviors, in contrast to the explicit feedback e.g., ratings with positive and negative preferences) recommendation problem in the cross-domain setting. The two challenges in this setting are the absence of negative signals and the noise of user-item interactions. The proposed framework (CDRIF) addresses the first issue by existing sampling strategies, i.e., uniform sampling (Rendle et al., 2012; Ding et al., 2020). And CDRIF addresses the second issue by existing denoising algorithms, i.e., adaptive denoising and co-teaching denoising (Wang et al., 2021b; Han et al., 2018). CDRIF introduces an item popularity-based calibration factor as the weight of loss function. CDRIF shows improvement over two baselines (EMCDR and PTUPCDR) on two datasets.

### Strengths
S1: Using a popularity-based calibration factor to weigh the loss function seems promising as an alternative to attention-based methods.

S2: The writing is easy to follow.

### Weaknesses
W1: The technical contributions are very limited. The proposed framework (CDRIF) consists of three core components, i) generating negative samples, ii) reducing noise, iii) reweighting by calibration factors. However, the first component directly uses the existing uniform sampling (Rendle et al., 2012; Ding et al., 2020). The second component directly uses existing denoising algorithms, i.e., adaptive denoising and co-teaching denoising (Wang et al., 2021b; Han et al., 2018). The third component is a very simple item popularity-based calibration. The novelty of combining these existing techniques is not sufficiently justified, and the paper lacks a deep exploration of why this specific combination is superior to other possible combinations or modifications of these existing methods. The item popularity-based calibration factor, while potentially useful, is presented as a simple weighting scheme without a clear theoretical or empirical justification for its specific form or parameters. 

W2: The evaluation is very weak. There are only two baselines, EMCDR (Man et al., 2017) and PTUPCDR (Zhu et al., 2022). For cross-domain recommendation (CDR) methods (applicable for both explicit and implicit feedback), there are so many advanced learning techniques, just name a few bellows: graph neural networks based CDR, transfer learning based CDR, attention mechanism based CDR, adversarial learning based CDR. The paper fails to compare against a wider range of state-of-the-art methods, particularly those that are specifically designed for implicit feedback and cross-domain scenarios. The absence of comparisons with methods that utilize more sophisticated techniques, such as graph-based or attention-based models, makes it difficult to assess the true performance and contribution of the proposed method. The choice of baselines seems arbitrary and does not represent the current landscape of CDR research.

W3: Many related works are ignored. Also, see the above weak W2. In detail, transfer learning is a main research thread to address the cross-domain recommendation (for both explicit and implicit feedback). For example, the CoNet method (Collaborative Cross Networks for Cross-Domain Recommendation) can address the cross-domain recommendation from implicit feedback as investigated in this ICLR submission. In its task setting on the Cheetah Mobile dataset, it recommends apps (the target domain) by exploiting knowledge from news reading history (the source domain). Obviously, the reading logs are implicit feedback and the installations of apps are also implicit feedback. As a result, the claim in the introduction “to the best of our knowledge, prior to our study, no existing CDR research has offered algorithms to handle implicit feedback scenarios” does not hold true. The paper's claim of novelty is undermined by the omission of relevant prior work, particularly in the area of transfer learning for implicit feedback CDR. This lack of awareness of the existing literature raises concerns about the thoroughness of the research.

W4: the newly introduced dataset is not detailed. I read the Appendix A.2 for the dataset description on PubMed and DBLP. I checked the web pages on PubMed and DBLP, but I still do not know: How to align the authors on these two domains (name disambiguation)? Where to get the topic identification of an author? Why use the topic as the items and what is the reason to recommend a topic to an author? Why not use the {venue, paper/references, potential co-author et al} as the items instead? Is any data sample to be shown? By the way, will this dataset be released to use for research purposes? What is the cleaning, filtering, and preprocessing detail for this newly introduced dataset?

### Questions
Q1: The PTUPCDR refers to (Zhu et al., 2020) (A deep framework for cross-domain and cross-system recommendations) in the Section "Realization of NARF: DNR", while PTUPCDR refers to (Zhu et al., 2022) (Personalized transfer of user preferences for cross-domain recommendation) in Table 1.  

Q2: how to determine the two hyperparameters alpha and beta in Eq. (14)?

Q3: In Eq. (14), for the sigma summation, $m$ should be $n$ which denotes the number of items instead of the number of users.

Q4: Below Eq. (14), what is $f_j$? And what is the relation between $f_j$ and $p_j$

Q5: In Eq. (14), for the positive pairs, the control hyperparameter alpha is the same for all user-item pairs. How about learning such control hyperparameter alpha_{i,j} according to individual user-item (u_i, v_j) pairs? This may be achieved by attention-based networks.

Q6: checking the syntax issue for this sentence, “the evaluation metrics
are recall@k and ndcg@k are computed following the all-ranking protocol”, which has two “are”s.

Q7: In Tables 2 and 6, how about the noise level equals zero?

Q8: there are so many implicit feedback benchmarks like Criteo (CTR clicks) and Microsoft MIND (news clicking). Why not ignore evaluations on such large, real-world datasets? By the way, the evaluated Amazon review dataset is NOT an implicit feedback dataset.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a cross domain recommendation methods based on denoising and calibrating the user preferences in the source and target domain. The experimental results seem promising but the paper is essentially unreadable with major issues in presentation. In particular the method is extremely difficult to understand, e.g. how are the calibration factors k_i computed from function 14 useful in determining the true preferences of the user, no intuition is provided. Moreover the paper mainly deals with matrix factorization type methods and there is not much discussion about more modern deep learning type methods and how it relates to those. Moreover the literature on cross-domain recommendation is quite big so some more extensive set of baselines could have been used. 
Overall I do not see the major contribution of this work to a general ML conference like iclr and this might be more suitable for a recommender systems conference,

### Strengths
Seems to have a good performance compared to the used baselines. 

Code availability

### Weaknesses
The paper introduces a cross domain recommendation methods based on denoising and calibrating the user preferences in the source and target domain. The experimental results seem promising but the paper is essentially unreadable with major issues in presentation. In particular the method is extremely difficult to understand, e.g. how are the calibration factors k_i computed from function 14 useful in determining the true preferences of the user, no intuition is provided. Moreover the paper mainly deals with matrix factorization type methods and there is not much discussion about more modern deep learning type methods and how it relates to those. Moreover the literature on cross-domain recommendation is quite big so some more extensive set of baselines could have been used. 
Overall I do not see the major contribution of this work to a general ML conference like iclr and this might be more suitable for a recommender systems conference,

  1 poor

  1 poor

  1 poor

Seems to have a good performance compared to the used baselines. 

Code availability

The paper is difficult to follow and does not provide good intuition on why the design choices where made. 

Compared to the literature on the topic the authors use a very limited set of baselines. 

The topic is a rather niche topic in the area of recommender systems and might not be interesting to the wider audience at iclr.

### Questions
Could the authors provide more intuition on the design choices of the algorithm. 
I also find papers with too many abbreviations very hard to follow. 
Simplify the presentation of the paper.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces Neural Adaptive Recommendation Feedback (NARF), a novel approach designed to enhance Cross-Domain Recommendation with Implicit Feedback (CDRIF). NARF comprises two main components: Implicit Feedback Calibration (IFC) and Dynamic Noise Reduction (DNR), aiming to address the challenges posed by the binary nature and noise in implicit feedback. The authors conduct extensive experiments on both synthetic and real-world datasets, demonstrating that NARF significantly outperforms baseline methods. The paper is well-structured, providing clear explanations of the methodology and a comprehensive evaluation of the proposed approach.

### Strengths
1.	The introduction of NARF as a method to handle implicit feedback in CDR is innovative. The two-step approach of IFC and DNR is well thought out and addresses the challenges of implicit feedback effectively.
2.	The paper includes a comprehensive set of experiments on both synthetic and real-world datasets, providing a thorough evaluation of the proposed method. The results show that NARF significantly outperforms baseline methods.
4.	The paper provides a clear and detailed description of the NARF approach, including the mathematical formulations and the rationale behind each component.

### Weaknesses
1.  It is important to balance denoising and preservation of unique user vehaviors : This weakness pertains to the treatment of implicit feedback in the denoising strategy and the Dynamic Noise Reduction (DNR) process within the NARF framework. The concern is that these processes might overly standardize user behavior, potentially leading to the loss of unique and valuable user behavior patterns inherent in implicit feedback. 

 n the NARF framework, implicit feedback is subjected to a denoising strategy to mitigate the impact of noisy interactions. Implicit feedback, by nature, is derived from user actions such as clicks, views, or purchases, and it encapsulates a wide array of user behavior patterns. These patterns are crucial as they provide unique insights into user preferences and behavior. However, the denoising strategy, as described in the paper, might not sufficiently differentiate between noise and genuine user behavior patterns that are less common or more nuanced. This is particularly evident in the sections of the paper where the authors discuss the implementation of the DNR process.

The DNR process aims to dynamically reduce noise by focusing on reliable user-item interactions. However, the criteria for determining reliability are primarily based on loss values computed during training. This approach raises the concern that unique user behavior patterns, which might initially result in higher loss values due to their rarity or complexity, could be mistakenly treated as noise and filtered out. This is especially problematic if these unique patterns are crucial for understanding specific user preferences or behavior in niche domains.

Furthermore, the paper does not provide a detailed discussion on how the NARF framework, and specifically the DNR process, handles the trade-off between denoising and preserving the richness of implicit feedback. The lack of this discussion leaves readers questioning whether the framework can adequately capture the diversity of user behavior inherent in implicit feedback, particularly in scenarios with diverse and biased datasets.

In summary, while the NARF framework aims to improve recommendation performance through denoising strategies, there is a need for a more explicit discussion and concrete examples in the paper to address concerns regarding the potential loss of inherent user behavior patterns in the implicit preferences. This is crucial for ensuring that the benefits of denoising do not come at the expense of overlooking valuable insights that implicit feedback can provide.

2. The cross-domain datasets used in the experiments are all sourced from Amazon, covering domains like movies, music, and books. These domains are relatively similar, and the use of more diverse and biased datasets could provide a more comprehensive evaluation of the proposed method.

3. It is imperative to maintain a consistent use of terminology when expressing the substitution of DNR with CTD in the ablation study, ensuring clarity and precision in communication. For instance, in Table 4, the term 'CTD' is utilized, whereas in the main model description sections, such as in Figure 3, the term 'DNR' is employed. This discrepancy necessitates attention to ensure consistency and avoid potential confusion for readers.

### Questions
•	How does the NARF framework ensure the preservation of unique user behavior patterns during the denoising process of implicit feedback? Are there specific mechanisms or safeguards in place to prevent the loss of these valuable insights?

•	"In the context of denoising implicit feedback, how does NARF balance the need for standardizing user behavior with the necessity to retain the inherent uniqueness of user interactions? Could you provide examples or scenarios where this balance is particularly crucial?

•	Could you elaborate on the strategies employed within the DNR process to avoid over-denoising? How does the system determine the optimal level of noise reduction to ensure that significant user behavior patterns are not inadvertently filtered out?

•	How might the performance of NARF vary when applied to more diverse and biased cross-domain datasets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
