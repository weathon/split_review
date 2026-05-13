# Uncertainty-aware Guided Diffusion for Missing Data in Sequential Recommendation

- Decision: Reject
- Scores: 6, 5, 10, 5

## Abstract
Denoising diffusion models (DDMs) have shown significant potential in generating oracle items that best match user preference with guidance from user historical interaction sequences. However, the quality of guidance is often compromised by the unpredictable missing data in the observed sequence, leading to suboptimal item generation. To tackle this challenge, we propose a novel uncertainty-aware guided diffusion model (DreamMiss) to alleviate the influence of missing data. The core of DreamMiss is the utilization of a dual-side Thompson sampling (DTS) strategy, which simulates the stochastical mechanism of missing data without disrupting preference evolution. Specifically, we first define dual-side probability models to capture user preference evolution, taking into account both local item continuity and global sequence stability. We then strategically remove items based on these two models with DTS, creating uncertainty-aware guidance for DDMs to generate oracle items. This can achieve DDMs’ consistency regularization, enabling them to resile against uncertain missing data. Additionally, to accelerate sampling in the reverse process, DreamMiss is implemented under the framework of denoising diffusion implicit models (DDIM). Extensive experimental results show that DreamMiss significantly outperforms baselines in sequential recommendation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The proposed method aims to tackle overlooking the missing data within the guidance for diffusion models. Specifically, they first detect the missing data by constructing local and global models and checking the continuity and stability. Based on the detected missing data, the authors then train diffusion models with uncertainty-aware guidance. Extensive results are provided to support the effectiveness.

### Strengths
- This paper is well-structured and easy to follow.
- The proposed method is well-motivated and novel. 
- The details of the experiments are revealed, and the code is released, which will ease the reproducibility of this paper.

### Weaknesses
- Some typos exist. For example, the first character in line 72 should be capitalized.
- This paper is not well-motivated. Why is Thompson sampling the best choice to derive the guide signal for a diffusion-based recommendation? Besides, no related experiments can verify the best of the Thompson sampling strategy compared to other sampling strategies.
- I noticed that the scale of datasets used in the experiments is relatively small, with interaction counts of fewer than one million. I recommend that the authors conduct experiments on larger datasets to further demonstrate the effectiveness of the proposed method, or the method's efficiency may be questioned.

### Questions
All my questions have been included in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes DreamMiss, a novel approach to handle missing data in sequential recommendation systems using denoising diffusion models (DDMs). The key innovation is a dual-side Thompson sampling (DTS) strategy that simulates missing data stochastically while preserving user preference patterns. The approach uses two probability models: 1) A local model that captures continuity between adjacent items A global model that evaluates sequence stability. 2) DreamMiss is implemented using denoising diffusion implicit models (DDIM) for faster sampling and achieves consistency regularization through uncertainty-aware guidance.

### Strengths
The paper is generally well-written.
The problem of missing data is crucial for developing sequential recommenders.

### Weaknesses
W1. Conceptual Clarity and Methodology Concerns.
The paper lacks clear theoretical justification for how generating additional missing data helps address the original missing data problem.
The approach of simulating missing data from already incomplete sequences raises questions about potential error propagation.
The methodology appears counterintuitive compared to traditional approaches that aim to recover or compensate for missing data.
The paper would benefit from a more rigorous theoretical analysis of why this approach is superior to data completion methods.

W2. Limited Validation of Dual-side Thompson Sampling (DTS).
The paper does not sufficiently justify why DTS is specifically effective for diffusion-based sequential recommenders.
There is inadequate theoretical analysis or empirical validation of the reliability of the continuity and stability metrics.
The generalizability of DTS to other recommendation architectures needs more thorough investigation.
The robustness of the probability models used in DTS requires more comprehensive validation.

W3. Incomplete Baseline Comparisons.
Notable omissions of important state-of-the-art baselines, particularly:
[1] Lin, Y.; Wang, C.; Chen, Z.; Ren, Z.; Xin, X.; Yan, Q.; de Rijke, M.; Cheng, X.; and Ren, P. A Self-Correcting Sequential Recommender. In TheWebConf 2023.
[2] Zhang, C.; Han, Q.; Chen, R.; Zhao, X.; Tang, P.; and Song, H. SSDRec: Self-Augmented Sequence Denoising
for Sequential Recommendation. In ICDE 2024.
These omissions make it difficult to fully assess the comparative advantages of the proposed method.
The evaluation would be more convincing with a more comprehensive comparison against recent approaches.

W4. Scalability Limitations.
The computational complexity of the proposed method may limit its practical applications.
Insufficient discussion of performance on large-scale recommendation systems.
Limited analysis of computational resource requirements for real-world deployment.
Need for more detailed discussion of potential optimization strategies for larger datasets.

W5. Dataset Limitations.
The evaluation relies on relatively small-scale datasets.
Questions about generalizability to larger, more complex real-world recommendation scenarios.
Need for validation on more diverse and larger-scale datasets.
Limited demonstration of effectiveness across different domains and data distributions.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
1

### Summary
Sorry, I am not familiar with this research area so I can't give a valuable score. Please overlook my score.

### Strengths
Sorry, I am not familiar with this research area so I can't give a valuable score. Please overlook my score.

### Weaknesses
Sorry, I am not familiar with this research area so I can't give a valuable score. Please overlook my score.

### Questions
Sorry, I am not familiar with this research area so I can't give a valuable score. Please overlook my score.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a dual-side Thompson sampling (DTS) strategy to simulate the stochastical mechanism of missing data, and integrates it into denoising diffusion models for sequential recommendation. Extensive experimental results show that DreamMiss significantly outperforms baselines.

### Strengths
1. The experimental results are sound.
2. The paper is overall well written.

### Weaknesses
1. The missing data issue is not well discussed. Thompson sampling can not tackle all the missing data issues. How the proposed model can address which kind of missing data should be discussed in the paper.
2. The rationale of accelerated sampling is not well explained.
2. The hypothesis of stability scores is not reasonable. In recommendation model training, data are often shuffled to remove the dependency among samples. However, the stability scores seems the opposite way; it used the batch information for sampling. It contradicts with the traditional way.

### Questions
1. The line 7 of Algorithm 1 seems a bit different than other DDPM models. There's no square root above the $(1 - \alpha_{\tau_s})$. Is it a typo?
2. Can the authors explain why accelerated sampling works? It seems to reduce thousands of iterations to less than 100 rounds, which is a huge improvement.
3. Based on the performance of Dreasmiss, can we say the DreamRec has a overfitting problem? With much more rounds of iteration DreamRec has inferior performance.

### Soundness
3

### Presentation
3

### Contribution
2
